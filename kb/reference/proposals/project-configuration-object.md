---
description: "Proposal: consolidate the project-shape constants scattered across commonplace modules (review scan roots, gates root, artifact roots, db path, sweep parallelism) into one explicit configuration object with per-project override, so consuming projects can reshape layout without editing the package"
type: kb/types/note.md
traits: [design-proposal]
tags: [kb-maintenance]
status: seedling
---

# Project configuration object

Commonplace is a framework installed into consuming projects (`commonplace-init`), but the project shape it assumes is hardcoded as module-level constants spread across the package. A consuming project with a different collection layout — say, reviewable notes outside `kb/notes/` and `kb/reference/` — cannot extend the system's scope without editing installed package code. This proposal consolidates the scattered constants into one explicit configuration object with a per-project override mechanism.

## Current state (as of 2026-06-12)

Project-shape constants and their homes:

| Constant | Module | What it pins |
|---|---|---|
| `NOTES_ROOT`, `REFERENCE_ROOT` | `review/review_target_selector.py` | which collections are reviewable (scan roots) |
| `GATES_ROOT` | `review/paths.py` | where review gates live |
| `BUNDLE_ARTIFACTS_ROOT` | `review/executor.py` | where review artifacts are written |
| `DEFAULT_DB_PATH` | `review/review_db.py` | review store location (env override `COMMONPLACE_REVIEW_DB` exists) |
| `DEFAULT_PARALLELISM` + `REVIEW_SWEEP_JOBS` env | `cli/review/review_sweep.py` | sweep fan-out width |
| scaffold directory list | `cli/init_project.py` | what `commonplace-init` creates |

Override mechanisms are inconsistent: the DB path has an env var and a `--db` flag, parallelism has a different env var, and the rest have nothing. `lib/project_paths.py` exists but covers indexing concerns, not these.

The hardcoded scan roots are the operative limitation: `list_reviewable_notes` walks exactly `kb/notes/` and `kb/reference/`, so collections added by a consuming project (or by this repo — `kb/agentic-systems/` is already a collection outside both roots) are invisible to review targeting.

## The design

One frozen dataclass (working name `ProjectConfig`) holding the table above, constructed once per CLI invocation from defaults merged with a per-project override source, and passed explicitly to the functions that consume it — no module-global mutation, no import-time `Path.cwd()`, in keeping with the lib/CLI split.

## Free choices

- **Override source.** A `[tool.commonplace]` table in the consuming project's `pyproject.toml`, a dedicated `commonplace.toml`/`kb/config.*` file, or env vars only. A file the KB ships with makes project shape reviewable content; env vars compose better with one-off invocations. These can layer (file then env), at the cost of precedence rules.
- **Threading style.** Pass `ProjectConfig` explicitly through call chains (verbose, honest) or resolve it once in each CLI `main` and close over it. Explicit passing matches the existing `repo_root`/`db_path` convention.
- **Scope of the first cut.** Scan roots alone would solve the operative limitation; the full table is more uniform but touches every review module. Partial adoption should start with scan roots.
- **Whether scan roots become collection-derived.** Instead of listing roots, the config could declare "every collection with `COLLECTION.md` whose contract opts into review" — stronger coupling to the collection model, no second list to maintain, but it gives `COLLECTION.md` a machine-read role it does not currently have.

## Adoption criteria

Adopt when a consuming project (or this repo) actually needs a non-default shape — the first concrete candidate is making additional collections reviewable. Until then the constants are stable and the consolidation is pure motion.

## Risks

- A config object grows by accretion; without a quality bar it becomes a junk drawer. The bar: only constants that vary per consuming project belong here — protocol constants (sentinel grammar, decision enums) do not.
- File-based config introduces a parse/validation surface (`commonplace-validate` would need to check it) and one more thing `commonplace-init` must scaffold.
- Collection-derived scan roots (the last free choice) would make review behavior depend on `COLLECTION.md` frontmatter — a binding, machine-consumed role that file has deliberately not had; that step needs its own decision.

---

Relevant Notes:

- [030-harness-facing seams: batch endpoints and runner adapters](../adr/030-harness-facing-seams-batch-endpoints-and-runner-adapters.md) — see-also: the same adaptability direction at the execution seam; this proposal addresses the project-shape seam
- [collection](../definitions/collection.md) — see-also: the unit a consuming project would reshape; one free choice derives scan roots from collection contracts
