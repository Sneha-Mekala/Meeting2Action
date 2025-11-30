# src/utils.py
import json
from pathlib import Path
from datetime import datetime

BASE_DIR = Path.cwd()

def write_json(path, obj):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, indent=2))

def read_json(path):
    p = Path(path)
    if p.exists():
        return json.loads(p.read_text())
    return None

def timestamp():
    return datetime.utcnow().isoformat() + "Z"
