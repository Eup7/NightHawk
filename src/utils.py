import os
import yaml
from pathlib import Path

def load_config(config_file='config/config.yaml'):
    """加载配置文件"""
    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        return {}

def ensure_dir_exists(directory):
    """确保目录存在，如果不存在则创建"""
    Path(directory).mkdir(parents=True, exist_ok=True)

def get_wordlist_path(wordlist_name):
    """获取字典文件的完整路径"""
    return os.path.join('wordlists', f"{wordlist_name}.txt") 