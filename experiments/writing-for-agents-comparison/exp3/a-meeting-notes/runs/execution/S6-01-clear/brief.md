# Decision brief: Pedalwise mobile team: release 4.2 sync (Tue 3 Nov 2026)

## Decisions
1. **The 4.2 release moves from Mon 9 Nov to Mon 16 Nov, as a single release with no 4.2 / 4.2.1 split.**
   Evidence: "**Agreed: 4.2 release moves to Mon 16 Nov.** Single release, no split." (§1 Release date, line 15); replaces "4.2 was meant to go Mon 9 Nov" (§1, line 11, Priya)
2. **Apple Pay comes out of 4.2 and moves to 4.3.**
   Evidence: "**Decision: Apple Pay comes out of 4.2 and moves to 4.3.**" (§2 Scope, line 21)
3. **The minimum iOS version rises from iOS 15 to iOS 16, starting with 4.2.**
   Evidence: "**Agreed: raise minimum iOS to 16 starting with 4.2.**" (§2 Scope, line 24)

## Action items
| # | Action | Owner | Deadline | Source |
|---|--------|-------|----------|--------|
| A1 | Fix PW-1182 (ride-end crash) and get it into a TestFlight build | Tom | Wed 11 Nov | "**Tom: fix PW-1182 and get it into a TestFlight build by Wed 11 Nov.**" (§3 Crash + backend, line 30) |
| A2 | Deploy pricing API v2 to staging | Aisha | Fri 6 Nov | "**Aisha: pricing API v2 deployed to staging by Fri 6 Nov.**" (§3 Crash + backend, line 31) |
| A3 | Hand final onboarding screens to Tom | Lena | Mon 9 Nov | "**Lena: final onboarding screens handed to Tom by Mon 9 Nov.**" (§4 Design + QA, line 37) |
| A4 | Full regression pass on the 4.2 release candidate | Marcus | Fri 13 Nov | "**Marcus: full regression pass on the 4.2 release candidate, done by Fri 13 Nov.**" (§4 Design + QA, line 39) |
| A5 | Send 4.2 release notes, including the iOS 16 requirement, to the support team | Priya | Fri 13 Nov | "**Priya: send 4.2 release notes (incl. the iOS 16 requirement) to the support team by Fri 13 Nov.**" (§5 Comms, line 44) |
| A6 | Bring dark mode back for discussion | Lena | the Jan planning | "Lena to bring it back in the Jan planning." (§2 Scope, line 25) |

## Open questions and contradictions
### Open questions
- Q1. Who cuts the 4.2 release candidate, and by when, so that "everything" is on staging before Marcus starts regression? Owner and date are unresolved. A1 delivers the crash fix to a TestFlight build, not explicitly to staging. (§4 Design + QA, lines 38 to 39; §3, line 30)
- Q2. Who carries out the iOS 16 minimum change for 4.2 (including removing the old map workaround Tom mentioned)? Owner and deadline are unresolved. (§2 Scope, lines 23 to 24)
- Q3. When will Android "catch up" so the old pricing v1 endpoint can be retired? Date and owner are unresolved; the notes say "no change there" for now. (§3 Crash + backend, line 32)
### Proposed, not decided
- P1. Dark mode (raised by Lena): "Dark mode came up again (Lena). Parked, not for 4.2." (§2 Scope, line 25). Status: parked, not in 4.2; to be raised again at the Jan planning (see A6).
### Contradictions
No contradictions found in the notes.

## Handoff summary
The team agreed to move 4.2 from Mon 9 Nov to Mon 16 Nov as a single release, to drop Apple Pay to 4.3, and to raise the minimum iOS version to 16 from 4.2 (§1 line 15; §2 lines 21, 24). Before release, Aisha deploys pricing API v2 to staging by Fri 6 Nov, Lena hands final onboarding screens to Tom by Mon 9 Nov, and Tom gets the PW-1182 crash fix into TestFlight by Wed 11 Nov (§3 lines 30 to 31; §4 line 37). Marcus runs full regression on the release candidate by Fri 13 Nov, and Priya sends release notes with the iOS 16 requirement to support by Fri 13 Nov (§4 line 39; §5 line 44). Still open: who cuts the release candidate and when, who owns the iOS 16 change, and when the pricing v1 endpoint can go; dark mode is parked until the Jan planning (§2 lines 23 to 25; §3 line 32; §4 line 38). The next sync is Tue 10 Nov, same time (line 50).
