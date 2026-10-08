---
description: "Use to independently judge profile support, natural units and inventory coverage against exact handed records"
type: types/instruction.md
---

# Verify memory profile

Give comparison consumers an independent judgment of whether the handed profile's values and coverage assessments are supported.

Read this instruction first, then all invocation Input reading batches. Follow
`worker-rules`, `collection`, `sources-contract`, `records-contract`,
`memory-profile-contract` and `profile-verification-contract`.

## Inputs and result

Judge the exact supplied `profile` against `boundary`, `runtime`, `memory`,
`epistemic` and `reconciliation`. Read `profile-answers` and `profile-refusal`
when supplied; assess declines as arguments, not established defects or repairs.
Do not inspect current-member paths or other attempts. `opening` supplies the
prepared content-check command directory.

Write the verdict to `output` with `verifies: profile`, the supplied `run-id`
and the boundary's `reviewed-boundary`. Apply the verification contract's
exact Verification, Blockers and Limits format. On retry, use
`previous-verification` and `previous-answers` as read-only baselines and
answer `refusal` under the shared correction protocol. There are three
attempts total, including failures; acceptance does not reset them.

## Judge classification

Check every axis for scope, support, coverage and its natural units. Resolve
superseded records through reconciliation. Inventory coverage is independent
of positive witnesses: `known` requires resolved included units and accepted
coverage evidence. Retain unresolved included alternatives rather than
omitting them or inferring absence or inapplicability from a known alternative.
Apply the supplied definitions without added conditions. Preserve supported
positives and route-specific evidence strength beside unresolved parts.

Use the verification contract's materiality threshold. An unsupported emitted
value or strength, unjustified absence or complete coverage, or materially
misleading bounded account is a blocker. Explain the incorrect inference and
why a limit cannot contain it. An authoring-ideal departure alone is not enough.
A local omission, coarse unit or cautious assessment can be a limit when the
axis already expresses incomplete coverage and emitted findings remain valid.
Name omitted records and the comparisons readers must withhold. It is a
blocker if it removes the only support for a system-level value or materially
changes the account. Neither a predecessor objection nor budget exhaustion
settles materiality. Faithful uncertainty is neither blocker nor limit.

A profile-value limit is admissible only when the affected axis or unit itself
expresses `partial`, `not-determinable` or `uninspected`; a synthesis caveat
does not travel with an extracted value. Write no replacement profile, record
or new quotation. Source reads may only resolve named ambiguities at cited
paths of the frozen revision; log each under Verification. New source facts
cannot replace supporting records. Do not execute or install the target.

## Check and return

Run the shared content check and repair findings. Structural acceptance does
not establish support. Code applies a valid verdict to the exact handed
profile; malformed verdicts refuse only the verifier candidate. No automatic
scope override is granted. Missing inputs or an unauthorized scope decision
require `problem` and stop. Do not delegate or publish. Return one line naming
both output files.
