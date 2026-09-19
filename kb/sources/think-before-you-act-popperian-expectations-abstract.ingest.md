---
description: "Mills and Lewis propose retaining causal expectations from internal simulations; the abstract motivates reuse but leaves refutation, representation changes, and reflective learning unestablished."
source: https://www.trustworthyai.ca/publication/think-before-you-act-popperian-expectations-for-adaptive-agents/
captured: "2026-09-19"
capture: trafilatura
capture_scope: abstract
doi: "10.1109/ACSOS-C66519.2025.00038"
genre: scientific-paper
snapshot_sha256: b1901435761a08ab54fa5e6a8b42b5766226b69ad8928e81a1f688611ed188ce
ingested: "2026-09-19"
occasion: "Reconsider the learning paradigm from Popperian epistemology: compare the epistemic process, computational realization, changeable representations and tests, fixed-model learning, reflection, and supporting evidence."
type: kb/sources/types/ingest-report.md
domains: [learning-theory, agent-memory, internal-simulation]
learning_claims: true
---

# Ingest: Think Before You Act: Popperian Expectations for Adaptive Agents

## Classification

The retained source is an author-hosted abstract of a six-page paper in the 2025 IEEE ACSOS Companion proceedings. It proposes an agent architecture and identifies its formalism, but the retained text contains no experimental results. Authors: John Mills and Peter R. Lewis; the publication venue and DOI establish a research publication, without independently establishing the proposal's effectiveness.

## Summary

Mills and Lewis propose extending Winfield's consequence engine with retained causal expectations learned from internal simulations. Their stated problem is that an agent can predict action consequences without physical commitment yet repeatedly simulate familiar scenarios if it cannot retain what those simulations taught it. The proposed architecture uses the Expectation Event Calculus (EEC) to create, update, and use interpretable causal expectations. The abstract presents this as a route to reflective reasoning and adaptation; it does not describe update rules, show how expectations are tested against the environment, or report efficiency, safety, or learning results.

## Quotes

No source quotes have been retained yet.

## Connections Found

For the learning-paradigm comparison, this is a proposed computational realization to compare with [learning by theory refinement](../notes/definitions/learning-by-theory-refinement.md): expectations are meant to persist, change, and guide action, but the abstract does not establish the outcome-driven revision and later reuse that close that loop. It also supplies a concrete retention problem alongside [discarding all experience-dependent state prevents cross-run accumulation](../notes/ephemeral-computation-prevents-accumulation.md). The useful shared distinction is between computing a consequence once and preserving something that can affect later decisions. Neither connection supplies evidence that this architecture successfully implements the full learning loop.

## Learning Claims (our opinion)

On the authors' account, internal simulation produces knowledge that an agent represents as causal expectations using EEC, retains, updates, and uses. EEC is the named formalism for those expectations; its syntax, inference rules, and revision operations are outside the capture. The available learning signal is described as simulation-derived. Whether environmental observations independently challenge the expectations, the simulator, or both is unresolved.

Relative to [theory refinement](../notes/definitions/theory-refinement.md), creating an expectation and reusing it are insufficient to establish revision against empirical cases. Updating an expectation might qualify, but the abstract does not show contradiction detection, candidate repair locations, or separately editable parts. Our epistemic reading therefore separates extracting reusable consequences from an internal model from correcting that model's mistaken claims. Simulation can expose consequences of assumptions without independently testing their truth. The Popperian name alone does not resolve which operation occurs here.

The explicit proposed changes are to expectations. The abstract does not say whether the simulator, EEC vocabulary, admissible actions, or test criteria can change. Following [learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), this leaves the effective update space unknown; it does not demonstrate that these choices are fixed or revisable. Retaining expectations suggests a possible learning path without changing model weights, but no fixed-weight model condition is reported. Finally, the authors' reflective-reasoning claim does not establish Commonplace's reflective case: the abstract describes action-consequence knowledge, without showing revision of a causally connected representation of the agent's own organization. This source identifies a relevant architecture to investigate, rather than requiring a change to our definitions.

## Extractable Value

1. **A concrete candidate for the epistemic-process comparison.** The proposed simulation-to-expectation path makes the decisive question specific: does the agent revise expectations from independent errors, or mainly retain consequences of its simulator? The abstract identifies the question without answering it. [deep-dive]
2. **Retention as a separate architectural function.** The motivation distinguishes prediction without physical action from retaining reusable knowledge of predicted consequences. That distinction is useful for KB designs that repeatedly reconstruct the same conclusion, although the source supplies no measured saving or validated reuse policy. [just-a-reference]

## Limitations (our opinion)

The capture is abstract-only. It cannot establish the formal semantics of EEC, implementation details, baselines, experimental interventions, or outcomes. The abstract's criticism of repeated simulation is the authors' motivation; it does not show how often repetition occurs or whether retaining and checking expectations is cheaper. A simpler account of any potential efficiency benefit is reuse of prior computation. Evidence distinguishing that benefit from error-correcting learning would be needed before attributing it to the Popperian mechanism.

No tested comparison is available, so the ingest cannot identify a controlled decomposition or attribute gains to any component. Nor does the abstract establish that simulated expectations remain reliable when the environment differs from the simulator. Missing descriptions of refutation, reflection, and representation changes leave these questions open; they do not establish that the full paper omits them.

## Recommended Next Action

Obtain and ingest the full paper as a distinct observation to resolve whether independent environmental errors revise retained expectations or the simulator, for comparison with [learning by theory refinement](../notes/definitions/learning-by-theory-refinement.md).
