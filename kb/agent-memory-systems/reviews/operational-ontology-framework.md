---
description: "Operational Ontology Framework review: public D+L+A artifact templates for governed AI work, with no implemented memory runtime"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-06-04"
---

# Operational Ontology Framework

Operational Ontology Framework, from FSTech Digital, is a public reference surface for operating AI systems with explicit Data, Logic, Action, governance artifacts, and write-back discipline. The reviewed repository contains docs, Markdown templates, and generic JSON examples; it explicitly does not publish production code, prompts, agents, adapters, deployment scripts, dashboards, or client implementations.

**Repository:** https://github.com/fstech-digital/operational-ontology-framework

**Reviewed commit:** [0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9](https://github.com/fstech-digital/operational-ontology-framework/commit/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9)

**Source directory:** `related-systems/fstech-digital--operational-ontology-framework`

## Core Ideas

**The repository publishes the map, not the machine.** The README says the public surface includes core concepts, D+L+A, governance artifacts, anti-patterns, schemas, and templates, while excluding production code, client implementations, prompts, agents, adapters, deployment scripts, and commercial playbooks ([README.md](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/README.md), [docs/examples-redacted.md](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/docs/examples-redacted.md)). That boundary is the most important code-grounded finding: this is a method/template repository, not an implemented agent-memory runtime.

**D+L+A turns memory into operational state.** The framework splits an operational AI system into Data, Logic, and Action: entities, relationships, state, sources, rules, routes, validations, policies, allowed actions, approvals, and audit trail ([docs/dla-model.md](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/docs/dla-model.md), [docs/what-is-operational-ontology.md](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/docs/what-is-operational-ontology.md)). Its memory relevance is not retrieval mechanics; it is the insistence that durable state, rules, and next actions must be explicit enough to bound later behavior.

**Five artifact families separate volatility and authority.** Pin stores invariants, Spec stores current work, Handoff stores session continuity, Facts store long-term observations with source/date/confidence, and Skills store reusable procedures refined through practice ([README.md](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/README.md), [docs/artifacts.md](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/docs/artifacts.md), [templates/](https://github.com/fstech-digital/operational-ontology-framework/tree/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/templates)). This vocabulary is useful because it names what changes rarely, what changes per task, what carries continuity, what records observations, and what should become reusable procedure.

**Context efficiency comes from partitioning, not selection code.** The framework lowers context complexity by telling adopters where different kinds of retained material belong: low-volatility invariants in Pin, high-volatility execution state in Spec, session carry-over in Handoff, longer-lived observations in Facts, and procedural know-how in Skills. I found no token budget, search index, relevance matcher, progressive loader, or automatic prompt assembly in the inspected checkout.

**Write-back is required as a discipline, not implemented as a loop.** The templates define destinations where future operators could record decisions, observations, completed work, next actions, and skill refinements ([templates/_handoff.md](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/templates/_handoff.md), [templates/_facts.md](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/templates/_facts.md), [templates/_skills.md](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/templates/_skills.md), [templates/_spec.md](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/templates/_spec.md)). The repository does not include code that watches traces, extracts memories, updates artifacts, promotes facts into skills, or verifies that write-back happened.

**Anti-patterns define the method's negative authority.** The docs reject prompt-as-architecture, retrieval-as-memory, automation before simplification, chatbot theater, no write-back, and unbounded agency ([docs/anti-patterns.md](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/docs/anti-patterns.md)). In this repository those are design constraints for adopters, not executable gates.

## Artifact analysis

- **Storage substrate:** `repo` `files` — The reviewed retained surface is Git-tracked Markdown documentation, Markdown templates, generic JSON examples, and repository policy files. The repository does not publish a database, vector store, graph store, prompt registry, service object, or model artifact.
- **Representational form:** `prose` `symbolic` — README/docs/templates carry prose guidance and section structure; the schema examples, decision routes, workflow examples, tables, checklist fields, source/date/confidence fields, and repository policies are symbolic shapes. There is no parametric retained state in the inspected checkout.
- **Lineage:** `authored` — The artifacts are authored public reference material and generic templates. I found no import pipeline and no durable artifacts derived from session logs, tool traces, event streams, trajectories, or evaluation traces.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` — In this repository the docs and templates advise and instruct adopters, route attention across Data/Logic/Action and Pin/Spec/Handoff/Facts/Skills, and sketch validation/audit fields. Stronger runtime authority is not verified because no agent loader, validator, router, or enforcement path is published.

**Framework docs.** The docs are authored knowledge and instruction artifacts for architects and agent operators. They explain how to make entities, rules, actions, escalation, state, and write-back explicit, but they do not themselves act on a future agent unless a host system loads them as instructions.

**Templates.** The templates are authored prose/symbolic system-definition candidates. Pin is meant to constrain future action with invariants, rules, boundaries, decision routes, and automations; Spec is current execution state and acceptance criteria; Handoff carries continuity; Facts hold observations and confidence; Skills define reusable procedures and refinement criteria. Their effective authority depends on adoption outside this repository.

**Schema examples.** The JSON files under `schemas/` are symbolic examples for pin, decision, and workflow shape ([schemas/pin.schema.example.json](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/schemas/pin.schema.example.json), [schemas/decision.schema.example.json](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/schemas/decision.schema.example.json), [schemas/workflow.schema.example.json](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/schemas/workflow.schema.example.json)). They are not wired to tests, a package, a CLI, or a schema validator in the public checkout.

Promotion path: conceptually, a Handoff can become Facts, repeated Facts can inform Skills, and durable Skills or rules can become Pin material. The repository names those destinations and criteria, but it does not implement promotion, provenance tracking, invalidation, or review of such transitions.

## Comparison with Our System

| Dimension | Operational Ontology Framework | Commonplace |
|---|---|---|
| Primary purpose | Public method and templates for governed operational AI | Git-native framework and KB for typed agent-operated knowledge artifacts |
| Published substrate | Markdown docs, Markdown templates, and generic JSON examples | Markdown collections, type specs, schemas, commands, validators, indexes, review workflows |
| Runtime implementation | Not published in this checkout | Implemented CLI commands, validation, indexing, skills, and review system |
| Memory artifacts | Pin, Spec, Handoff, Facts, Skills as generic artifact families | Notes, references, instructions, sources, reviews, ADRs, work artifacts, generated indexes |
| Context activation | Host/user discipline; no public loader or matcher | Agent instructions, collection contracts, `rg`, indexes, links, skills, validation and review workflows |
| Governance | Conceptual governance and artifact templates | Enforced frontmatter/type validation, link checks, review gates, replacement archives, Git history |

The strongest overlap is the claim that retained knowledge needs an explicit operational role. Operational Ontology's artifact families are a compact version of a Commonplace principle: memory changes future behavior only through a known consumer, authority path, and update discipline.

The biggest divergence is implementation. Commonplace ships executable validation, indexing, type contracts, review workflows, and source-grounding procedures. Operational Ontology Framework publishes the public vocabulary and template layer, while keeping real prompts, agents, adapters, dashboards, deployments, and client implementations outside the repository.

The second divergence is evidence reviewability. Commonplace can be reviewed from source text through generated indexes and validation behavior. Operational Ontology Framework can only be reviewed as authored guidance; claims about automatic write-back, retrieval, governance, or read-back must remain unverified unless a downstream implementation is inspected.

### Borrowable Ideas

**Pin as a name for invariants.** Ready now as vocabulary. Commonplace already has high-authority instructions and type specs, but "Pin" is a useful compact name for low-volatility operational invariants that should override temporary work state.

**Separate Handoff from Facts.** Ready for workshop design. Commonplace can keep session continuity distinct from durable observations so temporary state does not masquerade as long-lived knowledge.

**D+L+A as an audit lens.** Ready now as a review prompt. For any proposed agent workflow, ask which Data, Logic, and Action artifacts exist, where each persists, and which one has authority over the next action.

**Anti-pattern labels for adoption reviews.** Ready now. "Retrieval as memory," "prompt as architecture," and "no write-back" are concise failure labels that map cleanly onto Commonplace's distinctions between storage, activation, and maintained authority.

**Do not borrow template-only evidence as implementation evidence.** Ready as review discipline. A destination for write-back is not evidence of automatic trace learning; a schema example is not evidence of enforcement; an artifact taxonomy is not evidence of read-back.

## Write side

**Write agency:** `manual` — In the inspected repository, retained artifacts change by authored repository edits or by a downstream adopter manually filling templates. I found no implemented automatic write, curation, promotion, invalidation, consolidation, decay, synthesis, or trace-learning loop.

## Read-back

**Read-back:** `pull` — The public artifacts re-enter future work when a human, agent, or host system deliberately reads the docs/templates or copies them into an implementation. I found no published runner, hook, loader, relevance matcher, or pre-invocation memory injection path that automatically pushes retained project memory into an agent context.

The templates can support a push-capable downstream system if a host always loads Pin or selects artifacts before an agent acts, but that behavior is not implemented in this checkout. The reviewed repository therefore stays pull-only: useful to consult, not an observed activation mechanism.

## Curiosity Pass

**The most important source line is the absence claim.** "Map, not machine" is not marketing color; it materially limits what a code-grounded review can classify.

**The template names encode volatility.** Pin, Spec, Handoff, Facts, and Skills carry update-frequency and authority assumptions, which makes them stronger than generic "notes" or "memory" labels.

**Facts and Skills gesture toward learning without proving it.** Facts have source/date/confidence fields, and Skills say they improve through write-back after execution. Those are good destinations for learning outputs, but not evidence that this repository derives durable artifacts from traces.

**The schema examples are interface sketches.** They may be useful adoption aids, but without validator code, package metadata, tests, or CI, they should not be counted as enforcement.

**Commercial redaction changes the review target.** The public repo may describe a real private operational practice, but this review can only classify the public source surface.

## What to Watch

- Whether FSTech publishes a runner, CLI, agent integration, validator, or prompt-loading package; that would change the review from method-surface coverage to runtime coverage.
- Whether future examples show concrete lifecycle transitions from Handoff to Fact, Fact to Skill, Skill to Pin, or Spec completion to durable history.
- Whether the JSON examples become real schemas with tests, versioning, and migration rules.
- Whether a public implementation defines read-back policy: which artifacts are loaded before which actions, at what scope, and with what precedence.
- Whether write-back gains provenance fields that distinguish observed traces, human decisions, inferred facts, and promoted rules.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: the repository defines durable artifact destinations but no implemented activation path.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: docs, templates, schema examples, and policy files have different forms and authority levels.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: Facts, Handoff material, and framework docs mostly advise unless a host gives them stronger authority.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: Pin, Spec, Skills, decision routes, and schemas can instruct, route, or validate when adopted by a host system.
- [Agent memory is a crosscutting concern, not a separable niche](../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) - relates: the framework treats memory as operational state across rules, actions, escalation, and write-back.
