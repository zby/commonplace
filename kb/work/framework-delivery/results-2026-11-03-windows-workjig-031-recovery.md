# Windows Workjig 0.3.1 recovery acceptance (2026-11-03)

## Purpose

Run the unchanged [0.3.1 fixture](./workjig-031-recovery-fixture.py) on Windows with the installed Commonplace tool's interpreter, as the [handoff](./windows-delivery-handoff.md#workjig-031-recovery-acceptance) specifies. Earlier the same day the 0.3.0 fixture failed here on its in-hold read of `.lock`, because Workjig 0.3.0 locked byte 0 with `msvcrt.locking`, a mandatory lock.

## Setup

- Machine: Windows 11 Home 10.0.26300, Smart App Control on, Windows Defender, Avast and McAfee. The same machine and installation as the PyPI 0.3.3 acceptance run (`git show 600306e1d:kb/work/windows-install/results-2026-11-03-pypi-033.md`).
- Runtime: a Claude Code session in the Claude desktop app, bypass-permissions mode, no sandbox.
- Checkout: `61cabdc5b`. Fixture SHA-256 `08D47FFBA52BB8346596F227D9A957DD08A873EFEA7AD0C9AB69CEAFD624F0F8`, last changed in `61cabdc5b`; the copy in the session scratchpad had the same hash.
- Before: `llm-commonplace` 0.3.3 from PyPI with Workjig 0.3.0, over `C:\Program Files\Python314\python.exe`. The uv receipt pins `llm-commonplace==0.3.3` and that interpreter. No process was using the tool environment.

## Steps and results

1. **Dependency update.** `uv tool upgrade llm-commonplace --upgrade-package workjig`. Exit 0; the only change was `workjig==0.3.0` → `workjig==0.3.1`. uv kept the exact `==0.3.3` pin. Afterwards: `llm-commonplace` 0.3.3 with no `direct_url.json` (PyPI); Workjig 0.3.1, installer `uv`, no `direct_url.json` (PyPI, non-editable); `sys._base_executable` is still the python.org path; the receipt's requirement and interpreter are unchanged; `commonplace-validate` still resolves to the shim.
2. **Fixture.** `& (Join-Path (uv tool dir) 'llm-commonplace\Scripts\python.exe') '<scratchpad>\fixture031\workjig-031-recovery-fixture.py'`. Exit 0:
   - `empty` and `interrupted`, two repetitions each: `Run()` rejected the records with "run record is missing"; the lock bytes, including the read *inside* `hold()`, were unchanged; no `run.json` appeared.
   - `fresh-run`: `hold()` was refused while `Run()` held the lock; `run.json` was created.
   - `fresh-hold-then-run`, two repetitions: `Run()` was refused while `hold()` held the lock, then succeeded.
   - Workjig 0.3.1 from the tool's `site-packages`, `direct_url` null, temporary root removed.
3. **Commands after the update.** From the scratch project `<HOME>\cp-install-test-pypi033`, through the shims: `commonplace-task --help`, `commonplace-analysis --help` and `commonplace-init --check` exited 0.

## Not covered

- Commonplace 0.3.3 declares `workjig>=0.3.0`, so a fresh PyPI install could still resolve 0.3.0 if 0.3.1 were unavailable. The checkout's `>=0.3.1` floor ships with the next release.
- Security logs were not rechecked for this short run.
- The Claude default-permission and delivery check in the handoff.

## State left behind

The user tool is `llm-commonplace` 0.3.3 from PyPI with Workjig 0.3.1, over the same interpreter and shims. To return to 0.3.0: `uv tool install --reinstall --python 'C:\Program Files\Python314\python.exe' 'llm-commonplace==0.3.3' --with 'workjig==0.3.0'`.
