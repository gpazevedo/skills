# Decision brief: Pedalwise mobile team: release 4.2 sync
Tue 3 Nov 2026, 10:00 to 10:40. Attendees: Priya Nair (PM, chair), Tom Becker (iOS), Aisha Okafor (backend), Lena Varga (design), Marcus Hale (QA). Notes: Marcus.

## Decisions
1. Release 4.2 moves to Mon 16 Nov as a single release, with no split into 4.2 and 4.2.1.
   Evidence: "Agreed: 4.2 release moves to Mon 16 Nov. Single release, no split." (1. Release date)
2. Apple Pay comes out of 4.2 and moves to 4.3.
   Evidence: "Decision: Apple Pay comes out of 4.2 and moves to 4.3." (2. Scope)
3. Minimum iOS version rises from iOS 15 to iOS 16, starting with 4.2.
   Evidence: "Agreed: raise minimum iOS to 16 starting with 4.2." (2. Scope)

## Proposals (not decided)
- Split the release into 4.2 and 4.2.1, raised by unresolved. Not adopted: superseded by Decision 1. Evidence: "Short discussion about splitting into 4.2 and 4.2.1. Nobody keen, too much overhead for support." (1. Release date)
- Dark mode, recorded as parked and not for 4.2, to come back at the January planning, raised by Lena. Evidence: "Dark mode came up again (Lena). Parked, not for 4.2." (2. Scope)

## Action items
| Action | Owner | Deadline | Evidence |
|---|---|---|---|
| Fix PW-1182 (ride-end crash) and get it into a TestFlight build | Tom | by Wed 11 Nov | "Tom: fix PW-1182 and get it into a TestFlight build by Wed 11 Nov." (3. Crash + backend) |
| Deploy pricing API v2 to staging | Aisha | by Fri 6 Nov | "Aisha: pricing API v2 deployed to staging by Fri 6 Nov." (3. Crash + backend) |
| Hand final onboarding screens to Tom | Lena | by Mon 9 Nov | "Lena: final onboarding screens handed to Tom by Mon 9 Nov." (4. Design + QA) |
| Full regression pass on the 4.2 release candidate | Marcus | done by Fri 13 Nov | "Marcus: full regression pass on the 4.2 release candidate, done by Fri 13 Nov." (4. Design + QA) |
| Send 4.2 release notes (incl. the iOS 16 requirement) to the support team | Priya | by Fri 13 Nov | "Priya: send 4.2 release notes (incl. the iOS 16 requirement) to the support team by Fri 13 Nov." (5. Comms) |
| Bring dark mode back for discussion | Lena | in the Jan planning | "Lena to bring it back in the Jan planning." (2. Scope) |

## Open questions
- Was leaving dark mode out of 4.2 a group decision? The notes record it only as "Parked, not for 4.2", with no recorded agreement.
- When will everything be on staging so Marcus can start regression? Marcus "needs everything on staging before he starts regression", and the notes give a staging date only for pricing API v2 (Fri 6 Nov); the PW-1182 fix has a TestFlight date (Wed 11 Nov), not a staging date.

## Contradictions
- 4.2 release date: "4.2 was meant to go Mon 9 Nov." (1. Release date, Priya) vs "Agreed: 4.2 release moves to Mon 16 Nov." (1. Release date). Explicit change recorded: the latest outcome is Mon 16 Nov.

## Handoff summary
Release 4.2 now ships Mon 16 Nov as a single release (moved from Mon 9 Nov), Apple Pay moves to 4.3, and the minimum iOS version rises to 16 from 4.2. Before release, Aisha deploys pricing API v2 to staging by Fri 6 Nov, Lena hands the final onboarding screens to Tom by Mon 9 Nov, Tom gets the PW-1182 crash fix into a TestFlight build by Wed 11 Nov, and Marcus completes the full regression pass by Fri 13 Nov. Priya sends the release notes, including the iOS 16 requirement, to the support team by Fri 13 Nov. Dark mode is parked for 4.2, with Lena to bring it back at the January planning, though the notes do not record it as an agreed decision. Still unresolved is when everything will be on staging, which Marcus needs before he can start regression.
