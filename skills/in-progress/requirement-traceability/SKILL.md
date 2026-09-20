---
name: requirement-traceability
description: "Requirement traceability from spec to tests. Use when a spec already carries requirement IDs like `CPN-3:`, when the user asks for a spec's requirements to be traceable to tests, or when checking coverage for a spec that has them."
---

# Requirement Traceability

If the spec has no requirement IDs and the user has not asked for them, say so in one line and stop. Do not add IDs to a spec that does not use them.

This is an opt-in convention. A spec that carries IDs turns it on; a spec without them changes nothing. It makes "every requirement has a test" checkable instead of a judgement call.

Tell whether a spec carries IDs with one grep over its text:

```bash
grep -qE '^[[:space:]]*[0-9]+\.[[:space:]]+[A-Z]{2,5}-[0-9]+:' <spec>
```

## Requirement ID

Format `<KEY>-<n>`, like `CPN-3`. `KEY` is 2 to 5 uppercase letters chosen per spec. A bare `R3` would collide across specs and count another spec's test as coverage.

**The ID is always followed by a colon, and every match anchors on the colon.** `CPN-1` is a prefix of `CPN-10`, so a match without the colon reports an untested `CPN-1` as covered the moment `CPN-10` gets a test. Silent false coverage is the failure this convention exists to prevent. Grep `"CPN-3:"`, never `"CPN-3"`. Quote the colon in runner filters: `-t "CPN-3:"`.

IDs go on the spec's **User Stories**, after the list number (the list stays numbered), at the start of the story text:

```
Requirement key: CPN

1. CPN-1: As a shopper, I want to apply a coupon at checkout, so that I pay less.
2. CPN-2: As a shopper, I want an expired coupon rejected with a reason, so that I know why it failed.
```

One behaviour per ID: split compound stories. Never renumber or reuse an ID. A withdrawn one stays and is marked `(dropped)` right after the colon: `3. CPN-3: (dropped) As a shopper, ...`.

**Choose the KEY before writing.** Grep for KEYs already in use:

```bash
grep -rhoE '\b[A-Z]{2,5}-[0-9]+:' --exclude-dir={node_modules,.git} \
  --include='*.md' --include='*.ts' --include='*.tsx' --include='*.js' --include='*.py' . \
  | sed -E 's/-[0-9]+:$//' | sort -u
```

This sees KEYs in tests and in specs committed to the repo. It cannot see a spec that lives only in an issue tracker, so it is best-effort. The `Requirement key:` line records the spec's own KEY so a reader can see what is taken.

## Seam table

In the spec's **Testing Decisions**, map each seam to the IDs it covers:

```
| Seam | Requirement IDs |
| --- | --- |
| POST /checkout | CPN-1, CPN-2 |
| waived: needs a real payment provider | CPN-4 |
```

An uncovered ID shows up as an ID in no row, before any code exists. An ID that will not be tested gets a `waived: <reason>` row. A requirement is waived explicitly, never dropped silently.

## Test tag

The test name starts with its ID and a colon: `CPN-3: rejects expired coupons`. Where the language cannot put it in the name (a Python function), make it the first line of the test's docstring.

## Issue line

When the spec has IDs, each issue `to-tickets` produces carries a line `Covers: CPN-1, CPN-4`, and every ID lands on exactly one issue's `Covers:` line.

`Covers:` means **the IDs this issue makes fully testable**, not the IDs it touches. A requirement built across two slices goes on the last one only, so the earlier slice's check passes honestly.

## Coverage gap check

If `docs/agents/traceability.md` exists, run the command it names. Otherwise do it by hand. Save the spec text to a file first (for a tracker issue, `gh issue view N --json body -q .body > spec.md`), then:

```bash
SPEC=spec.md
T=$(mktemp -d)
TESTS=$(git ls-files | grep -E '(^|/)(tests?|__tests__)/|\.(test|spec)\.|(^|/)test_|_test\.' | grep -v '\.md$')

# IDs the spec defines (dropped ones excluded), and IDs it waives
grep -v '(dropped)' "$SPEC" | sed -nE 's/^[[:space:]]*[0-9]+\.[[:space:]]+([A-Z]{2,5}-[0-9]+:).*/\1/p' | sort -u > $T/defined
awk -F'|' '/^\|[[:space:]]*waived/ {print $3}' "$SPEC" | grep -oE '[A-Z]{2,5}-[0-9]+' | sed 's/$/:/' | sort -u > $T/waived

# IDs tagged in tests: a quoted name that starts with an ID and a colon
echo "$TESTS" | xargs -r -d '\n' grep -ohE "[\"'\`][A-Z]{2,5}-[0-9]+:" | tr -d "\"'\`" | sort -u > $T/tagged

echo "UNTESTED (fails):";      comm -23 $T/defined $T/tagged | comm -23 - $T/waived
echo "UNDEFINED ID (warns):";  comm -13 $T/defined $T/tagged
echo "NO ID (warns):";         echo "$TESTS" | xargs -r -d '\n' grep -nE "\b(it|test)\(\s*[\"'\`]" | grep -vE "[\"'\`][A-Z]{2,5}-[0-9]+:"
```

Adapt the last line's declaration pattern to the repo's runner (`def test_` for pytest, `func Test` for Go); the rest is unchanged. `comm` compares whole lines, colon included, which is what keeps `CPN-1:` and `CPN-10:` apart.

Report three classes:

- **Untested**: a defined, non-waived ID with no tagged test. This fails the check.
- **Undefined ID**: a tagged test whose ID the spec does not define (or has dropped). Warn: a typo or a stale test.
- **No ID**: a test with no ID. Warn: possible scope creep, or a test worth tying to a requirement.

For one issue's check, replace `defined` with the IDs on that issue's `Covers:` line and report only untested:

```bash
grep -E '^Covers:' issue.md | grep -oE '[A-Z]{2,5}-[0-9]+' | sed 's/$/:/' | sort -u > $T/defined
```

The script and the grep check presence only. Whether a tagged test asserts what its requirement says is judgement, and belongs to `code-review`'s Spec sub-agent.

### `docs/agents/traceability.md`

Optional, hand-written, absent by default: the grep above is the normal path. It names a repo's own check command in two lines:

```
Check command: `<command>`
Spec input: `stdin` or `path`
```

The command exits 0 when every ID is covered and 1 when any is untested, and takes IDs as trailing arguments to narrow the check to them. When the user names such a command, offer to write the file.
