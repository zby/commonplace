# Dynamic Cheatsheet exact-run audit

**Disposition: hold.** Do not replace the integrated incumbent. This older
alternative has consequential route errors and an incorrect evidence-availability
qualification; it adds no new source coverage. No integration was performed.

## Identity and inspection boundary

- Assignment: `audit-dynamic-cheatsheet-2529cdc2795b`.
- Run: `AAS-2026-10-09-dynamic-cheatsheet-2529cdc2795b-01`.
- Method/worktree HEAD: `23c9d9a95050a95e02c46d50b14a00f0d91014be`.
- Worktree: `/home/zby/llm/commonplace/.commonplace/worktrees/dynamic-cheatsheet-2529cdc2795b` (W below).
- Source: `https://github.com/suzgunmirac/dynamic-cheatsheet`, frozen at
  `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`; actual checkout HEAD matches,
  and source `git status --short` is empty.
- Source root (S): `W/related-systems/suzgunmirac--dynamic-cheatsheet`.
- Publication (P): `W/kb/agentic-system-analyses/retained/dynamic-cheatsheet`.
- Run state (R): `W/kb/agentic-system-analyses/state/<run-id>`.
- Auditor: Pi, `openai/gpt-6.1-sol`, medium; session
  `01a13b23-a502-712f-84c4-8379340d1bfd`. Published worker: Luna/medium.
- Method: discrepancy-led comparison of public overview/synthesis, relevant
  reports, incumbent and historical leads; direct read-only source inspection
  of orchestration/driver plus two historical result rows. No target execution.

## Consequential findings

1. **Retrieval-synthesis retention is incorrectly denied.**
   `P/runtime.md`, RT-RTE-retrieval, says “no persistent sheet update is made
   by this route”; its memory annotation treats retrieved context as transient.
   But `S/dynamic_cheatsheet/language_model.py:531–574` supplies the incoming
   sheet to the synthesis curator and returns the synthesized text as
   `final_cheatsheet`. `S/run_benchmark.py:273–280` saves and carries that return
   into the next example. The next synthesis curator can therefore consume
   the previous synthesized sheet. This changes the write/read-back account,
   not merely wording about temporary ranked example packets. Public synthesis
   does not qualify this incorrect linked route account.
2. **The default benchmark does not load the described curator instructions.**
   `P/runtime.md:14` describes the ordinary default cumulative route as reading
   generator and curator prompt files. `S/run_benchmark.py:38,97–100` instead
   defaults the curator path to null and passes literal `(empty)` without one.
   The cumulative library branch still calls the model, but the documented
   question/answer/prior-sheet substitutions then have no placeholders to fill.
   The instruction-bearing update description needs its explicit prompt-path
   condition beside the public claim. The incumbent already states this limit.
3. **Uninspected historical outputs are described as unavailable.**
   `P/synthesis.md:20,29,33` says no actual updated sheet is available, no actual
   update is supplied, and no run outputs are supplied. Its own boundary includes
   tracked results. In `S/results/AIME_2024/gpt-4o_DynamicCheatsheet_Cumulative.jsonl`
   rows 1–2, row 1 saves answer/sheet content saying 15 against target 315;
   row 2's generator prompt contains that exact 2,040-character sheet.
   File SHA-256: `5434d5793269b0227d00688379597ec7a17ab6dd7e73656ce039c48f90278672`.
   This is historical saved delivery evidence, not a fresh run, producer-revision
   proof, target-truth proof or proof of reliance/benefit. The publication must
   distinguish available-but-unassessed payloads from absent evidence.

## Historical and incumbent comparison

The June account at `kb/agent-memory-systems/reviews/dynamic-cheatsheet.md`
provides same-revision coverage leads, not current truth. The later account
moved outside that collection to `kb/agentic-systems/reviews-archive/dynamic-cheatsheet.md`
(September run); it explicitly records synthesis carry-forward and the two-row
historical discrepancy, with provenance and causal limits. The origin incumbent
is `AAS-2026-10-12-dynamic-cheatsheet-ca0a0b29d273-01`, at the same source commit.
Its current overview/synthesis include the prompt-path condition, synthesis
carry-forward, workflow and bounded execution/scoring/restart qualifications.
No replacement advantage was established. This audit does not independently
certify every incumbent claim or require preservation of every historical detail.

## Publication, operational evidence and validation

All 12 destination files, including the assembled manifest, exactly match
`R/effects/publish.json`'s file set and SHA-256 map. Manifest hash:
`2470f4aa6e225e1edb3730b50fa25404050b9061c1e3b22b300d1236faf2bf9e`;
`R/state/attempts/000064-publish.json` is completed and pins that hash.
All 11 Markdown bytes also match `R/set/`; its type-only manifest differs as
expected. Missing `R/artifact/ARTIFACT.yaml` is the earlier layout, not corruption.
Attempts 000026-runtime and 000028-memory record completed Luna/medium outputs
matching published report hashes. These establish recorded submission/acceptance,
not performed source reads or preflight obligations. No exact-run trace is supplied;
worker operation and exhaustive compliance remain uncertified.

From W, using `W/.venv/bin/commonplace-validate`, the publication directory
and each of its 11 Markdown members returned `VALIDATION SUCCESS`, exit 0:
`Files analysed: 1`, `Text files: 0`, `Diagnostics: 0 failures across 0 subjects;
0 warnings across 0 subjects` per invocation. Owned origin report validation
also returned `VALIDATION SUCCESS`, exit 0, one text file and zero diagnostics.
These are frozen-method deterministic checks, not semantic clearance.

## Unblock and stop

Unblock only through separately authorized correction, reverification and
republication addressing findings 1–3, followed by a new exact-byte audit and
an explicit replacement justification. Keeping the incumbent requires no such
replacement. Stopped after these bounded discrepancies; no provider calls,
additional sources, delegation, state-writing commands or outside mutation.
