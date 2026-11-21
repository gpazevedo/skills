# Ticket QB-203977: VAT totals wrong on multi-currency invoices since update

Customer: Lindqvist Marine Supplies Ltd (account LMS-0855)
Product: Quillbill Invoicing
Export of the full ticket history. All timestamps are UTC.
As-of time: 2026-11-10 14:20 UTC. This export was taken at that moment; treat it as the current time for every judgement about elapsed time, deadlines and what is still to come. Do not use the clock of the machine you run on.

---

**2026-11-09 10:47 UTC** | Event: Ticket created from email by Marta Kowalczyk. Priority: P2. Status: New.

**2026-11-09 10:47 UTC** | Marta Kowalczyk (customer, Finance Controller)

> Since your update last week, every multi-currency invoice we issue has the wrong VAT total. The VAT on the invoice doesn't equal the sum of the VAT on the lines. Our auditors require VAT to be rounded line by line, and that is how our account is set up. We've issued about 140 invoices in EUR and NOK since 2 November and I have no confidence in any of them.
>
> Under our Enterprise contract you are required to fix this within 24 hours. Please confirm today.
>
> Marta Kowalczyk
> Finance Controller, Lindqvist Marine Supplies

**2026-11-09 11:20 UTC** | Event: Assigned to Tom Reyes (Support Agent, Tier 1). Status: New → Open.

**2026-11-09 11:20 UTC** | Tom Reyes (Tier 1)

> Hi Marta, thanks for getting in touch. I've started looking at this. Could you send me two or three invoice numbers where you've seen the difference?
>
> Tom

**2026-11-09 12:05 UTC** | Marta Kowalczyk (customer)

> INV-LM-11402, INV-LM-11417 and INV-LM-11431. All in EUR.

**2026-11-09 14:30 UTC** | Internal note, Tom Reyes (not visible to customer)

> Account setting "VAT rounding: per line" is on; last changed 14 March 2026.
>
> The three invoices: each one's invoice VAT total is EUR 0.01 lower than the sum of its line VAT. Confirmed.
>
> Sample: 20 EUR invoices issued 2 to 9 Nov. 7 show a 0.01 difference (5 lower, 2 higher); 13 match. All 9 NOK invoices in the same period: none differ. 11 GBP invoices sampled: none differ.
>
> Reproduced in the customer's sandbox (copy of production settings): new EUR invoice, 3 lines of EUR 10.33 at 20% VAT. Line VAT 2.07 each, sum 6.21. Invoice VAT total shows 6.20, which is 20% of 30.99 rounded. Same invoice in GBP: VAT total 6.21. Looks like per-line rounding isn't applied to EUR invoices.
>
> In the sandbox, switched the rounding setting to "per invoice" and back to "per line": no change for EUR.
>
> Release notes for 8.2.4 (deployed 2 Nov): "Improved currency conversion precision for non-base-currency invoices." Possible link; not confirmed.

**2026-11-09 14:45 UTC** | Tom Reyes (Tier 1)

> Marta, here's what I've confirmed so far:
>
> - The three invoices you sent each have an invoice VAT total EUR 0.01 below the sum of the line VAT.
> - In a sample of 20 EUR invoices since 2 November, 7 have a difference of EUR 0.01 and the other 13 are correct. I found no differences in your NOK invoices (all 9 checked) or GBP invoices (11 checked).
> - I've reproduced the problem in your sandbox. On EUR invoices the VAT total seems to be calculated on the invoice total rather than line by line, even though your account is set to per-line rounding.
>
> A workaround would be to switch to per-invoice rounding, but I understand from your message that your auditors require per-line rounding.
>
> Tom

**2026-11-09 15:30 UTC** | Marta Kowalczyk (customer)

> Correct, per-invoice rounding isn't acceptable to our auditors. Seven out of twenty is bad enough. What I need:
>
> 1. the bug fixed;
> 2. to know whether you will correct the invoices already issued, or whether we have to raise a credit note for each one;
> 3. written confirmation of what you've found, for our auditors.
>
> And please confirm the 24 hours.

**2026-11-10 09:10 UTC** | Tom Reyes (Tier 1)

> Good morning Marta. On your three points:
>
> 1. I'm escalating the fault to our Product Engineering Support team today. I can't give you a fix date.
> 2. I'll ask engineering whether a fix would recalculate invoices already issued. I can't promise that it will, so please don't hold off on anything your auditors need.
> 3. I'll send you a written summary of what we've reproduced, including the sandbox example, by 17:00 UK time today (Tuesday 10 November).
>
> On the 24 hours, I'm not able to confirm contract terms myself. I've asked your Customer Success Manager, Owen Pryce, to go through the service-level terms in your contract with you.
>
> Tom

**2026-11-10 13:55 UTC** | Marta Kowalczyk (customer)

> Fine. Please make sure the summary arrives today. Our auditors are in on Thursday.

**2026-11-10 14:20 UTC** | Event: Escalated to Tier 2 (Product Engineering Support) by Tom Reyes. Status: Open → Escalated. Priority: P2.

**2026-11-10 14:20 UTC** | Internal note, Tom Reyes (escalation note)

> Per-line VAT rounding not applied to some EUR invoices since 8.2.4 (2 Nov). Reproduced in sandbox, details above. No differences found in NOK or GBP samples. Customer can't use per-invoice rounding (auditors). Open asks: fix; whether issued invoices will be recalculated; written summary for auditors, which I've promised by 17:00 UK time today and haven't sent yet. Auditors on site Thursday 12 Nov.
