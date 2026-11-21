# Decision brief: Pedalwise mobile team: release 4.2 sync
Tue 3 Nov 2026, 10:00 to 10:40. Attendees: Priya Nair (PM, chair), Tom Becker (iOS), Aisha Okafor (backend), Lena Varga (design), Marcus Hale (QA). Notes: Marcus.

## Decisions
1. The 4.2 release moves from Mon 9 Nov to Mon 16 Nov, as a single release with no 4.2/4.2.1 split.
   Evidence: "Agreed: 4.2 release moves to Mon 16 Nov. Single release, no split." (1. Release date)
2. Apple Pay is removed from 4.2 and moves to 4.3.
   Evidence: "Decision: Apple Pay comes out of 4.2 and moves to 4.3." (2. Scope)
3. The minimum iOS version rises from iOS 15 to iOS 16, starting with 4.2.
   Evidence: "Agreed: raise minimum iOS to 16 starting with 4.2." (2. Scope)

## Action items
| Action | Owner | Deadline |
| --- | --- | --- |
| Fix PW-1182 (ride-end crash) and get it into a TestFlight build | Tom | by Wed 11 Nov |
| Deploy pricing API v2 to staging | Aisha | by Fri 6 Nov |
| Hand final onboarding screens to Tom | Lena | by Mon 9 Nov |
| Full regression pass on the 4.2 release candidate | Marcus | done by Fri 13 Nov |
| Send 4.2 release notes (incl. the iOS 16 requirement) to the support team | Priya | by Fri 13 Nov |
| Bring dark mode back for discussion | Lena | in the Jan planning |

## Open questions
- Dark mode: "Parked, not for 4.2"; no target release decided, to be raised again by Lena in the Jan planning.
- Apple Pay: the SDK update is "still failing review on the sandbox account"; the notes give no owner or plan for resolving it before 4.3.
- Regression start depends on staging: Marcus "needs everything on staging before he starts regression"; the notes do not say when everything is expected to be on staging beyond the pricing API (Fri 6 Nov).

## Contradictions
None recorded.

## Handoff summary
4.2 now ships as a single release on Mon 16 Nov, without Apple Pay (moved to 4.3) and with a new minimum of iOS 16. Dark mode is parked with no release decided, and Marcus's regression pass depends on everything reaching staging first. The most urgent action is Aisha deploying pricing API v2 to staging by Fri 6 Nov.
