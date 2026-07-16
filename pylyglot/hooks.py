import sys, os
import importlib.machinery
import importlib.resources

from .translator import translate_file
from .config import options

class PylyglotSourceFileLoader(importlib.machinery.SourceFileLoader):

    def get_code(self, _):
        translated = translate_file(
            self.path, encoding=options["input_encoding"], 
            errors=options["encoding_errors"]
        )
        return compile(translated, self.path, "exec")

class PylyglotFileFinder(importlib.machinery.FileFinder):
    """Only defined for an "ininstance" call, no implementation."""
    pass

PYLYGLOT_SOURCE_SUFFIXES = None
def get_source_suffixes():
    global PYLYGLOT_SOURCE_SUFFIXES
    if PYLYGLOT_SOURCE_SUFFIXES is None:
        with importlib.resources.path("pylyglot", "languages") as path:
            file_list = os.listdir(str(path))

        file_list = [f".{f}" for f in file_list if f.endswith('.py') and not f.startswith("__")]
        file_list.insert(0, ".py") # Regular python
        PYLYGLOT_SOURCE_SUFFIXES = set(file_list) # Just in case
    
    return PYLYGLOT_SOURCE_SUFFIXES

# DEFAULT_LANGUAGE = None
def install():
    """Insert the pylyglot finder into sys.path_hooks."""
    if not any([isinstance(f, PylyglotFileFinder) for f in sys.path_hooks]):
        extension_list = get_source_suffixes()

        loader_details = [
            (importlib.machinery.ExtensionFileLoader, importlib.machinery.EXTENSION_SUFFIXES),
            (PylyglotSourceFileLoader, list(extension_list)),
            (importlib.machinery.SourcelessFileLoader, importlib.machinery.BYTECODE_SUFFIXES),
        ]

        sys.path_hooks.insert(0, PylyglotFileFinder.path_hook(*loader_details))
        sys.path_importer_cache.clear()