---
name: implement
description: "Implement a piece of work based on a spec or set of tickets."
disable-model-invocation: true
---

Implement the work described by the user in the spec or tickets.

Use /tdd where possible, at pre-agreed seams.

Run typechecking regularly, single test files regularly, and the full test suite once at the end.

If the spec carries requirement IDs, call the Skill tool with "requirement-traceability" and run its coverage check for the IDs this work covers; fix gaps before review.

Once done, use /code-review to review the work.

Commit your work to the current branch.
