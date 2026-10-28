# INSTALL.md Windows procedure, followed as written: afflicted machine (run 3)

- Procedure: `INSTALL.md` at committed HEAD `9874c8dfe` ("Require Git as the KB's version-control system"), Windows path, read fresh before looking at runs 1 and 2. Steps covered: step 1 checks, including the optional Trafilatura entry with its Windows reinstall; step 2 Windows install over an existing install, `uv tool update-shell`, the shim snippet, and the step 2 check; step 3 (`git rev-parse`, `git init`, `commonplace-init`, `--check`, `commonplace-validate landings`, `rg`); step 4 (template rename, first commit); the step 5 `--check`. Step 6 and the in-runtime parts of step 5 were not run, because they need an agent runtime restart.
- Package: the published `llm-commonplace` 0.3.1, a user-level uv tool, reinstalled over a healthy 0.3.1 that run 2 had left over the signed interpreter.
- Machine: as in runs 1 and 2. Windows 11 Home 10.0.26300, with Smart App Control on. Windows Defender, Avast and McAfee are registered.
- Runtime: Claude Code agent inside the Claude desktop app; Windows PowerShell 5.1.26100.
- Run: 2026-10-28, 14:30–14:34 local. `RunStart` was 14:29:59 for every `avcheck.ps1` call, with pattern `commonplace|Python314|\uv|trafilatura|cp-install-test`.
- Fresh-process method: this agent's own process keeps its startup environment. Every check marked "fresh child" ran in `powershell -NoProfile -Command` with `$env:Path` rebuilt from the registry as Machine + User. The app was not restarted.
- **Outcome: pass, with doc gaps.** Every step that was run passed.
  - Trafilatura, reinstalled over the signed interpreter, launched in 2.9 s. Avast lists `trafilatura.exe` as excepted, which confounds this result (observation 1).
  - The reinstall, update-shell and shims worked. The tool interpreter is PSF-signed, and all 21 stdlib extensions loaded.
  - The test project initialised, checked, validated and committed.
  - No Code Integrity or Defender record appeared in the whole run. Avast logged one record, an exception.

## Results

| Step | Command | Exit | Antivirus records | Result |
|---|---|---|---|---|
| Backup | user `Path` and `UV_TOOL_DIR` printed and saved to scratchpad `env-backup-run3.txt` | 0 | — | **done**; values under "State left behind" |
| 1 `uv` | `uv --version` | 0 | none | **pass**: 0.13.5 |
| 1 `git` | `git --version` | 0 | none | **pass**: 2.56.0.windows.3. The `uv` and `git` checks were issued in parallel by mistake (deviation 1) |
| 1 `rg` | `rg --version` | 0 | none | **pass**: 15.2.0 |
| 1 `curl` | `curl.exe --version` | 0 | none | **pass**: 8.21.0 |
| 1 `pdfinfo` | `pdfinfo -v` | 0 | none | **pass**: 25.07.0 |
| 1 `pdftotext` | `pdftotext -v` | 0 | none | **pass**: 25.07.0 |
| 1 signature | `(Get-AuthenticodeSignature 'C:\Program Files\Python314\python.exe') \| Select-Object Status, @{n='Signer';…}` | — | — | **pass**: `Valid`, `CN=Python Software Foundation` |
| 1 Trafilatura state | `uv tool list --show-paths --show-python` | 0 | none | `trafilatura v2.3.1 [CPython 3.15.1]`, i.e. over uv-managed 3.15.1 as in run 1 |
| 1 Trafilatura reinstall | `uv tool install --reinstall --python 'C:\Program Files\Python314\python.exe' "trafilatura>=2.2"` (the doc's Windows command plus `--reinstall`, as "If it is already installed over another interpreter, add `--reinstall`" says) | 0 | none | **pass**: "Ignoring existing environment for `trafilatura`: the requested Python interpreter does not match", 18 packages, 4 s. `Scripts\python.exe` is `Valid`, signed by the PSF; `pyvenv.cfg` `home = C:\Program Files\Python314`, 3.14.7. `<HOME>\.local\bin\trafilatura.exe` is `NotSigned`, as the doc warns |
| 1 Trafilatura launch | `trafilatura --version` (resolves to `<HOME>\.local\bin\trafilatura.exe`), `Start-Process` with `WaitForExit(30000)` | not captured (blank `ExitCode`, a known `Start-Process -NoNewWindow` quirk) | **Avast 14:30:51**: autosandbox candidate `trafilatura.exe` → "Not sandboxing (because the file is in the exception list)". No CI record | **pass**: `Trafilatura 2.3.1 - Python 3.14.7` in 2.9 s, no hang. Observation 1 |
| AV before step 2 | `avcheck.ps1` | 0 | `CI any=0 named=0; Defender det=0 ev=0; Avast chest=5 sandbox-new=1` | the one Avast record is the Trafilatura launch above |
| 2 install, as written | `uv tool install --python 'C:\Program Files\Python314\python.exe' llm-commonplace` | 0 | none | **no-op**: "`llm-commonplace` is already installed"; nothing replaced. Doc gap 1 |
| 2 overwrite | `uv tool install --reinstall --python 'C:\Program Files\Python314\python.exe' llm-commonplace` | 0 | none | **pass**: 22 packages uninstalled and reinstalled (`~`), 25 executables, 3 s. Instruction used: line 144 ("Use the same `--python` value in every later Windows … `--reinstall` command"). The doc's Windows troubleshooting entries say "reinstall with the step 2 Windows command plus `--reinstall`", and the step 2 section has no overwrite instruction. Doc gap 1 |
| 2 `update-shell` | `uv tool update-shell` | 0 | none | **pass**: "Executable directory `<HOME>\.local\bin` is already in PATH"; no change |
| 2 shims | the snippet, pasted unchanged into PowerShell (not saved as `.ps1`) | ok | none | **pass**: "Wrote 25 shims to `<HOME>\.local\commonplace-shims`". `commonplace-validate.cmd` is byte-identical before and after (same SHA-256), and the user `Path` is unchanged because the shims dir was already first. Rerunning is safe, as the doc says |
| AV after step 2 | `avcheck.ps1` | 0 | `CI any=0 named=0; Defender det=0 ev=0; Avast chest=5 sandbox-new=1` | no new record |
| 2 check: bin, resolution | fresh child: `uv tool dir --bin`; `(Get-Command commonplace-validate).Source`; `Get-Command -All commonplace-validate` | 0 | none | **pass**: bin `<HOME>\.local\bin`. Source `<HOME>\.local\commonplace-shims\commonplace-validate.cmd`, which the step 2 check now says is expected on Windows. `-All` lists the `.cmd`, the `sh` shim, then `<HOME>\.local\bin\commonplace-validate.exe` |
| 2 check: help | fresh child: `commonplace-init --help` | 0 | none | **pass**: usage printed, 0.6 s for the whole child |
| 2 signature | `Get-AuthenticodeSignature <UV_TOOL_DIR>\llm-commonplace\Scripts\python.exe` | — | — | **pass**: `Valid`, `CN=Python Software Foundation`; `pyvenv.cfg` `home = C:\Program Files\Python314`, 3.14.7 |
| 2 base executable | fresh child: the doc's own check, `& (Join-Path (uv tool dir) 'llm-commonplace\Scripts\python.exe') -c "import sys; print(sys._base_executable)"` | 0 | none | **pass**: `C:\Program Files\Python314\python.exe` |
| 2 probe | `<tool python.exe> -I kb\work\windows-signed-python-field-use\pyd-probe.py` (absolute paths, from this agent's process; the result does not depend on `Path`) | 0 | none | **pass**: 21 of 21 loaded, all from `C:\Program Files\Python314\DLLs`, 0.3 s |
| 3 git check | `git -C <HOME> rev-parse --show-toplevel`; then, in the new empty `<HOME>\cp-install-test-run3`, `git rev-parse --show-toplevel` | 128, 128 | none | `<HOME>` is not inside a repository, and neither is the project dir: "fatal: not a git repository". Per §3, run `git init` |
| 3 git init | `git init` (from the project root) | 0 | none | **pass**: "Initialized empty Git repository"; branch `master` |
| 3 init | fresh child, from the project root: `commonplace-init --name cp-install-test-run3` | 0 | none | **pass**: created the kb collections, heads and types dirs, both templates, 12 + 12 stubs, `.commonplace/library.md` and `.gitignore`, and refreshed `.claude/settings.local.json`. It printed the "resolve outside uv's tool executable directory … Remove or reorder the shadowing PATH entry" diagnostic for all 25 commands, which §3 now says to expect and ignore |
| 3 `--check` | fresh child: `commonplace-init --check` | 0 | none | **pass**: 26 × `ok` |
| 3 validate | fresh child: `commonplace-validate landings` | 0 | none | **pass**: `VALIDATION SUCCESS`, "Files analysed: 1", 0 failures, 0 warnings. `commonplace-validate --full landings` (which the output suggests) → "all 7 top-level collections have README.md", "collisions: none". This resolves run 2's observation 2 |
| 3 search | fresh child: `rg "Commonplace" kb/ --glob "*.md" -l` | 0 | none | **pass**: 7 `COLLECTION.md` hits |
| AV after step 3 | `avcheck.ps1` | 0 | `CI any=0 named=0; Defender det=0 ev=0; Avast chest=5 sandbox-new=1` | no new record |
| 4 rename | `mv AGENTS.md.template AGENTS.md`; `mv CLAUDE.md.template CLAUDE.md` (the doc's bash block, run in PowerShell, where `mv` is `Move-Item`) | ok | none | **pass**. `CLAUDE.md` is the two `@` import lines. Neither file names a machine path (searched for `<HOME>`, `C:\`, `Users`). `git status` then showed only `.gitignore`, `AGENTS.md`, `CLAUDE.md` and `kb/`; stubs, `.commonplace/` and `settings.local.json` are ignored |
| 4 commit | `git add kb AGENTS.md CLAUDE.md .gitignore`; `git commit -m "Set up Commonplace KB"` | 0, 0 | none | **pass**: root commit, 25 files. 23 "LF will be replaced by CRLF" warnings, because global `core.autocrlf=true`. Six empty scaffold directories were not committed: `kb/tasks`, `kb/{notes,reference,sources,reports}/types` and `kb/reports/cache/connect`. Working tree clean afterwards. Doc gaps 4, 5 |
| 5 check | fresh child: `commonplace-init --check` after the commit | 0 | none | **pass**: 26 lines, all `ok` |
| 5 in-runtime skill discovery; pi sub-agent | — | — | — | **not run** (needs a runtime restart; pi not in scope) |
| 6 runtime restart, `commonplace-validate --help` inside the agent, `cp-skill-*` resolution | — | — | — | **not run** (needs a runtime restart) |
| Final | `avcheck.ps1` at 14:33 | 0 | `CI any=0 named=0; Defender det=0 ev=0; Avast chest=5 sandbox-new=1` | clean apart from the Trafilatura exception record |

Deviations from the brief:

1. `uv --version` and `git --version` were sent as two parallel tool calls in one message. That breaks the one-at-a-time rule. Both returned at once. Both executables had already been launched in runs 1 and 2. Every later launch ran alone.
2. The probe ran from this agent's process, not from a fresh child. It uses absolute paths, so the result does not depend on `Path`. The `sys._base_executable` check did run in a fresh child.

## Doc gaps

1. **Step 2 has no overwrite instruction, and the as-written command silently does nothing over an existing install** (§2 "Install Commonplace as a user-level tool", the Windows block). Over a healthy existing tool, `uv tool install --python '…Python314\python.exe' llm-commonplace` prints "already installed" and exits 0. A user or agent reading exit 0 believes they reinstalled.
   - The only "overwrite" forms the doc has are elsewhere. Line 144 mentions "`--reinstall` command below", but no Windows `--reinstall` command follows in §2. The troubleshooting entries ("DLL load failed", "Third-party antivirus") say "the step 2 Windows command plus `--reinstall`". "Updating" offers `uv tool upgrade llm-commonplace`, which does not change the interpreter.
   - I used `--reinstall` with the same `--python`, following line 144 and those entries. §2 could state it directly: "If `llm-commonplace` is already installed, for example over another interpreter, add `--reinstall`." The Trafilatura bullet already says this.
   - Not tested: whether the as-written command would also be a no-op over an install on a *different* interpreter. With `--reinstall`, uv replaced Trafilatura's mismatched environment and said so.
2. **The optional Trafilatura entry has no check, and its one Windows claim is now out of date** (§1 "Optional", Trafilatura bullet; §1 "Check prerequisites").
   - "Check prerequisites" lists only required tools. No `trafilatura --version` line appears under "Optional", so a reader cannot tell whether the optional install worked. I ran `trafilatura --version` as the brief asked.
   - The bullet ends "Trafilatura on Windows is untested beyond that refusal". After the reinstall over the signed interpreter it launched in 2.9 s with no CI record, though with an Avast exception in place (observation 1). So the sentence is out of date, but this run does not establish a clean-machine result.
3. **Step 2 cleanup leaves the uv-managed interpreter, and the doc doesn't say whether to remove it** (§1 Trafilatura bullet, §2). After moving Trafilatura to the signed interpreter, `uv python list --only-installed` still shows uv-managed 3.15.1, 3.14.9 and 3.13.17 under `<HOME>\.local\share\uv\python`. They are unused by these tools and harmless. The doc's whole case is that these builds get refused, though, and it does not say whether to keep them (`uv python uninstall`). Minor.
4. **"Commit the `kb/` scaffold" drops the empty scaffold directories** (§4 last paragraph; "Resulting layout"). Git does not track empty directories, so the first commit omits `kb/tasks/` and the four collection `types/` dirs, and `kb/reports/cache/connect/` too. "Resulting layout" lists `kb/tasks/` as part of the project. A clone will lack `kb/tasks/` until someone runs `commonplace-init` there. The doc says each cloner runs init once, but does not say init recreates these directories, and that was not tested here. Either init should write a placeholder (`.gitkeep` or a README) or the doc should say so.
5. **The first commit's prerequisites and noise are not mentioned** (§4 last paragraph).
   - The commit needs a Git identity (`user.name`, `user.email`). A new machine without a global identity would fail at `git commit`. This machine had one.
   - With Git for Windows' default `core.autocrlf=true`, `git add` prints a "LF will be replaced by CRLF" warning for each of the 23 LF files init wrote. That is harmless, but alarming in an agent transcript.
   - Both are environment matters. One sentence would cover them.
6. **Order of the per-project fill-in versus the first commit is unclear** (§4). The "review the merged file and fill in the per-project parts" paragraph follows the *existing project* case. It is unclear whether a *new* project should fill in `KB Goals and Scope` before the "first recorded state" commit, or commit the template as shipped. I committed it as shipped (7 HTML comment placeholders remain in `AGENTS.md`).
7. **"Resulting layout" is incomplete** (§ "Resulting layout"). It omits `kb/tags/` (created, with `README.md` and `COLLECTION.md`), the project `.gitignore` and the `types/` subdirectories. It also does not show that the project is a Git repository, which §1 and §3 now require. Minor.
8. **Step 4's commands are bash-only** (§4). `mv` works in Windows PowerShell 5.1 as an alias of `Move-Item`, so nothing failed. Step 2 and the checks give separate PowerShell blocks, so the absence here is inconsistent rather than wrong. Minor; no change needed unless consistency matters.

No gap found:

- §1's one-line-at-a-time note now precedes the block, and `curl.exe` is right.
- The §2 check now says Windows resolves to `.local\commonplace-shims`.
- §3's `git rev-parse` / `git init` instruction is unambiguous for the not-in-a-repo case. The in-a-repo branch was not exercised: `<HOME>` is not a repository.
- §3 warns about init's shim diagnostic.
- Rerunning the shim snippet is safe and idempotent.

## Comparison with runs 1 and 2

| Topic | Run 1 (13:54) | Run 2 (14:12) | Run 3 (14:30, HEAD `9874c8dfe`) |
|---|---|---|---|
| Doc version | then-current text | uncommitted working tree | committed HEAD |
| `curl` check | **fail**: `curl` alias in PS 5.1 (gap 1) | fixed: `curl.exe` | pass |
| Trafilatura | required; over uv 3.15.1; **hung > 30 s**, CI 3077/3033 refused `_multiprocessing.pyd`; run stopped | optional, not run | optional; reinstalled over signed 3.14.7 per the new Windows command; **launched in 2.9 s**, no CI record. Avast exception for `trafilatura.exe` present in both run 1 and run 3 |
| Starting tool state | malformed (`Scripts\python.exe` missing) | malformed → install fails exit 2; `--reinstall` fails; only `uninstall` + install worked (gap 1) | healthy 0.3.1 → as-written install is a **silent no-op**; `--reinstall` works (gap 1, new). The malformed-tool remedy is now in troubleshooting (line 379); not exercised |
| Step 2 check vs shims | not reached | contradicts shims (gap 2) | fixed: Windows clause in the check |
| `git init` | not reached | missing from doc (gap 3) | present; followed; works |
| init's "remove the shadowing entry" text | not reached | doc silent at §3 (gap 4) | doc now says expected at §3; command text unchanged |
| Paste-able check block | gap 3 | gap 5 (note below block) | note now precedes block |
| `validate landings` "Files analysed: 1" | — | unexplained (obs. 2) | explained: one subject, the landing set; `--full` shows 7 collections pass |
| Steps 4–6 | not reached | out of scope | step 4 run and pass, with new gaps 4–7; step 5 `--check` pass; rest not run |
| AV records | CI 2 (trafilatura), Avast 1 | none | Avast 1 (trafilatura exception), CI 0, Defender 0 |
| Persistent changes | none | tool reinstalled, shims rewritten, shims dir prepended to user `Path`, test project | Trafilatura env rebuilt, Commonplace env reinstalled, shims rewritten identically, test project + git repo + commit; user `Path` and `UV_TOOL_DIR` unchanged |

Every run 2 doc gap is fixed at HEAD. Run 3's gaps come from a different starting state (a healthy existing install) and from reaching step 4 for the first time.

## Observations

1. **Avast has `trafilatura.exe` in its exception list.** Run 1 also logged "Not sandboxing (file is in the exception list)", so the exception predates run 1. Run 1's hang coincided with Code Integrity refusing `_multiprocessing.pyd` from the uv-managed 3.15.1. Run 3 had no CI record and no hang over the signed 3.14.7. That fits the doc's explanation. But this machine has never launched Trafilatura without the Avast exception, and Smart App Control's verdicts vary between sessions (per the doc), so one clean launch does not prove the fix. The unsigned `<HOME>\.local\bin\trafilatura.exe` launcher was not blocked this time.
2. **PowerShell 5.1 shows uv's and git's stderr progress as `NativeCommandError` records when stderr is merged (`2>&1`).** This applies to `uv tool install`, `uv tool update-shell`, `git add` and git's CRLF warnings. It is cosmetic and comes from my capture method. A user typing the commands without `2>&1` sees plain text. An agent that merges streams may misread it as failure; the exit codes were 0.
3. The reinstalled `Scripts\python.exe` keeps the python.org file timestamp (2026-08-05). That is expected for uv's venv launcher copy.

## State left behind

- User `Path`, before and after, **unchanged**: `<HOME>\.local\commonplace-shims; <HOME>\.local\bin; <HOME>\AppData\Local\Microsoft\WindowsApps; …WinGet\Packages\astral-sh.uv_…; …\ripgrep-15.2.0-…; …\poppler-25.07.0\Library\bin;`.
- User `UV_TOOL_DIR`: `<HOME>\.local\share\uv\tools` before and after, unchanged.
- Tools (`uv tool list --show-python`):
  - `llm-commonplace v0.3.1 [CPython 3.14.7]`: reinstalled at the same path over `C:\Program Files\Python314`, with 25 launchers in `<HOME>\.local\bin`.
  - `trafilatura v2.3.1 [CPython 3.14.7]`: **changed** from 3.15.1 to the signed python.org interpreter. Same path; its launcher in `<HOME>\.local\bin` was rewritten.
- uv-managed interpreters 3.15.1, 3.14.9 and 3.13.17 are still installed under `<HOME>\.local\share\uv\python`; not touched.
- Shims dir `<HOME>\.local\commonplace-shims`: 50 files (25 `.cmd`, 25 `sh`) rewritten byte-identically, still first on the user `Path`.
- Test project `<HOME>\cp-install-test-run3`: a new Git repository on branch `master`, with one commit `Set up Commonplace KB` (25 files) under the machine's existing global Git identity. It holds the init scaffold, `AGENTS.md`, `CLAUDE.md` (renamed from the templates) and `.gitignore`. Uncommitted, ignored machine outputs: 24 stubs, `.commonplace/library.md`, `.claude/settings.local.json`.
- Backup: `env-backup-run3.txt` in the session scratchpad.
- Checkout: only this report was added. Nothing committed. The pre-existing untracked `.codex/` was left alone.

## Disclosure review

Local identifiers are normalised to `<HOME>`. The user `Path` is abridged to directory names already recorded in this workshop. No secrets, tokens or credentials appear. The Git identity used for the test commit is the machine's existing global one and is not reproduced here.
