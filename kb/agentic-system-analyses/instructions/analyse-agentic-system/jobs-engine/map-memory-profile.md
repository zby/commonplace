---
description: "Use after record verification to classify accepted memory records into a revision-2 comparison profile"
type: types/instruction.md
---

# Map memory profile

Give comparison consumers supported memory values with the uncertainty each value carries expressed in the value itself.

Read this instruction first, then all invocation Input reading batches. Follow
`worker-rules`, `collection`, `sources-contract`, `records-contract` and
`memory-profile-contract`.

## Inputs and result

`boundary` fixes the frozen source and scope. `runtime`, `memory`, `epistemic`
and `reconciliation` are accepted records, gated by holding record-verification
acceptances. Read their supplied versions, not reconstructed member paths.
`opening` supplies the prepared command directory for the shared content check.

Write the complete revision-2 profile to `output`. On a retry, use
`previous-profile` and `previous-answers` as read-only baselines and answer
`refusal` under the shared correction protocol. There are three attempts
total, including failures; acceptance does not reset them.

## Classify from records

Apply the profile and record contracts without added classification conditions.
Each asserted value cites canonical accepted records, resolving supersessions
through reconciliation. Keep the natural units, separate evidence bases and
all supported positives beside unresolved parts. A positive witness does not
establish inventory completeness. `known` requires coverage evidence and all
included units resolved. Retain unresolved included units; do not omit them,
classify them absent or make them inapplicable because another route is known.
Name missing facts and prevented conclusions in warranted `partial`,
`uninspected` or `not-determinable` assessments. Preserve route-specific
strength; do not upgrade opaque alternatives from one wired witness.

Declare no records, add no quotes or evidence, edit no member and do not
reopen record verification. Do not read incumbent or reference profiles.
Source reading is limited to a named ambiguity in a cited record, at its
cited paths and frozen revision. Log each read under Comparison rationale
with path, lines and ambiguity resolved. Source understanding cannot replace
a missing supporting record. Do not execute or install the target.

## Check and return

Run the shared content check and repair findings. Code additionally
checks comparison revision, source and run identity, frozen-source integrity
and correction answers; semantic verification checks support and coverage.
A content pass is not acceptance. A missing required input, unauthorized scope
change or inability to produce a faithful profile requires `problem` and stop.
Do not delegate or publish. Return one line naming both output files.
