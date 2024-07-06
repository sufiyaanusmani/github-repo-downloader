from pathlib import Path

DATA_DIR = Path.cwd() / 'data'
DATA_DIR.mkdir(parents=True, exist_ok=True)

class Directory:
    DATA_DIR = DATA_DIR

class Colors:
    RESET = "\033[0m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    GREEN = "\033[92m"

class Message:
    ERROR = "error"
    WARNING = "warning"
    SUCCESS = "success"
    INFO = "info"
