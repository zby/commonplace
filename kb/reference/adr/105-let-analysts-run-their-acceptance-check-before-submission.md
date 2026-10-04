---
description: Analysts call the same read-only validator as acceptance, repair its findings locally, and quote frozen sources with path-only attributions
type: reference/types/adr.md
status: accepted
---

# 105 — Let analysts run their acceptance check before submission

**Status:** accepted
**Date:** 2026-10-04
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

Expose each analysis job's acceptance validator through
`commonplace-analysis-check`. Both callers use the same job constructors,
checking functions and refusal messages. Obtain the validator without replaying
the workflow. The command changes no draft, run state or attempt count; its
only write is a measurement line in the job's scratch log.

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

**Integrate immediately with `commonplace-validate`.** Desirable as a later
command unification, but combining it with this change would enlarge the task.
Checks remain functions of output and supplied context so integration does not
require changing their judgments. The separate command's name, text output,
exit statuses and JSONL scratch log are implementation choices.

## Consequences

Analysts receive the command and quotation form through shared worker rules,
job instructions and the source contract, loaded as declared dependencies.
Job constructors supply their validators to both the command and the engine.
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
and semantic success, or readers needing omitted ranges. Count check runs and
refusals by rule from scratch logs, acceptance refusals from engine records,
quotations written from accepted members, and missing or ambiguous passages
per check. Reconsider draft completion or numbered source views when those
observations warrant them.

**TODO: integrate run-context checks with `commonplace-validate`.** Keep the
checks callable outside the engine, with output and supplied run context as
inputs. The later direction is one validation command for analysts, acceptance
and maintainers. It does not move mechanical acceptance into an independent
verification job, and it changes nothing about that job in this decision.
