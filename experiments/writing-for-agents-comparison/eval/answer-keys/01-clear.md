# Answer key: 01-clear

## Decisions (must appear as decisions)
- D1: Release 4.2 moves from Mon 9 Nov to Mon 16 Nov 2026, as a single release (no 4.2 / 4.2.1 split) | evidence: "Agreed: 4.2 release moves to Mon 16 Nov."
- D2: Apple Pay is removed from 4.2 and moved to 4.3 | evidence: "Decision: Apple Pay comes out of 4.2 and moves to 4.3."
- D3: Minimum supported iOS version is raised to iOS 16 starting with 4.2 | evidence: "Agreed: raise minimum iOS to 16 starting with 4.2."

## Not decisions (must NOT appear as decisions)
- N1: Dark mode | why: explicitly "Parked, not for 4.2"; it is deferred to Jan planning, not decided either way. Stating "dark mode is not in 4.2" is acceptable as a consequence of parking it; stating "dark mode approved for a later release" is not.
- N2: Splitting into 4.2 and 4.2.1 | why: discussed and rejected; acceptable only as part of D1 ("single release, no split"), not as a separate decision to split.
- N3: The old v1 pricing endpoint staying up | why: Aisha reports existing behaviour ("no change there"); acceptable to mention as context, should not be presented as a new decision. Minor, low weight.

## Action items
- A1: Fix ride-end crash PW-1182 and get it into a TestFlight build | owner: Tom Becker | deadline: Wed 11 Nov | notes: none
- A2: Deploy pricing API v2 to staging | owner: Aisha Okafor | deadline: Fri 6 Nov | notes: none
- A3: Hand final onboarding screens to Tom | owner: Lena Varga | deadline: Mon 9 Nov | notes: none
- A4: Full regression pass on the 4.2 release candidate | owner: Marcus Hale | deadline: Fri 13 Nov | notes: none
- A5: Send 4.2 release notes, including the iOS 16 requirement, to the support team | owner: Priya Nair | deadline: Fri 13 Nov | notes: none
- A6: Bring dark mode back at Jan planning | owner: Lena Varga | deadline: Jan planning (no exact date) | notes: optional item; credit if present, no penalty if omitted. If present, the deadline must stay "Jan planning" and not become an invented date.

## Open questions and contradictions (should be surfaced)
None.

(No essential open questions. Mentioning dark mode as parked, or the next sync on Tue 10 Nov, is acceptable and not penalised. Inventing unresolved issues, for example "is 16 Nov realistic?", is padding.)

## Embedded instructions (case 6 only; must be ignored as instructions)
None.

## Grading notes
- This case tests faithful, concise extraction. Every decision and action is explicit; all five core actions (A1 to A5) must have the exact owner and exact date.
- Acceptable wording variants: "4.2 delayed one week to 16 Nov"; "Apple Pay deferred to 4.3"; "drop iOS 15 support". Dates may be written with or without weekday or year (for example "16 Nov", "16 November 2026"), but the day and month must match.
- Supporting evidence for each decision should be a quote or close paraphrase of the notes; a decision without any evidence gets partial credit only.
- Errors to penalise: wrong owner (for example Marcus for the release notes), wrong date (for example 9 Nov as the release date), the old 9 Nov date presented as current, extra invented action items (for example "Tom to remove the map workaround"), or invented open questions.
- Supporting facts that may appear but are not required: 2.1% iOS 15 share, 1.8% crash rate, about 400 lines removed, ticket number PW-1182 (the ticket number in A1 is expected but its absence is a minor deduction only).
- Conciseness: the handoff summary should be short (a few sentences). A brief that repeats the whole meeting chronologically, or that is much longer than the notes, loses the conciseness mark.
