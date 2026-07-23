import sys, os, re
import importlib.machinery
import importlib.resources

from .translator import translate_file, get_pylyglot_message
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
    def find_spec(self, fullname, target = ...):
        potential_files = [
            file for file in os.listdir(self.path)
            if  (file.split(".")[0] == fullname) \
            and (file.split(".")[-1] == "py")
        ]
        if len(potential_files) > 1:
            raise ImportError(get_pylyglot_message(options["default_language"], "hooks_duplicate_module", fullname=fullname, dir_path=self.path, potential_files=potential_files))        
        return super().find_spec(fullname, target)

def get_source_suffixes():

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