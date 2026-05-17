---
description: "Filesystem-first operational memory framework with Pin/Spec/Facts/Handoff/Skills artifacts and a small Python runner that promotes task learnings into project facts"
type: ../types/agent-memory-system-review.md
traits: [has-comparison]
tags: []
status: outdated
last-checked: "2026-04-13"
---

# Operational Ontology Framework

> Replaced 2026-05-16. See [Operational Ontology Framework](./operational-ontology-framework.md) for the current review.

Operational Ontology Framework is a small reference implementation from fstech-digital / Felipe Silva for running production-oriented agents with explicit project state in markdown files rather than persistent model memory or a database. The repository presents a broader framework, but the inspected implementation is intentionally compact: a Python CLI runner, provider adapters, templates, tests, and one customer-support example. It is closest to a project operations envelope for a single agent: rules, tasks, accumulated facts, and session handoffs are made explicit as files, while the model call remains a simple task executor. The repository is https://github.com/fstech-digital/operational-ontology-framework.

**Repository:** https://github.com/fstech-digital/operational-ontology-framework
**Reviewed commit:** https://github.com/fstech-digital/operational-ontology-framework/commit/a1034dee1a2f24a232238afa5ac878dca95f6549

## Core Ideas

**Five named memory artifacts, but four are loaded by the runner.** The README defines Pin, Spec, Handoff, Facts, and Skills as the operating ontology: Pin holds invariant rules, Spec holds tasks and execution state, Handoff records session continuation, Facts hold accumulated long-term knowledge, and Skills hold reusable procedures (https://github.com/fstech-digital/operational-ontology-framework/blob/a1034dee1a2f24a232238afa5ac878dca95f6549/README.md). The runner's boot path actually loads `_pin.md`, `_spec.md`, `_facts.md`, and the latest file under `handoffs/`; `_skills.md` exists as a template but is not read or injected by `agent.py` (https://github.com/fstech-digital/operational-ontology-framework/blob/a1034dee1a2f24a232238afa5ac878dca95f6549/agent.py, https://github.com/fstech-digital/operational-ontology-framework/blob/a1034dee1a2f24a232238afa5ac878dca95f6549/templates/_skills.md).

**The retrieval model is whole-file loading, not search.** README language says Boot queries the Fact Store for relevant context, but the code reads the entire `_facts.md` file and latest handoff into the system prompt. The only context-control mechanism is a rough character-count warning against model-family context estimates, plus capping within-session learnings to the last 10 entries (https://github.com/fstech-digital/operational-ontology-framework/blob/a1034dee1a2f24a232238afa5ac878dca95f6549/agent.py). There is no embedding index, no keyword retrieval, and no section selection. That is not a flaw for the current size; it is the design's simplicity boundary.

**Spec is both task queue and write-back surface.** `find_open_tasks()` scans `_spec.md` for unchecked markdown tasks while excluding a `## Blocked` section, then `mark_task_done()` replaces the first matching task with a checked task and a short `Learned:` annotation (https://github.com/fstech-digital/operational-ontology-framework/blob/a1034dee1a2f24a232238afa5ac878dca95f6549/agent.py). The example project shows the intended shape: open customer-support tickets under Current Sprint, completed tasks with learnings, and blocked tasks with an explicit next-check date (https://github.com/fstech-digital/operational-ontology-framework/blob/a1034dee1a2f24a232238afa5ac878dca95f6549/examples/customer-support/_spec.md).

**Trace-derived facts are promoted from the model's task result, not from a raw transcript.** Each task prompt asks the LLM to return JSON with `result`, `decision`, and `learned`. `consolidate_facts()` promotes non-default `learned` strings into `_facts.md` under `## Confirmed Patterns`, adding source, date, and `confidence: observed` metadata (https://github.com/fstech-digital/operational-ontology-framework/blob/a1034dee1a2f24a232238afa5ac878dca95f6549/agent.py). This makes the learning loop concrete but thin: the extracted signal is the agent's self-reported lesson, not a separately judged analysis of tool traces or execution logs.

**Handoff is an explicit cold-start artifact.** `generate_handoff()` writes a new timestamped markdown file for every run, with focus, decisions, tasks executed, and continuation advice (https://github.com/fstech-digital/operational-ontology-framework/blob/a1034dee1a2f24a232238afa5ac878dca95f6549/agent.py). The template emphasizes that a handoff is not the raw log; it is a state record for the next cold session (https://github.com/fstech-digital/operational-ontology-framework/blob/a1034dee1a2f24a232238afa5ac878dca95f6549/templates/_handoff.md). This is the repo's strongest alignment with the "store traces, load artifacts" principle.

**Provider portability is implemented as a tiny adapter seam.** `adapters.py` supports Anthropic, OpenAI, and Ollama through a shared `create_message(model, max_tokens, system, messages) -> str` interface, selected by the `ADAPTER` environment variable (https://github.com/fstech-digital/operational-ontology-framework/blob/a1034dee1a2f24a232238afa5ac878dca95f6549/adapters.py). The portability claim is credible at this layer because the runner depends only on text completion plus JSON-ish response parsing.

**Auditability is mostly a file-and-convention property.** The README says one task, one commit and points to `git log` / `git bisect`, but the runner does not invoke git, check repository cleanliness, or commit after task completion (https://github.com/fstech-digital/operational-ontology-framework/blob/a1034dee1a2f24a232238afa5ac878dca95f6549/README.md, https://github.com/fstech-digital/operational-ontology-framework/blob/a1034dee1a2f24a232238afa5ac878dca95f6549/agent.py). The implemented guarantee is lower but still useful: state is plain files, writes are atomic via temp-file rename, and tests cover the pure functions around parsing, task detection, fact consolidation, handoff discovery, and env loading (https://github.com/fstech-digital/operational-ontology-framework/blob/a1034dee1a2f24a232238afa5ac878dca95f6549/test_agent.py).

## Comparison with Our System

| Dimension | Operational Ontology Framework | Commonplace |
|---|---|---|
| Primary purpose | Run a project agent through task cycles with explicit operational memory | Build and operate an agent-readable knowledge base methodology |
| Primary substrate | Markdown project files plus optional git discipline | Markdown KB files with frontmatter, indexes, generated indexes, and validation |
| Core artifacts | Pin, Spec, Facts, Handoff, Skills template | Notes, indexes, instructions, sources, reviews, reference docs, workshop artifacts |
| Retrieval/loading | Load Pin + Spec + all Facts + latest Handoff | Search indexes/descriptions, then load selected files progressively |
| Learning loop | Promote per-task `learned` strings into Facts and handoffs | Human/agent revision, review gates, validation, explicit note promotion |
| Validation | Pytest over runner pure functions; template discipline | Deterministic validation plus semantic review workflows |
| Governance | Pin rules in prompt; Spec task state | AGENTS.md, collection conventions, type contracts, skills, validators |
| System boundary | Single project directory | Whole KB and packaged methodology for other KBs |

The deepest alignment is filesystem-first operational memory. Both systems treat files as the primary durable medium because they are readable, versionable, and directly accessible to agents. OOF is a clean external convergence point for the "files before database" bet, but it applies the bet to operational project state rather than to a long-lived conceptual library.

The deepest divergence is activation strategy. OOF does not try to solve fine-grained context activation: it loads the project's key files and relies on the prompt to make the right parts salient. Commonplace spends far more machinery on progressive disclosure, descriptions, indexes, and link semantics because the knowledge base is larger and the consumer may need only a small fragment. OOF is simpler and easier to run; commonplace is better suited to a corpus where "which knowledge should enter this call?" is the hard problem.

OOF also has a sharper operational-role separation than commonplace's default project workflow. Pin/Spec/Facts/Handoff is a useful vocabulary because it splits invariants, current work, learned observations, and continuation state. Commonplace has analogous layers - AGENTS instructions, workshop artifacts, source snapshots, notes, review records - but the names are less immediately task-runner-shaped.

## Borrowable Ideas

**Pin/Spec/Facts/Handoff as a project operations vocabulary (ready to borrow as wording).** The four-way split is easy to teach and maps cleanly to loading frequency: Pin is stable and high-priority, Spec is volatile and task-shaped, Facts are accumulated but pruneable, and Handoff is session-boundary state. Commonplace could use this vocabulary when explaining workshop project state, without adopting the runner.

**Handoff as a mandatory cold-start artifact (ready now).** The handoff template's discipline is strong: decisions need reasons, continuation needs concrete next steps, and the next session is assumed to start cold. This is directly compatible with commonplace's workshop-layer model.

**Blocked-task exclusion in task scanning (ready now).** The tiny `find_open_tasks()` rule that excludes a `## Blocked` section is exactly the kind of cheap convention that prevents an agent from wasting a run on known blocked work. Commonplace task conventions could copy this when a workshop has checklist-driven execution.

**Atomic file writes around agent-mutated memory (ready now).** The runner uses temp-file plus rename for Spec, Facts, and Handoff writes. For any commonplace command that lets an agent mutate operational state, atomic writes should be the default.

**Stale-fact marking as a file-native lifecycle hint (needs a use case).** OOF appends a stale marker to dated fact bullets older than 90 days, but only when consolidation runs with new facts. The idea is useful; the implementation is intentionally lightweight. In commonplace this belongs only where facts are high-volume and observational, not on curated theory notes.

**Minimal provider adapter contract (reference value).** The Anthropic/OpenAI/Ollama adapter seam is as small as it can be. It is useful evidence that some agent runners do not need a framework-level abstraction if their only model requirement is "system prompt + user message -> text."

## Trace-derived learning placement

Operational Ontology Framework is a **local filesystem runner** on axis 1 of the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md) and a **symbolic-artifact learner** on axis 2.

**Trace source.** The immediate trace source is not a raw conversation transcript or tool log. It is the per-task model output produced by `execute_task()`: a parsed JSON-ish record with `result`, `decision`, `learned`, `task`, and the raw output retained in memory for the current run (https://github.com/fstech-digital/operational-ontology-framework/blob/a1034dee1a2f24a232238afa5ac878dca95f6549/agent.py). The trigger boundary is task completion inside `run_cycle()`, plus a run-level handoff after the task loop ends.

**Extraction.** Extraction is delegated to the task prompt itself: the model must summarize what it did, name one key decision, and state one future-facing learning. The code then validates length and defaults, but it does not run a separate judge over the learning or compare it against existing facts (https://github.com/fstech-digital/operational-ontology-framework/blob/a1034dee1a2f24a232238afa5ac878dca95f6549/agent.py).

**Promotion target.** Promotion stays in inspectable symbolic artifacts. `learned` strings become `_facts.md` bullets with date/source/confidence metadata; task-local learnings become `Learned:` annotations in `_spec.md`; session summaries become timestamped handoff files under `handoffs/`. There is no embedding store, database service, or weight update.

**Scope.** Per-project and single-agent. The runner operates over one project directory and does not mine multiple agent runtimes, share facts across projects, or maintain a global playbook.

**Timing.** Online during deployment. Promotion occurs immediately after completed tasks and at the run handoff boundary.

**Survey placement.** OOF adds a lightweight local-runner point between single-session extensions and service-owned trace backends. It owns the execution cycle and artifact schema like a tiny runner, but its trace is much thinner than OpenViking's typed messages or cass-memory's normalized session logs. It reinforces the survey's claim that extraction is easy to make concrete when the target schema is narrow; the open problem remains evaluation, since the promoted learning is accepted from the agent's own self-report.

## Curiosity Pass

**The framework is stronger as an operating discipline than as a retrieval system.** The code does not implement selective Fact Store retrieval, skills loading, git commits, or the README's broader N5 validation framing. That is acceptable for a reference implementation, but the right review reading is "disciplined files around a model call," not "complete production memory layer."

**The self-report oracle is the bottleneck.** OOF's learning loop works if the model's `learned` sentence is actually useful. There is no recurrence check, no human gate, no contradiction detection, and no comparison against task outcome. This is still a useful bootstrap loop, but it should not be mistaken for robust curation.

**Facts can grow without an activation mechanism.** The Facts template warns that a Fact Store that only grows degrades and says to prune regularly (https://github.com/fstech-digital/operational-ontology-framework/blob/a1034dee1a2f24a232238afa5ac878dca95f6549/templates/_facts.md). The code flags stale facts only during consolidation with new facts, and it still loads the full file afterward. That means the long-term pressure is not storage; it is activation and pruning.

**The Skills artifact is currently doctrine, not runtime memory.** `_skills.md` is a thoughtful procedural-memory template, but the runner neither loads nor updates it. That makes Skills a manual extension point rather than an implemented learning target. If the repo later wires task learnings into skill refinement, its trace-derived placement would become more interesting.

**One-task-one-commit remains an operator convention.** The README's auditability story depends on git history, but `agent.py` does not stage or commit. That may be the right design - committing is environment-sensitive - but the repo should be read as providing commit-friendly artifacts, not as enforcing audit discipline itself.

## What to Watch

- Whether `_skills.md` becomes part of boot and write-back, turning procedural memory from a template into an active promotion target.
- Whether Fact Store retrieval gains selection, ranking, or section-level loading before the full-file strategy becomes noisy.
- Whether git commit discipline gets implemented, delegated to hooks, or remains a human/operator convention.
- Whether stale fact handling grows from a passive marker into a review workflow with retirement or contradiction handling.
- Whether the repo publishes empirical metrics for boot failure rate and handoff recovery time, which the README currently marks as pending.
- Whether the broader off-repo framework stays aligned with the code, or the code remains a compact demonstration of only the core artifact cycle.

---

Relevant Notes:

- [files-not-database](../../notes/files-not-database.md) - converges: OOF independently applies the files-first bet to operational agent memory, with git-friendly markdown as the primary substrate.
- [session-history-should-not-be-the-default-next-context](../../notes/session-history-should-not-be-the-default-next-context.md) - exemplifies: OOF's handoff is a compressed continuation artifact rather than raw transcript inheritance.
- [agent-memory-is-a-crosscutting-concern-not-a-separable-niche](../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) - exemplifies: OOF splits storage, activation, and learning visibly; storage is simple, activation is thin, and learning depends on a weak self-report oracle.
- [knowledge-storage-does-not-imply-contextual-activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - tension: OOF stores Facts but currently relies on whole-file prompt loading rather than a cueing or selection system to activate the right fact.
- [trace-derived-learning-techniques-in-related-systems](../trace-derived-learning-techniques-in-related-systems.md) - extends: OOF adds a local filesystem-runner case where task-output learnings promote directly into markdown facts and handoffs.
