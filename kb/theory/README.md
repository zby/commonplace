# Theory

The theory collection of the Commonplace KB: transferable claims, mechanisms, definitions, and synthesis about how agent-operated knowledge bases — LLM wikis — should be built and operated. This is the theory the rest of the repository runs on; the methodology these notes describe is what agents follow to maintain this wiki.

The central thread is [continual learning](./deployed-systems-can-learn-from-feedback-with-fixed-model-weights.md) — how deployed AI systems improve through structured knowledge that accumulates alongside the code — developed through [constraining](./definitions/constraining.md), source-derived reshaping, and the [discovery lifecycle](./definitions/discovery-lifecycle.md).

## Navigation

Start with **[tags](../tags/README.md)** to browse by topic (the main access path across the KB; each tag head recommends where to start and lists every member by collection), or start from a recurring problem in **[questions/](./questions/README.md)**. The build-time complete file listing linked at the bottom is an A–Z fallback rather than the primary browse view.

- [tags index](../tags/README.md) — primary topical browse path in `kb/tags/` linking every tag head (self-improving systems, learning theory, context engineering, evaluation, KB maintenance, and the rest).
- [questions/](./questions/README.md) — recurring theoretical questions treated as first-class thinking starting points beside claims.
- [definitions/](./definitions/README.md) — transferable vocabulary such as constraining, codification, and discovery lifecycle, one term per file. Selected Commonplace vocabulary lives in reference definitions instead.
- [evidence/](./evidence/README.md) — bounded datasets, experiments, trace cohorts, and comparative casebooks.
- [proposals/](./proposals/README.md) — finished theory waiting on an adoption decision.
- [agent-memory-requirements/](./agent-memory-requirements/README.md) — concrete agent-memory requirements inventory.

## How to read these notes

Titles are assertions, not topics, so following a link reads as a chain of reasoning: `since [title]` and `because [title]` compose into an argument rather than a table of contents. Each note carries a discriminating description and links to the sources or notes it rests on. An optional `user-verified: true` records explicit human attestation to the current contents; its absence makes no claim about truth, maturity, or currency.

## What belongs here

A claim earns a note when it changes how someone would build or operate a knowledge base. Pure pattern-recording without explanation belongs in `kb/log.md`, not here. For the full authoring contract — intended contribution, the explanatory-reach quality bar, title and link conventions, and type eligibility — see [COLLECTION.md](./COLLECTION.md).

## Not the right collection?

- Current-state docs about the shipped Commonplace system — architecture, type system, ADRs → [kb/reference/](../reference/README.md)
- Procedures, skills, review gates, how-to guidance → [kb/instructions/](../instructions/README.md)
- Current reviews and comparisons of external agent systems, including memory systems → [Agentic Systems](../agentic-systems/README.md)
- In-flight drafts, investigations, and migration plans → [kb/work/](../work/README.md)
