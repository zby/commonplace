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

## Without a virtual environment

The shims start the signed `python.exe` directly, so the tool needs no `Scripts\python.exe` of its own. `uv tool install` always builds a virtual environment, and so always writes that file. The package went into a plain folder instead:

```text
uv pip install --python "C:\Program Files\Python314\python.exe" --target C:\Users\zzbby\.local\share\commonplace\site-packages -e C:\Users\zzbby\commonplace
```

It installed 22 packages, including the editable `llm-commonplace` 0.3.0. The folder holds `_editable_impl_llm_commonplace.pth`, which points at the checkout, and a `bin\` of 25 uv launcher `.exe` files that nothing uses.

The `INSTALL.md` shim snippet was adapted and run once. It wrote 25 shims to `~\.local\commonplace-shims`, each a `.cmd` and an `sh` script running:

```text
"C:\Program Files\Python314\python.exe" -c "import site, sys; site.addsitedir(r'<target>'); sys.argv[0] = '<name>'; from <module> import <fn>; sys.exit(<fn>())"
```

`site.addsitedir` is required: it reads the `.pth` file that makes the editable install importable. The library is found through the checkout, so `sys.prefix` being the system Python's does not matter. The user `Path` was not changed; the shims were called by full path, one at a time:

- PowerShell: `commonplace-init --help` (exit 0); `commonplace-validate kb/work/windows-install/README.md` in the checkout (exit 0, no failures).
- Git Bash: `commonplace-source --help` (exit 0); `commonplace-validate` on this file (exit 0, no failures).
- `commonplace-init --check` in `C:\Users\zzbby\commonplace-kb`: exit 1, every stub, `library.md` and the read rule `stale`. Expected: that project was initialised against the PyPI 0.3.0 install, and the editable install moves the library root to the checkout's `kb/`. Not rerun; it is a separate project.

Afterwards, Code Integrity had no event naming Python or Commonplace. Avast's quarantine index and Auto-Sandbox log were unchanged since 2026-10-26.

## State left

- `C:\Program Files\Python314` installed; not on `PATH`.
- Package in `~\.local\share\commonplace\site-packages`; shims in `~\.local\commonplace-shims`; neither on `PATH`.
- `~\.local\share\uv\tools\llm-commonplace\` holds only an empty `Scripts\` plus uv's `.gitignore` and `CACHEDIR.TAG`. The blocked path is unresolved, but this layout does not need it.

## Open

- Put the shims on the user `Path`, restart the app, and check bare names in a fresh process.
- Rerun `commonplace-init` in `commonplace-kb`, then `--check`.
- This layout is not a uv tool, so `uv tool list`, `cp-skill-health-check` and `commonplace-init`'s shadowing warning do not recognise it (open problem 4 widens). Decide whether the install model changes (ADR 064) or the layout returns to a uv tool once the blocked path is cleared.
- Watch Avast in normal use over several days.
- Moving the checkout: rerun the `uv pip install … -e <new path>` command; the shims do not name the checkout.
