# src/extractors.py
import re
from typing import List, Dict
from datetime import datetime

# REGEX patterns
EMAIL_RE = re.compile(r'([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,})')
DATE_ISO_RE = re.compile(r'(\d{4}-\d{2}-\d{2})')  # yyyy-mm-dd
ACTION_KEYWORDS = re.compile(
    r'\b(action|todo|assign|to do|we will|please|follow up|follow-up|task)\b',
    re.I
)


def summarize_transcript(transcript: str, max_sentences: int = 3) -> str:
    """
    Very simple summarizer:
    Picks first few significant sentences.
    Works offline (no AI API).
    """
    sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', transcript) if s.strip()]
    top = sentences[:max_sentences]

    if not top:
        return "- No summary available."

    return "\n".join([f"- {s}" for s in top])


def extract_action_items(transcript: str) -> List[Dict]:
    """
    Extracts action items using regex + rule-based logic.
    Returns list of:
        {"task": ..., "owner": ..., "due": ..., "notes": ...}
    """
    results = []
    lines = [line.strip() for line in transcript.split("\n") if line.strip()]

    for ln in lines:
        # action keyword check
        if ACTION_KEYWORDS.search(ln):
            task = ln
            owner = None
            due = None
            notes = ""

            # extract email as owner
            email_match = EMAIL_RE.search(ln)
            if email_match:
                owner = email_match.group(1)

            # owner detection by name (fallback)
            if not owner:
                # look for pattern "Name will", "Name to"
                name_pattern = re.search(r'([A-Z][a-z]{1,20})\s+(will|to)\b', ln)
                if name_pattern:
                    owner = name_pattern.group(1) + "@example.com"

            # due date detection
            date_match = DATE_ISO_RE.search(ln)
            if date_match:
                due = date_match.group(1)
            else:
                # relative example: "next week"
                if re.search(r'next week', ln, re.I):
                    due = datetime.utcnow().date().isoformat()

            results.append({
                "task": task,
                "owner": owner,
                "due": due,
                "notes": notes
            })

    return results