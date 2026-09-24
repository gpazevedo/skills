# A skill may call a third-party API only behind an env key and a per-repo opt-in

`requirement-traceability`'s Judgement pass sends spec lines and tagged test excerpts (at most 60 lines each) to `api.typesafe.ai`. [ADR 0001](./0001-explicit-setup-pointer-only-for-hard-dependencies.md) records when a skill prints a setup pointer. This records when a skill sends repo content to someone else.

The rule: the call runs only when **both** an API key is set in the environment **and** the repo's hand-written `docs/agents/*.md` file carries an opt-in line (`Judgement: jev` in `docs/agents/traceability.md`). If either is missing the skill says "skipped" in one line and does nothing else. It prints no setup pointer: like the soft-dependency skills in ADR 0001, it degrades without the extra.

What it protects: this plugin installs into other people's repos, and a key in a shell is not consent for every repo that shell works in. The opt-in line is per repo and lives in the repo, so anyone reading the repo can see that it sends content out. The key is only ever read from the environment: never written to a file, a docs page, a changeset or a log.

The fallback: the skill behaves exactly as it did without the call. Here that means `code-review`'s Spec sub-agent reads every tagged test. The call is a first tier and never a gate, so a bad key, a rate limit or an outage costs the saving and nothing else.

`judge.mjs` is the first **runnable** file a promoted skill ships. `wizard/template.sh` and `hitl-loop.template.sh` are templates the agent copies into the user's repo, and `block-dangerous-git.sh` is a hook in `misc/`. Referring to a bundled file by relative link has precedent; shipping code that runs inside the consumer's repo does not, which is why the rule above exists.
