# Decision brief: Pedalwise mobile team, release 4.2 sync (Tue 3 Nov 2026)

Citations refer to the section headings in the notes (Section 1 to 5, Summary).

## Decisions

1. The 4.2 release moves to Mon 16 Nov, as a single release with no 4.2/4.2.1 split.
   Evidence: "Agreed: 4.2 release moves to Mon 16 Nov. Single release, no split." (Section 1)

2. Apple Pay is removed from 4.2 and moves to 4.3.
   Evidence: "Decision: Apple Pay comes out of 4.2 and moves to 4.3." (Section 2)

3. The minimum iOS version is raised to 16 starting with 4.2.
   Evidence: "Agreed: raise minimum iOS to 16 starting with 4.2." (Section 2)

4. Dark mode is not in 4.2 (parked).
   Evidence: "Parked, not for 4.2." (Section 2)

### Proposals not yet decided

None found in the notes. (The 4.2/4.2.1 split was discussed and not adopted; see Decision 1.)

## Action items

| Action | Owner | Deadline | Evidence |
|---|---|---|---|
| Fix PW-1182 and get it into a TestFlight build | Tom | Wed 11 Nov | "Tom: fix PW-1182 and get it into a TestFlight build by Wed 11 Nov." (Section 3) |
| Deploy pricing API v2 to staging | Aisha | Fri 6 Nov | "Aisha: pricing API v2 deployed to staging by Fri 6 Nov." (Section 3) |
| Hand final onboarding screens to Tom | Lena | Mon 9 Nov | "Lena: final onboarding screens handed to Tom by Mon 9 Nov." (Section 4) |
| Full regression pass on the 4.2 release candidate | Marcus | Fri 13 Nov | "Marcus: full regression pass on the 4.2 release candidate, done by Fri 13 Nov." (Section 4) |
| Send 4.2 release notes (including the iOS 16 requirement) to the support team | Priya | Fri 13 Nov | "Priya: send 4.2 release notes (incl. the iOS 16 requirement) to the support team by Fri 13 Nov." (Section 5) |
| Bring dark mode back in the Jan planning | Lena | Jan planning (no date stated) | "Lena to bring it back in the Jan planning." (Section 2) |

## Open questions and contradictions

### Open questions

- Apple Pay: the SDK update is "still failing review on the sandbox account" (Section 2). The notes do not say who will resolve this or by when for 4.3.
- The old v1 pricing endpoint "stays up until Android catches up" (Section 3). No Android date or owner is stated.
- Marcus "needs everything on staging before he starts regression" (Section 4). The notes do not say when the regression starts or whether Tom's TestFlight build (Wed 11 Nov) counts as "everything"; it is not stated how the 13 Nov regression deadline fits with that dependency.
- The date of the Jan planning session is not stated.
- Attendees' next sync is "Tue 10 Nov, same time" (Summary); no agenda or owner for it is stated.

### Contradictions

None found in the notes. (The original 9 Nov release date was replaced by the 16 Nov decision in Section 1; that is a recorded change, not a conflict.)

## Handoff summary

Decided: 4.2 ships Mon 16 Nov as a single release, Apple Pay moves to 4.3, and the minimum iOS version becomes 16 from 4.2. No proposals are pending, and dark mode is parked for Jan planning. The nearest deadline is Aisha's pricing API v2 on staging by Fri 6 Nov. The most important unresolved item is that Marcus's regression (due Fri 13 Nov) depends on everything being on staging, and the notes do not say when that will be complete, given the crash fix is due in TestFlight on Wed 11 Nov.
