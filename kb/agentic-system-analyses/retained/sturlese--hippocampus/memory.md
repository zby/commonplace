---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Hippocampus memory: model-curated Markdown pages, provenance archives, catalog selection and lifecycle cache reload."
run-id: AAS-2026-11-08-hippocampus-30a5ab9b2a87-01
source-identity: https://github.com/sturlese/hippocampus
reviewed-boundary: "99531951ae60a9814ac7d27a32dd00f0c81a5008"
---

# Hippocampus memory report

## Boundary and evidence

Hippocampus retains personal knowledge in a local Markdown vault. This member covers source acquisition and archiving, source and derived pages, conversation saving, catalog/journal/cache maintenance, question retrieval, session reload, structural evaluation and user-approved editorial change. It includes framework replacement as a separate instruction-change surface, not as knowledge extraction. The frozen source is SRC-1 at commit `99531951ae60a9814ac7d27a32dd00f0c81a5008`; source registration and host exclusions remain those of [boundary](boundary.md#source-register).

Direct reads: `CLAUDE.md`, all three canonical `.claude/skills/*/SKILL.md` files, all five `_templates/*.md` files, both host hook configurations, `scripts/on-stop.sh`, complete `scripts/vault_lint.py`, `wiki/hot.md`, `wiki/index.md`, `wiki/log.md`, `docs/why-no-vector-db.md` and `docs/what-happens-when-you-ingest.md`. All belong to SRC-1. Prompt/template/document passages supply doctrine/design; shell/Python/configuration supply implementation. Adapter dispatch, model selection and framework synchronization findings below are supplied runtime findings, not independent rereads. Git HEAD and clean worktree were checked before inspection. No target code was executed.

| Entry point or operation | SRC-1 source path | Coverage and limit |
|---|---|---|
| Inbox, outside path, paste, URL acquisition; dedup/re-ingest; large-source sections; sequential batches | `.claude/skills/ingest/SKILL.md` | Direct; [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [MEM-OBJ-archive](#mem-obj-archive), [MEM-OBJ-source](#mem-obj-source). Model protocol, no demonstrated extraction. |
| Conversation save, concept/project alternatives, overwrite question | `.claude/skills/save/SKILL.md`, `_templates/note.md`, `_templates/project.md`, `_templates/concept.md` | Direct; [RT-RTE-conversation-save](runtime.md#rt-rte-conversation-save), [MEM-OBJ-pages](#mem-obj-pages). No supplied conversation trace. |
| Derived knowledge, source links, contradiction callouts | `CLAUDE.md`, `_templates/entity.md`, `_templates/concept.md` | Direct; [MEM-OBJ-pages](#mem-obj-pages). Human resolution prescribed, not observed. |
| Catalog, operation journal, hot-cache replacement | `wiki/index.md`, `wiki/log.md`, `wiki/hot.md`, ingest/save/lint skills | Direct; separate objects below. Scaffold, not a populated vault. |
| Question routing, one-hop browsing, search fallback, cross-project consultation | `CLAUDE.md` | Direct; [RT-RTE-vault-query](runtime.md#rt-rte-vault-query). Read role specified; deployed external reader unobserved. |
| Startup/resume/clear/compact injection and stop-time refresh/persistence | `.claude/settings.json`, `.codex/hooks.json`, `scripts/on-stop.sh` | Direct; [RT-RTE-lifecycle-hooks](runtime.md#rt-rte-lifecycle-hooks), [MEM-OBJ-hot](#mem-obj-hot). Host event interpretation and compaction internals outside boundary. |
| Mechanical evaluation, editorial sampling, merge/delete/rejection | `scripts/vault_lint.py`, `.claude/skills/lint/SKILL.md` | Direct; [RT-RTE-vault-lint](runtime.md#rt-rte-vault-lint). No claim-truth oracle or enforced pre-write gate. |
| Canonical and Codex skill dispatch; host-native tools | `AGENTS.md`, `.agents/skills/ingest/SKILL.md`, `.agents/skills/save/SKILL.md`, `.agents/skills/lint/SKILL.md` | Supplied runtime account; no distinct memory service API or separate executor is asserted. |
| Framework update/diff/export | `scripts/sync_framework.sh` | Supplied [RT-RTE-framework-update](runtime.md#rt-rte-framework-update), [RT-RTE-framework-export](runtime.md#rt-rte-framework-export); future fetched revisions excluded. |
| Model and human browsing consumers | `README.md`, `.obsidian/` | Supplied boundary/runtime findings; host model internals, actual Obsidian rendering and populated private vault unavailable. Prevents claims about activated recall or quality. |

## Core ideas

1. **Knowledge and its original are separate.** The archive retains source material; source pages summarize claims; reusable pages consolidate knowledge. Hash/origin fields provide identity and a recovery pointer, not an epistemic warrant. See [MEM-OBJ-archive](#mem-obj-archive), [MEM-OBJ-source](#mem-obj-source), [MEM-OBJ-pages](#mem-obj-pages).
2. **The catalog is selection metadata, not the whole memory.** Its prose descriptions guide the model toward three to five pages. Wikilinks permit a further hop, while term search can recover material missed by catalog wording. A missed catalog entry is not absolute invisibility; see [RT-RTE-vault-query](runtime.md#rt-rte-vault-query).
3. **The hot cache is a second, automatic delivery path.** A foreground model rewrites a recent-context summary; SessionStart emits the whole file. A timestamp guard can request rewriting, but cannot establish semantic freshness. The 500-word policy is not a hard write limit; see [MEM-OBJ-hot](#mem-obj-hot).
4. **Semantic curation is model-operated, with selective human veto.** Ordinary ingest/save admits content without per-page approval; contradiction resolution and destructive lint changes ask the user. Structural checking reports defects but does not decide truth or gate every write. See [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [RT-RTE-conversation-save](runtime.md#rt-rte-conversation-save), [RT-RTE-vault-lint](runtime.md#rt-rte-vault-lint).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-archive
Label: Archived originals

Source-native identity: `inbox/_done/` originals and `_attachments/` referenced files. Substrate: local filesystem, conditionally versioned by Git. Original representational form depends on the input: prose notes are natural language; PDFs/images/data may have other encodings and opaque content. No populated payload is supplied. This object is distinct from the instruction/configuration objects in runtime; its closest route is [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), which produces rather than denotes it. Attachments are auxiliary payloads, not evidence of an automatic knowledge-extraction route for every file type.

Lineage: inbox files move without content editing; outside files are copied; pasted text is saved verbatim. URL acquisition archives extracted content plus URL/fetch metadata, not necessarily the original response bytes. Admission is model-mediated under a user ingest request; the user chooses the input, not every extracted claim. Archive collision handling chooses a suffixed filename before writing. Existing originals must not be overwritten. The later ordinary question route targets wiki pages, not this archive; `origin` makes manual recovery/source inspection possible, but a routine automatic archive-read consumer is not established. SRC-1: `.claude/skills/ingest/SKILL.md`, `_templates/source.md`, `CLAUDE.md`.

> - **A URL** — fetch it with the available web tool, save the extracted content to `inbox/_done/<slug>-<YYYY-MM-DD>.md` with `source_url` and `fetched` in frontmatter, then ingest.
> --- `.claude/skills/ingest/SKILL.md`

> 4. **Decide the archive path now**: `inbox/_done/<original-name>`; if that name is already taken, suffix with date-time (`report.md` → `report-20260711-1030.md`). Never overwrite an archived original.
> --- `.claude/skills/ingest/SKILL.md`

#### MEM-OBJ-source
Label: Source pages

Source-native identity: `wiki/sources/` pages from `_templates/source.md`. Substrate: local Markdown, conditionally Git-versioned. Operative parts: natural-language summary/key claims/notes; provenance and access metadata (`origin`, `content_hash`, URL, dates, links); source confidence label. Hash and path values have symbolic identity uses in dedup and file location. Confidence and claims require interpretation; no deterministic truth rule consumes the confidence label in the inspected linter. Distinct from [MEM-OBJ-archive](#mem-obj-archive): these pages are derived displays, not byte-preserving originals. Closest supplied record is the producing [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), not an existing object declaration.

The foreground model authors and admits summaries after a hash check; explicit user re-ingest overrides duplicate stopping. Later queries may select these pages through index/search/links; future ingests search their hashes and consult prior knowledge. Claim citations and origin preserve a path to evidence, not complete derivation or verification. SRC-1: `_templates/source.md`, `.claude/skills/ingest/SKILL.md`, `CLAUDE.md`, `scripts/vault_lint.py`.

> confidence: medium       # high | medium | low
> content_hash: "<sha256 of the original file>"
> origin: "inbox/_done/<original-filename>"
> --- `_templates/source.md`

#### MEM-OBJ-pages
Label: Entity concept project and note pages

Source-native identity: `wiki/entities/`, `wiki/concepts/`, `wiki/projects/`, `wiki/notes/`. Substrate: local Markdown with flat YAML, conditionally Git-versioned. Natural-language facts, definitions, explanations, decisions and synthesis are the knowledge-bearing parts. Symbolic link syntax and type/date/status/alias fields support structural checks and navigation; status is not a truth certificate. Distinct from [RT-OBJ-project-contract](runtime.md#rt-obj-project-contract): these are accumulated vault content, not the host's project instructions. Closest supplied producers are [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) and [RT-RTE-conversation-save](runtime.md#rt-rte-conversation-save).

Lineage differs by path. Ingest consolidates external source claims and cross-links source pages; save transforms the current conversation into conclusions rather than copying the transcript. Projects can retain dated decisions and rationale; notes can retain decisions/rationale or session synthesis. Concept templates solicit mechanisms and examples. This permits explanations but does not prove a particular saved page contains adequate reasons. Query synthesis and later ingest/editorial decisions consume selected pages as knowledge, not elevated instruction authority. Ordinary model-authored writes need no universal human content approval; new projects require confirmation, same-name save overwrites ask, contradictions are flagged for the user. SRC-1: all five `_templates/*.md`, `.claude/skills/ingest/SKILL.md`, `.claude/skills/save/SKILL.md`, `CLAUDE.md`.

> 1. **Identify what's worth keeping**: the synthesis, the decision and its rationale, the findings. Skip mechanical Q&A, setup steps, and anything already in the wiki (update the existing page instead — check `wiki/index.md`).
> --- `.claude/skills/save/SKILL.md`

> ## Decisions
>
> - <YYYY-MM-DD> — <decision and rationale>
> --- `_templates/project.md`

#### MEM-OBJ-index
Label: Wiki index

Source-native identity: `wiki/index.md`. Substrate: local Markdown. Natural-language one-sentence descriptions are relevance cues interpreted by the agent; symbolic wikilinks are page identifiers also parsed by the linter. This is access metadata, not a complete copy of page knowledge. No supplied object counterpart; closest consumer is [RT-RTE-vault-query](runtime.md#rt-rte-vault-query).

Ingest/save author or update entries; lint can propose repairing drift. User-approved bulk lint repairs are distinct from ordinary automatic model admission during ingest/save. Later questions use the question and descriptions to select pages; ingest uses the catalog to avoid duplicates. The catalog has no prescribed aggregate size cap. Catalog fit is an explicit design assumption, not measured scalability. SRC-1: `wiki/index.md`, `CLAUDE.md`, `.claude/skills/lint/SKILL.md`, `docs/why-no-vector-db.md`.

> Master catalog. One line per page: wikilink + one-sentence description. Newest entries first within each section.
> --- `wiki/index.md`

> **Scale.** The read path assumes a catalog a model can hold in context — hundreds to low
> thousands of pages, which is what a personal vault is. Point this at a corporate wiki with
> fifty thousand documents and the index stops fitting, at which point you want a real retrieval
> layer.
> --- `docs/why-no-vector-db.md`

#### MEM-OBJ-log
Label: Operations journal

Source-native identity: `wiki/log.md`. Substrate: local Markdown, conditionally Git-versioned. Form: natural-language operation descriptions and insights with symbolic page links, dates and origin paths. It is a derived activity journal, not the raw conversation/tool transcript or an exhaustive executable audit. No supplied object counterpart; producing routes are [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [RT-RTE-conversation-save](runtime.md#rt-rte-conversation-save), [RT-RTE-vault-lint](runtime.md#rt-rte-vault-lint).

Model instructions prepend entries without editing history; there is no append-only filesystem enforcement. The journal can document a mutation and support manual review, but its preservation does not establish a trace-fed learning route. Routine question instructions do not select it specially. It remains searchable under `wiki/`, so it is not inaccessible; actual later use is unobserved. SRC-1: `wiki/log.md`, `CLAUDE.md`, `.claude/skills/ingest/SKILL.md`.

> Append-only journal. New entries at the TOP. Never edit past entries.
> --- `wiki/log.md`

#### MEM-OBJ-hot
Label: Hot cache

Source-native identity: `wiki/hot.md`. Substrate: local Markdown, conditionally Git-versioned; copies are emitted by hooks into host context. Form: natural-language recent facts, changes and active threads plus symbolic dates/frontmatter. Unlike [RT-OBJ-hook-config](runtime.md#rt-obj-hook-config), this is retained payload rather than the event wiring. Closest producing/consuming record is [RT-RTE-lifecycle-hooks](runtime.md#rt-rte-lifecycle-hooks).

Lineage: the model overwrites the summary after ingest/save or page-changing lint, or in response to the timestamp-driven Stop request. The model selects facts and admits the rewrite; shell neither summarizes nor validates semantic completeness. Initial content is a day-zero scaffold, not evidence of actual retention. Later host startup/resume/clear/compact delivers the file without query targeting; questions and ingestion also explicitly read it. The cache has knowledge/context force, while the Stop rewrite message has instruction force. Recent-context replacement can remove details while leaving source pages reachable through index/search. No TTL or explicit per-fact eviction rule is specified. SRC-1: `wiki/hot.md`, `CLAUDE.md`, both hook configs, `scripts/on-stop.sh`; supporting hook passages in [RT-BAP-stop-refresh](runtime.md#rt-bap-stop-refresh).

> ├── hot.md      Recent-context cache, ≤500 words. Overwrite completely each refresh.
> --- `CLAUDE.md`

>             "additionalContextLimit": 5000
> --- `.codex/hooks.json`

The cache's 500-word size is prescribed; `scripts/vault_lint.py` counts body words and emits a warning above 500. Hook delivery itself does not truncate to 500 words. Codex's additional-context limit is host configuration whose units/truncation semantics are outside this source. Therefore neither limit proves the exact bytes or tokens ultimately visible to a deployed model.

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-vault-knowledge
Label: Retained vault knowledge authority

Consumer: foreground vault agent, or an external project agent configured by the documented consultation snippet. Channel: hook-supplied hot text and explicit file reads selected through catalog, links or search. Force: evidence/context for synthesis and curation, not permission for source text to redefine project rules. Horizon: later invocations and sessions while files persist; no observed behavioral activation. Distinct from [RT-BAP-project-guidance](runtime.md#rt-bap-project-guidance) and [RT-BAP-stop-refresh](runtime.md#rt-bap-stop-refresh), which carry instructions rather than knowledge payloads. SRC-1: `CLAUDE.md`, `.claude/skills/ingest/SKILL.md`, both hook configs. Supporting query and distrust passages: [RT-RTE-vault-query](runtime.md#rt-rte-vault-query), [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest).

> For context not in this project: read wiki/hot.md first, then wiki/index.md,
> then only the specific pages you need. Do not use it for general coding questions.
> --- `CLAUDE.md`

## Annotations

#### On [RT-RTE-conversation-save](runtime.md#rt-rte-conversation-save)

Memory-specific chain: current conversation → model-selected conclusions, decisions/rationale or findings → [MEM-OBJ-pages](#mem-obj-pages) and refreshed [MEM-OBJ-index](#mem-obj-index), [MEM-OBJ-log](#mem-obj-log), [MEM-OBJ-hot](#mem-obj-hot) → later session context and query synthesis. This is a trace-fed transformation afforded by the skill, not merely raw trace storage. The user triggers it, but the model selects retained content; ambiguity and overwrite questions are selective human interventions. The retained rationale may inform later page readers, but the skill does not preserve all intermediate reasoning or establish improved capacity. SRC-1: `.claude/skills/save/SKILL.md`, `_templates/note.md`; extraction passage in [MEM-OBJ-pages](#mem-obj-pages) and transcript exclusion in the supplied route.

#### On [RT-RTE-lifecycle-hooks](runtime.md#rt-rte-lifecycle-hooks)

Automatic read-back selector: event matching startup/resume/clear/compact; input is the existing hot file, selected part is the entire file if present, not facts ranked by the current question. Delivery is command stdout into external host context. Foreground model selection occurs earlier during rewriting, under a 500-word/four-section request, not in the SessionStart shell. Reloading a summary after host compaction can restore recent knowledge, but does not establish what conversation material the host discarded or kept. No independent subagent frame, verifiable verbatim-tail checkpoint or alternative local compaction artifact is established by these configs. SRC-1: both hook configs, `scripts/on-stop.sh`, `wiki/hot.md`; see [MEM-OBJ-hot](#mem-obj-hot).

## Write side

**Acquisition and admission.** [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) specifies four admission paths, hash duplicate rejection with explicit re-ingest override, never-overwrite archive naming, extraction and knowledge-page updating. The user selects inputs; the model determines most retained content and page-worthiness. Physical moves/copies/writes belong to host tools. These are separate responsibilities. Source distrust is a prompt rule, not a parser or runtime isolation barrier. Very large sources use natural-section provisional extraction followed by consolidation; the full-source/no-chunking walkthrough must not erase that alternative. Batch instructions defer combined cross-reference and metadata maintenance until all inputs are processed. A failed or interrupted sequence can leave intermediate files because no multi-file transaction is supplied.

**Conversation-derived memory.** Save is the explicit conversation-to-durable-result path, including decision rationale and session synthesis rather than transcript copying. The chain is retained in the route annotation. Hot rewriting is an automatic requested derivative of changed vault state; the prescribed journal and hot summary may carry experience-derived content after a save, but timestamp detection itself supplies no semantic evidence about the experience. This is not parameter learning: [RT-CMP-agent-model](runtime.md#rt-cmp-agent-model) leaves provider mutability uninspected and establishes no local training request.

**Curation and evaluation.** [RT-RTE-vault-lint](runtime.md#rt-rte-vault-lint) separates deterministic structural findings from editorial judgments. Direct Python inspection confirms a scan/report CLI (`--vault`, `--json`), not an automatic content editor. It detects duplicate basenames, not arbitrary semantic duplication under different names; alias collisions and index drift are separate checks. Its normal completed scan returns zero even with errors. The model may sample recent pages in a large vault, so editorial coverage is not guaranteed exhaustive. Safe fixes require bulk approval; merging, deleting or resolving contradictions require individual approval. Aging seeds after thirty days are candidates for review, not automatic expiry. A retained meta lint report is conditional on user desire or many findings; it is diagnostic material, not automatically consumed policy. SRC-1: `scripts/vault_lint.py`, `.claude/skills/lint/SKILL.md`.

> - **One-by-one approval**: deleting orphans (isolation may be intentional), merging duplicates, resolving contradictions (needs the user's judgment on which side is true).
> --- `.claude/skills/lint/SKILL.md`

**Withdrawal and recovery.** Contradiction callouts preserve competing content rather than withdrawing it; later questions can encounter either or both. Lint permits individually approved deletion/merge, and catalog repairs can remove dead entries, but no automatic propagation of a retracted claim across every derivative is specified by those instructions. Cache replacement can remove facts, without a guaranteed semantic invalidation dependency graph. The Git stop hook can preserve version history and stages deletions within its roots, but successful history creation is conditional and manual rollback is not automatic. Existing archive pointers aid inspection without making reconstruction exact. SRC-1: `CLAUDE.md`, lint skill, `scripts/on-stop.sh`; [RT-RTE-lifecycle-hooks](runtime.md#rt-rte-lifecycle-hooks).

**Instruction change.** Framework update/export can replace future behavior-shaping prompts/templates/hooks; their admission mechanisms differ from knowledge-page curation. Supplied [RT-RTE-framework-update](runtime.md#rt-rte-framework-update) and [RT-RTE-framework-export](runtime.md#rt-rte-framework-export) establish path/dirty-state admission and manual later review, not trace-responsive improvement or proof of deployment. Static shipped instructions are not accumulated read-back memory merely because loaded each session.

## Read-back

Two material paths coexist. The **requested path** is [RT-RTE-vault-query](runtime.md#rt-rte-vault-query): the foreground model reads hot, reads the catalog, selects three to five pages, follows at most one further wikilink hop, and if still not confident searches distinctive terms, aliases and likely synonyms. The query and catalog prose are selection inputs, unlike the unconditional hot injection. Pages have a prescribed 30–150-line range, but no enforced aggregate context/token budget is supplied. The fallback is bounded by strongest-match reading, not a complete corpus read. These are instructed model choices, not proven retrieval recall. The external-project consultation snippet affords another reader role without showing a deployed caller.

The **automatic path** is the lifecycle annotation: all hot content is emitted on the configured events, with the Codex limit caveat. Hot can therefore affect a later invocation without a separate explicit user query. Triggering a hook and delivering knowledge remain distinct from evidence that the knowledge changes the answer. A storage capability such as `origin` or Git history is not itself a later consumer route; neither is optional log/report retention proof of learning.

Working-context control is frontloaded page selection and cache substitution, not local trimming of accumulated conversation turns. Sequential source processing and section extraction can reduce a single read's breadth but do not specify eviction of prior turns. No foreground-to-child isolated context or returning child summary is prescribed in the inspected workflows. The external host's clear/compact operation is opaque; Hippocampus contributes only the summary reload. Files remain reachable after omission, but a wikilink is a string requiring a tool read, not a live heap reference or liveness marker. A stack-frame analogy does not explain this foreground workflow because no isolated frame is allocated and popped by Hippocampus. SRC-1: `CLAUDE.md`, ingest skill, both hook configs; [RT-RTE-lifecycle-hooks](runtime.md#rt-rte-lifecycle-hooks).

## Integration issues

- **No correction to a supplied runtime fact is required.** Direct inspection agrees with the supplied exceptions to forced refresh and with its fallback qualification. The source walkthrough's absolute invisibility claim for unindexed pages is contradicted by the shipped search fallback; this is a source-claim qualification, not a runtime correction. Evidence: SRC-1 `docs/what-happens-when-you-ingest.md`, `CLAUDE.md`; affected records: [MEM-OBJ-index](#mem-obj-index), [RT-RTE-vault-query](runtime.md#rt-rte-vault-query).
- **No duplicate declaration is intended.** New objects denote retained payloads/access metadata, whereas supplied objects denote project guidance and hook wiring. [MEM-BAP-vault-knowledge](#mem-bap-vault-knowledge) differs from the two instruction-authority paths. Existing routes are annotated or cited, not redeclared. Reconciliation can keep these distinctions without supersession.
- **Exact host-visible cache remains unresolved.** SRC-1 `.codex/hooks.json` declares an additional-context limit, but host handling is external. [MEM-OBJ-hot](#mem-obj-hot) and [RT-RTE-lifecycle-hooks](runtime.md#rt-rte-lifecycle-hooks) cannot establish exact delivered token counts, compaction survivors or successful hook activation.
- **Retention fidelity and benefit remain unresolved.** The source corpus is a scaffold; no saved conversation, source payload or post-update query trace is supplied. [MEM-OBJ-pages](#mem-obj-pages), [MEM-OBJ-source](#mem-obj-source), [RT-RTE-conversation-save](runtime.md#rt-rte-conversation-save) establish afforded derivation and later consumers, not faithful rationale retention, improved capacity, or exercised self-improvement.
- **Semantic withdrawal propagation remains unspecified in inspected procedures.** SRC-1 `CLAUDE.md` and lint skill offer callouts and approved edits, without a claim dependency invalidator. [MEM-OBJ-pages](#mem-obj-pages), [MEM-OBJ-hot](#mem-obj-hot), [RT-RTE-vault-lint](runtime.md#rt-rte-vault-lint) do not establish that every downstream summary is corrected when a source claim changes.

## Limitations and checks

The implementation tier applies to scripts/configuration, not to model compliance with extraction, source distrust, contradiction detection or retrieval selection. No target execution, provider calls, fixture creation or experimental intervention was performed. External host semantics and actual human/model browsing remain uninspected. No comparative reliability, capacity improvement or measured retrieval benefit follows from these source findings.

Source identity recheck: Git HEAD matched the full reviewed boundary and the worktree was clean before source reads. Method identity is the supplied invocation, memory-member type, worker rules and records contract; no prior analyses or outside evidence were consulted. Validation: the required role-specific `commonplace-validate` content check passed (exit 0). It reported: “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.”
