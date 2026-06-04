---
description: "Operational Ontology Framework review: public templates and artifact vocabulary for D+L+A governance, not an implemented runner or extractor"
type: ../types/agent-memory-system-review.md
status: current
last-checked: "2026-06-02"
---

# Operational Ontology Framework

Operational Ontology Framework is FSTech Digital's public reference for structuring AI work around explicit operational state, rules, actions, governance artifacts, and write-back discipline. The inspected repository is intentionally a method surface: README/docs, minimal artifact templates, and example schemas. It does not publish production code, prompts, agents, adapters, deployment scripts, or a runtime that reads, writes, retrieves, or validates the artifacts.

**Repository:** https://github.com/fstech-digital/operational-ontology-framework

**Reviewed commit:** [0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9](https://github.com/fstech-digital/operational-ontology-framework/commit/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9)

**Last checked:** 2026-06-02

## Core Ideas

**The repository publishes the map, not the machine.** The README says the repository contains core concepts, the D+L+A model, governance artifacts, anti-patterns, generic schemas, and templates, then explicitly excludes FSTech production code, client implementations, prompts, agents, adapters, deployment scripts, and playbooks ([README.md](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/README.md), [docs/examples-redacted.md](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/docs/examples-redacted.md), [NOTICE.md](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/NOTICE.md)). This matters for review placement: the code-grounded artifact is a public governance vocabulary, not an executable memory system.

**D+L+A is the governing frame.** The method splits operational AI into Data, Logic, and Action: entities/state/sources/ownership, rules/routes/validations/policies, and allowed execution with approvals and audit trail ([docs/dla-model.md](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/docs/dla-model.md), [docs/what-is-operational-ontology.md](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/docs/what-is-operational-ontology.md)). Its memory relevance is that retained context is not treated as undifferentiated recall; it is placed into operational roles that can constrain decisions and actions.

**Five artifact families separate volatility and authority.** Pin holds invariants, Spec holds current work, Handoff preserves session continuity, Facts hold long-term observations with source/confidence, and Skills hold reusable procedures refined by practice ([README.md](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/README.md), [docs/artifacts.md](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/docs/artifacts.md), [templates/](https://github.com/fstech-digital/operational-ontology-framework/tree/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/templates)). The families are a useful retained-artifact vocabulary even though the repo does not implement storage, retrieval, validation, or promotion logic around them.

**Write-back is a discipline, not an implemented learning loop.** Handoff, Facts, Spec, and Skills templates define places where future operators could record decisions, observations, completed work, and procedure refinements ([templates/_handoff.md](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/templates/_handoff.md), [templates/_facts.md](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/templates/_facts.md), [templates/_skills.md](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/templates/_skills.md), [templates/_spec.md](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/templates/_spec.md)). I found no code that ingests traces, runs extraction, updates those files, or decides which write-back becomes durable behavior-shaping material.

**Context efficiency comes from partitioning, not retrieval machinery.** The framework reduces context complexity by assigning material to roles: rarely changing invariants in Pin, volatile execution state in Spec, append-only continuity in Handoff, observed knowledge in Facts, and procedural know-how in Skills. There is no token budget, search index, relevance matcher, progressive disclosure engine, or automatic loading policy in the public checkout. Efficiency depends on a human or host agent loading the right artifact family for the next operation.

**Anti-patterns are part of the method's authority surface.** The docs reject prompt-as-architecture, retrieval-as-memory, chatbot theater, no write-back, and unbounded agency ([docs/anti-patterns.md](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/docs/anti-patterns.md)). These are prescriptive constraints on how adopters should build systems, but in this repository they remain prose guidance rather than executable gates.

## Artifact analysis

- **Storage substrate:** `files` — Markdown files in the public GitHub repository under `README.md` and `docs/`
- **Representational form:** `symbolic` — Prose, with small tables for concepts and failure modes
- **Lineage:** `authored` — Public docs, templates, example schemas, and policy files are authored reference material rather than generated from operational traces in the inspected checkout.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` — Docs and templates advise adopters, while Pins, Specs, Skills, schemas, guardrails, decision routes, and repository policies can instruct, route, constrain, or validate downstream work when adopted.

**Framework docs.** Storage substrate: Markdown files in the public GitHub repository under `README.md` and `docs/`. Representational form: prose, with small tables for concepts and failure modes. Lineage: authored public reference material, not generated from operational traces in the inspected checkout. Behavioral authority: system-definition artifact for adopters at design time; it instructs architects and agents to model Data, Logic, Action, write-back, and guardrails explicitly, but has no direct runtime authority unless copied into a host system's instructions or process.

**Templates.** Storage substrate: Markdown files under `templates/`. Representational form: mixed prose and symbolic section structure. Lineage: authored generic templates for artifact instances; filling them in would create project-specific retained artifacts outside this repository. Behavioral authority varies by template. Pin is intended as a system-definition artifact because its invariants, rules, decision routes, boundaries, escalation rules, and automations are supposed to constrain future agent action. Spec is a system-definition artifact for current execution state and acceptance criteria. Handoff and Facts are mostly knowledge artifacts when consumed as continuity, evidence, observations, preferences, decisions, and patterns. Skills are prose system-definition artifacts when a future agent follows them as procedures. Effective authority is not verified from code because the public repo does not wire any agent loader or enforcement path.

**Example schemas.** Storage substrate: JSON example files under `schemas/`. Representational form: symbolic examples for pin, decision route, and workflow shape. Lineage: authored examples, not compiled from templates or validated by repository code. Behavioral authority: descriptive/reference authority in this repo; they would become validation or routing system-definition artifacts only if a downstream implementation adopted them as schemas or generated checks from them.

**License, notice, security, and contributing boundaries.** Storage substrate: repository policy files. Representational form: prose legal and operational constraints. Lineage: authored public policy. Behavioral authority: system-definition artifact for repository participation and reuse, especially because the license excludes future code, prompts, agents, adapters, operational playbooks, and production/client-specific material from the public grant ([LICENSE](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/LICENSE), [SECURITY.md](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/SECURITY.md), [CONTRIBUTING.md](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/CONTRIBUTING.md)).

There is no implemented promotion path in the inspected repository. The conceptual path is clear: Handoff and Facts can inform future Skills, Specs, or Pins; repeated execution can refine Skills; decision routes can be made more explicit. But no checked code performs that promotion, checks it, or records lineage from raw traces to distilled rules.

## Comparison with Our System

| Dimension | Operational Ontology Framework | Commonplace |
|---|---|---|
| Primary purpose | Public method for operating AI under explicit Data, Logic, Action, and governance artifacts | Git-native framework and KB for typed agent-operated knowledge artifacts |
| Published substrate | Markdown docs, templates, and example JSON schemas | Markdown collections, type specs, schemas, commands, validators, generated indexes, review workflows |
| Runtime implementation | Not published in this checkout | Implemented CLI commands, validation, indexing, skills, and review system |
| Memory artifacts | Pin, Spec, Handoff, Facts, Skills as generic templates | Notes, references, instructions, sources, reviews, ADRs, work artifacts, generated indexes |
| Context activation | Host/user discipline; no public loader or matcher | Agent instructions, collection contracts, `rg`, indexes, links, skills, validation/review workflows |
| Governance | Conceptual governance and artifact templates | Enforced frontmatter/type validation, link checks, review gates, replacement archives, Git history |

The strongest overlap is the insistence that memory must be operationally typed. Operational Ontology's Pin/Spec/Handoff/Facts/Skills vocabulary is a compact version of a point Commonplace makes with collection contracts and artifact types: retained material changes future behavior only through a known role, consumer, and authority path.

The biggest divergence is implementation status. Commonplace ships executable commands, schemas, validators, generated indexes, and skills. Operational Ontology Framework explicitly withholds the production machine and publishes only the public reference surface. That makes it a useful design comparison but a weak implementation benchmark for retrieval, write-back, trace extraction, or activation.

The second divergence is reviewability versus commercial redaction. Commonplace keeps methodology, examples, commands, and operational rules in the same repository so a reviewer can inspect the whole path from source text to behavior-shaping artifact. Operational Ontology Framework documents the shape of such systems while leaving real prompts, agents, adapters, deployments, dashboards, and client implementations outside the public checkout.

**Read-back:** `pull` — From the inspected repository. A human or agent can deliberately read the docs/templates, but I found no relevance-gated or state/scoped pre-action push activation, no always-loaded agent config, and no runtime loader

### Borrowable Ideas

**Pin as an invariant artifact class.** Ready now as vocabulary. Commonplace already has higher-authority instructions and type specs, but "Pin" is a useful name for low-volatility operational invariants that should override volatile work state.

**Separate Handoff from Facts.** Ready for workshop design. Commonplace work artifacts could distinguish append-only session continuity from longer-lived observations more explicitly, preventing temporary handoff material from masquerading as durable knowledge.

**D+L+A as an audit prompt for agent workflows.** Ready as a lightweight review lens. For any proposed agent automation, ask what the Data, Logic, and Action layers are, where each persists, and which artifact has authority over the next action.

**Anti-pattern catalogue for adoption reviews.** Ready as a checklist. "Retrieval as memory" and "prompt as architecture" are concise failure labels that map cleanly onto Commonplace's distinction between stored knowledge and contextual activation.

**Do not borrow template-only claims as evidence of implementation.** Ready as a review discipline. The repo is a good reminder that artifact destinations and write-back vocabulary are not enough to claim trace-derived learning, push activation, validation, or runtime governance.

## Curiosity Pass

**The public repository is intentionally sparse.** That sparseness is itself part of the artifact: it keeps the method legible but prevents a code-grounded reviewer from verifying the operational layer the method describes.

**The artifact names are strong because they encode volatility.** Pin, Spec, Handoff, Facts, and Skills are not just document categories. They imply update frequency, conflict resolution, and read priority. The templates would be less useful if they were generic "notes."

**Facts and Skills gesture toward learning without implementing extraction.** Facts have source/date/confidence fields, and Skills say they improve through write-back after execution. Those are good destinations for learning outputs, but not evidence that this checkout derives durable artifacts from traces.

**The schema examples are interface sketches, not validators.** The JSON files are useful as shape examples, but without a package, command, CI check, or schema meta-definition they do not yet enforce anything.

**The framework is closest to Commonplace at the artifact-contract layer.** It is not a memory database, RAG engine, or agent runtime. Its useful comparison point is how it names retained surfaces and their authority.

## What to Watch

- Whether FSTech publishes a runner, CLI, agent integration, or validation package that turns the templates into enforceable artifacts.
- Whether future public examples include concrete lifecycle transitions: Handoff to Fact, Fact to Skill, Skill to Pin, or Spec completion to durable history.
- Whether schema examples become real JSON Schemas with tests, versioning, and migration rules.
- Whether an implementation defines a read-back policy: which artifacts are loaded before which actions, with what scope and precedence.
- Whether write-back gains provenance fields strong enough to distinguish observed traces, human decisions, inferred facts, and promoted rules.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - exemplifies: the repository defines durable artifact destinations, but not an implemented activation path.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - exemplifies: Pin, Spec, Handoff, Facts, Skills, schemas, and policy files need separate substrate/form/lineage/authority classification.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: Handoff and Facts mostly serve as evidence, reference, continuity, and advice unless a host gives them stronger authority.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: Pin, Spec, Skills, schemas, and repository policies can instruct, constrain, route, or validate when a host system consumes them with force.
- [Agent memory is a crosscutting concern, not a separable niche](../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) - contrasts: the public framework names crosscutting governance surfaces but omits the host runtime integration that would make them act.
