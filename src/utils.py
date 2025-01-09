import os
import yaml
from pathlib import Path

def load_config(config_file='config/config.yaml'):
    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        return {}

def ensure_dir_exists(directory):
    Path(directory).mkdir(parents=True, exist_ok=True)

def get_wordlist_path(wordlist_name):
    return os.path.join('wordlists', f"{wordlist_name}.txt") 