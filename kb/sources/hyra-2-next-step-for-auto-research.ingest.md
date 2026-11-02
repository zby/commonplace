---
description: "Tencent's Hyra 2.0 post argues auto-research should build reusable tools, not resample answers; graded Books memory and evidence-bearing review, compounding claimed but unmeasured"
source: https://hy.tencent.com/research/hyra2
captured: "2026-11-02"
capture: publicDetail-api-json-content
capture_scope: full-source
genre: tool-announcement
snapshot_sha256: 4ff965ab63ce537efeb1aa11b5bdd45691f6966da5707de9fad0d5642526b146
ingested: "2026-11-02"
type: types/ingest-report.md
domains: [automated-research, research-harness, tool-building, research-memory]
tags: [self-improving-systems, continual-learning, agent-memory]
learning_claims: true
---

# Ingest: Hyra 2.0: The Next Step for Auto Research

## Classification

This is a first-party announcement of an agent harness and the tools it produced, framed by a position argument about where automated research should go. It describes the architecture in prose and reports vendor-run benchmark results per tool; it releases no harness code, no ablation, and no comparison of the harness against a simpler loop. The capture is the English text of the post; images and the Chinese version were not captured.
Author: the Hyra team at Tencent Hunyuan, who build both the harness and the Hy models it uses. They have direct access to the work they describe and a commercial interest in its framing.

## Summary

Hyra 2.0 argues that automated research should move from "keep sampling until you hit a solution" toward improving tools, because an improved tool benefits every later task that uses it while a single answer does not. It divides tools into symbolic ones (code, rules, workflows, pipelines) and parameterized ones (trained models), and ranks them by generality up to a system that trains models. The harness organizes research into three levels: Overall (talks to humans, sets priorities), Mission (owns one research problem and its conclusions) and Worker (reads code, runs experiments, may challenge the Mission). A persistent task queue schedules Workers by priority, dependency and resource limits. A Research Board records ideas, findings and decisions; issues needing action are sent as messages that require an explicit response. Workers must attach evidence such as code versions, logs and execution traces to completion reports, and a fresh Review Worker receives the original problem and evidence before the producing Worker's conclusion. Project state, per-agent hierarchical memory and a shared knowledge base called Books are stored separately. Books entries state method, rationale, applicability conditions and evidence, and are graded Observation (single experiment), Verified (independently reproduced) or Convention (human-confirmed). Retrospectives distil transferable methods into skills. Reported outputs are per-tool results: a 1.96M-parameter inverse-folding model claimed 57 times faster than ProteinMPNN, a protein language model, a family of force-field models on an accuracy–speed Pareto frontier among 16 public models, a proof workflow credited with two verified conjectures, a qLDPC code construction and verification toolkit, a simulated robot-hand design, and processor tuning and bug finding for XiangShan. The post claims a recursive self-improvement loop through Hy model development, but every reported number measures one tool against its own benchmark.

## Quotes

No source quotes have been retained yet.

## Connections Found

The source's main role in this KB is as a frontier-lab practitioner case for [an optimal long-run learning strategy invests in its own machinery](../theory/an-optimal-long-run-learning-strategy-invests-in-its-own-machinery.md): it explicitly moves effort from single answers to reusable tools and justifies the move by amortisation over later tasks. It illustrates that allocation; it does not measure its return over any horizon. On the evidence for that return it is a counterpoint case for [compounding is tested in later improvement, not by the accepting metric](../theory/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md): the post asserts that better tools make a stronger tool-building system, yet reports only accepting metrics per tool, with no later-episode measure and no causal trace. The [Compound Engineering plugin review](../agentic-systems/reviews/compound-engineering-plugin.md) supplies the split this claim needs between a compounding mechanism and a compounding claim.

Its memory design is the most transferable part. Books' Observation / Verified / Convention grades are a deployed staged-authority scheme, evidence for [trace-extracted memory earns authority per operation, not at capture](../theory/trace-extracted-memory-earns-authority-per-operation-not-at-capture.md), and its human approval for shared-knowledge synchronisation and conventions is evidence for [continual learning requires governing behaviour-changing writes](../theory/continual-learning-requires-governing-behaviour-changing-writes.md). Its three separate stores are evidence for [active work state is not retrospective memory or chat history](../theory/active-work-state-is-not-retrospective-memory-or-chat-history.md), and its queue, required responses and evidence-bearing completion reports are evidence for [agent orchestration needs coordination guarantees, not just coordination channels](../theory/agent-orchestration-needs-coordination-guarantees-not-just.md). All four supports are design descriptions, not outcome measurements. Among sources, [Agora](./agora-git-as-shared-memory-for-collective-autoresearch.ingest.md) grades shared research memory by downstream reproduction over an immutable graph, and the [Hypothesis Evolution Protocol](./hypothesis-evolution-protocol-auditable-ai-scientists.ingest.md) enforces evidence attachment through tools where Hyra states it as policy.

Its symbolic/parameterized tool taxonomy compares with [treat continual learning as representational-form coevolution](../theory/treat-continual-learning-as-representational-form-coevolution.md): the two categories map onto the symbolic and distributed-parametric [representational forms](../theory/definitions/representational-form.md), but Hyra also retains natural-language Books entries and skills, calls skills tools, and has no category for them. Its claim that accelerating an existing model is easy because feedback is fast, and that slow verification is a bottleneck to be turned into a tool target, is evidence for [the boundary of automation is the boundary of verification](../theory/the-boundary-of-automation-is-the-boundary-of-verification.md). Its Review Worker ordering compares with [reasoning production is not reasoning evaluation](../theory/reasoning-production-is-not-reasoning-evaluation.md): showing the reviewer evidence before the conclusion addresses anchoring, but not a reviewer that reconstructs the answer instead of checking the reasoning, and it may invite that failure. Its "class of tasks" framing compares with [factory learning](../theory/factory-learning-is-experience-responsive-retention-that-improves.md), which would additionally require a declared family and evidence that later production depends on the retained change. [Defazio's theory-driven AI research](./a-new-era-of-theory-driven-ai-research-2084779496549548323.ingest.md) shares the rejection of sample search as the end state but proposes predictive theory where Hyra proposes tools.

## Learning Claims (our opinion)

**Mechanism on its own terms.** Hyra calls its learning "continual learning": preserving methods developed during research so later projects can use and improve them. Three paths carry it. Within a project, Workers' evidence and review results update per-agent memory (current hypotheses, ruled-out approaches, next steps) and the Research Board. Across projects, lessons become Books entries graded by reproduction and human confirmation, and retrospectives distil methods into skills that are "revised and refined through use". At the outermost level, Hyra improves training infrastructure, data pipelines and inference for Hy models, which are meant to become Hyra's own tools: the post's recursive self-improvement claim.

**Mapping onto Commonplace concepts.** The Books and skills paths are learning through retained artifacts outside weights, the continual-learning case. The Books grades put authority on a promotion path rather than at capture, as the KB's trace-extracted-memory account requires. The Hy-model path is a cross-form loop: symbolic and natural-language work that changes a parametric component. The taxonomy is a partial fit. Hyra's "parameterized tools" match the distributed-parametric form, but "symbolic tools" merges executable code with natural-language skills, which the KB separates because they are consumed and criticised differently. Whether the RSI loop counts as a [self-improving system](../theory/definitions/self-improving-system.md) depends on a boundary the post does not declare: Hy model training runs outside the harness, through the Hunyuan team and its approval gates.

**Tools as tentative theories.** Each Hyra tool encodes a conjecture: the inverse-folding model conjectures that one architecture predicts sequences for a class of proteins, and a force-field model conjectures an interatomic potential for a class of materials. In the KB's terms every such tool is a [tentative theory](../theory/definitions/tentative-theory.md), since that status has no required form, and the amortisation argument holds only if the tool's generality conjecture survives on later tasks. Each reuse tests the scope claim, which restates the compounding-is-tested point from the tool's side. The differences from a stated conjecture are differences of form. [Codification](../theory/definitions/codification.md) fixes a tool's predictions by computation, so a benchmark is a mechanical and repeatable test, though whether the code captures the intended claim stays open. Hyra's symbolic and parameterized categories track [addressability](../theory/definitions/addressable-theory.md): code has parts a failure can be traced to, while a trained model can only be replaced whole or retrained. And Hyra states scope for its natural-language methods but not for its tools: Books entries carry applicability conditions and are graded by reproduction, while a tool receives one benchmark number and no recorded route to refutation. The post's missing natural-language category is where its explicit theories live; its tools carry conjectures whose scope is tacit.

**Theory-builder conditions, judged separately** (against [theory builder](../theory/definitions/theory-builder.md)):

- *Localized content:* met by design description. Books entries state method, rationale and applicability conditions, and memory records name hypotheses and ruled-out approaches.
- *Consumption:* plausible, not shown. The post says skills are used in subsequent tasks and that lessons from one training run help later runs, but gives no case where a retained entry changed a decision.
- *Criticism:* the strongest condition. Review Workers check completion claims against evidence and may narrow a conclusion; Workers may challenge the Mission; Books entries are revised as evidence changes and promoted only after independent reproduction. This is criticism aimed at stated units. Evidence is design description only.
- *Iteration:* described. Review findings "must be faithfully retained", and the post says review flaws can become automated checks. No round-to-round trace is reported.

Persistence is claimed at the highest grade, across problems and projects through Books and skills. Learning in Simon's sense, improved capacity for later action, is asserted but not measured. The per-tool results show that the harness produced good tools; they do not show that retained Books entries or skills made later projects better or cheaper, and they do not distinguish the harness's contribution from the underlying model's.

**Fixed decomposition.** The Overall/Mission/Worker hierarchy, the three-store memory split, the Books grades and the human approval gates are fixed outside anything the post shows Hyra revising. The results test improvement inside that decomposition, at best; they give no evidence for the decomposition itself against a simpler loop or an alternative split, as [learning inside a fixed decomposition inherits its mistakes](../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) predicts.

**What it adds.** No revision to the KB's concepts is required. The source adds a deployed instance of three things the KB already argues: staged authority for research memory, separation of active work state from reusable knowledge, and reflective investment justified by amortisation. It also adds one productive mismatch: a practitioner taxonomy of tools that omits the natural-language form while relying on it.

## Extractable Value

1. **A frontier-lab compounding claim backed only by accepting metrics** -- Hyra states the reflective-investment rationale explicitly and reports seven tool results, none of which measures later-episode gain from earlier tool building. It is a current, clean case for the compounding-is-tested note's distinction and for a bounded `evidenced-by` reading of the long-run learning strategy note. [quick-win]
2. **Books' three-grade authority scheme** -- Observation (one experiment), Verified (independently reproduced) and Convention (human-confirmed), with method, rationale, applicability conditions and evidence required per entry. It is a compact, deployable design for research memory and adds a third instance beside Agora and HEP for a possible evidence note on staged authority in auto-research systems. Design description only. [experiment]
3. **Evidence-first review ordering** -- a Review Worker gets the original problem and evidence before the producing Worker's conclusion, to reduce anchoring. This is a concrete, cheap variant for Commonplace's own review gates, but its tradeoff against reconstruct-instead-of-check failures is untested. [experiment]
4. **The tool taxonomy's missing natural-language form** -- Hyra splits tools into symbolic and parameterized while depending on prose skills and Books entries. It is a ready example for the representational-form coevolution note of why a two-form taxonomy hides the form that carries most retained lessons. [quick-win]
5. **Verification speed as the named bottleneck** -- the claim that model acceleration is easy because feedback is fast, and that slow verification should become a tool-development target, with HyQEC and the XiangShan fuzzing and TLA+ work as verification-building examples. It supports the boundary-of-automation note with a practitioner framing. [just-a-reference]
6. **Per-tool results** -- HyInv, HyPLM, HyFF, HyProver, HyQEC, the simulated robot hand and XiangShan tuning are domain results with no bearing on KB methodology beyond showing what the harness was pointed at. [just-a-reference]

## Limitations (our opinion)

The post shows designs and outcomes, not the link between them. Every architectural claim (queue, Research Board, evidence attachment, Review Workers, Books grades, skills) is a description with no ablation, so none of the reported results can be attributed to any harness component rather than to the underlying model, the compute budget or the human researchers in the loop. Human approval gates and collaboration with mathematicians are part of the system, and the post does not separate their contribution.

The compounding and RSI claims are the post's central forward-looking argument and its least supported. Per-tool benchmark gains are the accepting metrics for each tool; as [compounding is tested in later improvement](../theory/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) argues, they cannot show that later work got better because of earlier work. Retained skills and Books entries are said to help later tasks, with no measurement.

The results are vendor-reported. Comparisons are chosen by the authors (ProteinMPNN, ESM-2, selected public force fields, one robot-hand baseline), several technical reports are promised rather than published, HyQEC is not yet released, and the robot-hand result is simulation only, as the post itself says. The XiangShan "2–3 months of iteration" equivalence is the authors' extrapolation from a dashboard.

Failure modes are absent: the post reports no failed projects, no review that overturned a claimed result, and no cost figures for tool development, so the economy argument ("the investment can be shared across many subsequent tasks") rests on assertion.

## Recommended Next Action

Add a one-line bounded case reading of Hyra 2.0 to [compounding is tested in later improvement, not by the accepting metric](../theory/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md), recording it as a frontier-lab compounding claim supported only by per-tool accepting metrics, linked to this ingest.

---

Relevant Notes:

- [Hyra 2.0: The Next Step for Auto Research](https://hy.tencent.com/research/hyra2) — derived-from: this analysis is worked out from the original post
- [An optimal long-run learning strategy invests in its own machinery](../theory/an-optimal-long-run-learning-strategy-invests-in-its-own-machinery.md) — is-evidence-for: practitioner case of reflective investment justified by amortisation, with no return measured
- [Compounding is tested in later improvement, not by the accepting metric](../theory/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) — compares-with: compounding asserted, only accepting metrics reported
- [Trace-extracted memory earns authority per operation, not at capture](../theory/trace-extracted-memory-earns-authority-per-operation-not-at-capture.md) — is-evidence-for: Books' Observation / Verified / Convention grades
- [Continual learning requires governing behaviour-changing writes](../theory/continual-learning-requires-governing-behaviour-changing-writes.md) — is-evidence-for: human approval for shared knowledge and conventions
- [Active work state is not retrospective memory or chat history](../theory/active-work-state-is-not-retrospective-memory-or-chat-history.md) — is-evidence-for: project state, agent memory and Books stored separately
- [Agent orchestration needs coordination guarantees, not just coordination channels](../theory/agent-orchestration-needs-coordination-guarantees-not-just.md) — is-evidence-for: queue scheduling, required responses and evidence-bearing completion
- [The boundary of automation is the boundary of verification](../theory/the-boundary-of-automation-is-the-boundary-of-verification.md) — is-evidence-for: slow verification named as the bottleneck
- [Treat continual learning as representational-form coevolution](../theory/treat-continual-learning-as-representational-form-coevolution.md) — compares-with: symbolic/parameterized tool taxonomy that omits natural-language artifacts
- [Representational form](../theory/definitions/representational-form.md) — defined-in: the forms Hyra's tool taxonomy maps onto
- [Reasoning production is not reasoning evaluation](../theory/reasoning-production-is-not-reasoning-evaluation.md) — compares-with: evidence-first review ordering addresses anchoring, not reconstruction
- [Factory learning is experience-responsive retention that improves the factory](../theory/factory-learning-is-experience-responsive-retention-that-improves.md) — compares-with: "class of tasks" retention without a declared family
- [Agora: Git as shared memory for collective autoresearch](./agora-git-as-shared-memory-for-collective-autoresearch.ingest.md) — compares-with: authority for shared research memory by reproduction
- [Hypothesis Evolution Protocol](./hypothesis-evolution-protocol-auditable-ai-scientists.ingest.md) — compares-with: evidence-linked revision enforced by tools versus stated as policy
- [A new era of theory-driven AI research](./a-new-era-of-theory-driven-ai-research-2084779496549548323.ingest.md) — compares-with: what auto-research should leave behind beyond answers
- [Compound Engineering plugin](../agentic-systems/reviews/compound-engineering-plugin.md) — compares-with: separating a compounding mechanism from a compounding claim
