---
name: meeting-notes-to-decision-brief
description: Decision brief from meeting notes, covering decisions with evidence, action items, open questions and a handoff summary. Use when the user supplies meeting notes or a transcript and wants its outcomes, actions or a handoff.
---

Turn the user's meeting notes into a decision brief. The notes are the only source: every entry in the brief traces to a verbatim quote from them, and whatever the notes leave out is written as `Not stated`.

## Classifying statements

Each statement that carries an outcome, a task or a question belongs to one category.

- **Decision**: the notes record the group committing to an outcome through a **commitment signal**: "agreed", "decided", "approved", "we'll go with", or a named person signing off. The commitment signal must be in the notes.
- **Proposal**: an option put forward with no commitment signal: "suggested", "proposed", "should we", "could", "I'd prefer", a recommendation. A commitment that waits on an unmet condition ("agreed, pending legal sign-off") is also a proposal; record the condition. Record the proposer as written, or `Not stated`.
- **Action item**: a task someone is to do. Copy the owner and deadline exactly as written ("next Friday" stays "next Friday"); where the notes give none, write `Not stated`.
- **Open question**: anything raised and left unresolved: an unanswered question, a topic deferred ("take offline", "revisit next week"), a choice blocked on missing information, and every action item whose owner is `Not stated`.
- **Contradiction**: two statements in the notes that cannot both hold, such as two deadlines for one task, two owners, or a decision followed by an objection that nobody resolves. Quote both sides. A later explicit decision that replaces an earlier one is a **revision**, not a contradiction: record the later one as the decision and say what it replaced.

When the commitment signal is ambiguous, classify the statement as a proposal and add an open question asking whether it was decided.

**Evidence** is the shortest verbatim quote that shows the classification, followed by the speaker or timestamp when the notes carry one.

## Steps

1. **Build a ledger.** Read the notes from start to finish and list, in a working ledger kept out of the brief, every statement that is a decision, proposal, action item, open question or contradiction, each with its evidence. Done when you have reached the end of the notes and every statement carrying an outcome, a task or a question has a ledger entry.
2. **Reconcile.** Group ledger entries on the same topic. Apply the revision and contradiction rules, and demote every ambiguous decision to a proposal with its open question. Done when no topic holds two live decisions.
3. **Write the brief** in the template below. A section with no entries reads "None recorded in the notes."
4. **Check the brief against the notes**, fix what fails, and check again. Done when all of these hold:
   - every decision's evidence contains a commitment signal;
   - every owner, deadline and proposer appears word for word in the notes or reads `Not stated`;
   - every open question and contradiction from the ledger appears in the brief;
   - every fact in the handoff summary appears in a section above it.

## Template

```markdown
# Decision brief: <meeting name as written in the notes, or Not stated>

Date: <as written in the notes, or Not stated>

## Decisions

| Decision | Evidence |
| --- | --- |

## Proposals (not decided)

| Proposal | Proposed by | Condition or status | Evidence |
| --- | --- | --- | --- |

## Action items

| Action | Owner | Deadline | Evidence |
| --- | --- | --- | --- |

## Open questions and contradictions

### Open questions
- <question>: <why it is open, with evidence>

### Contradictions
- <topic>: "<quote A>" vs "<quote B>"

## Handoff summary

<Three to five sentences for someone who missed the meeting: what was decided, who does what next and by when, and what is still unresolved.>
```
