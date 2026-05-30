---
description: "Repo-native document research app with file-only KB publication, canonical ask ownership, provenance traces, admissibility gates, and promoted interaction memories"
type: ../types/agent-memory-system-review.md
tags: [trace-derived]
status: current
last-checked: "2026-05-16"
---

# DocMason

DocMason is JetXu-LLM's repo-native document research app for private work files. The system treats the repository as the application surface: users place files in `original_doc/`, a Python CLI stages and validates a local evidence-first knowledge base, and supported host agents such as Codex or Claude Code answer through a governed canonical `ask` front door. The distinctive memory-system design is not "chat over documents" but a set of separated retained surfaces: raw source documents, staged compiler output, published knowledge bundles, retrieval and provenance traces, runtime front-door state, interaction-derived memories, and admissibility policy artifacts.

**Repository:** https://github.com/JetXu-LLM/DocMason

**Reviewed revision:** [9eebe64674de8a0fec2cf0ad4b725e77b7e8df98](https://github.com/JetXu-LLM/DocMason/commit/9eebe64674de8a0fec2cf0ad4b725e77b7e8df98)

## Core Ideas

**The repo is the app and the filesystem is the storage substrate.** The public architecture names `original_doc/` as the private source boundary, `knowledge_base/staging/` as the working area, `knowledge_base/current/` as the published read surface, and `runtime/` as the execution, review, and audit state ([`docs/architecture/README.md`](https://github.com/JetXu-LLM/DocMason/blob/9eebe64674de8a0fec2cf0ad4b725e77b7e8df98/docs/architecture/README.md)). The same boundaries are encoded in `WorkspacePaths`: source, staging, current, publish ledger, query sessions, retrieval traces, answers, agent work, control plane, and interaction ingest are all repository-local paths ([`src/docmason/project.py`](https://github.com/JetXu-LLM/DocMason/blob/9eebe64674de8a0fec2cf0ad4b725e77b7e8df98/src/docmason/project.py)). This makes retained state inspectable and git-friendly, but it also means correctness depends on path contracts and validation rather than a database schema.

**Original, staging, and current are authority boundaries, not convenience folders.** The agent contract explicitly says ordinary answers must not treat `original_doc/`, `knowledge_base/staging/`, or half-published work areas as equivalent truth ([`AGENTS.md`](https://github.com/JetXu-LLM/DocMason/blob/9eebe64674de8a0fec2cf0ad4b725e77b7e8df98/AGENTS.md)). Sync stages source documents, validates the generated KB, then publishes only successful builds to the current surface; it can also stop at action-required, pending synthesis, or blocking validation states ([`src/docmason/commands.py`](https://github.com/JetXu-LLM/DocMason/blob/9eebe64674de8a0fec2cf0ad4b725e77b7e8df98/src/docmason/commands.py)). The versioning layer records a single-current publish model with hidden published roots and a compact publish ledger ([`src/docmason/versioning.py`](https://github.com/JetXu-LLM/DocMason/blob/9eebe64674de8a0fec2cf0ad4b725e77b7e8df98/src/docmason/versioning.py)). Raw documents are source evidence; staged artifacts are rebuildable compiler output; current artifacts are the published knowledge-artifact surface an ordinary answer is allowed to rely on.

**Evidence is compiled into channel-aware manifests and retrieval records.** Source compilation creates source manifests, evidence manifests, unit structures, render assets, artifact indexes, derived affordances, and specialized PDF/Office sidecars. Retrieval artifacts then flatten these into source, unit, and artifact records with text, render, structure, notes, media channels, confidence, document context, semantic overlay labels, and trust priors ([`src/docmason/retrieval.py`](https://github.com/JetXu-LLM/DocMason/blob/9eebe64674de8a0fec2cf0ad4b725e77b7e8df98/src/docmason/retrieval.py), [`src/docmason/affordances.py`](https://github.com/JetXu-LLM/DocMason/blob/9eebe64674de8a0fec2cf0ad4b725e77b7e8df98/src/docmason/affordances.py)). The representational form is mixed: prose summaries and extracted text, symbolic JSON manifests, deterministic path/fingerprint metadata, rendered media references, and optional semantic overlay sidecars. These are knowledge artifacts when used as evidence and routing input; validation rules and source-scope policies become system-definition artifacts when they gate answer behavior.

**Canonical ask is the ordinary front door, with runtime ownership.** `AGENTS.md` makes canonical `ask` the only ordinary natural-language front door, while operator workflows such as sync, status, trace, and runtime-log review remain separate ([`AGENTS.md`](https://github.com/JetXu-LLM/DocMason/blob/9eebe64674de8a0fec2cf0ad4b725e77b7e8df98/AGENTS.md)). The implementation persists front-door state, host identity, conversation turns, run IDs, support basis, source-scope policy, trace IDs, selected artifacts, and admissibility repair fields ([`src/docmason/conversation.py`](https://github.com/JetXu-LLM/DocMason/blob/9eebe64674de8a0fec2cf0ad4b725e77b7e8df98/src/docmason/conversation.py), [`src/docmason/host_integration.py`](https://github.com/JetXu-LLM/DocMason/blob/9eebe64674de8a0fec2cf0ad4b725e77b7e8df98/src/docmason/host_integration.py)). That runtime state is a system-definition artifact family: it instructs which run owns a turn, which evidence basis is legal, and whether finalization may cross the commit barrier.

**Retrieval and provenance traces are first-class runtime artifacts.** `retrieve` logs query sessions under `runtime/logs/query-sessions/`, while `trace` logs answer/source provenance under `runtime/logs/retrieval-traces/` and updates a per-turn artifact index only when canonical binding is valid ([`src/docmason/retrieval.py`](https://github.com/JetXu-LLM/DocMason/blob/9eebe64674de8a0fec2cf0ad4b725e77b7e8df98/src/docmason/retrieval.py), [`src/docmason/runtime_log_index.py`](https://github.com/JetXu-LLM/DocMason/blob/9eebe64674de8a0fec2cf0ad4b725e77b7e8df98/src/docmason/runtime_log_index.py)). Trace artifacts map answers back to source, unit, artifact, relation, and knowledge-consumer records. They are derived knowledge artifacts for audit and answer support, but the binding validator gives them system-definition force when it demotes invalid logs or blocks post-commit canonical writes.

**Admissibility gates enforce answer honesty at the commit barrier.** `evaluate_commit_admissibility` checks active run ownership, attached shared-job settlement, trace/run version truth, governed multimodal refresh settlement, source-scope satisfaction, support manifests, illegal work-area citations, absolute machine paths, mixed-support explanation, and trace answer-state mismatch ([`src/docmason/admissibility.py`](https://github.com/JetXu-LLM/DocMason/blob/9eebe64674de8a0fec2cf0ad4b725e77b7e8df98/src/docmason/admissibility.py)). The source-scope policy builder separately distinguishes global, source-scoped soft, source-scoped hard, and compare modes, with target-source requirements and pending-interaction allowances ([`src/docmason/truth_boundary.py`](https://github.com/JetXu-LLM/DocMason/blob/9eebe64674de8a0fec2cf0ad4b725e77b7e8df98/src/docmason/truth_boundary.py)). This is stronger than ordinary RAG provenance: policy artifacts can prevent an answer from being returned even when retrieval found plausible text.

**Interaction memory is a staged promotion path from host traces into the published KB.** Claude Code hooks mirror session, prompt, tool-use, and stop events into `runtime/interaction-ingest/claude-code/` ([`src/docmason/hooks.py`](https://github.com/JetXu-LLM/DocMason/blob/9eebe64674de8a0fec2cf0ad4b725e77b7e8df98/src/docmason/hooks.py)). Codex and Claude native transcripts can be reconciled into native ledgers, pending interaction entries, attachments, relation hints, semantic classifications, and runtime overlays ([`src/docmason/interaction.py`](https://github.com/JetXu-LLM/DocMason/blob/9eebe64674de8a0fec2cf0ad4b725e77b7e8df98/src/docmason/interaction.py)). During sync, pending entries are grouped into `interaction-memory-*` directories with `source_manifest.json`, `evidence_manifest.json`, `interaction_context.json`, extracted turn text, copied attachments, `knowledge.json`, and `summary.md`, then loaded into the same retrieval/trace context family as corpus documents. That makes interaction memories trace-derived knowledge artifacts with ranking influence, not just logs.

## Comparison with Our System

| Dimension | DocMason | Commonplace |
|---|---|---|
| Primary purpose | Local document research app with governed answers over private files | Methodology KB and tooling for agent-operated knowledge bases |
| Storage substrate | Repo-local files: source docs, generated KB JSON/Markdown/media, runtime logs, control-plane records, adapters | Repo-local Markdown/YAML, Python CLI, schemas, indexes, review records, generated reports |
| Main retained surfaces | `original_doc/`, `knowledge_base/staging/`, `knowledge_base/current/`, `runtime/`, `skills/canonical/`, `adapters/` | Typed notes, collection contracts, instructions, skills, sources, reviews, validation reports, indexes |
| Authority model | Canonical ask, publish state, support contracts, source-scope policy, admissibility gates, host wrappers | Artifact type, collection contracts, AGENTS instructions, CLI validation, review gates, skills |
| Retrieval model | Deterministic lexical-plus-graph retrieval over source/unit/artifact records and interaction memories | Agent navigation with `rg`, authored links, indexes, connect reports, and validation output |
| Provenance model | Trace artifacts from answers to source/unit/artifact/consumer records plus runtime query logs | Source snapshots, citations, backlinks, git history, review notes, generated indexes |
| Trace-derived learning | Host interaction traces can become promoted interaction memories with retrieval-rank semantics | Review traces and operator experience are mostly manually promoted into notes/instructions/skills |
| Codification path | Strong gates and CLI code around answer legality; generated adapters translate host contracts | Stronger typed note/instruction/review conventions; less app-specific answer runtime |

DocMason is closest to commonplace on artifact-contract discipline. Both systems use the repo as the durable substrate, make generated views subordinate to source truth, and care about behavioral authority. DocMason pushes further on answer-time runtime governance: the canonical ask front door, run ownership, support contracts, source-scope policies, trace logging, and admissibility checks form a much tighter execution envelope than commonplace's ordinary note-writing workflows.

Commonplace is stronger as a general methodology library. Its notes, type specs, link vocabulary, and reviews are designed to accumulate transferable claims across projects. DocMason is application-shaped: its artifact contracts are excellent for document QA, but many categories are bound to user-facing answer safety over Office/PDF/Text corpora. Borrowing should preserve the mechanisms, not the product-specific folder names.

The most interesting divergence is promotion. Commonplace usually promotes from workshop experience into notes or instructions through human/agent review. DocMason has a concrete trace-to-memory pipeline: host conversation traces become pending runtime overlays, then published interaction memories that retrieval can rank and answer-time policy can consider. The tradeoff is that DocMason's promoted interaction memories are still evidence/context surfaces, not validated instructions or skills.

**Read-back:** push — canonical `ask` retrieves evidence and interaction memories into the governed answer path.

## Borrowable Ideas

**Treat original, staging, and current as explicit authority states.** Ready to borrow. Commonplace already separates sources, notes, generated indexes, and work areas; DocMason's strict "staging is not reader-facing truth" language would sharpen sync and review workflows that produce temporary generated artifacts.

**Persist support contracts next to runtime answer state.** Ready to borrow for review and fix workflows. A commonplace review run could record expected support basis, target scope, repairable gaps, and final fulfillment separately from the written review, making later validation less dependent on prose interpretation.

**Demote invalid runtime logs instead of silently accepting them.** Ready to borrow. DocMason's canonical log sanitizer keeps audit records but strips invalid canonical binding when the run/turn/front-door relationship no longer holds. Commonplace's review and agent-run logs could use the same pattern when stale traces should remain inspectable without retaining authority.

**Use evidence channels as retrieval contracts.** Ready to borrow selectively. Text/render/structure/notes/media channel descriptors make a query aware of which evidence form is actually available. In commonplace, a lighter version could distinguish source snapshots, code citations, local validation output, and review traces.

**Promote interaction memories through sync, not immediately.** Ready to borrow with stricter curation. DocMason's pending overlay lets interaction-derived material be visible while still awaiting promotion. Commonplace could apply this to workshop observations: pending context may advise a current task, but durable KB promotion should happen through a validation or review step.

**Do not borrow answer-runtime complexity wholesale.** Needs a document-app use case. The canonical ask/control-plane/admissibility stack is appropriate for user-facing document answers. Commonplace should borrow the contract pattern where review gates need it, not turn every note edit into a front-door run.

## Trace-derived learning placement

**Trace source.** DocMason qualifies as trace-derived learning. Raw traces include Claude Code hook mirrors for session, prompt, tool-use, and stop events; Codex or Claude native transcript reconciliation; canonical ask turn state; query-session logs; retrieval-trace logs; and answer files associated with conversation turns.

**Extraction.** Hook payloads are appended as JSONL mirror records. Native transcript reconciliation audits tool use, extracts DocMason command usage, consulted source IDs, direct KB/source access, render inspection, attachments, continuation type, relation hints, semantic profile, and assistant excerpts. Deterministic classifiers infer memory kind, durability, answer-use policy, and retrieval rank prior. Sync then groups pending entries by conversation into promoted interaction-memory directories.

**Storage substrate.** Raw and semi-raw traces live under `runtime/state/native-ledger/`, `runtime/interaction-ingest/`, `runtime/logs/query-sessions/`, `runtime/logs/retrieval-traces/`, `runtime/logs/turn-artifact-index/`, `runtime/runs/`, and `runtime/answers/`. Pending interaction overlays live under runtime interaction-ingest projection files. Distilled interaction memories are published into `knowledge_base/{staging,current}/interaction/memories/interaction-memory-*`.

**Representational form.** Raw traces are mixed JSON/prose/tool-call records plus optional attachment bytes. Pending overlays are symbolic JSON retrieval records with prose excerpts. Promoted memories are mixed retained artifacts: prose summaries and extracted turn text, symbolic source/evidence manifests, JSON interaction context, copied media, semantic metadata, and ranking policy fields. No inspected implementation trains weights or stores learned model parameters as the operative learned state.

**Lineage.** Interaction entries preserve conversation ID, turn ID, native turn ID, native ledger ID, interaction IDs, related source IDs, entry fingerprints, attachment hashes, and promotion metadata. Promoted memories keep interaction IDs, conversation IDs, input digests, source fingerprints, related-source relations, and generated manifests. Lineage is good at turn and file level; it is not a span-level derivation from transcript text into each summary sentence.

**Behavioral authority.** Raw runtime logs and native ledgers are knowledge artifacts for audit, reconciliation, and troubleshooting. Pending interaction overlays are advisory knowledge artifacts with constrained retrieval participation. Promoted interaction memories become stronger knowledge artifacts because they enter the published retrieval/trace surface with memory semantics and rank priors. They do not become system-definition artifacts by themselves unless future code consumes them as instructions, enforcement rules, or configuration. Canonical ask contracts, source-scope policy, runtime ownership records, and admissibility checks are system-definition artifacts because they route, validate, and block answer finalization.

**Scope and timing.** Scope is per local DocMason workspace and per host conversation, with relation edges back to corpus source IDs. Timing is staged: capture and reconciliation happen during or after host interaction; pending overlays can influence later asks before sync; durable promotion happens at sync/publication time.

**Survey placement.** On the [trace-derived survey](../trace-derived-learning-techniques-in-related-systems.md), DocMason belongs in the file-native interaction-trace-to-retrieval-memory family. It strengthens the survey's split between raw trace evidence and promoted retained artifacts, and it adds a useful authority distinction: trace-derived memories may affect retrieval ranking and context, while separate policy artifacts govern whether an answer is legally admissible.

## Curiosity Pass

- DocMason's most reusable idea is the authority separation, not the document parsers. `original_doc/`, staging, current, runtime logs, control-plane state, and interaction memories each have different truth status.
- The system is deliberately local and file-only, but it is not simple. Many guarantees that a database product might centralize are distributed across path contracts, JSON schemas, validators, runtime ownership checks, and host wrappers.
- Interaction memory is conservative in an important way: promoted memories influence evidence retrieval, but the inspected code does not let user corrections automatically rewrite canonical source documents or agent instructions.
- The implementation has strong answer gates, but the final answer still depends on the host agent performing the reasoning. DocMason can provide evidence, traces, and admissibility checks; it does not replace model judgment with a deterministic answer generator.
- The docs describe the app as natural-language first, while the code reveals a large hidden machinery layer. That is a reasonable product choice, but maintainers need to keep the hidden contracts from becoming too hard for agents to debug.

## What to Watch

- Whether interaction memories gain explicit review states, retirement policies, or promotion grades beyond pending/promoted.
- Whether semantic overlays remain additive sidecars or become a larger human/agent-authored knowledge layer with its own validation contract.
- Whether source-scope and admissibility policies become easier to express declaratively instead of being spread across Python helpers.
- Whether promoted interaction memories ever gain instruction or enforcement authority, which would change their classification from knowledge artifacts toward system-definition artifacts.
- Whether generated host adapters remain translations of canonical repository contracts or drift into parallel truth surfaces.

---

Relevant Notes:

- [Retained artifact](../../notes/definitions/retained-artifact.md) - defined-in: DocMason keeps behavior-shaping state across published KB artifacts, runtime turns, support contracts, traces, and interaction memories.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - defined-in: published source/unit/artifact records, provenance traces, and interaction memories primarily advise or evidence later answers.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - defined-in: canonical ask contracts, admissibility gates, source-scope policy, validation rules, and host wrappers instruct, route, or enforce behavior.
- [Behavioral authority](../../notes/definitions/behavioral-authority.md) - defined-in: DocMason separates evidence surfaces from gating and finalization surfaces.
- [Lineage](../../notes/definitions/lineage.md) - defined-in: source fingerprints, publish ledger records, trace IDs, interaction IDs, and input digests determine invalidation and audit paths.
- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - source-inspected placement: host interaction traces can become published interaction memories with retrieval influence.
- [A functioning KB needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) - compares-with: DocMason's runtime and staging layers keep temporal work out of the published knowledge surface until sync.
