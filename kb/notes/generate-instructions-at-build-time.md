---
description: Claw skills should be generated from templates at setup time, not parameterised with runtime variables — applying the general principle that indirection is costly in LLM instructions
type: note
traits: []
areas: [claw-design]
status: seedling
---

# Generate claw skills at build time, don't parameterise them

Since [indirection is costly in LLM instructions](../notes/indirection-is-costly-in-llm-instructions.md), claw skills should be generated from templates rather than parameterised with runtime variables.

Skills in `project_claw/skills/` hardcode `project_claw/` paths dozens of times — in grep commands, script invocations, save targets. Making the claw reusable across projects requires these paths to vary. Two options:

**Runtime variables** — skills contain `$CLAW_ROOT/notes/` and the LLM substitutes on every invocation. Adds interpretation overhead to every skill use, across every substitution site. Occasionally the LLM gets it wrong.

**Build-time generation** — a template contains `{{claw_root}}/notes/`, a setup script resolves it to `project_claw/notes/`, and the generated skill is literal. The LLM reads and acts directly.

Build-time generation is the right choice. It's [stabilisation applied to configuration](./methodology-enforcement-is-stabilisation.md) — the template is soft, the generated output is hard. You pay the flexibility cost once at setup time, not on every use.

The canonical form for skills is standalone (paths relative to claw root: `./notes/`, `./scripts/`). Embedding a claw in a parent project (like llm-do's `project_claw/`) is the special case that requires a path prefix. The generation step adds that prefix.

---

Relevant Notes:
- [indirection is costly in LLM instructions](../notes/indirection-is-costly-in-llm-instructions.md) — foundation: the general principle this applies; in code indirection is free, in LLM instructions it costs context and interpretation on every read
- [methodology enforcement is stabilisation](./methodology-enforcement-is-stabilisation.md) — template generation is a point on the stabilisation gradient
- [CLAUDE.md is a router, not a manual](./context-loading-strategy.md) — motivates: always-loaded context should be slim; variable interpretation adds complexity
- [generate topic links from frontmatter](./adr/001-generate-topic-links-from-frontmatter.md) — exemplifies: an earlier case of the same move — replacing LLM-interpreted output with a deterministic build step

Topics:
- [claw-design](./claw-design.md)
