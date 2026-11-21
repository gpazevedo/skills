# Generation prompt (experiment 4, all parts)

Differs from experiment 3 in one way: the genlog has no `tested` or `testing_note` field, so the log does not prompt testing; whether a generator tested is read from what it left in `scratch/`, which is collected. Sent verbatim to each generator, with `<DIR>` replaced by its sandbox path (`/tmp/wfa4-gen/<part>-G?`). The sandbox contains only `writing-for-agents/` (the assigned variant), `request.md` (the part's skill request) and an empty `out/`.

---

You are writing a new agent skill. Work only inside `<DIR>`. Read, list and search nothing outside that directory, do not use the web, and do not invoke any skills or skill tools: the only writing guidance you may use is the one in the directory.

1. Read `<DIR>/writing-for-agents/SKILL.md` and any files it points you to inside `<DIR>/writing-for-agents/`. Apply that guidance to the task below.
2. Read `<DIR>/request.md`. It is the request for the skill you must write.
3. Write the skill into `<DIR>/out/`, as the request says. You may create your own example inputs inside `<DIR>/scratch/` if you want to try the skill; nothing in `scratch/` is part of the skill.
4. Write `<DIR>/genlog.json` as a JSON object: `{"files_read": [full paths], "files_written": [paths in out/], "applied_note": "two or three sentences on how you applied the writing guidance"}`.

When you finish, reply with one line: done.
