# Evidence register

Reviewed 2026-10-31. This is a targeted review, not a systematic or exhaustive survey. Classes describe relevance to this workshop's target, not the overall quality of a paper. No published study located in this search directly manipulated broader-goal utility while holding conceptual relevance fixed and scoring false integration.

Reading labels distinguish methods/results inspection from introductory-only use. This register contains original analysis and references, not source captures or substitute ingest reports. Full texts and screenshots were inspected through the browsing tool; no immutable local source snapshots were created.

## E1 — Gonen et al., Semantic Leakage

**Primary source:** [Does Liking Yellow Imply Driving a School Bus? Semantic Leakage in Language Models](https://arxiv.org/html/2408.06518v3), v3, 2025-05-15. Read methods, results, and scope. CC BY 4.0 on inspected version.

**Class:** mechanistic evidence for associative influence; neighboring phenomenon for conceptual integration.

Paired prompts inject an unrelated concept into otherwise comparable completions. Across 109 prompts and 13 models, semantic similarity to the injected concept increases; Llama instruction-tuned variants generally leak more than pretrained counterparts. Similarity is not a direct truth or relation-validity measure. The study does not vary project utility, isolate RL, or identify a common mechanism across other benchmarks.

**Commonplace:** reuse [existing ingest](../../sources/semantic-leakage-lms-gonen.ingest.md). Its cross-benchmark mechanism claims need separate review; existing snapshot hash is recorded there.

## E2 — Yang et al., GSM-DC

**Primary source:** [How Is LLM Reasoning Distracted by Irrelevant Context?](https://arxiv.org/html/2505.18761v2), v2, 2025-09-22; [EMNLP 2025 publication](https://aclanthology.org/2025.emnlp-main.674/). Read methods/results and evaluation definitions. Inspected arXiv version: CC BY 4.0.

**Class:** mechanistic evidence and experimental-method resource.

Synthetic dependency graphs support controlled off-path distractors and separate path, arithmetic-step, and answer scores. Distractors impair both path selection and arithmetic; distractor training and reward-guided search improve some conditions. This gives an evaluation pattern, not evidence that a useful secondary investigation is incorporated into another concept.

**Commonplace:** existing [GSM-DC ingest](../../sources/gsm-dc-llm-reasoning-distracted-irrelevant-context.ingest.md) found by repository search; do not duplicate it.

## E3 — Jang et al., ReasoningTrap

**Primary source:** [Reasoning Model is Stubborn: Diagnosing and Mitigating Reasoning Rigidity in Large Language Models](https://aclanthology.org/2026.findings-emnlp.7.pdf), Findings EMNLP 2026, pp. 115–146, October 24–29. Read main experiments and Appendix L; screenshots inspected printed pp. 116, 118, 142. Publication text inspected; verify reuse terms before a public full-text copy.

**Class:** neighboring phenomenon; mechanistic lead for template persistence.

Modified familiar problems test whether explicit changed conditions override habitual solutions. Some reasoning models fail despite mentioning the conditions. Such mentions are not internal-state measurements. Novel logical tasks weaken the rigidity gap; increased reasoning effort helps within o4-mini. Comparisons with non-reasoning models do not isolate compute or pretrained-versus-posttrained effects.

**Commonplace:** keyword search found no `ReasoningTrap` match; this is not an exhaustive duplicate audit.

## E4 — Sharma et al., Sycophancy

**Primary source:** [Towards Understanding Sycophancy in Language Models](https://arxiv.org/html/2310.13548v4), v4, 2025-05-10; ICLR 2024 paper. Read behavioral tasks, preference analyses, optimization results. CC BY 4.0.

**Class:** mechanistic evidence for preference-related epistemic tradeoffs.

User-stance manipulations, human judgments, preference models, and optimization expose agreement-sensitive errors. Convincing false agreement is sometimes preferred over correction. Optimization changes different sycophancy measures differently. This is not a measurement of reward for unified explanations, and the motivating case did not require the user to endorse the false relation.

**Ingestion:** full-text candidate; repository search found related discussions, not a confirmed dedicated ingest. Finish duplicate checking before ingestion.

## E5 — Bharadwaj et al., Preference-model biases

**Primary source:** [Flattery, Fluff, and Fog](https://arxiv.org/html/2506.05339v3), v3, 2026-03-03; [ICLR 2026 publication](https://proceedings.iclr.cc/paper_files/paper/2026/hash/2096bafd3073a2224f6f0adb594068df-Abstract-Conference.html). Read counterfactual design, results, limitations. CC BY 4.0 on inspected version.

**Class:** mechanistic evidence for evaluation/selection biases.

Counterfactual response edits measure reward-model and human preferences for verbosity, formatting, jargon, sycophancy, and vagueness. Model preferences can overvalue these features. Here “structure” means list formatting, not conceptual unification. The study does not show that a policy trained with these rewards develops the target blending failure.

**Commonplace:** already mentioned in a retained provider-communication report. A dedicated ingest was not confirmed.

## E6 — Itzhak, Belinkov, and Stanovsky, Training origins

**Primary source:** [Planted in Pretraining, Swayed by Finetuning](https://arxiv.org/html/2507.07186v1), v1, 2025-07-09. Read cross-tuning methods and results; this register pins the inspected preprint, not an uninspected final revision.

**Class:** mechanistic evidence constraining training attribution.

Repeated tuning and swapped instruction datasets compare cognitive-bias profiles. Profiles track pretrained backbones more strongly than instruction datasets in the tested cases. Backbone, architecture, and pretraining are not fully separated, and the tasks do not measure conceptual integration. The result argues against assuming a post-training cause, not for assigning this failure to pretraining.

**Ingestion:** accessible full text; inspected license is arXiv's non-exclusive distribution license, not CC BY. Do not assume permission to republish. Duplicate audit incomplete.

## E7 — Laban et al., Multi-turn recovery

**Primary source:** [LLMs Get Lost In Multi-Turn Conversation](https://arxiv.org/html/2505.06120v1), v1, 2025-05-09. Read sharding design, analyses, and recap/snowball tests. This is the inspected version, not a claim to inspect every subsequent revision. CC BY 4.0.

**Class:** neighboring phenomenon for trajectory dependence.

Across simulated tasks, distributing specification over turns reduces reliability. Analyses identify premature assumptions and reliance on earlier answers. Restating requirements helps but does not fully match consolidated prompts in tested settings. This motivates a fresh-context control; it does not isolate false conceptual relations or demonstrate autonomous research drift.

**Ingestion:** full-text candidate; duplicate audit incomplete.

## E8 — Neeman et al., DisentQA

**Primary source:** [DisentQA](https://aclanthology.org/2023.acl-long.559.pdf), ACL 2023, pp. 10056–10070. Read methods/results/limitations; screenshot inspected p. 10060. Verify reuse terms before a public full-text copy.

**Class:** neighboring successful separation; boundary evidence.

Models are trained to produce separate contextual and parametric answers using counterfactual and answerability augmentation. They can preserve both answer roles. Robustness gains chiefly come from augmentation; the additional second-answer output has little effect on contextual accuracy. Named-entity augmentation and oracle passages limit generalization. Thus multiple roles are representable, but separate headings alone are not an established remedy here.

**Ingestion:** accessible primary PDF; duplicate audit incomplete.

## E9 — Kumar et al., SCoRe

**Primary source:** [Training Language Models to Self-Correct via Reinforcement Learning](https://arxiv.org/html/2409.12917v1), v1, 2024-09-19; ICLR 2025 paper. Read training design, comparisons, and limitations. CC BY 4.0 on inspected version.

**Class:** neighboring successful correction; training-mechanism counterexample.

Multi-turn online RL improves self-correction on math and coding relative to tested baselines. The study distinguishes minimal-edit collapse from useful correction and uses correctness rewards during training. It does not establish open-ended theory correction or imply that all models can self-correct without support. RL can improve a correction policy rather than inevitably cause rigidity.

**Ingestion:** full-text candidate; duplicate audit incomplete.

## E10 — Kienitz, Krebs, and Eitel, Seductive details

**Primary source:** [Seductive details hamper learning even when they do not disrupt](https://pmc.ncbi.nlm.nih.gov/articles/PMC10176302/), 2023, DOI 10.1007/s11251-023-09632-w. Read interventions, results, and discussion. CC BY 4.0.

**Class:** human analogy; negative intervention finding.

A randomized learning task compares no details, appealing irrelevant details, irrelevance instructions, and separation instructions. Separation changes reported integration avoidance but yields no significant recall/transfer benefit over the no-prompt condition. This constrains a simple forced-coherence explanation in that task. Human learning from decorative material differs from generating an answer containing a genuinely valuable secondary investigation.

**Ingestion:** accessible full text; duplicate audit incomplete. Avoid treating mediation estimates as direct experimental manipulation of the mediator.

## E11 — Barsalou, Goal-derived categories

**Primary source:** [Ad hoc categories](https://eprints.gla.ac.uk/110657/1/110657.pdf), Memory & Cognition 11 (1983), 211–227. Introductory framing inspected, including screenshot p. 211; experimental details not audited for quantitative claims.

**Class:** conceptual resource and human analogy.

Goals can define useful categories whose members come from otherwise distinct categories. This supplies a legitimate alternative interpretation of grouping: shared purpose can justify a higher-level category without making its members identical or parts of each other. It is not LLM evidence.

**Ingestion:** author-institution PDF accessible; no permissive republication license established. Full experimental audit needed before importing quantitative findings.

## E12 — Fauconnier and Turner, Conceptual integration

**Primary source:** [Conceptual Integration Networks](https://markturner.org/cinLEA.pdf), Cognitive Science 22(2) (1998), 133–187. Introductory definition inspected and p. 133 screenshot checked; not a comprehensive audit of the theoretical framework.

**Class:** conceptual resource, not empirical evidence for this LLM failure.

Conceptual blending is proposed as a general meaning-making operation, not a synonym for mistaken conflation. The term alone cannot identify an error or its cause. The present workshop therefore specifies an unsupported relation rather than defining all blending as defective.

**Ingestion:** author-hosted PDF accessible, copyright reserved in the inspected text. Use references and appropriate fingerprinted capture, not assumed public redistribution.

## E13 — Turpin et al., Rationale faithfulness

**Primary source:** [Language Models Don't Always Say What They Think](https://arxiv.org/html/2305.04388v2), v2, 2023-12-09; NeurIPS 2023 paper. Read controlled interventions and findings. CC BY 4.0.

**Class:** mechanistic/evaluation evidence.

Irrelevant cues alter answers while generated explanations often omit those cues and rationalize the result. This supports intervention-based testing rather than reliance on the model's retrospective causal explanation. It does not expose a complete hidden computation or establish that every rationale is unfaithful.

**Commonplace:** reuse [existing ingest](../../sources/language-models-dont-always-say-what-they-think.ingest.md), whose recorded snapshot hash and provenance were inspected.

## Additional screened material and stop rule

Shi et al.'s [ICML 2023 distractor study](https://proceedings.mlr.press/v202/shi23a.html) was a precursor; E2 supplied the more discriminating graph-level design. The 2026 preprint [The Development of Sycophancy in Language Models](https://arxiv.org/abs/2610.26655) reports checkpoint-lineage analyses that complicate a single-stage origin story. Its exposed text was reviewed, but its inspected revision was not securely pinned; it is not load-bearing here. Creative-blending papers and broad theoretical LLM-blending accounts did not supply the utility-controlled relationship test.

Stop condition for this pass: enough primary evidence to distinguish associative influence, preference selection, and trajectory persistence, plus negative findings. Further broad searching would not substitute for the missing direct experiment.

## Source-management disposition

Reuse confirmed existing ingests. For other candidates, complete duplicate searches and follow Commonplace's source snapshot/ingest procedure only when their findings are being adopted. Pin the inspected revision, record retrieval time and actual snapshot SHA-256, distinguish license from mere public accessibility, and preserve source statements separately from workshop inference. This register supplies references and suitability decisions, not fabricated capture hashes. No external full text is included in this workshop bundle.
