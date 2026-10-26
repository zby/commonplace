# Windows install check: published 0.3.0, real user install

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

## Findings

1. **`INSTALL.md`'s `--python ">=3.11"` is uncapped.** On 2026-10-26, uv picked 3.15, and the install failed on a machine without MSVC because pyyaml has no cp315 wheel. Linux would probably build from source instead, so the failure is Windows-specific. Candidates: an upper bound such as `">=3.11,<3.15"`, or the CI job pinning the Python it tests.
2. **HTTPS interception breaks uv's default trust store.** Antivirus web scanning and corporate proxies are common on Windows. `INSTALL.md`'s Windows troubleshooting could name `UnknownIssuer` and `UV_SYSTEM_CERTS=1`, and winget's matching `msstore` failure with `--source winget`.
3. **Packaged-app virtualisation of `%APPDATA%`.** A uv install run from inside the Claude desktop app, or presumably any MSIX-packaged agent, writes to a private copy of `%APPDATA%`. The managed-Python junction breaks, and the tools are invisible to other processes. Persisting `UV_TOOL_DIR`, `UV_PYTHON_INSTALL_DIR` and `UV_SYSTEM_CERTS` as user environment variables worked; `uv tool list` and `uv tool upgrade llm-commonplace` then worked in a fresh process. Not yet checked from a terminal outside the app. The library root moves to `%USERPROFILE%\.local\share\uv\tools\…`, and every path init writes follows it correctly.
4. **Smart App Control can block a specific uv-managed CPython build** (`0xc0e90002` for 3.13.17, while 3.14.9 and 3.15.1 ran). The health check's Windows troubleshooting has nothing for this.
5. **Health check portability.** Steps 1, 2 and 6 are Bash-only and had to be translated, which confirms the gap already filed to E1 in [execution-channel-compatibility](../execution-channel-compatibility/README.md).
6. **Desktop agent `PATH`.** The install-time process keeps its old `PATH` until a full app restart, as `INSTALL.md` already warns. The health check classified it correctly as runtime `PATH`, not a missing package.
7. **Persisted uv variables did not reach a later session.** In the re-run, a new session's process had the updated `PATH` but not `UV_TOOL_DIR`, `UV_PYTHON_INSTALL_DIR` or `UV_SYSTEM_CERTS`, so `uv tool list` and any `uv tool upgrade` run by the agent miss the installed tool. Without `UV_PYTHON_INSTALL_DIR` and `UV_SYSTEM_CERTS`, a reinstall from that process would also hit hazards 2 and 3 again. The `commonplace-*` commands are unaffected, because the executables and every path init writes are absolute. The health check has no classification for this: its step 4 reads `llm-commonplace` missing from `uv tool list` as "not installed", which would point to a reinstall into the wrong directory. A check that `uv tool dir` contains the library root named in `.commonplace/library.md` would tell the two apart. The workaround in finding 3 is less robust inside the desktop app than the fresh-process check suggested.
