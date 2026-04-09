---
description: Historical decision to move skills to top-level sources, keep KB Goals always-loaded, split types into core and local, and use dynamic type discovery for practitioner-defined types
type: adr
tags: [architecture]
status: superseded
---

# 013-skills-first-delivery-with-core-local-type-split

**Status:** superseded by [ADR-014](./014-scripts-as-python-package-one-tree-model.md)
**Date:** 2026-04-08

This ADR records the intermediate skills-first packaging direction. The later direct-install model in [ADR-014](./014-scripts-as-python-package-one-tree-model.md) removed plugin delivery and is the current implementation.

## Context

The current installation requires copying a ~160-line AGENTS.md template that carries a routing table, content workflow, escalation boundaries, conventions, and search patterns — all always-loaded into the agent's context. This is problematic for two reasons:

1. **Embedded KBs** (KB inside a code project) pay a high context cost. The routing table competes with the project's own CLAUDE.md content.
2. **The template hardcodes our types.** The routing table references `adr`, `related-system`, `structured-claim` — types specific to our KB, not every KB. A practitioner building a payments KB doesn't need these and would need to edit the template to remove them and add their own.

Meanwhile, skills have matured enough that most of the routing table can be absorbed into an on-demand `/write` skill. The question is what the installed system should look like, and where framework skills should live.

## Decision

### 1. Skills as primary delivery mechanism

The always-loaded template shrinks to ~50 lines: KB Goals (practitioner fills in), a KB-exists pointer, a skill reference table, key index paths, and three structural search patterns. Everything about *how to operate* the KB moves into skills that load on demand.

### 2. Plugin packaging

Framework skills live at the repo root in `skills/` and are distributed as a plugin (`.claude-plugin/plugin.json` + `.codex-plugin/plugin.json`) for automatic namespacing (`/commonplace:write`) and one-step installation. Symlink fallback remains for environments without plugin support.

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

`kb/instructions/` remains for non-skill instructions and repo-local workflows such as `WRITING.md`, `REVIEW-SYSTEM.md`, `FIX-SYSTEM.md`, and their helper procedures. We do **not** keep a compatibility mirror of framework skills under `kb/instructions/`; `skills/` is the canonical location.

**Repo-local skills** stay in `kb/instructions/` and are not part of the framework contract today:
- `review-related-system` — depends on `related-system` local type

This is a temporary boundary, not a claim that related-system review should stay local forever. The current reason is dependency packaging: `review-related-system` depends not only on the `related-system` type but also on review-system procedures that are not yet shipped as framework infrastructure. We will revisit this once the review system itself has a framework-installable surface.

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
- Framework and local concerns are clearly separated — framework skills live in `skills/`, KB procedures live in `kb/instructions/`, and the practitioner's `kb/` is entirely theirs.

**Harder:**
- Skills must be well-written because they replace always-loaded instructions. A broken `/write` skill means the agent can't create notes properly, while a broken routing table row in the old template was just one row.
- Two plugin manifests to maintain (Claude Code + Codex).
- Dynamic type discovery adds complexity to the `/write` skill — it must handle missing types gracefully, discover templates across multiple `types/` directories, and parse target-directory declarations from templates.
- The framework/local skill split means `review-related-system` is not part of the installed framework contract yet. Packaging it cleanly requires shipping the review system as framework infrastructure, not just copying the `related-system` type.
- Core type templates must remain generic — any convention specific to our KB that leaks into a core type template breaks the contract.

## Implementation Notes

This ADR no longer reflects the implemented packaging. The current repository layout follows [ADR-014](./014-scripts-as-python-package-one-tree-model.md):

- framework skills live in `skills/`
- `commonplace-init` installs them directly into `.claude/skills/` and `.agents/skills/`
- plugin manifests are gone
- `kb/instructions/` contains writing/review/fix procedures and repo-local workflows, not a framework-skill mirror

The open follow-up remains review-system packaging: once the review system becomes a framework surface, `review-related-system` can move from "repo-local workflow" to a shipped framework skill whose only extra dependency is the copied `related-system` type.

**Supersedes:** This decision refines [ADR-006 (two-tree installation layout)](./006-two-tree-installation-layout.md) by specifying what crosses the boundary between the two trees and in what form. ADR-006 is now superseded by [ADR-014](./014-scripts-as-python-package-one-tree-model.md) which replaces the two-tree model with a one-tree-plus-package model. The skills-first delivery mechanism described here remains valid; the backend packaging has changed.

**Refined by:** [ADR-014 (scripts as Python package)](./014-scripts-as-python-package-one-tree-model.md) — operational scripts are now an installed Python package; skills invoke `commonplace-*` commands rather than script paths.

---

Relevant Notes:

- [ADR-006: two-tree installation layout](./006-two-tree-installation-layout.md) — foundation: establishes `kb/` as user content and `commonplace/` as framework
- [agent context is constrained by soft degradation](../agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md) — grounds: why Goals must be always-loaded (scoping degrades silently)
- [agent statelessness makes routing architectural](../agent-statelessness-makes-routing-architectural-not-learned.md) — grounds: every session is day one; skills are permanent prosthetics
- [skills derive from methodology through distillation](../skills-derive-from-methodology-through-distillation.md) — grounds: the `/write` skill is a distillation of the routing table and content workflow
- [practitioner contract](../../work/system-documentation/practitioner-contract.md) — extends: the full framework-vs-practitioner boundary this ADR establishes
