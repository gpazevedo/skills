#!/usr/bin/env bash
# Builds a repo with a spec and two tickets that carry no requirement IDs, as to-spec and to-tickets write them.
set -eu
mkdir -p .scratch/coupons/issues
cat > spec.md <<'SPEC'
# Coupons

## User Stories

1. As a shopper, I want to apply a coupon at checkout, so that I pay less.
2. As a shopper, I want an expired coupon rejected with a reason, so that I know why it failed.
3. As a shopper, I want codes to be case insensitive, so that typing is easier.

## Testing Decisions

- Test through `POST /checkout` only.
SPEC
cat > .scratch/coupons/issues/01-apply-coupon.md <<'T1'
## What to build

A shopper enters a coupon code at checkout and the total drops by the coupon's discount. Codes match regardless of case.

## Acceptance criteria

- [ ] A valid code reduces the total
- [ ] `save10` and `SAVE10` are the same code

## Blocked by

- None (can start immediately)
T1
cat > .scratch/coupons/issues/02-expired-coupon.md <<'T2'
## What to build

An expired coupon is refused at checkout, and the shopper sees why.

## Acceptance criteria

- [ ] An expired code is refused with the reason "expired"

## Blocked by

- 01-apply-coupon
T2
git init -q . && git add -A && git -c user.email=e@e -c user.name=n commit -qm "coupons"
