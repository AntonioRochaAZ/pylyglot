"""
Pylyglot maintains a config JSON file with preferred
settings. This module defines functions to retrieve
it and change its values. 

It also defines the global "options" variable
(initialized with the cited config) for each run.


"""

import json
from pathlib import Path
import importlib.resources

# A little harder for people to change if it is in code:
default_config = {
    "verbose": False,
    "default_language": "en",
    "input_encoding": "utf-8",
    "encoding_errors": "strict", 
    "output_encoding": "utf-8"
}

with importlib.resources.path("pylyglot", "config.json") as path:
    config_path = Path(path).resolve()

def get_config_path() -> Path:
    """Returns the path to the config JSON file."""
    return config_path

def get_config() -> dict:
    """Returns the config dictionary."""
    with open(config_path, "r") as f:
        config = json.load(f)
    return config

def save_config(config: dict) -> None:
    """Saves a given config dictionary to the config file."""
    with open(config_path, "w") as f:
        json.dump(config, f, indent=4)


def set_config(key: str, value: str) -> None:
    """Sets a config's key to a given value.
    
    Raises
        ValueError: If trying to set the value of the "allow_renames" option.
        KeyError: If the key is not in config.

    """
    from .translator import get_pylyglot_message
    config = get_config()

    if key == "allow_renames":
        raise ValueError(get_pylyglot_message(options["default_language"], "config_allow_renames"))

    if key not in config:
        raise KeyError(get_pylyglot_message(options["default_language"], "config_key_error", key=key)) 

    old_value = config[key]
    config[key] = value
    save_config(config)

    if key == "default_language":
        # A little treat :)
        options["default_language"] = value

    print(get_pylyglot_message(options["default_language"], "config_set_success", key=key, old_value=old_value, value=value))

def reset_config():
    """Reset config to default."""
    from .translator import get_pylyglot_message
    save_config(default_config)
    print(get_pylyglot_message(options["default_language"], "config_reset_success"))

options = get_config() # Session options, initialized with user config.