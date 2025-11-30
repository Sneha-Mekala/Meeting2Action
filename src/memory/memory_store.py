# src/memory/memory_store.py
from pathlib import Path
import json
from ..utils import write_json, read_json

class MemoryStore:
    """
    Simple file-based memory store.
    Stores per-meeting JSON under mem/{meeting_id}.json
    """
    def __init__(self, base="mem"):
        self.base = Path(base)
        self.base.mkdir(parents=True, exist_ok=True)

    def store_meeting(self, meeting_id, data: dict):
        path = self.base / f"{meeting_id}.json"
        write_json(path, data)

    def load_meeting(self, meeting_id):
        path = self.base / f"{meeting_id}.json"
        return read_json(path)

    def list_meetings(self):
        return [p.name for p in self.base.glob("*.json")]
