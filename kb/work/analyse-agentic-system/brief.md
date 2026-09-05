# Brief: analyse an external agentic system

## Governing question

What executable public instruction should an agent follow to analyse an external agentic system once, at one pinned evidence boundary, while applying whole-runtime, memory/context, and epistemic lenses only where each is applicable?

## Audience and reader update

The immediate reader is an agent or maintainer conducting a code- or document-grounded external-system analysis. After following the instruction, the reviewer should be able to:

- state the system boundary, evidence tier, revision, and material uncertainty;
- explain how control progresses, context is assembled, and external state or actions are handled;
- identify whether a memory/context lens applies and, if so, analyse retention, transformation, read-back, activation, and behavioral authority;
- identify whether an epistemic lens applies and, if so, trace truth-apt candidates, transformations, warrant, acceptance, integration, and authority routes;
- distinguish absent, inapplicable, uninspected, claimed, implemented, observed, and causally supported mechanisms; and
- produce one bounded system-level synthesis without erasing lens-specific limits.

## Target

- Path: `kb/instructions/analyse-agentic-system/SKILL.md`
- Mode: new write
- Collection: `kb/instructions/`
- Type: `kb/types/instruction.md`
- Provisional title: “Analyse an Agentic System”

The target is a provisional public entry point. Workshop lens files are experimental subprocedures, not separately authorized promotion targets.

## User direction and retained intent

- Source: current conversation, 2026-08-20.
- Subject: revise the agent-memory review system by placing memory inside the agentic-systems collection and separating epistemic analysis as another conditional lens.
- Required architecture: one agentic-system analysis instruction should run memory analysis when the system has memory and epistemic analysis when it has knowledge-generation mechanisms.
- Correction with authority over prior framing: the separate memory collection exists because memory was reviewed first; it is not evidence that memory is conceptually outside agentic-system analysis.
- Immediate request: create a workshop and place in it instructions already understood or already functioning.
- Role: authoritative for purpose, scope, and collection relationship; it does not warrant claims about any external reviewed system.

## Intended practical purpose

Produce one system-first analysis workflow. It should inspect sources once, maintain one evidence register and revision boundary, route into conditional analytical lenses, and synthesize results around the system rather than around the historical order in which Commonplace developed its review methods.

## Operativity

- Intended consumer: an agent or maintainer explicitly asked to analyse, review, or refresh an external agentic system.
- Likely channel: a local user-invocable skill, discoverable by its trigger-focused description.
- Force: prescriptive source-analysis and artifact-writing workflow.
- Internal lenses may be invoked within fresh worker contexts, but the public workflow owns source preparation, applicability, artifact identity, cross-lens reconciliation, QA, validation, and reporting.
- Current workshop files have no automatic runtime consumer; they are trial inputs until promotion.

## Fixed analytical architecture

1. Establish the reviewed system, declared boundary, revision, source tier, and evidence register once.
2. Analyse the system's ordinary runtime responsibilities and control surfaces.
3. Record an explicit applicability disposition for each optional lens, including evidence and conclusions prevented by non-application or uncertainty.
4. Apply the memory/context lens when retained material accumulated or changed through use can affect a later invocation or action.
5. Apply the epistemic lens when material routes handle truth-apt content or the system makes a knowledge-production or warrant claim. The trigger must not depend on already concluding that the system successfully generates knowledge.
6. Reconcile shared objects and routes by stable IDs; do not duplicate source reading or silently upgrade evidence between lenses.
7. Write a bounded whole-system synthesis, preserving route-specific authority and uncertainty.

## Scope

Include:

- agent runtimes, harnesses, orchestration frameworks, agent operating layers, and narrower systems whose deployed behavior depends on model calls plus surrounding machinery;
- code-grounded and doc-grounded evidence, clearly separated;
- scheduler, context assembly, external state/action services, coordination, permissions, recovery, observability, governance surfaces, and retained behavior-shaping artifacts;
- memory as storage, write/maintenance, retrieval/read-back, activation, learning-from-use, and action-capacity support;
- epistemic production, checking, acceptance, integration, and direct policy adaptation through the accepted epistemic instruction's material-route boundary;
- explicit early exits for inapplicable lenses.

Exclude for this target:

- product rankings or generic adoption advice;
- a universal taxonomy of all agentic systems;
- automatic corpus relocation or semantic retrofit;
- changing `kb/agentic-systems/COLLECTION.md`, the current memory collection, schemas, parsers, or matrices before the target output shape is tested;
- promoting workshop lens files as independent public instructions without a separate disposition and authorization.

## Required distinctions

- Whole system vs analytical lens: memory and epistemic architecture are crosscutting views of one deployed system, not peer system categories.
- Retained state vs memory read-back: static shipped documentation or configuration is retained state, but memory read-back is accumulated-from-use material returning to later action.
- Storage vs context assembly vs activation: persistence does not imply selection into context, and context presence does not imply behavioral use.
- Content curation vs epistemic production: consolidation, deduplication, indexing, and fluent synthesis do not automatically establish warranted knowledge.
- Capability vs deployed behavior; doctrine vs implementation; reported operation vs observed run; observed contrast vs causal support.
- Epistemic authority, operational authority, and behavioral-authority path.
- Source preparation and review lifecycle vs the analytical claims written into the result.

## Evidence and source inputs

### Current operative procedures

- `kb/instructions/write-agent-memory-system-review/SKILL.md`
- `kb/agent-memory-systems/types/agent-memory-system-review.md`
- `kb/agent-memory-systems/types/agent-memory-system-review.schema.yaml`
- `kb/instructions/analyse-external-system-epistemic-architecture.md`
- `kb/reports/retained/epistemic-architecture-analysis-trials-20260820/acceptance.md`
- `kb/reports/retained/epistemic-architecture-analysis-trials-20260820/arc-trial.md`
- `kb/reports/retained/epistemic-architecture-analysis-trials-20260820/gbrain-trial.md`
- `kb/work/pi-agent-zerostack-comparison/review-instruction.md`

### Collection and framework state

- `kb/agentic-systems/COLLECTION.md`
- `kb/agentic-systems/README.md`
- `kb/agentic-systems/reviews/agno-agentos.md`
- `kb/agentic-systems/reviews/claude-code-dynamic-workflows.md`
- `kb/agentic-systems/reviews/exo.md`
- `kb/agentic-systems/reviews/gbrain.md`
- `kb/agent-memory-systems/COLLECTION.md`
- `kb/agent-memory-systems/review-framework-design.md`
- `kb/instructions/COLLECTION.md`
- `kb/types/instruction.md`

### Established analytical premises

- `kb/notes/agent-runtime-analysis-should-separate-scheduling-context-state.md`
- `kb/notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md`
- `kb/notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md`
- `kb/notes/runtime-structure-determines-governance-control-surfaces.md`
- `kb/notes/definitions/behavioral-authority.md`
- `kb/notes/knowledge-storage-does-not-imply-contextual-activation.md`

## Workshop baselines requested by the user

Preserve byte-for-byte copies of the three current procedures/contracts that are already operative, plus the bounded whole-system precedent. Create two narrower modular baselines only where the existing material already fixes the distinctions:

- runtime baseline: responsibilities and control surfaces, without claiming a complete universal taxonomy;
- memory/context baseline: the existing storage/write/read-back analysis, separated from publication, Commonplace comparison, curiosity, and collection routing.

Do not draft the cross-lens orchestrator by merely concatenating these files. Reconstruction must first identify duplicated fields, conflicting boundaries, and which layer owns each decision.

## Collection and type constraints

- Follow `kb/instructions/COLLECTION.md`: executable, frontloaded, explicit decisions and scope, minimal rationale.
- Follow `kb/types/instruction.md`: imperative title, trigger-focused description, and a named consumer/channel/force.
- A promoted target must not depend on `kb/work/`.
- Workshop copies may retain their original frontmatter because they are provenance snapshots, not library artifacts.

## Known uncertainties and acceptance criteria

- One-file vs per-system-package publication is open. The analysis workflow must be testable before this is fixed.
- Separate vs embedded lens instructions is open. The public entry point must remain singular either way.
- The instruction must not infer epistemic-lens inapplicability merely because no successful knowledge production is found; claimed or candidate truth-apt routes are enough to trigger inspection.
- It must avoid rerunning source preparation or letting lens workers analyse different revisions.
- It must preserve explicit inapplicability and uncertainty rather than make absent lens files carry hidden meaning.
- ~~It passes only after cold trials cover at least: runtime only; runtime plus memory with no material epistemic transformation; runtime plus epistemic routes; and runtime plus both memory and epistemic routes.~~ **SUPERSEDED 2026-08-21** by the authorized architecture amendment (user decision; see `README.md` "Design boundary" and `trial-evaluation.md`). Both lenses are now mandatory with depth proportionate to the evidence, so there are no lens combinations to cover: five cold trials returned both lenses applicable, the fifth targeting a deliberately trigger-poor subject, and the gate they were meant to exercise no longer exists. The criterion is retained here as history, not as a live requirement. The surviving depth criterion — that a brief lens pass still names what was inventoried, what was found, and what its thinness prevents — was validated by the sequentialthinking re-run.

Criteria above that presuppose the applicability gate (explicit dispositions, early exits for inapplicable lenses, preserved inapplicability) are read under the same amendment: the property they protected — never letting an absent lens section mean "there is nothing there" — is now carried by the mandatory scoping records and the brief-output floor rather than by an exit branch.
