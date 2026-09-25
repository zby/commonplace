---
description: "Prove2Me separates immutable theorem statements from proofs to coordinate agents, with human audits of meaning and case studies that do not isolate harness effects."
source: https://arxiv.org/abs/2608.28433
captured: "2026-09-24"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: dd52c9fd8cf0f7c74705d34dd00f288e543ba886f2aaa86f1591486a286adcce
ingested: "2026-09-25"
type: kb/sources/types/ingest-report.md
domains: [formal-verification, multi-agent-coordination, knowledge-reuse, learning]
learning_claims: true
---

# Ingest: Prove2Me: An Open Collaborative Platform for Scaling Math Formalization

## Classification

A research preprint describing a math-formalization platform, its coordination mechanisms, and completed missions. The outcome evidence consists of case studies rather than a controlled evaluation. Authors Shuze Chen, Kunal Marwaha, Xiaoyang Lu, Henry Yuen, and Tianyi Peng report on their own platform from university affiliations; their direct design knowledge does not supply independent evaluation.

## Summary

[Prove2Me](https://arxiv.org/abs/2608.28433) organizes decentralized formalization around immutable Lean theorem statements, separately submitted proofs, and human-audited missions. A proof must match its target's type in a pinned verification environment. Proof-sketches may import unproved statements, establishing conditional dependencies that close when their supporting lemmas are proved. Canonical milestones align contributors, while a searchable theorem library makes individual results reusable across missions. Humans check the mission's definitions, goal, and milestones for correspondence to the intended mathematics, assisted by an agent that translates Lean back into ordinary mathematical notation without seeing the original source. Four case studies report project-scale developments, including 151,000 lines produced by six agents, but different tasks, model generations, and billing conventions prevent attributing efficiency to the harness. The source's strongest contribution for Commonplace is an explicit separation between composition guarantees, semantic auditing, and shared reusable knowledge.

## Quotes

No source quotes have been retained yet.

## Connections Found

The platform supplies a concrete architectural example for [coordination guarantees](../notes/agent-orchestration-needs-coordination-guarantees-not-just.md): immutable statement interfaces and type-checked proof admission let independent contributions compose without changing what existing dependents assume. This guarantee is conditional on closure of imported obligations in the pinned Lean environment; an accepted sketch with open imports is not a completed proof. The case studies establish reported use of this arrangement, not its causal superiority over other coordination designs.

It also operationalizes the [formalization boundary](../notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md). Lean checks consequences of formal statements; the captain's review checks whether those statements express the intended mathematics. Restricting that semantic review to the mission core bounds what humans must inspect while agents expand the intermediate proof graph. The read-back procedure relocates part of the interpretation work to another agent and leaves the human responsible for the correspondence judgment.

## Learning Claims (our opinion)

The paper calls its discussion and correction mechanisms multi-agent continual learning. Agents share progress and reasoning, import earlier results, and can disprove proposed theorems. Its specific example is a Gotsman–Linial formalization used in one agent's proof-sketch, disproved by another agent, and replaced with a formulation that adds a missing boundary condition; the corrected theorem then closes the branch. This is a reported instance of criticism changing a retained statement and subsequent proof work, rather than evidence of model-weight training.

Our interpretation is that the episode supplies a local example consistent with [conjectural learning](../notes/definitions/conjectural-learning.md): an operative conjecture is criticized on its content, replaced, and used successfully. The theorem's explicit hypotheses make the repair [addressable](../notes/definitions/addressable-theory.md). Immutability of an individual stored statement does not prevent criticism or replacement by a new statement. The paper does not establish a general improvement in later mission performance, nor isolate the benefit of retaining criticism from that of simply adding a usable lemma.

The effective revision space includes new theorem statements, alternative proofs, dependency choices, and shared explanations. The published mission core and verification environment remain fixed for the proof work described. As in [learning inside a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), success within that space does not establish that the core faithfully expresses the source or that the platform's chosen decomposition is preferable to alternatives. Semantic auditing addresses the first question separately; the case studies do not test the second. The learning example does not require changing Commonplace's definition, but makes replacement of immutable knowledge objects a useful instance of revision.

## Extractable Value

1. **Separate stable interfaces from alternative solutions.** The immutable theorem statement is the shared contract; agents can supply different proofs without changing it. Conditional proof-sketches expose unfinished dependencies rather than silently treating them as established knowledge. This strengthens the existing coordination-guarantee account with a precise formal example, bounded by the Lean environment and eventual closure of obligations. [quick-win]
2. **Bound semantic auditing by a trusted target.** Humans review the goal, definitions, and milestones; the verifier checks the larger proof graph against those targets. This is a reusable design distinction between checking intended meaning and checking consequences, although ordinary prose KBs lack Lean's compositional proof guarantee. [quick-win]
3. **Retain a content-level correction episode.** The disproved lemma and its corrected successor illustrate how shared, addressable statements can carry criticism into subsequent work even when stored objects cannot be edited. The evidence is one reported episode, with broader transfer still unmeasured. [just-a-reference]

## Limitations (our opinion)

The reported missions are not matched comparisons. Corpora, difficulty, working patterns, and model generations differ, and the table compares metered API expenditure with consumer subscription prices. Lines of Lean are a size measure, not a common measure of mathematical difficulty or useful coverage. Stronger models or selected tasks could explain the small agent counts without a harness advantage. No ablation isolates immutability, milestones, search, discussion, or proof decomposition, so the results do not establish which component improves throughput or whether another decomposition would work better.

The semantic audit remains fallible. Requiring a human to confirm each statement records participation, not demonstrated understanding, and a source-blind read-back can still mistranslate Lean. The paper gives no measured audit error rate. Kernel acceptance addresses formal validity within the chosen environment, not the faithfulness of the encoded claim, as the formalization-boundary connection above requires.

This ingest analyzes the paper without inspecting or executing platform code. The described admission checks, dependency closure, and environment isolation are therefore source claims, not implementation findings. The paper itself leaves large-corpus retrieval, decentralized coordination, adversarial submissions, and extraction of human-readable insight as open problems. Those gaps limit claims of internet-scale reliability beyond the reported missions.

## Recommended Next Action

Add Prove2Me as a bounded worked example to [Agent orchestration needs coordination guarantees, not just coordination channels](../notes/agent-orchestration-needs-coordination-guarantees-not-just.md), explaining immutable theorem interfaces and conditional dependency closure while keeping the fixed verification environment and separate human semantic audit explicit.
