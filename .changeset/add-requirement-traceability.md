---
"mattpocock-skills": patch
---

Add the `requirement-traceability` skill (engineering bucket, model-invoked). It is an opt-in convention that ties each requirement in a spec to a test and makes "every requirement has a test" checkable. A spec that carries requirement IDs (`CPN-3:` on the user stories) turns it on; a spec without them changes nothing. The skill defines the requirement ID (always colon-anchored, so `CPN-1` never matches `CPN-10`), a seam table, an ID-prefixed test tag, a per-issue `Covers:` line, and a coverage gap check that reports untested IDs, tagged tests with an undefined ID, and tests with no ID.

`to-spec`, `to-tickets`, `tdd`, `implement` and `code-review` each gain one guarded step that calls it, and does nothing when the spec has no IDs. `code-review` hands the Spec sub-agent the test files and the gap list only when the spec carries IDs. Docs pages, `ask-matt` and `CONTEXT.md` are re-synced, and the `grill-with-docs` page now names traceability as the mitigation for the spec-to-test half of its "no ledger" complaint.

The gap check ignores commented-out and skipped tests, so a requirement whose only test is switched off is reported untested instead of covered. For runners that tag a test in its docstring (pytest), the "no ID" warning pairs each declaration with the line after it, so a correctly tagged test is no longer warned about. `scripts/test-traceability-check.sh` runs the block straight out of `SKILL.md` against a fixture and holds both behaviours in place.
