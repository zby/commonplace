---
description: "Operational Ontology Framework review: public files-first artifact model for Pin/Spec/Facts/Handoff/Skills governance, with no published runner implementation"
type: ../types/agent-memory-system-review.md
tags: [trace-derived]
status: current
last-checked: "2026-05-16"
---

# Operational Ontology Framework

Operational Ontology Framework is a public reference from FSTech for making AI work auditable by externalizing state, rules, actions, and write-back into simple project files. The reviewed repository is not an executable agent runner: its README says production code, prompts, agents, adapters, deployment scripts, and commercial playbooks are intentionally not published. What is published is still relevant to agent memory design: a compact five-artifact vocabulary, minimal markdown templates, and a D+L+A framing that treats Data, Logic, and Action as explicit operating surfaces rather than hidden prompt context.

**Repository:** https://github.com/fstech-digital/operational-ontology-framework

**Reviewed commit:** [0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9](https://github.com/fstech-digital/operational-ontology-framework/commit/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9)

## Core Ideas

**The public system is an artifact contract, not a runner.** The repo contains docs, schemas, and templates; `git ls-tree` shows no source package, CLI, MCP server, provider adapter, task scanner, tests, or implementation module. The README is explicit that the repository publishes the "public surface" and "map, not the machine," excluding production code, agents, adapters, deployment scripts, prompts, and client playbooks ([README.md](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/README.md), [docs/examples-redacted.md](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/docs/examples-redacted.md), [CONTRIBUTING.md](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/CONTRIBUTING.md)). Any review of "runner load path," "task execution," "fact consolidation," or "provider adapters" has to be negative for this commit: those surfaces are not present in the public checkout.

**Pin, Spec, Facts, Handoff, and Skills divide behavioral authority by volatility.** The central design is a five-file governance model. Pin holds invariants such as identity, domain entities, boundaries, immutable rules, decision routes, and automations; Spec holds current tasks, blockers, acceptance criteria, completed work, and sprint notes; Handoff records session focus, decisions, attempts, changed artifacts, continuation markers, and verification; Facts holds long-term observations with source, date, confidence, and aging review; Skills holds reusable procedures with triggers, steps, tools, done criteria, edge cases, refinement dates, and archival criteria ([docs/artifacts.md](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/docs/artifacts.md), [templates/_pin.md](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/templates/_pin.md), [templates/_spec.md](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/templates/_spec.md), [templates/_handoff.md](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/templates/_handoff.md), [templates/_facts.md](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/templates/_facts.md), [templates/_skills.md](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/templates/_skills.md)). The useful move is not the exact filenames; it is the authority split between stable constraints, active work state, episodic continuity, observed knowledge, and procedural know-how.

**The storage substrate is ordinary files, with schemas only as examples.** The repository's operative artifacts are markdown templates and three small JSON schema examples for Pin, decisions, and workflows ([templates/](https://github.com/fstech-digital/operational-ontology-framework/tree/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/templates), [schemas/](https://github.com/fstech-digital/operational-ontology-framework/tree/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/schemas)). There is no database, vector store, event log, cache, or generated index in the public repo. Representational form is mostly prose markdown with light symbolic structure: headings, checkboxes, tables, confidence labels, route conditions, approval flags, and write-back targets. That makes the system inspectable and easy to adopt, but leaves enforcement to whoever loads, edits, and reviews the files.

**D+L+A frames memory as operational control, not recall.** The docs define Data as entities, relationships, states, sources, and ownership; Logic as thresholds, routes, validations, policies, and exceptions; and Action as executable verbs with approvals and audit trail ([docs/dla-model.md](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/docs/dla-model.md), [docs/what-is-operational-ontology.md](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/docs/what-is-operational-ontology.md)). This is close to commonplace's retained-artifact vocabulary: stored state matters because it can narrow future interpretation, route decisions, authorize actions, or force escalation. Pin and workflow schemas are system-definition artifacts when consumed as rules, routes, validation targets, approvals, or configuration; Facts and Handoff entries are knowledge artifacts when consumed as evidence, continuity context, or advice; Skills become system-definition artifacts when an agent executes them as prescribed procedures.

**Write-back is the learning mechanism, but consolidation is manual or external.** The README names "No write-back" as an anti-pattern and says the system is for cases where execution must update durable state ([README.md](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/README.md), [docs/anti-patterns.md](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/docs/anti-patterns.md)). The templates show where learned material lands: completed Spec tasks include a `Learned:` line, Handoff records attempts/results and continuation markers, Facts accepts observed/inferred/verified observations, and Skills are refined after execution ([templates/_spec.md](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/templates/_spec.md), [templates/_handoff.md](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/templates/_handoff.md), [templates/_facts.md](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/templates/_facts.md), [templates/_skills.md](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/templates/_skills.md)). What is absent is an implemented extractor, judge, deduper, merger, or promotion pipeline that turns raw task outputs into canonical facts or skill edits.

**Audit and git claims are conceptual, not implemented machinery.** The docs repeatedly emphasize auditability, explicit rules, versioning, approvals, and write-back. The decision schema includes `record_reasoning`, `record_actor`, and `record_timestamp`; the workflow schema has `requires_approval` and `write_back.required` fields ([schemas/decision.schema.example.json](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/schemas/decision.schema.example.json), [schemas/workflow.schema.example.json](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/schemas/workflow.schema.example.json)). But this commit does not ship git hooks, validation commands, changelog appenders, immutable logs, signed records, or tests. The audit model is therefore an authoring convention over files, not a verified runtime guarantee.

## Comparison with Our System

| Dimension | Operational Ontology Framework | Commonplace |
|---|---|---|
| Primary substrate | Public markdown templates and example JSON schemas | Typed markdown collections with validators, indexes, skills, and review commands |
| Artifact split | Pin, Spec, Handoff, Facts, Skills | Notes, reference docs, instructions, sources, reviews, work artifacts, indexes |
| Behavior-shaping authority | Mostly conventions in artifact headings and comments | Type specs, collection conventions, validation, authored links, CLI commands, review workflows |
| Runtime/tool surface | None published in this checkout | `commonplace-*` commands plus local skills and repo-native workflows |
| Task execution | Spec template records tasks; no scanner or executor | Instructions and skills can be invoked by agents; validation/review commands are executable |
| Learning loop | Write-back into Spec/Facts/Handoff/Skills by discipline | Manual and semi-automated note writing, review bundles, validation, and index generation |
| Audit | Conceptual traceability and schema examples | Git history, deterministic validation, archived reviews, generated reports, explicit review artifacts |

The strongest convergence is files-first governance. Both systems assume that important operational state should be readable, versionable, and editable as ordinary artifacts rather than hidden in retrieval infrastructure. The Operational Ontology split is also attractively compact: an agent can understand the intended load order from the names alone. Pin constrains, Spec focuses, Handoff resumes, Facts inform, Skills execute.

The main divergence is implementation depth. Commonplace has shipped commands, type specs, validators, collection-local contracts, generated indexes, and review machinery. Operational Ontology Framework, at this commit, publishes the vocabulary and templates but not the runner that would load Pin before Spec, scan tasks, execute actions, call provider adapters, consolidate facts, generate handoffs, run tests, or enforce audit rules. That makes it a useful design reference, not a code-grounded peer runtime.

The authority gradient is cleaner than many larger systems. Pin is explicitly stronger than Facts: the Facts template says facts are not rules and Pin wins on conflict. Skills reference Pin constraints but should not duplicate them. Spec completed tasks are immutable history, with defects represented as new corrective tasks. Those are small rules, but they express real lifecycle discipline in a way many "memory" systems blur.

**Read-back:** pull — agents or external runners must deliberately load Pin, Spec, Facts, Handoff, and Skills; no public runner injects them.

## Borrowable Ideas

**A five-file cold-start bundle.** Commonplace could borrow the Pin/Spec/Facts/Handoff/Skills bundle as a workshop bootstrap shape for projects that do not need the full KB type system. Ready as a workshop convention, not as a framework-level replacement for notes/reference/instructions.

**Make invariant-over-observation precedence explicit.** "If a fact conflicts with the Pin, the Pin wins" is a useful rule. A commonplace analogue would name which artifacts outrank observations during agent action: project instructions, ADRs, active specs, facts, and scratch notes should not all have equal force. Ready as vocabulary; needs careful integration with existing definitions of knowledge artifact and system-definition artifact.

**Use Handoff as an append-only continuity artifact.** The Handoff template's split between decisions, attempts/results, changed artifacts, next executable action, pending decision, blocked item, and verification is a compact handoff contract. Commonplace work directories already have reports and review artifacts, but a normalized handoff file could help long-running workshops.

**Keep Skills separate from Facts.** The framework's distinction is crisp: Facts inform decisions, Skills execute actions. Commonplace already separates notes from instructions, but this line is worth preserving whenever trace-derived observations are promoted into procedures. Ready as a review heuristic.

**Add aging rules to volatile operational memory.** Facts and Skills both include 90-day review/archive guidance. Commonplace has status fields and review warnings, but workshop artifacts could use explicit age-based decay rules for volatile operational claims.

## Trace-derived learning placement

Operational Ontology Framework qualifies only in a template-level, externally executed sense. It does not ship code that mines traces, but it does define durable places where session and execution traces are supposed to be written back into behavior-shaping files.

**Trace source.** The intended raw signal is task execution: current Spec tasks, completed task results, Handoff decisions, attempts, changed artifacts, verification notes, and repeated skill executions. The public repo has no raw session log format and no transcript capture.

**Extraction.** Extraction is author- or agent-mediated by convention. The templates tell the operator to record `Learned:` lines in completed Spec tasks, observations in Facts with source/date/confidence, session attempts and next actions in Handoff, and skill refinements after execution. There is no implemented oracle, judge, confidence scorer, deduper, merger, or promotion gate.

**Storage substrate.** Raw traces, if kept, are outside the published system. Distilled retained state lives in ordinary markdown files created from the templates. Example symbolic constraints may also live in JSON schema-shaped Pin, decision, and workflow records.

**Representational form.** The retained operative parts are mixed. Handoff and Facts are mostly prose with light symbolic fields; Pin rules, decision routes, boundaries, workflow steps, approval flags, checkboxes, and confidence labels are symbolic enough to route or constrain behavior if a runner honors them; Skills are procedural prose consumed as executable instruction.

**Lineage.** Facts include source, date, and confidence; Handoff includes changed artifacts and verification; Spec completed items retain result summaries and learned strings. That gives local provenance, but not a regeneration path. Once a learning is promoted into Facts or Skills, it is canonical unless a human or external runner revises it.

**Behavioral authority.** Raw task outputs and handoff traces are knowledge artifacts when read as evidence or continuity context. Facts are knowledge artifacts unless an operator treats a confirmed pattern as a rule. Pin, decision routes, workflow schemas, and executable Skills are system-definition artifacts because they constrain decisions, authorize or block actions, route escalation, require approval, or instruct future execution.

**Scope and timing.** The loop is per project, offline or at session boundary, and file-local. It is not cross-project model learning, embedding training, or online policy adaptation.

**Survey placement.** The framework strengthens the survey claim that trace-derived learning can be a simple write-back discipline rather than an ML pipeline. It also weakens any claim that templates alone constitute an implemented learning system: the behavior change depends on an external operator or runner consistently promoting learned strings into the right files.

## Curiosity Pass

**The user's runner lens is the right question and the wrong answer for this commit.** The artifact names imply a project runner: load Pin, read Spec, perform tasks, append Handoff, consolidate Facts, refine Skills. The public repository does not implement that path. That absence should be preserved in the review because it is the main code-grounded finding.

**The framework is strongest as a minimum viable ontology.** It avoids the common overbuilt move of starting with a graph database, vector memory, or elaborate agent runtime. The five artifacts cover most operational state an agent needs to behave less statelessly.

**The biggest risk is authority by comment.** The templates contain strong guidance in comments, but no validator enforces it. A future implementation could accidentally flatten Pin, Facts, Handoff, and Skills into equal context snippets, losing the authority distinctions that make the framework valuable.

**Auditability is currently aspirational.** Versioned files can support audit, and the schemas name actor/reason/timestamp recording, but audit depends on implementation choices not present here. There is no append-only store, commit convention, proof gate, or test suite in the public checkout.

**The license and contribution policy reinforce the public-surface boundary.** The license excludes future code, prompts, agents, adapters, and playbooks unless separately licensed, and CONTRIBUTING tells contributors not to submit production code or implementation-specific playbooks ([LICENSE](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/LICENSE), [CONTRIBUTING.md](https://github.com/fstech-digital/operational-ontology-framework/blob/0c70e70b5fc634d9dda8bdb880bf75557f3ae9e9/CONTRIBUTING.md)). That makes the absence of runner code a deliberate publication boundary, not an accidental omission.

## What to Watch

- Whether FSTech publishes a runner, CLI, MCP server, provider adapters, or validation suite that turns the artifact model into executable machinery.
- Whether future schemas define full Pin/Spec/Facts/Handoff/Skills contracts rather than examples.
- Whether fact consolidation and skill refinement gain explicit promotion criteria, conflict handling, deduplication, and aging/retirement mechanics.
- Whether audit claims become tied to git conventions, append-only handoffs, signed records, tests, or policy gates.
- Whether the framework's five-file model appears in client-neutral examples detailed enough to evaluate load order and write-back behavior.

---

Relevant Notes:

- [Files beat a database for agent-operated knowledge bases](../../notes/files-not-database.md) - exemplifies: the framework's public artifact model assumes durable operational state should live in inspectable files rather than a hidden memory store
- [A functioning knowledge base needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) - compares-with: Pin/Spec/Handoff/Facts/Skills are a compact workshop-state bundle, though without commonplace's library and validation machinery
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - defined-in: Facts and Handoff entries usually advise, evidence, or resume future work
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - defined-in: Pin, decision routes, workflow approvals, and executable Skills have constraint, routing, configuration, or instruction force
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - qualifies: the framework defines write-back destinations for learned strings, but leaves extraction and promotion to external discipline
- [ByteRover CLI](./byterover-cli.md) - contrasts: ByteRover implements a file-backed memory product with runner services, MCP, review logs, manifests, and sidecars; Operational Ontology Framework publishes only the artifact vocabulary and templates
