# EchoWiki current-batch audit

## Disposition

**Integrate with recorded limits.** No consequential characterization defect was established in this bounded audit. The published synthesis already carries the queue-recovery exception, incomplete source preservation, direct replacement risk and lack of observed fidelity or improvement. Integration must not be described as certification that every worker obligation was fulfilled: the profile worker made and removed an unauthorized empty file outside its assigned workspace.

Blockers: **none for publication integration**. The coordinator should retain the operational deviation below when accepting this audit; acceptance does not retroactively authorize it.

## Identity and auditor profile

- Exact inventory row: EchoWiki, batch 03, `AAS-2026-10-14-echowiki-8d428f79523e-01`.
- Prepared worktree: `/home/zby/llm/commonplace/.commonplace/worktrees/echowiki-8d428f79523e`.
- Publication: that worktree's `kb/agentic-system-analyses/retained/echowiki/`.
- Stored run: that worktree's `kb/agentic-system-analyses/state/AAS-2026-10-14-echowiki-8d428f79523e-01/`.
- Frozen source: `https://github.com/mohammadmaso/echowiki`, local registered root `related-systems/mohammadmaso--echowiki` in that worktree. Actual HEAD and boundary/acquisition pin agree on `11446997423e88177dba62d6a3d5c1e8b4886c62`; source status was clean. Cutoff: 2026-10-14; implementation and doctrine/design only.
- Method/input revision: preparation and overview name `4266dabc470929df0ff753e57fee0c55d7b87fc6`. Stored `run.json` pins plan SHA-256 `5a5f56891d95a819c3f4fde00bb92eb301876598c022924ee52bed6262721bfd`; the worktree plan hashes to that value.
- Auditor: fresh Pi session `01a138f7-9140-765f-8139-d5bfc0419627`; Bash environment states `PI_PROVIDER=openai`, `PI_MODEL=gpt-6.1-sol`, `PI_REASONING_LEVEL=medium`. No delegation. Depth/nesting limit not exposed.
- Run manifest: `pi-sol`, Pi, launch model `gpt-6.1-sol`, medium; all eleven model attempts report `openai/gpt-6.1-sol`, medium.

## Method and historical boundary

I used discrepancy-led comparison, source spot checks and stored-state/trace inspection, not a second analysis. I read the overview, boundary, synthesis and all three verification reports completely. I compared the exact legacy account linked by the EchoWiki row in `systems.md`: [legacy review](../../../agent-memory-systems/reviews/echowiki.md). Search of `kb/agent-memory-systems/` also found three replaced July accounts. No moved EchoWiki account was found under `kb/agentic-systems/reviews/` or `reviews-archive/`. The linked current legacy account, rather than those superseded variants, is the comparison baseline.

Both old and new accounts pin the same source commit. Differences therefore are analytical changes, not evidence of an upstream upgrade. Historical claims were leads only. I independently read the complete frozen `src/wiki/compiler.ts`, `src/wiki/page-writer.ts` and `obsidian-plugin/src/main.ts` to check consequential differences. No new source acquisition, target execution, tests, provider calls or run advancement occurred.

## Consequential findings

1. **The core historical coverage survives.** Both accounts characterize a file-backed Obsidian/CLI compiler, not a deployed query agent or vector retrieval system. Both retain all-brief planning, selected prior-body reuse, editable compiler instructions, upstream approval, incomplete archival pointers and prompt-only protection of human edits. The new synthesis supplies a more precise production-to-consumption progression. The Mastra/Vercel design-versus-code discrepancy remains visible in the boundary. Removing the old Commonplace borrowing recommendations is not a characterization regression under the new analysis purpose.

2. **The new link guarantee is appropriately narrower than the legacy wording.** The legacy account says the whitelist prevents arbitrary links and strips impossible targets. Frozen `compiler.ts` constructs `knownTargets` from existing **and planned** names before successful generation, skips failed tasks and still cleans against that set. The new synthesis explicitly warns that an admitted planned link may lack an eventual target. No repair is needed.

3. **Source lineage and replacement risk are not hidden.** `writeSummary` emits `full_text: sources/<doc>.md`; the inspected compiler and plugin compile path do not copy raw source there. The plugin creates the directory, which is not an archival write. The published synthesis expressly withholds recoverable claim-level evidence. Generation only loads an old body for update tasks. Entity writes derive `isUpdate` from actual existence; concept writes keep the plan branch. The synthesis correctly distinguishes semantic replacement risk from identical metadata loss across both branches.

4. **Approval failure retention has a real concurrent exception, already published.** In frozen `main.ts`, `compilePendingItem` removes the queue entry after `compileRawPath` resolves. The same-path in-flight guard can resolve immediately while another compile remains active. The sequential guarantee therefore cannot be universal. Report verification retains this as a limit; the synthesis's delivery paragraph and limitations table explicitly carry the exception and warn against queue disappearance or UI completion as delivery evidence. This audit does not need to repair the publication by adding a qualification only here.

5. **The learning classification is conservative, not a demonstrated loss of capability.** The old account's “learning authority” describes retained-page influence and also says faithfulness was not tested. The new account preserves automatic later context supply but distinguishes that wiring from improved capacity. Profile verification records an overly cautious `trace_learning: not-determinable` overview despite a local log-feedback “no”. The synthesis explicitly preserves that local negative and unresolved generic-input/provider branches. Neither a positive trace-learning route nor a system-wide negative is established. This is an already-visible comparison limit, not an unsupported benefit claim.

## Publication and operational evidence

Read-only JSON inspection found all 33 stored attempts completed and all stored judgments accepted with empty findings. `effects/publish.json` records a completed publication at the exact inventory destination. Independently computed hashes match all thirteen entries in its `new` map. All twelve Markdown members are byte-identical to the working artifact; only `ARTIFACT.yaml` differs, by publication's addition of member hashes and worker identity. These facts establish stored engine completion and file identity, not universal worker compliance.

The raw batch stream `kb/work/agentic-system-reruns/outputs/echowiki.output` retains nested worker messages in completed `subagent` results. I paired tool calls with results by exact IDs within each worker. All eleven model-role results have exit code zero and contain executed `commonplace-run validate-output` calls ending in the member-content pass message. Memory, epistemic and profile workers also retain earlier failed preflights and subsequent passes; these are candidate repairs, not engine refusals or missing final checks. The profile/synthesis verifiers' matched reads contain handed records and contracts, not target-source reads, consistent with their published “Source-read log: none”. Report verification has extensive matched frozen-source reads.

**Established write-scope deviation:** at stream line 2832, worker `000024-memory-profile` executed write call `call_RCWKKjmt5oh7ctvwJiFwOl6w|fc_0c031f37b633b62c016aceebddf08c87d2bf43ba80ff92c8a1`, creating an empty `/home/zby/llm/commonplace/.commonplace/worktrees/echowiki-8d428f79523e-01/kb/unused`. Its matched Bash call `call_EI2Q2Acf0po5YZoRU8Njd3fS|fc_0c031f37b633b62c016aceebe788b087d2b70e7302d876dd4a` removed that file and its empty parent directories. Both are outside the authorized handout workspace. The worker's later scratch repair-log write acknowledges the accident. The published output hashes still match accepted products; this isolated empty-file excursion establishes no semantic contamination. It prevents claiming full write-boundary compliance, not acceptance of the bounded characterization.

I did not exhaustively audit every read range, exit-status-handling obligation, write path or nested reasoning statement. Worker traces are present, but trace availability and successful checks are not a blanket compliance verdict.

## Validation

Used the sibling preparation record's command environment: from the prepared worktree, with its `.venv/bin` first in PATH, called `commonplace-validate` by bare name. No output-file option was used.

Publication command:

```bash
commonplace-validate kb/agentic-system-analyses/retained/echowiki
```

Actual output:

```text
VALIDATION SUCCESS
Target: kb/agentic-system-analyses/retained/echowiki
Scope: kb/agentic-system-analyses/retained/echowiki
Files analysed: 1
Text files: 0
Diagnostics: 0 failures across 0 subjects; 0 warnings across 0 subjects
```

The directory is counted as one set artifact, not twelve independent file targets. Validation is deterministic, not semantic certification.

Report command:

```bash
commonplace-validate /home/zby/llm/commonplace/kb/work/agentic-system-reruns/audits/bash-current-echowiki.md
```

Actual output:

```text
VALIDATION SUCCESS
Target: /home/zby/llm/commonplace/kb/work/agentic-system-reruns/audits/bash-current-echowiki.md
Scope: /home/zby/llm/commonplace/kb/work/agentic-system-reruns/audits/bash-current-echowiki.md
Files analysed: 1
Text files: 1
Diagnostics: 0 failures across 0 subjects; 0 warnings across 0 subjects
```

## Coverage limits and follow-up

No target runtime outcomes, private vault, source/output pairs or controlled benefit comparisons were supplied or created. The new publication already states these limits. This audit is not exhaustive defect enumeration or proof of deployed reliability. It did not independently reconstruct every analyst record or every comparison unit.

No unblock condition is required for the recommended integration. If the coordinator requires strict worker-scope compliance rather than publication acceptance with an acknowledged operational deviation, that stricter decision must return to the operator; this audit does not authorize rewriting or retrying the frozen run.
