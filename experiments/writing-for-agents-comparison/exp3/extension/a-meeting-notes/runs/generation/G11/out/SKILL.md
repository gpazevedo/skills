---
name: meeting-notes-to-decision-brief
description: Decision brief from meeting notes, minutes or a transcript the user supplies. Use when the user wants the decisions, action items, open questions or a handoff summary pulled out of a meeting record.
---

Turn the user's meeting notes into a **decision brief**. The notes are the only source: every entry in the brief traces to a line in them, and anything the notes leave out stays **unresolved**, written as the marker `Not stated`.

## Steps

1. **Read the whole record before writing.** Later lines often settle, reverse or contradict earlier ones, so classify nothing until you have seen the end. Note the meeting date if the notes give one.

2. **Sort every substantive line** into one bucket: decision, proposal, action item, question, or context. Done when each line that carries content sits in a bucket; greetings and chatter can go unsorted.

3. **Separate decisions from proposals** with the test under [Decision or proposal](#decision-or-proposal). For each decision, quote the line or lines that show assent as its **evidence**. Done when every decision carries a verbatim quote and every proposal that never reached assent sits in Open questions.

4. **Write the action items.** Copy owner and deadline in the notes' own words ("by Friday", "next sprint"). An owner is a named person or team; "someone" or "we should" names no one. A missing owner or deadline is `Not stated`, and the gap also goes into Open questions. Done when every action from step 2 appears once, with all three fields filled.

5. **Write the open questions and contradictions**: questions raised and left unanswered, proposals left open, missing owners or deadlines, and **contradictions** (two lines that disagree on the same fact). A contradiction quotes both lines and stays unresolved.

6. **Write the handoff summary last**: three to five sentences a colleague who missed the meeting can act on, drawn only from the sections above.

7. **Audit the brief against the notes.** Done when every decision, owner, deadline and quote matches the notes word for word, and every `Not stated` marks a real gap.

## Decision or proposal

A **decision** has recorded assent: "agreed", "decided", "approved", "we'll go with X", a decision-maker signing off, or a clear outcome stated as settled. A **proposal** is a suggestion, preference, option or question ("X suggests", "should we", "what about", "I think we should"), however popular it sounds.

- Silence is not assent. "Nobody objected" with no stated outcome keeps the item a proposal; list it in Open questions as "Decided or still proposed?".
- An explicit later reversal ("scrap that, we'll do Y instead") makes the final state the decision; quote both lines as evidence.
- A decision followed by a request to revisit stays a decision, flagged in Open questions as up for revisiting, with the quote.
- When the wording leaves you unsure, treat it as a proposal and ask the question in Open questions. A wrongly promoted proposal costs more than a flagged one.

## Brief format

Reply in chat with this markdown, unless the user asks for a file. Keep every section heading; an empty section reads "None recorded in the notes."

```markdown
# Decision brief: <meeting name or "Meeting"> (<date as written, or Not stated>)

## Decisions
1. <decision, one sentence>
   Evidence: "<verbatim quote>" (<speaker, if named>)

## Action items
| Action | Owner | Deadline |
|---|---|---|
| <action> | <owner or Not stated> | <deadline as written or Not stated> |

## Open questions and contradictions
- <question or proposal left open>
- Contradiction: "<quote A>" vs "<quote B>"

## Handoff summary
<three to five sentences>
```

When the meeting date is stated, a relative deadline may carry the calendar date in brackets after the original wording: "by Friday (14 March)". Without a stated date, the original wording stands alone.
