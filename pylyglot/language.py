import importlib
from .utils import (
    get_supported_language_codes, 
    get_known_programming_language_extensions_dict,
    get_supported_programming_languages,
)

from . import jsonc

def get_prog_lang_info(extension: str):
    """
    Loading generic dictionaries about programming languages, 
    before knowing the human language the code is written in.
    This is particularly necessary for getting the comment symbol
    associated to the programming language.
    """
    with importlib.resources.path("pylyglot", "languages", "programming_languages.jsonc") as path:
        with open(path, "r") as f:
            json_file = jsonc.load(f)

    info = {
        key: json_file[key][extension]
        for key in json_file.keys()
    }
    return info

class LanguageClass:
    def __init__(self, language: str, programming_language_extension: str = "py"):
        # Checking if language is supported:
        supported_languages = get_supported_language_codes()
        if language not in supported_languages:
            # TODO: Translate this internal message to supported languages.
            raise ValueError(
                f"The specified language code ({language}) is not supported.\n"
                f"Supported language codes: {','.join(supported_languages)}"
            )
        self.language = language

        # Checking if programming language is supported for this language:
        # Get programming language name from extension:
        known_extensions = get_known_programming_language_extensions_dict()
        programming_language = known_extensions[programming_language_extension]
        # Check if the .jsonc file exists for the human language:
        supported_programming_languages = get_supported_programming_languages(language)
        if programming_language not in supported_programming_languages:
            # TODO: Translate this internal message to supported languages.
            raise ValueError(
                f"The specified programming language ({programming_language}) " 
                f"is not supported for the specified language ({language}).\n"
                f"Supported programming languages for this language: {','.join(supported_languages)}"
            )
        self.programming_language_extension = programming_language_extension
        self.programming_language = programming_language
        self.prog_lang_info = get_prog_lang_info(programming_language_extension)

        # Loading dictionaries:
        with importlib.resources.path("pylyglot", "languages", language, f"{programming_language}.jsonc") as path:
            import os
            print(path, os.path.exists(path))
            with open(path, "r") as f:
                json_file = jsonc.load(f, debug=True)
        # Setting class' attributes:
        for key, value in json_file.items():
            setattr(self, key, value)

        if programming_language == "python":
            # In this case, pylyglot has more features than just translation,
            # let's handle it:
            self.dictionary = self.dictionary.update(self.exception_dictionary)
            self.traceback_dictionary.update({v: k for k, v in self.exception_dictionary.items()})

    def __getattr__(self, attr: str):
        if attr in [
            "dictionary", 
            "exception_dictionary", 
            "traceback_dictionary",
            "pylyglot_internal_messages"
        ]:
            # If not defined, set to empty dictionary and return:
            setattr(self, attr, {})
            return getattr(self, attr)