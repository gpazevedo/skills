# Pedalwise release 4.2 sync, 3 Nov 2026: brief

## Decisions

- Release 4.2 moves from Mon 9 Nov to Mon 16 Nov, as a single release (no 4.2 / 4.2.1 split).
- Apple Pay is removed from 4.2 and moves to 4.3.
- Minimum iOS version rises from 15 to 16, starting with 4.2.
- Dark mode is parked and not in 4.2.

## Action items

| Owner | Action | Due |
|---|---|---|
| Aisha Okafor | Deploy pricing API v2 to staging | Fri 6 Nov |
| Lena Varga | Hand final onboarding screens to Tom | Mon 9 Nov |
| Tom Becker | Fix ride-end crash PW-1182 and get it into a TestFlight build | Wed 11 Nov |
| Marcus Hale | Full regression pass on the 4.2 release candidate | Fri 13 Nov |
| Priya Nair | Send 4.2 release notes, including the iOS 16 requirement, to the support team | Fri 13 Nov |
| Lena Varga | Bring dark mode back for discussion | January planning |

## Open questions

- Marcus needs everything on staging before he starts regression. Nobody owns a date for "everything on staging", so his Fri 13 Nov deadline depends on the crash fix and pricing v2 landing first.
- The old pricing v1 endpoint stays up until Android catches up. No date or owner was set for retiring it.

## Handoff summary

Release 4.2 now ships Mon 16 Nov as one release. The ride-end crash (PW-1182, 1.8% of ride-ending sessions on 4.1.3) and pricing API v2 not yet being on staging caused the slip. Apple Pay is dropped to 4.3, and the minimum iOS version rises to 16 (iOS 15 users are 2.1% of monthly active riders), which lets the team remove about 400 lines of map workaround. The critical path is: pricing v2 on staging (6 Nov), onboarding screens (9 Nov), crash fix in TestFlight (11 Nov), then regression and support comms (13 Nov). Next sync is Tue 10 Nov, 10:00.
