---
description: Deriving architectural requirements by decomposing concrete user stories into step-by-step context needs — not from abstract read/write operations but from what the agent actually has to load at each stage
type: kb/types/note.md
traits: []
tags: []
---

# Scenario decomposition drives architecture

Architectural decisions for agent-operated KBs are often framed around abstract read and write operations, with hop count as the headline cost. But hop count is a proxy, not a requirement. The real question is what context the agent needs at each step of a real user story, and whether the architecture puts that context within reach at the moment it is needed.

This note argues for a different unit of analysis: start from concrete user stories, decompose them into steps, identify what the agent needs at each step, and derive architectural requirements from the aggregate pattern. The architecture falls out of the decomposition — not the other way round.

## User stories as the unit of analysis

The right unit isn't "read" or "write" — it's a complete user story with its full chain of agent actions.

**Write a note.** A user asks to capture an insight. The agent must: find related notes → read them → read the applicable type definition → read the writing conventions → write the note → connect it to existing knowledge.

**Ingest a source.** A user provides a URL. The agent must: fetch the URL → read the source type definition → write a structured extraction → find related notes → write a source review → update connections.

**Respond to a change.** An upstream change lands. The agent must: notice the change → analyse how it applies → assemble evidence from the KB → write a grounded response.

**Answer a question.** A user asks something the KB should know. The agent must: search → read matches → follow links → synthesise an answer.

Each story involves multiple operations with different context requirements at each step. The decomposition is more informative than any single-operation metric because it exposes *when* each context item must be present and *how often* each step repeats across stories.

## Decomposition, generically

For any user story, the decomposition produces a step table:

| Step | Context needed | Where it lives | How the agent knows |
|------|----------------|----------------|---------------------|
| Route to the right location | Routing table | Control-plane file | Always loaded |
| Find related notes | Search capability + good descriptions | Notes with frontmatter | Always-loaded search patterns |
| Read related notes | The notes themselves | Library collection | Search results |
| Know what structure to use | Type definition or template | Type directory | Routing or writing-guide reference |
| Know how to write well | Writing conventions | Always-loaded writing guide | Routing |
| Write the file | All of the above in context | — | — |
| Connect to existing knowledge | Connection skill + index awareness | Skill body + area indexes | Skill description (always loaded) |

The value of the table isn't in any single row. It's in the pattern across rows and across stories: steps that appear in every scenario are candidates for always-loaded context, steps that appear in only one scenario are candidates for on-demand loading, and steps whose required context depends on a judgment call are candidates for an escalation path to deeper methodology.

## Architectural principles that fall out

The decomposition reveals a layered structure that matches the [instruction specificity should match loading frequency](./instruction-specificity-should-match-loading-frequency.md) principle, with the escalation path as a first-class concern:

**Steps common to every scenario → always-loaded context.** Routing and search patterns appear in every story. They belong in the control-plane file that the agent loads on every invocation. This includes an escalation hint that tells the agent when and where to look for deeper reasoning.

**Steps specific to a scenario → on-demand loading.** Type definitions, writing conventions, and skill bodies are needed only when the agent is doing that particular kind of work. The loading hierarchy handles this.

**The "find related notes" step is shared across most scenarios** — it appears in write-a-note, ingest-a-source, and answer-a-question. It depends on good descriptions, claim titles, and search patterns. Since [agents navigate by deciding what to read next](./agents-navigate-by-deciding-what-to-read-next.md), the description-as-retrieval-filter convention directly improves this step.

**The "know what structure to use" step motivates colocating operational artifacts with the content.** The step happens mid-scenario, when the agent is already working in the content tree. Forcing a tree-switch at that point would break flow. Keeping operational artifacts alongside the content preserves the common path inside one tree.

**The escalation path motivates keeping methodology separate from content.** If methodology were mixed into the content tree, every search would return both user notes and framework notes. The agent would have to filter constantly. Keeping them separate means the common-case search scope is clean, and the escalation is explicit — the agent decides it needs deeper reasoning and goes looking for it.

**The escalation path must be discoverable.** An agent can only escalate if it knows that methodology exists and where to find it. This is the job of whatever the agent loads on every session — typically a control-plane file. The file is already always loaded, so adding "for why things work this way, search the methodology source" costs nothing extra. No other mechanism is needed; provenance links embedded in every skill would be redundant with what the control-plane file already provides, and harder to maintain.

**The "connect to existing knowledge" step is the least optimised.** It appears at the end of both write-a-note and ingest-a-source, but is usually modelled as a separate skill invocation rather than an integral part of the write flow. The decomposition makes the gap visible even when individual operations look efficient.

## Escalation discoverability is a statelessness problem

The hardest gap the decomposition exposes is escalation discoverability. In any system where operational instructions have been [worked out from deeper methodology](./theory-and-methodology-form-a-two-layer-execution-system.md), the agent has no signal that it's in a case the procedures don't cover. Since [agent statelessness makes routing architectural](./agent-statelessness-makes-routing-architectural-not-learned.md), there's no "something feels off" intuition — the agent follows the procedure and may produce a suboptimal result without ever realising that deeper reasoning would have helped.

The control-plane file can tell the agent the escalation path exists, but it cannot guarantee the agent recognises an edge case. This is a design problem, not a training problem, and it falls out of the decomposition because the decomposition makes the procedure–methodology boundary explicit for every step.

## What the method is good for

The scenario-decomposition approach is most useful when:

- A system has at least two user stories with overlapping but non-identical step sequences
- Some steps are shared across stories and some are scenario-specific
- There's a boundary between "what the agent uses at runtime" and "the reasoning behind those conventions" that can be crossed deliberately

It's less useful for a system with a single user story (the decomposition degenerates to a single chain), or when there's no methodology layer beneath the operational instructions (no escalation to reason about).

---

Relevant Notes:

- [scenario-architecture](../reference/scenario-architecture.md) — current-state: how Commonplace instantiates the scenario-derived architecture today, including the two-tree split, the specific AGENTS.md fragment, and the `tests/scenarios/` measurement surface
- [Instruction specificity should match loading frequency](./instruction-specificity-should-match-loading-frequency.md) — confirms: the loading hierarchy (always-loaded → on-demand → methodology fallback) maps directly onto the step frequency patterns in the decomposition
- [Always-loaded context mechanisms in agent harnesses](./always-loaded-context-mechanisms-in-agent-harnesses.md) — extends: different always-loaded surfaces have different affordances and map onto different scenario patterns
- [agents-navigate-by-deciding-what-to-read-next](./agents-navigate-by-deciding-what-to-read-next.md) — foundation: the "find related notes" step works well precisely because navigation hints (descriptions, titles) are optimised for agent read/skip decisions
- [skills derive from methodology](./skills-derive-from-methodology.md) — grounds: the escalation path is the coverage gap in action — when the procedure doesn't cover the case, the agent needs the source
- [agent statelessness makes routing architectural](./agent-statelessness-makes-routing-architectural-not-learned.md) — constrains: the agent has no intuition for when it's in a gap case, making escalation discoverability a design problem rather than a training problem
- [Task-fitted structure costs cross-task reuse](./task-fitted-structure-costs-cross-task-reuse.md) — contrasts: deriving structure from current scenarios is right, but hardening it on that basis spends cross-task reuse as the scenario set drifts
