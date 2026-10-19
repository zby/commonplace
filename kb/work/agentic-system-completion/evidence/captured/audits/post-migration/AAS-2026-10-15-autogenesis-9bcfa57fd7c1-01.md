# Autogenesis later-publication audit

Disposition: **hold** — the public account omits a source-visible startup defect
on both named task entry paths. Deterministic validation passes; that does not
resolve the missing qualification. Parent owns acceptance and any recovery.

## Identity and binding

- Run: `AAS-2026-10-15-autogenesis-9bcfa57fd7c1-01`.
- Method: `a320038ed1a423b051eedbcec593172f8c2032f4`.
- Source: `https://github.com/DVampire/Autogenesis`, frozen Git revision
  `5b070d5cd497e951a188a01409138e8b530eaf4a`; source `.git/HEAD` independently agrees.
- Worktree (W): `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-17-autogenesis`.
- Publication (P): `W/kb/agentic-system-analyses/retained/autogenesis`.
- Source root (S): `W/related-systems/DVampire--Autogenesis`.
- State root (R): `W/kb/agentic-system-analyses/state/` plus the exact run ID above.
- Auditor: Pi project worker, `openai/gpt-6.1-sol`, medium reasoning, independently
  exposed by `PI_PROVIDER`, `PI_MODEL`, `PI_REASONING_LEVEL`; session
  `01a144de-f0de-7501-9fc4-ab7c293f1f06`. No nested delegation.
- Only the matching `unintegrated-publications` row of
  `audit-integration-intake-2026-10-15.json` was extracted. Its complete maps are
  the digest reference, not reproduced here. All 13 current files, including
  `ARTIFACT.yaml`, exactly match both intake maps and completed effect `new`.
- Preparation, run definition and publication-effect file hashes also match
  their intake pins. `R/effects/publish.json` is completed for this exact source,
  run and destination. No incumbent substitution or older hold is cleared.

## Historical comparison and consequential discrepancy

- `systems.md:73` identifies this source and the older unpublished operational
  failure. That earlier run is not this publication and was not recovered.
- Historical lead: `kb/agentic-systems/reviews/autogenesis.md`, especially
  “Completeness and reproducibility.” It combines paper v5, release `fd6ab4c3…`
  and main `5b070d5…`; this audit compares only the matching main revision.
  Paper results and release mechanisms are not evidence for current-main behavior.
- The historical seven collection errors were not rerun or independently counted.
  Their source lead is independently confirmed: `S/autogenesis/tool/__init__.py:4`
  unconditionally imports `from .other import *`, while that package directory
  contains `context.py`, `default/`, `__init__.py`, `README.md`, `server.py` and
  `types.py`, with neither `other.py` nor `other/`.
- Both advertised paths reach that package: `S/autogenesis/gateway/service.py:66`
  and `S/examples/run_meta_agent.py:37` import `tool_manager` from it.
  `S/autogenesis/cli.py:48-54` imports the Gateway in the terminal session path.
  Under ordinary package loading, reaching the missing relative import fails;
  dependency availability is not a repair for an absent local module.
- P's synthesis, “From request to model-directed action,” describes Gateway and
  direct runtime progression without this prerequisite failure. Its opening
  no-execution statement and general external-dependency limits do not disclose
  this concrete defect in the inspected local tree. Overview also omits it.
  Boundary lines 59/63 say tests were not executed and installation success is
  unestablished; those are uncertainty statements, not this static qualification.
- This changes how a reader can use the runtime account: its internal mechanisms
  are worth studying, but the inspected checkout needs a startup repair before
  the named ordinary paths can reach those mechanisms. Audit-only disclosure
  cannot repair that missing public qualification. This is the integration blocker.
- A related historical installer lead is narrower than a blanket false-success
  claim: `S/scripts/install.sh:248-294` tracks explicit import/CLI checks through
  `FAILED`, but the pytest pipeline at line 270 does not update that flag.
  No fresh install or test outcome is asserted here; this is supporting context.

## Preserved strengths and public limits

- Complete overview, synthesis and all three verification dispositions were read.
  Report and synthesis verification declare no blockers or limits; profile
  verification retains one grouped-storage limit, explicitly carried publicly.
- Independently sampled `S/autogenesis/extension/server.py:210-264` confirms live
  loading and manifest/archive commit precede optional smoke. `smoke_gate.py:51-102`
  uses a general agent and response success/constraint fields, not exact OK or
  compulsory changed-component invocation. Synthesis already qualifies both.
- Public synthesis also distinguishes wired change from exercised improvement,
  summaries from faithful memory, transcript replay from tier recovery, workflow
  success from factual verification, and route-local policy from host isolation.
  These valuable qualifications are not additional blockers.

## Sampled operational evidence

- Trace: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/batch-17/autogenesis.output`.
  Sampled the completed report-verifier result at JSONL line 2850,
  `result.details.results[0].messages` (zero-based indexes below), not duplicate
  streaming snapshots or merely proposed calls. Launch is line 2715.
- Same-worker call/result pairs: messages 2/3 read its invocation; 4/5 read
  `verify-reports.md`; 51/55 read `smoke_gate.py` with call ID
  `call_2kiot4gDqzeKtAy1FFAE7PJH`; 63/68 read the concrete parallel-review program.
- Messages 130/131 pair `call_G3m9ecqiWoBWSLYjidqhOljv` with successful
  `commonplace-run validate-output` output: “Member content check passes;
  invocation residue not checked. This is not job acceptance or claim support.”
  This establishes performed checks/source inspection in that worker, not just
  engine acceptance. It does not certify every worker or universal write scope.

## Validation, limits and unblock

- In W, with `W/.venv/bin` prepended to PATH, bare `commonplace-validate` passed
  P (one directory-artifact subject) and each of its 12 explicit Markdown members.
  Each reported one file, zero failures and zero warnings; no notices appeared.
- The absolute owned report was validated with the same cwd and command prefix:
  success, one text file, zero failures/warnings and no notices.
- No source acquisition, target execution, state-writing commands, Git commands,
  shared edits, integration, cleanup or batch-18 inspection occurred. Source
  cleanliness and all-worker compliance were not independently certified.
- Unblock through a supported new/corrected publication that publicly states the
  exact startup defect and bounds the runtime account accordingly, or through
  evidence showing why this frozen package import resolves despite the absent
  module. Recheck exact bytes and validation afterward; do not patch accepted
  bytes or infer a fresh seven-error test result from this audit.
