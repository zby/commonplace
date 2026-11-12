# Fix system

The fix system is the complement to the [review system](../reference/README-REVIEW-SYSTEM.md). Reviews identify problems; the fix system applies corrections. It consumes the findings of current `warn` and `fail` review results and produces auditable fix reports.

This system is experimental and opt-in, like the review system it depends on.

## Concepts

**Current warning.** A review result whose outcome is `warn` or `fail` and which is fresh: the hashes it records still match the note's watched parts and the criterion. `commonplace-review status --fresh --outcome warn fail --json` lists them, one row per (note, criterion) pair, with the path of its result file.

**Finding.** One actionable item in a current warning's result file. A verdict review is structured as `### Summary`, `### Findings` (items of the form `- <severity>: <finding>`) and, when needed, `### Suggested Revision`, ending with the result line.

**Stale result.** A `warn` or `fail` result whose note or criterion no longer matches its recorded hash. `--fresh` excludes it from the queue. Re-review it instead of fixing from its text.

**Fix strategy.** A named pattern of review warning + appropriate fix, catalogued in the [fix strategy taxonomy](./fix-warnings/fix-strategy-taxonomy.md). Agents classify each fix by strategy name to make fixes auditable and to grow the taxonomy over time.

**Fix report.** A per-note markdown file in `kb/reports/state/fixes/{note-stem}.fix-report.md` that maps each warning to its disposition, the strategy used when a fix is applied, and the status (`fixed`, `rejected`, or `deferred`). `Rejected` means the finding was judged spurious or inapplicable and the note was deliberately left unchanged; it is distinct from postponing a finding that may be valid.

## Pipeline

The fix system sits downstream of the review system:

```
gate sweep → result files → commonplace-review status (current warn/fail) → fix instruction → edited note + fix report → gate sweep
```

Reviews are never modified by fixes. The review system owns the assessment; the fix system owns the correction. An edit to the note stales exactly the pairs whose watched parts it changed; rerunning the sweep for that note re-reviews them.

## Components

### Warning queue

`commonplace-review status` reads the result files and launches nothing.

```bash
# Current warnings across every stored result
commonplace-review status --fresh --outcome warn fail --json

# Current warnings for specific notes
commonplace-review status {note-path}... --fresh --outcome warn fail --json
```

Each row carries `note`, `criterion-id`, `outcome`, `model` and `result`, the result file's path. Read the findings from that file. A pair the fixer rejected stays a fresh warning until the note or criterion changes, so check the note's existing fix report before working a finding again.

### Fix strategy taxonomy

[fix-strategy-taxonomy.md](./fix-warnings/fix-strategy-taxonomy.md) — a living codebook of named fix patterns. Strategies are organized by the review check they most commonly address but can apply across checks. Current categories:

- **Source residue** — stale paths, unframed domain examples, single-source vocabulary, temporal residue
- **Confidence miscalibration** — hedge own framework, hedge strength mismatch
- **Grounding** — qualifier dropped, scope narrowed, unsourced addition
- **Completeness** — boundary case acknowledged

New strategies are added when `new-pattern` reports from fix sweeps show recurring patterns (3+ instances).

## Instructions

### Fix one note

Instruction: [fix-review-warnings.md](./fix-warnings/fix-review-warnings.md)

1. `commonplace-review status {note-path} --fresh --outcome warn fail --json` — list the current warnings and read each row's result file
2. Read the target note in full
3. For each finding: read the recommendation and context, then decide whether to fix, reject, or defer it
4. Apply minimal edits to fixed findings and record evidence for rejected findings
5. Write fix report to `kb/reports/state/fixes/{note-stem}.fix-report.md`
6. If the note changed, rerun the gate sweep on it with `--all-gates`; freshness selects the pairs, so it asks every pair the edit staled, including ones that passed before

### Fix descriptions

Instruction: [fix-descriptions.md](./fix-warnings/fix-descriptions.md)

A specialized sub-procedure for description-field warnings from `commonplace-validate`. Called standalone or by the general fix instruction when it encounters description issues.

### Fix sweep

Instruction: [fix-review-warnings-sweep.md](./fix-warnings/fix-review-warnings-sweep.md)

1. `commonplace-review status --fresh --outcome warn fail --json` — build the queue, grouped by note and ordered by warning count, descending
2. Run locally unless several notes have disjoint note/report paths and a named fresh-context or parallel-capacity benefit; then give each single-use worker the exact note and report paths, the fix instruction, sole write ownership, validation/return requirements, and a substantive-decision stop, and verify each diff/report before closing the worker
3. Rerun the gate sweep on the edited notes
4. Report: fixed by strategy, rejected findings, deferred items, new patterns
5. If new patterns recur (3+ instances), propose adding to the taxonomy

## Constraints

- **Minimal edits** — fix the warning, not the surrounding prose
- **Don't change arguments** — fixes change framing, accuracy, and attribution, not claims or structure
- **Don't remove examples** — frame them instead
- **Don't edit result files** — reviews are regenerated by rerunning the sweep
- **Verify before assuming staleness** — check whether a flagged path/mechanism actually exists before removing it

## Outputs

Fix reports land in `kb/reports/state/fixes/`. Each report contains:

- A table mapping each finding to a strategy, summary, and status
- A warning-to-fix mapping for auditability
- Rejected findings with the evidence or reasoning that made the warning inapplicable
- Deferred items naming the exact claim/evidence/source decision, affected
  passage, acceptable responses, and reason the fixer could not choose
- New patterns not yet in the taxonomy
