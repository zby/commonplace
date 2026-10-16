---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "ai-memex-cli memory: source capture, session transformations, agent-edited wiki and instruction state, and selective later-session delivery"
run-id: AAS-2026-10-15-ai-memex-cli-4324549b4bc0-01
source-identity: "https://github.com/zelixag/ai-memex-cli"
reviewed-boundary: "4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f"
---

# ai-memex-cli memory report

## Boundary and evidence

The subject is the Markdown knowledge system fixed by [boundary](boundary.md), not the external agents' private memory. All source findings use SRC-1 at commit `4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f`. Included memory surfaces are captured web/local material, converted and semantically distilled sessions, wiki text and metadata, live schema instructions, catalog/action history, lint feedback, project projections, scene manifests and host bootstrap state. Installed skills are static workflow instructions unless subsequently changed; installation alone is not accumulated experience. External agent/provider histories, weights, compaction and qmd internals are uninspected dependencies, not attributed implementations.

Direct reads add implementation evidence from `src/core/distiller.ts`, `src/commands/distill.ts`, `src/commands/inject.ts`, `src/core/injector.ts`, `src/core/globber.ts`, `src/commands/glob.ts`, `src/core/wiki-index.ts`, `src/core/schema.ts`, `src/core/linker.ts`, `src/commands/link-check.ts`, `src/commands/init.ts`, `src/commands/new.ts`, `src/commands/log.ts`, `src/commands/migrate.ts`, `src/core/scene-manifest.ts`, and `src/core/context-registry.ts`; bounded direct reads cover ingest/lint prompt builders, mechanical lint, loop control, context installation/refresh/uninstall, context renderer and CLI read/write dispatch. Doctrine reads cover `templates/AGENTS.md`, source/synthesis templates and installed query, distill and safety references. Capture/watch/adapter/install-update control findings not independently reread here are explicitly supplied runtime evidence. No target execution, tests, network calls or model calls were performed.

| Entry point / operation | Source path, SRC-1 | Coverage and records / prevented conclusion |
|---|---|---|
| init; local/global schema and layout | `src/commands/init.ts` | Direct; [MEM-OBJ-wiki-schema](#mem-obj-wiki-schema), [MEM-OBJ-index-log](#mem-obj-index-log); admission table below |
| fetch URL/search/crawl; delegated fetch | `src/commands/fetch.ts` | Supplied [RT-RTE-capture-source](runtime.md#rt-rte-capture-source); [MEM-OBJ-raw](#mem-obj-raw). Extraction/network-helper fidelity not audited here |
| no-argument / explicit mechanical / delegated distill | `src/commands/distill.ts`, `src/core/distiller.ts` | Direct; [MEM-OBJ-session-markdown](#mem-obj-session-markdown), annotations on [RT-RTE-session-distill](runtime.md#rt-rte-session-distill); provider-format alternatives remain limited by recognized parser shapes |
| ingest and lint-first repair | `src/commands/ingest.ts`, `src/core/ingest-lint-loop.ts` | Direct prompt/loop reads plus supplied [RT-RTE-ingest-write](runtime.md#rt-rte-ingest-write), [RT-RTE-watch-repair](runtime.md#rt-rte-watch-repair); external editing result unknown |
| mechanical lint, semantic repair, link-check | `src/commands/lint.ts`, `src/core/linker.ts`, `src/commands/link-check.ts` | Direct; [MEM-OBJ-lint-results](#mem-obj-lint-results), [RT-RTE-semantic-lint](runtime.md#rt-rte-semantic-lint). Link-check only diagnoses, including with fix flag |
| watch startup/events/health checks and cleanup | `src/commands/watch.ts` | Supplied [RT-RTE-watch-repair](runtime.md#rt-rte-watch-repair); deletion events do not establish automatic knowledge withdrawal |
| new, log, migration | `src/commands/new.ts`, `src/commands/log.ts`, `src/commands/migrate.ts` | Direct; [MEM-OBJ-wiki-body](#mem-obj-wiki-body), [MEM-OBJ-page-metadata](#mem-obj-page-metadata), [MEM-OBJ-index-log](#mem-obj-index-log); distinct admission mechanisms below |
| search and foreground query/page reads | `src/commands/search.ts`, `templates/skills/ai-memex/references/query-workflow.md` | Direct; [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery); [MEM-RTE-query-save](#mem-rte-query-save) covers optional write-back |
| includes and keyword injection | `src/commands/inject.ts`, `src/core/injector.ts`, `src/core/globber.ts` | Direct; [MEM-OBJ-page-metadata](#mem-obj-page-metadata), annotation on [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery); task relevance and token cap not implemented by these options |
| project projection | `src/commands/glob.ts` | Direct; [MEM-OBJ-local-projection](#mem-obj-local-projection); old unselected copies can remain |
| host install/refresh/uninstall, scene triggers | `src/commands/context.ts`, `src/core/context-block.ts`, `src/core/scene-manifest.ts`, `src/core/context-registry.ts` | Direct bounded command/renderer reads and complete manifest/registry; [MEM-OBJ-context-registry](#mem-obj-context-registry), [MEM-OBJ-scene-manifest](#mem-obj-scene-manifest), [MEM-OBJ-host-bootstrap](#mem-obj-host-bootstrap). Host loading/use unobserved |
| slash commands, copied skills, config/update/onboard/status | `src/cli.ts`, `src/commands/install-hooks.ts`, `src/commands/update.ts` | CLI registration search and direct read/use dispatch; supplied [RT-RTE-install-update](runtime.md#rt-rte-install-update), [RT-OBJ-agent-profiles](runtime.md#rt-obj-agent-profiles). Onboarding interaction and status rendering not independently audited; no additional semantic memory writer inferred |
| exposed helpers versus live routes | `src/core/distiller.ts`, `src/commands/lint.ts` | Exported old extraction/compression helpers distinguished from structured distill caller; programmatic lint has a shipped loop consumer. Scoped searches of src/templates found CLI/skill/toolbox surfaces, not grounds for a repository-wide API absence claim |

No real vault or session artifact was supplied. Actual content, privacy, source quality, model compliance, behavioral activation and benefit cannot be concluded. Available files not read are inspection limits, not access gaps.

## Core ideas

1. **Source and derived knowledge are separate files, but source preservation is a maintenance instruction.** Capture writes raw material; ingestion requests derived wiki pages and provenance links. Direct fetch can replace a same-named raw file. The knowledge store is not an append-only database enforced across all writers ([MEM-OBJ-raw](#mem-obj-raw), [RT-RTE-ingest-write](runtime.md#rt-rte-ingest-write), [RT-RTE-capture-source](runtime.md#rt-rte-capture-source)).
2. **Session capture has materially different transformations.** Mechanical mode renders recognized messages, including nonempty system text, without semantic lesson extraction. Delegated mode asks for decisions with rationale and a schema learning note. The latter can place experience into future maintenance instructions, but actual instruction changes or improvements are unobserved ([MEM-OBJ-session-markdown](#mem-obj-session-markdown), [MEM-OBJ-wiki-schema](#mem-obj-wiki-schema), [RT-BAP-schema-prompt](runtime.md#rt-bap-schema-prompt)).
3. **Content, access metadata and instructions have different consumers.** Wiki prose informs an interpreting agent. Name/tags/description determine keyword ranking; schema prose guides maintenance; scene triggers and bootstrap instructions ask the host to consult the vault. None is a deterministic factual oracle ([MEM-OBJ-wiki-body](#mem-obj-wiki-body), [MEM-OBJ-page-metadata](#mem-obj-page-metadata), [MEM-OBJ-scene-manifest](#mem-obj-scene-manifest)).
4. **Later context is assembled rather than a full chat being replayed.** Query/search, explicit includes, keyword-ranked page sets, copied projections and installed digests select different material. Page counts are not token budgets. Children receive selected schema/index/target/report rather than the foreground session; child context retention and eviction remain external ([RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery), [RT-OBJ-ingest-prompt](runtime.md#rt-obj-ingest-prompt)).
5. **Maintenance feedback can shape another write without validating meaning.** Mechanical defects become the next child's priority list; safe semantic repairs are delegated immediately, ambiguous findings are requested as another wiki page. Stall/cap stops do not retract the prior edits, and cached copies can outlive source edits ([MEM-OBJ-lint-results](#mem-obj-lint-results), [MEM-OBJ-local-projection](#mem-obj-local-projection)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-raw
Label: Raw source documents

Source-native identity: vault `raw/<scene>/` files, with session files separately assessed below. Storage: filesystem Markdown/text. Form: natural-language evidence at ingest/query consumers; frontmatter paths/URLs are provenance/access fields, not verified truth. Lineage: supplied files, fetched pages or delegated captures. Initial authorship and reliability depend on each source and are unresolved without a real vault. Capture's user-selected URLs/results or code/model writes admit material; the maintainer is instructed to preserve it. Consumers: later ingest through file tools and search, which includes raw by default. Authority: evidence offered to an interpreting agent, not a privileged instruction role enforced by the store. Distinct artifact identity from the capture route [RT-RTE-capture-source](runtime.md#rt-rte-capture-source); not a duplicate route.

Evidence: SRC-1, `src/commands/search.ts`, `src/commands/ingest.ts`, and supplied capture record. The latter retains the direct fetch overwrite passage.

> - `raw/` — immutable source documents
> --- `templates/AGENTS.md`

The label is doctrine, qualified by actual capture writers. No source authenticity or automatic poisoning defense follows from placement in raw.

#### MEM-OBJ-session-markdown
Label: Converted and distilled session Markdown

Source-native identity: `raw/<scene>/sessions/*.md`. Storage: UTF-8 filesystem files. Form: rendered natural-language turns or semantic summaries, with symbolic source path/timing/count metadata. Original session state is outside the vault; no-argument conversion does not copy original JSONL. The caller selects a matching Codex thread ID when possible, otherwise latest modification time in bounded recursive discovery. It writes a stable derived name and skips when destination mtime is at least source mtime. Explicit mechanical input uses a date/slug path or out override and writes without that freshness check (SRC-1, `src/commands/distill.ts`).

Mechanical lineage: recognized JSON/JSONL message → normalized roles and flattened text → Markdown; tool-use names can survive, arguments and nested tool-result blocks do not. Nonempty system and textual tool messages can survive the structured path. When nothing parses, the entire input is rendered as one user message. Thus neither exhaustive transcript preservation nor uniform secret/tool/system stripping is established. These are readable transformations, not opaque checkpoints; external host checkpoint formats and compaction remain uninspected. The old `mechanicalExtract` and `buildDistillPrompt` exports are not the functions called by this command (SRC-1, `src/core/distiller.ts`, `src/commands/distill.ts`).

> if (role === 'system' && !text.trim()) return null;
> --- `src/core/distiller.ts:201-213`

> } else if (t === 'tool_result') {
>       /* 丢弃工具结果 */
> --- `src/core/distiller.ts`

Delegated lineage: input hint/role plus live schema/index → model-selected decisions, practices, examples, open questions and references → requested raw document plus brief schema append. Decisions are requested with rationale; the appended schema note is only requested to be brief and need not retain its reasons or source link. Later ingest is explicitly told to extract and cite session files, but downstream retention of complete reasons is not verified. The semantic output format lacks the mechanical output's mandatory original source-path field (SRC-1, `src/commands/distill.ts`, `src/commands/ingest.ts`).

> <List of concrete decisions made, with rationale>
> --- `src/commands/distill.ts`

> - When writing wiki pages, cite the session file under \`sources:\` and keep \`source-type: session\` where applicable.
> --- `src/commands/ingest.ts`

Consumers: later ingest and raw search, and later maintenance of any schema note actually written. This object is the retained result of [RT-RTE-session-distill](runtime.md#rt-rte-session-distill), not another declaration of that route. Trace origin can mix human requests, model responses and tool-derived text; an adapter label alone does not authenticate origin. Semantic extraction is requested curation; parser rendering is implemented transformation. Neither establishes improved future capacity.

#### MEM-OBJ-wiki-body
Label: Wiki page bodies

Source-native identity: `wiki/<scene>/<type-directory>/*.md` bodies. Storage: plain filesystem Markdown; form: natural-language knowledge including comparisons/syntheses, with wikilinks interpreted symbolically by link checks and as navigation by an agent. Lineage: agent ingestion, semantic repair, foreground saving/editing, new-page scaffolding and legacy migration. No actual page corpus was supplied. Consumers: subsequent page reads, search, injection, projections and maintenance scans. Authority: evidence/knowledge for synthesis and proposal formation, not mechanically accepted factual truth. Source links and contradiction handling are requested, not verified by normal ingest.

> 6. **When new claims contradict existing wiki content, explicitly note the contradiction** (e.g. quote both sides, link the conflicting pages, mark which source is newer) rather than silently overwriting. Preserving contradictions is how the wiki compounds honestly over time.
> --- `templates/AGENTS.md`

Evidence: SRC-1, `templates/AGENTS.md`, `src/core/wiki-index.ts`, `src/commands/ingest.ts`, `src/commands/migrate.ts`, `src/commands/new.ts`. Distinct retained object from [RT-RTE-ingest-write](runtime.md#rt-rte-ingest-write); metadata is separately assessed because its fixed selectors differ from the body consumer.

#### MEM-OBJ-page-metadata
Label: Page metadata and computed wiki index

Source-native identity: YAML frontmatter, basename IDs, outbound links, and `buildWikiIndex` result. Storage: persistent page headers plus recomputed in-process objects, not a separately persisted semantic/vector index in this helper. Form: symbolic fields/rules at ranking and validation consumers; descriptions are natural-language at model consumers. Lineage: templates/user/model headers and parsed body links; invalid YAML becomes empty metadata with full original content as body. Name/type/scene have fallbacks in the computed index. Required fields are name, description, type and scene; sources are optional. Mechanical validity therefore does not establish provenance completeness (SRC-1, `src/core/schema.ts`, `src/core/wiki-index.ts`).

> export const REQUIRED_FIELDS: (keyof Frontmatter)[] = ['name', 'description', 'type', 'scene'];
> --- `src/core/schema.ts`

Keyword scoring uses basename ID, name, tags and description, not body text. Exact ID/name/tag or substring matches receive fixed weights, nonpositive scores are discarded, then results are capped. Project keyword extraction reads package metadata/dependencies, README heading/bold text and bold text in existing local AGENTS. Inject adds at most 20 keyword-selected pages; CLI glob passes default max 30. These counts are not token/character budgets. Whole selected bodies are loaded only after ranking (SRC-1, `src/core/globber.ts`, `src/commands/inject.ts`, `src/commands/glob.ts`, `src/cli.ts`).

> const text = `${page.name} ${page.id} ${tags.join(' ')} ${page.frontmatter.description || ''}`.toLowerCase();
> --- `src/core/globber.ts`

Distinct operative part of wiki files, not a duplicate of the multi-route [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery). No exact-one supplied object container exists. Basename IDs also drive link existence checks; their apparent validity is not semantic resolution or duplicate disambiguation (`src/core/linker.ts`).

#### MEM-OBJ-wiki-schema
Label: Live vault schema and appended learning notes

Source-native identity: agent-specific vault schema Markdown, seeded from `templates/AGENTS.md`. Storage: filesystem. Form: natural-language behavior guidance plus symbolically parsed include directives. Initial writer is init code copying a shipped template or fallback; caller chooses invocation/path/agent, not necessarily each instruction. User/agent editing is possible; delegated distillation explicitly requests appending experience notes. Read-back: later ingest/lint/distill reload and inline the live file; inject Markdown emits its body, stripping include lines, while include resolution chooses additional files (SRC-1, `src/commands/init.ts`, `src/commands/distill.ts`, `src/commands/ingest.ts`, `src/commands/lint.ts`, `src/commands/inject.ts`).

> After writing the file, also update ${vault}/${contextFile} if it exists, appending a brief note about this session's key learnings.
> --- `src/commands/distill.ts`

This is the durable instruction endpoint behind [RT-BAP-schema-prompt](runtime.md#rt-bap-schema-prompt), distinct from the temporary [RT-OBJ-ingest-prompt](runtime.md#rt-obj-ingest-prompt). Session-derived additions can shape later maintenance through interpretation. The stored note's rationale/source completeness and actual causal influence are unknown; no learned parameter update is implied. Static seeded doctrine alone is not trace-fed learning.

#### MEM-OBJ-index-log
Label: Wiki catalog and action history

Source-native identity: vault `index.md` and `log.md`. Storage/form: filesystem natural-language catalog and dated log headings. Init creates both. Ingest/semantic lint request catalog additions and appended action history; `logCommand` mechanically reads existing history and rewrites it with a supplied dated entry. This implements append-shaped content, not a storage-level append-only invariant or concurrent append transaction (SRC-1, `src/commands/init.ts`, `src/commands/ingest.ts`, `src/commands/lint.ts`, `src/commands/log.ts`).

> await writeFileUtf8(logPath, existing.trimEnd() + '\n\n' + line);
> --- `src/commands/log.ts`

Later maintenance inlines catalog text; schema query doctrine tells an agent to read it. Search/glob/inject keyword indexing instead rebuilds metadata from wiki files, so a stale catalog and current directory scan are distinct views. The log records actions/optional notes, not guaranteed retained reasons or an established automatic replay consumer. Its mere persistence does not establish trace-fed behavioral revision. Distinct durable outputs of [RT-RTE-ingest-write](runtime.md#rt-rte-ingest-write) and [RT-RTE-semantic-lint](runtime.md#rt-rte-semantic-lint), not duplicate routes.

#### MEM-OBJ-lint-results
Label: Mechanical feedback and semantic findings

Source-native identity: `LintReport` issue objects and requested `overviews/lint-report-YYYY-MM-DD.md`. Mechanical report storage/form: symbolic in-process object/JSON, optionally terminal or watcher-log text; prior report survives to a subsequent child in the same loop, not a guaranteed cross-session issue database. Producers: wiki parse/link/frontmatter rules. Consumer: prompt builder turns up to 200 issues into natural-language fix priorities; model selects edits. Orphans are detected from wiki-to-wiki inbound links, not the root catalog; an instruction to link only from index need not satisfy this checker (SRC-1, `src/commands/lint.ts`, `src/core/linker.ts`, `src/commands/ingest.ts`, `src/core/ingest-lint-loop.ts`).

> for (const issue of report.issues.slice(0, 200)) {
> --- `src/commands/ingest.ts`

Semantic findings storage/form: requested ordinary wiki prose, with catalog/log updates, for later human/agent review. Safe fixes are requested directly; ambiguous findings are not automatically resolved by storage. Ordinary search/read/index routes can expose a written findings page; no dedicated mandatory reviewer consumer is wired in the inspected prompt/loop. Distinct outputs of [RT-RTE-semantic-lint](runtime.md#rt-rte-semantic-lint) and [RT-RTE-watch-repair](runtime.md#rt-rte-watch-repair), rather than a new shared route. Structural feedback is not factual ground truth.

#### MEM-OBJ-local-projection
Label: Copied local wiki subset and generated includes

Source-native identity: project `.llmwiki/local/wiki/` and generated `AGENTS.md`, or explicit into path. Storage/form: copied Markdown bodies/headers and natural-language warning plus symbolic include directives. Lineage: metadata scoring → copies with force → regenerated include list. Consumer: local include injection or a host's explicit local reads; selecting files establishes delivery capability, not host activation. The writer's force copy overwrites selected local edits but does not delete unmatched old copies. A stale file left behind is reachable by direct read or directory search even after its generated include disappears (SRC-1, `src/commands/glob.ts`).

> await cp(page.path, destPath, { force: true });
> --- `src/commands/glob.ts`

The template's “regenerates local” wording must not be read as complete garbage collection. A global deletion/rename does not revoke old copies through this function. Distinct durable artifact within [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery), not a second primary wiki or a duplicate route.

#### MEM-OBJ-scene-manifest
Label: Scene descriptions and consultation triggers

Source-native identity: `wiki/<scene>/_scene.md` frontmatter name, description, triggers. Storage: Markdown/YAML file. Form: symbolic arrays/fields when parsed, natural-language consultation guidance when rendered into host context. Lineage/admission: reader accepts existing files with a name; no manifest authoring operation or initial author is established by this reader. That unknown does not obscure the known parser/render transformation. Missing manifests fall back to requested scene name with empty description/triggers (SRC-1, `src/core/scene-manifest.ts`, `src/core/context-block.ts`, `src/commands/context.ts`).

> const data = matter(content).data as Record<string, unknown>;
>   if (!data['name']) return null;
> --- `src/core/scene-manifest.ts`

Consumer: context install/refresh for bound scene names, then host model reading rendered triggers and paths. Force is a request to consult scene files, not an event classifier implemented by memex. Binding does not filter the digest's page list, which is built from all wiki pages. Distinct retained selection guidance behind [RT-BAP-host-bootstrap](runtime.md#rt-bap-host-bootstrap).

#### MEM-OBJ-context-registry
Label: Installed context registry

Source-native identity: `~/.llmwiki/contexts.json` entries keyed by normalized project plus agent. Storage/form: filesystem JSON symbolic control metadata, not knowledge payload. Lineage: install/refresh upserts; uninstall removes. Fields include project, agent, host, mode, installation time and optional scenes, but no per-entry vault. Consumer: refresh-all dispatches writes to registered hosts using the invocation's resolved vault (SRC-1, `src/core/context-registry.ts`, `src/commands/context.ts`).

Refresh-all renders using existing scenes, then upserts without scenes. The registry implementation replaces the entry and only adds scenes when supplied. Consequently successful bulk refresh can lose scene bindings for a subsequent refresh; the first render may still contain the triggers. This bounds persistent scene-targeting claims and multi-vault assumptions.

> await upsertContext({ project: e.project, agent: e.agent, host: e.host, mode: e.mode });
> --- `src/commands/context.ts`

> ...(entry.scenes !== undefined ? { scenes: entry.scenes } : {}),
> --- `src/core/context-registry.ts`

Distinct control artifact of [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery), not page knowledge or an independent external consumer route.

#### MEM-OBJ-host-bootstrap
Label: Installed bootstrap instructions and digest

Source-native identity: marker-bounded project CLAUDE/AGENTS/GEMINI Markdown or Cursor rule. Storage: host filesystem. Form: generated natural-language instructions/page descriptions plus symbolic markers and Cursor configuration. Lineage: all wiki metadata plus optional scene manifests, registry mode and static command instructions → renderer → host-file write. Digest lists first five indexed pages per scene by default; descriptions collapse whitespace and truncate to 80 characters. It does not contain full bodies or their reasons/provenance, and bound scenes add trigger text without filtering the full digest. Minimal mode omits the digest (SRC-1, `src/core/context-block.ts`, `src/commands/context.ts`).

> return oneLine.length > 80 ? oneLine.slice(0, 77) + '…' : oneLine;
> --- `src/core/context-block.ts`

Consumer/channel/force/horizon are supplied in [RT-BAP-host-bootstrap](runtime.md#rt-bap-host-bootstrap): requested host-autoloaded guidance across sessions until replacement/removal. This object is the artifact, not a duplicate authority path. Refresh reloads current metadata, but host-loaded prior context and manually copied material are not retroactively withdrawn. Uninstall removes Markdown block/registry entry; Cursor handling empties a recognized file rather than deleting the path (`src/commands/context.ts`).

### Routes

#### MEM-RTE-query-save
Label: Foreground answer saving

Endpoints/progression: outer user question → retained page lookup/read → foreground synthesis → optional request to file a durable answer into the global wiki. Owner: foreground agent under the user/host protocol, not a separate deterministic query command. Proposer: model synthesis; decider: user save/archive request under installed query reference, or model judgment of durability under schema doctrine. User can decline saving; safety reference asks confirmation for destructive edits. No CLI transaction, reference-answer oracle or verified rollback is established for this afforded route. Mode: open query/synthesis; guidance asks citation and distinction of facts, inference and missing knowledge. Proposed durable change is a new or updated wiki answer; actual content approval and file effects are unobserved.

Distinct optional admission route from [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery)'s read/use progression; closest supplied claim [RT-CLM-management-use](runtime.md#rt-clm-management-use) already records the conflicting write guidance. Not a second declaration of either referent.

- Immediate return: requested foreground answer with cited supporting pages and missing knowledge.
- Later read-back: a saved wiki answer can reach later search, page reads, inject, maintenance or projection; unsaved chat alone establishes no memex read-back.
- Delegated visibility: foreground agent reads selected retained files; a requested write switches to ingest/distill workflow as appropriate under installed reference.
- Selection predicate: user question converted into search terms and model-chosen relevant page/link reads; saving selected by explicit user request in the query reference versus durability in schema.
- Invalidation or expiry: ordinary editable wiki content, with no special answer TTL; cached projections/host context need separate refresh.
- Activation or effect: saving and future reuse are afforded by instructions, not observed; citation delivery does not establish behavioral benefit.
- Evidence limits: no foreground transcript, saved answer or later consumption trace; which instruction the host prioritizes is unresolved.
- implementation conclusion status: afforded
- operation conclusion status: uninspected

Evidence: SRC-1, `templates/skills/ai-memex/references/query-workflow.md`, `templates/AGENTS.md`. Supplied management/use claim retains the write-only-if-requested passage.

> 4. **File the answer back as a new wiki page when it is durable** — pick the right type and directory: comparisons → `comparisons/<topic>.md`, broad surveys → `overviews/<topic>.md`, derived insights/theses → `syntheses/<topic>.md`. Don't let durable Q&A pairs disappear into chat history.
> --- `templates/AGENTS.md`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-capture-source](runtime.md#rt-rte-capture-source)

Retained content is [MEM-OBJ-raw](#mem-obj-raw); semantic admission into wiki is a later operation. Human choice of a search result is source selection, not verification of each captured claim. The supplied direct overwrite path falsifies a system-wide immutable-raw interpretation. Raw search is an alternative later consumer before ingestion; captured text need not first become wiki knowledge (SRC-1, `src/commands/search.ts`; supplied capture route).

#### On [RT-RTE-session-distill](runtime.md#rt-rte-session-distill)

The raw-to-derived-to-consumer chain is original external transcript → [MEM-OBJ-session-markdown](#mem-obj-session-markdown) → later ingest → [MEM-OBJ-wiki-body](#mem-obj-wiki-body) → query/inject/page reads. Delegated mode adds a parallel requested transcript → [MEM-OBJ-wiki-schema](#mem-obj-wiki-schema) append → subsequent management prompt path. Mechanical formatting is not equivalent to extracting lessons, and structured parsing does not apply the old helper's blanket system-role removal. The branch/fallback-specific provenance and detail losses above qualify any “complete history” description (SRC-1, `src/commands/distill.ts`, `src/core/distiller.ts`, `src/commands/ingest.ts`).

#### On [RT-RTE-ingest-write](runtime.md#rt-rte-ingest-write)

Write agency is delegated model selection/admission, with physical I/O performed by its host tools. The live schema/catalog are preselected context; the target and sources still require child discovery. Requested output lineage is source → pages plus catalog/log, with contradiction notes and citations requested by schema. The lint-priority instruction can authorize deleting an obsolete orphan in prose, while the safety reference separately requests explicit user confirmation for wiki deletion. Neither is enforced as a universal memex per-edit gate (SRC-1, `src/commands/ingest.ts`, `templates/AGENTS.md`, `templates/skills/ai-memex/references/safety-rules.md`).

#### On [RT-RTE-semantic-lint](runtime.md#rt-rte-semantic-lint)

The retained semantic report is ordinary wiki prose in [MEM-OBJ-lint-results](#mem-obj-lint-results), not a quarantined candidate store. The prompt separates direct safe repair from ambiguous findings needing review; it does not wire a subsequent reviewer or ensure contradictions are resolved. Newly created findings pages may themselves be searched/projected. Report dates do not implement expiry or acceptance state (SRC-1, `src/commands/lint.ts`).

#### On [RT-RTE-watch-repair](runtime.md#rt-rte-watch-repair)

Within-loop prior feedback is carried in memory and delivered to the next child; wiki edits are durable before the next lint. Clean triggers best-effort host projection refresh, not factual approval. The after-clean call uses refresh-all, so the registry scene-loss issue in [MEM-OBJ-context-registry](#mem-obj-context-registry) affects automatic as well as manual refresh. Watch unlink coverage is supplied runtime evidence; it does not establish removal propagation to wiki, local copies or loaded host context (SRC-1, `src/core/ingest-lint-loop.ts`, `src/commands/context.ts`, `src/core/context-registry.ts`; supplied watch route).

#### On [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery)

The request-based routes have different selectors: search scans wiki/raw content; inject resolves explicit includes and optional metadata keywords; glob copies metadata-ranked pages; foreground query reads model-chosen full pages/links. Injection's maxTokens/task fields are accepted but unused. Markdown includes schema body, JSON only file objects. An exact include is addressed delivery, not evidence of task inference. Search caps each backend/directory before scene/type filtering and final dedup/cap; default limit is ten, and wiki-first concatenation can consume that cap before raw results. Console snippets truncate to 160 characters; JSON has different display behavior. Empty output can reflect backend failure rather than absent knowledge (SRC-1, `src/commands/search.ts`, `src/commands/inject.ts`, `src/core/injector.ts`, `src/core/globber.ts`).

The push-like branch is clean-loop refresh: trigger clean structural report; code selects registered hosts plus wiki metadata/scene manifests; renderer emits count-bounded digest/descriptions and instructions into persistent host files. It does not send all page bodies into an already running model. A later host session must load those files and choose any further reads; that external contract is unobserved. No token budget or task ranking follows from default digest size (SRC-1, `src/core/ingest-lint-loop.ts`, `src/core/context-block.ts`, `src/commands/context.ts`).

#### On [RT-OBJ-ingest-prompt](runtime.md#rt-obj-ingest-prompt)

Working-context selection keeps foreground dialogue/tool exploration out of the child input supplied by memex, while retaining live schema/catalog/target and bounded prior defects. Child output and filesystem effects escape that invocation; external child history, window compaction, deletion and later provider reload are unknown. The task-frame analogy fits selected inputs and outputs at this caller boundary, not a proven host pop/eviction rule. Temporary prompt deletion is local file cleanup, not removal from provider context (supplied runtime prompt and ingestion account; SRC-1, `src/commands/ingest.ts`).

#### On [RT-BAP-schema-prompt](runtime.md#rt-bap-schema-prompt)

Session-derived schema notes have a later maintenance consumer because the live schema is reloaded each invocation. Their behavioral authority is interpreted guidance at that consumer; source content → schema append is a requested model transformation, not a fixed extractor or proven successful learning. Full raw reasoning can remain separately reachable through session files, but no guaranteed rationale link from a brief schema note is specified (SRC-1, `src/commands/distill.ts`, `src/commands/ingest.ts`; [MEM-OBJ-wiki-schema](#mem-obj-wiki-schema)).

#### On [RT-BAP-host-bootstrap](runtime.md#rt-bap-host-bootstrap)

The retained host payload is a projection with omitted bodies and truncated descriptions, not the whole wiki. Scene triggers are natural-language read guidance, while registry fields govern which files are rewritten. Missing per-entry vault and scene loss on bulk upsert bound cross-project/multi-refresh targeting. Uninstall withdraws the generated host entry, not the source wiki, old local projection or content already loaded into an external session (SRC-1, `src/core/context-block.ts`, `src/commands/context.ts`, `src/core/context-registry.ts`).

## Write side

Admission is separate from who authored material or executed filesystem writes. The mechanisms below cover initialization and alternative writers as well as delegated maintenance. A generic CLI caller may be a human or agent; invocation alone does not establish human content approval.

| Mechanism | Proposed content and admission control | Author / physical writer | Rejection, recovery and later consequence |
|---|---|---|---|
| init | Shipped schema/layout admitted after existing-vault/legacy checks; caller chooses scope/path/agent | Template authors; deterministic code writes | Refuses existing schema; no semantic review. Creates future schema/catalog inputs. SRC-1, `src/commands/init.ts` |
| direct/delegated fetch | Explicit URL/crawl rules, selected result indices or yes-all; delegated capture uses model selection | Remote author/model; helper or agent file tool | Partial failures logged, no batch rollback; same raw destination can be overwritten. Supplied [RT-RTE-capture-source](runtime.md#rt-rte-capture-source) |
| mechanical session conversion | Code accepts recognized messages or entire-text fallback; selected source and destination determine admission | Mixed transcript origin; deterministic renderer/writer | Dry-run/default freshness skip; explicit mechanical mode can overwrite. No redaction pass established. SRC-1, `src/commands/distill.ts`, `src/core/distiller.ts` |
| delegated distill | Model selects lessons and schema note using role/schema guidance; no per-note approval gate in caller | Model authors; external tools write | Failure logging/temp cleanup, not content rollback. Schema note and raw summary can have different provenance completeness. Supplied [RT-RTE-session-distill](runtime.md#rt-rte-session-distill) and direct prompt read |
| ingest | Model interprets target/source/schema, admits wiki edits directly; collaboration is requested protocol | Source authors/model; host tools | Safety asks confirmation, CLI does not enforce each write; partial edits remain on failure. Supplied ingestion route; direct prompt/schema reads |
| lint/repair loop | Code diagnoses structural defects; model decides repairs; semantic scan judges safe versus unresolved | Code report/model repair; host tools | Stop/cap/no-change does not undo edits; clean is structural only. SRC-1, `src/commands/lint.ts`, `src/core/ingest-lint-loop.ts` |
| scaffold new | Code admits template after valid type/nonempty name and destination-exists checks; not a vetted knowledge assertion | Template authors/caller name; code | Existing target refused. No catalog/log update in this function; empty description/source fields need later editing. SRC-1, `src/commands/new.ts`, `templates/source.md`, `templates/synthesis.md` |
| explicit log | Caller supplies action/target/note, code requires nonempty action | Caller authors; code rewrites full log | No claim check or atomic multiwriter append established. SRC-1, `src/commands/log.ts` |
| migrate | Valid legacy summary subtype selects fixed type/header/directory transformation; body kept | Existing page author; deterministic code | Dry-run, invalid subtype skip, conflict skip; writes target then removes source, no whole-vault rollback. Index/log/projections not updated here. SRC-1, `src/commands/migrate.ts` |
| foreground answer save/manual edit | Installed query reference requires save request; schema asks durable filing; unresolved protocol precedence | Foreground model/user and host file tools | Confirmation is instruction, actual host enforcement unknown. [MEM-RTE-query-save](#mem-rte-query-save) |
| glob projection | Caller/project keywords → fixed metadata ranking → forced selected copies and include rewrite | Existing page authors; code copies | No per-copy approval or unmatched-file cleanup; stale copies remain possible. SRC-1, `src/commands/glob.ts` |
| context install/refresh/uninstall | Initial caller chooses targets/mode/scenes; refresh software regenerates, uninstall removes managed block/entry | Renderer authors plus retained descriptions/triggers; code writes | Dry-run and per-host failure handling; no per-refresh human gate or snapshot rollback. SRC-1, `src/commands/context.ts` |
| instruction installation/product update | Caller admits shipped instructions/package changes, not a learned wiki revision | Maintainers; installer/package manager | Managed overwrite/pruning and manual recovery; no automatic semantic improvement selection. Supplied [RT-RTE-install-update](runtime.md#rt-rte-install-update) |

Maintenance can revise or remove knowledge without corresponding revocation everywhere. Schema doctrine asks preservation of both contradictory claims and consolidation of duplicate pages; semantic lint requests safe fixes/stubs and unresolved reports. Ingest lint feedback permits obsolete-orphan deletion, conflicting with safety's confirmation request. Link-check with fix flag only reports that automatic fixing is unimplemented. Migration physically removes old page paths; neither its code nor glob implements comprehensive downstream retraction. Source deletion is not a demonstrated reason to retract every derived claim. These conclusions concern the inspected commands and supplied watch registration, not all possible manual host actions (SRC-1, `templates/AGENTS.md`, `templates/skills/ai-memex/references/safety-rules.md`, `src/commands/ingest.ts`, `src/commands/lint.ts`, `src/commands/link-check.ts`, `src/commands/migrate.ts`, `src/commands/glob.ts`; [RT-RTE-watch-repair](runtime.md#rt-rte-watch-repair)).

> logger.info('Auto-fix not implemented in MVP. Agent should resolve these manually.');
> --- `src/commands/link-check.ts`

There is no basis to call mechanical formatting itself learning. The substantive trace-fed path is the delegated request to extract decisions/practices and append schema notes, followed by future schema loading. Reasons are requested in the distilled raw decisions section, but not guaranteed in the brief behavior-shaping schema note; later ingest may retrieve the raw source, not necessarily the reason behind every note. Actual improvement, reflection or exercised self-improvement requires evidence beyond this wired request and reload path.

## Read-back

| Later consumer | Trigger / selection / selected material | Delivery and budget | Authority and limits |
|---|---|---|---|
| maintenance child | New ingest/lint/distill call; code reads live schema/catalog, target/report; model discovers source/pages | Prompt or temporary-file wrapper; prior lint list max 200, no demonstrated overall token cap | Guidance/evidence interpreted by external agent; actual effect unobserved. [RT-OBJ-ingest-prompt](runtime.md#rt-obj-ingest-prompt), [MEM-OBJ-wiki-schema](#mem-obj-wiki-schema) |
| next repair child | Nonclean lint round; prior issue objects translated to high-priority repair instructions | Next invocation, bounded list; current loop report not universal cross-session memory | Fixed diagnosis feeds model decisions, not oracle-approved admission. [MEM-OBJ-lint-results](#mem-obj-lint-results) |
| foreground answering agent | User query; explicit search terms/backend/filter/cap, then model-selected full page/link reads | CLI paths/snippets/JSON followed by file reads; default ten results, display snippets 160 chars | Stored evidence supports answer; truncated result is not whole source or completeness proof. [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) |
| injection caller/outer agent | Explicit request; include paths/globs plus optional comma-separated keywords | Whole selected files; Markdown also schema body, JSON file objects only; 20 keyword pages, no implemented maxTokens/task budget | Delivery wired, host consumption unobserved. [MEM-OBJ-page-metadata](#mem-obj-page-metadata) |
| project-local later reader | glob creates copies, later include/read accesses them | Full copied pages, default CLI max 30 selections; explicit regeneration | Afforded knowledge context, not live global references; unmatched old copies may survive. [MEM-OBJ-local-projection](#mem-obj-local-projection) |
| later project host session | install/explicit refresh or clean-loop auto-refresh selects registry destinations and wiki metadata/manifests | Persistent bootstrap: default five entries per scene, descriptions truncated, optional scene trigger text; no token ranker | Requested autoloaded instructions; host loading/activation remains unobserved. [MEM-OBJ-host-bootstrap](#mem-obj-host-bootstrap), [RT-BAP-host-bootstrap](runtime.md#rt-bap-host-bootstrap) |
| semantic findings reviewer | Ordinary index/search/page access to a report, if actually written | Standard wiki page; no mandatory scheduled review consumer established | Review request is afforded, adjudication unknown. [MEM-OBJ-lint-results](#mem-obj-lint-results) |

The after-clean path is automatic persistent file supply, not an unsolicited injection API into a live host model. Exported parser/compression helpers are capabilities until a concrete caller is shown; the structured distill and loop consumers above are shown. Session capture is reimport on request, not evidence of external host compaction or checkpoint restoration. Current child exploration can remain outside foreground context; its exact eviction, provider memory and later reload are opaque ([RT-RTE-session-distill](runtime.md#rt-rte-session-distill), [RT-RTE-ingest-write](runtime.md#rt-rte-ingest-write)).

## Integration issues

1. **Additional context persistence limit:** [MEM-OBJ-context-registry](#mem-obj-context-registry) qualifies [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) and [RT-BAP-host-bootstrap](runtime.md#rt-bap-host-bootstrap). Refresh-all initially reads bound scenes, but its upsert omits them and replaces the entry. Later refresh may lose triggers; entries also lack per-vault identity while a bulk invocation supplies one vault. Evidence: SRC-1, `src/commands/context.ts`, `src/core/context-registry.ts`. This does not negate the first installed/rendered trigger path, but prevents assuming stable scene binding or vault-isolated refresh.
2. **Withdrawal implementation detail:** the runtime calls uninstall block removal; Cursor specifically empties a recognized rule file rather than deleting its path. [MEM-OBJ-host-bootstrap](#mem-obj-host-bootstrap), source `src/commands/context.ts`. This qualifies physical cleanup, not source wiki deletion or loaded-context revocation.
3. **Session label/format limits:** [MEM-OBJ-session-markdown](#mem-obj-session-markdown) adds structured parser behavior to [RT-RTE-session-distill](runtime.md#rt-rte-session-distill). Nonempty system text survives this path, nested tool results/arguments may not, and failed parsing preserves entire input as user text. The source comments' complete-history wording and generic distill label must not imply full fidelity, semantic learning or privacy filtering. Original external format coverage and actual transcript contents remain unknown.
4. **Admission guidance conflict retained:** [MEM-RTE-query-save](#mem-rte-query-save) is distinct from the supplied read route and [RT-CLM-management-use](runtime.md#rt-clm-management-use), not a replacement. Schema durable-save guidance differs from installed query opt-in saving. Ingest obsolete-page deletion guidance also differs from the safety confirmation rule. Source paths: `templates/AGENTS.md`, `templates/skills/ai-memex/references/query-workflow.md`, `templates/skills/ai-memex/references/safety-rules.md`, `src/commands/ingest.ts`. External host precedence/compliance remains unresolved; neither protocol is a universal content gate.
5. **Evaluation/read-back distinction:** [MEM-OBJ-lint-results](#mem-obj-lint-results) separates transient structural feedback from requested durable semantic findings. A findings page has ordinary retrieval paths, but no mandatory adjudicator is established in the inspected lint/loop code. Root-index links are also not counted by the current orphan checker despite prompt advice. This limits claims of accepted repairs, guaranteed closure or orphan repair by catalog update alone (`src/core/linker.ts`, `src/commands/ingest.ts`, `src/commands/lint.ts`).
6. **Artifact versus route identities:** all new objects above are retained payload/control parts behind supplied routes/authority paths, not renamed duplicates. Their nearest supplied records are cited in each declaration. No possible duplicate declaration of a supplied object was identified; schema is durable while the supplied ingest prompt is ephemeral. The optional save route overlaps the use workflow but adds distinct instruction-mediated admission. Reconciliation may connect these without superseding the valid broad routes.
7. **Unresolved operation facts:** initial source authors/trust, manifest authorship, exact external model state/history, resulting schema notes/pages, actual user approval, host loading, semantic accuracy and future benefit are not supplied. The known transformations and reload consumers remain supported; unknowns prevent observed learning or exercised self-improvement conclusions, not the architectural memory account. No new source or boundary change is required.

## Limitations and checks

Source identity was rechecked with checkout HEAD `4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f` and empty short status before source inspection. The member repeats boundary run ID/revision and supplied source identity exactly. The supplied invocation, member types, boundary/runtime members, collection, worker rules and record contract were read; source evidence stays within SRC-1. No prior analysis, target run, dependency install, agent launch or experiment was used. Fine-grained fetch extraction, all host installer variants, provider checkpoint formats, onboard interactions and real data remain uninspected rather than absent. Runtime facts used without independent full source inspection are marked as supplied above.

Deterministic output validation: passed using the invocation's `commonplace-run validate-output` command. This checks form, references and quotation occurrence, not semantic truth, operation or acceptance.
