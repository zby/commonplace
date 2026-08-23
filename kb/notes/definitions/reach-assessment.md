---
description: "Definition — judging whether a commitment's claimed explanatory-reach is genuine across natural-language, symbolic, and distributed-parametric forms"
type: kb/types/definition.md
tags: [foundations, computational-model, self-improving-systems]
---

# Reach-assessment

**Reach-assessment** is the capability of an evaluation process to judge
whether a candidate commitment's claimed
[explanatory-reach](../first-principles-reasoning-selects-for-explanatory-reach-over.md)
is genuine rather than adaptive fit presented as explanation. It evaluates the
content of the claim: whether the proposed mechanism or invariant supports the
generality claimed. Checking that a new case matches the commitment's stated
condition checks only the condition, not whether that condition names the real
boundary.

For example, retaining “route prompts under 500 tokens to a cheaper model”
after several successes does not establish that length explains task
difficulty. Reach-assessment must distinguish that mechanism from a correlation
in the fitting cases, such as by varying complexity while holding length fixed.

## Scope

The assessment route must match the
[representational form](./representational-form.md) carrying the commitment:

- Natural-language commitments require semantic judgment of their mechanism,
  alternatives, scope, and observed fit, such as the
  [four-part explanatory-reach test](../first-principles-reasoning-selects-for-explanatory-reach-over.md).
- Symbolic commitments can be assessed through intervention, invariance, or
  proof obligations when the relevant causal structure or domain has been
  formalized. The developed boundary is
  [formal symbolic systems assess explanatory-reach only through causal and proof obligations](../formal-systems-assess-explanatory-reach-through-causal-and-proof.md).
- Distributed-parametric commitments can be assessed through
  action-conditioned predictions tested over the interventions or shifts the
  commitment claims to cover. The developed route is
  [world models assess explanatory-reach through action-conditioned prediction](../world-models-assess-explanatory-reach-through-action-conditioned.md).

Mixed artifacts may compose these routes, but an assessment of one form does
not automatically warrant the others. Proof reaches only across its
axiomatized domain; observed predictive fit reaches only across the tested
shift class.

[Reflectivity](./reflective-system.md) supplies addressability, not this
judgment. A reflective process may represent, match, reject, or rescope a
commitment without being able to tell whether its stated scope is honest.

## Exclusions

- Reach-assessment is not boundary matching, metadata checking, confidence, or
  the structural capacity to rewrite a commitment.
- Empirical success on the fitting cases does not establish the mechanism or
  its reach beyond them.
- Causal vocabulary, a proof engine, or a learned world model does not by
  itself supply reach-assessment. The evaluation process must exercise the
  relevant causal, proof, intervention, or shift test.
- Observational causal discovery is not assumption-free; its warrant remains
  conditional on its discovery assumptions.

## Provenance and open boundary

The causal, proof, and predictive-world-model routes are established external
machinery. Commonplace's contribution is to group them by the role they play
when an improvement pathway evaluates a retained commitment. The
natural-language route remains unexplained: LLM-mediated evaluators appear able
to judge prose generalizations with some reliability, but this definition
names that missing capability rather than supplying a theory of it.

The hyphenated compound **reach-assessment** carries this technical sense, and
**explanatory-reach** names the property it judges. Bare *reach* remains
ordinary English. The oracle-side limit is **oracle domain** and the
generator-side limit is **search range**.

## Misuse Cases

- Assuming that a reflective system has reach-assessment because it can revise
  a stored scope statement.
- Treating a passing test suite or accurate predictor as evidence of reach
  without testing the claimed mechanism, intervention, or shift boundary.
- Citing this definition to claim that reach-assessment is unique to LLMs;
  causal inference and proof provide older formal routes.

---

Relevant Notes:

- [Reflective system](./reflective-system.md) — contrasts: supplies the structural capacity to represent and rewrite scope; reach-assessment is the judgment that capacity does not supply
- [Representational form](./representational-form.md) — grounds: the form carrying the commitment determines which assessment route is available
- [Formal symbolic systems assess explanatory-reach only through causal and proof obligations](../formal-systems-assess-explanatory-reach-through-causal-and-proof.md) — extends: develops the symbolic causal and proof routes and their formalization boundary
- [World models assess explanatory-reach through action-conditioned prediction](../world-models-assess-explanatory-reach-through-action-conditioned.md) — extends: develops the distributed-parametric route and its shift boundary
- [First-principles reasoning selects for explanatory-reach over adaptive fit](../first-principles-reasoning-selects-for-explanatory-reach-over.md) — grounds: supplies the four-part negative test for natural-language commitments
- [Abstract an experience into a lesson only when you can state where the lesson stops](../abstract-an-experience-only-when-you-can-state-the-boundary.md) — grounds: identifies boundary selection as judgment rather than mechanical derivation
- [Theory-mediated learning may improve sample efficiency under structured shifts](../theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) — extends: makes reach-assessment the load-bearing condition of the proposed sample-efficiency payoff

Derived into:

- [Formal symbolic systems assess explanatory-reach only through causal and proof obligations](../formal-systems-assess-explanatory-reach-through-causal-and-proof.md) — the causal and proof routes worked out from this definition's representational-form split
- [World models assess explanatory-reach through action-conditioned prediction](../world-models-assess-explanatory-reach-through-action-conditioned.md) — the distributed-parametric route worked out from this definition's representational-form split
