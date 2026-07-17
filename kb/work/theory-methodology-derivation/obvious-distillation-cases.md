# Obvious distillation cases

First staging pass for the library-side `distill*` migration. Corpus: `kb/notes/**/*.md` and `kb/reference/**/*.md`, excluding sources and generated reports. Sweep result on this branch: 110 files, 377 matching lines.

This is not a full classification table. Its job is to find the notes where the control regime is already obvious enough to schedule an early wave, and to mark the notes that should not be touched by a quick rewrite.

## Rule for the first pass

An "obvious" case is one where the replacement term follows from the note's own argument without needing the promoted definition notes in hand:

- **Discovery / abstraction** when a trace, episode, accepted edit, or repeated behavior becomes a reusable rule.
- **Derivation / selection** when already-recorded reasoning is reshaped into a task-facing artifact without adding a new substantive claim.
- **META / infrastructure** when the occurrence is a tag, definition page, link label, filename, or navigation surface.

Mixed cases stay out of the first pass even if one sentence looks easy.

## First semantic wave: obvious discovery / abstraction

These should be fixed before the broad derivation rename because they are the original mistake: using `distillation` for evidence-to-rule generalization.

Status: applied to the six semantic notes and the linked `agent-memory-README.md` summary. The `distillation` tag on `an-accepted-edit-verifies-the-change-not-the-rule.md` and old vocabulary in linked filenames remain deferred to the META/infrastructure wave.

| Note | Current usage | Replacement direction |
|---|---|---|
| `trace-extracted-memory-earns-authority-per-operation-not-at-capture.md` | `Distill` rung generalizes a verified fact into a rule | Rename the rung to abstraction / discovery-stage generalization; keep the per-operation authority theory |
| `an-outcome-check-licenses-replay-a-rule-needs-the-process-verified.md` | "distilling a rule" transfers a mechanism to new contexts | Reword as abstracting/generalizing a rule; the control regime is process evidence plus boundary/testing, not derivation |
| `an-accepted-edit-verifies-the-change-not-the-rule.md` | accepted edit verifies instance, rule extraction sits at the `distill` rung | Reword as rule extraction / conjecture; likely migrate the `distillation` tag to `discovery` after tag infrastructure is ready |
| `abstract-an-experience-only-when-you-can-state-the-boundary.md` | already argues about abstraction but cites `distillation` as the trace-to-rule mechanism | Replace `distill` language with abstraction / discovery lifecycle; preserve the boundary-statability oracle |
| `spec-mining-as-codification.md` | system "distills stochastic regularities into deterministic code" | Reword to mine/extract discovered regularities, then codify them |
| `research/adaptation-agentic-ai-analysis.md` | `Distill` when signal carries reusable judgment but not exact procedure | Split: reusable judgment from traces is discovery/abstraction; exact procedure can later be derived or codified |

Small linked surface to update with this cluster:

- `agent-memory-README.md` - its "verification, distillation, and consultation" summary should follow the renamed trace ladder.

Residues found while checking the applied wave (2026-07-17): sweeps grep `distill` and miss the single-l spelling — `a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md` had "verify, distil, consult" (fixed to "verify, abstract, consult" with the ladder rename); `claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md:30` still says AWM "distils successful traces into workflow prose" — trace→rule AMP usage, add to the Wave 1/2 list and use `distil` (single-l) in future sweep patterns.

## Second semantic wave: obvious derivation / selection

These are not the mistake. They are mostly use-shaped rewrites of existing reasoning, procedures, or traces for a bounded consumer. They should wait until the derivation/selection definitions exist, but they can be batched because the control regime is clear.

| Note | Current usage | Replacement direction |
|---|---|---|
| `skills-derive-from-methodology-through-distillation.md` | methodology -> skill in same medium | Retitle around derivation; preserve source-retention, residue, and edge-case fallback as derivation/cache semantics |
| `skills-are-instructions-plus-routing-and-execution-policy.md` | skills/instructions are distilled procedures | Split stable-core discovery from derived procedure body where needed; most references become derivation/proceduralization |
| `distillation-status-determines-directory-placement.md` | procedures distilled for execution belong in `kb/instructions/` | Reframe directory boundary as execution-shaped procedural derivation |
| `maintenance-operations-catalogue-should-stage-distillation-into.md` | stable manual operations are distilled into instructions | Reframe as staging until stable, then deriving an execution procedure |
| `ad-hoc-prompts-extend-the-system-without-schema-changes.md` | repeated prompts become skills through distillation | Reframe as discovery of a stable procedure, then derivation of the reusable skill |
| `capability-placement-should-follow-autonomy-readiness.md` | stable procedures are distilled into instructions/skills | Reframe as promotion plus derivation into the appropriate execution surface |
| `agents-md-should-be-organized-as-a-control-plane.md` | stable procedures are distilled into instructions/skills | Same as capability placement: promotion plus derivation |
| `scenario-decomposition-drives-architecture.md` | operational instructions distilled from deeper methodology | Reframe as derived procedures with explicit fallback to methodology |
| `session-history-should-not-be-the-default-next-context.md` | execution-boundary compression targeted to next stage | Reframe as selection plus derived handoff artifact; preserve "store more than you load" |
| `conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md` | prompt refinement is distillation of caller knowledge | Reframe as deriving a focused handoff prompt from caller context and target task |
| `bounded-context-orchestration-model.md` | compaction of scheduler state | Reframe as selection plus derivation for the orchestrator's context budget |
| `decomposition-heuristics-for-bounded-context-scheduling.md` | saved intermediates are often distillations | Reframe as derived intermediate artifacts shaped for later reuse |
| `llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md` | compaction applied to scheduler conversation state | Reframe as derived compaction / handoff artifact |
| `feasibility-is-the-heaviest-forks-net-load.md` | parent absorbs work and hands down a leaner task | Reframe as frontloaded selection/derivation for sub-agent feasibility |
| `pointer-design-tradeoffs-in-progressive-disclosure.md` | pointers and abstracts are distillations | Reframe as derived pointers / precomputed selection aids |
| `charting-the-knowledge-access-problem-beyond-rag.md` | TOCs, abstracts, overviews as navigation distillates | Reframe as derived navigation views for read/skip decisions; keep synthesis cases separate |
| `epiplexity-by-example-what-entropy-and-complexity-miss.md` | distillation raises extractable structure for a bounded observer | Reframe as observer-shaped derivation/selection unless the note needs the external ML term |
| `reverse-compression-is-when-llm-output-expands-without-adding.md` | distillation as productive compression preserving structure | Reframe as derivation or structure-preserving compression |
| `../reference/where-change-candidates-come-from-in-commonplace.md` | `cp-skill-ingest` folds connect findings into a durable ingest report | Reframe as selecting/folding discovered candidates into the report; likely derivation where the report preserves the findings |
| `../reference/design-rationale-management.md` | a design constraint can motivate extracting a use-shaped artifact from larger material | Reframe as selection plus derivation, unless the artifact adds a new design commitment |
| `../reference/proposals/factored-dependency-pairs-for-review-freshness.md` | source-as-gate checks consistency with the source snapshot a note distills | Reframe as source-derived consistency / derivation-gate language |

## META and infrastructure: defer

These are obvious, but they belong to the infrastructure wave, not the first semantic wave:

- `distillation-README.md`, `learning-theory-README.md`, `tags-README.md`, `README.md`, tag fields, and `covered_by` fields.
- `definitions/distillation.md` and cross-definition references in `definitions/constraining.md`, `definitions/codification.md`, `definitions/context-engineering.md`, `definitions/directed-reading.md`, `definitions/text-contract.md`.
- `Distilled into:` footer labels and backlink grammar.
- Filenames containing `distill*`.
- Link-only references where the target note is itself being renamed.
- Reference infrastructure and history: `../reference/link-vocabulary.md`, ADR 011's inline-gloss decision, ADR 005's historical "notes distill from which" comment, ADR 020's catalogue-sync wording, ADR 021's path-audit examples and old filename discussion, and `../reference/tag-readme-trace-observed-causal-connection.md`'s historical mention of `distillation-README.md`.

These should move after the semantic notes settle, otherwise generated navigation and backlinks will hide unresolved vocabulary decisions.

## Deliberately not first-wave

These notes have `distill*` uses that are semantically important or mixed enough to need the promoted receiving vocabulary before editing:

- `distillation-is-transformation-not-selection.md` - pivotal mixed note; its anti-selection argument survives, but its trace-to-rule evidence routes to discovery.
- `constraining-and-distillation-both-trade-generality-for-reliability.md` - foundational tradeoff note; likely needs a rewrite around derivation/selection rather than local substitutions.
- `distilled-artifacts-need-source-tracking.md` - lineage argument still matters, but "distilled artifact" is broader than the new derivation term unless the scope is restated.
- `a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md` - already partially migrated; should be aligned only after the source-tracking note is rewritten.
- `evolving-understanding-needs-re-distillation-not-composition.md` - holistic rewrite can be derivation, synthesis, or authored judgment depending on what the narrative adds.
- `memory-management-policy-is-learnable-but-oracle-dependent.md` - explicitly contrasts selection and distillation; must be reinterpreted under the new split, not patched.
- `minimum-viable-vocabulary-is-the-naming-set-that-most-reduces.md` and `information-value-is-observer-relative.md` - information-theoretic framing may need selection/derivation/discovery all at once.
- `legal-drafting-solves-the-same-problem-as-context-engineering.md` and `soft-bound-traditions-as-sources-for-context-engineering-strategies.md` - external analogies; preserve loose analogical force until the internal terms settle.
- `task-fitted-structure-costs-cross-task-reuse.md` - uses distillation as a contrast case; only safe after the tradeoff note is rewritten.
- `semantic-review-catches-content-errors-that-structural-validation.md` - discusses the old three-operation framework as a discovered error; may need historical wording rather than replacement.
- `../reference/proposals/automated-note-refinement-as-search-over-source-bundle.md` - explicitly asks whether automated refinement subsumes re-distillation; hold until the `evolving-understanding` note and source-bundle proposal can share the new vocabulary.

## Proposed execution order

1. Promote Wave 0 vocabulary: derivation, selection, and discovery lifecycle.
2. Apply the first semantic wave: the obvious discovery / abstraction cluster.
3. Apply the second semantic wave: the obvious derivation / selection cluster.
4. Revisit the deliberately-not-first-wave notes with the new definitions available.
5. Only then do META, tags, filenames, and `Distilled into:` infrastructure.
