---
type: note
description: "SwarmWorld's simulator-bound agent society: explicit episode memory, executable artifact inheritance, measurement-based skill status and limits on replay and scientific warrant."
traits: [has-external-sources]
generated-by: analyse-agentic-system
analysis-run: AAS-2026-09-25-swarmworld-01
source-identity: https://github.com/lamm-mit/SwarmWorld
reviewed-revision: "6af7ae9fa36d98b07b0492cf139658e8af1f6eab"
analysis-result: kb/reports/retained/agentic-system-analysis/AAS-2026-09-25-swarmworld-01/result.md
analysis-result-sha256: "774834cb6233b4c244513567f658de749d6b1f80f0dd2fae5c09d8e78cf6d78a"
---

# SwarmWorld

Evidence basis: source code and current architecture documentation at `6af7ae9fa36d98b07b0492cf139658e8af1f6eab`, inspected 2026-09-25. No target execution, live provider call or separately released study dataset was used.

SwarmWorld is a simulator for societies of agents that conduct local experiments and build persistent technological artifacts. Models propose plans, recipes, explanations and programs; the simulator controls physical consequences. Its historical Python package is `biofoundry`. This review covers the runtime, model-policy interface, memory, experiment and replay routes. Provider internals, physical-surrogate validity, renderer internals and exhaustive scenario validation are outside the boundary. [Source overview](https://github.com/lamm-mit/SwarmWorld/blob/6af7ae9fa36d98b07b0492cf139658e8af1f6eab/README.md) — evidenced-by.

## Execution and control

An operator chooses the seed, configuration and policy. At a scheduled macroturn, the LLM policy assembles local observations, selected memories and the agent's prior research state, sends a structured request, and queues validated actions. The simulator consumes one action per agent per tick and returns outcomes that can trigger replanning. CLI scripted policies, server manual actions and externally supplied PettingZoo actions are material alternatives: they bypass model generation while still reaching simulator checks. The model's schema is therefore narrower than the shared physical authority boundary. [Policy](https://github.com/lamm-mit/SwarmWorld/blob/6af7ae9fa36d98b07b0492cf139658e8af1f6eab/src/biofoundry/policies/llm.py), [simulation](https://github.com/lamm-mit/SwarmWorld/blob/6af7ae9fa36d98b07b0492cf139658e8af1f6eab/src/biofoundry/simulation.py) — evidenced-by.

Configuration changes the experiment. The named fifty-agent profile enables model planning, experience attention, program skills and reuse, but disables economy. Optional cultural inheritance exists in source and is inactive in that profile. With outage freezing enabled, any scheduled transient provider failure restores that planning batch's private memory and preserves queues. CLI/server retry without advancing the world; the convenience `actions()` wrapper consumes a queue after refresh even when refresh returns false. Freeze is a caller protocol, not a guarantee for every entry path. [Named profile](https://github.com/lamm-mit/SwarmWorld/blob/6af7ae9fa36d98b07b0492cf139658e8af1f6eab/configs/openai-gpt-5.6-luna-technology-ecology-50.yaml), [policy](https://github.com/lamm-mit/SwarmWorld/blob/6af7ae9fa36d98b07b0492cf139658e8af1f6eab/src/biofoundry/policies/llm.py) — evidenced-by.

## Memory and persistent behavior

Private notebooks, empirical observations, research state, experimental records, shared publications and program skills persist within an episode. The next model request explicitly receives retained material; authored goals and hypotheses also shape retrieval. Lexical relevance, locality, recency, program identities and optional citation/outcome statistics govern selection. The context character target is best effort, and initial selection diagnostics can include records later trimmed from the prompt. Citation and successful cited actions do not demonstrate dependence on the cited content. [Memory](https://github.com/lamm-mit/SwarmWorld/blob/6af7ae9fa36d98b07b0492cf139658e8af1f6eab/src/biofoundry/memory.py), [policy](https://github.com/lamm-mit/SwarmWorld/blob/6af7ae9fa36d98b07b0492cf139658e8af1f6eab/src/biofoundry/policies/llm.py) — evidenced-by.

Programs use a bounded, straight-line artifact language. Validated installed instructions affect future ticks; fork records preserve content identity and differences. A measured artifact observation marks a skill `verified` without requiring a performance pass. Ordinary skill views prefer verified entries but can include others; optional inheritance filters verified records and selects by measurement count and recency. It can preserve measured but poor behavior. [Program library](https://github.com/lamm-mit/SwarmWorld/blob/6af7ae9fa36d98b07b0492cf139658e8af1f6eab/src/biofoundry/program_library.py), [program VM](https://github.com/lamm-mit/SwarmWorld/blob/6af7ae9fa36d98b07b0492cf139658e8af1f6eab/src/biofoundry/programs.py) — evidenced-by.

## Experimental warrant

TEST exposes simulator measurements of a pending batch; enabled experience reuse retains the recipe that produced them. Publications can carry grounded resource provenance, but that does not test their prose. Artifact names and predicted functions remain claims while numeric geometry and executable instructions affect physics. BUILD's error text mentions a tested recipe, yet the inspected construction path checks supplied recipe/specification and available materials without enforcing a prior TEST. Material consumption also precedes later program validation, so action rejection does not guarantee rollback. [Experiment records](https://github.com/lamm-mit/SwarmWorld/blob/6af7ae9fa36d98b07b0492cf139658e8af1f6eab/src/biofoundry/science.py), [construction](https://github.com/lamm-mit/SwarmWorld/blob/6af7ae9fa36d98b07b0492cf139658e8af1f6eab/src/biofoundry/simulation.py) — evidenced-by.

Scorecards combine concrete material, program, performance, novelty and provenance criteria. Frozen-state artifact removal and held-out disturbance schedules provide implemented evaluation routes, but no executed comparison was admitted here. These routes concern simulator outcomes; they do not generally accept the truth of an explanation. Replay restores recorded actions and committed research state, then checks a serialized state projection. Adaptive retrieval statistics are omitted, so matching digests do not establish identical future prompts or a complete resumed policy. [Evaluation](https://github.com/lamm-mit/SwarmWorld/blob/6af7ae9fa36d98b07b0492cf139658e8af1f6eab/src/biofoundry/technology_ecology.py), [reconstruction](https://github.com/lamm-mit/SwarmWorld/blob/6af7ae9fa36d98b07b0492cf139658e8af1f6eab/src/biofoundry/counterfactuals.py) — evidenced-by.

Automatic continuation, feedback, measured input/output records and retrieval statistics form a wired trace-learning route within one episode. The runtime also wires a bounded reflective loop over its agents' history, progress and access metadata. Evidence-responsive plan/program revision is afforded. Criticism of an operative formulated theory, resulting capacity improvement and actual self-improvement remain uninspected; no causal recall or learning benefit follows from these structural routes alone.

## Scope

Findings describe implementation at the pinned source boundary. They do not validate the surrogate as real-world science, hidden provider reasoning, external studies or every scenario. Candidate-linked hypothesis/test/revision traces, matched learning comparisons and recalled-content interventions with replanning would support stronger conclusions.

- [Exact analysis result](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-swarmworld-01/result.md) — see-also: canonical records, quotations, both lenses and comparison fields.
- [Conjectural learning](../../notes/definitions/conjectural-learning.md) — defined-in: the stronger theory-and-criticism claim kept separate from retained feedback.
- [Reflective system](../../notes/definitions/reflective-system.md) — defined-in: the two-way self-representation route used here.
