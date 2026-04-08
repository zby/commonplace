# Plan: plugin skills + slim template

## Scope

This plan is about the **AGENTS.md.template** and skill surface shipped to users. It is not about this repo's own AGENTS.md, which has additional repo-specific content (development conventions, git rules, vocabulary, etc.) that other projects would define for themselves.

Assumption update: consumer projects no longer vendor a permanent `commonplace/` subtree. Skills are installed as a plugin, scripts are installed as a Python package, and `INSTALL.md` should describe initializing the local project tree directly.

## Principle

Always-loaded content should be limited to what the agent needs to **discover** the KB and **decide to use** it. Everything about **how to operate** the KB moves into skills that load on demand. Skills are distributed as a **plugin** for automatic namespacing and one-step installation.

## Distribution: plugin packaging

### Why plugins, not symlinks

- **Namespacing** — plugins get automatic `commonplace:write` namespacing, preventing collisions with project-specific skills. Symlinks require manual prefix hacks.
- **One-step skill install** — install the plugin, done. No symlink loops.
- **Symlink reliability** — the `/skills` command may not follow symlinks reliably.
- **Cross-platform** — both Claude Code and Codex have plugin systems. The SKILL.md format is the same; only the packaging wrapper differs.

### Plugin structure in the Commonplace source repo

```
commonplace/
  .claude-plugin/
    plugin.json                 # default skills/ path
  .codex-plugin/
    plugin.json                 # same, Codex format
  skills/                       # Actual skill files — clean for practitioners and plugins
    write/SKILL.md
    connect/SKILL.md
    validate/SKILL.md
    snapshot-web/SKILL.md
    ingest/SKILL.md
    convert/SKILL.md
    revise-iterative/SKILL.md
    review-related-system/SKILL.md
  kb/                           # Source material for seeded local project files
  types/
  src/commonplace/             # Python package for scripts/init
  AGENTS.md.template
  INSTALL.md
```

Key design: **skills live in `skills/`**. Non-skill content is not loaded from a vendored framework tree at runtime; it is seeded into the local project by initialization.

- **Practitioners see** a clean `skills/` directory at the plugin root. The plugin discovers skills there. No ambiguity about where skills live vs where instructions live.
- **Project-local procedures** such as WRITING, review system docs, and fix instructions are created in the user's own `kb/instructions/` by init.
- **Framework vs local distinction is by type dependency, not by directory.** All skills ship via the plugin. Framework skills work out of the box (core types installed). Local skills are discoverable but error gracefully until their type templates are installed.
- **Framework skills:** `write`, `connect`, `validate`, `snapshot-web`, `ingest`, `convert`, `revise-iterative` — depend only on core types (`note`, `text`, `index`, `source-review`).
- **Local skills:** `review-related-system` — depends on `related-system` type. Discoverable via plugin but errors with "type not found" until the practitioner copies the type template.

### Platform support

| | Claude Code | Codex |
|---|---|---|
| Plugin manifest | `.claude-plugin/plugin.json` | `.codex-plugin/plugin.json` |
| Optional catalog entry | N/A | Host repo `.agents/plugins/marketplace.json` |
| Skill invocation | `/commonplace:write` | `$commonplace-write` (or similar) |
| Control plane | `CLAUDE.md` | `AGENTS.md` |
| Skill format | Same `SKILL.md` | Same `SKILL.md` |

One set of SKILL.md files works on both. Only the packaging wrapper differs.

### Codex compatibility

Codex has a local plugin system that expects `.codex-plugin/plugin.json` at the plugin root. The plan must create **both** manifests:
- `.claude-plugin/plugin.json` for Claude Code
- `.codex-plugin/plugin.json` for Codex

Both point to the same `skills/` directory. The SKILL.md format is identical; only the manifest wrapper differs.

Codex also has an optional marketplace/catalog layer for UI ordering and install metadata. For now, local marketplace wiring is primarily a dogfooding concern for this repo. Consumer plugin distribution should be treated as a separate packaging/distribution problem from project initialization.

Minimal marketplace entry shape for dogfooding from a local checkout:

```json
{
  "name": "local-commonplace",
  "interface": {
    "displayName": "Local Commonplace Plugins"
  },
  "plugins": [
    {
      "name": "commonplace",
      "source": {
        "source": "local",
        "path": "./"
      },
      "policy": {
        "installation": "AVAILABLE",
        "authentication": "ON_INSTALL"
      },
      "category": "Productivity"
    }
  ]
}
```

Consumer install should not depend on a local `./commonplace` path.

## Current AGENTS.md.template — section-by-section disposition

### STAYS in template (always-loaded)

| Section | Why it must stay | Change needed |
|---|---|---|
| **KB Goals** (Purpose, Domain, Include/Exclude, Quality bar) | Cross-cutting scoping. Agent needs this to decide "does this belong in the KB?" before any skill fires. Scoping decisions [degrade silently](../../kb/notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md) without always-loaded Goals. | Keep inlined — the practitioner fills this in at install. |
| **KB exists pointer** | Agent must know `kb/` exists and is searchable. Skill trigger matching is unreliable for natural language — without this, "what did we decide about X?" never reaches the KB. | New — currently implicit, needs a short explicit section |
| **Skill reference** | Agent needs to know which skills are available for KB work. | New — replace routing table with a compact skill list using namespaced names |
| **Key Indexes** | Entry points for navigation when searching the KB. | Slim down — just the paths |

### Goals are always-loaded

KB Goals live in the control-plane file (CLAUDE.md / AGENTS.md), inlined in the template section the practitioner fills in at install. The agent sees them every turn. Skills don't need to read a separate file — Goals are already in context.

No `kb/GOALS.md` as a separate file. One location, no sync problem, no competing homes.

### MOVES to `/commonplace:write` skill

| Section | Current location | Notes |
|---|---|---|
| **Routing table** (12 rows) | Template | The core of `write`: map intent → directory + type template |
| **Content workflow** (5 steps) | Template | Becomes `write`'s procedure: search first → read WRITING.md → read type → write → connect |
| **Type routing** (text vs note vs specialized) | Template | Part of `write`'s routing logic |
| **Escalation boundary**: "cannot map artifact through routing table" | Template | Becomes `write`'s fallback: read WRITING.md |
| **Escalation boundary**: "editing in directory with local types/" | Template | `write` reads type templates as part of its routing |
| **Escalation boundary**: "artifact doesn't fit KB Goals" | Template | `write` checks fit against Goals (already in context) |

### MOVES to relevant existing skills

| Section | Current location | Destination skill |
|---|---|---|
| **Escalation boundary**: "touch sources without .ingest.md" | Template | `ingest` — already handles this |
| **Escalation boundary**: "task is review work" | Template | Future: promote review to a skill |
| **Escalation boundary**: "task is fixing review warnings" | Template | Future: promote fix to a skill |

### MOVES to WRITING.md

| Section | Current location | Notes |
|---|---|---|
| **Conventions** (links, filenames, frontmatter) | Template | WRITING.md already covers links and frontmatter. Add filename convention. |
| **Methodology reference** | Template | If we seed methodology notes locally, point to local `kb/notes/` or `kb/instructions/` entry points instead of `commonplace/kb/...`. |

### STAYS but slimmed

| Section | Change |
|---|---|
| **Search patterns** (3 of 4 stay) | Keep the three structural patterns (search by description, by type, by tag) — they teach the agent that frontmatter fields are searchable axes. Drop the plain keyword search. `rg` (ripgrep) is a system dependency — document in INSTALL.md prerequisites alongside git and python3. |

### DROPS entirely

| Section | Why |
|---|---|
| **"No wiki-links"** convention | Already enforced by WRITING.md's link format |
| **Git conventions** | Not the template's concern — each project has its own git rules |

## Resulting template

One template. Goals are inlined in the always-loaded context because the agent needs scope every turn — without it, scoping decisions [degrade silently](../../kb/notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md). This costs some context budget in embedded-KB projects, but correct scoping is worth the cost. ~50 lines; Goals + skill reference + key indexes.

See [AGENTS.md.template.draft](./AGENTS.md.template.draft) for the current draft.

## New artifacts to create

### 1. Plugin manifests
- `.claude-plugin/plugin.json` — Claude Code plugin manifest
- `.codex-plugin/plugin.json` — Codex local plugin manifest

Both declare the plugin name, description, and let their respective plugin systems discover `skills/`.

Codex marketplace metadata is a separate concern:
- It is **not** part of the plugin payload.
- This repo can ship a repo-local `.agents/plugins/marketplace.json` for dogfooding, pointing to `./`.
- Consumer plugin distribution should not assume a local `./commonplace` checkout; that packaging path still needs a concrete distribution story.

### 2. `skills/write/SKILL.md`
The main new skill. Absorbs routing table + content workflow + type routing.

**Type system context:** Types define required structure (sections, fields); traits route semantic review expectations. Type definitions are two files: `.md` (prose template, read by agents) and `.yaml` (machine-readable, read by validator). The `write` skill reads prose templates; the validator reads YAML. See `kb/work/type-system-rationalization/design.md`.

**Procedure:**
1. Parse arguments: optional type and optional topic
2. Check fit against KB Goals (already in context — always-loaded)
3. Search first — find related notes before writing
4. Route to directory and resolve type template. Core types are hardcoded:
   - `note` (default) → `kb/notes/`, base template from WRITING.md
   - `text` → `kb/notes/`, no template (raw capture)
   - `index` → `kb/notes/`, read `kb/notes/types/index.md`
   - `source-review` → `kb/sources/`, read `kb/sources/types/source-review.md`
   - Any other type → scan `kb/*/types/` for `{type}.md`. If the template exists, read it for the target directory and writing guidance. If not found, error with the list of available types (core + discovered).
5. Read WRITING.md for checklist (title-as-claim test, description quality, composability)
6. Set appropriate traits in frontmatter based on content:
   - Claim-shaped title → add `title-as-claim` to `traits:`
   - Contains comparison → add `has-comparison`
   - References external sources → add `has-external-sources`
   - Defines a term → add `definition`
7. Write the note
8. Run `/commonplace:validate`
9. Prompt: "Run /commonplace:connect to link this note?"

**Trigger:** `/commonplace:write`, `/commonplace:write [type]`, `/commonplace:write [type] [topic]`

### 3. Move existing skills to `skills/`
Move **framework** skill directories from `kb/instructions/` to `skills/`:
- `kb/instructions/validate/` → `skills/validate/`
- `kb/instructions/connect/` → `skills/connect/`
- `kb/instructions/ingest/` → `skills/ingest/`
- `kb/instructions/snapshot-web/` → `skills/snapshot-web/`
- `kb/instructions/convert/` → `skills/convert/`
- `kb/instructions/revise-iterative/` → `skills/revise-iterative/`

Skills that stay in `kb/instructions/` (local, not in plugin):
- `kb/instructions/review-related-system/` — depends on `related-system` local type
- `kb/instructions/evaluate-scenarios/` — internal to this repo's methodology

Non-skill instructions stay in `kb/instructions/`:
- WRITING.md, REVIEW-SYSTEM.md, FIX-SYSTEM.md
- review-gates/, fix-warnings/
- Plain .md instruction files (run-review-bundle-on-note.md, etc.)

### 4. Update skill internal references
Skills currently reference `kb/instructions/WRITING.md` and other paths relative to their old location. After moving to `skills/`, these paths need updating. Also, skills that invoke other skills by name need the `commonplace:` prefix.

### 5. Conventions in WRITING.md
Add filename convention: "Lowercase, hyphens for spaces, `.md` extension. Derived from the `# Title` heading."

WRITING.md currently says "see the Knowledge System section in root CLAUDE.md" for routing — update this to reference the `/commonplace:write` skill instead.

### 6. Slim template
The new AGENTS.md.template shown above.

### 7. Updated INSTALL.md

`INSTALL.md` should be rewritten around project initialization, not vendoring and copying by hand.

Target user flow:

**Claude Code / Codex alike:**

```bash
# 1. Install the Commonplace Python package
<package install command>

# 2. Install the Commonplace plugin
<plugin install step>

# 3. Initialize the local project tree
commonplace-init
```

`commonplace-init` is responsible for creating the local KB structure and seeding starter files. `INSTALL.md` should explain:

- prerequisites
- package installation
- plugin installation
- `commonplace-init`
- how to rerun init safely
- how to customize generated files after initialization

## Migration steps (ordered)

1. **Make type routing extensible via dynamic discovery.** `/write` should support practitioner-defined types without hardcoding them. Core seeded types can be treated as always present after `commonplace-init`; additional types should be discovered from local `kb/*/types/`.
2. **Promote `index` and `source-review` to seeded core types.** These should be part of the default local project scaffold rather than optional copy steps.
3. **Create plugin manifests** — `.claude-plugin/plugin.json` and `.codex-plugin/plugin.json`.
4. **Create `skills/` directory and move skill subdirectories** from `kb/instructions/` to `skills/`.
5. **Update internal references** in moved skills so they call packaged commands and local project paths, not vendored framework paths.
6. **Create `skills/write/SKILL.md`** — the new routing skill using dynamic local type discovery.
7. **Add filename convention to WRITING.md** and align WRITING with the skill-driven workflow.
8. **Package operational scripts** under `src/commonplace/` with CLI entry points.
9. **Add scaffold assets** to the Python package and implement `commonplace-init`.
10. **Create slim AGENTS.md.template** for local project initialization.
11. **Rewrite INSTALL.md** around plugin install + Python package + `commonplace-init`.
12. **Test install into a fresh repo.** Start with a blank repo, install the package and plugin, run `commonplace-init`, and verify:
    - the local KB tree is created correctly
    - plugin skills are discoverable
    - packaged commands are on PATH
    - `/commonplace:write` creates a note with correct frontmatter in local `kb/notes/`
    - `/commonplace:write index` creates an index
    - `/commonplace:validate` passes on the created notes
    - `/commonplace:connect` finds and links related notes
    - `/commonplace:ingest` snapshots a URL and writes a source-review
    - rerunning `commonplace-init` is safe

13. **Dogfood the one-tree setup** in real work:
    - slim CLAUDE.md / AGENTS.md to Development + Git + KB Goals only
    - verify note writing, ingestion, connection, validation, review sweeps
    - verify day-to-day KB work works without a vendored `commonplace/` subtree
    - live with the restructured layout before declaring migration complete

## Open questions

- **`.claude-plugin/plugin.json` format** — confirmed: only `name` is required. Optional: `version`, `description`, `author`, `homepage`, `repository`, `license`, `keywords`. Component paths (`skills`, `commands`, `hooks`, `mcpServers`) default to conventional directories at plugin root.
- **`/commonplace:write` vs `/commonplace:write-note`** — one skill with arguments or several? Leaning one with arguments for simpler installation.
- **Related system reviews** — ships via the plugin (all skills in `skills/`). Depends on `related-system` type, which is local. Discoverable but errors gracefully until the practitioner copies the type template.
- **Tasks** — no skill for task creation yet. Tasks don't have frontmatter and live in `kb/tasks/`. Different enough to defer.
- **Review/Fix promotion** — promote REVIEW-SYSTEM.md and FIX-SYSTEM.md to skills? They're complex enough, but adds to the skill count. Defer until after initial migration.
- **Log entries** — "append to kb/log.md" is too simple for a skill. Mention in WRITING.md and in `write` skill's "for quick observations" section.
- **Codex consumer plugin distribution** — local marketplace dogfooding is understood, but the consumer distribution path for the plugin still needs a concrete answer.
- **`commonplace-init` overwrite policy** — prompt, never overwrite, or support `--force` / `--dry-run`?
- **Methodology seeding** — should init seed only operational instructions and core types, or also a curated starter set of methodology notes?
