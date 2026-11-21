# Ticket QB-204518: Recurring invoices created but not sent

Customer: Harrow & Finch Accounting Ltd (account HF-0192)
Product: Quillbill Invoicing, Recurring Billing add-on
Export of the full ticket history. All timestamps are UTC.

---

**2026-11-12 09:14 UTC** | Event: Ticket created via support portal by Daniel Okafor. Priority: P2. Status: New.

**2026-11-12 09:14 UTC** | Daniel Okafor (customer, Finance Systems Lead)

> Hello,
>
> Our recurring invoices ran this morning but nothing has gone out to clients. We bill our retainer clients on the 12th of each month, and around 110 invoices should have been emailed at 07:00. In the invoice list they all show "Queued". As far as we can tell not one client has received theirs, and two clients have already rung to ask where it is. We haven't changed any settings on our side.
>
> Our clients' payment terms run from the send date, so every day this waits pushes back our collections. The next runs are tomorrow (the 13th) and Sunday (the 15th). Please treat this as urgent.
>
> Daniel Okafor
> Finance Systems Lead, Harrow & Finch

**2026-11-12 09:41 UTC** | Event: Assigned to Priya Nair (Support Agent, Tier 1). Status: New → Open.

**2026-11-12 09:41 UTC** | Priya Nair (Tier 1)

> Hi Daniel,
>
> Thanks for the detail. I'm looking at your account now. Could you send me the number of one invoice that should have gone out this morning, and tell me whether I may send that one invoice from our side as a test? It would go to your client exactly as it would have at 07:00.
>
> Priya

**2026-11-12 09:58 UTC** | Daniel Okafor (customer)

> INV-2026-11-0457, to Meadowgate Ltd, from the schedule "Meadowgate monthly retainer". Yes, go ahead and send it. It should have gone today anyway.

**2026-11-12 10:20 UTC** | Internal note, Priya Nair (not visible to customer)

> Job log for HF-0192: the recurring run at 07:00:03 UTC today generated 112 invoices. All 112 are in dispatch state "Queued - not dispatched". The dispatcher shows 0 send attempts and no errors for them.
>
> All 112 come from schedules created before 10 Nov (the v8.3 release). The account has 3 schedules created after 10 Nov; none was due today, so there is no direct comparison yet.
>
> Known issues: KI-3381 "Legacy recurring schedules skip auto-send after v8.3", opened by Engineering on 11 Nov, status Investigating, 2 other customers linked. Symptoms match. Not confirmed as the same cause.
>
> Test 1: manual Send on INV-2026-11-0457 from the invoice list at 10:15. Delivery log shows it accepted by the recipient's mail server at 10:16.
>
> Test 2: opened schedule "Meadowgate monthly retainer", saved it without changes, then used "Run now (test mode)", which sends only to the account owner. The test invoice was dispatched within 40 seconds. So re-saving seems to clear the fault for that schedule, at least in test mode. Not yet seen on a real scheduled run.

**2026-11-12 10:34 UTC** | Priya Nair (Tier 1)

> Daniel, here's where things stand.
>
> - Your 07:00 run created 112 invoices, and all 112 are queued but have not been dispatched. Our system shows no attempt to send them.
> - I sent INV-2026-11-0457 to Meadowgate manually at 10:15, and their mail server accepted it at 10:16.
> - Our engineering team is already investigating a known issue that looks like yours: schedules created before our 10 November release not sending automatically. I can't yet confirm that yours has the same cause.
> - In a test, re-saving one schedule appeared to restore automatic sending for that schedule.
>
> For today, the other 111 invoices can be sent from the invoice list: filter by status "Queued", select up to 50 at a time and choose Send.
>
> Priya

**2026-11-12 10:52 UTC** | Daniel Okafor (customer)

> Thanks Priya. We'll bulk-send today's 111 ourselves this afternoon. But we have 340 schedules, so re-saving each one by hand isn't realistic. Tomorrow's 07:00 run has 64 invoices and Sunday's has 90. Can you guarantee this will be fixed before tomorrow morning's run?

**2026-11-12 11:05 UTC** | Priya Nair (Tier 1)

> I understand, Daniel. I can't promise a fix time, because that depends on what engineering finds. I'm escalating your ticket to our Product Engineering Support team now, and I'll make sure they know your next run is at 07:00 UTC tomorrow, 13 November, with 64 invoices.
>
> I will email you an update by 16:00 UTC today with what they've found, even if that is only that they are still investigating.
>
> Priya

**2026-11-12 11:30 UTC** | Event: Escalated to Tier 2 (Product Engineering Support) by Priya Nair. Linked to known issue KI-3381. Status: Open → Escalated. Priority: P2 (unchanged).

**2026-11-12 11:30 UTC** | Internal note, Priya Nair (escalation note)

> Escalating: 112 invoices from pre-v8.3 recurring schedules stuck "Queued - not dispatched" after the 07:00 run; matches KI-3381. Manual send works; re-save plus test-mode run works for one schedule. Customer has 340 schedules; next runs 13 Nov 07:00 UTC (64 invoices) and 15 Nov (90). I've promised the customer an update by 16:00 UTC today.
