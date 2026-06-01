---
description: Decision to split installed projects into two directory trees — user content in kb/, framework in commonplace/ — with operational artifacts copied to kb/ for fast agent access and methodology kept in commonplace/ as fallback
type: ../types/adr.md
tags: []
status: superseded
---

# 006-two-tree-installation-layout

**Status:** superseded by [ADR-014](./014-scripts-as-python-package-one-tree-model.md)
**Date:** 2026-03-23

## Context

When a project adopts Commonplace, the agent needs access to two kinds of material:

1. **Operational artifacts** (types, WRITING.md, skills) — read on almost every write. These are the hot path.
2. **Methodology notes** — consulted when a skill or instruction doesn't cover an edge case. These are fallback.

The design question: should these live in one tree or two, and if two, what crosses the boundary?

A single tree (everything in `kb/`) is simpler to explain but creates problems:
- Every search returns both project notes and framework notes. The agent needs filtering instructions ("ignore notes with `source: commonplace`") — more instructions, more room for error.
- The user's content is interleaved with framework content. Ownership boundaries are unclear.
- Upgrading the framework means diffing files scattered across the user's tree.

A pure two-tree split (everything in `commonplace/`, nothing copied) avoids interleaving but adds friction:
- Every write instruction must specify which tree to read from: "for types, look in commonplace/; for content, write to kb/."
- The agent resolves a cross-tree path on every write — not more hops, but more complex instructions.

## Decision

Two trees at the project root:
- `kb/` — the user's knowledge base. Their notes, sources, tasks. Tracked in the project's git.
- `commonplace/` — the framework. Methodology, theory, canonical type definitions, skills, scripts. A git submodule or gitignored clone.

The boundary principle: **copy what the agent reads on the hot path; reference what it consults as fallback.**

The install step **copies operational artifacts** into `kb/`:
- Type definitions (`types/`, `kb/*/types/`)
- Writing guide (`kb/instructions/WRITING.md`)

It also creates the directory structure (empty dirs for notes, sources, tasks, work).

Everything else **stays in `commonplace/`** and is consulted on demand:
- Methodology notes
- Source snapshots
- Skills (symlinked into runtime discovery directories, not copied)
- Scripts

This keeps the common-case write path entirely within `kb/` (route from always-loaded control plane, read types, read WRITING.md, write file — all one tree) while keeping methodology one explicit search hop away. The benefit is simpler instructions, not fewer hops — hop count is the same whether artifacts are copied or read cross-tree.

## Consequences

**Easier:**
- The common write path stays within one tree. No cross-tree resolution in instructions.
- Searches over `kb/` return only the user's content. No filtering logic needed.
- The user has clean ownership: everything in `kb/` is theirs.
- Upgrades are straightforward: update the submodule (or pull the clone), re-copy operational artifacts. Commonplace-provided types are replaced; user-added types are left untouched.

**Harder:**
- Two copies of operational artifacts (canonical in `commonplace/`, working copy in `kb/`). If the canonical version changes, the install step must re-run. The types are stable enough that this is infrequent.
- The agent must know that methodology lives in a different tree. The control-plane routing table handles this ("for why things work this way, search `commonplace/kb/`"), but it's an extra concept for the always-loaded context to carry.
- Skill promotion requires symlinks into runtime-specific discovery directories (`.claude/skills/`, `.agents/skills/`). This is an install-time step, not an ongoing burden, but it adds setup complexity.

The naming choice `kb/` over `memory/` avoids collision with Claude Code's per-user auto-memory directory at `~/.claude/projects/<project>/memory/`. The two serve different purposes (shared project knowledge vs personal preferences), and using the same name would create ambiguity.

The historical installation procedure lived outside the shipped KB surface. This ADR is retained as superseded design history, not current setup guidance.

---

Relevant Notes:

- [014-scripts-as-python-package-one-tree-model](./014-scripts-as-python-package-one-tree-model.md) — the accepted decision that superseded this layout
