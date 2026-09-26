# evidenced-by audit — batch_00 (39 files, 91 edges)

Counting unit: one `evidenced-by` label occurrence. In `kb/agentic-systems/reviews/*` a single inline `— evidenced-by` label sometimes covers 2 links (e.g. arex-skill.md:20); counted once. Prose mentions of the word that are not edges: 0.

| class | notes (47) | other collections (44) | total |
|---|---|---|---|
| CORROB-OK | 0 | 0 | 0 |
| QUALIFY | 28 | 42 | 70 |
| CORROB-UNTESTED | 2 | 0 | 2 |
| ORIGIN | 13 | 1 | 14 |
| MISLABEL | 4 | 1 | 5 |

Dates used (git first-add, `--follow`) where decisive: universal-framework note 2026-07-08 vs ADR 017/018/019 (Apr), 042 (07-09, same commit series), 044 (07-11), 069 (08-22); linked-note 08-27 vs five-link-cap evidence 08-25 and descriptive-link-labels 08-10; omitted-loop 08-02 vs HGM ingest 04-24.

## Non-QUALIFY edges

| source file:line | target | class | reason | proposed fix |
|---|---|---|---|---|
| kb/notes/an-accepted-edit-verifies-the-change-not-the-rule.md:36 | Moen PDSA history (external PDF; ingest exists: `../sources/foundation-and-history-of-the-pdsa-cycle.ingest.md`) | CORROB-UNTESTED | Phrase says "decades-old corroboration", but the source is a methodological precedent reporting no test this claim could have failed. | Re-point to the ingest; `evidenced-by: independent precedent from quality improvement that bounds the claim — one improving test is not enough; predicting improvement under future conditions is a separate judgment the test never performed` |
| kb/notes/a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md:62 | ../reference/adr/044-user-verification-replaces-global-note-status.md | CORROB-UNTESTED | "the prediction played out" presents ADR 044 as a fulfilled prediction, but it was adopted three days after the note by the same operator acting on its recommendation, so it is an implementation, not an independent test. | `evidenced-by: later implementation (2026-07-11, three days after this note) of its status/lifecycle recommendation — the fused field was deleted and per-collection redefinition of assertion force was rejected; adopted under this note's influence, so not an independent test` |
| kb/notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md:71 | ../types/tag-readme.md | ORIGIN | The rule is presented as generalized from four instances ("The spread is what shows it generalizes"), and the tag-readme `complete` mark is the first of them; `abstracted-from` is not allowed toward `types/`. | `evidenced-by: origin instance — the `complete` mark is the shipped, validator-enforced case the rule was generalized from; the mark contract lives here` (also soften body line 42 "The spread is what shows it generalizes" to "The spread is what the generalization is built from") |
| kb/notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md:73 | ../reference/adr/027-package-scaffold-assets-without-source-tree-symlinks.md | ORIGIN | ADR 027's duplicated template is the fourth of the instances the rule is generalized from. | `abstracted-from: source-of-truth for the byte-identical `AGENTS.md.template` duplication, the fourth instance the rule generalizes` |
| kb/notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md:65 | ../agent-memory-systems/agentic-memory-systems-comparative-review.md | ORIGIN | The body says the comparative review "reveals" and "confirms" the decomposition; the note reads the decomposition off the review's axes and trilemma rather than testing it. | `abstracted-from: the matrix axes span storage, retrieval/activation, and learning, and the agency trilemma shows the subproblems trading off; this note generalizes that into the crosscutting claim` (also change body line 14 "confirms" to "reports") |
| kb/notes/agent-orchestration-needs-coordination-guarantees-not-just.md:60 | ./llm-context-is-composed-without-scoping.md | ORIGIN | This note is one of the three failure cases the missing-guarantee discriminator is built from, and it is a note, so `abstracted-from` is unavailable. | `grounds: flat inherited context fails by contamination when there is no isolation primitive — one of the three cases the discriminator generalizes` |
| kb/notes/agent-orchestration-needs-coordination-guarantees-not-just.md:61 | ./synthesis-is-not-error-correction.md | ORIGIN | This note is the second origin case of the three and is also a note. | `grounds: output aggregation fails by amplification when there is no adjudication primitive — one of the three cases the discriminator generalizes` |
| kb/notes/agent-orchestration-needs-coordination-guarantees-not-just.md:62 | https://arxiv.org/html/2603.10062v1 (link text already says "Ingest:"; ingest exists: `../sources/multi-agent-memory-computer-architecture-perspective.ingest.md`) | ORIGIN | This source is the third origin case, and the link text names the ingest while the URL points to arXiv. | Re-point to the ingest; `abstracted-from: shared multi-agent memory fails by inconsistency when there is no consistency protocol — one of the three cases the discriminator generalizes` |
| kb/notes/a-linked-note-discharges-its-own-grounding-so-a-citing-note-owes.md:113 | ./evidence/a-five-link-cap-missed-four-grounding-findings-in-twelve-reviews.md | ORIGIN | The assay (2026-08-25) predates the note (08-27) and tested link caps, not this claim; "shows" claims confirmation from a case the claim was built from. | `evidenced-by: origin case, recorded before this note — the misattribution FAIL illustrates a representation failure that no link count catches` |
| kb/notes/an-omitted-loop-function-and-a-frozen-one-need-different-repairs.md:103 | ../sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md | ORIGIN | HGM is one of the five systems the note's claim is built from (ingest 04-24, note 08-02); the "shows" clause reports HGM's own result, not a test of this note's claim. | `abstracted-from: the name-borrowing lineage substitutes a benchmark estimate for the utility proof; the paper's own finding that immediate benchmark score is a weak selection signal bounds the frozen-gate case` |
| kb/notes/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md:241 | ./evidence/a-five-link-cap-missed-four-grounding-findings-in-twelve-reviews.md | ORIGIN | The note rereads existing paired outcomes under its new placement ("reads differently"), so the data fitted the claim instead of testing it; the target is a note. | `evidenced-by: origin data, recorded before this note — the paired outcomes it rereads as a fact about note size rather than reviewer capacity; not a test of that reading` |
| kb/notes/a-retrieval-miss-is-a-local-reflective-path-failure.md:47 | ./evidence/commonplace-as-a-reflective-system.md | ORIGIN | The tag-readme trace events predate the note, and the body says the case "shows" the failure being converted; the note generalizes from that trace. | `evidenced-by: origin case — the observed trace where a symbolic check corrected the natural-language search recipe that had been missing a member; recorded before this claim, so it illustrates rather than tests it` (and body line 20 "shows" to "records") |
| kb/notes/a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md:53 | ../reference/adr/017-collection-md-is-the-register-convention-boundary.md | ORIGIN | ADR 017 (2026-04) predates the note (07-08) and is a shipped instance the claim generalizes. | `abstracted-from: shipped instance of the declaration obligation — COLLECTION.md is the mandatory per-collection contract surface, and a missing or vague one is "an operational defect"` |
| kb/notes/a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md:57 | ../reference/adr/018-types-are-path-references-to-instruction-docs.md | ORIGIN | ADR 018 (2026-04) is a pre-existing instance of the demotion. | `abstracted-from: shipped instance of the demotion — an open, collection-local type set` |
| kb/notes/a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md:58 | ../reference/adr/019-collection-owned-link-vocabulary.md | ORIGIN | ADR 019 (2026-04) is a pre-existing analogous instance. | `abstracted-from: analogous semantic-vocabulary demotion — collection-owned selections from a shared catalogue` |
| kb/agent-memory-systems/lightweight/incremental-self-improvement.md:88 | ../../sources/on-learning-how-to-learn-learning-strategies.ingest.md | ORIGIN | The lightweight review is written from this ingest ("Reviewed version: … local ingest"); the collection contract routes that back-link to `derived-from`. | `derived-from: local ingest classifies the report and extracts the payoff-per-time, reversible-promotion, and oracle-dependence lessons` |
| kb/notes/abstract-an-experience-only-when-you-can-state-the-boundary.md:58 | ./memory-management-policy-is-learnable-but-oracle-dependent.md | MISLABEL | The target note supplies a premise (the retrievability-not-transfer value of a preserved fact), not an observation. | `grounds: a preserved fact's value is its retrievability, not its transfer — the long-tail half of the decision` |
| kb/notes/agent-orchestration-needs-coordination-guarantees-not-just.md:63 | https://arxiv.org/pdf/2602.11865 (ingest exists: `../sources/intelligent-ai-delegation-tomasev-franklin-osindero.ingest.md`) | MISLABEL | The phrase says the source supplies borrowed vocabulary, not evidence. | Re-point to the ingest; `see-also: source of the accountability-vacuum and liability-firebreak vocabulary` |
| kb/notes/a-linked-note-discharges-its-own-grounding-so-a-citing-note-owes.md:114 | ./descriptive-link-labels-may-supply-claim-self-sufficiency.md | MISLABEL | The target note's ablation test (2026-08-10) predates this note and tested a different conjecture; here it supplies a premise. | `grounds: its label-ablation test attributes claim self-sufficiency to premises carried in the citing note's body, which is the text a representation check reads` |
| kb/notes/a-repeatable-operative-path-keeps-a-redesign-class-open-to-revision.md:71 | ../reference/commonplace-declared-frame.md | MISLABEL | The target supplies the boundary (a frame definition) used by the cases, not evidence. | `see-also: supplies the human-inclusive boundary used by the Commonplace cases` |
| kb/agent-memory-systems/thalo-type-comparison.md:164 | Toulmin argument (OWL Purdue, external) | MISLABEL | The target is a reference model that supplies the decomposition Thalo approximates, not evidence for a claim in the review. | `see-also: Toulmin's formal argumentation model provides the canonical decomposition (claim/grounds/warrant/qualifier/rebuttal/backing) that Thalo's opinion entity approximates with Claim/Reasoning/Caveats sections` (also consider body line 79 "The convergence … validates the choice", which asserts confirmation) |

## Upgrade opportunities among QUALIFY (optional)

- a-universal-knowledge-framework…:60 → ADR 069 (08-22, after the note): the binding-path audit could have found shared contract bundles binding, but found only local contracts. That is a real later test the phrase could name: `evidenced-by: after this note (2026-08-22), a binding-path audit that could have found shared contract labels binding found only local contracts ever bound; the shipped correction to clone-once prototypes followed`.
- a-universal-knowledge-framework…:59 → ADR 042 (07-09): it was committed together with an edit to the note, so it is not independent. Leave it as history, or say so explicitly.
- agentic-systems-interpret-underspecified-instructions.md:144 and the coordination-guarantees note: an ingest exists for the external arXiv target (`agent-behavioral-contracts-formal-specification-runtime.ingest.md`). Re-point it there.

## QUALIFY edges

Notes:
- kb/notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md:220 → evidence/commonplace-revision-used-theory-guided-computational-search.md
- kb/notes/accumulation-counts-dependence-through-the-retained-result.md:58 → sources/ashby-design-for-a-brain-ultrastability.md
- kb/notes/accumulation-counts-dependence-through-the-retained-result.md:59 → Self-Improving Algorithms (external PDF)
- kb/notes/addressability-grain-sets-a-matched-selective-read-floor.md:94 → reference/adr/025
- kb/notes/agentic-systems-interpret-underspecified-instructions.md:144 → arxiv 2602.22302 (ABC)
- kb/notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md:77 → sources/mini-exercise-mismanaged-geniuses-longcot-rlm.ingest.md
- kb/notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md:78 → sources/the-y-combinator-for-llms-solving-long-context-rot.ingest.md
- kb/notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md:81 → agentic-systems/reviews/claude-code-dynamic-workflows.md
- kb/notes/a-goal-holding-interpreter-fails-soft-workarounds-tax-a-bounded-budget.md:51 → evidence/tag-readme-trace-observed-causal-connection.md
- kb/notes/a-linked-note-discharges-its-own-grounding-so-a-citing-note-owes.md:115 → reference/adr/079
- kb/notes/an-insufficient-summary-precedes-the-source-rather-than-replacing.md:76 → evidence/seven-documentation-cases-left-routing-and-synthesis.md
- kb/notes/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md:243 → sources/descartes-discourse-on-the-method.ingest.md
- kb/notes/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md:244 → sources/lamport-how-to-write-a-21st-century-proof.ingest.md
- kb/notes/any-symbolic-program-with-llm-calls-is-a-select-call-program.md:105 → agentic-systems/reviews/claude-code-dynamic-workflows.md
- kb/notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md:97 → evidence/commonplace-as-a-reflective-system.md
- kb/notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md:98 → sources/goedel-machines-schmidhuber.ingest.md
- kb/notes/a-proximate-target-is-checked-for-achievement-not-for-warrant.md:79 → reference/design-rationale-management.md
- kb/notes/a-proximate-target-is-checked-for-achievement-not-for-warrant.md:80 → reference/tag-readme-trace-as-self-improving-loop.md
- kb/notes/areas-exist-because-useful-operations-require-reading-notes-together.md:146 → reference/adr/004 (existence witness)
- kb/notes/a-retrieval-miss-is-a-local-reflective-path-failure.md:48 → sources/memento-skills-let-agents-design-agents.ingest.md
- kb/notes/artifacts-must-preserve-named-choice-scope.md:224 → areas-exist-because-useful-operations-require-reading-notes-together.md
- kb/notes/a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md:59 → reference/adr/042
- kb/notes/a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md:60 → reference/adr/069
- kb/notes/automated-synthesis-is-missing-good-oracles.md:58 → agent-memory-systems/agentic-memory-systems-comparative-review.md
- kb/notes/automated-synthesis-is-missing-good-oracles.md:62 → sources/geometry-of-knowledge-extending-diversity-boundaries-llms.ingest.md
- kb/notes/automating-kb-learning-is-an-open-problem.md:97 → sources/knowledge-centric-self-improvement-2607.19592.ingest.md
- kb/notes/bitter-lesson-selects-against-unearned-reach-not-against-structure.md:77 → sources/in-search-of-lost-domain-generalization.ingest.md
- kb/notes/bitter-lesson-selects-against-unearned-reach-not-against-structure.md:78 → sources/rosenfeld-risks-of-invariant-risk-minimization.ingest.md

Agentic-systems reviews. These are descriptive attestations: pinned source code cited for factual statements about what a system does. They are not generalizations, so ADR 091's origin rule does not bite:
- kb/agentic-systems/reviews/agno-agentos.md:100 → sources/how-to-recursively-improve-your-agents-….ingest.md
- kb/agentic-systems/reviews/arex-skill.md:20, :26, :28, :38 → AREX-Skill pinned files
- kb/agentic-systems/reviews/contextpilot.md:34, :35, :36 → ContextPilot pinned files
- kb/agentic-systems/reviews/eal-bench.md:20, :22, :24, :32 → eal-bench pinned files
- kb/agentic-systems/reviews/ecdysis.md:20, :26 → Ecdysis pinned files
- kb/agentic-systems/reviews/evoontology.md:20, :22, :28, :30, :32 → EvoOntology pinned files
- kb/agentic-systems/reviews/meta-n.md:34, :35, :36 → meta-n pinned files
- kb/agentic-systems/reviews/modularrsi.md:20, :26 → ModularRSI pinned files
- kb/agentic-systems/reviews/primescientist.md:20, :22, :28, :36 → PrimeScientist pinned files
- kb/agentic-systems/reviews/skilllift.md:16, :18, :20, :22, :24, :26, :28 → SkillLift pinned files
- kb/agentic-systems/reviews/swarmworld.md:17, :21, :23, :27, :29, :33, :35 → SwarmWorld pinned files
