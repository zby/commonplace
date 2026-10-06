---
description: "Proposal: validate a candidate document's references and other applicable constraints against the current working set without validating unrelated documents or requiring a complete set."
type: reference/types/design-proposal.md
tags: [type-system, kb-maintenance]
---

# Document validation in working-set context

This proposal asks how a candidate document can be checked against the current
working set without making the whole set a validation target. The operator's
primary use is authoring feedback: check references originating in the candidate,
not every reference in the surrounding reports.

The document is the target; available members supply context. Reading a member
to resolve a reference does not make that member another target. The workflow
continues to own scheduling, authority and progress-dependent acceptance.

## Current state (as of 2026-10-06)

- [ADR 095](../adr/095-directory-artifacts-add-shared-set-validation.md) supplies
  directory artifacts with schema-owned membership, ordinary member validation
  and imperative set checks. Explicit directory validation checks the set;
  explicit member validation does not automatically check its containing set.
- The [analysis-set schema](../../agentic-system-analyses/types/agentic-system-analysis-set.schema.yaml)
  describes completed output membership, not the pre-synthesis working context.
  Its complete outcome requires six pinned members.
- `src/commonplace/lib/agentic_workflow.py` supplies report bodies and expected
  identities to job acceptance functions. `reference_refusals()` uses the shared
  set-reference checker over supplied bodies; `record_check()` checks the record
  set before synthesis. These are not an independently exposed candidate-only
  reference-checking interface.
- `ValidationRun.content_overrides` in `src/commonplace/lib/validation.py`
  supports replacement bytes for intended paths. It provides a way to read
  candidate bytes consistently, but does not by itself define which documents
  are targets and which are context.
- Under [ADR 105](../adr/105-let-analysts-run-their-acceptance-check-before-submission.md),
  `commonplace-analysis-check` obtains checks from a named run and job. It remains
  distinct from `commonplace-validate`; the job supplies context that an isolated
  document cannot supply alone.

## Problem

A document can conform locally while citing an unavailable or ambiguous record,
or carrying an identity inconsistent with its intended set. Checking only the
file misses those relationships. Checking the entire unfinished set can instead
report unrelated defects the author neither caused nor has authority to repair.

The missing distinction is between the target of a judgment and the context
needed to make it. A useful authoring check must identify both without requiring
the surrounding set to be complete or globally valid.

## Proposed checking boundary

For the candidate, check its local contract, its applicable identity and other
cross-document constraints, and references originating in its text or structured
fields. Resolve those references against its own declarations and the available,
authorized working context.

For context documents, inspect what is needed to establish the candidate's
conformance. Do not automatically run their full member checks or report their
unrelated outgoing-reference failures.

For example, a memory report citing a runtime record needs that record to
resolve. An unrelated unresolved reference in the epistemic report is not a
finding against the memory report. If the cited ID has conflicting declarations,
however, the ambiguity prevents checking the candidate's reference and belongs
in its result. Context is not assumed trustworthy merely because it is not a
validation target.

A context read or parse failure that prevents a required check must be explicit,
not silently treated as absence or successful resolution. Diagnostics should
name the affected candidate check and the blocking context. The design need not
invent a recoverable fragment when the supplied document cannot be parsed.

## Options

### A. Supply explicit context to a document check

A caller supplies the candidate, its intended identity or member slot, and the
context needed for its checks. The validator evaluates the document through the
ordinary pipeline plus applicable cross-document checks, without promoting the
context documents to targets.

Worker self-checks, acceptance and maintenance tools would consume this
interface. A workflow may assemble the context under its existing authority;
the checker need not reconstruct a job merely to resolve references. The oracle
is the supplied declarations, identity facts and other evidence required by the
candidate's contract. It establishes bounded conformance, not global set health.

This is the proposed starting direction, not an adopted interface. Explicit
context needs an accountable completeness boundary: callers cannot claim
set-wide uniqueness after supplying only a subset of the relevant declarations.

### B. Discover context from the document's artifact relationships

The validator could use the intended location, containing manifest or declared
relationships to discover context. The document remains the only target;
discovery changes how inputs are obtained, not the scope of validation.

An author or maintainer would invoke the document check, and the resolver would
supply context to its cross-document checks. The oracle remains the actual
related artifacts, not the relationship label alone. This reduces caller
bookkeeping but needs clear behavior for missing manifests, incomplete sets and
ambiguous membership. Filesystem proximity is neither evidence authority nor
permission to read another worker's output.

### C. Retain a workflow-specific adapter

Keep the analysis command responsible for selecting the candidate and context,
while separating target-scoped checks from whole-set checks in the shared
library. The existing acceptance and self-check consumers would invoke that
adapter; a general public interface could wait for another consumer.

This can deliver the desired feedback boundary without new CLI or directory-type
machinery. Its limitation is that a maintainer outside a run still needs a way
to supply equivalent context. One command name is not the goal; matching content
judgments for the same target and context is.

## Distinct operations

| Operation | Target and purpose |
|---|---|
| Document validation in set context | Check the candidate and its outgoing references against available context |
| Change-impact validation | Determine which other artifacts need checking after a replacement, including broken incoming references |
| Whole-set validation | Check collective consistency, membership and completion requirements at an integration or publication boundary |

Removing a declaration from a replacement document may break references in
other reports while leaving the candidate's own outgoing references valid.
That belongs to an explicit impact or whole-set check. A candidate can still
have its own correction contract requiring stable IDs; enforcing that rule
against its predecessor does not require validating every consumer.

[Generalized validation invalidation](./generalized-validation-invalidation-and-imperative-extension.md)
addresses affected-target selection. Neither that mechanism nor a working-set
type is prerequisite for target-scoped checking. A separate working-set type
may become useful when a consumer needs to judge the unfinished set as a whole.

## Forces and boundaries

- Candidate bytes must be read consistently at their intended slot. A context
  resolver must not count the incumbent and replacement as two declarations or
  reopen incumbent bytes while other checks see the candidate. Validation must
  not mutate accepted files.
- The supplied context must preserve the workflow's authorized evidence and
  reference scope. Unavailable future declarations do not resolve a reference.
- Candidate conformance does not attest that a frozen manifest pins those new
  bytes. Integrity claims about supplied context still require their checks;
  checking a hypothetical document does not silently rewrite hashes or certify
  publication. Whole-set replacement and candidate-manifest validation remain
  separate possible operations.
- Missing source access remains visible when a candidate check needs it.
  Reference resolution and quote occurrence establish neither semantic support
  nor coverage of the source system.
- Workflow conditions, correction budgets and publication authority remain
  separate from document validity. A narrower content check must not silently
  remove a required integration check or claim full job acceptance.
- Findings retain useful rule identity, affected candidate location, context
  limits and repair information. A context defect may block the check without
  making its repair the candidate author's responsibility.

## Free choices

Explicit versus discovered context, the consumer interface, and use of existing
content overrides remain open. Start with existing Python checks; the separate
[type-selected Python validation proposal](./type-selected-python-validation-checks.md)
is not a prerequisite. No constraint language, general source registry or
progress-state artifact is required here.

Directory-level semantic review and unfinished-set conformance remain separate
questions. Neither should expand a candidate check merely because it reads
several files.

## Adoption criteria

A candidate interface must demonstrate that:

- The candidate's missing references and identity disagreements are reported.
- Valid references resolve against the current authorized context even when the
  surrounding set is incomplete.
- An unrelated broken outgoing reference in a context member does not fail the
  candidate check.
- Ambiguity or unavailable context that prevents a candidate check is reported
  rather than treated as success.
- Replacement bytes are used consistently without changing accepted files.
- The same target and context give the same content findings during self-check
  and acceptance, with additional workflow checks identified separately.

Incoming-reference failures and whole-set incompleteness should remain visible
when those operations are explicitly requested, not leak into this operation.
Compare the cost of a general interface with a workflow adapter before selecting
one. Test fixtures establish checking behavior, not model adherence or the
semantic truth of a report. No live analysis run is prerequisite.
