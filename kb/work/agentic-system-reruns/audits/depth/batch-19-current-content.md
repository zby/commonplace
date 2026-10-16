# Batch 19 current-content: fault depth

## Bounded result

All seven holds remain. Six runs have faults at or before the initial analyst
reports; AREX-Skill has an unsupported assessment over otherwise useful installed
state records, not an established bad memory classification. ModularRSI has two
separate gate faults. A restart of public synthesis alone would not rebuild the
other six accounts. Agent Skills also retains a separate reserved-owner and
historical worker-compliance stop.

This is diagnosis under the [depth commission](../../batch-19-depth-commission.md),
not clearance, recovery or new target analysis. The restart recommendations below
are recommendations to the parent, not operations performed or authority to
perform them. Verification restart means the earliest warranted independent
judgment; author restart means the earliest authored material needing correction.
They are deliberately different.

## Inputs, locators and byte binding

Resolved the seven exact rows from
`kb/work/agentic-system-reruns/audit-integration-intake-2026-10-15.json`.
Its recomputed SHA-256 is
`31fabfd2e3a3bdb7046a1e8f4a5ff7af6bea9d3ee43d8afd2529a8dd8fb3ed19`,
matching the commission ledger. The two later audits come from
`audit-integration-later-46.json`, not the intake's earlier unaudited status.
Read all seven assigned audits completely, and the linked historical Agent Skills
path-confusion report. Each assigned audit's current digest matches its intake
or later-ledger pin.

Path conventions below make each evidence locator exact:

- `H` = `/home/zby/llm/commonplace/.commonplace/worktrees`.
- `E` = `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees`.
- For each row, `W` is the stated worktree, `R` is
  `W/kb/agentic-system-analyses/state/<exact run ID>`, `P` is
  `W/kb/agentic-system-analyses/retained/<slug>`, and `S` is
  `W/related-systems/<source directory>`.
- Attempt locators mean `R/state/attempts/<attempt>.json`; an output hash names
  `R/state/versions/<full hash>`. Prefixes below uniquely identify those hashes
  within that run. Installed member hashes were compared with attempt outputs;
  those comparisons, not downstream repetition, establish the version lineage.
- Every row's prepared command directory is `W/.venv/bin`, resolved from the
  intake and hash-checked preparation. No prepared execution command was invoked.

| Slug and exact run ID | W | Source identity / directory | Method revision | Frozen source revision |
| --- | --- | --- | --- | --- |
| agent-skills-for-context-engineering; `AAS-2026-10-12-agent-skills-for-context-engineering-2423c2f20f83-01` | `H/agent-skills-for-context-engineering-2423c2f20f83` | `https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering`; `muratcankoylan--Agent-Skills-for-Context-Engineering` | `cd6e8250c5277c5c6295b6940a9b01e034c9daa7` | `9ff0c99108b36d3b886defd825d8ac1f47dba374` |
| contextpilot; `AAS-2026-10-13-contextpilot-30d0d09e6cdc-01` | `H/contextpilot-30d0d09e6cdc` | `https://github.com/Tencent/ContextPilot`; `Tencent--ContextPilot` | `4266dabc470929df0ff753e57fee0c55d7b87fc6` | `782cbb6611fb610c4cf6fafda6022b7e89cae191` |
| openrsi; `AAS-2026-10-14-openrsi-c72dec9967a3-01` | `H/openrsi-c72dec9967a3` | `https://github.com/FrontisAI/OpenRSI`; `FrontisAI--OpenRSI` | `f7732e9c6bc5622031571d2d429bc017253eb64f` | `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa` |
| modularrsi; `AAS-2026-10-14-modularrsi-96b89989168e-01` | `H/modularrsi-96b89989168e` | `https://github.com/IQuestLab/ModularRSI`; `IQuestLab--ModularRSI` | `8414ddbd35da24645c020789bd824cb9749fa677` | `b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9` |
| jaz; `AAS-2026-10-15-jaz-a94bea79c61a-01` | `H/jaz-a94bea79c61a` | `https://github.com/jaz-lang/JAZ`; `jaz-lang--JAZ` | `a568c6dc489ad546374536b642c3889ce23149a8` | `0803d4971be785e95b80054b02259664d70fa3da` |
| arex-skill; `AAS-2026-10-15-arex-skill-1871063034b5-01` | `E/batch-17-arex-skill` | `https://github.com/VectorSpaceLab/AREX-Skill`; `VectorSpaceLab--AREX-Skill` | `a320038ed1a423b051eedbcec593172f8c2032f4` | `ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6` |
| autogenesis; `AAS-2026-10-15-autogenesis-9bcfa57fd7c1-01` | `E/batch-17-autogenesis` | `https://github.com/DVampire/Autogenesis`; `DVampire--Autogenesis` | `a320038ed1a423b051eedbcec593172f8c2032f4` | `5b070d5cd497e951a188a01409138e8b530eaf4a` |

**Fresh binding result:** recursively enumerated and hashed every regular file
under each P, including nested paths if present. Each actual set is exactly 13
files, with no extra files, and equals both immutable intake maps and the actual
completed `R/effects/publish.json:new` map. Each effect is completed. Preparation,
run-definition and effect bytes also match their intake pins. Source HEADs match
the revisions above and read-only source Git status is empty for all seven.

For reproducible compact identification, the final column below is SHA-256 of
UTF-8 `json.dumps(current_map, sort_keys=True, separators=(',', ':'))`, where keys
are P-relative POSIX paths and values are file SHA-256 strings. This is a newly
computed map fingerprint, **not** a historical audit fingerprint. The complete
per-file reference maps remain in the immutable intake.

| Slug | Completed publish attempt | Assembled manifest SHA-256 | Current recursive-map fingerprint |
| --- | --- | --- | --- |
| agent-skills-for-context-engineering | `000034-publish` | `595333b43c8bb4cfd789ec06c4e99ad377021e59e7ce18d94070842cd302a5ae` | `fbdb58c15a6a57084738a8ee3848420cbe5e8b9378f7cb63a56a9fb5204e2a02` |
| contextpilot | `000050-publish` | `0ffa71f5ee5c1e74c4ff3ee9b6cf8c99fff5256bcd26247024891c73f7cc5f8e` | `e81b8577cc24c33ab2d094c0e38b6468cdcf4772cec2a0fe8f9577fee4d20ea0` |
| openrsi | `000037-publish` | `149175fd1c6761ee95b03cd073af10bcb26f5385de0003115fd8870d404671b5` | `2308d4b243d28f41d46ec48e8f3c95958be5e4ff865985ed9195126b50976640` |
| modularrsi | `000043-publish` | `8323638d0eee402db0661bc9d85f43d74005be6a0e993d49c4bd73345e9a9d47` | `d640b8e6b62872ed2a102260d7a2b99ed10c2ac2b27ed878a4e13dd579f189d4` |
| jaz | `000037-publish` | `8377ad2b50098b77f737c18a13bf4a7ed4af8e4bf0286e4bc5ea093c4bb6af9a` | `a1a8a58e47f29a9f67ec258030211fe90ce40a9117cee9455db9a1b340ba5974` |
| arex-skill | `000033-publish` | `650596ab4865595da7ddecc9714286582c0672df96146dc1d8ebc541fbcc6252` | `9badb2bdf23dc8188fa6613601c4bb084d5e2a5cc33b888ffaf1438d82da89e3` |
| autogenesis | `000033-publish` | `fadbf61c0eb84397482689ea962e8103dbe0aa2ec3b0f4a52de4bec825d9a141` | `c436916c2d39f26c014946dfa1a04a9f7e67f494c2a29f1cb084bb2df3468130` |

Historical comparison: AREX's audit retains its complete 13-file map, which
matches. The other audits retain full-map equality statements plus selected
hashes rather than independent complete audit-time maps. Their retained manifest
hashes (and JAZ's public member hashes) match now; no historical mismatch was
found. The intake independently retains full maps for all seven. A prior prose
assertion of equality is not a separately recomputable historical map.

## Pinned missions and restart authority

Read the actual model-attempt names and pinned job instructions, not just the
current workflow labels. The relevant instruction pins are identical across
these seven runs; they are retained in each R's versions directory:

- `boundary`, `f0f7995a2524…`: trace shipped entry points and consumers, establish
  frozen identity and functional scope. A local defect does not demand a new source.
- `runtime`, `07451230c318…`: trace ordinary invocation, material routes and
  admission; challenge consequential claims with source countercases.
- `epistemic`, `7d698f1f7cbb…`: trace evaluators and consequential consumers;
  supplied runtime is provisional, not an inspection limit.
- `reconciliation`, `679917ce1d56…`: connect without judging, rewriting or
  strengthening the analysts. Its repetition cannot independently certify them.
- `report-verification`, `41163de951b2…`: independently check conditions,
  ordering, source support and consequential omissions; request correction to
  the responsible report or return problem for a boundary contradiction.
- `memory-profile`, `d548d5a9a1b0…`, and `profile-verification`, `6d359c591e5b…`:
  classify/check accepted records, not repair their underlying source account.
- `synthesis`, `3000dccb8643…`: public account from accepted members; no new
  evidence or record repair. `synthesis-verification`, `f737a0a1dc32…`: judge
  that public account; a discovered record fault becomes a public limit or problem,
  not a direct reopening of reconciliation.

Thus report faults normally require a **report-verification** restart, with
corrections routed to their actual author jobs. Later public verification is
another failed containment opportunity, not independent source confirmation.
No new profile-level error is established merely because a profile cites a
faulty route. Recheck affected classifications after correcting their premises.

## 1. Agent Skills: stronger doctrine already in the first epistemic output

Prior audit: [exact publication](../unintegrated/AAS-2026-10-12-agent-skills-for-context-engineering-2423c2f20f83-01.md).

- **Fault/source:** P/`epistemic.md:275`, `EPI-CLM-evidence-review`, attributes
  “no published change while conflicting sources remain unresolved.” S/
  `researcher/runbooks/autonomous-research-loop.md:52` instead says “Record both
  claims and prefer no published change until resolved.” The complete runbook
  preserves other PR prerequisites but does not turn this preference into a ban.
  The published record itself quotes the weaker wording at line 288.
- **Origin and propagation:** `000008-epistemic` output `942f1b4f57c8…` is the
  installed epistemic version. There is no intervening author correction in the
  stored model-attempt sequence. This is an initial author overstatement, not a
  reconciliation loss or synthesis-only expansion. Reconciliation `000019`
  (`334345e7ad9b…`) does not supersede this claim. The profile's memory mappings
  do not repair it. Synthesis's broad distinction between doctrine and software
  gates likewise cannot repair an incorrectly attributed doctrine record.
- **Failed barrier/restarts:** `000022-report-verification`, `8c1a74d368b6…`,
  explicitly accepts the source-curation claim, gates and runbook; its pinned
  mission had authority to request epistemic correction. Restart verification at
  `report-verification`; author rebuild at `epistemic`, not `synthesis`. Recheck
  downstream public qualifications and verification after correcting the claim.
- **Separate stop:** [historical path-confusion audit](../path-confusion-agent-skills.md)
  retains worker `000008-epistemic`'s altered `--artifact` path, manifest-load
  failure, inaccurate “exactly as supplied” attribution and incomplete independent
  grounding. Its exact same-worker call/result locator is T line 31, W52/W53,
  `call_HJkZasq3srhJVwSck7Vu0ii5|fc_0f71b3e42b964d52016acceeeb18ac87d2b1a36d03369e21b9`.
  This investigation read that report, not the original trace; it does not newly
  certify the historical action. Later publication cannot retroactively fulfill
  that worker's obligation. A stage reset cannot release the reserved owner,
  settle that attribution or dispose of the grounding concern. Parent must obtain
  the reserved owner's explicit disposition before any recovery.
- **Preservation/confidence:** retain acquisition, source/method identity and
  otherwise valid boundary. High confidence in semantic origin and missed barrier;
  historical compliance remains inherited evidence, not re-audited clearance.

## 2. ContextPilot: missing selector starts in boundary narrative, then runtime

Prior audit: [current-batch audit](../bash-current-contextpilot.md).

- **Fault/source:** the training chain requires dataset `agent_name` selecting
  `statelm_tool_agent` or a configuration override. S/
  `train/verl/experimental/agent_loop/agent_loop.py:1006–1008,1080–1121` fills a
  missing name from the default and instantiates the selected registry entry.
  `train/verl/trainer/config/rollout/rollout.yaml:207–208` defaults to
  `single_turn_agent`. The complete `statelm_tool_agent_grpo.yaml` inherits
  `ppo_trainer` without overriding it; the complete 8B launcher sets tools,
  partial rollout and ContextPilot options, not this selector. The audit's
  registration and generic-loop locators remain `statelm_agent_loop.py:451–452`
  and `single_turn_agent_loop.py:26–64`. Unfrozen transformed data may supply the
  proper value; its absence or a broken training run is **not** established.
- **Origin:** P/`boundary.md:46`, `000003-boundary` (`2c3771a58a19…`), already
  moves from manager/registered loop to ContextPilot production/consumption
  without this qualification. It is an early narrative omission, not an invalid
  source identity or scope exclusion. The decisive route overclaim is in initial
  `000005-runtime` output `1e7502065807…`, `RT-RTE-rollout-training`: launcher →
  worker → `StatelmToolAgentLoop` with no selector/fallback. Revised `000024-runtime`
  (`7291f97c81b2…`, installed) retains it. It was not introduced by that revision.
- **Propagation/barrier:** reconciliation `000032` (`1e84bae98a80…`) preserves
  training-to-update wiring while resolving different prediction/merge disputes;
  it did not delete a selector qualification present upstream. `000035-report-verification`
  (`4790b1004617…`) accepts the branch/credit/update chain. Profile `000041`
  (`53dca5d70b2c…`) maps that implemented chain; no independent selector proof
  appears there. Synthesis `000045` and verifier `000047` carry the unqualified
  architecture. Those are dependent repetitions.
- **Restarts:** verification at `report-verification`. For the first faulty
  authored account, restart `boundary` **narrative** and dependent `runtime`;
  `runtime` is the minimum record-rebuild depth if the parent preserves the valid
  boundary as an evidence/scope declaration. Do not silently leave its training
  paragraph unqualified under that choice. Reverify dependent epistemic/profile
  and public claims; no new acquisition is needed to state the conditional route.
- **Preservation/confidence:** keep opening/acquisition, source pin, broad
  whole-system scope and dataset-unavailability limit. High confidence in the
  initial runtime omission and boundary precursor; actual dataset activation is
  unknown and must remain so.

## 3. OpenRSI: initial runtime omission of default answer visibility

Prior audit: [exact publication](../unintegrated/AAS-2026-10-14-openrsi-c72dec9967a3-01.md).

- **Fault/source:** S/`OpenMLE-Gym/openmle-sandbox/README.md:80–109` places
  candidate execution and scoring on the same worker and explicitly calls the
  private directory an evaluation convention, not a security boundary. Its
  `node_workers/sandbox_builder/start_sandboxes.sh:150–154,177–181` mounts the
  shared root read-only with writable overlays. Read-only prevents writes, not
  reads of `data/private/test_answer.csv`. This establishes possible access on
  the shipped default route, not actual leakage or all-deployment insecurity.
- **Origin:** initial `000005-runtime` (`65680abfbc5d…`, installed) discusses
  alternate isolation grants at lines 32–39 and score authority at 148–170 without
  stating this concrete visibility limit. The boundary includes the sandbox and
  scoring responsibility; no excluded-source problem forces a new boundary.
  The epistemic account and reconciliation `000019` (`25bc4eba0ed9…`) retain
  score/check distinctions but do not recover the omitted qualification. No
  previously adequate qualification was found to have been lost in reconciliation.
- **Barrier/restarts:** `000022-report-verification` (`56bc0dbc34a7…`) accepts
  score authority and remote execution qualifications while leaving this default
  counterroute unstated. Its omission-search authority was sufficient. Restart
  verification there; rebuild `runtime` first, with applicable epistemic score
  assessments qualified next. Profile `000028` (`63b222703fd2…`) is not the origin.
  Synthesis `000032` and verifier `000034` need to carry the corrected evaluation
  limit; generic isolation and attribution caveats are not substitutes.
- **Preservation/confidence:** retain acquisition/boundary and positive search,
  memory and training routes. High confidence in initial runtime omission; no
  benchmark execution, numerical effect or historical candidate conduct inferred.

## 4. ModularRSI: two independent initial gate-account faults

Prior audit: [exact publication](../next-publications/AAS-2026-10-14-modularrsi-96b89989168e-01.md).

**H1 — review pass-through omitted.** S/
`src/harbor/agents/terminus_2_modular/self_evo/online_evo.py:1083–1098`
returns `passed=True`, verdict `skipped`, on timeout/error. The separate
missing-structured-verdict branch at 1106–1135 can pass until its health breaker
trips; timeout/error returns precede that accounting. Caller 1682–1710 gates on
`review.passed`, not an accepting substantive verdict. P/`runtime.md:186` says
configured review must pass but does not expose this distinction. This omission
is already in `000005-runtime` (`10e06ff18c46…`, still installed). Workflow and
public gate summaries do not restore it. Do not describe every review skip as
breaker-governed or claim an actual skipped-review promotion occurred.

**H2 — dormant partial-file acceptance described as active.** The same producer
at 1137–1155 explicitly disables partial accept and returns `drop_files=[]`;
other returns use the empty default (`_ReviewResult:974–984`). The caller's
1712–1741 branch remains but is not activated by this producer. Initial runtime
`000005` positively describes dropping files at lines 187/191. Initial
`000009-workflow` (`851cfa397440…`, still installed) independently repeats that
review can partially accept files at line 50, dependent on the runtime route.
This is a positive capability error, not merely H1's missing limitation.

Reconciliation `000029` (`84670088ff01…`) preserves post-review-repair temporal
limits; it neither repairs these gate claims nor loses an upstream correct
producer account. `000032-report-verification` (`29f6a8b55199…`) expressly
accepts “partial drops” and gate ordering. An earlier verifier `000022` requested
a different epistemic/editor-history correction; the resulting epistemic
`000024` does not change the unchanged faulty runtime/workflow versions.
Profile `000034` (`8da8378b4088…`) is downstream mapping, not either fault's
origin. Synthesis `000038:32` repeats active file dropping and omits fail-open;
verifier `000040` accepts bounded review without addressing either discrepancy.

**Restarts:** `report-verification` for both. Author rebuild `runtime` for H1;
`runtime` plus dependent `workflow` for H2, followed by reconciliation and
reverification of affected records/public text. Preserve correct post-review
repair, non-performance and editor-history qualifications. Acquisition/boundary
can stand. High confidence: both initial installed report versions and the
producer/caller discrepancy are retained; no target run or all-producer inventory
was performed. An alternate active producer would need a concrete frozen caller
connection, not inference from the dormant branch.

## 5. JAZ: invocation-local replay overclaim already in initial runtime

Prior audit: [exact publication](../next-publications/AAS-2026-10-15-jaz-a94bea79c61a-01.md).

- **Fault/source:** S/`src/jaz/hooks/builtin/replay.py:393–400` explicitly assumes
  sequential invokes and names sibling-queue mis-serving and wrong divergence
  latching under concurrency. Bodies 509–541 push children and choose the stack
  top rather than the query's invocation identity. The following send path uses
  that node's cursor/latch. This is an implementation condition, not a newly
  observed failed replay.
- **Origin/propagation:** `000005-runtime` (`22f3dcac941f…`, installed),
  `RT-RTE-replay-response` at P/`runtime.md:330`, describes active-invocation
  selection/live fallback without the condition. Memory `000007` annotates and
  classifies this same selector, not an independent identity-routing proof.
  Epistemic `000008` (`2410c86947c3…`) even mentions “stack concurrency” as a
  parent-record limit at line 60, but its parent has no such limit and its own
  replay-check record presents per-invoke withdrawal. This is a dangling
  qualification/dependency defect alongside the initial runtime omission, not
  a qualification removed by reconciliation `000019` (`be24d57261a5…`).
- **Barrier/restarts:** `000022-report-verification` (`72d61c14ada0…`) accepts
  the records. Restart it to request runtime correction and alignment of the
  epistemic dependency; author rebuild starts `runtime`, with memory/epistemic
  selector descriptions checked against the correction. Profile `000028`
  (`39d4cb5f9de4…`) already corrected a different provenance-coverage fault;
  preserve that correction rather than treating it as the replay origin.
  Synthesis `000032` and verifier `000034` must carry sequential nesting and
  concurrent misrouting consequences, not just generic fidelity uncertainty.
- **Preservation/confidence:** keep acquisition/boundary, early workflow-export
  limitations and non-rollback distinction. High confidence in report-level
  origin; no concurrent execution or complete replay proof attempted.

## 6. AREX-Skill: supported state records, unsupported reflection assessment

Prior audit: [later publication](../post-migration/AAS-2026-10-15-arex-skill-1871063034b5-01.md).

- **Fault/source:** the prepared method's `agentic-analysis-records.md:336` and
  `kb/notes/definitions/reflective-system.md` define reflection as an
  aspect-relative architectural capacity, not observed improvement. Within
  DisCo plus retained guidance, installed-library inventory/digests represent
  the managed library. S/`cli/packages/coding-agent/src/core/repo-skills-library-manager.ts`
  reads prior state and live trees to reject conflicts at 1435–1460;
  `detectConflicts:1214–1248` compares managed content with prior digests.
  `1517–1547` constructs/writes next state from staged inventory/digests and
  installs collection/router/state. Thus represented changes update retained
  state, and state-mediated operations affect later installed guidance. This
  does not establish scientific warrant, model self-theory, crash atomicity or
  successful improvement.
- **Depth distinction:** initial runtime `000005` (`2e470dc6d660…`),
  `RT-RTE-library-update`, and memory `000007` (`e3a07a03c24d…`),
  `MEM-OBJ-library-state`, already retain the relevant positive mechanisms.
  Epistemic `000008:261` warns against inferring reflection from packaging or
  iteration; that caution alone is not a contrary architectural finding.
  Reconciliation `000019:48` speaks of unestablished *exercised* properties; it
  does not erase the installed-state witness. No faulty profile value is
  established in `000024-memory-profile` (`d2b12819495c…`).
- **First explicit unsupported judgment/barrier:** `000022-report-verification`
  (`723c9f818d94…`), P/`report-verification.md:48`, calls reflection an
  unestablished property without disposing of the retained state witness.
  Synthesis `000028` (`a6f7c590677b…`) makes the stronger, explicit claim at
  line 46 that reflection's **two causal directions** are unestablished;
  `000030-synthesis-verification` (`55cb98459ba7…`) endorses it. Therefore the
  earliest evidenced faulty blanket judgment is report verification, while the
  explicit author overgeneralization is synthesis. A faulty source-native
  record or reconciliation deletion has not been demonstrated.
- **Restarts:** verification at `report-verification` to resolve its own blanket
  judgment under the pinned definition. Author rebuild of the public assessment
  starts at `synthesis`, using the existing records, not an automatic runtime or
  memory rebuild. `synthesis-verification` is the immediate public failed barrier
  and must be rerun. If the workflow requires an explicit aspect-level record
  assessment before that can be stated, route a bounded `runtime`/`epistemic`
  addition through report verification; that is a conditional record-completion
  need, not evidence that the existing mechanism records are false.
- **Preservation/confidence:** keep acquisition, boundary, positive installed
  state records and memory classifications. High confidence in the public
  overgeneralization and architectural counter-witness; moderate confidence in
  the precise earliest assessment scope because earlier “unestablished” wording
  mixes exercised and architectural properties. No live installation inspected.

## 7. Autogenesis: startup omission begins in boundary entry narrative

Prior audit: [later publication](../post-migration/AAS-2026-10-15-autogenesis-9bcfa57fd7c1-01.md).

- **Fault/source:** S/`autogenesis/tool/__init__.py:4` unconditionally imports
  `.other`; the frozen package directory has neither `other.py` nor `other/`.
  `autogenesis/gateway/service.py:66` and `examples/run_meta_agent.py:37` import
  `tool_manager` from that package. `autogenesis/cli.py:48–54` imports the
  Gateway for terminal sessions. Ordinary loading reaches the missing local
  module before the named task mechanisms; installing external dependencies
  does not supply an absent relative module. No import or test was executed.
- **Origin:** `000003-boundary` (`34b5f24c1f7c…`), P/`boundary.md:26`, already
  describes terminal Gateway startup and direct-driver task submission without
  this concrete prerequisite failure. Initial `000005-runtime`
  (`9fc67c7cd50f…`, installed) repeats it at lines 16–18 and declares
  `RT-RTE-gateway-task` wired without the startup qualification. This is an
  entry-chain omission, not a new discovery introduced by synthesis.
- **Barrier/propagation:** reconciliation `000019` (`865ec808b2ea…`) retains
  recovery/facade uncertainties but no import blocker. `000022-report-verification`
  (`abf77bd50e72…`) accepts the Gateway chain and cites direct-driver omission
  searches. Profile `000024` (`f4984817e36d…`) classifies internal retention;
  it supplies no proof that ordinary startup reaches those mechanisms.
  Synthesis `000028` and verifier `000030` repeat the chain. General no-execution
  and installation-unestablished statements do not state this known static fault.
- **Restarts:** verification at `report-verification`. Earliest affected author
  output is `boundary` narrative, followed by `runtime` entry-path rebuild;
  retaining boundary identity/scope is defensible, silently retaining its
  startup paragraph is not. Internal mechanism descriptions can remain as
  conditional source-level architecture. Do not require startup repair or new
  source acquisition merely to qualify this frozen checkout's account.
- **Preservation/confidence:** retain acquisition/source/method and coherent
  whole-system boundary. High confidence in missing-module origin and failed
  barrier; no fresh installation result, seven-error count or runtime outcome
  asserted. Already-public memory-facade and smoke limitations remain separate
  and are not replaced by this startup finding.

## Limits, stops and validation

No target code/tests/services, acquisition, analytical worker contact, delegation,
engine advancement/reset/judgment, accepted-output edit or Git write was performed.
Only this report was authored. Original trace streams were not needed to decide
these source/wording faults; prior audits' paired-action findings remain attributed
leads, not freshly established actions. Missing/uninspected traces do not mean no
source was read. One overbroad local search returned unrelated retained-member
matches; those were not used to diagnose any excluded run or incumbent.

No inaccessible evidence blocked the semantic depth recommendations. Remaining
limits are actual activation/outcome evidence, non-exhaustive source/variant
inspection, historical audit-map availability as distinguished above, AREX's
assessment-scope ambiguity, and Agent Skills' unresolved reserved-owner and
historical compliance disposition. Nothing here releases those stops or the
existing holds. A later accepted run cannot erase a historical operational fault.

Ran `commonplace-validate kb/work/agentic-system-reruns/audits/depth/batch-19-current-content.md`:
`VALIDATION SUCCESS`; Files analysed: 1; Text files: 1;
Diagnostics: 0 failures across 0 subjects; 0 warnings across 0 subjects.
Validation is restricted to this frontmatter-free workshop report. Deterministic
validation checks its admissibility, not these semantic conclusions.
