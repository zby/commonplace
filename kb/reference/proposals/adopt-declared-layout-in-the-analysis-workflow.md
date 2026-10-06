---
description: "Proposal: register the synthesis and the three verifications as members of the analysis set, thin the overview to an entry page, check drafts at their slot through commonplace-validate, and retire the separate analyst check command."
type: reference/types/design-proposal.md
tags: [type-system]
---

# Adopt the declared layout in the analysis workflow

[Directory types declare their layout](./directory-types-declare-their-layout.md)
shipped on 2026-10-06, and the analysis workflow's acceptance, round-close and
publication code moved onto the declared layout the same day. This proposal
is the remainder of that adoption: the run's products that still live outside
the set, the overview sections that copy other members, and the separate
check command that analysts run because `commonplace-validate` cannot check a
draft at its slot. It is written as an ordered plan for an implementer. The
operator selected this direction on 2026-10-06. It is not shipped behavior.

Its validator side is stage one of
[document validation in working-set context](./type-declared-cross-checks-and-one-validation-surface.md),
which this plan decides in place of the measurement runs the earlier version
of this proposal gated it on.

## Current state (as of 2026-10-06)

- **Adopted:** run opening writes `output/` with a type-only manifest before
  the boundary job, and the boundary is the set's first member; one helper,
  `set_findings` in `src/commonplace/lib/agentic_workflow.py`, validates
  `output/` as a directory artifact with a candidate's bytes placed at its
  slot through content overrides, and the analyst, reconciliation and profile
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
no way to receive a draft at its slot. Each is a place where the workflow
and the type can drift.

## Design

### Members

Four roles join the set's layout, each with the current version at its slot
and required when the disposition is `complete`:

| Role | Path | Type | Identity | Cites |
|---|---|---|---|---|
| synthesis | `synthesis.md` | synthesis | boundary: run-id, reviewed-boundary | boundary, runtime, memory, epistemic |
| record-verification | `record-verification.md` | verification | boundary: run-id, reviewed-boundary | boundary, runtime, memory, epistemic, reconciliation |
| profile-verification | `profile-verification.md` | verification | boundary: run-id, reviewed-boundary | runtime, memory, epistemic, memory-profile |
| synthesis-verification | `synthesis-verification.md` | verification | boundary: run-id, reviewed-boundary | boundary, runtime, memory, epistemic, synthesis |

The set rule gains one relation: every limit a verification declares names a
record the synthesis's Limitations section mentions. That check leaves the
synthesis acceptance function. The two overview copy rules are deleted.

Each verification role's `verifies` value is fixed by its slot. Whether the
layout gains a small fixed-fields facility for that or the workflow keeps
the check is a free choice.

### The overview

The overview becomes a code-written entry page: identity and disposition in
frontmatter, the synthesizer's description, a link to every member, the
amendment index and the deterministic validation account. The boundary,
source register, bounded synthesis, limitations and verification sections
leave it. Rules the overview type states about the synthesis's text, such as
reading without the members' context, move to the synthesis type. ADR 102's
stable path and entry role are unchanged; ADR 098 is amended on where the
judgments live.

### What stays outside the set

Correction request packets and change diffs are code-rendered views of
members and remain job inputs. Round set-check files are validation results
and remain what the verifier reads. Previous versions of a member, the
analyst's `answers.md` and run state remain working files. The set type's
statement that working inputs live outside the output directory is narrowed
to name these.

### Drafts checked through validate

`commonplace-validate` takes a draft and the member path it is intended for,
places the draft's bytes at that path through the existing content
overrides, validates the directory, and reports the findings attributed to
that path's role, with absent-member findings dropped. Nothing is written.
Repair advice moves from the workflow's wrapper onto the findings, so a
finding prints the same text whether validate or acceptance reports it. This
is stage one of the companion proposal.

### Acceptance

Each job's acceptance is the draft's validate result plus a labelled job
residue. The residue is what depends on the job's invocation, not on the
documents:

- boundary: the frozen checkout is at the recorded revision and clean, the
  source matches the run's parameters;
- analysts in a correction round: no record its predecessor declared is
  dropped, and `answers.md` answers every blocker addressed to it;
- profile: the comparison block is the current write version, and the
  source identity matches the run parameter;
- verifiers: blockers are written when the round's set check failed.

The handout names the residue so an analyst knows which refusals the
self-check cannot show. The parity test asserts that acceptance equals
validate's result for the draft plus the residue.

### Retirement

With the residue labelled and validate able to check a draft at its slot,
`commonplace-analysis-check` is removed: its entry point, module and test,
the isolated-worktree lookup of it, the worker rules' check section, the
command reference's two sections and its mention in the isolated-run
paragraph. The scratch count log goes with it; ADR 105's revisit counts
refusals from engine acceptance records instead. ADR 105 is amended to one
validation command for analysts, acceptance and maintainers.

### Order of work

1. Stage one of the companion proposal on `commonplace-validate`, with
   repair text on findings. It is independent of the new roles and analysts
   can use it at once.
2. The four roles in the set type, the limits-carried relation, the
   `verifies` fixing, the synthesis rules moved from the overview type, the
   overview type and renderer reduced, the copy rules deleted, publication
   and the site following the layout. ADR 098 amended.
3. The acceptance functions reduced to validate plus the labelled residue;
   the parity test retargeted; the command, its docs and its log retired;
   ADR 105 amended.
4. A regeneration run of dynamic-cheatsheet on the production configuration,
   the first set in the new shape, followed by one run on the test
   configuration on another system.

Steps 1 and 2 can proceed in parallel. Step 3 needs both. Step 4 needs the
adoption landed in the installed tool of the isolated worktree.

### What this changes for analysts and readers

An analyst runs one command on a draft and sees the type's findings for
their role, with the same repair text acceptance will print, plus a short
named list of what only acceptance checks. A reader of a retained set finds
the synthesis and each verification as the member its author wrote, pinned
in the manifest, and reaches them from the overview by link rather than
reading them inlined.

### Measurements

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
- **Check a synthesis draft at the overview slot by rendering it.** Rejected:
  the renderer needs the judged verifications and the validation account, so
  the candidate would not be the synthesizer's bytes.
- **Keep the overview self-contained under copy rules.** Possible, and it
  preserves what current readers get. Rejected by the operator: once every
  copied section has a member, the copies add only a rule to keep them equal.

## Forces

- **Expected incompleteness.** Verifications are written after the member
  they judge, so mid-run the working set lacks them. The layout already
  tolerates absent members in a working instance; callers drop absent
  findings deliberately, not failures in general.
- **One version per slot.** The set holds the current version of each
  member; earlier versions stay in the run directory. The predecessor check
  therefore stays in the residue.
- **Consistent bytes.** A draft placed at its slot replaces the incumbent for
  every check in the invocation and nothing is written to `output/`.
- **Replay.** Copying a verification or synthesis into its slot is a new
  coordinator write in a replayable sequence and must be idempotent on
  bytes, as the report copies are.
- **Published site.** Retained sets gain four pages; the overview stays the
  entry under ADR 102.
- **Two callers, one judgment.** Self-check and acceptance print the same
  text for the same set finding, so repair advice lives on the finding.
- **Isolated analysis worktrees** have their own command environment; the
  adoption must land there before a run on it counts as evidence.

## Free choices

The validate flag's name and shape, how repair text attaches to findings,
whether `verifies` is fixed in the layout or in the workflow residue, the
new members' file names, whether the overview links members in a list or a
table, and whether the regeneration run and the test run proceed in parallel.

## Adoption criteria

- The set type's layout names the synthesis and three verification roles,
  and a complete retained set contains them, pinned.
- The overview holds no section that copies another member, and the set
  rule has no copy check.
- `commonplace-validate` reports, for a draft at an intended member path,
  the findings for that role and nothing for other roles; acceptance equals
  that result plus the labelled residue, and the parity test says so.
- `commonplace-analysis-check` does not exist; worker rules and the command
  reference name only `commonplace-validate`.
- The regenerated retained set validates, and both runs are recorded with
  the measurements above.
