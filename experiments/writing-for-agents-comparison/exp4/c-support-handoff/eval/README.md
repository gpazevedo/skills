# Evaluation set (experiment 4, part c)

Copy of the experiment 3 part c set (`../../../exp3/c-support-handoff/eval/`), with two changes made before the `wfa4/preregistered` tag:

1. **As-of time.** Every `thread.md` now has an "As-of time" line right after the export header, giving the escalation time from the answer key (the time the key already says the handoff is judged at). Runners are told to treat it as the current time and not to use the machine's clock. In experiment 3, 24 of 72 handoffs mentioned the sandbox date because the cases had no as-of time.
2. **Concision bound.** The rubric's concision criterion is 10 for 800 words or fewer of the handoff's own prose, 5 for 801 to 1,200, 0 beyond. Dry run (`../../dry-run/`): two fresh agents with no skill, told to write the shortest complete handoff, produced 707 words of own prose for case 01 and 1,047 for case 03. The old bound of 350 words was unreachable (no handoff in experiment 3 met it). 800 is about 1.15 times the simple-case figure and 1,200 about 1.15 times the complex-case figure.

Cases' facts, answer keys and all other rubric criteria are unchanged. The dry run's two handoffs are throwaway: they were written without any candidate skill, the keys were not shown to the agents, and they are not scored.

Companies: Quillbill (cloud invoicing, UK hours; cases 01, 04, 05) and Tern Systems (IoT gateway, Perth hours UTC+8; cases 02, 03, 06).
