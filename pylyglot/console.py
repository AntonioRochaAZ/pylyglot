import sys, code, traceback
from importlib.metadata import version as get_version
from .translator import translate_source, get_language_module, translate_traceback_line, make_excepthook


class PylyglotConsole(code.InteractiveConsole):
    def __init__(self, language: str, **kwargs):
        super().__init__(**kwargs)
        self.language = language
        self.module = get_language_module(language)
        self.dictionary = self.module.dictionary
        sys.excepthook = make_excepthook(self.module.traceback_dictionary)

    def runsource(self, source, filename="<input>", symbol="single"):
        translated = translate_source(source, self.dictionary)
        return super().runsource(translated, filename, symbol)


def launch_console(language: str):
    # I don't like this feature but I am leaving this as a comment because 
    # I like that it exists 
    # try:
    #     import readline
    #     readline.parse_and_bind("tab: complete")
    # except ImportError:
    #     pass

    console = PylyglotConsole(language, locals={})
    banner = (
        f"Pylyglot {get_version("pylyglot")} {language} interpreter\n"
        f"Python {sys.version}"
    )
    console.interact(banner=banner)#, exitmsg=f"Saindo do Pylyglot {language}.")