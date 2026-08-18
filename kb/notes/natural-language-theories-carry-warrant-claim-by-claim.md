---
description: "Warrant attaches to individual claim-scope pairs inside a natural-language theory; criticizable structure makes the theory assessable but does not warrant it as a whole"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, learning-theory, discovery]
---

# Natural-language theories carry warrant claim by claim and scope by scope

A theory here is an account whose premises, mechanism, consequences, and scope can be inspected and revised as named parts, with at least one implication that could discriminate it from a rival. **Epistemic warrant** — support that licenses reliance on a specific claim over a specific domain — does not attach to such a theory as a whole. It attaches to **claim-scope pairs**: one material claim together with the domain its support covers. The pair is bookkeeping, not a new unit of theory; its job is to stop evidence for one claim or domain from spreading silently across the document.

## Criticizable structure gives candidacy, not warrant

Because a theory's parts are named, criticism has targets: vary a premise and check the predicted change in the conclusion, exclude a rival, state where transfer should stop, name a falsifier. This makes the theory a candidate for [explanatory-reach](./first-principles-reasoning-selects-for-explanatory-reach-over.md) — the account can keep working wherever the dependencies it names hold. But exposure is not support. Structure shows what evidence would count for or against each part; it does not supply that evidence. A stated boundary may track a correlate of the mechanism rather than the mechanism itself, and a consumer who matches a new case to it inherits the error.

This separates two thresholds. A theory crosses the structural threshold by exposing its dependencies and possible failures; each claim in it crosses the epistemic threshold only by acquiring warrant over a stated scope. [Reach-assessment](./definitions/reach-assessment.md) judges the second.

## Support accrues pair by pair

Each pair earns its support by its own route, as [derivation and inheritance give starting warrant while discriminating evidence or proof earns scope](./derivation-and-inheritance-give-starting-warrant-earns-scope.md). Derivation from independently supported constraints gives conditional starting warrant. Inheritance from tested work transfers warrant only when the source tests discriminated relevant rivals and the target preserves the constraints that made the source claim work. Discriminating evidence — an intervention, held-out comparison, or risky prediction that rivals would handle differently — earns the cases and failure modes it exercises. Transfer beyond the tested domain needs a justified relation between the evidence and the target class, such as coverage, sampling, or an invariant mechanism; which relation suffices is domain-dependent.

Two consequences follow. A document that mixes observations, derived consequences, abductive mechanisms, and conjectured boundaries carries mixed status by construction — which is why [mixed epistemic status must be preserved below the document level](./mixed-epistemic-status-must-be-preserved-below-the-document-level.md). And correction is local: a failed premise or a revised boundary withdraws warrant only from the pairs that depend on it, not from the theory.

[Representational form](./definitions/representational-form.md) does not change where warrant attaches. Natural-language consequences arise through interpretation, so a warranted pair is warranted under an interpretation of its claim. Formalization strengthens consequence-checking inside a chosen translation — as [formal systems assess explanatory-reach through causal and proof obligations](./formal-systems-assess-explanatory-reach-through-causal-and-proof.md) — but proving a translated consequence warrants that consequence, not the claims the translation omitted or changed.

## One theory, uneven warrant

The account that [agent context is constrained by soft degradation rather than hard token limits](./agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md) crosses the structural threshold: it states a mechanism, predictions, and a falsifier. Its warrant is uneven — the empirical inputs are specific to particular tasks and models, the headline claim is broader, and the workspace mechanism is a working hypothesis. Read pair by pair, the theory is partly warranted and partly conjectural; no document-level label captures that.

## Scope

- This note fixes where warrant attaches. It does not say how often natural-language theories achieve explanatory-reach, or how reliably human or language-model criticism assesses it.
- The warrant-routes account it leans on is framed for reusable decompositions; extending those routes to claims inside a theory is an inference that has not been separately tested.
- A pair is warranted under an interpretation. Whether that interpretation stays stable across interpreters, contexts, and wordings is an open empirical question, not part of the warranted scope.

---

Relevant Notes:

- [Reach-assessment](./definitions/reach-assessment.md) — defined-in: the judgment that separates claimed explanatory-reach from adaptive fit
- [Derivation and inheritance give starting warrant; discriminating evidence or proof earns scope](./derivation-and-inheritance-give-starting-warrant-earns-scope.md) — grounds: the routes by which individual pairs gain starting warrant and earn scope
- [Mixed epistemic status must be preserved below the document level](./mixed-epistemic-status-must-be-preserved-below-the-document-level.md) — extends: develops this claim-level accrual into an authoring and review rule
- [Formal symbolic systems assess explanatory-reach only through causal and proof obligations](./formal-systems-assess-explanatory-reach-through-causal-and-proof.md) — contrasts: what formal checks warrant inside a translation, and what stays outside it
