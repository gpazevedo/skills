# Decision brief: Pedalwise mobile team: release 4.2 sync (Tue 3 Nov 2026)

## Decisions
- 4.2 release moves to Mon 16 Nov as a single release, no 4.2/4.2.1 split. Evidence: "Agreed: 4.2 release moves to Mon 16 Nov. Single release, no split." (Section 1)
- Apple Pay is removed from 4.2 and moves to 4.3. Evidence: "Decision: Apple Pay comes out of 4.2 and moves to 4.3." (Section 2)
- Minimum iOS version is raised to 16 starting with 4.2. Evidence: "Agreed: raise minimum iOS to 16 starting with 4.2." (Section 2)
- Dark mode is not in 4.2. Evidence: "Dark mode came up again (Lena). Parked, not for 4.2." (Section 2)

## Proposals (not decided)
None found.

## Action items
| Action | Owner | Deadline | Evidence |
|---|---|---|---|
| Fix PW-1182 and get it into a TestFlight build | Tom | Wed 11 Nov | "Tom: fix PW-1182 and get it into a TestFlight build by Wed 11 Nov." (Section 3) |
| Deploy pricing API v2 to staging | Aisha | Fri 6 Nov | "Aisha: pricing API v2 deployed to staging by Fri 6 Nov." (Section 3) |
| Hand final onboarding screens to Tom | Lena | Mon 9 Nov | "Lena: final onboarding screens handed to Tom by Mon 9 Nov." (Section 4) |
| Full regression pass on the 4.2 release candidate | Marcus | Fri 13 Nov | "Marcus: full regression pass on the 4.2 release candidate, done by Fri 13 Nov." (Section 4) |
| Send 4.2 release notes (incl. the iOS 16 requirement) to the support team | Priya | Fri 13 Nov | "Priya: send 4.2 release notes (incl. the iOS 16 requirement) to the support team by Fri 13 Nov." (Section 5) |
| Bring dark mode back | Lena | "the Jan planning" (date and year not stated) | "Lena to bring it back in the Jan planning." (Section 2) |

## Open questions and contradictions
### Open questions
- Date of the "Jan planning" session is not stated, nor the year.
- Apple Pay: the notes say the SDK update is "still failing review on the sandbox account"; no owner or date is given for resolving this or for the 4.3 release.
- Android catch-up: "the old v1 endpoint stays up until Android catches up"; no date or owner stated.
### Contradictions
None found.

## Handoff summary
Decided: 4.2 ships Mon 16 Nov as a single release, Apple Pay moves to 4.3, minimum iOS becomes 16 from 4.2, and dark mode is not in 4.2. Aisha owns pricing API v2 on staging by Fri 6 Nov, Lena owns the onboarding screens handoff by Mon 9 Nov, and Tom owns the PW-1182 TestFlight build by Wed 11 Nov. Marcus owns regression and Priya owns the release notes to support, both by Fri 13 Nov. Unresolved: the Jan planning date for dark mode, the Apple Pay SDK review failure, and the Android catch-up timing for the v1 endpoint.
