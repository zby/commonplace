# Theory installed-project rehearsal

**Outcome: pass.** All six stages passed without supervisor assistance or product repair.

This is the supervisor's record for the Theory rename acceptance check, run on
2026-10-23 using [the isolated installation procedure](../../instructions/test-installed-commonplace.md)
and the installed scenario pack at the source commit below. Evidence paths in
this report are relative to
`/tmp/commonplace-theory-rehearsal-p3hafr_1/records/`. Raw traces, session logs,
input/source/final archives and inventories remain there for operator review;
this summary is readable without those local files. Do not discard the run
before operator acceptance. It tests one installed Aster Lending Library wiki,
not every external Commonplace consumer.

- Source: clean tracked checkout `f698aa90dacd936cc7ef6268f489ca0a5ec57ce9`, non-editable local install.
  Inventory, exclusions and source archive: `source-selection.json`, `source-initial/`.
  INSTALL.md SHA-256: `b53dc21598d39ba9cfe301b4f283b8141e8d62dde27785c5785ca98877ec748a`.
- Runtime: Codex CLI 0.163.0, gpt-6.1-sol, medium effort, separate CLI process per stage.
  Parent runs Pi; Codex was selected because the repository provides a verified
  Linux/Bubblewrap launcher for it. This is not a Pi runtime rehearsal.
- Isolation: repository helper; source read-only in stage 0, hidden later;
  tools/bin read-only later; stages 3/5 project read-only; evaluator records,
  future fixtures, real checkout and personal configuration hidden.
- Installation: llm-commonplace 0.2.0, /usr/bin/python3 3.12.3, regular local-source
  uv tool installation. direct_url.json confirms non-editable origin. Build
  output is in the stage-0 trace; wheel availability/checksums are recorded in
  `0-install-acceptance.json`. No wheel was rebuilt just to obtain evidence.
- Fresh instructions: full project AGENTS.md loaded automatically in all five
  later stages; see `instruction-loading-audit.json` and raw session logs.

| Stage | Outcome | Evidence |
|---|---|---|
| 0 install/setup | pass | `0-exec/`, `0-supervisor-validation.log`, `0-install-acceptance.json` |
| 1 write note | pass | `1-exec/`, `1-supervisor-validation.log`, `1-acceptance.json` |
| 2 ingest v1 | pass | `2-exec/`, `2-fixture.json`, `2-supervisor-validation.log`, `2-acceptance.json` |
| 3 answer before change | pass | `3-exec/`, `3-supervisor-validation.log`, `3-acceptance.json` |
| 4 incorporate v2 | pass | `4-exec/`, `4-fixture.json`, `4-supervisor-validation.log`, `4-acceptance.json` |
| 5 answer after change | pass | `5-exec/`, `5-supervisor-validation.log`, `5-acceptance.json` |

The fresh package exposes library Theory and scaffolds project Notes without
creating a Theory twin. Native ingest workers use fork_turns none and have
separate retained session logs. Both input snapshots and the v1 ingest's checksum
remain unchanged. Current guidance uses 72 hours for camera kits, seven days for
tripods, and inspection distinct from return recording. The former 48-hour rule
is historical. Both answer stages correctly leave fees unspecified and change
no project files. Every authored/cited artifact checked by the supervisor passed
installed validation without warnings.

Source files are unchanged after installation. Final tools/bin inventories
match their post-installation baselines exactly. Final project archive:
`project-final/`. All owned CLI processes exited, none timed out. Recovered or
expected command failures are retained in stage acceptance records: an initial
Git-root probe preceded git init; content searches and diff commands reported
normal nonzero results; stage 4 briefly checked for an unfinished worker's output
before waiting for it. No supervisor intervention, commits or publication occurred.

No product issue blocks this pack. Untested: live source capture, published-PyPI
installation, another OS/runtime, and arbitrary external consuming projects.
Keep this run and its report until the operator accepts disposal.
