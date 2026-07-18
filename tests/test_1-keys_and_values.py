from utils import get_all_language_modules

def test_keys():
    """
    This obviously does not work (python overwrites repeated entries).
    Using JSON files and trying to read them does not work either...
    TODO: Although with a JSON file I could parse it with re: 
    re.findall(r'".*"\:\s*".*"\s*,?', txt)
    """
    module_list = get_all_language_modules()
    for module in module_list:
         for dic in [
            module.dictionary,
            module.traceback_dictionary,
            module.pylyglot_internal_messages
        ]:
            key_list = list(dic.keys())
            assert len(key_list) == len(set(key_list))

def test_values():
    """
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
            assert len(value_list) == len(set(value_list))
