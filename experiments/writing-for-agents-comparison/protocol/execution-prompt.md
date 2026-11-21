# Execution prompt

Sent verbatim to each runner, one per (skill, case) pair, with `<DIR>` replaced by its sandbox path (`/tmp/wfa-exec/S?-C?`). The sandbox contains only `skill/` (one blinded candidate, renamed to its S label's folder) and `notes.md` (one case's meeting notes, unchanged).

---

You are an agent with one skill installed, in `<DIR>/skill/`. Work only inside `<DIR>`. Read, list and search nothing outside that directory, do not use the web, and do not invoke any other skills or skill tools.

The user has supplied meeting notes in `<DIR>/notes.md` and asks you to use the skill on them.

1. Read `<DIR>/skill/SKILL.md` and follow it, reading any files it points to inside `<DIR>/skill/`.
2. Produce what the skill says to produce for these notes and write it to `<DIR>/brief.md`. Write only the brief itself in that file.
3. The user is not available to answer questions. If the skill would have you ask the user something, write the question at the top of `brief.md` under a line `Clarifying question:` and then continue as the skill says to do without an answer.

When you finish, reply with every file you read (full paths) and one sentence on anything in the skill you found unclear.
