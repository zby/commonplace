---
description: "Maps agentic-adaptation signals onto artifact-analysis axes so KB learning records which retained surface changes, what authority it gains, and how to review it"
type: kb/types/note.md
traits: [title-as-claim, has-comparison, has-external-sources]
tags: [learning-theory, artifact-analysis, agent-memory, context-engineering]
---

# Adaptation signals choose pressure; artifact analysis chooses the retained surface

[Adaptation of Agentic AI](../../sources/adaptation-of-agentic-ai-survey-post-training-memory-skills.ingest.md) is useful because it separates adaptation by optimization locus and signal source: A1 updates the agent from tool-execution feedback, A2 updates the agent from output evaluation, T1 trains agent-agnostic tools, and T2 adapts tools under supervision from a fixed agent. That frame answers "where did the update pressure come from?" It does not answer the design question an agent-operated KB has to answer next: what retained behavior-shaping artifact should change, through which authority path, and with what review evidence?

That second question belongs to [axes of artifact analysis](../axes-of-artifact-analysis.md). Once an adaptation signal fires, the durable result may be a prose memory, prompt patch, skill, generated cue, route table, validator, typed schema, retrieval index, learned controller, adapter, or model checkpoint. Those choices differ by [storage substrate](../definitions/storage-substrate.md), [representational form](../definitions/representational-form.md), [lineage](../definitions/lineage.md), and [behavioral authority](../definitions/behavioral-authority.md). The survey's A1/A2/T1/T2 label tells us which component was optimized and what supervision signal was available; artifact analysis tells us what the system has actually learned in retained form and how future agents should trust, load, test, regenerate, or retire it.

## What the survey gives

The survey's four-way taxonomy is valuable as a signal map:

| Survey bucket | Adaptation pressure | Typical signal |
|---|---|---|
| A1 | update the agent from tool execution | verifiable tool outcomes: test pass/fail, retrieval relevance, API result |
| A2 | update the agent from its own output | final answer quality, preference score, holistic task result, judge verdict |
| T1 | train a reusable tool independently of one fixed agent | tool-level benchmark or pretraining objective |
| T2 | keep the agent fixed and adapt its environment | frozen-agent outputs supervising retrievers, memory updaters, search subagents, or skill libraries |

For KB methodology, the key gain is not the names. It is that signal density and component cost become visible. Execution-grounded signals are easier to use than holistic output scores. Updating a retriever, skill, prompt, validator, or memory store is usually cheaper and more inspectable than changing model weights. T2 therefore names a common practical pattern: keep the model fixed and improve the surrounding artifacts.

But "tool" is too coarse for Commonplace. A tool may be a symbolic validator, a prose skill, a vector index, a learned reranker, a subprocess wrapper, or a memory curator. A memory module may include raw traces, summaries, embeddings, routing rules, and generated prompts. Treating all of those as "external tools" hides the review method and lifecycle obligations that matter operationally.

## The missing retained-surface question

An adaptation event should be recorded as two linked decisions:

1. Which pressure was observed?
2. Which retained surface should absorb it?

The first decision is the survey's frame. The second is artifact analysis.

| Observed pressure | Weak retained surface | Stronger retained surface when pattern stabilizes | Review evidence |
|---|---|---|---|
| A tool repeatedly fails on one input shape | prose reminder or error note | symbolic validation, argument normalizer, better error message | tests over the failing input class |
| A worker always runs the same sequence | prompt instruction describing the sequence | orchestrator function, workflow, or script | execution tests and interrupt/retry behavior |
| Output structure is stable and easy to state | example output in a prompt | schema, parser, or validator | parse/validation tests |
| Agent outputs reveal recurring search misses | note or source review describing the miss | generated index, cue, query recipe, or retrieval policy | retrieval ablation and link/provenance audit |
| User overrides a rigid rule repeatedly | exception note | relaxed interface boundary or LLM-mediated judgment slot | integration tests plus override/appeal audit |
| A memory update improves task outcomes | new memory entry | cue, skill, retriever update, learned policy, or raw-trace retention rule | WITH/WITHOUT behavior comparison and lineage check |

This table is not a promotion ladder. The stronger surface is only stronger when the signal is strong enough and the target form matches the domain. A recurring failure can justify a validator in an exact-spec regime; in a proxy-theory regime, the same failure may justify relaxing a brittle symbolic rule back into a prose/LLM judgment path. This is why the survey's signal taxonomy needs [fixed artifacts split into exact specs and proxy theories](../fixed-artifacts-split-into-exact-specs-and-proxy-theories.md) and [operational signals that a component is a relaxing candidate](../operational-signals-that-a-component-is-a-relaxing-candidate.md) beside it.

## Constraining and relaxing use the same evidence differently

The old version of this note treated the survey mainly as an `llm-do` feature sketch: log failures, track outcomes, analyze patterns, and suggest prompt edits. Those are still useful operations, but the artifact-analysis frame changes what the analyzer should output. It should not merely say "edit the prompt." It should classify the proposed retained change:

- **Constrain** when the signal identifies a stable obligation with a strong enough oracle. Examples: add a schema when output shape is settled; add a path normalizer when tool failures are mechanical; codify an orchestration sequence when the same steps recur.
- **Abstract** when the signal carries reusable judgment but not exact procedure. Examples: write a bounded lesson from repeated troubleshooting, generalize a rule from accepted edits, extract a cue from trace-extracted mistakes.
- **Relax** when the codified artifact is a proxy theory showing brittleness. Examples: growing exception lists, frequent user overrides, process constraints that fail in integration, or validation rules whose failure conditions are hard to specify.

Each action is an artifact move. It changes representational form, authority, lineage, or lifecycle. Storing an LLM output is itself a [constraining](../definitions/constraining.md) move because it commits one sampled interpretation as a retained artifact; storing a prompt tweak, skill rule, or generated cue has the same issue. The adaptation signal can justify the change, but it does not by itself choose the retained form.

## Memory and skills are artifact bundles

The survey correctly treats memory and skills as adaptation mechanisms rather than passive storage. That corroborates the memory-requirements work, but a system still has to split the bundle. A "memory update" may contain:

- raw trace storage in an audit log;
- extracted prose facts in a memory file;
- embeddings and ranking behavior in a vector index;
- generated cues in an always-loaded prompt view;
- a symbolic validator mined from repeated mistakes;
- a skill instruction plus routing metadata;
- a learned memory-management policy.

Those are different operative parts. They can share one user-facing name while requiring different review methods: read prose, test symbolic code, probe distributed-parametric behavior, and validate lineage for derived views. [Memory design adds operational axes to artifact analysis](../memory-design-adds-operational-axes-to-artifact-analysis.md) adds the policy layer around those parts: capture, derivation, activation, authority assignment, lifecycle, and evaluation. The adaptation survey helps identify where the learning signal comes from; the memory design axes decide whether the resulting artifact is allowed to act later.

## Evaluation implication

The survey's evaluation section is strongest where it asks for component-counterfactual and dynamics-aware evaluation: swap one component, hold the rest fixed, and track accuracy, cost, safety, and forgetting over time. Artifact analysis makes that requirement sharper. The component to swap is not always a stored object. It may be one consumption path through an object: the retrieval ranking path, the prompt-assembly path, the validator path, or the training-input path.

For Commonplace, an adaptation evaluation should therefore report at least:

- the observed signal: execution feedback, output judgment, user override, accepted edit, retrieval failure, or task outcome;
- the retained artifact and operative part changed;
- the artifact fields: substrate, form, lineage, authority;
- the operational memory policy affected: capture, derivation, activation, authority, lifecycle, or evaluation;
- the counterfactual: what behavior changes when that retained surface is absent, stale, corrupted, or replaced?

Without those fields, endpoint improvement is ambiguous. A better task score could come from a better prompt, a better retriever, a more permissive validator, a memorized shortcut, or a learned policy that overfits the evaluator. The survey identifies the ambiguity; artifact analysis gives the bookkeeping needed to investigate it.

## Boundary

This note is not the main comparison between the survey and the memory-requirements map. That job belongs to [The adaptation survey corroborates memory requirements but misses artifact governance](../agent-memory-requirements/adaptation-survey-corroborates-memory-requirements.md). This note keeps the narrower operational payload that existing backlinks need: data-driven triggers for when to constrain, abstract, derive, or relax, interpreted through the retained-artifact taxonomy rather than through `llm-do` feature brainstorming.

## Open questions

- Should Commonplace define an "adaptation event" record with fields for signal, retained artifact, artifact axes, operational memory axis, and evaluation counterfactual?
- Are `source -> note` labels rich enough for source-side parallel-mechanism relationships, or should those remain in ingest prose until they become claims?
- When a signal suggests both a prompt edit and a validator, should the default be to preserve the prompt change as rationale for the validator or to keep only the symbolic artifact plus tests?

---

Relevant Notes:

- [Adaptation of Agentic AI ingest](../../sources/adaptation-of-agentic-ai-survey-post-training-memory-skills.ingest.md) - abstracted-from: source taxonomy whose signal/locus frame this note translates into retained-artifact decisions
- [Axes of artifact analysis](../axes-of-artifact-analysis.md) - grounds: supplies the storage substrate, representational form, lineage, and behavioral-authority fields that decide what the retained learning surface is
- [Where It Lives Is Not What It Is ingest](../../sources/where-it-lives-architectural-vocabulary-retained-adaptation.ingest.md) - see-also: external-facing statement of the same artifact-analysis vocabulary; cited for framing, not independent corroboration
- [The adaptation survey corroborates memory requirements but misses artifact governance](../agent-memory-requirements/adaptation-survey-corroborates-memory-requirements.md) - contrasts: covers the memory-requirements comparison; this note covers operational signal-to-artifact translation
- [Memory design adds operational axes to artifact analysis](../memory-design-adds-operational-axes-to-artifact-analysis.md) - extends: adds memory-specific capture, derivation, activation, authority, lifecycle, and evaluation policies around the retained artifact
- [Storing LLM outputs is constraining](../storing-llm-outputs-is-constraining.md) - extends: data-driven adaptation signals tell us when a retained output or prompt change is worth committing
- [Operational signals that a component is a relaxing candidate](../operational-signals-that-a-component-is-a-relaxing-candidate.md) - extends: relaxing signals are the reverse use of adaptation evidence, when a symbolic/procedural surface is a brittle proxy theory
- [Unified calling conventions enable bidirectional refactoring](../unified-calling-conventions-enable-bidirectional-refactoring.md) - enables: moving learned behavior between neural/prose/symbolic surfaces is cheaper when call boundaries stay stable
