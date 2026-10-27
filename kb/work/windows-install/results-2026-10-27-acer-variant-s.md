# Shim delivery round 2, variant S: Claude Code / Windows 11 Home / Windows PowerShell 5.1 (run s1)

- Round and procedure: round 2, [shim-delivery-test-plan.md](./shim-delivery-test-plan.md), tests R0–R7; R8 and R9 are afflicted-machine-only and were not run. Round 1's "Result classes", "Conflicting global installations" and "Antivirus observation" sections ([shim-test-plan-round-1.md](./shim-test-plan-round-1.md)) applied unchanged.
- Variant: **S**, shims that start the signed python.org interpreter (`C:\Program Files\Python314\python.exe`) and add a `uv pip install --target` folder with `site.addsitedir`.
- Checkout: `<WORKSPACE>`, `llm-commonplace` 0.3.0, HEAD `91d16ce27` ("Move the Windows shim delivery work into windows-install and retire superseded evidence"); one pre-existing untracked directory `kb/reports/connect/`, not created by this run.
- Prior related report: [results-2026-10-27-acer-variant-u.md](./results-2026-10-27-acer-variant-u.md), variant U on this same machine earlier today (run w3). This report follows its structure. It closes two of that run's gaps: the provenance expression is taken with `Select-Object -First 1` (its finding 3), and the harness now registers all 25 entry points rather than two ("Other package entry points" in its checks not run). Its signed-interpreter gap ("Signed python.org interpreter path") is what this run tests.
- Machine: the reference machine of the plan (Smart App Control off, Defender only). Every antivirus result below is **uninformative**.

## Identity

| Field | Value | Basis |
|---|---|---|
| Date/time | 2026-10-27, 21:15–21:25 local (UTC+1) | observed |
| Runtime and surface | Claude Code agent (subagent), PowerShell tool | observed |
| Runtime version | unknown | unknown |
| OS and version | Windows 11 Home, `Microsoft Windows NT 10.0.26300.0` | observed |
| Shell | Windows PowerShell 5.1.26100.9711 (`powershell.exe`); `pwsh` not installed | observed |
| Tool execution interface | every PowerShell tool call is a fresh process (distinct PIDs per call, e.g. 28044, 19712, 27460, 13504, 13084); the test bin directory was re-prepended in each | observed |
| Workspace | `<WORKSPACE>` (Git checkout, see above) | observed |
| Test root | `<TESTROOT>` = `<HOME>\commonplace\tmp\windows-shim-test-s1`, outside the checkout; did not exist before the run; left in place | observed |
| uv | `uv 0.11.29 (901092ee1 2026-07-15 x86_64-pc-windows-msvc)`, resolved at `<HOME>\.local\bin\uv.exe` | observed |
| `UV_CACHE_DIR` | `<TESTROOT>\.uv-cache`, set in every call that ran uv | observed |
| Interpreter under test | `C:\Program Files\Python314\python.exe`, CPython 3.14.7, `sys.prefix` `C:\Program Files\Python314`; Authenticode `Valid`, signer `CN=Python Software Foundation, O=Python Software Foundation, L=Beaverton, S=Oregon, C=US`; `importlib.util.find_spec('commonplace')` is `None` (no package in its own site-packages) | observed |
| Package folder | `<TESTROOT>\site-packages` (`--target`); `llm_commonplace-0.3.0.dist-info`, `_editable_impl_llm_commonplace.pth` → `<WORKSPACE>\src` | observed (R1, R2) |
| Antivirus | Windows Defender only in `root\SecurityCenter2` (`productState` 0x61100); AMProductVersion 4.18.26090.9, AMEngineVersion 1.1.26090.9, AntivirusSignatureVersion 1.461.230.0; real-time and behavior monitoring on; tamper protected | observed |
| Defender cloud/ASR | MAPSReporting 2, CloudBlockLevel 0, SubmitSamplesConsent 1, PUAProtection 2, `AttackSurfaceReductionRules_Ids` and `_Actions` null (no rules); exclusions: unknown (admin required) | observed |
| Smart App Control | `VerifiedAndReputablePolicyState` 0 (off) | observed |

## Conflicting installation record

Recorded before shim registration, in a process without the test bin directory:

| Observation | Result |
|---|---|
| `uv tool list` | `llm-commonplace v0.1.4` with `commonplace-*` entry points (first lines only retained) |
| `Get-Command commonplace-validate, commonplace-init, commonplace-source -All` | `commonplace-validate.exe` → `<HOME>\.local\bin\commonplace-validate.exe`; `commonplace-init.exe` → `<HOME>\.local\bin\commonplace-init.exe`; `commonplace-source`: no match |
| Tool environment | not re-inspected; the variant-U report records it as an editable install of `<WORKSPACE>`, dist-info 0.1.4 |

Option chosen: "keep it and prepend". `<TESTROOT>\bin-s` was prepended to `$env:PATH` inside every call that used a bare name, and `(Get-Command <name> -CommandType Application | Select-Object -First 1).Source` was recorded in the same call before every bare-name invocation. `uv tool uninstall` was not run; the user `PATH`, profiles, Defender settings and the signed Python's own site-packages were not modified.

After registration `Get-Command commonplace-validate -CommandType Application` returns three matches in order: `<TESTROOT>\bin-s\commonplace-validate.cmd`, `<TESTROOT>\bin-s\commonplace-validate` (the extensionless `sh` shim, which PowerShell lists as an application but does not execute for a bare name), `<HOME>\.local\bin\commonplace-validate.exe`. `commonplace-source` returns the two `bin-s` files only. The executed file was confirmed with `Trace-Command -Name CommandDiscovery` in R3, R6 and R7: the invocation-time "Command Found" record names the `.cmd` shim every time.

## R0 — instrument check

### Step 1: machine state

| Check | Result | Matches afflicted configuration? |
|---|---|---|
| Smart App Control | off (`VerifiedAndReputablePolicyState` 0) | no |
| `root\SecurityCenter2` products (read-only `Get-CimInstance`) | Windows Defender only | no (no Avast, no McAfee) |
| Code Integrity 3033/3077, total | 335 (unchanged from the variant-U run) | — |
| Code Integrity 3033/3077 naming Commonplace, Python or uv | 0 | no |
| `Get-MpThreatDetection` / `Get-MpThreat` | 0 / 0 records | — |
| Avast quarantine index, Auto-Sandbox log | not applicable (Avast not installed) | — |

No process was started through WMI and `-EncodedCommand` was not used anywhere in this run.

### Step 2: one uv-generated launcher, once

After R1, from `<WORKSPACE>`, observation armed (`$RunStart` 21:16:30):

```powershell
& <TESTROOT>\site-packages\bin\commonplace-validate.exe --help
```

The launcher is `NotSigned`, 46 080 bytes. Exit **1** after 0.4 s, 6 output lines, first lines `Traceback (most recent call last):` / `File "<frozen runpy>", line 203, in _run_module_as_main`; only the first two lines were retained. The launcher's embedded script (read from the file, not executed again) names `#!C:\Program Files\Python314\python.exe` and `from commonplace.cli.validate_notes import main`; the target folder is not on that interpreter's `sys.path`. The same import run directly with the signed Python, without the folder, ends `ModuleNotFoundError: No module named 'commonplace'` (exit 1). The launcher's error is therefore inferred to be that `ModuleNotFoundError`; it was not observed in full. Defender detections since `$RunStart`: 0; Defender events 1116/1117/1121/1122: 0; Code Integrity 3033/3077 (any): 0. The executable was still present afterwards.

### R0 verdict

No record from executing the generated launcher. **This machine cannot discriminate**; every antivirus result below is **uninformative**. For the afflicted-machine run: under variant S the `--target` launcher fails with exit 1 even when nothing blocks it, so R0 step 2 there must be judged on Code Integrity and Avast records and on whether Python started at all, not on the exit status.

## Results

All bare-name calls ran after prepending `<TESTROOT>\bin-s` in the same call, with the resolved source recorded first. "Antivirus records" are Defender detections since `$RunStart`, Defender events 1116/1117/1121/1122, and Code Integrity 3033/3077 naming Commonplace, Python or uv.

| Test | Exact top-level command(s) as run | Exit status | Resolved source (bare name) | Generated exe invoked? | Antivirus records in window | Result class and reason |
|---|---|---|---|---|---|---|
| R0 instrument check | `& <TESTROOT>\site-packages\bin\commonplace-validate.exe --help` (once) | 1 | n/a (explicit path) | **Yes**, once, the only invocation in the run | `$RunStart` 21:16:30; 0 / 0 / 0 (CI any: 0) | **uninformative**: no record; machine cannot discriminate |
| R1 install | `uv pip install --python 'C:\Program Files\Python314\python.exe' --target <TESTROOT>\site-packages -e <WORKSPACE>` | 0 | n/a | No. uv wrote 29 executables to `<TESTROOT>\site-packages\bin`: 25 `commonplace-*.exe` plus `dotenv.exe`, `idna.exe`, `jsonschema.exe`, `normalizer.exe`; after R0 step 2 the whole `bin` folder (29 files) was deleted and its absence confirmed | `$RunStart` 21:16:08; 0 / 0 / 0 | **pass** (installation): `Using CPython 3.14.7 interpreter at: C:\Program Files\Python314\python.exe`; `Resolved 22 packages`, `Built llm-commonplace @ file:///<WORKSPACE>`, `Installed 22 packages`, 11.1 s. Antivirus **uninformative** per R0 |
| R2 direct module dispatch | `& 'C:\Program Files\Python314\python.exe' -c "import site, sys; site.addsitedir(r'<TESTROOT>\site-packages'); sys.argv=['commonplace-validate','--help']; from commonplace.cli.validate_notes import main; raise SystemExit(main())"` | 0 | n/a (explicit path) | No | not armed | **pass**: 27 lines, first `usage: commonplace-validate [-h] [--full \| --json] [--output OUTPUT]`. From the same interpreter after `addsitedir`: `commonplace` from `<WORKSPACE>\src\commonplace\__init__.py`; `sys.prefix` `C:\Program Files\Python314`; distribution `llm-commonplace` 0.3.0 located at `<TESTROOT>\site-packages` |
| R3 registration | `powershell -NoProfile -File <WORKSPACE>\kb\work\windows-install\test-shims\register-test-shims.ps1 -PythonPath 'C:\Program Files\Python314\python.exe' -SitePackages <TESTROOT>\site-packages -BinDirectory <TESTROOT>\bin-s` | 0 | n/a | No. `bin-s` holds 25 `.cmd`, 25 extensionless `sh` shims, 1 dispatcher `.py`, 0 `.exe` | `$RunStart` 21:17:11; 0 / 0 / 0 | Printed `Distribution : 0.3.0 <TESTROOT>\site-packages`, `Count : 25`, and a **false-positive warning** (finding 2) |
| R3 shim dispatch | `commonplace-validate --help` (bare name, from `<WORKSPACE>`, inside `Trace-Command -Name CommandDiscovery`); separate call: `commonplace-source --help` (same) | 0; 0 | `<TESTROOT>\bin-s\commonplace-validate.cmd`; `<TESTROOT>\bin-s\commonplace-source.cmd`; trace "Command Found" names the shim in both | No | `$RunStart` 21:17:28 and 21:17:43; 0 / 0 / 0 each | Dispatch **pass**: validate help 27 lines, identical line for line to R2 run in the same call; source help 6 lines, first `usage: commonplace-source [-h]`. Antivirus **uninformative** |
| R4 initialised project | in `<TESTROOT>\projects\one` after `git init`: `commonplace-init --name one`; `commonplace-init --check`; `commonplace-validate landings`; `commonplace-validate kb/notes/shim-fixture-one.md` | 0; 0; 0; 0 | `bin-s\commonplace-init.cmd` / `bin-s\commonplace-validate.cmd` before each | No | not armed | **pass**: `Initialized Commonplace project at <TESTROOT>\projects\one`; `--check` 26 of 26 `ok:`; landings `VALIDATION SUCCESS`; fixture `VALIDATION SUCCESS`. Library root `<WORKSPACE>/kb` (below) |
| R5 second project | in `<TESTROOT>\projects\two` after `git init`: `commonplace-init --name two`; `commonplace-init --check`; `commonplace-validate landings`; `commonplace-validate kb/notes/shim-fixture-two.md`; `commonplace-validate kb/notes/shim-fixture-one.md`; then from `projects\one`: `commonplace-validate kb/notes/shim-fixture-two.md` | 0; 0; 0; 0; 1; 1 | shim before each | No | not armed | **partial**: project selection shown (each fixture validates only in its own project; the other reports `No matching note found for: kb/notes/shim-fixture-…md`). Both projects use one installation, so isolation is not shown |
| R6 validation sweep | from `<WORKSPACE>`, inside one `Trace-Command -Name CommandDiscovery`: one statement per target, `commonplace-validate <target>`, 14 targets (below) | 11 × 0; 3 × 1 | provenance recorded before each: 14 of 14 `bin-s\commonplace-validate.cmd`; trace: 14 of 14 invocation lookups found the shim (the other 42 "Command Found" records are the `Get-Command` provenance lookups, 3 per target) | No | `$RunStart` 21:19:23; 0 / 0 / 0 | **uninformative** (antivirus, per R0). Dispatch observed with provenance, 136 s. The three exit-1 targets are product results, identical to variant U |
| R7 fresh process | separate call (PID 13504): before prepend `bin-s` not on `PATH` and `commonplace-validate` resolves to `<HOME>\.local\bin\commonplace-validate.exe` (not invoked), `commonplace-source` to nothing; after prepend, inside `Trace-Command`: `commonplace-validate --help`, `commonplace-source --help`, then the 14-target sweep, each spelled `& $name @args` with `$name` a bare command name; supplementary call (PID 13084): literal `commonplace-validate --help` and `commonplace-source --help` | help 0, 0; sweep 11 × 0, 3 × 1; supplementary 0, 0 | 16 of 16 recorded and traced to `bin-s\*.cmd` (15 validate, 1 source); supplementary 2 of 2 | No | `$RunStart` 21:22:27 and 21:25:03; 0 / 0 / 0 each | **uninformative** (antivirus, per R0). Fresh-process resolution after re-prepend observed; all 14 sweep outputs byte-identical to R6. Does not test desktop-runtime `PATH` inheritance |

### R6/R7 target list and per-target results

Targets: the twelve top-level `kb/*/COLLECTION.md` directories of this checkout (`agent-memory-systems agentic-system-analyses agentic-systems articles instructions reference reports sources tags theory types work`) plus `landings` and `redirects`, the same 14 as the variant-U run.

| Target | R6 exit / first line / diagnostics | R7 exit | Matches variant U? |
|---|---|---|---|
| agent-memory-systems | 0 / VALIDATION WARNING / 0 failures, 2 warnings (171 files) | 0 | yes |
| agentic-system-analyses | 1 / `Traceback (most recent call last):` … `ModuleNotFoundError: No module named 'fcntl'` (`<WORKSPACE>\src\commonplace\lib\agentic_analysis\effects.py` line 9) | 1 | yes |
| agentic-systems | 0 / VALIDATION SUCCESS (24 files) | 0 | yes |
| articles | 0 / VALIDATION SUCCESS (8 files) | 0 | yes |
| instructions | 0 / VALIDATION SUCCESS (122 files) | 0 | yes |
| reference | 0 / VALIDATION WARNING / 2 warnings (242 files) | 0 | yes |
| reports | 1 / VALIDATION FAILED / 10 failures, 1 warning (10 × `validation.base.frontmatter-type`, 1 × `validation.base.link-health`) | 1 | yes |
| sources | 1 / VALIDATION FAILED / 2 failures across 1 subject, 22 warnings (rule ids include `validation.base.source-quotes`, `validation.base.verbatim-quote`, `validation.base.link-health`, `validation.schema.frontmatter-genre`) | 1 | yes |
| tags | 0 / VALIDATION WARNING / 1 warning | 0 | yes |
| theory | 0 / VALIDATION SUCCESS (450 files, 50 lines) | 0 | yes |
| types | 0 / VALIDATION WARNING / 1 warning | 0 | yes |
| work | 0 / VALIDATION WARNING / 21 warnings across 6 subjects | 0 | yes |
| landings | 0 / VALIDATION SUCCESS | 0 | yes |
| redirects | 0 / VALIDATION SUCCESS | 0 | yes |

The `fcntl` crash is open problem 10 in [README.md](./README.md); it reproduces under the signed interpreter as under the uv-managed one. The `reports` and `sources` failures have the same counts and rule ids as in the variant-U run, so they do not depend on the interpreter; whether they are Windows-specific was not determined.

### Installation behavior observed (R4/R5, not shim results)

- **Library root.** Both projects' `.commonplace/library.md` read `Library root: <WORKSPACE>/kb` (written as `C:/Users/…` forward-slash form), as expected for an editable install. A released (non-editable) package was not tested; see checks not run.
- **Package data under `--target`.** The editable install also wrote the packaged library to `<TESTROOT>\site-packages\share\commonplace\` (`instructions`, `reference`, `tags`, `theory`, `types`) and the scaffold to `<TESTROOT>\site-packages\commonplace\_data\`, while `sys.prefix` is `C:\Program Files\Python314`. This is the layout that code change 1 of [proposed-install-procedure.md](./proposed-install-procedure.md) addresses: `sys.prefix\share\commonplace` will not find it. The `commonplace\_data` folder (no `__init__.py`) did not shadow the editable package: `commonplace` imported from `<WORKSPACE>\src` (R2).
- **Command installation diagnostics.** Each init run printed one diagnostic, bounded here: `These commands resolve outside uv's tool executable directory (<HOME>\.local\bin): commonplace-ack-review (<TESTROOT>\bin-s\commonplace-ack-review.CMD), … , commonplace-x-snapshot (<TESTROOT>\bin-s\commonplace-x-snapshot.CMD). Remove or reorder the shadowing PATH entry; do not use uv tool install --force as the default repair.` All 25 entry points are listed with their `bin-s\…CMD` path. Unlike the variant-U run, there was no "not on `PATH`" list, because all 25 commands now have a shim. This is open problem 4 and code change 2 of the proposal, reproduced for variant S over the full command set.
- No `.envrc` was generated in either project.

## Findings

1. **Variant S dispatch works by bare name with recorded provenance**: observed. The signed python.org interpreter, started by the `.cmd` shim, reached the `--target` folder's distribution and ran `commonplace-validate` and `commonplace-source` from `<TESTROOT>\bin-s`, ahead of the uv tool executables in `.local\bin`. Trace-confirmed in R3, R6 and R7. No generated `commonplace-*.exe` ran outside R0 step 2.
2. **The registrar's shadowing warning is a false positive whenever `-SitePackages` is given**: observed. It printed `WARNING: The shims will reach llm-commonplace 0.3.0 <TESTROOT>\site-packages, not the copy under <TESTROOT>\site-packages …`, naming the same folder on both sides. Cause, in [register-test-shims.ps1](./test-shims/register-test-shims.ps1): `$dist` is `"<version> <path>"` (from the `DIST` line), and the check is `$dist.StartsWith($site)`, which compares a string that starts with the version against the path, so it is always false. The `Distribution` line itself was correct. The check should compare only the path part of `$dist`. The script was not changed.
3. **The `--target` install writes launchers that cannot work**: observed and inferred. `uv pip install --target` wrote 29 unsigned executables to `<target>\bin`. The one run started the signed interpreter, which does not have the target on `sys.path`, and failed with exit 1 (inferred `ModuleNotFoundError`). Variant S needs these launchers deleted, or never placed on `PATH`, and on the afflicted machine they remain unsigned files that antivirus may act on.
4. **The released-package library root is still open**: observed layout. The library data sits at `<target>\share\commonplace`, not at `sys.prefix\share\commonplace`; only the editable install's checkout path hid this in R4/R5.
5. **This machine is uninformative for the antivirus claim**: observed. Every armed window (R0 step 2, R1, R3 ×3, R6, R7 ×2) had 0 detections, 0 Defender events and 0 Code Integrity events naming Commonplace, Python or uv.
6. **Results are interpreter-independent on this machine**: observed. R6/R7 per-target exits, counts and rule ids equal the variant-U run's, including the `fcntl` crash (open problem 10). Because the `.local\bin` tool and both test installs are editable installs of the same source, output equality does not discriminate between installs; provenance rests on resolution and the trace.

## Evidence fields

- Date, runtime, shell, Windows version: 2026-10-27 21:15–21:25 UTC+1; Claude Code agent, PowerShell tool; Windows PowerShell 5.1.26100.9711; Windows 11 Home 10.0.26300.
- uv and interpreter: uv 0.11.29; `C:\Program Files\Python314\python.exe`, CPython 3.14.7, Authenticode Valid, PSF signer.
- `uv tool list` and pre-registration `Get-Command`: `llm-commonplace v0.1.4`; validate and init resolve to `<HOME>\.local\bin\commonplace-*.exe`; source resolves to nothing.
- Test root layout: `<TESTROOT>` containing `.uv-cache` (44 MB), `site-packages` (22 packages; its `bin` deleted), `bin-s` (25 `.cmd`, 25 `sh`, dispatcher), `projects\one`, `projects\two` (each a `git init` repository initialised by `commonplace-init`, one fixture note in `kb/notes/`), `r4-init-one.txt`, `r6\`, `r7\` (per-target outputs), `trace-r3-*.txt`, `trace-r6.txt`, `trace-r7*.txt`.
- Exact top-level commands, exit statuses and bounded output: in the Results and target tables.
- Resolved source of every bare-name call: the `.cmd` shim in `<TESTROOT>\bin-s` in every call (first element of `Get-Command`; trace-confirmed).
- Generated `commonplace-*.exe` invoked: only in R0 step 2, once. Created by R1, deleted after R0 step 2.
- Antivirus: Windows Defender as in the identity table; R0 verdict uninformative; 0 records in every armed window.
- Project selection: observed (working-directory derived). Project isolation: not run.
- Result classes: R0 uninformative; R1 pass (antivirus uninformative); R2 pass; R3 pass (dispatch; antivirus uninformative); R4 pass; R5 partial; R6 uninformative; R7 uninformative.

## Checks not run

| Check | Unmet prerequisite |
|---|---|
| R8, every command starts (25 × `--help`, one per call) | Afflicted machine only (plan R8); on this machine it would be uninformative |
| R9, Avast in normal use over several days | Afflicted machine with Avast installed |
| Smart App Control and Avast acceptance of the signed interpreter and the `.cmd` shims | Smart App Control on and Avast present (afflicted machine); here Smart App Control is off and Avast is absent |
| R5 project isolation | A project-aware shim selecting the interpreter or package folder from the working directory, and two installations with distinct markers |
| Production `-c` shim form | The production shim implementation; the harness dispatches through a dispatcher `.py` plus `COMMONPLACE_TEST_SHIM`/`COMMONPLACE_TEST_SITE` and resolves entry points at run time, not a `-c` program fixed at registration |
| Released-package library root | A non-editable install from a built wheel, plus code change 1 of the proposal (`_library_root()` looking beside the package folder); this run used `-e <WORKSPACE>` |
| Child-process chain (cmd.exe → signed python.exe) | Process-creation auditing; observed only indirectly (shim body, trace) |
| Defender exclusions | Administrator rights |
| Desktop-runtime `PATH` inheritance | In-runtime probe; out of scope for R7 |
| Full text of the R0 step 2 traceback | Only two of six lines were retained, and the plan allows one launch; the error is inferred from the embedded script and a direct-import control |

## State left behind

- `<TESTROOT>` left in place with the layout above. The trace files contain the full process `PATH` as written by `Trace-Command`; they are local only and are not quoted in this report.
- `<TESTROOT>\site-packages\bin` deleted (all 29 generated executables).
- No user `PATH`, profile, Defender, `uv tool` or system-Python change. `INSTALL.md` unchanged. The only change in the checkout is this file; nothing committed. `git status` otherwise shows only the pre-existing untracked `kb/reports/connect/`.

## Disclosure review

- Final payload reviewed: yes
- Local identifiers normalized: yes (`<WORKSPACE>`, `<HOME>`, `<TESTROOT>`; `C:\Program Files\Python314` kept as a public system path)
- Secrets, credentials, and private keys: none observed
- Full environment, PATH, and raw configuration output: absent
- Optional automated scan: not run
- Withheld or residual sensitive-looking material: none
