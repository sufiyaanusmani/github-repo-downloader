from pathlib import Path

DATA_DIR = Path.cwd() / 'data'
DATA_DIR.mkdir(parents=True, exist_ok=True)

class Directory:
    DATA_DIR = DATA_DIR
