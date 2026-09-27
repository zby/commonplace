---
description: "Use before a demo or release to execute user scenarios in an isolated Commonplace installation and check outcomes."
type: types/instruction.md
---

# Test Commonplace in an isolated installation

Determine whether an external user can complete ordinary wiki operations
using the installed package and its instructions.

You are the orchestrator. Read the scenario pack, launch its tasks, inspect
results, and judge each outcome. Scripts handle process isolation and state
capture; keep scenario decisions yourself. Agents under test receive only
the current prompt, installed instructions, and permitted inputs.

## Choose the package and runtime

- Default to a new wheel built from the working Commonplace checkout, including
  uncommitted package changes. Use a supplied wheel or PyPI release only when
  explicitly selected. Never substitute an editable install or silently fall
  back to a released version.
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
   `tools/`, `bin/`, `package/`, `inputs/`, and `records/`. Keep evaluator
   records and future fixtures outside the worker's readable scope. Save a
   copy of this instruction and the selected scenario pack in `records/` and
   use those copies throughout this run. The default pack is
   `tests/scenarios/installed/README.md` in the source checkout.
2. For a local build, record Git HEAD and whether the working tree is dirty.
   Build with `uv build --wheel --no-sources --no-config --out-dir
   <run>/package <checkout>`, using absolute paths. Put build temporary files
   and `UV_CACHE_DIR` under the run directory. Otherwise retain the explicitly
   selected wheel there. Record its origin, version, and SHA-256; the checksum
   identifies the actual build even when its version is unchanged. Stop on a
   build failure. No commit, version bump, or publication is needed.
3. From outside the checkout, install the exact wheel by absolute path with
   `uv tool install --no-config`, setting `UV_TOOL_DIR=<run>/tools`,
   `UV_TOOL_BIN_DIR=<run>/bin`, and `UV_CACHE_DIR=<run>/cache`. Use a Python
   interpreter accessible inside the isolation boundary. Put this bin directory
   first on the test PATH; verify the commands resolve there. Do not update
   the shell profile or developer installation. Set
   `PYTHONDONTWRITEBYTECODE=1` for setup, evaluator commands, and workers.
4. Initialize only the disposable project with `commonplace-init --root
   <project> --name <scenario-project>`. From that project, run
   `commonplace-init --check` and `commonplace-validate landings`. Supply local
   snapshots only at the stages named by the pack. No HTTP server or capture
   tools are needed; do not fetch the fixtures' synthetic URLs.
5. Verify that the worker can read the installed library and its permitted
   inputs, while the installation is read-only and the project has the chosen
   write mode. Exclude the parent conversation, checkout, personal memory,
   unrelated configuration/skills, evaluator records, and earlier session
   logs. An empty chat or temporary working directory alone is insufficient.
   Record the isolation check once, plus CLI/model/OS and network boundary.
   The worker may use native sub-agents when an installed skill requires them.
6. Archive the initial project and inventory installed `tools/` and `bin/`
   once. Use the state helper below. Do not archive or rehash the installation
   after every stage when it stays mounted read-only.

## Run the scenarios

For each stage, in order:

1. Supply its permitted fixtures, resolve prompt paths, and capture the project
   inventory. Use the exact scenario prompt; keep the acceptance key private.
2. Launch a fresh CLI session rooted in the test project. Preserve its raw
   trace and available session logs. Enforce read-only project access for
   answer stages. Observe the time limit and stop its workers when it expires.
3. Once the worker stops, capture and compare the project inventory. Inspect
   its response, changed artifacts, and cited evidence against the pack's
   acceptance key. Run the installed validator on authored KB artifacts from
   the disposable project. Check warnings according to the pack. A zero
   process exit code or the worker's self-report is not a verdict.
4. Inspect relevant trace evidence: runtime errors, project instruction loading,
   and fresh-worker launches where an installed skill requires them. Verify
   bootstrap's newly created instructions in the next scenario's session;
   do not launch a separate verification conversation. Missing evidence for
   a required criterion is a blocker, not an assumed pass.
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
`tools/` and `bin/` with their initial inventories. An unexpected installation
change prevents a full-chain pass. On interruption, preserve partial logs
and state and mark incomplete work `not run: interrupted`; distinguish this
from a timeout or product failure. Recover missing records after an abrupt
termination without inventing an exit status.

Write one short `records/report.md`: package origin/version/checksum,
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
