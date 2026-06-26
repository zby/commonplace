# General lineage refresh state design

This design takes the review system's storage lesson as the starting point: keep SQLite for lineage state, keep markdown files as the primary artifact API, and keep refresh execution outside the lineage subsystem.

The result is a hybrid system. It is less clean than "everything is files," but it gives Commonplace the two properties it needs for experimentation:

- agents and maintainers still read and edit ordinary markdown artifacts;
- automation gets a real indexed state store for dependency freshness, current baselines, append-only events, and model-aware derivations.

## Core Boundary

The lineage system answers:

> What retained artifacts, derivations, or artifact relations are stale, missing, acknowledged, retired, or current, and why?

It does not answer:

> Which runner, batch shape, prompt packing, queue, model invocation, or merge procedure should perform the refresh?

That boundary matters because the same stale target may be refreshed by a live agent, a batch sweep, an external orchestrator, a one-off command, a manual merge, or a trivial acknowledgement. Lineage state should survive changes in execution strategy.

## Responsibilities

In scope for the lineage layer:

- stable identities for lineage targets;
- accepted baselines for target dependencies;
- append-only lineage events;
- current-state views;
- stale/missing/retired selectors;
- dependency resolvers that can observe current versions;
- producer provenance, including model where it matters;
- machine-readable reasons that a target needs attention.

Out of scope for the lineage layer:

- prompt rendering;
- batch packing;
- runner adapters;
- queue scheduling;
- parallelism;
- retry policy;
- report parsing beyond accepted output metadata;
- applying merge-back edits;
- deciding whether a stale target should be fixed now.

Refresh tools consume lineage targets and later report accepted outcomes back to the lineage store.

## Primary API Remains Markdown

Markdown remains the authoring and inspection API:

- notes, sources, gates, type specs, instructions, reviews, connect reports, and generated analysis reports are still files;
- report types still define the readable shape of their markdown output;
- skills and commands still write or revise markdown artifacts;
- canonical notes do not become "DB records with prose payloads."

SQLite stores the operational relation that markdown files do not naturally own: which derivation was accepted, which inputs it depended on, which versions were observed, which model or producer made it, and whether those inputs still match.

Some generated markdown files should still carry self-describing frontmatter, especially one-shot derivatives that may be read outside the local DB. That frontmatter is an artifact API. It is not the freshness index.

## Target Model

A lineage target is the thing whose freshness can be asked.

Examples:

| target kind | logical key | why it needs lineage |
|---|---|---|
| review pair | `note_path`, `gate_path`, `model_partition` | accepted review freshness depends on note path, gate note path, and model partition |
| connect report | source artifact path, report contract, optional model | report depends on source artifact and current KB context |
| agent-memory-system review | review file path, external repo URL, reviewed revision, optional model | source is an external git repository, not a KB snapshot |
| generated index | index path, index contract | deterministic copy of library state should be checked or rebuilt |
| merge-back event | canonical artifact path, source report/event ids | canonical artifact was revised from previous version plus generated evidence |
| ad-hoc distillation | retained packet path or id, source set, prompt/spec | retained one-off source shaping may later need promotion or refresh |

The target key should be stable enough for lookup, but not pretend every target has the same shape. Store target keys as structured data, not concatenated strings. Review's `(note_path, gate_path, model_partition)` key is the first path-keyed target-kind schema, not the universal schema. `gate_path` is the gate note's repo-relative path; shorthands such as `prose/source-residue` are display or CLI conveniences, not the persisted identity.

## Event Model

Lineage should be append-only at the event layer.

Core event fields:

| field | role |
|---|---|
| `target_kind` / `target_key` | what freshness target this event updates |
| `event_kind` | `full-refresh`, `ack`, `merge-back`, `manual-override`, `migration-import`, `retire` |
| `output_ref` | file path, DB row, external revision, or null for pure ack |
| `operation_kind` | review, connect, source-ingest, index-build, merge-back, ad-hoc-distillation |
| `producer` | command, skill, agent, migration, or human operator |
| `model_partition` | declared model-side partition when the target or event is model-specific |
| `producer_model` | optional literal observed model, when available after execution |
| `accepted_at` | when this event became the accepted baseline |
| `inputs` | accepted dependency versions used for freshness checks |

The current baseline is the latest accepted event for a target according to the target kind's ordering rule. Review already uses this pattern through `acceptance_events` and `current_gate_acceptances`.

## Input Version Model

Each event records the dependency versions that made the accepted output valid.

Input records should include:

| field | examples |
|---|---|
| `input_kind` | `kb-file`, `review-gate`, `external-git-repo`, `source-snapshot`, `schema`, `prompt-contract`, `model-partition`, `db-row` |
| `input_key` | path, repo URL, schema id, prompt contract id |
| `role` | source, gate, contract, context, model, previous-output, previous-canonical |
| `version_kind` | content hash, git blob sha, package asset hash, source hash, semantic version, DB schema version |
| `accepted_version` | the version observed when the event was accepted |
| `snapshot_ref` | optional DB snapshot id or retained source path for the accepted input |

Freshness is computed by resolving the current version for each input and comparing it with `accepted_version`. The lineage store records accepted versions; resolver code observes current versions.

That resolver layer is deliberately narrower than a refresh runner. A resolver can say "this gate blob changed." It should not decide how to rerun the review.

Resolvers should be typed and substrate-specific. For local review inputs, the resolver should be `file-content`: hash canonical bytes and store the reviewed bytes in the lineage DB. A `package-asset` resolver can provide package version plus asset hash. Source-oriented target kinds may still refer to external Git repositories when the external source itself is Git-backed, but local review freshness should not depend on the user's Git checkout. The lineage store should record which resolver produced the accepted version so installed projects are not forced into Commonplace's local Git commit discipline.

The general lineage layer should not own diffing. Diffs are an explainer feature for particular domains, especially reviews. A review explainer can compare current text with stored input snapshots when it wants to show what changed. The lineage selector should remain useful when it only reports that an input version differs.

## Selector Contract

The lineage selector returns refresh targets, not jobs.

A target returned by the selector should contain:

- `target_kind`;
- structured `target_key`;
- `reason`: `missing`, `input-changed`, `output-missing`, `contract-changed`, `retired-source`, `manual-refresh-requested`;
- changed inputs with accepted and current versions;
- latest accepted event id, if any;
- output reference, if any;
- producer/model partition information needed to interpret the target;
- optional human-readable summary.

It should not contain:

- batch id;
- runner command;
- prompt path;
- concurrency settings;
- queue priority beyond a neutral severity or urgency hint;
- assumptions about whether refresh will be note-packed, gate-packed, source-packed, or manually merged.

Batch processors, review sweeps, and future orchestrators consume this selector output and choose an execution plan outside the lineage layer.

## Review Mapping

The current review subsystem can be mapped into the general model without forcing an immediate rewrite:

| current review concept | general lineage concept |
|---|---|
| `(note_path, gate_path, model_partition)` | lineage target of kind `review-pair` |
| `review_pairs` | review-specific output/provenance rows |
| `acceptance_events` | lineage events for review-pair targets |
| `current_gate_acceptances` | current baseline view for review-pair targets |
| accepted note snapshot hash | input version with role `source` |
| accepted gate snapshot hash | input version with role `gate` |
| `model_partition` | target partition; literal model telemetry is producer evidence |
| `review_runs` | execution provenance, not the identity of freshness |

The important migration is conceptual first: review batch tables and review freshness tables should not be treated as one inseparable subsystem. `review_runs` may remain review-specific execution provenance. The lineage part is the accepted baseline and stale selector over `(note_path, gate_path, model_partition)`. That is the first implementation of the general target/event/input pattern, specialized to two KB file inputs.

## Batch Isolation

Batch processing is an optimization over stale targets. It should remain replaceable.

A future review flow might:

1. ask lineage for stale `review-pair` targets;
2. group targets by gate, note, token budget, model, or external executor constraints;
3. run any number of batches;
4. parse outputs into review-specific result rows and markdown artifacts;
5. append accepted lineage events for the targets that actually completed.

The lineage store only needs steps 1 and 5. Everything between them can change as the system learns better packing, routing, model choice, or delegation.

This same shape also fits connect reports, source comparisons, generated indexes, and merge-back edits.

## SQLite Shape

The generic layer can start with a small table set beside or beneath the review DB:

```text
lineage_targets
  target_id
  target_kind
  target_key_json
  target_partition_json
  primary_artifact_path
  status

lineage_events
  event_id
  target_id
  event_kind
  operation_kind
  output_ref_json
  producer
  model_partition
  producer_model
  accepted_at
  note

lineage_input_snapshots
  snapshot_id
  content_hash
  media_type
  content
  created_at

lineage_event_inputs
  event_id
  input_kind
  input_key
  role
  resolver
  version_kind
  accepted_version
  snapshot_id
  provenance_ref_json
  policy_mode

current_lineage_baselines
  view: latest accepted event per target
```

This is not a full implementation proposal yet. The design constraint is more important than the exact table names: generic lineage tables should represent targets, events, and accepted dependency versions; type-specific systems should own their report bodies, parsing, prompts, and execution provenance.

## Markdown Integration

For generated artifacts that are retained as files, frontmatter can include a compact pointer back to lineage state:

```yaml
lineage:
  target_kind: review-pair
  event_id: 12345
  model_partition: claude-opus-4-6
```

For canonical authored notes, do not write "last model" frontmatter. If a note is changed by merge-back from a report, the lineage event should record:

- previous note version;
- source report or review event;
- source material/context used;
- accepting operator or producer;
- optional commit id once committed.

The note remains the canonical artifact. The derivative fact lives at the update-event layer.

## Storage Policy

The SQLite lineage store should be the canonical freshness index. Markdown artifacts remain the canonical human-readable outputs when the artifact itself is retained.

Default policy:

- commit authored source and canonical library files;
- commit retained generated reports only when they are durable evidence, reviewable output, or intentionally reusable context;
- keep cheap, bulky, or transient run artifacts out of git unless their type contract says otherwise;
- keep lineage DB local operational state by default, with export/import or migration tools if a future workflow needs shared lineage state.

This keeps the experiment surface open: Commonplace can add new derived artifact classes without immediately deciding that every intermediate report is either a library artifact or disposable scratch.

## Refresh Lifecycle

The generic lifecycle:

1. Discover targets from file contracts, type contracts, or explicit registration.
2. Resolve current input versions.
3. Compare current inputs with latest accepted lineage event.
4. Emit refresh targets with reasons.
5. Let a runner, command, agent, or human process those targets.
6. On accepted output, append lineage event and dependency versions.
7. Optional: write or update retained markdown artifacts.
8. Optional: export audit reports from the lineage DB.

This makes refresh automation more bitter-lesson-compatible without binding the lineage system to any particular batch processor.

## Open Questions

- Should the general lineage DB be the same SQLite file as review state, or a new `kb/reports/lineage-store.sqlite` with review-specific tables gradually folded in?
- Which target kinds need model as part of the target partition, and which only need model as event provenance?
- Which generated markdown types should carry lineage pointers in frontmatter?
- How much of the current review table shape should be retained after the snapshot migration, given that legacy SHA/commit fields are copied and dropped rather than preserved through compatibility views?
- How should local lineage DB state be backed up or shared when multiple agents operate on the same repo?
- Which selectors should be built first after review: connect report staleness, generated index freshness, or merge-back provenance?
