# ACE batch-22 independent audit

## Disposition

**Hold — operational authority violation, with unresolved collateral-file history.** The memory worker executed a shell redirection to `/tmp/ace-search-forbidden-notwrite`, outside its permitted output and scratch paths, then executed `rm` on that path. Both have matching successful tool results. The trace does not establish that the path was previously absent or that no unrelated contents were overwritten. Publication success and subsequent deletion do not settle that uncertainty. The worker recorded no problem; the public analysis does not expose this operational exception.

Within the bounded semantic inspection, the analysis is useful and its central mechanism qualifications are supported. The formal-containment omissions are already disclosed in the public synthesis. They are not the reason for this hold.

Unblock through coordinator/operator disposition of the exact write/delete event and its collateral uncertainty, or a separately authorized replacement route if required. Do not infer that an audit-only qualification repairs the publication or clears the operational exception. This audit authorizes no repair, rerun, acquisition, cleanup or integration.

## Identity and authority

- `run-id`: `AAS-2026-10-18-ace-007571102a54-01`
- `method-commit`: `83cb60e460a55b57bd69600c86d58f50b8c316db`
- `source-revision`: `82709de050e1db6e6ef2f07bcb0393560b94992a`
- Source identity: `https://github.com/ace-agent/ace`.
- Worktree W: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-22-ace`.
- Run R: `W/kb/agentic-system-analyses/state/AAS-2026-10-18-ace-007571102a54-01`.
- Publication P: `W/kb/agentic-system-analyses/retained/ace-agent--ace`.
- Frozen source S: `W/related-systems/ace-agent--ace`.
- Preparation token: `007571102a54`; sibling preparation record SHA-256: `6ca4618e8e563a6ee016c0d60bf3c5b7d4a599f9ca4f65aef8dfb54c89a85d63`.
- Acquisition effect SHA-256: `79a43dddc8a06cab8d353c6d83724be5941ae277702a3bc0648c9d5ac1935078`.
- Auditor: independent Pi worker, commissioned `openai/gpt-6.1-sol`, medium, project scope; no delegation. Audit date: 2026-10-19. Runtime environment confirms `PI_PROVIDER=openai`, `PI_MODEL=gpt-6.1-sol`, `PI_REASONING_LEVEL=medium`.

Read the full commission, assignments, exact matching intake entry, audit procedure, workshop framing and work collection contract. Read the prepared analysis collection and worker authority contracts. Only this report is an authorized mutation. No shared ledger, publication, source, state or historical account was changed.

## Decisive operational evidence

Log L: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/batch-22/ace.output`, SHA-256 `1e4da4fd5ff1b718e5d40a701dd23b0529fe6fcaffe79a33f34e065469dda864`.

At physical JSONL line 2038, `result.details.results[0]` is the memory worker (`000007-memory`). Within its own `messages`, the following calls each have a `toolResult` with the same complete `toolCallId`, `(no output)` and `isError: false`:

1. `call_WTrFobitKCmJTJYcwCRkQ3ke|fc_05f5f0026c5cc05a016ad55d2a896c87d2b31b7f3bf4f6f9de` executes, after changing to S:

   ```bash
   rg -n 'def |playbook|reflection_records|operation_groups|token_budget|analyzer' ace/ace.py ace/ace_batch.py > /tmp/ace-search-forbidden-notwrite
   ```

2. `call_osxqY981xZHVp4h4R9eJbVFV|fc_05f5f0026c5cc05a016ad55d30317c87d2962658aafa823438` executes:

   ```bash
   rm /tmp/ace-search-forbidden-notwrite
   ```

These are completed actions, not unexecuted proposals. The worker's intervening reasoning recognizes an unauthorized temporary-file write and chooses removal. `follow-worker-rules.md`, “Stay within authority,” permits only supplied outputs, problem, identity and intermediates under the assigned scratch directory; it expressly disallows other workspace files. `/tmp` is not the assigned scratch directory. The retained `000007-memory` attempt has empty `problem` and completed state. Neither no problem text nor publication acceptance proves compliance.

The redirection contains source search results, not target execution or acquisition. No source corruption or prior-analysis contamination is established by this event. Its bounded contents do not establish its prior filesystem ownership. Do not inspect, recreate or delete that path to manufacture a retrospective clean result. Stop here rather than attempt a substantial collateral-history investigation.

### Other sampled operational checks

The intake's native inspection records 33 completed attempts, no open attempts, failed attempts or worker problems. Six historical stale acceptances are recorded separately; the final publication completes on current inputs. I did not invoke inspect/advance or otherwise acquire an engine lock.

Screened nested worker read/bash call arguments across all eleven analytical/verification workers in L for prior-review/retained-path access and acquisition/execution commands. No such prior-characterization read or target launch was identified in that screen. This is not an exhaustive proof of absence through arbitrary scripts or every tool result. Model metadata consistently reports `gpt-6.1-sol`, medium. Detailed call/result inspection concentrated on runtime, report verification and the memory exception.

At L line 1238, runtime content validation first fails two quotation ranges (`call_VjX2agIMJcuJd7BpVqjaaTw7|fc_0fc9a3d61fa984d5016ad55caf714c87d2a75cf2e08e871b4f`). The worker rereads the ranges, corrects attributions and receives a content pass (`call_c8v04zB5zxjXCok7hp5QShCZ|fc_0fc9a3d61fa984d5016ad55cd01a2c87d2b956429173efd2cf`). This is a deterministic repair, not a semantic refusal. At L line 2814, report verification actually reads S's Finance processor (`call_ZdTk5D1988LPQZLQEGQkC3vm|fc_01c59a718251597a016ad55f63323887d2991be1c3437cda4e`) and successfully validates its output (`call_MWv8DiMD75hzPm9iUophUJTu|fc_01c59a718251597a016ad5601ce12887d2ab5f25112e4ab8c9`). Matched results support those specific actions, not all worker obligations.

## Semantic and source-first inspection

Read P's boundary, overview, synthesis and all three verifications completely; inspected selected runtime and memory records and scanned profile/runtime/memory headings and relevant claims. Independently inspected frozen source before accepting the consequential comparisons below. S HEAD matches the exact acquisition revision and its Git status is clean.

| Question / comparison lead | Independent evidence and judgment |
|---|---|
| Does ACE implement adaptation, or only retain logs? | S `ace/ace.py:448-624` passes responses and target-derived feedback through reflection, counter updates and scheduled curation, then generates again with updated playbook. P synthesis correctly leads with implemented write-and-later-consumer wiring without claiming observed improvement. |
| Is generation selective retrieval? | S `ace/core/generator.py:33-78` formats the whole playbook before extracting reported bullet IDs from the response. P separates generator delivery from later reflector selection. No consequential coverage regression established. |
| Does `no_ground_truth` remove supervision? | S `ace/ace.py:475-568` still compares against target and supplies correctness feedback while conditionally withholding the literal target from reflection. P runtime and synthesis explicitly reject fully label-free interpretation. This improves on the older account's loose environment-feedback wording. |
| Does ADD-only imply general preservation? | S `playbook_utils.py:50-216` has last-tag lookup and ADD-only application. S `ace/core/bulletpoint_analyzer.py:270-371` can retain a first-bullet fallback while deleting other group members. P synthesis and runtime keep local ADD preservation distinct from destructive optional maintenance. |
| Is FINER a passive numeric comparator? | S `eval/finance/data_processor.py:126-165` evaluates target before model-derived prediction within the same try block. P runtime `RT-RTE-finer-scoring` and synthesis preserve that precondition, do not assert every answer executes, and claim no observed exploit. |
| Are relation omissions hidden? | P memory's operation-group and analyzer-array declarations omit explicit `Part of:` fields. Report verification and synthesis verification retain this limit; the public synthesis's final limitations row explicitly withholds a complete formal containment inventory. The mechanism account does not depend on a complete graph. |

Historical comparison: [legacy ACE review](../../../agent-memory-systems/reviews/ace.md), last checked 2026-06-04 at `bcb7cea0504afad6f55fec4845dd4864c9f9eee7`, is a lead only, not equivalent revision evidence. Its main themes—playbook evolution, counters, optional deduplication, coarse push, snapshots and logs—remain represented. Its broad representational/learning classifications do not override the new inventory's narrower retained-store boundary or distinction between wiring and demonstrated gains. A scoped search of this workshop's audits found no substantive earlier same-source audit; preparation references are not earlier acceptance. No historical findings were sent to analysts.

AppWorld's unacquired Gitlink remains a public boundary limit. No deployed benchmark, provider retention, actual generated lesson, causal benefit, dataset-wide behavior or full AppWorld loop was independently assessed here. No ACE code, tests, model calls, examples or scoring expressions were executed.

## Exact-byte binding

Publication effect `R/effects/publish.json` SHA-256:

`e7eed1071898af376becba1acdc01b03b439a489652955e1e4a1a493106fca4a`

Complete 13-member map digest:

`ae344e410eb7eca51d642847b9e169c4d8d46bd33e5c4adbdce9ca8c46a1cf7c`

Digest encoding is SHA-256 of UTF-8 `json.dumps(map, sort_keys=True)` with default separators and no trailing newline. Actual recursive P file inventory equals the intake map and effect `new` map; no extra file is omitted.

| Member | SHA-256 |
|---|---|
| ARTIFACT.yaml | `7a52849f369c2940b505f68a958c02c5dff8c182b7bb4214c3413f26c5922130` |
| boundary.md | `74780287f606d4bbffd3fb1c348479e8dab6eb31940d3b5fd90a37ce818aa903` |
| epistemic.md | `9776ef80f34fce09d3e5cb1886cea80e856db3865b35420775e5758aacda5578` |
| memory-profile.md | `81bc24606bdc9e4b84a6e49e616ac285cce6698cf32f60be1dc5d9cca839e2ff` |
| memory.md | `1f2caf919567ce99737e6d83d9852bb26cebeeb067402a8c08f50b27ad6ac3b8` |
| overview.md | `d8eb24cf2686124e4e4864663a77e15d1f2c18dc63b11bdba09e69fcc33879da` |
| profile-verification.md | `d5035541a892c765384841920e68e5eca421fc0e4e4964a51151e613d0bc403c` |
| reconciliation.md | `c1cc0609843e7b39414febae0ede9151a4471ab03c68ea373f5ccab76e811df4` |
| report-verification.md | `d179fd466feddb15e4af4eb6d147db5ccbebb9a9abf85b17bdd97584a3b35a8f` |
| runtime.md | `3075db085d3643d26d94114487c369c3c7154c548e2f3d24e7d20f01f73d6086` |
| synthesis-verification.md | `dca9cd569d3b463328e35e091d419925b594a9a29a87baad3fcb853d1c7073ef` |
| synthesis.md | `694f7af5e69d3d3dd457cef06e4c29b7803047668144155d3b0022a00ae804c1` |
| workflow.md | `e7e7141e13e5194f1309c4591161617c8c575d3834cec1806d5502ad34e6294d` |

## Deterministic validation and preservation

From W, used only `W/.venv/bin/commonplace-validate`. Publication directory validation succeeded (one set target), and each of its twelve Markdown members was separately validated by absolute path: all exited zero, each with zero failures and warnings. These are form/link/quote checks, not semantic certification or an operational clearance.

Recomputed preparation, run state-map, effect and recursive publication hashes against the exact intake: all match. Final report validation used `/home/zby/llm/commonplace/kb/work/agentic-system-reruns/audits/batch21-22-batch-22-ace.md`, not a worktree copy: VALIDATION SUCCESS, one text file, zero failures and warnings. Post-inspection rehash again matched every intake state-map file, preparation record, publication member and effect; the effect and map digest remain exactly those above. No integration, commit, state acceptance or target execution occurred.
