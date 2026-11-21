# Ticket TRN-77391: High-temperature SMS alarms not received from some vat gateways

Customer: Kestrel Dairy Co-operative (account KDC-0418)
Products: TernGate G4 gateways, TernCloud alarm rules
Export of the full ticket history. All timestamps are UTC. Australia/Perth time (AWST) is UTC+8.
As-of time: 2026-11-24 06:00 UTC. This export was taken at that moment; treat it as the current time for every judgement about elapsed time, deadlines and what is still to come. Do not use the clock of the machine you run on.

---

**2026-11-19 07:50 UTC** | Event: Ticket created via portal by Aroha Ngata. Priority: P3. Status: Open.

**2026-11-19 07:50 UTC** | Aroha Ngata (customer, Plant Engineer)

> On Tuesday night vat 3 at our Brunswick plant went above 7°C for about 40 minutes and nobody received the high-temperature SMS. The TernCloud dashboard shows the reading went over the limit, so the sensor saw it.
>
> We tested the alarms on all nine vats this afternoon. Vats 4 to 9 sent the SMS within a minute; vats 1, 2 and 3 sent nothing. Each vat has its own gateway (VAT-GW-01 to VAT-GW-09).
>
> Until this is fixed our night staff are checking the dashboard every hour.

**2026-11-20 01:05 UTC** | Hannah Odum (Support Agent, Tier 1)

> Hi Aroha, thanks for testing all nine. I've checked the alarm rules in TernCloud: vats 1 to 9 all use the same rule template ("Vat high temp, above 7°C for 5 min") with the same SMS recipients, so the configuration doesn't explain the difference. I'd like to look at the gateways themselves.

**2026-11-20 01:10 UTC** | Hannah Odum (Tier 1)

> Could you download a diagnostic bundle from VAT-GW-01, 02 and 03 and attach them here? On each gateway's local web page, go to Maintenance > Diagnostics > Download bundle.

**2026-11-20 01:10 UTC** | Event: Status Open → Pending customer (Hannah Odum).

**2026-11-20 05:40 UTC** | Aroha Ngata (customer)

> Bundles for all three attached.

**2026-11-20 05:40 UTC** | Event: Status Pending customer → Open (customer reply).

**2026-11-20 07:15 UTC** | Internal note, Hannah Odum (not visible to customer)

> Bundles: the rule engine on all three gateways logs "RULE_EVAL_SKIPPED reason=TS_FUTURE" at every evaluation since 12 Nov. The gateway clocks are ahead of the sensor timestamps: GW-01 +9 min 12 s, GW-02 +8 min 40 s, GW-03 +11 min 03 s. The rule needs 5 minutes of readings, and with the clock that far ahead the window never fills, so the rule is skipped.
>
> NTP log on all three: "NTP sync failed: timeout (pool.terncloud.net:123)", repeated since 12 Nov. The bundles put GW-01 to 03 on VLAN 30. TernCloud shows GW-04 to 09 with their last time sync OK. Possible cause: UDP 123 blocked for VLAN 30. Not confirmed.

**2026-11-20 07:20 UTC** | Hannah Odum (Tier 1)

> Aroha, the clocks on those three gateways are running 8 to 11 minutes fast because they can't reach our time server, and that stops the alarm rule from evaluating. Could your IT team check whether outbound UDP port 123 is allowed from VLAN 30 at Brunswick? No rush before Monday; the hourly checks cover you over the weekend.

**2026-11-23 01:40 UTC** | Aroha Ngata (customer)

> IT says nothing has changed on VLAN 30 and outbound UDP 123 is allowed.
>
> But I need to tell you what happened on Sunday night. Vat 3 went over 7°C again at about 01:00 our time. No SMS. The night operator caught it on the hourly check, but by then it had been over the limit for about 50 minutes and we had to dump 18,000 litres. Our night staff can't keep doing hourly checks, and clearly they aren't enough. We'd like the cost of that milk covered.

**2026-11-23 02:15 UTC** | Event: Priority P3 → P2 (Hannah Odum). Reason recorded: "Missed alarm caused product loss; hourly manual checks not a practical workaround (clause 2.2)."

**2026-11-23 02:20 UTC** | Hannah Odum (Tier 1)

> I'm very sorry about the milk, Aroha. I've raised the ticket to P2. I'm not able to offer compensation myself, so I've passed your request to Joel Brandt, your account manager.
>
> Next, I'm going to send a command from TernCloud that sets the clock on GW-01 to 03 over HTTPS, which avoids the NTP port. Once that's done, could you run the alarm test on vats 1 to 3?

**2026-11-23 02:40 UTC** | Internal note, Hannah Odum

> Sent "Force time sync (HTTPS)" to GW-01, 02 and 03 at 02:35. GW-01 and GW-02: result OK, clock offset now under 1 s. GW-03: result "TIME_SET_REJECTED: RTC write error"; clock still +11 min 05 s.

**2026-11-23 03:05 UTC** | Aroha Ngata (customer)

> Test done. Vats 1 and 2 sent the SMS within a minute. Vat 3 still nothing.

**2026-11-24 01:30 UTC** | Internal note, Hannah Odum

> SLA check: P2 since Mon 10:15 AWST, so 27 business hours from then gives a due time of Thu 26 Nov 10:15 AWST. Plenty of time. Will try GW-03 again today.

**2026-11-24 05:20 UTC** | Internal note, Hannah Odum

> Aroha agreed by phone at 05:10 to a remote reboot of GW-03. Second "Force time sync (HTTPS)" to GW-03 at 05:15: same "TIME_SET_REJECTED: RTC write error". Rebooted GW-03 from TernCloud at 05:17; back online at 05:19; clock still +11 min. GW-01 and GW-02 still in sync (offset under 1 s), but NTP is still failing on all three, so 01 and 02 may drift again.

**2026-11-24 05:40 UTC** | Hannah Odum (Tier 1)

> Aroha, the second attempt and the remote reboot didn't fix the clock on GW-03. The gateway is refusing to set its clock, which may be a hardware fault. Vats 1 and 2 are still working. I'm escalating this to our Field Systems Engineering team now. You'll get an update from us by 17:30 AWST today (09:30 UTC).

**2026-11-24 06:00 UTC** | Event: Escalated to Tier 2 (Field Systems Engineering) by Hannah Odum. Status: Open → Escalated. Priority: P2.
