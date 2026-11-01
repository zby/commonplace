# Independent Codex Windows verification (2026-11-01)

The installed main build passes five representative command-start checks and a
fresh-project init, pointer check and landing validation. The checkout suite
passes: 821 passed, 13 skipped, no failures or collection errors. Init still
recreates both templates after they have been renamed. This run verifies
execution from Codex; it does not repeat native skill
discovery from an agent rooted in the initialized project.

## Runtime and provenance

- Checkout: `12294a433690934cec5f361c92b3edc57b8a4910`. Initial status contained
  only the operator-owned untracked `.codex/`, which was left alone.
- Installed `llm-commonplace`: metadata 0.3.2, non-editable Git main build at
  `55700da280c7839b0bb6038485b279ec5905e24a`, confirmed from installed
  `llm_commonplace-0.3.2.dist-info/direct_url.json`. Installed Workjig is 0.3.0.
  `git diff --stat 55700da28..HEAD` shows six documentation/workshop files;
  no product or test changes separate these revisions.
- Commands resolve to `C:\Users\zzbby\.local\commonplace-shims\*.cmd`.
  The init shim runs the existing tool environment's `Scripts\python.exe`.
  Generated library root is
  `C:/Users/zzbby/.local/share/uv/tools/llm-commonplace/share/commonplace`.
- Executor: Codex worker using `gpt-6.1-sol`; desktop tool execution,
  PowerShell 7.6.5. No full application restart
  was requested or performed; checks use the current inherited environment.
  This is not independent Explorer-started or fresh-app acceptance.
- Python `C:\Program Files\Python314\python.exe`: 3.14.7; Authenticode Valid,
  Python Software Foundation signer. A direct `-c` argument probe returned
  `['-c', '-m', '', 'tail']`, establishing that this shell preserves empty `-m`.
- uv 0.13.5 and ripgrep 15.2.0 resolve from the user's WinGet directories;
  both version commands run in this Codex sandbox. The earlier report's
  inability to resolve these tools does not describe this run.

## Security and execution boundaries

Before smoke tests, queried antivirus with
`Get-CimInstance -Namespace root/SecurityCenter2 -ClassName AntiVirusProduct`.
The sandbox denied CIM access; an authorized escalated retry returned Windows
Defender (393472), Avast Antivirus (266240) and McAfee (278528).
`Get-ItemProperty HKLM:\SYSTEM\CurrentControlSet\Control\CI\Policy -Name
VerifiedAndReputablePolicyState` returned 1 (Smart App Control on).

Backed up the user Path before tests in sandbox temp. Also retained a stable
copy at `C:\Users\zzbby\AppData\Local\Temp\commonplace-codex-20261101-user-path.txt`.
No persistent environment, active installation or security configuration changed.
No processes were launched through WMI or EncodedCommand. No executable sweep
or parallel command launches were used.

`uv tool list` initially failed opening the tool-directory `.lock` (access
denied); the escalated retry succeeded and listed 25 Commonplace entry points.
This is a lock-access limitation, not command discovery failure. The sandbox's
transient `$env:TEMP` directory could not be reused as a later working directory
(CreateProcess error 267). Scratch-project checks therefore ran escalated in
stable OS temp. These checks do not establish sandbox write access there.

## Installed-package checks

Each command ran separately by bare name in the current sandbox:

| Command | Exit |
|---|---:|
| `commonplace-init --help` | 0 |
| `commonplace-task --help` | 0 |
| `commonplace-analysis --help` | 0 |
| `commonplace-status --help` | 0 |
| `commonplace-validate --help` | 0 |

Coverage is five representative entry points, not all 25. Analysis help starting
does not establish Windows support for Linux-only analysis execution.

Created `C:\Users\zzbby\AppData\Local\Temp\commonplace-codex-independent-20261101`
and ran `git init` there as a standalone call. In that directory, escalated:

1. `commonplace-init --name codex-independent`: exit 0, no shadowing warning.
2. `commonplace-init --check`: exit 0; all 26 pointer entries `ok` (12 skills
   for each runtime, library index and Claude settings).
3. `commonplace-validate landings`: exit 0; one file, zero failures/warnings.
4. `Rename-Item AGENTS.md.template AGENTS.md` and
   `Rename-Item CLAUDE.md.template CLAUDE.md`.
5. `commonplace-init --name codex-independent`: exit 0; explicitly created
   `AGENTS.md.template` and `CLAUDE.md.template` again (10,704 and 36 bytes).

This independently reproduces [run 4's template recurrence](./results-2026-10-31-afflicted-main-run4.md).
No scratch commit was required. The project remains in temp for inspection.

## Checkout pytest

The full suite uses checkout code, not the non-editable user tool. Exact command
in the checkout, PowerShell 7:

```powershell
$env:UV_CACHE_DIR='C:\Users\zzbby\.cache\uv'
uv run --python 'C:\Program Files\Python314\python.exe' pytest -m '' -q -ra -p no:cacheprovider --continue-on-collection-errors --durations=10
```

The sandbox attempt failed before tests because it could not open the short
cache's `.lock`. The escalated retry is the reported run. uv rebuilt the checkout
editable package and uninstalled/installed two project-environment packages;
it did not reinstall the active user tool. Raw output is retained at
`C:\Users\zzbby\AppData\Local\Temp\commonplace-codex-20261101-pytest.log`.

Exit 0: **821 passed, 13 skipped, 2 warnings in 102.53 seconds**. The explicit
empty `-m` overrides the configured `not slow` filter, so this includes collected
slow tests. Windows deliberately ignores `tests/commonplace/agentic_analysis/`
at collection; those tests are not included in the skip count.

Exact skip groups from `-ra`:

| Count | Location/reason |
|---:|---|
| 1 | `docs/test_generated_redirects.py:57`: optional `mkdocs_redirects.plugin` missing |
| 4 | `link_helpers.py:18`: symlinks require Developer Mode or elevation |
| 2 | `tooling/test_isolated_codex.py:43`: Linux bubblewrap integration |
| 1 | `tooling/test_isolated_codex.py:82`: Linux-only launcher |
| 2 | `tooling/test_isolated_codex.py:100`: Linux-only launcher |
| 1 | `tooling/test_isolated_codex.py:144`: Linux-only launcher |
| 1 | `tooling/test_isolated_codex.py:150`: requires bubblewrap |
| 1 | `tooling/test_isolated_codex.py:174`: Linux-only launcher |

Both warnings are Python 3.14 `PurePath.as_uri()` deprecations at
`scripts/render_systems_table.py:34`, exercised by
`comparison/test_comparison_consumers.py::test_table_links_use_file_uris_across_windows_drives`.
The longest recorded test was the shipped-library build test (6.46 seconds).
The dated earlier workshop count of 890 passed is not reproduced; this run
reports its actual checkout selection and count without inferring a regression.
A bounded selection check found no inherited `PYTEST_ADDOPTS` or
`PYTEST_PLUGINS`. Configuration selects `tests/commonplace`, with no additional
file exclusion beyond the Windows analysis-directory rule found above.
`uv run --python 'C:\Program Files\Python314\python.exe' pytest -m '' --collect-only -q -p no:cacheprovider`
under the same short-cache setting returned **834 tests collected in 1.91s**,
matching 821 passed plus 13 skipped, with no deselection reported. Its raw log is
`C:\Users\zzbby\AppData\Local\Temp\commonplace-codex-20261101-collect.log`.

## Security observations and limits

Read-only Code Integrity inspection from 07:50 local time found signing refusals
for McAfee's `mc-sec-plugin-x64.dll` under `svchost.exe` and `nvspcap64.dll` under
`WaaSMedicAgent.exe`; no Python/Commonplace target was observed. Defender threat
detection returned no records.

The recently modified existing Avast `autosandbox.log` contains a 07:54:25 entry
for this checkout's `.venv\Scripts\pytest.exe`: "Not sandboxing (because the file
is in the exception list)." This pre-existing exception limits antivirus
acceptance for the suite. The run did not add or alter an exception. Existing
log inspection is not exhaustive evidence of all antivirus behavior.

Not covered: a new installation, PyPI release acceptance, all 25 launchers,
multi-day security behavior, Linux execution, remote CI, native skill discovery,
stub argument routing in a fresh rooted agent, or Claude's Windows read rule.
The [prior installed-project report](../framework-delivery/results-2026-10-31-windows-installed-project-agents.md)
retains its separate native-routing evidence and limitations.
