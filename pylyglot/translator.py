import tokenize, io, os, importlib, re, sys, traceback
from typing import Union, List, Tuple, Callable
from types import ModuleType
from importlib.metadata import version as get_version, PackageNotFoundError 
from warnings import warn
import runpy
from pathlib import Path

from . import config
from . import debug
from .language import LanguageClass, get_prog_lang_info

LANGUAGE_RE_FORMAT_STR  = r"^\s*{COMMENT_SYMBOL}\s*pylyglot:\s*([^#]*)#(?:\s*version:\s*([^#]*)#)?"
KEEP_LINE_RE_FORMAT_STR = r"{COMMENT_SYMBOL}\s*pylyglot:\s*keep\s*$"
SH_RE        = re.compile(r"^#!")

def get_language_class(language: str, programming_language: str, throw_exception: bool = True) -> Union[LanguageClass, None]:
    """Get the python module associated to a language

    Args:
        language: the language code. `Click here for the supported language codes <https://antoniorochaaz.github.io/pylyglot/languages.html>`_.

        throw_exception: whether to throw an exception if the module is not found. Defaults to True.

    Returns:
        The associated python module or None if it is not found and ``throw_exception`` is False
    """
    try:
        return LanguageClass(language, programming_language)
    except Exception as e:
        if throw_exception:
            raise e
        else:
            return None

def get_pylyglot_message(_language, _key, **_kwargs):
    lc = get_language_class(_language, "py")
    pim = lc.pylyglot_internal_messages
    if _key not in pim:
        # English fallback:
        lc = get_language_class("en", "py")
        pim = lc.pylyglot_internal_messages
    return pim[_key].format(**_kwargs)

def detect_language_from_extension(filename) -> Union[str, None]:
    extension = filename.split(".")[-1]
    match_lang = re.search(r"\.(.*)\."+extension+"$", filename)
    if match_lang:
        lang = match_lang.group(1)
        return lang
    return None

def detect_language(path: str, encoding: str="utf-8", errors="strict") -> Tuple[str, str]:
    """Detects the language of a file.

    This first checks for a comment in the first line of the file with the format "``# pylyglot: language_name #``"
    (if a #!/bin... line is the first line, we check for the second line).
    If it is not found, then it checks for the file extension (.language_name.py).

    `Click here for the supported file extensions and associated languages <https://antoniorochaaz.github.io/pylyglot/languages.html>`_.

    Args:
        path: Path to the file.
        encoding: Encoding used to read the source file before translation. Defaults to "utf-8".
        errors: Kwarg of bytes.decode(). Defaults to "strict"

    Raises:
        ValueError: if the file extension not end in .py.

    Returns:
        The name of the language or ``None``, if it is a regular python file OR if the language is not identified.
    """
    # Get programming language extension:
    filename = os.path.basename(path)
    prog_lang = filename.split(".")[-1]
    prog_lang_info = get_prog_lang_info(prog_lang)

    # Check for the # pylyglot: lang_name # comment
    with open(path, "rb") as f:
        source_bytes = f.read()
    source = source_bytes.decode(encoding, errors)

    sh_bool = False
    for line_idx, line in enumerate(source.splitlines()[:2]): # Loop through first 2 lines
        LANGUAGE_RE = LANGUAGE_RE_FORMAT_STR.format(COMMENT_SYMBOL=prog_lang_info["comment_symbol"])
        match_lang = re.match(LANGUAGE_RE, line.strip())
        match_sh   = SH_RE.match(line.strip())
        if match_lang:
            if not sh_bool and line_idx == 1:
                # We found the pylyglot comment AFTER a non "#!" line
                raise AssertionError(
                    'Pylyglot header found in the second line of the file, but first line is not a "#!" type line. ' \
                    'Pylyglot header must be the first line of the file (or the second only if a "#!" type line is the first).'
                )
            lang = match_lang.group(1).strip()
            version = match_lang.group(2).strip() if match_lang.group(2) else None
            if version is not None:
                try:
                    current_version = get_version("pylyglot")
                    if current_version != version:
                        # Change default_language to output_language (must store it in options!)
                        warn(get_pylyglot_message(config.options["default_language"], "translator_version_warning", path=path, version=version, current_version=current_version))
                except PackageNotFoundError:
                    pass
            return lang, prog_lang
        elif match_sh:
            sh_bool = True
            continue
    
    # If we got here, then we need to check for the extension:
    lang = detect_language_from_extension(filename)
    if lang is not None:
        return lang, prog_lang
    else:
        # In this case, we basically have something like
        # file.py (file.cpp or whatever), which is just a 
        # regular file written in the language.
        return "en", prog_lang
    
    # Just in case:
    raise RuntimeError(f"Could not detect language of file: {path}.\nEncoding and error strategy used: enconding: {encoding}, errors: {errors}.")

def identify_renames(source: str, dictionary: dict, tokenizer: Callable) -> dict:
    """
    Returns a rename map {original_name: safe_name} for any user-defined
    name that collides with a value of the dictionary (i.e. a keyword
    in the output language).  
    Renamings look like: ``f"{name}{number}_"``
    This function is called during the translation process in
    :func:`translator.translate_file`.

    Args:
        source: The source file (as a string).
        dictionary: The dictionary which will be used for translating the 
            source (so that name collisions can be identified).
    
    Returns:
        A dictionary associating the original name of the variable with the new one.
    """
    # collect all names actually used in the source
    tokens = list(tokenizer(source))
    print(tokens)
    all_names = {token for tok_type, token, *_ in tokens if tok_type == tokenize.NAME }

    dangerous_names = set()
    for k, v in dictionary.items():
        if k == v: # No issue in this case
            continue
        dangerous_names.add(v)
    
    renames = {}
    for name in dangerous_names:
        if name in all_names:
            # find a safe replacement that isn't already used
            i = 0
            candidate = f"{name}{i}_"
            while candidate in all_names:
                i+=1
                candidate = f"{name}{i}_"
            renames[name] = candidate
            all_names.add(candidate)  # mark as taken
    
    return renames

def translate_source(source: str, dictionary: dict, tokenizer: Callable, keep_lines: List[int] = None, debug: bool = False) -> str:
    """Does the actual translation from one language to another (including regular python).

    This function is not supposed to be used standalon, as the dictionary
    must be defined in advance according to the identified input language and the
    desired output language.

    Args:
        source: The source code to be translated (as a string).
        dictionary: The translation dictionary.
        keep_lines: Optionally, a list with the indexes of lines which 
            shouldn't be translated. This is necessary in some cases to avoid
            name collisions during some imports. `This is explained in this section of the documentation <https://antoniorochaaz.github.io/pylyglot/features.html#security-against-name-clashes-and-english-fallback>`_.
        
        debug: If true, prints the list of tokens generated by the tokenize.generate_tokens call.

    Returns:
        str: The translated source code as a string.
    """
    if keep_lines is None: keep_lines = list()

    tokens = tokenizer(source)
    if debug: print(list(tokens))
    result = []
    for tok_type, tok_string, tok_start, tok_end, tok_line in tokens:
        if tok_type == tokenize.NAME \
        and tok_string in dictionary \
        and tok_start[0] not in keep_lines:
            tok_string = dictionary[tok_string]
        result.append((tok_type, tok_string, tok_start, tok_end, tok_line))
    
    return tokenize.untokenize(result)


def translate_file(
    path: str, 
    output_language: str, 
    encoding: str = "utf-8", 
    errors: str ="strict",
    return_lc: bool = False
) -> str:
    """Translates a file from one language to another.

    Args:
        path: Path to the file to be translated.
        input_language: Language of the file. If None is passed, it will be automatically detected.
        output_language: Language we want to translate to. "en" --> regular python.
        encoding: Encoding used to read the source file before translation. Defaults to "utf-8".
        errors: Kwarg of bytes.decode(). Defaults to "strict"

    Returns:
        str: The translated source code as a string.
    """
    with open(path, "rb") as f:
        source_bytes = f.read()
    source = source_bytes.decode(encoding, errors)
    
    input_language, programming_language = detect_language(path, encoding, errors)
    print(input_language, programming_language)
    if input_language == "en":
        # Regular python file (assumed)
        if output_language == "en":
            # already plain Python/programming language, nothing to translate
            return source  
        # Otherwise:
        lc = get_language_class(
            output_language, programming_language)
        dictionary = {
            v: k for k, v in lc.dictionary.items()
        }
    else:
        # Input file not a regular python file, get dictionary: 
        lc = get_language_class(input_language, programming_language)
        dictionary = lc.dictionary
        if output_language != "en":
            # We want to output to a different language, not regular python.
            # update dictionary so that this works:
            in_dictionary = dictionary.copy() # Avoid changing the default dictionary idk
            inverse_out_dictionary = {v: k for k, v in lc.dictionary.items()}
            dictionary = {
                key: inverse_out_dictionary.get(
                    in_dictionary[key], in_dictionary[key]
                ) # if default python name not in inverse_out_dictionary, then just use default python name.
                for key in in_dictionary
            }
    
    # Avoid translating a variable into a keyword:
    rename_dict = identify_renames(source, dictionary, lc.prog_tokenizer)
    if len(rename_dict) != 0:
        if str(config.options["allow_renames"]).lower() == "true":
            # allow with warnings
            warn(get_pylyglot_message(config.options["default_language"], "translator_rename_dict", path=path, rename_keys=list(rename_dict.keys()))) 
        elif str(config.options["allow_renames"]).lower() == "no_warnings":
            pass # allow without warningss
        else:
            # do not allow
            raise RuntimeError(get_pylyglot_message(config.options["default_language"], "translator_rename_dict", path=path, rename_keys=list(rename_dict.keys())))
    dictionary = dictionary | rename_dict

    # Check which lines must not be translated
    KEEP_LINE_RE = re.compile(KEEP_LINE_RE_FORMAT_STR.format(COMMENT_SYMBOL=lc.prog_lang_info["comment_symbol"]))
    keep_lines = [
        i + 1  # tokenize line index starts at 1
        for i, line in enumerate(source.splitlines())
        if KEEP_LINE_RE.search(line) is not None
    ]

    output = translate_source(source, dictionary, lc.prog_tokenizer, keep_lines=keep_lines)
    if return_lc:
        output = (output, lc)
    return output

def translate_and_write(src_path: str, dst_path: str, output_language, **translate_file_options):
    """
    Translate file from one language to another, adding a line comment specifying its language 
    an pylyglot version at the beginning of it.
    """
    
    translated, lc = translate_file(
        src_path, 
        output_language=output_language, 
        encoding=translate_file_options["input_encoding"],
        errors=translate_file_options["encoding_errors"],
        return_lc = True
    )

    try:
        current_version = get_version("pylyglot")
    except PackageNotFoundError:
        current_version = "unknown"

    comment_symbol = lc.prog_lang_info["comment_symbol"]
    header = f"{comment_symbol} pylyglot: {output_language} # version: {current_version} #\n"
    lines = translated.splitlines(keepends=False)
    # Check for the #!/bin/sh-type line and keep it if it is the case.
    # Also check for the pylyglot header.
    line_idx = 0
    if lines[line_idx].startswith("#!"):  # TODO: think whether this could happen in other programming languages and how to deal with it.
        header = lines[line_idx] + header
        line_idx += 1
    LANGUAGE_RE = LANGUAGE_RE_FORMAT_STR.format(COMMENT_SYMBOL=lc.prog_lang_info["comment_symbol"])
    if re.match(LANGUAGE_RE, lines[line_idx].strip()):
        line_idx += 1 # Replace old header

    output = header + "\n".join(lines[line_idx:])

    # Make directory path if non-existant:
    os.makedirs(os.path.dirname(dst_path) or ".", exist_ok=True)
    # Write file:
    with open(dst_path, "w", encoding=translate_file_options["output_encoding"]) as f:
        f.write(output)
    print(f"Translated: {src_path} into {dst_path}.")


def translate_traceback_line(line: str, traceback_dictionary: dict) -> str:
    # handle fixed multi-word phrases first
    for phrase in traceback_dictionary.keys():
        if phrase in line and phrase in traceback_dictionary:
            line = line.replace(phrase, traceback_dictionary[phrase])
    return line

def make_excepthook(language: str):
    traceback_dictionary = get_language_class(language, programming_language="python").traceback_dictionary
    def pylyglot_excepthook(typ, value, tb):
        lines = traceback.format_exception(typ, value, tb)
        if typ is SyntaxError:
            lines.append(get_pylyglot_message(language, "translator_syntaxerror")) 
                
        for line in lines:
            print(translate_traceback_line(line, traceback_dictionary), end='', file=sys.stderr)
    return pylyglot_excepthook


def run_file(path: str) -> None:
    input_language, prog_lang = detect_language(path)
    if prog_lang != "py":
        # TODO: translate this message: 
        raise RuntimeError(f"Can only run python files (ending with .language_code.py). Extension: .{prog_lang}")
    if debug.VERBOSE_LEVEL >= 1:  print(f"> translator.run_file(): detected input language: {input_language}")

    # set excepthook for the main file
    sys.excepthook = make_excepthook(input_language)
    if debug.VERBOSE_LEVEL >= 1:  print(f"> translator.run_file(): sys.excepthook: {sys.excepthook}")
    
    # run through normal machinery - loader handles translation
    path = Path(path).resolve()
    parent = path.parent
    sys.path.insert(0, str(parent))
    module_name = str(path.name).split(".")[0]
    if debug.VERBOSE_LEVEL >= 1:  print(f"> translator.run_file(): Identified path: {path}")
    if debug.VERBOSE_LEVEL >= 1:  print(f"> translator.run_file(): Identified parent path: {parent}")
    if debug.VERBOSE_LEVEL >= 1:  print(f"> translator.run_file(): Identified module_name: {module_name}")
    if debug.VERBOSE_LEVEL >= 1:  print(f"> translator.run_file(): Running file...")
    runpy.run_module(module_name, run_name="__main__", alter_sys=True)