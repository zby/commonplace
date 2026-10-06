---
description: "Proposal: validate one member of a directory artifact in its set's context, resolving its role and relations from the directory type's layout, with a manifest present from the first write and no requirement that the set be complete."
type: reference/types/design-proposal.md
tags: [type-system, kb-maintenance]
---

# Document validation in working-set context

The directory-type mechanism from ADR 095 validates a set as a whole. This
proposal adds a member mode: one candidate file is validated against the
siblings its role relates to, through the same external definition, whether
or not the set is complete. The document is the target; available members
supply context. Reading a member to resolve a reference does not make that
member another target. Workflows continue to own scheduling, authority and
progress-dependent acceptance.

This proposal depends on
[directory types declare their layout](./directory-types-declare-their-layout.md).
Member mode needs a role lookup by path, per-role relations, a working
manifest from the first write and role-attributed findings, and the layout
proposal supplies all four. Nothing here is buildable before it. The layout
proposal's partial-instance validation already lets a workflow validate the
working directory and filter findings by role; this proposal adds what a
filter cannot give: reading only the context a role needs, checking scratch
bytes at an intended destination, and failing explicitly when context is
unusable instead of reporting the context's own defects.

The operator selected this direction. It is not shipped behavior or an
implementation commission.

## Current state (as of 2026-10-06)

- [ADR 095](../adr/095-directory-artifacts-add-shared-set-validation.md)
  recognizes a directory artifact by `ARTIFACT.yaml`. Set checks run only
  when the directory itself is validated. Explicit file validation checks that
  file alone and never reads a manifest.
- The analysis workflow writes `output/ARTIFACT.yaml` only at final assembly
  and at the blocked-outcome close, through `build_manifest` in
  `src/commonplace/lib/agentic_finalize.py`. During analysis the output
  directory has no manifest, so no validator path can see the working set.
- Member-in-context checks therefore live in workflow code. Analyst acceptance
  in `src/commonplace/lib/agentic_workflow.py` assembles sibling bodies
  privately and runs the shared record checker over them. That checker, in
  `src/commonplace/lib/agentic_records.py`, pools declarations and reports
  every body's unresolved references, so a sibling's dangling reference fails
  the candidate. The memory-profile type rule in
  `src/commonplace/lib/validation.py` reaches siblings through a hardcoded
  path convention with `boundary.md` as the overview stand-in.
- `ValidationRun.content_overrides` supplies replacement bytes at intended
  paths, and member discovery already includes supplied paths beside a
  directory.
- Under [ADR 105](../adr/105-let-analysts-run-their-acceptance-check-before-submission.md),
  analysts self-check through the job's acceptance validator. The job, not
  the type, supplies the context.

## Problem

A document can conform locally while citing an unavailable or ambiguous record
or carrying an identity inconsistent with its set. Checking only the file
misses those relationships. Checking the whole unfinished set reports defects
the author neither caused nor has authority to repair.

The type mechanism cannot express the middle case. It knows whole-set rules
but has no notion of one member checked against the others, and it cannot see
a set before the set is declared finished. Every workflow that builds a
directory artifact incrementally reimplements member-context checking
privately, and standalone validation of a working member stays file-only.

## Checking boundary

For the candidate: its local contract, its identity against the roles the
layout names, and the references originating in its own text or structured
fields, resolved against its own declarations and the roles it may cite.

For context members: read what the candidate's checks need. Do not run their
full member checks or report their unrelated outgoing-reference failures. A
context file that is absent, unparseable or ambiguous for a required check
fails that check explicitly, naming the candidate check and the blocking file.
Context is not trusted merely because it is not a target; a conflicting
declaration of a cited ID is a finding against the candidate's reference.

## Selected direction: member mode over the declared layout

### Finding the artifact

Membership stays positional. The validator finds the nearest `ARTIFACT.yaml`
at or above the candidate's directory, within the bound the layout proposal
sets for nesting, and takes the candidate's path relative to that root. With
no manifest in reach, the file receives file-only validation, and a consumer
requiring member conformance treats that as failure. No frontmatter field or
type-reference syntax is added; `type:` keeps meaning a type-spec document.

### Resolving the role and its context

The relative path matches a layout entry, which gives the role. An unmatched
path or an unavailable directory type fails; there is no fallback to file-only
validation. The role's relations name which siblings to read: the role that
supplies identity fields, and the roles whose declarations may be cited. Only
those files are read, and only for those checks. The layout's completeness
conditions are whole-set rules and do not apply in member mode.

### Reporting

Only findings originating in the candidate are reported. A pooled checker
that reports per-body failures today is filtered to the target in member
mode. Cross-member ambiguity, such as a cited ID declared twice among the
cited roles, is reported because it blocks the candidate's own reference.

### Scratch drafts

A scratch draft supplies its intended member path. Its bytes replace the
incumbent at that slot for every check in the invocation, and the artifact
and context are found from that destination. The caller supplies the
destination, not a list of sibling files.

### Operativity

Consumers would be explicit file validation of a member inside an artifact,
workflow acceptance and ADR 105 self-check, which would call member mode
instead of assembling context privately, and any future directory type. No
member mode exists; it must be built on the layout reader. The oracle is the
actual declarations and identity facts in the located siblings. Whole-set
validation of an unfinished working artifact fails as a set, which is correct;
it runs only at explicit points.

### First instance: the analysis set

Once the layout proposal lands for the analysis set, the working manifest,
the role-scoped relation checks and the retirement of the memory-profile path
heuristic are already in place. Adopting member mode then means analyst
acceptance and ADR 105 self-check call member mode with the job's output file
as scratch bytes at the member's destination, instead of assembling sibling
bodies privately. Where the manifest sits, and whether `boundary.md` is a
member, follows the layout proposal's nesting choice.

## Alternatives

- **Member-role declaration in frontmatter**, for example
  `type: analysis-set.md#memory`. Rejected. It states membership in a second
  place beside the manifest ADR 095 chose as the single recognition rule, and
  it changes what `type` means for every consumer: validation,
  type-conformance review, criteria resolution, documentation hooks and
  collection eligibility. With a layout, the role follows from the path and
  needs no declaration in the member.
- **Workflow-only context assembly.** Fix the pooled checker to report only
  the target's failures and leave context assembly in the workflow. This is
  the smallest repair of the motivating defect and can land before either
  proposal. It does not serve the purpose: the type mechanism learns nothing,
  standalone validation stays file-only, and the next directory type repeats
  the private implementation.
- **Caller-supplied context.** Tests and internal adapters may pass sibling
  bodies directly. Not the author-facing behavior; an explicit-context path
  must preserve the same target, replacement and checking semantics.

## Distinct operations

| Operation | Target and purpose |
|---|---|
| Document validation in set context | Check the candidate and its outgoing references against the roles it relates to |
| Change-impact validation | Determine which other artifacts need checking after a replacement, including broken incoming references |
| Whole-set validation | Check collective consistency, membership and completion requirements at an integration or publication boundary |

Removing a declaration from a replacement may break references in other
members while the candidate's own references stay valid. That belongs to an
explicit impact or whole-set check.
[Generalized validation invalidation](./generalized-validation-invalidation-and-imperative-extension.md)
addresses affected-target selection and is not prerequisite here.

## Forces

- **Consistent bytes.** A context resolver must not count the incumbent and
  replacement as two declarations or reopen incumbent bytes while other checks
  see the candidate. Validation must not mutate accepted files.
- **Authorized scope.** Context preserves the workflow's evidence and
  reference scope. Unavailable future declarations do not resolve a reference.
- **Bounded attestation.** Member-mode conformance does not pin bytes in a
  manifest, certify publication, or establish semantic support or source
  coverage. Workflow conditions, correction budgets and publication authority
  remain separate from document validity.
- **Repair information.** Findings keep rule identity, the affected candidate
  location and the blocking context. A context defect may block the check
  without making its repair the candidate author's responsibility.
- **Two callers, one judgment.** Self-check and acceptance must give the same
  content findings for the same target and context. Workflow-only checks,
  such as quotation anchoring against a frozen source, are identified
  separately so a narrower content pass does not claim job acceptance.

## Free choices

The consumer interface, the use of existing content overrides, and whether
whole-set rules and member-mode rules share one registration are
implementation choices. Start with existing Python checks; the
[type-selected Python validation proposal](./type-selected-python-validation-checks.md)
is not a prerequisite, and selecting a role does not authorize loading
repository Python code.

## Adoption criteria

A candidate implementation must demonstrate, with the layout proposal adopted:

- Explicit file validation of a member inside an artifact resolves its role
  from the layout and applies the role's relations; unmatched paths and
  unavailable directory types fail explicitly.
- A scratch draft at an intended destination is checked with context found
  from that destination.
- The candidate's missing references and identity disagreements are reported;
  an unrelated broken outgoing reference in a context member is not.
- Valid references resolve against the current context when the set is
  incomplete.
- Replacement bytes are used consistently without changing accepted files.
- For the analysis set: acceptance and self-check give the same content
  findings as explicit file validation of the member, with workflow checks
  identified separately, and the private sibling-body assembly is gone.

Incoming-reference failures and whole-set incompleteness stay visible when
those operations are requested, not in this one. Test fixtures establish
checking behavior, not model adherence or the semantic truth of a report. No
live analysis run is prerequisite.
