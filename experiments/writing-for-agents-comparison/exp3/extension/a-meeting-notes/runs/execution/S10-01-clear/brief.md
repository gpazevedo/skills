# Decision brief: Pedalwise mobile team: release 4.2 sync
Date: Tue 3 Nov 2026, 10:00 to 10:40 | Attendees: Priya Nair (PM, chair), Tom Becker (iOS), Aisha Okafor (backend), Lena Varga (design), Marcus Hale (QA)

## Decisions
1. **The 4.2 release moves from Mon 9 Nov to Mon 16 Nov, as a single release with no split into 4.2 and 4.2.1.**
   Evidence: "Agreed: 4.2 release moves to Mon 16 Nov. Single release, no split." (section 1, Release date). The original date was "meant to go Mon 9 Nov" (section 1); the split was discussed and "Nobody keen, too much overhead for support." (section 1)
2. **Apple Pay comes out of 4.2 and moves to 4.3.**
   Evidence: "Decision: Apple Pay comes out of 4.2 and moves to 4.3." (section 2, Scope)
3. **The minimum iOS version rises from iOS 15 to iOS 16 starting with 4.2.**
   Evidence: "Agreed: raise minimum iOS to 16 starting with 4.2." (section 2, Scope)

## Action items
| Action | Owner | Deadline | Source |
| --- | --- | --- | --- |
| Fix ride-end crash PW-1182 and get it into a TestFlight build | Tom | Wed 11 Nov | section 3, Crash + backend |
| Deploy pricing API v2 to staging | Aisha | Fri 6 Nov | section 3, Crash + backend |
| Hand final onboarding screens to Tom | Lena | Mon 9 Nov | section 4, Design + QA |
| Full regression pass on the 4.2 release candidate | Marcus | Fri 13 Nov | section 4, Design + QA |
| Send 4.2 release notes (incl. the iOS 16 requirement) to the support team | Priya | Fri 13 Nov | section 5, Comms |
| Bring dark mode back for discussion | Lena | "in the Jan planning" | section 2, Scope |

## Proposals not yet decided
- Dark mode: raised by Lena; "Parked, not for 4.2", to return at the Jan planning (section 2, Scope)

## Open questions and contradictions
None recorded in the notes.

## Handoff summary
The team agreed to move release 4.2 to Mon 16 Nov as a single release, to drop Apple Pay to 4.3, and to raise the minimum iOS version to 16 from 4.2. Dark mode is parked and not part of 4.2; Lena is to bring it back at the Jan planning. Next to act is Aisha, with pricing API v2 on staging by Fri 6 Nov, then Lena (onboarding screens by Mon 9 Nov) and Tom (PW-1182 fix in TestFlight by Wed 11 Nov). Marcus needs everything on staging before starting regression, which is due by Fri 13 Nov, the same day Priya sends release notes with the iOS 16 requirement to support. The next sync is Tue 10 Nov at the same time.
