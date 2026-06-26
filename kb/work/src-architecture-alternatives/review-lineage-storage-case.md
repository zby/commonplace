# Review lineage storage case

The review subsystem is the strongest local example of lineage leaving git-backed prose while the reviewed artifacts remain markdown. It should be studied separately because it witnesses the boundary named in `kb/notes/many-to-many-edge-state-is-where-files-yield-to-a-database.md`: churning state on an ownerless many-to-many edge. The base witness is the reviewed-note-path x gate-note-path relation; the current implementation also partitions that edge by model.

## Current Shape

Review content and review lineage are split:

- notes and gates are canonical markdown files in git;
- review runs are prompt invocations;
- review pairs are the requested `(note_path, gate_path)` units inside a run;
- review markdown files and bundle outputs remain readable generated artifacts;
- SQLite stores canonical lineage, freshness, and acceptance state;
- selectors compare current note/gate content hashes against the latest accepted baseline for `(note_path, gate_path, model_partition)`.

The storage-driving relation is `note_path x gate_path`: only the reviewed note and the gate note are markdown endpoints, and the churning state belongs to their edge. The current implementation adds `model_partition` as a partition of that edge state, stored in DB lineage state (`review_runs`, `review_pairs`, and `acceptance_events`), not in the note file or the gate file. A review by one model partition does not satisfy freshness for another model partition. This current DB placement does not preclude also writing model provenance into rendered review artifact frontmatter if review reports need to be self-describing outside the DB.

The core SQLite concepts are:

| concept | current role |
|---|---|
| `review_runs` | one prompt invocation, with runner, model partition, packing, status, telemetry/debug/raw output |
| `review_pairs` | one requested and possibly completed `(note, gate)` review inside a run, with model partition, status, decision, rationale, evidence, current note/gate fingerprints |
| `acceptance_events` | append-only accepted baseline events for selector and ack behavior, partitioned by model |
| `current_gate_acceptances` | latest acceptance per `(note_path, gate_path, model_partition)` key |
| `MANIFEST.json` | per-run filesystem artifact that maps pairs to prompt/output/result paths |

The important point is not "reviews use SQLite." The important point is why: review lineage became operational edge-state. The system needed indexed current-state lookup, append-only events, stale selectors, pair-level partial success, model partitions, and ack without rewriting prose artifacts. A filesystem edge-file design could represent this relation, but it would still be a hand-built relational store.

## Requirements Any Port Must Preserve

A file-backed replacement must preserve these behaviors:

- **Pair identity plus model partition**: every stored result is keyed by `(note_path, gate_path, model_partition)` plus the run that produced it. The `model_partition` is lineage state, not metadata on the note or gate.
- **Input provenance**: the system must know the exact note and gate content used during review generation. The chosen direction is DB-owned input snapshots, not Git commit retrieval.
- **Append-only acceptance**: full review, trivial ack, migration import, manual override, and future acceptance kinds should be events, not silent rewrites.
- **Current acceptance**: selector needs the latest accepted baseline per `(note_path, gate_path, model_partition)`.
- **Partial run state**: a run can complete some pairs and miss others; completed pairs must remain usable.
- **Readable review body**: humans and agents still need markdown for findings, rationale, and suggested revisions.
- **Model partitioning**: one model's acceptance does not make another model's review fresh.
- **Relocation support**: note renames need to update or resolve lineage records.
- **Warn/fix queue**: current accepted warning reviews must be discoverable without reading every stale or obsolete artifact.
- **Pruning/retirement**: obsolete runs and superseded review pairs need a cleanup story.

Pure prose files do not naturally provide these. A bare-MD port therefore needs manifests, ledgers, or generated indexes.

## File-Backed Candidate A: Run Directories Plus Event Ledger

Keep each run as a directory under `kb/reports/bundle-reviews/review-run-<id>/`:

```text
review-run-123/
  RUN.yaml
  prompt.md
  bundle-output.md
  pairs/
    prose__source-residue.md
    semantic__internal-consistency.md
```

`RUN.yaml` would replace the run/pair rows for that invocation:

```yaml
schema: review-run-v1
review_run_id: 123
model_partition: claude-3-5-sonnet-xhigh
runner: codex
started_at: "2026-06-23T10:15:00Z"
completed_at: "2026-06-23T10:22:00Z"
status: completed
packing: note
pairs:
  - review_pair_id: 891
    note_path: kb/notes/example.md
    gate_path: kb/instructions/review-gates/prose/source-residue.md
    status: completed
    decision: warn
    reviewed_note_hash: abc123
    reviewed_note_commit: deadbeef
    gate_hash: def456
    result_path: pairs/prose__source-residue.md
```

Each pair markdown file would hold readable review prose plus frontmatter for the pair fields that automation consumes. Acceptance would live in an append-only ledger, for example `kb/reports/reviews/acceptance-events.jsonl`:

```json
{"event_id":1,"note_path":"kb/notes/example.md","gate_path":"kb/instructions/review-gates/prose/source-residue.md","model_partition":"claude-3-5-sonnet-xhigh","accepted_review_pair_id":891,"accepted_note_hash":"abc123","accepted_gate_hash":"def456","accepted_at":"2026-06-23T10:22:00Z","acceptance_kind":"full-review"}
{"event_id":2,"note_path":"kb/notes/example.md","gate_path":"kb/instructions/review-gates/prose/source-residue.md","model_partition":"claude-3-5-sonnet-xhigh","accepted_review_pair_id":null,"accepted_note_hash":"abc999","accepted_gate_hash":"def456","accepted_at":"2026-06-24T09:00:00Z","acceptance_kind":"trivial-change-ack"}
```

Selector would derive current acceptance by reading the latest event per `(note_path, gate_path, model_partition)`. For scale, it would likely build a gitignored cache such as `current-acceptances.sqlite` or `current-acceptances.json`.

Pros:

- preserves append-only acceptance;
- keeps run artifacts inspectable;
- can be committed or ignored per retention policy;
- ports cleanly to artifact-lineage events beyond reviews.

Costs:

- selector must scan ledgers or maintain a generated cache;
- concurrent writes and event ids need care;
- note relocation needs ledger rewrite, aliasing, or a path-indirection layer;
- JSONL is machine-friendly but less pleasant for humans than SQLite queries.

## File-Backed Candidate B: Per-Artifact Current Manifests

Store current acceptance near the reviewed artifact or in a mirror tree:

```text
kb/reports/reviews/current/notes/example.yaml
```

```yaml
note_path: kb/notes/example.md
gates:
  prose/source-residue:
    claude-3-5-sonnet-xhigh:
      accepted_note_hash: abc999
      accepted_gate_hash: def456
      accepted_at: "2026-06-24T09:00:00Z"
      acceptance_kind: trivial-change-ack
      accepted_review_pair_id: null
```

Run directories and pair markdown remain as in Candidate A, but the selector reads a current manifest rather than deriving latest events.

Pros:

- selector is simple and fast;
- files are small and local to the reviewed artifact;
- easier to inspect current freshness at a glance.

Costs:

- ack rewrites current-state files, recreating the metadata-rewrite problem ADR 010 tried to remove;
- history is split between git history and run outputs unless an event ledger also exists;
- conflict risk rises when many gates or models update the same note manifest;
- stale current manifests become another derived copy that needs checking.

This option may be acceptable for low-volume artifact classes, but it is a weaker fit for high-churn review state.

## File-Backed Candidate C: Markdown Events With Generated Index

Represent each acceptance event as a small markdown or YAML file:

```text
kb/reports/reviews/events/2026/06/23/000123-full-review.yaml
```

Then generate a current-state index for selectors:

```text
kb/reports/reviews/current-acceptances.sqlite
```

or:

```text
kb/reports/reviews/current-acceptances.json
```

Pros:

- event files are append-only and individually inspectable;
- current-state lookup remains fast through a generated index;
- the generated index can be gitignored and rebuilt.

Costs:

- this recreates SQLite as a derived index over files;
- correctness now depends on index rebuild discipline;
- many tiny files may be worse than one ledger for git and filesystem performance.

This is the closest "bare files plus cache" analogue to the current DB. It may be valuable if git-auditable event files matter more than simple operational storage.

## Assessment

Workshop decision: keep SQLite as the lineage state substrate for review-like edge state. The file-backed candidates remain useful because they show which relations the DB must represent, but they are not the preferred production direction for the current review system.

The database is not intrinsically required for every part of review lineage. What is required is a separation between:

1. **readable review prose**;
2. **run/pair provenance**;
3. **append-only acceptance events**;
4. **fast current-state selectors**.

SQLite satisfies all four in one operational store. Bare markdown alone satisfies only the first. Markdown plus YAML/JSON manifests can satisfy the second and third. A generated cache or database-like index is still needed for the fourth once review volume grows, because the selector is maintaining current state over `note × gate` edges, partitioned by model. That is the relational edge-state part, and it is the part likely to reappear in any complex automatic dependency-maintenance mechanism. The implementation could be edge files at low volume; SQLite is the current real-DB answer.

The review freshness decoupling decision moves input baselines into SQLite. The current Git blob/commit fields couple review correctness to the user's VCS workflow. A self-contained review store hashes note and gate content itself, stores reviewed input snapshots once by content hash, and uses those DB-owned snapshots for freshness and optional review diffs.

The likely file-backed design, if we port, is:

- per-run `RUN.yaml` or `MANIFEST.json` as the canonical run/pair manifest;
- per-pair markdown files with frontmatter for consumed metadata;
- append-only `acceptance-events.jsonl` or event YAML files;
- gitignored generated current-state index for selectors;
- an explicit rebuild/check command that proves the current index matches the event source.

That design would make the review lineage case more portable to other artifact classes, but the current direction is to make SQLite the shared lineage layer instead: markdown artifacts remain readable outputs and authoring surfaces, while the DB owns accepted baselines, freshness selectors, and append-only lineage events. The same generic lineage pattern should store merge-back events, derived-analysis refreshes, compiled-view rebuilds, and ad-hoc distillation promotions without forcing all lineage into frontmatter.

The generalization should not absorb review batch execution. `review_runs` and prompt packing are execution provenance and optimization choices. The reusable lineage core is the target/event/input relation: what target was accepted, what it depended on, what model or producer created it, and whether those dependencies are still current.

## Open Questions

- Should acceptance events be committed, gitignored, or local-only like the current review DB?
- If events are committed, how much review churn is acceptable?
- Is path rewriting on note relocation acceptable, or should lineage use stable artifact ids?
- Should current-state indexes be generated and checked, or should the event ledger itself be the only source?
- Is JSONL sufficient, or do review events need YAML/Markdown for human review?
- Could this become one generic artifact-lineage ledger instead of a review-specific port?
