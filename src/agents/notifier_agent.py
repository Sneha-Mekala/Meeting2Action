# src/agents/notifier_agent.py
from ..tools.email_tool import EmailTool

class NotifierAgent:
    """
    Agent responsible for notifying owners by email (simulated).
    """
    def __init__(self):
        self.email = EmailTool()

    def run(self, created_issues):
        results = []

        for issue in created_issues:
            to_email = issue.get("assignee")

            if to_email:
                status = self.email.send_assignment(to_email, issue)
                results.append({
                    "issue": issue["id"],
                    "email_status": status["status"]
                })

        return results
