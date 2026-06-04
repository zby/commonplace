---
description: "llm-wiki-coordination review: Markdown wiki protocol layer for dialogue threads, RoleSpace peer evaluation, consensus frontmatter, and structural audit"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: outdated
last-checked: "2026-06-03"
tags: []
---

# llm-wiki-coordination

> Replaced 2026-06-04. See [llm-wiki-coordination](./llm-wiki-coordination.md) for the current review.

llm-wiki-coordination, from AEVYRA's `AEVYRA/llm-wiki-coordination` repository, is a documentation-first coordination layer for multi-agent work in Markdown or Obsidian-style wikis. At the reviewed commit it is not an autonomous agent runtime, scheduler, RAG service, or memory database. Its behavior-shaping surface is a set of Markdown protocols for dialogue threads, RoleSpace peer evaluation, multi-agent consensus, integrity audit, and persona/anchor-form ontology, plus one Python audit script that checks a downstream `wiki/` tree for protocol and graph invariants.

**Repository:** https://github.com/AEVYRA/llm-wiki-coordination

**Reviewed commit:** [126749634d1c8c2fd6141f59711c882c2d629699](https://github.com/AEVYRA/llm-wiki-coordination/commit/126749634d1c8c2fd6141f59711c882c2d629699)

**Last checked:** 2026-06-03

## Core Ideas

**The package is protocol-first, not runtime-first.** The README says the system is "a file-and-protocol layer, not an agent runtime" and the installation path is to copy or adapt files from `protocols/` and `tools/` into a downstream wiki ([README.md](https://github.com/AEVYRA/llm-wiki-coordination/blob/126749634d1c8c2fd6141f59711c882c2d629699/README.md)). There is no package manifest, no server, no model adapter, and no agent loop in this checkout; the only executable implementation is `tools/llm-wiki-audit.py` ([tools/llm-wiki-audit.py](https://github.com/AEVYRA/llm-wiki-coordination/blob/126749634d1c8c2fd6141f59711c882c2d629699/tools/llm-wiki-audit.py)).

**Dialogue memory is append-only by directory structure.** The dialogue protocol defines a thread as `thread.md`, `meta.yaml`, and numbered `entries/*.md`; each contribution is a new file, not an edit to someone else's text ([protocols/dialogue-thread-format.md](https://github.com/AEVYRA/llm-wiki-coordination/blob/126749634d1c8c2fd6141f59711c882c2d629699/protocols/dialogue-thread-format.md)). That gives the system a simple lineage boundary: prior contributions are preserved as source traces, while later entries can evaluate or close them without overwriting them.

**RoleSpace turns peer review into a lightweight symbolic signal.** Contributions are scored on Novelty, Coherence, and Robustness; each entry after the first records `last_eval` for the previous entry, and closure records `current_at_close` against a target vector ([protocols/rolespace-coordination.md](https://github.com/AEVYRA/llm-wiki-coordination/blob/126749634d1c8c2fd6141f59711c882c2d629699/protocols/rolespace-coordination.md), [protocols/dialogue-thread-format.md](https://github.com/AEVYRA/llm-wiki-coordination/blob/126749634d1c8c2fd6141f59711c882c2d629699/protocols/dialogue-thread-format.md)). This is not an embedding or learned ranker. It is a compact, human-readable control signal that tells the next agent which deficit a thread still has.

**Consensus and lifecycle are separate wiki authorities.** The consensus protocol uses frontmatter `consensus:` entries, revision markers, statuses such as `pending`, `accepted`, `contributed`, `disputed`, `stale`, and `dormant`, and a separate `lifecycle:` axis for content maturity ([protocols/multi-ai-consensus.md](https://github.com/AEVYRA/llm-wiki-coordination/blob/126749634d1c8c2fd6141f59711c882c2d629699/protocols/multi-ai-consensus.md)). The audit script checks only a narrow subset of this: missing consensus on structural pages, accepted lifecycle with pending consensus, and accepted lifecycle without consensus ([tools/llm-wiki-audit.py](https://github.com/AEVYRA/llm-wiki-coordination/blob/126749634d1c8c2fd6141f59711c882c2d629699/tools/llm-wiki-audit.py)).

**Context efficiency comes from protocolized indirection, not automated retrieval.** Long-running dialogue history is split into stable thread context, metadata, and individual entries so an agent can inspect just the thread head, current metadata, or latest entries instead of reloading one growing transcript ([protocols/dialogue-thread-format.md](https://github.com/AEVYRA/llm-wiki-coordination/blob/126749634d1c8c2fd6141f59711c882c2d629699/protocols/dialogue-thread-format.md)). The audit script also narrows inspection to Markdown files under `wiki/` and protocol-specific paths. There is no implemented top-k retrieval, token budgeter, or semantic index; context selection remains a human/agent workflow.

**The audit script codifies only the lower protocol layers.** The integrity-audit protocol describes L0-L5, but the Python script implements L0 hygiene, L1 graph checks, L2 dialogue/consensus/crypto checks, and optional L3 cross-protocol checks ([protocols/integrity-audit.md](https://github.com/AEVYRA/llm-wiki-coordination/blob/126749634d1c8c2fd6141f59711c882c2d629699/protocols/integrity-audit.md), [tools/llm-wiki-audit.py](https://github.com/AEVYRA/llm-wiki-coordination/blob/126749634d1c8c2fd6141f59711c882c2d629699/tools/llm-wiki-audit.py)). The README explicitly leaves L4-L5 semantic and portability review to a human or AI auditor ([README.md](https://github.com/AEVYRA/llm-wiki-coordination/blob/126749634d1c8c2fd6141f59711c882c2d629699/README.md)).

## Artifact analysis

- **Storage substrate:** `repo` — The standing system artifacts are repository files: Markdown protocol specs, a concept note, README/AGENTS guidance, changelog, and a Python audit script; downstream memory lives in copied wiki files, not in this repository's own runtime store.
- **Representational form:** `prose` `symbolic` — Prose protocols carry most of the authority, while YAML/frontmatter shapes, dialogue-entry schemas, N/C/R vectors, lifecycle/consensus fields, and the Python audit rules give selected parts symbolic consequences.
- **Lineage:** `authored` `imported` `trace-extracted` — Protocol docs and audit rules are authored from the source workflow, copied/adapted into downstream wikis as imports, and downstream dialogue entries accumulate as agent-authored traces that can be closed or crystallized.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `learning` — Dialogue entries begin as source-trace knowledge; protocols instruct agents; consensus/lifecycle and hard audit findings can gate workflow; RoleSpace vectors route later contributions; the audit script validates structure; crystallization turns traces into canon.

**Protocol Markdown files.** Storage substrate: repo files under `protocols/` and `concepts/`. Representational form: prose with embedded symbolic schemas, examples, state names, and invariants. Lineage: authored extraction from a private wiki workflow, then revised in v0.2.0 according to the changelog ([CHANGELOG.md](https://github.com/AEVYRA/llm-wiki-coordination/blob/126749634d1c8c2fd6141f59711c882c2d629699/CHANGELOG.md)). Behavioral authority: system-definition artifacts when copied into a downstream wiki's workflow layer; they instruct agents how to write entries, evaluate previous contributions, use consensus blocks, and audit the graph.

**Dialogue thread directories in a downstream wiki.** Storage substrate: downstream repo/files under a dialogue root such as `wiki/agents/dialogue/`. Representational form: mixed, with prose entries plus symbolic YAML fields (`n`, `type`, `author`, `last_eval`, `current_at_close`, `status`, participants, RoleSpace targets). Lineage: agent-authored traces accumulated as append-only entries; closure and crystallization are derived from previous entries and user recognition. Behavioral authority: source-trace knowledge artifacts while discussion is ongoing; candidate system-definition artifacts when a closure proposes canon pages or a crystallized output becomes accepted wiki knowledge.

**RoleSpace vectors and `last_eval`.** Storage substrate: frontmatter inside downstream entry files and `meta.yaml`. Representational form: symbolic numeric vector plus prose rationale in the entry body. Lineage: peer-evaluated from the immediately previous contribution, not self-scored. Behavioral authority: routing and evaluation authority for the next participant because the vector identifies thread deficits and closure readiness. Effective scoring quality is not verifiable from static source.

**Consensus blocks.** Storage substrate: downstream Markdown frontmatter. Representational form: symbolic mapping from agent id to status/revision string. Lineage: authored by participating agents after review in the same session, with stale invalidation rules described in the protocol ([protocols/multi-ai-consensus.md](https://github.com/AEVYRA/llm-wiki-coordination/blob/126749634d1c8c2fd6141f59711c882c2d629699/protocols/multi-ai-consensus.md)). Behavioral authority: governance system-definition artifact; it gates or qualifies lifecycle claims but does not by itself retrieve memory into an agent's context.

**Integrity audit script.** Storage substrate: `tools/llm-wiki-audit.py`. Representational form: symbolic Python checks over filesystem paths, regexes, YAML parsing, link indexes, dialogue schemas, consensus fields, and hard/warn/info findings. Lineage: authored implementation of selected audit invariants; it is invalidated when protocol semantics or downstream wiki layout changes. Behavioral authority: validation authority when run by a maintainer or agent; hard findings can block workflow by exit code, while semantic L4-L5 findings are outside the script.

**Persona Manifest ontology.** Storage substrate: `concepts/persona-manifest-ontology.md`. Representational form: prose ontology with some normative boundaries, especially around anchor forms, recognition, and private-key claims. Lineage: authored conceptual model. Behavioral authority: interpretive system-definition artifact for projects that use persistent AI personae; it informs how agents talk about identity, continuity, recognition, and signatures, but has no executable enforcement except the audit script's narrow crypto-claim check.

**Promotion path.** The intended path is discussion -> structured entries -> peer review -> closure/crystallization -> canon/consensus -> audit. That is a real authority ladder in the protocol design, but only part of it is executable here. The repository provides structure and lower-layer checks; actual crystallization, semantic review, and wiki read-back depend on the downstream project and its agents.

## Comparison with Our System

| Dimension | llm-wiki-coordination | Commonplace |
|---|---|---|
| Primary purpose | Drop-in protocol layer for multi-agent Markdown wiki coordination | Git-native methodology KB with typed artifacts, validation, reviews, source snapshots, and generated indexes |
| Main retained artifact | Protocol docs, dialogue entries, consensus frontmatter, RoleSpace vectors, audit findings | Typed Markdown notes, instructions, reviews, ADRs, reports, indexes, and validation outputs |
| Context strategy | Split dialogue into directories and entries; agents pull the relevant protocol/thread pieces | Search, indexes, links, collection contracts, type specs, skills, reports, and validation/review commands |
| Governance | Consensus blocks, lifecycle states, peer-evaluation vectors, hard/warn/info audit findings | Collection contracts, schemas, deterministic validation, semantic gates, review archives, git history |
| Learning loop | Manual/staged trace-to-canon protocol from dialogue entries to crystallized knowledge | Deliberate source-grounded writing, workshop/library promotion, validation, review, and curated indexes |
| Automation boundary | One generic audit script for lower-layer structure | Multiple installed commands for validation, indexing, snapshots, review bundles, gates, and note operations |

The strongest alignment with Commonplace is the belief that durable agent memory should be made out of inspectable files with explicit authority levels. Both systems treat markdown as more than notes: the file layout, frontmatter fields, indexes, and validators are part of how future agents are constrained.

The main divergence is maturity of the type system and shipped machinery. Commonplace has collection contracts, type specs, schemas, and deterministic commands that operate on this repository's own artifacts. llm-wiki-coordination is an extraction package: it gives a downstream wiki a protocol vocabulary and one lower-layer audit script, but it does not ship templates, a complete validator for every stated semantic rule, or an agent workflow that closes the loop from discussion into canon.

The RoleSpace mechanism is the distinctive idea. It records the shape of a dialogue deficit as a small symbolic vector, which can guide who should speak next and what kind of contribution is missing. Commonplace has semantic review gates and issue-style findings, but not a comparable participation-balance signal for multi-agent deliberation.

**Read-back:** `pull` — The reviewed repository provides copied protocol files, downstream dialogue files, and an audit command that agents or humans must deliberately read or run; it does not implement a hook, matcher, scheduler, or host integration that pushes retained wiki memory into an acting agent before a task.

### Borrowable Ideas

**Peer evaluation in the next entry.** Commonplace review reports could borrow the structural rule that a contribution is evaluated by the next participant rather than by itself. Ready for workshop use in multi-agent review threads, but not needed for ordinary single-agent note writing.

**Deficit vectors for deliberation.** A lightweight Novelty/Coherence/Robustness vector could help route multi-pass review bundles: novelty for new framing, coherence for KB integration, robustness for adversarial checks. Needs a real multi-agent review workflow before becoming a core type.

**Hard errors as named invariants.** Commonplace validation already has checks, but naming invariants separately from findings can make reports easier to debate and retire. Ready as documentation cleanup for validation and review-gate outputs.

**Separate lifecycle from consensus.** Commonplace status fields and semantic review state are related but not identical. The consensus/lifecycle split is a useful reminder not to collapse artifact maturity, reviewer agreement, and user acceptance into one field. Ready as a lens for future type revisions.

**Append-only dialogue directories.** For long investigations, one-file transcripts become context-heavy and hard to review. A Commonplace workshop could use thread directories with `thread.md`, metadata, and entry files when multiple agents contribute over time. Needs a target workflow so the structure does not become overhead.

**Do not borrow ontology without enforcement.** The Anchor Form/Recognition vocabulary is coherent inside its source tradition, but Commonplace should not import it unless it creates concrete review, identity, or signature behavior. Otherwise it would add terms without operational payoff.

## Write-side placement

**Write agency:** `automatic` `manual` — the review identifies a trace-derived or rule-driven path that changes retained memory from execution/session evidence; manual surfaces are included where the reviewed prose describes user or operator authoring.

**Curation operations:** `synthesize` `invalidate` `decay` `promote` — the existing review evidence identifies automatic store-changing operations matching these curation classes.

### Trace-derived learning
**Trace source:** `session-logs` `trajectories` — The retained traces are downstream dialogue threads: contribution files, peer evaluations, closure entries, and consensus updates across a multi-agent thread.

**Learning scope:** `per-project` `cross-task` — Scope is project/wiki-local, but crystallized canon and consensus state can shape later tasks in that wiki.

**Learning timing:** `staged` — Dialogue accumulates first, then closure, recognition, canonization, consensus, and audit happen in staged/manual steps.

**Distilled form:** `prose` `symbolic` — Crystallized canon is prose knowledge, while RoleSpace vectors, consensus frontmatter, lifecycle states, and audit findings are symbolic governance state.

**Trace source.** The qualifying trace source is downstream multi-agent dialogue: individual contribution files, peer evaluations, closure entries, and consensus updates. The repo's own README names the intended flow as discussion to structured entries to peer review to crystallized knowledge to audit ([README.md](https://github.com/AEVYRA/llm-wiki-coordination/blob/126749634d1c8c2fd6141f59711c882c2d629699/README.md)).

**Extraction.** Extraction is protocolized rather than automated. Agents write entries, the next entry evaluates the previous one, the accumulated RoleSpace vector indicates whether the thread is mature, and a closure entry proposes canonization. User Recognition or a delegated closer is the oracle at crystallization time. The audit script can check several structural prerequisites, but it does not synthesize canon or judge semantic adequacy.

**Scope and timing.** Scope is project/wiki-local. Timing is staged and mostly manual: dialogue entries accumulate during a thread, closure happens when the vector and external recognition conditions are met, consensus is recorded on structural pages, and audit runs afterward or on demand.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), this belongs in the trace-to-canon protocol family rather than the automatic transcript-mining family. It strengthens the survey's distinction between raw trace artifacts and higher-authority system-definition artifacts: entries are preserved evidence, RoleSpace/consensus fields are symbolic governance state, and crystallized canon is the behavior-shaping output. It weakens any claim that trace-derived learning must be automated to be architecturally relevant.

## Curiosity Pass

**The repository says "templates" in AGENTS.md, but v0.2.0 is documentation-first.** README installation says there are no generated templates yet and tells users to copy/adapt `protocols/` and `tools/` ([README.md](https://github.com/AEVYRA/llm-wiki-coordination/blob/126749634d1c8c2fd6141f59711c882c2d629699/README.md), [AGENTS.md](https://github.com/AEVYRA/llm-wiki-coordination/blob/126749634d1c8c2fd6141f59711c882c2d629699/AGENTS.md)). Treat AGENTS.md as contributor guidance with some stale wording, not as evidence of shipped templates.

**The audit script's default layout is narrower than the protocol package.** It assumes a downstream `wiki/` directory, special-cases `wiki/agents/dialogue`, checks several entrypoint names, and flags structural pages under `workflows`, `concepts`, `agents`, and `entities` ([tools/llm-wiki-audit.py](https://github.com/AEVYRA/llm-wiki-coordination/blob/126749634d1c8c2fd6141f59711c882c2d629699/tools/llm-wiki-audit.py)). Projects using different roots must adapt the script or accept blind spots.

**RoleSpace is a control signal, not a quality guarantee.** N/C/R scoring can improve turn-taking and make deficits visible, but the repo cannot prove that scores are calibrated, independent, or predictive. The script checks shape and sums, not epistemic quality.

**The private-key guard is a small but useful enforcement example.** The persona ontology says models should not be treated as holding private keys, and the audit script implements regex checks for private-key claims with negation handling. That is the clearest example of prose ontology becoming executable validation.

**The system's own context-efficiency story is mostly by convention.** Directory threads reduce the need to edit or reload one giant transcript, but there is no command that assembles a bounded thread digest or decides which entries matter for a new task.

## What to Watch

- Whether generated templates or an installer appear. That would change the review from "copy protocol docs" to a concrete scaffold with stronger adoption affordances.
- Whether the audit script gains configuration for alternate wiki roots and protocol scopes. That would make it safer as a drop-in tool rather than a source-specific script generalized by convention.
- Whether crystallization becomes executable: creating `crystallized.md`, updating canon pages, or verifying signatures. That would strengthen the trace-derived placement from manual protocol to implemented promotion.
- Whether semantic L4-L5 review gets a retained report schema. That would make high-level audit findings comparable with lower-layer script findings.
- Whether RoleSpace scores are evaluated against downstream outcomes. Without calibration evidence, they remain useful coordination metadata but weak evidence of contribution quality.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: llm-wiki-coordination defines a manual/staged dialogue-trace to canon path rather than automatic transcript mining.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: the repo separates protocol prose, symbolic frontmatter, audit code, and downstream dialogue artifacts by substrate, form, lineage, and authority.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: protocols, consensus fields, RoleSpace vectors, and audit rules constrain future wiki-agent behavior.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: raw dialogue entries remain evidence/reference until closure, consensus, or canonization gives them stronger authority.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: the repo stores and audits coordination memory but leaves read-back to deliberate agent/human pulls.
- [Symbolic context engineering is bounded by symbol availability](../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) - frames: RoleSpace, status fields, and consensus ids can only route behavior once the downstream wiki emits those symbols.
