---
description: "Practitioner architecture makes a governed repository the durable project substrate beneath replaceable models, sessions, roles, and interfaces"
source: https://x.com/yoheinakajima/status/2085784422339768686
captured: "2026-08-10T10:52:37.315669+00:00"
capture: xdk
genre: practitioner-report
snapshot_sha256: 04805b533168881ab7a6d15cec499b0b397faa32e43be258b76d7c107350f074
status_id: 2085784422339768686
conversation_id: 2085784422339768686
post_count: 6
ingested: "2026-08-10"
type: kb/sources/types/ingest-report.md
domains: [agent-architecture, context-engineering, agent-memory, orchestration]
---

# Ingest: Building a Repo-Centric Modular Agent Stack

## Classification

Yohei Nakajima describes the modular architecture he says he currently uses for agentic projects and relates it to ActiveGraph, an approach he says he previously developed.
Author: @yoheinakajima is the designer reporting his own operating model. That gives the account direct authority for its design intent and practitioner vocabulary, but not independent evidence that the architecture improves reliability, substitution cost, or long-horizon performance.

## Summary

The report proposes that a governed project repository, rather than a model, agent, conversation, or IDE session, should be the durable unit of agentic work. The repository holds canonical events and artifacts plus regenerable projections; compact instruction files route into stable invariants, reusable role procedures, project-local contracts, and transient task context; replaceable models enter through thin adapters; and bounded heartbeats reconcile state, act, verify, record a state delta, and exit. Local project managers coordinate detailed work while a portfolio-level Chief of Staff routes attention without becoming a second system of record. Verification, provenance, explicit epistemic status, and durable human decisions govern which transitions become accepted project state. The report's main value is this integrated architecture and its vocabulary, not demonstrated effectiveness.

## Connections Found

The source is a strong practitioner convergence case for [session history should not be the default next context](../notes/session-history-should-not-be-the-default-next-context.md) and [active work state is not retrospective memory or chat history](../notes/active-work-state-is-not-retrospective-memory-or-chat-history.md): it treats conversation as temporary scaffolding and makes current objectives, blockers, evidence, approvals, decisions, and next actions the cross-session handoff. Its canonical-record/derived-projection split also instantiates [Keep Lineage And Compiled Views From Drifting](../notes/agent-memory-requirements/keep-compiled-views-aligned.md), while its compact root file and layered instruction stack instantiate [AGENTS.md should be organized as a control plane](../notes/agents-md-should-be-organized-as-a-control-plane.md).

At the runtime level, repository state, instruction/context layers, and heartbeat coordination independently support [Agent runtimes decompose into scheduler context engine and execution substrate](../notes/agent-runtime-analysis-should-separate-scheduling-context-state.md). [Echel](../agent-memory-systems/reviews/echel.md) is the closest inspected implementation: it combines project-owned Markdown, deterministic graph projections, task-scoped packets, evidence gates, and an operator surface. [The log is the agent](./the-log-is-the-agent-2065129901427130678.ingest.md) supplies the sharpest contrast: both make executors replaceable over canonical state and treat loaded context as a projection, but this report chooses the governed project rather than an exhaustive session log as the durable unit. [The GitHub for Context Doesn't Exist Yet](./the-github-for-context-doesn-t-exist-yet-2077772169455530152.ingest.md) adds the cross-project governance, dependency, security, and ownership problems that this repository-local architecture leaves mostly implicit.

## Extractable Value

1. **The project, not the executor, is the durable unit.** Externalizing current work, decisions, evidence, authority, procedures, and acceptance conditions into a project-owned environment makes model, session, interface, and individual-agent replacement an adapter problem. This is the source's highest-reach synthesis, but its sufficiency conditions need to be derived across multiple implementations rather than accepted from this account alone. [deep-dive]

2. **Continuation should optimize for reconstructable operational state, not exhaustive conversational memory.** A fresh capable agent needs enough structured clues to determine what is live, what changed, what remains blocked, and what counts as completion. Preserving every token is neither necessary nor sufficient. This directly sharpens the session-history and active-work-state notes. [quick-win]

3. **Canonical state and prepared context have different authority.** Dashboards, summaries, queues, indexes, briefs, and agent context packages may be useful while stale or incomplete; they remain safe only when treated as traceable projections that can be regenerated, compared, or challenged against a more durable record. [quick-win]

4. **Executor substitution requires externalized procedure as well as externalized memory.** A shared repository does not make two models interchangeable if each still carries private role behavior or policy. Reusable role contracts plus thin interface adapters are the proposed second half of portability. This is plausible and testable, but the source reports no substitution trial. [experiment]

5. **A bounded heartbeat is a compact control-loop pattern.** Reconcile state, select bounded work, act, verify, record the result, and exit; continuity stays in project state rather than in a long-lived model context. This is a useful implementation pattern, though the missing captured diagrams and lack of operational code leave its exact transition contract unspecified. [just-a-reference]

6. **Human judgment can be control state rather than memory transport.** Objectives, priorities, ambiguity resolutions, approvals, and changes of direction become durable records so they affect later work without a human repeatedly briefing each new executor. The distinction is useful, but the report does not specify conflict resolution, expiry, or authority precedence. [quick-win]

7. **Generation and acceptance are separate state-transition operations.** Schemas, tests, validators, reproduction, and structured review can keep a generator from self-certifying consequential changes, especially changes to its own instructions or orchestration. The source provides design convergence, not evidence that any particular verifier is adequate. [just-a-reference]

## Limitations (our opinion)

This is a broad first-person architecture essay, not a code-grounded system description or comparative evaluation. It provides no repository, schemas, example state records, task corpus, success rates, costs, latency, scale limits, failed deployments, or before/after comparison. Many interventions are bundled -- repository persistence, event lineage, layered instructions, role separation, bounded execution, hierarchical coordination, independent verification, epistemic labels, and durable human decisions -- so the account cannot identify which parts are necessary or whether their governance cost exceeds their continuation benefit.

The central substitutability claim is therefore a design hypothesis. The report does not demonstrate that a fresh agent can reconstruct state reliably, that two different models interpret the same role contract consistently, or that the Chief-of-Staff/project-manager split prevents context loss or coordination failure. A repository can preserve inspectable state while still failing to select the right state for a call, resolve contradictory records, retire stale policy, or keep generated projections synchronized.

The capture is also incomplete at several load-bearing points. Passages introducing the conventional/current architecture, reconstruction test, canonical graph relations, instruction stack, role contract, heartbeat, hierarchy, portfolio view, verification pattern, epistemic states, human interface, state delta, and compounding loop are followed by blank space, apparently where structured lists or diagrams occurred in the original X article. The surrounding prose supports the high-level analysis, but exact field sets and transition diagrams should not be inferred from this snapshot.

Finally, the ActiveGraph framing may privilege event history, lineage, and projection mechanics because those are the author's existing design vocabulary. Git and structured records provide an inspectable substrate, but they do not by themselves establish semantic dependency, authorization, verification quality, or correct context selection. The report names those obligations without showing their implementation.

## Recommended Next Action

Write one structured-claim note, **“Externalized project state and role contracts make execution components replaceable,”** using this report together with [The GitHub for Context Doesn't Exist Yet](./the-github-for-context-doesn-t-exist-yet-2077772169455530152.ingest.md), [Effective harnesses for long-running agents](./effective-harnesses-for-long-running-agents.ingest.md), and [Echel](../agent-memory-systems/reviews/echel.md). Scope the claim to project-shaped work and make reconstructable current state, explicit authority, provenance, context selection, and independent verification necessary conditions rather than treating repository storage alone as sufficient.
