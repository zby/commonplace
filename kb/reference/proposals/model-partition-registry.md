---
description: "Proposal: introduce a model partition registry for review validation, aliases, and runner defaults without making the registry the review identity"
type: kb/types/note.md
traits: [design-proposal]
tags: [kb-maintenance]
status: seedling
---

# Model partition registry

Commonplace review identity is `(note_path, gate_path, model_partition)`. `model_partition` should stay the opaque freshness partition that ADR 032 defines; the registry proposed here would only move alias, validation, and runner-default metadata out of Python code and into review configuration/state.

This is a later simplification, not a requirement for the queued-job pipeline. Jobs can store both `model_partition` and nullable `runner_model` without a partition table.

## Current state (as of 2026-06-30)

ADR 032 defines `model_partition` as a declared, frozen model-side freshness partition. Freshness treats it as opaque: a partition can be exact, coarse, or parameterized, but telemetry must not re-key review state after execution.

The current alias registry is in code. `src/commonplace/review/review_model.py` defines `MODEL_PARTITION_REGISTRY`, builds `MODEL_PARTITION_ALIASES`, and exposes helpers such as `normalize_model_partition` and `build_model_partition`.

Existing subprocess paths already distinguish the declared partition from the concrete runner model in places: commands normalize the user-supplied model into a `model_partition`, but pass a `runner_model` value to runner adapters.

ADR 034 shipped the queued-job design without adopting this registry: `review_jobs.model_partition` is the freshness key, `review_jobs.runner_model` is nullable execution metadata, and there is no `model_partitions`, `model_partition_aliases`, or `model_partition_runner_models` table in the review schema.

## Proposed shape

Add registry tables only when alias/default management becomes operational friction:

```sql
model_partitions (
    model_partition TEXT PRIMARY KEY,
    description TEXT,
    created_at TEXT NOT NULL
)

model_partition_aliases (
    alias TEXT PRIMARY KEY,
    model_partition TEXT NOT NULL REFERENCES model_partitions(model_partition)
)

model_partition_runner_models (
    model_partition TEXT NOT NULL REFERENCES model_partitions(model_partition),
    runner TEXT NOT NULL,
    runner_model TEXT NOT NULL,
    PRIMARY KEY (model_partition, runner)
)
```

Job creation may use `model_partition_runner_models` to choose a default runner model for a `(model_partition, runner)` pair. It must still store the resolved `runner_model` on the job. Changing registry defaults later must not mutate old jobs or accepted review identity.

## Forces

- `model_partition` is identity, not necessarily a literal model name.
- Runner defaults are operational configuration, so changing them must not re-key existing reviews.
- The current code registry is simple and visible, but adding aliases or defaults requires a package change.
- A strict foreign-key registry improves validation but can block ad-hoc partitions that ADR 032 explicitly permits.
- Automatically inserting unknown partitions preserves ad-hoc use but weakens validation unless those rows are marked as unverified or user-created.

## Non-goals

- Do not derive acceptance identity from telemetry.
- Do not re-key existing jobs, job items, or acceptance rows when registry defaults change.
- Do not require this table for the queued-job refactor.
- Do not make `runner_model` part of freshness identity.

## Open choices

- Should unknown partitions be rejected, auto-inserted, or accepted with a warning?
- Are per-runner default models required configuration, advisory suggestions, or only a CLI convenience?
- Should registry changes be managed by review DB migrations, a dedicated CLI, or a project config file that syncs into SQLite?
- Should aliases be immutable once used by an acceptance row?

## Adoption criteria

Adopt this when the in-code alias registry or runner-default mapping becomes operational friction: multiple projects need different defaults, operators need to add aliases without a package release, or job creation needs validated defaults for more than one runner.

---

Relevant Notes:

- [032-review freshness uses DB snapshots, not Git](../adr/032-review-freshness-uses-db-snapshots-not-git.md) — see-also: establishes `model_partition` as an opaque freshness partition rather than observed telemetry identity
- [Review architecture](../review-architecture.md) — part-of: review-state architecture that would host the registry if adopted
