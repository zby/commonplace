---
description: "RIPA separates persistent agent state from execution bindings and demonstrates bounded checkpoint continuity, while leaving behavioral fidelity and cross-host authority conditional."
source: https://arxiv.org/abs/2609.00546
captured: "2026-09-24"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: db579f816418437c8f49c4a13258628e5cdb10258be6657e99edf2f7b4c9b1e1
ingested: "2026-09-25"
type: ingest-report
domains: [agent-memory, runtime-portability, checkpointing, agent-identity]
---

# Ingest: Runtime-Independent Persistent Agents

## Classification

A systems research paper combining an architectural contract, an Enoch reference implementation, and bounded live migration studies. This observation is arXiv v2, dated 19 September 2026. Authors Zhenyu Zhao and Roy Zhao list independent-researcher and University of Washington affiliations, respectively. They report their own implementation and studies; the affiliations do not provide independent validation of the outcomes.

## Summary

RIPA defines a persistent agent as installed identity, durable memory and workflow state, and a versioned executable body, with models, harnesses, hosts, and interaction surfaces treated as replaceable bindings. Its migration protocol fences the source, checkpoints and validates state, binds target providers, reconstructs context, and authorizes continuation. One operational instance preserves recorded state across host, joint model/harness, and chat-surface substitutions; a separate cross-host task resumes from a verified intermediate artifact. Within the same Enoch architecture, five supervised Codex–Muse–Codex round trips and five matched same-runtime controls complete simple workflows on their first attempts. A separate planned interruption preserves the checkpoint and rejects an old reply before recovery completes. These are demonstrations of mechanical continuity with explicit drivers, fixed body revisions within each migration, and governed authority. They establish neither behavioral equivalence nor the superiority of the identity/memory/body partition over alternative designs.

## Quotes

No source quotes have been retained yet.

## Connections Found

The strongest role is bounded evidence for [active work state being distinct from retrospective memory or chat history](../notes/active-work-state-is-not-retrospective-memory-or-chat-history.md). The cross-host task retains an intermediate artifact, its hash, a next-stage descriptor, and the task ID. A fresh runtime consumes that state to continue unfinished work. Because the model calls are tool-free and an external driver manages the stages, this supports explicit continuation state without validating the note's broader workshop, closure, or evidence-gate recommendations.

The paper also gives a concrete comparison for [separating scheduling, context assembly, and external state](../notes/agent-runtime-analysis-should-separate-scheduling-context-state.md): drivers advance work, fresh sessions receive reconstructed inputs, and durable records preserve progress. This is a mapping between analytical responsibilities, not evidence that either decomposition is uniquely correct. Relative to the [portable context-layer account](./from-harness-lock-in-to-portable-context-layer.ingest.md), RIPA adds an explicit question about who may continue after copying state. Its governed promotion point makes continuation authority a separate portability obligation alongside movable artifacts, access contracts, and execution policy.

## Extractable Value

1. **A checkpoint needs executable continuation information.** The retained artifact, integrity check, stage pointer, and task identity show how a new runtime can resume without reconstructing pending work from conversation. The evidence is one cross-host synthetic task plus supervised round trips within a fixed Enoch design, not a general task-portability result. This supplies a concrete example for the active-work-state note. [quick-win]
2. **Copying state and authorizing a successor are separate operations.** Identical identity and memory records can exist in multiple copies. RIPA therefore requires a governed promotion point and leaves the source fenced. The distinction generalizes beyond its identity terminology, but cross-host exclusivity depends on cooperating executions and trusted custody; local epoch checks do not revoke a detached copy's external credentials. [deep-dive]
3. **Mechanical continuity and behavioral fidelity need separate tests.** Hashes, task lineage, checkpoints, and stale-attempt rejection check preserved state and control. Correct identity recall is a narrower behavioral witness. A useful portability evaluation would retain both kinds of checks while using independent reasoning sessions and tasks with meaningful file or tool effects. The reported controls show that the bounded workflow also completes without migration; they do not isolate the effects of each changed binding. [experiment]

## Limitations (our opinion)

The studies demonstrate feasibility inside one evolving Enoch body lineage. Three frozen body revisions support different evidence groups; their deterministic test totals and live results must not be pooled. The body is held fixed within each migration, and all studies retain the chosen identity/memory/body partition, provider contracts, explicit checkpoint representation, and migration machinery. Same-runtime controls vary migration under that design. They do not compare alternative partitions, checkpoint formats, or memory-only approaches, and there is no ablation establishing which architectural choice causes success. Ordinary durable-workflow mechanisms explain much of the observed task continuity without settling a general theory of agent identity.

External validity is narrow. The operational case carries nonempty private memory but injects no unfinished task or pending external effect; its public record is redacted. The separate cross-host task has an empty long-term-memory fixture and simple tool-free model calls. The Muse study uses explicit drivers and operator-mediated interaction, and its cases share a Muse conversation despite fresh installed roots. Five successful ordinary round trips are not a reliability estimate. The paper provides no controlled behavioral-equivalence, cost, or unattended-operation result, and the observed client identifiers do not independently attest the served model backends. Chat-surface substitution does not demonstrate translating unread-message positions or preserving cross-provider delivery guarantees.

Authority and recovery claims have distinct boundaries. Cross-host promotion is governed by operators rather than distributed consensus. Local stale-process checks do not prove provider-side fencing or exclude detached credentialed copies. The fault is one prescribed interruption before a reply; one completion in that trace does not establish exactly-once external effects. Exception rollback and incomplete-import guards do not establish crash-atomic multi-file conversion. The fault archive needed a supplement of previously recorded files and a read-only verifier adaptation; stale-reply rejection rests on retained stderr rather than a separately captured helper exit record. Those disclosures limit the evidence without nullifying the recorded recovery.

This ingest assesses the paper only. No implementation code or released verifier was inspected or executed, so mechanism descriptions and reported outcomes remain source claims rather than an independent reproduction.

## Recommended Next Action

Update [Active work state is not retrospective memory or chat history](../notes/active-work-state-is-not-retrospective-memory-or-chat-history.md) with the paper's verified-artifact and next-stage checkpoint example, retaining its explicit-driver, tool-free-task, and bounded-migration qualifications.
