# Independence clustering of evidence

Source: imported from the [ChatGPT second opinion](./chatgpt-second-opinion.md). Probably the highest-value import — this menu was otherwise silent on correlated evidence, which FLF explicitly calls out.

Tag each evidence item with an `independence_cluster` and its shared dependencies (dataset, method, authorship, citation lineage), so reviews and dashboards can flag "12 items, 3 plausibly independent clusters." Ten papers are not ten pieces of evidence if they share the same dataset, method, assumptions, or citation lineage.

It is the evidence-side analogue of the reviewer-side logic in [error correction works with above-chance oracles and decorrelated checks](../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md). Its link-level expression is `correlated-with` / `independent-of` edges (see [dialectical link vocabulary](./dialectical-link-vocabulary.md)); its review-level expression is the `correlation-double-counting` gate (see [epistemic review gates](./epistemic-review-gates.md)).
