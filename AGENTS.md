# Commonplace

`CLAUDE.md` is a symlink to this file (`AGENTS.md`). Edit `AGENTS.md` directly.

A framework for building agent-operated knowledge bases. This repo contains the methodology, type definitions, writing conventions, instructions and skills, and the Python commands that get installed into projects.

The commonplace repo is itself a knowledge base — it uses its own knowledge system to document the methodology for building knowledge bases. There is no separation between "user content" and "methodology" here; the methodology IS the content.

## KB Goals

### Purpose

This KB accumulates methodology for building agent-operated knowledge bases — the theory, design patterns, and operational conventions that make KBs effective. It supports agents and maintainers making decisions about KB architecture, type systems, writing quality, context engineering, and knowledge organization.

### Domain

Agent-operated knowledge base methodology: how to structure, write, connect, validate, review, and maintain knowledge artifacts for consumption by LLM agents. Adjacent topics (learning theory, cognitive science, software architecture) are in scope only where they directly inform KB design decisions.

### Include

- Design decisions about KB methodology (type systems, linking, indexing, review)
- Context engineering theory (distillation, constraining, codification)
- Operational patterns (writing workflows, validation, maintenance)
- Evaluations and comparisons with external knowledge systems

### Exclude

- Application-specific KB content (belongs in consuming projects)
- General software engineering unless it informs KB methodology
- Raw logs without analysis (use `kb/log.md`)

### Quality bar

A design insight is worth a note when it changes how someone would build or operate a KB. Observations about what works are worth a log entry on first occurrence and a note when the mechanism is understood. Pure pattern-recording without explanation belongs in a log entry, not a note.

## Key Indexes

- `kb/notes/tags-index.md` — top-level navigation hub: tag indexes, foundations, evaluation, gaps
- `kb/notes/links-index.md` — linking methodology: semantics, navigation, contracts
- `kb/agent-memory-systems/README.md` — curated index of external agent-memory/knowledge systems
- `kb/agent-memory-systems/dir-index.md` — auto-generated directory listing for agent-memory-system coverage
- `kb/notes/dir-index.md` — auto-generated directory listing (rebuild with `commonplace-refresh-indexes`)
- `kb/reference/README.md` — shipped-system documentation entry point: architecture, type system, operator guide, and ADR navigation
- `kb/reference/navigation.md` — how agents navigate the KB with `rg`, titles/descriptions, indexes, links, connect reports, and future search layers
- `kb/reference/adr/` — architecture decision records for the shipped commonplace system
- `kb/reference/link-vocabulary.md` — label catalogue and authoring guidance for `COLLECTION.md` authors (consult when revising outbound rules)
- `kb/sources/dir-index.md` — auto-generated source listing

## Vocabulary

This section declares the active vocabulary: terms with specific meanings throughout this KB.

- **Context engineering** — the architecture and machinery for getting the right knowledge into a bounded context at the right time. Includes routing, loading, scoping, and maintenance. See `kb/notes/definitions/context-engineering.md`.
- **Distillation** — targeted transformation of recorded material into a use-shaped artifact for a particular downstream consumer. In KB practice this is usually directed context compression, because agents and maintainers work under bounded context. ML knowledge distillation (Hinton) is a sibling instance in a different substrate. See `kb/notes/definitions/distillation.md`.
- **Constraining** — making semantics more focused by narrowing the space of valid interpretations a text or symbolic artifact admits. Reliability, speed, cost control, and reviewability may follow, but they are consequences rather than the definition. Orthogonal to distillation. See `kb/notes/definitions/constraining.md`.
- **Codification** — constraining that crosses from natural language into a symbolic artifact with formal semantics or assigned consequences. Executable code is the main practical KB case, but schemas, grammars, route tables, and similar formal artifacts can also count. See `kb/notes/definitions/codification.md`.
- **Frontloading** — pre-computing parts of an LLM instruction whose inputs are known before the LLM runs, and inserting the result so the agent does not redo the work at execution time. *Economic* at broad scopes (build-time, install-time, session-start): saves repeated runtime work. *Constitutive* at narrow scopes (parent agent → sub-agent): without it, the sub-agent's effective context wouldn't fit the operation. See `kb/notes/frontloading-spares-execution-context.md`.
- **Retained artifact** — retained state that a later agentic loop can consume in a behavior-shaping way. The boundary is behavioral consequence, not storage label. See `kb/notes/definitions/retained-artifact.md`.
- **Operative part** — the behavior-affecting content, structure, parameterization, or mechanism within a retained artifact or consumption path. Classify the operative part when a stored object bundles several behavior-shaping parts. See `kb/notes/definitions/operative-part.md`.
- **Storage substrate** — where retained state persists: repo, database, vector store, prompt registry, service object, model-artifact store, etc. Storage is one field, not the taxonomy. See `kb/notes/definitions/storage-substrate.md`.
- **Representational form** — how an operative part is encoded and consumed: prose, symbolic, distributed-parametric, or mixed. Form determines the default review method: read prose, test/check symbolic artifacts, probe distributed-parametric artifacts. See `kb/notes/definitions/representational-form.md`.
- **Lineage** — source dependencies and derivation status needed to invalidate, regenerate, retire, or review retained behavior. See `kb/notes/definitions/lineage.md`.
- **Behavioral authority** — who consumes a retained artifact, through which channel, and with what force: advice, instruction, enforcement, ranking influence, audit trigger, or learning input. Replaces loose "role" shorthand when precision matters. See `kb/notes/definitions/behavioral-authority.md`.
- **Knowledge artifact** — retained artifact consumed as evidence, reference, context, explanation, or advice. It can change behavior through belief or consideration without binding the next action. See `kb/notes/definitions/knowledge-artifact.md`.
- **System-definition artifact** — retained artifact consumed with instruction, enforcement, routing, validation, configuration, evaluation, or learning force. This is an authority-path family, not a form or substrate. See `kb/notes/definitions/system-definition-artifact.md`.
- **Register** — one of three content modes (theoretical, descriptive, prescriptive) that determines a collection's quality goal, title conventions, and linking rules. See `kb/notes/definitions/register.md`.
- **Workshop** — a named workspace for temporal, work-in-flight documents. Lives in `kb/work/<workshop-name>/`. Value is consumed rather than accumulated — workshop artifacts have lifecycles and expiration; they produce library artifacts (notes, ADRs) when done. Contrast with the library layer (notes, indexes) where value accumulates over time. See `kb/notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md`.

## Development

- **Use `python3`** for stdlib-only throwaway tooling. Commonplace runtime code should live in the Python package and be invoked through `commonplace-*` commands. Use `uv run` for tests and optional-dependency workflows (`pytest`, `xdk`, MkDocs, etc.).
- **YAGNI** — don't implement features that aren't needed yet. If you identify a gap, create a note in `kb/notes/` instead of implementing it.
- **No backwards compatibility** — with no external consumers, always prioritize cleaner design over keeping old behavior alive. If backcompat code is ever needed, mark it with `# BACKCOMPAT: <reason> - remove after <condition>`.
- **Tests**: `uv run pytest` — all tests must pass.

## Git

- **Never `git add -A`** — review `git status` and stage specific files.
- **Prefer atomic stage+commit** — combine staging and committing in one command (`git add <files> && git commit -m "..."`). Leaving files staged without committing risks another agent's commit sweeping in unrelated changes.
- **If sandboxing blocks `git add` or `git commit`, retry the whole atomic command with escalation** — do not fall back to separate `git add` followed by a later `git commit`. Use explicit file paths in the atomic command, for example `git add path/one.md path/two.md && git commit -m "..."`.
- **Prefer atomic artifact commits over temporary navigation consistency** — do not partially stage shared README/index/navigation files just to make a new artifact immediately discoverable. Generated indexes and curated navigation can lag and be refreshed in a separate commit unless that navigation file is the primary target or can be staged wholly without sweeping unrelated work.
- **Check `git diff` before committing.**
- **Never `git reset --hard` or force-push** without explicit permission. Prefer safe alternatives: `git revert`, new commits, temporary branches.

## Using the KB

The knowledge base lives in `kb/`. Search it when working on methodology, design decisions, or operational patterns.

`kb/notes/` holds transferable claims and theory. `kb/reference/` holds shipped-system documentation and decision history for commonplace. `kb/instructions/` holds imperative procedures and how-to guidance.

For the full navigation model, read `kb/reference/navigation.md`. In short: use `rg` for cheap lexical search, scan titles and descriptions in directory/curated indexes before opening full files, and follow authored links when local context makes the relationship useful.

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

`commonplace-init` installs the `cp-skill-*` family (`cp-skill-write`, `cp-skill-validate`, `cp-skill-connect`, etc.) into `.claude/skills/` and `.agents/skills/`. The harness loads them automatically.

This repo also has a local-only `write-agent-memory-system-review` skill for external agent-memory-system reviews. It is symlinked into `.claude/skills/` and `.agents/skills/` here, but is not a promoted `cp-skill-*` framework skill.

### Commands

The `llm-commonplace` package provides `commonplace-*` CLI commands for validation, indexing, snapshots, note operations, and the review system. Documentation lives in `kb/reference/`:

- [commands.md](./kb/reference/commands.md) — CLI command reference
- [lib-modules.md](./kb/reference/lib-modules.md) — library modules (frontmatter, note_parser, type_resolver)
- [review-architecture.md](./kb/reference/review-architecture.md) — review system architecture and data model

For review work (single-note review, triage, ack, or sweep), read `kb/instructions/REVIEW-SYSTEM.md`.
For fixing review warnings, read `kb/instructions/FIX-SYSTEM.md`.

For writing conventions, each collection has a `COLLECTION.md` at its root: `kb/notes/COLLECTION.md` (theoretical register), `kb/reference/COLLECTION.md` (descriptive register), `kb/instructions/COLLECTION.md` (prescriptive register).
