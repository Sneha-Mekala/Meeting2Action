# src/agents/extractor_agent.py
from ..extractors import extract_action_items

class ExtractorAgent:
    """
    Agent that extracts action items from a transcript.
    """
    def run(self, transcript: str):
        return extract_action_items(transcript)
