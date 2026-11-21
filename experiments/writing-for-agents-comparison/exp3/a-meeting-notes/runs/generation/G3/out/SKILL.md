---
name: meeting-notes-to-decision-brief
description: Turn meeting notes into a decision brief. Use when the user supplies meeting notes and wants the decisions, action items, open questions or a handoff drawn from them.
---

# Meeting notes to decision brief

The notes are the only source. Every line of the brief **traces** to a passage in the notes, and every owner, deadline or outcome the notes leave out is written as **unresolved**. Write _unresolved_ even when the answer seems obvious from context: the reader of the brief needs to see the gap, so a plausible fill-in is worse than an honest blank.

## Steps

1. **Tag.** Walk the notes passage by passage and tag each item of substance with one kind from [Kinds](#kinds): decision, proposal, action, question. Keep the passage's exact wording and its location (speaker, timestamp, heading or line, whatever the notes carry). Done when every passage that states an outcome, assigns work or asks something carries a tag.
2. **Reconcile.** Read the tags against each other in order, because later passages settle, reverse or contest earlier ones. Promote a proposal to a decision only where a later passage shows it settled. Record every pair of passages that cannot both hold as a contradiction. Done when each proposal is either promoted with its settling passage or left a proposal, and each conflict is recorded.
3. **Write** the brief in the [format](#brief-format).
4. **Check** the brief against the notes, item by item. Done when all of these hold:
   - every decision quotes a passage that shows it settled;
   - every action item's owner and deadline match the notes word for word, or read _unresolved_;
   - every proposal appears exactly once, as a decision or under "Proposed, not decided";
   - every item in the brief traces to a quoted or located passage, the handoff summary included.

## Kinds

- **Decision**: the notes show the group settled it: "agreed", "decided", "approved", "we're going with", a vote carried, or the person with authority signed off.
- **Proposal**: put forward but not settled: "suggest", "propose", "could", "should we", "let's look at", "tentatively", "pending approval", or one person's preference that nobody confirmed. Support from some attendees without a recorded settlement keeps it a proposal.
- **Contested decision**: a decision that a later passage challenges with no resolution in the notes. List it under Decisions marked _contested_, and record the challenge as a contradiction. A later passage that explicitly reverses it makes the reversal the decision; quote both passages as evidence.
- **Action**: work someone is to do. Copy the owner as written; a vague owner ("someone", "we", "the ops team") is copied as written and noted as unconfirmed. Copy the deadline as written ("Friday", "before beta", "next week"), leaving relative dates in their original wording.
- **Question**: asked and not answered in the notes, or a decision that lacks a detail it needs to be carried out.
- **Contradiction**: two passages that cannot both hold, such as two dates for one deadline, or a decision and a later statement that undercuts it.

## Brief format

```markdown
# Decision brief: <meeting name from the notes, or "unnamed meeting"> (<date from the notes, or "date unresolved">)

## Decisions
1. **<the decision, one sentence>** <"(contested, see C1)" when contested>
   Evidence: "<exact words from the notes>" (<location>)

## Action items
| # | Action | Owner | Deadline | Source |
|---|--------|-------|----------|--------|
| A1 | <task> | <as written, or unresolved> | <as written, or unresolved> | "<exact words>" (<location>) |

## Open questions and contradictions
### Open questions
- Q1. <question> (<location>)
### Proposed, not decided
- P1. <proposal>: "<exact words>" (<location>). Status: <what the notes say remains to settle it>
### Contradictions
- C1. "<passage one>" (<location>) vs "<passage two>" (<location>)

## Handoff summary
<Three to five sentences for someone who missed the meeting: what was decided, who does what next, and what remains open or contested. Drawn only from the sections above.>
```

A section with nothing in it says so in one line ("No decisions recorded in the notes."), so the reader can tell an empty section from a skipped one.
