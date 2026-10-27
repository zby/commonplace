# Correction note: registered shim harness run — 2026-10-27

Applies to [2026-10-27-registered-shim-validation.md](./2026-10-27-registered-shim-validation.md). That report is unchanged; this note records what its pass results do not establish, reviewed against the machine state on the same day.

| Test | Reported | Corrected class | Reason |
|---|---|---|---|
| W3 shim dispatch | pass | partial | The call was spelled `commonplace-validate.cmd`; bare-name resolution was not exercised and no resolved source was recorded. On this machine the bare name `commonplace-validate` resolves to `<HOME>\.local\bin\commonplace-validate.exe`, a uv tool install of `llm-commonplace` 0.1.4 (observed via `Get-Command` and `uv tool list`). |
| W4 project one | pass | pass | — |
| W5 project two | pass | partial | Both projects dispatch to the same interpreter and package; the report says so. Only working-directory project selection was shown. Version-sensitive dispatch was not run. |
| W6 validation sweep | pass | partial; antivirus result uninformative | Exit statuses were observed. The antivirus result rests on "no alert appeared". Defender real-time protection is on, but `Get-MpThreatDetection` history on this machine is empty, including for the uv tool executables run earlier the same day, and no negative control through a generated executable was run. The original detection that motivates the design is not recorded anywhere in the repository. |
| W7 fresh process | pass | partial | The test bin directory is not on a fresh process's `PATH`; the report does not say how the fresh process resolved the shim or what source it resolved to. Does not bear on desktop runtime inheritance, which the native Windows probe of the same day already observed. |

Other observations:

- The test root `tmp\windows-shim-test-w1` is inside the source checkout (gitignored), against the plan's precondition; harmless for this run, but record it.
- `pwsh` is not installed on this machine; the registrar must be invoked with `powershell -NoProfile -File`.
- The harness calls the venv `python.exe` directly, so `uv.exe` is outside the executed path, unlike the production concept `uv run --no-sync`.

The test plan was revised the same day to require resolved-source provenance for every bare-name call, a recorded antivirus observation method, a negative control (W0), and separate partial/uninformative result classes.

## Disclosure review

- Final payload reviewed: yes
- Local identifiers normalized: yes
- Secrets, credentials, and private keys: none observed
- Full environment, PATH, and raw configuration output: absent
- Optional automated scan: not run
- Withheld or residual sensitive-looking material: none
