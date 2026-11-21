---
name: meeting-notes-to-decision-brief
description: Decision brief from meeting notes or a transcript. Use when the user supplies notes and asks for decisions, action items, or a handoff summary.
---

Turn the user's meeting notes into a decision brief. The brief carries only what is **on the record**: what the notes themselves say. Every field holds either something on the record or the marker `not stated`. A gap marked `not stated` is a correct answer; it tells the next reader exactly what to chase.

## Steps

1. **Harvest.** Read the notes end to end and pull out every candidate item with its **evidence**: the shortest verbatim quote that carries it, plus its location (speaker, timestamp, line or heading) when the notes give one. Candidates are anything that commits, suggests, asks, assigns or conflicts. Done when every line of the notes has either fed a candidate or is pure discussion with no commitment, suggestion, assignment or question in it.
2. **Classify** each candidate as a decision, proposal, action item, open question or contradiction, using the rules below. One statement can yield two items (a decision and the action item it assigns). Done when every candidate has a class.
3. **Fill** each item's fields from the record, copying owners, dates and figures in the notes' own words. Done when every field holds a quote-backed value or `not stated`.
4. **Audit.** Re-read the notes against the draft. Done when every field traces to a quote on the record and every commitment in the notes appears in the brief.
5. **Summarise** last, from the finished sections only (format below).

## Classification rules

**Decision**: the notes record the outcome as settled: the group agreed, someone with the authority ruled, or the wording is final ("agreed", "decided", "approved", "going with", "signed off"), and no objection stays open.

**Proposal**: anything short of settled. A suggestion or recommendation; a tentative lean ("probably", "leaning towards", "let's consider"); a conditional outcome ("if legal signs off", "pending budget"); one person's preference the notes do not show others accepting; an outcome with an objection still open. When the record is ambiguous, the item is a proposal. Record its condition or the open objection, since that is what turns it into a decision later.

**Reversal**: when the notes record an explicit change of mind ("scratch that, we'll keep the old vendor"), the final state is the decision, and its evidence quotes both statements.

**Action item**: a task the notes assign or someone volunteers for. Owner and deadline come from the record:
- "I'll do it" with a known speaker: the speaker is the owner.
- A group or role ("marketing", "the team"): copy it as written.
- A relative deadline ("by Friday", "next sprint"): copy it as written.
- No owner or deadline in the notes: `not stated`.

A decision that clearly needs follow-up work but has no assigned task stays a decision; the missing assignment becomes an open question ("Who owns migrating to Postgres (D2)?").

**Open question**: a question raised and left unanswered, a proposal awaiting someone's call, or a gap that blocks the handoff (a decision with no owner, an action item with no deadline that the notes treat as urgent).

**Contradiction**: two statements on the record that cannot both hold, with nothing later in the notes settling them: two different deadlines for one task, two owners for one item, a decision that conflicts with another decision. Quote both sides and leave the conflict standing.

## Brief format

Use this layout. Number items (D1, P1, A1) so sections can refer to each other. Keep every section heading; an empty section reads "None on the record."

```markdown
# Decision brief: <meeting title, or "not stated">

**Date:** <as written, or not stated>  **Attendees:** <as listed, or not stated>

## Handoff summary
<3 to 5 sentences for someone who missed the meeting: what was decided, what happens next and who drives it, what is still blocking. Refers to items by number.>

## Decisions
**D1. <the decision, one sentence>**
- Evidence: "<verbatim quote>" (<location>)
- Decided by: <as stated, or not stated>

## Action items
| # | Action | Owner | Deadline | Evidence |
|---|--------|-------|----------|----------|
| A1 | <task> | <as stated> | <as stated> | "<quote>" (<location>) |

## Proposals (not decided)
**P1. <the proposal, one sentence>**
- Raised by: <as stated, or not stated>
- Status: <condition, open objection, or "no decision recorded">
- Evidence: "<verbatim quote>" (<location>)

## Open questions and contradictions
- **Q1.** <question> (<location or related item>)
- **C1.** <subject>: "<quote one>" (<location>) vs "<quote two>" (<location>)
```
