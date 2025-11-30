# evaluate.py
import json
from src.extractors import extract_action_items

def compare_actions(pred, gold):
    """
    Compare predicted vs gold actions.
    Measures:
        - owner correctness
        - due date correctness
    """

    tp_owner = fp_owner = fn_owner = 0
    tp_due = fp_due = fn_due = 0

    # Gold lists
    gold_owners = [g.get("owner") for g in gold if g.get("owner")]
    gold_dues = [g.get("due") for g in gold if g.get("due")]

    # Pred lists
    pred_owners = [p.get("owner") for p in pred if p.get("owner")]
    pred_dues = [p.get("due") for p in pred if p.get("due")]

    # Compare owners
    for owner in pred_owners:
        if owner in gold_owners:
            tp_owner += 1
        else:
            fp_owner += 1

    for owner in gold_owners:
        if owner not in pred_owners:
            fn_owner += 1

    # Compare due dates
    for due in pred_dues:
        if due in gold_dues:
            tp_due += 1
        else:
            fp_due += 1

    for due in gold_dues:
        if due not in pred_dues:
            fn_due += 1

    return tp_owner, fp_owner, fn_owner, tp_due, fp_due, fn_due


def safe_pr(tp, fp, fn):
    precision = tp / (tp + fp) if (tp + fp) else 0.0
    recall = tp / (tp + fn) if (tp + fn) else 0.0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) else 0.0
    return {"precision": precision, "recall": recall, "f1": f1}


def evaluate(labels_file="data/labels.json"):
    with open(labels_file, "r", encoding="utf-8") as f:
        labels = json.load(f)

    owner_tp = owner_fp = owner_fn = 0
    due_tp = due_fp = due_fn = 0

    for item in labels:
        transcript = item["transcript"]
        gold = item["actions"]

        pred = extract_action_items(transcript)

        (tp_o, fp_o, fn_o, tp_d, fp_d, fn_d) = compare_actions(pred, gold)

        owner_tp += tp_o
        owner_fp += fp_o
        owner_fn += fn_o
        due_tp += tp_d
        due_fp += fp_d
        due_fn += fn_d

    owner_scores = safe_pr(owner_tp, owner_fp, owner_fn)
    due_scores = safe_pr(due_tp, due_fp, due_fn)

    print("\n### EVALUATION RESULTS ###")
    print("Owner Extraction:", owner_scores)
    print("Due Date Extraction:", due_scores)


if __name__ == "__main__":
    evaluate()