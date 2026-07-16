import json
from pathlib import Path

# A little harder for people to change if it is in code:
default_config = {
    "verbose": False,
    "default_language": "en",
    "input_encoding": "utf-8",
    "encoding_errors": "strict", 
    "output_encoding": "utf-8"
}

config_path = Path(__file__).resolve().parent/"config.json"

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
    config = get_config()

    if key not in config:
        raise KeyError(
            f'"{key}" not in pylyglot config file.'
            '\nTo see options, run "python -m pylyglot --getconfig"'
            '\nTo get the path to the config.json, run "python -m pylyglot --getconfigpath"'
        ) # TODO: translate

    old_value = config[key]
    config[key] = value
    save_config(config)
    print(f"Successfully updated config option {key} from {old_value} to {value}.") # TODO: Translate

def reset_config():
    save_config(default_config)
    print(f"Config was reset to defaults.") # TODO: translate

options = get_config() # Session options, initialized with user config.