# Consumer migration inventory for the conjectural-learning ontology

This is the bounded consumer inventory required by the
[closure plan](../closure-plan.md). It records migration actions without
editing the library. Historical titles, quotations, source-native terminology,
snapshot-bound reports, and superseded article bodies keep their wording.
Substantial targets are delegated to the existing [rewrite inventory](./README.md);
this file does not duplicate their draft specifications.

Target names marked **unresolved** below describe the initial inventory state;
the [current draft/destination table](./README.md#current-drafts-and-destinations)
now supplies their proposed final names. Use that table and the per-artifact
dispositions before changing links, navigation, or redirects. The settled definition
destinations are the eventual library versions of [Conjectural learning](../definitions/conjectural-learning.md),
[Tentative theory](../definitions/tentative-theory.md), and
[Addressable theory](../definitions/addressable-theory.md), plus the companion
[Commonplace studies conjectural learning through retained theories](../notes/commonplace-studies-conjectural-learning-through-retained-theories.md).

## Reproducible scan and counts

Run from the repository root:

```bash
rg -l -i 'learning by theory refinement|reflective theory refinement|theory refinement|theory-refinement|definitions/theory-refinement\.md|definitions/learning-by-theory-refinement\.md' AGENTS.md kb tests --glob '*.md' | sort

rg -n 'theory-refinement\.md#(tentative-theory|what-the-operation-requires-of-a-theory|departures)' AGENTS.md kb --glob '*.md'

rg -l '\.\./notes/definitions/(theory-refinement|learning-by-theory-refinement)\.md' kb/sources --glob '*.md' | sort

rg -n 'theory-refinement|learning-by-theory-refinement|Theory refinement|Learning by theory refinement' properdocs.yml kb/notes/tags-README.md kb/notes/*README.md kb/articles/README.md
```

At inventory creation the broad Markdown scan found **167 files**: 73 sources, 41
notes, 28 workshop files, 10 articles, seven reports, three agentic-system
files, two instructions, one type, one test scenario, and `AGENTS.md`. These
are discovery counts, not edit counts.

Concrete, mutually exclusive primary dispositions below cover all 167
Markdown paths from that snapshot. `properdocs.yml` is an additional
non-Markdown redirect action:

| Disposition | Count | Meaning |
|---|---:|---|
| substantial draft or retirement already owned by rewrite inventory | 14 | Do not perform a bounded replacement here |
| bounded system-facing consumer | 5 | `AGENTS.md`, instruction/test, or authored agentic-system contract/review action |
| bounded current note consumer | 29 | Inspect the cited statement, then retarget or rewrite by meaning |
| bounded current article consumer | 5 | Preserve the independent article claim and repair ontology framing or links |
| source-ingest present-day Commonplace commentary review | 43 | Preserve source claims; revise only our comparison/classification |
| peer-workshop minimal repair | 7 | Repair links or live framing without changing the workshop commission |
| Markdown navigation action | 4 | Article, note, and workshop navigation; `properdocs.yml` is counted separately |
| preserve historical, snapshot-bound, source-native, or superseded body | 46 | No prose rename; immutable results and generated reviews remain byte-preserved |
| active conjectural-learning workshop scaffolding | 14 | Consumed at closure rather than migrated as library consumers |

These primary dispositions total 167. A file can still need more than one
action inside its primary class, such as a semantic edit followed by a link
repair. The path lists below are the authoritative accounting; rerun the
searches immediately before migration because this workshop is active.

## System-facing and operational consumers

| Path and location | Current dependency | Migration action | Destination |
|---|---|---|---|
| `AGENTS.md:75` | Tentative theory is incorrectly defined as addressable and links to `theory-refinement.md#tentative-theory` | Replace the vocabulary entry with the settled status definition; remove addressability as a condition; update path | final `kb/notes/definitions/tentative-theory.md` |
| `kb/instructions/assess-learning-claims-during-ingest.md:23-27` | Loads Theory refinement as the single comparison basis | Load Conjectural learning for membership, and Addressable theory only when localization/selective repair matters; keep source-first and challengeable mapping | final conjectural-learning and addressable-theory definitions |
| `tests/scenarios/ingest-a-source.md:92-96` | Says the conditional instruction requires the theory-refinement definition | Mirror the instruction's final dependency wording and installed counterpart path | same two final definitions, if both remain required |
| `kb/agentic-systems/COLLECTION.md:60` | Binding collection contract defines theory refinement as a retained localized loop and reflective theory refinement as its self-directed case | Semantic rewrite required: describe conjectural learning, improved capacity, formulation/criticism, and reflective causal self-representation; do not require retained addressable state universally | final conjectural-learning and reflective-system definitions; addressability may remain a separate classification |
| `kb/agentic-systems/reviews/exo.md:98` | Footer points to evidence draft by old title | Reference repair after evidence successor title is fixed; body claim remains about operative path and independent evaluation | **unresolved evidence-note target name** |
| `kb/agentic-systems/reviews/wikiskill-stahl-g.md:45,51` | Generated projection pinned to an immutable analysis result; uses the old ontology | Preserve bytes under the collection's generated-review rule. New classification requires a separately commissioned analysis run after the shared method is migrated; no hand repair of this review | Historical destination handling must preserve both the projection and its exact result; check redirect-aware validation during migration |
| `kb/instructions/analyse-agentic-system/SKILL.md` | Substantial operational vocabulary target | Use its staged draft; no bounded edit here | rewrite inventory target |
| `kb/types/agentic-system-analysis-result.md` | Must match analysis skill classification | Use paired staged draft | rewrite inventory target |

## Definitions and substantive targets

These 14 files are not bounded consumers. Apply their reviewed drafts or
reasoned retirement from the rewrite inventory:

- `kb/notes/definitions/theory-refinement.md`
- `kb/notes/definitions/learning-by-theory-refinement.md`
- `kb/notes/reflective-theory-refinement-has-three-separate-lineages.md`
- `kb/notes/reflective-theory-refinement-needs-interpretation-and-retention.md`
- `kb/notes/learning-by-theory-refinement-may-improve-sample-efficiency.md`
- `kb/notes/disconnected-witnesses-do-not-establish-a-causal-path-through-theory.md`
- `kb/notes/evidence/three-2026-harnesses-retain-editable-rules-or-weights-not-rationale.md`
- `kb/notes/proposals/retained-theories-compared-with-retained-traces-under-resource-limits.md`
- `kb/notes/definitions/theory-builder.md`
- `kb/notes/definitions/reflective-theory-builder.md`
- `kb/instructions/analyse-agentic-system/SKILL.md`
- `kb/types/agentic-system-analysis-result.md`
- `kb/articles/learning-by-theory-refinement-with-fixed-models.md`
- `kb/articles/testing-the-theory-refinement-program.md`

The final names of the lineage, evidence, sample-efficiency, disconnected-path,
harness, reconstruction-proposal, lead-article, and testing-supplement
successors are **unresolved** until those drafts settle. Consumers below that
point to those files must follow their final disposition, not guess a slug.

## Bounded note consumers

The following table enumerates current note paths outside the substantial
queue. `Reference` means the claim survives and only the destination/title
changes. `Semantic` means old membership conditions occur in present-day
Commonplace prose and must be checked against the settled definitions.

| Paths and relevant location | Action | Destination or constraint |
|---|---|---|
| `kb/notes/a-claim-without-external-assessment-carries-three-obligations.md:49`; `kb/notes/addressable-theory-can-coordinate-heterogeneous-factory-development.md:56`; `kb/notes/cost-sensitive-formalisms-for-tentative-theory-search.md:16`; `kb/notes/program-theory-sustains-search-under-delayed-feedback.md:36` | Reference: replace `theory-refinement.md#tentative-theory` | final tentative-theory definition |
| `kb/notes/definitions/codification.md:37`; `kb/notes/definitions/representational-form.md:32,62`; `kb/notes/world-models-assess-explanatory-reach-through-action-conditioned.md:24,33` | Semantic: keep computed/interpreted consequences and localization claims, but attribute them to addressability/representational form rather than genus membership | final addressable-theory definition; codification and representational-form central claims stay |
| `kb/notes/revision-guided-by-rationale-needs-faithfulness-not-just-legibility.md:2,10-12,45` | Semantic: retain optional-rationale and rationale-faithfulness claim as a property of the chosen addressable treatment; remove “optional for theory refinement” as genus wording | final addressable-theory definition and companion |
| `kb/notes/addressable-theory-can-coordinate-heterogeneous-factory-development.md:136,156-157`; `kb/notes/program-theory-sustains-search-under-delayed-feedback.md:74,106,188,195`; `kb/notes/cost-sensitive-formalisms-for-tentative-theory-search.md:224,262-263` | Semantic plus references: retain narrower premise that these notes study addressable retained theories; update evidence/sample note links after names settle | final addressable-theory definition, companion, **unresolved evidence and sample targets** |
| `kb/notes/factory-learning-mechanisms-should-be-compared-on-the-same-causal-job.md:37,111`; `kb/notes/factory-construction-does-not-establish-knowledge-acquisition.md:70`; `kb/notes/theory-and-capacity-building-make-the-same-kind-of-commitment.md:34-47,72`; `kb/notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md:56,219` | Semantic: replace old paradigm row/path with conjectural learning or with Commonplace's retained-theory arrangement as the sentence requires; learning requires improved capacity | final conjectural-learning definition or companion; update old evidence/sample links |
| `kb/notes/bitter-lesson-selects-against-unearned-reach-not-against-structure.md:32,70`; `kb/notes/the-bitter-lesson-selects-production-methods-not-representational.md:69,94`; `kb/notes/the-bitter-lesson-defense-portfolio-has-one-load-bearing-member.md:92`; `kb/notes/unformalized-improvements-need-a-pre-formal-stage-in-the-loop.md:60`; `kb/notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md:53`; `kb/notes/definitions/reach-assessment.md:94`; `kb/notes/continual-learning-requires-governing-behaviour-changing-writes.md:28` | Reference plus wording: these point to the sample-efficiency conjecture, whose contribution survives; remove duplicated “Learning by learning” typo while retargeting | **unresolved sample-efficiency target name** |
| `kb/notes/citing-retained-theory-at-the-decision-point-is-a-mediation-trace.md:71`; `kb/notes/design-rationale-must-preserve-unregenerable-decision-premises.md:12`; `kb/notes/failure-explanation-changes-later-branch-decisions.md:36`; `kb/notes/naur-equates-machine-execution-with-formulated-criteria.md:140`; `kb/notes/reflection-makes-retained-lessons-second-order.md:26,51`; `kb/notes/residue-classes-need-different-mechanisms-so-architecture-is-mixed.md:137`; `kb/notes/specific-intent-may-out-yield-local-rationales-facts-stay-separate.md:52`; `kb/notes/evidence/commonplace-revision-used-theory-guided-computational-search.md:145`; `kb/notes/definitions/reflective-system.md:88` | Reference: preserve narrower retained-path mechanisms and evidence claims; retarget old evidence-note title | **unresolved evidence-note target name** |
| `kb/notes/open-ended-theory-learning-and-factory-learning-close-the-same.md:24,118,194,205` | Semantic plus reference: “formal theory-refinement system” is historical/classical and may remain; current Commonplace convergence and lineage links need successor targets | **unresolved evidence and lineage target names** |
| `kb/notes/bitter-lesson-selects-against-unearned-reach-not-against-structure.md:32`; `kb/notes/the-bitter-lesson-selects-production-methods-not-representational.md:69` | Semantic guard | Retain theory-space search as a possible mechanism; do not infer conjectural-learning membership without formulated criticism causing improved capacity |

### Semantic repairs confirmed during drafting

Parent integration adds these semantic repairs to the bounded inventory;
they are not mechanical title substitutions:

- `kb/notes/definitions/reach-assessment.md:94` and
  `kb/notes/discovery-README.md` must distinguish the selector's proposed
  capability from a reuse benefit that a supplied useful theory can deliver.
- `kb/notes/reflection-makes-retained-lessons-second-order.md:26,51` and
  `kb/notes/self-improving-systems-README.md:39` must route sample-efficiency
  payoff claims to the sample-efficiency successor. The evidence ladder
  retains only their separate causal-path use.
- `kb/articles/bootstrapping-an-autonomous-theory-builder.md:34` should say
  the builder is responsible for developing and revising addressable tentative
  theories, without presuming it has learned successfully. Its link at line
  137 moves from the old lead's `#what-is-new-in-the-setting` to the new lead's
  `#reflection-and-autonomy`; `#a-case` survives.

These are already-enumerated consumer paths; they do not add to the snapshot
counts.

## Articles

| Path | Disposition and action |
|---|---|
| `kb/articles/learning-by-theory-refinement-with-fixed-models.md`; `kb/articles/testing-the-theory-refinement-program.md` | Substantial drafts; final titles/slugs unresolved |
| `kb/articles/an-automated-software-house-as-a-second-test-of-theory-refinement.md` | Bounded-to-substantial check after lead definitions settle. At lines 21-32 and 287, replace paradigm membership with the retained-theory research arrangement where appropriate; preserve the independent software-house hypothesis and witness conditions. Filename/title unresolved if its central title depends on the retired term. |
| `kb/articles/nearest-existing-constructions-to-a-witness-house.md` | Bounded check at description, lines 15-19, 94, 339, 347 and frontmatter source link. Preserve survey evidence; repair lead/supplement and test-section links after final names settle. |
| `kb/articles/bootstrapping-an-autonomous-theory-builder.md` | Bounded reference check at lines 27-28, 137, 149, 215, 267, 388-402. Preserve bootstrap argument; retarget lead/testing/software-house links. |
| `kb/articles/what-an-automated-reviewer-should-measure.md` | Bounded semantic/reference check at frontmatter lines 10-11 and prose 113, 243-278. Preserve reviewer measures; distinguish conjectural learning from the retained-theory study arrangement. |
| `kb/articles/transition-closure-and-continuation-reliability.md` | Link-only repair at frontmatter line 6 and lines 16-17 if testing-supplement slug changes; the transition-closure claim is independent. |
| `kb/articles/automated-software-houses-with-fixed-llms.md`; `kb/articles/the-software-house-as-the-unit-of-training.md` | Superseded historical bodies: preserve terminology. Apply only lifecycle-required link/frontmatter repairs. The tentative-theory fragment at the latter's line 160 must retarget if the old definition is removed, without rewriting the historical argument. |

## Source ingests

Source titles, quotations, abstracts, and descriptions of source-side “theory
refinement” remain unchanged. Forty-three ingests contain present-day
Commonplace comparison links to the old definitions. Review only those
Commonplace-authored passages: map formulation/criticism/improved capacity to
Conjectural learning, addressable/local repair properties to Addressable
theory, and the chosen retained arrangement to the companion. Do not upgrade
missing evidence to absence.

The 43 commentary-review paths are:

```text
kb/sources/ai-scientists-results-without-scientific-reasoning.ingest.md
kb/sources/automated-hypothesis-validation-sequential-falsifications.ingest.md
kb/sources/automated-refinement-first-order-horn-clause-domain-theories.ingest.md
kb/sources/bounded-recursive-self-improvement.ingest.md
kb/sources/concept-bottleneck-models-paper-v3.ingest.md
kb/sources/driven-by-compression-progress.ingest.md
kb/sources/error-centric-intelligence-beyond-observational-learning.ingest.md
kb/sources/eurisko-learns-new-heuristics-and-domain-concepts.ingest.md
kb/sources/falsifybench-rule-discovery-games-full-text.ingest.md
kb/sources/flywheel-encoding-the-scientific-method.ingest.md
kb/sources/form-not-content-placebo-controlled-self-repair.ingest.md
kb/sources/generalization-adaptive-data-analysis-holdout-reuse.ingest.md
kb/sources/gepa-reflective-prompt-evolution.ingest.md
kb/sources/hypothesis-evolution-protocol-auditable-ai-scientists.ingest.md
kb/sources/in-defense-of-base-contraction.ingest.md
kb/sources/introspective-multistrategy-learning.ingest.md
kb/sources/lifefuse-mem-lifecycle-aware-state-fusion.ingest.md
kb/sources/llms-scientific-method-hypothesis-to-discovery.ingest.md
kb/sources/locating-hidden-failures-paper.ingest.md
kb/sources/locating-hidden-failures.ingest.md
kb/sources/logic-of-theory-change-partial-meet-contraction.ingest.md
kb/sources/longmemeval-benchmarking-chat-assistants-long-term-memory.ingest.md
kb/sources/memorylace-lifecycle-aware-consolidation-evidence-retrieval.ingest.md
kb/sources/meta-agent-challenge-autonomous-agent-development.ingest.md
kb/sources/optimal-ordered-problem-solver.ingest.md
kb/sources/past-bench-personal-agents-pdf.ingest.md
kb/sources/popper-conjectures-and-refutations.ingest.md
kb/sources/popper-epistemology-without-a-knowing-subject-1968.ingest.md
kb/sources/procedural-graphs-self-evolving-execution.ingest.md
kb/sources/recursive-self-improvement-since-1987.ingest.md
kb/sources/recursive-self-improvement.ingest.md
kb/sources/reflective-architecture-llm-based-systems-abstract.ingest.md
kb/sources/reinforcement-learning-self-modifying-policies.ingest.md
kb/sources/rulemem-active-rule-memory.ingest.md
kb/sources/scaffold-not-vocabulary-popperian-code-generation-skill.ingest.md
kb/sources/selection-without-signal-recovery-through-expression.ingest.md
kb/sources/shifting-inductive-bias-success-story-algorithm.ingest.md
kb/sources/socratic-agents-autonomous-scientific-discovery.ingest.md
kb/sources/sound-agentic-science-requires-adversarial-experiments.ingest.md
kb/sources/think-before-you-act-popperian-expectations-abstract.ingest.md
kb/sources/upml-framework-for-knowledge-system-reuse.ingest.md
kb/sources/why-am-and-eurisko-appear-to-work.ingest.md
kb/sources/wikiskill-persistent-knowledge-for-skill-evolution.ingest.md
```

Thirty additional ingests match only source-native, bibliographic, historical,
or otherwise non-linking occurrences in the bounded scan. Preserve them unless
a fresh line-by-line migration check finds a present-day Commonplace
classification:

```text
kb/sources/a-new-era-of-theory-driven-ai-research-2084779496549548323.ingest.md
kb/sources/agora-git-as-shared-memory-for-collective-autoresearch.ingest.md
kb/sources/alphadev-faster-sorting-2026-09-08.ingest.md
kb/sources/an-assumption-based-tms.ingest.md
kb/sources/argyris-organizational-learning-and-mis-1977.ingest.md
kb/sources/automated-design-of-agentic-systems.ingest.md
kb/sources/autora-automated-research-assistant.ingest.md
kb/sources/avo-agentic-variation-operators-autonomous-evolutionary-search.ingest.md
kb/sources/causal-inference-using-invariant-prediction.ingest.md
kb/sources/concept-bottleneck-models.ingest.md
kb/sources/discoverphysics-benchmarking-llms-out-of-the-box-scientific.ingest.md
kb/sources/dreamcoder-wake-sleep-full-paper.ingest.md
kb/sources/explanation-based-generalization-unifying-view-2026-09-08.ingest.md
kb/sources/explanation-based-generalization-unifying-view.ingest.md
kb/sources/formal-learning-theory.ingest.md
kb/sources/in-search-of-lost-domain-generalization.ingest.md
kb/sources/integrating-abduction-and-induction-in-machine-learning.ingest.md
kb/sources/intention-is-all-you-need-2022428696595108152.ingest.md
kb/sources/model-discovery-agent-bayesian-experiment-design.ingest.md
kb/sources/programming-as-theory-building.ingest.md
kb/sources/provably-bounded-optimal-agents.ingest.md
kb/sources/rainbow-architecture-based-self-adaptation.ingest.md
kb/sources/recap-early-work-theory-knowledge-refinement.ingest.md
kb/sources/requirements-aware-systems-research-agenda.ingest.md
kb/sources/requirements-reflection-runtime-entities.ingest.md
kb/sources/rome-locating-and-editing-factual-associations-in-gpt.ingest.md
kb/sources/seed-programmed-autonomous-general-learning.ingest.md
kb/sources/steve-yegge-fences-not-sandboxes.ingest.md
kb/sources/theory-refinement-analytical-empirical-methods.ingest.md
kb/sources/towards-causal-representation-learning.ingest.md
```

## Navigation and redirects

| Path and relevant location | Action |
|---|---|
| `kb/articles/README.md:34,38,40` | Rewrite the lead/supplement index entries after final article titles and slugs settle. Preserve the software-house hypothesis as a distinct arrangement. |
| `kb/notes/discovery-README.md:27` | Retarget the surviving sample-efficiency conjecture after its final name settles. |
| `kb/notes/self-improving-systems-README.md:39` | Correct the current mislabelled sample-efficiency link and retarget both evidence and rationale entries after final names settle. |
| `kb/work/README.md:10,15` | Preserve the active conjectural-learning description until closure; update or remove its entry only when the workshop closes. Keep the interface workshop's historical title and commission. |
| `properdocs.yml:47-69,100,140,173,205,208-209,232-237` | Recompute redirect destinations only after final article/note slugs settle. Existing historical source keys remain valid. The current `notes/definitions/theory-mediated-learning.md -> notes/definitions/theory-refinement.md` chain cannot terminate at a retired path; point it directly to the honest successor. Add redirects for retired **library** paths according to lifecycle procedure. Do not add redirects for deleted workshop paths. |

No occurrence was found in `kb/notes/tags-README.md`; generated or curated
indexes still need their normal refresh after promotion.

## Peer workshops

Only minimal repairs are proposed for the later migration commission. No
peer-workshop edit is authorized during this drafting stage. Do not revise
their investigations or experiment designs.

| Paths | Action |
|---|---|
| `kb/work/theory-refinement-interface/README.md:1-16,40,46`; `kb/work/theory-refinement-interface/theory-refinement-interface.md:1-31,133,299` | Preserve the workshop title and classical literature subject. Replace the live dependency on Commonplace's retired definition with Addressable theory/classical precedent or a direct source link. Flag any claim that its interface defines conjectural-learning membership; do not redesign the interface. |
| `kb/work/explanatory-theories-deployment-time-learning/README.md:7`; `.../exo-case.md:9`; `.../theory-mediated-improvement-loop.md:49` | Preserve the experiment commission and treatment names. Repair links to the final evidence/sample successor and describe retained/addressable theory as the treatment, not the genus. |
| `kb/work/first-downstream-run/README.md:47,65` | Link-only repair if testing-supplement filename or fragments change. |
| `kb/work/ideal-interpreter/README.md:43` | Preserve link to the interface workshop; no ontology edit unless that workshop is renamed independently. |

The six files under
`kb/work/popperian-maintenance-episode/fifth-episode-record/versions/` are
historical draft versions. Preserve their old titles and wording:
`v0-first-draft-cp-skill-write-13-48.md`,
`v1-full-pass-reframe-def1280a.md`, `v2-defensive-trim-4d707961.md`,
`v3-essay-level-rewrite.md`, `v4-second-pass-reframe.md`, and
`v5-bridge-as-equation.md`. Preserve recorded version bytes; resolve any
required live navigation outside the historical snapshots.

## Historical and snapshot-bound preserves

Do not rewrite these seven reports to current ontology; they record assessed
or generated state:

```text
kb/reports/cache/software-factory-note-inventory.md
kb/reports/retained/agentic-system-analysis/AAS-2026-09-17-wikiskill-stahl-g-01/result.md
kb/reports/retained/simplification-instruction-comparison-20260807/baseline.md
kb/reports/retained/simplification-instruction-comparison-20260807/candidate-churchill-zinsser.md
kb/reports/retained/simplification-instruction-comparison-20260807/candidate-established-style.md
kb/reports/retained/simplification-instruction-comparison-20260807/candidate-sentence-by-sentence.md
kb/reports/retained/theory-builder-boundary-cases-20260917.md
```

Also preserve `kb/articles/automated-software-houses-with-fixed-llms.md` and
`kb/articles/the-software-house-as-the-unit-of-training.md` as superseded
historical bodies, as specified above.

Also preserve the generated
`kb/agentic-systems/reviews/wikiskill-stahl-g.md`. Parent contract review moved
it from the bounded-edit class to this class: the collection prohibits tuning
a generated projection independently of its producing analysis. Its immutable
result is already included among the seven reports above. A new run is not
commissioned by ontology drafting.

## Active workshop files consumed at closure

The broad scan finds 14 files inside `kb/work/conjectural-learning/` other
than this inventory. They are working basis, decisions, drafts, probes, and
accounting, not consumers to promote mechanically:

```text
kb/work/conjectural-learning/README.md
kb/work/conjectural-learning/definitions/addressable-theory.md
kb/work/conjectural-learning/definitions/conjectural-learning.md
kb/work/conjectural-learning/migration-map.md
kb/work/conjectural-learning/notes/commonplace-studies-conjectural-learning-through-retained-theories.md
kb/work/conjectural-learning/rewrites/README.md
kb/work/conjectural-learning/rewrites/builder-disposition.md
kb/work/conjectural-learning/rewrites/definition-remnants.md
kb/work/conjectural-learning/rewrites/evidence-disposition.md
kb/work/conjectural-learning/rewrites/kb/instructions/analyse-agentic-system/SKILL.md
kb/work/conjectural-learning/rewrites/kb/notes/disconnected-witnesses-do-not-establish-a-causal-path-through-theory.md
kb/work/conjectural-learning/rewrites/lineage-disposition.md
kb/work/conjectural-learning/stability-test/content.md
kb/work/conjectural-learning/stability-test/strain-report.md
```

Other active-workshop files that do not match the scan still follow the
closure plan: promote unique decisions or claims, then delete the workshop
without redirects.

## Migration gates

Before applying this inventory:

1. Fix the unresolved successor titles and slugs from the substantive drafts.
2. Re-run all four searches above and compare their path sets with this file.
3. Apply semantic rewrites before mechanical links so wrong membership claims
   are not preserved under new names.
4. Repair exact old fragments: `#tentative-theory` to Tentative theory;
   `#what-the-operation-requires-of-a-theory` to Addressable theory with
   semantic review; and `#departures` by its actual reflective or machinery
   meaning. The exact file list is in [definition remnants](./definition-remnants.md#exact-inbound-fragment-repairs).
5. Refresh navigation and redirect destinations only after final paths exist.
6. Re-run validation and the broad scan, allowing only historical,
   source-native, snapshot-bound, and explicitly preserved occurrences.
