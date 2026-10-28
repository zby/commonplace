# Shim delivery round 2, variant U: afflicted machine (run u2)

- Round and procedure: round 2, [shim-delivery-test-plan.md](./shim-delivery-test-plan.md), tests R0–R8; R9 not started for this variant (see Findings). Machine, runtime, shell, uv, antivirus products, baseline and observation method are as in the companion run [results-2026-10-28-afflicted-variant-s.md](./results-2026-10-28-afflicted-variant-s.md), which ran immediately before this one; only the differences are recorded here.
- Variant: **U**, shims that start the `Scripts\python.exe` of a uv venv on a uv-managed CPython.
- Checkout: `<WORKSPACE>`, `llm-commonplace` 0.3.1, HEAD `9c37c5617`.
- Machine: afflicted (Smart App Control on; Avast, McAfee, Defender registered). Antivirus results **informative**: R0 here produced an Avast reaction, and the companion run's R0 a Code Integrity block.

## Identity (differences from the companion run)

| Field | Value | Basis |
|---|---|---|
| Date/time | 2026-10-28, 08:45–08:56 local (UTC+1) | observed |
| Test root | `<TESTROOT>` = `<HOME>\cp-shim-2026-10-28\u`, new for this run | observed |
| Interpreter | `<TESTROOT>\.venv\Scripts\python.exe` (46 592 bytes, `NotSigned`), created by `uv venv --managed-python --python 3.14`; base `<HOME>\.local\share\uv\python\cpython-3.14-windows-x86_64-none\python.exe` (a junction to `cpython-3.14.9-windows-x86_64-none`; `NotSigned`); CPython 3.14.9 | observed |

## Results

| Test | Exact top-level command(s) | Exit | Resolved source | Generated exe invoked? | Antivirus records in window | Result |
|---|---|---|---|---|---|---|
| R1 install | `uv venv --managed-python --python 3.14 <TESTROOT>\.venv`; `uv pip install --python <TESTROOT>\.venv\Scripts\python.exe -e <WORKSPACE>` | 0; 0 | n/a | no; 31 `.exe` in `Scripts` (25 `commonplace-*`) | **Avast Auto-Sandbox 08:45:13: `<TESTROOT>\.venv\Scripts\python.exe` => `Sandboxing (no custody)`**; CI 0; Defender 0 | **pass** (install completed: `Resolved 22`, `Installed 22`); antivirus reaction recorded |
| R0 step 2 | `Start-Process <TESTROOT>\.venv\Scripts\commonplace-validate.exe --help` | 0 after 4.3 s | n/a | yes, once | **Avast 08:46:15: `commonplace-validate.exe` => `Sandboxing (no custody)`**; 08:46:18 `python.exe` => `Not sandboxing (because the file is in the exception list)`; CI 0 | **pass** (instrument): Avast reaction observed. The help text began `usage: python.exe <TESTROOT>\.venv\Scripts\commonplace-validate`, not `usage: commonplace-validate`, which fits a sandboxed run. Smart App Control did not block this launcher, though it blocked the companion run's launcher 9 minutes earlier |
| R2 direct dispatch | `& <TESTROOT>\.venv\Scripts\python.exe -c "…validate_notes import main…"` with `--help` | 0 | n/a | no | Avast: `python.exe` in exception list | **pass**: 27 lines; distribution 0.3.1 at `<TESTROOT>\.venv\Lib\site-packages` |
| R3 registration | `powershell -NoProfile -File …\register-test-shims.ps1 -PythonPath <TESTROOT>\.venv\Scripts\python.exe -BinDirectory <TESTROOT>\bin-u` | 0 | n/a | no; 25 `.cmd`, 25 `sh`, 0 `.exe` | as R2 | Count 25 |
| R3 shim dispatch | `commonplace-validate --help`; `commonplace-source --help` | 0; 0 | `bin-u\…cmd` both | no | as R2 | **pass** |
| R4 / R5 | as the companion run, in `<TESTROOT>\projects\one` and `two` | all 0 | `bin-u\…cmd` | no | as R2 (5 entries) | R4 **pass** (26 of 26 `ok:`, landings success, library root `<WORKSPACE>/kb`, open-problem-4 diagnostic printed); R5 **partial** |
| R6 sweep | same 13 targets as the companion run | 13 × 0 | 13 of 13 `bin-u\commonplace-validate.cmd` | no | CI 0 named; Avast 12 entries, all exception list | **pass**: 91 s; all 13 outputs byte-identical to variant S |
| R7 fresh process | PID 7100; nothing resolves before prepend; then `--help` ×2 and the sweep | 0, 0; 13 × 0 | 15 of 15 `bin-u\…cmd` | no | CI 0 named; Avast 14 entries, all exception list | **pass**: outputs byte-identical to R6 |
| R8 every command | 25 tool calls, one `<name> --help` each, as in the companion run | 23 × 0; 2 × 1 (`fcntl`) | 25 of 25 `bin-u\<name>.cmd` | no | 24 windows: CI 0 named, Avast exception list only. **`commonplace-x-snapshot` window: Code Integrity 3077 + 3033 at 08:54:51, the uv-managed `python.exe` loading `DLLs\_decimal.pyd`** | **partial**: every command started, but Smart App Control refused a stdlib extension during one of them; exit 0 because `decimal` falls back to pure Python |

R8 start times: mostly 0.2–0.9 s, but `commonplace-ack-review` (the first) took **21 s**, `commonplace-task` 10.8 s and `commonplace-x-snapshot` 5.1 s, against 0.5 s, 0.5 s and 2.9 s under variant S. No antivirus record explains the delays; none reached the 30 s stop limit.

### Stdlib extension probe (added; not in the plan)

After the R8 block, one probe: `<TESTROOT>\.venv\Scripts\python.exe -I <HOME>\cp-shim-2026-10-28\tools\pyd-probe.py`, importing 21 stdlib C extensions in turn. **4 were refused by Smart App Control**, each `ImportError: DLL load failed … Zasady kontroli aplikacji zablokowały ten plik`, with matching Code Integrity 3077/3033 pairs (08:55:27–08:55:35):

| Refused | Consequence |
|---|---|
| `_decimal.pyd` | `decimal` silently uses the pure-Python fallback |
| `_asyncio.pyd`, `_overlapped.pyd` | `asyncio` cannot be imported on Windows (the Proactor event loop needs `_overlapped`) |
| `pyexpat.pyd` (so `_elementtree` too) | `xml.parsers.expat` and the C ElementTree fail; any XML parsing through them fails |

The other 17 (`_ssl`, `_hashlib`, `_sqlite3`, `_ctypes`, `_socket`, `select`, …) loaded. The signed python.org interpreter loaded all 21 with no record (companion run). In total this run has 7 Code Integrity 3077 blocks on uv-build files (`_decimal` 3, `pyexpat` 2, `_asyncio` 1, `_overlapped` 1), and the launcher, `python.exe` and third-party `.pyd` files were never refused.

## Findings

1. **Variant U is blocked in part by Smart App Control.** The shims themselves start, but the unsigned uv-managed CPython has stdlib extensions that Smart App Control refuses at load time. Which files get refused is a reputation verdict and may change. It matches open problem 2, where a whole build (3.13.17) was refused; here 3.14.9 starts, but 4 of its 21 probed extensions do not load. The commands under test today happen not to need `asyncio` or `pyexpat` for `--help` and validation, so R3–R7 pass. That is luck, not acceptance.
2. **Avast sandboxes U's per-install executables on first run.** It sandboxed the venv's `python.exe` and the generated launcher, then moved `python.exe` to its exception list within a minute. Variant S triggered no Avast entry at all.
3. **Smart App Control verdicts vary for uv launchers.** U's `commonplace-validate.exe` ran (sandboxed by Avast), while S's launcher from the same uv version was blocked 9 minutes earlier. The S launcher embeds a different interpreter path, so the files differ.
4. **Unexplained slow starts under U** (21 s, 10.8 s, 5.1 s), with no matching record. This fits the 2026-10-26 hang without explaining it.

## Decision rule outcome (provisional)

The plan's rule 1 needs U to pass R0–R8; U is **partial** at R8 and fails the extension probe. Rule 2 applies: **U is blocked or inconsistent and S passes.** It is provisional until S's R9 (several days of normal use) shows nothing. R9 was not started for U, because R8 already decides against it as the main procedure. Variant T was not run (its tool path is still refused by Avast; plan, variants table).

## State left behind

`<HOME>\cp-shim-2026-10-28\u\` (`.venv`, `bin-u`, `projects\one`, `projects\two`, `r6`, `r7`) left in place, not on `PATH`. The venv's launchers are in Avast's sandbox history and exception list. No change to the user `Path`, the uv tool directory, the uv-managed Python installs, Avast, Defender or Smart App Control. `INSTALL.md` unchanged.

## Disclosure review

- Final payload reviewed: yes
- Local identifiers normalized: yes (`<WORKSPACE>`, `<HOME>`, `<TESTROOT>`; machine name omitted)
- Secrets, credentials, private keys: none observed
- Full environment, PATH and raw configuration output: absent
- Withheld or residual sensitive-looking material: none
