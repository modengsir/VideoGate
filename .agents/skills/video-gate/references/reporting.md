# Reporting contract

Return a human-readable Markdown table with **all eight checks** for the selected gate:

| Rule | Status | Severity | Evidence / location | Minimal fix |
|---|---|---|---|---|
| G1-01 | FAIL | P0 | script line 2 contradicts character description | Lock original style anchor |

Then give counts of PASS/FAIL/UNVERIFIED, blocking prerequisites, top three repair actions, decision (`BLOCKED`/`READY_WITH_NOTES`/`READY`), explicitly unseen media, and a reminder that human sign-off is required.

Machine-readable results must follow `schemas/review-result.schema.json` from repository root. Exactly eight checks, stable numbered IDs in order. Required top-level fields: `schema_version`, `gate`, `input_version`, `reviewer`, `capabilities`, `checks`, `decision`, `ready_for_next_stage`, `human_approval_required`, `limitations`. Each check: `rule_id`, `status`, `severity`, `location`, `evidence`, `minimal_fix`. Do not claim the result was programmatically validated unless you ran a validator.
