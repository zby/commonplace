---
description: "Discovery Foundation Models proposes revisable research state and validated skill transfer; its GALILEO case supports a narrower physical feedback loop, not the full framework."
source: https://arxiv.org/abs/2609.15973
captured: "2026-09-24"
ingested: "2026-09-25"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: aa06bed8529e3cadf495573f19097aa594b616db41b3c30cc118404e87e27cfc
learning_claims: true
type: kb/sources/types/ingest-report.md
domains: [automated-science, learning-systems, agent-memory, evaluation]
---

# Ingest: Discovery Foundation Models: Toward Open-Ended Discovery Intelligence

## Classification

This scientific preprint primarily proposes a capability definition, system organization, training objectives, and evaluation protocol. It also summarizes an empirical therapeutic-discovery case, GALILEO, without supplying that study's full experimental record.
Author: Ling Yang, Zhenfei Yin, and Yingcheng Wu present the framework and solicit scientific collaborations. The retained source is arXiv version 1; it does not establish peer review or independent validation of the proposed framework.

## Summary

Discovery Foundation Models defines discovery capability as constructing and revising problems, representations, hypotheses, interventions, and validation procedures, then improving those operations across tasks. Its Zetema organization keeps these objects in linked research state, separates predictions from external observations, and promotes candidate research lessons into reusable Discovery Skills only after transfer tests. Training combines trajectory supervision, verification, predictive modeling, scientific feedback, and skill selection; evaluation separates current knowledge progress from future research capability. These are specifications rather than a reported general DFM training run or comparative benchmark. The GALILEO case describes biological feedback changing peptide-design policies, hypotheses, and assays over five optimization rounds, plus reported reuse of a resulting design grammar. That case remains bounded by its therapeutic domain, molecular modality, experimental interfaces, and objectives; it does not establish the general framework or cross-domain discovery transfer.

## Quotes

No source quotes have been retained yet.

## Connections Found

The paper is a methodological companion to [A checked outcome licenses retaining an episode, not abstracting its explanation](../notes/checked-outcome-licenses-episode-retention-not-abstraction.md). Its distinction between episode evidence and a candidate research lesson makes the same attribution problem explicit: success may depend on privileged information or an unrecorded human correction. Its proposed transfer controls add an evaluation design, not independent empirical confirmation of the note.

It compares with [Theory builder](../notes/definitions/theory-builder.md) by assigning capability to the declared system of models, retained state, tools, validators, environments, and participating humans. The definitions differ: DFM requires seven coupled discovery capabilities and transfer across tasks and domains, whereas the KB definition centers continuing responsibility for addressable tentative theories. A capability specification alone does not establish that a deployed instance meets either definition.

Compared with [AutoRA](./autora-automated-research-assistant.ingest.md), which composes research components around user-supplied variables and methods, DFM explicitly makes formulation and representation changes research operations. This is a contrast of proposed scope. The bounded GALILEO case does not demonstrate that a broader decomposition outperforms AutoRA's or that the full DFM organization is necessary.

## Learning Claims (our opinion)

The source distinguishes revision within an investigation from improvement across investigations. Within-task revision uses external outcomes to change the implicated problem, representation, hypothesis, measurement, or intervention. Cross-task learning distills attributed experience into a Discovery Skill: a state-dependent trigger, a proposed operation, an expected effect, and validation evidence. Later counterexamples can narrow the trigger, weaken the skill, or remove it. The proposed training procedure can also change policy, verifier, predictive-model, and retrieval parameters; fixed weights are not assumed.

This is compatible with [conjectural learning](../notes/definitions/conjectural-learning.md) where an explicit hypothesis or skill guides decisions through its content, remains open to criticism, and the process improves future capacity. Parameter updates or a stored skill alone do not establish those conditions. Zetema's linked assumptions, validity ranges, evidence, and revisions specify support for [addressable theories](../notes/definitions/addressable-theory.md), but their storage format does not establish that a learner actually diagnoses or repairs the relevant part. The paper adds a concrete way to test the distinction between possessing research advice and improving research decisions through it.

GALILEO's reported reopening of rejected motif organizations under revised hypotheses is more informative than a final successful peptide: it describes criticism changing later actions. The reported grammar transfer suggests a subsequent use, but the summary lacks matched controls isolating the effect of the retained rule from selection, additional experimentation, or human contributions. It is suggestive evidence for conjectural learning by the coupled system, not a controlled demonstration of that causal mechanism or general discovery improvement.

The framework explicitly addresses [learning inside a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) by exposing representations and evaluators to revision. Nevertheless, its seven capabilities, proposed state fields, available experimental interfaces, and training signals are design commitments. No reported comparison establishes that they admit all consequential corrections or outperform alternative organizations. GALILEO demonstrates reported adaptation within substantially supplied domain and experimental boundaries.

## Extractable Value

1. **Test a promoted lesson against competing memory explanations.** Section 7.4 proposes no-memory, fact-only, full-trajectory, successful-solution, domain-skill, and Discovery Skill controls under matched resources. Hold out research mechanisms as well as surface wording and test cases where the skill should not apply. This supplies a concrete experimental extension to the existing episode-versus-abstraction note; it is a proposed protocol, not a demonstrated benefit of skill memory. [experiment]
2. **Keep current research progress separate from future capacity.** A falsified mechanism or a nonreplicating effect can be a supported episode result without establishing improved future discovery behavior. Reporting both targets prevents successful research outputs from silently serving as evidence for a learning method. [quick-win]
3. **Preserve the relation a lesson claims.** The trigger–operation–expected-effect–validation structure makes a candidate lesson testable and allows negative evidence to limit when it applies. Linked alternatives, failed branches, and human interventions help distinguish that relation from a retrospective success story. This operationalizes an existing KB distinction without showing that this particular schema is superior. [quick-win]
4. **Retain GALILEO as a bounded candidate learning case.** The reported five-round peptide loop connects physical outcomes to hypothesis and design-policy revision, including recovery of previously rejected branches. Its fixed domain, modality, objectives, and experimental interfaces limit reuse; assessing the claimed grammar transfer requires the primary study and its controls. [deep-dive]

## Limitations (our opinion)

The formal losses and reference algorithm specify how capabilities might be trained. The paper reports no general DFM training run, framework ablation, or matched comparison of research-state representations. Named capabilities and explicit records could improve observability without producing better discovery. Ordinary iterative experimentation, expert correction, or additional resources could explain the summarized case's progress; the present account does not isolate the proposed organization as its cause.

GALILEO is attributed to Jiang et al. (2026), but the retained reference list supplies no corresponding full entry. Section 5.7 reports biological assays, five optimization rounds, and transfer into other peptide-design workflows without full methods, sample sizes, uncertainty estimates, or the matched transfer comparisons proposed later in the paper. Those reports are insufficient to assess effect reliability, independent replication, or clinical efficacy. Human-executed specialized assays also belong in the attribution boundary; calling the workflow autonomous does not assign all consequential work to the model.

The most reusable material is therefore the evaluation design. Even there, process scores depend on judgments about correct attribution, useful representation, scientific value, and appropriate revision. The paper identifies independent validation as necessary but does not demonstrate a general oracle for those judgments. Permitting evaluator revision does not itself establish that the revised evaluator measures progress more faithfully.

## Recommended Next Action

Extend [A checked outcome licenses retaining an episode, not abstracting its explanation](../notes/checked-outcome-licenses-episode-retention-not-abstraction.md) with the paper's matched memory and transfer controls as a proposed way to test reusable lessons, explicitly preserving their unexecuted status in this source.
