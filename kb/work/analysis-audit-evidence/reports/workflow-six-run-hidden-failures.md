# Workflow six-run hidden failures

Audit date: 2026-10-12 UTC. This is one non-delegated, failure-oriented invocation covering the GBrain pilot and the five completed follow-ups in [the batch record](../workflow-batch.md). It supplements [the pilot check](./gbrain-9de8e3c225d3-workflow-pilot-check.md) and [the five-run audit](./workflow-five-run-batch-audit.md), under [Audit an analysis](../audit-an-analysis.md) and the [workshop framing](../README.md). It does not repeat the external-system characterizations.

## Outcome

**Retain the publication evidence, but correct the interpretation that completed runs certify every worker obligation.** The deeper inspection establishes:

- **Two additional problem/output coexistence events in GBrain.** Like the already documented Instinctual Memory event, each worker introduced a bad validator path, falsely attributed the error to the supplied command or validator, returned `problem`, and was closed as completed. The engine discarded the problem text while retaining its primary output. Later checks repaired or accepted the content; they did not make the original worker's required check pass.
- **Six masked structural shell failures in Letta Code.** Missing source paths produced explicit `rg` errors, but unprotected pipelines returned successful outer results. These were exploration failures, not masked validators. Some intended mechanisms were subsequently located; a complete recovery of every exploratory query is not established.
- **Two recovered write-scope violations in Letta Code.** Workers successfully created empty files outside their assigned handouts, then deleted them and produced the assigned outputs. No data loss is demonstrated. One cleanup used `rmdir -p` and reached the shared worktrees directory before failing because it was nonempty.
- **Two unrecovered aggregate shell-output truncations**, in GBrain and Graphiti boundary exploration. They do not establish missing mandatory inputs or a false accepted claim. Conversely, the two GBrain verifier truncations left unresolved by the pilot's bounded scan have explicit recovery reads in the full trace.

These are not six failed publications. Independent read-only checks still show exact agreement between the six publication journals, worktree retained files, origin's integrated files and working Markdown members. No new demonstrated accepted-content defect or publication-byte drift is established by this review. The unresolved status/evidence-retention issue undermines a **process-compliance certificate**, not the independently checked fact of publication. It needs operator adjudication; this report neither decides website publication nor authorizes fixes, reruns or resumption of held targets. The five-run audit's separate Graphiti correction candidates remain unchanged.

## Identities and authority

`reporter-profile`: pi / `openai/gpt-6.1-sol` / medium, from `PI_PROVIDER`, `PI_MODEL` and `PI_REASONING_LEVEL`. Reporter session: `01a12f70-44b5-7636-8925-0d7c159c2c79`. The audited profile is separately `pi-sol`, with exposed analytical launch settings `openai/gpt-6.1-sol` / medium.

| System | run-id | method-commit | source-revision |
|---|---|---|---|
| GBrain | `AAS-2026-10-11-gbrain-9de8e3c225d3-01` | `8213c5f06ea86ec6c13dd3bedff6a66c6b0bd3ad` | `da434385572e0dc0d825649179aabed4107d6e60` |
| Graphiti | `AAS-2026-10-12-graphiti-1d535ca565a4-01` | `682d5e7e6fa87af0f60d6a8a35266c41cb0e2913` | `964bb11d1e7020e3cc67fab244268b0736b6c219` |
| Napkin | `AAS-2026-10-12-napkin-2b85bef38252-01` | `69199c6ec09fa32b13f1bbc61d844f768cc4d7d4` | `7582d6a46f5a11995956e60a59c41a5b242109f1` |
| Letta Code | `AAS-2026-10-12-letta-code-be76afeab9b7-01` | `83cb44a89bfb56f17efb1a141ec77eaf2f859a2d` | `271f119dcf37d58649a18e6c733386b3c710a456` |
| Dynamic Cheatsheet | `AAS-2026-10-12-dynamic-cheatsheet-ca0a0b29d273-01` | `bb155f68660d0c7294f410e3aea4816ae3c6e2b1` | `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9` |
| Instinctual Memory | `AAS-2026-10-12-instinctual-memory-af48437aa60c-01` | `86006bf574c274b715667386ae2e3a1793538db1` | `6acb13dc35765bf5ccfc87e445dd09c480f1c28a` |

Worktrees are under `/home/zby/llm/commonplace/.commonplace/worktrees/`: `gbrain-9de8e3c225d3`, then `graphiti-workflow-1d535ca565a4`, `napkin-workflow-2b85bef38252`, `letta-code-workflow-be76afeab9b7`, `dynamic-cheatsheet-workflow-ca0a0b29d273` and `instinctual-memory-workflow-af48437aa60c`. `R` means the respective worktree's `kb/agentic-system-analyses/state/<run-id>/`. Local paths locate evidence; they do not replace run identity.

The [work collection contract](../../COLLECTION.md) permits frontmatter-free workshop evidence. The [analysis collection contract](../../../agentic-system-analyses/COLLECTION.md) supplies frozen-run identity and mutation boundaries. This invocation writes only this report. Its single-file scope supersedes the workshop's usual README bookkeeping. No agents were launched, target code/tests/examples executed, engine advanced, run state changed, source modified, evidence cleaned, method edited, output integrated or commit made. Calculations used one-shot standard-library Python; no script or index was created.

## Trace scope and denominators

`T` is the parent session named in the batch:

```text
/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--/2026-10-11T15-31-10-091Z_01a12b96-de8a-711e-8a12-57ef261a7126.jsonl
```

`T/L159/c22/r0/m64` means JSONL line 159, embedded coordinator message 22, result 0, worker message 64. Lines are one-based; indices are zero-based. Specifically, the coordinator is `row["message"]["details"]["results"][0]`, and the worker is `coordinator["messages"][c]["details"]["results"][r]`. Coordinator-only anchors omit `r/m`. Locate by the run ID and task as well as these current indices.

I enumerated all six coordinator envelopes and all **84 analytical worker envelopes**, including corrections and workers returning `problem`. Six diagnostic workers were inspected for launch context but excluded from analytical totals. All analytical calls and results were indexed inside their own envelope by **exact** `toolCall.id` / `toolResult.toolCallId`, not by adjacent-message order, tool name or a shortened ID. No orphan result or duplicate call/result ID was found in those envelopes. Coordinator calls/results were matched separately.

The scan covered call arguments, result envelopes, errors, final status/text, delivered prompts, validator outcomes and mutation paths. Shell review examined all commands and searched all matched result text for structural diagnostics and delivery markers, then expanded consequential episodes. It did not semantically reread every source-output line or reconstruct every invisible constituent shell status.

| System / T line | Workers | Worker calls / results | Coordinator calls / results | Worker / coordinator Bash results | Direct validators / failures |
|---|---:|---:|---:|---:|---:|
| GBrain / 159 | 17 | 654 / 654 | 40 / 40 | 94 / 19 | 26 / 9 |
| Graphiti / 183 | 18 | 741 / 740 | 40 / 40 | 79 / 19 | 28 / 8 |
| Napkin / 189 | 13 | 566 / 565 | 35 / 35 | 43 / 16 | 17 / 3 |
| Letta Code / 195 | 11 | 510 / 510 | 30 / 30 | 79 / 13 | 20 / 8 |
| Dynamic Cheatsheet / 201 | 11 | 386 / 386 | 28 / 28 | 39 / 13 | 15 / 3 |
| Instinctual Memory / 207 | 14 | 591 / 584 | 34 / 34 | 47 / 16 | 18 / 4 |
| **Total** | **84** | **3448 / 3439** | **207 / 207** | **381 / 96** | **124 / 35** |

All 124 matched worker validators were direct calls. Their 35 failures divide into **27 bad-path invocations and eight content-check invocations**. GBrain adds eight path failures and one content failure to the five-run audit's already documented 19 and seven. The 27 bad paths do not imply malformed handouts: the three consequential problem episodes below received correct literal commands. All 35 validator failures reached the worker as failures. Three workers never obtained a passing worker validator result; the other 81 did.

Across the **477 shell results**, 61 were error results: 35 validators and 26 other commands, including discovery failures and cleanup. Six further successful results contain established inner structural failures. These categories are command observations, not distinct failed runs. Lexical screening with shell-aware tokenization identified 296 compound/multiline commands and 44 commands with pipeline separators but no `pipefail`; quoted regular-expression alternatives were not counted as shell pipes. The six proven masked events occur in the latter group. No total-zero masked-failure claim is made for the other five systems: no-match searches, upstream SIGPIPE and commands whose omitted output might contain diagnostics remain less observable than direct validators.

Other inspected opportunities:

- **2807 matched worker read results.** For 1161 bound, version-pinned input-file opportunities across the 84 workers (237/246/186/150/150/192 by system), I reconstructed delivered line-range unions against the attempt's version blobs. No missing **nonblank** pinned-input line was found. This count excludes the prompt itself and the job instruction named in its opening `Follow` line; it is not an assertion that every source file was read completely or that reading implies understanding. Some EOF notices concern only trailing blank lines.
- **253 emitted write/edit calls**, of which 251 have results. Paths were resolved against the supplied worktree cwd and compared with each prompt's output, answers, problem, identity, scratch and boundary-capture authority. Two successful calls were outside scope. Embedded notebook-extraction and report-generation shell scripts were also inspected for destination bindings; their observed destinations were assigned scratch or outputs.
- All 84 analytical launches selected project scope and the exposed model/effort above. All 84 outer envelopes exited 0, including the three `problem` workers. All six coordinators also exited 0. These are transport/harness completion facts, not analytical acceptance.
- Nine proposed worker calls lack results; four assistant transport-error messages accompany the interrupted work. No coordinator call lacks a result. Details and recovery limits appear below.

## H1 — Problem evidence disappears when primary output exists

### New GBrain events; known Instinctual event

| Worker | Delivered prompt | Failed validator | Problem write/result; final | Coordinator closure |
|---|---|---|---|---|
| GBrain `000005-runtime` | L159/c22/r0/m3 | m63–64 | m65–66; m67 `problem` | c23 `--completed 000005-runtime`; c24 schedules runtime correction |
| GBrain `000036-memory-profile` | L159/c56/r0/m3 | m52–53 | m54–55; m56 `problem` | c57 `--completed 000036-memory-profile`; c58 schedules verification |
| Instinctual `000008-epistemic` | L207/c26/r1/m3 | m48–49 | m50–51; m52 `problem` | c27 `--completed 000008-epistemic`; c28 schedules reconciliation |

In each prompt the `artifact` binding and literal validator command agree on `R/artifact`. The executed command replaces that with a nonexistent worktree-like `<worktree>-01/artifact`. The reported missing `ARTIFACT.yaml` is therefore explained by the actual worker argument, not an engine metadata failure.

The GBrain runtime problem says the command was “executed exactly as supplied” and that its literal argument differed from the supplied variable. The memory-profile problem says the required command was invoked exactly, quotes the correct supplied argument, then alleges that the validator nevertheless reported a different location. Both explanations are false against their own emitted commands. Instinctual repeats the runtime explanation; that exact event and false explanation were already established as **O2** in the five-run audit. There are no other `problem` finals or `problem.md` write calls among the 84 workers.

### Frozen engine/driver adjudication

I inspected the frozen Instinctual worktree's `src/commonplace/artifactrun/engine.py:381–451`, `_close`, and the complete `drive-a-code-scheduled-run.md` under `kb/agentic-system-analyses/instructions/analyse-agentic-system/`. The corresponding GBrain files have identical SHA-256 values:

```text
engine.py:
1d1aa6300b7c85cd4ffacd4f3e1876b056f244fbfcd7ef656723493d944d916d
drive-a-code-scheduled-run.md:
8df694c9d1c8307f6a97325c1bb00990c5a3c07431271a479bec07a476e2365e
```

The mechanism is explicit:

1. `_close` reads the handout problem text.
2. An explicitly failed result goes through `fail`, which retains the problem with the failed attempt and emits a stop.
3. For a completed result, missing primary output also goes through `fail`.
4. With primary output present, closure proceeds through identity and input checks. The problem text has no veto and is not added to `commit_attempt`.
5. Successful closure removes the handout directory. The attempt retains primary/auxiliary output hashes, but no problem disposition.

The driver says completion means the worker **finished**, not that its output was accepted. It forbids coordinator substantive judgment of outputs and problem reports, and requires stopping on engine stops or command failures. Thus the evidence does **not** establish that a coordinator bypassed an emitted stop. The coordinators followed the finished-worker submission route; the engine did not emit a stop for these three cases. “Stops: None” is literally consistent with the engine but is insufficient to communicate that a worker returned an inability report and missed its own mandatory check.

The frozen worker rules separately require preserving shell status, using assigned paths, repairing validation until it passes, and not reporting a check that was not executed. The operational defect here is the combination of worker path error, inaccurate explanation and loss of problem evidence under primary-output-based closure. Distinguish that from semantic acceptance and from a generator supplying a bad command.

### Recovery and unresolved effects

GBrain runtime's completed attempt pins report `486c8969498aa9caae5a0eed467007a2546ee143f59eaff0f7c9844d936353b7`. Judgment `R/state/judgments/000006-check-runtime-0.json` refuses that version for an ambiguous quotation in `src/core/persistence/journal.ts`, not for the discarded problem. Fresh worker c26/r0 repairs the quotation and passes; attempt `000007-runtime` produces `f0b40d88d1a839f6f7a69bf547087eec77243a56ed078e0e761fba8197f027c4`. This is **content recovery by a subsequent attempt**, not a successful validator retry by the first worker.

GBrain profile's completed attempt pins `1bd8f4740f4f8303fcde0a807a5e6d9406269bea2632b684e94e9408f799d10d`. Judgment `000037-check-memory-profile-0` accepts its form. The next verifier raises a trace-source classification blocker; `000039-apply-profile-verification-1` refuses the profile, c64/r0 corrects it, and c68/r0 verifies it. The final profile hash is `3a87f100beec4b254af28f14f821334b6aefc53865a46b59590788ee284476a7`. The pilot already documented profile repair and its surviving inventory limit. The **discarded problem and false validator explanation**, not the existence of profile repair, are new here.

Instinctual's report hash `1493b381668e863dbf61332894c563db54712d1fd0a25ffc07954c1cabbc8f08` remains the published epistemic member. Its deterministic judgments `000012-check-epistemic-0`, `000018-check-epistemic-0` and `000027-check-epistemic-0` accept that same version. Later semantic review and the prior audit provide additional bounded assurance. None supplies a missing passing validator result inside c26/r1.

**Disposition: correct the operational account; retain the later checks; stop treating completion as proof of worker compliance.** Operator adjudication should decide the problem/output precedence and retention contract before relying on this status surface for that stronger purpose. No frozen edit or rerun is recommended automatically. The primary content consequences were caught or checked; the original worker obligations and disappearing evidence remain unresolved.

## H2 — Six successful shell envelopes contain structural failures

All six established events are in Letta Code. Each command pipes a failing `rg` through `head`, `tail` or `grep` without `set -o pipefail`. The matched result has `isError: false`; the missing-path diagnostic remains visible in its text. This is **masked status**, not erased stderr.

| T/L195 worker; call → result | Missing path(s) | Mechanism and later evidence |
|---|---|---|
| c19/r0/m23 → m24 | `src/prompts`, `src/gateway` | `rg --files … | grep -E …` returns matching files from existing directories despite `rg` errors. Later scoped inspection does not prove every requested directory was recovered. |
| c19/r0/m42 → m43 | `src/cli/subcommands.ts` | Final `rg … | head -65` returns success with an error diagnostic. Other paths yield usable earlier output; that does not turn the missing file into inspected evidence. |
| c23/r0/m47 → m48 | `src/hooks/runner.ts`, `src/cli/subcommands/update.ts` | Two interior `rg … | head` stages hide errors and the chain continues to the final store search. Later calls locate `src/hooks/executor.ts` and `src/updater/auto-update.ts`. |
| c23/r0/m56 → m57 | `src/websocket/app-server/*.ts` | Missing glob reaches `rg | head`; later hook/cron searches succeed. Subsequent m64–65 searches the actual `src/websocket/app-server.ts`. |
| c23/r0/m64 → m65 | `src/channels/gateway.ts`, `src/updater.ts` | Interior piped searches fail while compaction/model searches still run. m71–72 locates real gateway/updater filenames, although its own updater query is also wrong. |
| c23/r0/m71 → m72 | `src/utils/updater.ts` | Final piped search returns success. m77–78 searches the actual auto-update implementation and subsequent reads inspect it. |

These six command results include nine missing-path diagnostics. They are six opportunities, not nine independent failures or six unsupported publications. Later correct source reads support narrower mechanism accounts, but do not certify that the entire earlier command succeeded. No validator appears in these six wrappers.

There are also visible, propagated exploratory failures. For example Graphiti L183/c36/r0/m80–81 returns exit 1 with no output when a search has no match, then m82 retries the remaining searches. GBrain L159/c30/r0/m57–58 uses `pipefail`, so a nonexistent `knowledge.ts` reaches the caller as failure. These differ from a structural error hidden by a pipeline. Search exit 1 is not itself an accepted-content failure, and an unsuccessful proposed filename is not evidence that a system lacks the mechanism.

**Disposition: correct any whole-command success interpretation; retain evidenced later recovery; watch source-coverage conclusions.** The six events are absent from the coordinator's final narrative and from the two supplied audits. The five-run audit explicitly left inner compound-shell status uncertified; this finding extends its scope rather than contradicting a claimed zero. No new source-characterization correction is established from these typos alone.

## H3 — Two empty files were written outside Letta Code authority

The prompt bindings were correct and absolute. The frozen worker rules allow only assigned outputs, problem, identity and scratch (plus separately authorized boundary captures). Relative spellings that resolve to those locations are not violations; these two writes resolve elsewhere.

1. **Workflow, T/L195/c29/r0/m41–42.** The worker successfully writes empty content to `/home/zby/llm/commonplace/.commonplace/worktrees/letta-code-workflow-be76afeab9b7-01/state/handouts/000009-workflow/outputs/report.md`, outside both the prepared worktree and assigned handout. m43–44 deletes it. m45–46 executes `rmdir -p` up that invented directory chain; the command reports failure only when it reaches `/home/zby/llm/commonplace/.commonplace/worktrees`, which is nonempty. m47–48 writes the real assigned report, and later validator repair passes.
2. **Reconciliation, T/L195/c33/r0/m43–44.** The worker successfully writes empty content to `/home/zby/llm/commonplace/.commonplace/worktrees/letta-code-workflow-be76afeab9b7-01/none`. No binding authorizes this path. m45–46 deletes it and removes the invented directory successfully. m47–50 writes the assigned identity and reconciliation report; later checks pass.

The successful removals establish local recovery. Neither trace establishes pre-existing valuable bytes at the wrong paths, so do not assert an overwrite loss. The workflow's recursive directory removal nevertheless reaches outside authority; “the final file is correct” is not retrospective authorization for either write or cleanup. I performed no cleanup during this audit.

**Disposition: retain recovery evidence; correct the compliance account; watch mutation containment.** Both events are new for these six runs and absent from the coordinator finals and supplied audits. They resemble the earlier, separately documented Letta Code identity-write incident, but are not that same event. Publication integrity remains supported; no additional out-of-scope write/edit call was demonstrated in the screened 253 calls and inspected shell destinations.

## H4 — Read coverage: two residual aggregate gaps, three recovered outputs

There are five actual outer Bash truncation markers across the six worker sets. Requested bounded file slices, source strings saying “truncated”, and notices about remaining file lines are not automatically delivery failures.

| Event | Delivered shell output | Recovery in the same worker | Disposition |
|---|---|---|---|
| GBrain L159/c18/r0/m13 | Only lines 9479–10878 of 10878; aggregate tracked-file listing | No read of the saved full output. m14–15 repeats source identity/root listing and computes grouped inventory; later source probes narrow the scope. | Watch: literal full-list delivery not recovered, but broad inventory exploration is not an exhaustive source-read obligation. |
| Graphiti L183/c18/r0/m30 | Only lines 598–877 of 877; aggregate notebook/source searches | No read of the saved full output. m31–32 extracts notebook code; later scoped source reads provide narrower evidence. | Watch: no whole-command coverage certificate; no demonstrated wrong accepted claim. |
| GBrain L159/c38/r0/m89 | Only lines 105–800 of 800 | m90–91 reads saved log lines 1–104. | Retain: explicit recovery of the omitted prefix. |
| GBrain L159/c52/r0/m72 | Only lines 53–927 of 927 | m73–74 reads saved log lines 1–60. | Retain: omitted lines 1–52 recovered, with overlap. |
| GBrain L159/c52/r0/m76 | Only lines 261–818 of 818 | m77–78 and m79–80 read saved log lines 1–130 and 131–260. | Retain: omitted prefix recovered. |

The saved-log paths are retained in the original Bash result markers; the subsequent read arguments exactly identify them. The last two events were already flagged by pilot **T2** as recovery not certified by that bounded scan. The deeper trace resolves that uncertainty favorably. It would be false to say the pilot documented an unrecovered failure there, or that this audit newly discovered those truncations.

The 1161-file input-range reconstruction found no missing nonblank line among its version-pinned bound files. In particular, it does not turn partial source reads into failed mandatory full-source reads. It also does not certify exact reading-batch order, full recovery of every exploratory no-match pipeline, model comprehension or exhaustive source coverage. **Disposition: retain the demonstrated input recovery; watch the two remaining aggregate delivery gaps, without elevating them to publication blockers.**

## H5 — Transport proposals: nine unmatched calls, recovered work

The nine-call difference is entirely inside workers:

- Graphiti L183/c26/r1/m76: one proposed edit, no matching result, and a stream-ended transport error. Subsequent edit/check work continues; a later deterministic error is repaired and validation passes.
- Napkin L189/c24/r0/m62: one proposed report write, no result, with the same stream-ended error. Later write/check calls complete the assigned output.
- Instinctual L207/c34/r0/m35: seven proposed reads of workflow, reconciliation, four analyst answers and report-check, no results, with a stream-ended error. Later matched reads recover those inputs; the pinned-input coverage check does not count the proposals as delivered reads.
- Instinctual L207/c52/r0/m39: a 503 upstream connection/reset error; no unmatched tool call is attached to this error. Later profile work resumes.

All four transport messages and all nine unmatched calls were already documented as **O3** in the five-run audit. None occurred in the GBrain envelopes. The coordinator finals omit them, but the prior audit did not miss them.

A proposed call is not proven executed merely because it appears in assistant content. Absence of a result also does not prove an interrupted edit/write had no external effect. Subsequent assigned outputs and byte checks establish the final artifact effect, not exactly-once transport behavior. **Disposition: retain the recovery and trace evidence; watch effect ambiguity rather than counting nine failed jobs.**

## H6 — Acceptance and completion were not publication-byte drift

The six coordinator final responses say publication completed and preserve inspect output, including its warning that completion is not a fresh filesystem audit. Their finals have no open/failed attempts or canonical-peer drift. Historical stale acceptances are visible; they are not automatically current acceptance/version defects.

I independently compared the exact 13-file retained map for each run with `R/effects/publish.json["new"]`, all working Markdown members with worktree retained bytes, and origin's integrated files with worktree retained bytes. All **78 published files** agree with their journals and integrated copies; all **72 Markdown members** agree with working members. The working and published manifests have different roles and were not required to be identical. Every published digest has a version blob. All **539 version blobs** have filenames matching their SHA-256 contents: 98/103/87/81/81/89 by system. All six source checkout HEADs match `source-revision` and have empty `git status --porcelain`.

This is a fresh byte/provenance check, not a fresh target execution or a new semantic audit. Frozen-set validation passes and receipt/manifest checks from the supplied audits remain attributed to those audits; I did not rerun the frozen sets' validators or an engine inspect command here. The status lineage and exact GBrain/Instinctual judgments inspected in H1 explain the relevant acceptance transitions. No direct primary-output write/edit after that worker's final passing validator was found; shell-generated destinations were inspected separately. These checks do not prove every semantic judgment holds under every historical peer version.

**Disposition: retain publication evidence.** Correct “all obligations satisfied” interpretations, not the narrower true statement “publication job completed.” No new false coordinator claim of independent filesystem validation was established. For Instinctual and the two GBrain workers, final success hides a missing worker check only if success is read more broadly than the frozen driver defines it.

## What is new, and where it was absent

“Retained reports” below means the six integrated analysis sets, not this workshop's audits. Their purpose is source analysis, not a complete runtime incident ledger. Absence from them is not automatically an authoring defect. Coordinator finals are a separate surface; the supplied prior audits are a third.

| Evidence | Coordinator final narratives | Integrated analysis sets | Supplied prior audits | This review |
|---|---|---|---|---|
| Two GBrain problem/output closures and false explanations | Not disclosed | Problem text not retained as a run incident; later content repairs represented | Not identified by the bounded pilot | New consequential status evidence; recurrence in a second run |
| Instinctual problem/output closure | “Stops: None”; problem not disclosed | Problem text not retained; same epistemic bytes published | Five-run O2 explicitly documents it | Confirmed; frozen driver adjudication and comparison extended |
| Six Letta masked structural shell results | Not disclosed | No incident ledger | Five-run audit expressly leaves constituent statuses uncertified | Newly established masked-status events |
| Two Letta out-of-scope writes and removals | Not disclosed | No incident ledger | Not identified for this run | Newly established recovered authority violations |
| Two boundary aggregate-output gaps | Not disclosed | Bounded source accounts, not full output delivery | Not specifically identified | New limited delivery findings; no accepted-claim error established |
| GBrain verifier truncations | Not disclosed | Source account remains bounded | Pilot T2 flags uncertainty | Recovery established, not a new failure allegation |
| Bad validator paths, quotation repairs, semantic/profile repairs | Mostly final status only; historical attempts remain in inspect | Relevant analytical repairs/limits retained, not full command history | Explicitly documented in the prior audits | Broader counts, no relabeling as newly missed incidents |
| Four transport errors/nine unmatched proposals | Not disclosed | No transport incident ledger | Five-run O3 explicitly documents them | Confirmed recovery and limits |
| Publication-byte agreement | Finals qualify completion as not an independent audit | Published bytes retained | Independently checked previously | Fresh agreement check, not a new substantive characterization |

These observations support status-contract adjudication and mutation/status monitoring, not a controlled estimate of method failure rates. The six systems are a purposive sample; workers and retries are not independent runs. The supplied reports retain timing boundaries and repair costs. This deeper review does not replace their descriptive timing comparison or attribute those costs to the newly expanded trace coverage.

## Reproducing an anchor without exposing reasoning payloads

The parent session contains nested evidence even without standalone child session files. This minimal read-only extraction pairs a selected result by exact ID and emits only tool text. Change the indices for the anchors above; do not dump all assistant blocks or signatures.

```python
import json
from pathlib import Path

trace = Path("/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--/2026-10-11T15-31-10-091Z_01a12b96-de8a-711e-8a12-57ef261a7126.jsonl")
line, c, r, m = 159, 22, 0, 64
with trace.open() as stream:
    row = next(json.loads(s) for i, s in enumerate(stream, 1) if i == line)
coordinator = row["message"]["details"]["results"][0]
worker = coordinator["messages"][c]["details"]["results"][r]
result = worker["messages"][m]
calls = {b["id"]: b for event in worker["messages"]
         for b in event.get("content", []) if b.get("type") == "toolCall"}
call = calls[result["toolCallId"]]
assert call["id"] == result["toolCallId"]
print(call["id"], call["name"], call["arguments"])
print("isError:", result.get("isError"))
print("\n".join(b.get("text", "") for b in result.get("content", [])
                if b.get("type") == "text"))
```

For this anchor the full matched ID is `call_5gTfEoLVB4QWPRZD9GQAvxEy|fc_06009f1fdc3f05a4016acc1c2c06c087d2915b20ed44bd5fdd`. The GBrain line 159 SHA-256, including its newline, is `c4257c59fb7df5178839bb6907f51dc9db2f07f28e4e22a801de8062ceb82384`, matching the pilot's anchor. Attempt JSON and judgment filenames in H1 independently locate the pinned output and repair lineage. No encrypted reasoning content is needed for any finding.

## Validation and final boundary

Only this Markdown report is an authored validation target. The narrow command returned exit 0:

```text
commonplace-validate kb/work/analysis-audit-evidence/reports/workflow-six-run-hidden-failures.md
VALIDATION SUCCESS
Files analysed: 1
Text files: 1
Diagnostics: 0 failures across 0 subjects; 0 warnings across 0 subjects
```

Exact-ID duplicate/orphan checks passed for all 90 analytical-worker/coordinator envelopes. Final Git status review showed this report as the only newly authored path from this invocation; the pre-existing concurrent edits and five-run report remain untouched. No pytest, target tests, run advancement, source changes, integration or cleanup was performed. Broader graph connection through `cp-skill-connect` would require separate authorization and is not performed here.
