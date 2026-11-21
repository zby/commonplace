---
name: cp-skill-review
description: "Review KB notes with commonplace-review: check status and warnings, run gate sweeps, compression checks, or report criteria (critique, friction, premises, role), and retry or resume runs. Never writes a note; use cp-skill-revise to edit."
type: types/instruction.md
user-invocable: true
allowed-tools: Read, Grep, Glob, Bash
argument-hint: "[status | notes/dirs...] [--criteria ...] [--grouping pair|bundle]"
---

# cp-skill-review

Goal: inspect review status or produce fresh review results for selected notes without modifying any note.

## What it can and cannot do

**Can do:**
- Judge notes with headless workers against catalog gates, bundles, `type`/`collection` conformance, compression checks, or open-ended report criteria, reusing fresh stored results (hashed over each criterion's `watches:` note parts, criterion text, output contract, and any rejected finding decisions for that pair).
- Resume interrupted sweeps (`--resume`), dismiss worker problems or a single answer (`retry`), inspect retained observations (`show`), and run isolated single-assessment fixtures (`fixture create` / `--fixture`).
- Exact flags live in `commonplace-review --help` and `commonplace-review ACTION --help`.

**Cannot do (limitations):**
- **Never writes, fixes, commits, or reverts notes.** To edit or improve a note, switch to `cp-skill-revise`. Do not launch reviewer sub-agents yourself or review pairs in your own context.
- **No recursive directory sweeps or automatic ignored-tree pickup.** Passing a directory covers only its direct frontmatter-bearing notes (skipping indexes, `COLLECTION.md`, type specs, and subdirectories); notes in validation-ignored directories must be named explicitly.
- **No freshness or catalog results for `role`, `compression-synthesis`, `--criterion-file`, `--input`, or `--fixture` runs.** They never skip as fresh, never replace stored results, and `status` refuses `role` and `compression-synthesis` (inspect output with `commonplace-review show RUN`).
- **Reviewers cannot search the corpus.** A worker sees only the note, its criterion, files the note directly links to, and at most one criterion-derived local path (such as a snapshot for `(snapshot required)`). Corpus-wide discovery belongs to `cp-skill-connect` or `role`'s pre-collected inbound links.
- **Results are local and do not survive moves.** Result files live under gitignored `kb/reports/state/review/results/` on this machine; moving or renaming a note orphans old results (delete orphans as ordinary files; pairs review afresh).
- **Guard detects changes; it does not prevent or attribute them.** Profile write limits are best-effort (Claude Code's Bash denial is not verified to block writes; Codex and Pi can write the workspace). `guard.changed` lists paths changed during the run (including edits from other sessions), misses ignored files and mid-run reverts, and reverts nothing; only fixture trials fail on a dirty guard.
- **No certification.** `fresh` means inputs have not changed, not approval; `report` means a report criterion completed, not a verdict; `pass` means one gate found nothing to flag.

## Pick the command and selectors

- **Check status or warnings** (launches nothing):
  - `commonplace-review status NOTES... [--criteria ...] [--stale | --fresh]` — applicable pairs including `missing` ones.
  - `commonplace-review status --fresh --outcome warn fail --json` — current warnings across stored results (the fixing queue), with each result file path. Without `NOTES`, `status` lists every stored result and lists orphaned results separately.
- **Run a review**:
  - `commonplace-review NOTES... [--criteria ...] [--grouping pair|bundle] [--profile NAME]`
- **Selectors**:
  - Default (no `--criteria`): every catalog bundle plus `type` and `collection`.
  - Catalog gate ids (`prose/source-residue`), bundle names (`prose`), `type` / `type/<name>`, `collection` / `collection/<path>`.
  - Opt-in criteria (never included by default): `critique`, `friction`, `premises`, individual compression checks (`compression/core-claim-obscured`, `compression/branch-bloat`, `compression/detail-overhang`, `compression/marginal-value-redundancy`; bare `compression` is refused), `compression-synthesis` (one note, requires `--input ROLE=PATH`), and `role` (one note, collects inbound links).
  - Draft gate: `--criterion-file PATH` (evidence only; writes no catalog result).
  - Use `--force` only when the operator asks to re-judge fresh pairs. Under `--grouping bundle`, a pair with rejected findings is asked alone outside its bundle call.

## Execution environment

- **Worker-launching commands** (`commonplace-review NOTES...`, `--criterion-file`, `--fixture`, `--resume`) spawn the configured headless worker CLI, which needs outbound model-API network access and writable harness state outside the workspace. If your runtime runs shell commands in a sandbox that blocks network access or writes outside the workspace, run these commands outside that sandbox (requesting sandbox bypass or escalated execution up front) rather than probing inside the sandbox first.
- **Local-only commands** (`status`, `show`, `fixture create`, `retry`, `acknowledge`) launch no workers and need only workspace access; keep them in the default sandbox.

## Procedure

Resolve relative links below from this skill's real location in the library.

1. **Count what will launch before running.** For criteria with freshness, run `commonplace-review status NOTES... [--criteria ...] --stale`. Report the missing/stale count to the operator before spending paid launches; if none, stop. Confirm before launching when the operator has not already authorized that scope or launch count (including unassessed-freshness runs such as `role` and `compression-synthesis`).
2. **Choose grouping and run.** Use `--grouping bundle` for several catalog gates per note to share fixed context; keep the default `--grouping pair` for one or two gates or when independent contexts matter (bundle vs. pair verdict quality has not been compared). Apply the [execution environment](#execution-environment) rule before launching.
3. **Read the JSON report.** Check `counts`, `stopped`, `guard`, and per-pair `state`, `outcome`, and `problem`. Exit 0 means every pair has a current result, 1 means incomplete, and 2 means a command failure or another process holding the run. Always inspect `guard.changed`.
4. **Report results accurately.** If a `role` report lists relied-on terms or claims missing from the note's sibling write brief (`brief:` in frontmatter), tell the operator and offer to add them or create the brief in a separate write step (`cp-skill-write`); never edit a brief without the operator's word.
5. **Stops, retries, or multi-note sweeps.** Follow [run-review-batches.md](../run-review-batches.md) for `--resume`, `retry`, `acknowledge`, and stop handling.
