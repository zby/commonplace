---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Arsumbris memory: file-backed typed knowledge, declared graph/guidance consumers, session ledger and host state within the entry-repository boundary."
run-id: AAS-2026-10-15-arsumbris-a9be6bac297f-01
source-identity: https://github.com/arsumbris/arsumbris
reviewed-boundary: "716bb14f2bf50e249d414525c8e07c50478fc786"
---

# Arsumbris memory report

## Boundary and evidence

This report covers the file substrate and its graph consumers, profile-selected guidance, raw session events, host configuration/state and device-local access metadata. The frozen boundary is the complete entry artifact, not the sibling engine/host/MCP implementations. It inherits the Source register of [boundary](boundary.md#source-register): SRC-1 at `716bb14f2bf50e249d414525c8e07c50478fc786`. Most conclusions are documentary contracts. Only device seeding has inspected implementation. No execution evidence establishes activation or benefit.

Direct reads: SRC-1, `README.md`, `INSTALL.md`, `au-engine.md`, `au-host.md`, `au-mcp.md`, `MIGRATION.md`, and the complete `scripts/seed-device-config.py`. The supplied runtime supplies the safety passage and bootstrap/extension findings. These sources do not contain the sibling packages' actual knowledge, skills, governance procedures, ingestion transforms or evaluators. The exclusion prevents conclusions about their curation, selection and evaluation, not a finding that those mechanisms do not exist.

| Entry/operation | Source path and inspection | Coverage / missing fact and prevented conclusion |
| --- | --- | --- |
| Repository/workspace declarations, indexing, direct `au daemon start .`, versioned reads/subscriptions | `au-engine.md`, direct documentary read | [MEM-OBJ-knowledge-files](#mem-obj-knowledge-files), [MEM-OBJ-type-definitions](#mem-obj-type-definitions), [MEM-OBJ-live-graph](#mem-obj-live-graph), [MEM-RTE-graph-reuse](#mem-rte-graph-reuse); no engine dispatch implementation or query algorithm here. |
| MCP file tools, engine reads, native redirects, hooks, ledger | `au-mcp.md`, direct documentary read | [RT-RTE-mediated-action](runtime.md#rt-rte-mediated-action), [MEM-OBJ-session-ledger](#mem-obj-session-ledger); read tracking, event schema and ledger replay unknown. |
| Skills, graph-walk injects, computed session-start context, adapter launch | `au-mcp.md`, direct documentary read | [RT-BAP-profile-guidance](runtime.md#rt-bap-profile-guidance) and annotation; exact selector, budget and delivered bodies unavailable. |
| Host file access, config saving, composition, viewStore, selection/focus/preview | `au-host.md`, direct documentary read | [RT-RTE-host-edit](runtime.md#rt-rte-host-edit), [MEM-OBJ-view-store](#mem-obj-view-store) and annotation; config reload and local-state durability unverified. |
| Diagnostics, rename/move/delete preview, workspace removal | `au-engine.md`, `MIGRATION.md`, direct documentary reads | [MEM-RTE-graph-reuse](#mem-rte-graph-reuse), [MEM-CLM-maintenance-limits](#mem-clm-maintenance-limits); no general deletion/withdrawal/revalidation implementation. |
| Extension discovery/load/rebuild, version adoption/refusal | `au-host.md`, `au-mcp.md`, `MIGRATION.md`, `INSTALL.md`, direct documentary reads | [RT-RTE-extension-load](runtime.md#rt-rte-extension-load); guidance/code editing afforded, no trace-fed update established. |
| Device registry/template/tool paths and bootstrap | `scripts/seed-device-config.py`, direct implementation read; `INSTALL.md`, direct documentary read | [RT-OBJ-device-config](runtime.md#rt-obj-device-config), [RT-RTE-device-seeding](runtime.md#rt-rte-device-seeding) and annotations; downstream readers absent. |
| Knowledge-package ingest, research, rules, writing and governance | `INSTALL.md`, direct documentary inventory | Outside frozen source: package names and purpose only; substantive admission/curation and later reuse cannot be traced. |
| Harness model state, compaction, sub-agent frames, provider memory | `INSTALL.md`, `au-mcp.md`, direct documentary reads | [RT-CMP-agent-harness](runtime.md#rt-cmp-agent-harness); no context-isolation/compaction contract or checkpoint alternatives supplied. |

## Core ideas

1. Files, not the live graph, are the declared durable knowledge substrate. The graph is a cross-repository, in-memory interpretation updated on file changes. Natural-language knowledge and symbolic type constraints have different consumers; a graph representation does not make all content symbolic.
2. Type errors are retained as diagnostics, not admission vetoes. Read-before-write mediation is another control: it checks a prior read, not truth, relevance or content approval. Host and ordinary filesystem edits remain alternative admission paths. See [RT-CLM-diagnostic-saves](runtime.md#rt-clm-diagnostic-saves) and [RT-CLM-mediation-floors](runtime.md#rt-clm-mediation-floors).
3. Profiles control intended agent context through triggered skills, always-on graph-walk injects and per-session computed injection. The documentation establishes selection/delivery intent but neither exact retained knowledge selected nor successful model consumption.
4. Session events and device paths must not be mistaken for distilled experience. Events are raw traces with no shown trace-to-guidance transformation; paths enable resolution/launch rather than encode domain knowledge. These distinctions survive even though all can influence later work.

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-knowledge-files
Label: Repository knowledge files

Source-native identity: Git-tracked repositories of Markdown/YAML plus indexed untyped assets. Storage is files; Markdown bodies can be natural-language content, while frontmatter fields and references participate in symbolic graph rules. Media/assets remain opaque payloads here; indexing as an untyped member establishes neither textual extraction nor model-visible summaries. Initial knowledge provenance and per-content human approval are unspecified. Later graph clients and projections can request changed content; an agent interprets delivered prose rather than receiving mechanically guaranteed instructions. Distinct from [RT-OBJ-device-config](runtime.md#rt-obj-device-config), which locates repositories, and [RT-OBJ-agent-profile](runtime.md#rt-obj-agent-profile), which selects session surfaces. No supplied record declares this content substrate. SRC-1, `au-engine.md`:

> You scope different areas of work into their own git-tracked repo.
> --- `au-engine.md`

> The engine will parse markdown and YAML,
> and the type system only applies on those filetypes for now.
> But media files or other assets are also be indexed as untyped members.
> --- `au-engine.md`

#### MEM-OBJ-type-definitions
Label: Type definitions

Source-native identity: YAML type definitions, including fields, inheritance, reference constraints, body requirements and metadata. Storage is repository files; symbolic constraints are interpreted by the engine, whereas prose `guidance` requires human/model interpretation if delivered. Definitions are authored, not shown automatically learned from traces. Their declared authority is structural diagnosis and discovery; invalid knowledge remains readable/savable. A field's prose guidance is not shown being enforced as a semantic check. Executable-entry metadata also affects extension discovery, separately covered by [RT-RTE-extension-load](runtime.md#rt-rte-extension-load); this record describes the type substrate, not another loader. No supplied object counterpart. SRC-1, `au-engine.md`:

> You define your own types in a small YAML typing language.
> --- `au-engine.md`

> # optional body
> body:
>   - section: My Section
>     fills: myInlineOrRef
>     guidance: "Must contain a contribution to myReference"
>     body:
>       - section?: My Optional Subsection
> --- `au-engine.md`

#### MEM-OBJ-live-graph
Label: Live cross-repository graph

Source-native identity: one in-memory graph over mounted repos. Representational form: symbolic parsed members, relations and type/diagnostic structure; source prose remains interpreted content when read. Lineage is file indexing and change-driven updates, not trace-based abstraction. Graph durability is not asserted: durable files are separate from the declared in-memory index. Consumers include engine clients, MCP plugins and host projections. Their graph access supports retrieval/discovery and diagnostics; it does not establish adoption of content as warranted knowledge. No supplied object counterpart; the graph is state used by, not identical to, [RT-RTE-host-edit](runtime.md#rt-rte-host-edit) and [RT-RTE-mediated-action](runtime.md#rt-rte-mediated-action). SRC-1, `au-engine.md`:

> It indexes every mounted repo (deps) and holds them as one graph in memory.
> Change a file, and the graph updates.
> --- `au-engine.md`

#### MEM-OBJ-session-ledger
Label: Session event ledger

Raw trace, not a derived knowledge artifact. The source declares per-session event appends but gives neither physical storage/durability nor exact event payload schema. Its representational form is a symbolic event sequence with payload contents unresolved; readable tool-result strings do not establish the complete ledger payload. [RT-RTE-mediated-action](runtime.md#rt-rte-mediated-action) already describes the producer; this distinct object is its retained trace result, not a duplicate route. No later replay, summarization, evaluator or trace-to-instruction consumer is established by SRC-1, `au-mcp.md`. Read tracking (`ctx.hasRead`) exists in an example, but the source does not say that it is reconstructed from the ledger.

> - `observe` — every event is appended to the session's ledger.
> --- `au-mcp.md`

#### MEM-OBJ-view-store
Label: Per-viewer local state

Source-native identity: `viewStore`, distinguished from the shared composition. This is an opaque operative part of host state: serialization, storage location, lifetime, retained payloads and reload mechanism are not given. The named interface affords viewer state but cannot establish durable cross-session memory. Local UI state is distinct from shared pane configuration in [RT-RTE-host-edit](runtime.md#rt-rte-host-edit); no supplied record declares this store. Selection/focus/preview channels are current UI coordination, not proven retained memory. SRC-1, `au-host.md`:

> - `viewStore` — per-viewer local state, kept outside the shared composition.
> --- `au-host.md`

### Routes

#### MEM-RTE-graph-reuse
Label: Changed-file graph reuse

Endpoints: file author/writer → repository files → engine index/diagnostics → later engine client, projection or agent tool. Trigger: a file change and a later read/query/subscription. The writer proposes content; engine code owns indexing and structural diagnostics. Human per-content control depends on the writing route: direct editing can supply text, while launching an agent or accepting arbitrary projection code does not establish approval of every write. Initial content and historical reasons are unspecified. This is ordinary open editing, not a documented curriculum or improvement experiment; there is no answer oracle. Guidance bodies shaping proposals are outside the source. Rejection is route-dependent: MCP can deny unread writes, while diagnostic errors explicitly do not block save/read. Rollback/recovery implementation is unavailable; Git-tracked storage alone is not an implemented rollback workflow.

This route isolates the declared file-to-later-consumer chain shared by [RT-RTE-mediated-action](runtime.md#rt-rte-mediated-action) and [RT-RTE-host-edit](runtime.md#rt-rte-host-edit), plus direct filesystem writes and engine clients. It is not a replacement for either route and is not a part of exactly one. The graph is refreshed from files, not shown to distill their meaning or retain author reasoning. SRC-1, `au-engine.md`, and the diagnostic passage in [RT-CLM-diagnostic-saves](runtime.md#rt-clm-diagnostic-saves) support the chain.

- Immediate return: engine-facing reads observe a version; subscriptions stream changes; exact write acknowledgments and diagnostic result layouts are unspecified here.
- Later read-back: changed durable files can reach subsequent engine reads and host file rendering by declared contract; a specific later agent invocation and its delivered context are unobserved.
- Delegated visibility: uninspected — a shared graph is described, but per-session grants, sub-agent inputs and cross-session boundaries are not supplied.
- Selection predicate: entry repo, dependencies and edit/discover membership determine the mounted domain; explicit repository/path selects a file read. A requested path is not evidence of automatic relevance targeting; graph-walk selection for injects is separately unresolved.
- Invalidation or expiry: file changes update the graph by declaration; edit members are live and discover members pinned. Cache eviction, stale-reference cleanup, reindex atomicity and retained history are uninspected.
- Activation or effect: declared retrieval/rendering/diagnostics over changed files; no observed later decision or benefit established.
- Evidence limits: documentary graph and host interfaces only; no engine/host/plugin implementation or observed consumer invocation.
- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

> - The daemon serves consumers over a Unix socket.
> - Reads observe a version.
> - Mutations go through one guarded write path.
> - Subscriptions stream changes.
> --- `au-engine.md`

The supplied [RT-RTE-host-edit](runtime.md#rt-rte-host-edit) carries the host file-read/write consumer passage. Repo-targeting defaults are qualified by SRC-1, `MIGRATION.md`:

> - **A read or write that names no repo** now scopes to the served entry repo, not the shallowest one. Pass `repo` explicitly where you relied on the old default.
> --- `MIGRATION.md`

### Claims

#### MEM-CLM-maintenance-limits
Label: Maintenance and withdrawal limits

The documented maintenance surface includes diagnostics, mutation previews and workspace membership changes, but the entry artifact does not trace withdrawn content into every later cache, injection or session. Thus neither diagnostic rejection of knowledge nor complete withdrawal propagation is established. This adds source-native maintenance details to [RT-CLM-diagnostic-saves](runtime.md#rt-clm-diagnostic-saves), not a duplicate of its save contract. SRC-1, `MIGRATION.md`:

> - **`remove_workspace_member`** refuses to remove the repo that contains the workspace.
> --- `MIGRATION.md`

> - **`PreviewMutationOp` gained `rename`, `move_dir` and `delete_dir`.** A `switch` over it that must be exhaustive needs the three new cases.
> --- `MIGRATION.md`

A preview operation name establishes an API vocabulary, not an exercised delete or a later-consumer invalidation guarantee. For extensions, incompatible runtime metadata can prevent load, and changed projections require rebuild/reload; [RT-RTE-extension-load](runtime.md#rt-rte-extension-load) retains those passages and conditions. Retained files need not be deleted merely because executable loading was rejected.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-OBJ-device-config](runtime.md#rt-obj-device-config)

Access metadata, not source knowledge. Symbolic YAML persists on the local filesystem. Lineage: repository manifests and existing registry rows → parsed name/path mappings; template paths → ordered gallery list; discovered executables → tool paths. Descriptions are printed during discovery but not retained in the name/path registry. No author reasoning is serialized. Existing locations survive rediscovery, including conflicts; missing repositories are not automatically evicted. Documented consumers are host startup/gallery and engine resolution, not the model as domain context. SRC-1, `scripts/seed-device-config.py`:

>     for name in sorted(merged):
>         lines.append(f"  - name: {yaml_scalar(name)}")
>         lines.append(f"    path: {yaml_scalar(merged[name])}")
> --- `scripts/seed-device-config.py`

#### On [RT-RTE-device-seeding](runtime.md#rt-rte-device-seeding)

Write agency is caller opt-in via `--write`, then deterministic discovery/merge, not human approval of each entry. Preserving user entries is not authentication or content curation. The seeder itself rereads existing config on subsequent invocations, establishing an implemented later merge consumer even though host/engine read-back remains documentary. Registry rewrite drops original comments; tool paths preserve existing top-level keys. These are configuration transformations, not trace-fed learning. SRC-1, `scripts/seed-device-config.py`:

>     existing = parse_repos_yaml(engine_cfg)
>     merged = dict(existing)                         # preserve existing rows (and their locations)
> --- `scripts/seed-device-config.py`

#### On [RT-BAP-profile-guidance](runtime.md#rt-bap-profile-guidance)

The retained guidance source is repository content; full bodies and initial provenance are unavailable. Skills combine symbolic frontmatter selection metadata with a Markdown instruction body. Inject instances seed a graph walk; session-start hooks compute injection per session. The profile determines eligible skills/injects/hooks; the adapter materializes them for the harness. Graph-walk traversal, stopping rules, trust ranking, byte/token budgets, exact selected parts and rendered payloads are not supplied. Always-on delivery is intended automatic supply, while a triggered skill's exact trigger owner and matching predicate remain unknown. Computed injection is a context transformation, but its inputs and whether it derives anything from accumulated traces are unknown. It cannot be classified as trace learning merely because it runs at session start.

The later consumer is the harness agent, through interpreted natural language, not a symbolic validity gate. Static shipped guidance is context configuration rather than read-back under the record contract; changed guidance would become read-back only if consumed in a later invocation, a chain not demonstrated here. No trimming, retained summary, verbatim tail, reload stub or sub-agent frame is specified. Consequently the stack-frame lens has no evidenced application within this entry artifact; the graph is externally queryable data, not a model-window reference/liveness mechanism. Evidence: SRC-1, `au-mcp.md`, launch-guidance passage already retained in the supplied record, and:

> au-mcp-adapter-cc/bin/launch.ts   # materializes the skills/injects, prints the spawn command
> --- `au-mcp.md`

#### On [RT-RTE-host-edit](runtime.md#rt-rte-host-edit)

Shared composition/pane configuration is symbolic pool entries and references persisted by `saveConfig`; exact storage and reload path are unspecified. Its authority is UI arrangement/configuration, separate from prose delivered to an agent. The file read example renders returned content to a projection, providing a documented consumer rather than merely an unused storage API. `viewStore` is separately opaque. Unmount cleanup disposes a subscription, not retained knowledge or file history. SRC-1, `au-host.md`:

> A composition arranges projection INSTANCES into a workspace.
> It is its own type (not a projection). The host always opens a composition.
> --- `au-host.md`

>   host.files.read('README.md').then(r => render(r.content))   // read the graph (engine-backed)
> --- `au-host.md`

## Write side

The knowledge write paths have different admission mechanisms. [MEM-RTE-graph-reuse](#mem-rte-graph-reuse) separates proposed file content from structural checks. [RT-RTE-mediated-action](runtime.md#rt-rte-mediated-action) describes automatic mediator admission and possible `ask`; no approval presentation/persistence contract is supplied. [RT-RTE-host-edit](runtime.md#rt-rte-host-edit) describes UI/code file writes and saved pane config. Ordinary filesystem changes are also an explicit graph-update trigger, so MCP floors cannot establish universal admission. Diagnostics do not veto content. There is no supported truth-ranking admission mechanism at this boundary.

Type/guidance/code authoring is afforded by composable repos and extension examples, but actual authoring instructions are outside this source. Knowledge-package names such as ingest and governance are not evidence of their transforms. SRC-1, `INSTALL.md` describes `au-ingest` as:

>   - `au-ingest` (files → typed source notes), and the `au-tree-research` feature package.
> --- `INSTALL.md`

This is a declared acquisition purpose, not an inspectable raw-to-note-to-consumer path. No claim is made about lost reasons, human approval, summarization, embedding or evaluator results inside those absent package bodies.

[MEM-OBJ-session-ledger](#mem-obj-session-ledger) retains raw events by declaration. No source passage supplies automatic raw-ledger → derived instruction/summary → later model consumption, compaction or alternative checkpoint forms. Known file indexing and config merging remain positive transformations despite unresolved provenance elsewhere; neither is a semantic trace-fed revision. Maintenance/rejection/withdrawal limits remain local to [MEM-CLM-maintenance-limits](#mem-clm-maintenance-limits). Device discovery prunes fixtures, preserves previous entries and requires explicit write mode; it is automatic configuration maintenance after caller authorization, not per-content curation.

## Read-back

The best-supported reuse contract is durable changed files → live graph → later read/render, [MEM-RTE-graph-reuse](#mem-rte-graph-reuse). Direct engine clients, host projections and agent-facing file/engine tools are alternative consumers, not interchangeable evidence of model context. Versioned reads and subscriptions provide access/change delivery; no automatic semantic relevance ranker or context budget is specified. Knowledge scope is selected through entry/dependency/workspace membership, with live edit and pinned discovery sets (SRC-1, `au-engine.md`).

Profile-guided delivery is annotated on [RT-BAP-profile-guidance](runtime.md#rt-bap-profile-guidance). Its graph-walk seed is a targeting input, but that fact does not reveal the selected retained material or its final representation. Source trust is likewise only partially specified: repository membership admits indexed content, and stamper hooks are described as folding trustworthy metadata into writes. That label alone supplies no provenance verification algorithm or model trust guarantee (SRC-1, `au-mcp.md`):

> - `stamper` — fold trustworthy metadata into a governed write.
> --- `au-mcp.md`

Device files have an implemented later merge consumer and documented launch/resolution consumers. Shared composition has a documented later host-use role but no inspected reload. Viewer-local state and the ledger have no established later read route. The read-guard's prior-read state influences mediator decisions, but neither its physical store nor ledger lineage is specified. These limits prevent a system-wide claim of durable session replay, experience distillation or learned guidance.

## Integration issues

- Additive clarification to [RT-RTE-device-seeding](runtime.md#rt-rte-device-seeding): its host/engine consumers remain documentary, but the seeder itself implements subsequent configuration read/merge. The source read and passage are in its annotation. This narrows any interpretation that *all* later consumers are uninspected; no contradiction with the record's explicit host/engine limit is required.
- [MEM-RTE-graph-reuse](#mem-rte-graph-reuse) overlaps the retained-result/read side of [RT-RTE-mediated-action](runtime.md#rt-rte-mediated-action) and [RT-RTE-host-edit](runtime.md#rt-rte-host-edit), while adding direct engine/filesystem paths. Distinct identity: shared file-to-index-to-later-consumer chain, not either complete initiating route. Reconciliation should connect them rather than substitute one for another.
- [MEM-OBJ-session-ledger](#mem-obj-session-ledger) makes explicit an object mentioned by [RT-RTE-mediated-action](runtime.md#rt-rte-mediated-action); no competing object declaration is supplied. Its schema, durability, later reader and relationship to `hasRead` remain unresolved; event retention cannot warrant trace learning.
- [MEM-OBJ-view-store](#mem-obj-view-store) is not shared composition configuration. Its opaque payload and lifetime prevent attributing durable viewer memory. [MEM-CLM-maintenance-limits](#mem-clm-maintenance-limits) likewise cannot establish withdrawal propagation into model contexts or caches.
- Guidance selector/budget/materialization and semantic acquisition/maintenance rules remain outside the source. [RT-BAP-profile-guidance](runtime.md#rt-bap-profile-guidance) can support intended instruction delivery, not complete knowledge read-back or successful adoption. No additional correction to supplied facts or possible duplicate declarations identified.

## Limitations and checks

HEAD was rechecked as `716bb14f2bf50e249d414525c8e07c50478fc786`; the checkout was clean. The tracked entry tree matched the supplied boundary inventory. No other source, prior analysis, target execution or model service was used. The governing job, memory/boundary/runtime types, collection, worker rules and records contract were read completely, including bounded continuations. The documentary/implementation distinction was retained throughout.

Countercases checked before settling conclusions: bad data remains readable/savable despite a guarded seam; host/external writes prevent universal MCP admission; device config is itself reread despite absent downstream implementation; session-start computation is not necessarily trace-fed; projection unmount cleanup is not knowledge withdrawal. Missing sibling code and execution evidence prevent claims of reliable injection, durable ledger replay, comprehensive withdrawal, trace-based learning or improved future behavior. These are limits, not evidenced absences.

Validation: the invocation-specific deterministic output check passed; it checks form and quotation occurrence, not semantic acceptance or operation.
