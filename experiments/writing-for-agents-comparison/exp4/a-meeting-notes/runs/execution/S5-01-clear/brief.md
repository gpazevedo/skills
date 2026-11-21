# Decision brief: Pedalwise mobile team, release 4.2 sync (Tue 3 Nov 2026)

## 1. Decisions

1. **4.2 release moves to Mon 16 Nov, as a single release with no split into 4.2 and 4.2.1.**
   Evidence: "Agreed: 4.2 release moves to Mon 16 Nov. Single release, no split." Context: the ride-end crash is still open and the pricing API is not on staging (Priya); nobody favoured a split.
2. **Apple Pay comes out of 4.2 and moves to 4.3.**
   Evidence: "Decision: Apple Pay comes out of 4.2 and moves to 4.3." Tom raised it; Priya: "fine, it was a nice-to-have for this one anyway."
3. **Minimum iOS version is raised to 16 starting with 4.2.**
   Evidence: "Agreed: raise minimum iOS to 16 starting with 4.2." Rationale in the notes: iOS 15 users are 2.1% of monthly active riders (Lena's analytics); dropping 15 removes about 400 lines of map workaround (Tom).
4. **Dark mode is not in 4.2.**
   Evidence: "Dark mode came up again (Lena). Parked, not for 4.2."
5. **The pricing v2 and crash fix commitments are recorded as owner-stated deliverables** (see Action items): Tom, PW-1182 fix in a TestFlight build by Wed 11 Nov; Aisha, pricing API v2 on staging by Fri 6 Nov.
   Evidence: bolded entries "Tom: fix PW-1182 and get it into a TestFlight build by Wed 11 Nov" and "Aisha: pricing API v2 deployed to staging by Fri 6 Nov."

## 2. Proposals not yet decided

None found in the notes.

(The 4.2 / 4.2.1 split was discussed and rejected, so it is not a live proposal.)

## 3. Action items

| Action | Owner | Deadline |
|---|---|---|
| Deploy pricing API v2 to staging | Aisha | Fri 6 Nov |
| Hand final onboarding screens to Tom | Lena | Mon 9 Nov |
| Fix PW-1182 and get it into a TestFlight build | Tom | Wed 11 Nov |
| Full regression pass on the 4.2 release candidate | Marcus | Fri 13 Nov |
| Send 4.2 release notes (incl. the iOS 16 requirement) to the support team | Priya | Fri 13 Nov |
| Bring dark mode back in the Jan planning | Lena | "the Jan planning" (no exact date stated) |
| Resolve the Apple Pay SDK review failure on the sandbox account | Not stated | Not stated |

Note: the last row is not an explicit action in the notes; it is the open issue behind the Apple Pay move, listed unowned. Its work is for 4.3 and no date is given.

## 4. Open questions and contradictions

**Open questions**
- Apple Pay SDK update "still failing review on the sandbox account": cause, owner and target date are Not stated. It moves to 4.3, but no 4.3 date is given.
- Jan planning: the date of the meeting is Not stated.
- Android catching up to the v1 pricing endpoint: Aisha said v1 "stays up until Android catches up"; no date or owner for that is Not stated.
- Release candidate: the notes do not say who cuts the 4.2 release candidate or when. Marcus "needs everything on staging before he starts regression"; the only dated inputs are the Wed 11 Nov TestFlight build (Tom) and Fri 13 Nov regression finish (Marcus). Whether the candidate exists in time for Marcus is Not stated.
- Whether the support team has been or will be told about the iOS 16 change earlier than the Fri 13 Nov release notes: Not stated.

**Contradictions**
None found in the notes. (Aisha's "pricing v2 needs at least till end of this week" and the Fri 6 Nov staging deadline are consistent.)

## 5. Handoff summary

4.2 now ships Mon 16 Nov as a single release; Apple Pay moves to 4.3, minimum iOS becomes 16 from 4.2, and dark mode is not in 4.2. Owed: Aisha pricing v2 on staging by Fri 6 Nov, Lena onboarding screens to Tom by Mon 9 Nov, Tom the PW-1182 fix in TestFlight by Wed 11 Nov, Marcus regression by Fri 13 Nov, and Priya release notes to support by Fri 13 Nov. Lena is to bring dark mode back in the Jan planning (date Not stated). Unresolved: the Apple Pay SDK review failure has no owner or date, and who produces the release candidate for regression is not stated. The next sync is Tue 10 Nov.
