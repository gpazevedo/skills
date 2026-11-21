# Pedalwise mobile team: release 4.2 sync

**Date:** Tue 3 Nov 2026, 10:00 to 10:40
**Attendees:** Priya Nair (PM, chair), Tom Becker (iOS), Aisha Okafor (backend), Lena Varga (design), Marcus Hale (QA)
**Notes:** Marcus

---

### 1. Release date

- Priya: 4.2 was meant to go Mon 9 Nov. Not realistic with the ride-end crash still open + pricing API not on staging yet.
- Tom: crash fix is understood now, it's the GPS callback firing after the ride is closed. Needs about a week incl. testing.
- Aisha agrees, pricing v2 needs at least till end of this week.
- Short discussion about splitting into 4.2 and 4.2.1. Nobody keen, too much overhead for support.
- **Agreed: 4.2 release moves to Mon 16 Nov.** Single release, no split.

### 2. Scope

- Apple Pay: SDK update still failing review on the sandbox account. Tom doesn't want it blocking everything else.
- Priya: fine, it was a nice-to-have for this one anyway.
- **Decision: Apple Pay comes out of 4.2 and moves to 4.3.**
- Minimum iOS version. Currently iOS 15. Lena's analytics: iOS 15 users are 2.1% of monthly active riders.
- Tom: dropping 15 lets us remove the old map workaround, about 400 lines.
- **Agreed: raise minimum iOS to 16 starting with 4.2.**
- Dark mode came up again (Lena). Parked, not for 4.2. Lena to bring it back in the Jan planning.

### 3. Crash + backend

- Ride-end crash = ticket PW-1182. Crash rate on 4.1.3 is 1.8% of sessions that end a ride.
- **Tom: fix PW-1182 and get it into a TestFlight build by Wed 11 Nov.**
- **Aisha: pricing API v2 deployed to staging by Fri 6 Nov.**
- Aisha mentioned the old v1 endpoint stays up until Android catches up, no change there.

### 4. Design + QA

- Lena: onboarding screens are 80% done, waiting on final copy from Priya (Priya sent it this morning, so unblocked).
- **Lena: final onboarding screens handed to Tom by Mon 9 Nov.**
- Marcus: needs everything on staging before he starts regression.
- **Marcus: full regression pass on the 4.2 release candidate, done by Fri 13 Nov.**

### 5. Comms

- Support team need to know about the iOS 16 change before release, they'll get questions.
- **Priya: send 4.2 release notes (incl. the iOS 16 requirement) to the support team by Fri 13 Nov.**

---

**Summary of decisions:** 4.2 ships Mon 16 Nov, Apple Pay moves to 4.3, minimum iOS 16 from 4.2.

Next sync: Tue 10 Nov, same time.
