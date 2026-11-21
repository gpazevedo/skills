# Ticket QB-202861: Card payments failing with "PCX-402"

Customer: Brackenridge Veterinary Group Ltd (account BV-3307)
Products: Quillbill Invoicing, PayCollect card payments integration
Partial export. All timestamps are UTC.

This export contains messages 7 to 12 of 12. Messages 1 to 6 (2026-11-03 14:20 UTC to 2026-11-04 15:00 UTC) are not included; see earlier messages in the full ticket. The ticket event log below is complete.

---

## Ticket events before message 7

- **2026-11-03 14:20 UTC** | Event: Ticket created via portal by Sunil Mehta (message 1). Priority: P2. Status: New.
- **2026-11-03 15:02 UTC** | Event: Assigned to Priya Nair (Support Agent, Tier 1). First agent response sent (message 2). Status: New → Open.
- **2026-11-04 09:30 UTC** | Event: Status Open → Pending customer (Priya Nair).
- **2026-11-04 15:00 UTC** | Event: Status Pending customer → Open (customer reply, message 6).

## Messages and events from message 7

**2026-11-04 15:40 UTC** | Message 7 | Priya Nair (Tier 1)

> Thanks Sunil, and sorry the reconnect didn't help. As I said in my earlier message, the next step is for me to look at the payment logs on our side. I'll come back to you tomorrow morning.
>
> Priya

**2026-11-04 17:10 UTC** | Message 8 | Sunil Mehta (customer, Practice Operations Manager)

> Priya, every single card payment has failed since Monday. We've had clients come in to collect their pets and their saved card is declined at the desk, which is embarrassing for our staff. We did exactly what your earlier message said and reconnected PayCollect, so this is not on our side.
>
> And as you said in your message yesterday, we'll be expecting October's subscription fee to be credited for all this. Please confirm.
>
> Sunil Mehta
> Practice Operations Manager, Brackenridge Veterinary Group

**2026-11-05 09:05 UTC** | Event: Reassigned from Priya Nair to James Whitfield (Support Agent, Tier 1).

**2026-11-05 09:40 UTC** | Message 9 | James Whitfield (Tier 1)

> Hi Sunil, I'm James, and I've taken over your ticket from Priya, who is away today. I've checked the payment logs on our side:
>
> - Since 2 November 14:00 UTC there have been 38 card payment attempts on your account. 31 failed with the error "PCX-402 token not found" and 7 succeeded.
> - All 31 failures used cards that were saved before 1 November. All 7 successes used cards saved on or after 1 November.
>
> I'd like to retry the collection on one failed invoice, INV-BV-20931, to see whether the error repeats. If it succeeds, your client's card will be charged for that invoice. May I go ahead?
>
> On the October credit: I'm not able to agree credits. Under our policy that is for your Customer Success Manager, so I've passed your request to Callum Reid.
>
> James

**2026-11-05 09:55 UTC** | Message 10 | Sunil Mehta (customer)

> Yes, retry INV-BV-20931. And I want the credit confirmed in writing, not passed around.

**2026-11-05 10:20 UTC** | Message 11 | Internal note, James Whitfield (not visible to customer)

> Retried collection on INV-BV-20931 at 10:12. Failed again: "PCX-402 token not found". The card token on that invoice was created 14 Oct 2026. The PayCollect API response says "token not found in vault".
>
> Integration log: PayCollect connection was re-authorised on 4 Nov at 14:41 UTC, so the customer's reconnect did happen. Failures continue after it (14 of the 31 failures are after 14:41 on 4 Nov).
>
> Release notes for v8.2.3 (deployed 1 Nov): "Card vault migrated to PayCollect v3." Possible link with tokens saved before 1 Nov; not confirmed.
>
> I can't see in my view which reconnect steps Priya sent or what else was tried in messages 1 to 6.

**2026-11-05 10:40 UTC** | Message 12 | James Whitfield (Tier 1)

> Sunil, the retry on INV-BV-20931 failed with the same error, so no charge was made. The failures all involve cards saved before 1 November, which suggests a problem on our side with older saved cards rather than with your settings. I'm escalating this to our Product Engineering Support team now. I'll update you by 16:00 UTC today.
>
> James

**2026-11-05 11:00 UTC** | Event: Escalated to Tier 2 (Product Engineering Support) by James Whitfield. Status: Open → Escalated. Priority: P2.
