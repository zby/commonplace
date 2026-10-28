# INSTALL.md Windows procedure, followed as written: afflicted machine (stopped at step 1)

- Procedure: `INSTALL.md` as a new user reads it, Windows path: step 1 prerequisites and checks, step 2 Windows command with `--python 'C:\Program Files\Python314\python.exe'`, `uv tool update-shell`, the shim snippet from "Windows: Smart App Control blocks the commands", verification, then a test KB with `commonplace-init`.
- Package: the published `llm-commonplace`, user-level uv tool, overwriting a tool that `uv tool list` reports as malformed.
- Machine: this machine (Windows 11 Home 10.0.26300), Smart App Control on (`VerifiedAndReputablePolicyState` = 1). Antivirus in `root\SecurityCenter2`: Windows Defender, Avast Antivirus, McAfee.
- Runtime: Claude Code agent inside the Claude desktop app; Windows PowerShell 5.1.26100.
- Run: 2026-10-28, 13:54–13:57 local. `RunStart` for `avcheck.ps1` = 13:54:00, pattern `commonplace|Python314|\uv|cp-install-test` (plus `trafilatura|\.local` for the hang diagnosis).
- **Outcome: stopped in step 1.** The `trafilatura --version` prerequisite check did not return within 30 seconds, and the testing rules say to stop at a launch that hangs over 30 seconds. Steps 2–6 were not run. Nothing persistent was changed.

## Results

| Step | Command | Exit | Antivirus records | Result |
|---|---|---|---|---|
| Backup | user `Path` and user `UV_TOOL_DIR` printed and saved to a scratchpad `env-backup.txt` | 0 | — | **done**; values under "State left behind" |
| AV baseline | `Get-CimInstance root\SecurityCenter2 AntiVirusProduct`; SAC policy state | 0 | — | Defender, Avast, McAfee; SAC = 1 |
| 1 `uv` | `uv --version` | 0 | none | **pass**: uv 0.13.5 |
| 1 `git` | `git --version` | 0 | none | **pass**: 2.56.0.windows.3 |
| 1 `rg` | `rg --version` | 0 | none | **pass**: 15.2.0 |
| 1 `curl` | `curl --version`, exactly as written | error | none | **fail as written**: in Windows PowerShell 5.1 `curl` is an alias of `Invoke-WebRequest`, which treats `--version` as a host name ("cannot resolve the remote name '--version'"). `curl.exe --version` → 0, curl 8.21.0 (Schannel). Doc gap 1 |
| 1 `trafilatura` | `trafilatura --version` (resolves to `<HOME>\.local\bin\trafilatura.exe`), run in a job with a 30 s wait | none (timed out) | **Avast 13:54:37**: autosandbox candidate `trafilatura.exe` → "Not sandboxing (file is in the exception list)". **Code Integrity 3077 + 3033 at 13:55:12**: uv-managed `cpython-3.15.1\python.exe` refused `DLLs\_multiprocessing.pyd` (did not meet Enterprise signing level) | **hang > 30 s; run stopped here.** The process did not linger: it ended with the job's shell, and no `trafilatura` or `python` process remained. The tool's `pyvenv.cfg` has `home = <HOME>\.local\share\uv\python\cpython-3.15.1-windows-x86_64-none`, an unsigned uv-managed build. Doc gap 2 |
| 1 `pdfinfo`, `pdftotext` | not run | — | — | not reached |
| 1 signature | `Get-AuthenticodeSignature 'C:\Program Files\Python314\python.exe'` (a cmdlet, not a launch; run read-only after the stop) | — | — | `Valid`, `CN=Python Software Foundation` |
| 2 install, `update-shell`, shim snippet | not run | — | — | not reached |
| 5 verification, probe | not run | — | — | not reached |
| 6 test KB | not run | — | — | not reached; `<HOME>\cp-install-test-2026-10-28` not created |

`avcheck.ps1` summary at 13:55: `CI any=2 named=2; Defender det=0 ev=0; Avast chest=5 sandbox-new=1`. Both CI records and the one Avast record are the trafilatura launch above. A `pre-step-2` observation was not taken because step 2 was not reached.

## Doc gaps

1. **`curl --version` fails in Windows PowerShell 5.1** (`INSTALL.md` §1 "Check prerequisites", Windows PowerShell block, line `curl --version`). PowerShell 5.1, the default `powershell.exe` on Windows 11, aliases `curl` to `Invoke-WebRequest`. The Windows block should say `curl.exe --version`. `cp-skill-snapshot-web` may have the same issue if it calls `curl` from PowerShell; not checked.
2. **The trafilatura prerequisite is installed over a uv-managed, unsigned interpreter, and Smart App Control blocks it** (`INSTALL.md` §1 "Required", the Trafilatura bullet: `uv tool install "trafilatura>=2.2"`). On Windows that command picks a uv-managed CPython, here 3.15.1, the same thing the next bullet's signed-Python prerequisite exists to avoid. On this machine Code Integrity refused its `_multiprocessing.pyd`, and the version check did not return within 30 s. The doc applies the signed-interpreter reasoning only to Commonplace. On Windows it should also install Trafilatura with `--python 'C:\Program Files\Python314\python.exe'`, which means listing the python.org bullet before the Trafilatura bullet. The check `trafilatura --version` also starts an unsigned uv launcher in `.local\bin`, the hazard that "Windows: Smart App Control blocks the commands" describes for Commonplace's launchers, and the doc offers no shim or other remedy for it. The troubleshooting section names only `commonplace-*` commands, so a user whose prerequisite check hangs has no entry that applies.
3. **The prerequisite check gives no guidance on hangs** (`INSTALL.md` §1 "Check prerequisites": "If any required tool is missing, install it before continuing"). The check assumes that a tool is either present or missing. On Windows with Smart App Control, a present tool can hang or be refused. The warning "Do not test the install by launching every executable in a loop" appears only at the end of troubleshooting, but the prerequisite block is itself a list of first launches that a user will paste in one go.

Not reached, so not assessed: the malformed-tool remedy (the doc names `--reinstall` under "Third-party antivirus" and `uv tool uninstall` under "Updating", and warns against `--force` as a default under "Bare name resolves elsewhere"), the "Antivirus blocks the tool environment's path" entry, whether the snippet handles a shims dir that exists but is not on `Path`, and `commonplace-init`/`commonplace-validate` on a new KB.

## State left behind

- User `Path`: unchanged. Before and after: `<HOME>\.local\bin; <HOME>\AppData\Local\Microsoft\WindowsApps; …WinGet\Packages\astral-sh.uv_…; …WinGet\Packages\BurntSushi.ripgrep.MSVC_…\ripgrep-15.2.0-…; …WinGet\Packages\oschwartz10612.Poppler_…\poppler-25.07.0\Library\bin;` (verified by comparing with the backup after the stop).
- User `UV_TOOL_DIR`: unchanged, `<HOME>\.local\share\uv\tools` before and after. User `UV_TOOL_BIN_DIR`: unset.
- Tool dir `<HOME>\.local\share\uv\tools`: untouched. It holds `llm-commonplace` (last written 2026-10-27, no `Scripts\python.exe`, still malformed) and `trafilatura`.
- Shims dir `<HOME>\.local\commonplace-shims`: untouched, 50 entries, not on the user `Path`.
- Test KB: not created.
- Backup file: `env-backup.txt` in the session scratchpad, outside the checkout.

## Disclosure review

Local identifiers normalized (`<HOME>`). No secrets. The user `Path` above is abridged to directory names already recorded in this workshop.
