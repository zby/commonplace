## Outcome: no material defect established in the three questions checked

- **run-id:** `AAS-2026-10-20-openresearch-62725ad1cd0a-01`
- **method-commit:** `005a3f2dd621cb140a0cf90f4e48d9cd5ca1ffad`
- **source-revision:** `2c45ff3183b494aac4001bd44eefbe57a3c249ae`

The suspicious reads had meaningful follow-ups, and the selected accepted conclusions survived source verification. This is a bounded result, not a correctness certificate for the analysis.

Paths below are relative to the supplied `source_root` or `run_directory`. Trace locators identify physical JSONL lines in `calls/launches/<launch-id>/stdout.log`.

### 1. Did the interrupted epistemic searches conceal a substantive reporting gate?

**Lead.** The epistemic worker first searched a nonexistent MCP-gate path, then retried with an `&&` pipeline that again stopped early. This could have left the analyst misunderstanding whether “gates” validate research results.

**Affected accepted passages.** `artifact/synthesis.md:34,38` distinguishes instructed evidence checking, numerical chart validation, and ungated description retention.

**Decisive evidence and recovery.**

- Epistemic trace `7e120c513a22446499c928ea1fae35f4:1506` contains successful matches from the corrected `src/commands/mcp_gate.rs` and chart helper before the pipeline stopped. The subsequent `description|archived` search has no matches in frozen `src/commands/project.rs`; its exit status stops the remaining invocation search. Thus this second incident is not another missing-file failure.
- Later successful read results at trace lines **1535** and **1539** supply the complete chart helper and invocation hook respectively.
- Frozen `src/commands/invocation_gate.rs:8-30,33-59` exports invoking-model identity into Bash commands; it does not inspect scientific evidence.
- `src/commands/mcp_gate.rs:104-145` advertises an approval tool and relays permission requests—not result acceptance.
- `agent-skills/orx-figures/assets/orx_chart.py:10-57` checks chart inputs before serialization and writing. It does not verify measurement provenance.
- `src/plane/local_plane.rs:239-258` saves caller-supplied description text directly.
- `agent-skills/orx-results/SKILL.md:8-17` supplies precisely the reporting prerequisites summarized in the accepted synthesis.

**Conclusion.** The accepted distinctions are supported on these paths. The interrupted search did not establish a missing scientific-admission mechanism or a false account of the chart validator.

**Uncertainty / smallest follow-up.** No correction is indicated for these passages. A claim about every possible report producer would require broader inspection; this audit did not establish such a universal negative.

### 2. Did the memory-worker failure undermine the retained-context comparison?

**Lead.** A missing delegation-skill path stopped a compound search before its final hook/memory search. The consequential question was whether the accepted profile overstated automatic retained-context updates or conflated transcripts with native context.

**Affected accepted passages.** `artifact/synthesis.md:42-46`; `artifact/memory-profile.md:941-966,1126`, especially the fallback-compaction `trace_learning: yes` finding with wired basis.

**Decisive evidence and recovery.**

- Memory trace `08bcfe5352834116a0c0d5b469aef6e5:1587` shows the repeated hook/memory search completed; **1614** contains the corrected `orx-agent-delegation/SKILL.md` read. This is checked recovery, not merely an inferred repair.
- Frozen `src/local/chat/mod.rs:1682-1759` selects native versus fallback compaction, supplies prior bootstrap and transcript to the summarizer, rejects empty output, persists the summary, and then clears the native ID.
- `src/local/harness/mod.rs:67-161` imposes the 32-KiB snapshot bound and retains tool labels/status rather than full tool bodies.
- `src/local/chat/mod.rs:5626-5644` supplies bootstrap only on ordinary preparation without a native session; `prepared_input` bypasses that composition.
- `src/local/chat/mod.rs:8024-8059` distinguishes persisted bootstrap from parent-leaf reconstruction and legacy copied side-chat context.

**Conclusion.** The fallback-compaction comparison has a concrete derived-write/later-delivery chain. The accepted text appropriately withholds claims of improved capacity and full-context fidelity. No material defect was established.

**Uncertainty / smallest follow-up.** Provider-native payloads and the separate ACP reseeding implementation were not independently verified here. Any further check should target those alternatives rather than repeat the resolved delegation-path repair.

### 3. Did runtime path failures distort the permission boundary?

**Lead.** Runtime searches referenced nonexistent `chat/host.rs` and `commands/exp/` paths, potentially missing admission and enforcement responsibilities.

**Affected accepted passage.** `artifact/synthesis.md:22` describes route-specific permissions, Codex workspace-write Plan mode, and a separate operator-shell mutation path without claiming a demonstrated model exploit.

**Decisive evidence and recovery.**

- Runtime trace `3b6f150f6d7c4afb930c6970ca32b028:565` identifies the missing `chat/host.rs`; **639** identifies the nonexistent experiment directory. **716** successfully locates/searches `chat/mod.rs`, and **735** successfully reads `commands/exp.rs`. Later direct reads of the permission and shell implementations are visible in the trace inventory.
- Frozen `src/local/chat/mod.rs:3456-3501` checks gate tokens and turn activity, then applies bypass/Plan policy or proceeds toward review.
- `src/local/harness/codex.rs:1342-1365` maps Plan to `workspace-write` and `on-request`.
- `src/local/chat/mod.rs:1814-1915` launches operator Bash and records its outcome without consulting model permission mode.

**Conclusion.** These implementations support the accepted route-specific account. Neither the failures nor the inspected source justify upgrading the operator-shell path into a demonstrated model bypass.

## Process causation and coverage

**Process causation:** No content defect was established, so no failure-to-defect causal attribution is supported. The selected original traces show substantive recovery. Routine validator-path, citation-attribution, and pending-marker failures were deprioritized as apparent repairs; I did not certify every validation recovery or treat successful validation as semantic evidence.

I verified the selected reporting-gate distinctions, fallback-context persistence/delivery, and permission-policy differences. Literature reconstruction, compute snapshot reproducibility, release updates, native checkpoint internals, and the full skill/guidance inventory remain unexamined. No target execution, validator rerun, network access, file mutation, or worker launch was performed.
