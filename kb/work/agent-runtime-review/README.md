# Workshop: Agent-runtime review

## What this is

Scoping work for expanding external-system reviews from **agent memory systems** to **agent runtimes** — the runtime layer that executes the agentic loop and governs context engineering at execution time (tool dispatch, context/compaction, permissions, skills, orchestration — *and* memory as one subsystem). Grounds in the same retained-artifact theory the memory reviews already use.

This README is the framing/scoping doc. It exists to settle a handful of decisions deliberately before any collection gets stood up. It is not a build plan yet.

## Naming decision (settled 2026-06-06)

The concept is **agent runtime**, not "harness". "Harness" carries the tack-and-bridle metaphor — you harness a horse or a workload you're trying to break — which frames the model as the dumb draft animal and the scaffolding as the thing doing the real work. That's backwards for what we'd be studying, and the metaphor leaks into how reviews read.

"Agent runtime" names the layer by its job: the runtime that *executes the agentic loop* and consumes retained artifacts while it runs. Neutral, field-standard, no metaphor. Prior workshops (`harness-fundamentals`, `harness-taxonomy-convergence`) use "harness" in their titles; treat that as legacy vocabulary, not a competing term. Renaming those is out of scope here.

Candidate collection name: `kb/agent-runtimes/`. Candidate vocabulary term: **Agent runtime**.

## Why this fits the KB (and fits *better* than memory did)

The memory reviews already run on substrate-agnostic vocabulary — `retained-artifact`, `operative-part`, `representational-form`, `behavioral-authority`, `storage-substrate`, `lineage` never assumed "memory". A runtime is full of exactly these: system prompts (prose / instruction), tool schemas (symbolic / routing), permission rules and hooks (codification / enforcement), skill and command definitions, compaction policies. The four-field record classifies all of them unchanged.

The deeper reason is the KB's own center of gravity. Our core concepts — **context engineering**, **frontloading**, **distillation**, **constraining** — are *precisely what a runtime does at execution time*. A runtime is context engineering made concrete. Memory was one slice of that; runtimes are the whole machine. They are the richest external corpus of context-engineering-in-practice we could study.

## What we already have (build on, don't duplicate)

The "active control loop" is **not** a gap in our theory — it is partially built and scattered across the workshop layer:

- `kb/work/harness-taxonomy-convergence/` — a component model for what a runtime is made of: **Scheduler / Context engine / Execution substrate**, plus a **governance/maintenance axis** running across them. Reconciles three independent component decompositions (Vtrivedy10, Raschka, Commonplace) and two operational/control vocabularies (Lopopolo, cybernetics).
- The promoted tool-loop note family — the scheduler model: `kb/notes/tool-loop-index.md`, `kb/notes/bounded-context-orchestration-model.md`, `kb/notes/the-practical-scheduler-is-the-host-language.md`, and siblings. This is the active-control vocabulary we already own.
- `kb/work/harness-fundamentals/harness-boundary.md` — where the runtime boundary sits.
- `kb/agent-memory-systems/` — 150+ code-grounded reviews whose memory subjects are frequently *runtime subsystems* already (Letta, mem0, cognee, crewai-memory are framework/runtime reviews wearing a memory hat).

So the central theory task is **integration, not invention**: connect the retained-artifact four-field record (which describes *retained state*) with the Scheduler/Context-engine/Execution-substrate component model and the scheduler/tool-loop notes (which describe *active control*). A runtime review needs both axes.

## Open decisions

### 1. Review grain
A "memory system" was a fairly bounded unit. An "agent runtime" ranges from a while-loop-plus-dispatcher to a full IDE agent, and each is a bundle of subsystems.

- **Option A — whole-runtime note**: one review per runtime, subsystems as sections.
- **Option B — subsystem-by-subsystem** against the component model, with memory as one named subsystem.
- *Leaning:* a runtime review is explicitly multi-subsystem (classified against Scheduler / Context engine / Execution substrate + governance), with each subsystem carrying the four-field record. Memory becomes a runtime subsystem rather than a sibling category.

### 2. Collection topology
The expansion is a *superset*, not a sibling — memory is a subsystem *of* a runtime, and the existing corpus already blurs the line.

- **Option A — new `kb/agent-runtimes/`** that treats the existing memory corpus as the memory-subsystem layer beneath it; cross-links both ways.
- **Option B — broaden `agent-memory-systems`** into `agent-systems` / `agent-runtimes` with memory as a facet.
- *Leaning:* Option A, but this is the highest-stakes open call (it touches 150+ existing reviews, `systems.csv`, the review type spec, and the `write-agent-memory-system-review` skill).

### 3. Comparison anchor
Memory reviews compare each system against "Our System" (Commonplace-as-KB). Runtimes need a different facet: **Commonplace-as-runtime** — skills, commands, validation gates, `COLLECTION.md` routing, the review system, hooks. Same project, different face. Worth naming explicitly in the type spec so reviewers anchor consistently.

### 4. Review type / skill reuse
Does an agent-runtime review reuse `agent-memory-system-review` (with extra subsystem/component fields), or get its own type and a sibling `write-agent-runtime-review` skill? Depends on decision 2. Don't fork the skill until topology is settled.

## What would close this workshop

A decision record (likely an ADR under `kb/reference/adr/`, plus a vocabulary entry for **Agent runtime**) that settles: the term, the collection topology, the review grain, the comparison anchor, and the type/skill plan — and a short note (or a promoted integration of the existing scheduler + taxonomy-convergence work) stating how the retained-artifact record and the runtime component model compose into a single review skeleton. Once those exist, this workshop promotes them and disappears.

## Links

- `kb/agent-memory-systems/COLLECTION.md` — the collection this expands from; review structure and four-field record
- `kb/work/harness-taxonomy-convergence/structure-governance-matrix.md` — candidate component skeleton — draws-on
- `kb/notes/tool-loop-index.md` — the scheduler/active-control vocabulary — draws-on
- `kb/notes/definitions/context-engineering.md` — why runtimes are the central corpus — grounds
- `kb/notes/definitions/retained-artifact.md` — the substrate-agnostic record that transfers — grounds
