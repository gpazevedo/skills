---
name: meeting-notes-to-decision-brief
description: Turns meeting notes into a decision brief: decisions with evidence, action items, open questions, handoff summary. Use when the user supplies meeting notes, minutes or a transcript and wants decisions, action items or a summary extracted.
---

Turn the user's meeting notes into a **decision brief**. The notes are the only source: every line of the brief traces to them, and anything they leave out stays **unresolved** in the brief, written as missing.

## Classifying statements

Sort every substantive statement in the notes into one of these. The brief is only as good as this sort.

- **Decision**: the notes record agreement or a final call. Markers: "agreed", "decided", "approved", "we'll go with", "confirmed", "signed off", a vote result, or a named decision-maker settling it. A decision needs **evidence**: the quoted words from the notes that show it was settled.
- **Proposal**: an idea put forward and not recorded as settled. Markers: "suggested", "proposed", "could", "should we", "what if", "recommends", "leaning towards", "to be confirmed", "pending approval". A proposal that later gets a decision marker becomes a decision; quote the later line as the evidence.
- **Action item**: a task someone is to do. Keep the owner and deadline exactly as the notes state them, including vague ones ("next week", "Sam's team").
- **Open question**: anything raised and not answered, any proposal never settled, and any decision missing a detail it needs to act on (who, when, how much, which option).
- **Contradiction**: two parts of the notes that cannot both be true (a decision later reversed without comment, two different deadlines for one task, two people credited as owner, figures that disagree). Quote both sides.

A call that still waits on someone's approval ("we'll go with April 10, Priya to confirm with exec") is a proposal; name the approver in an open question. When a statement's status is otherwise ambiguous, classify it as a proposal and add an open question asking whether it was decided. Promoting a proposal to a decision is the one error this brief exists to prevent.

## Steps

1. **Read the notes end to end** before writing anything, since later lines often settle, reverse or contradict earlier ones. Done when you have read the last line.
2. **Classify** every substantive statement using the categories above. Done when every statement that records an idea, a call, a task or a question sits in exactly one category, and every decision has a quote as evidence.
3. **Check the gaps.** For each action item, record a missing owner as `Owner: not stated` and a missing deadline as `Deadline: not stated`. For each decision, ask what someone would need to act on it; add each missing piece as an open question. Done when every action item has both fields filled (with the stated value or `not stated`) and every decision has been checked.
4. **Write the brief** in the format below. Done when every classified item appears in its section, and every name, date and figure in the brief appears in the notes.
5. **Write the handoff summary last**, from the finished sections. Done when it is at most five sentences, covers only what the sections already contain, and a reader who missed the meeting knows what was settled, what happens next and what is still unresolved.

## Brief format

```markdown
# Decision brief: <meeting title or topic as given in the notes>
<date and attendees, if the notes state them; otherwise "Date: not stated">

## Handoff summary
<at most five sentences>

## Decisions
1. <decision, stated plainly>
   - Evidence: "<quote from the notes>" (<speaker or location, if given>)

## Action items
| Action | Owner | Deadline | Source |
|---|---|---|---|
| <task> | <as stated, or "not stated"> | <as stated, or "not stated"> | "<short quote>" |

## Proposals not decided
- <proposal> (raised by <name, if stated>)

## Open questions and contradictions
- <open question>
- Contradiction: "<quote A>" vs "<quote B>"
```

Leave a section in place with the line `None recorded in the notes.` when it has no items, so the reader can tell empty from forgotten. Write vague owners and deadlines verbatim and add an open question when the vagueness blocks the work.
