---
description: "Proposal: validate working directory artifacts and candidate member replacements through the same content contract used by workflow acceptance and later maintenance."
type: reference/types/design-proposal.md
tags: [type-system, kb-maintenance]
---

# Working-set and candidate validation

This proposal asks whether authors, workflow acceptance and maintainers can
check the same artifact contract while a multi-document result is still being
built. A candidate member would be checked in its intended set without replacing
the accepted member. The workflow would continue to own scheduling, authority
and progress-dependent acceptance.

The question is about validation context and artifact boundaries, not a new
cross-check language. [Type-selected Python validation checks](./type-selected-python-validation-checks.md)
addresses how types could select executable checks. Existing registrations are
sufficient to explore this proposal.

## Current state (as of 2026-10-06)

- [ADR 095](../adr/095-directory-artifacts-add-shared-set-validation.md) supplies
  directory artifacts with schema-owned membership, ordinary member validation
  and imperative set checks. Hashes are optional in the generic mechanism;
  supplied hashes always bind. Directory artifacts need not be finished.
- The [analysis-set schema](../../agentic-system-analyses/types/agentic-system-analysis-set.schema.yaml)
  requires six pinned members for a complete outcome and only the overview for
  other outcomes. It does not represent the pre-synthesis record set.
- `src/commonplace/lib/agentic_workflow.py` checks the record set before synthesis
  through `record_check()`, composing member, identity and reference checks.
  Its job validators also supply the run context for candidate acceptance.
  Final set validation uses the ordinary directory path after manifest assembly.
- `ValidationRun.content_overrides` in `src/commonplace/lib/validation.py`
  already accepts replacement bytes for members and manifests. The directory
  loader discovers supplied candidate paths as well as actual files. This is
  library support, not a general candidate-replacement CLI contract.
- Under [ADR 105](../adr/105-let-analysts-run-their-acceptance-check-before-submission.md),
  `commonplace-analysis-check` obtains a candidate's checks from a named run and
  job. It remains distinct from `commonplace-validate`. Synthesis and verification
  outputs now have local types; untyped intermediate output is not a universal
  premise for this proposal.

## Problem

A report can conform locally while disagreeing with its set or referencing an
unavailable record. During authoring, the workflow constructs the context needed
to judge those relationships. After assembly, directory validation supplies a
related context. The code shares checks, but the working set's validity is not
fully represented by the finished directory contract.

The intended improvement is one content-validity model usable before and after
submission. One command name is neither necessary nor sufficient: forwarding a
job name through another command would leave context and ownership unchanged.

## Options

### A. Retain job-context checks over shared validation functions

Keep the workflow as the source of working-set context. Worker self-checks and
acceptance continue to call the same job validator; ordinary directory
validation remains the later maintenance surface. Consolidate common checks
where duplication is demonstrated without adding a working artifact type.

The job constructor supplies expected identity, relevant members and frozen
source to existing checks. Their oracle is the supplied artifact/evidence set;
job acceptance additionally applies workflow conditions. This may be adequate
when no other consumer needs to validate unfinished sets independently.

### B. Give working sets an explicit directory contract

Represent the set under construction with a type that permits its legitimate
incompleteness while checking members and their relationships. This could be a
separate working-set type or explicit states of one type. The finished contract
would still require full membership and exact-byte pins.

Authors and the workflow would validate the working artifact through the
ordinary directory pipeline. The type and set contents, rather than only job
construction, would identify the applicable content requirements. Expected
identity could come from a declared set fact or related artifact; the design
must not fabricate a provisional public overview merely to satisfy the current
finished-set checker.

The oracle is the declared membership, identity and reference scope. Permitting
a missing member does not warrant accepting an unresolved reference. A valid
working set establishes only the properties its state requires, not readiness
for publication or completion of scheduled work.

### C. Check a candidate as a replacement within its set

Expose the existing content-override capability through a supported consumer
interface. A caller supplies the candidate and its intended member slot;
validation evaluates that hypothetical set without mutating accepted files.
This can complement option B or check replacements in an already complete set.

The validator consumes the candidate view through its shared read context.
All checks must observe that view, including referential checks; reopening
accepted files independently would test different bytes. Findings describe
the candidate set, not the on-disk incumbent.

Supplied hashes continue to bind. A changed member paired with an old digest
fails. A working contract may permit omitted pins, while a frozen candidate
needs a corresponding candidate manifest. Neither route silently disables
integrity checks. The interface must distinguish legitimate candidate metadata
from the incumbent evidence it is replacing.

## Forces and boundaries

### Validity is not permission or progress

A directory contract can state required results and relationships. It does not
schedule workers, allocate correction rounds, permit publication or determine
whether a particular worker may read another report. Candidate context must
preserve the workflow's authorized reference scope rather than treating every
file in a run directory as available evidence.

Invocation-specific expected values, correction obligations and other
progress-dependent checks remain workflow responsibilities unless a separately
justified artifact makes them checkable facts. No new progress record is
required simply to eliminate a job argument.

### Missing evidence is not success

Member and set checks can establish form, agreement and reference resolution.
Quote occurrence additionally needs the frozen source. Missing source access
must remain visible as unverified or failed under the caller's existing
acceptance policy, not disappear when the entry point changes. Deterministic
success establishes neither semantic support nor coverage of the source system.

### Preserve useful feedback

Workers need specific refusal reasons and repair information; maintainers need
stable diagnostic identities and evidence limits. A shared checking path must
not lose these or silently change warning/failure policy. Command naming and
presentation may remain different when the consumers need different views.

### Keep infrastructure proportional

The directory mechanism already supports optional members, conditional schemas,
optional hashes and candidate byte views. Establish what these can express
before expanding it. A general source registry, a declared run-progress artifact,
nested membership and non-Markdown members are outside this proposal unless a
concrete validation need makes one a separate decision.

## Candidate direction and free choices

Explore a working contract together with candidate replacement before choosing
a new public command or generalized extension mechanism. Keep option A if the
alternative adds metadata and state management without removing meaningful
context duplication or enabling another consumer.

Separate versus stateful types, the location of shared identity, how a candidate
view is supplied, and one command versus a thin workflow-specific wrapper remain
open. A broad weakening of the finished-set schema is not an acceptable shortcut.

Directory-level semantic review remains an open question, not part of this
adoption. It needs its own account of reviewer inputs and version identity;
deterministic working-set validation does not supply that account automatically.

## Adoption criteria

Adopt a working-set contract when a real authoring or maintenance consumer can
use it without reconstructing a workflow job, and it replaces rather than adds
a competing definition of content validity. Demonstrate permitted incompleteness,
forbidden membership, identity disagreement and unresolved references against
representative working and complete sets.

Adopt candidate replacement when the same candidate and context yield the same
content findings during self-check and acceptance, without modifying incumbent
bytes or bypassing hashes. Test candidate-aware referential reads as well as
local schema checks. Keep independent workflow-acceptance checks explicit.

Compare implementation and maintenance cost with the existing shared-function
route, and preserve diagnostic and repair detail. A passing fixture establishes
interface behavior, not model adherence. No live external-system analysis,
Python extension framework or generic invalidation engine is prerequisite.
