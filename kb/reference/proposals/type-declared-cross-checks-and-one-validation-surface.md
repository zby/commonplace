---
description: "Proposal: validate one draft of a directory artifact at its intended member path, in its set's context, in two stages: first the whole-set check filtered to the draft's role, then role-scoped context reading with explicit failure on unusable context."
type: reference/types/design-proposal.md
tags: [type-system, kb-maintenance]
---

# Document validation in working-set context

The directory-type mechanism from ADR 095 validates a set as a whole, and
the declared layout of
[ADR 111](../adr/111-directory-types-declare-their-layout.md), adopted from
the proposal "Directory types declare their layout", lets it validate an
incomplete working instance with findings attributed to roles. This proposal adds a member mode: one candidate file is validated at
its intended member path, against the siblings its role relates to, whether
or not the set is complete. The document is the target; available members
supply context. Reading a member to resolve a reference does not make that
member another target. Workflows continue to own scheduling, authority and
progress-dependent acceptance.

The proposal is staged, and each stage is adoptable on its own. Stage one
exposes what the layout mechanism already computes: the whole-set check with
a draft's bytes at its slot, filtered to the draft's role. Stage two changes
what is read and how context defects are reported. Stage one is what
[adopting the declared layout in the analysis workflow](./adopt-declared-layout-in-the-analysis-workflow.md)
needs to retire the separate analyst check command; that plan decides stage
one and records the measurements that would warrant stage two. The operator
selected this direction on 2026-10-06. Neither stage is shipped behavior.

## Current state (as of 2026-10-06)

- [ADR 095](../adr/095-directory-artifacts-add-shared-set-validation.md)
  recognizes a directory artifact by `ARTIFACT.yaml`. Set checks run when the
  directory itself is validated. Explicit file validation checks that file
  alone and never reads a manifest.
- The layout proposal shipped on 2026-10-06 (commit 3c5da8c85). A directory
  type declares roles with paths, types, identity sources and cited roles;
  validation of a working instance reports absent members and relation
  findings per role.
- The analysis workflow writes `output/ARTIFACT.yaml`, naming only the type,
  at run opening, so the working set is recognized from its first member.
  Its acceptance helper, `set_findings` in
  `src/commonplace/lib/agentic_workflow.py`, validates `output/` through
  `ValidationRun` with the candidate's bytes placed at its slot by content
  overrides and filters the findings to the candidate's role. The private
  sibling-body assembly and the memory-profile path heuristic are gone
  (commit 7dcf8076f). That helper is stage one, reachable only from workflow
  code.
- The set type checks every member's quotations against the boundary's
  frozen source (commit 86ae3c8e1), so quotation anchoring is a set relation,
  not a workflow-only check.
- Under [ADR 105](../adr/105-let-analysts-run-their-acceptance-check-before-submission.md),
  analysts self-check through `commonplace-analysis-check`, which loads the
  run's workflow definition to reach the job's validator. The job, not the
  type, supplies the context. `commonplace-validate` cannot take a draft at
  an intended member path.

## Problem

A document can conform locally while citing an unavailable or ambiguous record
or carrying an identity inconsistent with its set. Checking only the file
misses those relationships. Checking the whole unfinished set reports defects
the author neither caused nor has authority to repair.

The validator cannot express the middle case from the command line. The
mechanism exists inside the workflow, so a workflow that builds a directory
artifact incrementally is the only place a draft can be checked in context,
and standalone validation of a working member stays file-only.

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

Stage one meets this boundary by filtering: it reads the whole working set
and reports only the findings attributed to the candidate's role. Stage two
meets it by construction: it reads only the context the role names.

## Stage one: a draft at its intended path

`commonplace-validate` takes a draft and the member path it is intended
for. The validator finds `ARTIFACT.yaml` in that path's directory, places
the draft's bytes at the path through content overrides, validates the
directory, and reports the findings attributed to the path's role, with
absent-member findings dropped. Membership stays positional: the filename
gives the role. An unmatched filename or an unavailable directory type
fails; there is no fallback to file-only validation. Nothing is written.

Repair advice attaches to findings, so the same text prints whether the
validator or a workflow's acceptance reports the finding.

What stage one does not give: it reads every member present, so a sibling
that does not parse fails the invocation as a whole rather than the one
check that needed it; and it cannot distinguish a candidate finding from a
finding the set rule attributes to the candidate's role for another reason.
Both are acceptable for the analysis set, whose members are few and whose
rules attribute findings to the member that must repair them.

## Stage two: role-scoped context

The role's relations name which siblings to read: the role that supplies
identity fields, and the roles whose declarations may be cited. Only those
files are read, and only for those checks. A context file that is absent,
unparseable or ambiguous for a required check fails that check explicitly,
naming the candidate check and the blocking file. The layout's completeness
conditions are whole-set rules and do not apply. Only findings originating
in the candidate are reported; a pooled checker that reports per-body
failures is filtered to the target. Cross-member ambiguity, such as a cited
ID declared twice among the cited roles, is reported because it blocks the
candidate's own reference.

Stage two is warranted when a directory type has enough members that
reading them all per check is costly, when a sibling's parse failure blocks
drafts whose checks never needed it, or when a finding's attribution to a
role is not the same as its origin in the candidate. The adopt plan's
measurements record whether any of these occur in the analysis set.

## Operativity

Stage one's consumers are explicit validation of a draft by its author, and
workflow acceptance and self-check, which call the same path instead of a
workflow-private helper. Stage two's consumers are the same callers on a
directory type where the conditions above hold; none is known today. The
oracle for both is the actual declarations and identity facts in the located
siblings. Whole-set validation of an unfinished working artifact still fails
as a set when requested; that is correct, and it runs only at explicit
points such as round close and assembly.

### First instance: the analysis set

The analysis set has the working manifest, role-scoped relations and
role-attributed findings. Adopting stage one means its acceptance and
self-check call the validator with the job's output file at the member's
destination, and the separate check command retires. The adopt plan places
the synthesis and the verifications in the set first, so every job except
the boundary has a slot.

## Alternatives

- **Member-role declaration in frontmatter**, for example
  `type: analysis-set.md#memory`. Rejected. It states membership in a second
  place beside the manifest ADR 095 chose as the single recognition rule, and
  it changes what `type` means for every consumer: validation,
  type-conformance review, criteria resolution, documentation hooks and
  collection eligibility. With a layout, the role follows from the path and
  needs no declaration in the member.
- **Workflow-only context assembly.** Keep the helper private to the
  workflow and leave the separate check command. This is where the system
  is today. It does not serve the purpose: standalone validation stays
  file-only, the next directory type repeats the private implementation, and
  analysts keep a second command for the validator's own findings.
- **Caller-supplied context.** Tests and internal adapters may pass sibling
  bodies directly. Not the author-facing behavior; an explicit-context path
  must preserve the same target, replacement and checking semantics.
- **Stage two first.** Rejected: it builds role-scoped reading before any
  consumer has shown that whole-set reading with a filter is insufficient.

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
  such as a correction round's answers, are identified separately so a
  narrower content pass does not claim job acceptance.

## Free choices

The flag's name and shape, how repair text attaches to findings, and whether
whole-set rules and member-mode rules share one registration are
implementation choices. Start with existing Python checks; the
[type-selected Python validation proposal](./type-selected-python-validation-checks.md)
is not a prerequisite, and selecting a role does not authorize loading
repository Python code.

## Adoption criteria

Stage one is adopted when:

- `commonplace-validate` checks a draft at an intended member path with
  context found from that path's directory; an unmatched path or an
  unavailable directory type fails explicitly, and nothing is written.
- The findings reported are those attributed to the path's role, with
  absent-member findings dropped; findings for other roles are not reported.
- Replacement bytes are used consistently without changing accepted files.
- For the analysis set: acceptance and self-check give the same content
  findings as this invocation, with workflow checks identified separately,
  and no workflow-private helper assembles context.

Stage two is adopted when, in addition:

- Only the context the role's relations name is read for the candidate's
  checks, and a context file that is absent, unparseable or ambiguous for a
  required check fails that check by name without failing unrelated checks.
- The candidate's missing references and identity disagreements are
  reported; an unrelated broken outgoing reference in a context member is not.

Incoming-reference failures and whole-set incompleteness stay visible when
those operations are requested, not in this one. Test fixtures establish
checking behavior, not model adherence or the semantic truth of a report. No
live analysis run is prerequisite for either stage.
