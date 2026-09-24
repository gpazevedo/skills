#!/usr/bin/env bash
# Runs the coverage gap check exactly as `requirement-traceability/SKILL.md` writes it,
# against scripts/fixtures/traceability, and compares the output to the recorded expectation.
# The block is extracted from SKILL.md, so the skill's text is what is under test.
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

cp -r "$FIXTURE"/. "$WORK/repo"
cd "$WORK/repo"
git init -q . && git add -A

bash "$WORK/check.sh" > "$WORK/actual.txt" 2>"$WORK/err.txt"
cat expected.txt expected-pytest.txt > "$WORK/want.txt"

if diff -u "$WORK/want.txt" "$WORK/actual.txt"; then
  echo "PASS: coverage gap check matches the fixture expectation"
  exit 0
fi
echo "FAIL: the check's output drifted from scripts/fixtures/traceability/expected*.txt"
[ -s "$WORK/err.txt" ] && { echo "--- stderr ---"; cat "$WORK/err.txt"; }
exit 1
