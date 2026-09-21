---
description: "With models pinned, newly acquired theory-use procedures must persist outside their parameters; existing general machinery may already supply them, while code can make specified steps cheaper and more reliable"
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, self-improving-systems]
---

# A fixed-model house must retain missing procedures for theory use

A retained theory and the capacity to use it are different acquisitions. A
[software house](./definitions/software-house.md) needs operations that select
relevant commitments, derive consequences, check changes, notice contrary
evidence, and revise the account. A text stating design commitments does not
by itself perform these operations. It may describe some of them, and existing
machinery may already supply others.

When the house needs a procedure its existing machinery cannot perform
adequately, acquiring more theory text alone may leave that theory inert.
With models pinned, a newly acquired procedure cannot persist through changes
to their parameters. It must be carried by retained state outside them. In the
fixed-model regime considered here, the writable carriers are natural-language
and symbolic artifacts, including records from which a procedure can be
reconstructed. This does not require new code for every new theory.

## Theory possession requires application

[Knowledge storage does not imply contextual
activation](./knowledge-storage-does-not-imply-contextual-activation.md).
Retaining an account of tenant isolation is not enough if no process consults
it when changing a query. Testing the account also requires application:
derive what it predicts, expose that prediction to observations, and revise
an assumption when the evidence warrants it. The derive-and-test steps of the
[discovery lifecycle](./definitions/discovery-lifecycle.md) depend on the same
capacity as production use.

The knowing-that / knowing-how distinction helps name this failure mode. The
[three-space memory analogy](./three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy.md)
separates retained knowledge from skill in applying it. It does not establish
that either must occupy a separate component: [human analogies suggest
functions, not component boundaries](./human-analogies-suggest-functions-not-component-boundaries.md).
Nor must both be acquired anew. A new account can be usable immediately when
the house already has suitable operations.

## What pinning changes

Parameter learning is one possible place to consolidate a new procedure.
Pinning closes that route, not the capacity to learn through context, records,
or software. The [deployed system, not the model alone, is the unit of
learning](./the-deployed-system-not-the-model-is-the-unit-of-learning.md).
A fixed model can behave differently when retrieval, instructions, tools, or
scheduling change.

[Weight-resident methodologies](./weight-resident-methodologies-compress-behavior-in-context.md)
may already supply useful operations. A fixed interpreter can also apply many
new theories through the same retrieval, graph traversal, and checking tools.
Their reuse can make a new theory sufficient as the only retained change.

The relevant limit is the [effective update
space](./learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), not
whether an operation has a dedicated name or implementation. Existing tools,
histories, and compositions of calls may express it. An operation that is
possible but too costly is different from one the permitted machinery cannot
express. Both can motivate extending the machinery, but they require different
evidence.

## Where new procedures become necessary

Consider a theory that says every file contributing to a release manifest
needs a particular check. If the house already has a reliable dependency
traversal and a configurable check selector, it can apply the theory without
writing a new traversal or selector.

Suppose the exporter instead gains an include mechanism that the traversal
cannot follow. The house must repair or replace that operation, find another
adequate route, or fail to cover the affected files. A second failure is
possible even with a correct traversal: a model may invoke it too
inconsistently, or repeated interpretation may exceed the operating budget.
Retaining a scheduling rule or installing an automatic check can address that
failure.

The requirement is therefore conditional: when existing operations cannot
apply, check, or revise a theory reliably within the budget, the house needs a
change that supplies the missing capacity. It may change a procedure, the
representation the procedure consumes, or both. Project growth alone does not
prove that this limit has been reached.

## Why specified steps can move into code

Natural-language instructions are a workable carrier for a procedure. They
persist even when a model interprets them afresh at each use. Repeated
interpretation has a cost and may vary, but it is not the loss of all learning:
the instructions and other experience-dependent state remain. The
[ephemerality distinction](./ephemeral-computation-prevents-accumulation.md)
concerns what is discarded and what still affects later work.

[Code complements model-mediated operations](./code-complements-weight-prompt-with-symbolic-operations.md)
by assigning specified steps to a runtime. A traversal or bookkeeping rule can
then run without a fresh model judgment at each step. This can improve
repeatability, cost, and coverage. Exact execution remains relative to the
runtime, inputs, and environment; it does not establish that the procedure
implements the right requirement. Instructions can also be tested, and code
can still call models or depend on uncertain inputs.

[Codification](./definitions/codification.md) becomes necessary for a particular
operation only when it is needed to meet the declared outcome and resource
limits and no permitted alternative does so. There is no general threshold at
which every growing theory must become code. Reusable machinery can postpone
or remove the need for theory-specific implementations. The related
[two-layer execution account](./theory-and-methodology-form-a-two-layer-execution-system.md)
explains how a retained procedure can serve as a cheaper path while theory
remains available for cases it does not cover.

## What existing reports support

[Memento-Skills](../sources/memento-skills-let-agents-design-agents.ingest.md)
reports deploy-time revision of mixed instruction-and-code skill memory around
a frozen LLM. Its router is trained separately, so it is not evidence that all
distributed-parametric components remained fixed.

[SkillOpt](../sources/skillopt-executive-strategy-self-evolving-agent-skills.ingest.md)
reports validation-gated changes to natural-language skills with a frozen target
model and harness. It supports the instruction carrier, not a requirement to
turn every procedure into code.

[Self-harness](../sources/self-harness-harnesses-that-improve-themselves.ingest.md)
reports machinery revision through failure mining and regression-gated edits
under a fixed model and supplied outer method. It supports a machinery-learning
mechanism, not the stronger claim that new theories caused those revisions.
None of these reports establishes the proposed coupling by itself.

## A test of the coupling

Compare matched houses with the same fixed models, observations, tasks, and
resource ceilings. One may revise theory-use machinery; the other retains new
theories and records but uses the same frozen general machinery. Give the
frozen baseline capable retrieval, traversal, and checking operations, rather
than making repeated unaided model interpretation its only option.

Before testing, identify the operation expected to fail and the workload change
expected to expose it. Measure missed consequences, recovery, and total cost,
including procedure construction and maintenance. A machinery edit supports
the account only when it repairs the named failure and improves later work;
co-occurring theory and code edits alone do not show that relation.

If the frozen baseline remains adequate under the same limits, the proposed
need for new machinery was not established for those conditions. If it performs
better at comparable cost, that counts against the proposed extension. Do not
rescue a failed prediction by moving the claimed scale limit after the run.

## Scope

The strong requirement is to supply a missing capacity, not to rewrite every
component or to allocate one procedure per theory. The argument concerns
retained learning across the declared horizon; temporary computation can still
apply a theory or teach a lesson retained elsewhere. A stored procedure counts
as an acquisition only when its later use changes the house's capacity.

## Open Questions

Which operations exceed the existing machinery's reliability or budget on
real workloads? How much can generic procedures be reused across theories?
These determine whether a text-only writable surface suffices in practice,
rather than the fixed-model premise alone.

---

Relevant Notes:

- [Code complements the weight–prompt pair with independently executed symbolic operations](./code-complements-weight-prompt-with-symbolic-operations.md) — grounds: distinguishes model interpretation from runtime-assigned execution
- [Learning inside a fixed decomposition inherits its mistakes](./learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — grounds: defines the effective update space, including compositions of existing operations
- [The deployed system, not the model alone, is the unit of learning](./the-deployed-system-not-the-model-is-the-unit-of-learning.md) — grounds: places retained theory and its application machinery inside one learner
- [Explicit retention provides direct targets for selective revision](./only-explicit-retention-is-durable-writable-and-addressable.md) — mechanism: explains the inspection and revision affordances of written procedures without making them the only possible form of learning
- [An open-domain theory builder becomes a software house when new domains require production-machinery changes](./an-open-domain-theory-builder-becomes-a-software-house-when-new-domains-require-production-machinery-changes.md) — extends: applies the conditional procedure demand to the producer's boundary
- [Treat continual learning as representational-form coevolution](./treat-continual-learning-as-representational-form-coevolution.md) — extends: places theory and machinery revision within a wider learning process
- [Representational form](./definitions/representational-form.md) — defined-in: supplies the natural-language, symbolic, and distributed-parametric distinction
