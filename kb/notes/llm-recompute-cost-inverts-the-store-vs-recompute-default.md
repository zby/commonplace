---
description: "For an LLM consumer, in-context recompute is the expensive step, so materializing a derived value to be read pays off exactly where storing it would be premature denormalization in code"
type: kb/types/note.md
traits: [title-as-claim]
tags: [computational-model, context-engineering]
status: seedling
---

# LLM recompute cost inverts the store-vs-recompute default

Ordinary software defaults against storing a value it can derive. Normalize the schema, keep one source of truth, recompute on read: compute is cheap and abundant, whereas a stored derived copy is a standing liability — it can go stale, it can disagree with its source, and every writer now has two places to keep in sync. Denormalization is the exception you reach for only under measured pressure, and reaching for it early is a named smell. The whole bias runs one way: prefer recompute, distrust the stored copy.

For an LLM consumer the cost profile flips, because the recompute step is the expensive one. "Recompute in context" is not a cheap arithmetic op; it is a tool call, a file load, a search, or a stretch of unreliable reasoning — each spending the scarce resource and each able to fail. This inverts the default: [context is the central scarce resource in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md), so the thing ordinary software treats as free is here the dominant cost, and the thing it treats as a liability — a materialized derived value the consumer just reads — becomes the cheap path. Materializing a derived value so the model reads it instead of recomputing it is worthwhile *exactly* where, judged as code, it would be premature denormalization: a derived value, cheap to recompute, stored anyway. The judgment reverses because the consumer changed, an instance of the general point that [human–LLM differences are load-bearing for knowledge-system design](./human-llm-differences-are-load-bearing-for-knowledge-system-design.md) — here the difference is the relative price of storage versus recompute.

## The safety composition pushes materialization into symbolic form

The value theory alone says only *materialize it*. It does not say what the materialized copy must look like. That second constraint comes from composing this note with its safety half: once the value is recomputable from a live source, [a derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md). A materialized-and-trusted copy is one missed edit from silent, unbounded wrongness; a materialized-and-checked copy costs at most a bounded recomputation when dropped.

Requiring the check narrows *how* the value may be materialized. A validator can only re-derive and compare when the copy sits in a machine-parseable region that names its source — that is, when the materialized value is in symbolic rather than prose [representational form](./definitions/representational-form.md). So the two halves divide cleanly: the value theory says materialize the derived value, and the safety constraint says materialize it in a form code can validate. Value pulls a computation out of the model's context; safety pushes the result into a symbolic slot with a derivation rule behind it. Neither half is sufficient alone — value without safety gives you the hand-maintained stale copy, safety without value gives you a validator guarding a copy no one needed.

## Instances and one non-instance

This is the general value theory that two existing patterns instantiate:

- **The `mark` concept** — `complete`/`covered_by` on tag-READMEs — is a validated symbolic cache consumed by agents. The membership query is recomputable but costs a scoped sweep on every read; the mark materializes the answer so the agent reads it, and a validator re-derives it so it can't silently rot (the mark contract is in the [`tag-readme` type spec](../types/tag-readme.md)). Value plus safety, both halves present.
- **[Frontloading spares execution context](./frontloading-spares-execution-context.md)** is the sibling application at the level of a whole instruction: precompute — or generate — the parts of a consuming call's context whose inputs are already known, and insert the result so the call reads instead of works. It is broader than this note along one axis (its inserted parts need not be a *recomputed* derived value; they can be generated content), and this note is sharper along another (it isolates the store-vs-recompute inversion that makes the insert pay).

A **content-hash anchor** looks superficially similar and is *not* an instance. It records a past state — a snapshot the current ground truth cannot regenerate, since its entire job is to detect divergence from that past — so it is load-bearing, not an accelerator over a recoverable query. And it is consumed by code, not read by the model to spare a recompute. It fails both halves at once: nothing about it trades the model's expensive recompute for a cheap read, and its value is the recorded past, not a re-derivable present. The pattern here is specifically *a value the model would otherwise recompute, materialized for the model to read, checked because it is re-derivable* — not every stored derived byte.

## Scope

The inversion is about the *consumer's* recompute price, not about storage being free. A materialized value still costs to keep checked and still occupies context when read; the claim is only that the balance that makes recompute the default for a code reader makes materialization the default for a model reader. Where the derived value is consumed by code rather than read by the model, the ordinary software default applies unchanged — the flip rides entirely on who pays for the recompute.

## Open Questions

- What is the smallest general mechanism for a checked, machine-locatable materialized region inside prose instruction text, so the value half can be taken without hand-rolling a validator per case?
- Are there derived values worth materializing for a model reader that are *not* cheaply re-derivable, where the safety half must fall back to managed staleness rather than a Level A check?

---

Relevant Notes:

- [Context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — grounds: the premise that in-context recompute spends the binding scarce resource, which is what inverts the default
- [A derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — extends: the safety half that composes with this value half and forces the materialized copy into a checkable form
- [Frontloading spares execution context](./frontloading-spares-execution-context.md) — extends: the sibling application at instruction scale — precompute-or-generate the known parts of a consuming call's context, of which materializing a recomputed value is one case
- [Human–LLM differences are load-bearing for knowledge system design](./human-llm-differences-are-load-bearing-for-knowledge-system-design.md) — exemplifies: the store-vs-recompute inversion is one concrete human–LLM cost-profile difference that changes a design default
- [Representational form](./definitions/representational-form.md) — defined-in: the safety constraint pushes materialization from prose into symbolic form, the term this note uses for the machine-parseable target
