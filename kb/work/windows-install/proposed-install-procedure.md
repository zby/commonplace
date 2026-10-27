# Proposed Windows install procedure

Status: proposal, 2026-10-27. Written from one machine ([results](./results-2026-10-27-signed-python.md)) for other agents to verify before anything changes in `INSTALL.md` or the code. Each step names the evidence it rests on and what is still unverified.

## Idea

The `commonplace-*` commands fail on Windows for one reason: they start through files that are unsigned and new to the machine. Smart App Control blocks them, and antivirus sandboxes or deletes them. These are uv's launcher `.exe` files and the tool environment's own `Scripts\python.exe`.

The proposal starts every command through a signed python.org `python.exe` instead. The package goes into a plain folder rather than a uv tool environment, so no per-install `python.exe` is written. A shim per command (`.cmd` for PowerShell and cmd, `sh` for Git Bash) runs:

```text
"<signed python.exe>" -c "import site, sys; site.addsitedir(r'<package folder>'); sys.argv[0] = '<command>'; from <module> import <function>; sys.exit(<function>())"
```

## Differences from the current `INSTALL.md`

| | Current | Proposed (Windows) |
|---|---|---|
| Python | uv-managed, chosen by `--python ">=3.11"` | python.org 3.14 installed with winget; a prerequisite |
| Package location | uv tool environment, `uv tool dir` | plain folder, `%USERPROFILE%\.local\share\commonplace\site-packages` |
| Install command | `uv tool install` | `uv pip install --target` |
| Commands | uv launchers in `uv tool dir --bin` | shims in `%USERPROFILE%\.local\commonplace-shims`, on the user `Path` |
| Smart App Control workaround | optional troubleshooting | the normal path |

## Procedure

Run in PowerShell, outside any packaged app if possible (see open problem 5 in the [README](./README.md)). Paste the snippets; do not save them as `.ps1` files, which Smart App Control may restrict.

### 1. Prerequisites

```powershell
winget install --id astral-sh.uv -e --source winget
winget install --id Python.Python.3.14 -e --source winget --scope machine
```

- `--source winget` avoids the `msstore` source, which failed certificate checks on the test machine. Do not use the Microsoft Store Python: it is itself a packaged app.
- `--scope machine` puts Python in `C:\Program Files\Python314`, outside `%APPDATA%`, which packaged apps virtualise. It needs one UAC prompt. Unverified: whether a user-scope install (`%LOCALAPPDATA%\Programs\Python`) works as well from a terminal outside the app.
- Python 3.14, not 3.15: pyyaml had no cp315 wheel on 2026-10-26 (open problem 6).
- Python does not need to be on `PATH`; the shims use its full path.
- If uv fails with `UnknownIssuer`, set `UV_SYSTEM_CERTS=1` as a user variable (open problem 7).

Check: `(Get-AuthenticodeSignature 'C:\Program Files\Python314\python.exe').Status` is `Valid`, signed by the Python Software Foundation.

### 2. Install the package

Users:

```powershell
uv pip install --python "C:\Program Files\Python314\python.exe" --target "$HOME\.local\share\commonplace\site-packages" llm-commonplace
```

Development, from the checkout's root:

```powershell
uv pip install --python "C:\Program Files\Python314\python.exe" --target "$HOME\.local\share\commonplace\site-packages" -e .
```

- **The user install needs a code change first.** With `--target`, the library lands in `<package folder>\share\commonplace`. `_library_root()` in `src/commonplace/lib/library.py` looks in `sys.prefix\share\commonplace`, which under the system Python is `C:\Program Files\Python314\share\commonplace`. Proposed change: when that is missing, also try the `share\commonplace` folder next to the installed `commonplace` package (`Path(commonplace.__file__).parents[1] / "share" / "commonplace"`). The editable install is unaffected because it reads the checkout's `kb/`. Verified: the editable install only.
- uv also writes 25 unused launcher `.exe` files to `<package folder>\bin`. Delete that folder after each install, so antivirus has nothing to flag. Unverified: whether an option stops uv writing them.
- Unverified: how `--target` handles an upgrade over an existing install (`--upgrade`, or a clean folder each time).

### 3. Write the shims and put them on `PATH`

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

- `site.addsitedir`, not `sys.path.insert`: it reads the `.pth` file that makes an editable install importable.
- `$pyPosix` turns `C:\Program Files\…` into `/c/Program Files/…`; the `sh` shims quote it, so the space is safe. Verified in Git Bash.
- The `.cmd` shims pass arguments through cmd.exe, so `%`, `^` and `"` in arguments may be altered (unchanged from the current snippet).
- Rerun after every install or upgrade: a release can add or rename commands.
- Then fully restart every shell, IDE and desktop agent.

Verified on the test machine: the snippet's shim-writing part, with the shims called by full path. Not yet verified: the `PATH` step and bare names in a fresh process.

### 4. Check

In a new process, one command at a time:

```powershell
(Get-Command commonplace-validate).Source   # ends in .local\commonplace-shims\commonplace-validate.cmd
commonplace-init --help
```

```bash
command -v commonplace-validate             # ~/.local/commonplace-shims/commonplace-validate
commonplace-source --help
```

Then continue with `INSTALL.md` step 3 (`commonplace-init`).

## Code and documentation changes this needs

1. **Library location** for the user install (step 2). Required before the user install can work.
2. **`commonplace-init`'s installation warning.** `installation_warnings()` in `src/commonplace/cli/init_project.py` warns when commands resolve outside `uv tool dir --bin`. With this layout that is every command (open problem 4). It needs another way to recognise a correct install, for example: the command resolves to a shim whose package folder holds the installed `llm-commonplace`.
3. **`cp-skill-health-check`.** It looks for `llm-commonplace` in `uv tool list`, which this layout never appears in. It needs the same recognition, and the Windows symptoms from the README (Code Integrity events, `uv trampoline failed to canonicalize script path`, the blocked path).
4. **`INSTALL.md`.** Step 1 gains the Windows Python prerequisite; step 2 gains the Windows procedure; the Smart App Control section becomes background, and `Updating` gains the Windows upgrade steps.
5. **A decision on the one-install-path constraint and ADR 064** (user-level uv tool). This proposal is Windows-only. Record either that Windows gets its own path, with Smart App Control and antivirus as the reason, or that every platform moves to the same layout.

## Verification protocol for other agents

Goal: confirm or refute each "unverified" item above, on machines other than the test machine.

Before starting:

- Record Windows edition and build, whether Smart App Control is on (`(Get-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Control\CI\Policy').VerifiedAndReputablePolicyState`), the antivirus products (`Get-CimInstance -Namespace root\SecurityCenter2 -ClassName AntiVirusProduct`), and the harness (terminal, or which agent app).
- Back up the user `Path`.

While running:

- Start one command at a time. Never launch every executable in a loop: a stalled launch can hang the machine until restart.
- Never start processes through WMI or `powershell -EncodedCommand`. Avast treated that pattern as malware and deleted files.
- A process keeps the environment it started with. A check after a `PATH` change needs a fully restarted shell or app; say which.

Report, as a new `results-<date>-<machine>.md` in this workshop:

- Each step's command, exit code and any error, verbatim.
- For each "unverified" item: confirmed, refuted (with the evidence), or not tested.
- Code Integrity events 3033/3077 naming Python or `commonplace` during the run, and any antivirus quarantine, sandbox or block.
- What was left installed, and how to undo it.

Undo: remove `.local\commonplace-shims` from the user `Path`, then delete `.local\commonplace-shims` and `.local\share\commonplace`. Uninstall Python with `winget uninstall --id Python.Python.3.14` if it was installed for the test.
