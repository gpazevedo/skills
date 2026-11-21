---
name: meeting-notes-to-decision-brief
description: Decision brief from meeting notes. Use when the user supplies meeting notes, minutes or a transcript and wants the decisions, action items, open questions or a handoff summary pulled out.
---

Turn the user's meeting notes into a **decision brief**. The notes are the only source: every line of the brief traces back to them, and anything the notes leave out stays **unresolved** in the brief.

## Classifying statements

Every substantive statement in the notes is one of four kinds:

- **Decision**: the notes record the group settling something. Look for agreement or authority stated in the notes: "agreed", "decided", "approved", "we'll go with", "signed off", a vote result, or the person with authority confirming.
- **Proposal**: something put forward without recorded agreement: "suggested", "proposed", "could", "should we", "leaning towards", "X wants to", a plan one person describes. A proposal stays a proposal however sensible or likely it sounds.
- **Action**: a task someone is to do.
- **Question**: something the notes leave open, explicitly ("TBD", "need to check", "?") or by being cut off.

When a statement could be read as a decision or a proposal, classify it as a proposal. Promotion to decision needs words of agreement in the notes.

**Evidence** is a short verbatim quote from the notes, with its locator when the notes have one (speaker, timestamp, heading, item number). Quote; paraphrase is not evidence.

## Steps

1. **Read the whole of the notes**, including asides, parentheticals and anything appended after the main list. Note the meeting date, attendees and title if stated. Done when you have reached the last line.

2. **Classify every substantive statement** using the four kinds above. Done when each statement that settles, proposes, assigns or questions something has a kind.

3. **Find contradictions**: two statements in the notes that cannot both hold (a decision later reversed, two different deadlines for one task, two owners named for one task, a figure stated two ways). Record both sides with their evidence. A later reversal that the notes mark as final ("in the end we agreed...") is a decision; list the earlier position under contradictions too, so the reader sees the change.

4. **Fill the action items** from the actions:
   - Owner and deadline are copied as written: "Priya", "by Friday", "end of Q3". Keep relative deadlines in their original words.
   - Where the notes give no owner or no deadline, write `unstated`. A guess is a wrong answer here; `unstated` is the right one.
   - An action with no named person as owner ("we", "the team", "someone") keeps that wording and also gets an open question asking who owns it.
   - An action caught in a contradiction lists every stated owner or deadline, each as written, followed by "see Contradictions".

5. **Write the brief** in the format below.

6. **Check the brief against the notes**. Done when all of these hold:
   - Every substantive statement from step 2 appears in the section for its kind: Decisions, Proposals, Action items or Open questions (a decision may also generate an action; a contradiction also appears under Contradictions).
   - Every decision carries evidence that shows agreement, not just discussion.
   - Every owner, deadline, name, number and date in the brief appears in the notes.
   - Every `unstated` field has a matching open question.

## Brief format

```markdown
# Decision brief: <meeting title, or "Meeting" if none>
<date as written, or "Date: unstated"> · Attendees: <as listed, or "unstated">

## Decisions
1. <decision, one sentence>
   Evidence: "<quote>" (<locator>)

## Proposals (no agreement recorded)
1. <proposal, one sentence, naming who proposed it if stated>
   Evidence: "<quote>" (<locator>)

## Action items
| # | Action | Owner | Deadline | Evidence |
|---|--------|-------|----------|----------|
| 1 | <task> | <as written or `unstated`> | <as written or `unstated`> | "<quote>" |

## Open questions
- <question>. Source: "<quote>", or the gap that raises it (e.g. "Action 3 has no owner").

## Contradictions
- <what conflicts>. "<quote A>" (<locator>) vs "<quote B>" (<locator>). Status: <resolved in notes as ..., or unresolved>.

## Handoff summary
<3 to 5 sentences for someone who missed the meeting: what was decided, who is doing what next, and what is still open or only proposed. Built only from the sections above.>
```

Keep every section heading. An empty section reads `None recorded in the notes.`, so the reader can tell "nothing found" from "section forgotten".
