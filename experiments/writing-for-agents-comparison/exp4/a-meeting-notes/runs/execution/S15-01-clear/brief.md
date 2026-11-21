# Decision brief: Pedalwise mobile team, release 4.2 sync (Tue 3 Nov 2026)

## Decisions

1. **The 4.2 release moves from Mon 9 Nov to Mon 16 Nov, as a single release with no 4.2/4.2.1 split.**
   - Evidence: "Agreed: 4.2 release moves to Mon 16 Nov. Single release, no split."
2. **Apple Pay comes out of 4.2 and moves to 4.3.**
   - Evidence: "Decision: Apple Pay comes out of 4.2 and moves to 4.3." Priya: "fine, it was a nice-to-have for this one anyway."
3. **The minimum iOS version is raised from 15 to 16 starting with 4.2.**
   - Evidence: "Agreed: raise minimum iOS to 16 starting with 4.2."

### Proposals (not yet decided)

- **Dark mode: not for 4.2, revisit in Jan planning.** The notes say "Dark mode came up again (Lena). Parked, not for 4.2. Lena to bring it back in the Jan planning." There is no "agreed" or "decided" wording, so this is treated as a proposal; the notes do not say whether it was formally settled. Still needed: confirmation that it is out of 4.2, and a decision on it at the Jan planning.

## Action items

| Action | Owner | Deadline |
|---|---|---|
| Deploy pricing API v2 to staging | Aisha | Fri 6 Nov |
| Hand final onboarding screens to Tom | Lena | Mon 9 Nov |
| Fix PW-1182 (ride-end crash) and get it into a TestFlight build | Tom | Wed 11 Nov |
| Run full regression pass on the 4.2 release candidate | Marcus | Fri 13 Nov |
| Send 4.2 release notes (incl. the iOS 16 requirement) to the support team | Priya | Fri 13 Nov |
| Bring dark mode back in the Jan planning | Lena | Jan planning (no specific date stated) |

## Open questions and contradictions

- Contradictions: none found between the stated dates and owners.
- Dark mode: the notes say "Parked, not for 4.2" but do not say whether this was agreed by the group (see Proposals).
- Apple Pay: the notes say the "SDK update still failing review on the sandbox account." No owner or action is stated for resolving this before 4.3.
- Android: "the old v1 endpoint stays up until Android catches up." No date or owner is stated for Android catching up.
- Regression: Marcus "needs everything on staging before he starts regression." The notes do not say when regression starts. The stated dates are pricing v2 on staging by Fri 6 Nov and the crash fix in TestFlight by Wed 11 Nov.
- Release notes: the notes do not say who supplies the iOS 16 wording beyond Priya's own action.

## Handoff summary

Decided: 4.2 ships Mon 16 Nov as a single release, Apple Pay moves to 4.3, and the minimum iOS becomes 16 from 4.2. Dark mode was parked for 4.2, but the notes do not clearly say this was settled. Next: Aisha deploys pricing v2 to staging by Fri 6 Nov, Lena hands onboarding screens to Tom by Mon 9 Nov, Tom gets the PW-1182 fix into TestFlight by Wed 11 Nov, and Marcus finishes regression and Priya sends release notes to support, both by Fri 13 Nov. Still open: the Apple Pay SDK review failure has no stated owner or date.
