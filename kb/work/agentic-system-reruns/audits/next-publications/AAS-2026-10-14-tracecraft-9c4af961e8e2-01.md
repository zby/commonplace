# Tracecraft exact-publication audit

## Decision

**Integrate with recorded limits.** No consequential defect was established in the inspected scope. The public synthesis already carries the necessary qualifications: implementation inspection is not exercised deployment; backend arbitration is conditional; completion does not verify work; handoff text lacks a registered CLI reader; transcript retention is not automatic context restoration or demonstrated learning. This is an audit recommendation, not integration authority or exhaustive worker-compliance certification.

## Identity and inspection method

- Run: `AAS-2026-10-14-tracecraft-9c4af961e8e2-01`.
- Auditor: independent project worker, runtime environment `PI_PROVIDER=openai`, `PI_MODEL=gpt-6.1-sol`, `PI_REASONING_LEVEL=medium`; no delegation.
- Prepared worktree (W): `/home/zby/llm/commonplace/.commonplace/worktrees/tracecraft-9c4af961e8e2`.
- Command prefix: `W/.venv/bin` (expanded absolute path in commands below).
- Method revision and independently checked worktree HEAD: `a568c6dc489ad546374536b642c3889ce23149a8`.
- Source (S): `W/related-systems/arrmlet--tracecraft`, identity `https://github.com/arrmlet/tracecraft`, revision and independently checked HEAD `97c6b7447f8e696f0116357d9f86bb0ece25e5b1`. `GIT_OPTIONAL_LOCKS=0 git status --porcelain` on S returned no entries.
- Publication (P): `W/kb/agentic-system-analyses/retained/tracecraft`.

Read the complete next-61 commission, audit procedure, earlier substantive commission, repository instructions, work collection contract and workshop framing. Used only the exact-run inventory row for intake. Chose a bounded discrepancy-led comparison: old memory/coordination coverage versus current public synthesis, then checked history, task arbitration and handoff delivery against the pinned implementation. Sampled actual nested worker calls/results for independent source checking and the profile refusal/correction cycle. No source acquisition, target execution, state-writing engine commands or publication edits.

## Publication identity

Recomputed the complete relative-file SHA-256 map under P: **all 13 files match the inventory exactly**, with no extra files. Independently read the completed `effects/publish.json` and `state/attempts/000037-publish.json` under this exact run. The effect names this destination, exact run and source identity; its new-file map agrees with the inventory and actual files. The attempt is completed and pins the assembled manifest.

Assembled `ARTIFACT.yaml` hash: `ca2c75f8ea1e98fb2523dc01c1d1eb3ed64bf9485646b29885f424f339fa3a4f`. This is not the inventory's type-only working declaration hash `093c6e4a6c7cab7e4e1a9db63f6d2d45eec6a24bf51f7b287dd1db929b388322`. Preparation is ready, token `9c4af961e8e2`, with the same frozen method commit. Publication success establishes retained bytes, not semantic adequacy or observed operation.

## Historical comparison and consequential checks

Historical lead: `kb/agent-memory-systems/reviews/tracecraft.md`, checked 2026-06-05 at `7d77daaaf17d3f18b7718e3ddfc8ee2576446adc`. That historical source was not acquired or inspected. The account is a coverage lead, not current truth or proof that the two revisions are equivalent.

1. **Memory history is a current addition to the old simple-KV account, not an unsupported preservation guarantee.** S `sdk/tracecraft/cli/memory.py:37–124` writes the snapshot before the live value, supports metadata reads and selects the newest requested history entries before displaying them oldest-first. P `synthesis.md`, “Claim work, exchange progress and declare completion,” preserves those details and rejects enforced immutability or proof of successful live replacement. The old account's absence of history is not a current omission.
2. **Backend-specific ownership remains qualified.** S `sdk/tracecraft/s3.py:47–62` sends `IfNoneMatch="*"`; `hf.py:52–69` performs exists-then-write. S `cli/steps.py:37–70,96–151` shows cooperative claims, a caller-string owner check, `--force`, and status written before handoff. P synthesis explicitly distinguishes the backend race, cooperative identity, missing work verification and status/handoff crash window. This retains and sharpens the historical warning against equating backend guarantees.
3. **Handoff intent is not wired delivery.** S `docs/s3-architecture.md:91–93` illustrates `tracecraft handoff`; S `cli/__init__.py:55–66` does not register that command. S `cli/steps.py:171–225` displays state or polls, not handoff content. P synthesis and its limitations table publicly preserve the documentation/implementation mismatch and avoid inferring recipient uptake from a completion receipt. No audit-only caveat is needed to repair this point.
4. **The principal historical architectural coverage survives with narrower conclusions.** Bucket state, explicit reads, artifacts, four host adapters and trace preservation remain visible in the synthesis. The historical blanket pull-only/no-learning language becomes scoped uncertainty: established dynamic deliveries are requested reads, while opaque artifacts, host checkpoints and incompletely assessed evaluator consumers prevent a system-wide negative. The synthesis expressly withholds numerical benchmark results, faithful host reconstruction, secret-removal guarantees, exact-once recovery and demonstrated benefit. The old Commonplace borrowing proposals and watch list are not required source-first findings. I did not independently re-audit adapters, redaction, compaction or every comparison classification.

## Selected actual operational evidence

Trace T: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/tracecraft.output`. Locators below are physical JSONL lines; nested calls are paired by full tool-call ID within the same returned worker's `messages`, not inferred from stream updates or proposals.

- **Independent report checking occurred.** T line 2305 launches handout `000022-report-verification`; line 2412 returns its worker. Within that worker, `call_bKIBfZVjdiCr9kHO6DQPRLh1|fc_06e1d27039abb93e016acfe516162887d2bc82c3e843f3ecf2` reads S `cli/steps.py` and has a non-error result containing the implementation. `call_BX7Oy4zMWcU6GDxRlIcSITaN|fc_06e1d27039abb93e016acfe516163c87d287ba1bebb46294de` likewise returns `cli/memory.py`. `call_lRTPmmYXPaBCGWaYd8FTQdBL|fc_06e1d27039abb93e016acfe5575a6c87d28c7879244fd78083` reads the architecture handoff section successfully. Its subsequent output-validation call returned “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” These are actual source reads, not publication-as-compliance.
- **A deterministic preflight failure was repaired locally.** T line 3136, worker `000026-profile-verification`, call `call_rr5OxSn3EGfVLOzfaK9tIQYa|fc_0ceada7b19c1df59016acfe7b03cb887d2b4cc8163aeee48b2`, returned exit 1: `[artifact] profile-verification.md: unresolved source SRC-1; the Source register is outside the documents this one may cite: epistemic.md, memory-profile.md, memory.md, runtime.md, workflow.md`. Its next edit succeeded; call `call_mQUJDkkFC071CFKOnuDulhQp|fc_0ceada7b19c1df59016acfe7be5c0887d2b9cdb263db4cf758` then returned the member-content pass disclaimer. This is not a semantic pass inferred from exit status.
- **A semantic refusal caused a substantive revision.** T line 3477, worker `000028-memory-profile`, call `call_k2gmTLgFVHWfjqd1g6C2Qdrr|fc_09e36045b84c6b9b016acfe861eb2887d2b1617f90738233da` actually reads the refusal for `000027-apply-profile-verification-1`. Its blocker is omitted ranking authority: retained session metadata sorts list entries by recency/size before a limit, independently of informational display. Call `call_CVY52CAYtSY5GY5d7hkkw4oJ|fc_09e36045b84c6b9b016acfe88b6b9487d2be942b745bbdaffc` successfully replaces four profile blocks. Its later validation returns the member-content pass disclaimer. Current P `memory-profile.md:489–521,1066` distinguishes inspection information from ranking; the synthesis also names the sort-before-limit mechanism. This is a retained correction, not a silently ignored refusal.

This sample establishes performed reads and revision work, not exhaustive adherence by all workers. No consequential scope violation was established in the selected actions. A direct attempt to read the historical handout refusal path now returned `ENOENT: no such file or directory`; its contents and execution evidence above were recovered from T, without recreating handouts or changing state.

## Validation

From W, ran the recorded-prefix command:

```text
/home/zby/llm/commonplace/.commonplace/worktrees/tracecraft-9c4af961e8e2/.venv/bin/commonplace-validate kb/agentic-system-analyses/retained/tracecraft
```

Actual result: `VALIDATION SUCCESS`; target and scope `kb/agentic-system-analyses/retained/tracecraft`; files analysed 1 (set target), text files 0; **0 failures across 0 subjects, 0 warnings across 0 subjects**. No notices were emitted. This deterministic result does not verify every quotation or certify semantic compliance.

From W, also ran the same absolute validator executable with the absolute origin report path `/home/zby/llm/commonplace/kb/work/agentic-system-reruns/audits/next-publications/AAS-2026-10-14-tracecraft-9c4af961e8e2-01.md`. Actual result: `VALIDATION SUCCESS`; files analysed 1, text files 1; **0 failures across 0 subjects, 0 warnings across 0 subjects**. No notices were emitted.

## Limits and integration conditions

No hold blocker is established. Integrate only these inspected bytes, retaining the existing public qualifications; parent must recheck the byte map and own integration/full review. Changed bytes require reassessment. The source-level checks here are deliberately narrower than the publication's whole-system account; benchmark outputs, external service behavior, actual agent uptake, all nested-worker obligations and every source quotation were not independently verified. Stronger claims would require deployment/uptake traces, backend contention and failure evidence, and assessed benchmark records; they are not prerequisites for integrating the already-qualified implementation account. No additional source acquisition or substantial reanalysis was undertaken.
