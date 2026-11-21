# Decision brief: Pedalwise mobile team: release 4.2 sync
Tue 3 Nov 2026, 10:00 to 10:40. Attendees: Priya Nair (PM, chair), Tom Becker (iOS), Aisha Okafor (backend), Lena Varga (design), Marcus Hale (QA). Notes: Marcus.

## Handoff summary
Release 4.2 moves from Mon 9 Nov to Mon 16 Nov as a single release with no 4.2.1 split, Apple Pay moves out to 4.3, and the minimum iOS version rises to 16 starting with 4.2. Before release, Aisha deploys pricing API v2 to staging by Fri 6 Nov, Lena hands final onboarding screens to Tom by Mon 9 Nov, and Tom gets the PW-1182 ride-end crash fix into a TestFlight build by Wed 11 Nov. Marcus then runs the full regression pass on the 4.2 release candidate by Fri 13 Nov, and Priya sends release notes (including the iOS 16 requirement) to the support team by Fri 13 Nov. The biggest open point is the tight run-up to regression: Marcus needs everything on staging before he starts, the crash fix is only due Wed 11 Nov, and his pass is due Fri 13 Nov. The next sync is Tue 10 Nov, same time.

## Decisions
1. Release 4.2 moves to Mon 16 Nov as a single release, with no split into 4.2 and 4.2.1. This reverses the earlier plan to ship on Mon 9 Nov.
   Evidence: "Agreed: 4.2 release moves to Mon 16 Nov. Single release, no split." (§1 Release date); earlier plan: "4.2 was meant to go Mon 9 Nov." (§1 Release date, Priya)
2. Apple Pay comes out of 4.2 and moves to 4.3.
   Evidence: "Decision: Apple Pay comes out of 4.2 and moves to 4.3." (§2 Scope)
3. The minimum iOS version rises from iOS 15 to iOS 16, starting with 4.2.
   Evidence: "Agreed: raise minimum iOS to 16 starting with 4.2." (§2 Scope)
4. Dark mode is not in 4.2; it is parked.
   Evidence: "Dark mode came up again (Lena). Parked, not for 4.2." (§2 Scope)

## Action items
| Action | Owner | Deadline | Notes |
|---|---|---|---|
| Deploy pricing API v2 to staging | Aisha | by Fri 6 Nov | §3 Crash + backend. Old v1 endpoint stays up until Android catches up. |
| Hand final onboarding screens to Tom | Lena | by Mon 9 Nov | §4 Design + QA. Was waiting on final copy from Priya; notes say Priya sent it, so unblocked. |
| Fix PW-1182 (ride-end crash) and get it into a TestFlight build | Tom | by Wed 11 Nov | §3 Crash + backend. Cause per Tom: GPS callback firing after the ride is closed. |
| Full regression pass on the 4.2 release candidate | Marcus | by Fri 13 Nov | §4 Design + QA. Depends on everything being on staging first ("needs everything on staging before he starts regression"). |
| Send 4.2 release notes (incl. the iOS 16 requirement) to the support team | Priya | by Fri 13 Nov | §5 Comms. Follows from decision 3. |
| Bring dark mode back for discussion | Lena | "in the Jan planning" | §2 Scope. Follows from decision 4. |

## Open questions and contradictions
- **Open:** Regression timing. Marcus "needs everything on staging before he starts regression" (§4 Design + QA), but the crash fix is only due in TestFlight "by Wed 11 Nov" (§3) and the regression pass is due "by Fri 13 Nov" (§4). The notes do not say whether the crash fix counts as part of "everything on staging", or what happens to the Mon 16 Nov date if any input slips.
- **Open:** Apple Pay for 4.3. The SDK update is "still failing review on the sandbox account" (§2 Scope, Tom); the notes record no owner or deadline for getting it through review for 4.3.
- **Open:** Removing the old map workaround. Tom said "dropping 15 lets us remove the old map workaround, about 400 lines" (§2 Scope); the notes do not say whether this removal is part of 4.2, and record no owner or deadline for it.
- **Open:** Dark mode itself is unresolved beyond 4.2: "Parked, not for 4.2. Lena to bring it back in the Jan planning." (§2 Scope)
- **Open:** Pricing API v1 retirement. "the old v1 endpoint stays up until Android catches up, no change there" (§3 Crash + backend, Aisha); the notes give no date for Android catching up.
- **Contradiction:** None recorded in the notes.
