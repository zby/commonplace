# Plan: plugin packaging + slim template

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
  plugin.yml                    # Claude Code plugin manifest
  skills/                       # Plugin skills (discovered automatically)
    write/SKILL.md
    connect/SKILL.md
    validate/SKILL.md
    ingest/SKILL.md
    snapshot-web/SKILL.md
    review-related-system/SKILL.md
    convert/SKILL.md
    revise-iterative/SKILL.md
  kb/                           # Methodology content + operational artifacts
    notes/                      # Methodology notes (this repo's own KB)
    sources/
    work/
    instructions/               # Non-skill instructions (WRITING.md, REVIEW-SYSTEM.md, etc.)
      WRITING.md
      REVIEW-SYSTEM.md
      FIX-SYSTEM.md
      review-gates/
      fix-warnings/
  types/                        # Type definitions (copied during init)
  scripts/                      # Utility scripts
  AGENTS.md.template            # Slim control-plane template
  INSTALL.md                    # Installation guide
```

Key change: **skills move from `kb/instructions/*/` to `skills/`** at the repo root. This is the plugin convention — the plugin system discovers skills from the `skills/` directory. Non-skill instructions (WRITING.md, review gates, fix strategies) stay in `kb/instructions/`.

### Platform support

| | Claude Code | Codex |
|---|---|---|
| Plugin manifest | `plugin.yml` | marketplace / `.agents/` |
| Skill invocation | `/commonplace:write` | `$commonplace-write` (or similar) |
| Control plane | `CLAUDE.md` | `AGENTS.md` |
| Skill format | Same `SKILL.md` | Same `SKILL.md` |

One set of SKILL.md files works on both. Only the packaging wrapper differs.

### Codex compatibility

Codex also has a plugin system (v0.110.0+) with marketplace distribution. For users not using plugins, the fallback is symlinking into `.agents/skills/` — same as today but with the new `skills/` source directory. Codex discovers skills by walking `.agents/skills/` from cwd up to repo root, so the layout works.

## Current AGENTS.md.template — section-by-section disposition

### STAYS in template (always-loaded)

| Section | Why it must stay | Change needed |
|---|---|---|
| **KB Goals** (Purpose, Domain, Include/Exclude, Quality bar) | Cross-cutting scoping. Agent needs this to decide "does this belong in the KB?" before any skill fires. | None — keep as-is |
| **KB exists pointer** | Agent must know `kb/` exists and is searchable. Skill trigger matching is unreliable for natural language — without this, "what did we decide about X?" never reaches the KB. | New — currently implicit, needs a short explicit section |
| **Skill reference** | Agent needs to know which skills are available for KB work. | New — replace routing table with a compact skill list using namespaced names |
| **Key Indexes** | Entry points for navigation when searching the KB. | Slim down — just the paths |
| **Git conventions** | About repo workflow, not KB. Stays because it's project-level. | Keep as-is |

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

## Resulting template

```markdown
# {{project_name}} Knowledge Base

<!-- One sentence: what this KB is and who it serves. -->

## KB Goals

### Purpose
<!-- What decisions or actions does this KB support? Who uses it? -->

### Domain
<!-- Scope boundary. Be specific enough that an agent can decide "does this belong?" -->

### Include
-
-

### Exclude
-
-

### Quality bar
<!-- When is knowledge worth a note vs. a log entry vs. nothing? -->

## Using the KB

The knowledge base lives in `kb/`. Search it when the user asks about decisions, reasoning, design rationale, or project knowledge.

```bash
rg "keyword" kb/notes/ --glob "*.md"
```

Key entry points:
- `kb/notes/index.md` — directory listing of all notes

<!-- Add tag indexes here as they emerge -->

### Skills

| Task | Skill |
|---|---|
| Write a note, ADR, or structured claim | `/commonplace:write` |
| Connect a note to related notes | `/commonplace:connect` |
| Validate note structure | `/commonplace:validate` |
| Snapshot an external URL | `/commonplace:snapshot-web` |
| Ingest and analyze a source | `/commonplace:ingest` |
| Review a related system | `/commonplace:review-related-system` |
| Convert between note types | `/commonplace:convert` |

For the full writing checklist and conventions, see `commonplace/kb/instructions/WRITING.md`.

## Git

- **Never `git add -A`** — review `git status` and stage specific files.
- **Prefer atomic stage+commit** — combine staging and committing in one command.
```

~45 lines filled in vs ~160 currently. KB Goals is the only part the user writes.

## New artifacts to create

### 1. `plugin.yml`
Claude Code plugin manifest. Declares the plugin name, description, and lets the plugin system discover `skills/`.

### 2. `skills/write/SKILL.md`
The main new skill. Absorbs routing table + content workflow + type routing.

**Procedure:**
1. Parse arguments: optional type (note, structured-claim, adr, index), optional topic
2. Read `kb/GOALS.md` if it exists — check fit
3. Search first — find related notes before writing
4. Route to directory based on type:
   - `note` (default) → `kb/notes/`
   - `structured-claim` → `kb/notes/`
   - `adr` → `kb/notes/adr/`
   - `index` → `kb/notes/`
5. Read the relevant type template from `kb/notes/types/` (if not default note)
6. Read WRITING.md for checklist
7. Write the note
8. Run `/commonplace:validate`
9. Prompt: "Run /commonplace:connect to link this note?"

**Trigger:** `/commonplace:write`, `/commonplace:write [type]`, `/commonplace:write [type] [topic]`

### 3. Move existing skills to `skills/`
Move skill directories from `kb/instructions/` to `skills/`:
- `kb/instructions/validate/` → `skills/validate/`
- `kb/instructions/connect/` → `skills/connect/`
- `kb/instructions/ingest/` → `skills/ingest/`
- `kb/instructions/snapshot-web/` → `skills/snapshot-web/`
- `kb/instructions/review-related-system/` → `skills/review-related-system/`
- `kb/instructions/convert/` → `skills/convert/`
- `kb/instructions/revise-iterative/` → `skills/revise-iterative/`
- `kb/instructions/evaluate-scenarios/` → `skills/evaluate-scenarios/`

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

# 3. Create kb/ structure
mkdir -p kb/notes/types kb/sources/types kb/tasks/{backlog,active} kb/work
cp commonplace/kb/instructions/WRITING.md kb/instructions/WRITING.md
cp commonplace/types/* types/
cp commonplace/kb/notes/types/* kb/notes/types/
cp commonplace/kb/sources/types/* kb/sources/types/

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

# 3. Create kb/ structure (same as above)

# 4. Add KB section to AGENTS.md
cat commonplace/AGENTS.md.template >> AGENTS.md
```

Step 2 is the big simplification — one command replaces the symlink loop + directory creation.

## Migration steps (ordered)

1. **Create `plugin.yml`** — minimal plugin manifest
2. **Create `skills/` directory and move skill subdirectories** from `kb/instructions/`
3. **Update internal references** in moved skills (paths, cross-skill invocations)
4. **Create `skills/write/SKILL.md`** — the new routing skill
5. **Add filename convention to WRITING.md** + update WRITING.md's reference to CLAUDE.md routing
6. **Update `.claude/skills/` symlinks** in this repo to point to new `skills/` location
7. **Create slim AGENTS.md.template**
8. **Slim this repo's AGENTS.md** to use the new template format
9. **Update INSTALL.md** with plugin-based procedure
10. **Test** — install into a fresh test repo, verify skills work with namespace prefix

## This repo: dogfooding

This repo installs its own plugin (or symlinks from `skills/`). The AGENTS.md shrinks to:
- KB Goals (for the commonplace methodology KB)
- Using the KB section (pointer + skill list)
- Development conventions (python3, uv, YAGNI)
- Git conventions

Vocabulary section drops — already in `kb/notes/definitions/`, referenced by WRITING.md.

## Open questions

- **`plugin.yml` format** — need to verify the exact schema. Research done so far confirms the approach but not the specific fields.
- **`/commonplace:write` vs `/commonplace:write-note`** — one skill with arguments or several? Leaning one with arguments for simpler installation.
- **Related system reviews** — keep as separate `commonplace:review-related-system` skill (complex workflow) or fold into `write`? Keep separate.
- **Tasks** — no skill for task creation yet. Tasks don't have frontmatter and live in `kb/tasks/`. Different enough to defer.
- **Review/Fix promotion** — promote REVIEW-SYSTEM.md and FIX-SYSTEM.md to skills? They're complex enough, but adds to the skill count. Defer until after initial migration.
- **Log entries** — "append to kb/log.md" is too simple for a skill. Mention in WRITING.md and in `write` skill's "for quick observations" section.
- **validate_notes.py** — moves with its skill to `skills/validate/`. The `REPO_ROOT` computation (`Path(__file__).resolve().parents[3]`) needs adjusting since the path depth changes from `kb/instructions/validate/` (depth 3) to `skills/validate/` (depth 2).
- **Evaluate-scenarios** — internal to this repo's methodology, not general KB operation. Stays in `kb/instructions/evaluate-scenarios/` as a repo-local skill, not part of the plugin.
