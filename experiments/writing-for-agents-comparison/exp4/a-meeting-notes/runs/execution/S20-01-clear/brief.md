# Decision brief: Pedalwise mobile team: release 4.2 sync (Tue 3 Nov 2026)

## Decisions
- 4.2 release moves to Mon 16 Nov, as a single release with no 4.2/4.2.1 split - Evidence: "Agreed: 4.2 release moves to Mon 16 Nov." Single release, no split." (Section 1, Release date)
- Apple Pay comes out of 4.2 and moves to 4.3 - Evidence: "Decision: Apple Pay comes out of 4.2 and moves to 4.3." (Section 2, Scope)
- Minimum iOS version is raised to 16 starting with 4.2 - Evidence: "Agreed: raise minimum iOS to 16 starting with 4.2." (Section 2, Scope)

## Proposals not yet decided
None found in the notes.

## Action items
- Fix PW-1182 and get it into a TestFlight build - Owner: Tom - Deadline: Wed 11 Nov
- Deploy pricing API v2 to staging - Owner: Aisha - Deadline: Fri 6 Nov
- Hand final onboarding screens to Tom - Owner: Lena - Deadline: Mon 9 Nov
- Full regression pass on the 4.2 release candidate - Owner: Marcus - Deadline: Fri 13 Nov
- Send 4.2 release notes (incl. the iOS 16 requirement) to the support team - Owner: Priya - Deadline: Fri 13 Nov
- Bring dark mode back in the Jan planning - Owner: Lena - Deadline: Jan planning (as stated)

## Open questions and contradictions
- Open: Dark mode - "Parked, not for 4.2" (Section 2); revisit in the Jan planning, Lena to bring it back. No decision on 4.3 or later is recorded.
- Open: Apple Pay SDK update "still failing review on the sandbox account" (Section 2); no one is recorded as owning the fix, and the notes give no date for 4.3.
- Contradictions: None found in the notes.

## Handoff summary
Decided: 4.2 ships Mon 16 Nov as a single release, Apple Pay moves to 4.3, and minimum iOS becomes 16 from 4.2. Still undecided: dark mode (parked until Jan planning) and the Apple Pay SDK review failure, which has no owner or date in the notes. Soonest owed is Aisha's pricing API v2 on staging by Fri 6 Nov, then Lena's onboarding screens to Tom by Mon 9 Nov and Tom's PW-1182 TestFlight build by Wed 11 Nov. The main gap is that nothing is recorded about who resolves the Apple Pay review issue for 4.3.
