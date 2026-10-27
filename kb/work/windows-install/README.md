# Windows install

## Commission

Posed by the operator on 2026-10-27. Make a normal user-level install of Commonplace work on Windows 11: `uv tool install` succeeds, and every `commonplace-*` command starts and keeps working in new processes, with Smart App Control on and third-party antivirus present, both inside and outside the Claude desktop app. The work was split out of [framework-delivery](../framework-delivery/README.md) because that workshop covers many unrelated delivery questions, which distracted agents working on the install.

**Closes when** `INSTALL.md` gives one Windows procedure that has been verified on this machine in fresh processes, inside and outside the desktop app, and each open problem below is fixed, documented as a known limit, or rejected with a reason. Durable results go to `INSTALL.md`, `cp-skill-health-check`, `commonplace-init`, or an ADR when a decision changes the install model (ADR 064, ADR 086). Then delete this directory and its entry in `kb/work/README.md`.

## Scope

In scope: installing the package and its Python, uv's directories and certificates, `PATH`, starting the commands, Smart App Control, antivirus, and how `commonplace-init` and the health check treat the resulting layout.

Out of scope:

- Making skills and their shell commands work on Windows, including the health check's Bash-only steps. That is E1 in [execution-channel-compatibility](../execution-channel-compatibility/e1-windows-execution.md).
- Probe runs, harness delivery, and the check that `--check` passes without a control plane. Those stay in [framework-delivery](../framework-delivery/README.md).

## Constraints

- **One install path on every platform** (framework-delivery, 2026-09-24). A Windows-only fix must be either troubleshooting for a Windows hazard or a change every platform takes. Record which.
- **Do not turn Smart App Control off.** Windows cannot turn it back on without a reinstall.
- **Testing rules learned on this machine** (2026-10-26):
  - Start one command at a time; never launch every executable in a loop, because a stalled launch can hang the machine until restart.
  - Never start processes through WMI or `powershell -EncodedCommand`; Avast treated that pattern as malware and deleted the tool's `python.exe`.
  - Before a run, record the antivirus products (`root\SecurityCenter2`) and back up the user `Path`.
  - A process keeps the environment it started with. A check needs a fully restarted app or shell, and the record says which.
- Commits carry `Workshop: kb/work/windows-install`.

## Evidence

The first install, on 2026-10-26, is recorded in [results-windows-install-030.md](../framework-delivery/results-windows-install-030.md). It stays in framework-delivery as the historical record; new runs are recorded in this directory. Numbers in brackets below are that file's finding numbers.

## Open problems

1. **Smart App Control blocks and stalls the uv launchers** [10]. The `.exe` files in `uv tool dir --bin` are unsigned and unique to each install, so they have no reputation. The verdict varies between runs; one launch hung until restart.
2. **Smart App Control can block a uv-managed CPython build** [4]. 3.13.17 was blocked; 3.14.9 and 3.15.1 ran. The builds are unsigned.
3. **Avast deletes or sandboxes tool files** [11]. It deleted the tool environment's `Scripts\python.exe` and repeatedly sandboxes the launchers. The symptom is `uv trampoline failed to canonicalize script path`. Windows' own logs show nothing.
4. **`commonplace-init` treats shims as an installation error** [12]. It warns that every command resolves outside uv's tool directory.
5. **The desktop app virtualises `%APPDATA%`** [3, 7]. uv's default directories there break the Python junction and hide tools from other processes. The user-level `UV_TOOL_DIR`, `UV_PYTHON_INSTALL_DIR` and `UV_SYSTEM_CERTS` work around it, but a later app session did not inherit them.
6. **`--python ">=3.11"` has no upper bound** [1]. uv picked 3.15, which has no pyyaml wheel, and the build failed without MSVC.
7. **HTTPS interception breaks uv's certificate check** [2]. `UnknownIssuer`; fixed by `UV_SYSTEM_CERTS=1`. winget's `msstore` source fails the same way; `--source winget` avoids it.
8. **The app keeps its `PATH` until a full restart** [6]. `INSTALL.md` already warns; the health check classifies it correctly.
9. **Long paths are off by default** [9]. About 60 characters of headroom remain at the checkout location. On 2026-10-27, `uv run` failed with `Trivial strip failed` while installing the project into `.venv`. uv's cache sat in the desktop app's virtualised `…\Packages\AnthropicPBC.Claude_…\LocalCache\Local\uv\cache`, the wheel's library paths went past the limit, and uv compared a `\\?\` path with a plain one. Setting `UV_CACHE_DIR=C:\Users\zzbby\.cache\uv` fixed it, so problems 5 and 9 combine.
10. **Unix-only `fcntl` file locking** (found 2026-10-27). `commonplace-task --help` and `commonplace-analysis --help` crash on import. The command starts, so the install looks fine, but it cannot work. The import is in Workjig (`workjig/run.py`, 0.1.0; another agent is making Workjig Windows-compatible as of 2026-10-27) and also in Commonplace's own code: `src/commonplace/lib/agentic_analysis/effects.py`, `src/commonplace/lib/agentic_analysis/worktree.py`, `src/commonplace/headless/jobs.py`, `scripts/sync_x_likes.py`, and `tests/commonplace/agentic_analysis/test_publication_locking.py`. Fixing Workjig alone does not fix these commands.
11. **The full test suite cannot pass on Windows** (2026-10-27, Python 3.14.7, `uv run pytest -m ''` from Git Bash; PowerShell 5.1 drops the empty `''` argument). 795 passed, 47 failed, 21 skipped, 6 collection errors. All failing tests are Commonplace's own; Workjig's tests were not run. Causes, from one-line tracebacks:
    - `fcntl` (problem 10): the 6 collection errors and about 6 failures, through Workjig and through Commonplace's own imports.
    - `\` instead of `/`: about 20 failures. Most are messages that tests compare as strings, but relocation is a real bug: it writes Markdown links such as `[def](..\notes\definitions\d.md)`.
    - Symlink creation needs a privilege (`WinError 1314`): 4 failures, all in test setup.
    - Probably line endings: this checkout has `core.autocrlf=true`, so files are CRLF on disk. A content-hash mismatch and the 6 full-pass "does not match canonical frontmatter rendering" failures fit this; not confirmed.
    - One each: printing ` ` to a cp1250 console (`UnicodeEncodeError`), and a Windows path used inside a regular expression (`bad escape \l`).
    - A few, in the tag-readme and unquoted-source checks, not yet diagnosed. Since commit `f4ea589dd` (2026-10-26) the full suite runs in GitHub CI rather than before each push, so this no longer blocks pushing. Fixing the failures moved to [windows-test-suite](../windows-test-suite/README.md) on 2026-10-27; the `fcntl` imports in problem 10 are its item 1.

## Attempts

- **Shims through the tool environment's `python.exe`** (2026-10-26). The `INSTALL.md` snippet worked: commands resolved to the shims and ran without Code Integrity blocks. Avast then deleted that `python.exe`, probably triggered by the WMI test harness, not by the shims. Not retested on a repaired install.
- **Signed python.org 3.14.7 as the tool's base** (2026-10-27, [results](./results-2026-10-27-signed-python.md)). Installed and ran with a valid PSF signature and no Code Integrity block. The editable tool install then failed: the exact path `llm-commonplace\Scripts\python.exe` refuses any file, probably an Avast block left from the 2026-10-26 deletion. Without a virtual environment it worked: `uv pip install --target` into a plain folder, shims that start the signed `python.exe` and add that folder with `site.addsitedir`. Commands ran from PowerShell and Git Bash by full path with no Code Integrity or Avast reaction. Not yet on `PATH`, and not a uv tool, so the health check and init do not recognise it.

## Machine state (2026-10-27)

- No Commonplace tool environment: `~\.local\share\uv\tools\llm-commonplace` is missing, `~\.local\bin` holds only `trafilatura.exe`, and `~\.local\commonplace-shims` is gone.
- No real system Python. `python.exe` in `WindowsApps` is the Microsoft Store alias; no Store Python is installed. uv has 3.13.17, 3.14.9 and 3.15.1 under `~\.local\share\uv\python`, all unsigned.
- User variables: `UV_TOOL_DIR` is `~\.local\share\uv\tools`. User `Path` starts with `~\.local\bin`.
- Checkout: `C:\Users\zzbby\commonplace`. Test project: `C:\Users\zzbby\commonplace-kb`.

## Next: shims through a signed system Python

**Proposed procedure:** [proposed-install-procedure.md](./proposed-install-procedure.md) (2026-10-27) gives the full Windows procedure, the code and documentation changes it needs, and a verification protocol for other agents. Verifiers record their runs as new results files in this directory.

**Round 2 tests (2026-10-27):** [shim-delivery-test-plan.md](./shim-delivery-test-plan.md) tests the two deliveries side by side, shims over the signed python.org interpreter (S) and over the uv-managed interpreter (U), with a harness in [test-shims/](./test-shims/register-test-shims.ps1) that registers a shim for every entry point. It runs first on the reference machine (Smart App Control off, so antivirus results there are uninformative), then on this machine, and ends with the decision rule for `INSTALL.md`. Round 1, variant U only, is in [execution-channel-compatibility](../execution-channel-compatibility/windows-shim-test-plan.md).

Proposed by the operator on 2026-10-27. Start the commands with a Python outside the uv tool environment instead of uv's launchers or the environment's `Scripts\python.exe`.

**Operator direction (2026-10-27): Windows installs may require a system Python.** A python.org build is signed by the Python Software Foundation, so Smart App Control can trust it by signature, and antivirus should treat it better than unsigned, per-install files. The uv-managed builds are unsigned and stay a fallback only. This adds a Windows-only prerequisite, which touches the one-install-path constraint: record whether it becomes Windows troubleshooting, a Windows prerequisite with a stated reason, or a change every platform takes.

To test:

- Does Smart App Control run the signed `python.exe` every time, including the shims' `-c` launch?
- Does Avast leave it alone, with no sandboxing and no deletion, in normal use?
- Does uv build the tool environment against it with `--python <path>`, without downloading its own build?

Constraints found in the code:

- **Library location.** `_library_root()` in `src/commonplace/lib/library.py` uses the source checkout for an editable install, otherwise `sys.prefix/share/commonplace`. Under a foreign interpreter `sys.prefix` is wrong, so a non-editable install would need `COMMONPLACE_LIBRARY_ROOT`. An editable install from the checkout finds the library under any interpreter.
- **Matching versions.** Compiled dependencies such as pyyaml match one Python minor version. Build the tool environment with the interpreter the shims run: `uv tool install --python <python.exe> --editable .`.
- **Editable `.pth`.** The shim must add the tool's `Lib\site-packages` with `site.addsitedir()`, not `sys.path.insert()`, or the editable install's `.pth` file is not read.
- Open problem 4 still applies to these shims.
