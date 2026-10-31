# Windows install run 4: main build on the afflicted machine (2026-10-31)

## Purpose

Check the `INSTALL.md` Windows procedure against the unreleased fixes on `main`, in particular open problem 4 (init reporting the shims as shadowing) and the `fcntl` crash of problem 10. Published 0.3.2 lacks both fixes, so the tool was installed from GitHub `main`, not from PyPI.

## Setup

- Commit: `55700da28` (`main` = `origin/main` after `git pull`). Package metadata says 0.3.2; the build is 102 commits past `v0.3.2`.
- Machine: Windows 11 Home 10.0.26300, Smart App Control on (`VerifiedAndReputablePolicyState` 1). Antivirus in `root\SecurityCenter2`: Windows Defender, Avast, McAfee.
- uv 0.13.5. Interpreter: `C:\Program Files\Python314\python.exe`, Authenticode `Valid`, signer Python Software Foundation.
- User variables, unchanged by this run: `UV_TOOL_DIR=<HOME>\.local\share\uv\tools`, `UV_PYTHON_INSTALL_DIR=<HOME>\.local\share\uv\python`, `UV_SYSTEM_CERTS=1`. User `Path` starts with `<HOME>\.local\commonplace-shims;<HOME>\.local\bin`; backed up in the session scratchpad before the run.
- Runtime: a Claude desktop app session. The app's oldest process started at 20:41 today, after the user variables were last changed (2026-10-28), so its inherited environment comes from a full restart.
- Starting tool: `llm-commonplace v0.3.1 [CPython 3.14.7]`. No other process was using it.

## Steps and results

1. **Install.** `uv tool install --reinstall --python 'C:\Program Files\Python314\python.exe' "llm-commonplace @ git+https://github.com/zby/commonplace@main"`, with `UV_CACHE_DIR=<HOME>\.cache\uv` set for the process only. Exit 0; built `55700da28`, Workjig 0.2.1 → 0.3.0, 25 executables. A non-editable install, so the library comes from the tool environment (`…\llm-commonplace\share\commonplace`), as for a PyPI user. `sys._base_executable` is the python.org path.
2. **Shims.** The `INSTALL.md` snippet, pasted unchanged: "Wrote 25 shims". All 50 files are byte-identical to the previous ones, as expected when the module names do not change.
3. **Every command starts.** In children of the app with `Path` read from the registry, each of the 25 commands was run with `--help`, one at a time, through its `.cmd` shim, with a 60 s timeout. All exited 0, in 0.2–4.3 s. `commonplace-task` and `commonplace-analysis` no longer crash on `fcntl` (problem 10 fixed for installed users once released).
4. **Init in a new project** (`<HOME>\cp-install-test-run4`): `git rev-parse` failed, so `git init`; `commonplace-init --name run4` exit 0 and **printed no shadowing warning** (problem 4 fixed). `commonplace-init --check` exit 0, every entry `ok`. `commonplace-validate landings` exit 0. `.commonplace/library.md` names the tool environment's `share/commonplace` as the library root, and `instructions\cp-skill-health-check\SKILL.md` exists there.
5. **Git Bash shims.** `command -v commonplace-validate` resolves to the shims directory; `commonplace-status --help` and `commonplace-init --check` exit 0.
6. **Step 4.** Renamed the two templates and committed (`Set up Commonplace KB`); exit 0.
7. **Inside the app, inherited environment.** The session's own `PATH` contains the shims directory and `UV_TOOL_DIR` is set. `Get-Command commonplace-validate` resolves to the `.cmd` shim, and the command runs.
8. **Outside the app.** A `.cmd` script in the scratchpad was started through `explorer.exe`, so its parent is Explorer rather than the app. `where` lists the shim first, then the uv launcher. `uv tool dir --bin` is `<HOME>\.local\bin`; `commonplace-init --help`, `--check`, a rerun of `commonplace-init`, `commonplace-validate landings` and `commonplace-task --help` all exited 0, with no shadowing warning.
9. **Security logs since the run started (20:44).** Code Integrity 3077/3033: 10 events, all `svchost.exe` refusing McAfee's own `mc-sec-plugin-x64.dll`; none concerns Python or Commonplace. Defender detections: 0. Avast logs: no line naming Commonplace, the tool directory or `Python314`.

## Gaps found

1. **Rerunning init after step 4 recreates the templates.** After the rename and first commit, the outside-app rerun of `commonplace-init` created `AGENTS.md.template` and `CLAUDE.md.template` again, and they show as untracked. `INSTALL.md` says rerunning init is safe and tells users to rerun it after upgrades. It does not say the templates come back. Either init should skip the templates when `AGENTS.md` exists, or the guide should say to delete them. Not Windows-specific.
2. **Open problems 5, 7 and 9 have no `INSTALL.md` text.** This run, like the earlier ones, depended on user variables that `INSTALL.md` does not mention: `UV_SYSTEM_CERTS=1` for HTTPS-inspecting antivirus (problem 7), `UV_TOOL_DIR` and `UV_PYTHON_INSTALL_DIR` outside the desktop app's virtualised `%APPDATA%` (problem 5), and a short `UV_CACHE_DIR` for `uv run` in a checkout (problem 9). On a new machine with the same antivirus, step 2 would fail with `UnknownIssuer`. Fixed later the same day: `INSTALL.md` now has a section, "Windows: uv behind antivirus or inside the Claude desktop app".

## Not covered

- An agent rooted in the scratch project (skill discovery, the health-check skill's shim rule, stubs with arguments). That is item 4 of the [Windows delivery handoff](../framework-delivery/windows-delivery-handoff.md).
- The published package: 0.3.2 lacks these fixes. Repeat steps 1–4 from PyPI after the next release.
- Trafilatura, and the uv launchers in `<HOME>\.local\bin` (not started).
- Multi-day antivirus behaviour ([windows-signed-python-field-use](../windows-signed-python-field-use/README.md)).

## State left behind

- Tool: `llm-commonplace 0.3.2` from `git+https://github.com/zby/commonplace@55700da28`, non-editable, over python.org 3.14.7, in the same tool directory. To go back to the published package: `uv tool install --reinstall --python 'C:\Program Files\Python314\python.exe' llm-commonplace`, then rerun the shim snippet.
- Shims: unchanged bytes. User `Path` and user variables: unchanged.
- Test project `<HOME>\cp-install-test-run4`: Git repository with one commit, plus the two untracked templates from gap 1.
- Checkout: this report and the workshop updates only.
