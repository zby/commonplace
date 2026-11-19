---
description: Run a gate sweep with commonplace-review over chosen notes and criteria, then read its JSON report and settle problems, stops and guard findings
type: types/instruction.md
---

# Run review batches

Review chosen notes against chosen criteria so that every selected (note, criterion) pair has a fresh result file. `commonplace-review` launches the reviewer workers, checks each review and writes the results; the agent running this procedure chooses the scope, runs the command and settles what the report hands back. Do not launch reviewer sub-agents yourself, and do not review the pairs in your own context.

A result is fresh while the hashes it records still match the note's watched parts (title, description or body, as the criterion's `watches:` declares; the whole note when it declares none) and the criterion's text. Results live under `kb/reports/state/review/results/<note-path>/<criterion-id>.md`.

## Inputs

- **Notes** — files or directories. A directory means its reviewable notes, not recursively; it skips indexes, collection contracts and type specs. Name files in a validation-ignored directory one by one.
- **Criteria** — catalog gate ids (`prose/source-residue`), bundle names (`prose`), the lenses `type` and `collection` (or `type/<name>`, `collection/<path>`), and opt-in criteria: individual compression checks (`compression/core-claim-obscured`, `compression/branch-bloat`, `compression/detail-overhang`, `compression/marginal-value-redundancy`; bare `compression` is refused) and the report criteria (`critique`, `friction`, `premises`, `compression-synthesis`, `role`). Without `--criteria`, a review covers every bundle plus `type` and `collection`; opt-in criteria are never included unless named. `compression-synthesis` and `role` run alone on one note with unassessed freshness (`status` refuses them; read output with `show RUN`).
- **Profile** — optional; a worker profile from the library's `instructions/review-profiles.yaml`. Without `--profile` the file's `default` is used.

## Steps

1. **Check what the sweep would ask.** This launches nothing:

   ```bash
   commonplace-review status {notes...} --criteria {criteria...} --stale
   ```

   Each row is a pair that is `missing` or `stale` (with `note`, `criterion` or both changed). If there are none, stop: every pair is fresh. Without `--criteria`, `status` and `commonplace-review` both cover all gates.

2. **Choose the grouping.** A launch's fixed context dominates its cost. For several catalog gates on each note, add `--grouping bundle`: one worker per note and bundle asks that bundle's stale gates together, and each gate still gets its own result file. Keep the default `--grouping pair` for one or two gates per note, or when each gate must be judged in a separate context. Under `--grouping bundle`, a pair with rejected findings is asked alone outside its bundle call, and every `type`, `collection`, compression and report pair is one call each under either grouping.

3. **Run the sweep:**

   ```bash
   commonplace-review {notes...} --criteria {criteria...} [--grouping bundle] [--profile NAME]
   ```

   It asks only pairs without a fresh result. `--force` asks fresh pairs too; use it only when the user asks for a new judgment of fresh pairs. `--max-workers N` bounds concurrent workers (default 4).

4. **Read the JSON report.** It names `run-dir`, gives `counts` by pair state, `stopped`, `guard` and one entry per pair with `state`, `outcome` and `problem`. The exit code is 0 only when every pair has a current result, 1 otherwise, and 2 when the command itself failed. The guard does not change the exit code, so read `guard` in the report every time. Handle each case:

   - **`fresh` or `reviewed`** — the pair has a current result; `outcome` is `pass`, `warn` or `fail`, or `report` for report criteria.
   - **`problem`** — the worker reported that it could not judge the pair; `problem` holds its reason. Fix the cause if it is in the note or the environment. Then either run the sweep again, which opens a new run, or dismiss the problem with `commonplace-review retry {run-dir} {job}` and continue the same run with `--resume {run-dir}`. A resumed run replays a problem that was not dismissed. A pair's `job` name is `<note>::<criterion-id>`; a bundle call's is `<note>::<bundle>/*`.
   - **`out-of-attempts`** — three attempts produced no acceptable review: each ended without a valid result line or returned no answer. `problem` holds the last rejection. Correction also stops early on **no progress** before repeating an already rejected prompt/input combination; inspect the diagnostics rather than spending calls on identical feedback (an explicit answer dismissal remains available when another attempt is warranted). Run the sweep again; if the same pair fails again, report it with the rejection text.
   - **`stopped` is set, pairs `not-run`** — a launch failed for a reason outside the task, a **controller failure** occurred (missing validation dependencies or corrupt evidence — repair the controller or its inputs before retrying; incomplete captures are not silently backfilled on resume), or the harness reported a usage limit. Results already written stay. Repair the cause or wait for the limit to reset, then rerun with `--resume {run-dir}` and the same notes and criteria. If the resumed run reports a launch that an earlier controller left unsettled, confirm that its process and children have exited, then run `commonplace-review acknowledge {run-dir} {launch}`.
   - **`guard.changed` is non-empty** — these checkout paths changed while the run was open. Other sessions' edits show up too, so inspect each path and decide whether a worker wrote it; nothing is reverted for you. A worker must write only its output file under the run directory. Only fixture trials fail on a dirty guard.

5. **Verify.** Rerun step 1. No rows means every selected pair is fresh.

## Rules

- A rerun without `--resume` opens a new run directory under `kb/reports/state/review/runs/`, even when nothing is stale.
- One process at a time may hold a run; a second exits 2.
- `--resume` replays every call whose work is unchanged. Give the same notes and criteria, and either no `--profile` or the one the run was opened with.
- `retry {run-dir} {job} --key {key}` dismisses one recorded answer instead of the problems. The answer's result file already makes the pair fresh, so the rerun needs `--force`.
- Editing a criterion stales every pair that names it, even when the edit only rewords it: its hash changes. Collect related edits to one gate before sweeping, and sweep its pairs once afterwards.
- Do not edit or move result files to make a pair fresh. Delete an orphaned result, one whose note or criterion is gone, as an ordinary file; `commonplace-review status` lists them apart.

## Verify

- `commonplace-review status {notes...} --criteria {criteria...} --stale` prints no rows.
- The report's `guard.clean` is true, or every path it named has been inspected and explained.

---

Relevant Notes:

- [Review system](../reference/README-REVIEW-SYSTEM.md) — operates-on: the result files, freshness rules and command surface this procedure drives
- [Commands](../reference/commands.md#commonplace-review) — operates-on: the command catalogue entry; run `commonplace-review --help` for full options
