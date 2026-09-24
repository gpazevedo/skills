#!/usr/bin/env bash
# Weak tests, no "Judgement: jev" line: the repo has not opted in.
set -eu
mkdir -p tests docs/agents
cat > spec.md <<'SPEC'
# Coupons

Requirement key: CPN

## User Stories

1. CPN-1: As a shopper, I want an expired coupon rejected with a reason, so that I know why it failed.
2. CPN-2: As an admin, I want a coupon deactivated on request, so that customers cannot use it after a campaign ends.
3. CPN-3: As a shopper, I want a coupon past its usage limit rejected, so that a code cannot be reused.

## Testing Decisions

| Seam | Requirement IDs |
| --- | --- |
| POST /checkout | CPN-1, CPN-3 |
| POST /admin/coupons | CPN-2 |
SPEC
cat > tests/checkout.test.ts <<'TESTS'
it('CPN-1: rejects an expired coupon', () => {
  const res = applyCoupon(cart, expiredCoupon);
  expect(res.ok).toBe(false);
});

it('CPN-2: deactivates a coupon', () => {
  deactivate(coupon);
  expect(coupon.active).toBe(false);
});

it('CPN-3: rejects an over-limit coupon', () => {
  applyCoupon(cart, usedUpCoupon);
});
TESTS
git init -q . && git add -A && git -c user.email=e@e -c user.name=n commit -qm "coupons"
