---
description: "Anthropic reports offline correction and wiki-building experiments that bound when editable agent memory improves later work, with task-dependent gains and maintenance costs."
source: https://www.anthropic.com/research/components-of-agent-memory
captured: "2026-11-07"
capture: trafilatura
capture_scope: full-source
genre: practitioner-report
snapshot_sha256: b7488c193898cad521afe68e441533d4ad633f78664ab66568ddd53ae0610b60
ingested: "2026-11-07"
type: types/ingest-report.md
domains: [agent-memory, offline-memory-correction, knowledge-wikis, memory-evaluation]
learning_claims: true
---

# Ingest: The components of agent memory

## Classification

An experiment-bearing practitioner report describing Anthropic's memory designs and selected evaluations, rather than a scientific paper with a complete experimental protocol. Author: Anthropic, the developer of Claude and the Managed Agents infrastructure used in the reported work; this gives direct implementation experience but also a commercial interest in the results.

## Summary

Anthropic separates agent memory into transcripts, editable notes, navigational representations such as linked wikis, and a small injected context layer. “Dreaming” means offline computation that checks, reorganizes, or promotes this material. Reported CL-Bench database-task results compare persistent memory with stateless sessions and show model-dependent gains; rigid writing rules can hurt stronger models while explicit reading and testing instructions help a weaker one. A Pokémon case reports correction of an erroneous location note against its transcript, followed by successful navigation. In a 350,000-file internal corpus, a wiki built through repeated offline sessions complements rather than replaces search: wiki plus search reaches 61% of graded criteria versus 53% for search alone and 48% for wiki alone, with about 20,000 fewer answer-time tokens per question for the combined approach. These are comparisons within the tested file/wiki/search setup, not evidence that its layered decomposition is optimal. Other tasks show no clear wiki benefit or a wiki larger than its corpus. A legal-task revision improves reported criteria coverage from 72% to 100%, but jointly changes instructions, page ownership, and verbatim preservation, so it does not isolate any one cause.

## Quotes

> Right, “Memory + dreaming,” where an offline pass corrected the note: an arrow shows the agent heading back to the cave entrance.
> --- `kb/sources/.snapshots/components-of-agent-memory.md` @ `sha256:b7488c193898cad521afe68e441533d4ad633f78664ab66568ddd53ae0610b60` — Figure 7 alternative text

> We then tested whether dreaming could help Claude avoid this trap. We ran dreaming on the memory folder that contained the wrong location for the PokéCenter: Claude checked the note against the session transcript, caught its error, and rewrote it. The transcript gave Claude a ground truth to validate its memory against. With the corrected memory note, Claude went straight back into Mt. Moon and eventually reached Cerulean City.
> --- `kb/sources/.snapshots/components-of-agent-memory.md` @ `sha256:b7488c193898cad521afe68e441533d4ad633f78664ab66568ddd53ae0610b60` — Dreaming can correct memory

## Connections Found

The strongest role is bounded evidence for [retaining episode evidence as a route to re-examining a distilled rule](../theory/retaining-episode-evidence-keeps-a-distilled-rule-open-to.md). The Mt. Moon example connects an identified mistaken note, transcript-based criticism, a retained correction, and different subsequent navigation. It does not establish transcripts as infallible ground truth: recorded observations and mistaken agent narration must still be distinguished.

The wiki evaluations compare with [access burden versus transformation burden](../theory/access-burden-and-transformation-burden-are-distinct-query-dimensions.md): multi-document judgment and arithmetic benefit more than some single-document lookups. Within the supplied wiki/search arrangement, this supports task-sensitive evaluation of preprocessing, not a causal separation of easier retrieval from precomputed synthesis. The contract-table failure supplies a concrete case for [coordination guarantees rather than channels alone](../theory/agent-orchestration-needs-coordination-guarantees-not-just.md). Shared writes erased facts; the successful revision introduced single-writer contract pages and exact quotations together, leaving their separate effects unresolved.

## Learning Claims (our opinion)

The source's mechanism is cross-session adaptation through editable files, not weight updates. Task answers, grader corrections, transcripts, and source documents inform notes and wiki pages; later sessions consult the retained text. Offline passes can revise both domain content and instructions for building that content. The source excludes within-conversation learning and compaction from its own definition of memory; that is a scope choice, not a claim that those processes cannot improve action.

Against the [theory-builder definition](../theory/definitions/theory-builder.md), the evidence differs by condition:

- **Localized content:** directly illustrated by explicit location claims, database rules, contract pages, and wiki-building instructions. The Mt. Moon repair targets one mistaken claim, an example of [addressable theory](../theory/definitions/addressable-theory.md), without demonstrating precise fault localization for every note.
- **Consumption:** reported navigation changes after correction give a concrete content-sensitive example. Memory-enabled benchmark gains support usefulness of the compound system, but do not show that every stored rule was read or acted on; some models often failed to consult memory.
- **Content-directed criticism:** transcript checking challenges a stated location claim, and the contract-task loop diagnoses omissions and overwrites before changing instructions. Merely collecting guesses, as reported for Sonnet 4.6, is weaker evidence and does not establish this condition.
- **Iteration:** corrected notes guide subsequent play, database memories persist between fresh question sessions, and revised wiki instructions shape a rebuild. These demonstrate reported within-run and cross-session retention on the evaluated tasks, not durable transfer across unrelated problems.

These cases are consistent with theory building in the stronger reported configurations, not in every memory-enabled run. Improved capacity for future action remains a separate empirical judgment: the reported task gains support it locally, while the Pokémon model comparison does not isolate memory quality from other model differences. The instruction-revision loop is a partial example of revising the learning method itself, rather than only using retained domain content.

The effective update space includes notes, links, page organization, and some construction instructions. Models, tool affordances, available evidence, and grading criteria remain externally supplied. Following [the fixed-decomposition boundary](../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), improvement within that space does not validate the chosen hierarchy or demonstrate that it preserves every distinction future tasks need. The report strengthens the case for testing consumption and criticism separately; it does not require revising the definition to equate storage with learning.

## Extractable Value

1. **A concrete correction case for retained evidence.** The Mt. Moon episode adds a reported example to the existing re-examination note: a transcript can support targeted criticism of a stored claim and a changed next action. Its reach is the repair mechanism, not a general reliability estimate. [quick-win]
2. **A task-sensitive test of wiki value.** In the tested large-corpus wiki/search setup, combined access beats either source alone; simpler lookup tasks can show no clear benefit. A Commonplace evaluation could stratify questions by cross-document synthesis needs and count offline construction cost separately from answer-time token savings. This tests whether a maintained representation earns its cost, not whether wikis are universally preferable. [experiment]
3. **A bundled ownership-and-fidelity repair worth separating experimentally.** Per-contract single-writer pages with verbatim terms replace a lossy shared table, improving reported coverage from 41/57 to all 57 criteria. The reusable warning is that concurrent loss and abstraction loss can coexist; attribution requires varying them separately. [experiment]

## Limitations (our opinion)

The report presents selected vendor experiments without a complete reproducible protocol, run distributions, uncertainty estimates, or an independent replication. The Pokémon salience comparison explicitly uses one run per compared model, and models differ in more than memory behavior. The timing rule learned during play is a local conjecture, not a validated general game mechanic. The navigation correction is informative as a case but cannot estimate autonomous correction reliability.

The internal-corpus evaluation uses 25 questions and substantial offline work, reaching 128 sessions; its figure labels generation budgets up to 128M tokens. Answer-time savings therefore do not establish net savings or a break-even reuse rate. Wiki growth can improve coverage while increasing maintenance and error exposure. The 87% versus 73% merger result concerns the subset requiring cross-document work, judgment, or arithmetic, not all knowledge work.

The legal-task intervention changes ownership, quotation fidelity, and construction guidance together. Likewise, the weaker-model prompt combines reading memory with testing theories. Neither result identifies the individual causal contribution of its components. The biological analogy motivates the schedule but does not establish the architecture. All reported gains remain bounded by the tested models, evidence, tools, and tasks; the report leaves maintenance cadence and reliable freshness unresolved.

## Recommended Next Action

Update [Retaining episode evidence keeps a distilled rule open to re-examination](../theory/retaining-episode-evidence-keeps-a-distilled-rule-open-to.md) with the Mt. Moon correction as a bounded vendor-reported case, explicitly separating transcript observations from agent interpretations.
