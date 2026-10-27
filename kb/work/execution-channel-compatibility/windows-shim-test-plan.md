# Windows shim validation test plan

## Purpose

Validate the established Windows command design: Commonplace-owned shims invoke uv-managed Python and the Commonplace module, without invoking uv-generated `commonplace-*.exe` entry points.

This plan validates a candidate design. It is not a test of the installation procedure in `INSTALL.md`: that procedure is tested by following it unchanged in a clean environment and a freshly launched agent runtime, and recording the result as a probe report.

## The claim under test

The design exists because the uv-generated `commonplace-*.exe` launchers were blocked on a Windows 11 Home machine on 2026-10-26. The record is on `origin/main`, which this branch's base (`2430377f8`, 2026-08-08) predates: `kb/work/framework-delivery/results-windows-install-030.md` (the run, findings 4, 10 and 11) and `kb/work/windows-install/README.md` (open problems 1 to 3, testing rules). What blocked:

- **Smart App Control** (`VerifiedAndReputablePolicyState` 1; Code Integrity events 3033 and 3077, policy `{0283ac0f-fff1-49ae-ada1-8a933130cad6}`) refused the unsigned, per-install uv launchers in `.local\bin`. Verdicts varied between runs, and one launch hung until the computer was restarted. It also blocked one uv-managed CPython build (3.13.17, `0xc0e90002`) while 3.14.9 ran.
- **Avast** Behavior Shield deleted the tool environment's `Scripts\python.exe` (detection `IDP.HELU.PSE95%s_cmd`, recorded against `powershell.exe` started through WMI with `-EncodedCommand`), and Avast Auto-Sandbox repeatedly sandboxed the launchers. McAfee was also registered. Windows Defender logged nothing.

The claim is therefore: *the shim path executes under Smart App Control with Avast present, where the generated launchers were blocked*. Two consequences:

1. A machine without Smart App Control on, or without that antivirus, cannot validate the claim. Dispatch tests on such a machine show that the shim works mechanically; they say nothing about acceptance. The antivirus result of every test on that machine is **uninformative**, not pass. The reference machine for this plan has Smart App Control off, Defender only, and no Code Integrity event naming Commonplace, Python or uv.
2. The shim path has its own executable components. The harness here starts the uv-managed `python.exe`, which is `NotSigned` and of the same build family that Smart App Control blocked once. The `origin/main` proposal (`kb/work/windows-install/proposed-install-procedure.md`, operator direction of 2026-10-27) instead starts a python.org interpreter signed by the Python Software Foundation and installs the package with `uv pip install --target`, so no per-install executable is written or run. A harness built on the uv-managed interpreter tests the fallback, not that proposal.

## Result classes

Every test reports one of:

- **pass** — the test's claim was observed, with the provenance evidence this plan requires;
- **partial** — the command succeeded but the harness cannot establish the full claim (state which part);
- **blocked** — a prerequisite was unavailable; not a verdict on the design;
- **uninformative** — the test ran but its instrument cannot detect the failure it exists to detect (an antivirus test whose negative control produced no detection).

A test whose provenance check was not recorded is **partial**, not pass. An exit status of 0 is never sufficient on its own.

## Preconditions

- Windows PowerShell execution. Windows PowerShell 5.1 (`powershell.exe`) is the baseline; `pwsh` (PowerShell 7) is not installed on the reference machine, so every scripted step must run under `powershell -NoProfile -File`.
- `uv` available by bare name.
- Network access to PyPI, or a populated uv cache.
- A disposable test directory outside the source checkout. If the runner cannot write outside the checkout, use a gitignored directory inside it and record the deviation.
- Antivirus real-time protection enabled, and an observation method for it (see **Antivirus observation**).
- The shim implementation or temporary equivalent available for the run.
- The original antivirus detection record (see **W0**).

Use a project-local cache when the runner cannot access the default user cache:

```powershell
$env:UV_CACHE_DIR = Join-Path $TestRoot '.uv-cache'
```

### Conflicting global installations

Before any bare-name test, record what the bare names resolve to in the test process:

```powershell
uv tool list
Get-Command commonplace-validate, commonplace-init -All -ErrorAction SilentlyContinue |
  Select-Object Name, CommandType, Source
```

On the reference machine a user-level `uv tool install` of `llm-commonplace` puts uv-generated `commonplace-*.exe` files in `<HOME>\.local\bin`, which is on the user `PATH`. Those are exactly the executables the design avoids, and they satisfy any bare-name call that the shim does not intercept. Choose one of:

1. uninstall the tool for the duration of the run (`uv tool uninstall llm-commonplace`) and restore it afterwards — an operator decision, because it changes durable user state; record the before and after `uv tool list`; or
2. keep it, prepend the test bin directory ahead of every other entry in the test process, and record resolved provenance in every bare-name test.

Either way, a bare-name result whose recorded source is not the test shim is a **failed** provenance check, whatever the exit status.

## Antivirus observation

"No alert appeared" is not evidence. Record antivirus results from the product's own records, bounded to the run window.

For Microsoft Defender:

```powershell
$RunStart = Get-Date
# ... run the test ...
Get-MpThreatDetection -ErrorAction SilentlyContinue |
  Where-Object { $_.InitialDetectionTime -ge $RunStart } |
  Select-Object InitialDetectionTime, ThreatID, ProcessName, @{n='Resources';e={$_.Resources -join '; '}}
Get-WinEvent -FilterHashtable @{ LogName='Microsoft-Windows-Windows Defender/Operational'; Id=1116,1117,1121,1122; StartTime=$RunStart } -ErrorAction SilentlyContinue |
  Select-Object TimeCreated, Id, @{n='Message';e={$_.Message.Split([char]10)[0]}}
```

Event IDs 1116 and 1117 are malware detections and actions; 1121 and 1122 are attack surface reduction rule blocks and audits, which is where a policy that blocks unsigned or low-prevalence executables reports. Record the count of records and the first line of each; do not retain full messages, since they contain local paths. Record the Defender engine and signature versions and the cloud-protection settings from `Get-MpComputerStatus` (`AMEngineVersion`, `AntivirusSignatureVersion`) and `Get-MpPreference` (`MAPSReporting`, `CloudBlockLevel`, `AttackSurfaceReductionRules_Ids` and `_Actions`). Some of these need administrator rights; record `unknown` for what cannot be read.

For another product, record its name, version, and the equivalent history query before the run starts.

Exclusion lists cannot be read without administrator rights on the reference machine. Record `exclusions: unknown` unless the operator confirms none apply to the test root or to Python executables.

## Shim registration

After completing INSTALL.md, register the deterministic test shims with [REGISTRATION.md](./test-shims/REGISTRATION.md). The registrar writes only a disposable bin directory and invokes the selected uv-managed Python directly. Prepend that bin directory to the test process PATH; do not add .venv\\Scripts and do not invoke generated commonplace-*.exe files.

Harness boundary: the registered shims are `.cmd` files that call one hardcoded interpreter and a dispatcher covering only `commonplace-init` and `commonplace-validate`. The production concept is `uv run --no-sync python -m <module>`, which also puts `uv.exe` in the executed path. Results from the harness therefore say nothing about uv's own antivirus acceptance, about the other package entry points, or about project-aware interpreter selection.

## Test W0 — establish that the antivirus failure is observable

Run W0 before any shim test on a machine. It has three parts.

### W0a — the original detection record

The record exists; cite it rather than reconstructing it. From `origin/main`:

- `kb/work/framework-delivery/results-windows-install-030.md`, sections "Smart App Control hang" and "Shim workaround test and Avast detection", findings 4, 10, 11 and 12;
- `kb/work/windows-install/README.md`, open problems 1 to 5 and the testing rules;
- `kb/work/windows-install/results-2026-10-27-signed-python.md`, the signed python.org attempt and the path Avast left blocked.

Summary: 2026-10-26, Windows 11 Home 10.0.26300, Claude desktop app Code tab; Smart App Control on; Avast, McAfee and Defender registered in `root\SecurityCenter2`. Blocked files were uv launchers in `.local\bin` (`commonplace-source.exe` ten times, `commonplace-review-job-list.exe` three times) and in an isolated `%TEMP%\cp-030\bin` install, all by Code Integrity (Smart App Control), during a loop that ran `--help` on every executable; the loop hung until restart. Avast then deleted the tool environment's `Scripts\python.exe` after a WMI-launched encoded PowerShell command, and sandboxed `commonplace-validate.exe` and `commonplace-promotion-candidates.exe`.

Record in this run's report whether the current machine matches that configuration: Smart App Control state, the `root\SecurityCenter2` products, and the count of Code Integrity events 3033 and 3077 naming Commonplace, Python or uv (filter by name; McAfee driver loads flood that log).

### W0b — on-demand scan of the executables

Scan the generated entry points and the shim path's own executables without running them. This gives a static verdict from the local engine and signatures:

```powershell
& "$env:ProgramFiles\Windows Defender\MpCmdRun.exe" -Scan -ScanType 3 -File "$TestRoot\.venv\Scripts\commonplace-validate.exe"
& "$env:ProgramFiles\Windows Defender\MpCmdRun.exe" -Scan -ScanType 3 -File "$TestRoot\.venv\Scripts\python.exe"
Get-AuthenticodeSignature "$TestRoot\.venv\Scripts\commonplace-validate.exe", "$TestRoot\.venv\Scripts\python.exe", (Get-Command uv).Source | Select-Object Path, Status, @{n='Signer';e={$_.SignerCertificate.Subject}}
```

Record the scan verdicts and the signature status of each executable. A static clean verdict does not rule out a behavioral or reputation block; a static detection on the generated executable establishes that this machine can observe the failure.

### W0c — execution control through the generated executable

With antivirus observation armed, run the same W6 sweep through the generated executable:

```powershell
& $TestRoot\.venv\Scripts\commonplace-validate.exe notes
```

This is the only test in the plan that deliberately invokes a generated entry point. It may quarantine the executable; run it only against the disposable test environment, never against a working installation.

### W0 verdict

- Detection observed in W0b or W0c: this machine can test the design. W6 and W7 antivirus results are meaningful.
- No detection in either: this machine cannot distinguish the shim from the executable it replaces. Mark every antivirus result from this machine **uninformative**, complete the dispatch tests anyway (they still establish the mechanism), and run the antivirus tests on an informative environment per the next section.

## Antivirus tests on an informative environment

When the reference machine is uninformative, the claim is tested where the failure reproduces. In order of evidential value:

1. **The originating machine** from W0a: Smart App Control on, Avast and McAfee present. This is the only environment that tests the actual claim. Run W0c, then W3, W6, and W7 there, with observation armed. Follow the testing rules recorded in `kb/work/windows-install/README.md` on `origin/main`: start one command at a time and never loop over every executable, since a stalled launch hung that machine until restart; never start processes through WMI or `powershell -EncodedCommand`, since Avast treated that as malware and deleted files; record the `root\SecurityCenter2` products and back up the user `Path` before the run; and do not turn Smart App Control off, since Windows cannot turn it back on without a reinstall. On that machine, read Code Integrity events 3033 and 3077 filtered by file name, Avast's quarantine index and Auto-Sandbox log, in addition to the Defender queries above.
2. **A Smart App Control machine** without Avast. Smart App Control is an evaluation-mode setting on fresh Windows 11 installs and cannot be turned on after it has been off, so this means a fresh Windows 11 install or virtual machine that has never had it turned off. Confirm with W0c that the generated launcher is blocked (Code Integrity 3077), then run W3, W6, and W7. Because the harness's uv-managed `python.exe` is unsigned, this environment tests whether the shim path survives the same reputation check, which is the design's real risk; a run with the signed python.org interpreter from the `origin/main` proposal tests the proposal instead.
3. **A hardened Defender configuration** as a weaker analogue. On a disposable virtual machine with administrator rights, enable the attack surface reduction rule "Block executable files from running unless they meet a prevalence, age, or trusted list criterion" (rule id `01443614-cd74-433a-b99e-2ecdc07bfc25`) in block mode and raise the cloud block level, confirm with W0c that the launcher is blocked (event 1121), then run W3, W6, and W7. This approximates Smart App Control's reputation check but is not the same policy.
4. **Reputation lookup** for the executables, if the operator agrees to submit public files to an external scanner. Submit only the uv trampoline and the uv-managed `python.exe`, never project content. This records whether other engines flag the files; it is supporting evidence only.

A run on environment 2, 3 or 4 is recorded as a separate report naming the configuration. It does not replace environment 1 while that machine is reachable.

Until an informative environment has produced a W6 pass with a W0c detection, the design's antivirus claim is **unverified**, and `INSTALL.md` should not present the shim path as the supported Windows command path on antivirus grounds.

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

Run the intended shim by bare name, without the `.cmd` extension, from the test process. Record provenance in the same tool call, before invoking:

```powershell
(Get-Command commonplace-validate -CommandType Application).Source
commonplace-validate --help
$LASTEXITCODE
```

Pass requires the recorded source to be the registered shim under the test bin directory. A call spelled `commonplace-validate.cmd` tests the file, not resolution, and is **partial**. Verify that the shim reaches the same module behavior as W2 and does not call a generated Commonplace executable.

## Test W4 — initialized project

Initialize a disposable project through the shim, then validate a known fixture. Record the selected project root and package/runtime provenance. Record the generated `.envrc` and the init output's Windows note as installation behavior under review; they are not shim results.

## Test W5 — project selection and project isolation

These are two claims. The harness can establish only the first.

- **Project selection**: repeat W4 from a second project root. Confirm that the command derives its project from the working directory without any change to the user `PATH`. This is a property of the commands, not of the shim.
- **Project isolation**: requires two independent Commonplace installations with distinct package or runtime markers (different versions, or a marker file in each environment), each with its own shim registration, and a shim that selects the interpreter from the working directory. The current harness hardcodes one interpreter, so this part is **not run** until a project-aware shim exists. Do not report W5 as pass while this part is not run; report **partial** and name the missing shim capability.

## Test W6 — scripted operation

Run the larger scripted validation operation that previously triggered antivirus detection: the full collection sweep from `commands.md`, through the shim:

```powershell
foreach ($c in 'theory','reference','instructions','agent-memory-systems','sources') { commonplace-validate $c; $LASTEXITCODE }
commonplace-validate landings
commonplace-validate redirects
```

Collection names follow the checkout under test; take them from the `COLLECTION.md` directories under `kb/` and from `commonplace-validate --help` as observed in W2, and record the list used.

Record the exact top-level shim command, child process behavior, duration, exit status, the antivirus observation per **Antivirus observation**, and the W0 verdict that makes the antivirus observation meaningful or uninformative.

## Test W7 — fresh-process repeat

Terminate the PowerShell process. Start a fresh one. The test bin directory is not on the fresh process's PATH: prepend it again in that process, record `Get-Command` provenance, then repeat W3 and W6 by bare name.

This tests that the shim works without any shell mutation carried over from the registration process and that a second process reaches the same interpreter. It does not test whether a desktop agent runtime inherits the directory: that question is answered by probe reports from inside the runtime (see the native Windows probe of 2026-10-27, which observed user `PATH` inherited into Codex desktop tool calls and no shell state preserved between calls). State this boundary in the report.

## Evidence fields

Each report records:

- date, runtime, shell, Windows version if exposed;
- uv version and managed Python path;
- `uv tool list` and the pre-registration `Get-Command` resolution for both shim names;
- test root and project layout, normalized in the saved report, and whether the root is inside the checkout;
- exact top-level commands, spelled as run (bare name or with extension);
- exit status and bounded output;
- resolved source of every bare-name call;
- whether a generated `commonplace-*.exe` was invoked, and in which test;
- antivirus product, engine and signature versions, cloud and attack surface reduction settings where readable, the W0 verdict, the signature status of each executable in the path, and the bounded detection records for each test;
- project-selection result, and project-isolation marked run or not run;
- checks not run and their prerequisites;
- the result class of every test.

A test is **blocked** when installation cannot acquire dependencies, the shim is unavailable, or the antivirus result cannot be observed. Do not classify a blocked run as a pass or failure of the shim design.
