# Deferred general lineage refresh state design

This is the weight-3 contingency design for a future second lineage mesh. It is **not** the current implementation plan. Review keeps its purpose-built SQLite store; every other present case remains at artifact-local metadata, stable source handles, report contracts, or commit history until it develops churning many-to-many edge state plus a real selector or audit query.

If that trigger appears, the design takes the review system's storage lesson as the starting point: keep SQLite for operational lineage state, keep Markdown files as the primary artifact API, and keep refresh execution outside the lineage subsystem. The resulting hybrid would preserve two properties:

- agents and maintainers still read and edit ordinary markdown artifacts;
- automation gets an indexed state store for dependency freshness, current baselines, auditable events, and model-aware derivations.

Until then, this file is a schema and boundary sketch to test the general vocabulary. It must not be cited as evidence that a generic lineage database has been approved or earned.

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
- auditable lineage events when a cross-class history is required;
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

If a cross-class event surface is built, lineage history should be append-only at that event layer. This is a proposed audit model, not a description of current review storage: review acceptance is now a current-state upsert with inline pruning of superseded evidence.

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

The generic current baseline would be derived from accepted events according to the target kind's ordering rule. Current review reaches a similar selector result through the `acceptance` current-state table and guarded `current_gate_acceptances` view, not through an append-only acceptance-event log.

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
| `review_jobs` | review-specific invocation, packing, status, and optional execution provenance |
| `review_pairs` | review-specific requested pair, decision, and completed evidence row |
| `acceptance` | current baseline for review-pair targets; successful writes upsert by the full key |
| `current_gate_acceptances` | guarded current baseline view, restricted to completed jobs with decisions |
| accepted note snapshot hash | input version with role `source` |
| accepted gate snapshot hash | input version with role `gate` |
| `review_jobs.model_partition` / `acceptance.model_partition` | target partition; literal runner model and telemetry are producer evidence |

This is a conceptual mapping, not a migration plan. Review already separates execution concerns from freshness APIs while keeping both in one purpose-built store. Its accepted baseline and stale selector over `(note_path, gate_path, model_partition)` remain the first implementation witness for the general target/input vocabulary.

Recent conformance work also limits how much generic input machinery review needs. Type specs and `COLLECTION.md` contracts become the gate document in separate factored `(note, dependency)` pairs. The default answer to another review dependency is another pair with that dependency on the gate side, not a wider N-input target. A generic lineage input set is for derivations that cannot honestly factor into independent pairs.

## Batch Isolation

Batch processing is an optimization over stale targets. It should remain replaceable.

A future review flow might:

1. ask lineage for stale `review-pair` targets;
2. group targets by gate, note, token budget, model, or external executor constraints;
3. run any number of batches;
4. parse outputs into review-specific result rows and markdown artifacts;
5. record accepted baselines for the completed targets using that subsystem's chosen semantics.

The lineage store only needs steps 1 and 5. Everything between them can change as the system learns better packing, routing, model choice, or delegation.

This boundary may fit connect reports, source comparisons, generated indexes, and merge-back edits if any of them later earns swept freshness state. Their current forms do not.

## SQLite Shape

Once a second churning mesh meets the escalation trigger, a generic layer could start with a small table set separate from the review schema:

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

This is not a full implementation proposal. The design constraint is more important than the exact table names: any future generic lineage tables should represent targets, events, and accepted dependency versions; type-specific systems should own their report bodies, parsing, prompts, and execution provenance. Do not fold review into these tables merely to make the abstraction look uniform.

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

## Storage Policy If Escalated

If built, the SQLite lineage store would be the canonical freshness index for the target kinds explicitly registered in it. Markdown artifacts would remain the canonical human-readable outputs when the artifact itself is retained. Unregistered artifact classes would continue to use their lighter existing carriers.

Default policy:

- commit authored source and canonical library files;
- commit retained generated reports only when they are durable evidence, reviewable output, or intentionally reusable context;
- keep cheap, bulky, or transient run artifacts out of git unless their type contract says otherwise;
- keep lineage DB local operational state by default, with export/import or migration tools if a future workflow needs shared lineage state.

This keeps the experiment surface open without pre-registering every derived artifact class in a database.

## Refresh Lifecycle If Escalated

The candidate generic lifecycle:

1. Discover targets from file contracts, type contracts, or explicit registration.
2. Resolve current input versions.
3. Compare current inputs with latest accepted lineage event.
4. Emit refresh targets with reasons.
5. Let a runner, command, agent, or human process those targets.
6. On accepted output, append lineage event and dependency versions.
7. Optional: write or update retained markdown artifacts.
8. Optional: export audit reports from the lineage DB.

This would make refresh automation more bitter-lesson-compatible without binding the lineage system to any particular batch processor.

## Open Questions

- What concrete second churning mesh and selector would be sufficient to activate this design?
- If activated, should the generic lineage DB be separate from the purpose-built review store?
- Which target kinds need model as part of the target partition, and which only need model as event provenance?
- Which generated markdown types should carry lineage pointers in frontmatter?
- How should local lineage DB state be backed up or shared when multiple agents operate on the same repo?
- Is ordinary commit history sufficient for merge-back provenance, and what query would justify a shared append-only event surface?
