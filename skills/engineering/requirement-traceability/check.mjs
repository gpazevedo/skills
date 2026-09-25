#!/usr/bin/env node
// Coverage gap check: every live, non-waived requirement ID has a tagged test that is not commented out or skipped.
// Usage: node check.mjs <spec.md | -> [ID...]   ("-" reads the spec from stdin; IDs narrow UNTESTED, e.g. to one ticket's Covers: line)
// Exit 0: every ID is tested. Exit 1: some ID is untested.
import { readFileSync } from "node:fs";
import { readSpec, taggedIds, testFiles, untagged } from "./tags.mjs";

const byNumber = (a, b) => a.localeCompare(b, "en", { numeric: true });

const [spec, ...ids] = process.argv.slice(2);
const { stories, waived } = readSpec(readFileSync(spec === "-" ? 0 : spec, "utf8"));
const defined = new Set(stories.map((s) => s.id));
const expected = ids.length ? ids.map((i) => i.replace(/:$/, "")) : [...defined];
const files = testFiles();
const tagged = taggedIds(files);

const untested = expected.filter((id) => !tagged.has(id) && !waived.has(id)).sort(byNumber);
const undefinedIds = [...tagged].filter((id) => !defined.has(id)).sort(byNumber);

console.log("UNTESTED (fails):");
untested.forEach((id) => console.log(`${id}:`));
console.log("UNDEFINED ID (warns):");
undefinedIds.forEach((id) => console.log(`${id}:`));
console.log("NO ID (warns):");
untagged(files).forEach((line) => console.log(line));
process.exit(untested.length ? 1 : 0);
