import tokenize, io, os, importlib, re

def get_dictionary(language: str, throw_exception: bool = True):
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

def detect_language(path: str, source: str):
    filename = os.path.basename(path)
    match = extension_re.search(filename)
    if match:
        return match.group(1) 
    
    # If we got here, then the extension doesn't give us a lot of information
    for line in source.splitlines()[:2]:
        match = pylyglot_re.match(line.strip())
        if match:
            return match.group(1).strip()
    return None

def translate_file(path: str, language: str, encoding: str = "utf-8", errors="strict") -> str:
    # Loading file in bytes:
    with open(path, "rb") as f:
        source_bytes = f.read()
    # Decoding with proper encoding:
    source = source_bytes.decode(encoding, errors)
    
    # Identifying language if necessary:
    if language is None:
        language = detect_language(path, source)
    if language is None:
        raise ValueError('')

    # Loading language dictionary:
    dictionary = get_dictionary(language)
    if dictionary is None: return None # TODO is this ok?
    
    # Actual translation:
    tokens = tokenize.generate_tokens(io.StringIO(source).readline)
    result = []
    for tok_type, tok_string, *rest in tokens:
        if tok_type == tokenize.NAME and tok_string in dictionary:
            tok_string = dictionary[tok_string]
        result.append((tok_type, tok_string))
    return tokenize.untokenize(result)

def run_file(path: str, language: str, **kwargs):
    translated_file = translate_file(path, language, **kwargs)
    # TODO: what if the file imports from other files...
    return exec(translated_file)
