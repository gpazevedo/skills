# Decision brief: Pedalwise mobile team: release 4.2 sync
Date: Tue 3 Nov 2026, 10:00 to 10:40  ·  Attendees: Priya Nair (PM, chair), Tom Becker (iOS), Aisha Okafor (backend), Lena Varga (design), Marcus Hale (QA)

## Decisions
1. **The 4.2 release moves from Mon 9 Nov to Mon 16 Nov, as a single release with no 4.2/4.2.1 split.**
   Evidence: "**Agreed: 4.2 release moves to Mon 16 Nov.** Single release, no split." (section 1, Release date)
   Evidence: "Short discussion about splitting into 4.2 and 4.2.1. Nobody keen, too much overhead for support." (section 1, Release date)
   Evidence: "**Summary of decisions:** 4.2 ships Mon 16 Nov, Apple Pay moves to 4.3, minimum iOS 16 from 4.2." (closing summary)
2. **Apple Pay comes out of 4.2 and moves to 4.3.**
   Evidence: "**Decision: Apple Pay comes out of 4.2 and moves to 4.3.**" (section 2, Scope)
   Evidence: "Priya: fine, it was a nice-to-have for this one anyway." (section 2, Scope)
3. **The minimum iOS version rises from iOS 15 to iOS 16, starting with 4.2.**
   Evidence: "**Agreed: raise minimum iOS to 16 starting with 4.2.**" (section 2, Scope)
   Evidence: "**Summary of decisions:** 4.2 ships Mon 16 Nov, Apple Pay moves to 4.3, minimum iOS 16 from 4.2." (closing summary)

## Action items
| Action | Owner | Deadline | Source |
| --- | --- | --- | --- |
| Deploy pricing API v2 to staging | Aisha | Fri 6 Nov | "Aisha: pricing API v2 deployed to staging by Fri 6 Nov." |
| Hand final onboarding screens to Tom | Lena | Mon 9 Nov | "Lena: final onboarding screens handed to Tom by Mon 9 Nov." |
| Fix ride-end crash PW-1182 and get it into a TestFlight build | Tom | Wed 11 Nov | "Tom: fix PW-1182 and get it into a TestFlight build by Wed 11 Nov." |
| Full regression pass on the 4.2 release candidate | Marcus | Fri 13 Nov | "Marcus: full regression pass on the 4.2 release candidate, done by Fri 13 Nov." |
| Send 4.2 release notes, including the iOS 16 requirement, to the support team | Priya | Fri 13 Nov | "Priya: send 4.2 release notes (incl. the iOS 16 requirement) to the support team by Fri 13 Nov." |
| Bring dark mode back for discussion | Lena | the Jan planning | "Lena to bring it back in the Jan planning." |

## Proposals not decided
- Dark mode: raised by Lena; status: "Parked, not for 4.2", to be raised again at the Jan planning; no decision on whether or when it ships.

## Open questions and contradictions
- **Question:** Dark mode is recorded as "Parked, not for 4.2" with no "agreed" or "decided" wording, so this brief treats it as a proposal rather than a decision. Its exclusion from 4.2 went unchallenged, but whether and when it ships later is not settled.
- **Question:** Marcus "needs everything on staging before he starts regression", and his regression pass is due Fri 13 Nov. The PW-1182 fix is due in a TestFlight build only by Wed 11 Nov, and the notes do not say when it reaches staging or when the 4.2 release candidate is cut. How much time regression actually gets is Not stated.
- **Question:** The old pricing v1 endpoint "stays up until Android catches up"; no date or owner for the Android move to v2 is stated.
- **Contradiction:** None recorded.

## Handoff summary
The team agreed to move release 4.2 from Mon 9 Nov to Mon 16 Nov as a single release, to drop Apple Pay from 4.2 and move it to 4.3, and to raise the minimum iOS version to 16 starting with 4.2. Next, Aisha deploys pricing API v2 to staging by Fri 6 Nov, Lena hands the final onboarding screens to Tom by Mon 9 Nov, and Tom gets the PW-1182 ride-end crash fix into TestFlight by Wed 11 Nov. Marcus then runs the full regression pass on the 4.2 release candidate by Fri 13 Nov, and Priya sends the 4.2 release notes, including the iOS 16 requirement, to the support team by the same day. Dark mode remains a proposal, parked for the Jan planning, where Lena will bring it back. Still open: when the crash fix and release candidate reach staging for regression, and when Android moves off the pricing v1 endpoint.
