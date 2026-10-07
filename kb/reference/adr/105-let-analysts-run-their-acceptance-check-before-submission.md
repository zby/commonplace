---
description: Analysts validate drafts at their declared member slots, acceptance adds labelled invocation residue, and quotations use frozen-source path-only attributions
type: reference/types/adr.md
status: accepted
---

# 105 — Let analysts run their acceptance check before submission

**Status:** accepted
**Date:** 2026-10-04
**Amended 2026-10-06:** One validation command checks drafts at declared member
slots. Acceptance adds labelled invocation residue; a content pass is not job
acceptance. The quotation decision remains in force.
**Amends:** [ADR 094](./094-quotations-require-a-unique-occurrence-or-a-containing-range.md) for citation construction and authoring-time checking. Its normalization and uniqueness rules remain in force.

## Context

A local type check cannot establish a working member's identity against its
run, resolve references against the members already supplied, or check quoted
text against the frozen source. Finding these mechanical defects after
submission consumes a worker retry and reloads the context needed for repair.
Copying selected source text into a helper input and then copying its generated
citation into a report also exposes the same quotation to two editing steps.

Analysts need the complete mechanical check while they still own the draft.
They also need refusal messages that identify the rule, location and repair.
Code can determine an expected identity or a quotation's occurrence. It cannot
determine which occurrence supports a finding or whether the analysis is sound.

## Decision

Expose the shared set-member judgment through `commonplace-validate`, with
a positional draft, `--set <directory>` and `--member <slot>`. Membership is
closed and positional. Replace the incumbent's bytes in memory for every
check and report findings for the candidate's role. Deliberately drop absent
members in a working instance; do not suppress failures generally. Validation
writes nothing, including no scratch log, and never loads the workflow.

Acceptance uses those same findings and repair text, plus labelled
**invocation residue**: checks against the frozen checkout and run parameters,
correction requests, predecessor reports and answers, current comparison
version and run identity, and blockers after a failed round check. A content
pass never claims job acceptance. Retire the separate check command, not a
wrapper under its old name.

Report independent failures together. Stop a dependent check when its required
input cannot be parsed or resolved. Give every refusal a rule, output location
and repair instruction. State the expected value where it is determined, and
show bounded occurrence candidates for ambiguous quotations. The analyst writes
the repair and checks again. Code never repairs the output.

Accept a blockquote ending in a source path alone. Resolve Git paths at the
run's frozen commit and captures at the registered, checksum-verified path.
A supplied revision or checksum must still agree with the run. Keep existing
completed citations valid. Every accepted quotation must occur exactly once
under whitespace-only normalization, either in the file or in a containing
range. A missing passage fails without a suggested replacement and requires
rereading the source and reconsidering the supported claim.

For ambiguity, offer an attribution only when its range isolates the unchanged
passage. Otherwise show source context and request a longer passage. More than
ten occurrences receive no candidate list. Analysts choose by context; they
never calculate ranges. Remove quotation generation commands and their worker
instructions. Published quotations need no range unless ambiguity requires it,
and need no repeated revision. The member and run retain the source identity.
Quoted spacing stays as the analyst wrote it, subject to the existing matcher.

## Considered alternatives

**Keep generation and add a check.** Closes the acceptance gap but keeps selection
files, batch escaping and the second copy of quotation text. No other live
consumer requires that command.

**Complete citations inside drafts.** Avoids the second copy and preserves
source-derived presentation, but requires output mutation and more rules for
partial completion. The operator chose analyst-owned repair instead.

**Designate passages by position.** Avoids retyping but a wrong position can
return genuine, unintended evidence. It also needs trusted source numbering.
Text remains the anchor for now.

**Repair values or escalate repeated errors around the run loop.** Adds recovery
machinery where fuller messages and a local check let the analyst act directly.
Retry and repair limits remain unchanged.

**Keep a separate acceptance-check wrapper.** Rejected in the amendment:
loading workflow code and a job identity to validate member content keeps a
second judgment surface. Invocation-dependent checks remain in acceptance,
labelled separately, rather than becoming a validation command.

## Consequences

Analysts receive the command and quotation form through shared worker rules,
job instructions and the source contract, loaded as declared dependencies.
The CLI and job constructors consume one shared draft-at-slot validation API;
the engine additionally consumes invocation residue.
The shared citation parser supplies source identities to structural validation,
frozen-source checks and publication. Source quotations and fenced examples
stay outside record and ordinary-link scans. Maintainers find the command
through its installed entry point and command reference.

Local repair avoids spending a submission attempt on defects the check already
knows how to detect. Independent verification jobs retain their semantic role.
A pass attests to form and occurrence, not claim support or analytical quality.
Readers lose automatic source spacing and usually lose line ranges. The
checker does not choose evidence, and preflight results apply to the supplied
context and draft bytes at that time.

Fixtures establish parity, non-mutation and quotation behavior. They do not
establish that analysts use the tool or submit fewer refused outputs. Existing
frozen sets remain unchanged. This decision applies to analysis jobs with
registered run context, not to general KB citations lacking that context.

**TODO: revisit the analyst acceptance check and path-only quotation** after
the first few separately commissioned analyses, or earlier on repeated local
failures, avoidable acceptance refusals, quotations not found near the old batch
failure rate, hand-written ranges or revisions, confusion between mechanical
and semantic success, or readers needing omitted ranges. Record set findings
delivered per run and job, findings concerning another
member (expected zero), invocation-residue refusals by rule, and disagreements
between self-check and acceptance for identical bytes. Validation does not
write these measurements; the workflow retains them with acceptance evidence.
Count quotations from accepted members and missing or ambiguous passages
in retained findings. Reconsider draft completion or numbered source views
when those observations warrant them.

Draft-at-slot validation and acceptance must agree on every shared finding
for identical bytes, asserted by integration tests. This does not move
mechanical acceptance into an independent verification job or establish that
analysts use the check.
