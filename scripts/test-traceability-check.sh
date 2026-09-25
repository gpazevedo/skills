#!/usr/bin/env bash
# Runs the coverage gap check and the Covers: structural check exactly as
# `requirement-traceability/SKILL.md` writes them, against scripts/fixtures/traceability,
# and compares each output to its recorded expectation.
# The blocks are extracted from SKILL.md, so the skill's text is what is under test.
set -uo pipefail

ROOT=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
SKILL=$ROOT/skills/engineering/requirement-traceability/SKILL.md
FIXTURE=$ROOT/scripts/fixtures/traceability
WORK=$(mktemp -d)
trap 'rm -rf "$WORK"' EXIT

# The first two bash blocks under "## Coverage gap check": the check, then the pytest variant.
awk '
  /^## Coverage gap check/ { sec = 1; next }
  !sec { next }
  /^```bash/ && !inblk { n++; if (n <= 2) inblk = 1; next }
  inblk && /^```/ { inblk = 0; next }
  inblk { print }
' "$SKILL" > "$WORK/check.sh"

[ -s "$WORK/check.sh" ] || { echo "FAIL: no bash block found under '## Coverage gap check'"; exit 1; }

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

bash "$WORK/check.sh" > "$WORK/actual.txt" 2>"$WORK/err.txt"
cat expected.txt expected-pytest.txt > "$WORK/want.txt"

bash "$WORK/covers.sh" > "$WORK/covers-actual.txt" 2>>"$WORK/err.txt"

status=0
if diff -u "$WORK/want.txt" "$WORK/actual.txt"; then
  echo "PASS: coverage gap check matches the fixture expectation"
else
  echo "FAIL: the check's output drifted from scripts/fixtures/traceability/expected*.txt"; status=1
fi
if diff -u expected-covers.txt "$WORK/covers-actual.txt"; then
  echo "PASS: structural check matches the fixture expectation"
else
  echo "FAIL: the structural check's output drifted from scripts/fixtures/traceability/expected-covers.txt"; status=1
fi
[ "$status" = 0 ] || { [ -s "$WORK/err.txt" ] && { echo "--- stderr ---"; cat "$WORK/err.txt"; }; }
exit $status
