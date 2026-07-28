import os, importlib.resources
from typing import List
from types import ModuleType
from pathlib import Path

from pylyglot.translator import get_language_module

def get_languages_folder() -> Path:
    with importlib.resources.path("pylyglot", "languages") as path:
        languages_folder = Path(path).resolve()
    return languages_folder

def get_all_language_modules() -> List[ModuleType]:
    languages_folder = get_languages_folder()
    language_list = os.listdir(languages_folder)
    entries_to_ignore = [file for file in language_list if file.startswith("__") or file.endswith("__")]
    for entry in entries_to_ignore:
        language_list.remove(entry)

    module_list = [get_language_module(lang.removesuffix(".py")) for lang in language_list]
    return module_list

def get_all_language_sources() -> List[str]:
    languages_folder = get_languages_folder()
    language_list = os.listdir(languages_folder)
    entries_to_ignore = [file for file in language_list if file.startswith("__") or file.endswith("__")]
    for entry in entries_to_ignore:
        language_list.remove(entry)
    src_list = []
    for language in language_list:
        with open(languages_folder/language, "r") as f:
            src = f.read()
            src_list.append(src)
    return src_list