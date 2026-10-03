# Report-collection split proposal

## Commission and status

Requested by the operator on 2026-10-03, drafted by an agent. This is a
proposal awaiting adoption. It authorizes no relocation, method edit or run.
Adoption revises [ADR 099](../../reference/adr/099-agentic-analysis-method-and-reports-belong-to-the-collection.md),
which chose one collection contract on 2026-10-01, so it needs an ADR.

## Motivation

The split is intended to make a difficult analytical workflow feasible through
aggressive, role-specific input reduction. Analysts must trace source behavior,
apply several distinctions, preserve evidence, and produce mutually consistent
records. Mandatory material unrelated to their assigned work adds reading and
context cost without helping them perform those tasks.

The design objective is the smallest complete instruction set for each role.
Every additional mandatory input needs a task-specific reason. This is an
operator-selected optimization priority, not a claim that this run proves a
particular context limit or that fewer bytes necessarily improve analysis.

Three facts produce the cost:

1. The root doctrine tells every writer to read the target collection
   contract before writing.
2. Analysis workers write report members under `kb/agentic-systems/reports/`,
   so their contract is `kb/agentic-systems/COLLECTION.md`.
3. That contract is 13.7 KB and also governs reviews, comparisons, method
   authoring, publication and outbound linking. An analyst needs a subset of
   those rules; the per-job coverage check below must establish which subset.

A separate collection would give report authors a small, independently
maintained contract while preserving the root reading rule. The target is
2–3 KB, not a measured result yet. Unrelated changes to review, comparison or
method-authoring rules would no longer automatically enlarge analyst input.

The motivation is the standing per-job reading cost and control over its future
growth. The two recovered path errors below are secondary delivery evidence,
not the reason to split or proof that the large contract caused analytical
mistakes.

## Observation

Observed in the stopped run `AAS-2026-10-03-graphiti-05`: both parallel
analysts guessed `kb/agentic-systems/reports/COLLECTION.md`, received a
missing-file error, located the real contract and read it whole. The cost
was two failed calls and two 13.7 KB reads. Anchors are in the
[Sol run follow-up plan](./sol-run-follow-up-plan.md), item 1.

That plan's item 1 would supply the whole contract in every job packet.
This fixes discovery but makes the full reading cost routine. It is a valid
immediate repair, not necessarily the desired permanent input structure.

## Alternatives

**Shorten the existing contract.** Extract specialist authoring, maintenance
and migration procedures into separately loaded instructions. This can reduce
mandatory input without relocation. It retains one shared contract for several
artifact classes, so keeping irrelevant rules out of analyst input requires
continuing discipline across those consumers.

**Separate the analysis collection.** Preferred for the operator's optimization
priority: give workflow-produced analysis artifacts their own small contract
and a boundary against unrelated input growth. Relocation and ownership changes
are costs to manage, not reasons by themselves to retain a costly input
structure. The contract prototype must demonstrate the expected reduction.

**Exempt workers from the collection read.** A narrow, explicitly authorized
exception could reduce input immediately, but adds a special consumption rule
and requires another account of how workers receive all binding requirements.
It is not adopted here and must not appear as an implicit stopgap.

## Proposal

Create a separate top-level collection for analysis reports, with a minimal
contract that a report writer can follow as the root rule states.
The collection is `kb/agentic-system-analyses/`, named by the operator on
2026-10-03. The former `reports/` level disappears: `state/`, `retained/`,
`retained-archive/` and `types/` sit directly under the collection root.

Workers generate the analysis inside this collection. Publication selects an
accepted report for public discovery by linking to it; it does not generate a
second compact review that restates the analysis elsewhere.

### Publication by reference

The analysis collection owns the authored result and its accepted version.
Publication owns public selection and navigation. A public entry may name the
system, give a short navigation description, and link to the accepted report.
For a multi-file analysis set, the link targets its reader-facing overview,
which exposes the accepted members and reconciliation. Readers must not be
left to resolve conflicting worker drafts themselves.

Working files remain excluded from public site output and navigation until
acceptance. Validation and independent review still establish acceptance of
exact report bytes; changing publication does not waive those gates. The
coordinator controls assembly, retention and the public link. Workers cannot
publish by writing into a publicly visible location.

The link identifies a stable accepted version. A subsequent analysis receives
its own identity, and publication changes the selected link only after its
acceptance. Failed or interrupted publication must leave the prior selection
valid or expose an explicit recovery condition. Retention or relocation within
the collection may still be needed to freeze the accepted bytes, but publication
must not require reauthoring them as a separate review.

No pointer format or navigation location is selected here. Existing pins,
provenance, comparison readers and freshness checks need a replacement
consumption path before the generated-review contract can be retired.

### What moves

| From `kb/agentic-systems/` | Disposition |
|---|---|
| `reports/state/` | Moves. Stays ignored local state, skipped by ordinary validation. |
| `reports/retained/` | Moves. |
| `reports/retained-archive/` | Moves as history. Operator statement, 2026-10-03: the archive serves comparison only and is no procedure's input, so it needs no pin preservation beyond its own bytes. |
| `types/` member types: overview, runtime report, memory report, epistemic report, reconciliation report, analysis set, run state | Move. Type identities change to the new collection's `types/` path. |
| `types/generated-review.md` | Retire from new-run publication once its consumers have an accepted-report reference path; preserve historical use as needed. |
| `reviews/` | No new duplicate generated reviews. Existing generated reviews need migration, replacement by navigation, or explicit retirement; ordinary authored reviews are not automatically affected. |
| `comparisons/`, `README.md`, `COLLECTION.md` | Stay; navigation and consumers change to reference accepted analyses. |
| `instructions/` (method, job instructions, shared analysis contracts) | Open; see decisions. |

Moving reports and their types together keeps local type eligibility
without a resolver exception. ADR 099 rejected "move only the types" for
that reason; this proposal does not reopen it.

### The minimal contract

Target size: 2–3 KB, treated as a serious input budget. It states only what a
report writer or report reader needs. If it grows, first ask whether a rule
belongs in a type or a role-specific instruction; do not omit binding rules
merely to meet the budget:

- what a report member is: a typed, workflow-produced part of one analysis set;
- the quality goal, fidelity and economy, and that source-native operation
  precedes any Commonplace concept;
- the lifecycle of `state/`, `retained/` and `retained-archive/`, moved from
  the agentic-systems contract;
- working-state authorship and repair within the assigned job's authority,
  with coordinator-owned assembly and publication;
- retained-set immutability: substantive corrections require a new run;
  archives preserve historical evidence;
- type eligibility for the local types;
- the accepted report or set overview is the public analysis, not input to a
  duplicate generated review;
- what does not belong: separate comparative essays, comparison tables,
  transfer scans, method-authoring procedures.

The agentic-systems contract loses its report-lifecycle section and keeps a
pointer. Record definitions and the theory-builder conditions stay in the
shared analysis contracts that packets already supply; the new contract does
not duplicate them.

Each job packet supplies the new contract as a `read-first` path, so workers
do not locate it themselves and its bytes participate in job dependencies.
Workers that produce no collection member need no such entry.

### What the relocation and publication change must touch

Found by search on 2026-10-03; an implementation plan must redo the inventory.

- Workflow, publication, analysis, set and validation code under
  `src/commonplace/lib/`, and their tests.
- Site publication: `properdocs.yml` excludes `agentic-systems/reports/**`
  with re-inclusions for retained members, and `properdocs_hooks.py` treats
  the collection names `messages` and `reports` as unpublished. A new
  top-level collection is published unless these are updated.
  `tests/commonplace/docs/test_site_publication_boundaries.py` covers this.
- The analysis skill, job instructions, `worker-rules.md`, landscape
  synthesis, taxonomy refresh and the transfer scan, which name report paths.
- `kb/reference/commands.md`, `kb/reference/validation-contract.md` and
  `scripts/README.md`.
- Generated-review rendering, types, publication checks, navigation and
  downstream consumers that currently discover a set through review metadata.
  Replace that dependency with accepted-report references before removing it.
- Existing generated reviews and their retained-set pins. The operator's
  intended refresh now produces analyses linked directly, not another layer
  of compact reviews. Future refresh does not authorize broken pins in the
  interim: decide whether each current review/set pair moves mechanically,
  stays valid until replaced by navigation, or is explicitly retired.
- Published URLs and redirects, including existing redirects into
  `retained-archive/`. An archive can have navigation consumers even when no
  procedure consumes it. Preserve historical bytes without silently retyping
  them; give links and redirects an explicit disposition.

Commit the `commonplace-relocate-*` result alone, without content edits.

## Open decisions

1. **Where the method lives.** Recommended: leave `instructions/` in
   `kb/agentic-systems/` if it continues to govern the broader analysis,
   review and comparison system. Choose ownership by those consumers, not
   by directory size: workers do not read every file in a collection.
   Packets supply the needed method files explicitly. The cost is that
   instructions in one collection define content for another.
2. **The two current retained sets and `layout-migration-2026-10-01/`.**
   The new ADR must explicitly authorize any bounded migration and its hash
   map; ADR 099 authorized its own migration, not every future move. Decide
   whether to migrate current sets, keep them until replacement, or retire
   them under separate authority. The migration report describes the earlier
   layout and may itself become history.
3. **Sequencing against the Sol plan.** Recommended: item 1 of that plan
   becomes "supply the new collection's contract" and depends on this split.
   If the split is delayed, keep the current contract rule unless the operator
   separately adopts a scoped exception. Do not silently omit the contract.
4. **Public selection and reader entry point.** Choose where links to accepted
   analyses live and how consumers identify the selected version and its
   provenance. Keep that navigation lightweight. Determine whether the current
   overview already provides sufficient synthesis and reconciliation access;
   any required reader-facing improvement belongs in the analysis itself,
   not in a duplicate review.

## Costs and risks

- This is the second layout migration of these reports within a week. ADR 099
  moved them on 2026-10-01. The new ADR must state why one contract no
  longer fits the selected priority: analyst input reduction now takes
  precedence over keeping all research artifacts under one contract.
- It overlaps files with uncommitted isolation work (`SKILL.md`,
  `drive-a-code-scheduled-run.md`) and with the Sol repairs. It should start
  after isolation lands, and no run may be open across the relocation: a run
  keeps its opening method commit.
- The evidence is one run and two recovered errors. The split is justified by
  the standing per-job reading cost, not by error frequency.
- Removing generated reviews changes the public discovery and consumer
  interface, not merely paths. A link to an unreviewed draft, stale selection,
  or unreconciled member is not equivalent to publishing an accepted analysis.

## Check before adoption

Draft the minimal contract first and measure it. For each job, list the
collection-level rules its output depends on and their consumption paths.
Confirm each rule is in the draft contract or a supplied role/type instruction.
Use this check to remove irrelevant mandatory input, not to justify loading
everything defensively. Measure the complete mandatory packet before and after,
so moving text into another always-loaded file cannot masquerade as a saving.

Compare the resulting packet against shortening the existing contract. Prefer
the split if it supplies a sufficient small contract and a clearer boundary
against unrelated input growth. If the draft cannot stay near 3 KB, first test
whether specialist rules belong elsewhere; return unresolved sufficiency or
budget trade-offs to the operator before relocation.

Settle current-set/review pins, archive navigation, and sequencing after the
isolation changes are committed. Demonstrate that an accepted analysis is
readable through its report or overview without the generated review; that
comparison consumers can resolve the selected set and provenance; and that
unaccepted work remains unpublished. Check initial publication, replacement,
and interrupted link updates without changing accepted bytes. These are
migration obligations, not evidence against input optimization.

A separately commissioned live run should measure
input size and read calls alongside coverage, acceptance and repair outcomes.
Reduced bytes alone do not demonstrate improved analytical quality.

## What closes this proposal

An accepted ADR revising ADR 099 and the affected publication contracts, plus
a completed relocation and publication-by-reference transition; or a recorded
rejection with the chosen alternative for item 1 of the Sol plan.
