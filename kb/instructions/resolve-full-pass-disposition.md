---
description: Resolve, reject, supersede, or reconcile a retained full-pass delete or merge disposition
type: kb/types/instruction.md
---

# Resolve a full-pass disposition

Use this procedure when a typed `kb/reports/full-pass/*/*/full-pass-report.md` has `resolution: pending`, or when a failed guard left a report requiring reconciliation. The report and its `.txt` captures are one retention unit; never remove or rewrite a capture independently.

Inputs:

- `{report-path}` — one `full-pass-report.md` under `kb/reports/full-pass/`.
- explicit user decision when accepting, rejecting, or applying an alternative. Agents may mark `superseded` only from a deterministic changed-input guard result.

## Inspect and guard

1. Read the full report and its `source`, `disposition`, rationale, merge fields, and current `resolution`. Stop if it is not `pending` unless reconciling an interrupted transition.
2. Run `commonplace-validate {report-path}`. A validation failure blocks resolution.
3. Run `commonplace-guard-full-pass-report {report-path}` immediately before recording a rejection or beginning any filesystem mutation.
4. Interpret the JSON and exit status:
   - Exit 0 with every input `matching`: the decision may proceed.
   - Exit 1 with any `changed`: preserve every live artifact and resolve the report to `superseded` with `resolution_authority: version-guard`. State which guarded paths changed. Do not accept, reject, rebase, or apply an alternative.
   - Exit 1 with `missing` or `corrupt-capture`: leave `resolution: pending` and reconcile. Absence cannot prove a delete or merge succeeded; capture corruption is not source drift.
   - Exit 2: leave the report unchanged and repair or reconcile the invalid invocation/report.

If several inputs are returned, inspect every result; the command never short-circuits after the first failure.

## Resolve a matching recommendation

Proceed only with an explicit user decision:

- **Accept delete.** Delete only `source`. Verify it is absent and that no unintended path changed. Then record `accepted`; `resulting_paths` is empty.
- **Accept merge.** Reconcile the captured source into the named live `merge_target` as a semantic edit, update affected backlinks as needed, remove invalid `user-verified` attestation from the edited target, and delete the source only after the target contains the accepted result. Verify the source is absent, the target exists at the recorded path, and validation succeeds. Record `accepted` with the target in `resulting_paths`. Do not substitute `commonplace-relocate-note` for semantic reconciliation.
- **Reject.** Leave source and target byte-identical. Record `rejected` with every guarded live path in `resulting_paths` and explain why the recommendation was declined.
- **Apply an alternative.** Perform only the user-authorized alternative, verify every resulting path and validate each edited artifact, then record `alternative-applied` with all surviving result paths. An opposite-direction merge is an alternative, not acceptance of the original merge.

Never record a terminal state before its filesystem postconditions succeed. If mutation succeeds only partly, leave the report pending and reconcile the ambiguous state.

## Render terminal resolution

Update the canonical frontmatter fields:

```yaml
resolution: accepted | rejected | alternative-applied | superseded
resolved_at: "<UTC ISO-8601 timestamp>"
resolution_authority: user | version-guard
resolution_summary: <what happened>
resolution_rationale: <why>
resulting_paths: [<every surviving path left by the resolution>]
```

Use `user` only for accepted, rejected, or alternative decisions. Use `version-guard` only for deterministic supersession caused by a readable changed input. Deterministically render `## Resolution` from those fields: null or empty values are `—`; non-empty resulting paths are comma-separated code spans.

Run `commonplace-validate {report-path}` after rendering. Retain the report and captures while a rejection or alternative remains load-bearing. An accepted report may be removed with its packet after Git history durably records the operation; pending reports must never be pruned.
