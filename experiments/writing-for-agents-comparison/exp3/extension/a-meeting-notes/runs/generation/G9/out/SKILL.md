---
name: meeting-notes-to-decision-brief
description: Turns meeting notes, minutes or a transcript into a decision brief (decisions with evidence, action items, open questions, handoff summary). Use when the user supplies notes from a meeting and wants what was decided, who does what, or a handoff for someone who missed it.
---

Turn the user's meeting notes into a **decision brief**. The notes are the only source: every line of the brief traces to them, and anything the notes leave out stays visibly **unstated** in the brief.

## Core distinction: decided vs proposed

A **decision** is an item the notes record as closed: agreed, approved, signed off, "we're going with", "final", or an owner accepting it on behalf of the group. A **proposal** is an item the notes record as still open: suggested, floated, recommended, "should we", "let's look at", one person's preference, or agreement "in principle" pending something.

Classify by what the notes record, not by how sensible the idea sounds. When the wording is ambiguous, it is a proposal, and it goes under open questions with the wording quoted. A later line that explicitly reverses an earlier one makes the later line the decision; note the reversal. Two lines that conflict without either one closing the matter are a **contradiction**, even when one of them sounded final ("Dec 1 confirmed" then, later, "launch is still Nov 20"): the item leaves Decisions and goes under contradictions with both quotes.

## Steps

1. **Read the whole set of notes before writing.** Note how lines can be located (timestamps, speaker names, headings, or bullet order) so evidence can point back to them. Done when you have read to the last line.

2. **Sort every substantive statement** into one of: decision, proposal, action item, question, contradiction, or background. Done when no substantive statement is left unsorted. An item can land in two places (a decision that creates an action item).

3. **Write the decisions.** For each: the decision in one sentence, then the **evidence**: a short verbatim quote from the notes with its locator. Done when every decision carries a quote; an item you cannot quote moves to open questions.

4. **Write the action items.** Keep each owner and deadline in the notes' own words ("by Friday" stays "by Friday"; "Sam's team" stays "Sam's team"). Where the notes give no owner or no deadline, write `unstated`. Where an action depends on something still a proposal, say so. Done when every action has an owner field and a deadline field, filled from the notes or marked `unstated`.

5. **Write open questions and contradictions.** Include questions raised but not answered, proposals that never closed, items the notes leave incomplete (an action with an `unstated` owner, a decision missing a detail it needs), and every contradiction with both conflicting quotes side by side. Leave contradictions unresolved: report both sides and who could settle it, if the notes say. Done when every proposal from step 2 and every `unstated` field appears here or is covered by an entry here.

6. **Write the handoff summary last**, from the sections above only: three to five sentences for someone who missed the meeting, covering what was decided, what happens next and by whom, and the biggest unresolved item.

7. **Check the brief against the notes.** Every name, date, number and owner in the brief appears in the notes; every decision has a quote; nothing in the brief is a proposal promoted to a decision. Fix anything that fails, then deliver.

## Brief format

```markdown
# Decision brief: <meeting title or topic, as given in the notes>
<date and attendees if the notes give them; otherwise omit this line>

## Handoff summary
<3 to 5 sentences>

## Decisions
1. <decision>
   Evidence: "<verbatim quote>" (<locator>)

## Action items
| Action | Owner | Deadline | Notes |
|---|---|---|---|
| <action> | <as written, or unstated> | <as written, or unstated> | <dependency or source locator> |

## Open questions and contradictions
- **Open:** <question or unclosed proposal> ("<quote>", <locator>)
- **Contradiction:** "<quote A>" (<locator>) vs "<quote B>" (<locator>). <who could resolve it, if stated>
```

Write "None recorded in the notes." under any section that is empty. Put the handoff summary first in the delivered brief even though you write it last.
