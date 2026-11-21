# Handoff: QB-203977, Lindqvist Marine Supplies Ltd (LMS-0855)

As of 2026-11-10 14:20 UTC. Escalated Tier 1 (Tom Reyes) to Tier 2 Product Engineering Support. Priority P2.

## 1. Problem as currently understood
Since release 8.2.4 (deployed 2 Nov), some EUR invoices show an invoice VAT total that differs by EUR 0.01 from the sum of line VAT, although the account is set to per-line VAT rounding. NOK and GBP samples show no difference. Account: Quillbill Trade, Quillbill Invoicing (cloud), UK data region, base currency GBP, EUR/NOK/GBP enabled (account record).

*Reported by customer*
- Every multi-currency invoice since the update has wrong VAT; about 140 EUR and NOK invoices issued since 2 Nov (Marta Kowalczyk, 9 Nov 10:47).
- Auditors require per-line rounding; per-invoice rounding is not acceptable (Marta, 9 Nov 15:30).
- Example invoices INV-LM-11402, INV-LM-11417, INV-LM-11431, all EUR (Marta, 9 Nov 12:05).
- Auditors on site Thursday 12 Nov (Marta, 10 Nov 13:55; account record flag says 12 to 13 Nov).

*Verified by support* (Tom Reyes, internal note 9 Nov 14:30)
- Account setting "VAT rounding: per line" is on, last changed 14 Mar 2026 (read from account).
- The three invoices each have invoice VAT EUR 0.01 below the sum of line VAT (checked invoices).
- Sample of 20 EUR invoices issued 2 to 9 Nov: 7 differ by 0.01 (5 lower, 2 higher), 13 match. All 9 NOK sampled and 11 GBP sampled: no difference.
- Reproduced in the customer's sandbox: EUR invoice, 3 lines of EUR 10.33 at 20%; line VAT 2.07 each (sum 6.21), invoice VAT 6.20 (20% of 30.99). Same invoice in GBP gives 6.21.
- In sandbox, switching rounding to "per invoice" and back to "per line" changed nothing for EUR.

*Unverified hypotheses*
- Per-line rounding is not applied to EUR invoices / VAT is computed on the invoice total (Tom, from one sandbox case).
- Release 8.2.4 note "Improved currency conversion precision for non-base-currency invoices" is the cause (Tom: "possible link; not confirmed").

## 2. Tried and result
- 9 Nov 11:20, Tom: asked customer for example invoices. Worked (customer sent three, 12:05).
- 9 Nov 14:30, Tom: checked three invoices and sampled 20 EUR, 9 NOK, 11 GBP invoices. Worked (see above).
- 9 Nov 14:30, Tom: reproduced in sandbox. Worked.
- 9 Nov 14:30, Tom: toggled rounding setting per invoice and back in sandbox. Failed (no change for EUR).
- 10 Nov 09:10, Tom: asked CSM Owen Pryce to go through the contract service-level terms with the customer. No response recorded in thread.
- 10 Nov 14:20, Tom: escalated to Tier 2. Done.
- Customer-side attempts: none stated in thread.

## 3. Commitments to the customer
- Written summary of what was reproduced, including the sandbox example, by 17:00 UK time on 10 Nov (17:00 UTC, as the UK is on GMT in November). Tom Reyes, 10 Nov 09:10. OPEN, not yet sent as of 14:20; 2h40m remaining. Customer expects it today for auditors (13:55).
- Ask engineering whether a fix would recalculate already-issued invoices. Tom, 10 Nov 09:10. OPEN. Tom explicitly did not promise recalculation.
- CSM to go through service-level terms with the customer. Tom, 10 Nov 09:10 (stated as a request made). OPEN, no confirmation it happened.
- No fix date promised; Tom said he cannot give one. The 24-hour fix and "confirm today" are the customer's demand (9 Nov), not a commitment by support. No one at support has confirmed a 24-hour term.

## 4. Service-level status and deadline
Blocked: support policy not supplied. No deadline and no service-level terms are given.
- Tier from account record: Enterprise, terms in MSA Schedule 3 (Schedule 3 itself not supplied).
- Clock start candidate from thread: ticket created 9 Nov 10:47 UTC at P2. Severity classification is not stated in any supplied source.
- Customer's claim of a "24 hour" fix is unverified; do not treat it as the term.
- Deadline: Not determinable.

## 5. Recommended next action (support's judgement, not a commitment)
First: Tier 2 owner (Product Engineering Support on-call) ensures the written summary goes to Marta before 17:00 UTC today (10 Nov), using the sandbox example and sample counts above, clearly separating verified findings from the unconfirmed 8.2.4 hypothesis. This is the next customer-facing touchpoint and is due in 2h40m.
Alternatives:
- Confirm with Tom or Owen Pryce that the summary is being sent by Tier 1 with Tier 2 input, so it is not missed, because Tom still holds the promise.
- Have Tier 2 check the 8.2.4 change for per-line rounding on non-base-currency invoices and ask Owen for the Schedule 3 terms, because the deadline and the invoice-recalculation answer are both undetermined and auditors arrive 12 Nov.

## 6. Open questions
- Support policy and MSA Schedule 3: severity definition, response and fix targets, clock rules. Please supply; needed for section 4.
- Is P2 the correct severity given the audit on 12 to 13 Nov?
- Why are only some EUR invoices affected (7 of 20) and none of NOK or GBP? Does the pattern depend on the rounding of line amounts?
- Marta says "every" multi-currency invoice is wrong; verified evidence shows 7 of 20 EUR and 0 of 9 NOK. Extent across the ~140 invoices is unmeasured.
- Will a fix recalculate issued invoices, or must the customer raise credit notes?
- Has Owen Pryce contacted the customer?
- Is the account's rounding setting honoured elsewhere (e.g. PDF output) after 8.2.4?
