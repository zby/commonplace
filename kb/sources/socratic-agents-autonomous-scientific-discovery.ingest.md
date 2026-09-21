---
description: "AHOIS couples causal questioning to optical experiments, offering a supervised theory-revision case without evidence of durable cross-task learning or autonomous revision of its own machinery."
source: https://arxiv.org/abs/2606.26722
captured: "2026-09-19"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 92482c85051203938ac824e2e0c2e0aa661da34647ed64c644ef1cbc56e8945b
ingested: "2026-09-19"
occasion: "Assess 2026 computational implementations and evaluations of conjecture, criticism, revision, and persistence for a learning paradigm grounded directly in Popper; distinguish epistemic commitments, implementation choices, and demonstrated effects."
type: kb/sources/types/ingest-report.md
domains: [scientific-discovery, theory-refinement, multi-agent-systems]
learning_claims: true
---

# Ingest: Socratic agents for autonomous scientific discovery in high-dimensional physical systems

## Classification

A scientific preprint reporting a five-agent architecture, experiments on a real multimode-fibre optical platform, and comparisons of criticism protocols. Xianrui Zeng and colleagues report work from the Chinese Academy of Sciences and collaborating institutions. The evidence is an author-run physical demonstration and evaluation; the captured representation is arXiv v1, dated 25 June 2026.

## Summary

AHOIS couples a hypothesis-generating agent to a physics critic constrained to ask questions instead of supply conclusions. Separate agents translate plans into instrument actions, monitor acquisition validity, and analyze data. Shared experimental state records hypotheses, assumptions, expected observations, uncertainty, actions, and results. On a supervised optical platform, the authors report discovery of useful backscattered interference encoding, adaptive scanning, modality-specific diagnosis, and adaptation of a published imaging protocol. The encoding achieved 76.97% MNIST and 83.17% Fashion-MNIST classification accuracy from 16 × 16 measurements; these demonstrate information retained by the proposed encoding, not the critic's isolated effect. Within the supplied optical setting and agent roles, Socratic criticism reportedly outperformed no reviewer, generic review, and a non-Socratic critic on reasoning and planning metrics. Human supervision includes factual correction and interpretive guidance; agent-led acquisition for protocol transfer stopped at pilot scale, with researchers collecting the larger dataset. The paper supports an implemented, supervised hypothesis-revision loop more directly than durable learning or unrestricted scientific autonomy.

## Quotes

No source quotes have been retained yet.

## Connections Found

For the occasion, AHOIS is a concrete physical-experiment counterpart to [conjectural learning](../notes/definitions/conjectural-learning.md): explicit assumptions and proposed consequences become objects of criticism and revision before further action. Its historical framing is Socratic inquiry; treating this as a Popper-compatible implementation is our comparison, not an attribution of a directly Popper-derived design. The strongest reusable connection is to [diagnostic richness](../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md). Recording expected observations alongside acquired measurements, and distinguishing detector or calibration failure from explanatory failure, gives diagnosis more to work with than a scalar score. The paper supplies a mechanism example, not an ablation of those state fields. Its criticism comparison holds the optical task and broader division of work in place, so reported gains do not establish that this five-agent decomposition is necessary or preferable to alternative representations and interfaces.

## Learning Claims (our opinion)

The source's mechanism is iterative revision of explicit physical explanations through clarification, constraint checking, causal questioning, counterexamples, and experimental feedback. In one reported dialogue, the planner abandons the assumption that sharper focusing and denser raster scanning necessarily improve measurements. It revises the explanation to include collection efficiency, detector response, object interaction, and measurement redundancy. This is a plausible candidate for conjectural learning: criticism of what the account says changes it, and the revised account informs experimental choices. It counts as learning only if that criticism improved the planner's capacity for later action. Applying an existing optical principle or selecting a denoising model, by itself, would establish use of knowledge rather than revision of that knowledge.

The learner receives instrument observations, acquisition-integrity checks, analytical results, criticism, and human correction. It can change hypotheses, experimental plans, scanning strategies, processing choices, and reconstruction code. The paper does not show corresponding revision of the five-agent partition, the available instrument interface, or the criticism protocol. As [learning inside a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) distinguishes, success within this update space does not validate the choices fixed outside it. Natural-language explanations have interpreted consequences; instrument measurements constrain their interpretation without making causal diagnosis automatic.

Shared state and recorded trajectories establish within-workflow continuity and auditability. They do not establish that revised theories are admitted to a persistent library, retrieved in later independent tasks, or improve later behavior because they were retained. Training the downstream classifiers and reconstruction networks is a separate parametric learning process, not evidence that the scientific agents learn their own reasoning method. The report therefore adds a supervised external-domain revision case to our account, while leaving recurrent learning through durable theory retention and reflective revision of the system itself unresolved.

## Extractable Value

1. **Separate epistemic commitments from their realization.** Explicit assumptions, competing explanations, rejection conditions, and revisability are compatible with a Popper-grounded learning paradigm. A questioning-only critic, five agent roles, and natural-language shared state are particular implementation choices; this paper does not establish them as philosophical requirements. This distinction makes the source useful without importing its architecture wholesale. [quick-win]
2. **Use the criticism comparison as bounded design evidence.** The four reported conditions compare no review, generic review, non-Socratic criticism, and Socratic criticism within the supplied optical setting. The Socratic condition leads on normalized consistency, plan validity, efficiency, and downstream performance. This motivates a matched experiment on questioning versus answer-giving; it does not compare alternative whole-system decompositions or establish persistence. [experiment]
3. **Retain evidence that can distinguish theory failure from measurement failure.** The shared state and integrity-monitor role make detector noise, saturation, calibration drift, and explanatory error separable candidates. Relative to the diagnostic-richness note, the contribution is a concrete physical counterpart to software traces, with no controlled estimate of the retention mechanism's effect. [quick-win]

## Limitations (our opinion)

The captured full main paper refers important details to Supplementary Information that is not included here: underlying language models, prompts, permissions, representative trajectories, confidence intervals, and sample sizes. The report cannot establish matched inference budgets, evaluator independence, scoring reliability, or statistical uncertainty for the criticism comparison. The reported ordering of questioning types by mean utility is not enough to infer isolated causal effects of each question class. More structured prompting, additional deliberation, or human guidance remain possible contributors to the reported gains.

The paper calls its rubric dimension uncertainty calibration, but describes judging whether observations, inferences, and unresolved claims are distinguished. That is not itself a probabilistic calibration test. The optical classifier results test whether measurements preserve useful information; they do not directly measure the correctness or novelty of every mechanistic explanation. The architecture operates in a known physical domain with established constraints, and the authors explicitly stop short of claiming discovery of new physical laws.

Human input reaches beyond emergency vetoes: Figure 5 assigns supervisors factual correction and guidance toward coherent physical explanations. Bulk acquisition for the protocol-transfer experiment was researcher-run. These boundaries prevent reading the demonstration as independent completion of the whole scientific workflow. Neither the implemented code nor experiments were independently inspected or executed for this ingest. The results remain author-reported, and there is no demonstrated cross-task retention or test of replacing the fixed agent organization.

## Recommended Next Action

Review the existing [conjectural-learning definition](../notes/definitions/conjectural-learning.md) against AHOIS as a candidate supervised external-domain example, requiring an identifiable explanation–revision–decision episode before promoting it as evidence and keeping durable retention explicitly unestablished.
