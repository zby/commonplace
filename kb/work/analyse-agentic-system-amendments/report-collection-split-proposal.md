# Report-collection split proposal

## Commission and status

Requested by the operator on 2026-10-03, drafted by an agent. This is a
proposal awaiting adoption. It authorizes no relocation, method edit or run.
Adoption revises [ADR 099](../../reference/adr/099-agentic-analysis-method-and-reports-belong-to-the-collection.md),
which chose one collection contract on 2026-10-01, so it needs an ADR.

## Problem

Analysis workers write report members under `kb/agentic-systems/reports/`.
The root doctrine tells every writer to read the target collection contract.
The governing contract, `kb/agentic-systems/COLLECTION.md`, is 13.7 KB and
must stay large: it also governs reviews, comparisons, method authoring,
publication and outbound linking. A report writer needs almost none of it.

Observed in the stopped run `AAS-2026-10-03-graphiti-05`: both parallel
analysts guessed `kb/agentic-systems/reports/COLLECTION.md`, received a
missing-file error, located the real contract and read it whole. The cost
was two failed calls and two 13.7 KB reads. Anchors are in the
[Sol run follow-up plan](./sol-run-follow-up-plan.md), item 1.

That plan's item 1 would supply the whole contract in every job packet.
This makes the read permanent while worker input size is already a problem.
The alternative considered first was a stated exception in `worker-rules.md`
telling workers not to read a collection contract. It is cheap, but it
leaves the root rule and the job rules in conflict and resolves the conflict
by exemption.

## Proposal

Create a separate top-level collection for analysis reports, with a minimal
contract that a report writer can follow as the root rule states.
The working name here is `kb/agentic-system-reports/`; the name is the
operator's choice.

### What moves

| From `kb/agentic-systems/` | Disposition |
|---|---|
| `reports/state/` | Moves. Stays ignored local state, skipped by ordinary validation. |
| `reports/retained/` | Moves. |
| `reports/retained-archive/` | Moves as history. Operator statement, 2026-10-03: the archive serves comparison only and is no procedure's input, so it needs no pin preservation beyond its own bytes. |
| `types/` member types: overview, runtime report, memory report, epistemic report, reconciliation report, analysis set, run state | Move. Type identities change to the new collection's `types/` path. |
| `types/generated-review.md` | Stays. Reviews stay in `kb/agentic-systems/reviews/`. |
| `reviews/`, `comparisons/`, `README.md`, `COLLECTION.md` | Stay. |
| `instructions/` (method, job instructions, shared analysis contracts) | Open; see decisions. |

Moving reports and their types together keeps local type eligibility
without a resolver exception. ADR 099 rejected "move only the types" for
that reason; this proposal does not reopen it.

### The minimal contract

Target size: 2–3 KB. It states only what a report writer or report reader
needs:

- what a report member is: a typed, workflow-produced part of one analysis set;
- the quality goal, fidelity and economy, and that source-native operation
  precedes any Commonplace concept;
- the lifecycle of `state/`, `retained/` and `retained-archive/`, moved from
  the agentic-systems contract;
- workflow-only authorship: correct through a new run, never by hand edit;
- type eligibility for the local types;
- what does not belong: reviews, comparisons, transfer scans, method.

The agentic-systems contract loses its report-lifecycle section and keeps a
pointer. Record definitions and the theory-builder conditions stay in the
shared analysis contracts that packets already supply; the new contract does
not duplicate them.

Each job packet supplies the new contract as a `read-first` path, so workers
do not locate it themselves and its bytes participate in job dependencies.
Workers that produce no collection member need no such entry.

### What the relocation must touch

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
- The generated reviews, which pin retained-set paths and hashes. The
  operator plans to regenerate all reviews, so they are replaced, not migrated.

Commit the `commonplace-relocate-*` result alone, without content edits.

## Open decisions

1. **Where the method lives.** Recommended: leave `instructions/` in
   `kb/agentic-systems/`. Workers receive those files by absolute path, and
   moving them makes the new collection larger, not minimal. The cost is
   that instructions in one collection define content for another.
2. **The two current retained sets and `layout-migration-2026-10-01/`.**
   Either relocate them under ADR 099's bounded migration exception, with a
   new hash map, or drop them once regenerated runs replace them. The
   migration report describes the earlier layout and may itself become history.
3. **Sequencing against the Sol plan.** Recommended: item 1 of that plan
   becomes "supply the new collection's contract" and depends on this split.
   If the split is delayed, use the `worker-rules.md` exception as a stopgap
   and remove it when the split lands.
4. **Collection name.**

## Costs and risks

- This is the second layout migration of these reports within a week. ADR 099
  moved them on 2026-10-01. The new ADR must state why one contract no
  longer holds: the worker reading cost was not weighed then.
- It overlaps files with uncommitted isolation work (`SKILL.md`,
  `drive-a-code-scheduled-run.md`) and with the Sol repairs. It should start
  after isolation lands, and no run may be open across the relocation: a run
  keeps its opening method commit.
- The evidence is one run and two recovered errors. The split is justified by
  the standing per-job reading cost, not by error frequency.

## Check before adoption

Draft the minimal contract first and measure it. Then list, for each job,
the collection-level rules its output depends on, and confirm each is in the
draft contract or in a file the packet already supplies. If the draft cannot
stay near 3 KB, or a job needs a rule that lives only in the large contract,
return to the operator before relocating anything.

## What closes this proposal

An accepted ADR revising ADR 099 plus a completed relocation, or a recorded
rejection with the chosen alternative for item 1 of the Sol plan.
