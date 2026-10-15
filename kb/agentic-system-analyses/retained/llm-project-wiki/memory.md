---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "LLM Project Wiki memory: source snapshots, compiled pages, gap records and generated maintenance rules in a prompt-only package."
run-id: AAS-2026-10-14-llm-project-wiki-c6c664168f3e-01
source-identity: https://github.com/akash-r34/llm-project-wiki
reviewed-boundary: "1fdfba9129a46afd18aa68a83f12d6716ab694c6"
---

# LLM Project Wiki memory report

## Boundary and evidence

This report covers the persistent project reference and its specified producers, maintenance operations and later model consumers. I directly read both tracked files, `README.md` and `SETUP_PROMPT.md`, completely, verified HEAD against the boundary revision, and enumerated the two-file tracked tree. SRC-1 supplies doctrine/design; the README's example counts are reported operation, not an inspected installation. The runtime findings were supplied and were checked against those direct reads. No generated vault, host session, evaluator result or target execution is supplied. The source identity and access limits remain those of [the boundary](boundary.md#source-register).

Included surfaces are source copies, compiled pages, access/freshness metadata, navigation, logs, templates, schema, generated commands, project rules and health checks. Existing project memory is an input/fallback whose actual contents and authorship are unavailable, not an independently inspected store. Provider weights and host context management remain outside this prompt-package boundary; this prevents claims about host compaction, model learning or automatic instruction loading. Obsidian/Dataview/Templater implementations and consuming project artifacts are also excluded; query execution, concrete page correctness and successful persistence/reload cannot be established.

### Coverage inventory

All source paths in the table are directly inspected SRC-1 doctrine/design. Record links identify supplied runtime declarations or this member's additions, not evidence of exercised operation.

| Entry point or memory operation | Source path | Covering records | Missing fact or bounded conclusion |
|---|---|---|---|
| Pasted setup; missing/existing vault branch; initial project/memory audit | `README.md`; `SETUP_PROMPT.md`, Step 0, Phases 0–1 | [RT-RTE-vault-bootstrap](runtime.md#rt-rte-vault-bootstrap), [RT-RTE-gap-audit](runtime.md#rt-rte-gap-audit) | Actual project input provenance and model admission outcomes unavailable. |
| Shell sync; instruction-copy header; manual copy and timestamp recovery | `SETUP_PROMPT.md`, Phase 2, G2 | [RT-RTE-source-sync](runtime.md#rt-rte-source-sync), [MEM-OBJ-sources](#mem-obj-sources) | Generated script unavailable; copies need not cover raw entity code. |
| Full build, entity/concept/decision authoring; gap heuristic | `SETUP_PROMPT.md`, Phase 3, heuristic, quality bar | [MEM-OBJ-wiki](#mem-obj-wiki), [RT-RTE-vault-bootstrap](runtime.md#rt-rte-vault-bootstrap) | Model transformations prescribed, not observed. |
| Question/edit lookup; insufficiency fallback; stale marking | `SETUP_PROMPT.md`, Phase 4 | [RT-RTE-wiki-lookup](runtime.md#rt-rte-wiki-lookup), [MEM-OBJ-index](#mem-obj-index), [MEM-OBJ-page-metadata](#mem-obj-page-metadata) | No token budget or enforced source prohibition; host loading unknown. |
| Diff ingest, dry-run, new entities and logged gaps | `SETUP_PROMPT.md`, Phase 2 | [RT-RTE-diff-ingest](runtime.md#rt-rte-diff-ingest), [MEM-OBJ-log](#mem-obj-log) | One Git comparison plus open gaps is not all stale state. |
| Status/milestone callers and memory sync checklist | `SETUP_PROMPT.md`, Phase 4, G1/G6 | [RT-BAP-maintenance-rules](runtime.md#rt-bap-maintenance-rules), [RT-BAP-project-rules](runtime.md#rt-bap-project-rules) | Optional generated callers; no shipped hook or registered tool implementation. |
| Schema, templates and maintenance commands | `SETUP_PROMPT.md`, Phases 1–2, G0/G1 | [RT-OBJ-schema](runtime.md#rt-obj-schema), [RT-OBJ-wiki-ingest](runtime.md#rt-obj-wiki-ingest), [MEM-OBJ-templates](#mem-obj-templates) | Actual conventions, plugin execution and command discovery unavailable. |
| Health dashboard, stale/index queries and self-audit | `SETUP_PROMPT.md`, Phases 1/6, G4/G5 | [MEM-OBJ-health](#mem-obj-health), [RT-CLM-audit-completeness](runtime.md#rt-clm-audit-completeness) | Diagnostics do not demonstrate semantic correctness or full validation. |
| Existing-vault repair; link/schema fixes; manual refresh; protocol revision | `SETUP_PROMPT.md`, G0–G7 | [RT-RTE-gap-audit](runtime.md#rt-rte-gap-audit) | Direct source read and copy are alternate admission paths; live adoption unobserved. |
| Git tracking and manuals | `SETUP_PROMPT.md`, Phase 5; `README.md`, Usage | [MEM-CLM-retention-limits](#mem-clm-retention-limits) | Files are intended to be committed; no installed Git history or rollback procedure supplied. |
| CLI/library/service dispatch, compaction and checkpoint alternatives | Complete two-file tracked tree | [RT-OBJ-setup-prompt](runtime.md#rt-obj-setup-prompt), [RT-CMP-claude-code](runtime.md#rt-cmp-claude-code) | Package ships instructions and embedded examples, not these implementations. Host alternatives are uninspected, not proven absent. |

## Core ideas

The specified mechanism is **model-authored compilation followed by page-first lookup**, not embedding search. A future model reads a question/intent table and relevant pages before falling back to pre-existing memory or source. The compiled pages retain full excerpts, constraints and cross-references; selection reduces requested breadth rather than imposing a measured context limit. See [RT-CLM-wiki-first](runtime.md#rt-clm-wiki-first) and [MEM-OBJ-wiki](#mem-obj-wiki).

Two different update chains must not be collapsed. Source sync copies project memory/docs; diff ingest interprets changes into Wiki pages. Question-time gaps are retained as task-derived error reports, then used by ingest or audit to guide later page creation. A raw gap log is not itself compiled knowledge, and copying alone does not update knowledge. These chains are prescribed, not observed ([RT-RTE-source-sync](runtime.md#rt-rte-source-sync), [RT-RTE-diff-ingest](runtime.md#rt-rte-diff-ingest), [MEM-OBJ-log](#mem-obj-log)).

Freshness and authority are interpretive protocols. `status: stale` supports maintenance/status decisions, while the archived instruction header asks readers not to treat selected copies as live rules. Neither is host access control. The concrete countercases—manual copy, unheaded Memory/Rules copies, one-commit diff selection, and broader audit/source fallback—qualify literal immutability, automatic freshness and universal wiki-only use ([RT-CLM-sources-immutability](runtime.md#rt-clm-sources-immutability), [RT-RTE-gap-audit](runtime.md#rt-rte-gap-audit)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-sources
Label: Sources snapshots

Source-native identity: generated `Sources/Memory/`, `Sources/Rules/`, `Sources/Docs/`. Substrate: project vault files intended for Git tracking. Natural-language memory/docs/rules coexist with literal configuration or code excerpts; fixed shell copying transports bytes without semantic compilation. The selected instruction-copy header is natural-language trust guidance for a model, not a symbolic enforcement boundary. Lineage is copying existing project files through adapted rsync or G2 manual copy, plus that header insertion. Original human/model authorship is installation-specific and uninspected. Consumers are bootstrap, ingest and audit models; snapshots have reference authority, not intended live instruction authority (SRC-1, `SETUP_PROMPT.md`, Phases 1–3, G2).

No supplied object counterpart after comparison with [RT-OBJ-schema](runtime.md#rt-obj-schema) and [RT-OBJ-wiki-ingest](runtime.md#rt-obj-wiki-ingest): those are maintenance instructions, not copied source content. [RT-RTE-source-sync](runtime.md#rt-rte-source-sync) declares the producer route, not this store.

> │   ├── Memory/       ← will hold memory file snapshots
> │   ├── Rules/        ← will hold rules/config snapshots
> │   └── Docs/         ← will hold root docs and any design docs
> --- `SETUP_PROMPT.md`

The supplied source-sync record retains the copying/header passages. The standard pattern copies memory, rules and docs, not every raw entity source file. Phase 3's demand to read every Sources file therefore does not alone establish codebase coverage; Phase 0 inspection and G3 direct code scans are additional paths. The actual adapted script remains unknown.

#### MEM-OBJ-wiki
Label: Compiled Wiki page content

Source-native identity: generated `Wiki/` pages of six specified types, excluding the separately assessed `_Health` dashboard and access metadata. Substrate: Markdown files in a tracked vault. Primary consumption is natural-language model interpretation; literal signatures/schema/code excerpts retain symbolic form where read as code, but their inclusion does not execute them. Lineage: model synthesis from project audit, Sources and targeted code reads, followed by model section revisions and audit repairs. Consumers: later question/edit models, status callers and maintenance models. Authority: task knowledge and reference constraints at lookup; not a separately enforced instruction hierarchy (SRC-1, `SETUP_PROMPT.md`, Phases 1, 3–4, G3).

Distinct from [RT-OBJ-schema](runtime.md#rt-obj-schema), which governs the pages, and [RT-RTE-vault-bootstrap](runtime.md#rt-rte-vault-bootstrap), which produces them. No supplied page-content object counterpart after comparison.

> - Non-obvious implementation logic with code excerpts
> - Constraints and edge cases (not obvious things — write what a future LLM would need to know that isn't obvious from the name)
> - A `## Cross-References` section with `[[wikilinks]]` to related pages
> --- `SETUP_PROMPT.md`

> **Decision pages MUST include:**
> - The decision made
> - Why (the forces, constraints, and context that drove it)
> - What was rejected and why
> - Consequences
> --- `SETUP_PROMPT.md`

Decision rationale is explicitly requested and reaches later decision-page readers through lookup. Reasons for entity constraints may be retained as prose but are not universally required. No corresponding requirement retains the reasoning behind every maintenance-rule repair. Neither source claims nor excerpts are independently evaluated merely by inclusion.

#### MEM-OBJ-page-metadata
Label: Page lineage and freshness metadata

Source-native identity: Wiki frontmatter `type`, `updated`, `status`, `sources`, and entity `source_file:`. Substrate: Markdown frontmatter. Representational form: symbolic keys/string values for grep/query consumers; model-interpreted labels during authoring and maintenance. Lineage: templates and model writes, updated by stale marking, ingest and audit. Consumers include stale-page queries, source/path grep, status fallback and maintenance models. This is access/lineage metadata, not the page's domain knowledge. Source references afford dependency tracking but do not prove supported content or complete provenance (SRC-1, `SETUP_PROMPT.md`, Phases 1–4, G5).

No supplied metadata object counterpart after comparison with [RT-OBJ-schema](runtime.md#rt-obj-schema), the specification rather than its instances. [RT-RTE-wiki-lookup](runtime.md#rt-rte-wiki-lookup) and [RT-RTE-diff-ingest](runtime.md#rt-rte-diff-ingest) manipulate/select these instances.

> - Frontmatter schema for each type (required fields: `type`, `updated`, `status`, `sources`)
> --- `SETUP_PROMPT.md`

> - `source_file:` frontmatter pointing to the exact file
> --- `SETUP_PROMPT.md`

Stale-marking grep and ingest dependency grep use different strings; the prompt supplies no demonstrated reconciliation of their concrete path conventions. Incorrect or missing metadata can prevent selection even while the page exists. G5's incomplete presence checks are already qualified by [RT-CLM-audit-completeness](runtime.md#rt-clm-audit-completeness).

#### MEM-OBJ-index
Label: Index navigation

Source-native identity: generated `index.md`. Substrate: Markdown; natural-language question/intent mappings interpreted by the foreground model, wikilink targets consumed symbolically by navigation tools, and a specified symbolic Dataview block. Lineage: bootstrap model writes the intent table/TOC; audit checks and repairs missing page entries. Later lookup models read the index to select pages; audit models read it for inventory. Selection authority does not imply the table contains a validated or exhaustive intent mapping (SRC-1, `SETUP_PROMPT.md`, Phase 1, G0/G4).

Distinct from the instruction [RT-OBJ-schema](runtime.md#rt-obj-schema) and the consuming [RT-RTE-wiki-lookup](runtime.md#rt-rte-wiki-lookup); no supplied object counterpart after comparison.

> 2. A **Semantic Lookup** table: "question / intent → wiki page" (15–20 entries covering the most common LLM questions about this project)
> 3. A full TOC grouped by domain, with `[[wikilinks]]` to every wiki page
> --- `SETUP_PROMPT.md`

No embeddings, ranking algorithm or numerical retrieval budget is specified for this table. The supplied package supports semantic matching by a model, not a claimed dense-vector mechanism.

#### MEM-OBJ-log
Label: Activity and gap log

Source-native identity: generated `log.md`. Substrate: append-only Markdown by instruction. Natural-language entries with formatted operation/time/subject/count metadata. Lineage: bootstrap and ingest summaries, task-time gap notes, source-staleness notes and audit summaries. Gap origin is the model's encounter with missing/wrong wiki coverage during a project task; other records summarize maintenance actions. These are task/maintenance reports, not verbatim conversation or tool traces. Actual author compliance, error provenance and append-only enforcement are uninspected (SRC-1, `SETUP_PROMPT.md`, Phases 1, 4, 6, G0/G2/G7).

Distinct from [RT-OBJ-schema](runtime.md#rt-obj-schema), which defines grammar, and [RT-RTE-diff-ingest](runtime.md#rt-rte-diff-ingest), which consumes gaps and appends results; no supplied log-object counterpart after comparison.

> 2. Read `log.md` — find the most recent `ingest` timestamp and any open `[gap]` entries
> --- `SETUP_PROMPT.md`

> This tells you: when the wiki was last updated, what was intentionally deferred, and what the maintainer already flagged as missing. Do not re-discover things that are already logged.
> --- `SETUP_PROMPT.md`

The Phase 4 gap format retains a topic, task and one-sentence diagnosis; Phase G retains issue categories and result counts. This is enough to request later repair/defer rediscovery, not a full claim/test/result/blame history. The prompt calls entries `[gap]` but its displayed entry says `gap |`; concrete parsing and closed-gap representation are unspecified.

#### MEM-OBJ-templates
Label: Page templates

Source-native identity: generated six files in `Templates/`. Substrate: vault template files. Representational form: symbolic placeholder/frontmatter structures where emitted by Templater, with natural-language section guidance interpreted during page authoring. Lineage: bootstrap creation; G3 uses these files for missing pages. Templates guide prospective content; they are not accumulated task traces. Concrete plugin syntax and execution are unavailable (SRC-1, `SETUP_PROMPT.md`, Phase 1, G3).

Distinct from [RT-OBJ-schema](runtime.md#rt-obj-schema), the governing conventions; no supplied template-object counterpart after comparison.

> Six Templater template files (one per page type). Each must emit correct frontmatter with all required fields pre-filled with `<placeholder>` values. Include a `## Cross-References` section stub in each.
> --- `SETUP_PROMPT.md`

#### MEM-OBJ-health
Label: Wiki health dashboard

Source-native identity: generated `Wiki/_Health.md`. Substrate: Markdown containing specified Dataview queries. Query form is symbolic under plugin interpretation; model/human readers interpret displayed results as diagnostic guidance. Lineage: bootstrap generation and G1 repair. Consumers: maintenance readers/plugin rendering; results select stale, old, orphan and schema-violation candidates, not independently verified false domain claims. No concrete query body or observed display is supplied (SRC-1, `SETUP_PROMPT.md`, Phase 1, G1).

Distinct from compiled page content and [RT-CLM-audit-completeness](runtime.md#rt-clm-audit-completeness), a claim about validation; no supplied dashboard-object counterpart after comparison.

> Dataview-powered health dashboard with four queries:
> - Stale pages (`status: stale`)
> - Old pages (`status: current` AND `updated` > 30 days)
> - Orphan candidates (entity/concept pages with `file.inlinks` length = 0)
> - Schema violations (pages missing `type` or `updated`)
> --- `SETUP_PROMPT.md`

The age expression is a requested condition, not inspected query semantics. Its listed schema diagnostic covers fewer fields than the full schema requirement. Query results do not autonomously repair pages.

### Routes

none declared in this member

### Claims

#### MEM-CLM-retention-limits
Label: Retention without specified withdrawal

Claimed operation: vault content persists across project sessions through files and intended Git tracking; housekeeping excludes only per-machine UI state. The inspected prompt asks to create/update/fix pages, resolve gaps and correct links, but supplies no explicit obsolete-page retirement, source-deletion propagation or rollback protocol. This bounded finding prevents inferring that deleted source entities stop influencing future lookup. The example sync lacks a deletion flag, so it does not by itself remove destination copies when project files disappear (SRC-1, `SETUP_PROMPT.md`, Phases 2/5, G3/G4).

Distinct from [RT-CLM-sources-immutability](runtime.md#rt-clm-sources-immutability): this concerns retention/deletion rather than write permissions or instruction authority. This is a limit on the inspected specification, not an absence claim about generated installations.

> Keep tracked: `community-plugins.json`, `core-plugins.json`, all `Wiki/` and `Sources/` files.
> --- `SETUP_PROMPT.md`

> Fix each orphan by adding a wikilink to it from the most relevant existing page. Fix each broken link by either creating the missing page or correcting the link text.
> --- `SETUP_PROMPT.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-OBJ-schema](runtime.md#rt-obj-schema)

Memory-specific lineage: model-written conventions are retained in the vault, then requested as the first input to later maintenance. Curation can repair missing cadence/loop text during G6. Initial installation-specific content and its human/model provenance remain unknown. Authority at the actual intended consumer is maintenance instruction, not project-domain knowledge. The source distinguishes bootstrap-only Full Ingest from preferred Diff-Based Ingest (SRC-1, `SETUP_PROMPT.md`, Phase 1, G0/G6).

> - Operations: Diff-Based Ingest (preferred), Full Ingest (bootstrap only), Lint, Query
> - Ingest cadence: when to run (after every sync, at session start if stale, after merges)
> --- `SETUP_PROMPT.md`

#### On [RT-RTE-vault-bootstrap](runtime.md#rt-rte-vault-bootstrap)

Memory write agency is the foreground model: it transforms inspected sources into pages and creates navigation, templates and maintenance guidance. User pasting and later committing are not per-page approval. Admission guidance is the entity/decision rules, domain audit and quality bar. The generated source copies are reference input; compiled pages retain selected excerpts and reasons rather than a complete raw task trace. Initial read-all-Sources and domain-by-domain work specify scope but no context budget or isolated worker-return contract (SRC-1, `SETUP_PROMPT.md`, Phases 0–3/6).

> This is the main work. Read every file in `Sources/` and build out `Wiki/`. Work domain by domain.
> --- `SETUP_PROMPT.md`

#### On [RT-RTE-wiki-lookup](runtime.md#rt-rte-wiki-lookup)

Read-back is request-driven: question/intent → index mapping → selected retained Wiki pages → foreground model's current context. Page snippets are loaded by value; index links are navigation targets, not live references into the context window. There is no prescribed token budget, trimming or summary checkpoint. Insufficiency allows fallback and yields a retained diagnosis; targeted edits yield freshness metadata. Optional status reads Current Status first and checks stale state before fallback (SRC-1, `SETUP_PROMPT.md`, Phase 4). The supplied route and [RT-CLM-wiki-first](runtime.md#rt-clm-wiki-first) retain the lookup and gap passages.

#### On [RT-RTE-source-sync](runtime.md#rt-rte-source-sync)

Memory transformation is copying plus selected header insertion, not semantic curation. Selector inputs are project path globs and rsync destination timestamps. Admission is fixed shell selection once invoked; original source authorship and whether humans separately approved it are unknown. Persistence is copied files; delivery occurs only when bootstrap/ingest/audit later reads them. The README's read-only claim permits this update route and G2 manual copy. The marker's model-interpretive trust protection applies only to the three named Docs files, not universally to Sources contents (SRC-1, `SETUP_PROMPT.md`, Phase 2/G2; supporting passages in the supplied record).

#### On [RT-RTE-diff-ingest](runtime.md#rt-rte-diff-ingest)

Retained inputs are current snapshots/pages and open gap reports; model curation updates sections, dates and new pages. This is a prescribed trace-fed update where gap reports from earlier task insufficiency can shape a durable page subsequently consumed as project knowledge. It is not parameter training, and successful learning is unestablished. No raw conversation capture or automatic log-to-rule derivation is specified. Changed-path mapping and grep are candidate selectors; gap repair is a separate admission input and can introduce pages outside a simple existing dependency match. Budget is changed sections rather than a token limit. Persistence is Wiki and log; later delivery is lookup or audit, not an unsolicited page push (SRC-1, `SETUP_PROMPT.md`, Phase 2; update/gap passages retained in the supplied route).

#### On [RT-RTE-gap-audit](runtime.md#rt-rte-gap-audit)

Read-back starts from schema, log and index, including deliberate deferrals, then expands to code and existing pages. Curation includes direct source refresh, missing-page synthesis using templates, adding/correcting links, metadata repair and rewriting operational guidance. The output's methods can reach later instruction consumers through [RT-BAP-project-rules](runtime.md#rt-bap-project-rules) and [RT-BAP-maintenance-rules](runtime.md#rt-bap-maintenance-rules); actual loading is unobserved. Audit log summaries persist findings/results but do not require reasons for each method change. This limits criticism-dependent iteration claims without denying the specified repair path (SRC-1, `SETUP_PROMPT.md`, G0–G7; supplied route retains repair passages and independent theory assessments).

## Write side

The bootstrap model admits project-specific pages and method files under the prompt's quality/schema guidance. Human initiation and eventual Git commit are workflow controls, not a mandatory content approval gate. Existing project input can be human/model-authored; the source does not identify installation-specific provenance. The read-only label is a reference-layer policy, not immutable storage ([MEM-OBJ-sources](#mem-obj-sources), [RT-RTE-vault-bootstrap](runtime.md#rt-rte-vault-bootstrap)).

Once invoked, sync mechanically admits files by globs/timestamps and inserts selected warning headers. Ingest admits model-interpreted section/page changes from changed source, existing pages and gaps. Dry-run avoids writes but no required post-preview human approval or rejection criterion is specified. Audit admits direct repairs from source comparisons and structural checks, constrained to surgical patching rather than rebuild. Wrong updates have later audit as a recovery opportunity; no transactional rollback is requested. These separate admission mechanisms are accounted for in [RT-RTE-source-sync](runtime.md#rt-rte-source-sync), [RT-RTE-diff-ingest](runtime.md#rt-rte-diff-ingest), and [RT-RTE-gap-audit](runtime.md#rt-rte-gap-audit).

The experience chain is task insufficiency → one-sentence gap report → later ingest/audit interpretation → compiled page change → later lookup. Bootstrap/ingest/audit logs also inform subsequent maintenance about coverage and deferral. They are summaries rather than raw execution traces. The heuristic permits an earlier damaging error/constraint to become page knowledge, but specifies no trace collector or demonstrated automatic extraction:

> | An error or constraint that burned you before | Note in the entity page under "Constraints" |
> --- `SETUP_PROMPT.md`

Decision pages explicitly preserve reasons/rejected alternatives for later lookup. Maintenance summaries preserve issues/results without a comparable mandatory argument record. No model-weight update, host compaction output or alternative summary/checkpoint form is described in this package; host behavior remains uninspected. Page marking and link repair retain rather than withdraw material. Source deletion, retired entities, resolved-gap notation and substantive rejection need installation-specific policy before one can infer exclusion from later consumers ([MEM-OBJ-log](#mem-obj-log), [MEM-OBJ-wiki](#mem-obj-wiki), [MEM-CLM-retention-limits](#mem-clm-retention-limits)).

## Read-back

Ordinary lookup is a pull chain initiated by a project request, selected by the model using intent mappings, and delivered as page text through host file reads. Related-page wikilinks afford further navigation, not automatic complete-graph injection. The retained index has 15–20 requested intent entries; page count or table size is not a context token budget ([MEM-OBJ-index](#mem-obj-index), [RT-RTE-wiki-lookup](runtime.md#rt-rte-wiki-lookup)).

Maintenance is another pull chain. Ingest selects Git changed paths, mapped Sources references and open gaps; audit first reads schema/log/index and then selects candidates by actual entity coverage, stale flags and diagnostics. Health displays and stale-page queries deliver metadata-derived candidate sets to maintenance readers, not independently validated truth. `/status` is an additional specified consumer of project-state knowledge; `/phase-complete` is chiefly a stale-write/sync-reminder surface, not evidence that all Wiki content is injected. A documented session-start-if-stale cadence does not establish an automatic scheduler or unsolicited push ([RT-BAP-maintenance-rules](runtime.md#rt-bap-maintenance-rules), [MEM-OBJ-health](#mem-obj-health), [RT-RTE-gap-audit](runtime.md#rt-rte-gap-audit)).

The only specified working-context control is selective external-file loading with fallback. Material remains reachable on disk but enters the model window by value when read. Parallel scans do not establish stack-like isolated sub-agent frames or controlled return values; no eviction/reload-after-compaction mechanism is specified. The live rule files instruct later sessions; archived Sources copies are intended as reference, while Wiki pages are task knowledge. These are different authority paths even if all are Markdown interpreted by the same host model ([RT-BAP-project-rules](runtime.md#rt-bap-project-rules), [RT-CMP-claude-code](runtime.md#rt-cmp-claude-code)).

## Integration issues

- No correction to a supplied runtime fact is required after direct source inspection. The runtime's source-immutability, automatic-stale-marking, dry-run and incomplete-schema-check qualifications remain supported.
- New object records have no supplied object duplicates. Sources, Wiki content, page metadata, index, log, templates and dashboard are products/inputs of supplied routes, not synonyms for those routes or for schema/command files. The retention claim overlaps the limits of source-sync and audit but has a distinct deletion/withdrawal subject ([MEM-CLM-retention-limits](#mem-clm-retention-limits)).
- Initial code coverage remains unresolved: the standard sync covers memory/rules/docs, while entity writing requires concrete code excerpts. The bootstrap audit and G3 allow broader project inspection, so there is no source-read prohibition; the concrete generated script and acquisition coverage are unavailable. This prevents inferring exhaustive bootstrap entity coverage from “read every file in Sources” ([MEM-OBJ-sources](#mem-obj-sources), [MEM-OBJ-wiki](#mem-obj-wiki), [RT-RTE-vault-bootstrap](runtime.md#rt-rte-vault-bootstrap)).
- Path consistency across `sources`, `source_file:` and dependency grep, closed-gap representation, source deletion/obsolete-page retirement and status reset after ingest are unspecified. This prevents a freshness/withdrawal guarantee for all retained content, without removing the supported change/gap/audit mechanisms ([MEM-OBJ-page-metadata](#mem-obj-page-metadata), [MEM-OBJ-log](#mem-obj-log), [RT-RTE-diff-ingest](runtime.md#rt-rte-diff-ingest)).
- G1 describes a six-step ingest and G6 refers to gap resolution in step 4, whereas Phase 2 defines seven steps with gaps at step 5. This is an internal cross-reference discrepancy, not evidence that the substantive gap instruction is missing. Generated command contents and actual repair are unavailable; completeness should be judged on content, not those step numbers (SRC-1, `SETUP_PROMPT.md`, Phase 2/G1/G6; [RT-OBJ-wiki-ingest](runtime.md#rt-obj-wiki-ingest)).
- The task-derived-gap-to-page chain supports prescribed experience-fed curation, not observed learning or theory criticism. Runtime's independent unknowns for criticism-dependent iteration and successful self-improvement should remain; audit summaries need not preserve all method-change reasons ([RT-RTE-gap-audit](runtime.md#rt-rte-gap-audit), [MEM-OBJ-log](#mem-obj-log)).

## Limitations and checks

The two-file package supports a declared persistence/maintenance/lookup design, not verified copied-source completeness, concrete page truth, actual cross-session reload, activation or benefit. I checked strong claims against alternate source-supported paths: audit/manual copy qualifies immutable sources; fallback and direct audit reads qualify wiki-only lookup; open gaps extend changed-path selection; absent deletion semantics limits freshness/withdrawal claims. I did not execute target snippets or inspect prior analyses.

Source identity recheck: Git HEAD is `1fdfba9129a46afd18aa68a83f12d6716ab694c6`; tracked paths are exactly `README.md` and `SETUP_PROMPT.md`. Method identity is the supplied job, member type, worker rules and records contract read completely for this attempt; no alternative method or source revision was substituted.

Validation: the invocation-specific deterministic output check passed. This checks structure, identity and quotation occurrence, not semantic support, operation or acceptance.
