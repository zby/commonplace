---
description: KB skills should be generated from templates at setup time, not parameterised with runtime variables — applying the general principle that indirection is costly in LLM instructions
type: note
traits: []
areas: [kb-design]
status: seedling
---

# Generate KB skills at build time, don't parameterise them

Since [indirection is costly in LLM instructions](../notes/indirection-is-costly-in-llm-instructions.md), KB skills should be generated from templates rather than parameterised with runtime variables.

Skills in `kb/instructions/` hardcode paths dozens of times — in grep commands, script invocations, save targets. Making the KB reusable across projects requires these paths to vary. Two options:

**Runtime variables** — skills contain `$CLAW_ROOT/notes/` and the LLM substitutes on every invocation. Adds interpretation overhead to every skill use, across every substitution site. Occasionally the LLM gets it wrong.

**Build-time generation** — a template contains `{{claw_root}}/notes/`, a setup script resolves it to `commonplace/kb/notes/`, and the generated skill is literal. The LLM reads and acts directly.

Build-time generation is the right choice. It's [stabilisation applied to configuration](./methodology-enforcement-is-stabilisation.md) — the template is soft, the generated output is hard. You pay the flexibility cost once at setup time, not on every use.

The canonical form for skills is standalone (paths relative to KB root: `./notes/`, `./scripts/`). Embedding a knowledge base in a parent project (like `commonplace/`) is the special case that requires a path prefix. The generation step adds that prefix.

---

Relevant Notes:

- [indirection is costly in LLM instructions](../notes/indirection-is-costly-in-llm-instructions.md) — foundation: the general principle this applies; in code indirection is free, in LLM instructions it costs context and interpretation on every read
- [methodology enforcement is stabilisation](./methodology-enforcement-is-stabilisation.md) — template generation is a point on the stabilisation gradient
- [CLAUDE.md is a router, not a manual](./context-loading-strategy.md) — motivates: always-loaded context should be slim; variable interpretation adds complexity
- [generate topic links from frontmatter](./adr/001-generate-topic-links-from-frontmatter.md) — exemplifies: an earlier case of the same move — replacing LLM-interpreted output with a deterministic build step

Topics:

- [kb-design](./kb-design.md)
