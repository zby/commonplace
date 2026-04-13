# Workshop: review-prompt-consolidation

## Question

How should the live-agent and subprocess review paths share a single source of truth for reviewer-facing instructions, so that changes to one path cannot leave the other stale?

## Why this workshop exists

The review system has two execution paths that both instruct an LLM to review a target note against a set of gates:

1. **Subprocess path** — `commonplace-review-sweep` and `commonplace-run-review-bundle` build a complete text prompt via `build_prompt` in `src/commonplace/review/run_review_bundle.py` and pipe it to a fresh runner subprocess (`claude-code` or `codex`).
2. **Live-agent path** — an agent already inside a harness calls `commonplace-create-review-run` to get JSON metadata, then follows imperative instructions in `kb/instructions/run-review-bundle-on-note.md` to read the target note, write per-gate reviews, and finalize the run.

Both paths convey the same reviewer-facing content: reading scope, output contract, the target note identity, the gate text, and a bundle template. Today that content lives in two files with slightly different wording, and the duplication produces silent drift.

**Concrete drift evidence (2026-04-11):** A review-sweep trace showed claude-code subprocesses re-reading gate files from disk even though the gate text was already inlined in the prompt. The fix to `build_prompt` changed the reading-scope bullet from `"- Read the requested gate definitions included below."` to `"- The requested gate definitions are included below. Do not read them from disk."` and also removed the `Requested gate definition files:` path list that had been advertising the on-disk location. The analogous instruction in `kb/instructions/run-review-bundle-on-note.md:23` still says `"- Read the requested gate definitions."` — the same latent bug, unfixed, in the other execution path. This workshop exists because that fix should not have needed to be applied in two places.

## Current drift surface

Inventory of what each path says, and where:

| Content | `build_prompt` (subprocess) | `run-review-bundle-on-note.md` (live agent) |
|---|---|---|
| Opening directive | `"Write gate reviews for {note_path} for gates: {gates}"` | implicit from instructions + CLI arguments |
| Reading scope (target note, link policy, gate source) | inline, post-fix wording | inline, pre-fix wording (latent bug) |
| Output contract (sentinels, severities, result line format) | inline | inline |
| Review run id | inline literal | captured from JSON |
| Pre-resolved markdown links | inline table | not provided — live agent resolves per-link |
| Bundle template (skeleton to fill) | inline | inline |
| Gate text | inline `=== gate: <id> ===` blocks | JSON `gates[].text` field |
| What to do after reviewing | sentinel-bracketed stdout → parsed by parent process | `commonplace-write-gate-review` per gate + `commonplace-finalize-review-run` |

Everything above the last row is duplicated content. Only the last row — how the completed review is recorded — is genuinely path-specific, because the subprocess returns stdout that the parent parses directly, while the live agent runs explicit recording commands.

## Decided direction: full consolidation

Make `build_prompt` the single source of truth for reviewer-facing instructions. Both paths use the same prompt. The only difference is who fills it in: a runner subprocess, or a live agent already inside a harness.

This is already mostly true for the subprocess paths. `commonplace-review-sweep` calls the library `run_bundle`, and `run_bundle` owns both the prompt-building side (`build_prompt`) and the bundle-parsing side (`parse_bundle_gate_reviews`). The live-agent path should join that same bundle protocol instead of growing a parallel prompt/parser pair.

For the live-agent path, this does **not** mean launching a new nested agent. `commonplace-create-review-run` only creates the review run and renders the canonical prompt for the already-running agent. The current agent follows that prompt, writes the bundle output, and then hands that output to a deterministic ingest command.

### Concrete shape

- **`commonplace-create-review-run --with-prompt`** returns the structured header (`review_run_id`, `gate_ids`, `note_path`, `model_id`, artifact paths) **and** the full `build_prompt` text. It does not invoke `claude-code`, `codex`, or any other runner.
- **The live agent emits sentinel-bracketed output** — the same `=== GATE REVIEW START: <gate-id> ===` ... `=== GATE REVIEW END: <gate-id> ===` format the subprocess path produces.
- **The live agent writes that output to the canonical bundle artifact:** `kb/reports/bundle-reviews/review-run-{id}/bundle-output.md`.
- **New command: `commonplace-ingest-bundle-output`** parses the bundle artifact and records per-gate reviews plus finalization in a single call. It must use the same bundle protocol library as `commonplace-review-sweep` / `commonplace-run-review-bundle`: `parse_bundle_gate_reviews`, `write_bundle_artifacts`, and the lifecycle recorder (`record_and_finalize_run`). The new CLI is a thin wrapper, not a second parser.
- **`run-review-bundle-on-note.md` shrinks to a thin orchestration script:** run create-review-run with prompt output, follow the returned prompt in the current agent, write `bundle-output.md`, run ingest. Roughly fifteen lines instead of ~100.
- **Per-gate `commonplace-write-gate-review` calls disappear from the normal live-agent flow.** The CLI stays available for manual recording edge cases (ack workflow, one-off edits, test fixtures) but is no longer the primary path.

This refines the older `review-run-lifecycle` direction. That workshop removed the split bundled live-agent path because it had no clear reason to exist when the normal split path could write one gate at a time. The new reason is prompt single-sourcing: bundled sentinel output lets the live-agent path consume the same reviewer-facing contract as the subprocess path without duplicating prose.

## Blast radius

Files and components that would change:

- `src/commonplace/cli/review/create_review_run.py` — add `--with-prompt`, include canonical artifact paths, and emit prompt text by calling the same library prompt builder used by `run_bundle`.
- `src/commonplace/cli/review/ingest_bundle_output.py` — **new**, thin wrapper around the existing bundle parser, artifact writer, and lifecycle recorder.
- `src/commonplace/review/run_review_bundle.py` — remains the bundle protocol owner for prompt construction, sentinel parsing, artifact writing, and review recording; may gain a small parameter for the output-destination variant (see open question 6), or some protocol helpers may be extracted if the module becomes too runner-specific.
- `kb/instructions/run-review-bundle-on-note.md` — shrink from ~100 lines to ~15 lines; most prose deleted.
- `kb/reference/review-architecture.md` — update the architecture description to reflect the unified shape.
- Tests — add coverage for `ingest_bundle_output`. Existing subprocess tests (`test_review_runs_direct_write.py`, `test_review_target_selector.py`) remain unchanged.
- `pyproject.toml` — register the new CLI entry point.

## Non-goals

- **Not changing the subprocess path semantics.** `review-sweep` and `run-review-bundle` continue to work as they do today; this workshop only adds a second caller of `build_prompt`.
- **Not changing the database schema or `review_runs` table structure.**
- **Not changing gate selection, staleness computation, or trait/type routing.**
- **Not removing `commonplace-write-gate-review` as a CLI surface.** It stays for manual edge cases.
- **Not touching the `gate-refactor` workshop's scope.** That workshop (`kb/work/gate-refactor/`) is about moving review storage from monolithic bundles to per-gate files. This workshop is about prompt construction. The two workshops share the database but not the design surface; they can land in either order.

## Open questions

These are the design decisions that need resolving before implementation begins.

### 1. How does the live agent deliver output to the ingest command? — resolved

Use a file-based canonical artifact:

```bash
kb/reports/bundle-reviews/review-run-{review_run_id}/bundle-output.md
```

The live agent writes the sentinel-bracketed review bundle there. Then `commonplace-ingest-bundle-output --review-run-id {id} --input-file kb/reports/bundle-reviews/review-run-{id}/bundle-output.md` parses and records it.

Stdin can be added later if there is a real caller. The first version should keep the intermediate artifact inspectable and reuse the existing bundle-review report directory.

### 2. How does the JSON-plus-prompt shape look on stdout? — resolved

- **A (marker-separated):** JSON on one line, then `=== PROMPT ===`, then prompt text. Easy to parse.
- **B (prompt-only):** the prompt itself includes the structured fields as inline text. Removes JSON entirely but the live agent has to parse `review_run_id` out of prose.
- **C (two modes):** keep the current JSON-only behavior for script callers, and add `--with-prompt` for live-agent use.

Decision: use option C. `commonplace-create-review-run` keeps its current non-prompt behavior for script callers. `--with-prompt` emits JSON with the normal structured fields plus `prompt`, `prompt_path`, and `bundle_output_path`.

### 3. Is `commonplace-write-gate-review` used anywhere outside the live-agent path? — resolved

Grep showed docs, tests, and the existing live-agent instruction path. The command stays available for manual edge cases and test fixtures, but the normal live-agent bundle workflow now uses `commonplace-ingest-bundle-output`.

### 4. How should ingest handle partial parsing failures?

If the live agent produces sentinel-bracketed output that parses cleanly for three gates and fails for the fourth, what's the right behavior?

- Fail the whole run (matches the subprocess path, `run_review_bundle.py:457-474`).
- Record the three successes, mark the fourth as ERROR.
- Require all-or-nothing.

Decision: match the subprocess path and fail the whole run. Consistent all-or-nothing behavior is more valuable than partial recovery here.

### 5. Should `create-review-run` emit the prompt by default? — resolved

No. Keep the current non-prompt behavior for script callers and add `--with-prompt` for the live-agent path. The prompt is a reviewer-facing artifact, not the minimal run-creation response, so making it opt-in keeps the command easier to compose while still avoiding duplicated instructions.

### 6. Does the output contract genuinely differ between paths? — resolved

The current `build_prompt` output contract says `"- Do not write files or invoke review helper scripts."` — appropriate for a subprocess returning stdout only. But the live agent **must** write `bundle-output.md` and invoke the ingest helper after finishing the semantic review. This is the one part of the prompt that legitimately differs between paths.

Options:
- Parametrize `build_prompt` with an `output_mode` argument (`"stdout"` vs `"file"`) that swaps the relevant bullets.
- Remove the "do not write files" bullet entirely from `build_prompt` and rely on the subprocess runner's sandbox to prevent file writes.
- Have `build_prompt` describe only the **format** of the review output (sentinels, severity, result line) and have each caller inject its own **destination** instructions via a trailing block.

Decision: use the first option. `build_prompt` owns both the shared bundle format and the small destination-specific contract, selected by `output_mode`.

## Next actions

1. Write an ADR capturing the architectural decision: one prompt/parser protocol, two executors, sentinel-bracketed output for both.
2. After landing: verify no new drift paths have been introduced by grepping for `"Read the requested gate"`, `"Reading scope"`, and the sentinel strings across `kb/` and `src/`.
