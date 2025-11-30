# tests/test_extractors.py
from src.extractors import extract_action_items

def test_simple_extraction():
    transcript = "Rohit: Action: Rohit (rohit@example.com) will finish by 2025-12-01."
    actions = extract_action_items(transcript)

    assert isinstance(actions, list)
    assert len(actions) >= 1

    first = actions[0]
    assert first["owner"] == "rohit@example.com"
    assert first["due"] == "2025-12-01"
    assert "Action:" in first["task"]