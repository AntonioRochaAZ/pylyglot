import tokenize, io, os, importlib, re, sys, traceback
from typing import Union
from importlib.metadata import version as get_version, PackageNotFoundError 
from warnings import warn

def get_dictionary(language: str, throw_exception: bool = True, with_traceback: bool = False) -> Union[str, None]:
    """Fetches the dictionary of the selected language.

    Args:
        language: The name of the langauge.
        throw_exception: Whether to throw an exception if the dictionary is not found. If ``False``, ``None`` is returned.

    """
    try:
        module = importlib.import_module(f"pylyglot.languages.{language}")
        if not with_traceback:
            return module.dictionary
        else:
            dictionary = module.dictionary.copy()
            tb_dictionary = module.traceback_dictionary.copy()
            return dictionary | tb_dictionary

    except Exception as e:
        if throw_exception:
            raise e
        else:
            return None

EXTENSION_RE = re.compile(r"\.(.*)\.py$")
LANGUAGE_RE = re.compile(r"^\s*#\s*pylyglot:\s*([^#]*)#(?:\s*version:\s*([^#]*)#)?")
KEEP_LINE_RE = re.compile(r"#\s*pylyglot:\s*keep\s*$")

def detect_language(path: str, encoding: str="utf-8", errors="strict") -> Union[str, None]:
    """Detects the language of a file.
    This first checks for a comment in the first line of the file with the format "# pylyglot: language_name #".
    If it is not found, then it checks for the file extension (.language_name.py).

    Args:
        path: Path to the file. 
        encoding: Encoding used to read the source file before translation. Defaults to "utf-8".
        errors: Kwarg of bytes.decode(). Defaults to "strict"
    
    Returns:
        The name of the language or None, if not identified (which is the case if it is a regular python file).
    """
    with open(path, "rb") as f:
        source_bytes = f.read()
    source = source_bytes.decode(encoding, errors)

    # Check for the # pylyglot: lang_name # comment
    for line in source.splitlines()[:2]:
        match = LANGUAGE_RE.match(line.strip())
        if match:
            lang = match.group(1).strip()
            if lang.lower() == "none": lang = None
            version = match.group(2).strip() if match.group(2) else None
            if version is not None:
                try:
                    current_version = get_version("pylyglot")
                    if current_version != version:
                        warn(f"Pylyglot file {path} generated with version {version}, but you are using {current_version} for translation! Translation could be inconsistent.")
                except PackageNotFoundError:
                    pass
            return lang
    
    # If we got here, then we need to check for the extension:
    filename = os.path.basename(path)
    match = EXTENSION_RE.search(filename)
    if match:
        lang = match.group(1)
        return lang
    
    # Assume default python file:
    return None

def identify_renames(source: str, dictionary: dict) -> dict:
    """
    Returns a rename map {original_name: safe_name} for any user-defined
    name that collides with a value of the dictionary 
    (i.e. a keyword in the output language).
    """
    # collect all names actually used in the source
    tokens = list(tokenize.generate_tokens(io.StringIO(source).readline))
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

def translate_source(source: str, dictionary: dict, keep_lines: list[int] = None, debug: bool = False) -> str:

    if keep_lines is None: keep_lines = list()

    tokens = tokenize.generate_tokens(io.StringIO(source).readline)
    if debug: print(list(tokens))
    result = []
    for tok_type, tok_string, tok_start, tok_end, tok_line in tokens:
        if tok_type == tokenize.NAME \
        and tok_string in dictionary \
        and tok_start[0] not in keep_lines:
            tok_string = dictionary[tok_string]
        result.append((tok_type, tok_string, tok_start, tok_end, tok_line))
    
    return tokenize.untokenize(result)


def translate_file(path: str, input_language: str, output_language: str = None, encoding: str = "utf-8", errors="strict") -> str:
    """Translates a file from one language to another.

    Args:
        path: Path to the file to be translated.
        input_language: Language of the file. If None is passed, it will be automati
        output_language: Language we want to translate to. None --> regular python.
        encoding: Encoding used to read the source file before translation. Defaults to "utf-8".
        errors: Kwarg of bytes.decode(). Defaults to "strict"

    Returns:
        str: The translated file as a string.
    """
    with open(path, "rb") as f:
        source_bytes = f.read()
    source = source_bytes.decode(encoding, errors)
    
    if input_language is None:
        input_language = detect_language(path, encoding, errors)
    if input_language is None:
        # Regular python file (assumed)
        if output_language is None:
            # already plain Python, nothing to translate
            return source  
        # Otherwise:
        dictionary = {v: k for k, v in get_dictionary(output_language).items()}
    else:
        # Input file not a regular python file, get dictionary: 
        dictionary = get_dictionary(input_language)
        if output_language is not None:
            # We want to output to a different language, not regular python.
            # update dictionary so that this works:
            in_dictionary = dictionary.copy() # Avoid changing the default dictionary idk
            inverse_out_dictionary = {v: k for k, v in get_dictionary(output_language).items()}
            dictionary = {
                key: inverse_out_dictionary.get(
                    in_dictionary[key], in_dictionary[key]
                ) # if default python name not in inverse_out_dictionary, then just use default python name.
                for key in in_dictionary
            }
    
    # Avoid translating a variable into a keyword:
    dictionary = dictionary | identify_renames(source, dictionary)

    # Check which lines must not be translated
    keep_lines = [
        i + 1  # tokenize uses 1-based line numbers
        for i, line in enumerate(source.splitlines())
        if KEEP_LINE_RE.search(line) is not None
    ]

    return translate_source(source, dictionary, keep_lines=keep_lines) 

FIXED_TRACEBACK_PHRASES = [
    "Traceback (most recent call last):",
    "During handling of the above exception, another exception occurred:",
    "The above exception was the direct cause of the following exception:",
]

def translate_traceback_line(line: str, traceback_dictionary: dict) -> str:
    # handle fixed multi-word phrases first
    for phrase in FIXED_TRACEBACK_PHRASES:
        if phrase in line and phrase in traceback_dictionary:
            line = line.replace(phrase, traceback_dictionary[phrase])
    # then tokenize-based replacement for exception names and identifiers
    try:
        return translate_source(line, traceback_dictionary)
    except Exception:
        return line

def make_excepthook(inv_dictionary: dict):
    def pylyglot_excepthook(type_, value, tb):
        lines = traceback.format_exception(type_, value, tb)
        for line in lines:
            print(translate_traceback_line(line, inv_dictionary),
                  end='', file=sys.stderr)
    return pylyglot_excepthook


def run_file(path: str, input_language: str, **translate_file_kwargs) -> None:
    """Runs a file written in non-standard python.
    
    Args:
        path: the path to the file.
        input_language: the name of the language the file is written in. 
            If None is passed, it will be automatically identified in :func:`~translator.translate_file`.
        **translate_file_kwargs: See kwargs of :func:`~translator.translate_file`.
    
    """
    if input_language is None:
        input_language = detect_language(path, **translate_file_kwargs)
    translated_file = translate_file(path, input_language, output_language=None, **translate_file_kwargs)
    full_dictionary = get_dictionary(input_language, with_traceback=True)
    sys.excepthook = make_excepthook({v: k for k, v in full_dictionary.items()})
    return exec(translated_file)
