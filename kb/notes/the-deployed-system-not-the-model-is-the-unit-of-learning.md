---
description: "Because prompts, retrieval, tools, and runtime policy jointly determine deployed behavior, model-only learning leaves consequential system choices fixed"
type: kb/types/note.md
traits: [title-as-claim, synthesis]
tags: [learning-theory, deploy-time-learning, computational-model]
---

# The deployed system, not the model alone, is the unit of learning

Learning in an LLM-based application should evaluate and improve the deployed system that produces user-visible behavior, not only the model inside it. Prompts, retrieval, context assembly, scheduling, memory, tools, validators, and execution boundaries all shape what the user receives. Their joint behavior therefore sets the evaluation boundary. Within that boundary, the writable learning surface consists of the consequential retained choices that an evidence-responsive improvement process can change. Improving only the weights leaves some of those choices outside the learning loop.

This broader boundary does not diminish model learning. It places model learning inside the larger [behavior-determining organization](./definitions/behavior-determining-organization.md) that produces the outcomes being improved. A model update can improve semantic judgment across many uses. A prompt revision can resolve a deployment-specific ambiguity. A validator can turn a recurring failure into an enforced invariant. Each counts as system learning when an improvement process uses evidence from system behavior to select and retain the change, allowing it to affect later executions. The changes act on different parts of the causal path, but they can participate in the same [proposal-selection improvement loop](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md).

## Why the model looked like the right boundary

The prompt-to-completion interface made the model a useful shorthand for the system: it appeared to receive the task, perform the work, and return the result. Deployment made more machinery consequential. Long-running work needs durable state, bounded context, exact tool execution, permissions, and verification. These functions come from a runtime that can be decomposed into [scheduler, context engine, and execution substrate](./agent-runtimes-decompose-into-scheduler-context-engine-and-execution.md).

These components do not merely support behavior produced elsewhere. A retriever determines which evidence becomes available. A scheduler determines which calls happen and what state survives. A validator determines which candidate outputs can take effect. Changing any one can change the result while the model remains fixed, so calling the result "model behavior" attributes joint behavior to one component.

## User outcomes set the evaluation boundary

Users encounter the system's correctness, reliability, latency, cost, safety, and ability to complete the task. They need not care whether a successful step came from parametric recall, a retrieved instruction, a generated program, or a deterministic tool. Their outcomes therefore define an end-to-end evaluation boundary.

The writable learning surface is narrower than that boundary. It contains the consequential free choices that the improvement process is allowed to revise. A stronger model may absorb a prompt heuristic. A stable interpretation may become code. A brittle rule may return to model judgment. A retrieval step may disappear when the capability becomes reliable elsewhere. The model checkpoint is one mutable part of this organization; it does not carry the system's capacity by itself.

## Model-only learning freezes the system decomposition

Because [learning inside a fixed decomposition inherits its mistakes](./learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), updating only model weights fixes the surrounding prompts, interfaces, context policies, tools, scheduler, and checks in advance. Optimization can improve every choice the model is allowed to make, but it cannot touch a mistaken distinction, missing action, or poor division of work outside that update space.

A capable model can sometimes compensate for a poor fixed layer. It can infer an intention a prompt omitted, reconstruct state that the harness failed to preserve, or reproduce an operation that should have been a tool. Such compensation can improve measured behavior, but it does not show that the fixed decomposition was right. It may instead spend model capacity and inference cost repairing the same system error on every run.

This limitation is causal rather than terminological because [LLM output deviation has three sources with non-substitutable remedies](./llm-output-deviation-has-three-sources-with-non-substitutable.md). Those remedies act on different parts of the system:

- Underspecification can require revising the natural-language specification, changing assembled context, or committing a settled interpretation to a symbolic artifact.
- Interpreter failure can require a better model, but it can also require detection, correction, validation, or architectural separation outside the failing interpreter.
- Indeterminism can require changes to decoding, voting, retry policy, or the runtime that controls sampled execution.

A weight update may reduce more than one symptom, but it cannot directly apply every remedy. The improvement process therefore needs a route to propose and evaluate changes to whichever part of the deployed system produced the failure.

## Whole-system learning can coordinate distinct update mechanisms

Expanding the writable surface does not require one optimizer or update cadence. Parametric training, prompt revision, harness search, test generation, and program repair can remain distinct mechanisms. What unifies them is evaluation against the deployed objective and operative retention: candidate changes must survive comparison and affect later runs.

The retained encoding of a change—its [representational form](./definitions/representational-form.md)—can be model weights, natural language, symbolic code, or a mixture. The form does not determine whether the change counts as learning; the improvement process does. A computational process can propose prompts, schedulers, tools, schemas, tests, and context policies. Human edits remain engineering inputs unless an evidence-responsive improvement loop evaluates and incorporates them.

This mixed system is compatible with the Bitter Lesson because [the lesson selects production methods, not representational forms](./the-bitter-lesson-selects-production-methods-not-representational.md). Prompts and code can be learned products when computational processes generate and select them. Consequential harness structure should therefore face search and selection rather than remain exempt merely because it sits outside the weights. When the allocation among weights, prompts, and code is itself a consequential free choice, that allocation should also remain revisable. [Representational-form coevolution](./treat-continual-learning-as-representational-form-coevolution.md) covers both the contents of each form and their division of responsibility.

## Scope

- Whole-system learning does not require every component to remain mutable. Objectives, hard dependencies, exact interfaces, and other warranted constraints can stay fixed. The claim targets consequential free choices that are frozen merely because they sit outside the current updater.
- "Deployed system" is ambiguous when a shared model, retriever, or tool couples several deployments, because a deployment-local boundary can miss an intervention's cross-deployment effects. Which boundary to draw — a single deployment, the smallest independently governable causal domain, or a coupled fleet — is left open here.
- This note does not claim that current whole-system optimizers scale. Cross-component credit assignment, validation cost, compatibility, and safe retention remain open problems.
- Whether a future model can generate a sufficient surrounding system on demand is separate. This note concerns the boundary at which deployed behavior is evaluated and improved, not whether every useful component must persist between runs.

---

Relevant Notes:

- [Behavior-determining organization](./definitions/behavior-determining-organization.md) — defined-in: identifies retained components by their causal effect on future behavior rather than by whether they are model weights
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — mechanism: distinguishes evidence-responsive learning from durable but unevaluated maintenance changes
- [Continual learning's open problem is governing behaviour change, not storing knowledge](./continual-learning-open-problem-is-behaviour-not-knowledge.md) — context: continual learning is the regime where excluding non-model components is most consequential; this note's unit claim applies there and beyond
- [LLM output deviation has three sources with non-substitutable remedies](./llm-output-deviation-has-three-sources-with-non-substitutable.md) — grounds: specification, interpreter, and sampling failures require access to different repair surfaces
- [Learning inside a fixed decomposition inherits its mistakes](./learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — grounds: model-only optimization cannot repair consequential choices excluded from its effective update space
- [The bitter lesson selects production methods, not representational forms](./the-bitter-lesson-selects-production-methods-not-representational.md) — grounds: computational production makes natural-language and symbolic system components compatible with the lesson
- [Moving the interpretation-enforcement boundary requires cross-form coverage](./moving-the-interpretation-enforcement-boundary-requires-coverage.md) — mechanism: governing transfers between model interpretation and formal enforcement requires access to both sides and their mapping
- [Co-Harness](../sources/co-harness-co-evolving-harness-and-model-weights.ingest.md) — evidenced-by: a research ingest of a bounded attempt to co-evolve model weights with prompts, tools, skills, memory, and middleware
- [Meta-Harness](../sources/meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md) — evidenced-by: a research ingest of end-to-end harness search around fixed weights
