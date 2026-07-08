# Adjudication as a separate, labeled, downstream layer

Layer: assessment.

If a verdict is wanted (Rootclaim-style Bayesian aggregation), it should be its own artifact that reads the neutral map as input and is never merged into it. The map is the durable, defensible object; the verdict is a replaceable opinion computed over it.

This is the most important design principle for the whole layer, and the reason the [inquiry "control room" that carries the verdict is rejected](./rejected-candidates.md): fusing `current_answer` / `confidence` into the case root collapses mapping the debate into winning it, and bounded-context theory says the two then get silently averaged.
