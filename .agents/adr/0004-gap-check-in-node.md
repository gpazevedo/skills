# The coverage gap check runs in Node, sharing its rules with the Judgement pass

`requirement-traceability`'s coverage gap check was a bash block inside `SKILL.md`: GNU `grep`, `xargs`, `awk` and `comm`. The Judgement pass (`judge.mjs`, ADR 0003) needed the same rules in Node: which files are tests, where a tag counts, which tests are skipped, where a test ends. Two copies of those rules drifted the first time they changed: a skip whose test name wraps onto the next line had to be fixed twice, once in `awk` and once in JS.

So the check is `check.mjs`, and both scripts import the rules from `tags.mjs`. One fixture set (`scripts/fixtures/judge`, run by `node --test scripts/test-tags.mjs`) pins the rules for both.

What it bought:

- **No false green.** A quoted ID counts only where a test name sits (the first argument of `it(`, `test(` or `t.Run(`, or a pytest docstring's first line). The grep counted any quoted string that started with an ID, so `expect(label).toBe('CPN-1: …')` made an untested `CPN-1` look covered. That rule was too awkward to write as a grep.
- **No per-runner adaptation.** JS/TS, pytest and Go are recognised without the user swapping a declaration pattern.
- **Portability.** No GNU-only flags, so macOS works as is.

What it cost: Node is now needed for the check itself, not only for the opt-in pass. The check stays package-free, and `Check command:` in `docs/agents/traceability.md` still replaces it with a repo's own command. The `Covers:` structural check stays in bash: it reads the spec and the tickets, not test files, so it shares no rules with either script.
