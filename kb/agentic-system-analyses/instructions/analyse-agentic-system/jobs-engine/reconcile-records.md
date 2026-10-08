---
description: "Use with the opt-in engine reconciliation hand-out to connect pinned analyst records without judging or rewriting their findings"
type: types/instruction.md
---

# Reconcile the pinned analyst records

State how the three reports connect and where they disagree so the record verifier can judge them as one bounded account.

Read this instruction first, then complete the invocation's Input reading
batches, recovering truncated reads. Follow `worker-rules`, `collection`,
`sources-contract`, `records-contract` and the supplied report contracts.
The coordinator owns scheduling, acceptance and recovery. This instruction
serves only the opt-in engine's reconciliation job, not the live legacy workflow.

## Inputs, authority and result

`boundary` fixes the frozen source and Source register. `runtime`, `memory`
and `epistemic` are the pinned reports to connect. `opening` is JSON metadata
including the prepared `command-path`. Use the supplied `system` and `run-id`.
Write the whole member to `output` under `reconciliation-contract`, repeating
`boundary`'s `reviewed-boundary`. Write only `output`, `problem` and intermediate
files under `scratch`; all inputs and previous outputs are read-only. Do not
edit reports, engine state or the working set, publish, stage, commit, delegate
or launch a worker. Inspect source text, never execute or install the target.

`refusal = absent` means no refusal input. When supplied, repair the named
Findings and the blockers addressed to reconciliation. Use
`previous-reconciliation`, when supplied, as the prior completed output by
identity, not as a mutable member path. Reconcile the supplied reports again;
do not copy an old connection after its evidence changes. If optional
`runtime-answers`, `memory-answers` or `epistemic-answers` are supplied, assess
what their corrections or declines mean for cross-report disagreements.
There are no round numbers, request files, change files or run-state paths to
reconstruct. Do not discover other workers' outputs.

## Connect without judging

Follow `reconciliation-contract` for exact sections and fields. State every
identity between records as a supersession or rule it out. An unresolved
disagreement is an `Unresolved conflict:` paragraph naming the full IDs, both
findings, each finding's evidence and the conclusion it prevents. Faithful
uncertainty alone is not a disagreement. A report relying on another report's
record disagrees when that record no longer says what the dependent finding
requires. Describe a declined objection concerning two reports with both
positions, not as an automatically established defect.

Do not select the strongest-sounding status, replace a record's value,
strengthen or narrow a report's finding, allocate IDs or declare parts.
`Amendment:` is only for supersession backed by identity evidence. Both IDs
remain declared in their original reports. Containment alone does not justify
supersession. For a missing required part, retain a conflict naming the
combined ID, missing part in prose, evidence and prevented conclusion.
Resolve references against the supplied Source register and analyst reports.
Claim support is the verifier's question; only the declaring analyst changes
its report.

## Check and return

Run the shared draft-at-slot content check with the supplied validation paths.
Repair findings and rerun. A pass checks form and quotation occurrence, not
semantic support or acceptance. Code separately checks the frozen source,
method and invocation identity. An unavailable required input, necessary
boundary change or unauthorized consequential scope decision requires
`problem`; bounded uncertainty belongs beside its affected conclusion.
Return one line naming the file written.
