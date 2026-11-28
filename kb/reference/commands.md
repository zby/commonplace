---
description: Complete published catalogue of commonplace-* CLI commands — one-line purpose and where to get live options (--help) or operating skills
type: types/note.md
tags: []
---

# Commonplace CLI commands

Complete catalogue of the `commonplace-*` commands installed by the user-level `llm-commonplace` uv tool (`test_command_catalogue_integrity.py` checks exact parity with `pyproject.toml`). Run `<command> --help` (and `<command> <action> --help`) for live flags and contracts; use `commonplace-source` to inspect the executing Python package.

## Project setup

### commonplace-init

Scaffold a new Commonplace project (without overwriting user files) and refresh machine-specific library pointers (skill stubs, `.commonplace/library.md`, Claude Code read rule). `--check` reports drift without writing. See [architecture](./architecture.md).

### commonplace-source

Print the filesystem path of the `commonplace` package supplying the running commands.

## Validation and status

### commonplace-status

Print a compact, read-only project situation report (versions, Git state, scoped `--collection` validation, lifecycle checks, and optional `--review` counts) with stable next-action IDs.

### commonplace-validate

Run deterministic validation on a note, directory, collection, `types`, `landings`, `redirects`, `lifecycle`, `today`/`recent` (with `--collection`), a directory-artifact role draft (`--artifact` + `--role`), or an ingest handoff candidate (`--handoff`). To check several edited files without sweeping their collections, pass their `.md` paths together: `commonplace-validate PATH [PATH ...]`. See [validation contract](./validation-contract.md).

### commonplace-verify-quotes

Audit `verbatim`-marked quotations across Markdown files or directories, including unresolved pairings that ordinary validation passes.

## Note operations

### commonplace-relocate-note

Rename or move one note (plus its sibling `<stem>.brief.md` write brief if declared) and rewrite KB backlinks. Dry-runs unless `--apply` is passed.

### commonplace-relocate-directory

Move a KB directory, rewrite links, and optionally add one ProperDocs redirect. Dry-runs unless `--apply` is passed.

### commonplace-promotion-candidates

Rank unstructured text files in a collection by incoming links and write `kb/workflow-state/data/current/promotion-candidates/<collection>/report.md`.

## Sources and snapshots

### commonplace-github-snapshot

Capture a GitHub issue or PR into ignored `kb/sources/.snapshots/` (`--reobserve` writes a dated re-capture). Used by `cp-skill-snapshot-web`.

### commonplace-x-snapshot

Capture an X/Twitter post, thread, or article into ignored `kb/sources/.snapshots/` (`--reobserve` writes a dated re-capture). Used by `cp-skill-snapshot-web`.

### commonplace-ingest-handoff

Open (`prepare`), `publish`, `close`, and `prune` the staging handoff under `kb/workflow-state/data/current/ingest/` for an ingest draft. Used by `cp-skill-ingest`.

## Review and editing

### commonplace-review

Run read-only semantic reviews with headless workers (`status`, gate sweeps, compression checks, opt-in report criteria, `show`, `fixture`, `retry`, `acknowledge`). Never writes a note. Operated via `cp-skill-review` and [run-review-batches.md](../instructions/run-review-batches.md).

### commonplace-revise

Run note-editing and revision workflows (`--full`, `--quick`, `--pass`, `--finding`, `--plan`, `triage`, `apply`, `publish`, `answers`, `decisions`, `rewrite`, `try`). The only review/editing command that writes a note. Operated via `cp-skill-revise`.

## Tasks and analyses

### commonplace-sub-worker

Checkout trial: `commonplace-sub-worker run --profile NAME --brief PATH` asks one read-mode worker. The [verify skill](../instructions/verify/SKILL.md) defines when to use it and how to handle the result. Run records may become public. A successful call returns its answer as JSON. If the command detects a checkout change it returns a nonzero status and the affected paths instead, even if the worker failed. It cannot attribute the change and never reverts it.

### commonplace-task

Run one runbook from `kb/tasks/` unattended in the current checkout and verify its resulting commit (`run`).

### commonplace-analysis

Run isolated, commit-bound agentic-system analyses and bounded queues (`analyse`, `batch`, `resume`, `report`), plus low-level worktree preparation, inspection, recovery, and integration (`prepare`, `run`, `inspect`, `retry`, `acknowledge`, `reset`, `inspect-integration`, `integrate`). Operated via `analyse-agentic-system`; run `commonplace-analysis <subcommand> --help` for recovery and batch input details.

---

*No generated-index rebuild command exists:* ProperDocs generates directory indexes and tag membership pages during site builds. Browse the [topic index](../tags/README.md) or search the checkout with `rg`.
