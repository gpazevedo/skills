# Grading prompts (experiment 3 extension, part a)

## Case grader

Sent verbatim to both graders of each case, with `<DIR>` = `/tmp/wfa3x-grade/a/C?-g1` or `-g2`. The sandbox contains `rubric.md` (experiment 1's rubric, unchanged), `notes-<case>.md`, `key-<case>.md` and the twelve briefs under `briefs/<case>/<id>.md` (same random ids for both graders of a case).

---

You are grading decision briefs that an AI produced from meeting notes. Work only inside `<DIR>`. Read nothing outside it, do not use the web, and do not invoke any skills.

1. Read `<DIR>/rubric.md` in full. It is the only scoring standard. Ignore its "Agreement check" section, which does not apply here.
2. Read the notes and answer key, then grade every brief in `<DIR>/briefs/<case>/`. Grade each brief on its own against the key; do not rank briefs against each other or let one brief change how you score another.
3. Apply the rubric literally. For every point deducted and every critical failure, quote the brief (or say the expected item is absent) and cite the answer-key ID. Where the rubric and the key leave the size of a deduction open (for example an invented open question the key calls padding), deduct 3 points per item, as the rubric does for an invented action, and say so in the deduction's reason. Evidence for a decision may appear anywhere in the brief, as long as it is clearly tied to that decision.
4. Write `<DIR>/grades.json`: a JSON array with one object per brief: `{"brief_id": "abcd", "case": "<case>", "scores": {"decision_recall": 0, "decision_precision": 0, "evidence_fidelity": 0, "actions": 0, "open_questions": 0, "handoff": 0}, "total": 0, "critical_failures": [{"type": "...", "key_id": "...", "quote": "..."}], "extra_content": false, "unneeded_clarification": false, "usefulness": 3, "deductions": [{"criterion": "...", "points": 0, "key_id": "...", "quote": "...", "reason": "..."}]}`.

`total` is the sum of the six (or seven) scores, rounded to one decimal place. Check that the file parses as JSON before you finish. Reply with one line per output (id, total, critical failure count), then at most three sentences on any judgement call another grader might make differently.

## Q1 grader (skill documents)

Sent verbatim, with `<DIR>` = `/tmp/wfa3x-grade/a/q1`. The sandbox contains `rubric.md` and `skills/S1/` to `skills/S12/`.

---

You are reviewing twelve AI-written agent skills that all answer the same request: turning meeting notes into a decision brief. Work only inside `<DIR>`. Read nothing outside it, do not use the web, and do not invoke any skills.

1. Read the "Q1 checklist for the skill documents" section of `<DIR>/rubric.md`.
2. For each folder in `<DIR>/skills/`, read every file and score the six checklist items 0 to 2, with one sentence of justification each. Score each skill on its own.
3. Write `<DIR>/q1.json`: a JSON array of `{"label": "S1", "items": {"1": 2, "2": 1, ...}, "total": 0, "justifications": {"1": "...", ...}, "words": 0, "files": ["SKILL.md", ...]}`, where `words` is the total word count of the skill's files. Check that it parses.

Reply with one line per skill: label, total, number of files.
