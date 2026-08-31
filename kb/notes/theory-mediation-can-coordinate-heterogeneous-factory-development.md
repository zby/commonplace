---
description: "Natural-language theory may be a versatile factory-learning mechanism because one LLM-interpretable account can connect tasks, solver limits, failures, evidence, and changes across heterogeneous production machinery"
type: kb/types/note.md
traits: [title-as-claim, has-comparison]
tags: [foundations, learning-theory, self-improving-systems]
---

# Theory mediation can coordinate heterogeneous factory development

Natural-language theory may be a particularly versatile mechanism for [factory development](./definitions/factory-development.md) because one LLM-interpretable account can connect task structure, relevant solver limitations, observed failures, proposed interventions, scope conditions, and evidence, then guide changes across heterogeneous production machinery.

This is a comparative hypothesis, not a definition of learning and not a claim that theory is necessary. A software factory can learn through trial and error, trajectory reuse, program search, learned policies, direct optimization, or mixtures. The question is whether theory mediation provides useful leverage when a change must coordinate several artifact kinds or when decisive feedback is sparse, delayed, or arrives under a structured shift.

## The coordination problem

A failure in software production may not identify the artifact that should change. The same symptom can arise from:

- a mistaken understanding of the task or product family;
- a decomposition that drops necessary dependencies;
- context selection that omits relevant evidence;
- an intermediate representation that cannot express required distinctions;
- a tool or algorithm that performs the wrong transformation;
- an evaluator that rewards a proxy;
- a workflow that stops before delayed consequences arrive; or
- conflicting schemas, prompts, tests, and runtime assumptions.

The remedy can therefore span natural-language guidance, symbolic software, schemas, tests, workflows, retrieval policy, and model-facing context. A fixed update operator for one artifact kind may repair the local symptom while leaving the shared explanation inconsistent elsewhere.

A retained theory can instead state a cross-artifact commitment such as:

> The final decision depends on relations among evidence units, so independent summaries are insufficient; extraction may be parallelized, but the representation and aggregation path must preserve cross-unit relations for a later reconciliation pass.

An LLM can interpret that claim into changes to decomposition, intermediate schemas, map-reduce code, prompts, aggregation logic, and tests. The theory is useful only if it actually changes those decisions and remains revisable when later outcomes contradict it.

## What theory can represent in one medium

A factory-relevant theory may include:

- **task or domain claims** — what distinctions, dependencies, invariants, and variations matter;
- **solver claims** — which operations are reliable, bounded, expensive, or prone to a known failure mode;
- **production claims** — why a decomposition, workflow, representation, or tool should work;
- **evaluation claims** — which observations would support or defeat the proposed organization;
- **scope claims** — where the account applies and where it should not transfer; and
- **revision claims** — which parts should change when a prediction fails.

The relevant self-knowledge is therefore not a complete theory of the model's internals. It is a task-relevant theory of the relation among the task, the current solver, and interventions that can make the task tractable.

## Theory guides search; it does not replace it

Theory mediation does not require deductively deriving every factory change. The theory can shape a generate-and-verify process by controlling:

- which failure explanations are plausible;
- which machinery is worth inspecting;
- which candidate decompositions or tools to try;
- which experiments are informative;
- which checks should reject a proposal; and
- how an observed result should revise the retained account.

Blind or stochastic exploration can remain inside the process. A learned policy can propose candidates. Code can execute exact transformations and tests. The theory-mediated claim is that addressable theory causally changes search, diagnosis, evaluation, recovery, or revision.

The [scheduler–LLM separation](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) gives the complementary implementation principle: semantic interpretation can remain model-mediated while exact progression, bookkeeping, and stabilized invariants move into software. Theory can guide which invariants should be codified without requiring the LLM to execute them unreliably on every run.

## Why versatility is plausible

Theory mediation has four potential advantages for heterogeneous factory learning.

### Cross-artifact reach

The same explanation can guide coordinated edits to prompts, schemas, workflows, tests, code, tools, and documentation. This can reduce the need for one separately trained update policy per artifact class.

### Selective revision

Addressable claims can be revised or rescaled without discarding the whole retained state. A failed prediction may defeat one scope condition or mechanism claim while preserving unrelated parts of the factory theory.

### Delayed credit assignment

A theory records why an earlier production decision was made and what consequences it predicted. When a later requirement exposes damage, the retained joins can connect the consequence to the earlier decomposition or representation choice.

### Transfer under structured shifts

A mechanism-level claim may apply to a new product variation even when surface details differ. This could improve sample efficiency relative to replaying only concrete trajectories, provided the theory captures real structure rather than a plausible story.

These are hypotheses. Natural language also introduces ambiguity, retrieval cost, contradiction, interpretation error, and rationalization. A theory can coordinate several artifacts into the same mistake.

## Comparative predictions

Against information- and budget-matched alternatives, theory mediation should earn support when it:

1. transfers one retained explanation into several causally coherent machinery changes;
2. predicts where a decomposition, representation, evaluator, or tool will fail before exhaustive trial;
3. improves recovery after delayed feedback by identifying the earlier commitment that should change;
4. supports targeted rescoping instead of copying or discarding an entire trajectory;
5. reduces new human specialization when a related but unanticipated family variation appears; or
6. leaves an intervention-sensitive trace: withholding, replacing, or corrupting the theory changes consequential factory-development choices.

It should narrow or lose when:

- the retained theory is ignored or reconstructed post hoc;
- direct search or optimization reaches better machinery at comparable total cost;
- trajectory reuse transfers as well with less maintenance;
- theories become self-confirming because their evaluators share the same assumptions;
- cross-artifact coordination increases correlated error;
- human judgment required to maintain theory grows with the system; or
- each new domain still requires people to supply the decisive decomposition and evaluator.

## Theory content and factory machinery are different roles

A natural-language artifact can be consumed as evidence, advice, an instruction, a constraint, or a generator input. Merely storing a theory beside the factory does not make production theory-mediated. The causal path must show how the theory changes model calls or executable machinery and how later evidence revises the same retained surface.

Conversely, theory need not remain in natural language forever. Stable claims can be codified into validators, schemas, tools, or workflows. A brittle symbolic rule can be relaxed back into an interpretable hypothesis. Theory mediation describes the learning relation, not a requirement that every useful result remain prose.

## Scope

- The claim concerns versatility across factory-development decisions, not universal superiority on every task.
- Natural-language theory is one representational surface inside the deployed system; model weights and symbolic machinery remain essential.
- A theory of the task alone may be insufficient when decomposition depends on solver limits. A theory of the solver alone may be insufficient when task dependencies determine what must be preserved.
- Theory mediation can coexist with fixed general machinery and with non-theoretical search at lower levels.
- Reflection is not required for every theory-mediated factory change. It is claimed only when a causally connected representation of selected aspects of the same system participates in operation or revision.

---

Relevant Notes:

- [Factory-learning mechanisms should be compared on the same causal job](./factory-learning-mechanisms-should-be-compared-on-the-same-causal-job.md) — grounds: supplies the neutral comparison frame and failure conditions
- [Program theory sustains search under delayed feedback](./program-theory-sustains-search-under-delayed-feedback.md) — grounds: explains how retained rationale connects later consequences to earlier choices
- [Theory-mediated self-improvement needs interpretation and retention](./theory-mediated-self-improvement-needs-interpretation-and-retention.md) — grounds: supplies the causal mediation and retained-revision requirements
- [Theory-mediated learning may improve sample efficiency under shifts](./theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) — extends: states the structured-transfer conjecture
- [Natural-language project state specializes search heuristics](./natural-language-project-state-specializes-search-heuristics.md) — mechanism: explains one way explicit theory can alter an LLM's proposal distribution
