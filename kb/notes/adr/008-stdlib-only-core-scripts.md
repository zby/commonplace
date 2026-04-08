---
description: Core scripts use only Python stdlib by defining a strict frontmatter grammar that a regex parser handles completely
type: adr
tags: [architecture]
status: accepted
---

# 008-Stdlib-only core scripts

**Status:** accepted
**Date:** 2026-03-24

## Context

Commonplace scripts are invoked by agents via skill instructions (e.g., `uv run scripts/notes_selector.py`). When commonplace is installed into another project, the scripts need to be callable from that project's working directory. A Python venv tied to the commonplace directory creates friction: every skill invocation would need to `cd` to the commonplace root or use `uv run --directory`, and the user must run `uv sync` as a setup step.

Several scripts imported PyYAML to parse frontmatter. But a survey of all frontmatter across the KB showed that only a tiny subset of YAML is actually used: top-level scalar fields and inline lists (`[a, b, c]`). No nesting, no block-style lists, no multi-line scalars, no anchors.

## Decision

Define a **strict frontmatter grammar** as a proper subset of YAML, and implement a single shared parser (`scripts/frontmatter.py`) that handles it completely using only stdlib. The grammar:

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

All scripts — including `validate_notes.py` — now use this shared module. PyYAML is removed entirely from core and validation scripts. Move all external dependencies (`mkdocs`, `xdk`) to optional dependency groups in `pyproject.toml`. Core scripts (`scripts/`) require only Python 3.11+ stdlib.

## Consequences

- **Easier installation**: `python3 scripts/foo.py` works without a venv. No `uv sync` needed for core operations. (Note: [ADR-014](./014-scripts-as-python-package-one-tree-model.md) later moved scripts into an installed package with `commonplace-*` entry points. The stdlib-only constraint remains — it means the package has no runtime dependencies.)
- **No cwd problem**: Skills can invoke scripts from any working directory by using an absolute path to the script. (Now moot — commands are on `$PATH` after `pip install`.)
- **Grammar is the contract**: The frontmatter grammar is defined in one place (`scripts/frontmatter.py` docstring). Validation enforces it. If the grammar needs to grow, the parser and the grammar spec evolve together.
- **Duplicate key detection preserved**: The shared parser detects and reports duplicate keys, maintaining the validation guarantee that PyYAML's custom loader previously provided.
- **Optional capabilities still need setup**: MkDocs site building needs `pip install commonplace[docs]`, X snapshots need `pip install commonplace[snapshot]`.
- **Block-style YAML is intentionally unsupported**: If someone writes `tags:\n  - foo\n  - bar`, the parser won't understand it. This is a feature — the grammar is narrow by design and the validator will flag the error.

---

Relevant Notes:

- [commonplace-architecture](../commonplace-architecture.md) — overall system structure
- [commonplace-installation-architecture](../commonplace-installation-architecture.md) — two-tree installation model this decision supports
- [006-two-tree-installation-layout](./006-two-tree-installation-layout.md) — the installation layout that motivates portable scripts
- [deterministic-validation-should-be-a-script](../deterministic-validation-should-be-a-script.md) — validation now uses the shared grammar parser instead of PyYAML
- [files-not-database](../files-not-database.md) — files-first philosophy that this decision extends to the tooling layer
