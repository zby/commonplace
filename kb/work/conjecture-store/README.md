# Conjecture store: migration plan

## Goal

Move Commonplace from a library that retains mostly corroborated theory to a
system whose primary state is a large store of cheap, criticizable conjectures,
with the corroborated theory collection derived from that store as a
projection at a stated threshold. The migration must keep the KB operational
and useful at every stage, because users are onboarded next month on the
current contracts.

Posed by the operator on 2026-10-23, after a research handoff on explanatory
reach, compression and conjectural learning
([research notes](./research-notes.md)). The operator's diagnosis: the theory
collection permits conjectures, but in practice almost everything that enters
it has evidence first, and the scale of weakly supported conjectures a theory
builder needs is not reached. The target architecture the operator named: a
big blob of conjectures with a projection that yields the current set of
corroborated theories within a specified threshold.

## Standing constraints

- **Operational throughout.** Each stage is useful on its own. Nothing
  consumer-facing changes before stage 2, and stage 2 ships only with
  evidence from stage 1.
- **The theory collection keeps its current meaning until stage 2.** It is
  the belief set at the strictest threshold. No existing theory note is
  migrated, relabelled or given a status field.
- **Status is read from location, not from a field**, as elsewhere in the KB
  (content routing; the note schema rejects `status`). Promotion and
  demotion are relocations. Refutation is a move into a `refuted/`
  subdirectory.
- **No conjecture is a premise.** Other artifacts may point to a conjecture;
  none may cite it as a premise or use its terms as settled vocabulary. This
  is the rule already applied to `kb/theory/proposals/`.
- **Retention is cheap; promotion pays the toll.** The store's bar is
  statability and refutability, not support
  ([ad hoc explanation can be rational when error is cheap and local](../../theory/ad-hoc-explanation-can-be-rational-when-error-is-cheap-and-local.md)).

## Starting state (as of 2026-10-23)

Verified in this checkout:

- `kb/theory/COLLECTION.md` permits a note that "states its conjectural
  force", and `kb/theory/proposals/` holds finished theory awaiting
  vocabulary adoption. Neither is the shape of a half-formed conjecture: the
  first meets the theory quality bar and review, the second is for adoption
  state, not doubt.
- `AGENTS.md` sets the bar "write a note when its mechanism is understood";
  first observations go to `kb/log.md`.
- `kb/log.md` holds about twenty `SYNTHESIS`, `ABSTRACTION` and `METHOD`
  entries that are conjectures awaiting more instances. Neither
  `cp-skill-write` nor `cp-skill-connect` reads the log, so a second witness
  can arrive without anyone noticing.
- `kb/reports/cache/connect/` holds 662 cached connect reports, gitignored.
  463 have a non-empty `## Synthesis Opportunities` section and 278 a
  non-empty `## Maintenance Observations` section with about 420 items
  (counted 2026-10-24). The connect-report type says a later triage step may
  promote these into the log or notes; none has run, so they are lost with
  the cache. Note that `rg` skips this directory unless given `--no-ignore`.
- The installed-project scaffold (`src/commonplace/scaffold_manifest.py`)
  ships `kb/notes`, `kb/reference`, `kb/instructions`, `kb/tags`,
  `kb/sources`, `kb/work` and `kb/reports`. There is no theory collection in
  consumer projects, so a conjecture collection is additive there.
- No controlled theory-builder learning run has been performed
  ([testing whether a theory builder learns](../../articles/testing-whether-a-theory-builder-learns.md)).

## Target architecture

Popper's schema is problem, tentative theory, error elimination, new
problem. The store holds all four as data: a problem key on each conjecture,
the conjecture itself, a machine-readable critical record (refuters,
witnesses, criticism rounds), and rivals grouped by problem. "What we
currently believe" is a projection: for each live problem, the conjecture
whose record clears the threshold. The theory collection is that projection
materialized.

The bootstrap trick is that the current theory collection already is the
projection at the strictest threshold. The store starts beside it, empty,
and the threshold is lowered later. Nothing migrates.

**One store holds both kinds of conjecture; the projection sorts them.**
Theory conjectures claim to hold for any system. Design conjectures argue
for a Commonplace design, which is arguing a theory with some variables
bound to our choices, and some of those choices are bare: picked because
something had to be picked, with no theory behind them. The store does not
separate the kinds. Each conjecture declares its bindings in a `choices`
field, and two projections read the same store:

| Projection | Selects | Materializes as |
|---|---|---|
| Theory | empty `choices`, level at or above threshold | `kb/theory/` notes |
| Current design | `choices` all matching live ADRs, level at or above threshold | `kb/reference/` ADRs and design proposals |

A design conjecture's theory content is whatever survives when its bound
choices are quantified out; that content promotes separately, and only when
the generalization is argued. When a bound choice is revised, the conjecture
is moot, not refuted.

**The projection selects; it does not transform.** Decided 2026-10-24 after
the operator required materialized projections that a person can edit in
any editor. A projection that rewrote content would make the theory
collection a derived copy, and an edit to it a write-back problem
([a derived copy of recomputable truth must be checked or absent](../../theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md),
ADR 025). So each conjecture is one file carrying its record, and the
projection decides only where that file lives. The theory collection is
materialized as location, the file a person opens there is the conjecture
itself, and editing its body or appending to its record is ordinary
editing. The projection command is a reconciler: it computes each
conjecture's level from its record, compares with its location, and
proposes moves. Location is then an enforced mark in the KB's sense,
recomputable from the record and checked by validation; a hand-moved file
whose location disagrees with its record is flagged, not accepted.

Three consequences:

- Theory notes and conjecture records converge on one type at stage 2. A
  theory note is a conjecture whose record cleared the threshold; theory
  notes gain the record fields, and the theory contract's prose demands
  apply to any file in that location. This is a larger change to theory
  than the editorial stages make, and it is what makes editing work.
- The design projection does not materialize as ADRs. An ADR records a
  decision event and cites the design conjectures it rests on. Design
  conjectures are read in the store, with a generated index by live binding.
- Editor edits bypass the skills, so trigger sweeps and the reconciler run
  from the recurring heartbeat
  ([recurring task runner](../recurring-task-runner/README.md)) and from
  validation, not only from the write skill.

The cost is one shared type contract for the store and theory, which
forecloses a lighter record for theory notes. Accepted: a theory note
without stated refuters is already a defect by the KB's standards. The KB's placement test already uses this free-variable
reading (`kb/theory/COLLECTION.md`, evidence placement), and the
[decision-lifecycle-evidence](../decision-lifecycle-evidence/README.md)
workshop already treats proposals and ADRs as views of a continuing decision
record; the store gives that view a source.

## Threshold vocabulary (decided at stage 0)

The projection reads an ordered set of levels, computed from the critical
record and never stored:

| Level | Computed from the record |
|---|---|
| `stated` | Written with a problem, at least one refuter and a trigger. |
| `criticized` | At least one recorded criticism round from an independent critic that did not meet a refuter. |
| `witnessed` | At least one witness: an artifact, episode or test outcome that a trigger matched or an author recorded. |
| `corroborated` | Witnesses from two independent sources, at least one criticism round, and no open refuter. Eligible for promotion. |

`refuted` and `moot` are locations (`refuted/`, `moot/`), not levels: a
stated refuter was met, or a bound choice was revised. Both stay retained
because rivals guide discriminating experiments
([competing causal theories](../../theory/competing-causal-theories-can-guide-distinguishing-experiments.md))
and because a moot design conjecture may still carry theory content.

This vocabulary is the one decision that must be fixed now, because the
record fields follow from it and changing them later means a sweep. The
levels may gain finer steps; renaming or reordering them is a sweep.

## Stage 0: additive store, editorial projection

Runs before onboarding. Closes when the store exists, is seeded, and the
write and connect skills check it.

1. **Create the collection** `kb/conjectures/` with `cp-skill-add-collection`,
   using the draft type contract in this workshop
   ([conjecture type](./conjecture.md), [schema](./conjecture.schema.yaml)).
   The type becomes `conjectures/types/conjecture.md`. Subdirectory
   `refuted/`. No tag participation: conjectures stay out of tag heads, and
   the directory listing plus trigger queries are their index.
2. **Seed the store** from its two existing sources: the log's `SYNTHESIS`,
   `ABSTRACTION` and `METHOD` entries, and the `## Synthesis Opportunities`
   and `## Maintenance Observations` sections of the cached connect reports.
   One script (`--no-ignore` for the cache) extracts candidates into a triage
   file keyed by the artifacts each names; a person decides which become
   conjecture records, which become log fixes, and which are dropped. The
   raw pool is hundreds of items, many duplicated across reports of
   neighbouring artifacts, so triage groups by named artifact first. Log
   entries that become conjectures are closed in the log with a pointer. A
   conjecture seeded from a connect report records the report path as its
   first witness source, so the cache stops being the only copy.
3. **Promotion is relocation.** A conjecture that reaches `corroborated`
   and has empty `choices` is moved with `commonplace-relocate` into
   `kb/theory/`, in its own commit, keeping its record; the prose is then
   edited by a person to meet the theory contract. Until stage 2 the moved
   file changes type to `types/note.md`, so the record fields ride as
   additional frontmatter the note schema already permits. A design
   conjecture is not moved: an ADR that adopts it cites it, and the
   conjecture stays in the store. Demotion is the reverse move. No
   automation.
4. **Skills check the store.** `cp-skill-write` and `cp-skill-connect` run
   the open trigger queries against each new artifact and report matches as
   candidate witnesses. This is the only behaviour change, and it is the
   second-witness mechanism the KB lacks today. The matched conjecture's
   record is updated by the author, not the skill.
5. **Review is structural.** Validation checks the schema. The
   type-conformance gate checks only that refuters are refuters, that the
   trigger could match the missing piece, and that rivals share the problem
   key verbatim. Warrant gates do not run on conjectures.

Consumers are untouched. The collection is not in the scaffold yet.

Replanning point: if triage of the raw pool yields fewer than twenty
conjectures with a statable refuter, the sources are producing observations
rather than conjectures, and the plan returns to decision before stage 1.
If it yields more than about two hundred, hand triage does not scale and
stage 0 needs a cheap gate before a person sees a candidate.

## Stage 1: machine-readable record, advisory projection

Runs during onboarding. Closes when a computed belief set has been compared
against the hand-curated theory collection for at least one full cycle.

1. **A command reconciles the projections.** `commonplace-conjectures
   reconcile --level <level>` reads every record, computes its level,
   compares with its location, and reports proposed moves: into
   `kb/theory/` for unbound conjectures at or above the level, into
   `refuted/` or `moot/` when the record or a superseded ADR says so, and
   back out when a theory note's record no longer clears the level. It
   also writes a generated index of design conjectures by live binding.
   The report and index are build-time generated, never committed
   (ADR 025); the moves are proposals a person performs.
   Trigger sweeps and the reconciler run as recurring tasks on the
   heartbeat, so edits made in an editor are matched and checked without an
   agent session.
2. **Theory stays authored.** The generated page is advisory. The test of the
   projection is whether the conjectures it marks `corroborated` are the
   ones a person would promote, and whether the notes it would demote are
   ones a person would doubt.
3. **Discovery writes into the store only.** The pair sampler and the
   candidacy evaluators from the research notes produce conjecture records.
   They never touch theory. Their yield is scored by later uptake: trigger
   hits and promotions, not generator scores.
4. **Criticism rounds become records.** A criticism of a conjecture is a
   dated entry in its record with the critic's identity, the verdict and a
   pointer, so `criticized` can be computed.

Replanning point: if after one cycle the computed set and the curated set
disagree on more than a stated fraction of promotions, the threshold
vocabulary or the record fields are wrong, and stage 2 does not start.

## Stage 2: invert

Runs after stage 1 closes. Closes when consumers can opt in.

1. **Theory becomes the projection output.** Promotion and demotion are
   proposed by the reconciler and acknowledged by a person, then automatic
   for the levels the stage 1 comparison showed to be trustworthy.
   Validation treats location as an enforced mark: a file whose location
   disagrees with its computed level fails.
2. **One type for store and theory.** Theory notes gain the record fields
   (`problem`, `refuters`, `missing`, `trigger`, `witnesses`, `criticism`,
   `choices`); existing notes are backfilled in a sweep, with `refuters`
   written from each note's scope or caveats section. The theory contract
   keeps its prose demands for files in its location.
3. **Ship the collection in the scaffold** and update consumer contracts.
   This is the first point where onboarded users see a change.
4. **Revisit the theory quality bar** in `AGENTS.md`: it becomes a promotion
   bar, with retention governed by the conjecture type.

## Acceptance example: the workflow engine investigation

The five workflow-engine rivals in [candidates](./candidates.md) are kept as
the store's test case, not only as seed content. The investigation ran from
2026-10-03 to 2026-10-21. It mapped the design space, reversed a bare choice
(whether the harness or the workflow process drives), moved into a sibling
repository and back, extracted a library, and adopted a rival on one witness
source. Commonplace will keep investigating this way, so the store must serve
investigations with this shape and these changes of direction.

The store passes when the next such investigation is recorded live: a record
written when each rival is stated, updated when each ADR lands, with the
design projection correct through every reversal. Reconstructing the record
afterwards from the ADRs, as `candidates.md` did, is the failure the store
exists to prevent. The cost of passing is one record edit per ADR, so an ADR
that decides between rivals cites their records in the same commit.

What the example already fits:

- A refuted rival stays, in `refuted/`, because it guides the next test
  (rival 2).
- A rival goes moot when a binding drops, without being refuted (rival 4).
- A design conjecture is adopted below `corroborated`, by ADR citation and
  not by level (rival 5). This is the uncontested-bulk case the design
  projection exists for.
- ADR return points are refuters with triggers, and the reversed bare choice
  appears on both sides of the rivalry, so `## Rivals` can say what decides.

What the example exposes, decided here for stage 0:

1. **Problems get restated.** The problem drifted from "replaceable
   orchestrators" (the 2026-10-03 proposal) to "survives interruption,
   headless launch" (ADR 118). The verbatim rule needs a move for that: a
   restatement edits `problem` on every rival in one commit, Git keeps the
   old sentence, and the type-conformance check catches a partial
   restatement because the rivals no longer agree.
2. **Records get merged.** Twice, two records turned out to be one
   (Treadle's two runners; ADR 118 and the Workjig extraction). A merge
   appends the absorbed record's witnesses and criticism to the survivor,
   dated as they were, names the absorbed claim in the survivor's text, and
   deletes the absorbed file in the same commit. Nothing is rewritten, so
   the append-only record holds. The lifecycle table gains a `Merged` row.
3. **Supersession is a trigger.** When an ADR that adopted a design
   conjecture is superseded, the stage 1 reconciler proposes a relocation:
   to `refuted/` if the superseding ADR met a refuter, to `moot/` if it
   revised a binding. Stage 0 does this by hand at the ADR's commit.
4. **Witnesses live outside the repository.** Treadle's ADRs are witnesses
   and criticism for rival 3. A free-text `source` records them, but trigger
   sweeps see only this repository, so outside witnesses are entered by hand.
   Accepted; the sibling-repository case is also the second project the
   first candidate conjecture asks for.

## What this workshop does not decide

- Whether problems become first-class artifacts. Stage 0 records the problem
  as a field on each conjecture, so problem indexing stays reachable without
  a second home for content.
- The sampler policy and evaluator weights for discovery. These are stage 1
  experiments, scored by uptake.
- How consumer projects without a theory collection name their projection.
  For them `kb/notes/` plays the theory role; the stage 2 contract update
  decides the mapping.

## What closes the workshop

Stage 0 shipped and the stage 1 command specified as a design proposal under
`kb/reference/proposals/` or decided as an ADR. The threshold vocabulary and
the no-premise rule move into the live type contract and collection
contract. The research notes are mined for theory notes or deleted.

## Files

- [conjecture.md](./conjecture.md) — draft stage 0 type contract, written as
  a type spec so it validates where it is headed
- [conjecture.schema.yaml](./conjecture.schema.yaml) — draft schema
- [research-notes.md](./research-notes.md) — synthesis of the research
  handoff that motivated the store: evaluators, samplers, experiments
- [candidates.md](./candidates.md) — conjectures raised while planning,
  written in the draft type's shape; seeded into the store at stage 0. Its
  workflow-engine rivals are the store's acceptance example
- [prior-work-epistack.md](./prior-work-epistack.md) — decisions extracted
  from the deleted 2026-07 epistack framework-additions menu that the store
  reaches again: map versus verdict, no stored credence, independence of
  witnesses, gap versus crux
