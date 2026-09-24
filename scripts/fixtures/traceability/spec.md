# Coupons (fixture spec for the coverage gap check)

Requirement key: CPN

## User Stories

1. CPN-1: As a shopper, I want to apply a coupon at checkout, so that I pay less.
2. CPN-2: As a shopper, I want an expired coupon rejected with a reason, so that I know why it failed.
3. CPN-3: (dropped) As a shopper, I want to stack coupons.
4. CPN-4: As a shopper, I want a refund to restore my coupon, so that I can reuse it.
5. CPN-5: As a shopper, I want analytics on coupon use, so that pricing improves.
6. CPN-6: As a shopper, I want my coupon to survive a refresh, so that I do not retype it.
7. CPN-10: As a shopper, I want codes to be case insensitive, so that typing is easier.

## Testing Decisions

| Seam | Requirement IDs |
| --- | --- |
| POST /checkout | CPN-2, CPN-10 |
| waived: needs a real payment provider | CPN-4 |
