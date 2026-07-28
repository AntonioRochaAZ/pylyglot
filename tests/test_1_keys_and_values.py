import re
from utils import get_all_language_sources, get_all_language_modules

KEY_VALUE_RE = re.compile(r'("([^"]*)"|\'([^\']*)\')\s*\:\s*("([^"]*)"|\'([^\']*)\')\s*,?')

def test_repeated_entry():
    """
    Tests if an entry is defined more than once (keys and values)
    Based on the source code and not in the defined dictionaries
    """
    src_list = get_all_language_sources()
    for src in src_list:
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
                assert key_list.count(key) == 1 # This will print the key
        # Just in case:
        assert len(key_list) == len(key_set)

        value_set = set(value_list)
        if len(value_list) != len(value_set):
            for value in value_list:
                assert value_list.count(value) == 1 # This will print the key
        # Just in case:
        assert len(value_list) == len(value_set)
        
            
def test_dunder_methods():
    """Tests that dunder methods start and end with "__". """
    module_list = get_all_language_modules()
    for module in module_list:
         for dic in [
            module.dictionary,
        ]:
            for key, value in dic.items():
                if value.startswith("_") or value.endswith("_"):
                    assert key.startswith("__")
                    assert key.endswith("__")
                    assert value.startswith("__")
                    assert value.endswith("__")

def test_spaces_in_dicts():
    """
    May become deprecated in the future if we decide
    to allow this for backwards compatibility
    """
    module_list = get_all_language_modules()
    for module in module_list:
         for dic in [
            module.dictionary,
        ]:
            for key, value in dic.items():
                assert " " not in key
                assert " " not in value

def test_duplicate_values(verbose=False):
    """
    Tests for duplicate values.
    May become deprecated in the future if we decide
    to allow this for backwards compatibility
    """
    module_list = get_all_language_modules()
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
                    assert value_list.count(value) == 1 # This will print the key
