# A toy model of archive readability

Goal: make "how big an archive can a bounded-context system read?" precise enough to reason about.

This is a workshop note, so the model is deliberately narrow. The point is not realism; the point is to isolate the first-order constraints from the [bounded-context orchestration model](../../notes/bounded-context-orchestration-model.md).

## The task class

Fix one query `q`.

The system's job is:

1. inspect an archive of `N` source documents
2. decide which documents matter for `q`
3. synthesize the relevant information into a final answer

We are not modeling open-ended discovery, changing goals, or interactive clarification. This is one query against a static archive.

## The archive

Each source document has:

- a **pointer** of size `p`
- a **body** of size `s`

The pointer is a short description the system can read before deciding whether to open the full source. The body is the actual content.

For the simplest deterministic version:

- all pointers have the same size `p`
- all bodies have the same size `s`
- pointers are perfect: from the pointer alone, the system can tell whether the document is relevant to `q`

This is obviously unrealistic. It is also the cleanest place to start.

## The bounded call budget

Each LLM call has effective budget `M`.

So in one call the system can read at most:

- `floor(M / p)` pointers, or
- `floor(M / s)` full documents

or some mixture whose total effective cost stays below `M`.

The scheduler can keep arbitrary symbolic state in `K`, so anything already read can be stored outside the prompt and does not need to be re-read unless the scheduler chooses to reload it.

## Compression

When the system opens a relevant source, it compresses it into a task-shaped summary of size `a * s`, where `0 < a <= 1`.

`a` is the compression efficiency parameter:

- `a = 1` means no compression
- small `a` means strong compression

For now assume compression is perfect: the summary preserves everything the final synthesis needs from that source.

That assumption is the whole game. We will relax it later.

## Immediate consequences

### 1. Archive size is not bounded by `M`

Because `K` is unbounded symbolic state, the archive can be arbitrarily large in principle. The system can scan it in many bounded calls.

So the right question is not:

> how much archive fits in the prompt?

but:

> how much archive can be navigated and compressed into reusable artifacts fast enough?

### 2. Pointer reading is the first bottleneck

Before the system can decide whether to open a source, it must usually read its pointer.

If pointers are flat, scanning the archive requires about:

`ceil(N * p / M)`

pointer-reading calls.

So even before synthesis, there is a linear "pointer tax" in archive size.

This gives the first simple result:

> In the flat-pointer model, archive readability scales linearly with pointer cost.

If `p` is large, the system spends its budget deciding what to read rather than reading.

### 3. Compression determines whether synthesis can stay bounded

Suppose `R` documents are relevant.

After reading and compressing them, the system holds `R` summaries of size `a * s`.

If all summaries must be synthesized in one final call, then we need:

`R * a * s <= M`

If that does not hold, the system must synthesize hierarchically.

Let:

`b = floor(M / (a * s))`

Then `b` is the maximum fan-in of one synthesis call over summaries.

If `b >= 2`, the system can build a summary tree and reduce arbitrarily many summaries in principle.

This gives the second simple result:

> Flat archive scanning is limited by pointer tax; unbounded synthesis is possible only if compression yields bounded-size sufficient summaries.

### 4. The true limit is sufficiency, not size

This toy model assumes summaries are perfect. Under that assumption, arbitrary archive size is possible whenever:

- pointers let the scheduler find the relevant sources
- the system can compress each relevant source into a bounded summary
- the summaries can be recursively combined without losing what the final answer needs

So the model shifts the question from raw size to existence of sufficient statistics.

The deep constraint is not:

> Is the archive too big?

It is:

> Does this query admit bounded intermediate representations?

## Small propositions

### Proposition 1: flat-pointer readability

In the deterministic flat-pointer model, the number of calls needed just to inspect the archive is:

`Theta(N * p / M)`

So archive access is linear in archive size unless the pointer layer itself becomes hierarchical.

### Proposition 2: synthesis requires compressibility

If a query requires exact joint access to all relevant bodies and no bounded sufficient summary exists, then no amount of orchestration removes the final-context bottleneck.

In other words:

- unbounded archive traversal is possible
- unbounded exact joint reasoning is not

unless the task decomposes.

### Proposition 3: pointer tax and compression ratio are the two first-order parameters

In this simplest model, archive readability is governed first by:

- `p`, the cost of deciding what to open
- `a`, the cost of carrying forward what was learned

Everything else is a refinement of those two pressures.

## Why this model is useful

It is simple enough to make one claim sharp:

> In a bounded-context orchestration system, archive size is not the primitive bottleneck. Pointer tax and compression sufficiency are.

That is already better than asking whether a model has a 200k or 2M token window. The window only gives `M`. It says nothing about:

- how expensive the pointers are
- how good the routing is
- whether the query admits compact intermediate artifacts

## Next relaxations

The obvious next steps are:

1. **Noisy pointers**

Pointers are not perfect. Let pointer quality determine precision/recall of opening decisions. Then archive readability depends on false opens and false skips, not just pointer cost.

2. **Lossy compression**

Summaries are not perfect. Let compression preserve task-relevant information only with fidelity `f(a)`. Then stronger compression helps fit the budget but hurts answer quality.

3. **Pointer hierarchies**

Add cluster pointers above document pointers. This makes navigation logarithmic in depth rather than linear in raw document count when the hierarchy is good.

4. **Variable source sizes**

Real archives are heterogeneous. Some sources are cheap to classify and expensive to read; others are the reverse.

5. **Query classes**

Different queries have different sufficient statistics. Counting claims, finding one citation, reconciling contradictions, and extracting a workflow all have different compressibility.

## The likely direction

The cleanest next model is probably:

- two-level pointer hierarchy
- noisy pointer quality
- lossy compression

That would already let us ask a nontrivial question:

> for a fixed bounded-call budget, what archive size remains navigable at target answer quality?

But the point of this first toy model is narrower. It gets one thing on the table:

> a bounded-context system does not "read an archive" directly. It pays pointer tax to decide what to open, then pays compression cost to carry results forward.

Those are the first two costs to model.

---

Related notes:

- [how a system built around prompt limitations would look](./how-a-system-built-around-prompt-limitations-would-look.md)
- [bounded-context orchestration model](../../notes/bounded-context-orchestration-model.md)
- [context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md)
