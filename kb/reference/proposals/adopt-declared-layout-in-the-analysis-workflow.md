---
description: "Proposal: move analyst acceptance, round-close checks, self-check and publication in the analysis workflow onto the declared set layout, and measure two runs before deciding on member mode."
type: reference/types/design-proposal.md
tags: [type-system]
---

# Adopt the declared layout in the analysis workflow

[Directory types declare their layout](./directory-types-declare-their-layout.md)
gives a directory type a declared layout and lets whole-set validation of an
incomplete instance report findings per role. That proposal defines the
mechanism and settles the analysis set's layout. It does not bind the
analysis workflow to use the mechanism: an implementer could land the layout
while analyst acceptance keeps assembling sibling bodies privately. This
proposal is the workflow side. It states which workflow code moves onto the
layout, in what order, what stays workflow-only, and what two runs must show
before the companion
[document validation in working-set context](./type-declared-cross-checks-and-one-validation-surface.md)
is implemented, narrowed or withdrawn.

The operator selected this direction on 2026-10-06. It is not shipped
behavior.

## Current state (as of 2026-10-06)

- Run opening in `src/commonplace/lib/agentic_workflow.py` runs the boundary
  job, which writes `boundary.md` at the run root, reads its disposition, and
  only then creates `output/`. A withheld run closes with an overview-only
  `output/` and a manifest; a complete run creates an empty `output/` and
  starts the analysts. No manifest exists until final assembly.
- Analyst acceptance is `pass_refusals`: ordinary file validation of the
  report, then record-reference resolution over bodies assembled by
  `set_bodies` from the boundary and the cited reports with the candidate
  under its own member name, then identity against run state and the
  boundary, declaration-prefix ownership, and quotation anchoring against the
  frozen source. The reference step reports every body's failures, so a
  sibling's dangling reference fails the candidate.
- The profile job's acceptance, `profile_refusals`, repeats the identity
  checks against the boundary and run parameters and runs the same pooled
  reference check with the profile added. The synthesis job's acceptance
  runs it with the synthesis added.
- At round close, `record_check` validates each record member, checks its
  identity against the boundary, and runs the pooled reference check over the
  current record set, writing the result to a round file that the verifier
  reads.
- The memory-profile type rule in `src/commonplace/lib/validation.py` reaches
  the canonical record members and the boundary by a path convention under
  `kb/agentic-system-analyses/state/`.
- Under [ADR 105](../adr/105-let-analysts-run-their-acceptance-check-before-submission.md),
  `commonplace-analysis-check` obtains the job's validator through the same
  constructors, so self-check and acceptance already share one code path.
- Final assembly writes the overview, builds the manifest from a member-name
  list, validates the directory and records the manifest digest in run
  state. Publication copies the manifest and every member document of the
  checked set into `retained/<system>/`.
- One retained set exists, dynamic-cheatsheet, produced on 2026-10-04.

## Problem

The analysis workflow carries its own statement of what the set is and how
its members relate, in four acceptance functions and one type rule. Landing
the layout without moving the workflow onto it leaves that statement in
place beside the declared one, and the first runs after implementation would
exercise only whole-set validation at the end, which already works. The
operator's question, whether directory validation with a role filter is
enough for authoring feedback or whether member mode is needed, would go
unanswered.

## Design

### Order of work

1. **Setup writes the artifact first.** Run opening creates `output/` and
   writes the type-only manifest before the boundary job. The boundary job's
   destination becomes `output/boundary.md`. The withheld path is unchanged
   except that `output/` already exists.
2. **One set-finding function.** A coordinator helper validates `output/` as
   a directory artifact through `ValidationRun`, optionally with one
   candidate's bytes placed at its slot through content overrides, and
   returns the findings attributed to one role. This is the only place the
   workflow asks about set relations.
3. **Acceptance functions call it.** `pass_refusals`, `profile_refusals`
   and the synthesis validator drop their `set_bodies` and identity code and
   take set findings from the helper, filtered to the candidate's role.
   `record_check` calls it without a candidate and keeps every role's
   findings, since it is the whole-set check for the round. Missing-member
   findings are expected mid-run and are excluded by the helper's caller.
4. **Workflow-only checks stay and are labelled.** Declaration-prefix
   ownership, quotation anchoring against the frozen source, the profile's
   comparison version, and agreement with run state and run parameters are
   not set relations. They remain in the acceptance functions, and their
   refusal rules are distinguishable from type findings in the messages the
   analyst sees.
5. **The memory-profile type rule loses its path heuristic.** Its
   cross-member checks are now role relations in the layout; what remains is
   the profile's own content rules.
6. **Assembly and publication read the layout.** The manifest builder lists
   the roles present. Publication copies every member of the checked set, so
   the boundary follows once the set model enumerates members from the layout
   rather than from its name constants.
7. **Regenerate the retained set.** A fresh dynamic-cheatsheet run on the
   production configuration replaces the retained set, which has no boundary
   and cannot acquire one.

Steps 1 and 6 depend on the layout being implemented; steps 2 to 5 can be
written against the layout's validation interface as soon as it exists.
Step 7 is the first test run.

### What this changes for analysts

The refusal an analyst sees for a set relation is the type's finding for
their role: a dangling reference in their own report, an identity field that
disagrees with the boundary, a duplicate declaration they share. A sibling's
unresolved reference no longer appears. Workflow refusals keep their current
form. The self-check command changes nothing on the analyst's side.

### The two runs

The regeneration run on the production configuration and one further run on
the test configuration, on a different system, are the evidence for the
companion proposal's decision. Compare each run only with runs on the same
configuration. Record, per run and per analyst job:

- the number of set findings delivered, and how many concerned a member
  other than the analyst's own, which should be zero;
- any check the workflow needed that the helper could not express as
  directory validation plus a role filter;
- whether the type-only manifest, the partial-instance validation and the
  boundary inside `output/` passed replay, assembly, publication and the
  retained-set validation without a special case;
- whether a self-check and the subsequent acceptance ever disagreed on a set
  finding for the same bytes.

The outcome routes the companion proposal. If the first count is zero and
the second list is empty, directory validation with a filter is sufficient
for authoring feedback, and the companion is narrowed to checking a file
outside any job or withdrawn with this evidence named. If the second list is
non-empty, its entries are the companion's warrant.

## Alternatives

- **Land the layout and leave the workflow as it is.** Rejected: two
  statements of the set coexist, the layout's partial-instance validation
  has no consumer, and the runs answer nothing about member mode.
- **Implement member mode first, then adopt both at once.** Rejected: it
  stacks two unexercised mechanisms, and the workflow would be rewritten
  twice if member mode proves unnecessary.
- **Filter in the acceptance functions rather than in one helper.**
  Rejected: four copies of the same filter is the drift the layout removes.

## Forces

- **Expected incompleteness.** Mid-run directory validation reports absent
  required members. The helper's callers must drop those findings
  deliberately, not suppress failures in general, or a genuinely missing
  cited member would pass.
- **Candidate bytes at the slot.** The candidate lives in a job workspace and
  is accepted into `output/` only after validation. The helper must place the
  candidate at its slot through content overrides so the set sees one version
  of that member, and must not write to `output/`.
- **Verifier input.** The round-close record check writes a file the
  verifier job reads. Its format and the rules it names should survive the
  change so the verifier's instruction does not need rewriting.
- **Replay.** Writing the manifest at setup is a new effect in an already
  replayable sequence. It must be idempotent on bytes, as the existing
  coordinator writes are.
- **Published site.** Retained sets gain a boundary page. ADR 102 keeps the
  overview as the stable public entry; the boundary is a member, not an
  entry.
- **Isolated analysis worktrees** have their own command environment. The
  adoption must land in the installed tool before a run on it counts as
  evidence.

## Free choices

The helper's signature, how roles are named in refusal messages, whether the
round-file format changes, and whether the regeneration run and the test run
proceed in parallel.

## Adoption criteria

- `output/` holds a type-only manifest and the boundary before any analyst
  job runs, and a replay of a completed run writes nothing new.
- No acceptance function or type rule assembles sibling bodies or locates
  members by path convention; `set_bodies` and the memory-profile heuristic
  are gone.
- An analyst's acceptance and self-check deliver set findings for their role
  only, and workflow refusals are distinguishable from them.
- The round-close record check is a directory validation of the working
  instance, and the verifier job still receives what it reads today.
- The regenerated retained set contains the boundary and validates; the
  published entry is unchanged.
- The two runs are recorded with the measurements above, and the companion
  proposal's current state is refreshed to cite them.
