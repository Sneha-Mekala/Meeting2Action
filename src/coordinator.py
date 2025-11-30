# src/coordinator.py
from .agents.summarizer_agent import SummarizerAgent
from .agents.extractor_agent import ExtractorAgent
from .agents.task_creator_agent import TaskCreatorAgent
from .agents.notifier_agent import NotifierAgent
from .memory.memory_store import MemoryStore
from .tools.report_tool import ReportTool

class Coordinator:
    """
    Orchestrates the complete meeting processing pipeline:

    1. Summarize transcript
    2. Extract action items
    3. Store in memory (mem/)
    4. Create tasks (Jira mock + Sheet CSV)
    5. Notify owners (email log)
    6. Generate beautiful reports (DOCX/PDF/RTF)
    """

    def __init__(self):
        self.summarizer = SummarizerAgent()
        self.extractor = ExtractorAgent()
        self.task_creator = TaskCreatorAgent()
        self.notifier = NotifierAgent()
        self.mem = MemoryStore()
        self.reporter = ReportTool()

    def run_pipeline(self, transcript: str, meeting_id: str):
        # 1. Summary
        summary = self.summarizer.run(transcript)

        # 2. Extract actions
        actions = self.extractor.run(transcript)

        # 3. Store meeting data in local memory folder
        meeting_data = {
            "transcript": transcript,
            "summary": summary,
            "actions": actions
        }
        self.mem.store_meeting(meeting_id, meeting_data)

        # 4. Create tasks issue list
        created_issues = self.task_creator.run(actions)

        # 5. Notify owners through local email log
        notifications = self.notifier.run(created_issues)

        # 6. Generate report files (DOCX, PDF, RTF)
        report_files = self.reporter.generate(meeting_id, summary, actions, created_issues, notifications)

        return {
            "meeting_id": meeting_id,
            "summary": summary,
            "action_items": actions,
            "tasks": created_issues,
            "notifications": notifications,
            "reports": report_files
        }
