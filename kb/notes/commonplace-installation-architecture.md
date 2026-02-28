---
description: Design for how commonplace installs into a project — two trees (user's kb/ and framework's commonplace/), operational artifacts copied for prompt simplicity, methodology referenced for deeper reasoning
type: note
traits: []
areas: [claw-design]
status: seedling
---

# Commonplace installation architecture

When a project adopts commonplace, two directory trees coexist at the project root:

- `kb/` — the user's knowledge base. Contains their notes, sources, tasks. Tracked in the project's git.
- `commonplace/` — the framework. Contains methodology, claw design theory, type definitions, writing guide, skill templates, scripts. A git submodule or a gitignored clone.

The install step copies **operational artifacts** into `kb/` and renders skills into `.claude/skills/`. Methodology stays in `commonplace/` and is consulted on demand.

## Design motivation: optimizing read and write

The kb has two fundamental operations — **read** (find and retrieve knowledge) and **write** (create or update documents). The layout optimizes both by minimizing the instructions the agent needs and the tool calls (hops) required.

### Write path

Writing a document requires: (1) know where to put it, (2) know what structure is expected, (3) know how to write well, (4) write the file.

| Step | What the agent does | Hops | How the layout helps |
|------|-------------------|------|---------------------|
| Route | Consult CLAUDE.md routing table | 0 | Always loaded — no tool call needed |
| Structure | Read `kb/notes/types/` | 1 | Types are in the same tree as the target — predictable path |
| Conventions | Read `kb/WRITING.md` | 1 | Same tree, one fixed location |
| Write | Create file in `kb/notes/` | 1 | Direct write, no indirection |

**Common case: 3 hops, all within `kb/`.** If types or WRITING.md lived in `commonplace/`, hop count stays the same but the instructions grow: the agent needs to know which tree to read from, and the CLAUDE.md routing gets more complex ("for types, look in commonplace; for content, write to kb").

**Uncommon case: methodology fallback during write.** Sometimes the operational artifacts don't cover the judgment call. The skill says "use link semantics" but the agent isn't sure which semantic fits, or WRITING.md says "title as claim" but the document is a borderline case between single-claim and multi-claim. The agent then reads methodology from `commonplace/kb/notes/` — one extra search hop to a different scope. This is the write path escalating: route → types → WRITING → **methodology** → write.

The layout optimizes for the common case (stay in `kb/`) while keeping the fallback accessible (search `commonplace/kb/`). The escalation is explicit — the agent decides she needs more context and goes looking for it — not a resolution chain she must always follow.

### Read path

Reading has two cases: **project knowledge** (common) and **methodology** (rare fallback).

**Common case — project knowledge:**

| Step | What the agent does | Hops |
|------|-------------------|------|
| Search | `rg` or `qmd` across `kb/` | 1 |
| Read | Open the matching file | 1 |
| Follow links | Links are relative, within `kb/` | 1 per link |

**Rare case — methodology fallback:**

When the agent hits an edge case a skill doesn't cover, she searches `commonplace/kb/notes/` for deeper reasoning. This adds one search hop to a different scope. The CLAUDE.md routing tells her when: "for why things work this way, search `commonplace/kb/`."

**Why two trees beat one for reads.** If methodology were mixed into `kb/`, every search would return both project notes and framework notes. The agent would need instructions to distinguish them ("ignore notes with `source: commonplace` in frontmatter" or "filter by directory"). More results, more filtering logic, more instructions. Separating the trees makes the common-case search scope clean: `kb/` is only the user's content. The methodology tree is searched explicitly and only when needed.

### The principle

Both read and write have the same shape: a fast common path within `kb/`, and an explicit escalation to `commonplace/kb/` when the agent needs deeper reasoning. The layout optimizes the common path (one tree, predictable locations, no resolution logic) while keeping the fallback one hop away. The agent never follows a resolution chain — she either works in `kb/` or explicitly decides to consult methodology.

## What gets copied vs what stays

The boundary: **copy what the agent reads on the hot path, reference what she consults as fallback.**

| Artifact | Destination | Rationale |
|----------|-------------|-----------|
| Directory structure | `kb/` (empty dirs) | User needs somewhere to put content |
| Global types (`types/`) | `types/` | Agent reads for base type definitions (text, note) — at repo root for cross-collection visibility |
| Collection types (`kb/*/types/`) | `kb/*/types/` | Agent reads constantly during creation and validation — one lookup location, no cross-tree resolution |
| WRITING.md | `kb/WRITING.md` | Agent reads when creating any content — must be in the same tree |
| Methodology notes | stays in `commonplace/kb/notes/` | Fallback for edge cases where skills don't cover enough |
| Source snapshots | stays in `commonplace/kb/sources/` | Reference material for the methodology |
| Skill templates | rendered to `.claude/skills/` | Agent needs concrete skills, not templates |
| Scripts | stays in `commonplace/scripts/` | Run from there, no need to copy |

## Why copy operational artifacts instead of reading cross-tree

The alternative — keeping types and WRITING.md in `commonplace/` and having the agent read them from there — requires the agent to understand a cross-tree resolution order ("look in kb/ first, fall back to commonplace/"). This is trivial in code but adds friction in prompts. Every instruction that says "read the types" would need to specify which tree, or explain the fallback logic.

Copying eliminates this: the agent sees `kb/notes/types/` and reads it. One location, no indirection. The prompt stays simple.

Types are separate files, so upgrading is natural: the install script replaces commonplace-provided type files (identified by a `source: commonplace` marker or a manifest) and leaves user-added type files untouched. WRITING.md is a single file — upgrading shows a diff the user can review.

## Why keep methodology as reference instead of copying

Methodology notes are the reasoning behind the operational artifacts. The agent doesn't need them for routine work — [skills derive from methodology through distillation](./skills-derive-from-methodology-through-distillation.md) and handle the common cases. But distillation is not lossless: when the agent hits an edge case the skill doesn't cover, she needs the full reasoning. That's why [agent statelessness makes skill layers architectural](./agent-statelessness-makes-skill-layers-architectural-not-pedagogical.md) — the methodology is permanent infrastructure the agent returns to, not a learning aid she graduates from.

Keeping methodology in `commonplace/` rather than copying it:
- Gives the user clean ownership: everything in `kb/` is theirs
- Makes upgrades trivial: update the submodule or pull the clone
- Avoids interleaving framework notes with project notes — the user has good visibility of their own content

## Commonplace repo layout

The commonplace GitHub repo is itself a claw — it uses its own knowledge system to document the methodology for building claws.

```
commonplace/                             ← the GitHub repo
    types/                               ← global types (text, note)
    kb/                                  ← commonplace's own knowledge base
      WRITING.md                         ← writing conventions (canonical source)
      notes/
        types/                           ← note types (structured-claim, etc.)
        agent-learnings/
        related-systems/
        research/
        meta/
        *.md                             ← all methodology and theory notes
      sources/
        types/                           ← source types (source-review, etc.)
        *.md                             ← reference material (Willison, Karpathy, Toulmin, etc.)
      tasks/
        types/                           ← task types
        backlog/
        active/
        completed/
    skills/                              ← skill templates + install script
    scripts/                             ← standalone tools (index generation, topic sync, etc.)
    .claude/skills/                      ← rendered skills for commonplace's own use
    CLAUDE.md                            ← commonplace's own instructions
    LICENSE                              ← CC BY 4.0
    README.md
```

In the commonplace repo itself, there is no separation between "user content" and "methodology" — the methodology IS the content. The two-tree split (user's `kb/` vs framework's `commonplace/`) only emerges when commonplace is installed into another project.

In llm-do, `claw-design/` exists as a separate directory from `notes/` because llm-do has notes about many topics (runtime design, approval system, etc.) and claw design is just one. In commonplace, everything is claw design — a separate directory would be redundant. Subdirectories within `notes/` (like `research/`, `meta/`) provide sufficient organization.

## Installed project layout

```
my-project/
    types/                           ← copied from commonplace (global types)
    kb/                              ← user's content (project git)
      WRITING.md                     ← copied from commonplace
      notes/
        types/                       ← copied from commonplace
        agent-learnings/
      sources/
        types/                       ← copied from commonplace
      tasks/
        types/                       ← copied from commonplace
    commonplace/                     ← framework (submodule or gitignored clone)
      types/                         ← global types (canonical source)
      kb/
        WRITING.md                   ← canonical source
        notes/
          types/
          ...methodology notes...
        sources/
          types/
          ...reference material...
        tasks/
          types/
      skills/                        ← skill templates
      scripts/
    .claude/skills/                  ← rendered from commonplace/skills/
    CLAUDE.md                        ← includes generated routing fragment
```

## The CLAUDE.md fragment

The install step generates a Knowledge System section for the project's CLAUDE.md with:

- Routing table pointing to `kb/` for content creation ("where things go")
- Reference to `commonplace/kb/` for methodology ("why things work this way")
- Search patterns for both trees
- Skill descriptions

## Inclusion mechanism

Two supported approaches:

- **Git submodule**: reproducible, versioned. Setup: `git submodule add <url> commonplace`. Update: `git submodule update --remote`.
- **Clone + gitignore**: simpler. Setup: `git clone <url> commonplace` + add `commonplace/` to `.gitignore`. Update: `cd commonplace && git pull`.

Both produce a stable `commonplace/` directory at the project root. The install script checks for its presence.

## Types architecture

Types are directory-scoped, not global. Each collection (notes, sources, tasks) has its own `types/` subdirectory defining the structural expectations for documents in that collection.

Global types (the maturity ladder: `text` and `note`) are defined in `types/` at the repo root. Collection-specific types (structured-claim, source-review, task types) are defined in `kb/<collection>/types/`.

Types in a collection's `types/` directory apply to the entire collection, including its subdirectories (e.g., `notes/types/` covers `notes/related-systems/` and `notes/research/`). No separate types mechanism per partition — if a partition needs distinct structural expectations, they go in the partition's README as prose.

User customization: users can add type files to their `kb/*/types/` directories. On upgrade, commonplace-provided types are replaced; user-added types are left untouched.

## Naming: why `kb/` not `memory/`

The agentic ecosystem converges on "memory" for persistent agent state: OpenClaw uses `~/.openclaw/workspace/memory/`, Claude Code uses `~/.claude/projects/.../memory/`. The term is intuitive — "the agent's memory" is more natural than "the agent's knowledge base."

However, Claude Code already uses `memory/` for its own auto-memory directory at `~/.claude/projects/<project>/memory/`. That system is per-user, outside the repo, and serves a different purpose (personal preferences and session-spanning notes). Commonplace's directory is in-repo, checked into git, and shared across all users of the project. Using the same name for both would create ambiguity: "which memory?" — the user's personal Claude memory, or the project's shared knowledge base?

`kb/` is less evocative but unambiguous. No existing tool claims that name in the project root.

---

Relevant Notes:
- [extracting the claw system into its own repo](../notes/extract-kb-as-standalone-project.md) — parent plan: what moves vs what stays, naming, license; this note refines the installation architecture
- [skills derive from methodology through distillation](./skills-derive-from-methodology-through-distillation.md) — foundation: why methodology must remain accessible — distillation is lossy, and the agent needs the full reasoning for edge cases
- [agent statelessness makes skill layers architectural](./agent-statelessness-makes-skill-layers-architectural-not-pedagogical.md) — foundation: methodology is permanent infrastructure the agent returns to, not a learning progression
- [directory-scoped types are cheaper than global types](./directory-scoped-types-are-cheaper-than-global-types.md) — enables: the per-collection types/ directories implement the directory-scoped types proposal
- [context loading strategy](./context-loading-strategy.md) — constrains: the CLAUDE.md fragment must integrate into the loading hierarchy
- [generate instructions at build time](./generate-instructions-at-build-time.md) — enables: the install step that renders skills and copies operational artifacts
- [why directories despite their costs](./why-directories-despite-their-costs.md) — informs: the collection/partition distinction and the two-level types nesting limit

Topics:
- [claw-design](./claw-design.md)
