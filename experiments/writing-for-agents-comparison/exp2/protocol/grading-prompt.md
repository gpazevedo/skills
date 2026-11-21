# Grading prompts (experiment 2)

## Case grader

Sent verbatim to each of the two graders per case, with `<DIR>` replaced by its sandbox path (`/tmp/wfa-grade2/C?-g1` or `/tmp/wfa-grade2/C?-g2`). The sandbox contains `rubric.md`, `case/` (the case folder exactly as the runners saw it), `key.md`, and the six reviews under `reviews/<id>.md`, where each id is a random four-letter code (the same codes for both graders of a case, shuffled per case).

---

You are grading reviews of an expense claim that an AI produced. Work only inside `<DIR>`. Read nothing outside it, do not use the web, and do not invoke any skills.

1. Read `<DIR>/rubric.md` in full. It is the only scoring standard.
2. Read every file in `<DIR>/case/` (the claim, receipts, policy if present, and any other files) and `<DIR>/key.md`.
3. Grade every review in `<DIR>/reviews/`. Grade each review on its own against the key; do not rank reviews against each other or let one review change how you score another.
4. Apply the rubric literally. For every point deducted and every critical failure, quote the review (or say the expected item is absent) and cite the key's item or question. Evidence or grounds may appear anywhere in the review, as long as they are clearly tied to the item.
5. Write `<DIR>/grades.json`: a JSON array with one object per review:

```json
{
  "review_id": "abcd",
  "scores": {
    "coverage": 0,
    "verdict_accuracy": 0,
    "grounds": 0,
    "amounts": 0,
    "questions": 0,
    "summary": 0
  },
  "total": 0,
  "critical_failures": [
    {"type": "invented_policy_rule", "item": "4", "quote": "..."}
  ],
  "extra_content": false,
  "unneeded_clarification": false,
  "usefulness": 3,
  "deductions": [
    {"criterion": "amounts", "points": 10, "item": "total", "quote": "...", "reason": "..."}
  ]
}
```

`total` is the sum of the six scores, rounded to one decimal place. Check that the file parses as JSON before you finish. Reply with the file path and one line per review: id, total, critical failure count.

## Q1 grader (skill documents)

Sent verbatim, with `<DIR>` = `/tmp/wfa-grade2/q1`. The sandbox contains `rubric.md` and `skills/S1/` to `skills/S6/`.

---

You are reviewing six AI-written agent skills that all answer the same request: reviewing an expense claim against the organisation's policy. Work only inside `<DIR>`. Read nothing outside it, do not use the web, and do not invoke any skills.

1. Read the "Q1 checklist for the skill documents" section of `<DIR>/rubric.md`.
2. For each folder in `<DIR>/skills/`, read every file and score the six checklist items 0 to 2, with one sentence of justification each. Score each skill on its own.
3. Write `<DIR>/q1.json`: a JSON array of `{"label": "S1", "items": {"1": 2, "2": 1, ...}, "total": 0, "justifications": {"1": "...", ...}, "words": 0, "files": ["SKILL.md", ...], "supporting_files_note": "..."}`, where `words` is the total word count of the skill's files. Check that it parses.

Reply with the file path and one line per skill: label, total, number of files.
