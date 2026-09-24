---
name: requirement-traceability
description: "Requirement traceability from spec to tests. Use after `/to-tickets` to add requirement IDs to a spec and `Covers:` lines to its tickets, when a spec already carries requirement IDs like `CPN-3:`, or when checking coverage for a spec that has them."
---

# Requirement Traceability

This is an opt-in convention. It makes "every requirement has a test" checkable instead of a judgement call. A spec that carries IDs turns it on for `tdd` and `implement`; a spec without them changes nothing.

Two ways in:

- **The user invokes this skill on a spec without IDs**, usually right after `/to-tickets`: [annotate](#annotate-a-spec-and-its-tickets) the spec and its tickets.
- **Called from `tdd` or `implement`**, or asked to check coverage: if the spec has no IDs, say so in one line and stop. Never add IDs the user did not ask for.

Tell whether a spec carries IDs with one grep over its text:

```bash
grep -qE '^[[:space:]]*[0-9]+\.[[:space:]]+[A-Z]{2,5}-[0-9]+:' <spec>
```

## Annotate a spec and its tickets

Run once, after `/to-spec` and `/to-tickets`, before any `/implement`. `to-spec` and `to-tickets` know nothing of this convention, so this step adds it to what they wrote:

1. Choose the KEY (below) and add a `Requirement key:` line above the spec's User Stories.
2. Put an ID on each user story. Split compound stories first: one behaviour per ID.
3. Add the seam table to the spec's Testing Decisions. Report any ID in no row: that is a gap, visible before any code.
4. Add a `Covers:` line to each ticket (the [issue line](#issue-line)). Report any ID no ticket makes testable: a slicing gap for the user to settle. With no tickets (a one-session build), skip this step: `implement` then checks every ID.

Write the spec and tickets back where they live: files under `.scratch/<feature>/`, or the tracker via `docs/agents/issue-tracker.md`. Then show the user, verbatim, each annotated story (`1. CPN-1: As a ...`) and each ticket's `Covers:` line under the ticket's name, and ask: is every requirement covered by exactly one ticket?

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

One behaviour per ID does not mean one test per ID. A requirement often needs several tests (the main case, edge cases, errors); tag every one with the same ID. The gap check needs at least one; the Judgement pass reads them all together.

## Issue line

When the spec has IDs, each issue carries a line `Covers: CPN-1, CPN-4`, and every ID lands on exactly one issue's `Covers:` line. Annotation adds it; an issue written later by hand gets it too.

`Covers:` means **the IDs this issue makes fully testable**, not the IDs it touches. A requirement built across two slices goes on the last one in blocking order only, so the earlier slice's check passes honestly.

## Coverage gap check

If `docs/agents/traceability.md` has a `Check command:` line, run that command. Otherwise do it by hand. Save the spec text to a file first (for a tracker issue, `gh issue view N --json body -q .body > spec.md`), then:

```bash
SPEC=spec.md
T=$(mktemp -d)
git ls-files --cached --others --exclude-standard | grep -E '(^|/)(tests?|__tests__)/|\.(test|spec)\.|(^|/)test_|_test\.' | grep -v '\.md$' > $T/tests

# IDs the spec defines (dropped ones excluded), and IDs it waives
grep -v '(dropped)' "$SPEC" | sed -nE 's/^[[:space:]]*[0-9]+\.[[:space:]]+([A-Z]{2,5}-[0-9]+:).*/\1/p' | sort -u > $T/defined
awk -F'|' '/^\|[[:space:]]*waived/ {print $3}' "$SPEC" | grep -oE '[A-Z]{2,5}-[0-9]+' | sed 's/$/:/' | sort -u > $T/waived

# IDs tagged in tests: a quoted name that starts with an ID and a colon.
# A commented-out or skipped test is not coverage, so drop those lines first.
xargs -r -d '\n' grep -hE "[\"'\`][A-Z]{2,5}-[0-9]+:" < $T/tests \
  | grep -vE "^[[:space:]]*(//|/\*|\*|#)" \
  | grep -vE "(^|[^[:alnum:]_])(xit|xtest)\(|\.(skip|todo|failing)\(" \
  | grep -ohE "[\"'\`][A-Z]{2,5}-[0-9]+:" | tr -d "\"'\`" | sort -u > $T/tagged

echo "UNTESTED (fails):";      comm -23 $T/defined $T/tagged | comm -23 - $T/waived
echo "UNDEFINED ID (warns):";  comm -13 $T/defined $T/tagged
echo "NO ID (warns):";         xargs -r -d '\n' grep -nE "\b(it|test)\(\s*[\"'\`]" < $T/tests | grep -vE "[\"'\`][A-Z]{2,5}-[0-9]+:"
```

`comm` compares whole lines, colon included, which is what keeps `CPN-1:` and `CPN-10:` apart.

Adapt the last line's declaration pattern to the repo's runner. Where the ID sits in the test name, swapping the pattern is the whole change (`func Test` for Go). Where it sits in a docstring, the tag is on the line **after** the declaration, so a line-by-line filter reports every correctly tagged test as missing one. Pair each declaration with the next line first (pytest):

```bash
echo "NO ID (warns):"; xargs -r -d '\n' grep -nE -A1 'def test_' < $T/tests \
  | grep -v '^--$' | paste -d' ' - - | grep -vE "[\"'\`][A-Z]{2,5}-[0-9]+:"
```

Report three classes:

- **Untested**: a defined, non-waived ID with no tagged test. This fails the check.
- **Undefined ID**: a tagged test whose ID the spec does not define (or has dropped). Warn: a typo or a stale test.
- **No ID**: a test with no ID. Warn: possible scope creep, or a test worth tying to a requirement.

The check reads text, so it errs in both directions, unevenly. A commented-out or skipped test does not count as coverage, so its ID is reported untested: the safe direction. A string that merely starts with an ID and a colon does count, so keep IDs out of string literals that are not test names.

For one issue's check, replace `defined` with the IDs on that issue's `Covers:` line, then re-run the `UNTESTED` line above unchanged. It still subtracts `waived`, which matters because every ID lands on some issue's `Covers:` line, waived ones included:

```bash
grep -E '^Covers:' issue.md | grep -oE '[A-Z]{2,5}-[0-9]+' | sed 's/$/:/' | sort -u > $T/defined
```

The check confirms presence only. Whether a tagged test asserts what its requirement says is judgement, in two tiers: the Judgement pass below reads every tagged test cheaply, and `code-review`'s Spec sub-agent reads the tests against the spec as it always does.

## `docs/agents/traceability.md`

Optional, hand-written, absent by default: the grep above is the normal path. Each line is independently optional:

```
Check command: `<command>`
Spec input: `stdin` or `path`
Judgement: jev
```

`Check command:` names the repo's own presence check. With no such line, the grep block stays the presence check. The command exits 0 when every ID is covered and 1 when any is untested, and takes IDs as trailing arguments to narrow the check to them. `Judgement: jev` opts the repo in to the Judgement pass. When the user names a check command, or mentions Jev, offer to write the matching line.

## Judgement pass

The first tier of judging whether a tagged test asserts what its requirement says. It sends spec lines and tagged test excerpts (at most 60 lines each) to `api.typesafe.ai`, so it runs only when `TYPESAFE_API_KEY` is set **and** `docs/agents/traceability.md` has a `Judgement: jev` line. If either is missing, say "Judgement pass skipped" in one line and stop; do not point the user at setup.

Run [judge.mjs](judge.mjs) (Node, no packages) from the repo root, after the gap check. `-` reads the spec from stdin. Trailing IDs narrow the run: for one issue, take them from its `Covers:` line.

```bash
node <this skill's directory>/judge.mjs spec.md [ID...]
```

Exit 2 means it skipped, with the reason on stderr: report "skipped" and carry on. Otherwise it prints one row per ID, `ID | class | choice | confidence | test`, then the answering model and token use:

- **ok**: high-confidence `asserts`. Do not re-read.
- **flag**: high-confidence `partial` or `unrelated`: the requirement is not fully covered. Compare the requirement line with its tests, name the behaviour no assertion checks, and add assertions or tests (tagged with the ID) for it. Then re-run the pass for the flagged IDs. If you read the tests and still judge them complete, leave the flag and say why in your summary for review.

  **At most 3 rounds** of adding tests and re-running. If an ID is still flagged after the third re-run, stop and ask the user how to proceed: list each such ID, the behaviour you judge still unchecked, and what you tried. Do not start a fourth round unless the user says so.
- **uncertain**: low confidence, or no assertion call in the excerpt (an assertion inside a helper counts as none). Read the test yourself.
- **not judged**: no tagged test. The gap check owns presence.

The pass gates nothing: a flag or an uncertain row is a lead. Confidence moves about 0.03 between runs, so a row near 0.8 can switch between ok and uncertain.
