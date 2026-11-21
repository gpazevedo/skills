---
name: meeting-notes-to-decision-brief
description: Turn meeting notes into a decision brief (decisions with evidence, action items, open questions, handoff summary). Use when the user supplies meeting notes, minutes or a transcript and wants the outcomes extracted or handed off.
---

Turn the user's meeting notes into a **decision brief**. The notes are the only source. Every entry in the brief **traces** to a quoted line of the notes, and whatever the notes leave out stays **unresolved**: written as `Not stated` or listed as an open question.

## 1. Tag every line

Read the notes line by line and tag each statement that bears on an outcome:

- **Decision**: the notes record agreement or a final call. Signals: "agreed", "decided", "approved", "confirmed", "we will", "going with", a vote that passed, sign-off by the person the notes show holding the call.
- **Proposal**: a suggestion, option, recommendation or preference with no recorded agreement. Signals: "suggest", "propose", "could", "should we", "leaning towards", "X prefers", "to be confirmed", a call explicitly deferred. Support from some attendees leaves it a proposal; it becomes a decision only when the notes record the agreement.
- **Action**: a task someone is to carry out.
- **Question**: something raised and left unanswered.
- **Contradiction**: two statements that cannot both hold (different dates, figures, owners or outcomes for the same thing).

Tie-breakers:

- Between proposal and decision, tag it **proposal** and list it under open questions as "Decided or proposed?".
- An explicit revision ("changed to", "reversing the earlier call") is one decision: the later statement stands, and its evidence quotes both lines. Two conflicting statements with no recorded revision are a contradiction, and neither becomes a decision.

Done when every line is tagged or set aside as bearing on no outcome (greetings, attendance, small talk).

## 2. Fill the brief

Use this structure, in this order:

```markdown
# Decision brief: <meeting name as stated, or "Not stated">
Date: <as stated, or "Not stated">  |  Attendees: <as stated, or "Not stated">

## Decisions
1. <decision, one sentence>
   Evidence: "<short verbatim quote>" (<speaker, timestamp or section, as the notes give it>)

## Action items
| Action | Owner | Deadline | Source |
|---|---|---|---|
| <task> | <verbatim, or Not stated> | <verbatim, or Not stated> | "<short quote>" |

## Open questions and contradictions
- <unanswered question, undecided proposal, "Decided or proposed?" item, or contradiction>
  Source: "<quote>" (for a contradiction, quote both sides)

## Handoff summary
<3 to 5 sentences>
```

Section rules (a section with no entries reads `None recorded.`):

- **Decisions**: one entry per decision; the quote must itself show the agreement, not only the topic.
- **Action items**: copy owners and deadlines **verbatim**, so "next Friday" stays "next Friday" and "Sam's team" stays "Sam's team". Add a calendar date in brackets only when the notes give a full meeting date (day, month, year) that pins it down.
- **Open questions and contradictions**: every proposal that never became a decision lands here, with who proposed it if the notes say.
- **Handoff summary**: write it last, from the sections above only, for a reader who missed the meeting: what was decided, who does what next, and what is still unresolved.

## 3. Check before returning

Walk the finished brief against the notes:

- Every decision's quote records agreement; any that only records a suggestion moves to open questions.
- Every owner and deadline matches the notes word for word; every `Not stated` is genuinely absent from the notes.
- Every claim in the handoff summary appears in an earlier section.

Done when all three hold for every entry. Return the brief as the reply, or write it to a file if the user asked for one.
