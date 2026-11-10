import os
import importlib.resources
from typing import List

from . import jsonc

def get_known_programming_language_extensions_dict() -> dict[str, str]:
    """Gets all supported programming language extensions"""
    with importlib.resources.path("pylyglot", "languages", "programming_languages.jsonc") as path:
        print(path, os.path.exists(path))
        with open(path, "r") as f:
            json_file = jsonc.load(f)
    return json_file["extensions"]

def get_supported_language_codes() -> List[str]:
    """Gets all supported language codes"""
    with importlib.resources.path("pylyglot", "languages") as path:
        language_list = os.listdir(str(path))
        language_list = [f for f in language_list if os.path.isdir(os.path.join(path, f)) and not f.startswith("__")]
    return language_list

def get_supported_programming_languages(language: str) -> List[str]:
    """Gets all supported programming languages for a specified language"""
    with importlib.resources.path("pylyglot", "languages", language) as path:
        programming_language_list = os.listdir(str(path))
        programming_language_list = [f.split(".")[0] for f in programming_language_list if f.endswith('.jsonc') and not f.startswith("__")]
    return programming_language_list

def get_python_source_suffixes() -> List[str]:
    """Gets all source suffixes (``.language_code.py``)"""
    language_codes = get_supported_language_codes()

    suffix_list = [f".{language}.py" for language in language_codes]
    suffix_list.insert(0, ".py") # Regular python
    PYLYGLOT_SOURCE_SUFFIXES = set(suffix_list) # Just in case
    
    return PYLYGLOT_SOURCE_SUFFIXES

def get_programming_languages_source_suffixes() -> List[str]:
    """Gets all source suffixes (``.language_code`` + ``.programming_language_extension``)"""
    language_codes = get_supported_language_codes()
    prog_lang_exts = list(get_known_programming_language_extensions_dict().keys())

    suffix_list = [
        f".{language}.{ext}" 
        for language in language_codes
        for ext in prog_lang_exts
    ]
    for ext in prog_lang_exts:
        suffix_list.insert(0, f".{ext}") # Regular python etc.
    PYLYGLOT_SOURCE_SUFFIXES = set(suffix_list) # Just in case
    
    return PYLYGLOT_SOURCE_SUFFIXES