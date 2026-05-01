import tokenize, io, os, importlib, re
from typing import Union

def get_dictionary(language: str, throw_exception: bool = True) -> Union[str, None]:
    """Fetches the dictionary of the selected language.

    Args:
        language: The name of the langauge.
        throw_exception: Whether to throw an exception if the dictionary is not found. If ``False``, ``None`` is returned.

    """
    try:
        module = importlib.import_module(f"pylyglot.languages.{language}")
        return module.dictionary
    except Exception as e:
        if throw_exception:
            raise e
        else:
            return None

extension_re = re.compile(r"\.(.*)\.py$")
pylyglot_re = re.compile(r"^\s*#\s*pylyglot:\s*(.*)#")

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
        match = pylyglot_re.match(line.strip())
        if match:
            return match.group(1).strip()
    
    # If we got here, then we need to check for the extension:
    filename = os.path.basename(path)
    match = extension_re.search(filename)
    if match:
        return match.group(1) 
    
    # Assume default python file:
    return None
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
    
    tokens = tokenize.generate_tokens(io.StringIO(source).readline)
    result = []
    for tok_type, tok_string, tok_start, tok_end, tok_line in tokens:
        if tok_type == tokenize.NAME and tok_string in dictionary:
            tok_string = dictionary[tok_string]
        result.append((tok_type, tok_string, tok_start, tok_end, tok_line))
    
    translated_file = tokenize.untokenize(result)

    return translated_file 

def run_file(path: str, input_language: str, **translate_file_kwargs) -> None:
    """Runs a file written in non-standard python.
    
    Args:
        path: the path to the file.
        input_language: the name of the language the file is written in. 
            If None is passed, it will be automatically identified in :func:`~translator.translate_file`.
        **translate_file_kwargs: See kwargs of :func:`~translator.translate_file`.
    
    """
    translated_file = translate_file(path, input_language, output_language=None, **translate_file_kwargs)
    return exec(translated_file)
