---
name: meeting-notes-to-decision-brief
description: Turns meeting notes into a decision brief. Use when the user supplies meeting notes, minutes or a transcript and wants decisions, actions or a summary.
---

Turn the supplied notes into a **decision brief**. The notes are the only source of truth: every line of the brief traces to a quote or passage in them.

## Steps

1. **Ledger.** Read the notes end to end and list every statement that proposes, decides, assigns, asks or conflicts. Done when every passage of the notes is either in the ledger or judged to be discussion with none of those.
2. **Classify** each ledger entry:
   - **Decision**: the notes show commitment ("agreed", "approved", "we will", no dissent recorded). Quote that wording as evidence.
   - **Proposal**: suggested, floated, or "we should" with no recorded commitment. Proposals stay proposals, and go under Open questions.
   - **Action item**: a task someone is to do. Copy the stated owner and deadline verbatim; where the notes give none, write `owner: not stated` or `deadline: not stated`.
   - **Open question**: asked and unanswered, deferred, or missing a needed input (who, when, how much, which option).
   - **Contradiction**: two places in the notes that cannot both hold (different dates, owners, figures, outcomes). Quote both and leave unresolved.
3. **Write** the brief in the format below. Done when each ledger entry appears exactly once, and each decision carries a quote.
4. **Audit.** Re-read the brief against the notes. Done when no owner, deadline, number or name appears that the notes do not state, and every ambiguous "decision" has been checked against Decision versus Proposal.

Missing information stays **unresolved**: name the gap, never fill it with an inference. A vague phrase ("soon", "the team") is copied as written.

## Format

```
# Decision brief: <meeting title or date, as stated; else "untitled">

## Decisions
- <decision>. Evidence: "<quote>"

## Action items
| Action | Owner | Deadline | Source |

## Open questions and contradictions
- Proposal, not decided: <proposal>. Evidence: "<quote>". Missing: <what>
- Question: <question>
- Contradiction: "<quote A>" vs "<quote B>"

## Handoff summary
<3 to 5 sentences: what was decided, what is owed and by whom, what is still unresolved.>
```

Keep an empty section as `None found in the notes.`
