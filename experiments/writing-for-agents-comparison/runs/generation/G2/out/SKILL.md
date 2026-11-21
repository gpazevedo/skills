---
name: meeting-notes-to-decision-brief
description: Turn meeting notes or a transcript into a decision brief. Use when the user supplies notes and asks what was decided, for the action items, or for a summary to hand off.
---

Produce a decision brief from the meeting notes the user supplies. The notes are the only source: every item in the brief traces to a passage in them, and anything the notes leave out stays marked as not stated. If the user has not supplied the notes, ask for them and stop.

## Terms

- **Decision**: the notes record that the group, or a person with the authority to decide, settled the matter. Signals: "agreed", "decided", "approved", "signed off", "we will go with", "final". A decision is settled now, with no condition still to be met.
- **Proposal**: anything put forward but not settled. Signals: "suggested", "proposed", "recommend", "should", "could", "let's consider", "leaning towards", "tentatively", "pending", and any agreement that depends on a condition not yet met ("agreed if legal signs off"). When the wording does not show the matter was settled, it is a proposal.
- **Action item**: a task the notes record as to be done: assigned, taken on, or listed as an action ("Sam to draft the spec", "I'll send the invite", "someone needs to email the beta users"). It stays an action item when nobody owns it. A task only floated as an option ("we could email them") is a proposal.
- **Evidence**: a short verbatim quote from the notes plus a locator the reader can search for: timestamp, speaker, section heading, or line number, whichever the notes have.
- **Contradiction**: two passages in the notes that cannot both hold, such as two deadlines for one task, or a decision that a later passage disputes.
- **Not stated**: the literal value for any field the notes do not supply. Use it instead of inferring an owner from who spoke most, a deadline from the meeting cadence, or a date from a weekday.

## Steps

1. **Read the notes through once** before writing anything, so a later reversal or correction is known before you classify an earlier passage.
2. **Classify.** Go through the notes in order and sort every passage that settles, proposes, assigns, questions, or conflicts into the brief's sections below. When the notes show a later passage explicitly reversing an earlier one ("changed our minds", "scratch that"), record the final position and quote both passages in its evidence. When two passages conflict and the notes do not say which holds, record neither as a decision: list the conflict under contradictions, quoting both.
3. **Fill the action items.** Copy the owner and deadline exactly as written ("end of next week", "Priya or Tom"). Keep relative dates and shared ownership as written rather than resolving them. Where either is missing, write `Not stated` and add a line under open questions naming the item and the missing field. Where the notes give conflicting values, write `Conflicting` and list the conflict under contradictions.
4. **Write the handoff summary last**, from the sections already written: three to five sentences for someone who missed the meeting, covering what was decided, who does what next, and what is blocked or unresolved. It adds no claim that is not in the sections below it.
5. **Check, then stop.** Make one pass back through the notes against the brief. The brief is done when:
   - every decision, proposal, action item, question, and contradiction in the notes appears in the brief;
   - every decision and proposal has evidence, and no proposal is listed as a decision;
   - every action item has an owner and a deadline field, each copied from the notes, `Not stated`, or `Conflicting`;
   - every statement in the brief traces to a passage in the notes.

   Fix what fails, then deliver the brief in the reply, or to a file if the user asked for one.

## Brief format

Use these headings in this order. Write `None recorded in the notes.` under any section with no items, so the reader can tell empty from forgotten.

```markdown
# Decision brief: <meeting name or topic, as the notes give it> (<date, or Not stated>)

## Handoff summary
<three to five sentences>

## Decisions
1. <decision, one sentence>
   Evidence: "<verbatim quote>" (<locator>)

## Action items
| Task | Owner | Deadline | Evidence |
| --- | --- | --- | --- |
| <task> | <as written, Not stated, or Conflicting> | <as written, Not stated, or Conflicting> | "<quote>" (<locator>) |

## Proposals not decided
1. <proposal, and its condition or status if the notes give one>
   Evidence: "<verbatim quote>" (<locator>)

## Open questions and contradictions
- Question: <question raised and not answered in the notes, or missing field on an action item>
- Contradiction: <what conflicts>. "<quote A>" (<locator>) vs "<quote B>" (<locator>)
```
