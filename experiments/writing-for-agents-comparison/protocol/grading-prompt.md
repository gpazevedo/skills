# Grading prompts

## Case grader

Sent verbatim to each case grader (one per case, and to the agreement re-scorer), with `<DIR>` replaced by its sandbox path (`/tmp/wfa-grade/C?` or `/tmp/wfa-grade/agree`). The sandbox contains `rubric.md`, and for each case to grade `notes-<case>.md`, `key-<case>.md` and the briefs under `briefs/<id>.md`, where each id is a fresh random four-letter code.

---

You are grading decision briefs that an AI produced from meeting notes. Work only inside `<DIR>`. Read nothing outside it, do not use the web, and do not invoke any skills.

1. Read `<DIR>/rubric.md` in full. It is the only scoring standard.
2. For each case present, read its notes and answer key, then grade every brief listed for that case in `<DIR>/briefs/`. Grade each brief on its own against the key; do not rank briefs against each other or let one brief change how you score another.
3. Apply the rubric literally. For every point deducted and every critical failure, quote the brief (or say the expected item is absent) and cite the answer-key ID.
4. Write `<DIR>/grades.json`: a JSON array with one object per brief:

```json
{
  "brief_id": "abcd",
  "case": "01-clear",
  "scores": {
    "decision_recall": 0,
    "decision_precision": 0,
    "evidence_fidelity": 0,
    "actions": 0,
    "open_questions": 0,
    "handoff": 0
  },
  "total": 0,
  "critical_failures": [
    {"type": "fabricated_owner", "key_id": "A2", "quote": "..."}
  ],
  "extra_content": false,
  "unneeded_clarification": false,
  "usefulness": 3,
  "deductions": [
    {"criterion": "actions", "points": 5, "key_id": "A2", "quote": "...", "reason": "..."}
  ]
}
```

`total` is the sum of the six scores, rounded to one decimal place. Check that the file parses as JSON before you finish. Reply with the file path and one line per brief: id, total, critical failure count.

## Q1 grader (skill documents)

Sent verbatim, with `<DIR>` = `/tmp/wfa-grade/q1`. The sandbox contains `rubric.md` and `skills/S1/` to `skills/S6/`, each a candidate skill folder.

---

You are reviewing six AI-written agent skills that all answer the same request: turning meeting notes into a decision brief. Work only inside `<DIR>`. Read nothing outside it, do not use the web, and do not invoke any skills.

1. Read the "Q1 checklist for the skill documents" section of `<DIR>/rubric.md`.
2. For each folder in `<DIR>/skills/`, read every file and score the six checklist items 0 to 2, with one sentence of justification each. Score each skill on its own.
3. Write `<DIR>/q1.json`: a JSON array of `{"label": "S1", "items": {"1": 2, "2": 1, ...}, "total": 0, "justifications": {"1": "...", ...}, "words": 0}`, where `words` is the total word count of the skill's files. Check that it parses.

Reply with the file path and one line per skill: label, total.
