# ContextPilot renewed batch-19 publication audit

## Disposition

**Hold.** The original training-dispatch fault persists. The renewed account still connects the shipped training configuration to ContextPilot-specific context-management rollouts without stating the dataset/configuration selector or generic single-turn fallback. This is a missing architectural prerequisite, not merely missing evidence of execution or benefit. Neither successful publication nor the new verification discharges it.

Unblock through a separately authorized correction route: retain the conditional `statelm_tool_agent` selection, default `single_turn_agent` alternative and unavailable transformed-dataset evidence in the affected runtime records and public synthesis. Align the boundary's training narrative and dependent assessments, then independently reverify. No new source acquisition or target execution is needed to state this qualification. This audit authorizes no recovery operation.

## Identity and scope

- `run-id`: `AAS-2026-10-13-contextpilot-30d0d09e6cdc-01`.
- `method-commit`: `4266dabc470929df0ff753e57fee0c55d7b87fc6`.
- `source-revision`: `782cbb6611fb610c4cf6fafda6022b7e89cae191`.
- Source identity: `https://github.com/Tencent/ContextPilot`.
- **W**: `/home/zby/llm/commonplace/.commonplace/worktrees/contextpilot-30d0d09e6cdc`.
- **P**: `W/kb/agentic-system-analyses/retained/contextpilot`.
- **R**: `W/kb/agentic-system-analyses/state/AAS-2026-10-13-contextpilot-30d0d09e6cdc-01`.
- **S**: `W/related-systems/Tencent--ContextPilot`.
- **A**: `W/kb/agentic-system-analyses/state/.reset-history/AAS-2026-10-13-contextpilot-30d0d09e6cdc-01/04405cb201e3417abb1674b04b46607e`.
- **O**: archived pre-reset publication `A/effects/0/before`.
- Packet: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/batches-19-20-audit/packets/AAS-2026-10-13-contextpilot-30d0d09e6cdc-01.json`.
- Auditor: independent Pi session `01a14a8f-cc3b-761b-9ed2-ef772a3a0521`; observed environment `PI_PROVIDER=openai`, `PI_MODEL=gpt-6.1-sol`, `PI_REASONING_LEVEL=medium`. No delegation.

This is a completed bounded audit, not production reanalysis or certification of every worker obligation. Read the commission and audit procedure completely; read the workshop collection contract, prepared analysis collection/set, boundary, runtime and verification contracts and relevant pinned boundary/report-verification instructions. Read renewed overview, boundary, runtime, synthesis and all three verifications completely. Examined historical accounts and selected archived/versioned training passages; inspected the frozen dispatch/configuration chain directly. The hold stops broader source reconstruction and a full memory-profile reassessment.

## Exact-byte and incumbent binding

Recursively hashed all regular files beneath P and O. Both contain exactly the packet's 13 files, with no additional regular files. P's complete map equals both the packet and completed `R/effects/publish.json:new` map. The completed effect names this run, source identity and destination, with expected incumbent `absent`. All twelve Markdown member versions equal the `000094-publish` pins. `000093-assemble` emits the manifest and overview hashes installed in P; the manifest's twelve member entries agree with the map. Its immutable manifest version also hashes correctly.

| Binding | Independently observed SHA-256 |
| --- | --- |
| Renewed recursive member map, packet recipe | `61f6f599d6b0d476bf0256f8abf9aa9dfa654f49e458bd6f3a71aa09217b925f` |
| `R/effects/publish.json` | `3a7f0632e0fff4bbaaa7d50f6b04a1da54580aed87a9279f2c64f1868593294f` |
| `P/ARTIFACT.yaml` | `3b86d0b5719d33afa6075847c3c1259dfd24706fa7f453a2b96faa66f2683c2c` |
| `R/run.json` | `6d62c311d1b2a227ca01c38e8d814f46bb8dd04f54c46203ab5aa71328b7ee49` |
| W's sibling preparation record | `0a1888c10b077067ed55d17d2a378b0526c7fbf72680eed2e3f88f2ef387ba34` |
| `R/state/attempts/000094-publish.json` | `4074e5a870c338160e055a459314842539f8092f118fb726d1a0e0ce7f10186e` |
| Packet's predecessor reset report | `6617567469929d7479b529e69c3b4010934e8475e9698a9c8dab23386f6135ad` |
| O's manifest | `0ffa71f5ee5c1e74c4ff3ee9b6cf8c99fff5256bcd26247024891c73f7cc5f8e` |

The renewed map uses `sha256(json.dumps(map, sort_keys=True).encode())`. The predecessor's recorded digest `e81b8577cc24c33ab2d094c0e38b6468cdcf4772cec2a0fe8f9577fee4d20ea0` uses compact JSON separators, as documented in the depth report; recomputing that recipe matches. Applying the renewed default-separator recipe to the same old map yields `1228fd3680a8bebfaa4abae8bcbb03f7ab2983c90146eda1125cba61da7eb4be`. This is a serialization difference, not changed archived bytes.

Preparation is `ready` and supplies `W/.venv/bin`; its method commit matches observed W HEAD and immutable opening metadata. The acquired-source version pinned by publication equals the boundary's full source object and observed S HEAD. Source Git status is empty. W status shows the untracked publication, not a changed method. Opening metadata records the same run and source identity; its requested source revision is null, whereas acquisition supplies the actual frozen commit. Those are distinct fields, not a revision mismatch.

The packet reports no source-matched canonical publication and `integrated-exact-bytes: false`. A fresh search of canonical retained boundary members found no matching source identity. There is no canonical source peer to substitute for this publication or to exclude it as already integrated. No binding/incumbent stop was established.

## Original-fault adjudication

Historical inputs were leads, not premises supplied to production workers. Read [the prior hold](../bash-current-contextpilot.md), [the depth finding](../depth/batch-19-current-content.md), and the archived external-system review at `kb/agentic-systems/reviews-archive/contextpilot.md`. The external-system review inspects the same source commit and expressly retains dataset `agent_name`, generic fallback and missing transformed data. Its older reflection assessment is not adopted as source truth or independently reopened here.

### Frozen-source decision chain

1. `S/train/verl/experimental/agent_loop/agent_loop.py:1006–1008` fills missing batch `agent_name` from `config.agent.default_agent_loop`.
2. That file at `1080–1121` takes the selected name, asserts registry membership, instantiates that entry and calls its `run`.
3. `S/train/verl/experimental/agent_loop/statelm_agent_loop.py:451–452` registers the ContextPilot loop under `statelm_tool_agent`.
4. `S/train/verl/trainer/config/rollout/rollout.yaml:207–208` defaults to `single_turn_agent`. `ppo_trainer.yaml:8–36` imports that rollout configuration. The complete launcher-selected `train/examples/sglang_multiturn/config/statelm_tool_agent_grpo.yaml` inherits `ppo_trainer` and does not override the selector.
5. The complete `S/train/sh/run_qwen3-8b_longbenchv2.sh` supplies ContextPilot tools, partial-rollout settings and estimator but no default-agent override. It reads external transformed Parquet files. Those payloads are outside the frozen evidence; the boundary explicitly retains that gap.
6. `S/train/verl/experimental/agent_loop/single_turn_agent_loop.py:26–64` registers the fallback and implements a single generation rather than the inspected tool/context-management loop.

This establishes conditional dispatch. It does **not** establish that actual training selected the wrong loop, that the external dataset lacks `agent_name`, that training is broken, or that the ContextPilot-specific implementation is absent. The correction concerns which route the supplied configuration establishes, not a demand for observed training success.

| Original consequential fault | Archived evidence | Renewed evidence and adjudication |
| --- | --- | --- |
| Boundary training-entry narrative omits selector/fallback. | O/boundary.md, “Entry points and state consumers,” joins launcher, worker and ContextPilot loop without the condition. Its hash matches archived `000003-boundary`. | P/boundary.md, training paragraph before “Tracked top-level coverage,” replaces the explicit manager/instantiation chain with a more general included-loop description. **Changed but unresolved:** no selector or generic fallback is supplied, while downstream runtime still takes that connection for granted. Source identity and whole-system functional scope remain valid. |
| Runtime makes the ContextPilot training route the connected launcher path without its selection predicate. | Archived initial `000005-runtime`, output `1e750206580714eca75569a0c7afd7081fe621de6e27a903aca759eda200054d`, `RT-RTE-rollout-training`, directly says launcher → worker → `StatelmToolAgentLoop`. Installed old `000024-runtime` retains it. | **Persists.** P/runtime.md “Improvement and change admission” connects launcher settings directly to the asynchronous context-management loop. `RT-RTE-training-rollout` names `StatelmToolAgentLoop` as owner but its selection predicate lists tool parsing and budgets, not the loop selector. Neither dataset name nor fallback appears anywhere in the renewed set. |
| Public synthesis loses the architectural qualification and verification accepts the broader chain. | O/synthesis.md “From rollout experience to later policy”; archived `000035-report-verification` accepts the connected training account. | **Persists.** P/synthesis.md “What the training path adds” describes training snapshots and branches unconditionally at this source boundary. Its missing-data/no-operation limits do not disclose the generic alternative. P/report-verification.md “Evaluation and training” and “Consequential omission search” accept the training chain and stop without resolving selection; synthesis verification accepts the same dependent account. |

The other useful distinctions from the earlier publication remain visible in renewed public prose: task-local stores, state-local rather than universal FSM admission, deterministic review recovery, semantic-loss countercases, non-default restore, oversized-context possibility, logger versus trajectory-answer provenance, optional merge's unestablished shipped invocation, and update wiring versus demonstrated benefit. These are preservation observations, not a fresh proof of every source claim.

The new profile-verification limit about an omitted compaction learning-authority consumer is already carried in the synthesis Limitations table and synthesis verification. It is an explicitly partial inventory issue, not the selector defect and not a reason to demand full reconstruction here. Were the selector fault resolved, that recorded public limit could support a qualified positive disposition; it cannot repair a different missing public condition.

## Earliest author output and missed barriers

Original lineage is retained under `A/before/state/attempts/` and `A/before/state/versions/`. The boundary precursor is `000003-boundary` (`2c3771a58a19…`); the first decisive record overclaim is `000005-runtime` (`1e7502065807…`), independently inspected here. `000024-runtime` (`7291f97c81b2…`) is the installed archived continuation, not the origin. The first inspected original verifier `000022-report-verification`, output `56ba772a22886901963fa0ef8a7c7eb9c673cfd2fb0a9b45b360d81b49f9af90`, accepts `RT-RTE-rollout-training` in its training-record row while asking for unrelated prediction/merge repairs. The depth report's later final missed barrier `000035-report-verification` remains applicable; it is not the earliest inspected opportunity.

Renewed lineage is separately established, not inferred from old text:

- `000051-boundary` emits installed `5389cfb9f9f2…`: earliest renewed narrative precursor.
- `000053-runtime` emits `cc1f6154bcfd3d399579eb7416ec07d914e4db260495f1eb2de0684596ecf65c`: its initial improvement paragraph and `RT-RTE-training-rollout` already omit the selector. This is the earliest evidenced renewed decisive author output.
- `000070-report-verification` emits `75a6c69c20728aa16c46c8d2fc1655b5d7072cf6b3869306974629ebdf4d0d9c`: the first renewed report-verification barrier routes other blockers and discusses training omission searches, but not dispatch selection.
- `000072-runtime` emits installed `e06b83c06cdc…`; the omission survives its correction. Final `000083-report-verification` emits installed `7ec80fc51c08…`, declares no blockers or limits and accepts training wiring.
- `000089-synthesis` emits `ed357771611a…`; `000091-synthesis-verification` emits `7b71afe16523…`. These propagate/accept the broader account rather than establish independent selector evidence.

Attempt output mappings were read directly; the initial renewed runtime and first renewed verification version bytes were hash-checked. The report-verification instruction pin is `41163de951b29115cfad318fa1f3baf7b36a94ee730dbb93b2d91397145490b2`: it requires independent checks of conditions, ordering and consequential omissions, with correction routed to the responsible author. Successful checks and later dependent repetitions are not alternative evidence of fulfillment.

### Recovery depth and separate stops

- **Author restart:** boundary narrative alignment and runtime route correction, with dependent epistemic/profile/public claims checked after correction. The decisive record rebuild begins at runtime; if preserving the valid boundary identity/scope, do not silently preserve its unqualified training narrative.
- **Verifier restart:** independent report verification, then affected profile and synthesis verification. A synthesis-only restart cannot correct the underlying route account.
- **Deep reconstruction:** not established as necessary. This is a local dispatch/admission qualification in an otherwise supported source boundary, not a new source or target selection problem.
- **Operational/authority:** no new operational violation was established by the limited trace sample below. Old coverage limits remain limits; renewed acceptance cannot retroactively certify historical obligations. No recovery authority is granted.
- **Binding/incumbent:** no stop found; exact maps and source/method identities bind. The semantic hold is independent of deterministic validation.

## Bounded operational evidence

Used stored attempts and pins before examining the 402,773,542-byte renewed trace at `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/batch-19/AAS-2026-10-13-contextpilot-30d0d09e6cdc-01.output`. A streaming filter selected settled outer `message_end` worker results, not repeated streaming frames. Inspected only bounded nested source-call/result samples for boundary, initial runtime and final report verification. This was not a whole-log substantive read or a complete worker-compliance screen.

Exact zero-based nested-message locators within those settled outer results:

| Outer line / worker | Same-worker executed call and paired result | Observation |
| --- | --- | --- |
| 789 / `000051-boundary` | messages 14→15; `call_j2LAoInT3c9dqRXkbE6f0oqb\|fc_056aed47de890b66016ad327e4f2b887d2a6ddad6aa5e3a42d` | Read `related-systems/Tencent--ContextPilot/README.md`; result `isError: false`. |
| 1149 / `000053-runtime` | messages 21→22; `call_KagfgMQXVVEWn9KPpW68ZVNh\|fc_089db8b1e91378ea016ad328a4a70887d290df9ea979d6a87e` | Read `infer/src/contextpilot_fsm.py`, offset 826, limit 245, under S; result `isError: false`. |
| 4028 / `000083-report-verification` | messages 56→57; `call_9mPz0hPL9Om7a5tRuWD6Jlyw\|fc_08ae6c726862981f016ad33004088887d281a0e83ba55eee5b` | Read S's `infer/src/contextpilot.py`, offset 540, limit 210; result `isError: false`. |

Each selected worker result reports exit code zero. A second source-read pair per worker was also screened. These observations establish actual source inspection, not mere availability or an unexecuted proposal. They do not prove selector inspection, complete invocation recovery, every write's authority, absence of indirect legacy reads, or compliance by unsampled workers. The semantic missed barrier is established by the submitted output against source, not an inference about worker cognition.

The prior audit reported a broader 17-worker settled-action screen and an exact source-read pair for the old final verifier. This audit read that historical report, not the 419 MB original trace. Its historical coverage limits and findings remain attributed, not freshly certified or erased by the renewed run. No prior operational hold specific to ContextPilot was established in the supplied prior hold/depth findings beyond the semantic defect and their stated verification limits.

## Validation and remaining coverage limits

Executed from W in its exact prepared environment:

```text
.venv/bin/commonplace-validate kb/agentic-system-analyses/retained/contextpilot
VALIDATION SUCCESS
Target: kb/agentic-system-analyses/retained/contextpilot
Scope: kb/agentic-system-analyses/retained/contextpilot
Files analysed: 1
Text files: 0
Diagnostics: 0 failures across 0 subjects; 0 warnings across 0 subjects
```

The count denotes one directory artifact, not twelve individually counted text files. No quotation notice was emitted. Deterministic success does not resolve this semantic hold.

From W, also executed:

```text
.venv/bin/commonplace-validate /home/zby/llm/commonplace/kb/work/agentic-system-reruns/audits/batches-19-20/AAS-2026-10-13-contextpilot-30d0d09e6cdc-01.md
VALIDATION SUCCESS
Target: /home/zby/llm/commonplace/kb/work/agentic-system-reruns/audits/batches-19-20/AAS-2026-10-13-contextpilot-30d0d09e6cdc-01.md
Scope: /home/zby/llm/commonplace/kb/work/agentic-system-reruns/audits/batches-19-20/AAS-2026-10-13-contextpilot-30d0d09e6cdc-01.md
Files analysed: 1
Text files: 1
Diagnostics: 0 failures across 0 subjects; 0 warnings across 0 subjects
```

Only this assigned report was authored. No target code, tests, examples, provider, training job or benchmark was executed; no install/fetch, source/state/configuration edit, reset, advance, integration, commit or delegation occurred. No missing source blocked the dispatch judgment. Actual transformed-dataset selection, target operation, learning benefit, full memory-axis coverage and the historical review's reflection interpretation remain outside this bounded decision. Stop here rather than expand into a second analysis.
