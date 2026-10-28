# Windows signed Python in field use

## Commission

Posed by the operator on 2026-10-28, split from [windows-install](../windows-install/README.md) as that workshop's test R9. **Back burner:** the maintainers do not normally use Windows, so this waits for a new user who does.

The operator decided on 2026-10-28 that a Windows install needs the signed python.org interpreter as a prerequisite (windows-install, "Round 2 outcome"). The procedure that carries it is variant T: the uv tool built over the signed interpreter, with commands started through the `INSTALL.md` shims. The evidence is one day on one machine: the shims over the signed interpreter (variants S and T) ran with no Code Integrity, Defender or Avast record, while the uv-managed interpreter had four stdlib extensions refused. Smart App Control decides by reputation, and its verdicts vary between runs, so one clean day does not show that T stays accepted. This workshop observes the `INSTALL.md` Windows procedure in ordinary use over days, which is the only test of the deletion Avast made on 2026-10-26.

**Resume when** a Commonplace user runs the Windows procedure on a machine with Smart App Control on, or with third-party antivirus (Avast, McAfee or similar), and agrees to report. The machine the evidence came from also qualifies, if the operator works on it again.

**Closes when** one of these is recorded:

- at least a week of ordinary use on such a machine, with commands still starting and no quarantine, sandbox or Code Integrity entry naming the signed interpreter, the tool environment, the shims or `commonplace`: the prerequisite stands;
- an entry that does name them: reopen the decision in ADR 064 (or its amendment) with the record, and say which component was acted on.

Durable results go to ADR 064's evidence and to `INSTALL.md`'s Windows troubleshooting. Then delete this directory and its entry in `kb/work/README.md`.

## Constraints

- The testing rules in windows-install's README apply: start one command at a time; never start processes through WMI or `powershell -EncodedCommand`; record the antivirus products and back up the user `Path` before the first check; never turn Smart App Control off.
- A clean result counts only after a positive control on the same machine: one run of a uv-generated launcher that Smart App Control blocks or the antivirus reacts to (windows-install's [shim-delivery-test-plan.md](../windows-install/shim-delivery-test-plan.md), R0). Without it the machine cannot tell acceptance from absence, and the run is uninformative.
- Avast keeps an exception list learned per file: a new executable is sandboxed on its first run and excepted afterwards. The first runs after an install or upgrade are the informative ones; record them.
- Commits carry `Workshop: kb/work/windows-signed-python-field-use`.

## Method

Two scripts in this directory, ASCII only for Windows PowerShell 5.1:

- [avcheck.ps1](./avcheck.ps1) — the antivirus observation for one window: Code Integrity 3033/3077 events naming the given pattern, Defender detections and events, Avast's quarantine count and new Auto-Sandbox entries. Run `powershell -NoProfile -File avcheck.ps1 -RunStart <last check> -NamePattern '<pattern>'` on each day of use, with a pattern matching the install's paths.
- [pyd-probe.py](./pyd-probe.py) — imports 21 stdlib C extensions and reports which fail. Run once after install and after each Python upgrade: `<python.exe> -I pyd-probe.py`. A failure reading `DLL load failed … application control policy` is a Smart App Control refusal.

Record each check as a dated line in a `log.md` here: date, machine (Smart App Control state, antivirus products), Python version, commands used that day, the `avcheck` summary line and any entries it lists.

## Evidence so far

- [results-2026-10-28-afflicted-variant-t.md](../windows-install/results-2026-10-28-afflicted-variant-t.md) — T, the `INSTALL.md` procedure, passes a short run in a separate tool directory; its state section names the test root used there.
- [results-2026-10-28-afflicted-variant-s.md](../windows-install/results-2026-10-28-afflicted-variant-s.md) — S passes R0–R8 over the same signed interpreter, covering the tests T's short run skipped.
- [results-2026-10-28-afflicted-variant-u.md](../windows-install/results-2026-10-28-afflicted-variant-u.md) — the uv-managed interpreter's refused extensions and Avast's first-run sandboxing.

If windows-install has closed when this resumes, read these from git history.
