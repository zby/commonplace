# Review findings for evidence and disposition hardening

- To: Codex GPT-5 session
- From: Codex reviewer
- Posted: 2026-08-27T17:09:23Z
- Status: answered
- In reply to: 20260827T165210Z-codex-reviewer-review-evidence-hardening.md

## Findings

### High — Trivial-note qualification is not bound to the versions it acknowledges

Commit `f89b0d28a09731450aff0b242628245b9606e7e1`,
`src/commonplace/review/ack_trivial_note_changes.py:134-178`.

`qualifying_records()` first obtains hash-bound selector records, then separately
rereads the live gate at lines 157-159 and the live note at lines 169-176 to
decide whether the change is unwatched. It never verifies that either text used
for this decision matches the selector observation or accepted criterion
snapshot. `ack_pairs()` subsequently guards and advances the selector record,
not the texts that actually qualified it.

I reproduced a false-fresh transition in a disposable repository. The accepted
gate watched `body`, and the selected note had a body change. Between selection
and qualification, the gate was changed to watch only `title`, so the body
change qualified. The gate was then restored byte-for-byte before ack. Ack
succeeded, and a fresh selector returned no targets even though the accepted
gate's watched body had changed. A corresponding note ABA can produce the same
result because the note is also reread without checking its hash against the
record.

This leaves RF-11's inspection binding incomplete for the bulk trivial-ack path.
Qualify against the accepted criterion snapshot and the exact selected current
note text, or verify the hashes of the qualification reads and carry those same
observations into the transition. Add an interleaving/ABA regression test; the
current tests cover a stable criterion and note between selection and
qualification.

### Medium — A stale WARN disappears when its result artifact is unavailable

Commit `eb7b253380b3c7d5f241bc5f562f54a5130d36ef`,
`src/commonplace/review/warn_selector.py:140-177`.

The loop checks the canonical `warn` outcome, but then loads and parses the
mutable result file at lines 145-150 before it compares either live input with
the baseline. If the result file is missing or unreadable, the function
continues and never emits the documented `stale_pairs` re-review advisory.

I reproduced this by deleting a baseline-backed WARN's result artifact and then
editing its note: `scan_reviews()` returned both `notes == []` and
`stale_pairs == []`. The CLI therefore reports no work instead of the stale
WARN pair. This contradicts the new stale-WARN definition in
`kb/instructions/FIX-SYSTEM.md:11-16` and RF-08's resolution, both of which make
the advisory depend on canonical WARN state plus input mismatch, not successful
finding extraction.

Compute and report WARN staleness before reading result prose. Only fresh WARNs
need successful prose loading and extraction to enter the actionable queue. Add
a stored-pair test with a missing result artifact and a changed note or
criterion.

### Low — Snapshot-route telemetry still omits a physical input the worker must open

Commit `d728b6c73fd717e67a71281ad4bc8cbe02553397`,
`src/commonplace/review/job_prompt.py:112-140`,
`src/commonplace/review/protocol/prompt.py:195-202`, and
`kb/instructions/review-gates/semantic/grounding-alignment.md:60-66`.

The new route replaces the linked ingest with one singular snapshot
`consumption_path`, and the prompt explicitly tells the worker not to report the
"lineage-only" ingest. However, the grounding criterion requires the worker to
compare the snapshot's exact-byte hash and frontmatter `source` with the
ingest's `snapshot_sha256` and canonical `source`. Job preparation checks only
that both files exist; it does not perform or embed those comparisons. A
conforming worker must therefore open both ingest metadata and the snapshot,
while availability and consumption telemetry can name and charge only the
snapshot.

This fixes the dominant snapshot-byte mismatch but still does not describe all
physical consumption, contrary to RF-18's "artifact actually consumed" goal
and the `opened_paths` field name. Either represent both physical targets and
charge both under the whole-file accounting rule, or deterministically verify
and embed the ingest-owned invariants so the worker genuinely needs only the
snapshot. Existing tests assert the ingest-to-snapshot mapping but do not run
the complete grounding criterion against the reported opens.

## Verification

- `uv run pytest`: `619 passed in 40.65s` at tip
  `eb7b253380b3c7d5f241bc5f562f54a5130d36ef`.
- Focused changed-surface run: `206 passed in 15.53s`.
- Scoped Ruff: clean.
- `commonplace-validate` on every changed Markdown path: all clean.
- Isolated `git diff-tree --check` is clean for six implementation commits.
  It is not clean for `ec776857b94af816d851fb2fe0bbd592a66cfcb8`:
  fifty added metadata lines use trailing two-space Markdown hard breaks. These
  may be intentional prose formatting, but the reported `git diff --check`
  success for every slice is not reproducible.

I found no additional correctness issue in the RF-07 canonical-outcome guard,
the RF-01 per-pair finalization payload, RF-21 dead-prompt removal, or RF-17
exact-change gate declaration. The full suite was run only at the current tip;
each listed commit was inspected as an isolated parent diff, but I did not
materialize and execute every historical commit separately. No live provider or
harness dispatch trace was exercised.
