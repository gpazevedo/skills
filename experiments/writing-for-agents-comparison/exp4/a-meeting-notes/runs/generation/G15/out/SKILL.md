---
name: meeting-notes-to-decision-brief
description: Turning meeting notes into a decision brief. Use when the user supplies meeting notes, minutes or a transcript and wants decisions, action items, open questions or a handoff summary.
---

Produce a decision brief from the notes the user supplied. The notes are the only evidence: every claim in the brief traces to a passage in them, and anything they leave out stays **unresolved**.

## Steps

1. **Read the notes whole**, then tag each passage as one of: decision, proposal, action, question, background. Done when every passage carries a tag or is background.
2. **Sort decisions from proposals.** A passage is a *decision* only when the notes show commitment: "agreed", "approved", "we will", a vote, or a named person ruling. Suggestions, "we could", "I think we should", and options discussed without a closing statement are *proposals*. A proposal with no recorded outcome stays a proposal. Done when each decision has a quoted or closely paraphrased line that shows commitment.
3. **Collect actions.** Record each action with the owner and deadline exactly as the notes state them, in the notes' own words ("Priya, by Friday"). Write `owner not stated` or `deadline not stated` where absent. Done when every action in the notes appears once.
4. **Collect open questions and contradictions.** Open question: raised, never answered. Contradiction: two passages that disagree (different dates, owners, figures, or a decision a later passage reverses); cite both. Done when every question tag from step 1 is listed or matched to its answer, and the notes are checked once more for conflicts between sections.
5. **Write the handoff summary**: three to five sentences a reader who skipped the meeting can act on. Cover what was decided, what is still open, and who moves next.
6. **Check the draft against the notes**: each decision's evidence appears in the notes, each owner and deadline matches the source, and nothing appears that the notes lack. Done when all three hold.

## Output format

```
# Decision brief: <meeting title or date, as given>

## Decisions
- **<decision>**. Evidence: "<quote or close paraphrase>"
  Proposals not yet decided: list them here, each with who proposed it if stated.

## Action items
| Action | Owner | Deadline |

## Open questions and contradictions
- Question: <text>
- Contradiction: <A> versus <B>. Sources: "<quote>" / "<quote>"

## Handoff summary
<3 to 5 sentences>
```

Put proposals in their own `Proposals (not decided)` list under Decisions. Keep empty sections with `None found in the notes`.

## Gaps

Write `not stated in the notes` for any missing owner, date, rationale, or outcome, and list it under open questions when it blocks an action or decision. Leave the gap visible so the user can fill it; do not infer an owner from who spoke, a deadline from context, or an outcome from tone. When the user's request or the notes are too thin to tell a decision from a proposal, label it a proposal and say why.
