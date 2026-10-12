# Six-run worker preflight and engine agreement audit

Audit date: 2026-10-12 UTC. Commission: [Audit an analysis](../audit-an-analysis.md), with the operator's explicit deviations: inspect all six completed workflow runs in one invocation; omit timing; use stored evidence only. This report answers a narrow question, not a validation redesign or a fresh semantic audit.

## Outcome

**No passing worker preflight followed by a deterministic refusal of the submitted draft is established in these six runs.** This zero comes from enumerating the actual engine records, including later checks of unchanged candidates against changed partners—not from assuming that the previously reported 81 passing workers agreed with the engine.

There is **one deterministic refusal candidate**: GBrain judgment `000006-check-runtime-0`. Its producer's only and final preflight failed with exit 2 because the worker supplied a nonexistent artifact directory. The exact submitted report bytes were then refused for an ambiguous source quotation. Classification: **no passing preflight**. A fresh correction worker repaired the attribution, passed preflight, and received deterministic acceptance.

Eight additional refused judgments apply **semantic verifier blockers**. They are not shared deterministic-check disagreements. All eight have `Findings: none` and nonempty `Blockers`; the frozen handler can also refuse for verdict-dependent deterministic findings, but no such refusal is recorded here.

This is bounded evidence about stored execution. It does not establish validator/engine equivalence, universal worker compliance, avoided costs, factual correctness, or an absence of future disagreements.

## Identities and evidence boundaries

`reporter-profile`: pi / `openai/gpt-6.1-sol` / medium, from `PI_PROVIDER`, `PI_MODEL`, and `PI_REASONING_LEVEL`. Reporter session: `01a12fa2-4a2c-7150-8e32-86ea205d69f7`. The audited worker profile is separately pi-sol / `openai/gpt-6.1-sol` / medium.

| System | run-id | method-commit | source-revision |
|---|---|---|---|
| GBrain | `AAS-2026-10-11-gbrain-9de8e3c225d3-01` | `8213c5f06ea86ec6c13dd3bedff6a66c6b0bd3ad` | `da434385572e0dc0d825649179aabed4107d6e60` |
| Graphiti | `AAS-2026-10-12-graphiti-1d535ca565a4-01` | `682d5e7e6fa87af0f60d6a8a35266c41cb0e2913` | `964bb11d1e7020e3cc67fab244268b0736b6c219` |
| Napkin | `AAS-2026-10-12-napkin-2b85bef38252-01` | `69199c6ec09fa32b13f1bbc61d844f768cc4d7d4` | `7582d6a46f5a11995956e60a59c41a5b242109f1` |
| Letta Code | `AAS-2026-10-12-letta-code-be76afeab9b7-01` | `83cb44a89bfb56f17efb1a141ec77eaf2f859a2d` | `271f119dcf37d58649a18e6c733386b3c710a456` |
| Dynamic Cheatsheet | `AAS-2026-10-12-dynamic-cheatsheet-ca0a0b29d273-01` | `bb155f68660d0c7294f410e3aea4816ae3c6e2b1` | `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9` |
| Instinctual Memory | `AAS-2026-10-12-instinctual-memory-af48437aa60c-01` | `86006bf574c274b715667386ae2e3a1793538db1` | `6acb13dc35765bf5ccfc87e445dd09c480f1c28a` |

Worktrees under `/home/zby/llm/commonplace/.commonplace/worktrees/` are, respectively:

- `gbrain-9de8e3c225d3`
- `graphiti-workflow-1d535ca565a4`
- `napkin-workflow-2b85bef38252`
- `letta-code-workflow-be76afeab9b7`
- `dynamic-cheatsheet-workflow-ca0a0b29d273`
- `instinctual-memory-workflow-af48437aa60c`

`R` means the corresponding worktree's `kb/agentic-system-analyses/state/<run-id>/`. Evidence is in `R/run.json`, `R/state/attempts/<attempt-id>.json`, `R/state/judgments/<judgment-id>.json`, and `R/state/versions/<sha256>`. These are locators, not substitutes for run identity. The [batch record](../workflow-batch.md), [hidden-failure review](./workflow-six-run-hidden-failures.md), and [five-run audit](./workflow-five-run-batch-audit.md) supplied identities and trace leads; the counts below were independently computed from stored records.

`T` is the nested trace root:

```text
/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--/2026-10-11T15-31-10-091Z_01a12b96-de8a-711e-8a12-57ef261a7126.jsonl
```

`T/L159/c22/r0/m64` means one-based JSONL line 159, then zero-based coordinator message 22, result 0, worker message 64. The coordinator is `row["message"]["details"]["results"][0]`; the worker is `coordinator["messages"][c]["details"]["results"][r]`. Coordinator-only anchors omit `r/m`. Each inspected tool result was paired with the call having its exact `toolCallId` inside the same envelope. Proposed calls without results were not counted as executed checks or mutations.

The [work collection contract](../../COLLECTION.md) and [text type](../../../types/text.md) permit this frontmatter-free report. The [analysis collection contract](../../../agentic-system-analyses/COLLECTION.md) supplies frozen evidence boundaries. Only this report and its workshop README entry are authorized writes. No agents, analysis workflow, frozen engines, target code, or frozen validators were run; no sources, run state, retained artifacts, methods, or concurrent edits were changed. Inspection used one-shot standard-library Python without saving scripts.

## What counts as a deterministic judgment

I inspected the frozen GBrain worktree implementations, not the concurrently edited origin engine:

- `src/commonplace/artifactrun/handlers.py:182–254`: `check` and `apply_verification`.
- `src/commonplace/artifactrun/checks.py:66–89,141–158`: shared draft content findings, invocation checks, and judgment scope.
- `src/commonplace/cli/validate_notes.py:583–631`: worker draft preflight.
- `src/commonplace/lib/agentic_analysis/publication.py:189–226`: assembly's full pinned-artifact validation and overview acceptance.

The first three files have identical SHA-256 prefixes in all six worktrees: `8b428dd6560cd89a`, `bd8c6bd4542a84f4`, and `04e07cf0d8086a3b`, respectively. Scoped Git status for `src/commonplace` and analysis types was empty in each worktree. The run's retained declaration identifies the handlers and criteria; judgment `basis` records pin each invocation's actual inputs. Current origin changes are not evidence of frozen behavior.

The distinctions matter:

1. `check-*` invokes the shared content check with pinned candidate, partners and criteria, then adds declared checks and correction-answer/invocation checks. Its refusal is deterministic.
2. Each `apply-*-verification-0` first structurally checks the verifier document itself. A structural failure here would be a deterministic refusal candidate. All 24 such judgments accept.
3. Later judgments in that apply attempt concern the handed subjects. The handler applies authored semantic blockers and can also add deterministic findings caused by placing the verdict beside a subject. All eight recorded apply refusals contain only semantic blockers, with `Findings: none`.
4. `assemble-0` accepts the generated overview after full artifact validation. It is not a worker-draft opportunity.
5. `report-check` writes artifact findings but judges nothing. All nine stored outputs say exactly `# Artifact check`, blank line, `none`. Opening, acquisition and publication also have no stored judgment; completed attempts are not fabricated acceptance records.

Worker preflight explicitly says “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” Shared content code does not imply identical invocation inputs or all engine-only checks. This audit therefore classifies actual refusals rather than interpreting a pass as a stronger certificate.

## Denominators

All 247 attempt records were enumerated: **84 completed model attempts and 163 completed code attempts**, with no failed or open stored attempt. Their judgment references resolve to **186 judgment records**. Counts below separate structural evaluation from semantic application rather than labeling every code-produced judgment deterministic.

| System / T line | Attempts: model / code | `check-*`: accepted / refused | Apply verifier's own structural check: accepted / refused | Assembly accepted | Apply subject judgments: accepted / refused | Same-version later `check-*` |
|---|---:|---:|---:|---:|---:|---:|
| GBrain / 159 | 17 / 32 | 20 / 1 | 5 / 0 | 1 | 7 / 2 | 9 |
| Graphiti / 183 | 18 / 34 | 23 / 0 | 5 / 0 | 1 | 7 / 4 | 10 |
| Napkin / 189 | 13 / 24 | 15 / 0 | 4 / 0 | 1 | 7 / 1 | 6 |
| Letta Code / 195 | 11 / 22 | 14 / 0 | 3 / 0 | 1 | 7 / 0 | 6 |
| Dynamic Cheatsheet / 201 | 11 / 22 | 14 / 0 | 3 / 0 | 1 | 7 / 0 | 6 |
| Instinctual Memory / 207 | 14 / 29 | 19 / 0 | 4 / 0 | 1 | 7 / 1 | 9 |
| **Total** | **84 / 163** | **105 / 1** | **24 / 0** | **6** | **42 / 8** | **46** |

Thus **136 structural/assembly judgments: 135 accepted, one refused**; **50 apply-subject judgments: 42 accepted, eight semantically refused**. There are 106 `check-*` invocations over 60 distinct role/version pairs, including 46 rechecks of already checked bytes. The 24 verifier candidates account for the other model attempts. The nine artifact-check outputs are outside the 186 judgment denominator.

An independent exact-ID extraction of the final matched validator in each analytical worker confirms final preflight passes of **15/17, 18/18, 13/13, 11/11, 11/11, 13/14**, respectively: **81/84**. This confirms the aggregate but does not supply the zero-disagreement conclusion. That conclusion comes from inspecting the only structural refusal and checking the outcomes of every later structural judgment. No worker lacks a matched final validator result; three final validators fail.

For the **one deterministic refusal candidate**, classification counts are:

| Classification | Cases |
|---|---:|
| No passing preflight | 1 |
| Candidate changed after passing preflight | 0 |
| Partner/criteria context changed or differed after a pass, explaining a refusal | 0 |
| Engine-only check refused after a pass | 0 |
| Genuine shared-check disagreement | 0 |

These are classifications of refused judgments, not error rates over independent workers or systems.

## D1 — GBrain runtime: exact same submitted bytes, no passing preflight

**Producer:** completed model attempt `000005-runtime`, worker `T/L159/c22/r0`. Its primary report is:

```text
486c8969498aa9caae5a0eed467007a2546ee143f59eaff0f7c9844d936353b7
```

The successful report write at `m61–62` hashes to exactly that value. Both `R/state/attempts/000005-runtime.json["outputs"]["report"]` and judgment `000006-check-runtime-0`'s candidate basis and subject version pin it. The version blob has those exact bytes. This is not a comparison with the later published runtime member.

**Final preflight:** `m63 → m64`, exact call/result ID:

```text
call_5gTfEoLVB4QWPRZD9GQAvxEy|fc_06009f1fdc3f05a4016acc1c2c06c087d2915b20ed44bd5fdd
```

The executed command uses the correct frozen worktree validator and candidate but supplies:

```text
--artifact /home/zby/llm/commonplace/.commonplace/worktrees/gbrain-9de8e3c225d3-01/artifact --role runtime
```

The delivered prompt at `m3` instead binds the artifact under the real worktree's `kb/agentic-system-analyses/state/AAS-2026-10-11-gbrain-9de8e3c225d3-01/artifact`. The result has `isError: true`, reports missing `ARTIFACT.yaml` at the invented location, and says **Command exited with code 2**. This worker has exactly one matched validator invocation, no earlier pass, and final text `problem` at `m67`.

**Mutations after the check:** `m65–66` writes only `problem.md`; no subsequent report write/edit or shell mutation appears. The submitted report hash therefore agrees with the last successful report write before the failed check. There is no passing check after which a candidate mutation could explain disagreement. The worker's claim that it ran the supplied command exactly is contradicted by the emitted argument, as already documented in hidden-failure H1.

**Submission/engine lineage:** coordinator `T/L159/c23 → c24` submits `--completed 000005-runtime` and receives the runtime correction handout. Exact coordinator ID:

```text
call_b7wyC69XZNlSrzQXrkBXSPCl|fc_0773d5572098a629016acc1c4411bc87d2b358f1c344c9dc03
```

The stored completed code attempt `000006-check-runtime` references judgment `000006-check-runtime-0`, outcome `refused`. Its exact deterministic objection starts:

> [artifact] runtime.md: quote-anchored citation at line 111: quotation ambiguous: quote occurs 2 times in the source region; quote more context or supply a range containing one occurrence (src/core/persistence/journal.ts at the recorded commit)

It offers source regions `228–231` and `304–307`. `Blockers` is `none`; this is a shared content finding, not an authored semantic blocker or correction-answer check.

**Context:** the producer and engine both pin boundary `81bd5b93e4e844e8376fdcb3f8541c35f2b29766a3ac4ecbb03951987d061063`. Runtime type and records contract pins agree between producer and check. The engine has no memory, epistemic or workflow partner yet. Nevertheless the worker never reached a content check at its wrong artifact argument, so there is no successful worker criteria/partner snapshot to equate with the engine's. Classification remains **no passing preflight**, not a claimed identical-context discrepancy.

### Supported recovery, not retrospective agreement

Fresh producer `000007-runtime` is `T/L159/c26/r0`. A successful shell copy at `m26–27` starts from the previous report; successful edit `m28–29` adds `:228-231` to the ambiguous attribution. Applying that exact edit to the refused blob reconstructs the submitted correction hash:

```text
f0b40d88d1a839f6f7a69bf547087eec77243a56ed078e0e761fba8197f027c4
```

Its final preflight `m33 → m34` returns the explicit content-pass message, with no error. Exact ID:

```text
call_rLlP3akKZntuDmG2TNrsZvbm|fc_08836da92247422c016acc1c89eb6c87d2a6cb68319fbbb7bc
```

No subsequent mutation call occurs in that worker. `000008-check-runtime-0` accepts this corrected hash. Coordinator `c27 → c28` closes it using ID `call_RPIEuYthmBaSJb0FH9mNQaTJ|fc_0773d5572098a629016acc1c93385087d2b1d79bc80787dc1c`. This is a concrete passing-preflight/acceptance pair, not proof that the first worker passed or that its failed invocation would have produced the engine's finding.

## Later deterministic rechecks

I grouped `check-*` judgments by exact `(subject.role, subject.version)` and compared role-partner versions in successive judgment bases. **All 46 later same-version checks accept**, and each has a changed partner basis. No refusal is hidden by counting only initial checks.

The following shorthand lists the six-digit sequence prefixes of exact `check-*` judgment IDs; their role is shown. Every listed ID ends `-0`. The complete inventory below resolves each prefix to its stored filename.

| System | Later unchanged-candidate checks | Partner change from preceding check of those bytes |
|---|---|---|
| GBrain | runtime 000013,000015,000018; memory 000016,000019; epistemic 000020 | New memory, then epistemic, then workflow partners as applicable |
| GBrain | runtime 000028; epistemic 000029; workflow 000030 | Corrected memory partner |
| Graphiti | runtime 000011,000013,000016; memory 000014,000017; epistemic 000018 | New memory, then epistemic, then workflow partners as applicable |
| Graphiti | runtime 000029,000031; memory 000032 | Corrected memory, then corrected epistemic partners as applicable |
| Graphiti | workflow 000033 | Corrected runtime, memory and epistemic partners |
| Napkin | runtime 000011,000013,000016; memory 000014,000017; epistemic 000018 | New memory, then epistemic, then workflow partners as applicable |
| Letta Code | runtime 000011,000013,000016; memory 000014,000017; epistemic 000018 | New memory, then epistemic, then workflow partners as applicable |
| Dynamic Cheatsheet | runtime 000011,000013,000016; memory 000014,000017; epistemic 000018 | New memory, then epistemic, then workflow partners as applicable |
| Instinctual Memory | runtime 000011,000013,000016; memory 000014,000017; epistemic 000018 | New memory, then epistemic, then workflow partners as applicable |
| Instinctual Memory | memory 000026; epistemic 000027; workflow 000028 | Corrected runtime partner |

Instinctual's unchanged epistemic hash `1493b381668e863dbf61332894c563db54712d1fd0a25ffc07954c1cabbc8f08` accepts at `000012-check-epistemic-0`, `000018-check-epistemic-0`, and `000027-check-epistemic-0`. Its worker's failed final preflight at `T/L207/c26/r1/m48–49` does not become a worker pass merely because these later checks pass. Likewise GBrain's first profile passes structural check `000037-check-memory-profile-0` despite its worker's failed final validator at `T/L159/c56/r0/m52–53`; the subsequent profile refusal is semantic.

## Inventory of stored judgments and check outputs

This inventory enumerates every judgment without copying its large `basis`. Within each role list, a sequence `000004` denotes **exact ID `000004-check-<role>-0`**. All accept except GBrain runtime `000006`, marked refused. Assembly is listed separately. The associated attempt ID is the judgment ID without its final numeric suffix. Read each judgment's `subject.version` and `basis` for the exact candidate/partner/criteria hashes.

| System | Structural `check-*` judgments by role | Assembly judgment |
|---|---|---|
| GBrain | boundary: 000004; runtime: **000006 refused**,000008,000013,000015,000018,000028; memory: 000012,000016,000019,000027; epistemic: 000014,000020,000029; workflow: 000017,000030; reconciliation: 000022,000032; memory-profile: 000037,000041; synthesis: 000045 | `000048-assemble-0` accepted |
| Graphiti | boundary: 000004; runtime: 000006,000011,000013,000016,000025,000029,000031; memory: 000010,000014,000017,000028,000032; epistemic: 000012,000018,000030; workflow: 000015,000033; reconciliation: 000020,000035; memory-profile: 000040,000044; synthesis: 000048 | `000051-assemble-0` accepted |
| Napkin | boundary: 000004; runtime: 000006,000011,000013,000016; memory: 000010,000014,000017; epistemic: 000012,000018; workflow: 000015; reconciliation: 000020; memory-profile: 000025,000029; synthesis: 000033 | `000036-assemble-0` accepted |
| Letta Code | boundary: 000004; runtime: 000006,000011,000013,000016; memory: 000010,000014,000017; epistemic: 000012,000018; workflow: 000015; reconciliation: 000020; memory-profile: 000025; synthesis: 000029 | `000032-assemble-0` accepted |
| Dynamic Cheatsheet | boundary: 000004; runtime: 000006,000011,000013,000016; memory: 000010,000014,000017; epistemic: 000012,000018; workflow: 000015; reconciliation: 000020; memory-profile: 000025; synthesis: 000029 | `000032-assemble-0` accepted |
| Instinctual Memory | boundary: 000004; runtime: 000006,000011,000013,000016,000025; memory: 000010,000014,000017,000026; epistemic: 000012,000018,000027; workflow: 000015,000028; reconciliation: 000020,000030; memory-profile: 000035; synthesis: 000039 | `000042-assemble-0` accepted |

Apply inventory: `000025/0–1`, for example, denotes exact judgments `000025-apply-report-verification-0` and `000025-apply-report-verification-1` in the report column. Ranges are inclusive. **Every suffix 0 is the accepted structural verifier-candidate judgment.** Other suffixes apply the verifier to subjects; every one accepts except the eight exact IDs in the following refusal table.

| System | `apply-report-verification` sequences/suffixes | `apply-profile-verification` sequences/suffixes | `apply-synthesis-verification` sequences/suffixes |
|---|---|---|---|
| GBrain | 000025/0–1; 000035/0–5 | 000039/0–1; 000043/0–1 | 000047/0–1 |
| Graphiti | 000023/0–3; 000038/0–5 | 000042/0–1; 000046/0–1 | 000050/0–1 |
| Napkin | 000023/0–5 | 000027/0–1; 000031/0–1 | 000035/0–1 |
| Letta Code | 000023/0–5 | 000027/0–1 | 000031/0–1 |
| Dynamic Cheatsheet | 000023/0–5 | 000027/0–1 | 000031/0–1 |
| Instinctual Memory | 000023/0–1; 000033/0–5 | 000037/0–1 | 000041/0–1 |

### Semantic refusals excluded from deterministic disagreement

These are all eight apply refusals. Each stored packet starts `## Findings`, `none`, then `## Blockers` with an authored objection. Their semantics and repair chains are retained in the supplied audits; this inventory does not recast them as deterministic failures.

| System | Exact judgment ID | Subject / objection | Verifier trace |
|---|---|---|---|
| GBrain | `000025-apply-report-verification-1` | memory / missing separate checkpoint and retrieval-feedback object parts | T/L159/c38/r0 |
| GBrain | `000039-apply-profile-verification-1` | memory-profile / trace-source classification | T/L159/c60/r0 |
| Graphiti | `000023-apply-report-verification-1` | runtime / notebook input-origin account | T/L183/c36/r0 |
| Graphiti | `000023-apply-report-verification-2` | memory / notebook origin and bulk-retention account | T/L183/c36/r0 |
| Graphiti | `000023-apply-report-verification-3` | epistemic / notebook input-origin account | T/L183/c36/r0 |
| Graphiti | `000042-apply-profile-verification-1` | memory-profile / inferred-judgment selector classification | T/L183/c60/r0 |
| Napkin | `000027-apply-profile-verification-1` | memory-profile / missing permanent-unlink decay classification | T/L189/c48/r0 |
| Instinctual Memory | `000023-apply-report-verification-1` | runtime / short-fragment matching and local-backfill flush overclaims | T/L207/c34/r0 |

Artifact-check attempts: GBrain `000023-report-check`, `000033-report-check`; Graphiti `000021-report-check`, `000036-report-check`; Napkin, Letta Code and Dynamic Cheatsheet each `000021-report-check`; Instinctual Memory `000021-report-check`, `000031-report-check`. Each pins findings blob `ac3a9c2025687a1d4caf05aad8e3f4e1fda6bcc3b2de6dfb294b08cfcb3ea3ec`, containing `none`. These checks generate no refused judgment. All six assembly and publication attempts completed; this audit did not rerun them or re-certify publication bytes.

## Limits and disposition

No missing trace or record blocks the sole deterministic-refusal investigation. The nested trace contains both its worker call/result and coordinator closure; attempt, judgment and version records agree. Unexecuted transport proposals elsewhere in the runs remain excluded. The scoped question is answered: **zero observed passing-preflight/deterministic-refusal cases, one refusal without a passing preflight, eight semantic refusals outside that category**.

The audit is not an exhaustive reconstruction of every successful worker's filesystem at validation time. In particular, final-pass aggregates do not prove all partner/criteria snapshots identical or all engine-only obligations checked. The later recheck inventory shows actual outcomes under changed partners, not an equivalence theorem. For the one refusal, exact bytes and mutation lineage are established; for its successful correction, the edit-to-version reconstruction and absence of later worker mutations are also established. No counterfactual validator execution was performed.

Retain this evidence and the earlier status-handling findings. No validation redesign, method amendment, frozen repair, timing comparison, avoided-cost claim, commit or push follows from this report.

## Authored Markdown validation

Validation targets are this report and the README entry only. Both narrow commands returned exit 0:

```text
commonplace-validate kb/work/analysis-audit-evidence/reports/workflow-six-run-validation-agreement.md
VALIDATION SUCCESS
Files analysed: 1
Text files: 1
Diagnostics: 0 failures across 0 subjects; 0 warnings across 0 subjects

commonplace-validate kb/work/analysis-audit-evidence/README.md
VALIDATION SUCCESS
Files analysed: 1
Text files: 1
Diagnostics: 0 failures across 0 subjects; 0 warnings across 0 subjects
```

Judgment-reference uniqueness/completeness and subject-version presence checks passed for all six runs (36/40/28/25/25/32 judgments). `git diff --check` passed. No frozen engine or frozen artifact validation is part of these authored Markdown checks. Final status/diff inspection confined this invocation's changes to the two authorized paths; no commit or push was made.
