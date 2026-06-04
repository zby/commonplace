---
description: "llm-wiki-coordination review: Markdown protocol layer for multi-agent wiki dialogue, consensus, RoleSpace review, and structural audit"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: current
last-checked: "2026-06-04"
---

# llm-wiki-coordination

llm-wiki-coordination, from `AEVYRA/llm-wiki-coordination`, is a documentation-first coordination package for Markdown or Obsidian-style wikis. At the reviewed commit it provides protocol files for append-only multi-agent dialogue threads, RoleSpace peer evaluation, multi-agent consensus blocks, persona manifests, and a Python integrity-audit script. It is not an agent runtime: downstream agents or humans copy the protocol files into a wiki, create the retained files, and run the audit deliberately.

**Repository:** https://github.com/AEVYRA/llm-wiki-coordination

**Reviewed commit:** [126749634d1c8c2fd6141f59711c882c2d629699](https://github.com/AEVYRA/llm-wiki-coordination/commit/126749634d1c8c2fd6141f59711c882c2d629699)

**Last checked:** 2026-06-04

## Core Ideas

**The product is a filesystem protocol, not an execution loop.** The README explicitly positions the repository as a file-and-protocol layer that does not choose models, schedule agents, or execute tasks; installation means copying/adapting `protocols/` and `tools/llm-wiki-audit.py` into a downstream wiki ([README.md](https://github.com/AEVYRA/llm-wiki-coordination/blob/126749634d1c8c2fd6141f59711c882c2d629699/README.md)). This makes the retained memory inspectable and portable, but leaves orchestration and compliance to the host workflow.

**Dialogue memory is append-only by directory shape.** A long-running discussion is a directory with `thread.md`, `meta.yaml`, and numbered `entries/NNN-<author>.md` files; each contribution is a new file, and `last_eval` in an entry evaluates the previous entry rather than itself ([protocols/dialogue-thread-format.md](https://github.com/AEVYRA/llm-wiki-coordination/blob/126749634d1c8c2fd6141f59711c882c2d629699/protocols/dialogue-thread-format.md)). The design turns a chat transcript into separable retained artifacts: stable context, operational state, and per-turn contribution records.

**RoleSpace is symbolic peer-review state.** RoleSpace defines Novelty, Coherence, and Robustness axes, asks each agent to evaluate the previous contribution, and derives situational momentum from the gap between the accumulated vector and the target vector ([protocols/rolespace-coordination.md](https://github.com/AEVYRA/llm-wiki-coordination/blob/126749634d1c8c2fd6141f59711c882c2d629699/protocols/rolespace-coordination.md)). The mechanism is lightweight but high-authority: if agents follow it, the next contribution is routed toward a declared deficit rather than a fixed persona role.

**Consensus and lifecycle are separate governance axes.** The consensus protocol stores agent endorsement statuses and revision markers in frontmatter, separately from document maturity; it also defines stale invalidation after significant edits and dispute routing through dialogue threads ([protocols/multi-ai-consensus.md](https://github.com/AEVYRA/llm-wiki-coordination/blob/126749634d1c8c2fd6141f59711c882c2d629699/protocols/multi-ai-consensus.md)). This is a governance pattern for wiki pages, not a retrieval engine.

**Context efficiency comes from progressive disclosure, not search.** The thread format keeps stable context in `thread.md`, small operational state in `meta.yaml`, and historical contributions in separate entry files so an agent can inspect the latest entry and accumulated vector without loading the whole discussion ([protocols/dialogue-thread-format.md](https://github.com/AEVYRA/llm-wiki-coordination/blob/126749634d1c8c2fd6141f59711c882c2d629699/protocols/dialogue-thread-format.md)). There is no implemented ranking, embedding, compaction, or automatic context injection; the efficiency gain is structural.

**Audit is structural enforcement up to L3.** `llm-wiki-audit.py` scans a downstream `wiki/` tree for frontmatter hygiene, broken Markdown/Obsidian links, dialogue directory shape, RoleSpace vectors, consensus blocks, key-custody claims, and a few cross-protocol checks; it exits nonzero when HARD findings exist ([tools/llm-wiki-audit.py](https://github.com/AEVYRA/llm-wiki-coordination/blob/126749634d1c8c2fd6141f59711c882c2d629699/tools/llm-wiki-audit.py)). The protocol document says L4-L5 semantic and portability review remain AI/human work ([protocols/integrity-audit.md](https://github.com/AEVYRA/llm-wiki-coordination/blob/126749634d1c8c2fd6141f59711c882c2d629699/protocols/integrity-audit.md)).

## Artifact analysis

- **Storage substrate:** `files` `repo` — The shipped retained artifacts are Markdown protocol files, a Python audit script, and downstream wiki files stored in an ordinary filesystem/repository; there is no database, vector store, graph store, or service object in the inspected source.
- **Representational form:** `prose` `symbolic` — Protocol explanations, dialogue entries, thread context, persona ontology, and audit reports are prose; YAML frontmatter, `meta.yaml`, `consensus:` blocks, `last_eval` vectors, statuses, invariant IDs, regexes, and Python checks are symbolic. There is no parametric retrieval state.
- **Lineage:** `authored` — The package consists of authored protocols and tooling. Downstream dialogue entries are agent-authored records and can become evidence for later canonization, but the inspected repository does not implement automatic extraction from traces into durable memory.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` — Dialogue entries and crystallization summaries are knowledge artifacts; protocol files instruct agents; the audit script enforces by returning HARD/WARN/INFO findings and nonzero exit status; RoleSpace deficits, statuses, consensus blocks, and canon-page references route future work; structural and link checks validate the wiki.

**Protocol files.** `protocols/dialogue-thread-format.md`, `protocols/rolespace-coordination.md`, `protocols/multi-ai-consensus.md`, and `protocols/integrity-audit.md` are authored system-definition artifacts. Their authority depends on the host agent reading and following them; the repo itself does not install hooks that force every write through the protocol.

**Downstream dialogue directories.** In an adopting wiki, `thread.md`, `meta.yaml`, and `entries/` become durable coordination memory. `thread.md` carries stable context and open questions, `meta.yaml` carries status and RoleSpace targets, and entry frontmatter carries peer evaluation fields that future agents can calculate over ([protocols/dialogue-thread-format.md](https://github.com/AEVYRA/llm-wiki-coordination/blob/126749634d1c8c2fd6141f59711c882c2d629699/protocols/dialogue-thread-format.md)).

**Consensus blocks.** `consensus:` frontmatter on structural pages records per-agent status and revision alignment. The audit code checks accepted lifecycle pages for missing or pending consensus, but it does not implement the full stale-invalidation or active-agent timing policy described in the protocol ([protocols/multi-ai-consensus.md](https://github.com/AEVYRA/llm-wiki-coordination/blob/126749634d1c8c2fd6141f59711c882c2d629699/protocols/multi-ai-consensus.md), [tools/llm-wiki-audit.py](https://github.com/AEVYRA/llm-wiki-coordination/blob/126749634d1c8c2fd6141f59711c882c2d629699/tools/llm-wiki-audit.py)).

**Audit script.** `GenericWikiAudit` reads files under `wiki/`, parses frontmatter, builds link and heading indexes, validates dialogue entries, checks consensus blocks, detects private-key claims, and prints structured findings or JSON ([tools/llm-wiki-audit.py](https://github.com/AEVYRA/llm-wiki-coordination/blob/126749634d1c8c2fd6141f59711c882c2d629699/tools/llm-wiki-audit.py)). It is a validator and reporter, not a writer: it does not repair files, synthesize canon, or update memory.

Promotion path: the documented path is discussion -> structured entries -> peer review -> crystallized knowledge -> audit. At this commit, the structural protocol and audit checks exist, but crystallization into canon, signatures, tombstones, and L4-L5 semantic review are either manual, protocol-level, or explicitly out of scope.

## Comparison with Our System

llm-wiki-coordination and Commonplace share the premise that ordinary files can carry operational memory for agents. Both use Markdown, frontmatter, explicit conventions, and validation rather than a hidden vector-only memory layer. The major difference is scope: llm-wiki-coordination is a drop-in protocol kit for a downstream wiki, while Commonplace is a full knowledge-base methodology with collection contracts, type specs, validation, generated indexes, source snapshots, review workflows, and durable library/workshop layers.

The strongest overlap is the workshop layer. llm-wiki-coordination's dialogue directories resemble a Commonplace workshop artifact: they hold temporary but meaningful investigation state, preserve per-entry provenance, and can promote a result into canon after review. Commonplace is stricter about artifact typing and validation; llm-wiki-coordination is lighter and easier to graft onto an existing wiki.

The main tradeoff is authority. llm-wiki-coordination makes protocol state visible and auditable, but compliance relies on agents choosing to read the files and run the audit. Commonplace's commands and collection contracts make more of the behavior executable, though still not a full runtime that intercepts every edit.

### Borrowable Ideas

**Append-only dialogue entries for contested work.** Ready for workshop use. Commonplace could use a `thread.md` + `meta.yaml` + `entries/` shape for high-friction investigations where preserving each agent's contribution matters more than producing a clean draft immediately.

**Peer evaluation in the next entry.** Useful but needs a concrete workflow. The no-self-evaluation rule is a simple structural guard against self-scored progress, but Commonplace should only add it where multi-agent review is actually active.

**RoleSpace as review coverage vocabulary.** Ready as optional language for review bundles. Novelty, Coherence, and Robustness are compact axes for asking whether a discussion has added ideas, linked them, and stress-tested them.

**Consensus frontmatter is too heavy for ordinary notes.** Commonplace should not borrow per-agent consensus blocks broadly. The pattern fits protocol or ADR-level artifacts where stale endorsement matters, not every descriptive note.

**Audit layers map well to validator tiers.** The L0-L5 split is borrowable as naming: deterministic structure first, semantic review later, and semantic findings should not become hard blocks unless an explicit gate says so.

## Write side

**Write agency:** `manual` — Humans or agents manually copy protocol files, create dialogue directories and entries, update consensus blocks, write crystallization proposals, and run the audit. The inspected audit tool only reports findings and exit status; it does not automatically change stored memory.

## Read-back

**Read-back:** `pull` — Retained protocols, dialogue entries, consensus blocks, and audit findings re-enter future work only when an agent or human deliberately reads the files or runs the audit command. The repo does not implement a hook, scheduler, matcher, MCP server, prompt assembler, or runtime integration that pushes wiki memory into an agent before action.

Pull read-back is still useful: an agent can read the latest entry, compute RoleSpace deficits from `last_eval`, inspect consensus status before editing a structural page, or run `python3 tools/llm-wiki-audit.py` to get a structural issue list. But those are explicit lookup/check actions, and effective use depends on host instructions outside the package.

## Curiosity Pass

**The most practical memory mechanism is not the ontology.** The persona manifest and Trace/Recognition vocabulary are distinctive, but the reviewable engineering value is the directory thread shape plus auditable frontmatter.

**The audit implements less than the protocol describes.** The code checks concrete L0-L3 invariants, but stale consensus invalidation, active-agent dormancy, semantic contradiction review, crystallization output, and tombstone creation remain protocol obligations for humans or agents.

**The package treats coordination state as first-class memory.** `last_eval`, `current_at_close`, `consensus:`, lifecycle, and canon-page references are small symbolic fields, but they decide what future agents should inspect, accept, reopen, or challenge.

**Context efficiency is achieved by avoiding transcript monoliths.** The design does not compress history automatically; it lets future agents choose which entry files and summary fields to read.

## What to Watch

- Whether a future release adds executable crystallization that writes `crystallized.md`, patches canon pages, or records signatures; that would move the promotion path from documented protocol to implemented write-side behavior.
- Whether the audit grows repair or autofix operations. That would change the write side from manual-only to manual plus automatic validation-driven maintenance.
- Whether stale consensus and active-agent dormancy rules become code, since those are currently stronger in prose than in the audit implementation.
- Whether any host integration appears, such as an MCP server, pre-commit hook, AGENTS.md installer, or prompt assembler; that would change read-back from pull-only to push or both.
- Whether L4-L5 semantic audit gets a retained report format with citations; that would create a more Commonplace-like bridge from structural lint to reviewable semantic QA.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: llm-wiki-coordination stores protocols and dialogue memory, but activation is pull-only unless a host agent reads or runs it.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: protocol prose, symbolic frontmatter, audit code, and dialogue entries have different authority and review methods.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: dialogue entries, crystallization summaries, and audit reports mostly serve as evidence and reference.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: protocol files, consensus rules, RoleSpace fields, and audit checks shape later behavior with instruction, validation, routing, and enforcement force.
- [A functioning KB needs a workshop layer not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) - compares: dialogue thread directories are a workshop-style holding area for contested or in-flight reasoning before promotion.
