---
description: Commonplace's current scenario-derived architecture — the two-tree split between this repo and installed projects, the escalation path to `commonplace/kb/`, the CLAUDE.md fragment contract, and the test/scenarios measurement surface
type: note
tags: [architecture]
status: current
---

# Scenario architecture

How commonplace currently instantiates scenario-derived architecture. This is a current-state description of the two-tree split between the commonplace repo and installed projects, the escalation path, the CLAUDE.md fragment that makes it discoverable, and the measurement surface under `test/scenarios/`. For the general method of deriving architecture from scenario decomposition, see [scenario decomposition drives architecture](../notes/scenario-decomposition-drives-architecture.md).

## Two operating contexts

**Commonplace repo.** This repo is itself a knowledge base — it uses its own knowledge system to document the methodology for building knowledge bases. The `kb/` directory contains methodology notes, source reviews, type definitions, and reference documentation. There's no separate `commonplace/` directory because this *is* commonplace. When an agent writes a note here, it writes about KB design, and the related notes it finds are other methodology notes. One tree, no escalation needed.

**Installed project.** When a project adopts commonplace, `commonplace-init` creates `kb/` (the practitioner's content) and a clone or submodule of the commonplace repo sits at `commonplace/` (the framework source). Operational artifacts — types, `WRITING.md`, skills — are copied into the project so the agent's normal workflow stays within one tree. Skills are promoted into `.claude/skills/` and `.agents/skills/`. In normal operation, the agent should not need to consult `commonplace/` at all — everything it needs is [distilled](../notes/skills-derive-from-methodology-through-distillation.md) into skills and the `AGENTS.md` fragment. When the agent hits a case the distilled procedures don't cover, it escalates to `commonplace/kb/notes/` for the full reasoning.

The same user stories play out in both contexts. What differs is where context lives and whether escalation is possible.

## Write a note — decomposed against the current layout

### Common path (both contexts)

| Step | Context needed | Where it lives today | How the agent knows |
|------|---------------|----------------------|---------------------|
| Route to correct location | Routing table | `AGENTS.md` `## Using the KB` | Always loaded |
| Find related notes | Search capability + good descriptions | Notes with frontmatter in `kb/notes/` | `AGENTS.md` search patterns, qmd index |
| Read related notes | The notes themselves | `kb/notes/` | Search results |
| Know the structure | Type definition | `kb/types/note.md` (inlined into WRITING.md) or `kb/*/types/` | `AGENTS.md` routing or WRITING.md reference |
| Know how to write well | Writing conventions | `kb/instructions/WRITING.md` | `AGENTS.md` routing |
| Write the file | All of the above in context | — | — |
| Connect to existing knowledge | `commonplace-connect` skill + indexes | Skill body + `kb/notes/tags-index.md` and subordinates | Skill description (always loaded) |

In commonplace, types and WRITING.md are the originals. In an installed project, they're copies produced by `commonplace-init`. The agent doesn't know or care — the paths are the same.

### The escalation path (installed projects only)

At the "know how to write well" step, the agent may hit a judgment call the distilled procedures don't cover — for example, recognising whether a document should use a claim title or a topical one. In that case it escalates:

| Escalation step | Context needed | Where it lives |
|----------------|---------------|----------------|
| Recognize the gap | Awareness that methodology exists | `AGENTS.md` fragment: "for why things work this way, search `commonplace/kb/`" |
| Search methodology | Full reasoning behind the convention | `commonplace/kb/notes/` |
| Read source reasoning | e.g. `title-as-claim-enables-traversal-as-reasoning.md` | `commonplace/kb/notes/` |
| Apply judgment | The reasoning, now loaded, informs the decision | Already in context |
| Return to common path | Continue with the write | Back in `kb/` |

The escalation adds 2–3 hops to a different tree. It's expensive but rare — most writes don't hit the edge cases that require full methodology reasoning.

**In commonplace, this escalation doesn't exist.** The methodology notes *are* the content the agent is searching in the "find related notes" step. When the agent writes a note about title-as-claim conventions, it naturally encounters the full reasoning because that reasoning lives in the same `kb/notes/` it's already reading. The one-tree design means there's no gap between operational instructions and their justification.

## The AGENTS.md fragment contract

In installed projects, the `AGENTS.md` fragment that `commonplace-init` scaffolds is the single piece of always-loaded context that makes both the common path and the escalation path discoverable. It contains:

- The routing table (`## Using the KB`) — tells the agent where things go
- Search patterns (`rg` examples) — tells the agent how to find things
- An escalation hint — tells the agent that `commonplace/kb/` exists and when to consult it
- The `## KB Goals` section (filled in by the practitioner) — tells the agent what belongs here

The fragment is always loaded, so the agent always knows the escalation path exists. No other mechanism is needed — provenance links in skills would be redundant with what the fragment already provides, and harder to maintain.

## Measurable artifacts

The decomposition above is implemented as structured scenario files under `test/scenarios/` (for example `test/scenarios/write-a-note.md`). Each scenario file references actual source files by path, stores hop counts per step, and distinguishes fixed costs (always the same) from variable costs (depend on KB content). The `/evaluate-scenarios` skill reads these files, measures instruction bytes from the referenced sources, and produces a cost table — turning the architectural claims into verifiable measurements.

The key design: hops are stored in the scenario files (they're architectural, determined by the step structure), but instruction bytes are NOT stored — they're calculated dynamically by reading the actual source files. When the architecture changes (for example, inlining a type into WRITING.md), the evaluation re-runs against the current files without editing the scenario files.

## Current gaps

**End-to-end orchestration.** Most scenarios are multi-step chains. The chain sometimes breaks at the transition from primary task to connection step.

**The post-write connection gap.** Connecting new documents to existing knowledge is the final step in write and ingest scenarios — and the one most often dropped. It's modelled as a separate skill invocation (`commonplace-connect`) rather than an integral part of the write flow.

**Escalation discoverability in installed projects.** The fragment tells the agent *that* `commonplace/kb/` exists, but the agent still has to recognise it's in an edge case. No amount of routing can guarantee that recognition — this is a soft failure mode.

**Scenario awareness in skills.** The current skill set (`write`, `validate`, `connect`, `convert`, `ingest`, `snapshot-web`, `revise-iterative`) is operation-oriented rather than scenario-oriented. The agent composes them into workflows. Scenario-level orchestration could reduce this burden, but trades composability for convenience.

## Open questions

- Should connection be a step within the write/ingest workflow rather than a separate skill invocation? What's the mechanism — a skill that orchestrates the full scenario, or `AGENTS.md` instructions that remind the agent to connect after writing?
- How specific should the fragment's escalation hints be? A blanket "for deeper reasoning, search `commonplace/kb/`" may be too vague. Per-topic hints (e.g., pointing at a specific ADR) are more precise but harder to maintain.
- Orchestration quality (did the agent complete the full chain correctly?) remains unmeasured. Hop counts and byte budgets are tractable via `/evaluate-scenarios`; end-to-end correctness is not.

---

Relevant Notes:

- [scenario-decomposition-drives-architecture](../notes/scenario-decomposition-drives-architecture.md) — theory: the general method of decomposing user stories into step-by-step context needs and deriving architectural requirements from the pattern
- [006-two-tree-installation-layout](./adr/006-two-tree-installation-layout.md) — decision: the two-tree split between commonplace and installed projects that this architecture instantiates
- [014-scripts-as-python-package-one-tree-model](./adr/014-scripts-as-python-package-one-tree-model.md) — decision: `commonplace-init` as the install entry point and the one-tree model for operational artifacts
- [architecture](./architecture.md) — current-state: the broader repo layout this scenario architecture sits inside
- [control-plane-goals](./control-plane-goals.md) — current-state: how the `AGENTS.md` fragment carries the `## KB Goals` section that scenario decomposition depends on
- [instruction-generation](./instruction-generation.md) — current-state: how `commonplace-init` produces the fragment and the rest of the installed tree
