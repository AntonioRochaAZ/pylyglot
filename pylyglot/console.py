import sys, code, traceback, importlib
from .translator import translate_source, get_dictionary, translate_traceback_line


class PylyglotConsole(code.InteractiveConsole):
    def __init__(self, language: str, **kwargs):
        super().__init__(**kwargs)
        self.dictionary = get_dictionary(language)
        self.inv_dictionary = {v: k for k, v in self.dictionary.items()}
        self.language = language
        
        # merge traceback translations with inv_dictionary for traceback translation
        tb_module = importlib.import_module(f"pylyglot.languages.{language}")
        tb_dictionary = getattr(tb_module, 'traceback_dictionary', {})
        self.traceback_dictionary = {**self.inv_dictionary, **{v: k for k, v in tb_dictionary.items()}}

    def runsource(self, source, filename="<input>", symbol="single"):
        try:
            translated = translate_source(source, self.dictionary)
        except Exception:
            translated = source
        return super().runsource(translated, filename, symbol)

    def translate_traceback_line(self, line: str) -> str:
        return translate_traceback_line(line, self.traceback_dictionary)

    def showtraceback(self):
        """Override to translate traceback output."""
        try:
            type_, value, tb = sys.exc_info()
            lines = traceback.format_exception(type_, value, tb)
            translated_lines = []
            for line in lines:
                # translate each sub-line within the traceback block
                sub_lines = line.splitlines(keepends=True)
                translated_lines.append(
                    ''.join(self.translate_traceback_line(l) for l in sub_lines)
                )
            output = ''.join(translated_lines)
            self.write(output)
        except Exception:
            # if anything goes wrong, fall back to default
            super().showtraceback()

    def showsyntaxerror(self, filename=None, **kwargs):
        try:
            type_, value, tb = sys.exc_info()
            lines = traceback.format_exception_only(type_, value)
            translated_lines = [self.translate_traceback_line(l) for l in lines]
            self.write(''.join(translated_lines))
        except Exception:
            super().showsyntaxerror(filename, **kwargs)


def launch_console(language: str):
    try:
        import readline
        import rlcompleter
        readline.parse_and_bind("tab: complete")
    except ImportError:
        pass

    console = PylyglotConsole(language, locals={})
    banner = (
        f"Pylyglot {language} interpreter\n"
        f"Python {sys.version}"
    )
    console.interact(banner=banner)#, exitmsg=f"Saindo do Pylyglot {language}.")