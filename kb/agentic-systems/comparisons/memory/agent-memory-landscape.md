---
description: "Commit-bound memory comparison of all 191 current analyses (Oct 2026): wired existence counts per profile axis, withheld distributions, and grounded contrasts in admission, read-back, curation and trace learning"
type: types/note.md
traits: [has-comparison, has-external-sources]
tags: [agent-memory]
---

# What the 191 current agentic-system analyses show about agent memory mechanisms (October 2026)

The question: across every current analysis set, which memory mechanisms are wired, how are they admitted, read back, curated and fed by traces, and which population-level conclusions does the evidence withhold?

The short answer has three parts. First, the population supports existence counts: lower bounds on how many systems wire a mechanism. It does not support complete-value distributions, because almost no set assesses an axis completely. Second, every positive finding is static wiring or weaker. No finding in the population reaches `observed` or `causally supported`. Third, within those limits some contrasts are clear. Automatic admission is nearly universal, while manual admission is often only instructed or afforded. Push read-back mostly selects by coarse availability or identifiers, not inferred relevance. Synthesizing curation is rare. Trace-fed learning is wired in most code-grounded systems, but that count includes thin forms such as access counters.

## Evidence boundary

- **Mode:** current snapshot.
- **Inputs commit:** `5f92f75e502f8cd11ec318d8e69d3e17cbe53df3`. This commit holds every retained set, the profile and boundary contracts, the matrix reader under `src/commonplace/lib/` and `scripts/`, and the [synthesis instruction](../../instructions/synthesize-agent-memory-landscape/SKILL.md). Before reading, `git status --porcelain` on those paths printed nothing.
- **Selection rule:** all current analysis sets, with no `--review` filter. That is 191 sets under `kb/agentic-system-analyses/retained/`, one per source identity (191 distinct identities and 191 distinct runs). Nothing was excluded.
- **Matrix:** built with `scripts/build_systems_matrix.py` and no review filter. It exited 0, wrote 191 rows, and has SHA-256 `d68ae22877ff7b34ae598ce423b0a0d8f325ca180aef29880b09226403ec07a5`. The public [memory-systems.csv](./memory-systems.csv) is a separate output and is not this matrix.
- **Profile revision:** all 191 profiles are `comparison_version` 2. No revision-1 write-agency values are present, so no cross-revision pooling arises.
- **Source tiers:** 176 sets are code-grounded and 15 are doc-grounded. The counts below use only the code-grounded sets; the doc-grounded tier is discussed separately.
- **Boundary kinds:** 151 sets are whole-system, 34 cover a complete artifact with a partial loop, and 6 are subsystem-only. Among the code-grounded sets the split is 148, 24 and 4.
- **Analysis cutoffs:** 2026-10-11 to 2026-10-19. 139 of the 191 cutoffs fall on 2026-10-14 or 2026-10-15.
- **Lens:** the `memory-comparison` profile defined by the [memory profile type](../../../agentic-system-analyses/types/agentic-system-memory-profile.md). Examples are read from the cited members and their canonical records.
- **Validation:** `commonplace-validate` reports success for all 191 set directories. In 98 sets it also notes that quotations could not be checked, because the pinned source checkout is not present on this machine. Quotes in those sets are therefore unverified against source bytes here.
- **Verification mode:** local. Every count was recomputed from the matrix with an executable query. Each example was checked against its profile units, its cited records and the set's reconciliation. No independent reviewer was commissioned.

## How to read the numbers

- **Existence count:** the number of code-grounded systems (out of 176) with at least one profile finding for that value at `wired`, `observed` or `causally supported` basis. Each system counts once per value, however many stores or routes carry it. Both `known` and `partial` coverage count. Such a count is a lower bound for the population. It is not a prevalence estimate, because most axes are only partially assessed.
- **Weak-only:** systems whose findings for a value are all `claimed` or `afforded`. These are reported apart from the existence counts and never added to them.
- **No negatives from omission:** a missing value, an unresolved unit or a weaker finding is not a negative. Local `"no"` findings for trace learning are bounded to their unit and are reported as such.

### Complete-value distributions are withheld

A complete-value distribution answers questions such as "what share of systems are pull-only?". It needs an axis assessed `known`, with strong evidence for every positive finding. Few code-grounded sets meet that bar:

| Axis | Eligible sets (of 176) |
|---|---:|
| `storage_substrate` | 26 |
| `representational_form` | 15 |
| `read_back_signal` | 9 |
| `read_back_direction` | 7 |
| `write_agency` | 2 |
| `behavioral_authority` | 1 |
| `curation_operations` | 1 |
| `lineage`, `trace_learning`, `trace_source` | 0 |

No set in any tier assesses `trace_learning` or `trace_source` as `known`. The eligible sets are also self-selected: they are the ones whose inventories were small or simple enough to close. Their distributions would describe that subset, not the landscape, so this comparison reports none. This is the main limit on what the population can answer.

### Every positive finding is static wiring or weaker

The 191 profiles hold 9,852 findings. 7,958 are `wired`, 1,246 `claimed` and 648 `afforded`. None is `observed` or `causally supported`. Many cited records end with "operation conclusion status: uninspected" (for example [Hindsight's hook route](../../../agentic-system-analyses/retained/vectorize-io--hindsight/runtime.md#rt-rte-claude-hooks) and [SkillRL's policy update](../../../agentic-system-analyses/retained/aiming-lab--skillrl/runtime.md#rt-rte-policy-update)). Every count below therefore says that code connects a mechanism. None says the mechanism runs in deployment or changes outcomes.

## Wired existence counts by axis

All counts are over the 176 code-grounded sets. Axis assessments are given so that partial coverage stays visible.

| Axis | Axis assessment | Wired existence counts | Weak-only, most frequent |
|---|---|---|---|
| Storage substrate | partial 134, known 41, not-determinable 1 | files 160, in-memory 95, sqlite 60, vector 49, repo 29, graph 26, rdbms 25, kv 12, service-object 12, model-weights 7 | repo 10, service-object 4 |
| Representational form | partial 154, known 22 | symbolic 172, natural-language 163, parametric 82 | natural-language 11 |
| Lineage | partial 175, known 1 | other-compiled 164, imported 158, trace-extracted 140, authored 105 | authored 35, trace-extracted 17 |
| Behavioral authority | partial 168, known 7, not-determinable 1 | routing 164, knowledge 160, enforcement 149, ranking 138, validation 135, learning 123, instruction 94 | instruction 33, learning 24 |
| Write agency | partial 174, known 2 | automatic 173, manual 46 | manual 42 |
| Curation operations | partial 174, known 2 | evolve 148, consolidate 126, decay 111, invalidate 89, dedup 64, promote 46, synthesize 12 | consolidate 29, evolve 22 |
| Read-back direction | partial 158, known 18 | pull 169, push 139 | pull 7, push 5 |
| Read-back signal | partial 133, not-determinable 16, uninspected 10, known 10, inapplicable 7 | coarse 133, identifier 106, inferred-lexical 32, inferred-embedding 30, inferred-judgment 21 | coarse 4, identifier 3 |
| Trace learning | partial 151, not-determinable 24, uninspected 1 | yes 130 (local unit `"no"` in 5; no system-wide `"no"`) | yes 20 |
| Trace source | partial 140, not-determinable 35, uninspected 1 | session-logs 85, tool-traces 82, event-streams 35, trajectories 24 | session-logs 17, tool-traces 12 |

**Storage.** Files are wired in 160 of 176 systems, but rarely alone. 95 systems also wire at least one database-type substrate (sqlite, rdbms, vector, graph or kv). Only 25 wire files and nothing else. 16 systems have no wired file storage within their memory boundary. The profile classifies the operative store of retained parts, not their encoding.

**Authority.** All seven behavioral-authority values are each wired in at least 94 systems. Retained memory commonly routes, ranks, validates and vetoes, as well as informing. `instruction` has the lowest wired count and the most weak-only systems (33): standing directions from memory are more often asserted than traced to a consumer.

## Write admission: automatic is near-universal; manual is often instructed, not wired

Automatic admission is wired in 173 of 176 systems. Manual admission, meaning an explicit human decision on the content, appears in 88 systems at some basis. It is wired in only 46. In the other 42 it is only `claimed` or `afforded`: among those 42, 26 systems carry a claimed manual finding and 19 an afforded one (some carry both). Across the 176 systems the write-agency inventories contain 1,041 units. 240 of them are `not-determinable` and 113 `uninspected`, mostly because a generic caller does not show whether a human decided. So 88 systems with no manual finding is not evidence that 88 systems lack human control.

Three sets show the gap between instructed approval and wired control:

- **CQ** ([profile](../../../agentic-system-analyses/retained/mozilla-ai--cq/memory-profile.md), run `AAS-2026-10-14-cq-8fb3dc41c334-01`, manifest `8d2fcd66aa870727…`). The shipped skill says user approval is "a precondition of every direct `propose` call". The record classifies this as a natural-language policy with afforded implementation. The MCP handler and SDK clients accept content directly, and headless guidance lets the model admit proposals without a user ([RT-CLM-proposal-approval](../../../agentic-system-analyses/retained/mozilla-ai--cq/runtime.md#rt-clm-proposal-approval), [RT-RTE-knowledge-proposal](../../../agentic-system-analyses/retained/mozilla-ai--cq/runtime.md#rt-rte-knowledge-proposal)). Manual is afforded; automatic metadata, score, vector and drain writes are wired.
- **DocMason** ([profile](../../../agentic-system-analyses/retained/jetxu-llm--docmason/memory-profile.md), run `AAS-2026-10-13-docmason-deba9ae199d5-01`, manifest `f832cb91cd31db72…`). Manual admission is wired, but only for explicit user gate and scope decisions. The record notes that starting a question-answering run "is not approval of every generated sentence" ([RT-RTE-canonical-ask](../../../agentic-system-analyses/retained/jetxu-llm--docmason/runtime.md#rt-rte-canonical-ask)). Interaction capture and promotion into published memory are automatic.
- **cass_memory_system** ([profile](../../../agentic-system-analyses/retained/dicklesworthstone--cass_memory_system/memory-profile.md), run `AAS-2026-10-13-cass-memory-system-30c18219cf68-01`, manifest `2dcdb811124058ca…`). The single wired manual route is a batch yes/no approval when the initializer imports candidate "trauma" patterns into a permanent blocklist ([MEM-RTE-trauma-admission](../../../agentic-system-analyses/retained/dicklesworthstone--cass_memory_system/memory.md#mem-rte-trauma-admission)). Reflection, grading and curation writes are automatic. Generic add, mark and import callers stay `not-determinable`.

In all three, a wired manual route covers a narrow decision. Most retained content passes through automatic routes.

## Read-back: push usually selects coarsely

Pull is wired in 169 systems and push in 139. Among the 139 push systems, 56 wire at least one inferred selector (lexical, embedding or model judgment). The remaining 83 wire only coarse availability or identifier matching. All 139 carry at least one wired signal. 30 systems record no push finding at any basis. That is not evidence that they are pull-only: only 4 sets establish pull-only read-back at complete, strongly evidenced coverage. Seven sets mark read-back signal `inapplicable` on a known pull-only direction inventory.

Three contrasting push routes:

- **Hindsight** ([profile](../../../agentic-system-analyses/retained/vectorize-io--hindsight/memory-profile.md), run `AAS-2026-10-14-hindsight-34c2ca821edf-01`, manifest `3e9e67f75bff2a28…`). A Claude Code `UserPromptSubmit` hook builds a recall query from the prompt. It filters by score and emits the selected retained facts as `additionalContext` ([RT-RTE-claude-hooks](../../../agentic-system-analyses/retained/vectorize-io--hindsight/runtime.md#rt-rte-claude-hooks)). The profile records both embedding and cross-encoder-judgment selection on this route. Directive loading during reflect is a separate coarse push.
- **A-MEM** ([profile](../../../agentic-system-analyses/retained/wujiangxu--a-mem-sys/memory-profile.md), run `AAS-2026-10-16-a-mem-sys-eff95cd80440-01`, manifest `16fad56f4a88e833…`). The push consumer is the system's own memory-evolution model, not the answering agent. When a new note arrives, Chroma nearest-neighbour search supplies up to five retained neighbours, and the model decides whether to revise them ([RT-RTE-neighbor-evolution](../../../agentic-system-analyses/retained/wujiangxu--a-mem-sys/runtime.md#rt-rte-neighbor-evolution)).
- **Napkin** ([profile](../../../agentic-system-analyses/retained/michaelliv--napkin/memory-profile.md), run `AAS-2026-10-12-napkin-2b85bef38252-01`, manifest `54279eca29b4b0ad…`). The only positive push signal is a claimed always-loaded `NAPKIN.md` context note, selected whole rather than by relevance. Its search ranking serves explicit requests and therefore classifies as pull.

The profile counts relevance-ranked context injection as push only when no consumer requested it. Hindsight's hook is push; its ranked search results, returned on request, are pull.

## Curation: revision and forgetting are common; synthesis is rare

Wired curation operations: evolve in 148 systems, consolidate 126, decay 111, invalidate 89, dedup 64, promote 46 and synthesize 12. Eleven systems have no wired curation value. Most systems wire several operations: 120 wire between three and seven.

`synthesize` means creating a claim absent from the inputs. It is wired in only 12 systems: Agent-R, cass_memory_system, deja-vu, DocMason, eal-bench, Engraph, Kompl, LACP, Sparks, Swamp, VLM-wiki and Zikkaron. It is claimed or afforded only in 8 more. In cass_memory_system the wired synthesis is an inversion rule. A positive playbook rule whose decayed harmful count crosses a threshold becomes a new avoidance rule, and the original is deprecated. The record gives `Use cache` turning into `AVOID: cache. Marked harmful 3 times` ([EPI-RTE-curator-inversion](../../../agentic-system-analyses/retained/dicklesworthstone--cass_memory_system/epistemic.md#epi-rte-curator-inversion)). The record calls this "a policy rewrite", and the profile classifies it as policy synthesis, "not accepted causal knowledge". Synthesis in this population can therefore be mechanical and need not involve model inference.

## Trace learning: widely wired, uneven in depth

Trace learning means automatic, trace-fed writes that produce durable behavior-shaping artifacts or learned parameters. It is wired in 130 of 176 code-grounded systems. Another 20 reach `"yes"` only through claimed or afforded findings. The remaining 26 have no system-level value; 24 of those axes are `not-determinable`. No system has a system-wide `"no"`. Five systems (EchoWiki, ModularRSI, Phantom, REM and secure-llm-wiki) hold a wired local `"no"` unit, and the profile rules keep it out of the union.

Among the 130 wired systems:

- **Sources:** session logs feed learning in 85, tool traces in 82, event streams in 35 and trajectories in 24. 81 wire more than one source; 7 have no wired source finding.
- **Co-occurring values:** 122 also wire `learning` authority and 129 wire `trace-extracted` lineage.
- **Weights:** four update model weights: AgentFly, SAGE, Self-Training-LLM and SkillRL. The rest retain learning in artifacts, metadata or indexes.

The `"yes"` value spans very different depths:

- **REM** ([profile](../../../agentic-system-analyses/retained/satyammistari--rem/memory-profile.md), run `AAS-2026-10-14-rem-a81fdc774400-01`, manifest `0e45470aeb4b227b…`) reaches `"yes"` through two wired routes. Session turns are turned into parse metadata and vectors. Retrieval increments a `retrieval_count` that later adds a capped ranking bonus ([MEM-OBJ-retrieval-count](../../../agentic-system-analyses/retained/satyammistari--rem/memory.md#mem-obj-retrieval-count)). The README's "Write → Consolidate → Retrieve" loop stays claimed ([RT-CLM-memory-loop](../../../agentic-system-analyses/retained/satyammistari--rem/runtime.md#rt-clm-memory-loop)). The shipped Go router registers no endpoint that accepts the worker's semantic write-back ([RT-ABS-writeback-routes](../../../agentic-system-analyses/retained/satyammistari--rem/runtime.md#rt-abs-writeback-routes)). The profile keeps that as a bounded local `"no"` beside the system-level `"yes"`.
- **SkillRL** ([profile](../../../agentic-system-analyses/retained/aiming-lab--skillrl/memory-profile.md), run `AAS-2026-10-14-skillrl-0dba0e1c895e-01`, manifest `9771fa25ae76ce88…`) wires three routes. Failed validation trajectories feed admission of new skills into the training bank ([RT-RTE-validation-admission](../../../agentic-system-analyses/retained/aiming-lab--skillrl/runtime.md#rt-rte-validation-admission)). Offline experience is abstracted into rules. Reward-driven GRPO updates the actor's parameters ([RT-RTE-policy-update](../../../agentic-system-analyses/retained/aiming-lab--skillrl/runtime.md#rt-rte-policy-update)). In each case the record establishes wiring and states that "no evidence here establishes better later actions".
- **A-MEM** shows that automatic revision is not trace learning. A-MEM rewrites retained notes automatically, but its trace-learning axis is `not-determinable`. Its shipped paths do not update usage or history fields ([MEM-ABS-usage-feedback](../../../agentic-system-analyses/retained/wujiangxu--a-mem-sys/memory.md#mem-abs-usage-feedback)), and whether other writes are trace-fed is unresolved.

The 130 therefore counts access-count feedback, generated continuation summaries, rule extraction and weight updates alike. The profile vocabulary does not separate these depths. Splitting them would need a new axis or a reading of every set, which this comparison does not attempt.

## Doc-grounded tier (qualitative only)

Fifteen sets describe systems from papers, specifications or documentation: AgeMem, aide2, arsumbris, claude-code-dynamic-workflows, context-constitution, From Agent Memory to Portable Skills, incremental-self-improvement, interview-doc-agent, IsaacCLupus_mnemosyn_spec, llm-context-base, llm-project-wiki, Prove2Me_workspace, sig-releases, trajectory-informed-memory-generation and wikiskill. Their 531 findings are 495 claimed, 21 wired and 15 afforded. Ten of the fifteen claim trace learning, all at `claimed` basis.

AgeMem ([profile](../../../agentic-system-analyses/retained/2601-01885v1/memory-profile.md)) is the clearest case. It claims three routes: conversational extraction into long-term memory, summaries carried into later context, and GRPO updates of policy weights from scored trajectories. The profile records all three as claimed design, with "actual execution, causal benefit and production loading" unestablished. This tier shows which designs are described in documents; it gives no evidence that they are implemented.

## Withheld conclusions and evidence gaps

- **Prevalence and complete-set shares** are withheld for every axis, for the coverage reasons above. Statements such as "most systems are pull-only" or "X% lack human admission" are unsupported.
- **Deployment, activation and effect:** no finding reaches `observed` or `causally supported`. The population cannot say whether any memory mechanism improves task outcomes.
- **Absence of manual control or push read-back:** omitted findings are not negatives. Write-agency units are frequently `not-determinable` because generic callers do not reveal a human decision.
- **Depth of trace learning:** the `"yes"` value does not separate access counters from rule synthesis or weight updates. Splitting it needs a profile-revision decision, not a reading of this matrix.
- **Change over time:** there is one snapshot. No trend claim is made, and the legacy agent-memory-systems corpus is not merged in.
- **Quote verification:** 98 sets carry quotations that could not be checked against source bytes here. The findings rest on their accepted records and independent report verifications, not on a fresh check of the quotes.
- **Commonplace implications** are out of scope. They belong in a separately commissioned transfer scan.

## Query ledger

The query scripts and their output lived in a temporary working directory. Each query decodes `<axis>_units` as JSON. `strong` means basis ∈ {`wired`, `observed`, `causally supported`}. Denominator: the 176 code-grounded rows unless stated otherwise.

| Query | Test | Result |
|---|---|---|
| Q0 population | row count by `source_tier`, `comparison_version` | 191; 176 code, 15 doc; revision 2 only |
| Q1 axis coverage | count of `<axis>_assessment` | table above |
| Q2 existence | per system, any unit finding with value v and strong basis | table above |
| Q3 weak-only | value present only at `claimed`/`afforded` | table above |
| Q4 complete-set eligibility | axis `known` and every unit finding strong | eligibility table |
| Q5 basis census | count of every finding's basis, all 191 rows | 7,958 wired; 1,246 claimed; 648 afforded; 0 observed or causally supported |
| Q6 trace learning | strong `"yes"`; its strong `trace_source`, `learning` authority, `trace-extracted` lineage and `model-weights` co-occurrence | 130; 85/82/35/24; 122; 129; 4 |
| Q8 manual admission | `manual` at any basis vs strong; weak-only systems by basis | 88 vs 46; 42 weak-only (26 claimed, 19 afforded); 1,041 units with 240 not-determinable and 113 uninspected |
| Q9 push signal | strong `push` with strong inferred-* signal | 56 of 139 |
| Q10 curation | strong `synthesize`; systems with 3–7 strong operations | 12 systems named above; 120 |
| Q11 storage | strong files only; any strong database-type substrate; no strong files | 25; 95; 16 |
| Q13 doc tier | basis census over the 15 doc-grounded rows | 495 claimed, 21 wired, 15 afforded |
