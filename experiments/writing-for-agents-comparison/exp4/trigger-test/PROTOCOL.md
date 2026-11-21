# Description triggering test (experiment 4, phase 6)

Fixed before any generation. Reported separately from the verdict; it does not enter the decision rule.

## Question

Does revision 2's frontmatter description make the skill more or less likely to be chosen at the right moments than the original's?

## Procedure

- Two descriptions are tested, each in its own skill list: the original's and V2's (copied verbatim from `variants/original/writing-for-agents/SKILL.md` and `variants/improved-v2/writing-for-agents/SKILL.md`).
- Each skill list holds the tested skill and four fixed distractors: `pdf-tools` ("Read, merge, split and fill PDF files."), `commit-message` ("Write git commit messages from a diff."), `email-drafting` ("Draft and edit professional emails and letters."), `code-review` ("Review code changes for bugs and style problems.").
- For each description, two fresh agents with clean contexts (4 runs in total). Each sees only the skill list (name and description of five skills) and the 20 prompts below in its own random order, and answers for each prompt with the one skill name it would invoke first, or `none`. It is told nothing about the experiment, the tested skill's origin, or which prompts should trigger.
- A run's accuracy is the share of its 20 answers that are correct: `writing-for-agents` for prompts 1 to 10 (should trigger), anything else for prompts 11 to 20 (should not).
- Report accuracy, hits on the 10 positives and false triggers on the 10 negatives, per description, over the two runs.

## Prompts

Should trigger (writing or reviewing documents agents read):

1. Create a new skill that triages incoming bug reports for our repo.
2. Our AGENTS.md has grown to 600 lines and the agent keeps ignoring parts of it. Can you restructure it?
3. Review this SKILL.md and tell me why the agent skips step 3.
4. Write a CLAUDE.md for this monorepo so agents know the build commands and conventions.
5. Improve the description in my skill's frontmatter so it triggers more reliably.
6. I wrote a workflow doc for our deployment agent; can you check that its completion criteria are clear?
7. Edit our AGENTS.md to point to the testing guide instead of inlining it.
8. Draft a skill that walks an agent through preparing a release changelog.
9. Tighten the instructions file our support agent reads on every run; it's too long and vague.
10. Split this big SKILL.md into a main file and reference files the agent loads on demand.

Should not trigger (ordinary prose and other work):

11. Tighten the intro paragraph of my blog post about sourdough.
12. Write a README for my open-source library aimed at new users.
13. Fix the grammar in this cover letter.
14. Summarise this research article in five bullet points.
15. Draft an email to my landlord asking about the broken heater.
16. Write a commit message for this diff.
17. Review this Python function for bugs.
18. Rewrite my speech opening so it sounds less formal.
19. Explain how large language models use a system prompt.
20. Edit the user guide for our mobile app to be friendlier to customers.
