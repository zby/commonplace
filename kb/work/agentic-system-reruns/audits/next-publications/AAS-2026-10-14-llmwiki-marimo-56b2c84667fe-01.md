# llmwiki-marimo exact-publication audit

## Disposition

**hold** — the bounded semantic checks found no consequential defect requiring a public correction, but executed synthesis-worker calls crossed the assigned write boundary. An empty answers file was written under a different sibling directory and then removed. Whether the write overwrote pre-existing content is not established. Integration must not silently waive that ownership question. This is an operational hold, not a demand to repeat the analysis or add an audit-only qualification to its public claims.

The coordinator retains scheduling, full review, acceptance and integration. Nothing was integrated, recovered, cleaned up or delegated by this audit.

## Exact identities and inspection method

- `run-id`: `AAS-2026-10-14-llmwiki-marimo-56b2c84667fe-01`
- `method-commit`: `a568c6dc489ad546374536b642c3889ce23149a8`
- `source-revision`: `0b5d95b1663c4ca859ab554da40924d5091eb6ed`
- Source identity: `https://github.com/Clod/llmwiki-marimo` (Git; publication source ID SRC-1).
- Worktree: `/home/zby/llm/commonplace/.commonplace/worktrees/llmwiki-marimo-56b2c84667fe` (below, W).
- Command prefix: `W/.venv/bin`.
- Source checkout: `W/related-systems/Clod--llmwiki-marimo` (below, S).
- Publication: `W/kb/agentic-system-analyses/retained/llmwiki-marimo` (below, P).
- Run evidence root: `W/kb/agentic-system-analyses/state/AAS-2026-10-14-llmwiki-marimo-56b2c84667fe-01` (below, R).
- Trace: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/batch-13/llmwiki-marimo.output` (below, T).
- Auditor: independent Pi worker; runtime environment reports `PI_PROVIDER=openai`, `PI_MODEL=gpt-6.1-sol`, `PI_REASONING_LEVEL=medium`.

Read the complete commission, audit procedure, earlier substantive commission, root instructions, workshop framing and work collection contract. Read this exact inventory row, not adjacent assignments. The bounded method was discrepancy-led: compare historical retrieval/admission/maintenance/recovery coverage with the public synthesis; inspect the pinned implementations that discriminate changed mechanisms; examine retained judgments and selected completed worker transcripts for consequential operational differences. Historical assertions were leads, not truth.

## Byte and publication identity

Worktree HEAD equals the method commit. Source HEAD equals the source revision and `git status --porcelain` in S was empty. Worktree status showed only the untracked retained publication. The actual publication has exactly the 13 files below; every SHA-256 matched the inventory. The completed `R/effects/publish.json` has the same new-file map, exact run/source identities, destination P and expected prior state `absent`. `R/state/attempts/000037-publish.json` is completed. No origin incumbent was named in the supplied row; no substitute or replacement was evaluated.

| File | Verified SHA-256 |
|---|---|
| ARTIFACT.yaml | `215c62bc9c7e22de8349bfce75f66bf9d5e93c1a41d9a738f47a84ceeac5f830` |
| boundary.md | `c8f4e32d8cd2127c61a0e3eece5365183c87f9aae2fd03a87305d3fc69dc4e56` |
| epistemic.md | `4117032ef412905ee613b99c70cc7d742ef3fd802247451271738a0ba8f774f3` |
| memory-profile.md | `287fb0a291b770b05f43ff943a9d910edb5c2876b25d255f155dabb2b3ca6458` |
| memory.md | `ceaaf8da00dbd734b2c331413f4ab0b9edebb9bb0cc7917b04b4c99574e32973` |
| overview.md | `b1c61ef40e2108a73d9b5ebcdcae60c2b530f1739c5f718964ee34f434ce6309` |
| profile-verification.md | `24fc3dda91d25361bc4952729c19f69692b931800e8952f06e3efed41ac28587` |
| reconciliation.md | `22257cf46a527e863c988290153af4163b2822e7297b2202debc715e3552f326` |
| report-verification.md | `51fc0f732b724ea318cb8a5f9cae2c53bb34c9136fddf24330359ea41490c5a7` |
| runtime.md | `a44ee0d9b85fefca6b7a8ef2cbba240c0332e74cee3f4a91ab9b22ceb5a42bfb` |
| synthesis-verification.md | `75cccf7d8f3edad4fc9b60f974399752272d3db94aefbeaa88657e417229b530` |
| synthesis.md | `7ab0c01677323711ba51a47132c85072f984a3723c36ccf73e41658460de2068` |
| workflow.md | `0041cda55502339f6658179777ea014f10fd73ac7956ca1279510447bff600c9` |

The publication manifest is the assembled manifest, not the type-only working declaration. Its hash differs from the inventory's working-declaration hash `093c6e4a6c7cab7e4e1a9db63f6d2d45eec6a24bf51f7b287dd1db929b388322` as expected.

## Historical comparison and public qualifications

The sole historical account inspected was `kb/agent-memory-systems/reviews/llmwiki-marimo.md`, dated 2026-06-18 and attributed to revision `0dc8e731df6a4bbb03926b17a891d03736f1267a`. Its older checkout was not acquired or inspected. This is a comparison of retained coverage with current pinned implementation, not certification of historical accuracy or a commit-by-commit migration study.

1. **Retrieval is no longer adequately described as one prompt-directed pull cascade.** The new public synthesis distinguishes web-default pre-retrieval, strict tool retrieval and streaming. S `base/services/chat.py:220-303` implements separate pre-retrieval and strict branches; the latter checks `result.all_messages()` with `has_grounding` and `enforce_grounding`. S `base/domain/chat/agent.py:143-169` makes wiki tools conditional and permits injected tools. The route search in S `web/routes/chat.py` shows the default `PRE_RETRIEVAL` argument. P `synthesis.md`, “From retained pages to an answer,” already limits the predicate to tool-result presence, distinguishes streaming and avoids an entailment guarantee. This corrects/extends the old lead rather than losing its central mechanism.
2. **Human initiation is not universal approval of generated content.** S `base/services/chat.py:380-489` separates `draft_conversation`, `save_reviewed_page` and immediate `save_conversation`; the last explicitly drafts and saves without intervening review. S `base/domain/chat/wiki_tools.py:285-410` likewise separates drafting/writing and composes them in `save_to_wiki`. S `web/routes/chat.py:213-314` implements review, optional verification and a save endpoint without a required draft token or verdict. The public synthesis explicitly carries these route distinctions, including the save's nontransactional tail. The new dialogue-derived-page account does not confuse diagnostic trace files with learning or claim observed benefit.
3. **Recovery improves on an old watch item without becoming complete rollback.** S `base/domain/tools/reindex.py:1-32` describes no-model reconstruction from files, preserved Markdown, reconstructed references and lost DB-only metadata. S `base/domain/rollback/revert.py:34-40` limits tracked roots to wiki, ignore rules and configuration. P `memory.md#mem-obj-index-metadata`, runtime history restoration, and the public synthesis retain reconstruction/snapshot differences and missing generated-selector sidecars. The historical claim that rebuilding necessarily re-invokes generation must not be carried forward as current truth.
4. **Maintenance, references and diagnostics remain visible, not certified semantic repair.** P memory's maintenance route retains automatic generation, deletion, cross-links, warnings and stale-search countercases; its index object names `document_references`. The synthesis preserves warning-versus-adjudication, optional diagnostic verification and incomplete maintenance/evaluator coverage. It does not claim a graph retrieval strategy or exhaustive enforcement. These inspected public qualifications are sufficient for the bounded comparison; individual repair handlers and every graph consumer were not independently re-audited.

The overview description itself limits truth/improvement claims, and its validation section explicitly rejects semantic certification. The linked public synthesis states no target execution, provider call, passing tests, route-linked target trace or causal experiment. It exposes partial inventory, model identity/calibration, recovery and dataset-freshness limits. No missing public qualification was established in the selected checks.

## Operational evidence and hold

T is readable and contains this exact run. I streamed JSON and used completed top-level `tool_execution_end` subagent results, then paired assistant `toolCall.id` with `toolResult.toolCallId` inside each worker's own `messages`. Repeated stream updates were not counted as extra actions.

### Performed work, refusal and revision

- T line 2598 contains the completed `000022-report-verification` worker transcript. Its call `call_0Sd00kRnYQj731Z1QOSKswWm` (full ID prefix before `|`) read S `base/domain/chat/wiki_tools.py:198` onward and has a returned source result; `call_Zg5K6eXe4nufH8IY8H33Hd84` read the offline verification battery with a returned result. These substantiate actual source inspection behind the admission and evaluator qualifications, not just a verifier's assertion.
- The same worker's attempted quote edit `call_k3llq3vuYutktORs4OKZqtZL` returned an error: `Could not find the exact text ... The old text must match exactly including all whitespace and newlines.` Subsequent paired reads inspected the candidate; its final `validate-output` call `call_xmhHFerxNcseFrNbxCrqRBMA` returned `Member content check passes; invocation residue not checked. This is not job acceptance or claim support.` This was a failed edit, not a successful correction or engine refusal.
- Retained judgment `R/state/judgments/000027-apply-profile-verification-1.json` semantically refused the original profile: it understated implemented alias deduplication and wrongly attributed validation authority to dataset fields merely being checked. T line 3624's completed `000028-memory-profile` worker pairs an actual edit (`call_vzNPbwlAicu3vbsv42IuOWC7`) and correction answers with results; its validation returns a content pass. The revised profile hash is the published `287fb0...`. T line 3958 contains the subsequent verifier's actual input reads and validation. Judgment `000031-apply-profile-verification-1.json` accepts that revised profile. This is evidenced correction and rejudgment, not acceptance inferred from publication alone.

### Executed write-scope violation

T line 4299 contains the completed `000032-synthesis` worker transcript. Inside that worker:

- Message index 57: write call `call_SaHChggf1O6iT1sHMC06ijbM|fc_0d1301412abd698a016acfe9d9a99087d28af1a9c417ec557c` supplied empty content to `/home/zby/llm/commonplace/.commonplace/worktrees/llmwiki-marimo-56b2c84667fe-01/kb/agentic-system-analyses/state/AAS-2026-10-14-llmwiki-marimo-56b2c84667fe-01/state/handouts/000032-synthesis/outputs/answers.md`. Its paired tool result says `Successfully wrote to` that exact path.
- Message index 59: Bash call `call_pHd4QI5ZPSYFJYDRznyYw4v2|fc_0d1301412abd698a016acfe9e0a66487d2a65de24a7037610d` ran `rm` on that wrong-path file. The paired result reports `(no output)` and no error. This evidences an executed removal command, not a proposed cleanup; the record does not show a pre-write existence check or prior bytes.
- Message indices 61 and 63: paired writes created the synthesis, empty answers and worker identity under the correct W path. Message index 66's `call_IcrC26175Nl5IYiskMuGT0Ut` ran the supplied content check and returned a pass with the same invocation-residue disclaimer.

The extra `-01` in the sibling worktree directory is not part of W. The pinned `follow-worker-rules.md`, “Stay within authority,” permits only supplied outputs/problem/identity and scratch, and explicitly forbids other workspace files. The wrong-path write and removal violate that rule. Later correct output and validation do not erase the deviation. The inspected sequence establishes an empty write; it does not establish whether another owner's file existed beforehand, whether directories remain, or whether unrelated state was affected. This audit did not inspect or mutate the foreign directory or attempt cleanup. Determining its prior ownership and effects would exceed this bounded report's scope.

## Validation

Executed from W using the recorded absolute prefix, without `--output` or state-writing commands:

```text
W/.venv/bin/commonplace-validate kb/agentic-system-analyses/retained/llmwiki-marimo
VALIDATION SUCCESS
Target: kb/agentic-system-analyses/retained/llmwiki-marimo
Scope: kb/agentic-system-analyses/retained/llmwiki-marimo
Files analysed: 1
Text files: 0
Diagnostics: 0 failures across 0 subjects; 0 warnings across 0 subjects
VALIDATION_EXIT=0
```

The CLI reports one set target; this is not a claim of 13 independently counted file checks or exhaustive semantic compliance. No notices were emitted by that invocation.

Owned-report command, also from W:

```text
W/.venv/bin/commonplace-validate /home/zby/llm/commonplace/kb/work/agentic-system-reruns/audits/next-publications/AAS-2026-10-14-llmwiki-marimo-56b2c84667fe-01.md
VALIDATION SUCCESS
Files analysed: 1
Text files: 1
Diagnostics: 0 failures across 0 subjects; 0 warnings across 0 subjects
VALIDATION_EXIT=0
```

No notices were emitted. This checks the frontmatter-free workshop report as text, not the truth or completeness of the audit.

## Limits and concrete unblock conditions

This is not a second full analysis. I did not execute the target, acquire sources, examine the older checkout, certify all worker obligations, verify every quote semantically, or enumerate every repair/evaluator/security path. No absence of violations elsewhere is inferred. Report existence, worker exits, deterministic acceptance and exact publication bytes establish different facts.

To unblock this operational hold, the parent/operator must establish the ownership and collateral effects of the exact wrong-path write/removal, using authorized evidence: whether a pre-existing file was overwritten, whether any other run was affected, and whether remaining directories need a separately authorized disposition. If collateral damage is excluded or resolved, the parent must explicitly decide whether to accept the recorded worker-scope deviation. Do not rerun or patch this publication merely to obscure it. After that decision, unchanged bytes are eligible for **integrate with recorded limits** on the semantic scope inspected here, subject to the parent's full review, fresh byte-map verification and integration authority. Any changed publication requires a renewed exact-byte audit.
