# INSTALL.md Windows procedure, followed as written: afflicted machine (run 2)

- Procedure: `INSTALL.md` as a new user reads it, Windows path, using the uncommitted working-tree text of 2026-10-28 ~14:10. Since [run 1](./results-2026-10-28-afflicted-install-md.md), Trafilatura has moved under "### Optional" and out of the checks, the Windows block uses `curl.exe --version`, and a note says to run the checks one at a time. Steps covered: step 1 checks, step 2 Windows install, `uv tool update-shell`, the shim snippet from "Windows: Smart App Control blocks the commands", verification, and step 3 (`commonplace-init`, `--check`, `commonplace-validate landings`). Steps 4–6 (control plane, skills in a runtime, runtime restart) were out of scope.
- Package: the published `llm-commonplace` 0.3.1, as a user-level uv tool, replacing a tool that `uv tool list` reported as malformed (`Scripts\python.exe` missing since Avast's earlier action).
- Machine: as in run 1. Windows 11 Home 10.0.26300, Smart App Control on (`VerifiedAndReputablePolicyState` = 1). Antivirus in `root\SecurityCenter2`: Windows Defender, Avast Antivirus, McAfee.
- Runtime: Claude Code agent inside the Claude desktop app; Windows PowerShell 5.1. Trafilatura was not run or changed.
- Run: 2026-10-28, 14:12–14:15 local. `RunStart` = 14:12:00 for every `avcheck.ps1` call, pattern `commonplace|Python314|\uv|cp-install-test`.
- Before changing anything, the user `Path` and user `UV_TOOL_DIR` were compared with the run 1 backup. Both matched.
- **Outcome: pass, with doc gaps.** The tool installed at the default tool path over the signed interpreter. All 25 shims were written and put on the user `Path`, all 21 stdlib extensions loaded from `C:\Program Files\Python314\DLLs`, and the new project initialised, checked and validated through the shims. No Code Integrity, Defender or Avast record in the whole run.

## Results

| Step | Command | Exit | Antivirus records | Result |
|---|---|---|---|---|
| Env check | compare the user `Path` and `UV_TOOL_DIR` with `env-backup.txt` | — | baseline: none | **match**, both |
| 1 `uv` | `uv --version` | 0 | none | **pass**: 0.13.5 |
| 1 `git` | `git --version` | 0 | none | **pass**: 2.56.0.windows.3 |
| 1 `rg` | `rg --version` | 0 | none | **pass**: 15.2.0 |
| 1 `curl` | `curl.exe --version` | 0 | none | **pass**: 8.21.0. The run 1 gap is fixed |
| 1 `pdfinfo` | `pdfinfo -v` (first launch, through `Start-Process` with a 30 s wait) | 0 | none | **pass**: 25.07.0, 90 ms. Poppler writes the version to stderr, so PowerShell shows a `NativeCommandError` when stderr is merged; cosmetic |
| 1 `pdftotext` | `pdftotext -v` (first launch, 30 s wait) | 0 | none | **pass**: 25.07.0, 35 ms |
| 1 signature | `Get-AuthenticodeSignature 'C:\Program Files\Python314\python.exe'` | — | — | **pass**: `Valid`, `CN=Python Software Foundation` |
| Pre-step-2 state | `uv tool list`; `uv tool dir`; `uv tool dir --bin` | 0 | `avcheck` before step 2: `CI any=0 named=0; Defender det=0 ev=0; Avast chest=5 sandbox-new=0` | warns ``Ignoring malformed tool `llm-commonplace` (run `uv tool uninstall llm-commonplace` to remove)``; tool dir `<HOME>\.local\share\uv\tools`, bin `<HOME>\.local\bin` |
| 2 install, as written | `uv tool install --python 'C:\Program Files\Python314\python.exe' llm-commonplace` | **2** | none | **fail**: ``Invalid environment at `<HOME>\.local\share\uv\tools\llm-commonplace`: missing Python executable at `…\Scripts\python.exe` ``. Doc gap 1 |
| 2 `--reinstall` | the same command plus `--reinstall`. The doc's nearest remedy is the "Third-party antivirus" entry: antivirus "delete[s] files from the tool environment … repair … with `--reinstall`" | **2** | none | **fail**: the same error. Doc gap 1 |
| 2 uninstall | `uv tool uninstall llm-commonplace`. Taken from uv's own warning; the doc names this command only under "Updating", for switching editable ↔ published | 0 | none | **pass**: "Removed dangling environment for `llm-commonplace`" |
| 2 install | `uv tool install --python 'C:\Program Files\Python314\python.exe' llm-commonplace` | 0 | none | **pass**: 22 packages, 25 executables. `Scripts\python.exe` is `Valid`, signed by the PSF. `pyvenv.cfg` has `home = C:\Program Files\Python314`, version 3.14.7. **No `Access denied` at the default path**, so the "Antivirus blocks the tool environment's path" entry and a new `UV_TOOL_DIR` were not needed. Observation 1 |
| 2 `update-shell` | `uv tool update-shell` | 0 | none | **pass**: "Executable directory `<HOME>\.local\bin` is already in PATH"; no change |
| Shims | the snippet, pasted unchanged into PowerShell | ok | `avcheck` after: all zero | **pass**: "Wrote 25 shims to `<HOME>\.local\commonplace-shims`". All 50 files (25 `.cmd` + 25 `sh`) rewritten at 14:13:33. The snippet **added the existing, off-`Path` shims dir to the front of the user `Path`**, as intended |
| 5 base executable | first launch of the tool interpreter: `& (Join-Path (uv tool dir) 'llm-commonplace\Scripts\python.exe') -c "import sys; print(sys._base_executable)"` (`Start-Process`, 30 s wait) | 0 | none | **pass**: `C:\Program Files\Python314\python.exe`, 65 ms |
| 5 probe | `<tool python.exe> -I kb\work\windows-signed-python-field-use\pyd-probe.py` | 0 | none | **pass**: 21 of 21 loaded, all from `C:\Program Files\Python314\DLLs` |
| 5 resolution | fresh `powershell -NoProfile` child, with `$env:Path` rebuilt from the registry as Machine + User (the usual order for a new process), then `uv tool dir --bin`; `(Get-Command commonplace-validate).Source`; `commonplace-init --help` | 0, 0 | `avcheck` after: all zero | **pass**: source `<HOME>\.local\commonplace-shims\commonplace-validate.cmd`. `Get-Command -All` lists the `.cmd`, the `sh` shim, then `<HOME>\.local\bin\commonplace-validate.exe`. `--help` prints the usage, 553 ms for the whole child. Method: a plain child process inherits this agent's stale environment, so the child read `Path` from the registry; no app restart |
| 3 init | in a fresh child (same `Path` method), `Set-Location <HOME>\cp-install-test-2026-10-28; commonplace-init --name cp-install-test` | 0 | none | **pass**: created `kb\…` (all collections and heads), both templates, 12 + 12 skill stubs, `.commonplace\library.md`, `.gitignore`, `.claude\settings.local.json`. Printed the expected "resolve outside uv's tool executable directory" diagnostic for all 25 commands, ending with "Remove or reorder the shadowing PATH entry". Doc gap 4 |
| 3 `--check` | `commonplace-init --check` | 0 | none | **pass**: 26 × `ok` (24 stubs, `library.md`, read rule) |
| 3 validate | `commonplace-validate landings` | 0 | none | **pass**: `VALIDATION SUCCESS`, 0 failures, 0 warnings. It reported "Files analysed: 1, Text files: 0" with 8 landing `README.md` files present; not investigated. Observation 2 |
| 3 search | `rg "collection" kb/ --glob "*.md"` | 0 | none | **pass**: hits in the landings |
| Final | `avcheck.ps1` at 14:14:55 | 0 | `CI any=0 named=0; Defender det=0 ev=0; Avast chest=5 sandbox-new=0` | clean for the whole run |

Test KB location: the brief named `<HOME>\cp-install-test-2026-10-28\kb`. Step 3 runs `commonplace-init` from the project root and creates `kb\` itself, so the project root is `<HOME>\cp-install-test-2026-10-28` and the KB is at the named `kb\` path.

Deviation: the four already-launched checks (`uv`, `git`, `rg`, `curl.exe`) were sent as parallel tool calls, not strictly one at a time as the new note asks. Each executable had already been started once in run 1, and none hung. The first launches in this run (`pdfinfo`, `pdftotext`, the tool's `python.exe`, the shims) were run one at a time, each with a 30 s wait.

## Doc gaps

1. **No remedy for a malformed tool or a missing `Scripts\python.exe`** ("Troubleshooting command discovery" and "Windows: Smart App Control blocks the commands", entry "Third-party antivirus"). After Avast removed the tool's `python.exe`:
   - `uv tool list` warns "Ignoring malformed tool".
   - The step 2 command fails with exit 2: `Invalid environment … missing Python executable`.
   - The doc's only antivirus repair, rerunning step 2 with `--reinstall`, fails the same way.

   Only `uv tool uninstall llm-commonplace` followed by the step 2 command worked. The doc mentions `uninstall` only under "Updating". The "Third-party antivirus" entry should cover this symptom and give uninstall then install, or the troubleshooting list should gain a "Tool listed as malformed / Invalid environment" item. `--force` was not tried; "Bare name resolves elsewhere" discourages it as a default.
2. **The step 2 check contradicts the Windows shims** (§2 "Check the commands run": "The resolved command should be inside the directory printed by `uv tool dir --bin`"). On Windows, with the required shims, it resolves to `.local\commonplace-shims`. The exception is stated only in the troubleshooting section. A user following step 2 in order reads a failure. The check should carry a Windows clause.
3. **No `git init` for a new project** (§3, and §1's "Normal KB maintenance is expected to happen under version control"). The doc says the KB is versioned and that the control-plane files are committed (§4), but no step creates the repository. `commonplace-init` does not need one: it ran and passed `--check` in a folder that is not a repository, and writes a `.gitignore` anyway. Per the brief, no repository was created in this run.
4. **`commonplace-init`'s shim diagnostic tells the user to undo the shims.** The doc says the report is expected (Smart App Control section: "`commonplace-init` reports each command as resolving outside uv's tool executable directory … With these shims, that is expected"). But the command's own text ends "Remove or reorder the shadowing PATH entry; do not use uv tool install --force as the default repair", and a user sees that before they find the doc's note. This is open problem 4 (a code fix). Until it lands, §3 could mention it where init is first run.
5. **The "one at a time" note sits below a block designed for pasting** (§1 "Check prerequisites"). The note is right, but the block is still one paste-able unit. Minor: one block per line, or a sentence before the block, would match the instruction.

## Observations

1. **Avast did not block the default tool path this time.** Run t2 found 2 had attributed `Access denied` at `…\uv\tools\llm-commonplace\Scripts\python.exe` to a leftover block from 2026-10-26. At 14:13 the install wrote that exact file with no error and no Avast record. The block has lapsed or is intermittent. So the "Antivirus blocks the tool environment's path" entry was not exercised, and the doc did not need to lead there.
2. **`commonplace-validate landings` reported "Files analysed: 1, Text files: 0"** on a fresh scaffold with 8 landing READMEs. It passed; whether it counts one subject (the landing set) or skipped files was not checked.
3. **`uv tool update-shell` was a no-op**, because `<HOME>\.local\bin` was already on the user `Path` from the earlier install.

## State left behind

- User `Path`. Before (matches the run 1 backup): `<HOME>\.local\bin; <HOME>\AppData\Local\Microsoft\WindowsApps; …WinGet\Packages\astral-sh.uv_…; …\ripgrep-15.2.0-…; …\poppler-25.07.0\Library\bin;`. After: **`<HOME>\.local\commonplace-shims` prepended** by the snippet; the rest is unchanged.
- User `UV_TOOL_DIR`: `<HOME>\.local\share\uv\tools` before and after, unchanged. User `UV_TOOL_BIN_DIR`: unset.
- Tool dir: the malformed `llm-commonplace` was removed by `uv tool uninstall`. A new `<HOME>\.local\share\uv\tools\llm-commonplace` (0.3.1, over the signed python.org 3.14.7) was installed, with 25 launchers in `<HOME>\.local\bin`. `trafilatura` is untouched.
- Shims dir `<HOME>\.local\commonplace-shims`: 50 files rewritten (25 `.cmd`, 25 `sh`), now on the user `Path`.
- Test project `<HOME>\cp-install-test-2026-10-28` (KB at `…\kb`): scaffold, templates, stubs, `.commonplace\library.md`, `.gitignore`, `.claude\settings.local.json`. Not a git repository. `AGENTS.md.template` and `CLAUDE.md.template` are not renamed (step 4 was not run).
- Backup: `env-backup.txt` in the session scratchpad, from run 1, still valid for restoring the pre-run `Path`.
- Checkout: only this report was added. Nothing committed.

## Disclosure review

Local identifiers normalized (`<HOME>`). No secrets. The user `Path` is abridged to directory names already recorded in this workshop.
