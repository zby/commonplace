# Review lineage storage case

The review subsystem is the strongest local example of lineage leaving git-backed prose while the reviewed artifacts remain markdown. It should be studied separately because it may be the prototype for all automatic artifact lineage, or it may reveal the boundary where a database is justified.

## Current Shape

Review content and review lineage are split:

- notes and gates are canonical markdown files in git;
- review runs are prompt invocations;
- review pairs are the requested `(note_path, gate_id)` units inside a run;
- review markdown files and bundle outputs remain readable generated artifacts;
- SQLite stores canonical lineage, freshness, and acceptance state;
- selectors compare current note/gate SHAs against the latest accepted baseline for `(note_path, gate_id, model_id)`.

The core SQLite concepts are:

| concept | current role |
|---|---|
| `review_runs` | one prompt invocation, with runner, model, packing, status, telemetry/debug/raw output |
| `review_pairs` | one requested and possibly completed `(note, gate)` review inside a run, with status, decision, rationale, evidence, note/gate SHAs |
| `acceptance_events` | append-only accepted baseline events for selector and ack behavior |
| `current_gate_acceptances` | latest acceptance per `(note, gate, model)` key |
| `MANIFEST.json` | per-run filesystem artifact that maps pairs to prompt/output/result paths |

The important point is not "reviews use SQLite." The important point is why: review lineage became operational state. The system needed indexed current-state lookup, append-only events, stale selectors, pair-level partial success, model partitions, and ack without rewriting prose artifacts.

## Requirements Any Port Must Preserve

A file-backed replacement must preserve these behaviors:

- **Pair identity**: every stored result is keyed by `(note_path, gate_id, model_id)` plus the run that produced it.
- **Input provenance**: reviewed note SHA, reviewed note commit when available, and gate SHA are the exact inputs used during review generation.
- **Append-only acceptance**: full review, trivial ack, migration import, manual override, and future acceptance kinds should be events, not silent rewrites.
- **Current acceptance**: selector needs the latest accepted baseline per `(note, gate, model)`.
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
model_id: claude-3-5-sonnet-xhigh
runner: codex
started_at: "2026-06-23T10:15:00Z"
completed_at: "2026-06-23T10:22:00Z"
status: completed
packing: note
pairs:
  - review_pair_id: 891
    note_path: kb/notes/example.md
    gate_id: prose/source-residue
    status: completed
    decision: warn
    reviewed_note_sha: abc123
    reviewed_note_commit: deadbeef
    gate_sha: def456
    result_path: pairs/prose__source-residue.md
```

Each pair markdown file would hold readable review prose plus frontmatter for the pair fields that automation consumes. Acceptance would live in an append-only ledger, for example `kb/reports/reviews/acceptance-events.jsonl`:

```json
{"event_id":1,"note_path":"kb/notes/example.md","gate_id":"prose/source-residue","model_id":"claude-3-5-sonnet-xhigh","accepted_review_pair_id":891,"accepted_note_sha":"abc123","accepted_gate_sha":"def456","accepted_at":"2026-06-23T10:22:00Z","acceptance_kind":"full-review"}
{"event_id":2,"note_path":"kb/notes/example.md","gate_id":"prose/source-residue","model_id":"claude-3-5-sonnet-xhigh","accepted_review_pair_id":null,"accepted_note_sha":"abc999","accepted_gate_sha":"def456","accepted_at":"2026-06-24T09:00:00Z","acceptance_kind":"trivial-change-ack"}
```

Selector would derive current acceptance by reading the latest event per `(note_path, gate_id, model_id)`. For scale, it would likely build a gitignored cache such as `current-acceptances.sqlite` or `current-acceptances.json`.

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
      accepted_note_sha: abc999
      accepted_gate_sha: def456
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

The database is not intrinsically required by review lineage. What is required is a separation between:

1. **readable review prose**;
2. **run/pair provenance**;
3. **append-only acceptance events**;
4. **fast current-state selectors**.

SQLite satisfies all four in one operational store. Bare markdown alone satisfies only the first. Markdown plus YAML/JSON manifests can satisfy the second and third. A generated cache or database-like index is still needed for the fourth once review volume grows.

The likely file-backed design, if we port, is:

- per-run `RUN.yaml` or `MANIFEST.json` as the canonical run/pair manifest;
- per-pair markdown files with frontmatter for consumed metadata;
- append-only `acceptance-events.jsonl` or event YAML files;
- gitignored generated current-state index for selectors;
- an explicit rebuild/check command that proves the current index matches the event source.

That design would make the review lineage case more portable to other artifact classes. The same pattern could store merge-back events, derived-analysis refreshes, compiled-view rebuilds, and ad-hoc distillation promotions without forcing all lineage into frontmatter.

## Open Questions

- Should acceptance events be committed, gitignored, or local-only like the current review DB?
- If events are committed, how much review churn is acceptable?
- Is path rewriting on note relocation acceptable, or should lineage use stable artifact ids?
- Should current-state indexes be generated and checked, or should the event ledger itself be the only source?
- Is JSONL sufficient, or do review events need YAML/Markdown for human review?
- Could this become one generic artifact-lineage ledger instead of a review-specific port?
