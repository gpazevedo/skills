# Generation prompt

Sent verbatim to each generator (G1 to G6), with `<DIR>` replaced by its sandbox path (`/tmp/wfa-gen2/G?`). The sandbox contains only `writing-for-agents/` (the assigned variant), `request.md` (a copy of `skill-request.md`) and an empty `out/`.

---

You are writing a new agent skill. Work only inside `<DIR>`. Read, list and search nothing outside that directory, do not use the web, and do not invoke any skills or skill tools: the only writing guidance you may use is the one in the directory.

1. Read `<DIR>/writing-for-agents/SKILL.md` and any files it points you to inside `<DIR>/writing-for-agents/`. Apply that guidance to the task below.
2. Read `<DIR>/request.md`. It is the request for the skill you must write.
3. Write the skill into `<DIR>/out/`, as the request says. You may create your own example inputs inside `<DIR>/scratch/` if you want to try the skill; nothing in `scratch/` is kept.

When you finish, reply with:
- the files you wrote in `out/`;
- every file you read, with full paths;
- two or three sentences on how you applied the writing guidance.
