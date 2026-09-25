// Tests tags.mjs, the rules check.mjs and judge.mjs share, against scripts/fixtures/judge.
// Run: node --test scripts/test-tags.mjs
import { test } from "node:test";
import assert from "node:assert/strict";
import { excerpts, locations, taggedIds, untagged } from "../skills/engineering/requirement-traceability/tags.mjs";

process.chdir(new URL("fixtures/judge", import.meta.url).pathname);

const code = (id, file) => excerpts(id, [file]).map((e) => e.code);

test("a Python test ends where its body dedents", () => {
  assert.deepEqual(code("CRT-1", "tests/test_cart.py"), [
    '    """CRT-1: the total includes tax."""\n    assert total(100) == 110',
  ]);
});

test("a Python test method ends at the next method", () => {
  assert.deepEqual(code("CRT-2", "tests/test_cart.py"), [
    '        """CRT-2: a discount lowers the total."""\n        assert total(100, discount=10) == 99',
  ]);
});

test("a JS test ends at its closing parenthesis", () => {
  assert.deepEqual(code("CRT-3", "tests/cart.test.ts"), [
    "it('CRT-3: adds an item to the cart', () => {\n  expect(add([], 'apple')).toEqual(['apple']);\n});",
  ]);
});

test("a one-line JS test ends on its own line", () => {
  assert.deepEqual(code("CRT-4", "tests/cart.test.ts"), [
    "it('CRT-4: empties the cart', () => expect(clear(['apple'])).toEqual([]));",
  ]);
});

test("a JS tag on the line after it( ends where it( closes", () => {
  assert.deepEqual(code("CRT-5", "tests/cart.test.ts"), [
    "  'CRT-5: rejects a quantity of zero with a very long explanatory test name',\n  () => {\n    expect(() => add([], 'apple', 0)).toThrow('bad quantity :)');\n  },\n);",
  ]);
});

test("a Go subtest ends where t.Run closes", () => {
  assert.deepEqual(code("CRT-6", "tests/cart_test.go"), [
    '\tt.Run("CRT-6: sums prices", func(t *testing.T) {\n\t\tif Sum(1, 2) != 3 {\n\t\t\tt.Errorf("want 3 (got %d)", Sum(1, 2))\n\t\t}\n\t})',
  ]);
});

test("a test up to 200 lines is sent whole", () => {
  const [excerpt] = excerpts("CRT-7", ["tests/cart.test.ts"]);
  assert.equal(excerpt.code.split("\n").length, 101);
  assert.equal(excerpt.cut, false);
});

test("a test over 200 lines is cut at 200 and marked", () => {
  const [excerpt] = excerpts("CRT-8", ["tests/cart.test.ts"]);
  assert.equal(excerpt.code.split("\n").length, 200);
  assert.equal(excerpt.cut, true);
});

test("the output row marks a file whose excerpt was cut", () => {
  const tests = [...excerpts("CRT-8", ["tests/cart.test.ts"]), ...excerpts("CRT-1", ["tests/test_cart.py"])];
  assert.equal(locations(tests), "tests/cart.test.ts (cut), tests/test_cart.py");
});

test("a skipped test is not sent, even when its name wraps", () => {
  assert.deepEqual(excerpts("CRT-9", ["tests/cart.test.ts"]), []);
});

test("a Python test under a skip decorator is not sent", () => {
  assert.deepEqual(excerpts("CRT-10", ["tests/test_cart.py"]), []);
});

test("NO ID lists untagged tests in every language, wrapped names included", () => {
  const files = ["tests/cart.test.ts", "tests/test_cart.py", "tests/cart_test.go", "tests/untagged.test.ts"];
  assert.deepEqual(untagged(files), [
    "tests/cart.test.ts:22:it('after CRT-5', () => {});",
    "tests/test_cart.py:15:    def test_untagged(self):",
    'tests/cart_test.go:11:\tt.Run("untagged", func(t *testing.T) {})',
    "tests/cart_test.go:14:func TestNoSubtests(t *testing.T) {",
    "tests/untagged.test.ts:1:it('has no id', () => {});",
    "tests/untagged.test.ts:3:it(",
  ]);
});

test("a skipped or commented-out tag is not coverage", () => {
  const ids = taggedIds(["tests/cart.test.ts", "tests/test_cart.py"]);
  assert.ok(ids.has("CRT-3") && ids.has("CRT-5") && ids.has("CRT-1"));
  assert.ok(!ids.has("CRT-9") && !ids.has("CRT-10"));
});

test("an ID inside an assertion value is not a tag", () => {
  const files = ["tests/strings.test.ts", "tests/test_strings.py", "tests/strings_test.go"];
  const ids = taggedIds(files);
  assert.deepEqual([...ids], []);
  assert.deepEqual(excerpts("CRT-12", files), []);
});
