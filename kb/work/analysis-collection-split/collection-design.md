# Analysis collection design

## Status

Settled design, decided by the operator on 2026-10-03. Implementation is
commissioned by the [plan](./plan.md); this
file says what to build and why, and authorizes nothing by itself. It revises
[ADR 099](../../reference/adr/099-agentic-analysis-method-and-reports-belong-to-the-collection.md),
which chose one collection contract on 2026-10-01.

## Purpose

Analysis workers fail parts of their jobs. The operator's response is to
simplify the analyst's job: an analyst should hold only the analysis. Today
analysts write under `kb/agentic-systems/`, whose 13.7 KB contract also governs
reviews, comparisons, method authoring and publication. Root doctrine tells
every writer to read that contract, and the job packets omit it, so each
worker must resolve the contradiction itself.

A separate collection gives analysts a contract that addresses analysis only,
supplied to them by path. Measured per analyst role, it removes five to seven
unrelated concerns; shortening the shared contract removes one. The contract
is a small share of an analyst's input, so the lasting effect is the
boundary: publication, comparison and method authoring cannot add rules to
analyst input later. The full reasoning, the rejected alternatives and the
measurements are in [evidence](./evidence/motivation.md).

## The collection

The collection is `kb/agentic-system-analyses/`. `state/`, `retained/`,
`retained-archive/`, `types/` and `instructions/` sit directly under its root.

### The collection owns the whole run, and analysts see only analysis

The analysis collection holds the analyses, their run state, their types, the
analysis method and the current accepted sets. A run starts and ends
inside it. `kb/agentic-systems/` keeps hand-authored reviews, comparisons,
landscape synthesis and taxonomy maintenance.

Self-containment must not put publication into analyst input. The rule is
about what a worker reads, not about directories:

- The analysis contract states placement and immutability only. It says in
  one line that `retained/` holds the current analyses, and carries no other
  rule about selection or public exposure.
- Publication rules live in the publication instruction. Only the coordinator
  loads it. No analyst packet supplies it.
- An analyst's obligations end at an accepted member. A field or section that
  exists only for a publication or comparison consumer is a candidate to move
  to a coordinator step.

Current analyst inputs are not yet free of publication: the boundary job reads
`opening`, which its instruction describes as publication metadata, and the
memory job instruction mentions publication checks. Each needs a disposition:
keep with a stated analytical reason, reword, or move. The memory analyst
also produces the cross-system comparison profile. The operator decided on
2026-10-03 to move it to a separate job; its design is the
[profile job design](./profile-job-design.md).

### Publication replaces the system's set in `retained/`, and the list is generated

The workflow produces one accepted analysis per run. Its overview is the
reader-facing review: it gives the synthesis and limitations and links the
members and reconciliation. The workflow writes no second, compact review.

**What is current.** The current analysis of a system lives at
`retained/<system-slug>/`. The slug is the one the run ID already uses,
derived from the source identity. The path does not contain the run ID, so it
stays the same when a newer analysis replaces the set. There is one directory
per system, so the filesystem allows only one current set per source.

**Links follow the newest analysis.** A link to
`retained/<system-slug>/overview.md`, from a note, a comparison or another
site, always reaches the current analysis. It needs no redirect and no rewrite
when a new run is accepted. Anything that depends on an exact version must
cite the run ID and the commit, or the set's archive path once superseded.
The run ID stays in each member's frontmatter and in the manifest.

**Publication** does two things after acceptance, in one commit:

1. If `retained/<system-slug>/` exists, move that set unchanged to
   `retained-archive/<run-id>/`, under its own run ID.
2. Copy the accepted bytes unchanged into `retained/<system-slug>/`.

Both areas sit at the same depth, so a moved set's relative links should still
resolve and its bytes and manifest hashes should not change. This has not been
tested on a real set.

**The list.** No list file is written or committed. The current-analyses list
is generated, as directory indexes already are: the site build materializes
it in memory from the published files (ADR 025). It reads the overview
frontmatter of each set in `retained/`: system, description, reviewed
boundary, run ID, run date, evidence tier and the link to the overview. It is
the reader's entry point. One library function enumerates the current sets;
the site build and the comparison tools both call it, so they cannot disagree
about the population.

**Checks.** Validation requires that the directory name equals the slug of
the set's source identity, and that no two directories in `retained/` hold
the same source identity. An interrupted publication leaves either the old
set in place or an empty or partial directory; both are detectable, and
recovery is to finish the copy or restore the old set from the archive.
Committing both steps together means no committed state is partial.

There is no per-system reference file, no committed list file, no hash pin
from a pointer to a manifest and no redirect for a current analysis. The
manifest still pins every member.

Working files stay excluded from site output until acceptance. Validation and
independent review still establish acceptance of exact bytes. Only the
coordinator copies into `retained/`; a worker cannot publish by writing a file.

Costs:

- Code and contracts assume today that a retained directory is named by its
  run ID and that a retained run is never overwritten. Both change: the
  directory is named by system, and its content is replaced, with the old
  content preserved in the archive.
- A link to the current path silently changes target when a new analysis is
  accepted. That is the chosen behavior. A note whose claim depends on what a
  specific analysis said must cite the run ID, or its claim can drift from
  its evidence.
- Superseded sets go to `retained-archive/` by operator decision of
  2026-10-03. They are excluded from current validation and from the
  comparison population. Because nothing is migrated, the archive holds no
  old-contract sets.
- Old review addresses need a one-time move as each review is regenerated.
  About 65 KB files outside the collection link to
  `kb/agentic-systems/reviews/<slug>.md` today. Use the relocation command so
  inbound links are rewritten and site redirects are added. Hand-authored
  reviews that are not regenerated keep their paths.

**Revisit conditions.** The stable path per system, links that follow the
newest analysis, and the shared archive were chosen without evidence from
use. Their revisit conditions are `TODO` items in the
[decision draft](./drafts/decision-draft.md), which becomes the ADR, so
that a search for `TODO` over ADRs finds them after this workshop closes.

### What moves

| From `kb/agentic-systems/` | Disposition |
|---|---|
| `reports/state/`, `reports/retained/`, `reports/retained-archive/` | Not migrated. Operator decision, 2026-10-03: every analysis is regenerated under the new method. The new collection starts with empty `state/`, `retained/` and `retained-archive/`. The old `reports/` tree stays where it is as frozen history; see below. |
| `types/` member types: overview, runtime report, memory report, epistemic report, reconciliation report, analysis set, run state | Move. Type identities change to the new collection's `types/` path. |
| `types/generated-review.md` | Retire from new-run publication once its consumers read the current-analyses list; preserve historical use as needed. |
| `reviews/` | Hand-authored reviews stay (12 of the 13 files today). No new generated reviews are written there. The one existing generated review is replaced by its list entry or explicitly retired. |
| `comparisons/`, `README.md`, `COLLECTION.md` | Stay; navigation and comparison tools read the current-analyses list. |
| `instructions/analyse-agentic-system/` (skill, run driver, job instructions) and the shared contracts `agentic-analysis-boundary.md`, `agentic-analysis-sources.md`, `agentic-analysis-records.md` | Move. Operator decision, 2026-10-03: the new collection is self-contained and owns the analysis method. |
| `instructions/synthesize-agent-memory-landscape/`, `instructions/refresh-agent-memory-review-taxonomy.md` | Stay. They serve comparison, not analysis. |

The new collection is self-contained: an analysis run needs no method file,
type or contract from `kb/agentic-systems/`. The one dependency runs the other
way: comparison tools in `kb/agentic-systems/` read the current-analyses list
and the retained sets. No worker packet crosses the boundary.

**Nothing is migrated.** No retained set, archive or run state moves into the
new collection, so the split needs no hash map, no repinning and no bounded
migration authority. Consequences for the old tree:

- The two current sets and the earlier migration report name member types
  under `agentic-systems/types/`, which move. Once the types move, those sets
  no longer validate as current sets. Put `reports/retained/` under the same
  validation exclusion the archive already has. The archive's sets already
  name contracts that are no longer current, so this follows precedent.
- The one generated review pins one of those sets. Retire it when the types
  move, and regenerate that system first so the gap is short.
- The comparison population is empty until analyses are regenerated. The
  matrix, landscape synthesis and taxonomy refresh have no current input in
  that interval.
- The new `retained-archive/` then holds only superseded sets of the current
  contract. Historical old-contract sets stay in the old tree, so the two
  kinds are not mixed.
- Runs open under the old method finish there or stay as stopped evidence.
  They are not resumed under the new method.

New collection members and their types share one owner, which keeps local
type eligibility without a resolver exception. ADR 099 rejected "move only the types" for
that reason; this design does not reopen it.

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
- placement of the method under `instructions/`, with one sentence sending
  method authors to a separately loaded maintenance instruction;
- what does not belong: separate comparative essays, comparison tables,
  transfer scans, publication procedures.

Owning the method must not grow the analyst's contract. Method-authoring
rules live in the maintenance instruction, which only method authors load.
The contract carries the pointer and nothing else about authoring. The
[drafted contract](./drafts/analysis-collection-contract.md) was updated
to the decisions but not re-measured.

Publication rules are excluded: how an analysis is selected and listed belongs
to the publication instruction, which only the coordinator loads.

The agentic-systems contract loses its report-lifecycle section and keeps a
pointer. Record definitions and the theory-builder conditions stay in the
shared analysis contracts that packets already supply; the new contract does
not duplicate them.

Each job packet supplies the new contract as a `read-first` path, so workers
do not locate it themselves and its bytes participate in job dependencies.
Workers that produce no collection member need no such entry.

### Registered vocabulary

`AGENTS.md` requires reading a registered term's linked definition before
using it technically. The records contract uses four such terms: theory
builder, addressable theory, representational form and explanatory reach.
Their definition notes total about 39 KB and no packet supplies them.

The supplied contracts are the binding copy for workers. Check term by term
that the contract states what a worker needs to apply the term, and fill any
gap inline in a few lines. Then state in the worker rules that the supplied
contracts carry the operative definitions and the linked notes are
background. The method-maintenance instruction lists those notes as
dependencies to recheck when a definition changes.

### Consumers the change touches

Found by search on 2026-10-03. The implementation redoes this inventory.

- Workflow, publication, analysis, set, matrix and validation code under
  `src/commonplace/lib/`, and their tests.
- Site publication: `properdocs.yml` excludes `agentic-systems/reports/**`
  with re-inclusions for retained members, and `properdocs_hooks.py` treats
  the collection names `messages` and `reports` as unpublished. A new
  top-level collection is published unless configured otherwise. The new
  collection is a public site section: retained members are published and run
  state is excluded.
- The analysis skill, job instructions and `worker-rules.md`, which move and
  name report paths; landscape synthesis, taxonomy refresh and the transfer
  scan, which stay and name them.
- Skill projections: the `analyse-agentic-system` symlinks under
  `.agents/skills/` and `.claude/skills/`, and the method paths that
  `agentic_workflow.py` resolves for job packets and method-change guards.
- `kb/reference/commands.md`, `kb/reference/validation-contract.md` and
  `scripts/README.md`.
- Generated-review rendering, its type, publication checks and the
  comparison tools that discover a set through review metadata. They read
  the sets in `retained/` instead.

## Decisions

All are the operator's, 2026-10-03. Several adopt the agent's recommendations.

- Split over shortening; the collection is `kb/agentic-system-analyses/`.
- The collection is self-contained: it owns the method, types and publication.
- The comparison profile moves to its own job; see the
  [profile job design](./profile-job-design.md).
- Stable path per system; links follow the newest analysis; superseded sets
  go to the archive. Both carry revisit conditions in the decision draft.
- Nothing is migrated; every analysis is regenerated.
- The old `reports/` tree stays in `kb/agentic-systems/` as frozen history,
  excluded from validation.
- The list of current analyses is generated at site build.
- The accepted overview serves as the reader-facing review. Check this on the
  first regenerated analysis; any needed improvement goes into the overview
  type, not into a second document.
- Order of work: the relocation first, then the profile job, both before
  regeneration starts, so each system is regenerated once. The Sol run
  follow-up plan is revised afterwards.
- No trial run precedes the relocation. The first run after the split is the
  outcome check.
- When a system is regenerated, its hand-authored review is retired with the
  relocation command: inbound links are rewritten to the new stable path and
  a site redirect is added. The two are not kept side by side.
- The new collection is a public site section. Only retained members are
  published; run state stays excluded.
- Two decision records: one for the collection split and publication, one for
  the profile job.
- The boundary job's `opening` input, which its instruction calls publication
  metadata: establish what the job uses from it, then pass only those values
  as parameters or reword it as run metadata.
- Registered vocabulary: the supplied contracts are the binding copy for
  workers, as described above.

- The profile replay is authorized and runs on Luna.

Still with the operator: the regeneration order. No other design decision is
open.

## Costs and risks

- This is the second change of ownership for the analysis method and types
  within a week. ADR 099 moved them on 2026-10-01. No report is migrated, but
  method and type paths change again. The decision record must state why one
  contract no longer fits: simplifying analyst input now takes precedence
  over keeping all research artifacts under one contract.
- No run may be open across the relocation: a run keeps its opening method
  commit.
- The evidence is two audited runs and a hypothesis about soft degradation.
  No run has measured the effect of the contract on analysis quality. If
  re-measurement shows no reduction in concerns, references or conflicts for
  analyst roles, the simplification claim fails and the remaining case is
  coherence between root doctrine and job packets.
- Removing generated reviews changes how readers and tools discover an
  analysis, not only paths.

## What closes this design

Two accepted decision records and the implemented end state of the plan; or a
recorded rejection with its reason.
