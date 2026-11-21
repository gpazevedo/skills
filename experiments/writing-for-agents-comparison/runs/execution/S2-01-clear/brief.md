# Decision brief: Pedalwise mobile team: release 4.2 sync
Date: Tue 3 Nov 2026, 10:00 to 10:40  Attendees: Priya Nair (PM, chair), Tom Becker (iOS), Aisha Okafor (backend), Lena Varga (design), Marcus Hale (QA)

## Decisions
1. The 4.2 release moves to Mon 16 Nov, as a single release with no split into 4.2 and 4.2.1.
   Evidence: "Agreed: 4.2 release moves to Mon 16 Nov. Single release, no split." (1. Release date)
2. Apple Pay comes out of 4.2 and moves to 4.3.
   Evidence: "Decision: Apple Pay comes out of 4.2 and moves to 4.3." (2. Scope)
3. The minimum iOS version is raised to 16, starting with 4.2.
   Evidence: "Agreed: raise minimum iOS to 16 starting with 4.2." (2. Scope)

## Action items
| Action | Owner | Deadline | From decision |
| --- | --- | --- | --- |
| Fix PW-1182 (ride-end crash) and get it into a TestFlight build | Tom | by Wed 11 Nov | none |
| Deploy pricing API v2 to staging | Aisha | by Fri 6 Nov | none |
| Hand final onboarding screens to Tom | Lena | by Mon 9 Nov | none |
| Full regression pass on the 4.2 release candidate | Marcus | done by Fri 13 Nov | none |
| Send 4.2 release notes (incl. the iOS 16 requirement) to the support team | Priya | by Fri 13 Nov | 3 |
| Bring dark mode back | Lena | in the Jan planning | none |

## Open questions and contradictions
- Proposed, not decided: dark mode, raised again by Lena and parked for a later release ("Dark mode came up again (Lena). Parked, not for 4.2.")

## Handoff summary
The 4.2 release has moved to Mon 16 Nov as a single release, Apple Pay has moved out to 4.3, and the minimum iOS version rises to 16 starting with 4.2. Work in motion: Tom is fixing the ride-end crash (PW-1182) for a TestFlight build by Wed 11 Nov, Aisha is deploying pricing API v2 to staging by Fri 6 Nov, and Lena is handing final onboarding screens to Tom by Mon 9 Nov. Marcus runs the full regression pass on the 4.2 release candidate by Fri 13 Nov, and Priya sends the 4.2 release notes, including the iOS 16 requirement, to the support team by the same day. Dark mode is parked, not for 4.2, and Lena will bring it back in the Jan planning.
