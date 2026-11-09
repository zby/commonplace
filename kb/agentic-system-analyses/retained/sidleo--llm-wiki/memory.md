---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "llm-wiki memory: file-backed concepts, caller-mediated experience recording, derived navigation, rule injection and synchronization metadata."
run-id: AAS-2026-11-08-llm-wiki-97b740596442-01
source-identity: https://github.com/sidleo/llm-wiki
reviewed-boundary: f70e680d852a78d48504425d87252531e68c5624
---

# llm-wiki memory report

## Boundary and evidence

This account covers the knowledge-system responsibility frozen in boundary: Markdown concepts and source registration; retained directory rules; list/search/get and prompt selection; diagnostics, index/log maintenance and deprecation; bundle selection and synchronization metadata; migrations and shipped evaluation/examples. The source is SRC-1 at `f70e680d852a78d48504425d87252531e68c5624`. It is not a model runner. External hosts supply semantic synthesis, model invocation, context-window policy and any domain execution. Their transcripts, compaction state, credentials, weights and actual bundles are not supplied. Thus the report can establish file transformations and delivery paths, not model activation, factual warrant or improved capacity.

All new evidence below is implementation or attributed doctrine/design from SRC-1. No target, tests or examples were executed. Runtime findings are provisional; supplied quotations are reused by record citation. Direct source reads extended the boundary's initial scope as follows.

| Memory operation / part | Paths and inspection basis | Covering records / limit |
|---|---|---|
| File scanning, list, search, get, backlinks | Direct complete `packages/core/index.mjs`, `packages/core/lib/bundle.mjs`, `packages/core/lib/search.mjs`, `packages/core/lib/overview.mjs`, `packages/core/lib/ref.mjs`; direct CLI get, MCP search/get and pi get handler reads | [RT-RTE-bundle-read](runtime.md#rt-rte-bundle-read), [MEM-OBJ-concept-body](#mem-obj-concept-body), [MEM-OBJ-concept-metadata](#mem-obj-concept-metadata). Rendered output is not the entire stored record. |
| Create/update, provenance and source copy | Direct complete `packages/core/lib/write.mjs`, `packages/core/lib/ingest.mjs`; supplied runtime adapter admission traces | [RT-RTE-concept-create](runtime.md#rt-rte-concept-create), [RT-RTE-concept-update](runtime.md#rt-rte-concept-update), [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [MEM-OBJ-reference-source](#mem-obj-reference-source). Human approval is not authenticated by metadata. |
| Rule acquisition and read-back, context budget | Direct complete `packages/core/lib/rules.mjs`, `packages/core/lib/prompt.mjs`, `packages/mcp/lib/instructions.mjs`, `packages/codex/hooks/inject-context.mjs`, `packages/skill/SKILL.md`; supplied runtime DSH/pi lifecycle traces | [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery), [RT-OBJ-agents](runtime.md#rt-obj-agents), [RT-OBJ-append-system-prompt](runtime.md#rt-obj-append-system-prompt). Rule initialization/editing agency remains caller-dependent. |
| Structural evaluation, manual repair, withdrawal | Direct complete `packages/core/lib/validate.mjs`, `packages/core/lib/lint.mjs`, `packages/core/lib/indexlog.mjs`, `packages/core/lib/write.mjs`; CLI/tool dispatch searches | [MEM-RTE-bundle-diagnostics](#mem-rte-bundle-diagnostics), [MEM-RTE-index-refresh](#mem-rte-index-refresh), [MEM-RTE-directory-deprecation](#mem-rte-directory-deprecation). Diagnostics do not themselves revise claims. |
| Remote content and access metadata | Direct complete registry/autosync modules; Feishu ledger, status, backup, pull, push, forget and delete regions in `packages/core/lib/feishu.mjs`; supplied runtime sync/Git/DSH scheduling traces | [RT-RTE-remote-sync](runtime.md#rt-rte-remote-sync), [MEM-OBJ-wiki-cloud](#mem-obj-wiki-cloud), [MEM-OBJ-wiki-registry](#mem-obj-wiki-registry), [MEM-OBJ-wiki-autosync](#mem-obj-wiki-autosync). External service state unavailable; exhaustive Feishu sync/adopt orchestration and race safety not established. |
| Alternative production paths | Direct complete `scripts/migrate.mjs`, `scripts/migrate-to-feishu.mjs`; core serialization/export surfaces | [MEM-RTE-bundle-migration](#mem-rte-bundle-migration). These paths do not depend on gated create. |
| Shipped examples, attestation and evaluation | Direct schema frontmatter/lifecycle sections; demo join-inflation pitfall, revenue concept and SQL equality attester; first 130 lines of `scripts/smoke-test.mjs`; supplied boundary test inventory | [MEM-OBJ-concept-body](#mem-obj-concept-body), [MEM-RTE-bundle-diagnostics](#mem-rte-bundle-diagnostics). Synthetic examples and assertions are not observed sessions or attestation results. Other adapter tests, Obsidian templates and alternate-language guidance not newly inspected; no exhaustive test, template or translation-parity conclusion. |

Read-only byte comparison found each of the twelve inspected memory modules (`bundle`, `search`, `write`, `ingest`, `indexlog`, `validate`, `lint`, `overview`, `rules`, `registry`, `autosync`, `feishu`) equal between core and the four adapter `vendor-core/lib/` copies. This supports applying these specific core findings at the frozen adapter load paths; it does not certify installed packages or eliminate wrapper differences. Runtime supplies the loader account in [RT-CMP-core](runtime.md#rt-cmp-core).

## Core ideas

1. **Files, not a separate retrieval database, carry the knowledge.** A later graph rebuild reads concept bodies and selected metadata, deriving backlinks. Search returns summaries; get returns a body with backlink references. Backlink delivery surfaces related pitfalls without automatically reading their full advice ([RT-RTE-bundle-read](runtime.md#rt-rte-bundle-read), [MEM-OBJ-concept-body](#mem-obj-concept-body)).
2. **Experience recording is requested from the external agent.** The skill asks that missing facts and diagnosed pitfalls become new concepts. Core ingest only registers a source and a small Reference; it does not perform the semantic transformation. An afforded task-experience → agent-authored Pitfall → later retrieval path is present, but no autonomous transcript-to-memory pipeline or demonstrated learning follows ([RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [MEM-OBJ-reference-source](#mem-obj-reference-source)).
3. **Storage, trust labels and actual consumer input differ.** The file may retain sources, verification actors and computation bindings that the common get display omits. Confirmation gates selected creates; neither search nor get uses verified status as a universal read filter. Updating an approved file can preserve old verification entries ([MEM-OBJ-concept-metadata](#mem-obj-concept-metadata), [RT-RTE-concept-update](runtime.md#rt-rte-concept-update)).
4. **Maintenance preserves availability more than it enforces retirement.** Deprecation changes metadata, while ordinary search/get can still deliver the body. Diagnostics return structural issues; index/log maintenance produces navigation/history rather than semantic criticism. Remote deletion is a separate destructive operation ([MEM-RTE-directory-deprecation](#mem-rte-directory-deprecation), [MEM-RTE-bundle-diagnostics](#mem-rte-bundle-diagnostics), [RT-RTE-remote-sync](runtime.md#rt-rte-remote-sync)).
5. **Rules have both an executable and an interpretive consumer.** AGENTS gate extraction controls configured create calls; APPEND prose reaches host instruction channels. Broad collection, ancestor-chain requests, character limits and refresh cadence determine which retained text arrives. Delivery is not compliance ([RT-BAP-rule-delivery](runtime.md#rt-bap-rule-delivery)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-concept-body
Label: Concept body

Identity: the Markdown body of a nonreserved concept file. Form: natural-language knowledge, procedures and explanatory advice; embedded SQL/code is symbolic content only at a separate executing consumer, not because llm-wiki stores a code fence. Substrate: bundle filesystem, optionally replicated by Git or Feishu. Distinct from the runtime's rule objects and from [MEM-OBJ-concept-metadata](#mem-obj-concept-metadata); the closest supplied route is [RT-RTE-bundle-read](runtime.md#rt-rte-bundle-read), not a duplicate object declaration.

Lineage: caller-supplied text through create/update; alternatively migration, source-copy overlap or direct authoring. Semantic extraction belongs to the external agent. The demo pitfall retains a reason as well as a prescription, not just a label. SRC-1, `examples/demo-bundle/pitfalls/join-inflation.md`:

> [orders](/tables/orders.md) 与 [line_items](/tables/line_items.md) 是 1:N；若直接在订单粒度的 `total_usd` 上 join 行项再 `sum(total_usd)`，总额被放大 N 倍。
> --- `examples/demo-bundle/pitfalls/join-inflation.md`

Later consumers: lexical search reads body text internally; get delivers that concept's body to the requesting host/model. The host can interpret it as domain guidance across tasks/sessions. A backlink supplies title/type/ID references, not the linked body's reasons; a later get can load those reasons. This is knowledge delivery with interpretive force, not an enforced domain constraint. SRC-1, `packages/core/lib/search.mjs`:

> return { ...concept, backlinks, outlinks }
> --- `packages/core/lib/search.mjs`

The revenue demo points to SQL, executor instructions and an attester, but the read service does not execute those bindings. The shipped attester explicitly calls itself a demo placeholder (SRC-1, `examples/demo-bundle/references/attesters/sql-equality.md`):

> # sql-equality attester 说明（demo 占位）
> --- `examples/demo-bundle/references/attesters/sql-equality.md`

Thus neither its type nor its presence establishes an evaluated/attested computation in operation.

#### MEM-OBJ-concept-metadata
Label: Concept frontmatter and graph metadata

Identity: per-concept YAML fields, distinct from the body and reserved rules. Substrate: the same Markdown file; parsed objects/edge sets are ephemeral RAM derivatives. Form: symbolic fields at fixed code consumers (type/tag filters, IDs, status and staleness checks); natural-language title/description/source titles at host interpretation. Sources and computation/executor/attester pointers are retained provenance or capability descriptions, not evidence those targets were read or run. No counterpart object is declared in runtime; [RT-RTE-concept-create](runtime.md#rt-rte-concept-create) and [RT-RTE-concept-update](runtime.md#rt-rte-concept-update) establish the write routes.

Lineage and admission: caller supplies type, title, tags, sources and body; code stamps generated and optionally verified labels. Core create accepts extra fields, while the skill discourages custom fields. Updating merges omitted fields rather than invalidating all old provenance. This is a provenance convention, not independent source authentication. SRC-1, `packages/core/lib/write.mjs`:

> next.generated = { by: `agent:${producer}/${version}`, at: nowIso() }
> --- `packages/core/lib/write.mjs`

> const list = Array.isArray(next.verified) ? next.verified : next.verified ? [next.verified] : []
> --- `packages/core/lib/write.mjs`

Read consumers differ. Core get returns full parsed metadata, but MCP get displays type/status/runtime, description, backlinks and body; it omits sources, verified, stale_after, parameters and executor/attester/computation bindings unless duplicated in the body. CLI get also omits most frontmatter. An absolute path affords a separate host file read, not proof it happened. SRC-1, `packages/mcp/lib/tools.mjs`:

> `type: ${got.type}${got.meta.status ? ` | status: ${got.meta.status}` : ''}${got.meta.runtime ? ` | runtime: ${got.meta.runtime}` : ''}`,
> --- `packages/mcp/lib/tools.mjs`

Search indexes a fixed subset including generated.by, status and runtime, rather than all custom keys. Verified provenance is not a selection gate. `stale_after` drives lint warnings, not automatic exclusion. Back/out links are derived from body links, not typed epistemic relations (SRC-1, `packages/core/lib/search.mjs`, `packages/core/lib/bundle.mjs`, `packages/core/lib/lint.mjs`, `schema.md`).

#### MEM-OBJ-reference-source
Label: Registered raw source

Identity: the source file copied to references/refDir, distinct from the generated Reference concept. Form: opaque file payload to ingest copy; text only when UTF-8 reading succeeds, with a first-line excerpt used in the concept. Substrate: filesystem. Closest supplied record is [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest); this object is its retained input, not another route.

Lineage: explicit external caller path → sanitized basename copy, skipped if destination already exists. The concept stores resource/path/time and a short excerpt, not a complete semantic synthesis. SRC-1, `packages/core/lib/ingest.mjs`:

> const firstLine = srcText.split('\n').find((l) => l.trim() && !l.startsWith('---')) || ''
> --- `packages/core/lib/ingest.mjs`

> resource: `/${rel}`,
> --- `packages/core/lib/ingest.mjs`

The caller must read the resource separately for full-source synthesis. Non-Markdown payloads do not enter the concept graph. A copied `.md` source can itself fall within the nonreserved Markdown scan; raw and derived roles are therefore not guaranteed disjoint by directory placement. In particular the stem-based concept lookup can find the copied Markdown itself and skip creation of a separate Reference. The operation affords registration, not a uniform raw-to-derived pair for every extension (SRC-1, `packages/core/lib/ingest.mjs`, `packages/core/lib/bundle.mjs`).

#### MEM-OBJ-index
Label: Directory index

Identity: reserved index.md navigation files. Form: natural-language title/description summaries and symbolic Markdown links/type labels. Substrate: filesystem; derivation: graph → sorted directory entries. Distinct from the graph rebuilt by [RT-RTE-bundle-read](runtime.md#rt-rte-bundle-read). Core list does not use index.md as its retrieval database. Consumers are file-navigation users/hosts; regeneration is [MEM-RTE-index-refresh](#mem-rte-index-refresh). SRC-1, `packages/core/lib/indexlog.mjs`:

> const bodyText = renderIndexBody(graph, dir)
> --- `packages/core/lib/indexlog.mjs`

Root output gives top-level directory entries and counts; directory output gives direct concepts and subdirectory entries. Regeneration replaces index body content, preserving only the handled root version header; it is not a summarizing model call or a durable rationale archive.

#### MEM-OBJ-log
Label: Bundle change log

Identity: reserved log.md, distinct from [MEM-OBJ-index](#mem-obj-index) and from domain concepts. Form: textual operation entries under date headings with symbolic links; substrate: filesystem. Lineage: create/update/deprecate/ingest append operation descriptions; remote reconciliation can merge lines. It records that an operation occurred, not the old body, a complete transcript, an evaluation receipt or necessarily why a claim changed. SRC-1, `packages/core/lib/write.mjs`:

> await appendLog(root, 'Update', `Updated [${title}](${id}.md)`)
> --- `packages/core/lib/write.mjs`

Later consumers: explicit file readers and sync's log merger, not the ordinary concept graph. Raw operation retention alone supplies no automatic experience-to-policy transformation. [RT-RTE-remote-sync](runtime.md#rt-rte-remote-sync) is the closest supplied route; no supplied object has this referent. The log is derived operational history rather than raw model turns.

#### MEM-OBJ-wiki-cloud
Label: Feishu synchronization ledger and backups

Identity: `.wiki-cloud.json` access/change metadata and `.backup/<timestamp>/` copies, materially separate from concept truth/provenance. Form: symbolic JSON file tokens, directory tokens, local size/mtime, remote modification time and sync timestamps; backups retain previous file encodings. Substrate: local cache filesystem. Closest supplied route: [RT-RTE-remote-sync](runtime.md#rt-rte-remote-sync); no duplicate object.

Lineage/consumer: service listing and successful transfer results update the ledger; status/sync/delete consume it to classify changes or refuse destructive actions. It changes future synchronization decisions, not model weights or semantic beliefs. SRC-1, `packages/core/lib/feishu.mjs`:

> const localChanged = rec.localMtimeMs !== lf.mtimeMs || rec.localSize !== lf.size
>     const remoteChanged = rec.remoteModified !== rf.modifiedTime
> --- `packages/core/lib/feishu.mjs`

Pull backs up an existing local file before fetching; on failed fetch it attempts restoration. Backups are reachable for repair, not automatically selected as model context. Forget removes the ledger, not Markdown content; a later sync must re-establish its baseline. Explicit delete cleans both payload and ledger, subject to refusal and partial-failure limits.

#### MEM-OBJ-wiki-registry
Label: Named bundle registry

Identity: `~/.agents/wiki-registry.json` (environment-overridable); distinct access metadata, not retained domain content. Form: symbolic JSON mapping names to paths/backend specifications plus active name. Substrate: local filesystem, temporary file then rename on write. Caller/configuration supplies values; code normalizes and merges them with host config. Later resolver consumers select the bundle scanned or injected. Removing a registry entry removes access configuration, not its files. SRC-1, `packages/core/lib/registry.mjs`:

> if (reg.active && bundles[reg.active]) return { name: reg.active, ...bundles[reg.active] }
> --- `packages/core/lib/registry.mjs`

This object refines the selection state of [RT-RTE-remote-sync](runtime.md#rt-rte-remote-sync) and [RT-RTE-bundle-read](runtime.md#rt-rte-bundle-read), rather than duplicating either route. Per-agent/process overrides remain adapter state described by runtime; the global registry persists across sessions. Human versus software content approval is not resolved by a generic caller writing configuration.

#### MEM-OBJ-wiki-autosync
Label: Device-local autosync settings and results

Identity: `~/.agents/wiki-autosync.json` (overridable), not part of the bundle. Form: symbolic JSON enabled/interval/identity settings, lastRunAt/result counters/error and runningSince. Substrate: local filesystem with temporary-file/rename replacement. The operator/caller sets policy; DSH records sync outcomes. Later scheduling/status consumers use settings and timing markers; the last-result summary is not a domain memory or evidence of semantic improvement. SRC-1, `packages/core/lib/autosync.mjs`:

> enabled: raw.enabled === true,
> --- `packages/core/lib/autosync.mjs`

> const grace = (normalizeInterval(intervalMinutes) * 2 + 1) * 60 * 1000
>   return now - at > grace
> --- `packages/core/lib/autosync.mjs`

This is retained operational state under [RT-RTE-remote-sync](runtime.md#rt-rte-remote-sync), not a duplicate route. The timer itself is supplied-runtime evidence; no execution is observed.

### Routes

#### MEM-RTE-bundle-diagnostics
Label: Bundle validation and lint

Endpoints/progression: explicit CLI/tool/API request → graph/file inspection → errors/warnings/issues → caller. Code owns structural diagnosis; the external caller decides whether to revise content. Operating mode: open maintenance request, not a learning curriculum. Expected schema fields and dates are fixed predicates, not a factual answer oracle. The route differs from [RT-RTE-bundle-read](runtime.md#rt-rte-bundle-read): its product is a diagnostic, not retrieved advice. SRC-1, `packages/core/lib/validate.mjs`, `packages/core/lib/lint.mjs`, `packages/skill/bin/wiki.mjs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: validation ok/errors/warnings or lint issues and counts, formatted by caller adapters.
- Later read-back: inapplicable — these inspected routines do not persist diagnostic results or revise concepts; a caller can separately act through create/update.
- Delegated visibility: inapplicable — no internal model critic or subagent is called.
- Selection predicate: scan nonreserved Markdown; inspect frontmatter/type, links, orphan edges, duplicate titles, missing descriptions/indexes and stale_after versus now.
- Invalidation or expiry: recomputed on request; stale warnings depend on the evaluation time.
- Activation or effect: structured diagnosis delivered to caller, not admission enforcement or automatic semantic repair.
- Evidence limits: unknown types and optional fields are tolerated; no contradiction oracle or observed improved answer follows.

> return { ok: errors.length === 0, errors, warnings }
> --- `packages/core/lib/validate.mjs`

> issues.push({ sev: 'warn', kind: 'stale', id, msg: `${id}: 已过期（stale_after=${concept.meta.stale_after}）` })
> --- `packages/core/lib/lint.mjs`

Admission/rejection: these calls do not admit a knowledge change. A later revision is separately proposed and admitted through the supplied write routes. Calling lint is not per-content human approval, and a clean structural check is not a truth warrant.

#### MEM-RTE-index-refresh
Label: Index regeneration

Endpoints/progression: explicit index request/exported refreshIndex or write maintenance → build graph → render/write root and selected indexes → caller. Code owns deterministic navigation generation; caller chooses trigger/scope. Distinct from [RT-RTE-concept-update](runtime.md#rt-rte-concept-update), which changes concept content. SRC-1, `packages/core/lib/indexlog.mjs`, `packages/skill/bin/wiki.mjs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: refreshIndex returns paths written; individual index APIs return after writing.
- Later read-back: generated index files can be opened by later host/human file navigation; ordinary list/search/get rebuild from concepts instead.
- Delegated visibility: inapplicable — no model-worker context is created.
- Selection predicate: root plus requested dirs for updateIndex; refreshIndex adds directories containing concepts or existing index files.
- Invalidation or expiry: replacement on maintenance; stale indexes can persist if a write fails after the concept is durable.
- Activation or effect: overwrites derived navigation from titles/descriptions/type labels, not claim content.
- Evidence limits: exported refresh is a storage/maintenance capability; no deployed hypothetical file reader or successful recovery is claimed.

> await updateIndex(root, { dirs: [...dirs] })
> --- `packages/core/lib/indexlog.mjs`

Admission is deterministic rendering, not semantic selection or human content approval. No truth oracle is used. Core write routes call related index maintenance after file persistence. No automatic rollback restores a manually customized index body; concepts remain the source for regeneration.

#### MEM-RTE-directory-deprecation
Label: Directory deprecation

Endpoints/progression: caller selects directory → graph prefix selection → metadata status rewrite → log/index maintenance → adapter flush/return. Code sets the lifecycle marker; the caller decides which knowledge to retire. Mode: open maintenance. No answer oracle checks obsolescence. Proposed change is lifecycle metadata, not a new semantic assertion. This is distinct from the single-concept [RT-RTE-concept-update](runtime.md#rt-rte-concept-update), though both can change status. SRC-1, `packages/core/lib/write.mjs`, `packages/skill/bin/wiki.mjs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: deprecated and total counts, plus adapter online status when applicable.
- Later read-back: subsequent graph reads see status deprecated, but bodies remain retrievable; list can explicitly filter status.
- Delegated visibility: inapplicable — no target-side delegated model work.
- Selection predicate: all graph IDs below caller directory prefix (or whole bundle), with frontmatter and not already deprecated.
- Invalidation or expiry: marker persists until later update/edit; no expiry or removal of body occurs.
- Activation or effect: retained status and generated timestamp change; lint/list can expose retirement, but ordinary get/search do not veto it.
- Evidence limits: deprecation does not establish actual cessation of downstream use or truthful assessment of obsolescence.

> if (meta.status === 'deprecated') continue
>     meta.status = 'deprecated'
> --- `packages/core/lib/write.mjs`

Admission checks are code selection/frontmatter presence, not create's type confirmation gate. Caller can decline before invoking. Recovery is later status editing; batch file/log writes are not transactional. This is soft withdrawal, unlike Feishu explicit deletion under [RT-RTE-remote-sync](runtime.md#rt-rte-remote-sync).

#### MEM-RTE-bundle-migration
Label: Alternative bundle production by migration

Endpoints/progression: explicit script invocation → source scan/plan → dry-run report or file writes → later bundle readers; Feishu migration additionally registers remote/cache, copies Markdown, optionally refreshes index and syncs. Caller owns source/target/flags; code owns mapping and copying. Mode: bounded migration request, not a knowledge-improvement experiment. No factual answer oracle. Distinct from [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest): it converts whole legacy collections or replicates a bundle, rather than registering one source. SRC-1, `scripts/migrate.mjs`, `scripts/migrate-to-feishu.mjs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: plan, created/conflict/error report or remote initialization/sync/status results.
- Later read-back: produced .md files enter ordinary scan/search/get/rule delivery from the selected destination bundle.
- Delegated visibility: inapplicable — no target-side model worker performs synthesis.
- Selection predicate: legacy nonhidden Markdown except README; category/type inference and selected metadata remapping; Feishu migration copies nonhidden Markdown outside node_modules.
- Invalidation or expiry: legacy migration skips existing target files; source remains; Feishu copy can replace cache files before sync; no per-content verification expiry control.
- Activation or effect: metadata conversion, best-effort linkification and file retention, or bundle replication; not observed semantic improvement.
- Evidence limits: no migration executed; legacy metadata loss and copied instructions require separate downstream interpretation.

> else if (a === '--real') o.dryRun = false
> --- `scripts/migrate.mjs`

> report.conflicts.push(`${relTarget}: 目标已存在，跳过`)
> --- `scripts/migrate.mjs`

> await cp(join(from, rel), dest)
> --- `scripts/migrate-to-feishu.mjs`

Admission: migration flags (`--real` or `--apply`) authorize an operation, not demonstrated human review of each item. Legacy mapping creates process:migrate labels, infers Attested Computation from SQL presence, and drops unmapped old fields; that type inference is not attestation. Feishu migration copies reserved instruction files too and requests adopt:local sync. Neither script uses create's directory confirmation gate. Source copy preservation affords recovery of original material, not an atomic target rollback.

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-OBJ-agents](runtime.md#rt-obj-agents)

Memory-specific distinction: gate type names become symbolic admission inputs, while the remaining prose reaches interpretive readers only through explicit rule/file reading. `formatRuleAppendix` retains only gate sections from AGENTS, not the rest of its rationale. Existing rule initialization and whether edits were made by a human or model are not known from the parser. SRC-1, `packages/core/lib/rules.mjs`:

> const section = extractGateSection(r.content)
> --- `packages/core/lib/rules.mjs`

#### On [RT-OBJ-append-system-prompt](runtime.md#rt-obj-append-system-prompt)

Persistent domain instructions can be edited as files independently of concept create/update. Subsequent reads transform them into by-value text, subject to adapter limits; this is a cross-session behavioral-authority affordance, not evidence-responsive self-revision by itself. The skill explicitly directs file creation for these rules (SRC-1, `packages/skill/SKILL.md`); authorship/approval of actual bundle instructions is unresolved.

#### On [RT-RTE-bundle-read](runtime.md#rt-rte-bundle-read)

Selection chain: external host requests list/search/get; code chooses matching content; adapter delivers text to that requesting host. Search defaults to 20 results in core and emits ID/type/title/description/score, not passages. Get's backlinks expose related concept references without loading their full body. The displayed absolute path is access metadata, not a targeted selection algorithm. MCP search/get cap at maxGetChars (default 40000); MCP get can cut the body after references and suppress full stored metadata. CLI get prints the body and rule appendix separately. SRC-1, `packages/core/lib/search.mjs`, `packages/core/lib/ref.mjs`, `packages/mcp/lib/config.mjs`, `packages/mcp/lib/tools.mjs`, `packages/skill/bin/wiki.mjs`:

> return { text: lines.join('\n').slice(0, limits.maxGetChars) }
> --- `packages/mcp/lib/tools.mjs:291-291`

The get display in MCP and pi has no automatic rule appendix, unlike CLI. No trust/staleness filter is applied in searchGraph or getConcept. Thus stored provenance, lifecycle and actual model-visible evidence are not equivalent. This limits any interpretation that a retrieved computation was delivered with its attester or verified identity.

#### On [RT-RTE-concept-create](runtime.md#rt-rte-concept-create)

Caller authors proposed body/metadata; adapter code can reject configured types lacking a confirmation flag; core performs physical writes. These are separate roles. The skill asks for a human decision but flags/actor strings do not authenticate one. A create retained as unverified can still be consumed on a later read. The updated index is a derivative navigation surface; the log does not retain the full proposal or approval exchange. Source support is the supplied route plus `packages/core/lib/write.mjs` and [MEM-OBJ-log](#mem-obj-log).

#### On [RT-RTE-concept-update](runtime.md#rt-rte-concept-update)

The transformation is caller-directed replacement of body or merge of metadata, not automatic distillation of traces. Core keeps old body when omitted and old fields when unspecified; it refreshes generated regardless of whether the semantic change is independently checked. Old verified entries can survive without reapproval. The later get display does not reliably expose that distinction. Existing verified labels therefore describe retained provenance, not a mandatory fresh correctness gate ([MEM-OBJ-concept-metadata](#mem-obj-concept-metadata); SRC-1, `packages/core/lib/write.mjs`).

#### On [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)

Raw input may be external prose, binary data or task-derived material; the source path alone cannot classify trace origin. Copy registration and Reference creation are deterministic; the external agent's subsequent synthesis is afforded through the ordinary writes, not automatically performed. Minimum raw-to-derived support is the excerpt/resource stored in [MEM-OBJ-reference-source](#mem-obj-reference-source), with the Markdown-extension overlap noted there. No source correctness or freshness reconciliation follows from an existed flag.

#### On [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery)

Push context: lifecycle/initialize triggers cause code to collect root plus all nonhidden subdirectory APPEND files, ordered root first then directory name, independent of task relevance. The selector's inputs are bundle resolution, files and adapter configuration. MCP's session layer defaults to 12000 characters; its fixed SECTION_TEXT sits outside that session-layer cap. Truncating the assembled prefix can exclude later directories/rule endings; a broad collection is not complete delivery. Direct rules calls select an ancestor chain or broad collection by arguments and return requested text, subject to adapter output limits. SRC-1, `packages/core/lib/bundle.mjs`, `packages/mcp/lib/config.mjs`, `packages/mcp/lib/instructions.mjs`:

> return `${SECTION_TEXT}\n\n${context}`
> --- `packages/mcp/lib/instructions.mjs`

Codex persists only a session-keyed digest of rendered context under PLUGIN_DATA/context or a temporary fallback. This is symbolic suppression metadata, not a saved readable rule snapshot or chat summary. It compares the rendered/truncated text: changes outside that text need not change the digest. SessionStart forces delivery; other submissions skip an unchanged digest. SRC-1, `packages/codex/hooks/inject-context.mjs`:

> const stateFile = join(stateDir, sha256(sessionId) + '.sha256')
>   const digest = sha256(text)
> --- `packages/codex/hooks/inject-context.mjs`

These controls keep external text out or omit redundant additions; they do not remove old host turns, retain a verbatim conversation tail, or create an isolated worker frame. The stack-frame analogy does not apply. Files remain reachable through tools and host file access; pointers/path display are not live model-window references. External host compaction/reload semantics remain uninspected beyond the hook's stated SessionStart purpose. Runtime supplies DSH TTL/epoch and pi fresh-read behavior; these are different refresh cadences, not evidence of identical context at each model call.

#### On [RT-RTE-remote-sync](runtime.md#rt-rte-remote-sync)

Retention parts: Git history/local files; Feishu local Markdown/cache plus ledger/backups; registry active choice; device-local autosync settings/results. Their consumers and encodings are distinct in [MEM-OBJ-wiki-cloud](#mem-obj-wiki-cloud), [MEM-OBJ-wiki-registry](#mem-obj-wiki-registry) and [MEM-OBJ-wiki-autosync](#mem-obj-wiki-autosync). Automatically retaining counts/errors is operational trace retention, not trace-fed semantic learning. Remote changes become knowledge or instructions only after later file/graph/context reads. Sync's comparisons concern file identity/content changes, not truth or behavioral benefit.

Ordinary no-delete sync can resurrect a one-sided deletion. Explicit delete must remove both payload sides and ledger; it can stop after partial irreversible effects. Forget only drops access/change metadata. SRC-1, `packages/core/lib/feishu.mjs`:

> await rm(join(s.cacheDir, CLOUD_INDEX_FILE), { force: true })
> --- `packages/core/lib/feishu.mjs`

> delete idx.files[p.rel]
> --- `packages/core/lib/feishu.mjs`

Thus deregistration, ledger forgetting, deprecation and destruction are four different withdrawal effects. None proves that already delivered text was removed from an external model's context.

## Write side

**Acquisition and admission.** Domain input comes from external callers and authoring tools, not a target-owned model. Source registration copies raw input and may create a minimal Reference; semantic synthesis then needs agent interpretation and separate writes. Create's human-confirmation protocol is not universal: update, ingest, migration, exported core calls and direct file editing remain alternative production paths. The table and supplied write records distinguish these admissions; invocation consent does not imply review of each content item ([RT-RTE-concept-create](runtime.md#rt-rte-concept-create), [RT-RTE-concept-update](runtime.md#rt-rte-concept-update), [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [MEM-RTE-bundle-migration](#mem-rte-bundle-migration)).

**Requested curation and trace origin.** The skill asks agents to record missing facts after exploration and Pitfalls after diagnosing causes. The demo shows explanatory advice that could shape later action, but is synthetic retained content, not an observed trace transformation. SRC-1, `packages/skill/SKILL.md`:

> - 踩了坑 / 查出根因 → 记 `Pitfall`；与用户确认过的口径/约定 → 记 `Metric` 或 `Attested Computation`
> --- `packages/skill/SKILL.md`

The afforded chain is task observation → external agent's authored concept → code persistence → later lexical/get/file reader → host interpretation. No supplied execution establishes those links as exercised together. There is no need to treat operation logs or autosync counters as semantic learning merely because they persist. Equally, missing execution evidence does not erase the caller-mediated learning affordance. Whether a real concept preserves its reasons depends on authored body content; the demo does, the terse operation log does not, and backlinks alone do not deliver those reasons ([MEM-OBJ-concept-body](#mem-obj-concept-body), [MEM-OBJ-log](#mem-obj-log)).

**Maintenance and rejection.** Structural validation/lint report problems without directly changing the store. Separate writes admit correction; refresh rebuilds navigation. Rejected create proposals are returned to the caller rather than retained as a rejection corpus by core. Feishu conflicts and backups concern transfer/recovery, not claim evaluation. Deprecation retains the body and does not enforce read exclusion; explicit delete removes files but cannot recall already emitted text ([MEM-RTE-bundle-diagnostics](#mem-rte-bundle-diagnostics), [MEM-RTE-index-refresh](#mem-rte-index-refresh), [MEM-RTE-directory-deprecation](#mem-rte-directory-deprecation), [RT-RTE-remote-sync](runtime.md#rt-rte-remote-sync)).

**Working context.** The inspected target has no transcript compaction/checkpoint-summary producer. Its relevant mechanisms are retrieval on request, broad/scoped instruction selection, display compression (titles/types rather than full paths in overview), output truncation, caching and Codex digest suppression. These alter what is supplied, not the host's accumulated window. Their evidence is the read/context records, not an inference about host internals. No distributed-parametric memory or internally changing model parameters are established; external providers remain outside this source boundary.

## Read-back

| Retained material | Trigger / selector / selected parts | Delivery and later consumer | Authority and limit |
|---|---|---|---|
| Concept text/metadata | Host-requested list/search/get; lexical query + type/tag/limit or explicit ID/title/prefix | Tool text/stdout to requesting host/model; direct file navigation is also afforded | Interpretive domain knowledge; body/reasons require get or file read. Search returns summaries; no warrant implied. [RT-RTE-bundle-read](runtime.md#rt-rte-bundle-read). |
| Raw sources | Explicit resource/file request after registration | Host file-reading capability, not automatic ingest-result delivery of the entire payload | Full synthesis consumer not wired inside core; copied Markdown may also be scanned as a concept. [MEM-OBJ-reference-source](#mem-obj-reference-source). |
| APPEND / AGENTS | Automatic lifecycle collection or requested rules/CLI appendix; broad tree versus ancestor chain | Host prompt channels or returned rule text; parsed gate result separately consumed by create code | Natural-language instruction versus executable type veto. Caps/cache/reload differ; no reliable compliance result. [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery), [RT-BAP-rule-delivery](runtime.md#rt-bap-rule-delivery). |
| Index and log | File navigation; regeneration and sync merge | File readers and maintenance code, not ordinary graph retrieval | Navigation and operation history, not transcript-derived criticism. [MEM-OBJ-index](#mem-obj-index), [MEM-OBJ-log](#mem-obj-log). |
| Registry, ledger, autosync state, digest | Resolver, status/sync/delete, scheduling or later hook invocation | Code consumers choose bundle/transfer/admission/injection behavior | Symbolic operational control; not semantic knowledge or model training. [RT-RTE-remote-sync](runtime.md#rt-rte-remote-sync), [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery). |
| Backup / Git history | Explicit recovery; pull failure may restore backup | Filesystem repair, then later ordinary readers of restored content | Recovery affordance, not autonomous truth-based memory rollback. [MEM-OBJ-wiki-cloud](#mem-obj-wiki-cloud), [RT-RTE-remote-sync](runtime.md#rt-rte-remote-sync). |

No route here establishes that a later model acted differently because of a particular retained item. Persistence across invocations is supported by file reads/writes; activation and capacity improvement remain unobserved. Static shipped skill/prompt guidance is distinguished from through-use retained content: it can request read-back without itself being accumulated memory.

## Integration issues

1. **Consumer display is narrower than the core return.** [RT-RTE-bundle-read](runtime.md#rt-rte-bundle-read) correctly distinguishes core data from formatting but needs the memory qualification in [MEM-OBJ-concept-metadata](#mem-obj-concept-metadata): common get displays omit verified, sources, stale_after and computation bindings. Consequence: one cannot infer source-warrant or attestation visibility merely from retrieval of a concept. Direct MCP/CLI/pi handler reads establish this; no duplicate route is declared.
2. **MCP documentation promises a fallback that the inspected get handler does not implement.** `packages/mcp/lib/instructions.mjs` says rules are appended by core on get/create/update. `packages/core/lib/search.mjs` returns the concept/links only; the MCP get handler renders body/backlinks and returns without an appendix. CLI explicitly calls rulesAppendix. This corrects that source-native promise, not runtime's narrower CLI-specific finding. [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) should not be read as universal per-tool rule delivery. Explicit wiki_rules remains available; actual host use is unobserved.
3. **Raw/Reference roles overlap for Markdown ingest.** [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) is valid as a registration route, but a separate derived Reference is not produced uniformly. [MEM-OBJ-reference-source](#mem-obj-reference-source) identifies the copied `.md` / stem lookup case. Consequence: do not classify every ingest as semantic distillation or assume copied raw files stay outside graph retrieval.
4. **Retirement is consumer-dependent.** [MEM-RTE-directory-deprecation](#mem-rte-directory-deprecation) qualifies the runtime update lifecycle account; no supplied record is a duplicate of this batch route. Search/get still read deprecated material. Delete, deregister and forget have different effects. No recall of already supplied model context is established.
5. **Unresolved evidence questions.** Actual rule/concept initialization authorship and per-content human approval; whether an external agent synthesizes registered sources or retains experience with reasons; whether a later host reads omitted provenance/resources, follows backlink references or obeys delivered rules; exhaustive remote sync/adopt/race outcomes and external host compaction contracts remain uninspected. Relevant records are [RT-RTE-concept-create](runtime.md#rt-rte-concept-create), [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery), [RT-RTE-remote-sync](runtime.md#rt-rte-remote-sync). These prevent operational reliability/learning/compliance conclusions, not the bounded implementation account.

New objects distinguish retained parts absent from runtime's object declarations; new routes identify diagnostics, navigation regeneration, batch deprecation and migration rather than relabeling supplied routes. No possible duplicate remains identified after those comparisons. Existing rules and ordinary write/read/sync routes receive annotations instead of new IDs.

## Limitations and checks

Source HEAD was rechecked and equals the boundary pin. Source identity and run identity repeat the invocation and boundary exactly; governing job, member types, collection, worker rules and records contract were read from the supplied method paths. No separate method-commit value was supplied to this role, so none is inferred from the worktree. Additional coverage and deliberately uninspected surfaces are listed above. No new source ID, live service evidence, prior analysis or target execution was used.

The source supports a persistent knowledge and instruction delivery architecture with caller-mediated curation. It does not establish autonomous experience extraction, semantic truth checking, improved model capacity, exercise of retained behavioral changes, or prompt compliance. Structural test assertions and demo provenance remain attributed examples, not authenticated operational history. Those limits coexist with the implemented write/read paths.

Validation: the required commonplace-validate command passed: “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” The check establishes form and quotation occurrence, not analytical correctness or workflow acceptance.
