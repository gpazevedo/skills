---
type: llm
focus: last_message
weight: 2
---

Exactly one requirement, `CPN-1`, has no test. Every other ID from `CPN-2` to `CPN-12` is tagged on a test.

It passes only if both hold:

- The reply names `CPN-1` as a requirement with no test of its own.
- The reply does not answer that every requirement is covered, and does not claim some other ID is the untested one.

Judge only the coverage question. Remarks about how good the existing tests are, or about anything else in the repo, neither pass nor fail the reply.
