# Outcome: none established

No consequential residual defect was established as a result of the investigated execution failures. The evidence shows meaningful recovery: corrected source paths, equivalent direct reads, repaired quotation attribution, corrected validation invocations, and a later substantive profile correction. This is not a correctness certificate.

- **Run-id:** `AAS-2026-10-20-openresearch-62725ad1cd0a-01`
- **Method-commit:** `005a3f2dd621cb140a0cf90f4e48d9cd5ca1ffad`
- **Source-revision:** `2c45ff3183b494aac4001bd44eefbe57a3c249ae`

**Locator convention:** `artifact/…` and `calls/launches/…` are relative to the supplied run directory. Source paths are relative to the supplied source root. Trace line numbers are physical lines in each launch’s `stdout.log`; abbreviated call IDs identify the corresponding executions.

## Residual findings

**None established.**

The investigation selected three consequential claims from the accepted synthesis/profile and traced their dependencies backward.

### 1. Fallback compaction implements trace-fed retained context

**Accepted passage:** “Fallback compaction automatically turns recorded work and prior bootstrap material into a summary, persists it, clears the native session ID and supplies that seed to a later ordinary turn without native context” (`artifact/synthesis.md:42`). The profile emits `trace_learning: yes`, with wired basis, for that localized mechanism (`artifact/memory-profile.md:945–966`).

**Suspected failure dependency:** The memory worker’s failed chained search could have prevented inspection of delegation/context mechanisms or alternative memory paths. At trace line 1521, `call_OmaTjbf…` failed because `agent-skills/orx-delegation/SKILL.md` did not exist; the final hooks/memory search was consequently skipped.

**Recovery checked:** The worker listed the actual skill directories and reran the skipped hooks/memory search (`call_960w…`, result at line 1587), then successfully read `agent-skills/orx-agent-delegation/SKILL.md` (`call_tiWL…`, result at line 1614). More importantly, the failed search did not prevent the compaction evidence reads: the worker had already inspected the compaction implementation and subsequently inspected branch/context consumers. Independent report verification reread the compaction implementation and ordinary composition (`6dc3add…`, calls beginning at lines 1637–1640).

**Direct challenge:** Frozen `src/local/chat/mod.rs:1681–1762` implements the native/fallback split, nonempty model summary, bootstrap persistence, and native-ID clearing. Lines 1296–1309 gate bootstrap delivery on absence of a native session ID. The accepted text distinguishes this from opaque native compaction and does not claim observed improvement (`artifact/synthesis.md:42–44`; `artifact/memory-profile.md:1126`).

The failure therefore has no supported connection to a surviving false positive on this selected classification. Untraced alternatives remain coverage limits, not evidence against this localized implemented chain.

### 2. Permission guarantees are route-specific, not system-wide read-only guarantees

**Accepted passage:** Claude bridge requests receive token/busy-turn checks; Codex Plan includes workspace-write; operator shell is a separate mutation path; neither Plan nor a private worktree guarantees system-wide read-only behavior (`artifact/synthesis.md:22`).

**Suspected failure dependency:** Two runtime discovery commands used nonexistent paths. The first failed on `src/local/chat/host.rs`; its chained `wc` was skipped. The second stopped at nonexistent directory `src/commands/exp`, skipping its subsequent route search.

**Recovery checked:** The worker located the actual monolithic chat implementation and experiment file (`call_51hz…`, trace lines 712–716), then successfully read permission handling and shell execution (`call_0CZY…`, result line 872; `call_zeF7…`, result line 874). It also read the Codex policy mapping. Independent verification inspected token, busy-turn, bypass, plan-policy, human-review, shell, and Codex branches (`artifact/report-verification.md:20`; corresponding source-read calls in launch `6dc3add…` at lines 2401–2403).

**Direct challenge:** `src/local/chat/mod.rs:3456–3534` contains token and busy-turn checks plus bypass/plan/review branches; `:1814–1896` launches shell commands without a model permission-mode check. `src/local/harness/codex.rs:1342–1365` explicitly maps Plan to workspace-write. These support the accepted qualifications rather than a stronger isolation guarantee.

No load-bearing permission premise was shown to remain dependent on the failed paths.

### 3. Chart validation is implemented but does not establish scientific truth

**Accepted passage:** “The chart helper does enforce numerical/schema conditions before its own new write, but fabricated finite values can pass and arbitrary writers bypass it” (`artifact/synthesis.md:38`).

**Suspected failure dependency:** The epistemic worker’s first chained discovery command stopped at nonexistent `src/local/harness/mcp_gate.rs`, preventing chart and project searches. The corrected command reached the chart search but then returned 1 because the project search found no matches, skipping the invocation-related search.

**Recovery checked:** The next batch successfully read the complete chart helper (`call_DHAt…`, trace lines 1530/1535), invocation gate and invocation helper (`call_mCNY…`, result 1539; `call_bV5X…`, result 1536). Earlier reads of experiment/tree operations had already provided evidence relevant to the skipped project search. Independent verification reread the chart helper (`6dc3add…`, call at line 1668).

**Direct challenge:** `agent-skills/orx-figures/assets/orx_chart.py:10–49` checks structural/numerical conditions; `:52–57` validates and serializes before writing. There is no measurement-provenance check in that helper. The accepted passage confines enforcement to this helper and does not equate structural validity with scientific acceptance.

The source-read failures were recovered for this claim; the accepted qualification survives the challenge.

## Incident dispositions

| Incident | Disposition | Decisive evidence |
|---|---|---|
| **Epistemic**, scanner trace line **1380**, `call_b5vn…`: nonexistent MCP-gate path | **recovered** | The error’s own inventory supplied `src/commands/mcp_gate.rs`. Corrected search at lines 1502–1506 reached that file and chart checks; complete chart read followed at 1530–1535. |
| **Epistemic**, line **1506**, `call_2yO8…`: search exit 1 | **recovered**; no-match itself was **expected-nonzero** | Original event confirms MCP and chart searches succeeded; project search produced no match, so `&&` skipped invocation inspection. Direct invocation/gate reads at 1531–1539 fulfilled that skipped purpose. It was not treated as an entirely harmless successful chain. |
| **Epistemic**, line **15089**, `call_tGiG…`: ambiguous quotation | **recovered** | Complete diagnostic identifies three occurrences of a 404 branch. Edit at lines 15239–15240 selected `src/client.rs:915–917`; accepted `artifact/epistemic.md:351` retains that attribution. Frozen `src/client.rs:902–927` confirms the selected occurrence belongs to paper-markdown retrieval. The quotation repair does not weaken that underlying claim. |
| **Epistemic**, line **15411**, `call_spJ7…`: wrong artifact path | **recovered** | Correct-path validation ran separately at 15608 and returned exit 0 at 15611. This establishes execution of the intended structural check, not semantic correctness. |
| **Memory**, line **1521**, `call_OmaT…`: nonexistent delegation skill path | **recovered** | Directory discovery, rerun of skipped hooks/memory search, and successful equivalent skill read at 1583–1614. |
| **Memory**, line **11103**, `call_9pdE…`: validator rejected “Validation: pending” | **recovered** | Later check returned exit 0 at 11432; accepted `artifact/memory.md:354` replaces the pending marker and explicitly limits what validation establishes. No content conclusion was shown to depend on that marker. |
| **Memory-profile**, launch **f6cf629…**, line **6691**, `call_EMxm…`: wrong candidate path | **recovered** | Correct-path check returned exit 0 at 6893; a further check returned exit 0 at 7700. The accepted profile is a later revised attempt, not merely this initially validated draft. |
| **Runtime**, lines **565** and **639**, `call_kLZd…` / `call_OOmv…`: wrong host/file-layout assumptions | **recovered** | Actual file locations and route discovery at 712–716; successful direct reads of consequential permission, shell, experiment and wake-up paths followed. |
| **Additional masked error:** runtime line **1015**, `call_MaMe…` | **recovered** | `rg src/local/run_wake*` reported no such file, but subsequent commands made the combined result exit 0. Later discovery located wake-up functions in `src/local/chat/mod.rs`, followed by a successful read at 1365–1372. Thus shell success did mask an error, but did not leave that mechanism uninspected. |

### Substantive correction preserved

The first profile verification identified an unsupported emitted `ranking` value: archive visibility and changed comparison organization did not establish a relative-priority mechanism (`calls/launches/b147058…/inputs/refusal.md:7`). The revised accepted profile removes that finding, uses `not-determinable`, and explains the missing consumer/effect (`artifact/memory-profile.md:465–476`, `:1130`).

This was a successful semantic correction, not evidence that validation alone ensured adequacy. Its causal connection to the earlier wrong-path validator invocation is **not established**.

### Unresolved consequential concerns

None established within the selected dependency chains. The accepted report’s catalog-screening and `compute/CUSTOM.md` inventory omissions are explicitly preserved (`artifact/synthesis.md:48`, limitations table). Their causal connection to the investigated failures was not demonstrated; they are not attributed to those failures here.

## Coverage and limits

- Read the input map, full scanner report and attempt inventory, accepted synthesis, and complete memory profile, recovering its truncated ending.
- Examined all **nine scanner-recorded failed executions**, plus the masked runtime search error above.
- Inspected original process events and recovery operations for epistemic, memory, runtime, initial/revised profile, and report-verification launches. Inspected tool-call inventories for both profile-verification attempts and the substantive correction handoff.
- Read the exact epistemic, memory and runtime prompts and their frozen job instructions. Challenged selected claims against frozen source without execution.
- Did not independently trace every event in boundary, reconciliation, workflow, synthesis or synthesis-verification launches, nor audit all source, profile axes, receipt/publication mechanics, or retained outputs.
- Scanner excerpts were not used as proof of non-recovery. Truncated diagnostic excerpts relevant to the investigated incidents were resolved through original events. A bounded trace-index output was supplemented for the omitted epistemic range.
- Used **27 tool calls**, all for read-only inspection or in-memory parsing. No validation reruns, worker launches, network access, target execution or file mutation occurred.

The supported outcome is limited: these failures did not establish a consequential surviving defect in the selected accepted claims. It does not establish that every accepted conclusion is correct or that unexamined logs contain no other failures.
