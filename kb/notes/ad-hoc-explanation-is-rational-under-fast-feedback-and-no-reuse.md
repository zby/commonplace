---
description: "Prices two explanation regimes: local disposable guesses are rational under fast feedback and no reuse, reach machinery is priced for retention, so a KB charges the reach toll only at promotion"
type: kb/types/note.md
traits: [title-as-claim, has-comparison]
tags: [learning-theory, discovery, kb-maintenance]
---

# Ad hoc explanation is rational under fast feedback and no reuse

## Which sense of "ad hoc" this note uses

Two senses travel under the same phrase, and conflating them makes the claim below look like a defence of bad epistemics.

The **narrow** sense is the methodological one associated with Popper: an ad hoc modification is a content-reducing rescue that saves a theory from a refutation by removing what the theory forbade. That move is bad in both regimes described here, for the same reason in each — it buys survival by destroying the theory's testable content — and this note sets it aside entirely. Nothing below licenses it.

The **broad** sense is the everyday one, and it is this note's subject. An **ad hoc explanation** is a local, unintegrated account produced at the point of need, consumed to pick the next action, and discarded. It is not checked against the rest of what the agent believes, it is not written down for anyone else, and it forbids nothing beyond the case in front of it. "The build probably failed because the cache is stale" is an ad hoc explanation: it is a guess about a mechanism, it selects the next command, and after the rebuild nobody keeps it.

## The three conditions

An ad hoc explanation is rational when all three of these hold, and it loses its warrant as any one of them fails:

1. **Feedback is fast and cheap.** Acting on the guess returns a verdict quickly, and a wrong guess costs about one iteration.
2. **Nothing later reuses it.** The explanation is consumed by the action it selects and does not become an input to a further decision.
3. **Coherence demands are low.** Being wrong does not silently damage commitments made elsewhere, because nothing elsewhere depends on this account being true.

The mechanism is a substitution: cheap iteration compensates for weak theory quality. Under these conditions the environment is a better critic than any amount of pre-action reasoning, and it is a *faster* critic. Deriving consequences and testing them before acting spends the resource — iterations — that the guess would have spent anyway, and returns a verdict no earlier. The guess is not a shortcut past rigour; under fast feedback it *is* the cheaper test.

The conditions are the claim's boundary, and each fails distinctly. When feedback is delayed, a wrong guess is not corrected within the episode, so the agent keeps acting on it and the errors compound before any verdict arrives. When the explanation is reused, its error rate is paid once per consumer instead of once. When coherence demands are high, a wrong local account can be contradicted by a commitment the agent never re-examined, and the damage surfaces far from its cause.

## Reach machinery is priced for the opposite conditions

The heavy phases of the [discovery lifecycle](./definitions/discovery-lifecycle.md) — derive consequences, test against cases, integrate with prior claims — are the machinery that produces explanations with reach. That machinery is expensive on purpose, and its price buys exactly what the fast-feedback regime does not need: an account that survives contact with cases nobody has run yet, that stays true when a later consumer imports it, and that has been reconciled with what the system already holds.

So the two regimes are not better and worse practice. They are two pricings of the same activity, each matched to a different cost structure, and each is a failure when applied to the other's conditions:

| | Fast-feedback regime | Retention regime |
|---|---|---|
| Feedback latency | one iteration | delayed, sometimes indefinitely |
| Reuse | none; consumed by one action | artifact is a premise for later work |
| Coherence demand | low; nothing depends on it | high; a web of prior commitments |
| Rational method | guess, act, observe | derive, test, integrate |
| Wrong-way failure | over-ceremony | contamination |

Importing reach machinery into the fast-feedback regime is **over-ceremony**: it spends the iterations that would have answered the question, to produce a general account of a situation that will not recur. Importing ad hoc habits into the retention regime is **contamination**: an unintegrated local guess enters the durable set, later work builds on it, and the error propagates through consumers that never see the case that produced it. Contamination is the failure the quality bar exists to catch.

## Two bridges to what the KB already holds

**An ad hoc explanation is the degenerate case of a fallible held theory.** Since [holding a program theory means sustaining coherent search under delayed feedback](./program-theory-sustains-search-under-delayed-feedback.md), the work a theory does is control over search: it narrows candidates, interprets failures, and says when to backtrack. An ad hoc explanation does the last of these and nothing else — maximally local, zero integration, no commitments protected. That is why it is not the opposite of the heavy regime but its smallest instance, and why it earns its keep *inside* that regime at the failure-interpretation step. When a test run fails, a wrong guess about why still directs the next probe; the guess is discarded when the probe returns, and the surrounding theory absorbs the result. The regimes interleave at that granularity, so an agent doing careful long-horizon work is still generating disposable explanations continuously.

**Adopting one is a commitment at episode scale.** Nothing in the evidence entails "the cache is stale"; the agent resolved a choice the evidence left open, because acting required some choice. Since [commitment, not derivation, creates new ground truth](./commitment-not-derivation-creates-new-ground-truth.md), that resolution is a commitment in the same sense a retained artifact's additions are — the difference is scope of authority, not kind of act. An ad hoc explanation is ground truth for the length of one episode and for nobody else. This is what makes disposal the right default rather than a loss: the commitment's authority expires with the episode it was made for, so keeping the text past that point retains authority that was never earned.

## Commonplace already runs the split without naming its rationale

Three of this KB's standing policies are the same policy, and this note is the rationale they share: admit ad hoc material cheaply at the ephemeral tier, and charge the reach toll only at the boundary where material becomes durable.

- **The log-entry-versus-note quality bar.** A first occurrence goes to `kb/log.md` at essentially no cost; a note is owed a mechanism. That is not two levels of care about the same artifact — it is the ephemeral tier and the retention tier, with the bar sitting on the boundary between them.
- **The workshop layer.** [A functioning knowledge base needs a workshop layer, not just a library](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) argues the tiers from value trajectory: workshop documents consume value and are deleted, library documents accumulate it. This note supplies the epistemic half of the same architecture — the workshop is where explanations are allowed to be ad hoc, and deletion is what keeps that permission from becoming contamination.
- **Progressive constraining.** [Progressive constraining commits only after patterns stabilize](./progressive-constraining-commits-only-after-patterns-stabilize.md) defers codification until repeated runs show which interpretation is stable. That is the same toll on the codification axis: run cheap and unintegrated while feedback is fast, and pay for generality only where something will be reused.

The unifying prediction: a knowledge system whose capture path enforces the retention bar has misapplied the pricing, and will show it as low capture volume rather than as high quality. The bar belongs at promotion, not at admission.

## The LLM failure mode is retention, not generation

An LLM makes ad hoc explanation nearly free to generate. That inverts which side of the boundary needs guarding. The scarce, expensive thing is no longer producing a plausible account of why something happened — it is deciding which accounts are allowed to persist, and the volume arriving at that decision has gone up by orders of magnitude.

The specific hazard is that a fluent ad hoc explanation reads like a reaching one. Both are well-formed prose with a stated mechanism and confident causal language; the properties that distinguish them — whether varying a load-bearing premise constrains the conclusion, whether the account says where it fails, whether it has been checked against anything outside the case that produced it — are invisible on the surface. Fluency is evidence of neither, and a generator optimized for plausible continuation produces the surface without the substance by default.

So the promotion boundary needs a discriminator that fluency cannot satisfy, and the KB's [explanatory-reach](./first-principles-reasoning-selects-for-explanatory-reach-over.md) term already supplies one: a reaching explanation is hard to vary, so changing a premise must force a predictable change in the conclusion, and the note must name a specific way it could be wrong. Those tests are answerable only by inspecting the argument's structure, which is why they survive contact with fluent text. The operational rule at the boundary is that fluency does not count as reach, and the reviewer's felt sense that a passage "reads well" is exactly the signal to disregard.

Cheap regeneration strengthens the case for discarding rather than retaining. Since [LLM recompute cost inverts the store-versus-recompute default](./llm-recompute-cost-inverts-the-store-vs-recompute-default.md), a low-reach explanation that can be regenerated on demand at negligible cost has almost no retention value to weigh against its contamination risk — the asymmetry that made "write it down in case we need it" a good default no longer holds for this class of material.

## Scope

- This is a claim about explanation-handling policy in agent-operated knowledge bases and comparable factory-like systems, where the retained set is a shared input to later work. It is not general epistemology and says nothing about when a person should reason carefully.
- The three conditions are the claim's boundary, not hedges. Under delayed feedback, reuse, or high coherence demands the regime claim flips and ad hoc explanation stops being rational — that is the same claim, not an exception to it.
- The interleaving in the first bridge means the regimes are not a property of a *task*. A long-horizon retention-regime task contains many fast-feedback episodes, and misreading the note as "careful work bans guessing" inverts it.
- What would refute it: a knowledge base that reach-gates capture itself, with no ephemeral tier, and sustains capture velocity and quality — this would show the toll is affordable at admission and the tier split unnecessary. Or a corpus of retained ad hoc explanations that later work builds on without the error propagating, which would break the contamination mechanism the retention-side pricing depends on.
- The claim asserts universally: one clear case of an ad hoc explanation that is irrational despite all three conditions holding, or rational despite one clearly failing, refutes it.

## Open Questions

- The conditions are stated as thresholds but are plainly continuous. What the intermediate region looks like — feedback that takes an hour, an explanation two consumers might reuse — is unresolved, and a system needing a decision there gets no guidance from this note.
- Whether a third tier is warranted between workshop and library for explanations that are reused a few times within one project but never generalize, or whether that is exactly what the workshop already is.

---

Relevant Notes:

- [discovery lifecycle](./definitions/discovery-lifecycle.md) — defined-in: names the derive/test/integrate phases whose cost this note prices against the fast-feedback regime
- [A functioning knowledge base needs a workshop layer, not just a library](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — extends: works the two-tier split out as an architecture, where this note supplies why the tiers are priced differently
- [Progressive constraining commits only after patterns stabilize](./progressive-constraining-commits-only-after-patterns-stabilize.md) — mechanism: shows the same deferral policy operating on the codification axis, committing only where a pattern will be reused
- [First-principles reasoning selects for explanatory-reach over adaptive fit](./first-principles-reasoning-selects-for-explanatory-reach-over.md) — grounds: supplies the premise-variation and criticizability tests that fluent prose cannot fake at the promotion boundary
- [LLM recompute cost inverts the store-vs-recompute default](./llm-recompute-cost-inverts-the-store-vs-recompute-default.md) — grounds: establishes that cheap regeneration removes the retention value that would offset a low-reach explanation's contamination risk
- [Commitment, not derivation, creates new ground truth](./commitment-not-derivation-creates-new-ground-truth.md) — grounds: supplies the commitment/derivation boundary that makes adopting an ad hoc explanation an episode-scoped commitment
