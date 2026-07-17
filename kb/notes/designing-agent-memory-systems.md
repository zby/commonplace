---
description: "Derives agent-memory design pressures and links to a requirements inventory for agents designing or evaluating memory systems"
type: kb/types/note.md
traits: [synthesis, has-external-sources]
tags: [agent-memory, context-engineering, learning-theory]
---

# Designing a Memory System for LLM-Based Agents

An agent memory system should be designed from the effects memory must have, not from its storage layer or from the path that produced each memory. The success criterion is contextual competence: remembered material earns its place when it helps an agent answer, act, create artifacts, or update behavior under bounded context. [Agent memory needs discoverable, composable, trusted knowledge under bounded context](./agent-memory-needs-discoverable-composable-trusted-knowledge-under.md) states that criterion directly and makes discoverability, composability, and trust the minimum artifact-quality basis for remembered knowledge.

This note is a requirements map rather than a layer architecture. It is meant to be read by agents and maintainers designing or evaluating memory systems: first it derives the pressure categories a realistic system must satisfy, then it points to a concrete requirements inventory. The inventory is not a build sequence; it is a checklist of capabilities and failure modes to account for if memory is going to change downstream capacity rather than merely persist information.

Although the derivation starts from first principles, it was checked against the broad [Agent Memory Systems](../agent-memory-systems/README.md) review collection and revised where the reviewed systems exposed missing pressure: packaging, activation, authority, lifecycle, compiled-view drift, and effect-based evaluation. [The adaptation survey corroborates memory requirements but misses artifact governance](./agent-memory-requirements/adaptation-survey-corroborates-memory-requirements.md) adds an external taxonomy check: adaptation taxonomies are useful for asking where optimization happens, while this note asks what should drive the decision to govern a learned artifact as memory.

The detailed requirement notes live in [Agent Memory Requirements](./agent-memory-requirements/README.md). This synthesis explains why those requirements belong together.

## Start With Consumers

Contextual competence becomes operational only through the consumers whose capacity memory is supposed to change. Memory requirements come from the consumers memory must serve: acting agents, context schedulers, learning loops, reviewers, maintainers, governance processes, and work surfaces all depend on memory in different ways.

Each consumer fails differently. Agents repeat known mistakes, schedulers spend context on the wrong material, reviewers lose auditability, and work surfaces either disappear into traces or contaminate durable library memory. These are not separate feature requests yet; they are evidence that the requirements inventory must preserve consumer-specific pressure rather than flattening memory into generic recall.

That spread is why memory cannot collapse into one retrieval interface. Search may help an agent find a past artifact, but it does not by itself satisfy the reviewer who needs provenance, the scheduler that needs loading priority, or the maintainer who needs to reconstruct purpose.

## Treat Memory As Context Engineering

The consumer spread turns memory into a [context engineering](./definitions/context-engineering.md) (right-knowledge-into-bounded-context) problem because retention is cheaper than use. Text, traces, decisions, tests, schemas, and tool outputs can be kept far more cheaply than they can be inspected, trusted, shaped, and loaded into a bounded agent context.

The pressure is not storage scarcity. The pressure is deciding which retained material should influence a particular loop, in what form, with what authority, and under which lineage assumptions. Cheap storage creates candidates for memory use; contextual competence depends on selecting and shaping those candidates before the context window is spent.

As [Agent memory is a crosscutting concern, not a separable niche](./agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) argues, memory cuts across the runtime rather than sitting in one component. The execution substrate retains artifacts, the context engine selects and activates them, and the learning loop turns experience into readable or executable artifacts. The design question is therefore not where the memory box sits, but how retained material becomes usable capacity in the right loop.

## Use Retained-Artifact Fields

Once memory cuts across storage, retrieval, activation, and learning, the system needs vocabulary for what kind of artifact is being governed and how it is supposed to affect the consumer. [Axes of artifact analysis](./axes-of-artifact-analysis.md) supplies that vocabulary at the level of the retained artifact's operative part or consumption path. [Storage substrate](./definitions/storage-substrate.md) says where retained state persists. [Representational form](./definitions/representational-form.md) says how the operative part is encoded and consumed: prose, symbolic, distributed-parametric, or mixed. [Lineage](./definitions/lineage.md) says what source dependencies govern invalidation. [Behavioral authority](./definitions/behavioral-authority.md) says who consumes it, through which channel, and with what force.

Representational form and behavioral authority are separate fields. Prose and symbolic artifacts can both advise or instruct; a decision rationale is a [knowledge artifact](./definitions/knowledge-artifact.md) when the agent asks why a choice was made, and a [system-definition artifact](./definitions/system-definition-artifact.md) when it prevents the rejected alternative from being proposed again. The requirements inventory must preserve that separation because inspectability, execution, authority, and behavioral force do not move together.

A symbolic artifact has formal semantics consumed by a deterministic interpreter: schemas, tests, scripts, tools, validators, and typed data are symbolic in that sense. When a learned procedure becomes deterministic enough, it should move toward [codification](./definitions/codification.md) (committing procedure to a symbolic medium), because [bookkeeping work is more reliable on a symbolic substrate than when re-run through the LLM each time](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md). Codification is a form move, not automatically an authority move.

## Go Beyond Retrieval

With behavioral authority separated from form and substrate, retrieval is necessary, but it is not the whole memory problem. Search can expose past information, but it does not decide which remembered constraints, routines, and maintenance mechanisms should shape future work. Durable behavior-changing artifacts belong inside the memory problem because they are one way past experience changes future capacity.

[Raw accumulation does not create usable memory](./raw-accumulation-does-not-create-usable-memory.md) sharpens the same point from the ingress side: accumulated material only becomes usable memory when it has enough handles, scope, relationships, provenance, trust signals, and lifecycle pressure to be applied without replaying the original situation. [Knowledge storage does not imply contextual activation](./knowledge-storage-does-not-imply-contextual-activation.md): a stored lesson has not helped unless it appears in the right bounded context with enough priority and framing to change what happens next.

The error-correction asymmetry strengthens the symbolic-artifact requirement without making symbolic artifacts universally superior. High-authority behavior-changing memory at scale needs symbolic artifacts whose contracts, activation rules, lineage, lifecycle, authority, and evaluation are part of the memory system rather than left as informal convention. Deterministic substrates are better for repeatable bookkeeping, but moving a learned rule into that substrate also makes errors propagate more reliably.

## Set The Boundary

The preceding pressure categories need an operational boundary. At the broadest technical level, any persistent state that can affect future behavior is behavior-shaping substrate: model weights, prompts, tests, configs, tool descriptions, caches, and work surfaces all qualify. The memory system governs the narrower subset that preserves evidence, knowledge, preference, procedure, decision, or learned constraint for future use, and whose use needs memory operations.

This is an architectural choice, not a universal claim about what memory really is. System-definition artifacts can carry memory, but this design treats them as memory-system material only when they carry accumulated project knowledge and are governed as learned constraints. Otherwise, a regression test or `AGENTS.md` rule remains ordinary execution substrate or control-plane configuration.

## Requirements Inventory

The requirements inventory is organized by memory operation rather than by pressure category. Each operation usually answers more than one pressure:

- Consumer-specific failure modes: [create memory directly](./agent-memory-requirements/create-memory-directly.md), [import external knowledge](./agent-memory-requirements/import-external-knowledge.md), [serve multiple consumers](./agent-memory-requirements/serve-multiple-consumers.md), [activate behavior-changing memory](./agent-memory-requirements/activate-behavior-changing-memory.md), [make authority explicit](./agent-memory-requirements/make-authority-explicit.md), and [evaluate memory by effects](./agent-memory-requirements/evaluate-memory-by-effects.md).
- Context-engineering cost: [create memory directly](./agent-memory-requirements/create-memory-directly.md), [preserve evidence without loading history](./agent-memory-requirements/preserve-evidence-without-loading-history.md), [use trace extraction](./agent-memory-requirements/use-trace-extraction-as-meta-learning.md), [activate behavior-changing memory](./agent-memory-requirements/activate-behavior-changing-memory.md), and [retire, redact, supersede, and relax memory](./agent-memory-requirements/retire-redact-supersede-relax.md).
- Form and authority separation: [create memory directly](./agent-memory-requirements/create-memory-directly.md), [use trace extraction](./agent-memory-requirements/use-trace-extraction-as-meta-learning.md), [promote only when value exceeds cost](./agent-memory-requirements/promote-only-when-value-exceeds-cost.md), [keep compiled views aligned](./agent-memory-requirements/keep-compiled-views-aligned.md), and [evaluate memory by effects](./agent-memory-requirements/evaluate-memory-by-effects.md).
- Retrieval insufficiency: [preserve evidence without loading history](./agent-memory-requirements/preserve-evidence-without-loading-history.md), [serve multiple consumers](./agent-memory-requirements/serve-multiple-consumers.md), [activate behavior-changing memory](./agent-memory-requirements/activate-behavior-changing-memory.md), and [keep compiled views aligned](./agent-memory-requirements/keep-compiled-views-aligned.md).
- Symbolic-artifact governance: [use trace extraction](./agent-memory-requirements/use-trace-extraction-as-meta-learning.md), [activate behavior-changing memory](./agent-memory-requirements/activate-behavior-changing-memory.md), [promote only when value exceeds cost](./agent-memory-requirements/promote-only-when-value-exceeds-cost.md), [keep compiled views aligned](./agent-memory-requirements/keep-compiled-views-aligned.md), and [make authority explicit](./agent-memory-requirements/make-authority-explicit.md).
- Substrate versus memory-system boundary: [import external knowledge](./agent-memory-requirements/import-external-knowledge.md), [promote only when value exceeds cost](./agent-memory-requirements/promote-only-when-value-exceeds-cost.md), [keep compiled views aligned](./agent-memory-requirements/keep-compiled-views-aligned.md), [retire, redact, supersede, and relax memory](./agent-memory-requirements/retire-redact-supersede-relax.md), and [make authority explicit](./agent-memory-requirements/make-authority-explicit.md).

For the implementation mapping, [Agent memory coverage](../reference/agent-memory-coverage.md) tracks how Commonplace currently satisfies these needs and where gaps remain.

## Secondary Properties

The requirements above define whether a memory system improves contextual competence. Other properties can still make a memory system easier to adopt, cheaper to operate, and harder to strand outside the agent's real work:

- Native work-environment fit: memory should live where agents and humans already act when possible, so it can be inspected, patched, validated, diffed, reviewed, and committed through ordinary workflows.
- Cost-model flexibility: a memory system that rides on the host agent or IDE can use the host's existing economic model instead of requiring every memory operation to consume a separate metered API call.
- Portable degradation: if the specialized harness disappears, markdown, git, static sites, and ordinary scripts can still keep the memory inspectable.
- Inspectable generated surfaces: generated indexes, reports, and compiled views are easier to trust when they are rebuildable, diffable, and tied to visible source artifacts.

When a memory system must serve many agent clients, packaged surfaces can become architectural rather than cosmetic. [ByteRover](../agent-memory-systems/reviews/byterover-cli.md) ships CLI, daemon, MCP, hooks, rules, skills, connectors, and version-control surfaces around one substrate, while [Hindsight](../agent-memory-systems/reviews/hindsight.md) invests in many framework integrations.

## Partial Memory Subsystems

Several common designs solve real parts of memory, but leave other requirements to surrounding workflows:

- A vector database can provide retrieval, but artifact contracts, authority, activation, lifecycle, and behavioral evaluation must come from elsewhere.
- A transcript archive or summarizer can preserve and compress evidence, but usable future context still requires provenance, extraction, promotion, and selective loading.
- An always-loaded profile or self-editing prompt loop can change behavior, but ranking, source alignment, testing, rollback, and retirement need external governance.
- A wiki or rules engine can preserve or enforce knowledge, but runtime activation, artifact contracts, behavioral closure, rule selection, relaxation, and exception handling remain outside the substrate.
- A reusable memory package can give an initial prior, but local truth, local authority, and project-specific lifecycle have to be maintained by the consuming project.

These are real memory systems or memory subsystems. The distinction is that they externalize some of the maintenance burden, so a realistic architecture should name which requirements are handled internally and which are delegated to humans, scripts, review processes, host applications, or adjacent systems.

## Build Order Is Implementation-Specific

[Commonplace agent memory gap plan](../reference/commonplace-agent-memory-gap-plan.md) translates these requirements into a plan for closing Commonplace's current gaps: authority for automatic memory operations, candidate queues, lifecycle scheduling, compiled-view source alignment, session-trace capture, trace extraction, situation cues, behavioral evaluation, ranking, import/reingest maturity, and retrospective episodes where they answer real queries.

Each project will need its own version of that mapping. The requirements above are stable, but the order, depth, and integration of solutions depend on the host system, existing tooling, and the failure modes the project actually observes. The right sequencing comes from validated usefulness in the running system, not from working through this list top to bottom.

## What Remains Open

The hardest open problem is structural pattern detection across sessions. Many important lessons do not share keywords: stale pricing tables, outdated runbooks, and deprecated templates can all be instances of "derived artifacts drift from sources of truth." Recognizing that causal structure requires deeper analysis than ordinary search.

Discovery extraction also remains weak. Corrections and failures have visible signals; discoveries often have only surprise, elaboration, or later reuse. The realistic stance is to surface discovery candidates, not automatically graduate them.

The boundary between learned memory and work-surface authority is domain-dependent. Software projects have tests, linters, code review, issue trackers, and deployment gates. Other domains may lack those surfaces or have different authorities. The open question is which substitute surfaces can carry learned constraints when a domain lacks durable traces, recurring tasks, evaluable outcomes, or clear authority to modify behavior.

Finally, learned memory-management policy is attractive but oracle-dependent. Where the domain has clear success metrics, a learned policy may outperform inspectable heuristics. In open-ended knowledge work, reviewable rules, provenance, and behavioral tests remain the safer default. Memory management sits on the same [bitter-lesson boundary](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md): relax into learned policy where feedback is good, and keep artifact-side control where feedback is weak.

---

Relevant Notes:

- [Context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) - grounds the context-scarcity pressure behind selective loading and framing
- [Agent memory requirements](./agent-memory-requirements/README.md) - expands the derived requirements into one loadable note per need
- [The adaptation survey corroborates memory requirements but misses artifact governance](./agent-memory-requirements/adaptation-survey-corroborates-memory-requirements.md) - compares this requirements map with an external agentic-adaptation taxonomy
- [Trace-learning techniques in related systems](../agent-memory-systems/trace-learning-techniques-in-related-systems.md) - surveys systems that mine traces into preferences, tips, rules, skills, playbooks, and policy updates
