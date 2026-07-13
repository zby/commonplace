---
description: "Proposal: a ReviewConfig object owned by commonplace.review, consolidating the review subsystem's project-shape constants (scan roots, gates root, artifact root, db path) with per-project override — deliberately not a global ProjectConfig, so the experimental db-backed review subsystem stays decoupled from the stable core"
type: kb/types/note.md
traits: [design-proposal]
tags: [kb-maintenance]
---

# Review configuration object

The review subsystem's assumptions about project shape are hardcoded as module-level constants, so a consuming project with a different layout — reviewable notes outside `kb/notes/` and `kb/reference/` — cannot extend review scope without editing installed package code. This proposal consolidates those constants into one configuration object **owned by the review subsystem**, not a global `ProjectConfig`: review execution and freshness are experimental surfaces with a faster change cadence than `commonplace.lib`, and a package-wide config object would couple the stable core to them. Configuration is per subsystem; a subsystem earns a config object when its constants need to vary.

## Current state (as of 2026-07-13)

General freshness and review execution share one operational store ([ADR 052](../adr/052-general-freshness-store-review-first-migration.md)). Store path resolution lives in `commonplace.store` (`kb/reports/commonplace-store.sqlite`; `COMMONPLACE_STORE`, with `COMMONPLACE_REVIEW_DB` as a legacy fallback). Review modules re-export `DEFAULT_DB_PATH` and `resolve_db_path` from there. A `ReviewConfig` would still be review-owned, but its `db_path` field should align with `commonplace.store` rather than reintroducing a review-only default.

Project-shape constants partition cleanly by owner:

**Review-owned** (all of the live problem):

| Constant | Module | What it pins |
|---|---|---|
| `NOTES_ROOT`, `REFERENCE_ROOT` | `review/review_target_selector.py` | which collections are reviewable (scan roots) |
| gate catalog roots | `review/paths.py` | where review gates live |
| `REVIEW_JOBS_ROOT` | `review/artifacts.py` | where review job artifacts are written |
| `DEFAULT_DB_PATH` | `commonplace.store` (re-exported in `review/review_db.py`) | operational store location (`COMMONPLACE_STORE` / `--db`) |

Override mechanisms are inconsistent: the store path has env vars and a `--db` flag on review and freshness CLIs; scan roots, gate catalog roots, and artifact roots have no project override.

**Core-owned**: the scaffold/promoted-skills policy was the one core entry in this proposal's original table; it shipped separately as `commonplace.scaffold_manifest` (data the installer executes), which already gives the stable core its policy-as-data form without a runtime config object. `lib/project_paths.py` covers indexing concerns and is untouched. No core constant currently needs per-project variation.

The hardcoded scan roots are the operative limitation: `list_reviewable_notes` walks exactly `kb/notes/` and `kb/reference/`, so collections added by a consuming project (or by this repo — `kb/agentic-systems/` is already a collection outside both roots) are invisible to review targeting.

## The design

One frozen dataclass `ReviewConfig` in `commonplace.review`, holding the review-owned table above, constructed once per CLI invocation from defaults merged with a per-project override source, and passed explicitly to the functions that consume it — no module-global mutation, no import-time `Path.cwd()`, following the existing `repo_root`/`db_path` threading convention. Its `db_path` default delegates to `commonplace.store.resolve_db_path` so review and freshness CLIs share one override story (`COMMONPLACE_STORE`, legacy `COMMONPLACE_REVIEW_DB`, `--db`).

The core deliberately gets nothing: if a stable-core constant ever needs per-project variation, it gets its own object then, with its own (slower) change cadence. The two configs share at most an override-file format, not a type.

## Free choices

- **Override source.** A `[tool.commonplace.review]` table in the consuming project's `pyproject.toml`, a dedicated config file, or env vars only. A file the KB ships with makes project shape reviewable content; env vars compose better with one-off invocations. These can layer (file then env), at the cost of precedence rules.
- **Scope of the first cut.** Scan roots alone would solve the operative limitation; the full table is more uniform but touches every review module. Partial adoption should start with scan roots.
- **Whether scan roots become collection-derived.** Instead of listing roots, the config could declare "every collection with `COLLECTION.md` whose contract opts into review" — stronger coupling to the collection model, no second list to maintain, but it gives `COLLECTION.md` a machine-read role it does not currently have.

## Adoption criteria

Adopt when a consuming project (or this repo) actually needs a non-default review shape — the first concrete candidate is making additional collections reviewable. Until then the constants are stable and the consolidation is pure motion.

## Risks

- A config object grows by accretion; without a quality bar it becomes a junk drawer. The bar: only constants that vary per consuming project belong here — protocol constants (sentinel grammar, decision enums) do not.
- File-based config introduces a parse/validation surface (`commonplace-validate` would need to check it) and one more thing `commonplace-init` must scaffold.
- Collection-derived scan roots (the last free choice) would make review behavior depend on `COLLECTION.md` frontmatter — a binding, machine-consumed role that file has deliberately not had; that step needs its own decision.

---

Relevant Notes:

- [052-general freshness store, review-first migration](../adr/052-general-freshness-store-review-first-migration.md) — see-also: operational store path now owned by `commonplace.store`, not review-only tables
- [freshness architecture](../freshness-architecture.md) — see-also: shared store boundary review config must not fork
- [030-harness-facing seams: batch endpoints and runner adapters](../adr/030-harness-facing-seams-batch-endpoints-and-runner-adapters.md) — see-also: the same adaptability direction at the execution seam; this proposal addresses the review subsystem's project-shape seam
- [collection](../definitions/collection.md) — see-also: the unit a consuming project would reshape; one free choice derives scan roots from collection contracts
