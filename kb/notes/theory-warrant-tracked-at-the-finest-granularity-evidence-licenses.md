---
description: "Treat support for a theory as warrant for only the most specific claim, conjunction, model, and scope the evidence identifies; do not distribute joint warrant beyond what it entails without additional attribution"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, learning-theory, discovery]
---

# Theory warrant should be tracked at the finest granularity evidence licenses

A theory here is an account whose premises, mechanism, consequences, and scope can be inspected and revised as named parts and that has at least one implication that could discriminate it from a rival. **Epistemic warrant** is support that licenses reliance on specific truth-apt content over a specific domain. Track warrant at the finest granularity the support identifies. Often, that unit is one claim together with its supported scope. When evidence discriminates only a conjunction or integrated model, the warranted unit is that bundle and its scope. Joint warrant then reaches a component only through an identified route. Entailment is one such route: warrant that a literal conjunction is true warrants each conjunct. Comparative support — evidence that an integrated model outperforms a rival — entails no component's truth or causal contribution, so it stays joint until further evidence or argument attributes it.

This is a bookkeeping rule, not a proposal for a new unit of theory or a denial that a scoped theory-level claim can be warranted. Its job is to stop evidence for one claim, bundle, or domain from spreading silently across a document.

## Criticizable structure gives candidacy, not warrant

Naming a theory's parts gives critics useful targets only when the account also exposes the dependencies among them, rival-sensitive consequences, transfer boundaries, and possible falsifiers. A critic can then vary a premise and check the predicted change in the conclusion, exclude a rival, or state where transfer should stop. This makes the theory a candidate for [explanatory-reach](./first-principles-reasoning-selects-for-explanatory-reach-over.md): the account may keep working wherever its named dependencies hold.

Exposure is not support. Structure shows what evidence would count for or against each part; it does not supply that evidence. A stated boundary may track a correlate of the mechanism rather than the mechanism itself. A consumer who matches a new case to that boundary then inherits the error.

A theory crosses the structural threshold by exposing its dependencies and possible failures. A claim, conjunction, or model crosses the epistemic threshold only when it acquires warrant over a stated scope. [Reach-assessment](./definitions/reach-assessment.md) — judging whether a commitment works beyond the evidence that produced it — assesses the surplus scope. Evidence or proof must still warrant the cases or formal domain that it directly covers.

## Support follows evidence before dependencies propagate it

The warrant routes developed for reusable decompositions provide a proposed map for theory parts: [derivation and inheritance give starting warrant while discriminating evidence or proof earns scope](./derivation-and-inheritance-give-starting-warrant-earns-scope.md). Derivation from supported constraints gives conditional starting warrant. Inheritance transfers warrant only when relevant source tests were discriminating and the target preserves the constraints that made the source claim work. Discriminating evidence earns warrant only for the cases and failure modes it exercises, whether it takes the form of an intervention, held-out comparison, or risky prediction that relevant rivals would handle differently. Transfer beyond direct support requires a justified relation between the evidence and the target class, such as coverage, sampling, or an invariant mechanism.

These routes do not force component-level attribution when the evidence is joint. A test that discriminates only an integrated bundle from a rival warrants the bundle-scope pair. It does not by itself reveal which component produced the result. Where the warranted content entails a component outright — a supported conjunction entails its conjuncts — derivation transmits warrant without further evidence. Where the support is comparative rather than entailing, additional interventions, comparisons, proofs, or identification assumptions are needed before assigning it to individual components.

Evidential attribution and dependency propagation are separate operations. First, identify the most specific truth-apt unit the evidence supports. Then use the theory's dependencies to determine which other units inherit a derivation or lose warrant when a premise fails. A failed premise may affect one claim or every central commitment; the fact that they share a document does not determine either result.

One document can therefore mix observations, derived consequences, inferred mechanisms, and conjectured boundaries. [Mixed epistemic status must be preserved below the document level](./mixed-epistemic-status-must-be-preserved-below-the-document-level.md) because neither one document label nor one successful joint test assigns the same status to every component.

[Representational form](./definitions/representational-form.md) — whether retained content is encoded in natural language, symbols, model weights, or a mixture — changes which checks are available, but it does not relax the non-distribution rule. A natural-language claim is warranted under an interpretation of its words. Formalization strengthens the checking of consequences within a chosen translation. A proof warrants the consequences it entails in that formal domain, not claims the translation omitted or changed. Comparative support for an integrated model remains joint until further evidence attributes it, whatever form records the theory.

## One theory can carry individual and joint warrant

The account that [agent context is constrained by soft degradation rather than hard token limits](./agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md) crosses the structural threshold: it states a mechanism, predictions, and a falsifier. Its empirical inputs concern particular tasks and models; its headline claim is broader; and its workspace mechanism is a working hypothesis. The narrow regularities may carry individual warrant. A test of the integrated account might instead warrant only a joint model claim. Neither result gives the document a uniform status or assigns support to every component.

## Scope

- This note proposes evidence-relative bookkeeping, not an ontology that excludes scoped conjunctions, comparative model claims, or whole-theory propositions from carrying warrant. Joint warrant distributes to components only through entailment or evidence that attributes it; comparative support supplies neither by itself.
- Applying the linked warrant routes from reusable decompositions to claims and bundles inside theories is a proposed extension that has not been separately tested.
- Claim granularity depends on truth-apt content under an interpretation. Separate contents when reliance on one need not commit a consumer to the other; keep support at bundle level when the available evidence supports only their joint adequacy rather than the truth of each. Whether interpretations remain stable across readers, contexts, and wordings is an open empirical question.
- This note does not say how often theories achieve reliable generalization or how reliably human or language-model criticism assesses it.

---

Relevant Notes:

- [Reach-assessment](./definitions/reach-assessment.md) — defined-in: the judgment that separates directly checked cases from claimed generalization beyond them
- [Mixed epistemic status must be preserved below the document level](./mixed-epistemic-status-must-be-preserved-below-the-document-level.md) — extends: develops evidence-granular warrant into an authoring and review rule
- [Domain pricing routes an exception to idealization assessment but does not decide it](./domain-pricing-routes-an-exception-to-idealization-assessment.md) — extends: develops the non-distribution rule into a two-stage review architecture where routing and adequacy evidence carry different authority
