# Shim delivery round 2, variant S: afflicted machine (run s2)

- Round and procedure: round 2, [shim-delivery-test-plan.md](./shim-delivery-test-plan.md), tests R0–R8; R9 (several days of normal use) started at the end of this run and is open. Round 1's "Result classes", "Conflicting global installations" and "Antivirus observation" sections ([shim-test-plan-round-1.md](./shim-test-plan-round-1.md)) applied, with the Avast records added.
- Variant: **S**, shims that start the signed python.org interpreter (`C:\Program Files\Python314\python.exe`) and add a `uv pip install --target` folder with `site.addsitedir`.
- Checkout: `<WORKSPACE>`, `llm-commonplace` 0.3.1, HEAD `9c37c5617`; one pre-existing untracked `.codex/`, not created by this run.
- Machine: the afflicted machine (Smart App Control on; Avast, McAfee and Defender registered). R0 discriminated, so the antivirus results below are **informative**.
- Companion run: [results-2026-10-28-afflicted-variant-u.md](./results-2026-10-28-afflicted-variant-u.md), variant U on this machine immediately afterwards.

## Identity

| Field | Value | Basis |
|---|---|---|
| Date/time | 2026-10-28, 08:35–08:45 local (UTC+1) | observed |
| Runtime and surface | Claude Code agent (claude-opus-5-5) in the Claude desktop app's Code tab, PowerShell tool | observed |
| OS | Windows 11 Home 10.0.26300 | observed |
| Shell | Windows PowerShell 5.1.26100.9711; every tool call a fresh process | observed |
| Test root | `<TESTROOT>` = `<HOME>\cp-shim-2026-10-28\s`, outside the checkout and outside `%APPDATA%`; new for this run | observed |
| uv | 0.13.5, from the WinGet package directory; `UV_CACHE_DIR` = `<TESTROOT>\.uv-cache` in every uv call; user `UV_SYSTEM_CERTS=1` | observed |
| Interpreter | CPython 3.14.7, `sys.prefix` `C:\Program Files\Python314`; Authenticode `Valid`, signer Python Software Foundation; no `commonplace` in its own site-packages | observed |
| Smart App Control | `VerifiedAndReputablePolicyState` 1 (on) | observed |
| Antivirus | `root\SecurityCenter2`: Windows Defender (productState 393472), Avast Antivirus (266240), McAfee (278528). Defender AM 4.18.26100.4, engine 1.1.26100.4, signatures 1.463.1.0, real-time protection off (Avast active). Avast version: unknown. Exclusions: unknown | observed |
| User `Path` | backed up to `<HOME>\cp-shim-2026-10-28\user-path-backup.txt` before the run; unchanged at the end | observed |

## Conflicting installation record

`uv tool list`: `trafilatura v2.3.1` only, plus `warning: Ignoring malformed tool llm-commonplace` (the remains of the 2026-10-27 failed install; open problem 3). `Get-Command commonplace-validate, commonplace-init, commonplace-source -All`: no match. Nothing to shadow; the bin directory was still prepended in every call and the resolved source recorded before every bare-name call.

## Antivirus observation method

`avcheck.ps1` (in the test root's `tools\`; see State left behind), run at the end of every test call over that call's window, recorded:

- Code Integrity events 3033/3077 in the window, all and those naming Commonplace, Python, uv or the test root. McAfee's `mc-sec-plugin-x64.dll` loads produce unrelated 3033 events throughout (138 of the 140 events between 08:36 and 08:41); they are excluded by the name filter, and a grouped check confirmed that nothing else was hidden.
- Defender detections (`Get-MpThreatDetection`) and events 1116/1117/1121/1122.
- Avast: entry count of `chest\index.xml` (quarantine; 5 at baseline, the newest from 2026-10-26) and new entries in `log\autosandbox.log` with their result.

Baseline before the run: 0 Code Integrity events naming Commonplace, Python or uv in the log's retained history; Defender 1 old detection (2026-10-14, unrelated); Avast chest 5; Auto-Sandbox log last written 2026-10-27 15:13.

Avast's Auto-Sandbox log shows an **exception list learned per file**: on 2026-10-26/27 launchers were first `Sandboxing (no custody)` and later `Not sandboxing (because the file is in the exception list)`. New files in a new test root therefore start without that history; variant U's run shows the same transition within one minute.

## R0 — instrument check

Step 2, after R1: `Start-Process <TESTROOT>\site-packages\bin\commonplace-validate.exe --help` (the launcher is `NotSigned`). PowerShell refused it at process creation: `Zasady kontroli aplikacji zablokowały ten plik` ("an application control policy blocked this file"). Code Integrity logged 3077 and 3033 at 08:37:10 for that file. No Avast or Defender record. The launcher was still present afterwards.

**Verdict: this machine discriminates.** Smart App Control blocks the uv launcher that variant S's install writes.

## Results

| Test | Exact top-level command(s) | Exit | Resolved source | Generated exe invoked? | Antivirus records in window | Result |
|---|---|---|---|---|---|---|
| R0 step 2 | `Start-Process <TESTROOT>\site-packages\bin\commonplace-validate.exe --help` | refused | n/a | attempted once; blocked | CI 3077 + 3033 for that file | **pass** (instrument): block observed |
| R1 install | `uv pip install --python 'C:\Program Files\Python314\python.exe' --target <TESTROOT>\site-packages -e <WORKSPACE>` | 0 | n/a | no; uv wrote 29 executables to `site-packages\bin` (25 `commonplace-*.exe`); deleted after R0 | 0 / 0 / Avast none | **pass**: `Resolved 22 packages`, `Installed 22 packages`, 13 s |
| R2 direct dispatch | `& 'C:\Program Files\Python314\python.exe' -c "import site, sys; site.addsitedir(r'<TESTROOT>\site-packages'); …validate_notes import main…"` with `--help` | 0 | n/a | no | 0 / 0 / none | **pass**: 27 lines, `usage: commonplace-validate …`; `commonplace` from `<WORKSPACE>\src`; distribution 0.3.1 at `<TESTROOT>\site-packages` |
| R3 registration | `powershell -NoProfile -File …\register-test-shims.ps1 -PythonPath 'C:\Program Files\Python314\python.exe' -SitePackages <TESTROOT>\site-packages -BinDirectory <TESTROOT>\bin-s` | 0 | n/a | no; 25 `.cmd`, 25 `sh`, 0 `.exe` | 0 / 0 / none | Distribution `0.3.1 <TESTROOT>\site-packages`, Count 25; no shadowing warning (fixed in `70239f8f0`) |
| R3 shim dispatch | `commonplace-validate --help`; separate call `commonplace-source --help` | 0; 0 | `bin-s\commonplace-validate.cmd`; `bin-s\commonplace-source.cmd` | no | 0 / 0 / none each | **pass** |
| R4 initialised project | in `<TESTROOT>\projects\one`, after `git init`: `commonplace-init --name one`; `commonplace-init --check`; `commonplace-validate landings` | 0; 0; 0 | `bin-s\…cmd` | no | 0 / 0 / none (R4+R5 window) | **pass**: 26 of 26 `ok:`; landings `VALIDATION SUCCESS`; library root `<WORKSPACE>/kb` |
| R5 second project | same in `projects\two` | 0; 0; 0 | `bin-s\…cmd` | no | as R4 | **partial**: same installation for both projects |
| R6 sweep | from `<WORKSPACE>`, one `commonplace-validate <target>` per statement, 13 targets | 13 × 0 | 13 of 13 `bin-s\commonplace-validate.cmd` | no | 0 named (81 McAfee) / 0 / none | **pass**: 75 s |
| R7 fresh process | new call (PID 34168): before prepend no `commonplace-*` resolves; after: `--help` for validate and source, then the R6 sweep | 0, 0; 13 × 0 | 15 of 15 `bin-s\…cmd` | no | 0 / 0 / none | **pass**: all 13 outputs byte-identical to R6 |
| R8 every command | 25 tool calls, one `<name> --help` each, bare name through `cmd /c`, 30 s limit | 23 × 0; 2 × 1 | 25 of 25 `bin-s\<name>.cmd` | no | 0 / 0 / none in all 25 windows | **pass** (start): every command started in 0.2–2.9 s; the two exit-1 commands are open problem 10 |

R6/R7 targets: the `kb/*/COLLECTION.md` directories of the checkout except `agentic-system-analyses` (Linux only by operator decision): `agent-memory-systems agentic-systems articles instructions reference reports sources tags theory types work`, plus `landings` and `redirects`. First lines: `VALIDATION SUCCESS` for agentic-systems, articles, instructions, theory, landings, redirects; `VALIDATION WARNING` for the rest. All exit 0, unlike the reference run of 2026-10-27, where `reports` and `sources` exited 1 at an older HEAD. Variant U's outputs were byte-identical.

R8 exit 1: `commonplace-analysis` and `commonplace-task`, both `ModuleNotFoundError: No module named 'fcntl'` (open problem 10). The longest start was `commonplace-x-snapshot` at 2.9 s.

### Stdlib extension probe (added; not in the plan)

Variant U's R8 showed Smart App Control blocking a stdlib `.pyd` (see its report), so one probe ran under this interpreter for comparison: `python.exe -I <HOME>\cp-shim-2026-10-28\tools\pyd-probe.py`, which imports 21 stdlib C extensions in turn. All 21 loaded from `C:\Program Files\Python314\DLLs` (including `_decimal`, `_asyncio`, `pyexpat`, `_elementtree` and `_overlapped`); 0 Code Integrity, Defender or Avast records.

### Installation behaviour (not shim results)

- Init in both projects printed the open-problem-4 diagnostic: `These commands resolve outside uv's tool executable directory (<HOME>\.local\bin): commonplace-ack-review (<TESTROOT>\bin-s\…)`, listing all 25.
- Library root `<WORKSPACE>/kb` comes from the editable install. A released package was not tested; the package data lands in `<TESTROOT>\site-packages\share\commonplace`, not `sys.prefix\share\commonplace` (code change 1 of the proposal).

## Findings

1. **Variant S passes R0–R8 on the afflicted machine.** Across about 45 launches of the signed interpreter, including all 25 commands one by one, the run logged no Code Integrity event, no Defender record and no Avast quarantine or sandbox entry. The same machine blocked the uv launcher of the same install (R0).
2. **The signed interpreter's own extensions all load.** This rules out, for this build, the partial failure that variant U shows (a stdlib `.pyd` refused at load time).
3. **`uv pip install --target` writes 29 unsigned launchers into `<target>\bin`**, and Smart App Control blocks them. A production procedure has to delete them or never put that folder on `PATH`. They are also files Avast may act on during R9.
4. **The earlier hang did not recur.** No launch came near the 30 s limit.

## Checks not run

| Check | Unmet prerequisite |
|---|---|
| R9, Avast in normal use over several days | time; started, see below |
| R5 project isolation | a project-aware shim and two installations |
| Production `-c` shim form | the production shim; the harness uses a dispatcher `.py` and environment variables |
| Released-package library root | a non-editable install and code change 1 |
| Git Bash `sh` shims | not exercised in this run |
| Fresh desktop-app session inheriting a `PATH` entry | the shims were never on the user `Path` |
| Defender exclusions; Avast version and exclusions | administrator rights / Avast UI |

## State left behind

- `<HOME>\cp-shim-2026-10-28\` left in place (110 MB for both variants): `s\` (site-packages without `bin`, `bin-s`, `projects\one`, `projects\two`, `r6`, `r7`), `tools\` (`avcheck.ps1`, `r8.ps1`, `pyd-probe.py`) and the user-`Path` backup. Not on `PATH`.
- No change to the user `Path` (verified against the backup), to the uv tool directory, to Avast, Defender or Smart App Control, or to `C:\Program Files\Python314`. `INSTALL.md` unchanged.

## R9 (open)

To continue R9: keep `<TESTROOT>` registered (prepend `bin-s` per session), use it for ordinary validation, and on each day of use rerun `avcheck.ps1 -RunStart <last check>`. Record any quarantine, sandbox or Code Integrity entry naming `cp-shim-2026-10-28`, `Python314` or `commonplace`, and whether the commands still start.

## Disclosure review

- Final payload reviewed: yes
- Local identifiers normalized: yes (`<WORKSPACE>`, `<HOME>`, `<TESTROOT>`; the machine name omitted; `C:\Program Files\Python314` kept as a public system path)
- Secrets, credentials, private keys: none observed
- Full environment, PATH and raw configuration output: absent
- Withheld or residual sensitive-looking material: none
