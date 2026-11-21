---
name: meeting-notes-to-decision-brief
description: Turn meeting notes into a decision brief. Use when the user supplies meeting notes, minutes or a transcript and wants decisions, action items, open questions or a handoff summary.
---

Produce a decision brief from the notes the user supplied. The notes are the only source: every line of the brief traces to a quote or a clear paraphrase of them. Anything the notes leave out stays a **gap**, named as such.

## Steps

1. **Sweep the notes.** Read them end to end and tag each statement as one of: decision, proposal, action, question, contradiction, context. Done when every statement carries a tag or is judged context.
2. **Test each candidate decision.** A **decision** has explicit commitment in the notes ("agreed", "approved", "we will", no recorded dissent). A **proposal** is anything suggested, favoured, or "leaning towards" without that commitment. When commitment is ambiguous, file it as a proposal and say what confirmation is missing.
3. **Collect actions.** Done when every commitment to do something is listed, with owner and deadline copied exactly as stated. A missing owner or deadline is written `owner: unassigned` or `deadline: not stated`, never inferred from context or role. Relative dates ("next Friday") stay as written, with the meeting date beside them only if the notes give it.
4. **Hunt contradictions.** Compare decisions, actions, figures, names and dates across the whole notes. Done when every pair of conflicting statements is listed with both quotes, unresolved: the brief reports the conflict and leaves the choice to the reader.
5. **Write the brief** in the format below, then check it against the notes: every decision has a quote, every gap is marked, no owner, date or figure appears that the notes lack.

## Format

```
# Decision brief: <meeting title or topic>
Date / attendees: <as stated, else "not stated">

## Decisions
- <decision>. Evidence: "<quote>" (<speaker or location in notes, if given>)

## Proposals not yet decided
- <proposal>, raised by <who, if stated>. Missing: <what would make it a decision>

## Action items
| Action | Owner | Deadline | Source |

## Open questions and contradictions
- Question: <what is unanswered>
- Contradiction: "<quote A>" vs "<quote B>". Unresolved.

## Handoff summary
<five sentences or fewer: what was decided, what is pending, who acts next, what blocks progress>
```

Keep a section with no content and write `None found in the notes.` beneath its heading, so the reader sees it was checked.

## Gaps

A **gap** is information the brief needs and the notes lack: an owner, a deadline, a rationale, a number, an attendee, a decision outcome. Write `not stated` in place, and list gaps that block action under Open questions. When the user is available, offer to fill them; the brief itself waits for their answer.

The handoff summary repeats nothing beyond the sections above: it compresses them for a reader who stops there.
