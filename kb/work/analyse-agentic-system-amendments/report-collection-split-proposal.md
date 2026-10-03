# Report-collection split proposal

## Commission and status

Requested by the operator on 2026-10-03, drafted by an agent. This is a
proposal awaiting adoption. It authorizes no relocation, method edit or run.
Adoption revises [ADR 099](../../reference/adr/099-agentic-analysis-method-and-reports-belong-to-the-collection.md),
which chose one collection contract on 2026-10-01, so it needs an ADR.

2026-10-03: the operator chose the split over shortening after reading the
[complexity measurements](./split-drafts/complexity-measurements.md). The
split removes five to seven unrelated concerns per analyst role; shortening
removes one. This records the choice between alternatives. Relocation still
needs the ADR and an accepted implementation plan.

## Motivation

Analysis workers fail parts of their jobs. The audited runs show refused
submissions, retries, rules read and not applied, wrong-path reads and
classifications returned by reconciliation; see the
[fresh-run audit](./fresh-run-audit.md), the
[second-run audit](./second-run-audit.md) and the
[Sol run follow-up plan](./sol-run-follow-up-plan.md). The operator's response
is to simplify the analyst's job. The split serves that goal: an analyst should
hold only the analysis. Fewer bytes are one part of the simplification. The
larger part is complexity: how many concerns an analyst must hold, how many
references it must resolve, and how many instructions it must reconcile.

The system must also be coherent: the instructions a worker receives must agree
with the doctrine that binds it. Today the root doctrine requires every writer
to read the collection contract, and the job packets omit it. No observed job
resolved that contradiction cleanly. A contradiction is a complexity cost by
itself, and it is sufficient reason to change the structure. The context
argument below explains why the repair should be a small analysis-only
contract and not the full shared one.

The operator's working hypothesis is that analysis jobs are context bound.
The binding limit is not the provider window. It is the
[soft degradation boundary](../../notes/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md):
the point at which a worker misses instructions or leaves context unused while
its output stays fluent. That note names three pressures that move the
boundary: volume, interference and complexity. Analysts already carry a heavy
load of all three from the task itself. They trace source behavior, apply
several distinctions, preserve evidence and produce mutually consistent
records. The design objective is therefore to remove every mandatory input
that does not serve the assigned job, and to try each available reduction.

The current collection contract adds to each pressure:

| Pressure | Current cost | Effect of the split |
|---|---|---|
| Volume | Every writer of a collection member must read the 13.7 KB contract of `kb/agentic-systems/`. | The draft analysis contract is 2.2 KB. The modelled saving is 11.5 KB per job, 14–30% of the mandatory method files, by role. |
| Interference | That contract also governs reviews, comparisons, method authoring, publication and outbound linking. An analyst must hold those rules and rule them out. | The analyst's contract contains only rules for analysis members. Rules for other artifact classes cannot enter it later. |
| Complexity | The root doctrine tells writers to read the target collection contract, but packets do not supply it. Each worker must [resolve the reference itself](../../notes/model-resolved-indirection-adds-interpretation-work-to-llm-execution.md) and decide whether the root rule or the packet's reading list governs. The contract then mixes analysis rules with publication, review and comparison rules that the worker must separate. | Each packet supplies the contract as a literal `read-first` path, so the root rule and the packet agree. The contract addresses one concern, analysis. Publication stays in `kb/agentic-systems/`. |

Interference is the argument for a separate collection. Shortening the shared
contract can recover much of the volume, and a packet entry removes the lookup
without any relocation. But a contract shared by several artifact classes must
keep rules for each of them, so only separate ownership leaves the analyst with
no rules for other classes. The volume saving is real but modest, and it is not
the reason to prefer the split over shortening.

The contract is a small share of an analyst's mandatory input, so the split
alone removes a small share of the job's complexity. Its lasting effect is the
boundary: the analysis collection and the analyst packets address analysis
only, and publication, comparison and method authoring cannot add rules to
them later. Whether that reduction is real must be measured on the analyst
jobs themselves, not on the contract's size; see the check below.

The retained records show the current structure failing in every observed
job. The root doctrine requires the contract read, and each job packet gives an
explicit reading list that omits the contract. The two instructions
contradict each other, and workers resolved the contradiction differently:

- In the two Dynamic Cheatsheet runs, all 30 worker sessions had the root rule
  in context and none read the contract. Both accepted sets were written
  outside the required write path, and no check detected it.
- In the stopped Graphiti run, both parallel analysts tried to follow the
  rule, guessed a wrong path, and then read the whole contract.

No observed job produced a clean read. A general rule that a specific packet
silently contradicts is itself an interference cost: the worker must decide
which authority governs, and the system cannot tell which choice it made. The
root delegation rule already forbids this: a parent may omit a supplied rule
only after verifying delivery. The repair is to make the packet and the
doctrine agree, and a small contract makes agreement cheap enough to keep the
reading rule without an exception.

The records do not support a volume explanation. Peak worker context in the
Dynamic Cheatsheet runs was 18–44% of the provider window. Refused submissions
did not concentrate in the largest contexts, and retries passed at about the
same size. The recurring lapse was a rule read and not applied when writing,
such as the prohibition on record ranges in the
[fresh-run audit](./fresh-run-audit.md). It stopped in verification jobs once
their packets stated the rule conspicuously, and it then appeared in
reconciliation and synthesis, whose packets did not. This supports the
interference and complexity pressures, in two runs of one source on one model.
It does not establish that the contract's content caused any analytical error,
because no worker in those runs loaded it.

The collection contract is the smallest mandatory method input. Role files are
24–69 KB per job in the [input coverage draft](./split-drafts/input-coverage.md).
The same three-pressure check applies to them and is likely to yield more. That
work is separate from this proposal and does not depend on it.

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

### Analysis and publication are separately owned

The analysis collection holds analyses, their run state and their types. It
focuses on one activity: producing an accepted analysis of one system.

The publication mechanism stays in `kb/agentic-systems/`. That collection owns
the publication instruction, the reference type and its schema, public
selection, navigation, comparison populations and the site exposure rules.
Publication code copies accepted bytes into the analysis collection's
`retained/` area, but the rules for doing so are publication rules and live
with the mechanism.

The consequence for analysts is the purpose of this separation:

- The analysis contract states placement and immutability only. It carries no
  rule about selection, references, navigation or public exposure.
- No analyst packet supplies the publication instruction or the reference type.
- An analyst's obligations end at an accepted member. A field or section that
  exists only for a publication or comparison consumer is a candidate to move
  to a coordinator step; the complexity check below lists them.

Current analyst inputs are not yet free of publication: the boundary job reads
`opening`, which its instruction describes as publication metadata, and the
memory job instruction mentions publication checks. The memory analyst also
produces the cross-system comparison profile. Each of these needs a
disposition: keep with a stated analytical reason, reword, or move. Moving the
comparison profile out of the memory job is a method change. The operator
decided it on 2026-10-03; its design is the
[comparison-profile job proposal](./comparison-profile-job-proposal.md).

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
- what does not belong: separate comparative essays, comparison tables,
  transfer scans, method-authoring procedures.

Publication rules are excluded: that the accepted overview is the public
analysis, and how it is selected, belongs to the publication contract in
`kb/agentic-systems/`.

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
- The evidence is two audited runs and a hypothesis about soft degradation.
  No run has measured the effect of the contract on analysis quality. The
  split is justified by simplifying the analyst's job: fewer concerns,
  references and conflicting instructions. It is not justified by the byte
  saving alone. If the complexity check shows no reduction for analyst jobs,
  this justification fails and the remaining case is coherence.
- Removing generated reviews changes the public discovery and consumer
  interface, not merely paths. A link to an unreviewed draft, stale selection,
  or unreconciled member is not equivalent to publishing an accepted analysis.

## Check before adoption

The soft boundary is not directly observable and is not one stable number, so
no byte count shows that it was relieved. Check each pressure separately, then
check outcomes in a live run.

**Volume.** Measure the complete mandatory packet for each role before and
after, so that moving text into another always-loaded file cannot count as a
saving. Draft the shortened single contract and measure the same packets with
it. Do not compare the split against the unshortened incumbent alone. The
[input coverage draft](./split-drafts/input-coverage.md) holds both
measurements.

**Interference.** For each clause a worker must read, name the decision in that
worker's output that the clause governs. A clause with no such decision moves
to a type, a role instruction or a coordinator input. Run the same check on
the shortened candidate and count the clauses that address other artifact
classes and cannot be removed. Prefer the split if that count stays above
zero. Do not omit a binding rule to pass this check: confirm that each removed
clause is loaded with binding force by every role that needs it.

**Complexity.** Measure the analyst jobs, not the contract. For each analyst
role (boundary, runtime, memory, epistemic) take the complete mandatory packet
and count, for the incumbent, the shortened candidate and the split:

| Measure | What is counted | Target |
|---|---|---|
| Concerns | Activities other than the role's own analysis that the mandatory input gives rules for: publication, public selection, review authoring, comparison writing, method authoring, migration. | Zero |
| Model-resolved references | References the worker must resolve to act: a rule naming a file the packet does not supply, a path the worker must derive, a definition reachable only by following a link. | Zero |
| Authority conflicts | Pairs of loaded instructions that give different answers, so the worker must choose which governs. The root reading rule against the packet's reading list is one. | Zero |
| Output obligations | Required sections, fields, record kinds, controlled classifications and cross-record constraints in the role's output, each with the consumer it serves. | Record; flag every obligation whose only consumer is publication or comparison |
| Composition depth | For each output obligation, the number of separate files the worker must combine to satisfy it. Report the maximum and the count above two. | Record |

These counts are judgments. Retain the itemized list behind each count, so a
second reader can dispute an item, and apply one counting rule to all three
candidates. Run the same measures on reconcile, verify and synthesis packets
as a secondary result.

The first three measures are what the split can change. The last two describe
the complexity of the analysis task itself, which the split does not change.
Record them anyway: they show where the remaining complexity sits and give the
baseline for simplifying role files. Report the result per role as "before,
after shortening, after split". If the first three measures are equal for
shortening and the split, the split has no measured complexity advantage for
analysts.

**Outcome.** Run one analysis with the reduced inputs and compare it with the
audited runs. Count failed reads of supplied or derived paths, validation
failures before acceptance, refused submissions and retries, and verifier
rejections, alongside coverage and acceptance. Record them per job, with the rule or
obligation each failure concerns, so that failures can be matched to the
complexity measures of that role. Count separately the lapses in which a
worker read a rule and did not apply it. One run cannot attribute a
difference to the contract, so record the result as an observation. The run
needs separate commission. The operator decides whether a trial run with the
draft contract supplied in the packet precedes relocation, or whether the
first run after the split serves as this check. A trial before relocation is a
scoped exception to the root reading rule and must be authorized as one.

If the shortened contract reaches the same concern, reference and conflict
counts for analyst roles as the split, choose shortening. If the split's
counts are lower, state the difference per role in the decision. If sufficiency and
reduction conflict, return the trade-off to the operator before relocation.

Settle current-set/review pins, archive navigation, and sequencing after the
isolation changes are committed. Demonstrate that an accepted analysis is
readable through its report or overview without the generated review; that
comparison consumers can resolve the selected set and provenance; and that
unaccepted work remains unpublished. Check initial publication, replacement,
and interrupted link updates without changing accepted bytes. These are
migration obligations, not evidence against input optimization.

## What closes this proposal

An accepted ADR revising ADR 099 and the affected publication contracts, plus
a completed relocation and publication-by-reference transition; or a recorded
rejection with the chosen alternative for item 1 of the Sol plan.
