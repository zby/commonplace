# Windows shim validation: Claude Code / Windows 11 Home / Windows PowerShell 5.1 (run w3)

- Round and procedure: Windows shim validation test plan ([windows-shim-test-plan.md](../windows-shim-test-plan.md)), revised 2026-10-27, run on the rebased 0.3.0 checkout (HEAD `756ccca96`, "Match the shim test sweep to the current collections").
- Prior related reports: [2026-10-27-registered-shim-validation.md](./2026-10-27-registered-shim-validation.md) and its [correction note](./2026-10-27-registered-shim-validation-correction.md). This run addresses the correction's gaps: bare-name calls only, resolved source recorded in every bare-name call, test root outside the checkout, antivirus observation from Defender's own records, and a W0 negative control.
- Machine: the reference machine of the plan (Smart App Control off, Defender only). It is not the originating machine of W0a.

## Identity

| Field | Value | Basis |
|---|---|---|
| Date/time | 2026-10-27, 20:51–21:05 local (UTC+1) | observed |
| Runtime and surface | Claude Code agent (subagent), PowerShell tool | observed |
| Runtime version | unknown | unknown |
| OS and version | Windows 11 Home, `Microsoft Windows NT 10.0.26300.0` | observed |
| Shell | Windows PowerShell 5.1.26100.9711 (`powershell.exe`); `pwsh` not installed | observed |
| Tool execution interface | every PowerShell tool call is a fresh process; no shell state or `PATH` change carries over | observed (W7) |
| Workspace/current directory | `<WORKSPACE>` (Git checkout, `llm-commonplace` 0.3.0); one pre-existing untracked directory `kb/reports/connect/`, not created by this run | observed |
| Test root | `<TESTROOT>` = `<HOME>\commonplace\tmp\windows-shim-test-w3`, outside the checkout; did not exist before the run; left in place | observed |
| uv | `uv 0.11.29 (901092ee1 2026-07-15 x86_64-pc-windows-msvc)`, resolved at `<HOME>\.local\bin\uv.exe` | observed |
| `UV_CACHE_DIR` | `<TESTROOT>\.uv-cache`, set in every call that ran uv | observed |
| Managed Python | CPython 3.14.6; venv `home = <HOME>\AppData\Roaming\uv\python\cpython-3.14-windows-x86_64-none` | observed |
| Test venv interpreter | `<TESTROOT>\.venv\Scripts\python.exe`; `sys.version` 3.14.6; `commonplace` imported from `<WORKSPACE>\src\commonplace\__init__.py` (editable) | observed (W2) |
| Antivirus | Windows Defender only in `root\SecurityCenter2` (`productState` 0x61100); AMProductVersion 4.18.26090.9, AMEngineVersion 1.1.26090.9, AntivirusSignatureVersion 1.461.230.0; real-time and behavior monitoring on; tamper protected | observed |
| Defender cloud/ASR | MAPSReporting 2, CloudBlockLevel 0, SubmitSamplesConsent 1, PUAProtection 2, no ASR rule ids configured; exclusions: unknown (admin required) | observed |
| Smart App Control | `VerifiedAndReputablePolicyState` 0 (off) | observed |

## Conflicting installation record

Recorded before shim registration, in a process without the test bin directory:

| Observation | Result |
|---|---|
| `uv tool list` | `llm-commonplace v0.1.4` with `commonplace-*` entry points (first lines only retained) |
| `Get-Command commonplace-validate, commonplace-init -All` | `commonplace-validate.exe` → `<HOME>\.local\bin\commonplace-validate.exe`; `commonplace-init.exe` → `<HOME>\.local\bin\commonplace-init.exe` |
| Tool environment (read only, not executed) | `<HOME>\AppData\Roaming\uv\tools\llm-commonplace`; its `direct_url.json` and `.pth` show an **editable** install of `<WORKSPACE>` (`src`), dist-info 0.1.4 |

Option chosen: "keep it and prepend" (plan, "Conflicting global installations"). The test bin directory was prepended to `$env:PATH` inside every call that used a bare name, and the resolved source was recorded in the same call before the invocation. `uv tool uninstall` was not run; the user `PATH` was not modified. The `.local\bin` executables were used only for `Get-Command` resolution.

## W0 — antivirus observability

### W0a — original detection record and this machine's configuration

Cited, not reconstructed: [results-windows-install-030.md](../../framework-delivery/results-windows-install-030.md), sections "Smart App Control hang" and "Shim workaround test and Avast detection", findings 4, 10, 11 and 12; [windows-install/README.md](../../windows-install/README.md), "Constraints" (testing rules) and "Open problems" 1–5; [results-2026-10-27-signed-python.md](../../windows-install/results-2026-10-27-signed-python.md) (present in this checkout, not re-read for this run). On the originating machine, Smart App Control was on (Code Integrity 3033/3077, policy `{0283ac0f-…}`) and Avast, McAfee and Defender were registered; Avast's Behavior Shield and Auto-Sandbox acted while Defender logged nothing.

This machine:

| Check | Result | Matches originating configuration? |
|---|---|---|
| Smart App Control | off (`VerifiedAndReputablePolicyState` 0) | no |
| `root\SecurityCenter2` products | Windows Defender only | no (no Avast, no McAfee) |
| Code Integrity 3033/3077, total | 335 | — |
| Code Integrity 3033/3077 naming Commonplace, Python or uv (message filter) | 0 | no |
| `Get-MpThreatDetection` / `Get-MpThreat` | 0 / 0 records | — |

`root\SecurityCenter2` was read with a read-only `Get-CimInstance` query; no process was started through WMI and `-EncodedCommand` was not used anywhere in this run.

### W0b — on-demand scan and signatures

| Executable | `MpCmdRun -Scan -ScanType 3 -File` | Authenticode |
|---|---|---|
| `<TESTROOT>\.venv\Scripts\commonplace-validate.exe` (generated) | exit 0, "found no threats" | NotSigned |
| `<TESTROOT>\.venv\Scripts\python.exe` (venv launcher, 45 568 bytes) | exit 0, "found no threats" | NotSigned |
| `<HOME>\.local\bin\uv.exe` | not scanned | NotSigned |
| managed `python.exe` 3.14.6 under the venv `home` | not scanned | NotSigned |

### W0c — execution control through the generated executable

Run once, from `<WORKSPACE>`, observation armed (`$RunStart` 20:53:05):

```powershell
& $TestRoot\.venv\Scripts\commonplace-validate.exe theory
```

Exit 0, 11.5 s, 50 output lines (last lines: orphan-check detail lines and `Details: commonplace-validate --full theory`). Defender detections since `$RunStart`: 0; Defender events 1116/1117/1121/1122: 0; Code Integrity 3033/3077 naming Commonplace/Python/uv: 0. The executable was still present afterwards. The plan's W0c snippet names target `notes`; this checkout has no `kb/notes` collection, so `theory` was used as instructed.

### W0 verdict

No detection in W0b or W0c. **This machine cannot distinguish the shim from the executable it replaces.** Every antivirus result below is **uninformative**. The design's antivirus claim remains **unverified** (plan, "Antivirus tests on an informative environment").

## Shim registration

```powershell
powershell -NoProfile -File <WORKSPACE>\kb\work\execution-channel-compatibility\test-shims\register-test-shims.ps1 -PythonPath <TESTROOT>\.venv\Scripts\python.exe -BinDirectory <TESTROOT>\bin
```

Exit 0. Printed `Python = <TESTROOT>\.venv\Scripts\python.exe`, `BinDirectory = <TESTROOT>\bin`. Files written: `commonplace-init.cmd`, `commonplace-validate.cmd`, `commonplace-test-dispatch.py`. The `.cmd` body sets `COMMONPLACE_TEST_SHIM` and calls the hardcoded venv `python.exe` with the dispatcher; it names no `commonplace-*.exe`.

## Results

Order deviation: W1 ran before W0b/W0c, because W0b and W0c need the test venv's executables. All bare-name calls ran after prepending `<TESTROOT>\bin` in the same call. "Resolved source" is from `(Get-Command commonplace-validate -CommandType Application).Source` (or `commonplace-init`) recorded in the same call. Under PowerShell 5.1 this expression returned **both** matches in `PATH` order (`<TESTROOT>\bin\commonplace-*.cmd | <HOME>\.local\bin\commonplace-*.exe`); the first is the one executed, confirmed in W3, W6 and W7 with `Trace-Command -Name CommandDiscovery`, whose "Command Found" records name only the shim.

| Test | Exact top-level command(s) as run | Exit status | Resolved source (bare name) | Generated exe invoked? | Antivirus records in window | Result class and reason |
|---|---|---|---|---|---|---|
| W1 isolated installation | `uv venv --python 3.14 "$TestRoot\.venv"`; `uv pip install --python "$TestRoot\.venv\Scripts\python.exe" -e <WORKSPACE>` | 0; 0 | n/a | No. 25 `commonplace-*.exe` created in `.venv\Scripts` by the install, none executed in W1 | Defender detections 0, events 0 (both calls) | **pass** (installation: CPython 3.14.6 selected; 22 packages resolved, `llm-commonplace==0.3.0` built from the checkout, 14 s); antivirus **uninformative** per W0 |
| W2 module dispatch | `& $TestRoot\.venv\Scripts\python.exe -c "import sys; sys.argv=['commonplace-validate','--help']; from commonplace.cli.validate_notes import main; raise SystemExit(main())"` | 0 | n/a (explicit path) | No | not armed (no executable under test beyond python.exe) | **pass**: help printed (27 lines, `usage: commonplace-validate [-h] [--full \| --json] …`); module from `<WORKSPACE>\src` |
| W3 shim dispatch | `commonplace-validate --help` (bare name, from `<WORKSPACE>`) | 0 | `<TESTROOT>\bin\commonplace-validate.cmd` (first of two; trace confirms) | No | detections 0; Defender 1116/1117/1121/1122: 0; CI naming cp/python/uv: 0 | Dispatch **pass**: bare-name resolution to the shim recorded and traced; output byte-identical to W2. Antivirus **uninformative**. Caveat: identical output does not by itself discriminate from `.local\bin`, whose tool is an editable install of the same source |
| W4 initialized project | in `<TESTROOT>\projects\project-one` after `git init`: `commonplace-init --name project-one` (and a second identical run to capture diagnostics); `commonplace-init --check`; `commonplace-validate kb/notes/shim-fixture.md` | 0; 0; 0; 0 | `<TESTROOT>\bin\commonplace-init.cmd`, `<TESTROOT>\bin\commonplace-validate.cmd` | No | not armed | **pass**: project root `<TESTROOT>\projects\project-one`; `--check` 26 of 26 `ok`; fixture note validated (`VALIDATION SUCCESS`, 0 failures, 0 warnings). Package provenance: venv `python.exe` → `<WORKSPACE>\src` (editable); `.commonplace/library.md` names library root `<WORKSPACE>/kb` |
| W5 project selection / isolation | in `<TESTROOT>\projects\project-two` after `git init`: `commonplace-init --name project-two`; `commonplace-validate kb/notes/shim-fixture-two.md` from project-two, then the same from project-one | 0; 0; 1 (`No matching note found`) | shim in every call | No | not armed | **partial**: project selection shown (the fixture present only in project-two validates there and is not found from project-one, no user `PATH` change). Project isolation **not run**: the harness hardcodes one interpreter; needs a project-aware shim and two installations with distinct markers |
| W6 scripted operation | `foreach ($c in $targets) { commonplace-validate $c }` from `<WORKSPACE>`, inside `Trace-Command -Name CommandDiscovery`; 14 targets (list below) | 11 × 0; 3 × 1 (see below) | 14 of 14 resolutions to `<TESTROOT>\bin\commonplace-validate.cmd` (trace) | No | `$RunStart` 20:57:26; detections 0; Defender 1116/1117/1121/1122: 0; CI naming cp/python/uv: 0 | **uninformative** (antivirus, per W0). Dispatch mechanics observed with provenance, 170 s total. The three exit-1 targets are product results, not shim results |
| W7 fresh-process repeat | separate PowerShell tool call (= fresh process, PID 20636): prepend `<TESTROOT>\bin`; `commonplace-validate --help`; same 14-target sweep, inside `Trace-Command` | `--help` 0; sweep identical to W6 (11 × 0, 3 × 1) | before prepend: bin not on `PATH`, resolves to `<HOME>\.local\bin\commonplace-validate.exe` (not invoked); after prepend: shim; trace 15 of 15 to the shim | No | `$RunStart` 21:01:49; detections 0; Defender 1116/1117/1121/1122: 0; CI naming cp/python/uv: 0 | **uninformative** (antivirus, per W0). Fresh-process resolution after re-prepend observed; same interpreter reached (identical help and sweep results). Does not test desktop-runtime `PATH` inheritance: that is answered by in-runtime probes (native Windows probe of 2026-10-27, [2026-10-27-codex-app-windows-powershell-a1.md](./2026-10-27-codex-app-windows-powershell-a1.md)) |

### W6/W7 target list and per-target results

Targets: the twelve top-level `kb/*/COLLECTION.md` directories plus the `landings` and `redirects` targets named in `--help` (W2). Nested `COLLECTION.md` files (`kb/work/dialectical-sample`, a retained trial bundle under `kb/reports/retained/`) were excluded as not top-level collections. `types` is both a collection directory and a `--help` keyword; it was run once.

| Target | W6 exit / first line / diagnostics | W7 exit |
|---|---|---|
| agent-memory-systems | 0 / WARNING / 0 failures, 2 warnings | 0 |
| agentic-system-analyses | 1 / Python traceback: `ModuleNotFoundError: No module named 'fcntl'` (from `src\commonplace\lib\agentic_analysis\effects.py` line 9 via `sources.py`) | 1 |
| agentic-systems | 0 / SUCCESS | 0 |
| articles | 0 / SUCCESS | 0 |
| instructions | 0 / SUCCESS | 0 |
| reference | 0 / WARNING / 2 warnings | 0 |
| reports | 1 / FAILED / 10 failures, 1 warning (10 × `validation.base.frontmatter-type`, 1 × `validation.base.link-health`) | 1 |
| sources | 1 / FAILED / 2 failures, 22 warnings (rule ids include `validation.base.source-quotes`, `validation.base.link-health`, `validation.schema.frontmatter-genre`) | 1 |
| tags | 0 / WARNING / 1 warning | 0 |
| theory | 0 / SUCCESS (50 lines, 450 files; same exit and line count as W0c's generated-exe run) | 0 |
| types | 0 / WARNING / 1 warning | 0 |
| work | 0 / WARNING / 21 warnings | 0 |
| landings | 0 / SUCCESS | 0 |
| redirects | 0 / SUCCESS | 0 |

The `fcntl` crash is the known open problem 10 in [windows-install/README.md](../../windows-install/README.md) (Unix-only file locking in `agentic_analysis/effects.py`); it reproduces through the shim. The `reports` and `sources` failures are validator content findings on this checkout; `kb/reports/` contains the pre-existing untracked `kb/reports/connect/` directory, and whether the failures are Windows-specific was not determined.

### Installation behavior under review (W4/W5, not shim results)

- No `.envrc` was generated in either project, and the 0.3.0 init output contained no Windows `.envrc` note; the plan's expectation of one comes from an older model.
- Each init run printed "Command installation diagnostics": four commands of the installed package (`commonplace-analysis`, `commonplace-source`, `commonplace-status`, `commonplace-task`) are not on `PATH` (the 0.1.4 tool's `.local\bin` lacks them; the venv `Scripts` is deliberately not on `PATH`), and `commonplace-init` and `commonplace-validate` "resolve outside uv's tool executable directory (`<HOME>\.local\bin`)" to `<TESTROOT>\bin\commonplace-*.CMD`, with advice to remove the shadowing entry. This is open problem 4 (finding 12) reproduced with the test harness. It also corroborates, from inside Python, that the process `PATH` resolves both names to the shims.

## Findings

1. **Dispatch through the registered shim works by bare name with recorded provenance** — observed. W3, W4, W5, W6 and W7 all resolved to `<TESTROOT>\bin\*.cmd` ahead of the uv tool executables in `.local\bin`; no generated `commonplace-*.exe` was invoked outside W0c.
2. **This machine is uninformative for the antivirus claim** — observed. Smart App Control off, Defender only, no detection from static scan or from executing the generated launcher (W0c). Antivirus acceptance of the shim path remains unverified.
3. **The mandated provenance expression is ambiguous under PowerShell 5.1** — observed. `(Get-Command <name> -CommandType Application).Source` returns every match in `PATH` order, not just the executed one. The first element is the executed file (confirmed with `Trace-Command -Name CommandDiscovery`). The plan could specify `Select-Object -First 1` or the trace.
4. **Output equality cannot discriminate shim from uv tool executable on this machine** — observed. The user-level "v0.1.4" uv tool is an editable install of this checkout, so both paths would run the same source. Provenance rests on resolution and the trace, not on module behavior.
5. **One collection target crashes on Windows through the shim** (`fcntl`) — observed; known open problem 10.

## Evidence fields

- Date, runtime, shell, Windows version: 2026-10-27 20:51–21:05 UTC+1; Claude Code agent, PowerShell tool; Windows PowerShell 5.1.26100.9711; Windows 11 Home 10.0.26300.
- uv version and managed Python path: uv 0.11.29; CPython 3.14.6 at `<HOME>\AppData\Roaming\uv\python\cpython-3.14-windows-x86_64-none`.
- `uv tool list` and pre-registration `Get-Command`: `llm-commonplace v0.1.4` (editable from `<WORKSPACE>`); both names resolve to `<HOME>\.local\bin\commonplace-*.exe`.
- Test root and layout: `<TESTROOT>` outside the checkout, containing `.uv-cache`, `.venv`, `bin` (two `.cmd` shims and the dispatcher), `projects\project-one`, `projects\project-two` (each a `git init` repository initialized by `commonplace-init`, with one fixture note in `kb/notes/`).
- Exact top-level commands: in the Results table; every shim call spelled by bare name without `.cmd`.
- Exit status and bounded output: in the Results and target tables.
- Resolved source of every bare-name call: `<TESTROOT>\bin\commonplace-validate.cmd` or `<TESTROOT>\bin\commonplace-init.cmd` in every call (first element; second element `<HOME>\.local\bin\…exe` listed but not executed).
- Generated `commonplace-*.exe` invoked: only in W0c (`<TESTROOT>\.venv\Scripts\commonplace-validate.exe theory`, once). Created but not executed by W1.
- Antivirus: Windows Defender, AMProductVersion 4.18.26090.9, engine 1.1.26090.9, signatures 1.461.230.0, MAPSReporting 2, CloudBlockLevel 0, no ASR rules, exclusions unknown; W0 verdict uninformative; signatures: generated `commonplace-validate.exe` NotSigned, venv `python.exe` NotSigned, managed `python.exe` NotSigned, `uv.exe` NotSigned (uv not in the executed shim path); detection records: 0 in every armed window (W1 ×2, W0c, W3, W6, W7), Code Integrity 0 naming Commonplace/Python/uv.
- Project selection: observed (working-directory derived). Project isolation: not run.
- Checks not run: below.
- Result classes: W0 uninformative; W1 pass (antivirus uninformative); W2 pass; W3 pass (dispatch; antivirus uninformative); W4 pass; W5 partial; W6 uninformative; W7 uninformative.

## Checks not run

| Check | Unmet prerequisite |
|---|---|
| Antivirus claim (W0c, W3, W6, W7 on an informative environment) | Smart App Control on and/or Avast present (originating machine), a never-disabled Smart App Control install, or an admin VM with the ASR prevalence rule in block mode |
| W5 project isolation | A project-aware shim selecting the interpreter from the working directory, and two installations with distinct package or runtime markers |
| Production shim path (`uv run --no-sync python -m …`, `uv.exe` in the executed path) | Production shim implementation; the harness calls `python.exe` directly |
| Signed python.org interpreter path (`origin/main` proposal) | python.org interpreter and `uv pip install --target` layout; this harness uses the unsigned uv-managed CPython |
| Other package entry points | The dispatcher covers only `commonplace-init` and `commonplace-validate` |
| Child-process chain of the shim (cmd.exe → venv launcher → managed python.exe) | Process-creation auditing; observed only indirectly (shim body, `Trace-Command`), not by process records |
| Defender exclusions | Administrator rights |
| Desktop-runtime `PATH` inheritance | In-runtime probe; out of scope for W7 |
| Avast quarantine index, Auto-Sandbox log | Avast not installed on this machine |

## Disclosure review

- Final payload reviewed: yes
- Local identifiers normalized: yes (`<WORKSPACE>`, `<HOME>`, `<TESTROOT>`)
- Secrets, credentials, and private keys: none observed
- Full environment, PATH, and raw configuration output: absent
- Optional automated scan: not run
- Withheld or residual sensitive-looking material: none
