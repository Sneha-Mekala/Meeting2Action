# src/tools/jira_tool.py
import uuid
from pathlib import Path
from ..utils import write_json, timestamp
import json

JIRA_DB = Path("artifacts/jira_issues.json")

class JiraTool:
    """
    Local Jira-like tool. Stores issues in artifacts/jira_issues.json
    """
    def __init__(self):
        JIRA_DB.parent.mkdir(parents=True, exist_ok=True)
        if not JIRA_DB.exists():
            write_json(JIRA_DB, [])

    def create_issue(self, summary, assignee=None, due=None, description=None):
        issues = []
        try:
            issues = json.loads(JIRA_DB.read_text())
        except Exception:
            issues = []

        issue_id = f"ISSUE-{uuid.uuid4().hex[:8]}"
        issue = {
            "id": issue_id,
            "summary": summary,
            "assignee": assignee,
            "due": due,
            "description": description,
            "created_at": timestamp()
        }

        issues.append(issue)
        write_json(JIRA_DB, issues)

        return issue