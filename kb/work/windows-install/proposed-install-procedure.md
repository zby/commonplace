# Proposed Windows install procedure

Status: proposed as the primary Windows procedure, 2026-10-27. It was tested on one machine ([results](./results-2026-10-27-signed-python.md)). It must be verified by other agents before anything changes in `INSTALL.md` or the code.

## Summary

- **uv still installs the package and its dependencies**, with `uv pip install --target` into a plain folder instead of `uv tool install`.
- **The commands run through the signed system Python**: python.org 3.14, installed with winget. A shim per command starts it and loads the package folder.
- **The shim folder must be added to the user `PATH`.**
- **A fresh shell, or a full app restart, is required afterwards.** A running process keeps its old `PATH`.
- **The released-package (non-editable) layout still needs a code fix and a test.** Only the editable development install works today.
- **Fallback:** users who keep the original `uv tool` layout add an antivirus exception for the uv tool folder and use the existing `INSTALL.md` Smart App Control shims.

## Why

The commands fail on Windows because they start through files that are unsigned and new to each machine. These are uv's launcher `.exe` files and the tool environment's own `Scripts\python.exe`. Smart App Control blocks them, and antivirus sandboxes or deletes them. A python.org `python.exe` is signed by the Python Software Foundation and identical on every machine, so Smart App Control can trust it. No per-install executable is written or run.

## What is verified

On the test machine: Windows 11 Home, Smart App Control on, Avast, McAfee and Defender registered.

| Item | State |
|---|---|
| python.org 3.14.7 via winget, `--scope machine`; valid PSF signature; runs | verified |
| No Code Integrity or Avast reaction to the signed Python or the shims | verified, one session |
| Editable install with `uv pip install --target` | verified |
| Shims in PowerShell and Git Bash, called by full path | verified |
| Shim folder on the user `PATH`; bare names in a fresh process | not tested |
| Released-package install | fails until code change 1 below |
| Per-user Python install (`%LOCALAPPDATA%\Programs\Python`) | not tested |
| Upgrading in place with `--target` | not tested |
| Deleting uv's unused `bin\` launchers in the snippet | not tested |
| Avast in normal use over several days | not tested |
| Fallback: antivirus exception with the `uv tool` layout | not tested |

## Procedure

Run in PowerShell, outside any packaged app if possible ([README](./README.md), open problem 5). Paste the snippets; do not save them as `.ps1` files, which Smart App Control may restrict.

### 1. Prerequisites

```powershell
winget install --id astral-sh.uv -e --source winget
winget install --id Python.Python.3.14 -e --source winget --scope machine
```

- `--source winget` avoids the `msstore` source, which failed certificate checks on the test machine. Do not use the Microsoft Store Python: it is itself a packaged app.
- `--scope machine` installs into `C:\Program Files\Python314`, outside `%APPDATA%`, which packaged apps virtualise. It needs one UAC prompt.
- Use 3.14, not 3.15: pyyaml had no cp315 wheel on 2026-10-26 (open problem 6).
- Python does not need to be on `PATH`; the shims use its full path.
- If uv fails with `UnknownIssuer`, set `UV_SYSTEM_CERTS=1` as a user variable (open problem 7).

Check: `(Get-AuthenticodeSignature 'C:\Program Files\Python314\python.exe').Status` is `Valid`, signed by the Python Software Foundation.

### 2. Install the package with uv

Development, from the checkout's root (verified):

```powershell
uv pip install --python "C:\Program Files\Python314\python.exe" --target "$HOME\.local\share\commonplace\site-packages" -e .
```

Users (blocked until code change 1):

```powershell
uv pip install --python "C:\Program Files\Python314\python.exe" --target "$HOME\.local\share\commonplace\site-packages" llm-commonplace
```

uv also writes 25 launcher `.exe` files to `<package folder>\bin`. Nothing uses them; the snippet in step 3 deletes them so antivirus has nothing to flag.

### 3. Write the shims and add them to the user `PATH`

```powershell
& {
  $py = 'C:\Program Files\Python314\python.exe'
  $site = Join-Path $HOME '.local\share\commonplace\site-packages'
  if (-not (Test-Path $py)) { throw "No Python at $py." }
  $dist = Get-ChildItem "$site\llm_commonplace-*.dist-info" -ErrorAction SilentlyContinue
  if (-not $dist) { throw "No llm-commonplace in $site." }
  $pyPosix = '/' + $py.Substring(0,1).ToLower() + $py.Substring(2).Replace('\','/')
  $shims = Join-Path $HOME '.local\commonplace-shims'
  New-Item -ItemType Directory -Force $shims | Out-Null
  Remove-Item "$site\bin" -Recurse -Force -ErrorAction SilentlyContinue
  foreach ($line in Get-Content "$($dist.FullName)\entry_points.txt") {
    if ($line -match '^(commonplace-\S+) = ([\w.]+):(\w+)$') {
      $name, $mod, $fn = $Matches[1], $Matches[2], $Matches[3]
      $code = "import site, sys; site.addsitedir(r'$site'); sys.argv[0] = '$name'; from $mod import $fn; sys.exit($fn())"
      [IO.File]::WriteAllText("$shims\$name.cmd", "@`"$py`" -c `"$code`" %*`r`n")
      [IO.File]::WriteAllText("$shims\$name", "#!/bin/sh`nexec `"$pyPosix`" -c `"$code`" `"`$@`"`n")
    }
  }
  $userPath = [Environment]::GetEnvironmentVariable('Path', 'User')
  if (($userPath -split ';') -notcontains $shims) {
    [Environment]::SetEnvironmentVariable('Path', "$shims;$userPath", 'User')
  }
  "Wrote $((Get-ChildItem "$shims\*.cmd").Count) shims to $shims"
}
```

- Each shim runs `"<python.exe>" -c "import site, sys; site.addsitedir(r'<package folder>'); sys.argv[0] = '<command>'; from <module> import <function>; sys.exit(<function>())"`. There is a `.cmd` for PowerShell and cmd, and an `sh` script for Git Bash.
- `site.addsitedir`, not `sys.path.insert`: it reads the `.pth` file that makes an editable install importable.
- The `.cmd` shims pass arguments through cmd.exe, so `%`, `^` and `"` in arguments may be altered. Git Bash passes them unchanged.
- Rerun the snippet after every install or upgrade: a release can add or rename commands.

### 4. Restart

Fully restart every shell, IDE and desktop agent that will use the commands. A process started before step 3 keeps its old `PATH`.

### 5. Check

In a new process, one command at a time:

```powershell
(Get-Command commonplace-validate).Source   # ends in .local\commonplace-shims\commonplace-validate.cmd
commonplace-init --help
```

```bash
command -v commonplace-validate             # ~/.local/commonplace-shims/commonplace-validate
commonplace-source --help
```

Then continue with `INSTALL.md` step 3 (`commonplace-init`). A project initialised against another install reports `stale` from `commonplace-init --check` until init is rerun.

## Fallback: keep the `uv tool` layout

For users who keep `uv tool install` as in the current `INSTALL.md`:

1. Add an antivirus exception for the uv tool folder (`uv tool dir`; on the test machine `C:\Users\zzbby\.local\share\uv\tools\`). Without it, Avast sandboxed the launchers, deleted `Scripts\python.exe`, and then blocked that path from being written again.
2. Use the existing Smart App Control shims in `INSTALL.md`, which start the tool environment's `Scripts\python.exe`. With a python.org base, that file is a copy of python.org's signed `venvlauncher.exe`; with a uv-managed base, its signature was not checked. Building the tool with `--python "C:\Program Files\Python314\python.exe"` is therefore likely the better fallback.

Not tested. It is the user's decision to change antivirus settings; the procedure should say how, not do it.

## Code and documentation changes needed

1. **Library location for the released package.** With `--target`, the library lands in `<package folder>\share\commonplace`. `_library_root()` in `src/commonplace/lib/library.py` looks in `sys.prefix\share\commonplace`, which under the system Python is `C:\Program Files\Python314\share\commonplace`. Proposed: when that is missing, also try the `share\commonplace` folder next to the installed package (`Path(commonplace.__file__).parents[1] / "share" / "commonplace"`). The editable install is unaffected because it reads the checkout's `kb/`.
2. **`commonplace-init`'s installation warning.** `installation_warnings()` in `src/commonplace/cli/init_project.py` warns when commands resolve outside `uv tool dir --bin`, which with this layout is every command (open problem 4). It needs to recognise a shim whose package folder holds the installed `llm-commonplace`.
3. **`cp-skill-health-check`.** It looks for `llm-commonplace` in `uv tool list`, where this layout never appears. It needs the same recognition, plus the Windows symptoms in the README: Code Integrity events, `uv trampoline failed to canonicalize script path`, and the blocked path.
4. **Workjig on Windows** (open problem 10). `commonplace-task`, `commonplace-analysis` and the headless runners crash on the `fcntl` import whatever the install layout.
5. **`INSTALL.md`.** Step 1 gains the Windows Python prerequisite. Step 2 gains this procedure as the Windows path, with the `uv tool` layout and its antivirus exception as the fallback. The Smart App Control section shrinks to background. `Updating` gains the Windows upgrade steps.
6. **A decision on the one-install-path constraint and ADR 064** (user-level uv tool). This procedure is Windows-only. Record either that Windows gets its own path, with Smart App Control and antivirus as the reason, or that every platform moves to the same layout.

## Verification protocol for other agents

Goal: turn each "not tested" row in [What is verified](#what-is-verified) into verified or refuted, on machines other than the test machine.

Before starting:

- Record Windows edition and build, whether Smart App Control is on (`(Get-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Control\CI\Policy').VerifiedAndReputablePolicyState`, 1 means on), the antivirus products (`Get-CimInstance -Namespace root\SecurityCenter2 -ClassName AntiVirusProduct`), and the harness (terminal, or which agent app).
- Back up the user `Path`.

While running:

- Start one command at a time. Never launch every executable in a loop: a stalled launch can hang the machine until restart.
- Never start processes through WMI or `powershell -EncodedCommand`. Avast treated that pattern as malware and deleted files.
- After a `PATH` change, check in a fully restarted shell or app, and say which.

Report, as a new `results-<date>-<machine>.md` in this workshop:

- Each step's command, exit code and any error, verbatim.
- For each row tested: verified or refuted, with the evidence.
- Code Integrity events 3033/3077 naming Python or `commonplace` during the run, and any antivirus quarantine, sandbox or block.
- What was left installed, and how to undo it.

Undo: remove `.local\commonplace-shims` from the user `Path`, then delete `.local\commonplace-shims` and `.local\share\commonplace`. Uninstall Python with `winget uninstall --id Python.Python.3.14` if it was installed only for the test.
