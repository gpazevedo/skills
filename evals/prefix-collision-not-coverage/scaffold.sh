#!/usr/bin/env bash
# Twelve requirements. Every one is tagged except CPN-1, whose ID is a prefix of
# CPN-10, CPN-11 and CPN-12. A match that is not anchored on the colon reports it covered.
set -eu
mkdir -p tests
{
  echo "# Checkout"
  echo
  echo "Requirement key: CPN"
  echo
  echo "## User Stories"
  echo
  echo "1. CPN-1: As a shopper, I want to apply a coupon at checkout, so that I pay less."
  echo "2. CPN-2: As a shopper, I want an expired coupon rejected with a reason, so that I know why it failed."
  echo "3. CPN-3: As a shopper, I want codes to be case insensitive, so that typing is easier."
  echo "4. CPN-4: As a shopper, I want the discount shown before I pay, so that I can check it."
  echo "5. CPN-5: As a shopper, I want one coupon per order, so that the rules are clear."
  echo "6. CPN-6: As a shopper, I want my coupon to survive a refresh, so that I do not retype it."
  echo "7. CPN-7: As a shopper, I want a clear error for an unknown code, so that I can correct it."
  echo "8. CPN-8: As a shopper, I want the total recalculated on removal, so that I see the real price."
  echo "9. CPN-9: As a shopper, I want percentage coupons rounded down, so that I am never overcharged."
  echo "10. CPN-10: As a shopper, I want a coupon to expire at midnight UTC, so that the cutoff is predictable."
  echo "11. CPN-11: As a shopper, I want a used coupon rejected, so that it cannot be reused."
  echo "12. CPN-12: As a shopper, I want my coupon on the receipt, so that I have a record."
} > spec.md
{
  echo "it('CPN-2: rejects an expired coupon with a reason', () => { expect(apply('EXPIRED')).toEqual({ ok: false, reason: 'expired' }); });"
  echo "it('CPN-3: accepts a lowercase coupon code', () => { expect(apply('save10').ok).toBe(true); });"
  echo "it('CPN-4: shows the discount before payment', () => { expect(quote('SAVE10').discount).toBe(10); });"
  echo "it('CPN-5: allows only one coupon per order', () => { expect(apply('A', { applied: 'B' }).ok).toBe(false); });"
  echo "it('CPN-6: keeps the coupon across a refresh', () => { expect(reload(session).coupon).toBe('SAVE10'); });"
} > tests/coupon.test.ts
{
  echo "it('CPN-7: explains an unknown code', () => { expect(apply('NOPE').reason).toBe('unknown code'); });"
  echo "it('CPN-8: recalculates the total on removal', () => { expect(remove(order).total).toBe(100); });"
  echo "it('CPN-9: rounds percentage discounts down', () => { expect(quote('PCT15', 99).discount).toBe(14); });"
  echo "it('CPN-10: expires a coupon at midnight UTC', () => { expect(isExpired('SAVE10', midnightUtc)).toBe(true); });"
  echo "it('CPN-11: rejects a coupon that was already used', () => { expect(apply('USED').reason).toBe('already used'); });"
  echo "it('CPN-12: prints the coupon on the receipt', () => { expect(receipt(order).coupon).toBe('SAVE10'); });"
} > tests/checkout.test.ts
git init -q . && git add -A && git -c user.email=e@e -c user.name=n commit -qm checkout
