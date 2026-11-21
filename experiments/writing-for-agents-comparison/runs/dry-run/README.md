# Phase 3 dry run (not scored)

A hand-written throwaway skill (`throwaway-SKILL.md`, not a candidate) was run on case 01 with the execution prompt, and its brief was graded with the case-grader prompt. Both agents were fresh general-purpose subagents.

- Runner: 4 tool calls, 13 s. Read only its sandbox.
- Grader: 5 tool calls, 53 s. `grades.json` parsed; total 91.5 matched the sum of the six scores.

Fixes made to `protocol/grading-prompt.md` before Phase 4:

1. Briefs now sit under `briefs/<case>/<id>.md`, so a grader holding several cases (the agreement re-scorer) knows each brief's case.
2. Tie-break for unspecified deduction sizes (3 points per item, matching the rubric's invented-action penalty), and evidence may appear anywhere in the brief if clearly tied to its decision. The dry-run grader made both calls on its own; the line makes them consistent across graders. The rubric, cases, keys and decision rule are unchanged.
