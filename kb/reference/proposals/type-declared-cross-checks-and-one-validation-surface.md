---
description: "Proposal: one directory-member type declaration selects a document's contract and discovers context for candidate-only validation, without requiring a complete set."
type: reference/types/design-proposal.md
tags: [type-system, kb-maintenance]
---

# Document validation in working-set context

This proposal describes candidate-document validation through a single declared
directory-member type. The declaration selects a member contract, which supplies
the underlying document type and contextual constraints. The directory type's
member layout resolves related files from the candidate's containing directory.
The operator's primary use is authoring feedback: check references originating
in the candidate, not every reference in the surrounding reports.

The document is the target; available members supply context. Reading a member
to resolve a reference does not make that member another target. The workflow
continues to own scheduling, authority and progress-dependent acceptance.

The operator selected this direction for the proposal. It is not shipped behavior
or an implementation commission. Exact declaration syntax remains open.

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

## Selected design direction

### One declaration selects the member contract

A document declares either a standalone document type or a member of a directory
type. In the member form, the directory's member contract selects the underlying
document type. The instance does not independently repeat that type in a second
field. This prevents disagreement between two declarations of its local contract.

Illustrative syntax, not a finalized format:

```yaml
type: agentic-system-analyses/types/analysis-set.md#memory
```

The named directory type would define the `memory` role, its underlying
memory-report type, its location and its contextual constraints. The validator
would resolve that role, apply the underlying document contract, then apply the
member's contextual constraints. An unknown role or an unavailable contract is
a validation failure, not grounds to fall back to local-only validation.

The member contract composes local document requirements with requirements arising
from membership. Different directory types can reuse one underlying document
contract without copying it. A standalone declaration requests only that
standalone contract; it does not establish directory-member conformance. A
consumer requiring member conformance must not accept a standalone declaration
as an equivalent substitute.

### Discover instances through the directory layout

The directory type supplies the member layout; the containing directory supplies
the actual files. The validator uses that layout to locate the context needed
for the candidate's checks. It does not scan arbitrary nearby Markdown files.
A manifest or recorded workflow progress is not a prerequisite for this member
check. Whole-directory validation may retain its own manifest requirements.

A scratch draft needs an intended member path: check these candidate bytes as
that member, and discover context relative to that destination rather than the
scratch directory. The caller supplies the destination, not a hand-built list
of sibling reports. Candidate bytes replace the incumbent at that slot for all
checks in the invocation.

If a referenced file or declaration is absent, malformed in a way that prevents
resolution, or ambiguous, the required check fails. The checker does not defer
the failure because a file may become ready later. Readiness has no hidden
workflow meaning here: the actual content either supports the required check
or does not. A member not needed for any applicable candidate check need not
exist merely to make the directory complete.

Self-check, acceptance and standalone validation would consume the member-type
resolver. No such resolver is supplied by the current type contract; it must be
built. The oracle is the actual declarations and identity facts in the located
files, not the type reference itself. Successful checks establish bounded
conformance, not source support, publication integrity or execution history.

## Alternatives and trade-offs

- **Separate file-type and directory-membership fields.** This makes both
  declarations explicit, but repeats the underlying document type when the
  member contract already selects it. The selected design derives that type
  from one member declaration instead.
- **Caller-supplied context.** This can support tests and internal adapters, but
  is not the selected author-facing behavior. Discovery lets a maintainer check
  a member without reconstructing the producing job. An internal explicit-context
  path must preserve the same target, replacement and checking semantics.
- **Workflow-only context assembly.** This is a smaller local repair but leaves
  standalone validation without the declared relationship it needs. A workflow
  adapter may still supply the intended destination and enforce evidence access;
  it must not be the sole owner of the content-context relationship.

One command name is not the goal. Existing commands may remain if the same target
and resolved context receive the same content judgments.

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
addresses affected-target selection. That mechanism is not prerequisite for
target-scoped checking. A separate working-set type is needed only if the working
members require a distinct contract; incompleteness alone does not require one.
Member validation does not apply whole-directory completeness requirements.

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

The single member-type declaration and directory-layout discovery are the
selected proposal direction. Exact reference syntax, the representation of
member contracts and layout, the consumer interface, and use of existing content
overrides remain implementation choices. The illustration above does not
establish fragment syntax as a shipped type-reference format.

Start with existing Python checks; the separate
[type-selected Python validation proposal](./type-selected-python-validation-checks.md)
is not a prerequisite. Selecting a member contract does not authorize loading
repository Python code. No constraint language, general source registry or
progress-state artifact is required here.

Directory-level semantic review and unfinished-set conformance remain separate
questions. Neither should expand a candidate check merely because it reads
several files.

## Adoption criteria

A candidate interface must demonstrate that:

- One member declaration resolves both the underlying document contract and
  applicable contextual constraints, without an independent duplicate type field.
- Unknown members and unavailable contracts fail explicitly.
- Context files are discovered from the directory type's member layout at the
  intended destination, including for a scratch draft.
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
Implementation must update type-reference consumers and their contracts together;
passing one command while other consumers misread member declarations is not
completion. Test fixtures establish checking behavior, not model adherence or
the semantic truth of a report. No live analysis run is prerequisite.
