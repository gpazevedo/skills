# Grading notes (phase 7)

- 36 case-grader runs and 3 Q1 runs, fresh agents, outputs under labels S1 to S20 and random ids.
- Two case graders per case disagreed on some deductions, as expected. Both sets are kept and averaged.
- Q1, part a: the first run wrote generic per-level justifications instead of per-skill ones, so it was discarded (kept as the sandbox file `q1.attempt1-generic.json`, not used) and rerun with the same prompt. Q1 parts b and c: the first launch hit the concurrent-agent limit (b, c) and a rate limit (rerun), so they were run once more with the same prompt. Q1 is secondary and does not enter the decision rule.
- No grader reported unread outputs.
- Mappings were still sealed when these grades were committed.
