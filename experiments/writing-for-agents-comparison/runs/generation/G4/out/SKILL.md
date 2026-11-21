---
name: meeting-notes-to-decision-brief
description: Turn meeting notes into a decision brief of decisions with evidence, action items, open questions and contradictions, and a handoff summary. Use when the user supplies meeting notes, minutes or a transcript and wants decisions, action items or a summary for someone who missed the meeting.
---

Turn the meeting notes the user supplies into a decision brief. The notes are the only source: every line of the brief traces to them, and anything the notes leave out stays visibly unresolved in the brief.

## Terms

When an item fits neither *decision* nor *proposal* cleanly, treat it as a proposal and say why under open questions.

- **Decision**: the notes show the group, or a person with stated authority, settling the matter: "agreed", "decided", "approved", "signed off", "we will", "going with", or an unchallenged "let's do X" that the meeting acted on. A decision that depends on a condition ("approved if legal clears it") is a **conditional decision**: record it with its condition.
- **Proposal**: an option raised but not settled: "suggested", "proposed", "could", "should we", "leaning towards", "X wants to", "tentatively", "to be confirmed", or any decision-like line that someone in the notes disputed and nobody resolved. Who raised a proposal does not make it a decision, however senior they are.
- **Action item**: a task the notes assign or someone takes on ("Priya to draft", "I'll check", "AI: Sam"). An action item can exist for an undecided matter ("Sam to price both options"); record it as an action item and keep the matter under proposals.
- **Contradiction**: two places in the notes that cannot both be true: a figure, date, owner or outcome stated two different ways, or a decision later reversed without the reversal being made explicit. If the notes explicitly reverse an earlier decision ("we revisited this and dropped X"), record only the later decision and cite both lines as evidence.
- **Not stated**: the literal value for any field the notes do not supply. Write it rather than inferring a value from context, seniority, who spoke last, or the usual way such work is done.

## Steps

1. **Check the input.** If the user has not supplied meeting notes, ask for them and stop. If the notes are present but some part is unreadable or cut off, work from what is readable and list the gap as an open question.

2. **Classify every item.** Read the notes start to finish and classify each substantive line using [Terms](#terms). Done when every line that states a choice, a task, a question or a disagreement has one classification; small talk and pure background need none.

3. **Write the brief** in the format below. Rules for each section sit with that section.

4. **Trace check.** Walk the finished brief line by line against the notes. Done when:
   - every decision has a quoted evidence line that appears in the notes word for word;
   - every action item's owner and deadline is either the notes' own wording or "Not stated";
   - no item classified as a proposal appears under Decisions;
   - the handoff summary contains no fact absent from the sections above it.
   Fix any failure, then deliver the brief. The task ends at delivery: do not send the brief, create tickets, or contact owners unless the user asks.

## Brief format

Use Markdown, these headings in this order, and "None recorded." under any heading with nothing to list. Reply with the brief in chat unless the user asks for a file.

```markdown
# Decision brief: <meeting title, or "Meeting" if not stated>
Date: <as stated, or Not stated>  ·  Attendees: <as stated, or Not stated>

## Decisions
1. **<the decision, one sentence>**
   Evidence: "<exact quote from the notes>" (<speaker, timestamp or section, if the notes give one>)
   Condition: <for a conditional decision only>

## Action items
| Action | Owner | Deadline | Source |
| --- | --- | --- | --- |
| <task> | <as stated, or Not stated> | <as stated, or Not stated> | "<short quote>" |

## Proposals not decided
- <proposal>: raised by <who, or Not stated>; status: <e.g. "no agreement recorded", "disputed by X">

## Open questions and contradictions
- **Question:** <question the notes raise or leave unanswered, including any missing owner or deadline that blocks work>
- **Contradiction:** "<quote A>" vs "<quote B>": <what conflicts>. Unresolved.

## Handoff summary
<3 to 5 sentences for someone who missed the meeting>
```

Section rules:

- **Decisions**: if several lines together show a decision was settled, quote each.
- **Action items**: copy owners and deadlines in the notes' own words. Keep relative deadlines relative ("by next Friday"), because converting them needs a meeting date the notes may not give. When an owner is a group ("the team", "design"), keep the group. A missing owner or deadline is "Not stated" in the table, and also gets a line under open questions if it blocks the work.
- **Proposals not decided**: every item classified as a proposal, so the reader sees what was discussed but not settled.
- **Open questions and contradictions**: questions the notes ask but do not answer, information the brief needed but the notes lack, and every contradiction with both quotes. Do not choose a winner in a contradiction.
- **Handoff summary**: what was decided, what happens next and who owns it, and what is still open. Draw only on the sections above; call a proposal a proposal.
