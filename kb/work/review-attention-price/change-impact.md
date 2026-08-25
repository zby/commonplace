# Change impact of Mechanism B on the current system

Analysis date 2026-08-25, against commit `a6efeb52` (store schema v3, manifest `review-job-prompt-v3`). Two code maps were taken: the execution path (`src/commonplace/review/`, `protocol/`, `cli/review/`) and the store/freshness substrate (`src/commonplace/store.py`, `store-schema.sql`, `freshness/`). Line numbers are as of that commit.

## The finding that organizes everything else

Mechanism B is three separable changes, and the current system resists them very unequally:

| Layer | What it adds | Store schema | Freshness model | ADRs amended | Rough size |
|---|---|---|---|---|---|
| 1. **Pack** — code chooses the files, agent reads them | pack materialization, pack shapes, pack-aware prompt and criterion text | none | none | 079 (budget → pack ceiling); the "one derived path" allowance | moderate: ~5 modules, 1 criterion, 3 docs |
| 2. **Pin** — pack files become freshness inputs | N-ary inputs, a derived-input version kind, `pack-changed` staleness | v4, additive but wide | rewritten at every hardcoded "two" | 038, 073 (both argued *against* this), 052 | large: touches selector, integrity, view, ack, status, finalization signature |
| 3. **Split** — one pair, N passes, combined outcome | link positions, component graph, sibling jobs, combination at finalization, retained sibling evidence | v4/v5: pass linkage; pruning semantics change | one baseline per key kept; evidence 1:1 must widen | 029, 035, 036, 043, 067; run-review-batches "never split" | largest, and currently has no trigger (ADR 079) |

Layer 1 alone delivers what the mechanism exists for — exact budget control, exact charging, the ingest-contamination fix, deterministic consumption provenance. Layers 2 and 3 are consequences the design *permits*, not requirements of budget control. They should be decided separately, and both have data or arguments standing against doing them now.

## Layer 1 — packing

### What exists

- The resolver (`job_prompt.resolve_note_markdown_links:49`, `prepare_note_target:141`) already yields `ResolvedMarkdownLink(link_text, raw_target, repo_path, size_bytes)` per link, deduplicated by `available_link_cost` (`protocol/prompt.py:122`). Snapshot requirement is detected from the literal `(snapshot required)` in link text (`SNAPSHOT_REQUIRED_MARKER:18`); the snapshot path is derived by `_required_snapshot_path:40` but only recorded when *missing*. Nothing reads or copies target content.
- The prompt (`render_pairs_prompt:175`) embeds note and criterion text, then a per-note "Pre-resolved markdown links" table with the available-cost line (`:287-297`), and tells the reviewer to use the table instead of searching (`:226-241`). Reserved-sentinel lines in embedded text are rejected (`_validate_targets:140`) — the collision check the design wants already exists, for the one thing that is inlined.
- Job creation (`batch.prepare_grouped_review_job:78`) writes rows, attaches availability telemetry, renders the prompt, writes `prompt.md` and `MANIFEST.json` into `kb/reports/review-jobs/review-job-{id}/` (`artifacts.py:49-98`, gitignored). Consumption is parsed from the soft `review-consumption:` line (`parser.py`, `telemetry.with_review_link_consumption`) and priced against the availability list.
- Gate frontmatter schema has `additionalProperties: true`; only `resolve_criteria._load_frontmatter:94` reads it and ignores unknown keys. A `pack:` field validates today.

### What changes

1. **Pack builder** (new, beside `job_prompt.py`): from `NoteReviewTarget.resolved_links`, produce a pack manifest — per distinct target: source path, pack shape (`whole` | `quotes` | `head` | `snapshot`), materialized path, bytes. Shape by target type (ingest → `quotes`, snapshot-required → `snapshot`) then by criterion (`head` overrides for non-ingest targets). Extraction of `## Quotes` and of title + first paragraph is new code over `lib/note_parser.py`; the Quotes section format is fixed by ADR 073, so the extractor has a contract to test against.
2. **Materialization** in `batch.prepare_grouped_review_job` after `capture_review_inputs`: write `pack/` under the job dir; copies for whole notes, extracted files for `quotes`/`head`; the snapshot referenced by path, not copied (753 KB max; it is already local). Record pack manifest in MANIFEST.json (`artifacts.py:213-243`) and in `telemetry_json` beside availability — this is the consumption record from now on.
3. **Prompt**: replace the link table with the pack table (`pack path | source | shape | bytes`) and the reading-scope sentence with "read only the listed pack files"; keep the availability line. Manifest schema bumps to `review-job-prompt-v4`.
4. **Ceiling**: a pass-size ceiling in bytes (Track B's output; until then, a value that admits the corpus maximum, ~350 KB). Above it, the job is created in **pull mode**: no pack, today's link table, today's cap sentence, and a `pack_mode: pull` marker in telemetry. This is the counted fallback and it means layer 1 needs no splitting to ship.
5. **Criterion text**: `grounding-alignment` loses the sixteen-artifact sentence and the two-route reading instruction (the pack already applied the route); keeps the evidential rule that only Quotes are support. `misleading-link-text` declares `pack: head` and loses "at most 5 links". `concept-attribution` declares `pack: whole` and loses "up to 5". Each edit stales that criterion's population once — expected, ADR 079 did the same.
6. **Consumption telemetry**: `opened_paths` continue to be reported; pricing now resolves against the pack manifest; a path outside the pack becomes `opened_paths:outside_pack`, a new soft flag next to `unpriced`.
7. **Docs and contracts**: `README-REVIEW-SYSTEM.md:57-71` (the one-derived-local-path allowance becomes "the pack"), `review-architecture.md:107-112` ("linked files are reading context" stays true, the sentence about following links changes), `run-review-batches.md` unchanged (worker still reads one prompt), ADR 079 amended or superseded by an ADR selecting the pack ceiling.
8. **Tests**: `test_job_prompt.py` (2), `test_review_batch.py` (11), `test_review_protocol.py` (19), `test_review_telemetry.py` (3) extend; new tests for the extractors and the pack builder. `test_review_jobs_live_and_direct.py` (13) exercises the job dir and needs the pack directory.

### What does not change

Store schema, freshness inputs, the selector, finalization's transaction, ack paths, the worker instruction, the pair as unit of output. Nothing in `store.py`, `freshness/`, `review_db.py`.

### Risk

The reviewer still has file tools and can read outside the pack. Layer 1 measures that (flag 6) rather than preventing it; prevention would need a tool-mediated read path the parent controls, which ADR 067's one-prompt-one-output worker does not give. Accept and measure.

## Layer 2 — pinning the pack

### Why it is expensive

Every freshness surface hardcodes two inputs:

- `freshness_inputs` PK `(target_id, input_role)` + `UNIQUE(target_id, artifact_path, version_kind)`; `version_kind CHECK IN ('file-text')` (`store-schema.sql:34-45`). A Quotes section is a *derived* input: a new version kind whose live version is re-extracted from the ingest, plus a locator — path alone cannot identify two regions of one file.
- `freshness/integrity.py:83-97` raises when input count `!= 2`; `:98-127` asserts the two roles by name. `check_store_health` runs it.
- The `current_review_freshness_baselines` view joins exactly `note` and `criterion` (`store-schema.sql:143-152`); `freshness/selector.py:186-194` iterates a hardcoded two-tuple; staleness reasons are exactly `missing-baseline | criterion-changed | note-changed` (`README-REVIEW-SYSTEM.md:86-92`).
- `finalize_capture_refresh` (`finalization.py:30-56`) and `upsert_freshness_baseline` take literally two snapshot ids; `commonplace-ack-review`, `commonplace-ack-trivial-note-changes` (`watches:` has no meaning for a pack file), `commonplace-freshness-status`, `-ack`, `-retire` (`transitions.py:119-160` match by `input_role`) all assume the shape.
- Documented as a boundary, not an accident: `freshness-architecture.md:26-34` ("its two inputs are the note and criterion files … no synthetic criterion or third dependency is registered"), `review-architecture.md:85-87` ("pins exactly two source files").

### The arguments already on record against it

- **ADR 038** admitted the type spec as a dependency by factoring it onto the criterion side and *explicitly rejected* a third input because it "required a third acceptance column, taught ack a new input shape". A pinned pack is that rejected alternative, N-ary.
- **ADR 073** made ingest `## Quotes` append-only and tracked precisely so review need not pin them: support can only grow, so a PASS stays valid against Quotes. The pinning value is therefore only in linked *notes*, which do change — and the paired assay found no case where a linked-note change was the cause of a stale verdict; that was never measured.
- `kb/reference/proposals/factored-dependency-pairs-for-review-freshness.md` already holds the N-ary design as an unadopted fallback.

### The cheap substitute

Record the pack manifest with content hashes in `telemetry_json` and in the pair result file's frontmatter. That is full provenance (what was judged, byte-exact) without making it freshness identity. Staleness on pack change is then a query someone can run, not a selector reason. Defer layer 2 until a measured case shows linked-note drift invalidating verdicts at a rate worth a schema version.

## Layer 3 — splitting into passes

### What is missing

- **Positions.** `find_markdown_links_with_text` (`lib/note_parser.py:104`) returns `(text, target)` only — no offsets, lines, or paragraphs. The paragraph→target graph needs a positional parser; nothing in the codebase retains where a link sits.
- **Sibling linkage.** `review_jobs` has no parent/pass column; `review_pairs` is unique per job, so several jobs already may hold the same logical pair, but nothing marks them as passes of one review. New table or columns — and `store.py:189-192` fails on any unexpected table, so `EXPECTED_TABLES` and a v4 migration are mandatory.
- **Combination.** `record_and_finalize_job` (`finalization.py:281-333`) completes the job's own pairs and advances each baseline immediately; there is no combine step. The baseline's evidence is 1:1 with one pair row (`review_freshness_evidence`, `store-schema.sql:112-117`), and `prune_superseded_freshness_baselines` (`review_db.py:912+`) *deletes* the superseded pair and possibly its job — a second pass finalizing today evicts the first instead of joining it.
- **Contracts.** ADR 029 ("batching is a packing choice, not a protocol") — passes make packing protocol; ADR 035 removed partial salvage deliberately, and multi-pass is partial-evidence reasoning one level up; ADR 036 (acceptance is current state, superseded evidence pruned inline) conflicts with retaining siblings; ADR 043 (one baseline per key) survives if the combined result is the evidence; ADR 067 is fine (N workers) but `run-review-batches.md:84` says "do not invent, merge, split, or reorder jobs" and `:139` "do not combine multiple jobs into one output file"; `warn_selector` must pick which pass's rationale enters the fix queue; result-file naming is by pair ordinal within a job.

### Why not now

ADR 079 records the reopen condition and the paired assay supplied no divergent tail case. Under Mechanism B the trigger becomes "pack exceeds the pass size", which is measurable before any code from the resolver's size data plus a positional parse: the component-size distribution per note. If Track B's pass size is at or above the corpus maximum (~350 KB, 25 artifacts), layer 3 never fires and the pull-mode fallback in layer 1 is the whole tail policy. Compute that distribution first; it is also the number an adoption ADR would cite.

## Order of work

1. **Now, no code path touched**: component-size distribution script (`scripts/`), positional link parse as a throwaway or as the first piece of `note_parser` extension.
2. **Track A plumbing** (usage into `--telemetry-json`): independent of all three layers; one instruction edit and one runner capture.
3. **Layer 1** once Track B has a pass size — or before, with the ceiling set to admit the corpus maximum, since the ceiling is then a fallback marker and not a judgment input. The criterion edits are the only population-staling step; batch them with the ADR.
4. **Layer 2 and 3**: separate proposals, each with its own trigger. Layer 2's substitute (hashed pack manifest in provenance) ships with layer 1 at no cost and produces the data that would justify or bury layer 2.

## Blockers list, for the implementer

Hard, layer 2 or 3 only: `store-schema.sql:34-45` input shape and `file-text`-only version kind; `freshness/integrity.py:83-97`; the two-join view `:143-152`; `freshness/selector.py:186-194`; `finalization.py:30-56` signature; `review_db.py:912+` pruning; `store.py:189-192` expected-tables strictness. None of these is on layer 1's path.
