# Grounds drift reclassification results

**Date:** 2026-07-29

**Status:** maintainer adjudication complete for all 21 rows; no corpus edge, collection contract, catalogue entry, ADR, or durable instruction has changed.

**Protocol:** [grounds drift reclassification protocol](./grounds-drift-reclassification-protocol.md)

**Frozen additions:** [21-row manifest TSV](./grounds-drift-reclassification-manifest.tsv)

**All classification records:** [63-vote TSV](./grounds-drift-reclassification-votes.tsv)

## Result

All 21 live `grounds` tuples added after the 283-row direction-review baseline received three independent exact-choice votes. Every row has a 2/3-or-better exact result: 16 are unanimous (76.2%), five are contested (23.8%), and none is unstable.

The exact results are seven `explained-by`, five `premised-on`, five `extends`, three `evidenced-by`, and one `operates-through`. No classifier selected `see-also`, `connective-prose`, `remove`, `prerequisite-hold`, or a free-form identifier. The maintainer's no-notes→notes-`see-also` policy therefore needs no override in this cohort.

## Exact distribution

| exact result | rows | unanimous | contested | authorization impact |
|---|---:|---:|---:|---|
| `explained-by` | 7 | 4 | 3 | `candidate-new` ×7 |
| `premised-on` | 5 | 3 | 2 | `candidate-new` ×5 |
| `extends` | 5 | 5 | 0 | `authorized` ×5 |
| `evidenced-by` | 3 | 3 | 0 | `authorized` ×3 |
| `operates-through` | 1 | 1 | 0 | `candidate-new` ×1 |
| **total** | **21** | **16** | **5** |  |

## Rebaseline and execution check

A syntax-aware scan found 292 current live `grounds` tuples:

- 271 of the 283 direction-review baseline tuples survive;
- 12 baseline tuples disappeared: five premise rows, three extension/specialization rows, two mechanism rows, and two evidence rows;
- 21 tuples are additions, frozen in this run.

The 21 additions are unique notes→notes tuples. Each resolved exactly once at its recorded line before dispatch and again after the run. All 63 required records parse, and no tuple disappeared or moved.

The broader current legacy-label surface is 374 tuples: 82 active `mechanism` plus 292 active `grounds`. Prior maintainer decisions covered 353 of them; acceptance of all 21 exact-majority results here completes the current disposition ledger:

| exact disposition | current rows |
|---|---:|
| `premised-on` | 168 |
| `explained-by` | 73 |
| `extends` | 34 |
| `operates-through` | 33 |
| `exemplifies` | 21 |
| `defined-in` | 15 |
| `evidenced-by` | 11 |
| `is-evidence-for` | 10 |
| remove | 5 |
| `contrasts` | 2 |
| `rests-on` | 1 |
| `prerequisite-hold` | 1 |
| **total** | **374** |

The prerequisite hold remains outside label migration pending the `enables` / `precondition` family review. The five removal dispositions preserve tuple accounting but produce no successor edge.

## Authorization readout

With the semantic recommendation accepted, the implementation packet needs:

- catalogue and notes-contract registration of `premised-on` for 168 notes→notes tuples;
- catalogue and notes-contract registration of `explained-by` for 73 notes→notes tuples;
- catalogue and notes-contract registration of `operates-through` for 33 notes→notes tuples;
- a notes→notes pairing decision for `is-evidence-for`, now demonstrated by three current tuples.

The other exact dispositions use already-authorized pairings. The sole reference→notes row remains the previously accepted `rests-on` case. No notes→notes `see-also` authorization is needed, and the five weak edges are removed instead.

These are authorization consequences, not authorizations. They belong in the later catalogue, contract, ADR, and migration packet after semantic adjudication closes.

## Per-row classification ledger

Votes are `choice/confidence`. A 2/3 result remains an adjudication recommendation rather than an automatic disposition. Full reader needs, revision consequences, boundary tests, authorization records, and justifications are retained in the vote TSV.

| ID | source → target | A | B | C | exact result | status | auth |
|---|---|---|---|---|---|---|---|
| G001 | `kb/notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md:49 → kb/notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md` | `premised-on/high` | `evidenced-by/medium` | `premised-on/medium` | `premised-on` | **contested** | `candidate-new` |
| G002 | `kb/notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md:50 → kb/notes/self-improvement-is-relative-to-a-declared-objective.md` | `premised-on/medium` | `premised-on/medium` | `premised-on/medium` | `premised-on` | unanimous | `candidate-new` |
| G003 | `kb/notes/the-bitter-lesson-selects-production-methods-not-representational.md:72 → kb/notes/oracle-accumulation-improves-the-selection-environment.md` | `operates-through/high` | `explained-by/medium` | `explained-by/medium` | `explained-by` | **contested** | `candidate-new` |
| G004 | `kb/notes/the-meta-harness-ablation-bounds-summarization-not-theory-formation.md:44 → kb/notes/diagnostic-richness-constrains-outer-loop-learning-quality.md` | `extends/high` | `extends/high` | `extends/high` | `extends` | unanimous | `authorized` |
| G005 | `kb/notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md:48 → kb/notes/oracle-accumulation-improves-the-selection-environment.md` | `operates-through/high` | `operates-through/high` | `operates-through/high` | `operates-through` | unanimous | `candidate-new` |
| G006 | `kb/notes/a-goal-holding-interpreter-fails-soft-workarounds-tax-a-bounded-budget.md:46 → kb/notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md` | `explained-by/high` | `explained-by/high` | `explained-by/high` | `explained-by` | unanimous | `candidate-new` |
| G007 | `kb/notes/the-bitter-lesson-selects-production-methods-not-representational.md:68 → kb/notes/bitter-lesson-selects-against-unearned-reach-not-against-structure.md` | `explained-by/high` | `explained-by/medium` | `explained-by/high` | `explained-by` | unanimous | `candidate-new` |
| G008 | `kb/notes/a-goal-holding-interpreter-fails-soft-workarounds-tax-a-bounded-budget.md:44 → kb/notes/agentic-systems-interpret-underspecified-instructions.md` | `premised-on/medium` | `explained-by/medium` | `explained-by/high` | `explained-by` | **contested** | `candidate-new` |
| G009 | `kb/notes/constraining-and-extraction-both-trade-generality-for-reliability.md:40 → kb/notes/exact-implementation-does-not-validate-a-requirement.md` | `premised-on/high` | `premised-on/high` | `premised-on/medium` | `premised-on` | unanimous | `candidate-new` |
| G010 | `kb/notes/only-derivation-and-inheritance-warrant-a-scope-claim-use-earns-it.md:69 → kb/notes/definitions/representational-form.md` | `evidenced-by/high` | `evidenced-by/high` | `evidenced-by/high` | `evidenced-by` | unanimous | `authorized` |
| G011 | `kb/notes/a-proximate-target-is-checked-for-achievement-not-for-warrant.md:68 → kb/notes/exact-implementation-does-not-validate-a-requirement.md` | `extends/high` | `extends/high` | `extends/high` | `extends` | unanimous | `authorized` |
| G012 | `kb/notes/only-derivation-and-inheritance-warrant-a-scope-claim-use-earns-it.md:66 → kb/notes/bitter-lesson-selects-against-unearned-reach-not-against-structure.md` | `extends/high` | `extends/high` | `extends/high` | `extends` | unanimous | `authorized` |
| G013 | `kb/notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md:46 → kb/notes/bitter-lesson-selects-against-unearned-reach-not-against-structure.md` | `extends/high` | `extends/high` | `extends/high` | `extends` | unanimous | `authorized` |
| G014 | `kb/notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md:51 → kb/notes/warranted-autonomy-is-bounded-by-oracle-domain.md` | `premised-on/medium` | `explained-by/medium` | `premised-on/medium` | `premised-on` | **contested** | `candidate-new` |
| G015 | `kb/notes/the-bitter-lesson-selects-production-methods-not-representational.md:74 → kb/notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md` | `explained-by/high` | `explained-by/high` | `explained-by/high` | `explained-by` | unanimous | `candidate-new` |
| G016 | `kb/notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md:82 → kb/notes/exact-implementation-does-not-validate-a-requirement.md` | `premised-on/high` | `premised-on/high` | `premised-on/high` | `premised-on` | unanimous | `candidate-new` |
| G017 | `kb/notes/the-bitter-lesson-selects-production-methods-not-representational.md:71 → kb/notes/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md` | `explained-by/high` | `explained-by/high` | `extends/high` | `explained-by` | **contested** | `candidate-new` |
| G018 | `kb/notes/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md:50 → kb/notes/bitter-lesson-selects-against-unearned-reach-not-against-structure.md` | `extends/high` | `extends/high` | `extends/high` | `extends` | unanimous | `authorized` |
| G019 | `kb/notes/only-derivation-and-inheritance-warrant-a-scope-claim-use-earns-it.md:70 → kb/notes/definitions/reflective-system.md` | `evidenced-by/high` | `evidenced-by/high` | `evidenced-by/high` | `evidenced-by` | unanimous | `authorized` |
| G020 | `kb/notes/bitter-lesson-selects-against-unearned-reach-not-against-structure.md:53 → kb/notes/exact-implementation-does-not-validate-a-requirement.md` | `explained-by/high` | `explained-by/high` | `explained-by/high` | `explained-by` | unanimous | `candidate-new` |
| G021 | `kb/notes/the-bitter-lesson-selects-production-methods-not-representational.md:75 → kb/notes/the-meta-harness-ablation-bounds-summarization-not-theory-formation.md` | `evidenced-by/high` | `evidenced-by/high` | `evidenced-by/high` | `evidenced-by` | unanimous | `authorized` |

## Non-unanimous diagnostics

The five contested rows are repeated with all minority and majority justifications. Their full decision records remain in the vote TSV.

### G001 — premised-on (contested)

`kb/notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md:49 → kb/notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md`

- A — `premised-on/high`: The source argues that reflective machinery cannot be exempt by position and cites the symbolic layer as revisable content; the target concludes that schedulers, schemas, and invariants are learned and rewritten through codification even though symbolic execution remains separate.
- B — `evidenced-by/medium`: The source claims all loop machinery is revisable and must earn persistence; the target independently shows symbolic scheduling is justified yet non-static, with operational evidence moving constraints into validator code and codification revising the layer
- C — `premised-on/medium`: The source argues that reflective machinery is in loop scope and cites the symbolic layer as a learning target; the target argues for scheduler separation and concludes that this symbolic layer is revisable through codification

### G003 — explained-by (contested)

`kb/notes/the-bitter-lesson-selects-production-methods-not-representational.md:72 → kb/notes/oracle-accumulation-improves-the-selection-environment.md`

- A — `operates-through/high`: The source names accumulated evaluation checks as one discrete substitute for credit assignment in learned localized forms; the target describes the process that retains failure-derived checks and applies them exhaustively to later in-scope candidates, with explicit domain and maintenance limits.
- B — `explained-by/medium`: The source argues mixed deployments can retain localized forms and names accumulated evaluations among missing-loop fragments; the target explains lesson-versus-check channels, exhaustive enforcement, domain-limited reuse, and costs that produce and bound that advantage
- C — `explained-by/medium`: The source needs a reason localized state can contribute cumulatively to its proposed learning loop; the target explains that codified checks run exhaustively, prevent recurrent failures, and improve the selection environment within a maintained domain

### G008 — explained-by (contested)

`kb/notes/a-goal-holding-interpreter-fails-soft-workarounds-tax-a-bounded-budget.md:44 → kb/notes/agentic-systems-interpret-underspecified-instructions.md`

- A — `premised-on/medium`: The source's soft-failure argument requires an interpreter to derive another route from a retained goal; the target establishes the underlying one-to-many spec-to-program space and distinguishes that semantic freedom from execution noise.
- B — `explained-by/medium`: The target models natural-language execution as projection from a plural interpretation space; the source uses that same interpretive freedom to explain both deviation from intent and resilient rerouting after blockage.
- C — `explained-by/high`: The target models an instruction as admitting multiple valid programs selected at runtime; the source combines that interpretive plurality with a retained goal to explain re-derivation, workarounds, and soft blockage failure.

### G014 — premised-on (contested)

`kb/notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md:51 → kb/notes/warranted-autonomy-is-bounded-by-oracle-domain.md`

- A — `premised-on/medium`: The source replaces a frozen external meta-method with governance and an adoption decision outside the judged artifact; the target supplies the needed premise that unattended acceptance is warranted only within an oracle's domain and otherwise needs a human or narrower gate.
- B — `explained-by/medium`: The source replaces a frozen fixed point with adoption outside the judged text and independent checks; the target explains that bare autonomous gating is unwarranted beyond the domain its oracles can assess.
- C — `premised-on/medium`: The source assigns governance and an adoption decision outside the text being judged as the substitute for a frozen meta-method; the target establishes that unattended acceptance is warranted only where an oracle can discriminate adequately and otherwise retains a human gate.

### G017 — explained-by (contested)

`kb/notes/the-bitter-lesson-selects-production-methods-not-representational.md:71 → kb/notes/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md`

- A — `explained-by/high`: The source argues that current absorption at fixed difficulty does not collapse the form axis; the target explains this by separating yesterday's task from a harder frontier where horizon, complexity, and reliability demands can recreate an advantage for external structure.
- B — `explained-by/high`: The source rejects weights monism while conceding fixed-difficulty absorption; the target explains the coexistence by separating yesterday's task from the moving deployment frontier and states saturation and full absorption as explicit failure conditions
- C — `extends/high`: The target distinguishes absorption on fixed tasks from conditional recurrence when task difficulty and external reliability value keep moving; the source carries that distinction into its claim that scaling has not collapsed the form axis into weights

## Recorded maintainer decision

On 2026-07-29 the maintainer accepted all 21 exact-majority dispositions as written. There are no unstable rows to synthesize, no weak-adjacency links to preserve, and no new identifier beyond the three already accepted or pending registrations.

The five contested boundaries remain visible rather than being disguised as unanimity:

- `G001`: `premised-on` beats `evidenced-by` because the source imports the target's scheduler-as-revisable-machinery conclusion as support for its no-outside claim.
- `G003`: `explained-by` beats `operates-through` because the source invokes check accumulation inside a proposed, not implemented, localized learning loop.
- `G008`: `explained-by` beats `premised-on` because the target supplies the one-to-many interpretation mechanism that produces alternate routes.
- `G014`: `premised-on` beats `explained-by` because oracle-domain limits constrain when adoption may be unattended but do not explain the source's no-outside geometry.
- `G017`: `explained-by` beats `extends` because the moving-frontier account explains why fixed-difficulty scaffold absorption does not collapse the source's representational-form axis.

This acceptance settles semantic disposition only. It does not authorize contract changes or corpus mutation; those remain separate approval gates.
