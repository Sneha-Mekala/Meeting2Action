# src/agents/task_creator_agent.py
from ..tools.jira_tool import JiraTool
from ..tools.sheet_tool import SheetTool
from ..utils import timestamp

class TaskCreatorAgent:
    """
    Agent that creates tasks in Jira (local mock) and logs them to a sheet (CSV).
    """
    def __init__(self):
        self.jira = JiraTool()
        self.sheet = SheetTool()

    def run(self, actions: list):
        created_issues = []

        for action in actions:
            title = action.get("task", "")[:140]
            owner = action.get("owner")
            due = action.get("due")
            notes = action.get("notes", "")

            # create issue in mock Jira
            issue = self.jira.create_issue(
                summary=title,
                assignee=owner,
                due=due,
                description=notes
            )

            # write to "sheet" (CSV)
            self.sheet.append_row([
                issue["id"],
                title,
                owner or "",
                due or "",
                timestamp()
            ])

            created_issues.append(issue)

        return created_issues