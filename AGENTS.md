# Commonplace

`CLAUDE.md` is a symlink to this file (`AGENTS.md`). Edit `AGENTS.md` directly.

> **Vendored?** If this repository sits inside another project as a read-only knowledge base (a submodule or gitignored clone — see `INSTALL.md`, "Reader install"), you are a reader here, not an operator: navigate from `kb/notes/tags-README.md`, quote and cite freely, and do not create, edit, or commit anything under this directory. Everything below applies only when Commonplace itself is the working project. To contest a claim, open an issue at <https://github.com/zby/commonplace/issues>.

## Repository Overview

A framework for building agent-operated knowledge bases. This repo contains the methodology, type definitions, writing conventions, instructions and skills, and the Python commands that get installed into projects.

The Commonplace repo is itself a knowledge base — it uses its own knowledge system to document the methodology for building knowledge bases. There is no separation between "user content" and "methodology" here; the methodology IS the content.

## KB Goals and Scope

### Purpose

Support decisions about KB architecture, type systems, writing quality, context engineering, and knowledge organization — made by agents and maintainers working on Commonplace or on KBs built with it.

### Scope

Agent-operated knowledge base methodology: how to structure, write, connect, validate, review, and maintain knowledge artifacts for consumption by LLM agents.

In scope:

- Design decisions about KB methodology (type systems, linking, indexing, review)
- Context engineering theory (constraining, codification, knowledge reshaping)
- Operational patterns (writing workflows, validation, maintenance)
- Evaluations and comparisons with external knowledge systems

Out of scope:

- Application-specific KB content (belongs in consuming projects)
- General software engineering, learning theory, or cognitive science unless it directly informs KB design decisions
- Raw logs without analysis (use `kb/log.md`)

### Quality bar

A design insight is worth a note when it changes how someone would build or operate a KB. Observations about what works are worth a log entry on first occurrence and a note when the mechanism is understood. Pure pattern-recording without explanation belongs in a log entry, not a note.

## Vocabulary

Terms needed to understand the project's structure and everyday operations, alphabetical. Each links its full definition.

- **Assay** — any snapshot-anchored LLM evaluation executed through the review job pipeline. Closed-ended assays ask a fixed question; open-ended assays sample a space of possible findings. This question shape is distinct from the persisted `verdict`/`report` result kind. See `kb/reference/README-REVIEW-SYSTEM.md#concepts`.
- **Codification** — the far end of constraining, where natural language crosses into a symbolic artifact (code, schema, grammar) with formal semantics. See `kb/notes/definitions/codification.md`.
- **Collection** — a `kb/` subtree whose root contains `COLLECTION.md`; that file is the local authoring and routing contract for artifacts in the subtree. See `kb/reference/definitions/collection.md`.
- **Commonplace** — the name of this KB and framework. Capitalize it in prose; lowercase only in literal identifiers (`commonplace-*`, `llm-commonplace`, `src/commonplace/`, `kb/commonplace/`).
- **Criterion** — the instruction text applied to a note in an assay. It occupies the persisted `criterion_path` side of a review pair; a gate is a closed-ended, verdict-kind criterion, while critique is an open-ended, report-kind criterion. See `kb/reference/README-REVIEW-SYSTEM.md#concepts`.
- **Constraining** — narrowing the space of valid interpretations an artifact admits — from writing a convention up to committing to code. See `kb/notes/definitions/constraining.md`.
- **Context engineering** — getting the right knowledge into a bounded context at the right time: routing, loading, scoping, maintenance. See `kb/notes/definitions/context-engineering.md`.
- **Discovery lifecycle** — the staged path by which an ampliative conjecture earns acceptance: observe, conjecture, derive consequences, test, accept, integrate. The compound is the technical term; bare "discovery" stays ordinary English. See `kb/notes/definitions/discovery-lifecycle.md`.
- **Explanatory-reach** — the property that a claim keeps working beyond the cases that produced it because it captures why the pattern works; the quality goal of `kb/notes/` and the property reach-assessment judges. The compound is the technical term (adapted from Deutsch's "reach"); bare "reach" stays ordinary English. See `kb/notes/first-principles-reasoning-selects-for-explanatory-reach-over.md`.
- **Frontloading** — pre-computing parts of an instruction whose inputs are already known (at build, install, or session start) and inserting the result, so the consuming call's context carries the answer instead of the work. See `kb/notes/frontloading-spares-execution-context.md`.
- **Freshness baseline** — the current snapshot-pinned applicability boundary for one registered target. In v1 review targets are `review-pair` keys `(note, criterion, model partition)` with `note` and `criterion` `file-text` inputs; a baseline preserves an evidence review pair while tracking the latest accepted input snapshots — it is not endorsement or global approval. See `kb/reference/README-REVIEW-SYSTEM.md#concepts` and `kb/reference/freshness-architecture.md`.
- **Commonplace store** — the operational SQLite database (`kb/reports/commonplace-store.sqlite`; `COMMONPLACE_STORE`) holding artifact snapshots, freshness baselines, and review execution state. See `kb/reference/freshness-architecture.md`.
- **Gate** — a closed-ended, verdict-kind assay criterion. See `kb/reference/README-REVIEW-SYSTEM.md#concepts`.
- **Mark** — a frontmatter field that caches a value recomputable from ground truth recorded elsewhere, validated by code, and read by agents to spare an expensive in-context recompute (`complete`/`covered_by` on tag-READMEs). Recomputable, so never load-bearing; enforced-or-omitted, because a stale trusted cache is a trap. See `kb/types/tag-readme.md`.
- **Outcome** — the substantive `pass`, `warn`, or `fail` value produced by a completed verdict pair. Report pairs complete without an outcome; `ERROR` fails the job and is not an outcome. See `kb/reference/README-REVIEW-SYSTEM.md#concepts`.
- **Representational form** — how retained content is encoded and consumed: prose, symbolic (code, schemas, grammars), distributed-parametric (model weights), or mixed. Codification is the prose→symbolic crossing on this axis, and form sets the default review method: read prose, test symbolic artifacts, probe parametric ones. See `kb/notes/definitions/representational-form.md`.
- **Result kind** — the persisted pair protocol: `verdict` completes with an outcome; `report` completes without one. `REPORT` is a completion marker, not a fourth outcome. See `kb/reference/README-REVIEW-SYSTEM.md#concepts`.
- **System-definition artifact** — a retained artifact the system consumes with binding force: instruction, enforcement, routing, validation, or configuration (skills, schemas, COLLECTION.md files, validators). Contrast a knowledge artifact, consumed as evidence or advice that informs without binding. See `kb/notes/definitions/system-definition-artifact.md`.
- **Text contract** — the binding requirement a collection's `COLLECTION.md` declares: quality goal, title/description conventions, attribution requirements, maintenance semantics, and link grammar. A **profile** is a named, proven bundle of these features a collection may adopt, extend, or replace — theoretical, descriptive, and prescriptive are the shipped defaults; the set is open, guarded by worked-case-first promotion. See `kb/notes/definitions/text-contract.md` and the [profile catalogue](./kb/reference/text-contract-profiles.md).
- **Workshop** — a named workspace for work-in-flight documents, under `kb/work/<workshop-name>/`. Value is consumed rather than accumulated: a finished workshop produces library artifacts (notes, ADRs) and is deleted. See `kb/notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md`.

### Prose and registered identifiers

Use ordinary spaced phrases in prose (`adapted from`, `derived from`). Registered hyphenated identifiers (`adapted-from`, `operationalized-from`, `derived-from`, `abstracted-from`) name formal relations when used in a declared position such as a collection-authorized link label; they may also be mentioned as vocabulary names in documentation. Formal semantics attach to the identifier in the declared slot; the spaced phrase remains ordinary prose and does not itself assert a formal edge. See [link vocabulary](./kb/reference/link-vocabulary.md).

## Development

- **Use `python3`** for stdlib-only throwaway tooling; if the code is expected to be reused, save it to `scripts/` instead of discarding it (see `scripts/README.md`) — genuinely one-shot code stays a heredoc. Commonplace runtime code lives in the Python package as `commonplace-*` commands.
- **Package documentation**: [lib-modules.md](./kb/reference/lib-modules.md) — internal API of the `commonplace.lib` modules; [freshness-architecture.md](./kb/reference/freshness-architecture.md) — general freshness store and transitions; [review-architecture.md](./kb/reference/review-architecture.md) — review adapter and execution.
- **YAGNI** — don't implement features that aren't needed yet. If you identify a gap, write it down instead of implementing it: a system feature or design gap becomes a design proposal in `kb/reference/proposals/` (see its README for the contract); a transferable insight becomes a note in `kb/notes/`.
- **No backwards compatibility** — with no external consumers, always prioritize cleaner design over keeping old behavior alive. If backcompat code is ever needed, mark it with `# BACKCOMPAT: <reason> - remove after <condition>`.
- **Tests**: `pytest` — all tests must pass.

### Native Windows source checkout

This repository is operated directly from its checkout; do not run `commonplace-init` here. Set up the editable package from the repository root in PowerShell:

```powershell
$env:UV_CACHE_DIR = Join-Path (Get-Location) ".uv-cache"
uv venv
uv pip install -e .
```

A human working in one persistent PowerShell session may activate the venv with `.\.venv\Scripts\Activate.ps1`. Activation changes only that process and its children; desktop agent runtimes and agent tool calls may start fresh shells that do not inherit it.

In a fresh Windows shell, try a `commonplace-*` command by bare name once. If it is not found and the matching executable exists under `.venv\Scripts`, invoke the executable directly instead of repeatedly retrying activation or wrapping the command in `uv run`:

```powershell
& .\.venv\Scripts\commonplace-validate.exe kb\reference\commands.md
```

The same rule applies to every package entry point: `commonplace-foo` maps to `.venv\Scripts\commonplace-foo.exe`. Before reporting an installation failure, distinguish a missing executable from a missing `PATH` entry with `Test-Path .\.venv\Scripts\commonplace-foo.exe`.

`pytest` is installed with Commonplace because deterministic verification is part of operating this reflective system. In a fresh agent shell, run it as `& .\.venv\Scripts\pytest.exe`; for example, `& .\.venv\Scripts\pytest.exe tests\commonplace\lib\test_frontmatter.py -q`. If a sandboxed Windows session cannot write `.pytest_cache`, add `-p no:cacheprovider`; do not treat that cache-only warning as a test failure.

The source checkout's `.agents/skills/` and `.claude/skills/` projections are committed relative symlinks. A Windows checkout without symlink support may materialize them as plain files. If a `cp-skill-*` skill is not discoverable, read and follow its canonical `kb/instructions/<skill>/SKILL.md` directly; do not run `commonplace-init` to repair a source checkout.

## Git

- **Never `git add -A`** — review `git status` and stage specific files.
- **Prefer atomic stage+commit** — combine staging and committing in one command (`git add <files> && git commit -m "..."`). Leaving files staged without committing risks another agent's commit sweeping in unrelated changes.
- **If sandboxing blocks `git add` or `git commit`, retry the whole atomic command with escalation** — do not fall back to separate `git add` followed by a later `git commit`. Use explicit file paths in the atomic command, for example `git add path/one.md path/two.md && git commit -m "..."`.
- **Prefer atomic artifact commits over temporary navigation consistency** — do not partially stage shared README/index/navigation files just to make a new artifact immediately discoverable. Generated indexes and curated navigation can lag and be refreshed in a separate commit unless that navigation file is the primary target or can be staged wholly without sweeping unrelated work.
- **Check `git diff` before committing.**
- **Never `git reset --hard` or force-push** without explicit permission. Prefer safe alternatives: `git revert`, new commits, temporary branches.

## Using the KB

The knowledge base lives in `kb/`. Search it when working on methodology, design decisions, or operational patterns.

### Collection Routing

Read the target collection's `COLLECTION.md` before writing or connecting artifacts there.

| Path | Role | Use when |
|---|---|---|
| `kb/notes/` | theoretical profile | Writing transferable claims, mechanisms, definitions, synthesis, and KB methodology theory. |
| `kb/reference/` | descriptive profile | Describing the shipped Commonplace system, architecture, type system, commands, and ADRs. |
| `kb/instructions/` | prescriptive profile | Writing procedures, skills, review gates, operational rules, and how-to guidance. |
| `kb/agent-memory-systems/` | descriptive external-system coverage | Reviewing and comparing external agent memory, knowledge, and context-engineering systems. |
| `kb/agentic-systems/` | descriptive external-system coverage | Analysing external agentic systems and harnesses as whole systems — execution loops, orchestration APIs, control surfaces. |
| `kb/sources/` | captured source material | Storing external snapshots, ingests, and source reviews. |
| `kb/work/` | workshop layer | Holding in-flight investigations, drafts, migration plans, and temporary work that should eventually close or promote durable artifacts. |
| `kb/types/` | global type surface, not a collection | Looking up shared type specs used across collections. |

### Navigation

For the full model, read `kb/reference/navigation.md`. In short: use `rg` for cheap lexical search, scan titles and descriptions in curated indexes and scoped `rg` listings before opening full files, and follow authored links when local context makes the relationship useful.

Entry points:

- `kb/notes/tags-README.md` — top-level navigation hub: tag READMEs (including links), foundations, evaluation, gaps
- `kb/agent-memory-systems/README.md` — curated index of external agent-memory/knowledge systems
- `kb/reference/README.md` — shipped-system documentation entry point: architecture, type system, operator guide, and ADR navigation
- `kb/reference/adr/` — architecture outcome records for the shipped Commonplace system

Each tag's curated head is its `<tag>-README.md` (type `tag-readme`), small by type contract. It may declare two validator-enforced frontmatter marks: `complete: true` — the README links every note carrying the tag, so a reader can skip the by-tag `rg` sweep; `covered_by: [children]` — every tagged note also carries a listed child tag, so a reader can trust the typed routing. Maintenance of the marks lives in `kb/types/tag-readme.md` (ADR 026).

```bash
# Find notes by description
rg "^description:" kb/notes/ kb/reference/ kb/instructions/ --glob "*.md"

# Find notes by type (collection-local types use file-relative paths)
rg "^type: \./types/structured-claim.md" kb/notes/ --glob "*.md"
rg "^type: \.\./types/adr.md" kb/reference/ --glob "*.md"

# Find notes by tag
rg "^tags:.*learning-theory" kb/notes/ kb/reference/ kb/instructions/ --glob "*.md"
```

### Skills

The `cp-skill-*` family (`cp-skill-write`, `cp-skill-validate`, `cp-skill-connect`, etc.) is installed into `.claude/skills/` and `.agents/skills/` by `commonplace-init`; the harness loads them automatically. Repo-local skills (`roughdraft-review`, `write-agent-memory-system-review`) are symlinked the same way but are not promoted framework skills.

### Commands

The `llm-commonplace` package provides `commonplace-*` CLI commands for validation, snapshots, note operations, and the review system — reference in [commands.md](./kb/reference/commands.md). On Linux/macOS, call them and `pytest` by bare name: direnv puts `.venv/bin` on `PATH`, so never prepend `.venv/bin/` or wrap in `direnv exec` or `uv run`. On native Windows, follow the source-checkout fallback above: use the matching `.venv\Scripts\<command>.exe` when a bare command is unavailable, including `.venv\Scripts\pytest.exe` for tests. If neither the bare command nor the platform-specific venv executable exists or runs, use `cp-skill-health-check`.

For review work (single-note review, triage, ack, or sweep), read `kb/reference/README-REVIEW-SYSTEM.md`.
For fixing review warnings, read `kb/instructions/FIX-SYSTEM.md`.
