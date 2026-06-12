# Commonplace

**The theory of LLM wikis, running as one.**

Commonplace is a framework for agent-operated knowledge bases — LLM wikis in the sense [Karpathy sketched](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): a persistent, linked markdown layer that AI agents write, navigate, review, and maintain. The framework ships a type system, writing conventions, agent skills, and Python commands for building such a wiki around your own work.

It is **self-hosting**, in the bootstrapping sense. The theory of how to build LLM wikis lives in this repository as notes, and the methodology those notes lay out is executed here, not just described: LLM agents follow it to maintain the very wiki the theory lives in. The skills agents use to write, connect, and validate notes are themselves artifacts in the wiki, written and maintained the same way; the writing conventions govern the very files they are written in. Nothing here is documentation *about* a separate system. The wiki is the system, and reading this repo is watching it run.

**The content is AI-generated** through human-AI collaboration: a human directs the inquiry, and AI agents (Claude, ChatGPT, and others) draft, connect, and maintain the notes.

Rendered notes are available at <https://zby.github.io/commonplace/>. The HTML site is easier to browse than raw Markdown when reading across the KB.

## What's in the box

```
kb/                          Knowledge base
  types/                     Global types (text, note, instruction, definition, index)
  notes/COLLECTION.md         Writing conventions (theoretical register)
  reference/COLLECTION.md     Writing conventions (descriptive register)
  instructions/COLLECTION.md  Writing conventions (prescriptive register)
  log.md                     Improvement log — one-line observations appended during traversal
  notes/                     Notes — the primary knowledge unit
    types/                   Note-local type templates (structured-claim)
    adr/                     Architecture Decision Records
    related-systems/         External system comparisons
  sources/                   Snapshotted external sources + analysis
  tasks/                     Work tracking (status encoded by directory)
  work/                      Workshop space — connect reports, ingest staging, explorations
  instructions/              Framework skills, local procedures, and operator guidance
    write/SKILL.md           Promoted framework skill source
    connect/SKILL.md         Promoted framework skill source
    ingest/SKILL.md          Promoted framework skill source
    evaluate-scenarios/SKILL.md  Measure scenario costs
    re-ingest.md             Instruction (not yet promoted to skill)
    review-gates/            Review gates grouped by bundle/lens name (e.g. semantic/)
    ...

test/
  scenarios/                 Scenario fixtures for cost decomposition and evaluation

src/commonplace/             Packaged operational engine
  cli/                       User-facing commands
  review/                    Review system commands + support modules
  lib/                       Shared runtime helpers
  docs/                      MkDocs hooks and documentation assets
```

## Key ideas

**Title as claim, not topic.** Note titles are assertions that work as prose when linked: "approvals guard against LLM mistakes not active attacks" instead of "approvals system". Following links reads like a chain of reasoning.

**Progressive refinement.** Capture with zero friction — a file with no frontmatter is a valid `text` type with zero structural requirements. Add frontmatter to make it a `note`. Add Evidence/Reasoning/Caveats sections to make it a `structured-claim`. Structure is earned, not imposed.

**Files, not database.** Authored knowledge stays file-backed: universal interface, free versioning via git, zero infrastructure. Derived indexes solve scale problems without replacing the source of truth. The current scoped exception is the experimental review system, which stores review state in SQLite because that state behaves like local operational metadata rather than library content; see [010-review state should move to sqlite once reviews leave git and accumulate operational metadata](https://github.com/zby/commonplace/blob/main/kb/reference/adr/010-review-state-should-move-to-sqlite-once-reviews-leave-git-and.md).

**The network IS the knowledge.** Individual notes matter less than their relationships. Every link must articulate its relationship (extends, grounds, contradicts, exemplifies) — "related" is not a relationship. An unconnected note is invisible.

**Externalized methodology.** Knowledge accumulates in the KB, but the procedures for working with it — how to write, connect, validate — live in skills and docs, not in the agent's head. The agent reads them fresh every time. The KB is the memory; the skills are the manual.

## Skills and instructions

Framework skills are sourced from `kb/instructions/` and installed into consuming projects under `kb/commonplace/instructions/cp-skill-*/` with a `cp-skill-` prefix. The prefix keeps them distinct from both a project's own skills and the `commonplace-*` CLI commands. `commonplace-init` creates `.claude/skills/` and `.agents/skills/` symlink projections for common runtimes, and other IDEs or agent runtimes should expose the same canonical skill directories through their own skill mechanism. Plain KB procedures remain under `kb/instructions/` and load on demand. The project control-plane file (`CLAUDE.md` or `AGENTS.md`) still handles KB discovery and scoping.

Framework skills:

| Skill | Purpose |
|---|---|
| `cp-skill-write` | Route and draft a note, index, or discovered specialized type |
| `cp-skill-validate` | Check frontmatter, descriptions, types, links, structure |
| `cp-skill-connect` | Discover connections and write a `connect-report` artifact |
| `cp-skill-convert` | Convert raw text captures into structured notes |
| `cp-skill-health-check` | Diagnose broken Commonplace installs, skill discovery, command PATH, and direnv state |
| `cp-skill-ingest` | Ingest external source: snapshot → connect → classify → analyse |
| `cp-skill-snapshot-web` | Capture a URL to `kb/sources/` |
| `cp-skill-revise-iterative` | Iteratively revise a note without changing its claims |
| `cp-skill-revise-autoreason` | Revise a note with AutoReason-style incumbent/revision/synthesis judging |

Repo-local skills and procedures remain under `kb/instructions/`. Examples:
- `evaluate-scenarios` — scenario-cost measurement for this repo's methodology work
- Agent-memory-system reviews are handled by writing with the `agent-memory-system-review` type — workflow in `kb/agent-memory-systems/types/agent-memory-system-review.md`

## Content workflow

### Reading

Search the KB, read matching notes, follow links to deepen understanding. Link semantics (extends, grounds, contradicts) help the agent decide which connections are worth following. Good descriptions act as retrieval filters — they discriminate between similar notes so the agent reads fewer irrelevant ones.

### Writing

1. **Search first** — find related notes before writing
2. **Read the target collection's `COLLECTION.md`** — each collection has its own writing conventions, quality goals, and default templates. For notes, read `kb/notes/COLLECTION.md`.
3. **Read the directory type** — only if you're writing a specialized type (adr, index, related-system, or scenario in `test/scenarios/`). Skip this step for plain notes.
4. **Write** the note
5. **Connect** — link the new note from related notes and indexes. Use the `cp-skill-connect` skill or do it manually. Don't skip this — an unconnected note is invisible to future search.

## Usage

### Direct use (this repo)

Clone the repo and start working. The repo is a functioning knowledge base out of the box — skills, types, writing conventions, and methodology are all in place.

```bash
git clone https://github.com/zby/commonplace.git
cd commonplace
```

If you use `direnv`, make sure your shell has the direnv hook installed, then run `direnv allow` once after entering the repo. The `.envrc` sets `PATH` and `UV_CACHE_DIR` for the project. Start Codex or Claude Code from that direnv-loaded interactive shell so the runtime inherits the project venv; otherwise launch it with `direnv exec . <command>`.

Skills are installed under `kb/instructions/cp-skill-*/` in this repo and exposed to local agent runtimes through `.claude/skills/cp-skill-*/` and `.agents/skills/cp-skill-*/` symlinks. Other runtimes should expose the same canonical skill directories in their own way. The root `AGENTS.md` provides the project routing layer. The `kb/` directory is both the methodology and your workspace — new notes go alongside the existing ones.

This is the right mode when:
- You want to explore or contribute to the Commonplace methodology itself
- You want a standalone knowledge base without attaching it to another project
- You're evaluating the system before installing it elsewhere

### Installing into a project

Commonplace can be installed into any project as a Python package. See **[INSTALL.md](https://github.com/zby/commonplace/blob/main/INSTALL.md)** for the setup flow.

## Prerequisites

| Tool | Required | Purpose |
|---|---|---|
| Agent runtime | yes | Codex, Claude Code, or another internal LLM/IDE that can load project instructions and expose the `cp-skill-*` skill directories |
| [uv](https://docs.astral.sh/uv/) | yes | Install and run the Commonplace Python package |
| [git](https://git-scm.com/) | yes | Versioning, history-preserving renames in `convert` |
| [ripgrep](https://github.com/BurntSushi/ripgrep) (`rg`) | yes | Structured search — frontmatter queries, keyword matching, link scanning |
| [curl](https://curl.se/) | yes | PDF downloads in `snapshot-web` |
| [gh](https://cli.github.com/) | no | GitHub issue/PR snapshots in `snapshot-web` and `commonplace-github-snapshot` |

## Commands

Install the package first, then use the commands directly:

```bash
commonplace-validate kb/notes
commonplace-relocate-note old-note "New note title" --apply
commonplace-relocate-note old-note --to kb/notes/definitions --apply
commonplace-github-snapshot <url>
commonplace-x-snapshot <url>
```

## License

Commonplace is dual-licensed:

- Code in `src/` and package tooling: [MIT](https://github.com/zby/commonplace/blob/main/LICENSE-CODE)
- Knowledge-base content, documentation, templates, and bundled instructional artifacts: [CC BY 4.0](https://github.com/zby/commonplace/blob/main/LICENSE)
