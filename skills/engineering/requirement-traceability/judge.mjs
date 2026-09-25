#!/usr/bin/env node
// Judgement pass: per requirement ID, ask Jev whether the tagged tests assert what the requirement says.
// Usage: node judge.mjs <spec.md | -> [ID...]   ("-" reads the spec from stdin)
// Exit 0: the pass ran. Exit 2: skipped, one line on stderr says why.
import { existsSync, readFileSync } from "node:fs";
import { STRINGS, excerpts, locations, readSpec, testFiles } from "./tags.mjs";

const URL = "https://api.typesafe.ai/v1/systemone";
const GATE = 0.8; // Choice confidence at or above this counts as decided
const CONCURRENCY = 5;
const MAX_RETRIES = 4;
const ASSERTION = /\b(expect|should)\s*\(|\bassert|\bt\.(Errorf?|Fatalf?)\b/;

const QUESTION = {
  verdict: {
    type: "choice",
    instructions: "How much of the behaviour `requirement` describes do the assertions in `tests` check? The behaviour is what the requirement says the system does. A 'so that ...' clause says why the user wants it and is not itself behaviour a test has to assert.",
    criteria: {
      asserts: "The assertions check the behaviour the requirement describes",
      partial: "The assertions check part of that behaviour and leave another part unchecked",
      unrelated: "The assertions check something else, or the tests assert nothing at all",
    },
  },
};

class Skip extends Error {}

function optedIn() {
  if (!process.env.TYPESAFE_API_KEY) throw new Skip("TYPESAFE_API_KEY is not set");
  const file = "docs/agents/traceability.md";
  if (!existsSync(file) || !/^Judgement:\s*jev\s*$/m.test(readFileSync(file, "utf8")))
    throw new Skip(`${file} has no "Judgement: jev" line`);
}

async function post(body, attempt = 0) {
  const res = await fetch(URL, {
    method: "POST",
    headers: { Authorization: `Bearer ${process.env.TYPESAFE_API_KEY}`, "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
  if ([429, 529].includes(res.status) && attempt < MAX_RETRIES) {
    const wait = Number(res.headers.get("retry-after")) || 2 ** attempt;
    await new Promise((r) => setTimeout(r, wait * 1000));
    return post(body, attempt + 1);
  }
  if (res.status === 401) throw new Skip("the API key was rejected (401)");
  if (!res.ok) {
    const { detail } = await res.json();
    throw new Skip(`HTTP ${res.status}: ${JSON.stringify(detail?.message ?? detail)} (${res.headers.get("x-typesafe-request-id")})`);
  }
  return res.json();
}

async function judge({ id, requirement }, files) {
  const tests = excerpts(id, files);
  const where = locations(tests);
  if (!tests.length) return { id, cls: "not judged", choice: "no tagged test", confidence: "-", where };
  if (!tests.some((t) => ASSERTION.test(t.code.replace(STRINGS, ""))))
    return { id, cls: "uncertain", choice: "no assertion call", confidence: "-", where };
  const body = await post({ model: "jev-latest", state: { requirement, tests: tests.map(({ file, code }) => ({ file, code })) }, questions: QUESTION });
  const { choice, confidence } = body.answers.verdict;
  const cls = confidence < GATE ? "uncertain" : choice === "asserts" ? "ok" : "flag";
  return { id, cls, choice, confidence: confidence.toFixed(2), where, model: body.model, tokens: body.usage.input_tokens };
}

async function main() {
  const [spec, ...ids] = process.argv.slice(2);
  optedIn();
  const only = ids.map((i) => i.replace(/:$/, ""));
  const { stories: all, waived } = readSpec(readFileSync(spec === "-" ? 0 : spec, "utf8"));
  const stories = all.filter(({ id }) => !waived.has(id) && (!only.length || only.includes(id)));
  const files = testFiles();
  const results = [];
  let next = 0;
  const worker = async () => {
    while (next < stories.length) {
      const i = next++;
      results[i] = await judge(stories[i], files);
    }
  };
  await Promise.all(Array.from({ length: CONCURRENCY }, worker));
  for (const r of results) console.log([r.id, r.cls, r.choice, r.confidence, r.where].join(" | "));
  const models = [...new Set(results.map((r) => r.model).filter(Boolean))].join(", ") || "-";
  const tokens = results.reduce((n, r) => n + (r.tokens ?? 0), 0);
  console.log(`model: ${models}, input tokens: ${tokens}`);
}

main().catch((e) => {
  if (!(e instanceof Skip)) throw e;
  console.error(`Judgement pass skipped: ${e.message}`);
  process.exit(2);
});
