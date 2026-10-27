# Windows install check: published 0.3.0, real user install

Follow-up work on these findings moved to [windows-install](../windows-install/README.md) on 2026-10-27. This file stays as the record of the first run.

- Tester and date: Claude Code agent (claude-opus-5-5) in the Claude desktop app's Code tab, 2026-10-26, at the operator's request
- Scope: **not** the isolated run in [run-prompts.md](./run-prompts.md#windows--install-check-for-the-published-030-any-harness). The operator asked for a normal install on a machine with no developer tools. Commonplace went into the user-level uv tool directory with no `$root` isolation, and the project was kept (`C:\Users\zzbby\commonplace-kb`). The steps below map onto the prompt's steps where they apply. `cp-skill-health-check` ran afterwards in the same session.

**Result.** 0.3.0 installs, initialises, passes `--check` (26 `ok`) and validates on Windows 11 Home. Five things stood between `INSTALL.md` and a working install. Two are general Windows hazards that `INSTALL.md` does not mention: HTTPS interception and an uncapped Python choice. One is a Smart App Control block. Two come from running inside the Claude desktop app: AppData virtualisation and a process `PATH` frozen at launch.

## Environment

- Microsoft Windows 11 Home, 10.0.26300; Windows PowerShell 5.1.26100.9711 (the agent's shell)
- Harness: Claude desktop app, Code tab. The app is a packaged (MSIX) app, and its child processes inherit its file-system virtualisation. No `claude` CLI on the machine.
- Before the run: winget 1.29.380 and `curl.exe` 8.21.0 (Windows built-in). Missing: uv, git, rg, Poppler, Trafilatura, gh. A Microsoft Store `python.exe` alias was present and runs no Python.
- Installed with `winget install --id <id> -e --source winget`: uv 0.13.5, Git 2.56.0.windows.3, ripgrep 15.2.0, Poppler 25.07.0. gh was skipped (optional).
- Python used by the tool: 3.14.9 (uv-managed). Trafilatura 2.3.1 runs on 3.15.1.

## Steps

**Prerequisites (not in the prompt).** `winget install` without `--source winget` failed for all four packages. The `msstore` source returned `0x8a15005e : The server certificate did not match any of the expected values`. Passing `--source winget` installed all four.

**1. Install.** `uv tool install "trafilatura>=2.2"` and `uv tool install --python ">=3.11" llm-commonplace` failed in four successive ways:

1. `invalid peer certificate: UnknownIssuer` while downloading python-build-standalone from GitHub. Something on the machine intercepts HTTPS with a root that only the Windows store trusts. `--native-tls` (deprecated in uv 0.13.5 in favour of `--system-certs`, env `UV_SYSTEM_CERTS=1`) fixed it.
2. `Missing expected target directory for Python minor version link at C:\Users\zzbby\AppData\Roaming\uv\python\cpython-3.15.1-windows-x86_64-none`. uv's default Python and tool directories live under `%APPDATA%`. Inside the packaged app, writes there are redirected to `AppData\Local\Packages\AnthropicPBC.Claude_…\LocalCache\Roaming`, so the minor-version junction pointed at a real path that did not exist. Tools installed there would also be invisible outside the app. `UV_PYTHON_INSTALL_DIR` and `UV_TOOL_DIR` were set to `%USERPROFILE%\.local\share\uv\{python,tools}`.
3. `>=3.11` resolved to CPython 3.15.1. pyyaml 6.0.3 has no cp315 wheel, so it built from source and failed with `Microsoft Visual C++ 14.0 or greater is required`. Trafilatura installed fine on 3.15.
4. `--python 3.13` (3.13.17) downloaded but failed: `Querying Python … failed with exit status exit code: 0xc0e90002`. This is a code-integrity block, most likely Smart App Control on Windows 11 Home. That security setting was left alone.

`--python 3.14` (3.14.9) installed `llm-commonplace==0.3.0` with 22 packages and **25 executables**. `uv tool update-shell` added `C:\Users\zzbby\.local\bin` to the user `PATH`.

**2. Command ownership.** `(Get-Command commonplace-validate -All).Source` printed only `C:\Users\zzbby\.local\bin\commonplace-validate.exe`. That is `uv tool dir --bin`, so nothing shadows it.

**3. Init.** `git init`, then `commonplace-init --root . --name commonplace-kb` created the scaffold, 24 stubs, `.commonplace/library.md` and `.gitignore`, and refreshed `.claude/settings.local.json`.

**4. `--check`.** 26 `ok`, exit 0.

**5. File facts.** Paths use forward slashes and carry the drive letter. Neither file has a byte-order mark: the first bytes of `settings.local.json` are `123,13,10` (written with CRLF) and of `library.md` are `35,32,67`.

- Allow entry: `Read(//C:/Users/zzbby/.local/share/uv/tools/llm-commonplace/share/commonplace/**)`
- Stub path line: `C:/Users/zzbby/.local/share/uv/tools/llm-commonplace/share/commonplace/instructions/cp-skill-write/SKILL.md`
- `library.md` root: `C:/Users/zzbby/.local/share/uv/tools/llm-commonplace/share/commonplace`

**6. Validation.** `commonplace-validate landings`: `VALIDATION SUCCESS`, 0 failures, 0 warnings, exit 0. The four collections were not validated one at a time.

**7. Init rerun.** Not run.

**8. Read rule in Claude Code.** Not settled. Agent sessions in the project read library files without a prompt. But this session had also been granted `C:\Users\zzbby` as a working directory, which covers the library, so the reads do not isolate the `Read(//C:/…/**)` rule. No `claude` CLI was available for the headless check.

**9. Cleanup.** Not applicable: a kept user install.

## Health check (same session, before restarting the app)

`cp-skill-health-check` ran with its Bash steps translated by hand to PowerShell. Its report:

```text
- Project root: OK (C:\Users\zzbby\commonplace-kb)
- Layout: installed project
- Library pointers: OK (commonplace-init --check: all ok)
- Control-plane file: OK (CLAUDE.md imports @AGENTS.md and @.commonplace/library.md)
- Runtime skills: OK (.claude and .agents stubs present)
- Diagnostic context: other context (general check, no failing workflow)
- Worker launch: available (Agent tool exposed)
- Agent depth / remaining nesting / concurrent capacity: unknown
- Workflow nesting required: not applicable
- Fresh-context isolation: supported (non-fork Agent launches start fresh)
- Launch probe: not run (no delegation symptom)
- uv tool installation: OK (llm-commonplace 0.3.0, trafilatura 2.3.1)
- Runtime PATH: problem in this process; OK in the saved user environment
- Command ownership: uv tool (single candidate in C:\Users\zzbby\.local\bin)
- Validator: OK (VALIDATION SUCCESS, exit 0)
Likely cause: the app process predates the install, so its PATH lacks
C:\Users\zzbby\.local\bin and uv; the saved user PATH has both.
Recommended fix: fully restart the Claude app.
Maintenance observations: none (no .envrc, no .venv, no kb/commonplace).
```

Evidence: bare `uv` and `commonplace-*` were "not recognized" in the app's process. The saved user `PATH` contained `.local\bin` and the process `PATH` did not. With the saved `PATH` loaded, `commonplace-validate` resolved to `.local\bin` and exited 0. All 25 declared executables were present.

## Health check re-run (new session, same day)

`cp-skill-health-check` ran again in a new Code-tab session at 14:51, using the Bash tool (Git Bash) for steps 1, 2, 5 and 6 and PowerShell for step 4. It is not established that the app was fully restarted: the oldest running `claude` process started at 14:19:27, before the install. Its report:

```text
- Project root: OK (C:\Users\zzbby\commonplace-kb)
- Layout: installed project
- Library pointers: OK (commonplace-init --check: 26 ok, exit 0)
- Control-plane file: OK
- Runtime skills: OK (.claude and .agents, 12 stubs each)
- Diagnostic context: user-facing agent, general check
- Worker launch: available (Agent tool exposed)
- Agent depth / remaining nesting / concurrent capacity: unknown
- Workflow nesting required: not applicable
- Fresh-context isolation: supported
- Launch probe: not run (no delegation symptom)
- uv tool installation: problem in this process (see below)
- Runtime PATH: OK (C:\Users\zzbby\.local\bin on the process PATH)
- Command ownership: uv tool (single candidate per name)
- Validator: OK (landings: 0 failures, 0 warnings)
Likely cause: the process inherited the updated PATH but none of the
persisted uv variables, so uv falls back to %APPDATA% and sees no tools.
Recommended fix: fully restart the Claude app; until then pass UV_TOOL_DIR
explicitly to uv tool commands.
Maintenance observations: none (no .envrc, no .venv, no kb/commonplace).
```

Evidence: bare `uv`, `commonplace-init` and `commonplace-validate` resolved, the last two only to `C:\Users\zzbby\.local\bin`. `uv tool list` printed `No tools installed`. `uv tool dir` printed `C:\Users\zzbby\AppData\Roaming\uv\tools` and `uv python dir` printed `C:\Users\zzbby\AppData\Roaming\uv\python`. `UV_TOOL_DIR`, `UV_PYTHON_INSTALL_DIR` and `UV_SYSTEM_CERTS` were set at user scope and empty in the process, in both Git Bash and PowerShell. With `UV_TOOL_DIR` set by hand, `uv tool list` showed `llm-commonplace v0.3.0` (25 commands) and `trafilatura v2.3.1`. The receipt's entry points all target `C:/Users/zzbby/.local/bin`.

Re-run after a confirmed full app restart: pending.

## Trace review (same day)

At the operator's request, both session transcripts were read for errors that the summaries above hid. The install session is `2ae41090-…` (13:24–13:44 UTC) and the health-check session is `6a140887-…`; both are under `~\.claude\projects\C--Users-zzbby-commonplace-kb\`. Every tool result flagged as an error, or containing error-like text, was checked against its full output. The app's own log directory (`LocalCache\Roaming\Claude\logs`) was empty. The suspicious items were re-tested on the machine:

- **The "fresh process" check in finding 3 did not test inheritance.** The 13:35 call that showed `uv tool list` and `uv tool upgrade` working ran `powershell -NoProfile` but copied the three uv variables from user scope into the child by hand, and rebuilt `PATH` by hand too. It proved the variables' values are right, not that a new process receives them. Finding 7 shows a new app session did not.
- **`commonplace-init --check` does not notice a missing control plane.** Init wrote `AGENTS.md.template` and `CLAUDE.md.template`, and the agent renamed them at 13:33:50, as `INSTALL.md` step 4 says. Step 3 above omits that rename. Between init and the rename, `--check` reported 26 `ok` and `commonplace-validate landings` passed, with no `AGENTS.md` or `CLAUDE.md` in the project. Reproduced on a copy of the project with both files deleted: 26 `ok`, exit 0. A user who skips step 4 gets a clean check and an agent that never learns about `.commonplace/library.md`.
- **Two "failed" calls were false failures.** The 13:30:47 verification (exit 255) and the 13:38:51 diagnostic (`validate exit: -1`) both piped a native command into `Select-Object -First n`. Windows PowerShell 5.1 stops the upstream process and sets `$LASTEXITCODE` to -1. Reproduced: `commonplace-validate landings | Select-Object -First 1` gives -1, while the same command piped to `Out-Null` gives 0. Prompts that record exit codes should not truncate native output this way.
- **Git also depends on the HTTPS-interception workaround.** Git for Windows' system `gitconfig` sets `http.sslBackend=schannel`, so the clone worked; the explicit `-c http.sslBackend=schannel` was redundant. With `openssl`, `git ls-remote https://github.com/zby/commonplace.git` fails with `unable to get local issuer certificate`. This is the same interception as finding 2. SSH to GitHub on port 22 worked later the same day; `git push` over SSH succeeded.
- **Long paths are off.** `LongPathsEnabled` is 0 and `core.longpaths` is unset. Git refused the harness's 268-character scratchpad path with `Filename too long` (13:43:53). The longest tracked path in the checkout at `C:\Users\zzbby\commonplace` is 200 characters, which leaves about 60 characters for a deeper clone location or for longer generated paths.
- **CRLF checkouts are fine.** `core.autocrlf=true` comes from the same system config, so the checkout is CRLF. A CRLF copy of the project gave 26 `ok`, every collection validated, and a typed CRLF note from `kb/theory/` validated.
- **Leftovers from the failed attempts.** 68 MB of CPython 3.15.1 remain in the app's virtualised `LocalCache\Roaming\uv\python`, and a `python` directory remains in the real `AppData\Roaming\uv`. Both are unused. Under `.local\share\uv\python`, the Smart-App-Control-blocked 3.13.17 is unused, and 3.15.1 serves only Trafilatura.

## Smart App Control hang (same day)

The follow-up run in session `6a140887-…` stalled, and so did a recovery session (`26d22254-…`) after the operator restarted the computer. Both stalled on the same step: a loop that ran `--help` on every `commonplace-*.exe`, first in `.local\bin`, then in an isolated install under `%TEMP%\cp-030\bin`.

- **Session `6a140887-…`.** At 14:10 UTC, `commonplace-source` failed in Git Bash (`Permission denied`) and in PowerShell (`Zasady kontroli aplikacji zablokowały ten plik`, "an App Control policy blocked this file"). The 14:10:34 loop invoked each exe with `&`, and it never returned. The tool's default 2-minute timeout did not end it either. The operator restarted the computer.
- **Session `26d22254-…`.** At 14:24 the probe ran again, this time with `Start-Process`, stdin redirected from an empty file, and a 15 s `WaitForExit` per exe. The `.local\bin` pass finished in 70 s: 24 exes ran and `commonplace-source` was blocked. The `cp-030\bin` pass started at 14:25:22 and was still stalled at 14:30, even though the 15 s timeout should have ended each launch.

Evidence: `Microsoft-Windows-CodeIntegrity/Operational` events 3033/3077 (local time, UTC+1) name policy `{0283ac0f-fff1-49ae-ada1-8a933130cad6}`, and `HKLM:\SYSTEM\CurrentControlSet\Control\CI\Policy` has `VerifiedAndReputablePolicyState` = 1 (Smart App Control on). Blocked loads:

| File | Blocks | Local time |
|---|---|---|
| `.local\bin\commonplace-source.exe` | 10 | 15:10–15:24 |
| `.local\bin\commonplace-review-job-list.exe` | 3 | 15:11 |
| `cp-030\bin\commonplace-ack-review.exe` | 1 | 15:25:26 |
| `cp-030\bin\commonplace-finalize-review-job.exe` | 1 | 15:25:53 |
| `cp-030\bin\commonplace-github-snapshot.exe` | 1 | 15:26:06 |

Smart App Control's verdicts were not stable. `commonplace-review-job-list` was blocked in the first session and ran in the second. In `cp-030\bin`, each blocked launch took 13–27 s. After 15:26:06, no further block events appeared, yet the loop never resumed. Every `commonplace-*.exe` is a uv trampoline: an unsigned launcher with a unique hash, so Smart App Control has no reputation for it. Inference, not confirmed: process creation for the next exe stalled inside the reputation check, where neither `WaitForExit` nor the harness timeout can reach it, which would explain why a restart was needed. The operator also saw Windows notifications about blocked PowerShell features at the same time.

## Shim workaround test and Avast detection (same day)

`INSTALL.md` gained a workaround for finding 10: shims that start each command through the tool environment's `Scripts\python.exe`, which Smart App Control lets run, placed ahead of `.local\bin` on `PATH`. Its snippet was tested at 14:47–14:48 UTC, word for word except that the shims went into a new directory, `C:\Users\zzbby\cp-shim-test\shims`. The user `Path` was backed up first. To get processes with a fresh environment, PowerShell and Git Bash were started through WMI (`Win32_Process.Create`), PowerShell with `-EncodedCommand`; both reported the shims directory on `PATH`.

- **The procedure works.** In both shells, the bare names resolved to the shims. `commonplace-source` ran, `git init` and `commonplace-init --name` set up a new project, `--check` gave 26 of 26 `ok`, and `commonplace-validate landings` succeeded. A bad flag returned exit 2 with the right program name, and Git Bash passed through an argument containing a space. Code Integrity logged no blocks. The undo steps restored the user `Path` exactly.
- **`commonplace-init` contradicts the workaround.** Each plain init run warns that all 25 commands "resolve outside uv's tool executable directory". The warning comes from `installation_warnings()` in `cli/init_project.py`, and it tells the user to remove the shadowing `PATH` entry. `--check` stays clean. `INSTALL.md` now says the warning is expected with the shims.
- **Avast removed the tool's `python.exe`.** At 14:48:37 UTC, `…\uv\tools\llm-commonplace\Scripts\python.exe` disappeared; `pythonw.exe` and the launchers stayed. Avast's quarantine index (`C:\ProgramData\Avast Software\Avast\chest\index.xml`) gained entry 3 at 14:48:57: detection `IDP.HELU.PSE95%s_cmd`, a behavioural (IDP) detection recorded against `powershell.exe`. Its process chain names `git.exe`, `cmd.exe`, the uv-managed CPython 3.14.9, `uv.exe` and `conhost.exe`; the deleted file itself was not kept. Windows Defender and Code Integrity logged nothing. After that, every launcher failed with `error: uv trampoline failed to canonicalize script path`. The likely trigger was the test harness itself: WMI starting `powershell -EncodedCommand`, which then started cmd and Python, is a common malware pattern. Normal use of the shims was not shown to trigger it, but this was not tested either.
- **Avast also sandboxes the launchers.** `C:\ProgramData\Avast Software\Avast\log\autosandbox.log` lists `commonplace-validate.exe` from `.local\bin` as an "Autosandbox candidate" at 15:36, 15:40 and 15:50 local time, and `cp-030\bin\commonplace-promotion-candidates.exe` at 15:26. Smart App Control, Avast's Auto-Sandbox and Avast's Behavior Shield all act on the same unsigned, never-before-seen executables. The machine also registers McAfee as an antivirus product.
- **The snippet's tool path depends on `UV_TOOL_DIR`.** In a shell without it (finding 7), `uv tool dir` points under `%APPDATA%`, and the original snippet would add an empty shims directory to `PATH`. The snippet now stops before changing anything if `Scripts\python.exe` is missing. Tested: with a wrong `UV_TOOL_DIR` it threw, and left `PATH` and the shims directory untouched. With the correct one it also threw, which is how the missing `python.exe` was found. The wrapped version's success path still needs a run on a repaired install.

Noise that is not a product finding: the agent's guessed WinGet `Links\uv.exe` path (uv is linked from its package directory), a PowerShell parse error in the agent's own diagnostic, CLIXML progress records from nested `powershell`, and a `git commit -F -` here-string that Windows PowerShell 5.1 passed as a pathspec.

## Findings

1. **`INSTALL.md`'s `--python ">=3.11"` is uncapped.** On 2026-10-26, uv picked 3.15, and the install failed on a machine without MSVC because pyyaml has no cp315 wheel. Linux would probably build from source instead, so the failure is Windows-specific. Candidates: an upper bound such as `">=3.11,<3.15"`, or the CI job pinning the Python it tests.
2. **HTTPS interception breaks uv's default trust store.** Antivirus web scanning and corporate proxies are common on Windows. `INSTALL.md`'s Windows troubleshooting could name `UnknownIssuer` and `UV_SYSTEM_CERTS=1`, and winget's matching `msstore` failure with `--source winget`.
3. **Packaged-app virtualisation of `%APPDATA%`.** A uv install run from inside the Claude desktop app, or presumably any MSIX-packaged agent, writes to a private copy of `%APPDATA%`. The managed-Python junction breaks, and the tools are invisible to other processes. Persisting `UV_TOOL_DIR`, `UV_PYTHON_INSTALL_DIR` and `UV_SYSTEM_CERTS` as user environment variables worked; `uv tool list` and `uv tool upgrade llm-commonplace` then worked in a fresh process, but that process had the variables copied in by hand (see the trace review), so inheritance was not tested. Not yet checked from a terminal outside the app. The library root moves to `%USERPROFILE%\.local\share\uv\tools\…`, and every path init writes follows it correctly.
4. **Smart App Control can block a specific uv-managed CPython build** (`0xc0e90002` for 3.13.17, while 3.14.9 and 3.15.1 ran). The health check's Windows troubleshooting has nothing for this.
5. **Health check portability.** Steps 1, 2 and 6 are Bash-only and had to be translated, which confirms the gap already filed to E1 in [execution-channel-compatibility](../execution-channel-compatibility/README.md).
6. **Desktop agent `PATH`.** The install-time process keeps its old `PATH` until a full app restart, as `INSTALL.md` already warns. The health check classified it correctly as runtime `PATH`, not a missing package.
7. **Persisted uv variables did not reach a later session.** In the re-run, a new session's process had the updated `PATH` but not `UV_TOOL_DIR`, `UV_PYTHON_INSTALL_DIR` or `UV_SYSTEM_CERTS`, so `uv tool list` and any `uv tool upgrade` run by the agent miss the installed tool. Without `UV_PYTHON_INSTALL_DIR` and `UV_SYSTEM_CERTS`, a reinstall from that process would also hit hazards 2 and 3 again. The `commonplace-*` commands are unaffected, because the executables and every path init writes are absolute. The health check has no classification for this: its step 4 reads `llm-commonplace` missing from `uv tool list` as "not installed", which would point to a reinstall into the wrong directory. A check that `uv tool dir` contains the library root named in `.commonplace/library.md` would tell the two apart. The workaround in finding 3 is less robust inside the desktop app than the fresh-process check suggested.
8. **`--check` passes without a control plane.** With no `AGENTS.md` or `CLAUDE.md` in the project, `commonplace-init --check` reports 26 `ok` and validation passes, so skipping `INSTALL.md` step 4 goes unnoticed. Candidate: `--check` reports when no root instruction file references `.commonplace/library.md`.
9. **Windows long paths are off by default.** About 60 characters of headroom remain at this clone location. Candidates: a note in `INSTALL.md`'s Windows section, or a CI check on the longest tracked path.
10. **Smart App Control blocks and stalls the uv launcher executables.** With Smart App Control on, any `commonplace-*` command can be refused at launch. The verdict varies between runs, and in one case a launch apparently hung until the computer was restarted (see "Smart App Control hang"). This goes beyond finding 4: it affects the installed commands themselves, not just one CPython build. In Git Bash the block shows up only as `Permission denied`, which the health check would misread as a file-permission problem. Candidates: a Windows troubleshooting entry that names Code Integrity events 3033/3077 and `VerifiedAndReputablePolicyState`; a health-check step that reads that log instead of launching every executable; and a rule in the run prompts against batch-launching executables on Windows while Smart App Control is on. Turning Smart App Control off cannot be undone without reinstalling Windows, so that cannot be the default advice. Still open: whether the stall reproduces, and whether a signed launcher would avoid it. `%TEMP%\cp-030` is a leftover from this run.
11. **Third-party antivirus can break the tool environment, not just block it.** Avast's Behavior Shield deleted `Scripts\python.exe` after a test that started PowerShell through WMI with an encoded command, and its Auto-Sandbox repeatedly sandboxes the `commonplace-*` launchers. Windows' own logs show nothing about either. The symptom, `uv trampoline failed to canonicalize script path`, does not mention the antivirus; the health check has no classification for it, and `INSTALL.md` has none. A reinstall repairs it. Lessons for Windows test prompts: never launch processes through WMI or `-EncodedCommand`, and record which antivirus products are present (`root\SecurityCenter2`) before a run.
12. **`commonplace-init` treats the shim workaround as an installation error.** See "Shim workaround test and Avast detection". If the workaround stays, init and the health check need to recognise the shims, for example a shim that names the tool's `python.exe` or a marker file in its directory.
