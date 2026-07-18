# English: KEEP AS DEFAULT!
dictionary = dict()
exception_dictionary = dict()
traceback_dictionary = dict()

# PYLYGLOT INTERNAL MESSAGES
pylyglot_internal_messages = {
    # __main__.py:
    "main_arg_length_error": 
        "Pylyglot must receive at least 1 options: the path to the file.",
    "main_file_specified_twice": 
        "File path specified twice? {filepath}, {arg}.",
    "main_couldnt_interpret_argument": 
        "Couldn't interpret argument: {arg}. Make sure you have provided the right paths.",
    "main_couldnt_find_filepath": 
        "Could not identify filepath in command line arguments.",
    "main_console_and_translate": 
        'Pylyglot received both "console" and "translate" options at the same time (only one allowed).',
    "main_translate_destination": 
        "--translate requires a destination: python -m pylyglot --translate=output_language source_path destination_path", 
    "main_no_output_language_verbose": 
        'No translation language was specified for the translate option. Language identified by the destination file extension: {lang}.',
    "main_defaulting_to_default_language": 
        'No translation language was specified for the translate option, translating to default language: {default_language}.'
        '\nYou can change the default language by running "python -m pylyglot --setconfig default_langauge=language_code".',
    "main_file_and_destination_type_mismatch":
        "Specified filepath for translation ({filepath}) is a directory, but destination isn't ({destination}).",
    "main_console_language":
        'Pylyglot warning: No console language specified, using default langauge: {default_language}.'
        '\nYou can change the default language by running "python -m pylyglot --setconfig default_langauge=language_code".',
    
    # config.py:
    "config_key_error":
        '"{key}" not in pylyglot config file.'
        '\nTo see options, run "python -m pylyglot --getconfig"'
        '\nTo get the path to the config.json, run "python -m pylyglot --getconfigpath"',
    "config_set_success":
        'Successfully updated config option "{key}" from "{old_value}" to "{value}".',
    "config_reset_success":
        "Config was reset to defaults.",
    
    # translator.py:
    "translator_version_warning": 
        "Pylyglot file {path} generated with version {version}, but you are using {current_version} for translation! Translation could be inconsistent.",
    "translator_language_id_fail":
        "Could not identify language of the following file: {path}",
    "translator_syntaxerror":
        "Pylyglot warning: SyntaxErrors may come from the use of python keywords in code.\n",
}
