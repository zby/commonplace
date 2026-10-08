---
description: "Use with the record verifier hand-out to independently judge pinned records, reconciliation, structural findings and correction answers"
type: types/instruction.md
---

# Verify the pinned record set

Judge whether the reconciled records support a source-grounded bounded account, distinguishing material blockers from local limits.

Read this instruction first, then complete the invocation's Input reading
batches, recovering truncated reads. Follow `worker-rules`, `collection`,
`sources-contract`, `records-contract`, `boundary-contract` and the supplied
report and verification contracts. The coordinator owns
scheduling, judgment application and recovery.

## Inputs, authority and result

Judge exactly the supplied `boundary`, `runtime`, `memory`, `epistemic`,
`reconciliation` and `set-check`. `opening` is JSON metadata including the
prepared `command-path`. Use the supplied `system` and `run-id`. Write the
whole verification to `output` under `record-verification-contract`, with
`verifies: records` and `boundary`'s `reviewed-boundary`.

Write only `output`, `problem` and intermediate files under `scratch`. All
inputs, previous outputs and frozen sources are read-only. Do not correct
another author's text, change the boundary or working set, inspect other
attempts, alter engine state, publish, stage, commit, delegate or launch a
worker. Inspect source text; do not execute or install the target.

A subsequent attempt may supply `previous-verification` by identity and
optional `runtime-answers`, `memory-answers` and `epistemic-answers`. Read them
and judge the supplied records afresh. An answered blocker is not necessarily
settled. For `corrected`, check the changed finding and every passage depending
on it. For `declined`, judge the reason against frozen evidence; drop the
blocker or raise it again with why the reason fails. A previous verifier can
be wrong. Repair any supplied `refusal` of the verdict's own form.

## Judge coverage and materiality

Check every record, source anchor, evidence status, `Part of:` relation,
supersession and unresolved conflict. State the checks and dispositions in
Verification. Judge coverage against the frozen repository tree, not just
listed anchors. A shipped caller is not external merely because it calls an
API. Preserve supported findings; do not weaken them to produce uniform
coverage or avoid a content warning.

Apply the verification contract's materiality threshold. A blocker must
explain the incorrect reader inference and why a stated limit cannot contain
it. Unsupported claims, evidence strengths, absence or completeness claims
require correction. Local wording, coverage or classification issues can be
limits only while the remaining bounded conclusions hold. Faithfully scoped
uncertainty alone is neither a blocker nor a limit. Assess objections rather
than treating them as established defects.

Write each blocker as `- runtime: ...`, `- memory: ...`, `- epistemic: ...`
or `- reconciliation: ...`, naming full IDs, the defective passage, what is
wrong and its evidence. Indent continuation lines. A defect requiring two
reports to change is two separately addressed blockers. Address dependent
passages relying on a defective value to their own authors. Every structural
failure in `set-check` requires an explicit blocker addressed to its report;
if the finding cannot be routed within this job's authority, write `problem`
instead of silently dismissing it. A conflict missing IDs, both findings,
evidence or prevented conclusion is addressed to reconciliation. Conflicts
that the sources cannot settle become limits naming both positions and the
conclusions readers must withhold. Blockers and Limits are each exactly
`none` or a Markdown list under their required headings.

Write `problem` instead of a verdict when the whole record set cannot support
any bounded conclusion or evidence contradicts the frozen target or boundary
kind. Name paths, responsibilities and prevented conclusions. A local defect
within a supported boundary is not that case. Do not move an incorrect
classification into Limitations to accept it.

## Check and return

Run the shared draft-at-slot content check with the supplied validation paths,
repair findings and rerun. A pass establishes form and quotation occurrence,
not independent analytical correctness or acceptance. Code validates the
verdict and applies it to the exact versions this attempt was handed. A valid
verdict with blockers supplies refusals only to addressed authors; it does not
settle semantic gates for the other reports. A valid blocker-free verdict
settles the four record subjects against this verification, without automatic
operator overrides. Return one line naming the file written.
