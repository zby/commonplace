# Fix system

The fix system is the complement to the [review system](./REVIEW-SYSTEM.md). Reviews identify problems; the fix system applies corrections. It consumes warn findings from the review DB and produces auditable fix reports.

This system is experimental and opt-in, like the review system it depends on.

## Concepts

**Warn finding.** An actionable finding extracted from a gate review whose canonical decision is `warn`. The `commonplace-warn-selector` command parses these from the `### Findings` or `### Summary` sections of stored review prose.

**Fix strategy.** A named pattern of review warning + appropriate fix, catalogued in `kb/instructions/fix-warnings/fix-strategy-taxonomy.md`. Agents classify each fix by strategy name to make fixes auditable and to grow the taxonomy over time.

**Fix report.** A per-note markdown file in `kb/reports/fixes/{note-stem}.fix-report.md` that maps each warning to the fix applied, the strategy used, and the status (fixed or deferred).

## Architecture

The fix system sits downstream of the review system:

```
review gates → gate reviews (DB) → warn_selector → fix instruction → edited note + fix report
```

Reviews are never modified by fixes. The review system owns the assessment; the fix system owns the correction. After fixes land, the next review sweep re-evaluates the note against the same gates.

## Components

### Warn selector

`commonplace-warn-selector` builds the fix queue from the review DB.

- Reads current accepted reviews across all models
- Only considers reviews attached to a `review_run_id` (excludes legacy imports)
- Selects findings from reviews whose canonical decision is `warn`
- Extracts actionable items from `### Findings` sections (lines starting with `- warn:`)
- Falls back to `### Summary` or stripped review body when no structured findings exist
- Collapses model partitions to one current entry per `(note_path, gate_id)`, choosing the latest accepted warn review

CLI:

```bash
# Grouped summary
commonplace-warn-selector

# Full JSON with review text
commonplace-warn-selector --json

# Filter to specific notes
commonplace-warn-selector --json kb/notes/backlinks.md
```

### Fix strategy taxonomy

`kb/instructions/fix-warnings/fix-strategy-taxonomy.md` — a living codebook of named fix patterns. Strategies are organized by the review check they most commonly address but can apply across checks. Current categories:

- **Source residue** — stale paths, unframed domain examples, single-source vocabulary, temporal residue
- **Confidence miscalibration** — hedge own framework, hedge strength mismatch
- **Grounding** — qualifier dropped, scope narrowed, unsourced addition
- **Completeness** — boundary case acknowledged

New strategies are added when `new-pattern` reports from fix sweeps show recurring patterns (3+ instances).

## Instructions

### Fix one note

Instruction: `kb/instructions/fix-warnings/fix-review-warnings.md`

1. `commonplace-warn-selector --json {note-path}` — get actionable findings
2. Read the target note in full
3. For each finding: read the recommendation, read context, decide if fixable without changing the argument
4. Apply minimal edits, classify each fix by strategy name
5. Write fix report to `kb/reports/fixes/{note-stem}.fix-report.md`

### Fix descriptions

Instruction: `kb/instructions/fix-warnings/fix-descriptions.md`

A specialized sub-procedure for description-field warnings from `commonplace-validate-notes`. Called standalone or by the general fix instruction when it encounters description issues.

### Fix sweep

Instruction: `kb/instructions/fix-warnings/fix-review-warnings-sweep.md`

1. `commonplace-warn-selector --json` — build priority queue (sorted by finding count descending)
2. Delegate per-note fixes to sub-agents (can run in parallel)
3. Report: fixed by strategy, deferred items, new patterns
4. If new patterns recur (3+ instances), propose adding to the taxonomy

## Constraints

- **Minimal edits** — fix the warning, not the surrounding prose
- **Don't change arguments** — fixes change framing, accuracy, and attribution, not claims or structure
- **Don't remove examples** — frame them instead
- **Don't update stored reviews** — reviews are regenerated separately
- **Verify before assuming staleness** — check whether a flagged path/mechanism actually exists before removing it

## Outputs

Fix reports land in `kb/reports/fixes/`. Each report contains:

- A table mapping each finding to a strategy, summary, and status
- A warning-to-fix mapping for auditability
- Deferred items with reasons
- New patterns not yet in the taxonomy
