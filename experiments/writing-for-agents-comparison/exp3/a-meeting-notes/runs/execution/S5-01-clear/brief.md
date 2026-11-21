# Decision brief: Pedalwise mobile team: release 4.2 sync (Tue 3 Nov 2026)

## Decisions
1. The 4.2 release moves from Mon 9 Nov to Mon 16 Nov as a single release, with no split into 4.2 and 4.2.1.
   Evidence: "Agreed: 4.2 release moves to Mon 16 Nov. Single release, no split." (1. Release date)
2. Apple Pay comes out of 4.2 and moves to 4.3.
   Evidence: "Decision: Apple Pay comes out of 4.2 and moves to 4.3." (2. Scope)
3. The minimum iOS version is raised from iOS 15 to iOS 16 starting with 4.2.
   Evidence: "Agreed: raise minimum iOS to 16 starting with 4.2." (2. Scope)

## Proposals (not decided)
- Dark mode is parked and not included in 4.2. Status: "Parked", to be brought back in the Jan planning; no closure word recorded.
- The old pricing v1 endpoint stays up until Android catches up. Status: stated by Aisha as "no change there"; no closure word recorded.
- The next sync is Tue 10 Nov at the same time. Status: listed as "Next sync"; no closure word recorded.

## Action items
| Action | Owner | Deadline |
| --- | --- | --- |
| Fix PW-1182 (ride-end crash) and get it into a TestFlight build | Tom | Wed 11 Nov |
| Deploy pricing API v2 to staging | Aisha | Fri 6 Nov |
| Hand final onboarding screens to Tom | Lena | Mon 9 Nov |
| Full regression pass on the 4.2 release candidate | Marcus | Fri 13 Nov |
| Send 4.2 release notes (incl. the iOS 16 requirement) to the support team | Priya | Fri 13 Nov |
| Bring dark mode back for planning | Lena | Jan planning |

## Open questions and contradictions
- Question: Was dropping dark mode from 4.2 decided, or only parked pending the Jan planning? Source: 2. Scope.
- Question: Was keeping the v1 pricing endpoint up until Android catches up a decision, and when is Android expected to catch up? Source: 3. Crash + backend.
- Question: Is the next sync on Tue 10 Nov confirmed? Source: end of notes ("Next sync").
- Question: How will the Apple Pay SDK update that is failing review on the sandbox account be resolved for 4.3? Source: 2. Scope.
- No contradictions recorded in the notes.

## Handoff summary
The team agreed to ship 4.2 as a single release on Mon 16 Nov, move Apple Pay to 4.3, and raise the minimum iOS version to 16 from 4.2. Next, Aisha deploys pricing API v2 to staging by Fri 6 Nov, Lena hands onboarding screens to Tom by Mon 9 Nov, Tom gets the PW-1182 crash fix into TestFlight by Wed 11 Nov, and Marcus (regression) and Priya (support release notes) both deliver by Fri 13 Nov. Still unresolved are whether dark mode is formally out of 4.2, how long the v1 pricing endpoint stays up, and whether the Tue 10 Nov sync is confirmed.
