# Windows shim validation test plan

## Purpose

Validate the established Windows command design: Commonplace-owned shims invoke uv-managed Python and the Commonplace module, without invoking uv-generated `commonplace-*.exe` entry points.

## Preconditions

- Windows PowerShell execution.
- `uv` available by bare name.
- Network access to PyPI, or a populated uv cache.
- A disposable test directory outside the source checkout.
- Antivirus monitoring enabled.
- The shim implementation or temporary equivalent available for the run.

Use a project-local cache when the runner cannot access the default user cache:

```powershell
$env:UV_CACHE_DIR = Join-Path $TestRoot '.uv-cache'
```

## Shim registration

After completing INSTALL.md, register the deterministic test shims with [REGISTRATION.md](./test-shims/REGISTRATION.md). The registrar writes only a disposable bin directory and invokes the selected uv-managed Python directly. Prepend that bin directory to the test process PATH; do not add .venv\\Scripts and do not invoke generated commonplace-*.exe files.

## Test W1 — isolated installation

```powershell
uv venv $TestRoot\.venv
uv pip install --python $TestRoot\.venv\Scripts\python.exe -e .
```

Record dependency acquisition, build result, antivirus events, and whether any `commonplace-*.exe` was created or executed by the test harness.

## Test W2 — module dispatch

Invoke the CLI through uv-managed Python, bypassing generated entry points:

```powershell
& $TestRoot\\.venv\\Scripts\\python.exe -c "import sys; sys.argv=['commonplace-validate','--help']; from commonplace.cli.validate_notes import main; raise SystemExit(main())"
```

Record exit status and bounded help output.

## Test W3 — shim dispatch

Run the intended shim by bare name from a fresh PowerShell process. Verify that it reaches the same module behavior as W2 and does not call a generated Commonplace executable.

## Test W4 — initialized project

Initialize a disposable project through the shim, then validate a known fixture. Record the selected project root and package/runtime provenance.

## Test W5 — project isolation

Repeat W4 with a second project or worktree. Use distinct package/runtime markers where possible. Confirm that changing the working directory changes the selected project without changing the global user PATH.

## Test W6 — scripted operation

Run the larger scripted validation operation that previously triggered antivirus detection. Record the exact top-level shim command, child process behavior, duration, exit status, and antivirus result.

## Test W7 — fresh-process repeat

Terminate the PowerShell process. Start a fresh one and repeat W3 and W6. This tests that the supported path does not depend on shell mutation persistence.

## Evidence fields

Each report records:

- date, runtime, shell, Windows version if exposed;
- uv version and managed Python path;
- test root and project layout, normalized in the saved report;
- exact top-level commands;
- exit status and bounded output;
- whether a generated `commonplace-*.exe` was invoked;
- antivirus observation;
- project-selection result;
- checks not run and their prerequisites.

A test is **blocked** when installation cannot acquire dependencies, the shim is unavailable, or the antivirus result cannot be observed. Do not classify a blocked run as a pass or failure of the shim design.


