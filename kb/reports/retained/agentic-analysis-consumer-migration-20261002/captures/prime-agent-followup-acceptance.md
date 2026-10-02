# Prime Agent handoff follow-up acceptance

The operator authorized three fixes after the Prime Agent session report:
`kb/messages/20260905T191941Z-codex-orchestration-prime-agent-session-report.md`.
The citation clarification is explicit: quoted source code must be verified
by full-text search, not by trusting manually assigned line numbers.

## Implemented contract

1. The run-state type includes a copyable Git source mapping with `path` and
   `sha256: null`. Startup requires validation after filling the source, before
   inspection or delegation. This does not add an initializer or phase ledger.
2. Main and specialist procedures require minimal verbatim source excerpts for
   load-bearing findings. Code supports implementation claims; source prose can
   support claim-level findings. The parent retains each passage once on its
   canonical record. Existing publication checks search the whole pinned blob
   or immutable capture after whitespace normalization. Display line numbers,
   invented ellipses and formatting fences are excluded from quoted text.
   Complete results and memory reports with no quote anchors now fail standing
   validation. This catches the prior total omission of quoted evidence; it
   does not establish coverage or semantic support for every material claim.
3. Handoffs spell every identifier in full. Integration maps exact tokens after
   expansion, without substring replacement or implicit ranges. Standing result
   validation checks declarations and canonical references throughout ordinary
   prose, not only comparison fields. It rejects duplicate record declarations,
   unresolved canonical references, unintegrated proposal IDs outside
   Reconciliation, and shorthand/ranges. Source quotations and
   fenced evidence are excluded from identifier scanning. Memory reports reject
   shorthand; their comparison references retain the existing commissioned and
   proposed-record checks.

These requirements apply to the current workflow without an old-format
fallback. Completed generated analyses are not patched to pass the new rules.
The Prime Agent output remains the session's original evidence, not a newly
attested result under this contract.

## Bounded verification

Regression cases include the reported `OBJ-15/O2/O3/O4/O5` and `RTE-20–R9`, a
shortened tail after two full IDs, complete lists, unresolved references outside
comparison fields, duplicate declarations and unrelated IDs inside source
quotations/fences. An integration test proves the standing result validator
rejects corrupted prose references. The corrected Prime Agent result passes
the new identifier scan; that check does not retroactively certify its source
evidence under the restored quote requirement.

A publication fixture without quotes now fails for either its main result or
memory report. A pinned source-code fixture proves that quoted code is found
outside the attributed navigation line, while fabricated text present only in
the changed worktree is rejected. The Git source example passes actual running
state validation after substitution of the fixture repository and revision.

All 769 tests pass. Repository Ruff, changed-document validation and diff
checks pass. This is a machinery and contract check, not a
fresh production analysis or semantic audit of Prime Agent.
