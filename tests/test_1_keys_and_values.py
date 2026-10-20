import re
from utils import get_all_language_sources, get_language_file_list, get_all_language_modules

KEY_VALUE_RE = re.compile(r'("([^"]*)"|\'([^\']*)\')\s*\:\s*("([^"]*)"|\'([^\']*)\')\s*,?')

def test_repeated_entry():
    """
    Tests if an entry is defined more than once (keys and values)
    Based on the source code and not in the defined dictionaries
    """
    src_list = get_all_language_sources()
    language_file_list = get_language_file_list() # Just for reporting error
    error_list = []
    for i, src in enumerate(src_list):
        key_value_list = KEY_VALUE_RE.findall(src)
        key_list, value_list = [], []
        for tup in key_value_list:
            key, _, _, value, _, _ = tup
            key = key.strip('"').strip("'")
            value = value.strip('"').strip("'")
            key_list.append(key)
            value_list.append(value)

        key_set = set(key_list)
        if len(key_list) != len(key_set):
            for key in key_list:
                if key_list.count(key) != 1:
                    error_list.append(f"{language_file_list[i]}: {key}")
        # Just in case:
        if len(key_list) != len(key_set):
            error_list.append(f"{language_file_list[i]}")

        value_set = set(value_list)
        if len(value_list) != len(value_set):
            for value in value_list:
                if value_list.count(value) != 1:
                    error_list.append(f"{language_file_list[i]}: {value}")
        # Just in case:
        if len(value_list) != len(value_set):
            error_list.append(f"{language_file_list[i]}")

    if len(error_list) > 0:
        raise AssertionError("\n".join(error_list))
        
            
def test_dunder_methods():
    """Tests that dunder methods start and end with "__". """
    module_list = get_all_language_modules()
    error_list = []
    for module in module_list:
         for dic in [
            module.dictionary,
        ]:
            for key, value in dic.items():
                if value.startswith("_") or value.endswith("_"):
                    if not key.startswith("__") \
                    or not key.endswith("__") \
                    or not value.startswith("__") \
                    or not value.endswith("__") :
                        error_list.append(f"{module.__name__}: {key}: {value}")

    if len(error_list) > 0:
        raise AssertionError("\n".join(error_list))

def test_spaces_in_dicts():
    """
    May become deprecated in the future if we decide
    to allow this for backwards compatibility
    """
    module_list = get_all_language_modules()
    error_list = []
    for module in module_list:
         for dic in [
            module.dictionary,
        ]:
            for key, value in dic.items():
                if " " in key: error_list.append(f"{module.__name__}: {key}")
                if " " in value: error_list.append(f"{module.__name__}: {value}")

    if len(error_list) > 0:
        raise AssertionError("\n".join(error_list))
    
def test_duplicate_values():
    """
    Tests for duplicate values.
    May become deprecated in the future if we decide
    to allow this for backwards compatibility
    """
    module_list = get_all_language_modules()
    error_list = []
    for module in module_list:
         for dic in [
            module.dictionary,
            module.traceback_dictionary,
            module.pylyglot_internal_messages
        ]:
            value_list = list(dic.values())
            value_set  = set(value_list)
            if len(value_list) != len(value_set):
                for value in value_list:
                    if value_list.count(value) != 1: # This will print the key
                        error_list.append(f"{module.__name__}: {value}")
    
    if len(error_list) > 0:
        raise AssertionError("\n".join(error_list))
