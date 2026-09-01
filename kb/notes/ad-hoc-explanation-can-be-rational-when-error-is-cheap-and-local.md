---
description: "Explains why a disposable local guess can rationally select the next probe when error is cheap and contained, while retained explanations need reach checks"
type: kb/types/note.md
traits: [title-as-claim, has-comparison, synthesis]
tags: [learning-theory, discovery, kb-maintenance]
---

# Ad hoc explanation can be rational when error is cheap and local

## Which sense of "ad hoc" this note uses

Two senses travel under the same phrase, and conflating them makes the claim below look like a defence of bad epistemics.

The **narrow** sense is the methodological one associated with Popper: an ad hoc modification is a content-reducing rescue that saves a theory from a refutation by removing what the theory forbade. That move is bad in both regimes described here, for the same reason in each — it buys survival by destroying the theory's testable content — and this note sets it aside entirely. Nothing below licenses it.

The **broad** sense is the everyday one, and it is this note's subject. An **ad hoc explanation** is a local, unintegrated account produced at the point of need, consumed to pick the next action, and discarded. It is not checked against the rest of what the agent believes, it is not written down for anyone else, and it forbids nothing beyond the case in front of it. "The build probably failed because the cache is stale" is an ad hoc explanation: it is a guess about a mechanism, it selects the next command, and after the rebuild nobody keeps it.

## The cheap-and-local regime

A disposable ad hoc explanation can be a rational way to select the next probe when three conditions jointly keep the cost of error low:

1. **Feedback is fast and cheap.** Acting on the guess returns a verdict quickly, and a wrong guess costs about one iteration.
2. **Nothing later reuses it.** The explanation is consumed by the action it selects and does not become an input to a further decision.
3. **Coherence demands are low.** Being wrong does not silently damage commitments made elsewhere, because nothing elsewhere depends on this account being true.

The first condition makes correction cheap. The other two keep the error local. Together they let iteration substitute for some pre-action analysis: acting on the guess can test whether the selected probe helps sooner than fully integrating the explanation would. The resulting feedback evaluates the probe, not necessarily the guessed mechanism. A successful rebuild after clearing a cache does not prove that the cache caused the failure.

These conditions describe a sufficient regime, not a necessary-and-sufficient classification. As feedback slows, reuse grows, or consequences reach other commitments, the expected cost of a weak explanation rises. Up-front derivation, testing, and integration then become worth more. The relevant choice is the cheaper error-control policy for the episode, not an automatic switch triggered by crossing one unnamed threshold.

## Reach machinery is priced for errors that can propagate

The heavy phases of the [discovery lifecycle](./definitions/discovery-lifecycle.md) — derive consequences, test against cases, integrate with prior claims — are the machinery that produces explanations with reach. That machinery is expensive on purpose, and its price buys exactly what the fast-feedback regime does not need: an account that survives contact with cases nobody has run yet, that stays true when a later consumer imports it, and that has been reconciled with what the system already holds.

The two columns below are endpoints of a cost spectrum, not an exhaustive partition. Each method is priced for a different error path:

| | Fast-feedback regime | Retention regime |
|---|---|---|
| Feedback latency | one iteration | delayed, sometimes indefinitely |
| Reuse | none; consumed by one action | artifact is a premise for later work |
| Coherence demand | low; nothing depends on it | high; a web of prior commitments |
| Economical default | guess, act, observe | derive, test, integrate |
| Wrong-way failure | over-ceremony | contamination |

Using full reach machinery for a disposable probe can become **over-ceremony** when the analysis costs more than the error it prevents. Allowing an ad hoc explanation to enter the retained set without review creates **contamination**: later work can build on an unintegrated local guess without seeing the case that produced it. Contamination is the failure the quality bar exists to catch.

## Two bridges to what the KB already holds

**An ad hoc explanation performs one local search-control function that held theory also performs.** Since [holding a program theory means sustaining coherent search under delayed feedback](./program-theory-sustains-search-under-delayed-feedback.md), a held theory narrows candidates, interprets failures, and says when to backtrack. An ad hoc explanation can direct the next probe without supplying the integration or persistence needed for delayed feedback. When the probe returns, the guess can be discarded while the surrounding theory absorbs the result. Careful long-horizon work can therefore contain many cheap-and-local episodes without treating their disposable explanations as held theory.

**Using a guess as a probe premise is not yet retained commitment.** Nothing in the evidence entails "the cache is stale," but selecting a probe does not make the explanation ground truth. [Commitment, not derivation, creates new ground truth](./commitment-not-derivation-creates-new-ground-truth.md) defines commitment by fixing an addition in a retained artifact. A discarded explanation never crosses that boundary. If a workflow promotes the explanation into reusable machinery, that promotion is the commitment and must earn the review appropriate to retention.

## Commonplace places reach checks at the reuse boundary

Three of this KB's standing policies fit the same pricing rule: capture observations and provisional reasoning cheaply, but charge the reach toll before material becomes a reusable premise.

- **The log-entry-versus-note quality bar.** A first occurrence goes to `kb/log.md` at low cost; a note is owed a mechanism. The log retains the occurrence without granting a local explanation the status of reusable theory.
- **The workshop layer.** [A functioning knowledge base needs a workshop layer, not just a library](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) distinguishes in-flight documents whose value will be consumed from library artifacts whose value should accumulate. A workshop can carry provisional explanations during an investigation without promoting them into the library.
- **Progressive constraining.** [Progressive constraining commits only after patterns stabilize](./progressive-constraining-commits-only-after-patterns-stabilize.md) defers codification until repeated runs show which interpretation is stable. That is the same toll on the codification axis: run cheap and unintegrated while feedback is fast, and pay for generality only where something will be reused.

This model predicts that applying the library's reach bar to initial capture will suppress capture as well as reject weak material. The bar belongs at promotion into the reusable set; capture still needs enough structure to preserve what was observed.

## The LLM failure mode is retention, not generation

An LLM makes ad hoc explanation nearly free to generate. That inverts which side of the boundary needs guarding. The scarce, expensive thing is no longer producing a plausible account of why something happened — it is deciding which accounts are allowed to persist, and the volume arriving at that decision has gone up by orders of magnitude.

The specific hazard is that a fluent ad hoc explanation reads like a reaching one. Both are well-formed prose with a stated mechanism and confident causal language; the properties that distinguish them — whether varying a load-bearing premise constrains the conclusion, whether the account says where it fails, whether it has been checked against anything outside the case that produced it — are invisible on the surface. Fluency is evidence of neither, and a generator optimized for plausible continuation produces the surface without the substance by default.

So the promotion boundary needs a discriminator that fluency cannot satisfy, and the KB's [explanatory-reach](./first-principles-reasoning-selects-for-explanatory-reach-over.md) term already supplies one: a reaching explanation is hard to vary, so changing a premise must force a predictable change in the conclusion, and the note must name a specific way it could be wrong. Those tests are answerable only by inspecting the argument's structure, which is why they survive contact with fluent text. The operational rule at the boundary is that fluency does not count as reach, and the reviewer's felt sense that a passage "reads well" is exactly the signal to disregard.

Cheap regeneration strengthens the case for discarding rather than retaining. Since [LLM recompute cost inverts the store-versus-recompute default](./llm-recompute-cost-inverts-the-store-vs-recompute-default.md), a low-reach explanation that can be regenerated on demand at negligible cost has almost no retention value to weigh against its contamination risk — the asymmetry that made "write it down in case we need it" a good default no longer holds for this class of material.

## Scope

- This is a claim about explanation-handling policy in agent-operated knowledge bases and comparable factory-like systems, where the retained set is a shared input to later work. It is not general epistemology and says nothing about when a person should reason carefully.
- This is a possibility claim and cost model, not a claim that every guess satisfying a checklist is rational. The action must remain reversible enough that fast feedback can correct it.
- The conditions are continuous. As feedback slows or error propagation grows, this note predicts increasing value from pre-action analysis; it does not supply universal thresholds.
- The interleaving in the first bridge means the regimes are not properties of whole tasks. A long-horizon task can contain many cheap-and-local probes.
- The mechanism would lose support if cheap, reversible probes do not reduce total decision cost relative to pre-action integration in the stated regime, or if retaining unreviewed local explanations does not create the predicted downstream error risk.

## Open Questions

- How should a system estimate the intermediate region — feedback that takes an hour, an explanation two consumers might reuse, or a probe whose side effects are only partly reversible?
- Whether a third tier is warranted between workshop and library for explanations that are reused a few times within one project but never generalize, or whether that is exactly what the workshop already is.

---

Relevant Notes:

- [discovery lifecycle](./definitions/discovery-lifecycle.md) — defined-in: names the derive/test/integrate phases whose cost this note prices against the fast-feedback regime
- [A functioning knowledge base needs a workshop layer, not just a library](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — extends: works the two-tier split out as an architecture, where this note supplies why the tiers are priced differently
- [Progressive constraining commits only after patterns stabilize](./progressive-constraining-commits-only-after-patterns-stabilize.md) — mechanism: shows the same deferral policy operating on the codification axis, committing only where a pattern will be reused
- [First-principles reasoning selects for explanatory-reach over adaptive fit](./first-principles-reasoning-selects-for-explanatory-reach-over.md) — grounds: supplies the premise-variation and criticizability tests that fluent prose cannot fake at the promotion boundary
- [LLM recompute cost inverts the store-vs-recompute default](./llm-recompute-cost-inverts-the-store-vs-recompute-default.md) — grounds: establishes that cheap regeneration removes the retention value that would offset a low-reach explanation's contamination risk
- [Commitment, not derivation, creates new ground truth](./commitment-not-derivation-creates-new-ground-truth.md) — contrasts: fixes new ground truth only when an addition enters a retained artifact, the boundary a discarded probe premise does not cross
