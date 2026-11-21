---
name: meeting-notes-to-decision-brief
description: Turn meeting notes into a decision brief: decisions with evidence, action items, open questions and contradictions, and a handoff summary. Use when the user supplies meeting notes or a transcript and asks what was decided, who owes what, or for a brief or handoff.
---

Turn the meeting notes the user supplies into a decision brief. The notes are the only source: every entry in the brief traces back to something written in them, and anything the notes leave out stays visibly missing.

If the user has not supplied notes, ask for them and stop.

## Classifying statements

Read the notes once through before writing, so a later reversal or a later owner assignment is not missed. Then sort each statement that bears on what happens next into one of these:

- **Decision**: the notes record it as settled. Signals: "decided", "agreed", "approved", "signed off", "we will", "going with", a recorded vote that passed. A decision with a stated condition ("approved if legal clears it") stays a decision; write the condition with it, and list the unmet condition as an open question.
- **Proposal**: put forward but not recorded as settled. Signals: "suggested", "proposed", "should we", "we could", "leaning towards", "probably", "to be discussed", or a suggestion with no recorded response. When a statement could be either, it is a proposal: a proposal wrongly promoted to a decision sends the reader to act on something nobody agreed. List proposals under open questions as "Proposed, not decided".
- **Action item**: someone is to do something. It can come from a decision or stand alone.
- **Contradiction**: two statements in the notes conflict and the notes do not settle which holds (two different dates for the same launch, an item marked both approved and pending). An explicit reversal ("we changed our minds on X: now Y") is not a contradiction: record the final position as the decision and cite both statements as evidence.

## Missing information

Write what the notes say, in their words, and mark gaps as **not stated**. Do not fill a gap from context, job titles, likely intent, or the calendar:

- No owner named: `Owner: not stated`. A group owner ("the team", "eng") is recorded as written.
- No deadline: `Deadline: not stated`. Keep relative deadlines verbatim ("by Friday", "next sprint"); do not convert them to dates.
- A name, figure, or reference the notes leave unclear (initials that match two people, "the usual vendor"): record it as written and add it to open questions.

A gap is recorded once, at the item it belongs to. Add it to open questions only when it blocks a decision or the whole brief, not for every missing owner.

## Writing the brief

Use this structure. Keep every heading; a section with nothing in it says "None recorded in the notes."

```markdown
# Decision brief: <meeting title or topic as given in the notes>
Date: <as stated, or "not stated">  Attendees: <as stated, or "not stated">

## Decisions
1. <decision, one sentence>. <condition, if any>
   Evidence: "<short quote from the notes>" (<location: heading, timestamp, or speaker>)

## Action items
| Action | Owner | Deadline | From decision |
| --- | --- | --- | --- |
| <action> | <name or "not stated"> | <as written or "not stated"> | <decision number or "none"> |

## Open questions and contradictions
- Open: <question the notes raise and do not answer>
- Proposed, not decided: <proposal> ("<short quote>")
- Contradiction: "<statement A>" vs "<statement B>". Unresolved in the notes.

## Handoff summary
<3 to 5 sentences for someone who missed the meeting: what was decided, what is now in motion and with whom, and what is still open.>
```

Evidence is a short verbatim quote that shows the decision was made, not just discussed. If the only support is a paraphrase-level mention, that is a sign the item is a proposal.

The handoff summary restates the sections above; it adds no fact, owner, or date that is not already in the brief.

Return the brief in the reply. Write it to a file only when the user asks for one.

## Done when

- Every decision has an evidence quote, and every proposal in the notes is under open questions rather than decisions.
- Every action item has an owner and a deadline field, each either as written in the notes or "not stated".
- Every contradiction found in the read-through is listed, with both statements quoted.
- Every heading is present, and the handoff summary contains nothing absent from the sections above it.
