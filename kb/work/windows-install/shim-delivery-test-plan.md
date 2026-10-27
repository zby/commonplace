# Shim delivery test plan (round 2)

Status: written 2026-10-27 for the next runs: first on the reference machine (Smart App Control off, Defender only), then on the afflicted machine (Smart App Control on; Avast, McAfee and Defender registered) where the uv launchers were blocked. Round 1 is [shim-test-plan-round-1.md](./shim-test-plan-round-1.md) with its run [results-2026-10-27-acer-variant-u.md](./results-2026-10-27-acer-variant-u.md); it tested variant U only, on the reference machine.

## What is being decided

Every `commonplace-*` command is delivered on Windows through a shim: a `.cmd` file (and an `sh` file for Git Bash) that starts a Python interpreter on our module for that command. No uv-generated launcher `.exe` is on the supported path. The open question is which interpreter the shim starts, and `INSTALL.md` takes the answer. The variants:

| Variant | Interpreter the shim starts | How the package is installed | Signed? | Needs |
|---|---|---|---|---|
| **S** | python.org CPython, machine scope (`C:\Program Files\Python314\python.exe`) | `uv pip install --python <that python> --target <plain folder>`; the shim adds the folder with `site.addsitedir` | yes, Python Software Foundation | one elevated winget install; a code change for the released-package library root (windows-install proposal, code change 1) |
| **U** | uv-managed CPython (`python-build-standalone`) inside a uv venv or tool environment | `uv venv` + `uv pip install`, or `uv tool install` | no | uv only |
| **T** | the tool environment's `Scripts\python.exe` created by `uv tool install --python <signed python>` (a copy of python.org's signed `venvlauncher.exe`) | `uv tool install --python <signed python> llm-commonplace` | yes, by inheritance | the signed Python, and the `uv tool` layout that init and the health check already recognise |

S and U are the two deliveries under test. T is an optional third run: it keeps the current `INSTALL.md` layout and only changes the base interpreter, which may make it the smallest `INSTALL.md` change if it survives the afflicted machine. On that machine T's path `llm-commonplace\Scripts\python.exe` was still refused by Avast on 2026-10-27, so T is **blocked** there until that path is cleared or a different tool directory is used.

The decisive evidence is the afflicted machine. On the reference machine every antivirus result is **uninformative** (see round 1, W0 verdict); runs there establish only that the mechanism works.

## Prerequisites

Common:

- Windows PowerShell 5.1 (`powershell.exe`); `pwsh` is absent on the reference machine.
- `uv` by bare name. Set `$env:UV_CACHE_DIR` to a folder under the test root in every call that runs uv; inside the desktop app uv's default cache path is virtualised and too long.
- A disposable test root outside the checkout; the registrar at [test-shims/register-test-shims.ps1](./test-shims/register-test-shims.ps1).
- The round 1 plan's "Conflicting global installations" and "Antivirus observation" sections apply unchanged. Record `uv tool list` and the pre-registration `Get-Command` sources; prepend the test bin directory in every call; record the resolved source before every bare-name call.
- The testing rules in [README.md](./README.md): one command per first launch, never a loop over every executable, never WMI or `-EncodedCommand`, antivirus products and user `Path` recorded first, Smart App Control never turned off.

Variant S additionally:

```powershell
winget install --id Python.Python.3.14 -e --source winget --scope machine
(Get-AuthenticodeSignature 'C:\Program Files\Python314\python.exe') | Select-Object Status, @{n='Signer';e={$_.SignerCertificate.Subject}}
```

`Status` must be `Valid` with a Python Software Foundation signer. Record the exact Python version installed.

## The harness

[test-shims/register-test-shims.ps1](./test-shims/register-test-shims.ps1) writes one shim per `commonplace-*` entry point that the given interpreter can see, plus a dispatcher that resolves the entry point by name from the installed package metadata. It covers all commands, not only `init` and `validate`. Registration:

```powershell
# Variant S
powershell -NoProfile -File <checkout>\kb\work\windows-install\test-shims\register-test-shims.ps1 `
  -PythonPath 'C:\Program Files\Python314\python.exe' `
  -SitePackages <testroot>\site-packages `
  -BinDirectory <testroot>\bin-s

# Variant U
powershell -NoProfile -File <checkout>\kb\work\windows-install\test-shims\register-test-shims.ps1 `
  -PythonPath <testroot>\.venv\Scripts\python.exe `
  -BinDirectory <testroot>\bin-u
```

The harness differs from the production shims in two ways, record both: it dispatches through a Python file plus an environment variable rather than a `-c` program, and it resolves entry points at run time rather than at registration. Neither adds an executable to the path.

## Tests

Run the full series once per variant, in separate PowerShell tool calls, with a `$RunStart` captured at the top of each call and the antivirus observation taken at its end. Result classes are those of round 1: pass, partial, blocked, uninformative.

### R0 — instrument check (afflicted machine; recorded as uninformative elsewhere)

1. Record Smart App Control state, the `root\SecurityCenter2` products, and the baseline counts of Code Integrity events 3033/3077 naming Commonplace, Python or uv, Defender detections, and Avast's quarantine index and Auto-Sandbox log.
2. Run **one** uv-generated launcher once, from the variant's own install (`<testroot>\site-packages\bin\commonplace-validate.exe --help` for S after R1, `<testroot>\.venv\Scripts\commonplace-validate.exe --help` for U). Do not loop. Expect a Code Integrity 3077 block or an Avast reaction on the afflicted machine; record whichever occurred. If nothing occurred, the machine cannot discriminate and every antivirus result below is uninformative. Judge this step by the Code Integrity and antivirus records, not by the exit status: the S launcher exits 1 with `ModuleNotFoundError` even when nothing blocks it, because a `--target` folder is not on the signed interpreter's import path (observed on the reference machine, 2026-10-27). Smart App Control acts at process creation, before Python runs, so a block still shows as a 3077 event.

### R1 — install

Variant S, from the checkout root (editable, so the library root resolves through the checkout):

```powershell
uv pip install --python 'C:\Program Files\Python314\python.exe' --target <testroot>\site-packages -e <checkout>
```

Record the resolved package count, that uv also wrote launchers to `<testroot>\site-packages\bin`, and the antivirus observation. Do not delete those launchers before R0 step 2 has used one; delete them afterwards and record that.

Variant U:

```powershell
uv venv --python 3.14 <testroot>\.venv
uv pip install --python <testroot>\.venv\Scripts\python.exe -e <checkout>
```

Record the uv-managed interpreter's exact build and `Get-AuthenticodeSignature` status (expected `NotSigned`).

### R2 — direct module dispatch

Variant S:

```powershell
& 'C:\Program Files\Python314\python.exe' -c "import site, sys; site.addsitedir(r'<testroot>\site-packages'); sys.argv=['commonplace-validate','--help']; from commonplace.cli.validate_notes import main; raise SystemExit(main())"
```

Variant U: the same program through `<testroot>\.venv\Scripts\python.exe` without the `addsitedir` call. Record exit status and the first line of help.

### R3 — shim dispatch by bare name

Register the variant's shims. Then, in one call: prepend the variant's bin directory, record `(Get-Command commonplace-validate -CommandType Application).Source`, run `commonplace-validate --help`, record `$LASTEXITCODE`. Pass requires the recorded source to be the shim in the variant's bin directory. Repeat for `commonplace-source --help`, the command Smart App Control refused most often on the afflicted machine.

### R4 — initialised project

In `<testroot>\projects\one`: `git init`, then `commonplace-init --name one` through the shim; then `commonplace-init --check`; then `commonplace-validate landings`. Record exit statuses, the library root that init wrote into `.commonplace\library.md` (expected: the checkout's `kb` for an editable install), and whether init warned that commands resolve outside uv's tool directory (expected for S; record for U).

### R5 — second project

Repeat R4 in `<testroot>\projects\two`. This shows working-directory project selection only; both projects use the same installation. Report **partial** on that basis.

### R6 — validation sweep

From the checkout root, through the shim, one collection per statement:

```powershell
foreach ($c in 'theory','reference','instructions','agent-memory-systems','sources') { commonplace-validate $c; $LASTEXITCODE }
commonplace-validate landings
commonplace-validate redirects
```

Take collection names from the `COLLECTION.md` directories under `kb/` of the checkout under test and record the list used, **excluding `agentic-system-analyses`**. Agentic analysis runs on Linux only by operator decision (2026-10-27, [windows-test-suite](../windows-test-suite/README.md), item 1); validating that collection on Windows crashes on the `fcntl` import and tells us nothing about the shims. Record the exclusion in the report's target list instead of running it.

### R7 — fresh process

A new PowerShell tool call is a fresh process. Prepend the bin directory again, record provenance, repeat R3 and R6.

### R8 — every command starts (afflicted machine only, S and U)

One command per tool call, never a loop: run `--help` through the shim for each of the 25 entry points, with the antivirus observation after each. This is the operation that hung the afflicted machine when it was done through the uv launchers; through the shims no per-install executable is launched. Stop the series and record the point reached if any launch exceeds 30 seconds.

### R9 — Avast in normal use (afflicted machine, S and U)

Leave the variant registered and use it for ordinary validation over several days. Record any quarantine, sandbox or block entry, with date and file, and whether the commands still start. This is the only test that addresses the deletion observed on 2026-10-26.

## Evidence

One report per variant per machine, as `results-<date>-<machine>-<variant>.md` in this directory, with: the identity block, R0 instrument result, one row per test with exact command, exit status, resolved source, antivirus records in the window and result class, checks not run with the unmet prerequisite, state left behind, and the round 1 plan's disclosure review block. Normalise the checkout, home and test-root prefixes.

## Decision rule for `INSTALL.md`

Taken on the afflicted machine's reports only:

1. **U passes R0 through R8 and R9 shows nothing.** Windows keeps the uv-only prerequisite; `INSTALL.md` adds the shim step (already present as the Smart App Control section, which then becomes the normal Windows step 2). Smallest change.
2. **U is blocked or inconsistent and S passes.** The signed Python becomes a Windows prerequisite and S the main Windows procedure; U stays as the no-admin fallback with its known limit. This needs the library-root code change for released packages before `INSTALL.md` changes.
3. **T passes where it can run.** Prefer T over S when both pass: it keeps the `uv tool` layout and the existing shim snippet, so init and the health check need no change.
4. **Both S and U fail on Smart App Control or Avast.** The problem is not the launcher; record what was blocked and return to the windows-install README's open problems.

Until one of these is recorded, `INSTALL.md` keeps its current Windows text.
