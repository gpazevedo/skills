# Decision brief: Pedalwise mobile team: release 4.2 sync (Tue 3 Nov 2026)

## Handoff summary
The team agreed to move the 4.2 release from Mon 9 Nov to Mon 16 Nov as a single release with no 4.2.1 split, to take Apple Pay out of 4.2 and move it to 4.3, and to raise the minimum iOS version to 16 starting with 4.2. Next steps: Aisha deploys pricing API v2 to staging by Fri 6 Nov, Lena hands the final onboarding screens to Tom by Mon 9 Nov, Tom gets the PW-1182 ride-end crash fix into a TestFlight build by Wed 11 Nov, and Marcus finishes a full regression pass on the 4.2 release candidate by Fri 13 Nov. Priya sends the 4.2 release notes, including the iOS 16 requirement, to the support team by Fri 13 Nov. Dark mode is parked and not in 4.2; Lena is to bring it back in the Jan planning. The notes record no open questions or contradictions.

## Decisions
1. The 4.2 release moves from Mon 9 Nov to Mon 16 Nov, as a single release with no split into 4.2 and 4.2.1.
   Evidence: "4.2 was meant to go Mon 9 Nov. Not realistic with the ride-end crash still open + pricing API not on staging yet." (§1 Release date, line 11); "**Agreed: 4.2 release moves to Mon 16 Nov.** Single release, no split." (§1 Release date, line 15)
2. Apple Pay comes out of 4.2 and moves to 4.3.
   Evidence: "**Decision: Apple Pay comes out of 4.2 and moves to 4.3.**" (§2 Scope, line 21)
3. The minimum iOS version is raised to iOS 16 starting with 4.2.
   Evidence: "**Agreed: raise minimum iOS to 16 starting with 4.2.**" (§2 Scope, line 24)

## Action items
| Task | Owner | Deadline | Evidence |
| --- | --- | --- | --- |
| Deploy pricing API v2 to staging | Aisha | Fri 6 Nov | "**Aisha: pricing API v2 deployed to staging by Fri 6 Nov.**" (§3 Crash + backend, line 31) |
| Hand final onboarding screens to Tom | Lena | Mon 9 Nov | "**Lena: final onboarding screens handed to Tom by Mon 9 Nov.**" (§4 Design + QA, line 37) |
| Fix PW-1182 (ride-end crash) and get it into a TestFlight build | Tom | Wed 11 Nov | "**Tom: fix PW-1182 and get it into a TestFlight build by Wed 11 Nov.**" (§3 Crash + backend, line 30) |
| Full regression pass on the 4.2 release candidate | Marcus | Fri 13 Nov | "**Marcus: full regression pass on the 4.2 release candidate, done by Fri 13 Nov.**" (§4 Design + QA, line 39) |
| Send 4.2 release notes (incl. the iOS 16 requirement) to the support team | Priya | Fri 13 Nov | "**Priya: send 4.2 release notes (incl. the iOS 16 requirement) to the support team by Fri 13 Nov.**" (§5 Comms, line 44) |
| Bring dark mode back for discussion | Lena | the Jan planning | "Lena to bring it back in the Jan planning." (§2 Scope, line 25) |

## Proposals not decided
1. Dark mode (raised by Lena). Status: parked and not for 4.2; to be brought back in the Jan planning.
   Evidence: "Dark mode came up again (Lena). Parked, not for 4.2. Lena to bring it back in the Jan planning." (§2 Scope, line 25)
2. Splitting the release into 4.2 and 4.2.1. Status: not adopted; the team agreed a single release with no split (see Decision 1).
   Evidence: "Short discussion about splitting into 4.2 and 4.2.1. Nobody keen, too much overhead for support." (§1 Release date, line 14)

## Open questions and contradictions
None recorded in the notes.
