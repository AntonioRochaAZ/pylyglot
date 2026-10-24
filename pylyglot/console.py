import sys, code, traceback
from importlib.metadata import version as get_version
from .translator import translate_source, get_language_module, translate_traceback_line, make_excepthook

"""
# One could make a displayhook for translating some types when repr()
# in the console (for example). However, this could cause inconsistencies
# or different behaviours of python files according to the language,
# and potentially (more) confusion to students
import builtins
def displayhook(value):
    '''Based on pseudo-code from the sys.displayhook documentation'''
    if value is None:
        return
    # Set '_' to None to avoid recursion
    builtins._ = None
    text = repr(value)
    try:
        sys.stdout.write(text)
    except UnicodeEncodeError:
        bytes = text.encode(sys.stdout.encoding, 'backslashreplace')
        if hasattr(sys.stdout, 'buffer'):
            sys.stdout.buffer.write(bytes)
        else:
            text = bytes.decode(sys.stdout.encoding, 'strict')
            sys.stdout.write(text)
    sys.stdout.write("\n")
    builtins._ = value
"""

class PylyglotConsole(code.InteractiveConsole):
    """Implmenetation of Pylyglot console"""
    def __init__(self, language: str, **kwargs):
        """Stores language dictionary into attributes and makes excepthook."""
        super().__init__(**kwargs)
        self.language = language
        self.dictionary = get_language_module(language).dictionary
        sys.excepthook = make_excepthook(language)

    def runsource(self, source, filename="<input>", symbol="single"):
        """Translates source, then call's super().runsource()."""
        translated = translate_source(source, self.dictionary)
        return super().runsource(translated, filename, symbol)


def launch_console(language: str):
    """Launches console."""
    console = PylyglotConsole(language, locals={})
    banner = (
        f"Pylyglot {get_version('pylyglot')} {language} interpreter\n"
        f"Python {sys.version}"
    )
    console.interact(banner=banner)#, exitmsg=f"Saindo do Pylyglot {language}.")