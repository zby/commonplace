---
description: Core scripts use only Python stdlib by defining a strict frontmatter grammar that a regex parser handles completely
type: ../types/adr.md
tags: []
status: accepted
---

# 008-Stdlib-only core scripts

**Status:** accepted
**Date:** 2026-03-24

## Context

Commonplace scripts are invoked by agents via skill instructions (e.g., `uv run scripts/notes_selector.py`). When Commonplace is installed into another project, the scripts need to be callable from that project's working directory. A Python venv tied to the Commonplace directory creates friction: every skill invocation would need to `cd` to the Commonplace root or use `uv run --directory`, and the user must run `uv sync` as a setup step.

Several scripts imported PyYAML to parse frontmatter. But a survey of all frontmatter across the KB showed that only a tiny subset of YAML is actually used: top-level scalar fields and inline lists (`[a, b, c]`). No nesting, no block-style lists, no multi-line scalars, no anchors.

## Decision

Define a **strict frontmatter grammar** as a proper subset of YAML, and implement a single shared parser that handles it completely using only stdlib. The grammar:

```
frontmatter  := "---\n" line* "---\n"
line         := key ":" SP value NL
key          := [a-z][a-z0-9_-]*
value        := inline_list | quoted_string | unquoted_scalar
inline_list  := "[" ( item ( "," item )* )? "]"
item         := quoted_string | unquoted_item
quoted_string:= '"' [^"]* '"'  |  "'" [^']* "'"
unquoted_scalar := .+  (trimmed; must not start with [ or {)
```

PyYAML is dropped from core and validation scripts. External dependencies (`properdocs`, `xdk`) move to optional dependency groups. Core scripts require only Python 3.11+ stdlib.

Amended by [ADR-014](./014-scripts-as-python-package-one-tree-model.md): scripts became installed package entry points, and the package later acquired base runtime dependencies (including XDK and python-dotenv, because the base installation exposes `commonplace-x-snapshot` and an installed command must be executable without an unrequested extra). The frontmatter parser remains stdlib-only.

## Consequences

- **Easier installation**: scripts work without a venv. No `uv sync` needed for core operations.
- **No cwd problem**: Skills can invoke scripts from any working directory.
- **Grammar is the contract**: The frontmatter grammar is defined in one place, in the parser. Validation enforces it. If the grammar needs to grow, the parser and the grammar spec evolve together.
- **Duplicate key detection preserved**: The shared parser detects and reports duplicate keys, maintaining the validation guarantee that PyYAML's custom loader previously provided.
- **Optional capabilities still need setup**: ProperDocs site building needs the `docs` extra.
- **Block-style YAML is intentionally unsupported**: If someone writes `tags:\n  - foo\n  - bar`, the parser won't understand it. This is a feature — the grammar is narrow by design and the validator will flag the error.

---

Relevant Notes:

- [commonplace-architecture](../architecture.md) — overall shipped system structure
- [006-two-tree-installation-layout](./006-two-tree-installation-layout.md) — the installation layout that motivates portable scripts
- [014-scripts-as-python-package-one-tree-model](./014-scripts-as-python-package-one-tree-model.md) — the later packaging change that kept the stdlib-only runtime constraint while changing delivery
