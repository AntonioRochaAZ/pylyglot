import os
import importlib.resources
from typing import List

def get_supported_language_codes() -> List[str]:
    """Gets all supported language codes"""
    with importlib.resources.path("pylyglot", "languages") as path:
        language_list = os.listdir(str(path))
    language_list = [f.split(".")[0] for f in language_list if f.endswith('.py') and not f.startswith("__")]
    return language_list

def get_source_suffixes() -> List[str]:
    """Gets all source suffixes (``.language_code.py`` + ``.py``)"""
    language_codes = get_supported_language_codes()

    suffix_list = [f"{language}.py" for language in language_codes]
    suffix_list.insert(0, ".py") # Regular python
    PYLYGLOT_SOURCE_SUFFIXES = set(suffix_list) # Just in case
    
    return PYLYGLOT_SOURCE_SUFFIXES