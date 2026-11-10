# Reporting contract

Start with the selected gate, target specs and materials actually reviewed. Return a Markdown table with **all eight checks** for the selected gate.

| Rule and check | Status | Severity | Evidence / location | Minimal fix or evidence needed |
|---|---|---|---|---|
| G1-01 Character continuity | FAIL | P0 | Script line 2 contradicts the character description | Match the description to the approved reference |

- Cite the relevant quote, shot, timestamp or image ID and visible region. For UNVERIFIED, name the missing material or capability and what would resolve the check. Label any unverified P0 separately as a blocking prerequisite.
- Give counts of PASS/FAIL/UNVERIFIED and at most three priority actions.
- Give the stage recommendation (`BLOCKED`/`READY_WITH_NOTES`/`READY`) and its reason. List what could not be inspected, what materials are still needed and what the creator should verify manually before signing off.

Machine-readable results must follow `schemas/review-result.schema.json` from repository root. Exactly eight checks, stable numbered IDs in order. Required top-level fields: `schema_version`, `gate`, `input_version`, `reviewer`, `capabilities`, `checks`, `decision`, `ready_for_next_stage`, `human_approval_required`, `limitations`. Each check: `rule_id`, `status`, `severity`, `location`, `evidence`, `minimal_fix`. Do not claim the result was programmatically validated unless you ran a validator.
