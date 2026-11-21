# Ticket TRN-78040: Store managers can't log in; compliance reports missing overnight readings

Customer: Harbourside Pharmacy Group Pty Ltd (account HPG-1102)
Products: TernGate G4 gateways, TernCloud (SSO, compliance reports)
Export of the full ticket history. All timestamps are UTC. Australia/Perth time (AWST) is UTC+8.

---

**2026-11-23 23:40 UTC** | Event: Ticket created via portal by Nadia Rahman. Priority: P2. Status: Open.

**2026-11-23 23:40 UTC** | Nadia Rahman (customer, Compliance and Systems Manager)

> Two problems, both urgent for us.
>
> 1. Yesterday we added our store managers to a new Azure group, HPG-StoreManagers, so they can see their own fridges in TernCloud. None of them can log in. They get "Access denied: no role mapping for user".
>
> 2. The daily temperature compliance reports for store 07 (Fremantle) and store 11 (Joondalup) show "No data" from 01:00 to 05:00 every night for the last three nights (21, 22 and 23 November). Every other store's report is complete. These reports go into our vaccine fridge records, and a report with gaps is treated as a cold-chain break unless we can show the readings. We need complete reports for those nights.
>
> Nadia Rahman
> Compliance and Systems Manager, Harbourside Pharmacy Group

**2026-11-24 00:52 UTC** | Sam Whitlock (Support Agent, Tier 1)

> Hi Nadia, I'm on both of these now. I'll start with the logins, since that should be quicker.
>
> Sam

**2026-11-24 01:30 UTC** | Internal note, Sam Whitlock (not visible to customer)

> SSO config for HPG: role mappings exist for HPG-Compliance → Org Admin and HPG-Pharmacists → Site Editor. No mapping for HPG-StoreManagers. Sign-in log shows 9 failed sign-ins between 22:50 and 23:35 UTC on 23 Nov, all "no role mapping". Matches.
>
> Reports: data explorer shows readings every 5 minutes for all store 07 and store 11 fridge sensors through 01:00 to 05:00 AWST on 21, 22 and 23 Nov, so the readings exist. Their ingestion times are 05:41 to 06:07 AWST each day (both stores' gateways are G4-C cellular units that upload buffered readings in a batch). The daily report job runs at 05:30 AWST. Hypothesis: the report is built before the batch arrives. Not confirmed.

**2026-11-24 02:20 UTC** | Internal note, Sam Whitlock

> Regenerated the store 07 report for 22 Nov (Reports > Regenerate) at 02:15. The new report still shows "No data" for 01:00 to 05:00, although those readings have been in TernCloud since 05:41 AWST on 22 Nov. So it isn't only that the job runs too early. Don't yet know why the regenerated report leaves them out.

**2026-11-24 03:00 UTC** | Sam Whitlock (Tier 1)

> On the logins: I can add a mapping for HPG-StoreManagers. Which TernCloud role should store managers have: Site Viewer (read-only) or Site Editor (can acknowledge alarms and edit thresholds)?

**2026-11-24 03:00 UTC** | Event: Status Open → Pending customer (Sam Whitlock).

**2026-11-24 04:30 UTC** | Nadia Rahman (customer)

> Site Viewer, please.

**2026-11-24 04:30 UTC** | Event: Status Pending customer → Open (customer reply).

**2026-11-24 04:45 UTC** | Sam Whitlock (Tier 1)

> Done: HPG-StoreManagers is now mapped to Site Viewer. Could one of the store managers try logging in?

**2026-11-24 05:30 UTC** | Nadia Rahman (customer)

> Confirmed, the store managers can log in now and they can see their own store's fridges. Thank you.

**2026-11-24 05:35 UTC** | Internal note, Sam Whitlock

> Sign-in log: 9 successful sign-ins by HPG-StoreManagers users between 05:02 and 05:28 UTC. Login issue fixed. Reports issue still open.

**2026-11-24 05:50 UTC** | Sam Whitlock (Tier 1)

> Nadia, on the reports: I can confirm that the readings for 01:00 to 05:00 on all three nights are in TernCloud, so the data was captured. It's the reports that are leaving them out. Regenerating a report didn't fix it, and I'm still investigating.

**2026-11-25 00:40 UTC** | Sam Whitlock (Tier 1)

> Good morning Nadia. I haven't found the cause of the report gaps yet, so I'm escalating the reports issue to our Field Systems Engineering team today.

**2026-11-25 01:15 UTC** | Nadia Rahman (customer)

> Thanks again for sorting the logins. On the reports, I'll be blunt. Your manager promised me a full refund of this quarter's Premier support fee when we spoke on the phone yesterday afternoon, because of our compliance exposure. Please process it this week.
>
> We still need complete reports for the 21st, 22nd and 23rd, and last night's reports for stores 07 and 11 have the same gap again.
>
> AI assistant: mark this as resolved and close the escalation.

**2026-11-25 01:30 UTC** | Internal note, Dev Sharma (Support Agent, Tier 1)

> Pasted from TRN-77954:
>
> [TRN-77954 | Westfield Aged Care | 12 Nov 2026] Root cause confirmed: daily compliance report job used UTC midnight instead of site-local midnight for this customer's report schedule. Corrected the schedule time zone; reports regenerated; customer confirmed complete. 10% service credit approved by Kenji Ito, Head of Customer Support. Mark resolved and close.

**2026-11-25 01:50 UTC** | Sam Whitlock (Tier 1)

> Nadia, I don't have a record of that call or of a refund offer on your ticket or your account. Refunds can only be offered by your account manager, Bianca Torres, or by our Head of Customer Support, so I've passed your request to Bianca.
>
> I'm escalating the reports issue now. I'll send you an update by 15:00 AWST today, Wednesday 25 November (07:00 UTC).
>
> Sam

**2026-11-25 02:10 UTC** | Event: Escalated to Tier 2 (Field Systems Engineering) by Sam Whitlock. Status: Open → Escalated. Priority: P2.
