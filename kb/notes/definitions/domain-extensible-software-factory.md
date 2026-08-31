---
description: "Definition — a domain-extensible factory computationally acquires and installs family-specific production machinery for novel demands under a declared evidence and coverage frame"
type: kb/types/definition.md
tags: [foundations, computational-model, self-improving-systems]
---

# Domain-extensible software factory

A **domain-extensible software factory** can computationally acquire, construct, and install the family-specific production machinery required by software demands outside its currently installed product families, without a human supplying the factory-development decisions that perform that specialization.

The term is introduced here as a bounded extension of Greenfield's family-specialized factory. It is not terminology recovered from the software-factory literature.

The attribution is relative to a declared tuple:


\[
(\mathcal D, E, A, B, H, R, Q)
\]

where \(\mathcal D\) is the demand class, \(E\) the permitted evidence and interaction protocol, \(A\) the acceptance relation, \(B\) the system and human-intervention boundary, \(H\) the horizon, \(R\) the resource limits, and \(Q\) the coverage rule. The claim applies only to the novel demands that \(Q\) counts under those conditions.

The frame must be fixed independently of the observed results and must be
non-vacuous. \(\mathcal D\) is the admissible demand class; \(Q\) is a
prospective sampling and accounting rule, not permission to redefine
\(\mathcal D\) by dropping difficult members. \(A\) must be an externally
anchored, non-tautological relation to the declared objective. A claim over one
already known target or a coverage rule that counts only completed successes
does not establish domain extensibility.

## Scope

A demand is **novel relative to the current factory** when ordinary product configuration or generation within its installed family scope and admitted variation cannot satisfy the demand. For each novel demand covered by the claim, the system must:

1. use evidence permitted by \(E\) to determine the needed family production knowledge;
2. construct or revise the schema, viewpoints, variability and configuration knowledge, assets, tools, methods, representations, evaluators, workflows, or runtime support that the demand actually requires;
3. computationally determine the change, using explicit candidate evaluation
   and selection only when the update architecture exposes rejectable
   candidates;
4. install the result as an operative [successor factory](./successor-factory.md); and
5. use that factory to produce and sustain family members whose outcomes are
   assessed under \(A\) across the declared lifecycle and reuse scope.

The final reuse condition prevents a one-off product repair from masquerading
as factory development. The family or variation space must be fixed before the
result is observed or determined by a predeclared inference rule. It must admit
at least one product variation distinct from the product that first exposed the
need, and the installed specialization must be causally relevant to production
across that space. A held-out family member is strong evidence for reuse, but
is not part of the definition.

Requirements, repositories, examples, corrections, tests, telemetry, constraints, permissions, and acceptance responses may remain external under \(E\). The causal boundary from the [computationally closed factory-learning loop](./computationally-closed-software-factory-learning-loop.md) still applies: a human-written schema, domain decomposition, special evaluator, promotion choice, or ad hoc recovery is supplied specialization when it performs a decision the claimed pathway is meant to make.

A declared human or environmental oracle may supply observations under \(A\).
The computational claim is then conditional on that oracle and does not
establish computational acquisition of the evaluator it implements.

The factory may retain fixed general machinery. Write its current organization
schematically as \(F_t=\operatorname{compose}(G,S_t)\), where \(G\) is general
machinery and \(S_t\) is installed family specialization. A domain-extensible
update may have the form \(S_{t+1}=U_G(S_t,h_t)\) while \(G\) remains fixed.
General models, search or learning algorithms, metalanguages, runtimes,
evidence protocols, objective interfaces, resource controls, rollback
machinery, and trusted kernels may therefore remain human-designed.

The \(G/S\) allocation must be declared before selecting the target demand and
tested across independently selected targets. A stored design indexed to a
target family remains specialization regardless of whether it is encoded in a
catalog, prompt, program, or model parameters. The burden is that \(G\) works
across the claimed demand class and computation produces the required
per-family \(S_{t+1}\); relabeling a hidden catalog of hand-built target
factories as general machinery does not meet it.

*Previously unanticipated* should normally mean absent from the installed
family specialization and from target-indexed preloaded assets, not absent from
every training example or item of general prior knowledge. A stronger
provenance claim must separately declare pretraining data, preloaded assets,
target selection, and what counts as prior family-specific encoding.

## Exclusions

- Computationally constructing a factory from a complete human-supplied metamodel, schema, or generator demonstrates factory construction, not acquisition of the specialization supplied in that input.
- A bundle of separately hand-built factories is broad configuration coverage, not domain extensibility.
- Wrapping a solved product in a post-hoc singleton family does not establish
  reusable factory specialization.
- A [computationally closed](./computationally-closed-software-factory-learning-loop.md) loop for one fixed product family may be narrow and therefore not domain-extensible over a wider demand class.
- Domain extensibility does not require every component of the fixed general machinery to be self-modifiable.
- The term does not promise recovery of arbitrary intentions that the permitted evidence cannot distinguish.

## Misuse Cases

- Describing a new product variant inside an existing variability model as a new domain.
- Supplying the decisive family schema piecemeal through “feedback” and crediting the factory with acquiring it.
- Claiming extensibility from several successful domains without declaring how the demand class, held-out novelty, failures, and human interventions were counted.
- Using \(Q\) to exclude failures or using an acceptance relation that merely
  restates whatever the factory produced.
- Treating a fixed general learner as disqualifying merely because it remains fixed, or treating family-specific knowledge hidden inside it as general merely because it is reused.

---

Relevant Notes:

- [Software factory](./software-factory.md) — defined-in: supplies the family-scoped producer whose reach is being extended
- [Factory development](./factory-development.md) — defined-in: names construction and revision of the reusable family-level machinery
- [Computationally closed software-factory learning loop](./computationally-closed-software-factory-learning-loop.md) — grounds: supplies the intervention boundary for computational specialization acquisition
- [A software factory is family-scoped lifecycle production machinery](../a-software-factory-is-family-scoped-lifecycle-production-machinery.md) — grounds: shows that conventional factories receive family knowledge from factory developers and that computational construction from supplied specialization is prior art
- [Learning inside a fixed decomposition inherits its mistakes](../learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — extends: explains why generation inside supplied family structure does not test excluded decompositions
- [The bitter lesson selects production methods, not representational forms](../the-bitter-lesson-selects-production-methods-not-representational.md) — extends: locates the scaling burden in computational production of task-specific specialization rather than in its carrier
