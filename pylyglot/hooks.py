import sys, os, re
import importlib.machinery

from .translator import translate_file, get_pylyglot_message
from .utils import get_source_suffixes

from . import debug
from . import config

class PylyglotSourceFileLoader(importlib.machinery.SourceFileLoader):
    """Custom loader for Pylyglot files."""
    def get_code(self, _):
        """Translates file and returns compiled version"""
        if debug.VERBOSE_LEVEL >= 2:  print(f"> hooks.PylyglotSourceFileLoader.get_code(): self.path: {self.path}")
        translated = translate_file(
            self.path, encoding=config.options["input_encoding"], 
            errors=config.options["encoding_errors"]
        )
        if debug.VERBOSE_LEVEL >= 3:  print(f"> hooks.PylyglotSourceFileLoader.get_code(): translated file:\n{translated}")
        return compile(translated, self.path, "exec")

class PylyglotFileFinder(importlib.machinery.FileFinder):
    """Custom loader for Pylyglot files."""
    def find_spec(self, fullname, target = ...):
        """
        Wraps super().find_spec(), checking if there are multiple
        files with the same name (and raises an error if that is
        the case).
        """
        if debug.VERBOSE_LEVEL >= 2:  print(f"> hooks.PylyglotFileFinder.find_spec(): self.path: {self.path}")
        if debug.VERBOSE_LEVEL >= 2:  print(f"> hooks.PylyglotFileFinder.find_spec(): fullname: {fullname}")
        if debug.VERBOSE_LEVEL >= 2:  print(f"> hooks.PylyglotFileFinder.find_spec(): target: {target}")
        potential_files = [
            file for file in os.listdir(self.path)
            if  (file.split(".")[0] == fullname) \
            and (file.split(".")[-1] == "py")
        ]
        if debug.VERBOSE_LEVEL >= 2:  print(f"> hooks.PylyglotFileFinder.find_spec(): potential_files: {potential_files}")
        if len(potential_files) > 1:
            raise ImportError(get_pylyglot_message(config.options["default_language"], "hooks_duplicate_module", fullname=fullname, dir_path=self.path, potential_files=potential_files))        
        return super().find_spec(fullname, target)


# DEFAULT_LANGUAGE = None
def install():
    """Insert the pylyglot finder into sys.path_hooks."""
    if not any([isinstance(f, PylyglotFileFinder) for f in sys.path_hooks]):
        if debug.VERBOSE_LEVEL >= 2:  print("> hooks.install(): Installing hooks...")
        extension_list = get_source_suffixes()
        if debug.VERBOSE_LEVEL >= 2:  print(f"> hooks.install(): source suffixes: {extension_list}")

        loader_details = [
            (importlib.machinery.ExtensionFileLoader, importlib.machinery.EXTENSION_SUFFIXES),
            (PylyglotSourceFileLoader, list(extension_list)),
            (importlib.machinery.SourcelessFileLoader, importlib.machinery.BYTECODE_SUFFIXES),
        ]

        sys.path_hooks.insert(0, PylyglotFileFinder.path_hook(*loader_details))
        sys.path_importer_cache.clear()
    elif debug.VERBOSE_LEVEL >= 2: 
        print("> hooks.install(): Hooks appear to already be installed...")

    if debug.VERBOSE_LEVEL >= 2: 
        print("> hooks.install(): sys.path_hooks:", sys.path_hooks)