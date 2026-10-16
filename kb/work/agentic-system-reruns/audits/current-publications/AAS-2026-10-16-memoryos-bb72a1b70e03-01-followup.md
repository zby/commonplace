# MemoryOS batch 18 — independent publication followup

## Disposition

**Integrate with recorded limits.** No additional consequential publication defect was established by this bounded audit. The analysis is useful as a source-grounded implementation account, not as evidence of exercised reliability, factual acceptance or improved dialogue. Its necessary qualifications are already public in `synthesis.md`, including the ChromaDB backup loss, capacity-eviction failure and incomplete mechanism inventories.

This completes substantive inspection for this exact publication after the earlier group audit stopped at mechanical binding. It does not rewrite or erase [the incomplete report](./AAS-2026-10-16-memoryos-bb72a1b70e03-01.md). That report remains evidence of what its session did not inspect. Parent acceptance and safe integration remain separate decisions. No restart, integration or state change was performed or authorized here.

## Identity and fixed inputs

- Run: `AAS-2026-10-16-memoryos-bb72a1b70e03-01`.
- Auditor: Pi; provider/model `openai/gpt-6.1-sol`; reasoning `medium`; session `01a146fa-c5d5-70e1-86f6-b55511dd5b28`, read from this process's environment. This is an independent single-case followup, not a producing-worker session. No delegation.
- Governing inputs read completely: `publication-audit-current-commission.md`, `audit-a-rerun.md`, `kb/work/COLLECTION.md`, `kb/types/text.md`. The commission's completed-own-publication authority governs this case; no active batch-18 evidence was inspected.
- Intake: `kb/work/agentic-system-reruns/publication-audit-current-intake.json`, freshly verified SHA-256 `29c5a94a2c926f9c8b895cf5a5f50b0157461fa2a8aff39779131d14ab6d530e`. Only its exact-run publication row supplied worktree, preparation, source, maps, historical lead and completed trace lead.
- W: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-18-memoryos`.
- P: `W/kb/agentic-system-analyses/retained/bai-lab--memoryos`.
- R: `W/kb/agentic-system-analyses/state/AAS-2026-10-16-memoryos-bb72a1b70e03-01`.
- S: `W/related-systems/BAI-LAB--MemoryOS`, source identity `https://github.com/BAI-LAB/MemoryOS`, frozen HEAD `587ed7755c7aed179965792830ff1b5ad9a6fa92`. Fresh source Git status was clean.
- Frozen method / fresh W HEAD: `12fcd86e09c75f946baf6143d6473fff1e1b0583`; run plan SHA-256 `5a5f56891d95a819c3f4fde00bb92eb301876598c022924ee52bed6262721bfd`.
- Producer identity in the freshly parsed manifest: profile `pi-sol`, Pi, reported `openai/gpt-6.1-sol`, medium for every model role. This metadata is not proof of universal worker compliance.

## Fresh recursive publication and method binding

I recomputed SHA-256 over every regular file recursively below P, including the manifest, and compared the complete relative-path map, not just selected members. All **13 files** match the intake and the completed own publish effect's entire `new` map. The sorted compact JSON map digest is:

`3bac62f0947695b052064c1eb291420030db69ca50f713eca5dd174c2af20317`

Encoding: SHA-256 of UTF-8 JSON with sorted keys, separators `(',', ':')`, and no final newline; values are exact-file-byte SHA-256 hashes.

Fresh checks also established:

| Evidence | Fresh binding |
|---|---|
| `W.preparation.json` | Intake hash `2237c8d3e88af84d0f6575caad44fd604d3abb2c4813f8bb10452d4cedcf5b44`; ready worktree and command prefix |
| `R/run.json` | Intake hash `216d3b1ae1d395ce498882a0dfa49561a00f6f8859c891258d927757cdfb104d`; exact system/source/profile/command-path parameters and recorded plan identity |
| `R/effects/publish.json` | Intake hash `ba6dbb7c8aaa5c2ea7c649b46d0864955216e63f80426fb071ae05fa1da97f42`; completed; exact run/source/destination; expected absent; no old/archive map |
| `R/state/attempts/000049-publish.json` | Intake hash `71719892db6456641ea08ad8d34ce342e2537deab4a5f5b1d0f595773d38bef2`; completed; every role-specific member pin and manifest pin equals current bytes |
| Version store | Each of the 13 publication hashes resolves to a blob with that exact hash |
| Publish receipt | Blob `6bcbea07f1d0ca12955119bc42af13bb7ce5aa0a5e3833f0ff4b3cef4b41060f`; member map equals current publication; method commit matches |
| `ARTIFACT.yaml` | Parsed record equals intake; its 12 member hashes equal current member bytes |
| Opening | Attempt and metadata bytes equal intake; metadata blob `5dc4a07c6370e0507e1cb5680fe351ca843d953c6e0d6660c1f37dbb881acb2a` binds exact run/source/method |
| Acquire | Effect bytes and record equal intake; publish source pin `f0adeb83b5364b7a6cc4bae1d7d8c4d2c4c5f8c19a14228459284c6f86e814f4` identifies S and its actual frozen revision |
| Attempts | All 49 intake-listed attempt files freshly hash-match; no new attempt was invoked |

The opening and receipt's null requested `source-revision` do not erase the acquired revision: the acquire record, boundary and actual source HEAD agree on the full commit above. No source or method mismatch was found.

## Historical comparison and source challenges

The sole supplied historical lead, `kb/agent-memory-systems/reviews/MemoryOS.md`, was read completely. Its fresh SHA-256 is `1cdb2434dab42b6257ebdc026992cfa88939c3451cdc394d2979f74ffea550ed`. It identifies the same BAI-LAB repository, but reviews `1d717060350931af33d1d0dc3d4e50a72c125a48`, not this run's revision. Both commits are locally available. A read-only Git comparison shows differences only in six bundled MCP/Playground storage files (30 additions, 12 deletions); the PyPI, ChromaDB and evaluation implementations are unchanged between those pins. I inspected the short-term MCP diff: it adds a lock around saving. I did not attribute the important ChromaDB corrections to a later source revision.

I read the public boundary, overview and synthesis completely, all three verifications and reconciliation completely, the memory objects through the evaluation ledger, the runtime ChromaDB/evaluation records, and the profile's read-back/trace-learning units and comparison rationale. Other supporting sections were searched or sampled, not independently reverified line by line.

| Meaningful difference or challenge | Frozen-source check and disposition |
|---|---|
| Legacy describes ChromaDB as changing durability without changing the memory contract. The new account identifies a broken initial-page maintenance path. | S `memoryos-chromadb/storage_provider.py:57–72,102–200,230–246` initializes and returns the shared sessions dictionary, installs backup pages and deletes shared entries. `memoryos-chromadb/mid_term.py:55–57,76–94,152–179,236–268` aliases it, overwrites the freshly installed backup after new insertion, and has the distinct merge branch. S `memoryos-chromadb/memoryos.py:159–164,295–297` supplies the backup-only extraction/enrichment consumers. The new account correctly distinguishes surviving vector text from missing backup-fed maintenance. This is a substantive correction to the older lead, not a coverage regression or revision explanation. |
| The accepted runtime/memory records omit an additional ChromaDB capacity failure. Is an audit-only qualification needed? | Provider deletion removes the aliased session before `MidTermMemory.evict_lfu` calls `self.sessions.pop(lfu_sid)`. The second removal can raise before cleanup/rebuild. Report verification already records the omission; synthesis's alternate-route prose and Limitations explicitly carry it, and synthesis verification repeats it. The publication does not promise clean eviction or uninterrupted admission. Retain the existing public limit; no new hold is needed. This is a source deduction, not an observed incident. |
| Does the new analysis lose the older account's live trace-to-profile-to-answer mechanism? | S `memoryos-pypi/memoryos.py:129–259,261–366` implements heat-selected unanalyzed-page extraction, old-profile input, thirty-character profile admission, fact-line append, analyzed flags, pre-append migration, response prompt assembly and write-back before return. `memoryos-pypi/retriever.py:19–139` supports queue seven, session five and knowledge twenty defaults plus caught retrieval errors. The new synthesis retains the mechanism and adds consequential limitations. No lost central capability was found. |
| Legacy calls read-back both pull and pre-invocation push; the new profile emits pull on assessed request chains. | The frozen profile type at W `kb/agentic-system-analyses/types/agentic-system-memory-profile.md:167–182` distinguishes fulfilling a consumer request from an independent automatic supply. S `memoryos-pypi/memoryos.py:261–347` explicitly requests context within `get_response`, then formats it; MCP retrieval at `memoryos-mcp/server_new.py:146–190` separately returns requested data. The new profile states its chosen request-chain unit and does not count formatting as another push. It does not claim global pull-only completeness: remaining helper/driver alternatives and push signals remain uninspected. This is a declared classification/unit difference, not evidence that prompt assembly vanished. External host consumption is still unknown. |
| Legacy loosely groups product and benchmark evidence; does the new evaluation distinction have support? | S `eval/main_loco_parse.py:229–318` initializes capacity-one sample stores, imports and migrates conversations, generates question answers and saves a result ledger without admitting those answers as new dialogue. Search of `eval/dynamic_update.py:165` confirms user-only summary input. The new runtime/memory records and synthesis separate this pipeline from the product and keep README gains attributed. No reproduced performance, clean initial state or score-to-method feedback is claimed. |
| Are lack of validation and provenance limitations newly hidden? | The source profile-length/none filters and fact-line guards above establish structural admission, not truth checking. The synthesis explicitly carries missing enforced source-page lineage, caller-selected identity rather than authentication, no controlled benefit experiment, and best-effort/nontransactional persistence. The old account's central cautions remain visible, with more precise variant scope. |

The historical Commonplace comparison and borrowing suggestions are not required outputs of this source-first publication. Their absence is not a defect; transfer synthesis is separately commissioned. I did not treat the historical review as source truth or feed it back to a producer.

## Bounded completed operational evidence

I inspected only the supplied completed own trace `outputs/batch-18/memoryos.output` under the same external outputs root as W. Its fresh SHA-256 is `32c27d63958c71ef345677090f744197c5b551c12a74b906529cc48792bdc0a4`. The file is 379,538,773 bytes; I parsed its JSON events rather than treating large repeated streaming snapshots as independent evidence.

The coordinator's final assistant tool-call inventory binds the exact-run handoffs and explicit `gpt-6.1-sol`/medium launches. A bounded nested check focused on the final report verifier, because its public limit is load-bearing:

- Outer assistant call at line 4310, ID `call_BEjn5NDswucmdy0suAVHlVVd|fc_0c3e18d9cbfcc471016ad24c9818dc87d29d3fca1c3dfc4071`, hands off completed own `000034-report-verification`. Its matching `tool_execution_end` at line 4436 contains that worker's 123 messages and exit 0.
- Within that worker, source reads, read-only Git/search commands, a source-text comparison script, output writes and validation have matching tool results. Its Python script reads files and diffs text; it does not import or run target modules. I found no target execution, service start, fetch/install or collateral edit among this worker's recorded calls. This is a bounded worker check, not a universal compliance certification.
- Nested write call `call_VnHg6IO5W77HQhttU0VL65TA|fc_08d32786a0d4e3f0016ad24d95fafc87d29f94a0fa5d2d094f` has a successful matching result. Hashing its submitted verification content gives `0e445f5ce56af6b5d51b177b44f3388366fd02d56b08650b48b1ba72f47aa55b`, exactly the installed report-verification member and attempt output.
- Nested validation call `call_ElMUnkdq5zarOldF9nGRV53y|fc_08d32786a0d4e3f0016ad24dd70a7c87d2ae893b287bbc35a1` has the matching result: `Member content check passes; invocation residue not checked. This is not job acceptance or claim support.`

This check supports the exercised verification/output chain and the scope of its limitation. It does not infer complete obligation fulfillment from acceptance, exit 0, manifest identity or a proposed tool call. I did not exhaustively inspect every producing worker, reconstruct every earlier correction, or audit all writes and commands recursively across every nested worker.

## Validation

All commands use the intake-prepared command environment and **cwd W**, not the origin's user-level executable. No `--output`, tests or target execution were used.

Publication command:

```text
W/.venv/bin/commonplace-validate kb/agentic-system-analyses/retained/bai-lab--memoryos
```

Actual output, exit 0:

```text
VALIDATION SUCCESS
Target: kb/agentic-system-analyses/retained/bai-lab--memoryos
Scope: kb/agentic-system-analyses/retained/bai-lab--memoryos
Files analysed: 1
Text files: 0
Diagnostics: 0 failures across 0 subjects; 0 warnings across 0 subjects

Details: commonplace-validate --full kb/agentic-system-analyses/retained/bai-lab--memoryos
```

Report command:

```text
W/.venv/bin/commonplace-validate /home/zby/llm/commonplace/kb/work/agentic-system-reruns/audits/current-publications/AAS-2026-10-16-memoryos-bb72a1b70e03-01-followup.md
```

Actual output, exit 0:

```text
VALIDATION SUCCESS
Target: /home/zby/llm/commonplace/kb/work/agentic-system-reruns/audits/current-publications/AAS-2026-10-16-memoryos-bb72a1b70e03-01-followup.md
Scope: /home/zby/llm/commonplace/kb/work/agentic-system-reruns/audits/current-publications/AAS-2026-10-16-memoryos-bb72a1b70e03-01-followup.md
Files analysed: 1
Text files: 1
Diagnostics: 0 failures across 0 subjects; 0 warnings across 0 subjects

Details: commonplace-validate --full /home/zby/llm/commonplace/kb/work/agentic-system-reruns/audits/current-publications/AAS-2026-10-16-memoryos-bb72a1b70e03-01-followup.md
```

Deterministic success is not semantic certification.

## Limits and parent handoff

No execution of MemoryOS or its tests/services occurred. No fetch, installation, delegation, producer contact, active-run handout/log access, source mutation, state mutation, reset, advance, judgment, integration, staging, commit or cleanup occurred. The only authored path is this followup. The earlier incomplete group report remains unchanged.

This is a selective independent audit, not a replacement whole-system analysis. Paper, full dataset validity, model/dependency internals, external MCP hosts, deployed behavior and complete driver/helper coverage were not audited. Source checks tested the consequential comparison differences above; the rest of the supporting profile and analyst records were not exhaustively rederived. Necessary uncertainty and the known capacity-record omission are already public. No new deep, local-rework, operational/authority, evidence-binding or transfer hold is established; therefore there is no faulty installed-output/missed-barrier diagnosis or author/verification restart recommendation. Parent owns acceptance and any later safe integration guards.
