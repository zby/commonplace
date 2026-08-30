# Commonplace

**Research on knowledge systems, running as one.**

Commonplace studies how agentic systems can change after deployment through inspectable knowledge artifacts. It also puts that idea into practice: human-directed agents use and revise the Markdown, instructions, schemas, validators, tests, and code in this repository. When later work loads or enforces those artifacts, accepted changes can shape behavior without updating model weights. The repository makes both the mechanism and its governance visible.

Commonplace is also a **living doctrine**: an adopted, revisable framework for selecting and coordinating how model-mediated and symbolic operations are used. It is not limited to knowledge absent from model weights: relevant knowledge may fail to [activate](./kb/notes/knowledge-storage-does-not-imply-contextual-activation.md), while operations that require [faithful execution](./kb/notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) may still belong in code. Like the Ship of Theseus, Commonplace persists through a governed lineage of revisions even as its doctrine, prompts, code, and the models it uses change.

The theory's most immediate target is an **LLM wiki**, in the sense [AI researcher Andrej Karpathy sketched](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): a persistent, linked Markdown layer that agents build and maintain around a person's or project's work. This repository ships the framework for operating one — the type system, writing conventions, agent skills, and `commonplace-*` Python commands.

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
  reports/                Cache, state, and retained report outputs
  work/                   Workshop space — in-flight drafts and explorations
  tasks/                  Work tracking
  log.md                  Improvement log
  index.md                Rendered-site homepage

src/commonplace/          Packaged operational engine
  cli/                    The commonplace-* commands
  review/                 Review system
  lib/                    Shared runtime helpers
  docs/                   Rendered-site (ProperDocs) hooks and assets
```

## Key ideas

Five design principles the system is built on. The research claims behind them live in the [notes](https://zby.github.io/commonplace/).

**Title as claim, not topic.** Note titles are assertions that work as prose when linked: "approvals guard against LLM mistakes not active attacks" instead of "approvals system". Following links reads like a chain of reasoning — [why this works](https://github.com/zby/commonplace/blob/main/kb/notes/title-as-claim-enables-traversal-as-reasoning.md).

**Progressive refinement.** Capture with zero friction — a file with no frontmatter is a valid `text`, with zero structural requirements. Add valid note frontmatter, including `description` and `type: kb/types/note.md`, and it becomes a `note`. A note can later take a specialized type — a `definition`, an `adr` — but only when its content earns the extra structure. Structure is earned, not imposed ([the wikiwiki principle](https://github.com/zby/commonplace/blob/main/kb/notes/wikiwiki-principle-lowest-friction-capture-then-progressive-refinement.md)).

**Files, not database.** Authored knowledge stays file-backed: universal interface, free versioning via git, zero infrastructure. Derived indexes solve scale problems without replacing the source of truth. The one scoped exception is review state, which behaves like local operational metadata rather than library content and lives in SQLite ([ADR 010](https://github.com/zby/commonplace/blob/main/kb/reference/adr/010-review-state-should-move-to-sqlite-once-reviews-leave-git-and.md), [ADR 035](https://github.com/zby/commonplace/blob/main/kb/reference/adr/035-review-jobs-finalize-all-or-nothing-with-derived-artifacts.md)).

**The network IS the knowledge.** Individual notes matter less than their relationships. Every link must articulate its relationship (extends, grounds, contradicts, exemplifies) — "related" is not a relationship. An unconnected note is invisible ([linking methodology](https://github.com/zby/commonplace/blob/main/kb/notes/links-README.md)).

**Externalized methodology.** The procedures for working the wiki — how to write a note, connect it, validate it — are written down as skills and conventions, not baked into a particular model or assistant. Every agent reads them fresh, so a different model, or a new session, produces consistent work: the manual is on disk, not in the weights.

## Research threads

The methodology notes live under `kb/notes/`; the rendered-site homepage is [kb/index.md](./kb/index.md). Start with [deploy-time learning](./kb/notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md). The foundational vocabulary proceeds from [actionable methodology](./kb/notes/definitions/actionable-methodology.md), through [reflective system](./kb/notes/definitions/reflective-system.md), to [graded reflective coverage across representational forms](./kb/notes/reflective-coverage-is-graded-across-representational-forms.md), [governed adaptation](./kb/notes/governed-adaptation-requires-search-evaluation-and-retention.md) — search, evaluation, and operative retention — and [closure under recommendations](./kb/notes/a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md). Each property can hold without the others; [Commonplace as a reflective system](./kb/notes/evidence/commonplace-as-a-reflective-system.md) applies them to this repository.

On structure: a wiki accretes it, because structure is cheap to add and free to leave. Commonplace hardens only what an inherited constraint forces and leaves the rest collection-local and replaceable, [since task-fitted structure costs cross-task reuse](./kb/notes/current-task-fit-alone-does-not-warrant-costly-entrenchment.md).

## Skills, instructions, and commands

Commonplace gives agents three kinds of operative artifact.

**Commands** (`commonplace-*`) are the Python CLI — deterministic operations called by name. Install them once per OS user, update the durable command path, and restart the consuming shell or agent runtime:

```bash
uv tool install --python ">=3.11" llm-commonplace
uv tool update-shell
```

After restarting the consuming process, invoke the commands by bare name:

```bash
commonplace-validate kb/notes        # check frontmatter, types, links, structure
commonplace-init                      # scaffold Commonplace into the current project
commonplace-github-snapshot https://github.com/owner/repo/issues/123
```

A further family of commands drives the review system — selecting targets, queuing jobs, finalizing output. `commonplace-x-snapshot` requires the `snapshot` package extra. See [INSTALL.md](./INSTALL.md) for optional extras and the [review system overview](https://github.com/zby/commonplace/blob/main/kb/reference/README-REVIEW-SYSTEM.md) for review commands.

**Skills** (`cp-skill-*`) are agent procedures the harness auto-loads from their descriptions: when a task matches a skill, the agent invokes it. `commonplace-init` installs them into a consuming project.

| Skill | Purpose |
|---|---|
| `cp-skill-write` | Write or edit one artifact under its collection and type contracts |
| `cp-skill-validate` | Validate artifacts, collection landings, and site redirects |
| `cp-skill-connect` | Discover connections and write a `connect-report` |
| `cp-skill-convert` | Convert raw text captures into structured notes |
| `cp-skill-ingest` | Ingest an external source: local snapshot → connect → classify → tracked analysis |
| `cp-skill-snapshot-web` | Capture a URL into ignored `kb/sources/.snapshots/` |
| `cp-skill-ground` | Retain the minimum verbatim quotes that ground one source claim, or flag that the snapshot is required |
| `cp-skill-health-check` | Diagnose a broken Commonplace install |
| `cp-skill-revise-autoreason` | Revise a note with AutoReason-style incumbent/revision/synthesis judging |

**Instructions** are procedures written in Markdown, like skills, but without the auto-loading: the user or another skill invokes them explicitly. They live under `kb/instructions/`.

## Usage

Two ways to use Commonplace, by what you want from it: **install the system** to run a knowledge base of your own, or **vendor this repo read-only** so your agents can consult the research. A Python runtime, which uv can provision, is only needed for the full install — the vendored KB is plain markdown, so it drops into a TypeScript, Rust, or any other project with no programming environment attached.

### Installing into a project (full install)

Commonplace installs as a user-level uv tool, then scaffolds its KB content into any project. Your agents get the same type system, conventions, and skills, and accumulate knowledge about your domain rather than this one. The package ships the methodology — the research notes, reference docs, instructions, types, skills, and `commonplace-*` commands — but not the external-system reviews (`kb/agent-memory-systems/`, `kb/agentic-systems/`) or this repo's source corpus. The external-system reviews and source ingest analyses remain available on the [rendered site](https://zby.github.io/commonplace/). Raw source captures are local, ignored reading copies under `kb/sources/.snapshots/`; tracked ingests retain their external URL, capture provenance, and exact snapshot checksum without redistributing the captured source. See [**INSTALL.md**](https://github.com/zby/commonplace/blob/main/INSTALL.md) for the setup flow.

### Vendored inside your project (reader mode)

To give your agents the full research corpus — external-system reviews and sources included — without running a KB of your own, vendor this repo **inside** your project — a git submodule, a gitignored clone, or a plain copy — and add one routing paragraph to your project's `CLAUDE.md`/`AGENTS.md` (shipped as `AGENTS.md.reader-fragment`, so appending it is a single command). Placement inside the project root matters: agent harnesses scope file access to the root, so a subdirectory is readable without permission prompts while a sibling directory is not. Reading needs no Python, no venv, and no skills. See [INSTALL.md → Reader install](https://github.com/zby/commonplace/blob/main/INSTALL.md#reader-install-the-kb-as-a-vendored-reference) for the commands and the paste-ready routing block.

### Working in this repo (development)

Clone the repo to explore or contribute to the Commonplace methodology itself, or to evaluate the system before installing it elsewhere — it is a functioning knowledge base out of the box, with skills, types, writing conventions, and methodology all in place. New notes go alongside the existing ones, and the root `AGENTS.md` provides the project routing layer.

```bash
git clone https://github.com/zby/commonplace.git
cd commonplace
uv tool install --python ">=3.11" --editable .
uv tool update-shell
```

Restart the shells, IDEs, and agent runtimes that need the commands, then call every `commonplace-*` entry point by bare name. The editable tool observes ordinary source changes directly; after dependency, entry-point, build-metadata, or packaged-scaffold changes, rerun it with `uv tool install --reinstall --python ">=3.11" --editable .`. Run development dependencies through the project environment, for example `uv run pytest` and `uv run ruff check .`. This installation is user-level, so the checkout supplies the one active Commonplace command version for that OS user.

## Prerequisites

**Reader mode needs only an agent runtime and ripgrep (`rg`)** — the KB's navigation leans on `rg` for search, and most agent runtimes bundle it. No Python, no skills: the KB is plain files, so a copy of the repo inside your project works as well as a clone or submodule. The table below applies to the full install:

| Tool | Required | Purpose |
| --- | --- | --- |
| Agent runtime | yes | Codex, Claude Code, or another internal LLM/IDE that can load project instructions and expose the `cp-skill-*` skill directories |
| [uv](https://docs.astral.sh/uv/) | yes | Install the Commonplace command tool and run source-development dependencies |
| [git](https://git-scm.com/) | yes | Versioning, history-preserving renames in `convert` |
| [ripgrep](https://github.com/BurntSushi/ripgrep) (`rg`) | yes | Structured search — frontmatter queries, keyword matching, link scanning |
| [curl](https://curl.se/) | yes | PDF downloads in `snapshot-web` |
| [Trafilatura](https://trafilatura.readthedocs.io/) | yes | Main-content HTML extraction and Markdown conversion in `snapshot-web` |
| [Poppler](https://poppler.freedesktop.org/) (`pdfinfo`, `pdftotext`) | yes | PDF metadata and text extraction in `snapshot-web` |
| [gh](https://cli.github.com/) | no | GitHub issue/PR snapshots in `snapshot-web` and `commonplace-github-snapshot` |

## License

Commonplace is dual-licensed:

- Code in `src/` and package tooling: [MIT](https://github.com/zby/commonplace/blob/main/LICENSE-CODE)
- Knowledge-base content, documentation, templates, and bundled instructional artifacts: [CC BY 4.0](https://github.com/zby/commonplace/blob/main/LICENSE)
