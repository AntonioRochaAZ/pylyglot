import os, importlib.resources
from typing import List
from types import ModuleType

from pylyglot.translator import get_language_module

def get_all_language_modules() -> List[ModuleType]:
    with importlib.resources.path("pylyglot", "languages") as path:
        language_list = os.listdir(str(path))

    language_list.remove("__pycache__")
    language_list.remove("__init__.py")

    module_list = [get_language_module(lang.removesuffix(".py")) for lang in language_list]
    return module_list

def verify_language_verbose(language_code: str, verbose: bool = False) -> bool:
    ret_val = True

    module      = get_language_module(language_code)

    for dic in [
        module.dictionary,
        module.traceback_dictionary,
        module.pylyglot_internal_messages
    ]:
        key_list = list(dic.keys())
        value_list = list(dic.values())
        if len(key_list) != len(set(key_list)):
            repeated_keys = [key for key in key_list if key_list.count(key) != 1]
            ret_val = False
            if verbose:
                print(f"Language: {language_code}: REPEATED KEYS: {repeated_keys}")
            else:
                return False

        # The following may be allowed in the future for backwards compatibility
        if len(value_list) != len(set(value_list)):
            repeated_values = [value for value in value_list if value_list.count(value) != 1]
            ret_val = False
            if verbose:
                print(f"Language: {language_code}: REPEATED VALUES: {repeated_values}")
            else:
                return False
    

    if verbose:
        print(f"Language: {language_code}: ALL OK!")
    return ret_val