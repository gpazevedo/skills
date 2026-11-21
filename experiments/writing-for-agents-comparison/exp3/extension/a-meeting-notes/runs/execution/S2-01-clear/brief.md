# Decision brief: Pedalwise mobile team: release 4.2 sync

Date: Tue 3 Nov 2026, 10:00 to 10:40 | Attendees: Priya Nair (PM, chair), Tom Becker (iOS), Aisha Okafor (backend), Lena Varga (design), Marcus Hale (QA)

## Handoff summary

Release 4.2 moves to Mon 16 Nov as a single release with no split, Apple Pay moves out of 4.2 into 4.3, and the minimum iOS version rises to 16 starting with 4.2. The most urgent action items are Aisha deploying pricing API v2 to staging by Fri 6 Nov, Lena handing the final onboarding screens to Tom by Mon 9 Nov, and Tom getting the PW-1182 crash fix into a TestFlight build by Wed 11 Nov. Marcus then runs full regression and Priya sends release notes to support, both by Fri 13 Nov. Still unresolved are dark mode, which was parked rather than decided, and when the old v1 pricing endpoint can be retired, since that depends on Android catching up with no date stated.

## Decisions

1. **Release 4.2 moves to Mon 16 Nov.**
   Evidence: "Agreed: 4.2 release moves to Mon 16 Nov." (1. Release date)
2. **4.2 ships as a single release, not split into 4.2 and 4.2.1.**
   Evidence: "Single release, no split." (1. Release date)
3. **Apple Pay comes out of 4.2 and moves to 4.3.**
   Evidence: "Decision: Apple Pay comes out of 4.2 and moves to 4.3." (2. Scope)
4. **The minimum iOS version rises to 16 starting with 4.2.**
   Evidence: "Agreed: raise minimum iOS to 16 starting with 4.2." (2. Scope)

## Action items

| Action | Owner | Deadline | Evidence |
| --- | --- | --- | --- |
| Deploy pricing API v2 to staging | Aisha | by Fri 6 Nov | "Aisha: pricing API v2 deployed to staging by Fri 6 Nov." (3. Crash + backend) |
| Hand final onboarding screens to Tom | Lena | by Mon 9 Nov | "Lena: final onboarding screens handed to Tom by Mon 9 Nov." (4. Design + QA) |
| Fix PW-1182 (ride-end crash) and get it into a TestFlight build | Tom | by Wed 11 Nov | "Tom: fix PW-1182 and get it into a TestFlight build by Wed 11 Nov." (3. Crash + backend) |
| Full regression pass on the 4.2 release candidate | Marcus | done by Fri 13 Nov | "Marcus: full regression pass on the 4.2 release candidate, done by Fri 13 Nov." (4. Design + QA) |
| Send 4.2 release notes (incl. the iOS 16 requirement) to the support team | Priya | by Fri 13 Nov | "Priya: send 4.2 release notes (incl. the iOS 16 requirement) to the support team by Fri 13 Nov." (5. Comms) |
| Bring dark mode back for discussion | Lena | in the Jan planning | "Lena to bring it back in the Jan planning." (2. Scope) |

## Open questions and contradictions

### Open questions

- Whether and when dark mode will be done; it was parked for 4.2 with no decision on a later release (Proposed, not decided). Evidence: "Dark mode came up again (Lena). Parked, not for 4.2." (2. Scope)
- When the old v1 pricing endpoint can be retired; it stays up until Android catches up, and no date is given for that (Detail missing). Evidence: "the old v1 endpoint stays up until Android catches up, no change there." (3. Crash + backend)
- How the Apple Pay SDK review failure on the sandbox account will be resolved for 4.3; no owner or plan is recorded (Detail missing). Evidence: "Apple Pay: SDK update still failing review on the sandbox account." (2. Scope)

### Contradictions

None recorded in the notes.
