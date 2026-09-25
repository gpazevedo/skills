#!/usr/bin/env bash
# Runs the coverage gap check (check.mjs) and the Covers: structural check against
# scripts/fixtures/traceability, and compares each output to its recorded expectation.
# The structural check is extracted from SKILL.md, so the skill's text is what is under test.
set -uo pipefail

ROOT=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
SKILL=$ROOT/skills/engineering/requirement-traceability/SKILL.md
FIXTURE=$ROOT/scripts/fixtures/traceability
WORK=$(mktemp -d)
trap 'rm -rf "$WORK"' EXIT

CHECK=$ROOT/skills/engineering/requirement-traceability/check.mjs

# The first bash block under "### Structural check".
awk '
  /^### Structural check/ { sec = 1; next }
  !sec { next }
  /^```bash/ && !done { inblk = 1; next }
  inblk && /^```/ { inblk = 0; done = 1; next }
  inblk { print }
' "$SKILL" > "$WORK/covers.sh"

[ -s "$WORK/covers.sh" ] || { echo "FAIL: no bash block found under '### Structural check'"; exit 1; }

cp -r "$FIXTURE"/. "$WORK/repo"
cd "$WORK/repo"
git init -q . && git add -A

node "$CHECK" spec.md > "$WORK/actual.txt" 2>"$WORK/err.txt"; check_exit=$?
node "$CHECK" spec.md CPN-2 CPN-6 > /dev/null 2>>"$WORK/err.txt"; narrowed_exit=$?

bash "$WORK/covers.sh" > "$WORK/covers-actual.txt" 2>>"$WORK/err.txt"

status=0
if diff -u expected.txt "$WORK/actual.txt"; then
  echo "PASS: coverage gap check matches the fixture expectation"
else
  echo "FAIL: the check's output drifted from scripts/fixtures/traceability/expected.txt"; status=1
fi
if [ "$check_exit" = 1 ] && [ "$narrowed_exit" = 0 ]; then
  echo "PASS: the check exits 1 on an untested ID and 0 when narrowed to tested ones"
else
  echo "FAIL: exit codes were $check_exit (want 1) and $narrowed_exit narrowed (want 0)"; status=1
fi
if diff -u expected-covers.txt "$WORK/covers-actual.txt"; then
  echo "PASS: structural check matches the fixture expectation"
else
  echo "FAIL: the structural check's output drifted from scripts/fixtures/traceability/expected-covers.txt"; status=1
fi
[ "$status" = 0 ] || { [ -s "$WORK/err.txt" ] && { echo "--- stderr ---"; cat "$WORK/err.txt"; }; }
exit $status
