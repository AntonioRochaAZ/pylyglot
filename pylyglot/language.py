import importlib
from typing import Callable

from .utils import (
    get_supported_language_codes, 
    get_known_programming_language_extensions_dict,
    get_supported_programming_languages,
)

from . import jsonc
from . import config

def get_prog_lang_info(extension: str):
    """
    Loading generic dictionaries about programming languages, 
    before knowing the human language the code is written in.
    This is particularly necessary for getting the comment symbol
    associated to the programming language.
    """
    with importlib.resources.path("pylyglot", "languages") as path:
        path = path/"programming_languages.jsonc"
        with open(path, "r", encoding=config.options["input_encoding"]) as f:
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
        self.prog_tokenizer = self.get_token_identifier_fn(programming_language)

        # Loading dictionaries:
        with importlib.resources.path("pylyglot", "languages") as path:
            path = path/language/f"{programming_language}.jsonc"
            import os
            print(path, os.path.exists(path))
            with open(path, "r", encoding=config.options["input_encoding"]) as f:
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

    @staticmethod
    def get_token_identifier_fn(programming_language: str) -> Callable:

        if programming_language == "python":
            import tokenize, io 
            def get_python_tokens(src: str):
                return tokenize.generate_tokens(io.StringIO(src).readline)
            return get_python_tokens
        elif programming_language == "fortran":
            try:
                import tokenize, re
                from fparser.common.readfortran import FortranStringReader
                from fparser.common.sourceinfo import FortranFormat


                # Fortran lexical patterns
                TOKEN_RE = re.compile(
                    r"""('[^']*(?:''[^']*)*'|"[^"]*(?:""[^"]*)*")"""  # Strings
                    r"""|([A-Za-z_]\w*)"""                              # Names
                    r"""|(\d+(?:\.\d*)?(?:[EeDd][+-]?\d+)?"""          # Numbers
                    r"""|\.\d+(?:[EeDd][+-]?\d+)?)"""
                    r"""|(::|=>|\*\*|//|<=|>=|/=|==|[+\-*/=<>(),;:%.\[\]])"""  # Operators
                )

                def generate_fortran_tokens(source: str, isfree: bool = True):
                    """Generate Python-tokenize-compatible tokens from Fortran source."""

                    reader = FortranStringReader(source, ignore_comments=False)
                    reader.set_format(FortranFormat(isfree, True))

                    line_num = 1

                    while True:
                        try:
                            item = reader.next()
                        except StopIteration:
                            break

                        line = item.line

                        if hasattr(item, "comment"):
                            line = item.comment
                            yield (tokenize.COMMENT, line, (line_num, 0),
                                (line_num, len(line)), line)
                        else:
                            for match in TOKEN_RE.finditer(line):
                                text = match.group()

                                if match.group(1):
                                    tok_type = tokenize.STRING
                                elif match.group(2):
                                    tok_type = tokenize.NAME
                                elif match.group(3):
                                    tok_type = tokenize.NUMBER
                                else:
                                    tok_type = tokenize.OP

                                start = (line_num, match.start())
                                end = (line_num, match.end())

                                yield (tok_type, text, start, end, line)

                            yield (tokenize.NEWLINE, "\n",
                                (line_num, len(line)),
                                (line_num, len(line) + 1), line)

                        line_num += 1
                
                return generate_fortran_tokens
            except ImportError as e:
                raise ImportError("Must install fparser package (pip install fparser) for translating FORTRAN code")
            