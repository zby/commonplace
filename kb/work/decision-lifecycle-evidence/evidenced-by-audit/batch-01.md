# evidenced-by audit — batch_01 (35 files)

80 footer `evidenced-by` edges found in 35 files. There are no prose mentions of the word outside edges (0). Some files have no edges.

| class | count |
|---|---|
| CORROB-OK | 0 |
| QUALIFY | 36 |
| CORROB-UNTESTED | 6 |
| ORIGIN | 33 |
| MISLABEL | 5 |
| **total** | **80** |

Label constraints used: `abstracted-from`, `derived-from`, and `see-also` allow only reference, agent-memory-systems, agentic-systems, and sources. For an external URL, the fix keeps `evidenced-by` and rewrites the phrase to name the source's role as origin. For a note target, the fix uses `grounds` or `extends`.

## Non-QUALIFY edges

| source file:line | target | class | reason | proposed fix |
|---|---|---|---|---|
| kb/notes/borrowed-patterns-transfer-only-over-shared-mechanism.md:20 | reference/source-adoption-policy.md | MISLABEL | The policy applies the claim; applying a claim is not an observation that tests it. | `see-also: Commonplace's source-adoption policy applies this discriminator, giving programming patterns a fast pass only over the shared symbolic-artifact layer` |
| kb/notes/candidacy-evidence-licenses-escalation-not-acceptance.md:44 | domain-pricing-routes-an-exception-to-idealization-assessment.md (note) | ORIGIN | The target note was created one day before this note (08-19 vs 08-20), and this note generalizes from it as its "first worked witness". | `grounds: the pricing case this distinction was drawn from, including the observed pricing-gated-verdict failure mode` |
| kb/notes/claim-modality-is-the-inference-form-of-the-refuter.md:37 | reference/adr/066-… | ORIGIN | The note organizes the existing, shipped mode system, so the ADR is its source, not a test of it. | `abstracted-from: the shipped refuter-defined mode system this mapping organizes` |
| kb/notes/commitment-not-derivation-creates-new-ground-truth.md:86 | reference/link-vocabulary.md | MISLABEL | The registry states the boundary that this note explains; a registry is a definition, not evidence. | `see-also: the registered narrow semantics of derived-from against the ampliative lineage labels; this note supplies the mechanism behind that boundary` |
| kb/notes/commitment-not-derivation-creates-new-ground-truth.md:98 | reference/adr/056-… | CORROB-UNTESTED | The phrase and body line 57 say the note "predicts" this ADR, but the ADR was created on the same day as the note (2026-07-25), so it is a co-developed case, not a test made after the claim. | `evidenced-by: chose archiving over deletion for adopted proposals — the commitment-side disposal case, decided alongside this note, not a later test` (also soften body l.57 "predicts" to "explains") |
| kb/notes/commitment-not-derivation-creates-new-ground-truth.md:99 | reference/adr/025-… | CORROB-UNTESTED | The body presents the ADR as a confirmed prediction, but the ADR (2026-06-09) predates the note, so this is retrodiction. | `abstracted-from: deleted committed generated listings and regenerated them from frontmatter — the derivation-side disposal case the boundary was read from` |
| kb/notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md:40 | Raschka (external) | CORROB-UNTESTED | The phrase presents "independent practitioner convergence" as support, but it is agreement with the thesis, not a test the thesis could have failed. | `evidenced-by: a practitioner states the same thesis ("apparent model quality is really context quality"); agreement, not a test` |
| kb/notes/continual-learning-requires-governing-behaviour-changing-writes.md:38 | agent-memory-systems/trace-learning-techniques-in-related-systems.md | ORIGIN | "Surveyed systems already split…" describes the survey this claim was generalized from. | `abstracted-from: surveyed systems split into weight-promotion and artifact-promotion loops` |
| kb/notes/definitions/actionable-methodology.md:55 | sources/the-anatomy-of-a-design-theory-gregor-jones-2007.ingest.md | ORIGIN | The two sibling Gregor edges are already `derived-from`, and this source likewise supplies the definition's distinction. | `abstracted-from: separates core design-theory content from the additional agents and actions that implement it` |
| kb/notes/definitions/discovery-lifecycle.md:75 | Peirce, SEP (external) | ORIGIN | The definition is built on Peirce's phases of inquiry. The target is external, so `abstracted-from` is not available. | `evidenced-by: source of the abduction–deduction–induction phasing this definition adopts (origin, not a test)` — or ingest into sources/ and use `abstracted-from` |
| kb/notes/definitions/discovery-lifecycle.md:76 | Moen PDSA (external) | CORROB-UNTESTED | "Converging on the same loop" presents a parallel tradition as confirmation, but no test is named. | `evidenced-by: a parallel applied tradition (Shewhart–Deming PDSA) with the same conjecture–consequence–test shape; agreement, not a test` |
| kb/notes/definitions/discovery-lifecycle.md:77 | Scientific Discovery, SEP (external) | ORIGIN | The definition's framing of discovery as process versus product comes from this source. | `evidenced-by: source of the process/product distinction and the hypothesis-generation focus this definition adopts (origin, not a test)` |
| kb/notes/definitions/reflective-system.md:86 | sources/wuyts-ducasse-2001-symbiotic-reflection.ingest.md | CORROB-UNTESTED | The phrase says "corroborates", but the source was ingested on the note's creation day (2026-07-14) and reports no test of the threshold. | `evidenced-by: a separate formulation of the causal self-representation threshold and the introspection/intercession distinction; agreement, not a test` (or `abstracted-from` if it fed the definition) |
| kb/notes/definitions/tentative-theory.md:72 | sources/popper-a-realist-view-…1966.ingest.md | ORIGIN | The term is "Popper's term, borrowed as is". | `derived-from: the schema and the place of TT in it` |
| kb/notes/definitions/tentative-theory.md:73 | sources/popper-conjectures-and-refutations.ingest.md | ORIGIN | The term is borrowed from this source. | `derived-from: tentativeness as a lasting status` |
| kb/notes/definitions/theory-builder.md:262 | sources/popper-a-realist-view-…1966.ingest.md | ORIGIN | The definition is built from Popper's schema. | `abstracted-from: the schema, objective knowledge, and consumption` |
| kb/notes/definitions/theory-builder.md:263 | sources/popper-epistemology-without-a-knowing-subject-1968.ingest.md | ORIGIN | The definition's conditions are drawn from this source. | `abstracted-from: formulation as a condition of criticism, action guided by objective knowledge, self-criticism` |
| kb/notes/definitions/theory-builder.md:264 | sources/popper-conjectures-and-refutations.ingest.md | ORIGIN | The definition's conditions are drawn from this source. | `abstracted-from: the critical method against trial and error, and locating the refuted hypothesis` |
| kb/notes/diagnostic-richness-constrains-outer-loop-learning-quality.md:29 | agent-memory-systems/trace-learning-techniques-in-related-systems.md | ORIGIN | The phrase itself says the survey "grounds the axis". | `abstracted-from: the survey paragraph and the Meta-Harness ablation the diagnostic-richness axis was drawn from` |
| kb/notes/diagnostic-richness-constrains-outer-loop-learning-quality.md:30 | sources/meta-harness-…ingest.md | ORIGIN | The ingest (2026-03-31) predates the note (2026-05-19), and its ablation is the case the gradient was generalized from. | `abstracted-from: retained ablation extracts supply the three accuracy figures and the trace-access versus summaries comparison` |
| kb/notes/elicitation-requires-maintained-question-generation-systems.md:86 | x.com KatanaLarp post (external) | ORIGIN | "Motivates structured elicitation" marks this post as the case the claim came from. | `evidenced-by: the motivating case — deployment-failure insights retrievable on probe but absent in undirected review (origin, not a test)` |
| kb/notes/ephemeral-computation-prevents-accumulation.md:94 | blackhc essay (external) | ORIGIN | The essay supplies the premise pressures, not an observation that tests the claim. | `evidenced-by: source of the production-knowledge pressures this note builds on (origin, not a test)` |
| kb/notes/ephemerality-is-safe-where-embedded-operational-knowledge-has-low.md:110 | blackhc essay (external) | ORIGIN | Same essay, in the same role as the previous row. | `evidenced-by: source of the production pressures this note separates by continuity requirement (origin, not a test)` |
| kb/notes/evidence/commonplace-as-a-reflective-system.md:68 | evidence/tag-readme-trace-observed-causal-connection.md (note) | ORIGIN | The trace is the data this reading is built from. | `grounds: the full observed trace the causal-connection reading is built from` |
| kb/notes/evidence/commonplace-as-a-reflective-system.md:69 | reference/tag-readme-trace-as-self-improving-loop.md | ORIGIN | The allocation profile is read from this mapping. | `abstracted-from: the search, evaluation, and retention mapping the allocation profile is read from` |
| kb/notes/evidence/missing-rationale-does-not-exclude-a-builder-weights-do-across-runs.md:71 | sources/prime-agent-…ingest.md | ORIGIN | This evidence note is a reading of this report. | `abstracted-from: the refinement mechanism and the preserved specification exploit` |
| kb/notes/evidence/missing-rationale-does-not-exclude-a-builder-weights-do-across-runs.md:72 | sources/recursive-experiential-working-memory-evolution.ingest.md | ORIGIN | This evidence note is a reading of this report. | `abstracted-from: the repair-decision framing and the growth-only package` |
| kb/notes/evidence/missing-rationale-does-not-exclude-a-builder-weights-do-across-runs.md:73 | sources/apodex-1-1-…ingest.md | ORIGIN | This evidence note is a reading of this report. | `abstracted-from: offline weight training and the run-scoped coordination plane` |
| kb/notes/evidence/missing-rationale-does-not-exclude-a-builder-weights-do-across-runs.md:74 | sources/sutton-javed-…ingest.md | MISLABEL | The target states a position; it is not an observation or case. | `see-also: the weights-side position` |
| kb/notes/evidence/real-self-improving-systems-occupy-combinations-no-rung-captures.md:76 | sources/ashby-design-for-a-brain-ultrastability.md | ORIGIN | This is a casebook row; the claim generalizes over its own rows. | `abstracted-from: the operative, non-cumulative, non-reflective floor` |
| …real-self-improving…:77 | Self-Improving Algorithms (external) | ORIGIN | This is a casebook row, and the target is external. | `evidenced-by: casebook row the combination claim is drawn from — cumulative retention with no representation and no gate (origin, not a test)` |
| …real-self-improving…:78 | sources/dreamcoder-…ingest.md | ORIGIN | This is a casebook row. | `abstracted-from: iterative growth of a symbolic library…; the capture states no acceptance criterion` (keep phrase) |
| …real-self-improving…:79 | sources/knowledge-centric-self-improvement-…ingest.md | ORIGIN | This is a casebook row. | `abstracted-from: addressability operations exercised computationally, with warrant split by question` |
| …real-self-improving…:81 | six-reported-self-improvement-paths-….md (note) | MISLABEL | The target is a sibling analysis note, and the phrase itself says "extends". | `extends: the detailed five-system reading, adding HyperAgents, while this casebook remains at thirteen rows` |
| …real-self-improving…:82 | sources/self-harness-…ingest.md | ORIGIN | This is a casebook row. | `abstracted-from:` + existing phrase |
| …real-self-improving…:83 | sources/continual-harness-…ingest.md | ORIGIN | This is a casebook row. | `abstracted-from:` + existing phrase |
| …real-self-improving…:84 | sources/autogenesis-…ingest.md | ORIGIN | This is a casebook row. | `abstracted-from:` + existing phrase |
| …real-self-improving…:85 | sources/self-improving-ai-coding-agents-…ingest.md | ORIGIN | This is a casebook row. | `abstracted-from:` + existing phrase |
| …real-self-improving…:86 | sources/darwin-godel-machine-…ingest.md | ORIGIN | This is a casebook row. | `abstracted-from:` + existing phrase |
| …real-self-improving…:87 | agentic-systems/reviews/exo.md | ORIGIN | This is a casebook row. | `abstracted-from:` + existing phrase (see the upgrade note below if the row postdates the claim) |
| …real-self-improving…:88 | evidence/commonplace-as-a-reflective-system.md (note) | ORIGIN | This is a casebook row, and the target is a note. | `grounds: the human-inclusive joint-allocation reading this row places` |
| kb/notes/evidence/tag-readme-trace-observed-causal-connection.md:81 | reference/adr/026-… | ORIGIN | The trace is reconstructed from this ADR's record. | `abstracted-from: records the decision and implemented contract this trace reconstructs` |
| kb/notes/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md:57 | frontloading-spares-execution-context.md (note) | MISLABEL | The target is the experiment's subject (the text that was rewritten), not evidence about the result. | Drop the footer edge; keep the body link at l.14 as the target of the experiment. If a footer edge is wanted, use `evidenced-by: the retained artifact the experiment rewrote (experimental material, not independent evidence)` |
| kb/notes/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md:58 | claim-notes-should-use-toulmin-derived-sections-for-structured.md (note) | CORROB-UNTESTED | "Independently records" presents an earlier note (2026-02) as confirmation, but the target is a claim note, not a test. | `evidenced-by: an earlier, separate observation that added structure can stiffen mature arguments; agreement, not a test of this tradeoff` |

### Upgrade candidates

These edges are counted as QUALIFY or ORIGIN above, but each could become CORROB-OK if the phrase names a test.

- kb/notes/candidacy-evidence-licenses-escalation-not-acceptance.md:45 → the Pirolli evidence note was created 2026-08-26, six days after the claim (2026-08-20). This makes it a later, independent case, and the claim could have failed it if thematic fit had settled support. Suggested phrase: `evidenced-by: a later case (recorded after this claim) where the claim could have failed had thematic fit settled support; an independent pass showed it only routed assessment`.
- kb/notes/diagnostic-richness-constrains-outer-loop-learning-quality.md:31 → the AutoSaddler ingest was created 2026-08-25, after the note (2026-05-19). Its diagnosis ablation could have shown no gain from richer diagnosis. Suggested phrase: `evidenced-by: a later, independently built ablation (GAIA2, 62.0→57.8 Pass@1 without in-depth diagnosis) that the claim could have failed; bounded to one code-and-trace treatment against one shallow call`.
- The rows of real-self-improving… that were added after 2026-08-04 (DreamCoder l.78, Exo l.87) may be later tests of "no rung captures". That holds only if git shows they were new systems rather than moved or reworded rows. I did not verify this.

## QUALIFY edges

- kb/notes/brainstorming-maintainability-oracles-for-agentic-development.md:196 → reference/adr/005-quality-check-placement.md
- kb/notes/brainstorming-maintainability-oracles-for-agentic-development.md:197 → sources/why-software-factories-fail-slopcodebench-…ingest.md
- kb/notes/candidacy-evidence-licenses-escalation-not-acceptance.md:45 → evidence/independent-pass-tightened-three-of-four-pirolli-verdicts.md
- kb/notes/cheap-generation-breaks-text-volume-as-an-effort-signal.md:20 → news.ycombinator.com item 49336573
- kb/notes/choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md:33 → agent-memory-systems/reviews/Self-Training-LLM.md
- kb/notes/choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md:34 → sources/self-training-large-language-models-through-knowledge-detection.ingest.md
- kb/notes/choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md:35 → sources/into-the-unknown-self-learning-large-language-models.ingest.md
- kb/notes/citing-retained-theory-at-the-decision-point-is-a-mediation-trace.md:69 → evidence/tag-readme-trace-observed-causal-connection.md
- kb/notes/commitment-not-derivation-creates-new-ground-truth.md:100 → reference/adr/026-…
- kb/notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md:157 → sources/hyperagents.ingest.md
- kb/notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md:158 → sources/agent-optimizers-compound-terminal-bench.ingest.md
- kb/notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md:159 → sources/harness-updating-is-not-harness-benefit.ingest.md
- kb/notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md:160 → sources/poetiq-perspective-on-recursive-self-improvement.ingest.md
- kb/notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md:162 → evidence/commonplace-as-a-reflective-system.md
- kb/notes/computationally-directed-self-improvement-is-a-reallocation.md:90 → evidence/commonplace-as-a-reflective-system.md
- kb/notes/computationally-directed-self-improvement-is-a-reallocation.md:91 → sources/poetiq-perspective-on-recursive-self-improvement.ingest.md
- kb/notes/context-contamination-operates-below-an-agents-compliance-reasoning.md:59 → sources/semantic-leakage-lms-gonen.ingest.md
- kb/notes/context-contamination-operates-below-an-agents-compliance-reasoning.md:60 → sources/language-models-like-humans-show-content-effects-on-reasoning.ingest.md
- kb/notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md:38 → x.com odysseus0z post
- kb/notes/context-operation-interface-bounds-context-policy.md:40 → agent-memory-systems/reviews/scroll.md
- kb/notes/context-operation-interface-bounds-context-policy.md:41 → agent-memory-systems/reviews/virtual-context.md
- kb/notes/criteria-edits-invalidate-verdicts-process-edits-invalidate-artifacts.md:32 → sources/build-systems-a-la-carte.ingest.md
- kb/notes/cross-task-transition-policy-remains-scheduling-behind-tools.md:36 → agentic-systems/reviews/claude-code-dynamic-workflows.md
- kb/notes/definitions/addressable-theory.md:91 → sources/theory-refinement-analytical-empirical-methods.ingest.md
- kb/notes/definitions/addressable-theory.md:92 → sources/automated-refinement-first-order-horn-clause-domain-theories.ingest.md
- kb/notes/definitions/reflective-system.md:87 → sources/ashby-design-for-a-brain-ultrastability.md
- kb/notes/derivation-and-inheritance-give-starting-warrant-earns-scope.md:73 → reference/commonplace-as-an-instrument.md
- kb/notes/diagnostic-richness-constrains-outer-loop-learning-quality.md:31 → sources/autosaddler-…ingest.md
- kb/notes/domain-pricing-routes-an-exception-to-idealization-assessment.md:81 → cseweb.ucsd.edu mop.pdf
- kb/notes/domain-pricing-routes-an-exception-to-idealization-assessment.md:82 → wikipedia Monkey_patch
- kb/notes/domain-pricing-routes-an-exception-to-idealization-assessment.md:83 → v8.dev/blog/fast-properties
- kb/notes/domain-pricing-routes-an-exception-to-idealization-assessment.md:84 → v8.dev/docs/hidden-classes
- kb/notes/domain-pricing-routes-an-exception-to-idealization-assessment.md:85 → erlang.org release_handling
- kb/notes/domain-pricing-routes-an-exception-to-idealization-assessment.md:86 → selflanguage self-power.pdf
- kb/notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md:99 → academic.oup.com pgae233
- kb/notes/evaluation-automation-is-phase-gated-by-comprehension.md:55 → sources/improving-ai-skills-with-autoresearch-evals-skills-…ingest.md (the body at l.20 says "matches"; consider making it "illustrates")
