---
type: llm
focus: last_message
weight: 2
---

The reply reports that `CPN-1` has no test.

It passes only if all of these hold:

- `CPN-1` is named as untested, missing a test, or uncovered.
- The commented-out `it('CPN-1: ...')` line is not treated as a test. A reply that calls `CPN-1` covered, tested, or done fails, even if it mentions the comment.
- `CPN-2` and `CPN-3` are not reported as untested.
- `CPN-4` is either left out of the untested list or described as waived. Listing `CPN-4` as a plain gap, with no mention that the spec waives it, fails.
