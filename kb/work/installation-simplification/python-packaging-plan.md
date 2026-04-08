# Plan: scripts as a Python package, project initialized locally

Follow-up to `plan.md`. This replaces the two-tree assumption for operational tooling.

## Decision

Commonplace should ship:

- skills as a plugin
- scripts as a Python package
- project-local KB structure via initialization, not via a permanently vendored `commonplace/` subtree

The Python package is the operational engine. It provides:

- validator
- review system
- snapshot helpers
- index generation and sync tools
- note maintenance tools
- project initialization

The plugin remains the skill surface only.

## Installation model

The consumer installation story should look more like Django project setup than vendoring a framework repo:

1. install the Commonplace plugin
2. install the Commonplace Python package
3. run an init command that creates and seeds the local project structure

After initialization, the user's repo contains the KB directories and starter assets it needs directly under the project root.

No permanent `commonplace/` framework subtree is required in the consuming project.

## Resulting architecture

### 1. Plugin

The plugin ships skill definitions only:

- plugin manifest
- `skills/`

Skills invoke stable commands provided by the Python package. They do not shell out to relative files under `scripts/`.

### 2. Python package

The package ships:

- operational code
- package data needed by operational code
- scaffold/init assets used to create project-local files

### 3. Initialized project tree

The user's repo contains the local KB and control-plane files after running init:

```text
my-project/
├── AGENTS.md or CLAUDE.md
├── kb/
│   ├── instructions/
│   ├── notes/
│   ├── sources/
│   ├── tasks/
│   ├── work/
│   └── reports/
├── types/
└── ...
```

This is the only content tree the operational tools act on.

## Repository structure

Target source layout for the Commonplace repo:

```text
commonplace/
├── .claude-plugin/
│   └── plugin.json
├── .codex-plugin/
│   └── plugin.json
├── skills/
│   ├── validate/SKILL.md
│   ├── write/SKILL.md
│   ├── snapshot-web/SKILL.md
│   └── ...
├── src/commonplace/
│   ├── __init__.py
│   ├── cli/
│   │   ├── init_project.py
│   │   ├── validate_notes.py
│   │   ├── generate_notes_index.py
│   │   ├── sync_generated_index.py
│   │   ├── sync_topic_links.py
│   │   ├── relocate_note.py
│   │   ├── github_snapshot.py
│   │   ├── x_snapshot.py
│   │   ├── run_review_bundle.py
│   │   ├── run_gate_sweep.py
│   │   ├── create_review_run.py
│   │   ├── write_gate_review.py
│   │   ├── finalize_review_run.py
│   │   ├── ack_gate_review.py
│   │   └── promotion_candidates.py
│   ├── review/
│   │   ├── review_db.py
│   │   ├── review_metadata.py
│   │   ├── review_model.py
│   │   ├── review_runners.py
│   │   ├── review_target_selector.py
│   │   ├── resolve_gates.py
│   │   ├── warn_selector.py
│   │   ├── gate_sweep_format.py
│   │   └── data/
│   │       └── review-schema.sql
│   ├── lib/
│   │   ├── frontmatter.py
│   │   └── type_resolver.py
│   ├── scaffold/
│   │   ├── __init__.py
│   │   ├── AGENTS.md.template → ../../../AGENTS.md.template
│   │   ├── kb/
│   │   │   └── instructions → ../../../../kb/instructions
│   │   └── types → ../../../types
│   └── migrations/
│       └── ...
├── pyproject.toml
├── uv.lock
└── INSTALL.md
```

Notes:

- `skills/` stays outside the Python package.
- `scaffold/` uses symlinks to the repo's canonical files rather than maintaining copies. The symlinks point to `kb/instructions/`, `types/`, and `AGENTS.md.template` at the repo root. During development (editable install), `importlib.resources` follows the symlinks to the live files. During wheel builds, hatchling dereferences the symlinks and embeds the actual file contents — the wheel is self-contained.
- This means edits to instruction files, type definitions, or the AGENTS template are immediately available to `commonplace-init` without any sync step.

## Package responsibilities

The Python package owns:

- all current Python in `scripts/` that is intended for execution
- shared libraries currently imported implicitly from sibling files
- package data required by code
- scaffold assets copied into user repos by init

This is broader than "just scripts". It includes the assets that make script execution and project setup work reliably.

## Root semantics

The one-tree model removes the need for `framework_root`.

Tools operate against a single explicit root:

- `workspace_root` — the initialized user project

Working rules:

- read/write user artifacts from `workspace_root`
  - `kb/notes/`
  - `kb/sources/`
  - `kb/work/`
  - `kb/reports/`
  - `types/`
- read scaffold assets from package data
  - `commonplace.scaffold.*`
- read review schema from package data
  - `commonplace.review.data`

There should be no runtime dependence on a separate vendored framework checkout.

## Package data

The package must ship two classes of non-Python data.

### 1. Runtime data

Example:

- `review-schema.sql`

This should be loaded with `importlib.resources`.

### 2. Scaffold/init data

`src/commonplace/scaffold/` contains symlinks to the repo's canonical assets:

- `AGENTS.md.template` → `../../../AGENTS.md.template`
- `kb/instructions` → `../../../../kb/instructions`
- `types` → `../../../types`

These are loaded from package data via `importlib.resources` and copied into the local project during initialization. The symlink approach avoids maintaining duplicate files — the scaffold always reflects the current state of the repo's instructions and type definitions.

## Init command

The package should expose a first-class init command, for example:

```bash
commonplace-init
```

Responsibilities of `commonplace-init`:

- create the local `kb/` directory structure
- create `types/`
- seed `kb/instructions/`
- seed review gates and fix instructions
- seed core type templates
- seed `AGENTS.md` or emit a fragment for the user to merge
- avoid overwriting user-modified files without explicit confirmation

This command becomes the main bridge between the packaged framework and the user's local repo.

## Invocation model

Skills invoke commands, not file paths.

Before:

```bash
python3 <path-to-script>/validate_notes.py "$ARGUMENTS"
```

After:

```bash
commonplace-validate-notes "$ARGUMENTS"
```

Development inside the Commonplace repo continues to use:

```bash
uv run commonplace-validate-notes "$ARGUMENTS"
```

Runtime contract:

- supported installs provide CLI commands
- skills assume those commands exist
- missing commands are setup errors
- `uv run` is a development convenience, not the primary user-facing contract

## Installation story

Commonplace installation now has three explicit steps:

1. install the plugin
2. install the Python package
3. run `commonplace-init`

`INSTALL.md` should be rewritten around this flow.

It should describe:

- prerequisites
- plugin install
- Python package install
- project initialization
- re-running init or sync commands safely over time

## CLI surface

Use stable `commonplace-*` command names to avoid collisions.

### Stable public commands

- `commonplace-init`
- `commonplace-validate-notes`
- `commonplace-generate-notes-index`
- `commonplace-sync-generated-index`
- `commonplace-sync-topic-links`
- `commonplace-relocate-note`
- `commonplace-github-snapshot`
- `commonplace-x-snapshot`
- `commonplace-run-review-bundle`
- `commonplace-run-gate-sweep`
- `commonplace-create-review-run`
- `commonplace-write-gate-review`
- `commonplace-finalize-review-run`
- `commonplace-ack-gate-review`
- `commonplace-promotion-candidates`

These get:

- a `main()` entry point
- a `[project.scripts]` entry
- compatibility expectations across releases

### Internal package modules

These are importable implementation details, not public command interfaces:

- frontmatter parsing
- type resolution
- review DB helpers
- review metadata/model/runner helpers
- gate resolution helpers
- formatting helpers

### Internal or migration-only tools

These should not be documented as stable public commands unless a real user-facing need appears:

- repair scripts
- one-off migration scripts
- reparse / prune / import repair tools
- MkDocs-specific internal hooks

## Review system status

The review system is first-class in this design.

That means:

- review modules move into the package
- schema loading moves to package data
- review CLIs become formal entry points
- review gates are seeded locally by init rather than read from a vendored framework tree

The review system is the main reason "scripts as a real package" is the right design.

## Migration plan

### Phase 1: establish package skeleton

1. Create `src/commonplace/` with `__init__.py`.
2. Add package submodules for:
   - `cli`
   - `review`
   - `lib`
   - `scaffold`
3. Update `pyproject.toml` to use src layout and define entry points.

### Phase 2: move shared libraries

1. Move `frontmatter.py` into the package.
2. Move `type_resolver.py` into the package.
3. Update imports in validator and review code to package imports.

### Phase 3: move validator and snapshot tools

1. Move validator and snapshot scripts into package CLI modules.
2. Add `main()` wrappers where needed.
3. Update skills to call command names instead of file paths.

### Phase 4: move review system

1. Move review modules into package subpackages.
2. Move `review-schema.sql` into package data.
3. Rewrite schema loading to use `importlib.resources`.
4. Rewrite any subprocess chaining that still assumes sibling script files on disk.

### Phase 5: add init/scaffold system ✓

1. Created `src/commonplace/scaffold/` with symlinks to `kb/instructions/`, `types/`, and `AGENTS.md.template`. Symlinks avoid file duplication; hatchling dereferences them into wheels.
2. Implemented `commonplace-init` using `importlib.resources` to copy scaffold files into the target project.
3. Overwrite policy: existing files are never overwritten. Rerunning init is safe and idempotent.
4. `AGENTS.md.template` is seeded as-is; user renames to `CLAUDE.md` or `AGENTS.md`.

### Phase 6: docs and install

1. Rewrite `INSTALL.md` around plugin + Python package + init.
2. Remove the two-tree install story from user-facing docs.
3. Document which commands are stable and which remain internal.

### Phase 7: retire old `scripts/` layout

1. Remove or shrink the root-level `scripts/` directory after migration.
2. Leave wrappers only if needed during transition.
3. Drop wrappers once skills and docs no longer reference them.

## Compatibility policy

There is no strong reason to preserve old script-path invocation forever.

Because Commonplace has no large external installed base yet, prefer a clean move:

- skills migrate to command invocation
- docs migrate to package commands
- two-tree installation docs are removed rather than maintained in parallel
- temporary wrappers are optional and should be short-lived if used at all

## Open questions

- ~~What exactly should `commonplace-init` seed by default versus only on request?~~ **Resolved:** seeds all instructions, review gates, fix-warnings, type definitions, and AGENTS.md.template by default.
- ~~How should rerunning init handle local modifications~~ **Resolved:** never overwrite existing files. `--force` and `--dry-run` can be added later if needed.
- ~~Should AGENTS/CLAUDE setup be fully generated, or should init emit a mergeable fragment?~~ **Resolved:** init seeds `AGENTS.md.template` as-is; user copies/renames it.
- How should plugin installation for consumers work in the absence of a vendored local plugin path?

## Recommended next move

Treat this as the primary packaging direction.

The first implementation slice should be:

1. package skeleton in `src/commonplace/`
2. move `frontmatter.py`, `type_resolver.py`, and `validate_notes.py`
3. define one working CLI command end-to-end
4. add a minimal `commonplace-init` that creates local directories
5. use that slice to lock the one-tree init model before moving the review system
