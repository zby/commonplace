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

### Concrete shape

- **`commonplace-create-review-run`** returns the structured header (`review_run_id`, `gate_ids`, `note_path`, `model_id`) **and** the full `build_prompt` text. The live agent uses the JSON for subsequent CLI calls and follows the prompt for the actual review.
- **The live agent emits sentinel-bracketed output** — the same `=== GATE REVIEW START: <gate-id> ===` ... `=== GATE REVIEW END: <gate-id> ===` format the subprocess path produces.
- **New command: `commonplace-ingest-bundle-output`** parses sentinel output and records per-gate reviews plus finalization in a single call. The parser (`parse_bundle_gate_reviews`) and recorder (`record_and_finalize_run`) already exist as library functions in `src/commonplace/review/run_review_bundle.py:216-241` and `src/commonplace/review/review_db.py` — the new CLI is a thin wrapper.
- **`run-review-bundle-on-note.md` shrinks to a thin orchestration script:** run create-review-run, follow the prompt, write output to a file, run ingest. Roughly fifteen lines instead of ~100.
- **Per-gate `commonplace-write-gate-review` calls disappear from the normal live-agent flow.** The CLI stays available for manual recording edge cases (ack workflow, one-off edits, test fixtures) but is no longer the primary path.

## Blast radius

Files and components that would change:

- `src/commonplace/cli/review/create_review_run.py` — emit prompt text alongside JSON header.
- `src/commonplace/cli/review/ingest_bundle_output.py` — **new**, thin wrapper around existing parser and recorder.
- `src/commonplace/review/run_review_bundle.py` — `build_prompt` stays authoritative; may gain a small parameter for the output-destination variant (see open question 6).
- `kb/instructions/run-review-bundle-on-note.md` — shrink from ~100 lines to ~15 lines; most prose deleted.
- `src/commonplace/docs/REVIEW.md` — update the architecture description to reflect the unified shape.
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

### 1. How does the live agent deliver output to the ingest command?

- **A (file-based):** write sentinel-bracketed output to a temp file, pass the path to `ingest-bundle-output --input-file`. Clear but requires a file-cleanup decision and picks a filename.
- **B (stdin piped):** `cat review.md | commonplace-ingest-bundle-output --review-run-id N`. Elegant for one-shot execution but loses the ability to inspect the output before ingesting.
- **C (both):** accept either `--input-file` or stdin. Most flexible, two code paths.

Recommendation pending: probably C, with the prompt instructing the live agent to use a file so a human can inspect the intermediate artifact.

### 2. How does the JSON-plus-prompt shape look on stdout?

- **A (marker-separated):** JSON on one line, then `=== PROMPT ===`, then prompt text. Easy to parse.
- **B (prompt-only):** the prompt itself includes the structured fields as inline text. Removes JSON entirely but the live agent has to parse `review_run_id` out of prose.
- **C (two modes):** `--json-only` (current behavior for scripts) and `--with-prompt` (new default for live-agent use).

Recommendation pending: probably A, because the live agent needs the structured fields programmatically for later CLI calls.

### 3. Is `commonplace-write-gate-review` used anywhere outside the live-agent path?

- **Known:** tests use it as a fixture setup. That usage stays.
- **Unknown:** whether any interactive workflow, ack process, or manual edit path depends on it.
- **Action:** grep for `commonplace-write-gate-review` outside `test/` and `src/` before finalizing the instructions-file rewrite.

### 4. How should ingest handle partial parsing failures?

If the live agent produces sentinel-bracketed output that parses cleanly for three gates and fails for the fourth, what's the right behavior?

- Fail the whole run (matches the subprocess path, `run_review_bundle.py:457-474`).
- Record the three successes, mark the fourth as ERROR.
- Require all-or-nothing.

Recommendation pending: match the subprocess path (fail whole run) — consistent behavior is more valuable than partial recovery.

### 5. Should `create-review-run` emit the prompt by default?

CLAUDE.md says "no backwards compatibility — with no external consumers, always prioritize cleaner design." So yes, by default is fine. But some test fixtures might only want the JSON header. A `--json-only` flag could preserve that case without changing the default.

### 6. Does the output contract genuinely differ between paths?

The current `build_prompt` output contract says `"- Do not write files or invoke review helper scripts."` — appropriate for a subprocess returning stdout only. But the live agent **must** write files (to feed ingest). This is the one part of the prompt that legitimately differs between paths.

Options:
- Parametrize `build_prompt` with an `output_mode` argument (`"stdout"` vs `"file"`) that swaps the relevant bullets.
- Remove the "do not write files" bullet entirely from `build_prompt` and rely on the subprocess runner's sandbox to prevent file writes.
- Have `build_prompt` describe only the **format** of the review output (sentinels, severity, result line) and have each caller inject its own **destination** instructions via a trailing block.

The third option is probably the cleanest — it factors "what the review looks like" from "how to deliver it." The first option is the most conservative.

## Next actions

1. Resolve open questions 1, 2, and 6 — these shape the public CLI surface.
2. Write an ADR capturing the architectural decision: one prompt source, two callers, sentinel-bracketed output protocol for both.
3. Implement: extend `create-review-run`, add `ingest-bundle-output`, rewrite `run-review-bundle-on-note.md`, update `src/commonplace/docs/REVIEW.md`.
4. Test parity: add coverage for the ingest path; verify that subprocess and live-agent paths produce equivalent database state for the same `(note, gates, model)` tuple.
5. After landing: delete the duplicated prose from `run-review-bundle-on-note.md` and verify no new drift paths have been introduced by grepping for `"Read the requested gate"`, `"Reading scope"`, and the sentinel strings across `kb/` and `src/`.
