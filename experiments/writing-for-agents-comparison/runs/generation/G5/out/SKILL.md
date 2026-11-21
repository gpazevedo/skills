---
name: meeting-notes-to-decision-brief
description: Turns meeting notes into a decision brief of decisions with evidence, action items, open questions and a handoff summary. Use when the user supplies meeting notes or a transcript and wants the decisions, action items or a handoff extracted.
---

The notes are the only source. Every line of the brief traces to something the notes say; where the notes are silent, the brief says **unresolved**.

## Steps

1. **Inventory the notes.** Read them end to end and tag every substantive statement as one of: _decision_, _proposal_, _action item_, _question_, or context. Use the rules under [Decision or proposal](#decision-or-proposal). Done when every statement that commits, suggests, assigns or asks something carries a tag.
2. **Find contradictions.** Compare the tagged statements for conflicts: two dates, owners, numbers or outcomes for the same thing, or a decision later reversed. Done when every pair that cannot both be true is listed with both sides.
3. **Write the brief** in the [template](#brief-template) below. Done when every decision, proposal, action item and question from step 1, and every contradiction from step 2, has its entry in the brief.
4. **Audit against the notes.** For each decision, confirm its evidence quote appears in the notes and actually records agreement. For each action item, confirm owner and deadline match the notes word for word, or read **unresolved**. Move any decision that fails to Proposals. Done when every entry passes.

## Decision or proposal

A **decision** is an outcome the notes record as settled: "agreed", "decided", "approved", "signed off", "we're going with", "final", or a minutes entry headed as an outcome or resolution.

A **proposal** is anything still open to the group: "suggested", "proposed", "floated", "what if we", "should we", "leaning towards", "probably", one person's stated preference with no recorded agreement, or an outcome that waits on someone's approval.

When the wording sits between the two, tag it a proposal and add an open question asking whether it was decided. A reversed decision keeps only the latest outcome as the decision, and the reversal goes under Contradictions.

## Evidence

Evidence is a short verbatim quote from the notes, with its location when the notes have one (speaker, timestamp, agenda item or section heading). Quote the words that carry the agreement, so a reader can check the classification without opening the notes.

## Action items

Copy owner and deadline exactly as the notes state them: "Priya", "the design team", "by Friday", "before launch". Write **unresolved** for any owner or deadline the notes leave out, and list it again under Open questions. An action the notes assign to "we" or "someone" has an **unresolved** owner.

## Brief template

```markdown
# Decision brief: <meeting name or topic, as the notes give it>
<date and attendees as the notes state them, or unresolved>

## Decisions
1. <decision>
   Evidence: "<quote>" (<location>)

## Proposals (not decided)
- <proposal>, raised by <name or unresolved>. Evidence: "<quote>"

## Action items
| Action | Owner | Deadline | Evidence |
|---|---|---|---|

## Open questions
- <question the notes raise, or a gap: unresolved owner, deadline, or decision status>

## Contradictions
- <topic>: "<quote A>" (<location>) vs "<quote B>" (<location>). <Latest outcome, if the notes record an explicit reversal; otherwise unresolved.>

## Handoff summary
<3 to 5 sentences for someone who missed the meeting: what was decided, who does what next, and what is blocked or unresolved. Drawn only from the sections above.>
```

Write "None recorded." under any section the notes give nothing for.
