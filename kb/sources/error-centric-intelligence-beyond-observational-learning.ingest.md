---
description: "Thomas proposes error-driven changes to hypothesis spaces and structural diagnostics for causal learning; the contribution is conceptual and does not establish that fixed-model systems cannot create knowledge."
source: https://arxiv.org/abs/2510.15128
captured: "2026-09-19"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 6a64e2cd4cf7b05ad29f9f5ae9f327700ff43243fc8d66160e291c030920bd5a
ingested: "2026-09-19"
occasion: "Reconsider the learning paradigm from Popperian epistemology: compare the epistemic process, computational realization, changeable representations and tests, fixed-model learning, reflection, and supporting evidence."
type: types/ingest-report.md
domains: [learning-theory, critical-rationalism, causal-reasoning]
learning_claims: true
---

# Ingest: Towards Error-Centric Intelligence I: Beyond Observational Learning

## Classification

A theoretical scientific preprint combining proposed definitions, causal-identifiability arguments, structural principles, and mathematical diagnostics. It reports no implemented learning system or new empirical comparison. Marcus A. Thomas identifies the work as independent and explicitly disclaims institutional endorsement. The retained paper is arXiv v1; its mathematical presentation is not evidence of experimental validation.

## Summary

Thomas proposes Causal Mechanics, a research program in which conjecture and criticism can change variables, mechanisms, intervention semantics, and invariances rather than only fit parameters inside an existing hypothesis class. The central motivation is that observationally equivalent causal worlds may respond differently to interventions, so observational adequacy alone cannot guarantee interventional competence. Three questions organize the program: how actions expose implicit errors, which errors remain unreachable in the available hypothesis space, and how structural conjectures make them reachable. The paper proposes a Locality–Autonomy Principle for modular changes, geometric Independent Causal Mechanisms for structural separability, and a Compositional Autonomy Principle for preserving analogies during learning. These supply conditional diagnostics and theoretical arguments, not a demonstrated algorithm for generating or retaining new explanatory structures. Its stronger claims about intelligence, AGI, and LLM knowledge creation go beyond the causal-identifiability result.

## Quotes

No source quotes have been retained yet.

## Connections Found

The paper is a conceptual comparator for the [theory-builder definition](../notes/definitions/theory-builder.md): both tie the growth of knowledge to criticism, though the definition makes membership depend on a working criticism process and leaves improvement of future capacity to a separate test, where Thomas builds durable incorporation into learning itself. Thomas emphasizes changing what a learner can represent and test, while Commonplace separately chooses a recurrent causal path through retained, addressable theories. Its unreachable-error question sharpens [learning inside a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) by naming intervention semantics and invariance assumptions as possible revision targets. Neither connection supplies measured evidence that the proposed loop works.

The [theory-builder boundary](../notes/definitions/theory-builder.md) is decisive for reading the human–LLM discussion. Thomas credits the human with conjecture, criticism, and retention; the KB includes whoever performs those internal roles within the assessed system. [Retained artifacts enable deployment-time adaptation](../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) supplies the counterpoint: fixed weights do not establish fixed operative system state. The paper itself lists external memory and interface changes among possible ways of changing a hypothesis class, but does not evaluate such systems.

## Learning Claims (our opinion)

The source defines learning as durable incorporation of knowledge through criticism signals, including prediction errors, failed goals, violated constraints, inconsistencies, and representational limits. Its proposed division of labor is creative conjecture, comparative criticism, and structural revision. Bayesian comparison, predictive scoring, severity tests, and causal checks can perform criticism; none is presented as sufficient by itself to originate explanatory content. Proposed revision targets include variables, mechanisms, model classes, invariances, and intervention semantics. The proposal therefore concerns the contents and rules of inquiry as well as parameter values.

This partly maps onto the [theory-builder definition](../notes/definitions/theory-builder.md). Revising a formulated mechanism against criticism fits conditions 1 and 3. Introducing an entirely new representational apparatus fits too, since the definition lets revision change a core assumption, the problem, or the machinery, provided the result is a stated theory that is consumed, criticized, and retained. Separately editable mechanisms are finer [addressability](../notes/definitions/theory-builder.md#addressability), a design commitment above condition 1's minimum. Thomas's explanatory knowledge has stronger conditions than the KB's tentative theory: it must concern mechanisms and support counterfactual or interventional reasoning. The source's broad definition of learning also admits durable internal state that fails condition 1, so it covers systems outside the builder class. The paper describes no realized system, so it receives no builder verdict. Neither term should be substituted for the other.

The useful pressure on the KB is to specify which representation and criticism choices its own loop can revise. Changing an invariant, the interpretation of an intervention, or the tests that expose an error can matter more than revising a claim within unchanged tests. Yet the paper's diagnostics presuppose a chosen mechanism partition, algebra of primitives, covered compositions, and evaluation distributions. It does not supply an executed process that discovers and revises all those choices. Its formal results concern properties conditional on them, not evidence that the decomposition was learned or is preferable to alternatives.

The fixed-model argument needs a narrower boundary than the paper sometimes gives it. A fixed conditional-distribution family does not by itself establish that a surrounding system cannot generate, execute, criticize, and retain new programs or theories through its available interface. For Commonplace, the relevant question is whether the required correction lies outside the whole system's effective update space. The source's human–LLM dialogue account identifies a plausible route through human intervention and selection, but does not experimentally isolate the human's contribution or show that every model contribution is only reproduction of prior knowledge.

Reflection remains a separate [qualifier](../notes/definitions/theory-builder.md#qualifiers). Revising a theory of an external causal system is not yet revising a causally connected theory of the learner's own organization. Thomas demands endogenous hypothesis-space revision for general intelligence, but this paper supplies neither a realized reflective learner nor recurrent retention and consumption evidence. It motivates broader revision targets without establishing a reflective builder or requiring a change to the definition.

## Extractable Value

1. **Separate inquiry from its current computational realization.** The paper makes representation and intervention semantics explicit objects of conjecture. This helps the KB ask whether its machinery can revise the assumptions that make errors expressible, beyond revising theories within them. The contribution is a design question, not evidence that all fixed interfaces are inadequate. [quick-win]
2. **Use causal non-identifiability as a precise limit on observational evidence.** Observational agreement cannot distinguish interventions in otherwise observationally equivalent worlds without additional causal assumptions or evidence. This supports requiring a stated evidence interface rather than inferring causal adequacy from predictive fit. [just-a-reference]
3. **Test preservation of structure separately from task scores.** The proposed diagnostics measure unintended effects of local edits, violations of declared laws, and disagreement between translating before or after composition. They suggest candidate tests for modular theory updates, conditional on a justified partition and adequate test coverage; their value for KB artifacts remains untested. [experiment]

## Limitations (our opinion)

The source offers no benchmark, ablation, retained-update trace, or outcome comparison for its proposed learning program. Its standard non-identifiability argument bounds observational inference; it does not establish that AGI is chiefly theory-limited, that scale cannot help knowledge creation, or that every useful representational change requires a neural architecture edit. Definitions of intelligence and AGI stipulate a target and do not demonstrate necessity or sufficiency for an independently measured capability.

The paper sometimes treats structural intervention as necessarily changing the hypothesis space. That depends on the chosen space: an existing causal-model language may already express the intervened model. Likewise, fixed model weights, a fixed program language, and a fixed set of effective hypotheses are different restrictions. The KB's [effective-update-space distinction](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) requires examining accessible histories and composable operations before declaring an error unreachable.

The modularity arguments are conditional. Exact locality and disjoint mechanism support remove first-order gradient interference; that does not guarantee absence of forgetting for shared mechanisms, finite updates, or realistic training trajectories. Analogy diagnostics constrain covered primitives and compositions under mapping and regularity assumptions. Neither result demonstrates that a learner can discover the needed structure. The proposed constructor-theoretic task-cost alternative to description length is explicitly speculative and lacks practical surrogates. Part II is referenced but is outside this observation.

## Recommended Next Action

Closed: the [theory-builder definition](../notes/definitions/theory-builder.md#qualifiers) answers the question this ingest raised. Condition 3 allows revision to reach the representation and criticism machinery but does not require it; a builder whose method is itself stated, consumed, and criticized is reflective, a qualifier assessed separately from membership.
