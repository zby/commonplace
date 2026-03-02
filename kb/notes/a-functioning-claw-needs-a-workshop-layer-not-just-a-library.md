---
description: The current type system models permanent knowledge (library) but not in-flight work with state machines, dependencies, and expiration (workshop) — tasks are a prototype of the missing layer, and a functioning claw needs both plus bridges between them
type: note
areas: [claw-design]
status: seedling
---

# A functioning claw needs a workshop layer, not just a library

The claw's [current type system](./document-classification.md) — text, note, structured-claim, spec, adr — is a maturity ladder for knowledge. Documents move toward permanence: a text gets promoted to a note, a note crystallises into a structured claim, insights accumulate into specs and ADRs. The [wikiwiki principle](./wikiwiki-principle-lowest-friction-capture-then-progressive-refinement.md) animates this ladder: capture with zero friction, then refine in place. The status field (seedling, current, speculative) modulates commitment but not lifecycle. A seedling and a current note are structurally identical — one just hasn't been endorsed yet.

This works well for **durable knowledge**. But a functioning claw also needs to support **work in motion** — documents that have lifecycles, change state, interact with each other, and eventually produce outcomes — durable artifacts in the KB, actions on the outside world (drafted emails, responses to messages, code changes), or simply get discarded. The task system (`tasks/`) is the clearest example: it has state machines (backlog → active → completed), directional dependencies (blocks/blocked-by), and expiration (completed tasks become irrelevant). None of this maps onto the existing type system.

## The library/workshop distinction

**Library documents** accumulate value over time. A note becomes more useful as it gets connected, refined, and referenced. Deletion is a signal something went wrong.

**Workshop documents** consume value over time. A task becomes less useful as it progresses — its value is transferred into code, decisions, or actions on the world. Completion and archival are success states.

| Property | Library | Workshop |
|----------|---------|----------|
| Value trajectory | Accumulates | Consumed |
| State | Status (commitment level) | State machine with valid transitions |
| Relationships | Bidirectional (related, extends, contradicts) | Directional (blocks, depends-on, produces) |
| Time sensitivity | Ages slowly, staleness is a bug | Urgency and staleness are features |
| Success state | Referenced and connected | Completed or discarded |
| End state | Remains in KB | Archived or deleted |

## Temporal document types beyond tasks

Tasks aren't the only workshop documents. A claw that supports real workflows would likely need:

- **Decision threads** — the process that produces an ADR. Currently invisible: an ADR appears fully formed, but the discussion, alternatives weighed, and context gathered along the way are lost. Lifecycle: proposed → discussing → decided → (produces ADR).
- **Experiments/probes** — hypothesis-driven work. "Does X actually improve Y?" Has a result that changes what happens next. Lifecycle: hypothesis → running → concluded → (produces note or nothing).
- **Queues/inboxes** — items waiting for processing. Sources awaiting ingestion already work this way informally (files sit in `sources/` until someone runs `/ingest`). Lifecycle: unprocessed → triaged → handled.
- **Reviews (periodic)** — the recurring tasks already model this. Due → in-progress → reported, with recurrence.
- **Session logs** — what happened in a work session, what was learned, what's left unfinished. Currently not captured at all.

## Bridges between the layers

The relationship between library and workshop is **bidirectional**:

- **Workshop → library:** Workshop processes produce durable artifacts. An ADR is what's left after a decision thread concludes. A note might be what's extracted when a task completes. A source review is what a queue item becomes after processing.
- **Library → workshop:** Workshop documents draw on permanent knowledge. A task's instructions might include standard prompts from the library. A decision thread references existing notes as evidence. An experiment's hypothesis builds on established claims. Temporal LLM instructions can compose permanent prompt fragments stored as library documents.

This means there are two kinds of bridges needed:

**Extraction bridges** (workshop → library) — moving durable insights out of temporal documents. At the deterministic end, this is [spec mining](../notes/spec-mining-as-crystallisation.md): extracting rules and verifiers from observed workshop behavior. But extraction is broader — it also produces non-deterministic library artifacts like notes, ADR drafts, and judgment precedents.
- A `/crystallize` operation that extracts learnings from a completed task into a note
- Decision threads that automatically produce ADR drafts when they reach the "decided" state
- Experiment conclusions that prompt for note creation
- Session logs that flag insights for promotion

**Composition bridges** (library → workshop) — making permanent knowledge available to temporal processes:
- Task templates that pull in relevant library content (standard prompts, established constraints)
- Decision threads that automatically surface related notes and prior decisions
- Experiments that reference the claims they're testing

## Current state of the gap

The task system is the only workshop-like subsystem, and it lives entirely outside the KB:

- No document type in the classification hierarchy
- No frontmatter schema (uses ad-hoc templates)
- No `/validate` coverage
- No `/connect` awareness
- No backlink tracking between tasks and notes
- Indexed by qmd for search, but that's the only integration

This is fine for now — the claw is primarily a knowledge system and the task system works adequately with its own conventions. But this note exists to mark the gap: when we want to build a claw that supports real workflows (not just knowledge management), the workshop layer is where most of the new design work will be needed.

## Open questions

- Should workshop and library share a type system, or remain parallel hierarchies? The intuition is that we'll have **one big knowledge base and many smaller temporal subsystems**. Each temporal subsystem (tasks, decision threads, experiments, queues) has its own state machine, its own relationships, its own lifecycle — trying to unify them under one type hierarchy would be forced. What they share is that they all **depend on the library** (reference notes, include prompts, use established claims to make decisions), so they need to link into the KB. But their internal structure is diverse enough that local conventions per subsystem — what [why directories despite their costs](./why-directories-despite-their-costs.md) already argues for tasks — is likely the right default as more temporal types appear.
- How much formalism do workshop documents need? Tasks work with ad-hoc markdown templates. Would validated state machines help agents, or just add ceremony?
- Is the three-space model ([knowledge / self / operational](./three-space-agent-memory-maps-to-tulving-taxonomy.md)) the right framing? Workshop documents map roughly to the "operational space" — high churn, consolidation, graduation to knowledge. But the Tulving mapping may be decorative rather than load-bearing.
- What's the minimum viable bridge? Probably `/crystallize` on task completion — extract learnings into a note, link back to the archived task for provenance.
- [Claw learning is broader than retrieval](./claw-learning-is-broader-than-retrieval.md) argues the KB needs action-oriented knowledge types (preferences, procedures, precedents, voice). Workshop documents are precisely the kind of action-oriented artifacts that produce those knowledge types — should the workshop layer be designed with action-capacity as the success metric rather than retrieval?
- Skills already have implicit [type signatures](../notes/instructions-are-typed-callables.md) (`/ingest: source → source-review`). Could extraction bridges be formalised as skills with workshop-input, library-output signatures?

---

Relevant Notes:
- [three-space agent memory maps to Tulving's taxonomy](./three-space-agent-memory-maps-to-tulving-taxonomy.md) — the operational space maps to the workshop layer; different metabolic rates for different memory types
- [why directories despite their costs](./why-directories-despite-their-costs.md) — acknowledges tasks as a parallel subsystem; the question is whether more temporal types invalidate the "small subsystem" justification
- [document classification](./document-classification.md) — the library-oriented type hierarchy this note identifies as insufficient for workshop documents
- [automating KB learning is an open problem](./automating-kb-learning-is-an-open-problem.md) — the extraction bridge (workshop → library) is a specific instance of the broader automation challenge
- [the wikiwiki principle](./wikiwiki-principle-lowest-friction-capture-then-progressive-refinement.md) — the refinement-in-place ladder (text → note → structured-claim) is specifically a library pattern; workshop documents don't refine toward permanence, they consume themselves
- [claw learning is broader than retrieval](./claw-learning-is-broader-than-retrieval.md) — the action-oriented knowledge types this note identifies (preferences, procedures, precedents) are what workshop processes produce and consume; the workshop layer is where action-capacity learning happens
- [spec mining is crystallisation's operational mechanism](../notes/spec-mining-as-crystallisation.md) — extraction bridges are spec mining applied to workshop artifacts: observe repeated behavior in work processes, extract deterministic library knowledge
- [instructions are typed callables](../notes/instructions-are-typed-callables.md) — skill type signatures (source → source-review) already model extraction bridges; workshop → library bridges could be formalised as skills with temporal-input, permanent-output signatures
- [stabilisation is learning](../notes/agentic-systems-learn-through-three-distinct-mechanisms.md) — extraction bridges are stabilisation: collapsing workshop process outcomes into permanent library artifacts, moving knowledge from high-churn to steady-growth
- [active-campaign understanding needs a single coherent narrative](./active-campaign-understanding-needs-a-single-coherent-narrative-not-composed-notes.md) — theorist's THEORY.MD exemplifies the workshop layer; a concrete instance of a workshop artifact with holistic-rewrite lifecycle

Topics:
- [claw-design](./claw-design.md)
