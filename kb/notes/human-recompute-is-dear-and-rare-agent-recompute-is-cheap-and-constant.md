---
description: "Reconstructing a system from its source is expensive but rarely repeated for a human, cheap but repaid every session for an agent; the opposite profiles leave documentation's audience question to magnitudes rather than principle"
type: kb/types/note.md
traits: [title-as-claim, has-comparison]
tags: [document-system, context-engineering]
---

# Human recompute is dear and rare; agent recompute is cheap and constant

Documentation that describes a system a reader could instead read directly is a **cache**. The source is the ground truth; the document is a materialized answer that spares the reader the work of reconstructing it. So the decision to write it, and the decision to write two of it, is a cache-value decision:

> value ≈ (cost of one recompute) × (number of recomputes avoided) − (maintenance)

Segmenting by audience — a human-facing layer and an agent-facing layer over the same subject matter — is justified when the two audiences' values diverge enough that one artifact serves neither well. It is not free: each layer pays its own maintenance term, and the terms do not share.

The claim here is about the two readers' profiles. **Reconstructing a system's shape from its source is expensive for a human but rarely repeated, and cheap for an agent but repaid every session.** The inversion runs in opposite directions on the two terms.

That is what leaves the segmentation question open. Were the readers to invert on cost alone, one of them would plainly need the cache more, and the design question would be settled before any measuring. Two opposed inversions compose into no ordering at all, so which reader benefits more is a question about magnitudes. The value model below is one decomposition, not an exhaustive account of what makes a cache worth keeping — other terms exist, and adding them does not restore an ordering the first two failed to supply.

## The two readers invert on cost and on frequency

**Per-read recompute cost.** For a human, reconstructing a system's shape from its source is expensive: reading is slow in wall-clock terms, and holding the relationships among many files exceeds working memory, so the reconstruction has to be rebuilt in pieces and stitched. For an agent, the same reconstruction is cheap: it reads at machine speed, and it can target the slice it needs by search rather than by reading through. Cheap does not mean free — an agent [pays linearly for every byte it loads](./design-for-the-first-time-human-except-on-access-cost.md), where a human reading the same artifact pays sublinearly — but per unit of understanding recovered, the agent's price is the lower one.

**Number of recomputes avoided.** For a human, one recompute buys a durable mental model. Having reconstructed the architecture once, the reader retains it across encounters, for months or years; the cache is consulted a handful of times before it stops being needed. For an agent, nothing survives the session boundary. Since [each session starts without any learned model of the system](./agent-statelessness-makes-routing-architectural-not-learned.md), the recompute is paid again on every task that needs it, indefinitely.

So the profiles are:

| | per-read recompute cost | recomputes avoided |
|---|---|---|
| human reader | high | low |
| agent reader | low | high |

High × low against low × high. The two products are formed from inverted factors, so their ratio is not determined by the sign of either factor — it depends on the magnitudes, and it can land on either side.

## Consequence: single-property arguments do not decide

Two arguments circulate, and each uses exactly one column:

- *Agents are stateless, so they need more written documentation than humans.* True premise, uses only the frequency column.
- *Agents read fast and search well, so they need less written documentation than humans.* Also a true premise, uses only the cost column.

Both are sound about their factor and both are incomplete, and because they pull in opposite directions, neither wins by default. Any argument that reaches a segmentation conclusion from one consumer property has, structurally, dropped a term that opposes it.

## Consequence: the crossover depends on quantities you can measure

Two quantities move the products, and both are measurable before deciding:

- **Source size per unit of understanding** — how much source a reader must traverse to reconstruct one answer the document would have given. This scales the recompute cost for both readers. A small, legible source pushes the agent's already-cheap recompute toward negligible, which collapses the agent-facing cache's value; a large or scattered one raises the cost for both readers and can justify a cache for each.
- **Reader turnover** — how often a *fresh* human arrives. The human's low recompute count is an artifact of retention by a stable population. Turnover resets it: a stream of first-time human readers converts the human column toward the agent's profile, high cost paid at high frequency, which is the configuration where a human-facing cache is worth the most.

Neither quantity is exotic. Both are the kind of thing a maintainer can estimate from the repository and its contributor history, which is what makes this a decidable question rather than a matter of taste.

## Consequence: near-equal products argue for one artifact

Where the two products are close, the segmentation is a pure loss. One artifact then serves both readers at the cost of one maintenance term; two artifacts serve them slightly better at the cost of two, plus the standing risk that the layers disagree with each other as well as with the source. The default under uncertainty is therefore the single artifact, and the case for splitting has to be made from an estimated gap, not from the observation that the readers differ. That the readers differ is the premise of the question, not an answer to it.

## Consequence: segmentation strips the drift detector from the low-traffic layer

Segmentation carries one cost that is not symmetric between the layers, and it comes from the same factor that motivated the split.

Read traffic is a documentation cache's staleness detector. A reader who consults the document and then touches the source is the event that surfaces disagreement; nothing else routinely compares the two. So detection rate rides on read frequency — the same *n* that sets cache value.

That makes the low-frequency layer doubly disadvantaged. The human-facing layer accrues fewer avoided recomputes *and* generates fewer detection events, and the second effect has no ceiling: it rots silently between reads, and [the process that would notice consults the artifact that drifted](./stale-self-description-conceals-its-own-staleness.md). A rarely-read layer that is nevertheless trusted is precisely the state that [a derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) forbids — a hand-maintained copy of something the source could re-derive, with no check behind it and no traffic to expose it.

Before splitting, then: either the low-traffic layer earns a check, or the split must be worth the standing risk of a false cache. This is a distinct consideration from splitting the *access path* — giving each consumer a materialization with cheap access over a single source of truth leaves one thing to maintain and one thing to check, and does not incur this cost at all.

## Reconciliation: "cheap for an agent" is a comparison, not an absolute

This note says in-context recompute is cheap for an agent. Elsewhere the KB argues that [LLM recompute cost inverts the store-vs-recompute default](./llm-recompute-cost-inverts-the-store-vs-recompute-default.md) precisely because in-context recompute is *expensive*. These do not conflict; they hold the same quantity against different comparison classes.

That note compares an LLM's recompute against a CPU's, inside ordinary software's store-versus-recompute reasoning. Against a machine instruction, a file load or a search or a stretch of model reasoning is enormously expensive — expensive enough to reverse the software default that says recompute rather than store. This note compares an LLM's recompute against a *human's*. Against a person reading and holding a codebase in mind, the same operation is the cheap one.

Both comparisons are load-bearing where they are made, and both are instances of the general point that [human–LLM differences are load-bearing for knowledge-system design](./human-llm-differences-are-load-bearing-for-knowledge-system-design.md). The general lesson is that a recompute cost has no absolute reading: it is a price in someone's currency, and which consumer is expensive depends entirely on who else is in the comparison.

## An existential witness

That the low-cost, high-frequency configuration can actually occur — and can come out against segmentation — is shown by at least one case rather than argued in the abstract. In this repository the Python source is 85 modules totalling about 460 KB, averaging roughly 5 KB each, which puts the per-answer traversal for an agent low. Its descriptive documentation is co-maintained with the code, not maintained on a separate cadence: of the last 120 commits touching `src/`, 72 also touch `kb/reference/`. And its reader-facing surface is small and stable — a root README, a published site home, and a landing file per collection.

Those measurements witness that a repository can land in the region where one artifact set serves both readers. They are not evidence that segmentation is generally unwarranted: a repository with a larger or more scattered source, or with high human turnover, moves the products and can land on the other side. The finding "this repository needs no separate human documentation layer" is local, and it is an instance of the claim above, not the claim.

## Scope

- The framing treats documentation as a cache over a re-readable source. Documentation that records something the source cannot regenerate — a decision and its rejected alternatives, a history, an intent — has no recompute to price, so this argument does not reach it. There the artifact is load-bearing rather than an accelerator, and the segmentation question has to be decided on other grounds.
- The agent's high recompute count is conditional on no cross-session retention. An agent with durable memory of a system moves toward the human's profile on that factor, and the balance has to be recomputed rather than inherited from this note.
- Comparing the two readers' per-read costs requires a common currency — money, wall-clock time, or opportunity cost — and the exchange rate is not fixed. It moves with inference prices and with the value of the human's time. This note asserts the *direction* of each inequality under current conditions, not a stable ratio, and a large enough shift in that rate is a genuine defeater for the cost column.

## Open Questions

- Is there a defensible way to express both readers' recompute costs in one currency, or does the comparison stay ordinal — direction known, magnitude not?
- Can a low-traffic documentation layer be given a cheap mechanical check that substitutes for the drift detection its missing read traffic would have supplied, and if so, does that remove the asymmetry that argues against segmentation?
- Where a source is large enough that both readers want a cache, do they want the *same* cache? The argument here decides whether to split, not what the split would contain.

---

Relevant Notes:

- [Human–LLM differences are load-bearing for knowledge system design](./human-llm-differences-are-load-bearing-for-knowledge-system-design.md) — exemplifies: the cache-value inversion is one concrete human–agent cost-profile difference that changes a design default, alongside that note's dual-audience table
- [LLM recompute cost inverts the store-vs-recompute default](./llm-recompute-cost-inverts-the-store-vs-recompute-default.md) — contrasts: same recompute quantity, opposite verdict, because that note's comparison class is CPU recompute and this note's is human recompute
- [Agent statelessness makes routing architectural, not learned](./agent-statelessness-makes-routing-architectural-not-learned.md) — grounds: the premise that an agent's recompute is paid every session, which supplies the frequency column
- [Stale self-description conceals its own staleness](./stale-self-description-conceals-its-own-staleness.md) — mechanism: why a low-traffic layer's drift is not merely undetected but self-concealing
- [A derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — grounds: the prohibition that a rarely-read, unchecked documentation layer violates
- [Design for the first-time human, except on access cost](./design-for-the-first-time-human-except-on-access-cost.md) — contrasts: that note splits the *access path* behind a single source of truth; this note asks whether the *content* should be split at all, which is where the second maintenance term appears
- [Context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — grounds: what the agent spends on a recompute, and why its cost is not zero even when it is lower than the human's
