---
description: "When audiences trade per-reconstruction savings against recurrence, neither factor alone determines cache value; among feasible alternatives, segmentation separately depends on whether specialization repays every cost introduced by the split"
type: kb/types/note.md
traits: [title-as-claim, has-comparison]
tags: [document-system, context-engineering]
---

# Opposed recompute factors do not decide documentation segmentation

Documentation that describes a system readers could reconstruct from source acts as a **cache**. The source remains the ground truth; the document materializes an answer and saves some reconstruction work. One useful decision model estimates the cache's operating value over a chosen horizon:

> net cache value ≈ (net saving per equivalent reconstruction) × (reconstructions avoided) − (maintenance)

An equivalent reconstruction produces the same output at the same reliability threshold. The net saving is the cost of reaching that threshold from source minus the cost of reaching it through the document. Both costs should include access, transformation, verification, and failure recovery. Evaluate the savings, number of avoided reconstructions, and maintenance over the same horizon and in a currency the project actually uses. This model is a decision aid, not an exhaustive account of value.

Whether to maintain a cache and whether to split it by audience are related but distinct decisions. The first asks whether the cache has positive net value. The second asks whether an audience-specific arrangement improves on the best shared arrangement. Hard authorization, safety, regulatory, access, and contractual constraints filter candidate architectures before either economic comparison. Among the feasible alternatives that remain, a split pays only when **specialization value**—the marginal benefit of tailoring content to an audience—exceeds every incremental system cost introduced by the split.

Suppose both benefit factors are positive and two audiences have crossed profiles: one saves more per reconstruction but avoids fewer reconstructions, while the other saves less each time but avoids more. **Those directions alone determine neither the product nor the net cache value after maintenance.**

## Crossed factors leave cache value unordered

A conditional human-agent regime illustrates the inversion. A stable human maintainer may save more by consulting documentation than by reconstructing a scattered system model, yet retain that model across later encounters. A stateless agent may save less on each encounter because it can search source quickly, yet repeat the work across many relevant fresh sessions. These are project conditions to measure, not fixed properties of humans and agents.

When measurements establish this illustrative regime, the human profile is high saving × low recurrence, while the agent profile is low saving × high recurrence. The products remain unordered without magnitudes. Either audience can have the larger avoided-reconstruction benefit, and audience-specific maintenance can change the net ordering again.

## Single-property arguments omit an opposing factor

Two common arguments each consider only one factor:

- *Agents are stateless, so they need more written documentation than humans.* Statelessness makes each relevant fresh session a potential repetition. It determines neither how many such sessions occur nor how much work the document would save on each one.
- *Agents read fast and search well, so they need less written documentation than humans.* Fast source access can reduce part of the reconstruction cost. It does not determine the net saving because using the document also incurs access, transformation, verification, and failure-recovery costs.

Each argument identifies a real mechanism but leaves the opposing factor and both magnitudes unmeasured. Neither property alone orders cache value.

## Compare cache values over one horizon

Estimate the following quantities over a common horizon before comparing cache values:

- **Equivalent output and reliability** — the answer or system model each reader must recover, together with the accuracy threshold that makes reconstruction and document consultation comparable.
- **Comparison currency** — wall-clock latency, direct money, opportunity cost, or an explicit, decision-specific conversion among them.
- **Net saving per reconstruction** — the access, transformation, verification, and recovery costs of reconstructing from source, less the corresponding costs of using the document.
- **Human reacquisition** — retention, context switching, source churn, contributor turnover, and the rate at which relevant new readers arrive.
- **Agent recurrence** — relevant fresh-session volume after accounting for long sessions, source or system maps retained across sessions, prompt caches, and other reuse supplied by the surrounding agent runtime.
- **Maintenance** — the cost of keeping each candidate artifact accurate over the same horizon, including the cost of finding drift.

Repository size and contributor history are proxies for only some of these quantities, not measurements of the decision itself. Charge the full ongoing maintenance of a shared cache when assessing whether that artifact pays. If the two readers consume non-substitutable resources and no defensible exchange rate exists, their cache values remain incomparable; the project should not force them into a numerical ranking.

## Segmentation requires specialization value

Even exact audience-specific cache values show only how valuable a particular content arrangement is to each audience. They do not show whether both audiences can use the same content. Two audiences can value a cache equally yet need incompatible explanations or representations. They can value it differently yet use one shared artifact successfully. It is also possible that only one audience justifies maintaining a cache at all.

For optional alternatives, first define the objective and the required output or reliability threshold. The baseline is the best feasible shared arrangement under that objective. Specialization value is the audience-fit benefit of a specialized arrangement relative to that baseline. When a split adds a layer to an otherwise unchanged shared arrangement, it pays only when this benefit exceeds every system-wide cost caused by the split over the same horizon and in a defensible common currency. If the architectures are mutually exclusive rather than nested, compare their total net values instead. If qualitative fit and maintenance are non-substitutable, no scalar comparison is available; another declared constraint or decision rule must decide.

Count drift detection in the split's incremental burden. Low traffic reduces incidental detection opportunities only when uses sometimes compare the layer with source; traffic is neither a detector nor a substitute for managed maintenance. Different access paths also need not create a second claim authority. [Serving multiple consumers does not require one retrieval interface](./agent-memory-requirements/serve-multiple-consumers.md), and [lineage and compiled views can be kept from drifting](./agent-memory-requirements/keep-compiled-views-aligned.md) when one maintained source remains authoritative. The generator and its view rules still incur maintenance even when they do not duplicate the claims.

## Scope

- This framing treats documentation as a cache over a re-readable source. Documentation that records something the source cannot regenerate—such as a decision and its rejected alternatives, a history, or an intent—offers no recomputation to price. [Attempted recovery identifies informational gaps, not provenance or authority](./documentation-generates-the-system-rather-than-describing-it.md): segment such content according to the historical, evidential, or governing role it serves. It becomes load-bearing authority only when a separate causal path puts it into the live change loop.
- The crossed human-agent profile is conditional. Small or legible sources, expensive agent verification, frequent human reacquisition, low agent workload, or durable runtime reuse can remove or reverse either inequality.
- The product result assumes positive factors, equivalent outputs, and savings expressed on a common scale. Without a common scale, audience cache values are incomparable for a more basic reason.

## Open Questions

- Which representative reconstruction tasks, target outputs, and reliability thresholds make human-agent savings comparable?
- What observable failure or use pattern establishes that audience-specific content adds enough fit value to repay its second maintenance surface?

---

Relevant Notes:

- [Information value is observer-relative](./information-value-is-observer-relative.md) — exemplifies: the crossed-factor model is a concrete observer-pair value decomposition
- [LLM recompute cost shifts the store-vs-recompute balance](./llm-recompute-cost-inverts-the-store-vs-recompute-default.md) — grounds: inference, context reconstruction, review, maintenance, and consistency costs jointly determine whether storing an LLM-facing cache pays
- [Design for the first-time human, except on access cost](./design-for-the-first-time-human-except-on-access-cost.md) — extends: consumer-specific materialization can vary access cost without creating a second content authority
- [Promote Only When Future Value Exceeds Maintenance Cost](./agent-memory-requirements/promote-only-when-value-exceeds-cost.md) — exemplifies: a second documentation layer is a durable promotion with review and maintenance obligations
- [ADR 025 — Complete generated indexes are build-time-only artifacts](../reference/adr/025-complete-generated-indexes-are-build-time-only.md) — evidenced-by: one maintained metadata source can supply generated and query-time access paths without making both canonical
