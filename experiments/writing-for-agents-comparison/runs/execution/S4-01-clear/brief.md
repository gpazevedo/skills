# Decision brief: Pedalwise mobile team: release 4.2 sync

**Date:** Tue 3 Nov 2026, 10:00 to 10:40  **Attendees:** Priya Nair (PM, chair), Tom Becker (iOS), Aisha Okafor (backend), Lena Varga (design), Marcus Hale (QA)

## Handoff summary
Release 4.2 moves from Mon 9 Nov to Mon 16 Nov as a single release (D1), Apple Pay is pushed to 4.3 (D2), the minimum iOS version rises to 16 from 4.2 (D3), and dark mode is parked until the Jan planning (D4, P1). The run-up to release is driven by five dated tasks: Aisha puts pricing API v2 on staging by Fri 6 Nov (A2), Lena hands Tom the onboarding screens by Mon 9 Nov (A3), Tom gets the PW-1182 crash fix into TestFlight by Wed 11 Nov (A1), and Marcus finishes regression and Priya briefs support on the release, both by Fri 13 Nov (A4, A5). Still open: no one is named for the work that follows D2 and D3 (Q1, Q2), and no task or date covers producing the release candidate Marcus needs on staging before regression (Q3). The next sync is Tue 10 Nov (D5).

## Decisions
**D1. Release 4.2 moves from Mon 9 Nov to Mon 16 Nov, as a single release with no 4.2 / 4.2.1 split.**
- Evidence: "4.2 was meant to go Mon 9 Nov." (Priya, section 1, line 11) then "**Agreed: 4.2 release moves to Mon 16 Nov.** Single release, no split." (section 1, line 15)
- Decided by: not stated (recorded as "Agreed"; the split was dropped after "Nobody keen, too much overhead for support", line 14)

**D2. Apple Pay comes out of 4.2 and moves to 4.3.**
- Evidence: "**Decision: Apple Pay comes out of 4.2 and moves to 4.3.**" (section 2, line 21)
- Decided by: not stated (Tom: "doesn't want it blocking everything else", line 19; Priya: "fine, it was a nice-to-have for this one anyway", line 20)

**D3. Minimum iOS version rises from 15 to 16 starting with 4.2.**
- Evidence: "**Agreed: raise minimum iOS to 16 starting with 4.2.**" (section 2, line 24)
- Decided by: not stated (recorded as "Agreed")

**D4. Dark mode is not in 4.2.**
- Evidence: "Dark mode came up again (Lena). Parked, not for 4.2." (section 2, line 25)
- Decided by: not stated

**D5. The next sync is Tue 10 Nov, same time.**
- Evidence: "Next sync: Tue 10 Nov, same time." (line 50)
- Decided by: not stated

## Action items
| # | Action | Owner | Deadline | Evidence |
|---|--------|-------|----------|----------|
| A1 | Fix PW-1182 (ride-end crash) and get it into a TestFlight build | Tom | Wed 11 Nov | "**Tom: fix PW-1182 and get it into a TestFlight build by Wed 11 Nov.**" (section 3, line 30) |
| A2 | Deploy pricing API v2 to staging | Aisha | Fri 6 Nov | "**Aisha: pricing API v2 deployed to staging by Fri 6 Nov.**" (section 3, line 31) |
| A3 | Hand final onboarding screens to Tom | Lena | Mon 9 Nov | "**Lena: final onboarding screens handed to Tom by Mon 9 Nov.**" (section 4, line 37) |
| A4 | Full regression pass on the 4.2 release candidate | Marcus | Fri 13 Nov | "**Marcus: full regression pass on the 4.2 release candidate, done by Fri 13 Nov.**" (section 4, line 39) |
| A5 | Send 4.2 release notes, including the iOS 16 requirement, to the support team | Priya | Fri 13 Nov | "**Priya: send 4.2 release notes (incl. the iOS 16 requirement) to the support team by Fri 13 Nov.**" (section 5, line 44) |
| A6 | Bring dark mode back for discussion | Lena | the Jan planning | "Lena to bring it back in the Jan planning." (section 2, line 25) |

## Proposals (not decided)
**P1. Add dark mode.**
- Raised by: Lena
- Status: parked; Lena to bring it back in the Jan planning (A6)
- Evidence: "Dark mode came up again (Lena). Parked, not for 4.2. Lena to bring it back in the Jan planning." (section 2, line 25)

**P2. Keep the old pricing v1 endpoint up until Android catches up.**
- Raised by: Aisha
- Status: no decision recorded (stated by Aisha as "no change there"; no one is recorded agreeing)
- Evidence: "Aisha mentioned the old v1 endpoint stays up until Android catches up, no change there." (section 3, line 32)

## Open questions and contradictions
- **Q1.** Who owns raising the minimum iOS version to 16 (D3), including removing the old map workaround ("about 400 lines", line 23)? No owner or deadline on the record.
- **Q2.** Who owns the Apple Pay work moved to 4.3 (D2), given the SDK update is "still failing review on the sandbox account" (line 19)? No owner or deadline on the record.
- **Q3.** Who produces the 4.2 release candidate, and by when, so Marcus can start regression (A4)? Marcus "needs everything on staging before he starts regression" (section 4, line 38), but no task or date covers it.
