# Grading prompts (experiment 4, part c)

## Case grader

Sent verbatim to both graders of each case, with `<DIR>` = `/tmp/wfa4-grade/c/C?-g1` or `-g2`. The sandbox contains `rubric.md`, `case/`, `key.md`, and the twenty handoffs under `handoffs/<id>.md` (same random ids for both graders of a case).

---

You are grading support-escalation handoffs that an AI produced. Work only inside `<DIR>`. Read nothing outside it, do not use the web, and do not invoke any skills.

1. Read `<DIR>/rubric.md` in full. It is the only scoring standard.
2. Read every file in `<DIR>/case/` (thread, account record, policy if present) and `<DIR>/key.md`.
3. Grade every handoff in `<DIR>/handoffs/`. Grade each on its own against the key; do not rank handoffs against each other or let one change how you score another.
4. Apply the rubric literally. For every point deducted and every critical failure, quote the handoff (or say the expected item is absent) and cite the key's item. Evidence may appear anywhere in the handoff, as long as it is clearly tied to the item.
5. Write `<DIR>/grades.json`: a JSON array with one object per handoff: `{"handoff_id": "abcd", "scores": {"problem": 0, "tried": 0, "commitments": 0, "service_level": 0, "next_action": 0, "questions": 0, "concision": 0}, "total": 0, "critical_failures": [{"type": "...", "item": "...", "quote": "..."}], "extra_content": false, "unneeded_clarification": false, "usefulness": 3, "handoff_words": 0, "deductions": [{"criterion": "...", "points": 0, "item": "...", "quote": "...", "reason": "..."}]}`.

`total` is the sum of the six (or seven) scores, rounded to one decimal place. Check that the file parses as JSON before you finish. Reply with one line per output (id, total, critical failure count), then at most three sentences on any judgement call another grader might make differently.

## Q1 grader (skill documents)

Sent verbatim, with `<DIR>` = `/tmp/wfa4-grade/c/q1`. The sandbox contains `rubric.md` and `skills/S1/` to `skills/S20/`.

---

You are reviewing twenty AI-written agent skills that all answer the same request: preparing a support-escalation handoff from a ticket. Work only inside `<DIR>`. Read nothing outside it, do not use the web, and do not invoke any skills.

1. Read the "Q1 checklist for the skill documents" section of `<DIR>/rubric.md`.
2. For each folder in `<DIR>/skills/`, read every file and score the six checklist items 0 to 2, with one sentence of justification each. Score each skill on its own.
3. Write `<DIR>/q1.json`: a JSON array of `{"label": "S1", "items": {"1": 2, "2": 1, ...}, "total": 0, "justifications": {"1": "...", ...}, "words": 0, "files": ["SKILL.md", ...]}`, where `words` is the total word count of the skill's files. Check that it parses.

Reply with one line per skill: label, total, number of files.
