# Signed system Python: first attempt, 2026-10-27

- Tester: Claude Code agent (claude-opus-5-5) in the Claude desktop app's Code tab, at the operator's request.
- Antivirus products registered in `root\SecurityCenter2`: Windows Defender, Avast Antivirus, McAfee. Smart App Control on (`VerifiedAndReputablePolicyState` 1).
- User `Path` backed up before any change. No `PATH` change was made.

## Steps

1. **Install the signed Python.** `winget install --id Python.Python.3.14 -e --source winget --scope machine` installed python.org 3.14.7 into `C:\Program Files\Python314` after one UAC prompt. The Microsoft Store was not used: the Store Python is itself a packaged app, and the `msstore` source fails certificate checks on this machine.
2. **Check it.** `python.exe` has a `Valid` Authenticode signature from the Python Software Foundation and ran (`sys.prefix` is `C:\Program Files\Python314`). Code Integrity logged no event naming Python or uv in the 30 minutes around the install. The log holds 462 events 3033 in that window, all McAfee driver loads, so filter by name when reading it.
3. **Editable tool install against it.** `uv tool install --python "C:\Program Files\Python314\python.exe" --editable C:\Users\zzbby\commonplace` (uv 0.13.5) resolved 22 packages, then failed: `failed to copy file from C:\Program Files\Python314\Lib\venv\scripts\nt\venvlauncher.exe to C:\Users\zzbby\.local\share\uv\tools\llm-commonplace\Scripts\python.exe: Access denied (os error 5)`.

## The blocked path

On a python.org base, a venv's `Scripts\python.exe` is a copy of `venvlauncher.exe`, which is itself PSF-signed. Copy tests:

- To the scratchpad as `python.exe`: ok.
- Into `llm-commonplace\Scripts\` under another name: ok.
- Into another tool directory, `tools\cp-copytest\Scripts\python.exe`: ok.
- To `llm-commonplace\Scripts\python.exe`: denied. Writing a plain text file to that exact path is also denied.

No file exists at that path (`dir /a`). Avast's quarantine (`chest\index.xml`) has no new entry, and Windows Defender has no matching detection. The path is exactly where Avast deleted `python.exe` on 2026-10-26 (open problem 3), so the likely cause is Avast blocking that path after its earlier detection. Nothing in Avast's logs names the rule, so this is an inference.

## State left

- `C:\Program Files\Python314` installed; not on `PATH`.
- `~\.local\share\uv\tools\llm-commonplace\` holds only an empty `Scripts\` plus uv's `.gitignore` and `CACHEDIR.TAG`. No launchers, no shims.

## Open

- Does the block survive a restart, or an Avast exception for the tool directory (set by the operator in Avast)?
- Then the remaining checks from the README: shims through the signed `python.exe`, and Avast's treatment of it in normal use.
