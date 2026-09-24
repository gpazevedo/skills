---
type: llm
focus: last_message
weight: 1
---

The spec carries no requirement IDs, and the user did not ask for traceability.

Judge one thing only: whether the reply leaves the traceability convention switched off.

It passes unless the reply does one of these:

- Assigns identifiers such as `CPN-1:` or `REQ-2:` to the user stories, or rewrites the spec to carry them.
- Adds a `Covers:` line, a seam table keyed by requirement ID, or a coverage gap report.

Everything else is out of scope for this grader. How good the spec review is, how long it is, and whether it names tests at all neither pass nor fail it. Offering traceability as a suggestion passes; applying it unasked does not.
