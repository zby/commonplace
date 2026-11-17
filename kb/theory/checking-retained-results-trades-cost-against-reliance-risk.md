---
description: "Retaining a derived result saves recurring work; how often to check it trades check cost against the risk of relying on stale or wrong content, worked through the completeness mark and the connect report"
type: types/note.md
traits: [title-as-claim]
tags: [context-engineering, kb-maintenance, claims-and-grounding]
---

# Checking retained results trades cost against reliance risk

A retained derived result saves work: a consumer that reads it skips the discovery and derivation it would otherwise repeat on every use, so one production is amortized over many uses. This is the saving [frontloading spares execution context](./frontloading-spares-execution-context.md) argues for results computed before an LLM call, extended here to persisted artifacts. Checking spends part of that saving. A check that fully recomputes the result on every use largely defeats it; when verification is cheaper than derivation, checking on every use can still save work.

Against the saving stands the risk of reliance. A retained result goes stale because its source and the copy have separate update paths. A stale copy can also hide its own error: when a consumer treats the copy as exhaustive and stops on it, the copy suppresses the search that would have exposed what it misses, which is how [indexes lower recall when they suppress retrieval that would find more](./indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md). This requires that the consumer actually stops and that the suppressed search would find more task-relevant material.

How often to check a retained result therefore depends on the cost of checking relative to the risk of relying on stale or wrong content. Accepting some risk between checks can be right, provided it is an explicit choice rather than a hidden consequence of trusting the copy. Two retained results in this KB land differently.

## The completeness mark: a stop-authorizing claim with a defined check

A tag head's `complete: true` [mark](../types/tag-readme.md) asserts that every artifact carrying the tag in the participating collections is reached from the head in one hop. Its contract lets readers skip the by-tag `rg` membership search. That permission is the mark's value and its risk: a false mark tells exhaustive consumers to stop looking while members are still out there.

The validator performs the membership derivation when the head is validated, rather than on every read. This lets subsequent reads reuse the checked result. The check applies a defined rule (one-hop reach over tagged artifacts) to named inputs (the participating collections and nothing else), which the validator reads when they are supplied. An inexpensive, defined check on a claim that authorizes stopping makes enforcement attractive. Enforcement is reactive: the validator flags a gap when the head is next validated, so a mark can be false in between. The check covers reach given the tags; whether an assignment fits the tag is for semantic review.

## The connect report: candidates whose reuse can be reasonable

A [connect report](../types/connect-report.md) records one discovery pass for a target artifact and proposes candidate links. Its contract tells readers to treat the contents as suggestions to evaluate, not as state already in the KB, so it does not authorize stopping the way the mark does. Assessing a candidate against the target's actual claim, evidence and contract calls for judgment. Some properties remain mechanically checkable, such as link resolution and required sections, but checking them does not reconstruct that judgment.

Rerunning discovery costs real work, and the result's dependencies are broad. A pass reads indexes and runs searches across the KB, so material added anywhere it searches may change what a renewed pass finds. The design difficulty is tracking a sufficient dependency set, including newly added relevant material. Reusing an earlier report can be reasonable when rerunning costs more than the risk accepted for the task. That risk is not zero: a consumer that treats a report as the full set of connections falls under the suppression mechanism, and a missed connection need not announce itself.

## No known change does not establish freshness

The absence of a known change is evidence of freshness only if every relevant change reaches the checker. Even the enforced mark can be stale until its head is next validated, and a reused connect report reflects the KB as of its pass. Assurance dates from the last check.

## What a mechanical check requires

A mechanical check derives a retained result from, or compares it against, identified available inputs. Relying on one requires:

1. **A derivation or comparison rule** that can be applied without judgment.
2. **A locatable copy and source:** the checker can find the retained result and the inputs it depends on.
3. **A source available at check time.**
4. **A sufficiently trustworthy checker.** Testing or centralizing a validator lowers the cost of assurance but does not prove the validator correct.

These conditions make a check possible and worth relying on, not free or current. The mark's contract supplies the first three; nothing in it establishes the fourth.

## Scope

- The trade-off is qualitative. No costs, risks or refresh intervals are calibrated.
- The suppression mechanism is conditional. It makes no claim about how often consumers stop on a copy or how often the fallback search finds more.
- The connect report's candidate-only status is a contract on readers, not evidence of how consumers behave.

## Open Questions

- When is a checker trustworthy enough to rely on?
- Do omissions in candidate-only results such as connect reports usually fail silently?

---

Relevant Notes:

- [LLM recompute cost inverts the store-vs-recompute default](./llm-recompute-cost-inverts-the-store-vs-recompute-default.md) — grounds: why recomputation is costly enough for retained results to be worth keeping
- [An enforced tag-README is a MOC with a machine-checked contract](./an-enforced-tag-readme-is-a-moc-with-a-machine-checked-contract.md) — extends: develops the completeness-mark example
- [History has one chance to become checkable](./history-has-one-chance-to-become-checkable.md) — contrasts: content with no later source to check against, where condition 3 fails
