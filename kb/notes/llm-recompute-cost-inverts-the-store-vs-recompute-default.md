---
description: "For model-facing derived values, costly model-side recomputation shifts cache economics toward checked materialization, but persistence pays only when its total expected cost beats the alternatives and the copy substitutes for work"
type: kb/types/note.md
traits: [title-as-claim]
tags: [computational-model, context-engineering]
---

# LLM recompute cost shifts the store-vs-recompute balance

Ordinary software usually avoids storing values it can derive cheaply. Recomputing from a single source of truth avoids a standing consistency liability: a stored copy can go stale, diverge from its source, or force each source change to maintain two surfaces. Persisting the value therefore needs enough workload pressure to repay that liability.

For a value consumed by a model, however, model-side derivation can be unusually expensive. It may require loading files, searching, selecting tools, or reasoning unreliably. These operations consume bounded context, add latency, and can fail. A checked value that the model can read directly may therefore be worth materializing, even when ordinary code could derive it cheaply.

Expensive model-side derivation does not by itself justify persistence. Code may instead derive the narrow answer on demand and return only that answer to the model. The relevant comparison has three paths: model-side derivation, external on-demand derivation, and persisted checked materialization. For a stated validity window, compare their total expected costs, including creation, expected reads, source changes, validation and invalidation, retrieval, context use, and failure recovery. [Opposed recompute factors do not decide documentation segmentation](./human-recompute-is-dear-and-rare-agent-recompute-is-cheap-and-constant.md) supplies the general cache ledger. The LLM-specific change is that model-side derivation can make the recomputation term much larger.

## Checked materialization needs a deterministic checking path

The economic case explains why a copy may earn its cost. It does not make the copy safe. When a live source can regenerate the value, [a derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md). A trusted copy needs a machine-locatable boundary, an explicit binding to its source and derivation, deterministic comparison semantics, and enforcement before the model consumes it. If validation fails, the system must withhold the copy from trusted use and fall back to recomputation.

Checkability does not require a fully symbolic payload. For example, a deterministic generator can reproduce a natural-language paragraph byte for byte inside a delimited region bound to its source. The payload remains natural language, while its envelope and validation path are symbolic. The retained artifact therefore has mixed [representational form](./definitions/representational-form.md). Fully symbolic content is one implementation, not a consequence of checkability alone.

The economic and safety constraints remain distinct. Materialization pulls repeated derivation out of the model's bounded call. Validation keeps the resulting cache subordinate to the live source and prevents it from becoming a second authority.

## An instance, a broader pattern, and a non-instance

- **Instance — a `mark` on a tag README.** A scoped file sweep can recover the answer that `complete` or `covered_by` materializes for an agent to read. A validator re-derives the answer and rejects a false mark; the [`tag-readme` type spec](../types/tag-readme.md) defines the contract.
- **Broader pattern — [frontloading spares execution context](./frontloading-spares-execution-context.md).** Frontloading precomputes or generates parts of a call whose inputs are already known, so the call reads an answer instead of doing the work. The inserted material need not be a copy of a derived value, while this note concerns the narrower store-versus-recompute choice.
- **Non-instance — a content-hash anchor.** A content-hash anchor records an unrecoverable past state so code can detect later divergence. Its value lies in preserving that historical record, not in caching the answer to a recoverable current query for a model reader.

## Decision boundaries

**The materialized answer must replace work, not merely precede it.** A model may read an answer and then inspect the source or rerun the derivation because the answer is insufficient or untrusted for the task. In that case, materialization adds cost instead of removing it. [An insufficient summary precedes the source rather than replacing it](./an-insufficient-summary-precedes-the-source-rather-than-replacing.md) develops this substitution condition.

**Selective layers must also satisfy an addressability condition.** If a summary or routing layer is read selectively to reduce source reads, [its smallest addressable unit must be finer than the source's](./addressability-grain-not-compression-ratio-decides-whether-a.md). This condition governs savings in raw read volume, not materialization in general. A same-grain value can still pay by avoiding discovery or unreliable reasoning, while a finer-grained value can still lose once maintenance cost and low reuse are counted.

**The consumer boundary matters.** When code consumes the derived value, the ordinary software presumption applies. If code derives one boolean on demand and returns it to the model, that is external on-demand derivation rather than model-side recomputation. Its latency and orchestration costs still belong in the comparison.

## Open Questions

- What is the smallest general mechanism for a machine-locatable, source-bound materialized region inside natural-language instruction text, so a validator can re-derive it before trusted consumption?
- Are any derived values worth materializing for a model reader even when they are not cheaply re-derivable? If so, what managed-staleness rule can make them trustworthy when mechanical re-derivation before consumption is unavailable?
