# evidenced-by audit — batch 05 (34 source ingests)

Every file in this batch is a `kb/sources/*.ingest.md` report. Only **3** lines are labelled edges, all inside the reports' "Connections Found" lists. The other occurrences are **recommendations** that tell a later author to add an `evidenced-by` edge from a note to the source. These are not edges yet, although 8 of them already exist in the target note. I audited them anyway because they will shape the edges that authors write. A recommendation's context phrase is the framing the recommendation gives.

Structural finding: `kb/sources/COLLECTION.md` does not authorize `evidenced-by`. Its note-bound labels are `is-evidence-for`, `abstracted-from`, `rests-on`, `compares-with`, `defined-in` and `see-also`. All three labelled edges therefore carry a label the sources collection does not allow, whatever their phrases say.

## Counts

| class | labelled edges | recommended edges | total |
|---|---|---|---|
| CORROB-OK | 0 | 0 | 0 |
| QUALIFY | 0 | 21 | 21 |
| CORROB-UNTESTED | 0 | 7 | 7 |
| ORIGIN | 0 (1 flagged secondarily) | 4 | 4 |
| MISLABEL | 3 | 1 | 4 |
| **total** | **3** | **33** | **36** |

Prose mentions that are neither edges nor edge recommendations: 3 (`a-harness-for-every-task-dynamic-workflows.ingest.md:33`, `borretti-human-routers-of-machine-words.ingest.md:47`, `where-it-lives-retained-adaptation-2026-06-23.ingest.md:35`; the last one correctly warns against citing a self-authored draft as independent `evidenced-by` from the notes it came from).

## Non-QUALIFY edges

### Labelled edges (existing)

| source file:line | target | class | reason | proposed fix |
|---|---|---|---|---|
| kb/sources/agentic-code-reasoning.ingest.md:44 | notes/structured-prompt-gains-do-not-establish-distribution-selection.md | MISLABEL (+ORIGIN) | `evidenced-by` is not a sources-collection label. The phrase says the paper "supplies the note's central contrast", so the note was built from it; the note's own footer edge back to this ingest (`evidenced-by: records the code-verification gains…`) should be `abstracted-from`. | `(is-evidence-for): supplies the case the note generalizes from — 5–12 pp template gains on code verification alongside the Claude Sonnet code-QA null (84.8% vs 85.3%); the bundled intervention does not isolate the mechanism.` Also change the note's footer label to `abstracted-from`. |
| kb/sources/language-models-like-humans-show-content-effects-on-reasoning.ingest.md:48 | notes/structured-prompt-gains-do-not-establish-distribution-selection.md | MISLABEL | The label is not allowed in sources. The phrase is already bounding ("does not distinguish…", "bounds those experiments"). | Change the label only: `— is-evidence-for: <existing phrase unchanged>` |
| kb/sources/prompt-stability-code-llms-emotion-personality-variations.ingest.md:64 | notes/structured-prompt-gains-do-not-establish-distribution-selection.md | MISLABEL | The label is not allowed in sources. The phrase is illustrative ("another case…"). The note's footer does not cite this ingest, so the edge is one-sided. | `— **is-evidence-for**: <existing phrase unchanged>` |

### Recommended edges (instructions to authors)

| source file:line | target | class | reason | proposed fix |
|---|---|---|---|---|
| kb/sources/a-harness-for-every-task-dynamic-workflows.ingest.md:69,73 | notes/rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md; notes/orchestration-strategies-and-run-state-have-opposite-persistence.md (not yet authored) | CORROB-UNTESTED | The report tells authors to frame the edges as "corroborating practitioner testimony". A shipped instance shows that the pattern exists; it is not a test the claims could have failed. | Replace "framed as corroborating practitioner testimony" with "framed as an existence instance: `evidenced-by: a shipped first-party system that has the model write ephemeral orchestrators; shows existence only, not effectiveness`" |
| kb/sources/foundation-and-history-of-the-pdsa-cycle.ingest.md:45 | notes/definitions/discovery-lifecycle.md (not yet authored) | CORROB-UNTESTED | The report calls the edge "corroborating the conjecture-consequence-test core … first independent, applied support". A historical account of a parallel cycle does not test a definition. | `evidenced-by: an industrial conjecture-test cycle developed independently of the Peirce lineage; a parallel instance, not a test of the definition` |
| kb/sources/effective-harnesses-for-long-running-agents.ingest.md:59 | notes/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md (not yet authored) | CORROB-UNTESTED | The report says "practitioner evidence that a frontier model … still required" scaffolding but names no risk. The report could serve as a weak test, because a frontier model finishing long-horizon work without scaffolding would have counted against the claim. | `evidenced-by: risked a frontier model completing a longer-horizon build without explicit work state, decomposition, or end-to-end verification; uncontrolled practitioner report, produced independently of the note` |
| kb/sources/from-human-memory-to-ai-memory-survey-llm-memory-mechanisms.ingest.md:30,52 | notes/three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy.md (not yet authored) | CORROB-UNTESTED | The report calls the survey "support for its 'decorative analogy' hedge". The survey is a taxonomy, not a test. | `evidenced-by: a second, paper-grade human-to-agent taxonomy mapping whose quadrants reduce to object/form/time policy dimensions; illustrates the decorative-analogy hedge, not a test of it` |
| kb/sources/in-toto-farm-to-table-guarantees.ingest.md:37,58 | notes/the-boundary-of-automation-is-the-boundary-of-verification.md (already authored, with an instance phrase) | CORROB-UNTESTED | The report calls in-toto "a fourth corroborating source" and "cross-domain corroboration" in a convergence argument. One confirming instance does not test the claim, which would have been at risk only from automation succeeding where verification is expensive. The authored note phrase is neutral and can stay. | Ingest wording: "adds in-toto as a fourth cross-domain instance (automation followed cheap verification); it does not test the converse". The note edge phrase can stay. |
| kb/sources/llm-agents-are-not-always-faithful-self-evolvers.ingest.md:44,62 | notes/agent-memory-requirements/evaluate-memory-by-effects.md; notes/agent-memory-requirements/activate-behavior-changing-memory.md (not yet authored) | CORROB-UNTESTED | The report says "direct support for 'evaluate by effects'" and "central empirical anchor … reconfirms". The first target is a prescription and the paper exemplifies its WITH/WITHOUT method. If the activation note's Behavioral Faithfulness section was written from the paper, that edge is origin. | evaluate-memory-by-effects: `evidenced-by: exemplifies the WITH/WITHOUT effect test on self-evolving agents; shows that stored experience can go unused`. activate-behavior-changing-memory: `abstracted-from` if the section was written from the paper; otherwise `evidenced-by: condensed experience in context left behaviour largely unchanged` |
| kb/sources/llm-agents-are-not-always-faithful-self-evolvers.ingest.md:44,62 | notes/knowledge-storage-does-not-imply-contextual-activation.md (already authored: "causal perturbations show stronger behavioral dependence…") | CORROB-UNTESTED | This paper does report a test: causal perturbation of condensed experience could have shown that the agents used it. The authored phrase does not say what the claim risked or that the evidence was independent. | `evidenced-by: risked agents depending on condensed experience placed in context; causal perturbations across frameworks and backbones found weaker dependence than on raw trajectories; an independent study` |
| kb/sources/borretti-human-routers-of-machine-words.ingest.md:51,70 | new synthesis note: "delegating prose skips concretization" (not yet written) | ORIGIN | The proposed note is to be written from this polemic and the Weizenbaum quote, citing them as `derived-from`/`evidenced-by`. | `abstracted-from` for both (the synthesis claim goes beyond them). Do not use `evidenced-by`. |
| kb/sources/position-bias.ingest.md:76 | new note "Pairwise LLM judges flip ~45%…" (not yet written) | ORIGIN | The note's numeric priors would come from this benchmark. | Cite this ingest as `abstracted-from` (or `derived-from` if the note only restates the numbers). The seven reverse edges from seedlings are illustrative and QUALIFY. |
| kb/sources/self-revising-discovery-systems-agentic-ai.ingest.md:52 | new note on retrieval/search/discovery as distinct operations (not yet written) | ORIGIN | The note would be "framed around" this paper's schema-change mechanism. | `abstracted-from` |
| kb/sources/the-vision-of-autonomic-computing.ingest.md:50 | notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md (not yet authored) | ORIGIN | The report cites Kephart & Chess "as the origin of the MAPE-K reference-model tradition the note already invokes". That is lineage, not evidence. | `abstracted-from: the MAPE-K reference model the loop decomposition descends from (via Weyns and Petrovska)` |
| kb/sources/prov-overview.ingest.md:35,47 | notes/definitions/lineage.md (not yet authored) | MISLABEL | PROV is the standard that the definition's "deliberately narrower than full provenance" contrast refers to. It is a reference point, not an observation. | `see-also: W3C PROV, the full-provenance standard this definition deliberately narrows` |

## QUALIFY (recommended edges; fine as framed)

- kb/sources/agent-optimizers-compound-terminal-bench.ingest.md:55 → notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md (authored)
- kb/sources/borretti-human-routers-of-machine-words.ingest.md:43 → notes/reverse-compression-is-when-llm-output-expands-without-adding.md, notes/vibe-noting.md (illustrative reverse edges)
- kb/sources/can-ai-agents-conduct-open-ended-ai-research.ingest.md:67 → notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md
- kb/sources/circling-back-clearing-up-myths-about-the-deming-cycle.ingest.md:47 → notes/definitions/discovery-lifecycle.md
- kb/sources/discoverphysics-benchmarking-llms-out-of-the-box-scientific.ingest.md:76 → notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md
- kb/sources/dulleck-kerschbamer-doctors-mechanics-computer-specialists.ingest.md:49 → notes/the-boundary-of-automation-is-the-boundary-of-verification.md
- kb/sources/emerging-markdown-formats-that-shape-coding-agent-behavior.ingest.md:56 → notes/agent-memory-requirements/promote-only-when-value-exceeds-cost.md
- kb/sources/falsifybench-inductive-reasoning-rule-discovery-games.ingest.md:66 → notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md (+ deferred explanatory-reach/Popperian reverse edges)
- kb/sources/figma-agent-security-review-thread-2081739292859421118.ingest.md:49 → notes/increasing-computational-autonomy-relocates-human-effort.md
- kb/sources/fluent-self-improving-software-factory-2081823472016335059.ingest.md:49 → notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md
- kb/sources/harnesscompass-guiding-automatic-harness-evolution.ingest.md:51 → notes/diagnostic-richness-constrains-outer-loop-learning-quality.md
- kb/sources/jdegoes-recursive-agent-architecture-2081854216264392934.ingest.md:49 → notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md
- kb/sources/language-model-harnesses-are-compositional-generalizers.ingest.md:48 → notes/rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md
- kb/sources/memento-skills-let-agents-design-agents.ingest.md:71 → notes/a-retrieval-miss-is-a-local-reflective-path-failure.md (authored)
- kb/sources/position-bias.ingest.md:76 → seedling reverse edges (brainstorming, operational-signals, out-of-spec-output, reliability-dimensions)
- kb/sources/self-improving-ai-coding-agents-through-accumulated-rules.ingest.md:64 → notes/an-accepted-edit-verifies-the-change-not-the-rule.md
- kb/sources/semantic-leakage-lms-gonen.ingest.md:86 → notes/context-contamination-operates-below-an-agents-compliance-reasoning.md (authored)
- kb/sources/the-log-is-the-agent-2065129901427130678.ingest.md:60 → notes/the-four-field-record-exposes-an-efficiency-security-and-sovereignty.md
- kb/sources/the-y-combinator-for-llms-solving-long-context-rot.ingest.md:70 → notes/rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md (authored; recommendation struck through)
- kb/sources/why-almost-never-use-ai-to-write-anything-substantive.ingest.md:56 → notes/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md
- kb/sources/why-software-factories-fail-slopcodebench-2081797628552270027.ingest.md:61 → notes/brainstorming-maintainability-oracles-for-agentic-development.md (authored)
