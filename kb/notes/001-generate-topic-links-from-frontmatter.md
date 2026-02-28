---
description: Replace LLM-generated Topics footers with a deterministic script that reads the areas: frontmatter field
type: adr
traits: []
areas: [claw-design, links]
status: accepted
---

# ADR-001: Generate Topic links from frontmatter

**Status:** Accepted

**Date:** 2026-02-21

## Context

Notes have an `areas:` field in YAML frontmatter listing which indexes they belong to. The `Topics:` footer section contains markdown links to those same indexes, providing navigation back to the index from the rendered note.

Previously, `/connect` (an LLM skill) generated these Topics links using semantic judgment. But the mapping is entirely mechanical: read `areas`, write links. This led to drift:

- 6 notes had `areas:` but no Topics section
- 5 notes had Topics linking to the wrong index (e.g., `areas: [approvals-index]` but Topics pointed to `[index]`)

This is the general pattern described in [storing LLM outputs is stabilization](../../notes/storing-llm-outputs-is-stabilization.md): when a step is deterministic, replace the stochastic LLM step with code.

## Decision

Created `scripts/sync_topic_links.py` — a Python script that:

1. Reads frontmatter `areas:` field (single source of truth)
2. Generates the correct `Topics:` footer section
3. Replaces any existing Topics section or appends one
4. Resolves relative paths when index files are in parent directories

The script takes explicit file/directory arguments — agents run it only on notes they've changed, not the whole corpus.

The `/connect` skill's Gate 6 now calls this script instead of doing manual grep-and-edit.

## Consequences

- **Topics footers are always correct** — no more drift between frontmatter and footer
- **One fewer LLM judgment call** — `/connect` focuses on semantic work (finding relationships), not mechanical linking
- **Idempotent** — running the script twice produces the same result
- **Works across directories** — `docs/notes/` and `docs/claw-design/` both supported
- **Testable** — 38 unit tests cover parsing, generation, path resolution, and edge cases

Topics:
- [claw-design](./claw-design.md)
- [links](./links.md)
