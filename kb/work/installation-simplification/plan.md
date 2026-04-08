# Plan: plugin packaging + slim template

## Scope

This plan is about the **AGENTS.md.template** — the control-plane file shipped to users who install commonplace into their projects. It is not about this repo's own AGENTS.md, which has additional repo-specific content (development conventions, git rules, vocabulary, etc.) that other projects would define for themselves.

## Principle

Always-loaded content should be limited to what the agent needs to **discover** the KB and **decide to use** it. Everything about **how to operate** the KB moves into skills that load on demand. Skills are distributed as a **plugin** for automatic namespacing and one-step installation.

## Distribution: plugin packaging

### Why plugins, not symlinks

- **Namespacing** — plugins get automatic `commonplace:write` namespacing, preventing collisions with project-specific skills. Symlinks require manual prefix hacks.
- **One-step install** — install the plugin, done. No symlink loops, no directory creation scripts.
- **Symlink reliability** — the `/skills` command may not follow symlinks reliably.
- **Cross-platform** — both Claude Code and Codex have plugin systems. The SKILL.md format is the same; only the packaging wrapper differs.

### Plugin structure

```
commonplace/
  .claude-plugin/
    plugin.json                 # Claude Code plugin manifest
  .codex-plugin/
    plugin.json                 # Codex local plugin manifest
  skills/                       # Framework skills (depend only on core types)
    write/SKILL.md
    connect/SKILL.md
    validate/SKILL.md
    snapshot-web/SKILL.md
    ingest/SKILL.md
    convert/SKILL.md
    revise-iterative/SKILL.md
  kb/                           # Methodology content + operational artifacts
    notes/                      # Methodology notes (this repo's own KB)
    sources/
    work/
    instructions/               # Non-skill instructions + local skills
      WRITING.md
      REVIEW-SYSTEM.md
      FIX-SYSTEM.md
      review-gates/
      fix-warnings/
      review-related-system/SKILL.md  # Local skill — depends on related-system type
  types/                        # Base type definitions: .md (prose) + .yaml (machine-readable)
  scripts/                      # Utility scripts
  AGENTS.md.template            # Slim control-plane template
  INSTALL.md                    # Installation guide
```

Key changes:
- **Skills split into framework and local.** Framework skills (in `skills/`) depend only on core types (`note`, `text`, `index`) and are discovered by the plugin system. Local skills (in `kb/instructions/`) depend on our local types and are only available in this repo (or to practitioners who explicitly adopt those types and symlink the skills).
- **Framework skills:** `write` (routes to `note` by default), `connect` (searches notes by description), `validate` (checks any type's frontmatter), `snapshot-web` (writes to `kb/sources/`, no type dependency), `ingest` (snapshots external sources and writes `.ingest.md` using `source-review` type — ingestion is a basic KB operation, not domain-specific), `convert` (text→note, core types only), `revise-iterative` (works on any note).
- **Local skills:** `review-related-system` (writes `related-system` type notes — specific to our practice of comparing knowledge systems). Only makes sense if the practitioner has the corresponding local type installed.

### Platform support

| | Claude Code | Codex |
|---|---|---|
| Plugin manifest | `.claude-plugin/plugin.json` | marketplace / `.agents/` |
| Skill invocation | `/commonplace:write` | `$commonplace-write` (or similar) |
| Control plane | `CLAUDE.md` | `AGENTS.md` |
| Skill format | Same `SKILL.md` | Same `SKILL.md` |

One set of SKILL.md files works on both. Only the packaging wrapper differs.

### Codex compatibility

Codex has a local plugin system that expects `.codex-plugin/plugin.json` at the plugin root. The plan must create **both** manifests:
- `.claude-plugin/plugin.json` for Claude Code
- `.codex-plugin/plugin.json` for Codex

Both point to the same `skills/` directory. The SKILL.md format is identical; only the manifest wrapper differs.

For users not using plugins, the fallback is symlinking into `.agents/skills/` — same as today but with the new `skills/` source directory. Codex discovers skills by walking `.agents/skills/` from cwd up to repo root, so the layout works.

## Current AGENTS.md.template — section-by-section disposition

### STAYS in template (always-loaded)

| Section | Why it must stay | Change needed |
|---|---|---|
| **KB Goals** (Purpose, Domain, Include/Exclude, Quality bar) | Cross-cutting scoping. Agent needs this to decide "does this belong in the KB?" before any skill fires. | **Move to `kb/GOALS.md`** — skills read it on demand. The template includes a one-line pointer: "KB goals and scope are in `kb/GOALS.md`." See "Single source of truth for Goals" below. |
| **KB exists pointer** | Agent must know `kb/` exists and is searchable. Skill trigger matching is unreliable for natural language — without this, "what did we decide about X?" never reaches the KB. | New — currently implicit, needs a short explicit section |
| **Skill reference** | Agent needs to know which skills are available for KB work. | New — replace routing table with a compact skill list using namespaced names |
| **Key Indexes** | Entry points for navigation when searching the KB. | Slim down — just the paths |

### Single source of truth for Goals

KB Goals live in **`kb/GOALS.md`** — one file, one location. The always-loaded template carries only a pointer: "KB goals and scope are in `kb/GOALS.md`." Skills read `kb/GOALS.md` on demand when they need scoping context (e.g., `/write` checks fit before creating a note).

The install step creates `kb/GOALS.md` from a template with commented-out examples. The practitioner fills it in. The always-loaded template does NOT duplicate the goals — it just tells the agent the file exists and where to find it.

This resolves the competing-homes problem: `kb/GOALS.md` is the source of truth; the template is a pointer.

### MOVES to `/commonplace:write` skill

| Section | Current location | Notes |
|---|---|---|
| **Routing table** (12 rows) | Template | The core of `write`: map intent → directory + type template |
| **Content workflow** (5 steps) | Template | Becomes `write`'s procedure: search first → read WRITING.md → read type → write → connect |
| **Type routing** (text vs note vs specialized) | Template | Part of `write`'s routing logic |
| **Escalation boundary**: "cannot map artifact through routing table" | Template | Becomes `write`'s fallback: read WRITING.md |
| **Escalation boundary**: "editing in directory with local types/" | Template | `write` reads type templates as part of its routing |
| **Escalation boundary**: "artifact doesn't fit KB Goals" | Template | `write` reads GOALS.md and checks fit |

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
| **Methodology reference** | Template | Add line: "For deeper reasoning, search `commonplace/kb/notes/`" |

### DROPS entirely

| Section | Why |
|---|---|
| **"No wiki-links"** convention | Already enforced by WRITING.md's link format |
| **Search patterns** (4 grep examples) | Agents know how to grep. WRITING.md has graph utilities. |
| **Git conventions** | Not the template's concern — each project has its own git rules |

## Resulting template

See [AGENTS.md.template.draft](./AGENTS.md.template.draft) — ~35 lines filled in vs ~160 currently. KB Goals is the only part the user writes. Everything else is boilerplate that could be generated by an init skill.

## New artifacts to create

### 1. Plugin manifests
- `.claude-plugin/plugin.json` — Claude Code plugin manifest
- `.codex-plugin/plugin.json` — Codex local plugin manifest

Both declare the plugin name, description, and let their respective plugin systems discover `skills/`.

### 2. `skills/write/SKILL.md`
The main new skill. Absorbs routing table + content workflow + type routing.

**Type system context:** Types define required structure (sections, fields); traits route semantic review expectations. Type definitions are two files: `.md` (prose template, read by agents) and `.yaml` (machine-readable, read by validator). The `write` skill reads prose templates; the validator reads YAML. See `kb/work/type-system-rationalization/design.md`.

**Procedure:**
1. Parse arguments: optional type and optional topic
2. Read `kb/GOALS.md` if it exists — check fit
3. Search first — find related notes before writing
4. Route to directory and resolve type template. Core types are hardcoded:
   - `note` (default) → `kb/notes/`, base template from WRITING.md
   - `text` → `kb/notes/`, no template (raw capture)
   - `index` → `kb/notes/`, read `kb/notes/types/index.md`
   - `source-review` → `kb/sources/`, read `kb/sources/types/source-review.md`
   - Any other type → scan `kb/*/types/` for `{type}.md`. If the template exists, read it for the target directory and writing guidance. If not found, error with the list of available types (core + discovered).
6. Read WRITING.md for checklist (title-as-claim test, description quality, composability)
7. Set appropriate traits in frontmatter based on content:
   - Claim-shaped title → add `title-as-claim` to `traits:`
   - Contains comparison → add `has-comparison`
   - References external sources → add `has-external-sources`
   - Defines a term → add `definition`
8. Write the note
9. Run `/commonplace:validate`
10. Prompt: "Run /commonplace:connect to link this note?"

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

New installation procedure:

**Claude Code:**
```bash
# 1. Add commonplace
git submodule add <url> commonplace

# 2. Install the plugin
claude plugin install ./commonplace

# 3. Create kb/ structure, copy core types, and initialize
mkdir -p kb/notes/types kb/sources/types kb/tasks/{backlog,active} kb/work kb/instructions types
cp commonplace/kb/instructions/WRITING.md kb/instructions/WRITING.md
cp commonplace/templates/GOALS.md kb/GOALS.md        # practitioner fills this in
touch kb/log.md                                       # improvement log
cp commonplace/types/* types/                        # base types (note.md, note.yaml, text.yaml)
# Copy only core types — note, text, index, source-review
for t in note text index; do
  cp commonplace/kb/notes/types/$t.md kb/notes/types/ 2>/dev/null
  cp commonplace/kb/notes/types/$t.yaml kb/notes/types/ 2>/dev/null
done
for t in source-review; do
  cp commonplace/kb/sources/types/$t.md kb/sources/types/ 2>/dev/null
  cp commonplace/kb/sources/types/$t.yaml kb/sources/types/ 2>/dev/null
done
# Other types (adr, structured-claim, related-system, etc.) stay in
# commonplace/ as examples — copy manually if you want them.

# 4. Add KB section to your control-plane file
# Copy the template and fill in KB Goals
cat commonplace/AGENTS.md.template >> CLAUDE.md
```

**Codex:**
```bash
# 1. Add commonplace
git submodule add <url> commonplace

# 2. Install plugin or symlink skills
codex plugin install ./commonplace
# OR: manual symlink fallback
mkdir -p .agents/skills
for skill in commonplace/skills/*/; do
  ln -sfn "$PWD/commonplace/skills/$(basename "$skill")" ".agents/skills/$(basename "$skill")"
done

# 3. Create kb/ structure and copy type definitions (same as above)

# 4. Add KB section to AGENTS.md
cat commonplace/AGENTS.md.template >> AGENTS.md
```

Step 2 is the big simplification — one command replaces the symlink loop.

## Migration steps (ordered)

**Dependency:** The type-system rationalization workshop (`kb/work/type-system-rationalization/`) should land its YAML type definitions (phases 1-2) before this migration, so the install copy step has `.yaml` files to copy and the `write` skill can reference the updated type list. The trait migration (phase 3) and review integration (phase 4) can happen independently.

1. **Make type routing extensible via dynamic discovery.** Currently the routing table in CLAUDE.md hardcodes which types exist and where they route. The `/write` skill must support practitioner-defined types without hardcoding them. Design: core types (`note`, `text`, `index`, `source-review`) are hardcoded in the skill — they're guaranteed to exist after install and this avoids a filesystem scan for the common case. For any type not in the hardcoded set, the skill scans `kb/*/types/` for a matching `.md` template. If found, the template itself declares which collection directory it targets (e.g., `adr.md` declares it writes to `kb/notes/adr/`) — this replaces the hardcoded routing table for local types. If not found, the skill errors with available types listed. This is a prerequisite for everything else — without extensible routing, `/write` can't be a framework skill.

2. **Promote `index` and `source-review` to core types.** Currently these are defined in `kb/*/types/` alongside local types like `adr` and `related-system`, with no distinction. To make them core, we need to:
   - Verify that the `index` type template (`index.md`, `index.yaml`) has no dependencies on local conventions (our specific tags, our specific indexes). It should work for any KB's indexes.
   - Verify that the `source-review` type template works for any external source, not just our ingestion conventions.
   - Move these into `types/` at the repo root alongside `note` and `text` base definitions, if that's where core types live. Or mark them in `kb/*/types/` with a convention that distinguishes core from local — depends on where the type-system-rationalization workshop lands.
   - Ensure validation and the `/write` skill treat these as core types that are always available.
   - Update WRITING.md if it references indexes — confirm it documents the `index` type as part of the base set.

3. **Narrow the install to core types only.** Once `index` and `source-review` are established as core alongside `note` and `text`, change the install copy commands to only copy these four. All other types (`structured-claim`, `adr`, `related-system`, `spec`, `review`, task types) stay in `commonplace/` as examples the practitioner can optionally copy. See [practitioner contract](../system-documentation/practitioner-contract.md) for the full classification.

4. **Create plugin manifests** — `.claude-plugin/plugin.json` and `.codex-plugin/plugin.json`
5. **Create `skills/` directory and move framework skill subdirectories** from `kb/instructions/`. Local skills (`review-related-system`) stay in `kb/instructions/`.
6. **Update internal references** in moved skills (paths, cross-skill invocations)
7. **Create `skills/write/SKILL.md`** — the new routing skill, using dynamic type discovery from step 1
8. **Add filename convention to WRITING.md** + update WRITING.md's reference to CLAUDE.md routing
9. **Update skill symlinks** in this repo — `.claude/skills/`, `.agents/skills/`, and `~/.codex/skills/` (if used) — to point to new `skills/` location instead of `kb/instructions/`
10. **Create slim AGENTS.md.template**
11. **Update INSTALL.md** with plugin-based procedure
12. **Test** — install into a fresh test repo, verify: skills work with namespace prefix, `/write` discovers only core types, `/write adr` fails gracefully until practitioner copies the adr type template

## Open questions

- **`.claude-plugin/plugin.json` format** — confirmed: only `name` is required. Optional: `version`, `description`, `author`, `homepage`, `repository`, `license`, `keywords`. Component paths (`skills`, `commands`, `hooks`, `mcpServers`) default to conventional directories at plugin root.
- **`/commonplace:write` vs `/commonplace:write-note`** — one skill with arguments or several? Leaning one with arguments for simpler installation.
- **Related system reviews** — stays as a local skill in `kb/instructions/`, not in the plugin. Depends on `related-system` type. Practitioners who want it copy the type and symlink the skill manually.
- **Tasks** — no skill for task creation yet. Tasks don't have frontmatter and live in `kb/tasks/`. Different enough to defer.
- **Review/Fix promotion** — promote REVIEW-SYSTEM.md and FIX-SYSTEM.md to skills? They're complex enough, but adds to the skill count. Defer until after initial migration.
- **Log entries** — "append to kb/log.md" is too simple for a skill. Mention in WRITING.md and in `write` skill's "for quick observations" section.
- **validate_notes.py** — moves with its skill to `skills/validate/`. The `REPO_ROOT` computation (`Path(__file__).resolve().parents[3]`) needs adjusting since the path depth changes from `kb/instructions/validate/` (depth 3) to `skills/validate/` (depth 2).
- **Step 3/4 copy commands** — should there be a `/commonplace:init` skill that handles directory creation and artifact copying interactively? Would further reduce installation friction.
