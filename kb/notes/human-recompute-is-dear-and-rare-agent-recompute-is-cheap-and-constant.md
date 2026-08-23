---
description: "When audiences invert on net reconstruction savings and recurrence, neither factor alone orders cache value; segmentation also depends on whether specialization repays a second maintenance surface"
type: kb/types/note.md
traits: [title-as-claim, has-comparison]
tags: [document-system, context-engineering]
---

# Opposed recompute factors do not decide documentation segmentation

Documentation that describes a system a reader could instead reconstruct from source acts as a **cache**. The source remains the ground truth; the document materializes an answer and spares the reader some reconstruction work. Its value can be decomposed as:

> net cache value ≈ (net cost saved per equivalent reconstruction) × (reconstructions avoided) − (maintenance)

An equivalent reconstruction reaches the same output and reliability threshold. The net saving is the cost of reaching that threshold from source minus the cost of reaching it through the document. Both costs include access, transformation, verification, and failure recovery, measured in a currency the project actually uses. The model is a decision aid, not an exhaustive account of value.

Writing a cache and splitting it by audience are related but distinct decisions. Writing the cache asks whether its net value is positive. Splitting it asks whether **specialization value** — the marginal benefit of tailoring a second content layer to one audience — exceeds the incremental maintenance and drift burden.

In the regime considered here, both factors are positive and the audiences have crossed profiles: one saves more per reconstruction but avoids fewer reconstructions, while the other saves less each time but avoids more. **The directions of those differences do not order their cache values.** Their magnitudes are needed even for that narrower comparison, and the resulting cache-value ordering still does not decide whether audience-specific content is worth maintaining.

## A crossed-factor regime leaves cache value unordered

A common human-agent regime illustrates the inversion. A stable human maintainer may save more by consulting documentation instead of reconstructing a scattered system model, but retain that model across later encounters. A stateless agent may save less each time because it can search the source quickly, yet repeat the work across many relevant fresh sessions. These are project conditions to test, not fixed properties of humans and agents.

**Net saving per reconstruction.** Humans read slowly and must hold relationships across files. Agents can search and load source quickly, but search does not guarantee complete discovery, and verification can dominate their cost. The relevant quantity is not source-reading cost alone; it is the difference between reconstruction from source and consultation of the document at the same output threshold. [Access burden and transformation burden are distinct](./access-burden-and-transformation-burden-are-distinct-query-dimensions.md), so repository size alone cannot stand in for either reader's net saving.

**Reconstructions avoided.** Human retention can reduce repetition, while [a fresh agent session starts without a learned system model](./agent-statelessness-makes-routing-architectural-not-learned.md). But statelessness creates another opportunity to save work only when a relevant fresh session occurs. Human context switching, source churn, and reader turnover can raise human reacquisition; low agent workload, long-running sessions, durable repository maps, and prompt caches can lower agent recurrence.

When measurement establishes the illustrative regime, its profile is:

| | net saving per reconstruction | reconstructions avoided |
|---|---|---|
| human reader | high | low |
| agent reader | low | high |

High × low competes with low × high. If the human saving is larger but human recurrence is lower, neither product inequality follows from those two facts. The magnitudes can put either audience's avoided-reconstruction benefit ahead; subtracting audience-specific maintenance adds another quantity to measure rather than restoring an ordering.

A small, legible source or expensive agent verification can remove or reverse the saving inequality. Frequent human reacquisition can remove the recurrence inequality. The model still applies, but the table no longer describes that project.

## Single-property arguments drop an opposing factor

Two arguments circulate, and each uses exactly one column:

- *Agents are stateless, so they need more written documentation than humans.* Statelessness supplies recurrence per relevant fresh session. It does not supply the number of such sessions or the saving produced by a document.
- *Agents read fast and search well, so they need less written documentation than humans.* Fast access can lower one reconstruction cost, but it does not price document consultation, transformation, verification, or failure recovery.

Each argument identifies a real mechanism but leaves its opposing factor and both magnitudes unmeasured. Neither property alone orders cache value, much less the marginal value of a separate audience-specific layer.

## Comparing cache values requires measured magnitudes

Estimate at least these quantities before comparing cache values:

- **Equivalent output and reliability** — the answer or system model each reader must recover, plus the accuracy threshold that makes reconstruction and document consultation comparable.
- **Comparison currency** — wall-clock latency, direct money, opportunity cost, or an explicit decision-specific conversion among them.
- **Net saving per reconstruction** — the access, transformation, verification, and recovery costs of reconstructing from source, less the corresponding costs of using the document.
- **Human reacquisition** — retention, context switching, source churn, contributor turnover, and the rate at which relevant new readers arrive.
- **Agent recurrence** — relevant fresh-session volume after accounting for long sessions, durable maps, prompt caches, and other harness-level reuse.
- **Maintenance** — the cost of keeping each candidate artifact accurate, including the cost of finding drift.

Repository size and contributor history are proxies for parts of this list, not measurements of the decision itself. If the two readers consume non-substitutable resources and no defensible exchange rate exists, their cache values remain incomparable; the project should not manufacture a scalar crossover.

An LLM reconstruction can also be expensive relative to a CPU instruction while being cheaper than a human reconstruction in a measured project regime. [LLM recompute cost can therefore invert the software store-versus-recompute default](./llm-recompute-cost-inverts-the-store-vs-recompute-default.md) without establishing either side of the human-agent inequality here. Every cost claim needs its comparison class, output threshold, and currency.

## Cache value and audience fit answer different questions

Even exact audience-specific cache values would answer only whether each audience benefits from avoiding reconstruction. They would not reveal whether both audiences can use the same content. Two audiences can value a cache equally yet need incompatible explanations or representations. They can value it differently yet use one shared artifact successfully, or only the higher-value audience may justify a cache at all.

The split decision therefore needs one more measurement: specialization value relative to the best shared content. A second layer pays only when that marginal audience-fit benefit exceeds its incremental maintenance and drift burden. When specialization gain is unknown, one maintained content source is the safer provisional default because the second correctness surface has a known cost and an unproven benefit. This is a maintenance-preserving default, not a theorem derived from equal products.

Different access paths need not create that second content surface. Multiple consumer-specific views can be generated over one maintained source because [serving multiple consumers does not require one retrieval interface](./agent-memory-requirements/serve-multiple-consumers.md).

## A low-traffic layer gets fewer drift-discovery opportunities

Drift becomes visible when someone or something compares the document with changed source. Read traffic can create opportunities for that comparison, so a low-traffic layer may remain stale longer even though traffic is not itself a detector. A split must price this loss of incidental detection alongside direct maintenance.

If a copy is mechanically re-derivable and machine-comparable, [it must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md). Judgment-dependent prose does not meet that condition; it needs an explicit managed-review cadence instead. Splitting only the access path over one maintained source avoids the second content layer's drift surface.

## Scope

- The framing treats documentation as a cache over a re-readable source. Documentation that records something the source cannot regenerate — a decision and its rejected alternatives, a history, an intent — has no recompute to price, so this argument does not reach it. There the artifact is load-bearing rather than an accelerator, and the segmentation question has to be decided on other grounds.
- The crossed human-agent table is a conditional regime. Small or legible sources, expensive verification, frequent human reacquisition, low agent workload, or durable harness-level reuse can remove or reverse either inequality.
- The crossed-factor result assumes positive factors, equivalent outputs, and savings expressed on a common scale. Under those assumptions, opposite factor orderings do not order the products. Without a common scale, audience cache values are incomparable for a more basic reason.

## Open Questions

- Which representative reconstruction tasks and output thresholds make human-agent savings comparable?
- What observable failure or use pattern establishes that audience-specific content adds enough fit value to repay its second maintenance surface?
- For judgment-dependent low-traffic prose, what review schedule best substitutes for missing incidental source comparisons?

---

Relevant Notes:

- [Information value is observer-relative](./information-value-is-observer-relative.md) — exemplifies: the crossed-factor model is one concrete observer-pair value decomposition
- [For its load-bearing part, documentation generates the system rather than describing it](./documentation-generates-the-system-rather-than-describing-it.md) — grounds: its recovery test separates cache content from documentation whose value cannot be recomputed from source
- [Promote Only When Future Value Exceeds Maintenance Cost](./agent-memory-requirements/promote-only-when-value-exceeds-cost.md) — exemplifies: a second documentation layer is a durable promotion with review and maintenance obligations
