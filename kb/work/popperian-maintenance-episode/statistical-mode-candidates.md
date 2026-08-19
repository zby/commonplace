# Modality-mismatch candidates: claims that should be statistical or ideal-type

Started 2026-08-19 to give the statistical mode its worked cases before the three-mode ADR fixes its guard text. The three modes and their refuters: universal (one counterexample), statistical (prevalence evidence), ideal-type (unpriced-ordinary exceptions or dominance failure). Undeclared reads as universal — which is why the corpus is expected to hold both overclaimed universals whose evidence is prevalence-shaped and claims hedged into vacuity to survive universal reading.

## Anchor case (operator-supplied): the soft-degradation note

`kb/notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md` is a compound of both new modes, and its frontmatter shows the tension on its face: the title asserts a universal contrast — "constrained by soft degradation, **not** hard token limits" — while its own description retreats to "not **just** by provider token limits." Two modalities in the same frontmatter block.

**The binding claim is statistical.** "The soft bound is the binding constraint — performance degrades well before the hard limit is reached" is, read universally, refuted by any workload where the hard limit binds first (bulk single-pass ingestion of a document that simply exceeds the window, short tasks far below any degradation region). The claim's actual content is prevalence-shaped: *in typical agent workloads*, the soft bound binds before the hard one — and its cited evidence is exactly prevalence-shaped (benchmark rates, MECW's task-dependence). Under statistical mode, the refuter is a prevalence result: a substantial class of ordinary agent workloads where no measurable degradation precedes the hard limit.

**The mechanism model is ideal-type.** The three-dimension decomposition (volume, complexity, relevance/interference) plus the workspace-saturation hypothesis is a deliberately simple first-order model the note itself declines to assert exactly: "distinguishable but not fully separable," "a hypothesis, not yet a general explanation." Its adequacy record would read: declared use — routing context-engineering decisions (what to exclude, decompose, front-load); omitted mechanism — dimension interactions and model-family variance; dominance condition — the three dimensions should carry most observed degradation; falsifier — a degradation regime with no corresponding workspace effect (already stated in the note), or a fourth independent dimension that carries more of the variance than any of the three.

**Diagnosis.** The note already does modality work informally — hedges, scope concessions, a "working hypothesis" header — but the title must overclaim (universal "not X") because titles have no mode to declare, and the description quietly corrects it ("not just X"). With declared modes, the title claim is statistical and the mechanism section is a declared idealization; nothing about the content needs to weaken.

## Survey results (2026-08-19, one thorough sweep of kb/notes/)

Classes: **A** — universal-stated, statistical-in-substance; **B** — hedged into vacuity; **C** — idealized model without the label. 22 candidates; the tiers rank exemplar quality for first conversions.

### Tier 1 — clearest exemplars for first conversions

1. `task-fitted-structure-costs-cross-task-reuse.md` — **A**. Categorical cost title; the body already wrote the statistical qualifier: "The cost is real but not always decisive… The claim is that this bet is often invisible and rarely revisited, not that it is always wrong." Only the title mode is missing. Refuter (statistical): evidence that task-fitted structure is typically revisited and retired at low cost. *Outcome (run 1, pass s5qz): diagnosis wrong — the pass located the warranted claim in the warrant structure, not the prevalence observation, and reframed to a universal insufficiency claim (now `current-task-fit-alone-does-not-warrant-costly-entrenchment.md`). Lesson: Class A membership flags a mismatch but does not fix the target mode; where the warranted claim lives decides it.*
2. `structure-activates-higher-quality-training-distributions.md` — **A**. Body is entirely prevalence-shaped ("on average", "tends to", 5–12pp benchmark gains) and already carries a survived null (Sonnet code-QA 84.8% vs 85.3%). Refuter: representative sample of tasks/models with no mean lift.
3. `entropy-management-must-scale-with-generation-throughput.md` — **A**. Deontic-universal title; the note names its own gap ("self-selected anecdotes establish a failure mode, not its prevalence or effect size"). Refuter: measured drift rates across high-throughput systems with sub-proportional cleanup.
4. `agent-runtimes-decompose-into-scheduler-context-engine-and-execution.md` — **C**. A textbook ideal-type declaration written as a hedge: "in many real systems the boundaries blur. The claim is that the functions are analytically distinct." Refuter: a runtime where the decomposition mispredicts which limitation a change fixes, or a rival decomposition with better reach.
5. `files-not-database.md` — **A** (or **C**). Universal comparative; concedes a scoped exception whose predicate lives in a sibling note ("past some level of complexity a real database carries that structure better"). Statistical, or ideal-type if the many-to-many-edge predicate is promoted into the note as the declared regime boundary.

### Tier 2 — strong Class A

6. `knowledge-storage-does-not-imply-contextual-activation.md` — prevalence evidence throughout (AppWorld discovery >90%, exploitation <7%; seven hedge markers, the corpus maximum). Refuter: activation tracking storage closely in representative settings.
7. `apparent-success-is-an-unreliable-health-signal-in-framework-owned.md` — "typically/usually/often" carry the claim. Refuter: silent-recovery rate low enough that success stays a usable health proxy.
8. `prose-has-no-dereference-reinforce-facts-at-point-of-use.md` — body explicitly graded ("the further… the lower the chance"); statistical with the form gradient as conditioning variable.
9. `llm-generation-confidence-tracks-typicality-not-soundness.md` — the anti-correlation half rests on "and it often does"; that half is statistical, the decoupling half can stay universal. A note that needs a *mixed* modality declaration.
10. `traditional-debugging-intuitions-break-when-tool-loops-can-recover.md` — "most/usually/often" carry it.
11. `stale-indexes-are-worse-than-no-indexes.md` — universal comparative; both branches probabilistic in the body.
12. `indirection-is-costly-in-llm-instructions.md` — "occasionally gets it wrong"; applicability condition is itself a frequency.

### Tier 3 — Class C (ideal-type without the label)

13. `bounded-context-orchestration-model.md` — self-describes the cost measure as "idealized"; the whole cluster already reasons ideal-typically, calling real systems "degraded variants" of "the clean model." The degraded-variant vocabulary *is* correction-term reasoning, unlabeled. Refuter: a regime where the clean model mispredicts feasibility direction or degradation is unbounded rather than a correction.
14. `access-burden-and-transformation-burden-are-independent-query.md` — "vary independently" posited; its own open question undercuts clean separability. Two-axis first-order model.
15. `storing-llm-outputs-is-constraining.md` — opens with a mode declaration in disguise: "Working hypothesis… not yet an empirical generalization."
16. `agent-memory-needs-discoverable-composable-trusted-knowledge-under.md` — explicitly "first-order… a minimal basis, not an exhaustive ontology."
17. `memory-design-adds-operational-axes-to-artifact-analysis.md` — "mutually independent" axes posit; sibling admits crosscutting.

### Tier 4 — Class B (hedged into vacuity; the ratchet's predicted end state, confirmed in the corpus)

18. `the-framework-is-often-larger-than-the-durable-contribution.md` — "often" in the title, "tends to" twice in the body, no rate or refuter anywhere. Needs a statistical strengthening: what measured ratio would refute.
19. `weakly-discriminated-qualities-tend-to-be-underselected.md` — well-behaved B: names its three enabling conditions but no rate. Good second-wave conversion.
20. `memory-backed-personalization-can-look-like-model-improvement.md` — bare possibility claim; the refutable core ("it cannot make one of several prompt-compatible commissions authoritative without user-specific evidence") is already in paragraph two and could be promoted to the title as a universal.
21. `human-analogies-suggest-functions-not-component-boundaries.md` — stacked modals ("can reveal", "can also lead", "may suggest"); normative core unfalsifiable as stated.
22. `codified-scheduling-patterns-can-turn-tools-into-hidden-schedulers.md` — the hedge does no work; the underlying distinction is sharp enough for a universal restatement.

### Existing house-style templates for mode declaration

`claim-routed-reading-may-beat-reading-first-for-synthesis-notes.md` ("Status: conjecture… a hypothesis with a named test") and `descriptive-link-labels-may-supply-claim-self-sufficiency.md` ("Status: conjecture, partially tested" + a named ablation) already declare non-universal modes informally. The modality field should subsume this idiom rather than coexist with it — status-conjecture is a discovery-lifecycle stage declaration, modality is a claim-form declaration, and the ADR should say how the two compose.

## Readout for the ADR

- Class A is the largest class: the corpus systematically states statistical claims as universals because titles had no mode to declare — the body then absorbs the modality as hedges and scope concessions. Conversion mostly costs a mode declaration, not a rewrite.
- Class B confirms the ratchet's predicted end state empirically: unfalsifiable tendency claims exist in the library now, and two of them (20, 22) should move *up* to universals — the modes cut both ways.
- Class C shows ideal-type reasoning is already native practice (the "clean model / degraded variant" cluster) — the mode formalizes existing vocabulary rather than importing physics.
- Recommended first conversions: #1 (statistical — the qualifier is already written), #4 or #13 (ideal-type — declaration nearly present), #18 (vacuity-repair — the guard's first test from the weak side).
