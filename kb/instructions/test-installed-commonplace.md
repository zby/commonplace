---
description: "Use before a demo or release to execute user scenarios in an isolated Commonplace installation and check outcomes."
type: types/instruction.md
---

# Test Commonplace in an isolated installation

Determine whether an agent can install Commonplace by following INSTALL.md
and then complete ordinary wiki operations in fresh sessions.

You are the orchestrator. Read the scenario pack, launch its tasks, inspect
results, and judge each outcome. Scripts handle process isolation and state
capture; keep scenario decisions yourself. Agents under test receive only
the current prompt and permitted inputs. The installation agent reads the
source copy's INSTALL.md by following a path in its prompt; do not supply the
document separately or inline its contents. Later agents use only the
installed project.

## Choose the package and runtime

- Default to a disposable source copy of the working Commonplace checkout,
  including tracked working-tree changes and explicitly identified untracked
  package inputs. The installation agent installs from that directory with
  a regular, non-editable install; the installer builds the package. Do not
  prebuild a wheel, install Commonplace, or run init on the agent's behalf.
  A published-release test must be explicitly selected and recorded separately.
- Find a command-line agent similar to yourself: prefer your application's CLI
  counterpart and the same model where available. Verify its supported launch
  options and record material differences. Launch each task in a separate
  process with fresh context, not an internal sub-agent or resumed chat.
- If no suitable CLI, authentication, or isolation mechanism is available,
  report the blocker and stop. Do not attempt the scenarios yourself.
- Default limits are 15 minutes per stage and 60 minutes overall. Use a smaller
  process timeout when less run time remains. Do not reconstruct token or cost
  figures that the runtime does not provide.

For Codex CLI on Linux, use the conditional
[Codex launch branch](./test-installed-commonplace-codex.md). Other runtimes
must satisfy the same isolation and evidence requirements through verified
launch mechanisms.

## Prepare once

1. Create a disposable run directory outside the checkout with `project/`,
   `tools/`, `bin/`, `source/`, `cache/`, `tmp/`, `inputs/`, and `records/`. Keep evaluator
   records and future fixtures outside the worker's readable scope. Save a
   copy of this instruction and the selected scenario pack in `records/` and
   use those copies throughout this run. The default pack is
   `tests/scenarios/installed/README.md` in the source checkout.
   Before launching, check that each acceptance requirement follows from its
   prompt, supplied inputs, or installed contracts. A required citation target
   or execution method must be explicit there; otherwise accept equivalent
   evidence and methods. Resolve contradictions before freezing the pack.
2. Record Git HEAD, working-tree status, and the selected source files. Copy
   them to `<run>/source/`, preserving the paths required by the build and
   the full `INSTALL.md`. Exclude `.git`, credentials, local environments,
   caches, runtime state, prior transcripts, and the scenario pack, acceptance
   key, and future fixtures. Record exclusions and hash/archive the supplied
   tree so its exact inputs are recoverable. Verify that the build inputs
   remain complete; stop rather than silently substitute committed files for
   selected working-tree changes. Keep the real checkout inaccessible.
3. Prepare an empty `project/` and isolated writable tool, executable, cache,
   and build-temporary directories. Provide Python and uv as runtime
   prerequisites, not a Commonplace installation. Set `UV_TOOL_DIR`,
   `UV_TOOL_BIN_DIR`, `UV_CACHE_DIR`, and `TMPDIR` to those run-local paths,
   put the run's executable directory first on PATH, and set
   `PYTHONDONTWRITEBYTECODE=1`. Do not modify the user's shell profile.
4. Verify the installation boundary before stage 0: the agent can read the
   source copy, including its INSTALL.md, write installation outputs and the project (including `.agents/skills/`),
   and use the build/dependency and model services needed for installation.
   It cannot access the real checkout, personal instructions/configuration,
   evaluator records, or future fixtures. Start in `project/`; the source
   checkout's contributor instructions must not become project instructions.
   Permit build-generated files only in the disposable source/build area;
   the agent may not repair or alter the supplied source or INSTALL.md.
5. Point stage 0 to `INSTALL.md` inside the source copy. Give it the source
   and project paths, the scenario brief, and the
   isolation adaptations: follow INSTALL.md's full-install path, replacing
   the published package argument with the source directory, without
   `--editable`; use the supplied run-local tool directories and PATH instead
   of changing a real shell profile. Select a Python interpreter available
   to later sessions. Skip optional live-capture dependencies: this pack uses
   fixed snapshots. Do not replace INSTALL.md with a supervisor-written list
   of installation or template-activation steps, a separate copy, or inline
   excerpts. The prompt names the file; the agent reads it from the source.
6. Archive the empty project before stage 0. After that agent finishes, inspect
   its trace for reading INSTALL.md and performing the build/install, init,
   and setup. Verify command resolution, installed package origin/version,
   and absence of editable/source-tree dependencies. Retain build logs and
   wheel checksum if the installer leaves a wheel available; do not rebuild
   solely to obtain one. Compare the supplied source with its initial
   inventory and distinguish build outputs from forbidden source edits.
7. From the initialized project, run the installed `commonplace-init --check`
   and `commonplace-validate landings`, then assess stage 0's project files.
   Before stage 1, remove source/build/cache access and mount installed
   `tools/` and `bin/` read-only. Inventory that accepted installation as the
   baseline for final integrity checks. Probe command startup and library
   access in this later-session boundary. Each later stage gets only its
   prompt, the project, installed library, and that stage's permitted fixtures.
   Stages 3 and 5 also mount the project read-only. The worker may use native
   sub-agents when an installed skill requires them.

## Run the scenarios

For each stage, in order:

1. Supply its permitted fixtures, resolve prompt paths, and capture the project
   inventory. Use the exact scenario prompt; keep the acceptance key private.
2. Launch a fresh CLI session rooted in the test project. Preserve its raw
   trace and available session logs. Enforce read-only project access for
   answer stages. Observe the time limit and stop its workers when it expires.
3. Once the worker stops, capture and compare the project inventory. Inspect
   its response, changed artifacts, and cited evidence against the pack's
   acceptance key. Run the installed validator on authored and cited KB
   artifacts from the disposable project. Use a collection root or individual
   artifact paths; a report subdirectory need not be a collection. Let the
   validator check quote matching, snapshot checksums, and source pairing;
   assess policy meaning and evidential support yourself. Do not require the
   worker to duplicate mechanical checks. Check warnings and unavailable-source
   diagnostics according to the pack. A zero process exit code or the worker's
   self-report is not a verdict.
4. Inspect relevant trace evidence: runtime errors, project instruction loading,
   and fresh-worker launches where an installed skill requires them. Verify
   bootstrap's newly created instructions in the next scenario's session;
   do not launch a separate verification conversation. Missing evidence for
   a required criterion is a blocker, not an assumed pass.
   Include delegated workers and nested tool results in the audit. Inspect
   command diagnostics even when a compound command exits zero. Record each
   recovered error with its cause, recovery, and effect on acceptance; separate
   expected nonzero results such as a diff showing changes or a search finding
   no matches. A clean final artifact does not erase earlier execution errors.
5. Record `pass`, `fail`, or `blocked` with a short reason and evidence paths.
   Stop on the first failure or blocker and mark remaining stages `not run`.
   Keep diagnosis and repair out of this rehearsal; after a fix, start a new
   run. Answer domain questions only from the pack's brief. For Commonplace
   guidance, reply `Use the installed instructions and your judgment`. Record
   any intervention; an assisted result cannot pass the unassisted chain.

Detailed context accounting is optional: collect it only when requested.
Normally retain raw logs and any usage totals the runtime already emits;
report missing figures as unknown. Do not count file reads or reconstruct
context sizes as a prerequisite for advancing to the next stage.

## Finish or stop

Stop owned processes, then archive the final project and compare installed
`tools/` and `bin/` with their post-installation baseline inventories. If
installation never completed, retain its partial outputs and mark later
stages not run. An unexpected installation
change prevents a full-chain pass. On interruption, preserve partial logs
and state and mark incomplete work `not run: interrupted`; distinguish this
from a timeout or product failure. Recover missing records after an abrupt
termination without inventing an exit status.

Write one short `records/report.md`: source origin/inventory, INSTALL.md hash,
installed package origin/version, available build or wheel evidence,
runtime and isolation method, a stage outcome table with evidence paths,
interventions, and the first issue to fix. The chain passes only if all stages
and final integrity checks pass without repair. List untested surfaces; local
snapshots do not test source capture. Retain the run and report until the
operator accepts their disposal. Do not modify the real KB, publish, commit,
or repair Commonplace as part of this procedure.

## State helper

The orchestrator uses `scripts/capture_test_state.py` from the checkout:

```bash
python3 scripts/capture_test_state.py capture <directory> <new-record-directory>
python3 scripts/capture_test_state.py compare <before-record-directory> <after-record-directory>
```

Add `--archive` to the initial and final project captures. Use unique output
paths outside the captured directory. Capture writes `inventory.json` and,
with `--archive`, `files.tar.gz`; compare prints added, removed, and modified
paths. Changes still return exit status 0. Interpret these facts yourself.
