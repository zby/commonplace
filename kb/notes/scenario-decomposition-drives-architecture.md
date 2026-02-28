---
description: Deriving architectural requirements by decomposing concrete user stories into step-by-step context needs — not from abstract read/write operations but from what the agent actually has to load at each stage, in both the commonplace repo and installed projects
type: note
traits: []
areas: [claw-design]
status: seedling
---

# Scenario decomposition drives architecture

The [installation architecture](./commonplace-installation-architecture.md) reasons about read and write as abstract operations and optimizes for hop count. [Scenarios](./scenarios.md) describes what the KB is used for. What's missing is the bridge: start from concrete user stories, decompose them into steps, identify what the agent needs at each step, and derive architectural requirements from that analysis.

The scenarios must work in two distinct contexts: this repo, where the methodology is the content; and installed projects, where user content and methodology are separate trees.

## Two operating contexts

**Commonplace repo.** This repo is itself a claw — it uses its own knowledge system to document the methodology for building claws. The `kb/` directory contains methodology notes, source reviews, type definitions, everything. There's no separate `commonplace/` directory because this IS commonplace. When the agent writes a note here, it's writing about KB design, and the related notes it finds are other methodology notes. One tree, no escalation needed.

**Installed project.** When a project adopts commonplace, the install script creates `kb/` (the user's content) and clones the commonplace repo to `commonplace/` (the framework). Operational artifacts — types, WRITING.md — are copied into `kb/` so the agent's normal workflow stays within one tree. Skills are rendered into `.claude/skills/`. In normal operation, the agent should not need to consult `commonplace/` at all — everything is [distilled](./skills-derive-from-methodology-through-distillation.md) into skills and the CLAUDE.md fragment. But distillation is not lossless. When the agent hits a case the distilled procedures don't cover, it must escalate to `commonplace/kb/notes/` for the full reasoning.

The same four user stories play out in both contexts. What differs is where context lives and whether escalation is possible.

## User stories as the unit of analysis

The right unit isn't "read" or "write" — it's a complete user story with its full chain of agent actions.

**Write a note.** User asks to capture an insight. Agent must: find related notes → read them → read type definition → read WRITING.md → write the note → connect it to existing knowledge.

**Ingest a source.** User provides a URL. Agent must: fetch the URL → read source type definition → write structured extraction → find related notes → write source review → update connections.

**Respond to a change.** From scenarios: notice an upstream change → analyze how it applies → assemble evidence from KB → write a grounded response.

**Answer a question.** User asks something the KB should know. Agent must: search → read matches → follow links → synthesize an answer.

Each story involves multiple operations with different context requirements at each step. The decomposition below uses "write a note" as the primary example because it's the most step-rich and makes the escalation path visible.

## Write a note — decomposed

### Common path (both contexts)

| Step | Context needed | Where it lives | How the agent knows |
|------|---------------|----------------|-------------------|
| Route to correct location | Routing table | CLAUDE.md | Always loaded |
| Find related notes | Search capability + good descriptions | KB notes with frontmatter | CLAUDE.md search patterns |
| Read related notes | The notes themselves | `kb/notes/` | Search results |
| Know the structure | Type definition | `kb/notes/types/` | CLAUDE.md routing or WRITING.md reference |
| Know how to write well | Writing conventions | `kb/WRITING.md` | CLAUDE.md routing |
| Write the file | All of the above in context | — | — |
| Connect to existing knowledge | /connect skill + index awareness | Skill body + area indexes | Skill description (always loaded) |

This is the same in both contexts. In commonplace, types and WRITING.md are the originals. In an installed project, they're copies. The agent doesn't know or care — the paths are the same.

### The escalation path (installed projects only)

The common path assumes the distilled instructions cover the case. When they don't, the agent needs the full methodology reasoning.

**Example:** At the "know how to write well" step, the agent reads WRITING.md and sees "title as claim." It's writing about a complex architectural component — is this a single-claim document or a multi-claim spec? WRITING.md says multi-claim specs get topical titles, but the boundary is a judgment call. The skill procedure doesn't cover this. The agent must escalate:

| Escalation step | Context needed | Where it lives |
|----------------|---------------|----------------|
| Recognize the gap | Awareness that methodology exists | CLAUDE.md fragment: "for why things work this way, search `commonplace/kb/`" |
| Search methodology | Full reasoning behind the convention | `commonplace/kb/notes/` |
| Read source reasoning | e.g. title-as-claim-enables-traversal-as-reasoning.md | `commonplace/kb/notes/` |
| Apply judgment | The reasoning, now loaded, informs the decision | Already in context |
| Return to common path | Continue with the write | Back in `kb/` |

The escalation adds 2-3 hops to a different tree. It's expensive but rare — most writes don't hit the edge cases that require full methodology reasoning.

**In commonplace, this escalation doesn't exist.** The methodology notes ARE the content the agent is searching in the "find related notes" step. When the agent writes a note about title-as-claim conventions, it naturally encounters the full reasoning because that reasoning lives in the same `kb/notes/` it's already reading. The one-tree design means there's no gap between operational instructions and their justification.

### Other scenarios — key differences

**Ingest a source** follows the same pattern but with an additional complication: the /ingest skill orchestrates most steps, so the escalation path is mediated by the skill. If the skill's extraction procedure doesn't cover an unusual source format, the agent would need to consult methodology — but the skill would need to signal that escalation is available. Current skills don't do this.

**Answer a question** rarely escalates because it's a read-only scenario — the agent searches, reads, follows links, synthesizes. No structural decisions. But in an installed project, the agent sometimes needs to answer questions about *how the KB works* (e.g., "what types of notes can I create?"). That's a methodology question, not a content question. The routing in CLAUDE.md must distinguish: "for your content, search `kb/`; for how the system works, search `commonplace/kb/`."

**Respond to a change** is the most complex scenario because it chains reading (assemble evidence) with writing (compose response). The escalation path could trigger during either phase — during evidence assembly if the agent needs to understand KB conventions to evaluate note quality, or during response composition if the note structure doesn't fit standard types.

## Architectural principles that fall out

The decomposition reveals a layered structure that matches the [context loading strategy](./context-loading-strategy.md), but now with the escalation path as a first-class concern:

**Steps common to every scenario → always-loaded context.** Routing and search patterns appear in every story. They belong in CLAUDE.md. This includes the escalation hint: the CLAUDE.md fragment must tell the agent that `commonplace/kb/` exists and when to consult it.

**Steps specific to a scenario → on-demand loading.** Type definitions, WRITING.md, and skill bodies are needed only when the agent is doing that particular kind of work. The loading hierarchy handles this.

**The "find related notes" step is shared across most scenarios** — it appears in write-a-note, ingest-a-source, and answer-a-question. It depends on good descriptions, claim titles, and search patterns. This is where the system is strongest: since [agents navigate by deciding what to read next](./agents-navigate-by-deciding-what-to-read-next.md), the description-as-retrieval-filter convention directly improves this step.

**The "know what structure to use" step motivates copying operational artifacts into `kb/`.** These steps happen in the middle of a scenario, when the agent is already working in `kb/`. Forcing a tree-switch at that point would break flow. The copy keeps the common path in one tree.

**The escalation path motivates keeping methodology in a separate tree.** If methodology were mixed into `kb/`, every search would return both user notes and framework notes. The agent would need to filter constantly. Keeping them separate means the common-case search scope is clean, and the escalation is explicit — the agent decides it needs deeper reasoning and goes looking for it.

**The escalation path must be discoverable.** The agent can only escalate if it knows methodology exists and where to find it. This is the job of the CLAUDE.md fragment that the install script generates for the user's project. The fragment already contains the routing table and search patterns — it must also contain the escalation instructions: "for why things work this way, search `commonplace/kb/`." The fragment is always loaded, so the agent always knows the escalation path exists. No other mechanism is needed — provenance links in skills would be redundant with what the CLAUDE.md fragment already provides, and harder to maintain.

**The "connect to existing knowledge" step is the least optimized.** It appears at the end of both write-a-note and ingest-a-source, but requires a separate skill invocation. This is a gap in both contexts.

## Where the system is strong

**Search and retrieval.** The combination of always-loaded search patterns, description-as-retrieval-filter, and claim titles means the "find related notes" step works well. This holds in both contexts — the conventions are the same whether the content is methodology (commonplace) or user notes (installed project).

**Common-path efficiency.** The decomposition confirms that the installation architecture's design — copy operational artifacts, keep methodology separate — produces a clean common path. Most writes stay in `kb/` with 3 hops. The agent doesn't need to understand the two-tree structure for routine work.

## Where gaps remain

**End-to-end orchestration.** Most scenarios are multi-step chains. The chain sometimes breaks at the transition from primary task to connection step.

**The post-write connection gap.** Connecting new documents to existing knowledge is the final step in write and ingest scenarios — and the one most often dropped. It's modeled as a separate skill invocation rather than an integral part of the write flow.

**Escalation discoverability.** In installed projects, the agent has no signal that it's in a case the distilled procedures don't cover. Since [agent statelessness makes skill layers architectural](./agent-statelessness-makes-skill-layers-architectural-not-pedagogical.md), there's no "something feels off" intuition — the agent follows the procedure and may produce a suboptimal result without ever realizing methodology would have helped. The CLAUDE.md fragment is the mechanism: it must tell the agent that `commonplace/kb/` exists and when to consult it. The fragment is always loaded, so the escalation path is always discoverable — but the agent still has to recognize it's in an edge case, which no amount of routing can guarantee.

**Scenario awareness in skills.** Current skills are operation-oriented (validate, connect, convert, ingest, snapshot-web) rather than scenario-oriented. The agent must compose them into workflows. Scenario-level orchestration could reduce this burden, but trades composability for convenience and adds a layer to the skill hierarchy.

## Measurable artifacts

The decomposition tables above are now implemented as structured [scenario files](../scenarios/write-a-note.md) in `kb/scenarios/`. Each scenario file references actual source files by path, stores hop counts per step, and distinguishes fixed costs (always the same) from variable costs (depend on KB content). The `/evaluate-scenarios` skill reads these files, measures instruction bytes from the referenced sources, and produces a cost table — turning the architectural claims in this note into verifiable measurements.

The key design: hops are stored in the scenario files (they're architectural, determined by the step structure), but instruction bytes are NOT stored — they're calculated dynamically by reading the actual source files. This means when we change the architecture (like inlining types into WRITING.md), we re-run the evaluation and get updated numbers without editing the scenario files.

## Open Questions

- Should connection be a step within the write/ingest workflow rather than a separate skill invocation? What's the mechanism — a skill that orchestrates the full scenario, or CLAUDE.md instructions that remind the agent to connect after writing?
- How specific should the CLAUDE.md fragment's escalation instructions be? A blanket "for deeper reasoning, search `commonplace/kb/`" may be too vague. Per-topic hints ("for link semantics reasoning, see `commonplace/kb/notes/link-contracts-framework.md`") are more precise but harder to maintain. The right granularity is probably somewhere between — enough to direct the agent toward the right area of the methodology, not so much that the fragment becomes a second routing table.
- ~~How do we evaluate whether end-to-end orchestration is improving? The [scenarios](./scenarios.md) describe what to evaluate against, but we don't yet have metrics for "did the agent complete the full chain?"~~ Partially addressed: the [scenario files](../scenarios/write-a-note.md) and `/evaluate-scenarios` skill provide cost metrics (hops, instruction bytes). Orchestration quality (did the agent complete the full chain correctly?) remains unmeasured.

---

Relevant Notes:
- [scenarios](./scenarios.md) — foundation: defines the concrete use cases this note decomposes into step-by-step context needs
- [commonplace-installation-architecture](./commonplace-installation-architecture.md) — extends: the abstract read/write analysis with scenario-grounded decomposition that confirms the two-tree design and derives the escalation path
- [context-loading-strategy](./context-loading-strategy.md) — confirms: the loading hierarchy (always-loaded → on-demand → methodology fallback) maps directly onto the step frequency patterns in the decomposition
- [agents-navigate-by-deciding-what-to-read-next](./agents-navigate-by-deciding-what-to-read-next.md) — foundation: the "find related notes" step works well precisely because navigation hints (descriptions, titles) are optimized for agent read/skip decisions
- [skills-derive-from-methodology-through-distillation](./skills-derive-from-methodology-through-distillation.md) — grounds: the escalation path is the distillation gap in action — when the distillate doesn't cover the case, the agent needs the source; the CLAUDE.md fragment makes this discoverable
- [agent-statelessness-makes-skill-layers-architectural](./agent-statelessness-makes-skill-layers-architectural-not-pedagogical.md) — constrains: the agent has no intuition for when it's in a gap case, making escalation discoverability a design problem rather than a training problem

Topics:
- [claw-design](./claw-design.md)
