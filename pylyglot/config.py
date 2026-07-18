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

def get_config_path():
    return config_path

def get_config():
    with open(config_path, "r") as f:
        config = json.load(f)
    return config

def save_config(config):
    with open(config_path, "w") as f:
        json.dump(config, f, indent=4)


def set_config(key, value):
    from .translator import get_pylyglot_message
    config = get_config()

    if key not in config:
        raise KeyError(get_pylyglot_message(options["default_language"], "config_key_error", key=key)) 

    old_value = config[key]
    config[key] = value
    save_config(config)
    print(get_pylyglot_message(options["default_language"], "config_set_success", key=key, old_value=old_value, value=value))

def reset_config():
    from .translator import get_pylyglot_message
    save_config(default_config)
    print(get_pylyglot_message(options["default_language"], "config_reset_success"))

options = get_config() # Session options, initialized with user config.