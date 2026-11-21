# Decision brief: Pedalwise mobile team: release 4.2 sync

Date: Tue 3 Nov 2026, 10:00 to 10:40  |  Attendees: Priya Nair (PM, chair), Tom Becker (iOS), Aisha Okafor (backend), Lena Varga (design), Marcus Hale (QA)

## Decisions
1. **Release 4.2 moves from Mon 9 Nov to Mon 16 Nov as a single release, with no split into 4.2 and 4.2.1.**
   Evidence: "Agreed: 4.2 release moves to Mon 16 Nov. Single release, no split." (section 1, Release date)
2. **Apple Pay is removed from 4.2 and moves to 4.3.**
   Evidence: "Decision: Apple Pay comes out of 4.2 and moves to 4.3." (section 2, Scope)
3. **The minimum iOS version rises from iOS 15 to iOS 16 starting with 4.2.**
   Evidence: "Agreed: raise minimum iOS to 16 starting with 4.2." (section 2, Scope)

## Proposals not yet decided
- Dark mode, parked and not in 4.2; to be raised again at the January planning (raised by Lena)

## Action items
| Action | Owner | Deadline |
| --- | --- | --- |
| Fix the ride-end crash (PW-1182) and get it into a TestFlight build | Tom | Wed 11 Nov |
| Deploy pricing API v2 to staging | Aisha | Fri 6 Nov |
| Hand the final onboarding screens to Tom | Lena | Mon 9 Nov |
| Run the full regression pass on the 4.2 release candidate | Marcus | Fri 13 Nov |
| Send the 4.2 release notes, including the iOS 16 requirement, to the support team | Priya | Fri 13 Nov |
| Bring dark mode back for discussion | Lena | "in the Jan planning" |

## Open questions and contradictions
- **Open:** Dark mode is recorded as "Parked, not for 4.2"; the notes do not say whether it is planned for any later release (section 2, Scope).
- **Open:** Marcus needs everything on staging before he starts regression, but the notes give no date by which the full 4.2 release candidate (including the PW-1182 fix, due in TestFlight Wed 11 Nov) will be on staging (section 4, Design + QA).
- **Open:** The old pricing v1 endpoint stays up "until Android catches up"; no date for that is stated (section 3, Crash + backend).

## Handoff summary
The team agreed to ship 4.2 as a single release on Mon 16 Nov instead of Mon 9 Nov, to drop Apple Pay to 4.3, and to raise the minimum iOS version to 16 from 4.2. The schedule now depends on Aisha getting pricing API v2 to staging by Fri 6 Nov, Lena handing onboarding screens to Tom by Mon 9 Nov, Tom getting the PW-1182 crash fix into TestFlight by Wed 11 Nov, and Marcus finishing regression by Fri 13 Nov. Priya is to send release notes, including the iOS 16 requirement, to support by Fri 13 Nov. Still unresolved: when the full release candidate will be on staging for regression to start, when the v1 pricing endpoint will be retired, and where dark mode lands after the January planning. The next sync is Tue 10 Nov at the same time.
