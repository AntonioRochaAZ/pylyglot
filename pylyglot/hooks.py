"""Made by Claude AI"""
import sys
import importlib
import importlib.util
from pathlib import Path
from .translator import detect_language

import importlib.abc
import importlib.util

class PylyglotLoader(importlib.abc.Loader):
    def __init__(self, language: str, path: str):
        self.language = language
        self.path = path

    def create_module(self, spec):
        return None  # use default module creation

    def exec_module(self, module):
        from .translator import translate_file
        
        translated = translate_file(self.path, input_language=self.language)  # ← named arg
        
        module.__file__ = self.path
        module.__loader__ = self
        module.__package__ = module.__spec__.parent
        
        code = compile(translated, self.path, "exec")
        exec(code, module.__dict__)


class PylyglotFinder:
    def find_spec(self, fullname, path, target=None):
        search_paths = path if path else sys.path
        module_name = fullname.split(".")[-1]

        for directory in search_paths:
            directory = Path(directory)
            
            # first try exact match
            candidate = directory / f"{module_name}.py"
            
            # if not found, look for {module_name}.*.py (e.g. pt_br_2.pt_br_simples.py)
            if not candidate.exists():
                matches = list(directory.glob(f"{module_name}.*.py"))
                if not matches:
                    continue
                if len(matches) > 1:
                    raise ImportError(
                        f"Ambiguous import '{module_name}': multiple pylyglot files found in {directory}:\n"
                        + "\n".join(str(m) for m in matches)
                    )
                candidate = matches[0]

            try:
                language = detect_language(str(candidate))
            except OSError:
                continue
            
            if language is None:
                # Use python default
                continue

            loader = PylyglotLoader(language, str(candidate))
            return importlib.util.spec_from_file_location(
                fullname,
                candidate,
                loader=loader,
            )
        return None


def install():
    """Insert the pylyglot finder into sys.meta_path."""
    if not any(isinstance(f, PylyglotFinder) for f in sys.meta_path):
        sys.meta_path.insert(0, PylyglotFinder())