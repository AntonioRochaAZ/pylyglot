import sys, os, re
import importlib.machinery

from .translator import translate_file, get_pylyglot_message
from .config import options
from .utils import get_source_suffixes

class PylyglotSourceFileLoader(importlib.machinery.SourceFileLoader):
    """Custom loader for Pylyglot files."""
    def get_code(self, _):
        """Translates file and returns compiled version"""
        translated = translate_file(
            self.path, encoding=options["input_encoding"], 
            errors=options["encoding_errors"]
        )
        return compile(translated, self.path, "exec")

class PylyglotFileFinder(importlib.machinery.FileFinder):
    """Custom loader for Pylyglot files."""
    def find_spec(self, fullname, target = ...):
        """
        Wraps super().find_spec(), checking if there are multiple
        files with the same name (and raises an error if that is
        the case).
        """
        potential_files = [
            file for file in os.listdir(self.path)
            if  (file.split(".")[0] == fullname) \
            and (file.split(".")[-1] == "py")
        ]
        if len(potential_files) > 1:
            raise ImportError(get_pylyglot_message(options["default_language"], "hooks_duplicate_module", fullname=fullname, dir_path=self.path, potential_files=potential_files))        
        return super().find_spec(fullname, target)


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