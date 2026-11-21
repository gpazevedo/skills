# Decision brief: Pedalwise mobile team, release 4.2 sync
Date / attendees: Tue 3 Nov 2026, 10:00 to 10:40. Priya Nair (PM, chair), Tom Becker (iOS), Aisha Okafor (backend), Lena Varga (design), Marcus Hale (QA). Notes by Marcus.

## Decisions
- 4.2 release moves to Mon 16 Nov, as a single release with no 4.2/4.2.1 split. Evidence: "Agreed: 4.2 release moves to Mon 16 Nov." Single release, no split. (Section 1, Release date)
- Apple Pay is removed from 4.2 and moves to 4.3. Evidence: "Decision: Apple Pay comes out of 4.2 and moves to 4.3." (Section 2, Scope)
- Minimum iOS version is raised to 16 starting with 4.2. Evidence: "Agreed: raise minimum iOS to 16 starting with 4.2." (Section 2, Scope)
- Dark mode is parked and not in 4.2. Evidence: "Parked, not for 4.2." (Section 2, Scope). Rationale for iOS 16 as stated: not stated beyond Lena's analytics (iOS 15 users are 2.1% of monthly active riders) and Tom's note that dropping 15 removes about 400 lines of old map workaround.

## Proposals not yet decided
None found in the notes.

## Action items
| Action | Owner | Deadline | Source |
|---|---|---|---|
| Fix PW-1182 and get it into a TestFlight build | Tom | Wed 11 Nov | Section 3 |
| Deploy pricing API v2 to staging | Aisha | Fri 6 Nov | Section 3 |
| Hand final onboarding screens to Tom | Lena | Mon 9 Nov | Section 4 |
| Full regression pass on the 4.2 release candidate | Marcus | Fri 13 Nov | Section 4 |
| Send 4.2 release notes (incl. the iOS 16 requirement) to the support team | Priya | Fri 13 Nov | Section 5 |
| Bring dark mode back in the Jan planning | Lena | "the Jan planning" (no specific date; deadline: not stated) | Section 2 |

## Open questions and contradictions
- Contradiction: None found in the notes. Dates and figures are consistent across sections as written.
- Question: Who owns moving Apple Pay to 4.3 and fixing the SDK sandbox review failure? owner: unassigned, deadline: not stated.
- Question: Marcus "needs everything on staging before he starts regression", but the notes give no deadline for the iOS release candidate itself beyond the TestFlight build by Wed 11 Nov. Who produces the release candidate, and by when? owner: unassigned, deadline: not stated.
- Question: Who updates the app's minimum iOS setting and removes the old map workaround? owner: unassigned, deadline: not stated.
- Question: The release notes are for the support team; who communicates anything to riders? Not stated.

## Handoff summary
Decided: 4.2 ships Mon 16 Nov as a single release, Apple Pay moves to 4.3, minimum iOS becomes 16, and dark mode is parked. Nothing is pending as a proposal. Pending items are the five dated actions plus Lena's dark mode item for the Jan planning. Next to act are Aisha (staging by Fri 6 Nov) and Lena (screens by Mon 9 Nov). Progress is blocked on staging being complete before Marcus's regression, and the release candidate and Apple Pay owners are not stated.
