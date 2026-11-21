# Decision brief: Pedalwise mobile team: release 4.2 sync

Date: Tue 3 Nov 2026

## Decisions

| Decision | Evidence |
| --- | --- |
| The 4.2 release moves to Mon 16 Nov as a single release, with no split into 4.2 and 4.2.1. This is a revision: it replaces the earlier plan to release on Mon 9 Nov ("4.2 was meant to go Mon 9 Nov", Priya). | "Agreed: 4.2 release moves to Mon 16 Nov. Single release, no split." (section 1) |
| Apple Pay comes out of 4.2 and moves to 4.3. | "Decision: Apple Pay comes out of 4.2 and moves to 4.3." (section 2) |
| The minimum iOS version is raised to iOS 16, starting with 4.2. | "Agreed: raise minimum iOS to 16 starting with 4.2." (section 2) |

## Proposals (not decided)

| Proposal | Proposed by | Condition or status | Evidence |
| --- | --- | --- | --- |
| Split the release into 4.2 and 4.2.1. | Not stated | Not adopted: the decision on the release date says "Single release, no split." | "Short discussion about splitting into 4.2 and 4.2.1. Nobody keen, too much overhead for support." (section 1) |
| Dark mode. | Lena | Parked, not for 4.2; to come back in the Jan planning. | "Dark mode came up again (Lena). Parked, not for 4.2." (section 2) |
| Keep the old v1 pricing endpoint up until Android catches up. | Aisha | No commitment signal; stated as current status. See open questions. | "Aisha mentioned the old v1 endpoint stays up until Android catches up, no change there." (section 3) |

## Action items

| Action | Owner | Deadline | Evidence |
| --- | --- | --- | --- |
| Fix PW-1182 (ride-end crash) and get it into a TestFlight build. | Tom | Wed 11 Nov | "Tom: fix PW-1182 and get it into a TestFlight build by Wed 11 Nov." (section 3) |
| Deploy pricing API v2 to staging. | Aisha | Fri 6 Nov | "Aisha: pricing API v2 deployed to staging by Fri 6 Nov." (section 3) |
| Hand the final onboarding screens to Tom. | Lena | Mon 9 Nov | "Lena: final onboarding screens handed to Tom by Mon 9 Nov." (section 4) |
| Complete a full regression pass on the 4.2 release candidate. | Marcus | Fri 13 Nov | "Marcus: full regression pass on the 4.2 release candidate, done by Fri 13 Nov." (section 4) |
| Send the 4.2 release notes, including the iOS 16 requirement, to the support team. | Priya | Fri 13 Nov | "Priya: send 4.2 release notes (incl. the iOS 16 requirement) to the support team by Fri 13 Nov." (section 5) |
| Bring dark mode back for discussion. | Lena | the Jan planning | "Lena to bring it back in the Jan planning." (section 2) |

## Open questions and contradictions

### Open questions
- Dark mode: deferred, not resolved. It was parked for 4.2 and is to be raised again at the Jan planning: "Parked, not for 4.2. Lena to bring it back in the Jan planning." (section 2)
- Old v1 pricing endpoint: was keeping it up until Android catches up decided, and when is that expected? The notes record it only as a remark with no commitment signal and no date: "Aisha mentioned the old v1 endpoint stays up until Android catches up, no change there." (section 3)

### Contradictions
None recorded in the notes.

## Handoff summary

The 4.2 release moved from Mon 9 Nov to Mon 16 Nov as a single release with no split, Apple Pay moves out of 4.2 to 4.3, and the minimum iOS version rises to iOS 16 starting with 4.2. Aisha deploys pricing API v2 to staging by Fri 6 Nov, Lena hands the final onboarding screens to Tom by Mon 9 Nov, and Tom fixes the ride-end crash PW-1182 and gets it into a TestFlight build by Wed 11 Nov. Marcus completes a full regression pass on the 4.2 release candidate by Fri 13 Nov, and Priya sends the 4.2 release notes, including the iOS 16 requirement, to the support team by Fri 13 Nov. Still unresolved: dark mode is parked until Lena brings it back in the Jan planning, and it is unclear whether keeping the old v1 pricing endpoint up until Android catches up was decided.
