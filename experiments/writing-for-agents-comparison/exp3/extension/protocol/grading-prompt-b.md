# Grading prompts (experiment 3 extension, part b)

## Case grader

Sent verbatim to both graders of each case, with `<DIR>` = `/tmp/wfa3x-grade/b/C?-g1` or `-g2`. The sandbox contains `rubric.md` (experiment 2's rubric, unchanged), `case/`, `key.md`, and the twelve reviews under `reviews/<id>.md` (same random ids for both graders of a case).

---

You are grading reviews of an expense claim that an AI produced. Work only inside `<DIR>`. Read nothing outside it, do not use the web, and do not invoke any skills.

1. Read `<DIR>/rubric.md` in full. It is the only scoring standard.
2. Read every file in `<DIR>/case/` (the claim, receipts, policy if present, and any other files) and `<DIR>/key.md`.
3. Grade every review in `<DIR>/reviews/`. Grade each review on its own against the key; do not rank reviews against each other or let one review change how you score another.
4. Apply the rubric literally. For every point deducted and every critical failure, quote the review (or say the expected item is absent) and cite the key's item or question. Evidence or grounds may appear anywhere in the review, as long as they are clearly tied to the item.
5. Write `<DIR>/grades.json`: a JSON array with one object per review: `{"review_id": "abcd", "scores": {"coverage": 0, "verdict_accuracy": 0, "grounds": 0, "amounts": 0, "questions": 0, "summary": 0}, "total": 0, "critical_failures": [{"type": "...", "item": "...", "quote": "..."}], "extra_content": false, "unneeded_clarification": false, "usefulness": 3, "deductions": [{"criterion": "...", "points": 0, "item": "...", "quote": "...", "reason": "..."}]}`.

`total` is the sum of the six (or seven) scores, rounded to one decimal place. Check that the file parses as JSON before you finish. Reply with one line per output (id, total, critical failure count), then at most three sentences on any judgement call another grader might make differently.

## Q1 grader (skill documents)

Sent verbatim, with `<DIR>` = `/tmp/wfa3x-grade/b/q1`. The sandbox contains `rubric.md` and `skills/S1/` to `skills/S12/`.

---

You are reviewing twelve AI-written agent skills that all answer the same request: reviewing an expense claim against the organisation's policy. Work only inside `<DIR>`. Read nothing outside it, do not use the web, and do not invoke any skills.

1. Read the "Q1 checklist for the skill documents" section of `<DIR>/rubric.md`.
2. For each folder in `<DIR>/skills/`, read every file and score the six checklist items 0 to 2, with one sentence of justification each. Score each skill on its own.
3. Write `<DIR>/q1.json`: a JSON array of `{"label": "S1", "items": {"1": 2, "2": 1, ...}, "total": 0, "justifications": {"1": "...", ...}, "words": 0, "files": ["SKILL.md", ...]}`, where `words` is the total word count of the skill's files. Check that it parses.

Reply with one line per skill: label, total, number of files.
