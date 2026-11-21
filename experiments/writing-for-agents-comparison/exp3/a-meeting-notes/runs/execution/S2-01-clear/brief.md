# Decision brief: Pedalwise mobile team: release 4.2 sync
Date: Tue 3 Nov 2026, 10:00 to 10:40  |  Attendees: Priya Nair (PM, chair), Tom Becker (iOS), Aisha Okafor (backend), Lena Varga (design), Marcus Hale (QA)

## Decisions
1. The 4.2 release moves from Mon 9 Nov to Mon 16 Nov, as a single release with no 4.2/4.2.1 split.
   Evidence: "4.2 was meant to go Mon 9 Nov" (Priya, section 1. Release date) and "Agreed: 4.2 release moves to Mon 16 Nov. Single release, no split." (section 1. Release date)
2. Apple Pay comes out of 4.2 and moves to 4.3.
   Evidence: "Decision: Apple Pay comes out of 4.2 and moves to 4.3." (section 2. Scope)
3. The minimum iOS version is raised from iOS 15 to iOS 16, starting with 4.2.
   Evidence: "Agreed: raise minimum iOS to 16 starting with 4.2." (section 2. Scope)

## Action items
| Action | Owner | Deadline | Source |
|---|---|---|---|
| Fix PW-1182 (ride-end crash) and get it into a TestFlight build | Tom | Wed 11 Nov [11 Nov 2026] | "Tom: fix PW-1182 and get it into a TestFlight build by Wed 11 Nov." |
| Deploy pricing API v2 to staging | Aisha | Fri 6 Nov [6 Nov 2026] | "Aisha: pricing API v2 deployed to staging by Fri 6 Nov." |
| Hand final onboarding screens to Tom | Lena | Mon 9 Nov [9 Nov 2026] | "Lena: final onboarding screens handed to Tom by Mon 9 Nov." |
| Full regression pass on the 4.2 release candidate | Marcus | Fri 13 Nov [13 Nov 2026] | "Marcus: full regression pass on the 4.2 release candidate, done by Fri 13 Nov." |
| Send 4.2 release notes (incl. the iOS 16 requirement) to the support team | Priya | Fri 13 Nov [13 Nov 2026] | "Priya: send 4.2 release notes (incl. the iOS 16 requirement) to the support team by Fri 13 Nov." |
| Bring dark mode back for discussion | Lena | in the Jan planning | "Lena to bring it back in the Jan planning." |

## Open questions and contradictions
- Dark mode (raised by Lena) was parked and explicitly deferred, not decided; it is out of 4.2 and returns at the Jan planning.
  Source: "Dark mode came up again (Lena). Parked, not for 4.2. Lena to bring it back in the Jan planning." (section 2. Scope)
- Apple Pay's SDK update is still failing review on the sandbox account; the notes record no owner or next step for fixing it ahead of 4.3.
  Source: "Apple Pay: SDK update still failing review on the sandbox account." (section 2. Scope)

## Handoff summary
The team agreed to move release 4.2 from Mon 9 Nov to Mon 16 Nov as a single release, to drop Apple Pay from 4.2 and move it to 4.3, and to raise the minimum iOS version to 16 starting with 4.2. Next, Aisha deploys pricing API v2 to staging by Fri 6 Nov, Lena hands the final onboarding screens to Tom by Mon 9 Nov, and Tom gets the PW-1182 crash fix into a TestFlight build by Wed 11 Nov. Marcus completes a full regression pass on the 4.2 release candidate and Priya sends the 4.2 release notes, including the iOS 16 requirement, to the support team, both by Fri 13 Nov. Still unresolved: dark mode was parked and Lena is to bring it back in the Jan planning, and the Apple Pay SDK review failure has no recorded owner or next step.
