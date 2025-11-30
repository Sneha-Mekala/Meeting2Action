# src/tools/email_tool.py
from pathlib import Path
from ..utils import timestamp, write_json
import json

EMAIL_LOG = Path("logs/email_log.json")

def ensure_email_log():
    EMAIL_LOG.parent.mkdir(parents=True, exist_ok=True)
    if not EMAIL_LOG.exists():
        write_json(EMAIL_LOG, [])

class EmailTool:
    """
    Local email logger. Writes "sent emails" to logs/email_log.json
    """
    def __init__(self):
        ensure_email_log()

    def send_assignment(self, to_email, ticket):
        # Read existing log
        try:
            entries = json.loads(EMAIL_LOG.read_text())
        except:
            entries = []

        entry = {
            "to": to_email,
            "ticket": ticket,
            "sent_at": timestamp()
        }

        entries.append(entry)
        write_json(EMAIL_LOG, entries)

        print(f"[EmailTool] Simulated email sent to {to_email} for ticket {ticket['id']}")

        return {"status": "sent"}