# Commonplace

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
- `kb/notes/related-systems/related-systems-index.md` — external system comparisons
- `kb/notes/index.md` — auto-generated directory listing (rebuild with `commonplace-generate-notes-index kb/notes`)
- `kb/sources/index.md` — auto-generated source listing

## Vocabulary

Terms used in this KB with specific meanings:

- **Context engineering** — the architecture and machinery for getting the right knowledge into a bounded context at the right time. Includes routing, loading, scoping, and maintenance. See `kb/notes/definitions/context-engineering.md`.
- **Distillation** — compressing knowledge for a specific task under a context budget. The main operation context engineering performs, but not the only one. Not ML knowledge distillation (training a student to mimic a teacher). See `kb/notes/definitions/distillation.md`.
- **Constraining** — narrowing the interpretation space of an artifact (less generality, more reliability/speed/cost). Orthogonal to distillation. See `kb/notes/definitions/constraining.md`.
- **Codification** — committing a procedure to a symbolic medium (natural language → code). The far end of constraining. See `kb/notes/definitions/codification.md`.
- **Workshop** — a named workspace for temporal, work-in-flight documents. Lives in `kb/work/<workshop-name>/`. Value is consumed rather than accumulated — workshop artifacts have lifecycles and expiration; they produce library artifacts (notes, ADRs) when done. Contrast with the library layer (notes, indexes) where value accumulates over time. See `kb/notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md`.

## Development

- **Use `python3`** for stdlib-only throwaway tooling. Commonplace runtime code should live in the Python package and be invoked through `commonplace-*` commands. Use `uv run` for tests and optional-dependency workflows (`pytest`, `xdk`, MkDocs, etc.).
- **YAGNI** — don't implement features that aren't needed yet. If you identify a gap, create a note in `kb/notes/` instead of implementing it.
- **No backwards compatibility** — with no external consumers, always prioritize cleaner design over keeping old behavior alive. If backcompat code is ever needed, mark it with `# BACKCOMPAT: <reason> - remove after <condition>`.
- **Tests**: `uv run pytest` — all tests must pass.

## Git

- **Never `git add -A`** — review `git status` and stage specific files.
- **Prefer atomic stage+commit** — combine staging and committing in one command (`git add <files> && git commit -m "..."`). Leaving files staged without committing risks another agent's commit sweeping in unrelated changes.
- **Check `git diff` before committing.**
- **Never `git reset --hard` or force-push** without explicit permission. Prefer safe alternatives: `git revert`, new commits, temporary branches.

## Using the KB

The knowledge base lives in `kb/`. Search it when working on methodology, design decisions, or operational patterns.

```bash
# Find notes by description
rg "^description:" kb/notes/ kb/instructions/ --glob "*.md"

# Find notes by type
rg "^type: structured-claim" kb/notes/ kb/instructions/ --glob "*.md"

# Find notes by tag
rg "^tags:.*learning-theory" kb/notes/ kb/instructions/ --glob "*.md"
```

### Skills

| Task | Commonplace skill |
|---|---|
| Write a note or index | `commonplace-write` |
| Connect a note to related notes | `commonplace-connect` |
| Validate note structure | `commonplace-validate` |
| Snapshot an external URL | `commonplace-snapshot-web` |
| Ingest and analyze a source | `commonplace-ingest` |
| Convert between note types | `commonplace-convert` |
| Iteratively revise a note | `commonplace-revise-iterative` |

These skills are installed into both `.claude/skills/` and `.agents/skills/` by `commonplace-init`.

### Commands

The `llm-commonplace` package provides `commonplace-*` CLI commands for validation, indexing, snapshots, note operations, and the review system. For the full reference, read `src/commonplace/docs/COMMANDS.md`.

For review work (single-note review, triage, ack, or sweep), read `kb/instructions/REVIEW-SYSTEM.md`.
For fixing review warnings, read `kb/instructions/FIX-SYSTEM.md`.

For the full writing checklist and conventions, see `kb/instructions/WRITING.md`.
