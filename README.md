# Commonplace

**Research on knowledge systems, running as one.**

Commonplace is a growing body of research on how to build the most powerful agentic systems. The bet is simple: an LLM can consume a theory and act on it, and can even write the code that theory calls for — so an _actionable_ theory of how to build such systems is itself a way of building them. Commonplace aims to be that theory: one closed under its own recommendations, telling an agent when to reason from prose, when to freeze knowledge into durable code, and how to verify what it produces.

The theory's most immediate target is an **LLM wiki** in the sense [Karpathy sketched](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): a persistent, linked markdown layer that agents build and maintain around your own work, turning ephemeral chats into a durable, growing body of your thinking. This repository ships everything needed to run one — the type system, writing conventions, agent skills, and `commonplace-*` Python commands.

It is also the first deployment. The research lives here as notes, and LLM agents follow the methodology those notes lay out to maintain the wiki it lives in. The content is AI-generated throughout — a human directs the inquiry; agents (Claude, ChatGPT, and others) draft, connect, and maintain the notes.

This page covers the tool: what's in the repo, how to use it, and how to install it. The research is best read on the rendered site at <https://zby.github.io/commonplace/>.

## What's in the box

```
kb/                       Knowledge base
  types/                  Global types (text, note, instruction, definition, index)
  notes/                  Notes — the primary knowledge unit (theoretical register)
  reference/              Shipped-system docs and ADRs (descriptive register)
  instructions/           Framework skills, review gates, and operator procedures (prescriptive register)
  agent-memory-systems/   Reviews of external agent-memory and knowledge systems
  agentic-systems/        Reviews of external agentic systems and harnesses
  sources/                Snapshotted external sources + analysis
  reports/                Generated review, connect, and fix reports
  work/                   Workshop space — in-flight drafts and explorations
  tasks/                  Work tracking
  log.md                  Improvement log
  index.md                Rendered-site homepage

src/commonplace/          Packaged operational engine
  cli/                    The commonplace-* commands
  review/                 Review system
  lib/                    Shared runtime helpers
  docs/                   Rendered-site (MkDocs) hooks and assets
```

## Key ideas

Five design principles the system is built on. The research claims behind them live in the [notes](https://zby.github.io/commonplace/).

**Title as claim, not topic.** Note titles are assertions that work as prose when linked: "approvals guard against LLM mistakes not active attacks" instead of "approvals system". Following links reads like a chain of reasoning — [why this works](https://github.com/zby/commonplace/blob/main/kb/notes/title-as-claim-enables-traversal-as-reasoning.md).

**Progressive refinement.** Capture with zero friction — a file with no frontmatter is a valid `text`, with zero structural requirements. Add frontmatter and it becomes a `note`. A note can later take a specialized type — a `definition`, an `adr` — but only when its content earns the extra structure. Structure is earned, not imposed ([the wikiwiki principle](https://github.com/zby/commonplace/blob/main/kb/notes/wikiwiki-principle-lowest-friction-capture-then-progressive-refinement.md)).

**Files, not database.** Authored knowledge stays file-backed: universal interface, free versioning via git, zero infrastructure. Derived indexes solve scale problems without replacing the source of truth. The one scoped exception is review state, which behaves like local operational metadata rather than library content and lives in SQLite ([ADR 010](https://github.com/zby/commonplace/blob/main/kb/reference/adr/010-review-state-should-move-to-sqlite-once-reviews-leave-git-and.md), [ADR 035](https://github.com/zby/commonplace/blob/main/kb/reference/adr/035-review-jobs-finalize-all-or-nothing-with-derived-artifacts.md)).

**The network IS the knowledge.** Individual notes matter less than their relationships. Every link must articulate its relationship (extends, grounds, contradicts, exemplifies) — "related" is not a relationship. An unconnected note is invisible ([linking methodology](https://github.com/zby/commonplace/blob/main/kb/notes/links-README.md)).

**Externalized methodology.** The procedures for working the wiki — how to write a note, connect it, validate it — are written down as skills and conventions, not baked into a particular model or assistant. Every agent reads them fresh, so a different model, or a new session, produces consistent work: the manual is on disk, not in the weights.

## Skills, instructions, and commands

Commonplace gives agents three kinds of operative artifact.

**Commands** (`commonplace-*`) are the Python CLI — deterministic operations called by name. Install the package, then:

```bash
commonplace-validate kb/notes        # check frontmatter, types, links, structure
commonplace-init                     # scaffold Commonplace into a project
commonplace-github-snapshot <url>    # snapshot a GitHub issue/PR into kb/sources/
commonplace-x-snapshot <url>         # snapshot an X/Twitter thread
```

A further family of commands drives the review system — selecting targets, queuing jobs, finalizing output; see the [review system overview](https://github.com/zby/commonplace/blob/main/kb/reference/README-REVIEW-SYSTEM.md).

**Skills** (`cp-skill-*`) are agent procedures the harness auto-loads from their descriptions: when a task matches a skill, the agent invokes it. `commonplace-init` installs them into a consuming project.

| Skill | Purpose |
|---|---|
| `cp-skill-write` | Route and draft a note, index, or specialized type |
| `cp-skill-validate` | Check frontmatter, descriptions, types, links, structure |
| `cp-skill-connect` | Discover connections and write a `connect-report` |
| `cp-skill-convert` | Convert raw text captures into structured notes |
| `cp-skill-ingest` | Ingest an external source: snapshot → connect → classify → analyse |
| `cp-skill-snapshot-web` | Capture a URL into `kb/sources/` |
| `cp-skill-health-check` | Diagnose a broken Commonplace install |
| `cp-skill-revise-iterative` | Iteratively revise a note without changing its claims |
| `cp-skill-revise-autoreason` | Revise a note with AutoReason-style incumbent/revision/synthesis judging |

**Instructions** are procedures written in Markdown, like skills, but without the auto-loading: the user or another skill invokes them explicitly. They live under `kb/instructions/`.

## Usage

### Direct use (this repo)

Clone the repo and start working — it is a functioning knowledge base out of the box, with skills, types, writing conventions, and methodology all in place. New notes go alongside the existing ones, and the root `AGENTS.md` provides the project routing layer.

```bash
git clone https://github.com/zby/commonplace.git
cd commonplace
```

If you use `direnv`, make sure your shell has the direnv hook installed, then run `direnv allow` once after entering the repo. The `.envrc` sets `PATH` and `UV_CACHE_DIR` for the project. Start Codex or Claude Code from that direnv-loaded interactive shell so the runtime inherits the project venv; otherwise launch it with `direnv exec . <command>`.

This is the right mode for exploring or contributing to the Commonplace methodology itself, running a standalone knowledge base, or evaluating the system before installing it elsewhere.

### Vendored inside your project (reader mode)

To give your agents the research without running a KB of your own, vendor this repo **inside** your project — a git submodule or a gitignored clone — and add one routing paragraph to your project's `CLAUDE.md`/`AGENTS.md`. Placement inside the project root matters: agent harnesses scope file access to the root, so a subdirectory is readable without permission prompts while a sibling directory is not. Reading needs no Python, no venv, and no skills. See [INSTALL.md → Reader install](https://github.com/zby/commonplace/blob/main/INSTALL.md#reader-install-the-kb-as-a-vendored-reference) for the commands and the paste-ready routing block.

### Installing into a project

Commonplace can be installed into any project as a Python package. Your agents get the same type system, conventions, and skills, and accumulate knowledge about your domain rather than this one. See [**INSTALL.md**](https://github.com/zby/commonplace/blob/main/INSTALL.md) for the setup flow. This composes with reader mode: a project can vendor this KB for reading and run its own for writing.

## Prerequisites

| Tool | Required | Purpose |
| --- | --- | --- |
| Agent runtime | yes | Codex, Claude Code, or another internal LLM/IDE that can load project instructions and expose the `cp-skill-*` skill directories |
| [uv](https://docs.astral.sh/uv/) | yes | Install and run the Commonplace Python package |
| [git](https://git-scm.com/) | yes | Versioning, history-preserving renames in `convert` |
| [ripgrep](https://github.com/BurntSushi/ripgrep) (`rg`) | yes | Structured search — frontmatter queries, keyword matching, link scanning |
| [curl](https://curl.se/) | yes | PDF downloads in `snapshot-web` |
| [gh](https://cli.github.com/) | no | GitHub issue/PR snapshots in `snapshot-web` and `commonplace-github-snapshot` |

## License

Commonplace is dual-licensed:

- Code in `src/` and package tooling: [MIT](https://github.com/zby/commonplace/blob/main/LICENSE-CODE)
- Knowledge-base content, documentation, templates, and bundled instructional artifacts: [CC BY 4.0](https://github.com/zby/commonplace/blob/main/LICENSE)
