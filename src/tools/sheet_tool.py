# src/tools/sheet_tool.py
import csv
from pathlib import Path

SHEET_CSV = Path("artifacts/sheet_rows.csv")

class SheetTool:
    """
    Appends rows to a CSV file to simulate a tracker (Google Sheets).
    """
    def __init__(self):
        SHEET_CSV.parent.mkdir(parents=True, exist_ok=True)
        if not SHEET_CSV.exists():
            with SHEET_CSV.open("w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["ticket_id", "task", "owner", "due", "created_at"])

    def append_row(self, row):
        with SHEET_CSV.open("a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(row)
        return {"status": "ok"}
