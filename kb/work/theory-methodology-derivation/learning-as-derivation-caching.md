# Learning framing: promotion is caching derivations

How the two-layer structure is a form of learning, and what kind.

## Amortization, not acquisition

In the [two-layer structure](../../notes/theory-and-methodology-form-a-two-layer-execution-system.md), the theory can already handle every case — nothing new becomes *derivable* when a corner case is promoted into the methodology. What changes is the cost profile: an expensive re-derivation becomes a cheap lookup. Learning here is **amortization**. This fits [deploy-time learning](../../notes/deploy-time-learning-is-the-missing-middle.md) (adaptation through durable inspectable artifacts) but names a mechanism the current operation decomposition (accumulation, constraining, distillation, discovery) doesn't isolate: the artifact update adds no reach and narrows no interpretation — it caches a computation.

It also fits [learning is not only about generality](../../notes/learning-is-not-only-about-generality.md) exactly: promotion improves reliability, speed, and cost on the covered distribution while generality is held by the other layer.

## The cognitive-architecture analogue: proceduralization

ACT-R's **production compilation** and SOAR's **chunking**: declarative knowledge (the theory) is slow to apply because each use requires interpretive reasoning over it; when the same derivation recurs, the architecture compiles it into a procedural rule that fires directly. The declarative layer is retained for novel cases. This is the source passage's pattern almost verbatim — including the testable promotion criterion: in ACT-R terms, learning has occurred when the case is resolved by rule-firing without retrieving the declarative source, which matches "the agent resolves it from the methodology alone."

ML has a name for the same move: **amortized inference** — replace per-instance expensive inference with a cheap learned function, and fall back to full inference where the amortization gap is large.

## Open questions

- Is "caching derivations" a missing fifth operation in the learning-theory decomposition, or just distillation run continuously against a use distribution? (If the [vocabulary thread](./derivation-selection-vocabulary.md) lands, the answer is probably: it is *derivation*, run incrementally, with the use distribution doing the selection.)
- The proceduralization literature has a known failure mode — compiled rules persist after the declarative knowledge that justified them is revised. That is the mark-staleness trap at the methodology scale. Does the KB need an explicit "recompiled-since" discipline for derived methodology, or does review freshness already cover it?
- Does the analogue earn a citation-level borrowing (a source ingest for ACT-R/SOAR chunking) or is a one-line mention in the structure note enough?

---

Working links:

- [deploy-time learning is the missing middle](../../notes/deploy-time-learning-is-the-missing-middle.md) — grounds: the timescale and artifact frame this learning happens in
- [learning is not only about generality](../../notes/learning-is-not-only-about-generality.md) — grounds: capacity decomposes into generality vs reliability+speed+cost; promotion moves only the second bundle
- [readable artifact loop is the tractable unit for continual learning](../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) — see-also: the loop promotion runs inside
