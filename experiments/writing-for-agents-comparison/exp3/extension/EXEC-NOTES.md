# Execution notes (extension)

- c/S3-C6: first runner stopped by an API usage limit after writing a partial handoff.md and no runlog; the partial output was deleted and the run repeated with a fresh agent in the same sandbox after the limit reset.
- c/S9-C3: runner's final reply failed with the same API error, but handoff.md and runlog.json were complete; kept.
- a/S6-C6: omitted from its batch by the orchestrator (13th in the sealed order) and run last, after the other 107; same prompt and sandbox.
- Every runlog lists only files inside its own sandbox.
