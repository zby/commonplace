# Plan: retrofit reviews to the write-side / read-side template

Migrate every live agent-memory-system review to the **write-side / read-side**
template (decision log `../../agent-memory-systems/review-framework-design.md`,
D3 + D4). Strategy: make the tooling *strict* for the new layout first — removing
the migration backcompat per the repo's no-backcompat rule — so
`commonplace-validate` and the matrix build become the worklist and the
done-condition for the retrofit. Then fan the retrofit out one sub-agent per
review, then rebuild and verify the whole corpus.

This is the **layout** retrofit (rename + write-side tokens + timing removal),
distinct from the earlier `../agent-memory-matrix-retrofit/` (one-hot lead tokens).

## Sequence

- **Phase 0 — make the tooling strict** (orchestrator, do once, *not* delegated). Below.
- **Phase 1 — per-review retrofit** (delegated fan-out). See `runbook.md`.
- **Phase 2 — verify the live corpus** (orchestrator). Below.

The template change itself, the scope, and the per-review procedure live in
`runbook.md`; this plan owns the tooling work that brackets the fan-out.

---

## Phase 0 — make the tooling strict

After Phase 0, fixtures pass but **live reviews fail validation** — that failure
set is the Phase 1 worklist. Commit Phase 0 atomically (parser + schema + spec
wording + fixture + tests).

### 0a. Parser — add the write-side axes

`src/commonplace/lib/systems_matrix.py`:

- Add to `ONEHOT_AXES`:
  ```python
  "Write agency": {"wa_manual": "manual", "wa_automatic": "automatic"},
  "Curation operations": {
      "op_consolidate": "consolidate", "op_dedup": "dedup",
      "op_evolve": "evolve", "op_synthesize": "synthesize",
      "op_invalidate": "invalidate", "op_decay": "decay",
      "op_promote": "promote"},
  ```
- **Applicability:**
  - `Write agency` is **universal** (like `Lineage` / `Behavioral authority`) —
    flag when missing on any review.
  - `Curation operations` is **gated on automatic agency** — applicable iff
    `wa_automatic == "1"`; blank (not flagged) when manual-only. Add a gate
    analogous to `PUSH_AXES`/`TRACE_AXES` (e.g. `AUTOMATIC_AXES = {"Curation
    operations"}`), resolved after the `Write agency` token is parsed.
- Add both axes' columns to `COLUMNS` in a `# write side` block (before the
  `# read-back` block). They flow into `_PARSED_ONEHOT`/`PARSED` automatically.
- Cross-check (cheap sanity, optional): a `trace-derived` review should carry
  `wa_automatic`; a `push`/`both` review usually does too. Don't hard-fail on it.

### 0b. Schema — remove backcompat, require the new layout

`kb/agent-memory-systems/types/agent-memory-system-review.schema.yaml`:

- **Remove the migration relaxation.** The `trace-derived` conditional currently
  matches the substring `"Trace-derived learning"` so old headings stay valid —
  delete that tolerance. Require the new structure: when `trace-derived`, body must
  contain `"### Trace-derived learning"`.
- Add global body constraints (all reviews):
  - **require** `"\\*\\*Write agency:\\*\\*"` (the required verdict),
  - **forbid** `"## Trace-derived learning placement"` (old heading gone),
  - **forbid** `"\\*\\*Read-back timing:\\*\\*"` (dead token gone).
- Leave the `push-activation` → `"Read-back placement"` conditional as is.
- Update `headings.description` if its wording drifts; drop any
  `# BACKCOMPAT` / "during migration" comments removed.

### 0c. Spec wording

In `...types/agent-memory-system-review.md`, reword the Write-side **Trigger** so
"manual-only ... needs no section" becomes "keeps the `## Write-side placement`
heading with just the `**Write agency:** \`manual\`` verdict" (the placement
decision in `runbook.md`). Update the skeleton if needed so it matches.

### 0d. Fixture + tests

- `test/commonplace/lib/fixtures/zikkaron_review.md`: rename the trace section to
  `## Write-side placement` + `### Trace-derived learning`; add `**Write agency:**`
  and `**Curation operations:**` tokens consistent with the prose. (Timing token is
  already removed.)
- `test/commonplace/lib/test_systems_matrix.py`: assert the new `wa_*` / `op_*`
  columns one-hot correctly; assert `Write agency` is flagged when missing and
  `Curation operations` is blank-not-flagged for a manual-only system.

### 0e. Gate

`.venv/bin/pytest test/commonplace/lib/test_systems_matrix.py` and the docs/schema
tests green. Do **not** expect the full build/validate to be clean yet — every live
review now raises warnings (missing `**Write agency:**`, old heading, timing token)
and build flags; that *is* the Phase 1 worklist.

**Severity note:** the validator hard-fails only on frontmatter
`description`/`tags`/`type`; all body/heading schema violations are **warnings**, so
live reviews read `Overall: PASS (N warnings)`, not FAIL. Making them hard fails
would mean broadening `_FAIL_PATHS` in `src/commonplace/lib/validation.py`, which
changes validator semantics for every note type — out of scope. The worklist
therefore keys on build flags + structural grep, not `Overall: PASS` (see
`runbook.md`).

---

## Phase 1 — per-review retrofit

Run `runbook.md`: build the worklist from build flags + structural grep (validate
reports warnings, not failures), fan out one sub-agent per file, confirm each
reaches `PASS (clean)` before moving on.

---

## Phase 2 — verify the live corpus

1. `python3 scripts/build_systems_matrix.py` → **0 flags** on repo-reviewed rows.
2. Validate every in-scope review → all `Overall: PASS (clean)`.
3. `.venv/bin/pytest` full suite green.
4. `python3 scripts/render_systems_table.py` to regenerate the human table.
5. Confirm no `## Trace-derived learning placement` / `**Read-back timing:**` remain
   in live (non-`.replaced`) reviews.
6. Commit; close this workshop and promote any durable lessons to a note.
