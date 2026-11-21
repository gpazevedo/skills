# Decision brief: Pedalwise mobile team: release 4.2 sync
Tue 3 Nov 2026, 10:00 to 10:40 · Attendees: Priya Nair (PM, chair), Tom Becker (iOS), Aisha Okafor (backend), Lena Varga (design), Marcus Hale (QA)

## Decisions
1. Release 4.2 moves from Mon 9 Nov to Mon 16 Nov as a single release, with no split into 4.2 and 4.2.1.
   Evidence: "**Agreed: 4.2 release moves to Mon 16 Nov.** Single release, no split." (1. Release date)
2. Apple Pay is taken out of 4.2 and moves to 4.3.
   Evidence: "**Decision: Apple Pay comes out of 4.2 and moves to 4.3.**" (2. Scope)
3. The minimum iOS version rises from iOS 15 to iOS 16, starting with 4.2.
   Evidence: "**Agreed: raise minimum iOS to 16 starting with 4.2.**" (2. Scope)

## Proposals (no agreement recorded)
1. Splitting the release into 4.2 and 4.2.1 was discussed and not taken up; Decision 1 records "no split".
   Evidence: "Short discussion about splitting into 4.2 and 4.2.1. Nobody keen, too much overhead for support." (1. Release date)
2. Lena raised dark mode again; the notes record it as parked and not for 4.2, to come back at the Jan planning, with no agreement wording.
   Evidence: "Dark mode came up again (Lena). Parked, not for 4.2." (2. Scope)

## Action items
| # | Action | Owner | Deadline | Evidence |
|---|--------|-------|----------|----------|
| 1 | Fix the ride-end crash PW-1182 and get it into a TestFlight build | Tom | by Wed 11 Nov | "**Tom: fix PW-1182 and get it into a TestFlight build by Wed 11 Nov.**" (3. Crash + backend) |
| 2 | Deploy pricing API v2 to staging | Aisha | by Fri 6 Nov | "**Aisha: pricing API v2 deployed to staging by Fri 6 Nov.**" (3. Crash + backend) |
| 3 | Hand the final onboarding screens to Tom | Lena | by Mon 9 Nov | "**Lena: final onboarding screens handed to Tom by Mon 9 Nov.**" (4. Design + QA) |
| 4 | Run a full regression pass on the 4.2 release candidate | Marcus | by Fri 13 Nov | "**Marcus: full regression pass on the 4.2 release candidate, done by Fri 13 Nov.**" (4. Design + QA) |
| 5 | Send the 4.2 release notes, including the iOS 16 requirement, to the support team | Priya | by Fri 13 Nov | "**Priya: send 4.2 release notes (incl. the iOS 16 requirement) to the support team by Fri 13 Nov.**" (5. Comms) |
| 6 | Bring dark mode back for discussion | Lena | in the Jan planning | "Lena to bring it back in the Jan planning." (2. Scope) |

## Open questions
- Who works on the Apple Pay SDK update that is failing review, now that it moves to 4.3? No owner or next step is recorded. Source: "Apple Pay: SDK update still failing review on the sandbox account." (2. Scope)
- When will the v1 pricing endpoint be retired? The notes tie it to Android with no date. Source: "the old v1 endpoint stays up until Android catches up, no change there." (3. Crash + backend)
- Who removes the old map workaround that dropping iOS 15 allows, and when? No action is recorded. Source: "dropping 15 lets us remove the old map workaround, about 400 lines." (2. Scope)
- Will dark mode be scheduled for a later release? It is parked until the Jan planning. Source: "Parked, not for 4.2. Lena to bring it back in the Jan planning." (2. Scope)

## Contradictions
None recorded in the notes.

## Handoff summary
Release 4.2 now ships Mon 16 Nov as a single release, Apple Pay moves to 4.3, and the minimum iOS version rises to 16 starting with 4.2. Aisha is deploying pricing API v2 to staging by Fri 6 Nov, Lena is handing the final onboarding screens to Tom by Mon 9 Nov, and Tom is fixing crash PW-1182 into a TestFlight build by Wed 11 Nov. Marcus runs full regression on the release candidate by Fri 13 Nov, and Priya sends release notes with the iOS 16 requirement to support by Fri 13 Nov. Dark mode is parked until the Jan planning, and no owner is recorded for the failing Apple Pay SDK update, the v1 endpoint retirement or the map workaround removal.
