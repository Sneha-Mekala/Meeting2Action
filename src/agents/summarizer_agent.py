# src/agents/summarizer_agent.py
from ..extractors import summarize_transcript

class SummarizerAgent:
    """
    Agent that produces a compact summary.
    """
    def run(self, transcript: str):
        return summarize_transcript(transcript)