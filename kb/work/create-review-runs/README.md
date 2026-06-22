# Workshop: create-review-runs

Goal: design a shared review-run preparation layer that creates review runs and canonical prompts for different packing strategies without duplicating setup logic across review commands.

## Problem

The review system already has one pair protocol: the unit of work is `(note_path, gate_id)`, and prompts request one sentinel-delimited block per pair.

The current command surface has multiple ways to prepare those pairs:

- `commonplace-create-review-run` — live-agent path for one note and many gates.
- `commonplace-run-review-bundle` — subprocess path for one note and many gates.
- `commonplace-run-gate-sweep` — subprocess path for one gate across many notes.
- `commonplace-prepare-review-batch` — external-executor path for arbitrary pairs.

The issue is not prompt rendering itself; `render_pairs_prompt(...)` is already shared. The issue is the layer before it: resolving notes and gates, creating one or more `review_runs`, assigning artifact paths, preparing `NoteReviewTarget`s, and returning enough structured data for either a subprocess runner or a live/external executor.

## Design target

Create a library-level preparation API, tentatively named `create_review_runs`, that owns:

- resolving gate ids from explicit gates or bundles;
- filtering gates by note type and traits;
- reading note and gate provenance;
- creating `review_runs` plus requested `review_pairs`;
- preparing `NoteReviewTarget`s;
- assigning artifact paths;
- rendering a canonical prompt when requested.

The API should support multiple packing strategies over the same pair model.

## API direction

Input may be an arbitrary list of selected pairs:

```text
kb/notes/foo.md::semantic/explanatory-reach
kb/notes/foo.md::compression/marginal-value-redundancy
kb/notes/bar.md::semantic/explanatory-reach
```

But arbitrary pairs are only a **selection format**, not an execution format. Prompt execution should have exactly two packing strategies:

- `pack_by=note`
- `pack_by=gate`

The preparation layer groups the selected pairs according to the chosen packing strategy and returns a flat list of review runs. Runs that share a prompt share the same prompt and output paths.

## Strategy 1: pack by note

Use when one note should be reviewed by many gate bundles.

Input shape:

```text
note: kb/notes/foo.md
gate bundles: semantic, prose, compression
batch_size: N
```

Pair shape:

```text
foo.md :: semantic/explanatory-reach
foo.md :: semantic/internal-consistency
foo.md :: prose/source-residue
foo.md :: compression/marginal-value-redundancy
...
```

Run shape:

- one `review_run` per prompt invocation;
- many `review_pairs`;
- one artifact directory per run: `kb/reports/bundle-reviews/review-run-{id}/`;
- the run records its `prompt_path`, `bundle_output_path`, and selected gate bundles;
- one prompt containing one note and up to `batch_size` gate bundles can be derived from runs with the same `prompt_path`.

Current users:

- `commonplace-create-review-run --with-prompt`
- `commonplace-run-review-bundle`

## Strategy 2: pack by gate

Use when one gate should be run across many notes.

Input shape:

```text
gate: compression/marginal-value-redundancy
notes: kb/notes/foo.md, kb/notes/bar.md, ...
batch_size: N
```

Pair shape:

```text
foo.md :: compression/marginal-value-redundancy
bar.md :: compression/marginal-value-redundancy
...
```

Run shape:

- one `review_run` per prompt batch;
- each run has one `review_pair` per note under that gate;
- each run records its `prompt_path` and `bundle_output_path`;
- one prompt may include several notes by grouping runs with the same `prompt_path`;
- each prompt batch has one run id and one run artifact directory.

Current user:

- `commonplace-run-gate-sweep`

## Rejected strategy: arbitrary sparse pair prompt

Do not keep arbitrary sparse pair batching as a public execution shape.

Example selected pairs:

```text
kb/notes/foo.md::semantic/explanatory-reach
kb/notes/foo.md::compression/marginal-value-redundancy
kb/notes/bar.md::prose/source-residue
```

The old arbitrary-pair prompt shape would put multiple notes and unrelated gates into one sparse matrix prompt. That is flexible but cognitively noisy: the reviewer must switch both note context and gate lens in one call.

Instead, use the same selected pairs but choose a packing:

### `pack_by=note`

```text
Prompt 1: foo.md with semantic/explanatory-reach + compression/marginal-value-redundancy
Prompt 2: bar.md with prose/source-residue
```

With `batch_size=1`, `foo.md` would instead get one prompt for the `semantic` bundle and one prompt for the `compression` bundle.

### `pack_by=gate`

```text
Prompt 1: semantic/explanatory-reach over foo.md
Prompt 2: compression/marginal-value-redundancy over foo.md
Prompt 3: prose/source-residue over bar.md
```

For `pack_by=gate`, each prompt may contain up to `batch_size` notes for the same gate, defaulting to 5.
For `pack_by=note`, each prompt may contain up to `batch_size` gate bundles for the same note, defaulting to 5. With `batch_size=1`, this becomes one prompt per note per gate bundle.

## Prototype

Standalone prototype lives in [prototype](./prototype/README.md). It does not import or mutate production review code.

Implemented API sketch:

```python
create_review_runs(
    pairs,
    pack_by="note" | "gate",
    batch_size=5,
    output_root="generated",
)
```

Tests cover note-packed gate-bundle batching, gate-packed note batching, flat run output, prompt derivation, prompt file creation under the workshop, deduplication, path assignment, and invalid inputs.

## Review-pair DB migration

The cleaned live review DB was copied into ignored workshop scratch space:

```bash
kb/work/create-review-runs/db-scratch/review-store.sqlite
```

The migration script is [scripts/migrate_review_pairs.py](./scripts/migrate_review_pairs.py). It is a workshop script, not an installed `commonplace-*` command.

Run the migration plan:

```bash
python3 kb/work/create-review-runs/scripts/migrate_review_pairs.py --dry-run
```

Apply it to a copied DB, leaving the scratch source unchanged:

```bash
python3 kb/work/create-review-runs/scripts/migrate_review_pairs.py \
  --db kb/work/create-review-runs/db-scratch/review-store.sqlite \
  --copy-to kb/work/create-review-runs/db-scratch/review-store-migrated.sqlite \
  --apply
```

Schema direction:

- `review_runs` becomes an executor invocation table. It no longer carries `note_path`, `reviewed_note_sha`, or `reviewed_note_commit`.
- `review_pairs` becomes the atomic `(note_path, gate_id)` table, with primary key `review_pair_id`.
- Existing `review_run_gates` rows become requested `review_pairs`.
- Existing `gate_reviews` data is copied into the matching `review_pairs` row.
- Existing `manual-import` `gate_reviews` rows have no parent run, so the migration creates one synthetic completed `review_run` per manual-import row.
- `acceptance_events.accepted_review_id` becomes `acceptance_events.accepted_review_pair_id`.
- `legacy_gate_review_map` records the old `gate_reviews.id` to new `review_pairs.review_pair_id` mapping during migration; the live DB drops legacy maps after validation.

The current scratch migration result:

```text
legacy_review_runs: 2103
legacy_review_run_gates: 7864
legacy_gate_reviews: 8926
legacy_manual_import_reviews: 2507
legacy_acceptance_events: 8951
legacy_null_acceptances: 1527
requested_review_pairs: 7864
synthetic_review_runs: 2507
migrated_review_pairs: 10371
migrated_acceptance_events: 8951
```

After applying to `review-store-migrated.sqlite`, the migrated DB has:

```text
review_runs: 4161
review_pairs: 10371
completed pairs: 8926
missing pairs: 1445
pending pairs: 0
foreign_key_check: clean
```

## Open design questions

- Should `create_review_runs` be a single function with a strategy enum, or separate constructors over one shared lower-level primitive?
- Should prompt rendering be optional in the preparation result, or should preparation only return targets and artifact paths?
- Should batch artifact paths be owned by the same API, or only single-run artifact paths?
- How should dry-run work when no DB rows should be created? Existing `run-review-bundle --dry-run` prints a prompt without persisting a run.
- Should workshop-local gates, such as `kb/work/agent-note-improvement/compression/`, be supported only after promotion to `kb/instructions/review-gates/`, or should the API accept a gate root override?

## What would close this workshop

The workshop closes when it produces:

- a concrete API sketch for `create_review_runs`;
- a migration plan for `create_review_run`, `run_review_bundle`, `run_gate_sweep`, and `prepare_review_batch`;
- focused tests showing the note-packed and gate-packed paths share preparation logic while preserving current behavior.

## Relevant local context

- [review system architecture](../../reference/review-architecture.md) — current review package structure and pair protocol.
- [review system reference](../../reference/REVIEW-SYSTEM.md) — operational workflow and storage model.
- [run-review-bundle-on-note](../../instructions/run-review-bundle-on-note.md) — live-agent single-note review flow.
- [ADR 029](../../reference/adr/029-review-execution-unified-on-note-gate-pairs.md) — pair protocol unification; packing is a strategy, not a separate protocol.
- [ADR 030](../../reference/adr/030-harness-facing-seams-batch-endpoints-and-runner-adapters.md) — external batch endpoints and runner adapters.
