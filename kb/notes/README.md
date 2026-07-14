# Notes

The theoretical register of the Commonplace KB: transferable claims, mechanisms, definitions, and synthesis about how agent-operated knowledge bases — LLM wikis — should be built and operated. This is the theory the rest of the repository runs on; the methodology these notes describe is what agents follow to maintain this wiki.

The central thread is [deploy-time learning](./deploy-time-learning-is-the-missing-middle.md) — how deployed AI systems improve through structured knowledge that accumulates alongside the code — developed through the [constraining](./definitions/constraining.md), [distillation](./definitions/distillation.md), and discovery operations.

## Navigation

- [tags index](./tags-README.md) — the top-level hub linking every tag README (foundations, evaluation, learning theory, links, and the rest), plus the workshop layer and open gaps.
- [definitions/](./definitions/dir-index.md) — the project's core vocabulary (register, constraining, distillation, codification, and the rest), one term per file.

## How to read these notes

Titles are assertions, not topics, so following a link reads as a chain of reasoning: `since [title]` and `because [title]` compose into an argument rather than a table of contents. Each note carries a maturity mark (`seedling` → `current`) and links to the sources or notes it rests on, so you can tell how much weight a claim holds before you build on it.

## What belongs here

A claim earns a note when it changes how someone would build or operate a knowledge base. Pure pattern-recording without explanation belongs in `kb/log.md`, not here. For the full authoring contract — register, the reach quality bar, title and link conventions, and types — see [COLLECTION.md](./COLLECTION.md).

## Not the right collection?

- Current-state docs about the shipped Commonplace system — architecture, type system, ADRs → [kb/reference/](../reference/)
- Procedures, skills, review gates, how-to guidance → [kb/instructions/](../instructions/)
- Reviews of external agent-memory and knowledge systems → [kb/agent-memory-systems/](../agent-memory-systems/)
- In-flight drafts, investigations, and migration plans → [kb/work/](../work/)
