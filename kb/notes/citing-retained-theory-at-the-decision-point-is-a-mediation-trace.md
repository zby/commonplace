---
description: "A decision record that cites the theory it followed supplies cheap, checkable evidence that the theory was consumed — necessary for a record-based mediation claim, but short of showing correct or load-bearing use"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, self-improving-systems]
---

# Citing retained theory at the decision point is a mediation trace

A system that retains theory and also changes itself invites an attribution: *this change was guided by that theory*. The attribution needs evidence, because two situations produce the same surface record. In one, the retained theory entered the decision and shaped it. In the other, the theory sat in the repository while the decision was made on other grounds, and the two merely co-occur. Co-occurrence is the expected case rather than a remote failure, because retained theory can accumulate faster than it is consulted, and [a stored representation that is never consulted is inert](./an-action-model-matters-only-through-its-consumption-path.md).

A **mediation trace** is a record that discriminates between those two situations. The cheapest available form is a citation placed where the decision is made: the commit message names the ADR it implements, the ADR names the note whose argument it applies, the workshop entry names the claim it is testing, the review packet names the criterion it applied. The citation is not decoration on the decision record; it is the evidence that a mediation claim later rests on.

## Why the citation carries evidential weight

Two properties do the work, and they are separable.

It is **cheap**, because [reflection buys addressability](./reflection-buys-addressability.md): where retention runs through a readable self-representation, the retained theory is a nameable object with a stable handle, so recording which one was consumed costs a path and a phrase. It is also cheap for the same reason that [the why is cheap at the decision surface and expensive to recover from the state it produced](./structure-inference-needs-capture-at-the-decision-surface.md) — at the moment of decision the deciding process is already holding the material that explains it.

It is **checkable**, because a reader can open the cited artifact and ask a specific question of it: does this argument determine this decision, or is the decision underdetermined by it? That question has a wrong answer. A citation to an artifact whose content does not bear on the decision is visibly a bad citation, which is what makes the good ones informative.

Placement matters as much as content. [Production history is convertible to checkable form at production time](./history-has-one-chance-to-become-checkable.md), by records or by re-derivability. A decision made by a language model in one context window is not re-derivable, so the records route is what remains, and the record has to be written where the decision was made.

## What the trace shows and what it does not

A citation establishes one link in a [behavioral-authority](./definitions/behavioral-authority.md) path: it identifies which retained artifact a named consumer took up. That is narrower than it looks, and three gaps stay open.

- **Correct application.** The trace shows the theory was read; it does not show it was read correctly. A decision can cite an argument and then draw a conclusion the argument does not license.
- **Load-bearing versus decorative use.** A citation can name the theory the decider endorses rather than the one that actually moved the decision. This is the espoused-theory gap under a different name, and a decorative citation looks the same on the page as a governing one.
- **Testing.** A trace records that the theory was consumed. It says nothing about whether the outcome went on to support or defeat the theory, and [an accepted result verifies the change rather than the rule behind it](./an-accepted-edit-verifies-the-change-not-the-rule.md).

So the trace is necessary evidence for a record-based mediation claim and not sufficient for one. If no record names a theory, an attribution to that theory rests on memory or assertion rather than on anything a later reader can check. The protocol that would close the remaining gaps adds a second step in the other direction: read the outcome back against the cited theory, and record whether it went as the theory predicted. That step is the same displacement [that separates compounding from repeated maintenance](./compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) — the evidence has to come from a later episode and a quantity other than the one that accepted the change. Citation plus read-back is a loop; citation alone is a pointer.

## Two failure modes

**Post-hoc citation.** A citation added after the decision, during cleanup or review, records what a later reader thought was relevant rather than what the decider consumed. The reconstructed record can look identical to a contemporaneous one, so the practice degrades what a reader can infer from citations across the corpus, not only from the reconstructed entry. This is the practical cost of the production-time constraint: once the moment passes, the cheap and honest route is to say the decision's grounds were not recorded.

**Citing what was loaded rather than what governed.** An agent working with a large retrieved context can cite everything it retrieved. The resulting record is a retrieval log wearing a mediation trace's clothes. The trace is informative in proportion to how selective it is, so the useful citation names the artifact whose content the decision would change without, not the artifacts that happened to be in the window.

Both failures share a shape: the citation stops tracking consumption and starts tracking something correlated with it. Neither is detectable from the record alone, which is why a corpus of traces needs occasional audit against an independent signal rather than trust by accumulation.

## Scope

- The claim applies where decisions are recorded in addressable artifacts and the retained theory has a stable reference. Where reasoning is weight-resident, or happens inside one context window and is discarded, there is no decision record to carry a citation; mediation there has to be probed — by ablation, by paired replay with the theory withheld, or by interpretability tooling — rather than read off a trace.
- Cheapness is relative to the recording practice already in place. Where decisions are not recorded at all, adding the citation means adding the decision record, which is a larger cost than a phrase.
- The note treats the citation as evidence about consumption. It takes no position on whether citing a theory is good practice for reasons other than traceability, such as making the decision reviewable by a person.
- A trace is evidence for a mediation claim about one decision. Aggregating traces into a claim about a system's pathway needs its own argument, since [warrant tracks at the granularity the evidence identifies](./theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md).

## Open Questions

- How to distinguish a decorative citation from a load-bearing one without running an intervention. The clean test withholds or replaces the cited theory and checks whether the decision changes, but [that contrast has to actually be run](./an-experiment-identifies-only-the-contrast-it-actually-runs.md), and it is unavailable for decisions already made. Whether a weaker signal — citation selectivity, the specificity of the claim cited, whether the decision record restates the argument rather than only naming it — carries enough discrimination is untested.
- Whether a corpus of traces degrades predictably as citation becomes routine, in the way a recorded signal can drift once it is expected, and what audit rate would keep it honest.
- Whether the read-back step can be automated at all, or whether judging an outcome against a cited theory remains a judgment a person supplies.

---

Relevant Notes:

- [Reflection buys addressability](./reflection-buys-addressability.md) — grounds: supplies the addressability that makes the cited theory a nameable object with a stable handle
- [Behavioral authority](./definitions/behavioral-authority.md) — defined-in: names the consumer, channel, and force that a citation identifies one link of
- [Bottom-up structure inference needs capture at the decision surface, not the state](./structure-inference-needs-capture-at-the-decision-surface.md) — mechanism: explains why the why is cheap at the decision point and expensive to recover afterward
- [History has one chance to become checkable](./history-has-one-chance-to-become-checkable.md) — grounds: the production-time constraint that makes post-hoc citation a different and weaker record
- [Compounding is tested in later improvement, not by the accepting metric](./compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) — extends: supplies the displaced read-back that a citation alone does not provide
- [An accepted edit verifies the change, not the rule](./an-accepted-edit-verifies-the-change-not-the-rule.md) — contrasts: the parallel gap on the outcome side — acceptance judges the instance, citation records the consumption
- [An experiment identifies only the contrast it actually runs](./an-experiment-identifies-only-the-contrast-it-actually-runs.md) — grounds: bounds what the withhold-the-theory intervention could establish about decorative citation
- [Theory warrant should be tracked at the finest granularity evidence licenses](./theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md) — extends: constrains aggregating individual traces into a pathway-level mediation claim
- [An action model matters only through its consumption path](./an-action-model-matters-only-through-its-consumption-path.md) — grounds: the inertness of stored-but-unconsulted representation that makes co-occurrence the default expectation
- [Reflective system](./definitions/reflective-system.md) — defined-in: the two-way causal connection a mediation trace supplies observed evidence for in one direction
- [The tag-readme change as an observed causal-connection trace](./evidence/tag-readme-trace-observed-causal-connection.md) — evidenced-by: one worked instance where the decision records name the retained claim they were read through
- [A consumption channel delivers force without the history that earned it](./a-consumption-channel-delivers-force-without-the-history-that.md) — contrasts: the converse gap — the path confers force without reading the record, where a trace records the read without conferring correctness
- [Theory-mediated self-improvement needs both interpretation and retention from one substrate](./theory-mediated-self-improvement-needs-interpretation-and-retention.md#the-attribution-needs-one-co-indexed-path) — extends: the co-indexed path a citation plus read-back serves; a citation alone is a pointer
