---
type: llm
focus: last_message
weight: 2
---

The user asked for the requirements in a three-story spec to be made traceable, with two tickets: ticket 01 builds applying a coupon and case-insensitive codes; ticket 02 builds refusing an expired coupon.

Judge one thing only: whether the reply shows the spec and tickets annotated.

It passes when the reply shows all of these:

- Each of the three user stories carries an ID of the form `<KEY>-<n>:` with one shared KEY of 2 to 5 uppercase letters.
- Each ticket has a `Covers:` line.
- Every ID appears on exactly one ticket's `Covers:` line: the apply and case stories on ticket 01, the expiry story on ticket 02.

Anything else (wording, a seam table's exact shape, extra advice) neither passes nor fails it.
