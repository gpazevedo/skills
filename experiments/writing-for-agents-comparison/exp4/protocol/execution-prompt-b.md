# Execution prompt (experiment 4, part b)

Sent verbatim to each runner, with `<DIR>` replaced by its sandbox path (`/tmp/wfa4-exec/b/S?-C?`). The sandbox contains only `skill/` (one blinded candidate) and `input/` (one case folder, unchanged).

---

You are an agent with one skill installed, in `<DIR>/skill/`. Work only inside `<DIR>`. Read, list and search nothing outside that directory, do not use the web, and do not invoke any other skills or skill tools.

The user has supplied an expense claim in `<DIR>/input/` and asks you to use the skill on it.

1. Read `<DIR>/skill/SKILL.md` and follow it, reading any files it points to inside `<DIR>/skill/`.
2. Produce what the skill says to produce and write it to `<DIR>/review.md`. Write only the review itself in that file.
3. The user is not available to answer questions. If the skill would have you ask the user something, write the question at the top of `review.md` under a line `Clarifying question:` and then continue as the skill says to do without an answer.
4. Write `<DIR>/runlog.json` as a JSON object: `{"files_read": [full paths], "unclear": "one sentence on anything in the skill you found unclear"}`.

When you finish, reply with one line: done.
