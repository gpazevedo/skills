# Ticket TRN-77102: ALL gateways offline after firmware update

Customer: Coldwater Freight Pty Ltd (account CWF-2210)
Products: TernGate G4 gateways, TernCloud
Export of the full ticket history. All timestamps are UTC. Australia/Perth time (AWST) is UTC+8.

---

**2026-11-16 01:05 UTC** | Event: Ticket created by Marcus Lee (Support Agent, Tier 1) during a phone call from Grant Tobias (customer). Priority: P2. Status: Open. Customer requested P1 (see call note).

**2026-11-16 01:05 UTC** | Call note, Marcus Lee (internal)

> Grant Tobias (Operations Manager) called. Says all Coldwater gateways stopped reporting after the firmware update on the weekend. Says his team rebooted all the Darwin gateways and it made no difference. Asked for P1. I told him I'd check the fleet and call him back within the hour. Logged at P2 until I've seen the fleet status.

**2026-11-16 01:12 UTC** | Grant Tobias (customer, email)

> Putting my call in writing. Every one of our gateways went dark after your firmware push on the weekend. We've lost all our temperature data for the last three days and we're running blind across the network.
>
> Your engineer told me on the phone last week that 4.7.2 was fixed and safe to roll out, so this one is on Tern. It's costing us around $40,000 a day in stock we can't certify for delivery. This needs to be P1.
>
> Grant Tobias
> Operations Manager, Coldwater Freight

**2026-11-16 01:32 UTC** | Marcus Lee (Tier 1, email after call-back)

> Grant, as discussed on the phone just now, here's what I can see in TernCloud as of 01:25 UTC (09:25 AWST):
>
> - Your fleet has 61 gateways. 47 are online and reporting normally. 14 are offline.
> - The 14 offline gateways are all at your Darwin depot (11 units) and Katherine depot (3 units). Each one last reported between 18:20 and 18:24 UTC on Saturday 14 November, during your scheduled firmware window (rollout started at 18:00 UTC).
> - All 61 gateways were updated to firmware 4.7.2 in that window. The 47 online gateways are all running 4.7.2.
> - Readings from the 47 online gateways are complete in TernCloud, with no gaps. For the 14 offline gateways, TernCloud has no readings after their last report. G4 gateways store readings locally when they can't reach TernCloud and upload them when they reconnect, so I can't yet tell whether any data has actually been lost.
>
> Because fewer than half of your gateways are offline, the ticket stays at P2 under our support policy. That doesn't change how seriously we're taking it.
>
> I can't find a record of a call or a ticket with Coldwater last week. The last ticket on your account was TRN-75530, closed on 2 October. If you can tell me who you spoke to, I'll follow it up.
>
> Could someone at Darwin tell me what the front-panel lights show on two or three of the units?
>
> Marcus

**2026-11-16 02:10 UTC** | Internal note, Marcus Lee (not visible to customer)

> Tern Connect console: all 14 SIMs are status Active. Their last data sessions ended between 18:21 and 18:24 UTC on 14 Nov. No session attempts since.
>
> Model check: all 14 offline units are G4-C (cellular). All 47 online units are G4-E (Ethernet). So the hardware model, not the firmware version alone, separates the two groups. The 4.7.2 release notes include "cellular modem firmware updated to MX-31.4 (G4-C only)". Possible link; not confirmed.
>
> Sent remote SMS wake to DRW-GW-01, DRW-GW-05 and KTH-GW-02 at 02:05 UTC. No response from any of them by 02:10.

**2026-11-16 03:05 UTC** | Grant Tobias (customer, email)

> Darwin site lead says every unit shows a solid green power light and a flashing amber NET light. They power-cycled all 11 Darwin units again this morning and the lights came back the same. Nobody at Katherine has touched theirs yet.
>
> As for last week, it was one of your engineers. I don't remember his name, but he was clear it was fixed.
>
> And make no mistake, every site is affected: Perth can't dispatch the Darwin loads without the certificates.

**2026-11-16 03:40 UTC** | Marcus Lee (Tier 1, email)

> Thanks, Grant. According to our LED guide, a flashing amber NET light on a G4-C means the cellular modem isn't registered on the mobile network. With the SIMs still showing as active on the carrier side, that points to a problem on the gateway side rather than with the SIM accounts, but I can't confirm the cause yet and I can't give you a fix date.
>
> Please don't factory-reset any of the units, because that would erase any readings stored on them.
>
> I'm escalating this to our Field Systems Engineering team now. I'll send you an update by 12:00 AWST tomorrow, Tuesday 17 November (04:00 UTC), or sooner if engineering has news.
>
> Marcus

**2026-11-16 03:50 UTC** | Event: Escalated to Tier 2 (Field Systems Engineering) by Marcus Lee. Status: Open → Escalated. Priority: P2 (unchanged; customer's request for P1 recorded and not applied, as 14 of 61 gateways are offline).
