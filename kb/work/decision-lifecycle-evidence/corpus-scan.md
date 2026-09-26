# Existing articles and system reviews: decision and evidence records

## Scope and result

Scanned on 2026-09-25 at the operator's request, after opening this workshop.
The question was where the existing corpus describes ADRs or similar ways of
retaining proposals, deliberation, implementation state, and outcome evidence.
This is a reading map of retained analyses, not a new external-system review
or a decision to adopt their mechanisms. Sources were not refreshed.

The lexical sweep covered all six article bodies in `kb/articles/`, all 46
review files in `kb/agentic-systems/reviews/`, and the 30 exact retained results
referenced by those reviews. All 30 result files matched their reviews'
`analysis-result-sha256` at the check. Authored full reviews without that
metadata were searched directly. Relevant passages were then read for the
entries below; this was not a full rereading of every system analysis.

The explicit search for `ADR`, `ADRs`, and `architecture/architectural decision`
found **no occurrences in those article, review, or referenced-result bodies**.
Navigation and collection-contract mentions were excluded. A second search
for decision records, proposals, rationale, approval, experiment logs, and
ledgers found the related mechanisms below. The lexical result does not mean
the reviewed systems lack ADRs: their analyses may simply omit that feature.

An additional lookup in `kb/sources/` and the legacy
`kb/agent-memory-systems/reviews/` found direct ADR and decision-history leads.
Those are separated below; they are not evidence from the newer full-review
corpus. The existing reviews' Commonplace comparison columns were not counted
as evidence that an external system uses ADRs.

## What the self-improvement articles already ask us to retain

| Article | Relevant content | Reading consequence for this workshop |
|---|---|---|
| [Testing Whether a Theory Builder Learns](../../articles/testing-whether-a-theory-builder-learns.md), the seven tests and “Record what people contribute” | Separates retention, use, and causal effect; treats a decision citation as limited use evidence. Asks for human contributions to be recorded as noticing, diagnosis, choice, or acceptance. | A decision record can contribute deliberation and actor evidence, while later use and improvement still require separate observations and comparisons. |
| [Bootstrapping an Autonomous Theory Builder](../../articles/bootstrapping-an-autonomous-theory-builder.md), transfer and return of judgment | Tracks which judgments move to computation or return to people; proposes human decisions per completed, verified improvement as the measure. | Counting ADRs or accepted changes would miss the human work the proposed measure needs. |
| [Which Existing Self-Improving Systems Are Theory Builders](../../articles/which-existing-self-improving-systems-are-theory-builders.md), human-assisted systems and “The next comparisons” | Calls for the proposer's diagnosis beside a change. The Wheelhouse account retains rulings that later become obsolete; the Fluent account separates shaping and review; Exo preserves failure evidence. These accounts have different evidence strengths, and the article does not establish a unified decision-record format. | Preserve reasons and their timing, and keep changed or unsuccessful choices inspectable. Use the system entries as leads, not proof of an implemented ADR lifecycle. |

The other three articles were searched but did not add a comparably specific
recording mechanism under this question. Their omission here is relevance
selection, not a judgment about their wider value.

## Closest mechanisms in the full agentic reviews

### WikiSkill: intervention history survives candidate rejection

The [paper-based exact analysis](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-wikiskill-01/result.md)
describes separate execution traces, wiki explanations, accepted skills,
`PURPOSE.md` rationale, and `skill-impact.md` intervention history
(`OBJ-1`–`OBJ-8`). The impact record carries proposal metadata, target, diff,
score, and acceptance decision. Rejection restores the skill while retaining
wiki and intervention history for later proposals (`RTE-3`–`RTE-6`).

This is the closest described separation of the currently accepted artifact
from the richer record of how it was produced. **Evidence limit:** this is
doc-grounded, with routes marked claimed and implementation uninspected.
Later consumption of `PURPOSE.md` is also uninspected. It does not show an ADR
generated from that history.

The separate [stahl-g WikiSkill implementation analysis](../../reports/retained/agentic-system-analysis/AAS-2026-09-17-wikiskill-stahl-g-01/result.md)
provides a code-grounded comparison. Candidate bytes and a note survive
independently of adoption (`RTE-3`). Export and installation are distinct from
loop completion (`RTE-4`–`RTE-5`). Event history preserves earlier content.
However, inheritance does not copy original raw traces or prior gate history;
some delivery paths omit proposal rationale, and a legacy resume path
substitutes a generic purpose. Retention, transport, and later delivery are
therefore separate things to inspect. These are wired paths, not observed
proof that the retained reasons improve later work.

### Ecdysis: deliberation and outcome records can remain disconnected

The [exact analysis](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-ecdysis-01/result.md)
records a review dialogue and modification specification (`OBJ-3`), round
decisions (`OBJ-5`), and optional checkpoint state (`OBJ-7`, `RTE-9`). The
dialogue contains diagnoses, objections, and disputed edits; rationale is
requested but not enforced within each nested change. The round records
retain scores and acceptance but omit the actual review, edit reasons,
harness identity, and checkpoint links. They are not automatically persisted
or reused as later review history by the trainer.

This is a useful case for testing whether a richer record really connects
deliberation to implementation and outcome, rather than merely storing each
somewhere. The analysis establishes wiring and omissions, not an observed
candidate's successful causal chain.

### EvoOntology: a hypothesis precedes candidate evaluation

The [exact analysis](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-evoontology-01/result.md),
the hypothesis route before `RTE-5` and `RTE-5` itself, describes instructions
to state a limitation, proposed cause, expected change, and possible refuting
evidence. Hypotheses, rejection notes, and evidence references persist.
Publication requires candidate-linked evaluation input and recomputes a gate
over supplied records.

This supplies a reading lead for decision-time expectations and later
evaluation. Its boundary is explicit: instructions afford the causal
reasoning, and arithmetic checks do not establish evaluation provenance,
matched conditions, or the truth of supplied regression judgments.

### Exo: rollback preserves attempt evidence

The [authored full review](../../agentic-systems/reviews/exo.md), “The
self-modification loop” and “The rewind preserves the record of what was
tried,” describes durable rebuild records containing identity, reason,
status, and completion. Sandbox rewind preserves the event log while
restoring filesystem state. This separates recovery of the operative system
from retention of failed attempts. It is a recovery and recording mechanism;
the review does not establish an automatic improvement trigger or measured
benefit from that record.

### AI Agents in Depth: release eligibility and activation differ

The [authored full review](../../agentic-systems/reviews/ai-agent-book.md),
`RTE-5` and “Continual evolution is proposal, selection, retention, and
activation,” distinguishes evidence, diagnosis, candidate checks, release,
activation, and later measurement. Its evidence reaches a wired
candidate-to-canary route and an observed older decision record, while
production activation and executed rollback are absent from the sample.
The review also notes experiment ledgers retaining negative results beside
completed protocol gates. This is a particularly clear example of why
completion, eligibility, deployment, and benefit need different evidence.

### Experiment ledgers: persistence and admission need checking

Two further leads qualify what “we recorded the experiment” means:

- [oh-my-pi's exact analysis](../../reports/retained/agentic-system-analysis/AAS-2026-09-05-oh-my-pi-02/result.md),
  `RTE-8`, `RTE-9`, `RTE-31`, and `RTE-32`: measurements, model-supplied
  disposition, Git consequences, iteration notes, and approved-plan reload
  are separate routes. A logged keep is not automatically a verified gain;
  conflicting submitted metrics can produce warnings rather than rejection.
- [Compound Engineering's full review](../../agentic-systems/reviews/compound-engineering-plugin.md),
  improvement-loop analysis: optimization keeps an experiment log across
  local resumes, but that log lives in gitignored `.context/`. Local
  persistence is not shared retention unless exported.

## Additional ADR and decision-history leads from the legacy corpus

These entries summarize what the older reviews report. They have not been
refreshed or upgraded to full analyses in this scan.

| Lead | Relevant mechanism in the retained review | Important boundary |
|---|---|---|
| [kgai](../../agent-memory-systems/reviews/kgai.md), “Two planes, one log” and “Promotion path” | Immutable decisions carry who/why/when and structural mutations. An append-only log is canonical; a rebuildable graph supplies current structure and decision history, with supersession and as-of replay. | Closest structural precedent for a history plus current views. The review does not establish separate proposed/implemented states or an ADR renderer. Capture enforcement does not enforce code compliance or prove benefit. |
| [Echel](../../agent-memory-systems/reviews/echel.md), product wiki, product graph, and evidence/gates | Explicit `wiki/decisions/ADR-*.md` files coexist with tasks, evidence registry, risks, generated graph, work packets, reviews, and readiness/proof outputs. Registered evidence can block task closure. | The direction reported is authored ADRs and other records into generated views, not ADRs generated from a canonical decision log. Graph and evidence-link checks do not prove semantic adequacy. |
| [llm-context-base](../../agent-memory-systems/reviews/llm-context-base.md), “Promotion path” | Decision records include an `Outcome` section that feeds later decisions. | A simple document-based comparison case. The process is manual or agent-authored, without code-run promotion gates. |
| [Archie](../../agent-memory-systems/reviews/archie.md), “Promotion path” | Work items and session-derived reasoning are promoted manually through Git into documentation, ADRs, scripts, and deployment packages. | A concrete ADR workflow, but no automatic curation loop or demonstrated later outcome evaluation. |

## Questions the scan adds to the workshop

The next focused reading should compare **kgai's canonical history and
rebuildable views**, **Echel's ADR/task/evidence relations**, and **WikiSkill's
retention of rejected interventions**. They address different parts of the
question and should not be treated as one ready-made design.

The examples also sharpen the evaluation cases:

1. Can a chosen but unimplemented decision guide work without appearing in
   the shipped-architecture view?
2. Can a later reader join a proposal's original reasons to its exact change,
   evaluation, and disposition, including rejection?
3. What remains after rollback, workshop closure, export, installation, and
   session resume? Is it merely stored, or also reachable by its next consumer?
4. Can a completed implementation remain explicitly unevaluated, and can a
   completed evaluation retain a negative result?

These are reading-derived questions for design work. No status model,
retention policy, database, or mechanism has been adopted by this scan.
