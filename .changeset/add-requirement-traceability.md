---
"mattpocock-skills": patch
---

Add the `requirement-traceability` skill (in-progress bucket, model-invoked). It is an opt-in convention that ties each requirement in a spec to a test and makes "every requirement has a test" checkable. A spec that carries requirement IDs (`CPN-3:` on the user stories) turns it on; a spec without them changes nothing. The skill defines the requirement ID (always colon-anchored, so `CPN-1` never matches `CPN-10`), a seam table, an ID-prefixed test tag, a per-issue `Covers:` line, and a coverage gap check that reports untested IDs, tagged tests with an undefined ID, and tests with no ID. Answers the "no ledger tying each resolved answer through to a spec, a ticket and a test" gap in the `grill-with-docs` docs.
