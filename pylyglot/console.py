import sys, code, traceback
from importlib.metadata import version as get_version
from .translator import translate_source, get_language_module, translate_traceback_line, make_excepthook


class PylyglotConsole(code.InteractiveConsole):
    def __init__(self, language: str, **kwargs):
        super().__init__(**kwargs)
        self.language = language
        self.dictionary = get_language_module(language).dictionary
        sys.excepthook = make_excepthook(language)

    def runsource(self, source, filename="<input>", symbol="single"):
        translated = translate_source(source, self.dictionary)
        return super().runsource(translated, filename, symbol)


def launch_console(language: str):
    console = PylyglotConsole(language, locals={})
    banner = (
        f"Pylyglot {get_version("pylyglot")} {language} interpreter\n"
        f"Python {sys.version}"
    )
    console.interact(banner=banner)#, exitmsg=f"Saindo do Pylyglot {language}.")