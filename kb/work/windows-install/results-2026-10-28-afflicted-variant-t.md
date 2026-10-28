# Shim delivery round 2, variant T: afflicted machine (run t2)

- Procedure: [shim-delivery-test-plan.md](./shim-delivery-test-plan.md), variant T, short form: R1, R0, R3, the R6 sweep and the stdlib extension probe. R4, R5, R7 and R8 were not repeated; S covers them over the same signed interpreter.
- Variant: **T**, `uv tool install --python 'C:\Program Files\Python314\python.exe' --editable <WORKSPACE>`, with the shims from `INSTALL.md`'s Smart App Control section.
- Why it could run: T was blocked on this machine because Avast refuses the default tool path `…\uv\tools\llm-commonplace\Scripts\python.exe`. The plan allows a different tool directory, so this run set `UV_TOOL_DIR=<TESTROOT>\tools` and `UV_TOOL_BIN_DIR=<TESTROOT>\toolbin` for each process.
- Machine, runtime, antivirus and observation method: as in [the variant S run](./results-2026-10-28-afflicted-variant-s.md), 09:09–09:12 local, about 25 minutes after it. `<TESTROOT>` = `<HOME>\cp-shim-2026-10-28\t`. Observation by `avcheck.ps1` from [windows-signed-python-field-use](../windows-signed-python-field-use/README.md), with the pattern `cp-shim|Python314|commonplace|\uv`.

## Results

| Test | Command | Exit | Antivirus records | Result |
|---|---|---|---|---|
| R1 install | `uv tool install --python 'C:\Program Files\Python314\python.exe' --editable <WORKSPACE>` | 0 | none | **pass**: 22 packages, 25 executables in `toolbin`. The tool's `Scripts\python.exe` is Authenticode `Valid`, signed by the Python Software Foundation (python.org's `venvlauncher.exe`); `pyvenv.cfg` home `C:\Program Files\Python314` |
| R0 control | `Start-Process <TESTROOT>\toolbin\commonplace-validate.exe --help` (`NotSigned`), once | 0 | **Avast 09:12:03: `Sandboxing (no custody)`** for that launcher; help began `usage: python.exe …` | **pass** (instrument) |
| R3, registrar shims | registrar with `-PythonPath <TESTROOT>\tools\llm-commonplace\Scripts\python.exe`; `commonplace-validate --help`, `commonplace-source --help` | 0, 0 | none | **pass**; source `<TESTROOT>\bin-t\…cmd` |
| R3, `INSTALL.md` shims | the `INSTALL.md` snippet unchanged, except that it wrote to `<TESTROOT>\snippet-shims` and did not change the user `Path`; the same two `--help` calls | 0, 0 | none | **pass**; source `<TESTROOT>\snippet-shims\…cmd`; these are the production `-c` shims |
| Git Bash `sh` shim | `commonplace-source --help`, with `command -v` showing `snippet-shims/commonplace-source` | 0 | not armed | **pass** |
| R6 sweep | the 13 targets of the S run, through the snippet shims | 13 × 0 | none | **pass**: provenance 13 of 13. Every output matched S's except `work`, which grew between the runs |
| Extension probe | `<TESTROOT>\tools\llm-commonplace\Scripts\python.exe -I pyd-probe.py` | 0 | none | **pass**: 21 of 21 loaded from `C:\Program Files\Python314\DLLs` |

## Findings

1. **T works on this machine wherever its tool path is not blocked.** It keeps the `uv tool` layout that ADR 064, `commonplace-init` and the health check recognise. The interpreter the shims start is PSF-signed, and its base is the signed python.org install, so the stdlib extensions load from signed files.
2. **Avast's block of the default tool path is left over from 2026-10-26.** It affects this machine only, and only that one path. A user without that history would use the default `UV_TOOL_DIR`; this run did not test that, because it is not possible here.
3. **By decision rule 3, T is preferred over S.** It changes `INSTALL.md` only by adding the prerequisite and the `--python` value; the shim step stays as it is. For a machine whose tool path is blocked, the fallback is another `UV_TOOL_DIR`, as in this run; it keeps the `uv tool` layout, so S is not needed there.

## State left behind

`<TESTROOT>` (`tools`, `toolbin`, `bin-t`, `snippet-shims`, `r6`) left in place, not on `PATH`. No user `Path` or user-level `UV_TOOL_DIR` change: both variables were set only inside the test processes.

## Disclosure review

Local identifiers normalized (`<WORKSPACE>`, `<HOME>`, `<TESTROOT>`); no secrets; no full environment or `PATH` output.
