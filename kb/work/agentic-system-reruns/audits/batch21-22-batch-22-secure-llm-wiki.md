# Batch 22 Secure LLM-Wiki independent audit

## Disposition

**Integrate with recorded limits.** No consequential semantic defect was established in this bounded inspection. The publication already distinguishes a source-inspected implementation from demonstrated security, factual warrant, faithful extraction or causal benefit. The historical review's stronger security framing is not a reason to restore those claims. Procedural deviations below prevent certification of literal worker compliance; they did not establish wrong-source analysis, unauthorized target execution or consequential collateral mutation in the inspected evidence.

This is an exact-byte recommendation, not integration authority. No repair, integration, acquisition, target execution, cleanup, delegation or commit was performed. Only this report was written. Coordinator-owned ledgers and unrelated ingests were untouched.

## Assignment and identity

Audit date: 2026-10-19. Fresh independent auditor: `openai/gpt-6.1-sol`, commissioned medium effort, project scope; runtime `PI_MODEL=gpt-6.1-sol`, session `01a152c1-0905-7356-98c5-8c2e74ac4311`. Read the complete commission, assignment ledger, exact matching intake entry, audit procedure, workshop framing and `kb/work/COLLECTION.md` before judgment.

Paths below use these literal bases:

- W: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-22-secure-llm-wiki`
- R: W + `/kb/agentic-system-analyses/state/AAS-2026-10-19-secure-llm-wiki-df02f419bddb-01`
- P: W + `/kb/agentic-system-analyses/retained/nicobleh--secure-llm-wiki`
- S: W + `/related-systems/nicobleh--secure-llm-wiki`
- L: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/batch-22/secure-llm-wiki.output`

Run: `AAS-2026-10-19-secure-llm-wiki-df02f419bddb-01`. Prepared method/inputs commit: `83cb60e460a55b57bd69600c86d58f50b8c316db`. Preparation token `df02f419bddb`, ready at `2026-10-19T01:24:03.295169+00:00`; record W + `.preparation.json`. Plan digest recorded in `run.json`: `5a5f56891d95a819c3f4fde00bb92eb301876598c022924ee52bed6262721bfd`. The frozen worker rules and exact role criteria remain pinned in the run. Worker profile: `pi-sol`; manifest reports all eleven model roles as `openai/gpt-6.1-sol`, medium.

Source: `https://github.com/nicobleh/secure-llm-wiki`, Git revision `dfbc60e37487b61e9a5cbce1271a13576a776d51`, SRC-1. Acquisition effect is completed, with `path-existed: false`, `initial-head: null`, and the same source path/revision. No new source was acquired during audit. Read-only Git inspection found S at that exact HEAD with empty porcelain status. This establishes current checkout identity, not its entire historical mutation record.

## Semantic and historical inspection

Read P's overview, synthesis, boundary, manifest and all three independent verifications. The synthesis carries the significant limitations in its main account and seven-row limitations table, not merely in an audit appendix. Investigated selected discrepancies directly in SRC-1: `src/secure_wiki/extraction/extractor.py` in full; `src/secure_wiki/__main__.py` acquisition/pipeline and query/context ranges; `src/secure_wiki/read/hygiene.py` and `src/secure_wiki/gate/write_gate.py` in full; `src/secure_wiki/store/wiki_store.py` serialization/save/reload range; and `tests/test_injection_corpus.py` in full. This is not a second whole-system analysis.

Historical comparison lead: `kb/agent-memory-systems/reviews/secure-llm-wiki.md`, checked 2026-06-05, reviewed the **same full commit**, despite owner-name case differences. Scoped searches found no same-source report under this workshop's `audits/` or the current `kb/agentic-systems/` tree. The old review was used only by this auditor, not supplied to analysts.

### Decisive findings

1. **The new publication corrects the apparent sanitizer guarantee rather than losing it.** The old narrative describes sanitized text progressing into extraction. In the actual `_run_pipeline`, `report = sanitize(source_text)` is followed by `extract_claims(source_text, ...)` and a batch review with `source_text=source_text`; sanitizer flags are enforced later in the write gate. The new synthesis explicitly states that original transformed/truncated text reaches both models. This qualification changes security understanding and is already public. Anchors: P `RT-RTE-extraction-parsing`, `EPI-OBJ-source-text`, synthesis “Acquisition, proposal and admission”; S `__main__.py` `_run_pipeline`.

2. **Nonce compatibility gaps and empty extraction are correctly bounded.** `_parse_items` checks the nonce on whole envelope JSON but accepts bare arrays and linewise items without uniform verification. `extract_claims` returns proposals that still pass through downstream admission. Empty extraction returns from the pipeline without creating a quarantined claim. The synthesis states both points and does not infer a demonstrated injection exploit. This is more precise than calling the entire pipeline uniformly fail-closed. Anchors: S `extraction/extractor.py` `_parse_items`; S `__main__.py` no-claims branch; P `RT-RTE-extraction-parsing` and synthesis.

3. **Admission is neither truth checking nor reliable contradiction detection.** The write gate rejects an untrusted proposal whenever any active trusted claim exists, not only an overwrite of the same subject. Vector comparison chooses maximum similarity with .95/.85 thresholds and otherwise uses a same-section/different-source heuristic. Review is precomputed once for the batch. The publication retains these mechanisms and distinguishes them from factual warrant. The corpus test supplies fixed extracted text and mocks the reviewer verdict using the expected manifest outcome; it is not live efficacy evidence. Anchors: S `gate/write_gate.py` gates 3–5; S `tests/test_injection_corpus.py`; P synthesis “Acquisition, proposal and admission” and limitations. No security certification is justified by passing validation or by the test definitions.

4. **Coarse selection is preserved despite a changed comparison label.** The old review calls query startup a coarse push. The new profile/verifier classify operator-requested startup loading as pull under the current contract. Source still selects every eligible claim by trust/status before the question; no question-conditioned retrieval is silently invented. `load_for_context` also excludes untrusted labels regardless of the requested minimum and permits pending pages only when requested. `cmd_query` freezes startup context, sends each current question without accumulated dialogue, streams the answer and does not save feedback. These operative facts and their limits are public. The profile's narrower direction classification is not a lost runtime path. Anchors: S `read/hygiene.py` `load_for_context`; S `__main__.py` `cmd_query`/`cmd_context`; P profile verification read-back bullet and synthesis “Durable handoff and later reliance”.

5. **Storage counterpaths are not hidden by the normal gate account.** `_deserialize` reloads frontmatter rather than the duplicated Markdown body; `save_claim` writes supplied claims without enforcing ingestion gates, and the file write precedes the Git commit. The new synthesis explicitly qualifies direct/local writes and partial persistence; it does not invent a remote unauthenticated endpoint. The old review's atomic claim/provenance/quarantine framing remains recognizable without its stronger audit-trail implication. Anchors: S `store/wiki_store.py` `_deserialize` and `save_claim`; P `MEM-OBJ-claim-text`, report verification, synthesis.

The bounded source checks support the publication's central account and selected historical differences. No audit-only qualification is being substituted for a missing public semantic limitation.

## Operational and source-first evidence

Intake's native inspection records 33 completed attempts, no open attempts, no failed attempts, no refusal, no worker-problem text and publication-job completion. Six earlier deterministic acceptances are stale, while the later checks and publication completed. This is an engine coverage record, not operational certification. The audit did not advance or re-inspect the engine through a state-locking command.

Inspected L's actual nested worker messages, not just coordinator summaries. Enumerated all eleven analytical worker result packets and their shell/write/edit calls. In the inspected call inventory, writes target the assigned output/identity paths or the profile worker's assigned scratch, and shell calls perform source inventory/search, environment reporting, Commonplace content checks, or local profile generation. No target execution, source acquisition, Git commit, deletion, or cross-worktree write was established in this inventory. This does not prove completeness of every nested tool obligation or exclude actions outside the retained evidence.

Selected paired call/results within the same workers:

- Runtime worker (`000005-runtime`, L subagent result at one-based line 1295): `call_feNSowUCna68haMq2cy4iZDE|fc_0e895b1fe8a4c105016ad57396642c87d2814c82ceb7501c07` returned content-check failure (code 1) for malformed evidence-basis formatting. The worker edited its own candidate and `call_Qx4fUP2dyFtKejvsqKbDdBWL|fc_0e895b1fe8a4c105016ad573aac08887d28715c1fc136bd536` returned “Member content check passes; invocation residue not checked.” This was a deterministic formatting repair, not a semantic refusal ignored by publication.
- Memory worker (`000007-memory`, L parallel result at line 2140): `call_MlBE5gtFYY08yPQnLyB8LvXk|fc_00bb714786337b01016ad573eeb39087d2ab99e4779f89fa44` returned runtime identity `openai/gpt-6.1-sol`, medium, the registered source commit and empty Git status. Its later validation call `call_fr5mDPzC0IIilPkVYkRtUrQl|fc_00bb714786337b01016ad574d5370887d286926e9d59ee64f9` returned a content pass, not claim-support certification.
- Profile worker (`000024-memory-profile`, L result at line 3407): inspected the actual `write` content for `scratch/build-profile.py` and the execution/result pair `call_r8a5J5r6d8XxnzoUwm1nl6uo|fc_0d3eb41f074495fd016ad5778d35e087d29f48527a8bc82d66`. The script imports YAML/Path, assembles profile data from record identifiers and writes the assigned profile output. It does not execute the target or acquire sources; its execution returned no output. Closed handout scratch is no longer present, so this judgment relies on retained call content rather than a surviving scratch file, consistent with the frozen rules' disposable-workspace provision.

**Observed procedural deviations:** the memory and profile workers use relative output paths in `write` calls; report verification uses relative source paths and a relative `cd`, despite the frozen worker rule requiring supplied absolute paths. Several identity/source inventory shell calls use `;`, rather than separate commands or dependent `&&`, so final shell success cannot certify each earlier command. The paired returned text and correct absolute output destination in the profile script narrow the consequences; no wrong-source or off-scope mutation was established. These remain actual deviations, not certified compliance or repairs by the auditor. The publication's deterministic-check disclaimer correctly avoids claiming every worker obligation was satisfied.

No historical characterization exposure was found in the inspected worker action inventory. That is a bounded observation, not an exhaustive proof of all input-reading, truncation-recovery, or source-first obligations. Source-first judgment is independent of the historical comparison in this audit.

## Exact-byte binding

The complete recursive 13-file publication map equals both intake's publication map and `effects/publish.json`'s `new` map. Expected incumbent is `absent`; `old` and `archive` are null. Digest encoding: SHA-256 of UTF-8 `json.dumps(member_map, sort_keys=True)` with default separators and no terminal newline.

| Binding | SHA-256 |
|---|---|
| Preparation record | `15958f363ca6776631f0bb4c92d65a440af4d8d745344f0d2355fd5a8acb2862` |
| `run.json` | `fe4727e6766b21c6063bffa1b6183ce63b92264999ba0fe71c18a11dffbf7e7d` |
| Acquisition effect | `e3343566c29d8ff65ea04dde8bfc28313dc645ad5bb8c55ca8c2f499216e0b72` |
| Publication effect | `f0cea62f4bfbe502b628432f3c9b3da760777941fc973338dc1f5a2a2d441dda` |
| Complete member-map digest | `77c15f998e5f90967bf1c63e16522a7875a5d5739e5d46778f19bd89a054d09a` |
| Coordinator log L | `4f70537a2cd5a2b2ccb7aa90074e9647e13130481b19f3d954d2dd59b63f1279` |

Complete member map:

```text
ARTIFACT.yaml 73f299e7ae900c9e5d0deae2569e1a1fec1f251551e40a0b9b810680ad06e0d9
boundary.md a9df984bf8c0380a732bfa2f139237326c6f57901521b24b9c628583612799ac
epistemic.md f13ae7541d6d6bea6a6e592d8bb2c45c96387ee523c6209b7df223b90b38ffcd
memory-profile.md d61e5e20a9b445a88d4368f465691f200e60cecbe33b356765457e414ca7ec78
memory.md 62cd8307c219c055d9511e50436e326eae84f752f2856e4d962fba5c8d420582
overview.md 82b4dc22fe1f927c3a20df1df500976e07673de9f7c763d3c1bf5518b7622760
profile-verification.md c471fa3fad3fca08eb3f592bb66b22436b74e445c58113ac61fca71987b1344c
reconciliation.md f0f7965681edb507c9b4ff40d99f68a655077e42ecda0f4882a9dc2352fbcdf4
report-verification.md bcd4ace4cb5a1cd52cc6582873a0ff40f33bc758c9dfc239a54253949c689f3d
runtime.md a51743ec5e91d83b09844da8d4cc416642f51e8d03c01dc9cf59a239da1f4047
synthesis-verification.md d1c5b71970e5c91e02735da36e81d8cf87c53a418b65e557c8ea2bfa24e2226e
synthesis.md a0b7f88f75f621b3232fd9725ee5e9cf112f70b8cafd5038892c674642c8543d
workflow.md 2e08cf2f32ae5523b5d121e9d5d6be7e48d387c8d99e2a69ec0f79f1dfd8ad57
```

## Deterministic validation and coverage limits

Validation uses only W's prepared `.venv/bin/commonplace-validate`, invoked from W, without `--output`:

- Publication directory: `VALIDATION SUCCESS`; files analysed 1 (the directory artifact), text files 0, zero failures and warnings, exit 0.
- This report: supplied as absolute origin path to the same validator; `VALIDATION SUCCESS`, files analysed 1, text files 1, zero failures and warnings, exit 0.
- After inspection, all 157 intake state-map entries matched their recorded hashes. The complete publication file set, each member, preparation record and publication effect also matched intake. Rehashing is byte preservation evidence, not semantic certification.

Limits: selected discrepancy-led source and trace inspection only; no full reread of every analyst record or every worker input/result. No target/provider execution, payload efficacy review, independent causal experiment, external-provider inspection or reconstruction of a deployed wiki was attempted. The publication already carries the resulting source-only, instance, factual, vector and recovery limits. Current empty source status and selected worker call inventory cannot establish all historical filesystem effects. Further security-efficacy investigation would be a separate analysis, not necessary to accept this accurately bounded implementation account.
