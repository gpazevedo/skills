#!/usr/bin/env bash
# Builds a repo whose spec carries requirement IDs, where CPN-1's only test is commented out.
set -eu
mkdir -p tests
cat > spec.md <<'EOF'
# Coupons

Requirement key: CPN

## User Stories

1. CPN-1: As a shopper, I want to apply a coupon at checkout, so that I pay less.
2. CPN-2: As a shopper, I want an expired coupon rejected with a reason, so that I know why it failed.
3. CPN-3: As a shopper, I want codes to be case insensitive, so that typing is easier.
4. CPN-4: As a shopper, I want a refund to restore my coupon, so that I can reuse it.

## Testing Decisions

| Seam | Requirement IDs |
| --- | --- |
| POST /checkout | CPN-2, CPN-3 |
| waived: needs a real payment provider | CPN-4 |
EOF
cat > tests/checkout.test.ts <<'EOF'
it('CPN-2: rejects an expired coupon with a reason', () => {});
it('CPN-3: accepts a lowercase coupon code', () => {});
// it('CPN-1: applies a coupon at checkout', () => {});
EOF
git init -q . && git add -A && git -c user.email=e@e -c user.name=n commit -qm "coupons"
