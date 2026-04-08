---
description: Decision to deliver commonplace as a plugin with skills as the primary interface, splitting types into core (note, text, index, source-review) and local, with Goals inlined and dynamic type discovery for practitioner-defined types
type: adr
tags: [architecture]
status: proposed
---

# 013-skills-first-delivery-with-core-local-type-split

**Status:** proposed
**Date:** 2026-04-08

## Context

The current installation requires copying a ~160-line AGENTS.md template that carries a routing table, content workflow, escalation boundaries, conventions, and search patterns — all always-loaded into the agent's context. This is problematic for two reasons:

1. **Embedded KBs** (KB inside a code project) pay a high context cost. The routing table competes with the project's own CLAUDE.md content.
2. **The template hardcodes our types.** The routing table references `adr`, `related-system`, `structured-claim` — types specific to our KB, not every KB. A practitioner building a payments KB doesn't need these and would need to edit the template to remove them and add their own.

Meanwhile, skills have matured enough that most of the routing table can be absorbed into an on-demand `/write` skill. The question is what the installed system should look like.

### What the plan explored

The [installation-simplification workshop](../../work/installation-simplification/plan.md) explored:
- Moving routing from always-loaded template into skills (the `/write` skill absorbs the routing table, content workflow, and type routing)
- Plugin packaging for one-step installation with automatic namespacing
- Which types are framework (every KB needs them) and which are our local content types
- Whether Goals should be in a separate file or always-loaded (resolved: always-loaded, because scoping decisions [degrade silently](../agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md) without them)
- How the `/write` skill handles practitioner-defined types it doesn't know about (dynamic discovery)
- A [practitioner contract](../../work/system-documentation/practitioner-contract.md) defining what the framework provides vs what the practitioner owns

## Decision

### 1. Skills as primary delivery mechanism

The always-loaded template shrinks to ~50 lines: KB Goals (practitioner fills in), a KB-exists pointer, a skill reference table, key index paths, and three structural search patterns. Everything about *how to operate* the KB moves into skills that load on demand.

### 2. Plugin packaging

Skills are distributed as a plugin (`.claude-plugin/plugin.json` + `.codex-plugin/plugin.json`) for automatic namespacing (`/commonplace:write`) and one-step installation. Symlink fallback remains for environments without plugin support.

### 3. Core types vs local types

Four **core types** ship with the framework and are copied to the practitioner's `kb/*/types/` at install:

| Type | Collection | Why core |
|------|-----------|----------|
| `note` | `kb/notes/` | Default structured writing type. Every KB needs this. |
| `text` | `kb/notes/` | No frontmatter. Raw capture. Every KB needs a low-friction entry point. |
| `index` | `kb/notes/` | Curated navigation hub. Tags need indexes to become navigable. |
| `source-review` | `kb/sources/` | Source analysis. Ingestion is a basic KB operation. |

All other types (`structured-claim`, `adr`, `related-system`, `spec`, `review`, task types) are **local types** — they stay in `commonplace/` as examples the practitioner can optionally copy. Framework skills depend only on core types.

### 4. Framework skills vs local skills

Seven **framework skills** move to `skills/` and ship via the plugin:
- `write` — routes to `note` by default, discovers local types dynamically
- `connect` — searches notes by description
- `validate` — checks frontmatter against type definitions
- `snapshot-web` — snapshots URLs into `kb/sources/`
- `ingest` — snapshots and analyzes sources using `source-review` type
- `convert` — converts between core types (text→note)
- `revise-iterative` — iteratively revises notes

**Local skills** stay in `kb/instructions/` and are not part of the plugin:
- `review-related-system` — depends on `related-system` local type

### 5. Goals are always-loaded

KB Goals are inlined in the control-plane template, not in a separate `kb/GOALS.md` file. The agent needs scope every turn to decide whether work belongs in the KB. A pointer-only approach means scope is available only after a skill fires — but scoping decisions happen *before* skill invocation, and without Goals in context, those decisions degrade silently.

### 6. Dynamic type discovery

The `/write` skill hardcodes core types (guaranteed to exist, no filesystem scan needed) and discovers local types dynamically by scanning `kb/*/types/` for matching templates. Type templates declare their target directory so the routing doesn't need to be hardcoded. If a requested type isn't found, the skill errors with the list of available types.

This lets practitioners add their own types by dropping templates into `kb/*/types/` — no registration step, no template modification, no skill changes.

## Consequences

**Easier:**
- Installation is simpler — plugin install + copy core types + fill in Goals. No 160-line template to understand and customize.
- Embedded KBs pay less context cost — ~50 lines instead of ~160.
- Practitioners can add domain-specific types without editing framework files.
- Framework and local concerns are clearly separated — the practitioner's `kb/` is entirely theirs.

**Harder:**
- Skills must be well-written because they replace always-loaded instructions. A broken `/write` skill means the agent can't create notes properly, while a broken routing table row in the old template was just one row.
- Two plugin manifests to maintain (Claude Code + Codex).
- Dynamic type discovery adds complexity to the `/write` skill — it must handle missing types gracefully, discover templates across multiple `types/` directories, and parse target-directory declarations from templates.
- The framework/local skill split means `review-related-system` isn't available by default — practitioners who want it must copy the type and symlink the skill manually.
- Core type templates must remain generic — any convention specific to our KB that leaks into a core type template breaks the contract.

**Supersedes:** This decision refines [ADR-006 (two-tree installation layout)](./006-two-tree-installation-layout.md) by specifying what crosses the boundary between the two trees and in what form. ADR-006 remains valid for the overall layout; this ADR specifies the delivery mechanism within that layout.

---

Relevant Notes:

- [ADR-006: two-tree installation layout](./006-two-tree-installation-layout.md) — foundation: establishes `kb/` as user content and `commonplace/` as framework
- [agent context is constrained by soft degradation](../agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md) — grounds: why Goals must be always-loaded (scoping degrades silently)
- [agent statelessness makes routing architectural](../agent-statelessness-makes-routing-architectural-not-learned.md) — grounds: every session is day one; skills are permanent prosthetics
- [skills derive from methodology through distillation](../skills-derive-from-methodology-through-distillation.md) — grounds: the `/write` skill is a distillation of the routing table and content workflow
- [installation-simplification plan](../../work/installation-simplification/plan.md) — extends: the detailed migration steps this ADR summarizes
- [practitioner contract](../../work/system-documentation/practitioner-contract.md) — extends: the full framework-vs-practitioner boundary this ADR establishes
