---
description: "Proposal: register the synthesis and the three verifications as members of the analysis set, thin the overview to an entry page, check drafts in their role through commonplace-validate, and retire the separate analyst check command."
type: reference/types/design-proposal.md
tags: [type-system]
---

# Adopt the declared layout in the analysis workflow

Directory types declare their layout, and the analysis workflow's
acceptance, round-close and publication code moved onto the declared layout
on 2026-10-06. This proposal is the remainder of that adoption: the run's
products that still live outside the set, the overview sections that copy
other members, and the separate check command that analysts run because
`commonplace-validate` cannot check a draft in its role.

It is written as a mission for an implementer: the situation, the intent
and the end state, the boundaries that hold, and what is left to the
implementer's judgment. It does not prescribe the sequence of work. The
operator selected this direction on 2026-10-06. It is not shipped behavior.

Its validator side, draft validation in a role, shipped under
[ADR 113](../adr/113-artifact-runs-execute-declared-plans-with-pinned-judgments.md);
this plan had decided it in place of the measurement runs the earlier version
of this proposal gated it on.

## Current state (as of 2026-10-06)

- **Adopted:** run opening writes `output/` with a type-only manifest before
  the boundary job, and the boundary is the set's first member; one helper,
  `set_findings` in `src/commonplace/lib/agentic_workflow.py`, validates
  `output/` as a directory artifact with a candidate's bytes placed at its
  role through content overrides, and the analyst, reconciliation and profile
  acceptance functions take their set findings from it filtered to the
  candidate's role; the round-close record check is that validation of the
  whole working instance with absent and later roles dropped; the
  memory-profile path heuristic and the private sibling-body assembly are
  gone; the manifest builder and publication enumerate members from the
  layout. Under commits 7dcf8076f and 3c5da8c85; recorded here rather than
  proposed below.
- **Adopted:** each analyst report type declares its `record-prefix`, and
  validating a report checks its declarations against it (commit f186d3c4b).
- **Adopted:** quotations resolve through one pinned-source resolver,
  `src/commonplace/lib/quote_grounding.py`, for ingests and for the analysis
  set. The set type checks every member's quotations against the boundary's
  frozen source; pinned bytes absent from the machine leave them unverified,
  reported as information, and acceptance treats unverified as a refusal
  (commit 86ae3c8e1). The earlier version of this proposal listed quotation
  anchoring as workflow-only; that is no longer so.
- The synthesis and the three verifications are documents in the run
  directory, not members. Code copies the synthesis's two sections and each
  verification's account into the overview at assembly, and the set rule
  checks that the overview's boundary sections and source register are copies
  of the boundary's.
- Analyst acceptance in a correction round also reads the request packet,
  the analyst's `answers.md` and the previous report version. The packet and
  the change diffs are code-rendered from members; nothing else reads them.
- `commonplace-analysis-check` (ADR 105) loads the run's workflow definition
  to obtain the job's validator, prints its refusals with rule names and
  repair lines, and appends a count line to the job's scratch log.
  `commonplace-validate` checks a file alone or a directory as a set; it
  cannot take a draft at an intended member path.
- `kb/agentic-system-analyses/retained/` is empty. The only produced set,
  dynamic-cheatsheet of 2026-10-04, is archived because it has no boundary
  member and fails the current set type.

## Problem

Three statements of the run remain beside the layout. The judgments and the
public synthesis are outside the set, so their identity and record checks
stay in workflow code and the retained set carries them only as code
excerpts. The overview duplicates members under copy rules that exist
because those members once were not members. And analysts need a second
command for the same findings that validate computes, because validate has
no way to receive a draft in its role. Each is a place where the workflow
and the type can drift.

## Intent

One statement of what a run produces, and one validation surface for it.
Everything a run produces as a product or a judgment is a member of the set,
declared in the layout, pinned in the manifest and published as the author
wrote it. Everything a run produces as a working aid stays outside. A draft
is checked by the same validator, with the same findings and the same repair
text, whether its author runs the check or the workflow accepts it, and the
workflow's own acceptance adds only what depends on the job's invocation.

The purpose behind the intent: the workflow and the type cannot drift when
the type is the only statement, a retained set is complete evidence of the
run without the run directory, and an analyst needs one command they can
also use on any other KB file.

## End state

The mission is complete when all of the following hold.

- The set type's layout declares the synthesis and the three verifications
  as roles, required for a `complete` disposition, with identity from the
  boundary and citation scopes that match what each document may cite. A
  retained complete set holds them, pinned. The relation that every limit a
  verification declares is carried by the synthesis's Limitations is a set
  relation.
- The overview copies no other member. It is a code-written entry page:
  identity and disposition, the synthesizer's description, links to every
  member, the amendment index and the deterministic validation account. The
  set rule has no copy check. Rules the overview type stated about the
  synthesis's text live in the synthesis type.
- `commonplace-validate` checks a draft at an intended member path and
  reports the findings for that path's role, with repair text on the
  findings, writing nothing. Acceptance for every job is that result plus a
  labelled job residue, and a test asserts the equality.
- `commonplace-analysis-check` does not exist, and no instruction, command
  reference or worktree setup names it. ADR 105 is amended to one validation
  command, and ADR 098 is amended on where the judgments live.
- A regenerated dynamic-cheatsheet set on the production configuration and
  one run on the test configuration on another system validate in the new
  shape, with the measurements below recorded.

## Boundaries

These hold throughout and are not the implementer's to trade.

- **Membership stays closed and positional.** A member is a file at a
  declared path; nothing declares membership in frontmatter.
- **One version per role.** The set holds the current version of each
  member. Earlier versions, the answers file, correction packets, change
  diffs, round set-check files and run state stay outside the set and are
  never published. The set type's statement that working inputs live outside
  is narrowed to name them, not removed.
- **Validation writes nothing.** A draft placed in its role replaces the
  incumbent for every check in one invocation and leaves `output/` as it was.
- **Replay is byte-idempotent.** Copying a verification or synthesis into
  its role is a coordinator write in a replayable sequence and must behave
  as the report copies do.
- **ADR 102 is unchanged.** The overview's path and its role as the public
  entry stay; the boundary and the new members are members, not entries.
- **Two callers, one judgment.** Self-check and acceptance print identical
  text for the same set finding. The residue is labelled so a narrower
  content pass never claims job acceptance.
- **Absent is expected mid-run.** Callers drop absent-member findings
  deliberately and never suppress failures in general.
- **Isolated worktrees count only after the adoption is installed there.**

## Delegated to the implementer

Within the boundaries, the implementer decides, and need not ask:

- The sequence and parallelism of the work. One ordering that respects the
  dependencies: the validator's draft-in-role invocation is independent of
  the new roles and useful to analysts at once; retirement of the command
  needs both; the regeneration run comes last.
- The validate flag's name and shape, and how repair text attaches to
  findings.
- The new members' file names, and whether each verification role's
  `verifies` value is fixed by a small layout facility or stays in the job
  residue.
- Which checks join the residue. The expected residue is the boundary
  against the frozen checkout and run parameters, the predecessor and
  answers checks in correction rounds, the profile's current comparison
  version and run identity, and the verifier's blockers after a failed round
  check. A check the implementer finds expressible as a layout relation
  should move into the layout; a check that turns out to depend on the
  invocation joins the residue.
- The overview's form within its end state, for instance a list or a table
  of members.
- How the worker rules and the handout name the residue to analysts.
- Whether the regeneration run and the test run proceed in parallel.

## Reserved to the operator

Report and wait rather than decide:

- Adding members beyond the four named, or changing the set's membership
  policy.
- Publishing anything the boundaries name as staying outside the set.
- Any change to what the overview is for, or to ADR 102's entry path.
- Keeping the check command in any form.

## Report back when

- A check the workflow needs cannot be expressed as a layout relation and
  also does not depend on the job's invocation; it is the warrant the
  companion proposal's stage two is waiting for.
- Acceptance and self-check cannot be made equal for the same bytes.
- Thinning the overview breaks a consumer: the published site, the
  landscape synthesis, the comparison matrix or a transfer scan.
- Replay, assembly, publication or retained-set validation needs a special
  case for the new members.
- A run on the new shape is refused for a reason the implementer cannot
  attribute to the draft.

## Measurements

Record per run and per job: the set findings delivered and how many
concerned another member, which should be zero; the residue refusals by
rule; and whether a self-check and the following acceptance ever disagreed
on a set finding for the same bytes. These feed ADR 105's revisit and the
companion proposal's decision on its stage two.

## Alternatives

- **Keep the check command as a wrapper.** It already shares code with
  acceptance. Rejected: it loads the workflow definition to check a file,
  which needs the run-code guard and a job name, and it keeps a second
  command whose only distinct content is the repair text.
- **Give non-member types a declared relation and let validate take a
  context directory.** This is the companion proposal's stage two applied to
  verifications and the synthesis as outsiders. Rejected here because
  membership answers the same need with the mechanism that exists, and gives
  the retained set the judgments as bytes.
- **Register every run file, including packets and diffs.** Rejected: they
  are derived from members, no check needs them once the verifications are
  members, and publishing them presents views as products.
- **Check a synthesis draft in the overview role by rendering it.** Rejected:
  the renderer needs the judged verifications and the validation account, so
  the candidate would not be the synthesizer's bytes.
- **Keep the overview self-contained under copy rules.** Possible, and it
  preserves what current readers get. Rejected by the operator: once every
  copied section has a member, the copies add only a rule to keep them equal.
- **Prescribe the sequence of work.** The earlier version of this proposal
  did. Rejected: the dependencies are few and visible, and an implementer
  who meets the end state within the boundaries needs no order imposed.

## Forces

- **Expected incompleteness.** Verifications are written after the member
  they judge, so mid-run the working artifact lacks them. The layout already
  tolerates absent members in a working instance.
- **Repair information.** An analyst acts on a finding only if it names the
  rule, the location and the repair; moving repair text onto findings is
  what lets one validator serve both callers.
- **Published site.** Retained sets gain four pages; readers who relied on
  the overview being self-contained follow one link.
- **Evidence from runs.** The measurements are the only way to learn whether
  whole-artifact reading with a role filter suffices; they must be recorded, not
  reconstructed.

## Free choices

Everything under "Delegated to the implementer".

## Adoption criteria

The end state above, observed: the layout and a pinned retained set with the
new roles; an overview without copies and a set rule without copy checks;
validate checking a draft in its role with acceptance equal to it plus the
labelled residue, asserted by a test; the check command gone from code and
documents; both runs recorded with their measurements.
