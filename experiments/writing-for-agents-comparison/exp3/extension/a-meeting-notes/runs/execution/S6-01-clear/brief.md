# Decision brief: Pedalwise mobile team: release 4.2 sync
Date: Tue 3 Nov 2026, 10:00 to 10:40. Attendees: Priya Nair (PM, chair), Tom Becker (iOS), Aisha Okafor (backend), Lena Varga (design), Marcus Hale (QA). Notes: Marcus.

## Handoff summary
Release 4.2 moves from Mon 9 Nov to Mon 16 Nov as a single release, Apple Pay moves out of 4.2 to 4.3, and the minimum iOS version rises to 16 starting with 4.2. Next, Aisha puts pricing API v2 on staging by Fri 6 Nov, Lena hands the final onboarding screens to Tom by Mon 9 Nov, Tom gets the PW-1182 crash fix into a TestFlight build by Wed 11 Nov, and Marcus finishes regression on the release candidate by Fri 13 Nov. Priya sends the 4.2 release notes, including the iOS 16 requirement, to the support team by Fri 13 Nov. Dark mode is parked and not in 4.2, with Lena to bring it back at the Jan planning. Still unresolved: when and by whom the 4.2 release candidate is cut, the 4.3 timing for Apple Pay, and how long the v1 pricing endpoint stays up.

## Decisions
1. The 4.2 release moves from Mon 9 Nov to Mon 16 Nov, as a single release with no split into 4.2 and 4.2.1.
   - Evidence: "**Agreed: 4.2 release moves to Mon 16 Nov.** Single release, no split." (section 1, Release date)
2. Apple Pay comes out of 4.2 and moves to 4.3.
   - Evidence: "**Decision: Apple Pay comes out of 4.2 and moves to 4.3.**" (section 2, Scope)
3. The minimum iOS version rises from iOS 15 to iOS 16, starting with 4.2.
   - Evidence: "**Agreed: raise minimum iOS to 16 starting with 4.2.**" (section 2, Scope)

## Action items
| Action | Owner | Deadline | Source |
|---|---|---|---|
| Fix PW-1182 (ride-end crash) and get it into a TestFlight build | Tom | Wed 11 Nov | "Tom: fix PW-1182 and get it into a TestFlight build by Wed 11 Nov." |
| Deploy pricing API v2 to staging | Aisha | Fri 6 Nov | "Aisha: pricing API v2 deployed to staging by Fri 6 Nov." |
| Hand final onboarding screens to Tom | Lena | Mon 9 Nov | "Lena: final onboarding screens handed to Tom by Mon 9 Nov." |
| Full regression pass on the 4.2 release candidate | Marcus | Fri 13 Nov | "Marcus: full regression pass on the 4.2 release candidate, done by Fri 13 Nov." |
| Send 4.2 release notes (incl. the iOS 16 requirement) to the support team | Priya | Fri 13 Nov | "Priya: send 4.2 release notes (incl. the iOS 16 requirement) to the support team by Fri 13 Nov." |
| Bring dark mode back for discussion | Lena | the Jan planning | "Lena to bring it back in the Jan planning." |

## Proposals not decided
- Split the release into 4.2 and 4.2.1 (raised in discussion, no name stated); rejected, superseded by decision 1 ("Single release, no split").
- Dark mode (raised by Lena); recorded as "Parked, not for 4.2", with no decision on whether or when it ships.
- Remove the old map workaround, about 400 lines, once iOS 15 is dropped (raised by Tom); given as a benefit of decision 3, not recorded as agreed work.

## Open questions and contradictions
- Who cuts the 4.2 release candidate, and by when? Marcus "needs everything on staging before he starts regression", but no date or owner is stated for the release candidate, and Tom's crash fix lands only on Wed 11 Nov, two days before regression must be done.
- Who submits 4.2 to the App Store for the Mon 16 Nov release? Owner: not stated.
- When does 4.3 ship, and who owns getting the Apple Pay SDK update through review on the sandbox account? Not stated.
- Is removing the old map workaround part of 4.2, and if so who does it and by when? Not stated.
- How long does the v1 pricing endpoint stay up? The notes say only "until Android catches up", with no date or owner.
- Dark mode: "the Jan planning" has no exact date; is dark mode a candidate for 4.3 or later? Not stated.
- Contradiction: None recorded in the notes.
