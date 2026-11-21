# Decision brief: Pedalwise mobile team: release 4.2 sync (Tue 3 Nov 2026)

## Decisions
1. The 4.2 release moves to Mon 16 Nov as a single release, with no split into 4.2 and 4.2.1.
   Evidence: "**Agreed: 4.2 release moves to Mon 16 Nov.** Single release, no split." (notes by Marcus)
2. Apple Pay comes out of 4.2 and moves to 4.3.
   Evidence: "Priya: fine, it was a nice-to-have for this one anyway." and "**Decision: Apple Pay comes out of 4.2 and moves to 4.3.**"
3. The minimum iOS version is raised to 16 starting with 4.2.
   Evidence: "**Agreed: raise minimum iOS to 16 starting with 4.2.**"
4. Dark mode is parked and not included in 4.2.
   Evidence: "Dark mode came up again (Lena). Parked, not for 4.2."

## Action items
| Action | Owner | Deadline |
|---|---|---|
| Fix PW-1182 (ride-end crash) and get it into a TestFlight build | Tom | by Wed 11 Nov |
| Deploy pricing API v2 to staging | Aisha | by Fri 6 Nov |
| Hand final onboarding screens to Tom | Lena | by Mon 9 Nov |
| Full regression pass on the 4.2 release candidate | Marcus | done by Fri 13 Nov |
| Send 4.2 release notes (incl. the iOS 16 requirement) to the support team | Priya | by Fri 13 Nov |
| Bring dark mode back for discussion | Lena | in the Jan planning |

## Open questions and contradictions
- Apple Pay: "SDK update still failing review on the sandbox account." No owner or deadline is recorded for resolving this before 4.3 (Owner: Not stated; Deadline: Not stated).
- The old v1 pricing endpoint "stays up until Android catches up"; no date or owner is recorded for retiring it.
- Marcus "needs everything on staging before he starts regression", but the TestFlight build with the PW-1182 fix is due Wed 11 Nov and regression must be done by Fri 13 Nov; the notes do not say whether that window is enough.

## Handoff summary
Release 4.2 now ships Mon 16 Nov as a single release, without Apple Pay (moved to 4.3) and with a new minimum of iOS 16; dark mode is parked until the Jan planning. Aisha deploys pricing API v2 to staging by Fri 6 Nov, Lena hands final onboarding screens to Tom by Mon 9 Nov, and Tom gets the PW-1182 crash fix into TestFlight by Wed 11 Nov. Marcus then completes the full regression pass on the release candidate by Fri 13 Nov, and Priya sends the release notes, including the iOS 16 requirement, to support by the same day. No owner is named for the failing Apple Pay SDK review or for retiring the v1 pricing endpoint. The next sync is Tue 10 Nov, same time.
