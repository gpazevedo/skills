# Decision brief: Pedalwise mobile team: release 4.2 sync (Tue 3 Nov 2026)

## Decisions
- **4.2 release moves to Mon 16 Nov, as a single release with no split into 4.2 and 4.2.1.** Evidence: "Agreed: 4.2 release moves to Mon 16 Nov. Single release, no split."
- **Apple Pay comes out of 4.2 and moves to 4.3.** Evidence: "Decision: Apple Pay comes out of 4.2 and moves to 4.3."
- **Minimum iOS version is raised to 16 starting with 4.2.** Evidence: "Agreed: raise minimum iOS to 16 starting with 4.2."

Proposals (not decided):
- Dark mode in 4.2: raised by Lena. The notes say "Parked, not for 4.2", with Lena to bring it back in the Jan planning. No decision on whether to build it.

## Action items
| Action | Owner | Deadline |
|---|---|---|
| Fix PW-1182 and get it into a TestFlight build | Tom | Wed 11 Nov |
| Deploy pricing API v2 to staging | Aisha | Fri 6 Nov |
| Hand final onboarding screens to Tom | Lena | Mon 9 Nov |
| Full regression pass on the 4.2 release candidate | Marcus | Fri 13 Nov |
| Send 4.2 release notes (incl. the iOS 16 requirement) to the support team | Priya | Fri 13 Nov |
| Bring dark mode back in the Jan planning | Lena | Jan planning (exact date not stated in the notes) |

## Open questions and contradictions
- Question: Apple Pay SDK update is "still failing review on the sandbox account". Who resolves this, and when? Owner not stated, deadline not stated.
- Question: What is the target date for 4.3? Not stated in the notes.
- Contradiction: None found in the notes. The original date (Mon 9 Nov) is explicitly replaced by the agreed Mon 16 Nov.

## Handoff summary
The team agreed to move 4.2 to Mon 16 Nov as a single release, to move Apple Pay to 4.3, and to raise the minimum iOS version to 16. Dark mode is parked and is not decided. Still open: who fixes the Apple Pay sandbox review failure, and the 4.3 date, neither of which is stated in the notes. Aisha moves first (pricing API v2 on staging by Fri 6 Nov), then Lena (onboarding screens by Mon 9 Nov), Tom (TestFlight build by Wed 11 Nov), and Marcus and Priya (regression pass and support release notes, both by Fri 13 Nov). The next sync is Tue 10 Nov, same time.
