---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "FrameCode-VibeWork memory: host-curated Markdown, bounded session handoffs, disposable retrieval and source-review metadata."
run-id: AAS-2026-11-08-framecode-vibework-d38fb53e8013-01
source-identity: https://github.com/sistema2d/framecode-vibework
reviewed-boundary: "847cdcedc02d08531961c8367f4e2ddb2dc392f1"
---

# FrameCode-VibeWork memory report

## Boundary and evidence

This report covers retained project knowledge, handoffs, source-review metadata, derived indexes/graphs, product QA knowledge and the routes that return these to later work. The frozen source is SRC-1 at commit `847cdcedc02d08531961c8367f4e2ddb2dc392f1`, as registered in [boundary](boundary.md#source-register). FCVW ships a Markdown governance system and optional Python support, not the host's model executor or transcript manager. Its memory loop combines host-performed authoring with executable discovery and checking. No target code was executed here. Python findings are implementation evidence; skill/policy/template findings are doctrine/design. No supplied execution evidence establishes use or benefit.

The supplied runtime was used as a provisional inventory, not as a source-reading limit. Direct reads added the complete wiki contract, curator, AI policy, note template, product QA guide, governance-validator skill, index builder, retriever, chunk selector, knowledge graph, source checks, product checker and decision trace. Selected MCP handlers, hook session-start/pre-edit and queue derivation/recommendation were read directly. Other runtime findings below remain attributed to the supplied records. The checkout HEAD was rechecked against the frozen revision. The analysis method is the supplied memory job, member type, worker rules and records contract; neither target instructions nor target feedback were treated as binding instructions.

| Entry point or operation | SRC-1 source paths and inspection | Coverage and conclusion limits |
|---|---|---|
| Plan/evidence acquisition and procedural revision | Supplied `AGENTS.md`, factory/self-improvement and upgrade findings | [RT-RTE-governed-change](runtime.md#rt-rte-governed-change), [RT-RTE-asset-admission](runtime.md#rt-rte-asset-admission), [RT-RTE-framework-upgrade](runtime.md#rt-rte-framework-upgrade). Host performs writes; release replacement is separate from knowledge curation. No observed content approval or later activation. |
| Curated knowledge, raw/source records and feedback | Direct `FCVW/wiki/README.md`, `FCVW/governance/TEMPLATE_NOTE.md`, curator | [MEM-OBJ-wiki](#mem-obj-wiki), [MEM-OBJ-wiki-metadata](#mem-obj-wiki-metadata), annotation on asset admission. Raw imports and attributed feedback are not validated derived knowledge. Initial imported content approval remains unspecified. |
| Session close, resume and archive | Direct `FCVW/AI.md`, curator and wiki lifecycle | [MEM-OBJ-session](#mem-obj-session), [MEM-RTE-session-handoff](#mem-rte-session-handoff). Alternative checkpoint is QA discovery frontier, not a hidden transcript store. |
| Markdown indexing and lexical/graph retrieval | Direct `tools/build_context_index.py`, `tools/retrieve_context.py`, `tools/context_selection_fcvw.py` | [MEM-OBJ-context-index](#mem-obj-context-index), [MEM-RTE-index-build](#mem-rte-index-build), annotation on [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery). APIs expose selection capacity; the CLI is a concrete caller. No automatic index freshness rejection. |
| Typed graph, digests, due dates and review candidates | Direct `tools/knowledge_graph_fcvw.py`, `tools/knowledge_sources_fcvw.py` | [MEM-OBJ-knowledge-graph](#mem-obj-knowledge-graph), [MEM-RTE-source-review](#mem-rte-source-review). Warnings and graph relationships do not themselves edit or reject claims. |
| Selected-section reads, routing, digest, validator and next-plan MCP tools | Direct `tools/mcp_server_fcvw.py` handlers and `tools/plan_queue_fcvw.py` derivation/recommendation | Annotation on [RT-RTE-mcp-checks](runtime.md#rt-rte-mcp-checks). Section reads and plan queue consume retained state despite not writing memory. Dependency evaluator internals were not independently inspected; no claim that dependency evidence is semantically true. |
| Session-start push and edit/stop checks | Direct `tools/hook_fcvw.py` session-start/pre-edit; supplied activation and stop findings | Annotation on [RT-RTE-hook-lifecycle](runtime.md#rt-rte-hook-lifecycle). Plan filenames cross into host context; not plan bodies, session summaries or automatic compaction. Host registration/honoring outputs is unobserved. |
| Product inventory, expectations, exact runs and checkpoint | Direct `FCVW/skills/QA/PRODUCT_WIKI.md`, `tools/qa_wiki_fcvw.py` | [MEM-OBJ-product-contract](#mem-obj-product-contract), [MEM-OBJ-qa-run](#mem-obj-qa-run), [MEM-RTE-product-review](#mem-rte-product-review). Browser/application execution is external; checker verifies declared scope, not truth. |
| Optional semantic review and deterministic lint | Direct governance-validator skill and source/graph/product checks; supplied validator/local-driver records | [MEM-RTE-source-review](#mem-rte-source-review), [RT-RTE-local-checks](runtime.md#rt-rte-local-checks). Semantic review is an advisory host procedure, not an inspected model service. Full validator/test internals were not independently audited, preventing exhaustive enforcement claims. |
| Navigation graph and generated catalog | `tools/document_graph_fcvw.py` function/CLI inventory; wiki contract; supplied boundary | Separate link/reachability mechanism from typed graph. Full body uninspected: no detailed link-resolution or generated-catalog completeness claim. It does not substitute for the inspected typed graph route. |
| Cross-tool traces and local reports | Direct `tools/trace_fcvw.py`, retrieval/product trace call sites; supplied local-check driver | [MEM-OBJ-decision-trace](#mem-obj-decision-trace), [RT-RTE-local-checks](runtime.md#rt-rte-local-checks). Logs are evidence, not demonstrated trace-fed memory updates. |
| JIT skills and delegated contexts | Direct AI loading policy; supplied [RT-RTE-work-packages](runtime.md#rt-rte-work-packages) | Static shipped instructions are not use-accumulated memory. Revised skills can become later behavioral guidance. Host allocation, return serialization, trimming, provider state and exact live context remain outside the source. |

Excluded host transcripts, model weights, deployed application records and live external sources prevent claims about hidden memory, automatic provider compaction or real-task quality. They do not erase the known file-based transformations. Packaging/localization and repository administration are within the system boundary but are not separate memory consumers established here; upgrade effects are retained through the supplied runtime record.

## Core ideas

FCVW separates historical evidence, current canonical project state and reusable wiki knowledge. It asks the host to promote sourced reusable material, preserve audit history and avoid treating a session or retrieval result as authoritative instruction. The wiki is a small search/on-demand surface rather than an always-loaded journal. [MEM-OBJ-wiki](#mem-obj-wiki), [MEM-OBJ-session](#mem-obj-session).

Its strongest continuity mechanism is a bounded handoff: changed files, decisions, validation, risks and next authorized action are synthesized and linked, then rechecked on resume. This is a prescribed raw-work-to-derived-summary-to-next-session chain, not an implemented transcript compactor. Rotation moves older sessions without destroying them. [MEM-RTE-session-handoff](#mem-rte-session-handoff).

Optional tools reconstruct disposable access structures from Markdown. The index carries copied text plus symbolic routing/ranking fields; the graph reconstructs declared relationships and inverse edges. Neither is an independently warranted knowledge store. Source-digest mismatch creates review work rather than silently correcting knowledge. [MEM-RTE-index-build](#mem-rte-index-build), [MEM-RTE-source-review](#mem-rte-source-review).

Context control is mainly selective entry, not runtime eviction: narrow handoffs, JIT skills, routes, selected sections, bounded excerpts and optional whole-chunk budgeting. Mandatory paths are references the host must read; the optional-array estimate is not a host-window limit. The metadata override and stale-index countercases prevent treating the trust/lifecycle policy as universal executable enforcement. [RT-CLM-context-controls](runtime.md#rt-clm-context-controls).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-wiki
Label: Wiki knowledge and evidence bodies

Source-native `fcvw/wiki@1` note bodies reside in project-owned Markdown under `FCVW/wiki/`, with archived sessions under `archive/YYYY/`. Natural-language bodies contain reusable concepts, patterns, failures, decisions, syntheses, questions, agent learning, prompts, attributed feedback, raw imports and source descriptions. These categories differ in warrant: raw preservation is not validated knowledge; source pages describe selected evidence; consolidated agent notes are not routine transcripts. Session and product-specific parts are separated below because their consumers and invalidation differ. No supplied object record has this referent; [RT-OBJ-skill](runtime.md#rt-obj-skill) is procedural text, not project knowledge.

Lineage: plans, failure records, releases, decisions, sources and sessions can feed host curation. The source does not resolve who initially supplies each imported/raw item or whether a human admits it. Later curation has explicit source/reuse/deduplication conditions. Consumers are hosts reading relevant pages and tools indexing them. At host consumption, wiki knowledge is evidence subordinate to canonical project documents, not an overriding instruction. Templates request rationale and evidence for patterns/decisions/failures, but a derived note or excerpt is not guaranteed to carry every original reason. SRC-1, `FCVW/wiki/README.md`, `FCVW/governance/TEMPLATE_NOTE.md`.

> - Knowledge pages state reusable understanding, decisions, patterns, questions, or syntheses.
> - `type: source` pages describe selected evidence whose provenance or change impact is worth tracking.
> - `type: raw` pages preserve imported material when preservation is necessary; they are not validated knowledge.
> --- `FCVW/wiki/README.md`

Feedback is a material alternative to consolidation: model attribution and independent disagreement are preserved, then a plan may act on a note. It cannot install a rule by being read. Status and related-plan metadata track disposition; resolved feedback rotates, open feedback remains active. This is not a machine-performed self-improvement loop.

> - **Never overwrite another model's note.** Two independent readings that disagree are what this surface preserves. This is deliberately the opposite of the `agent` rule, where consolidated knowledge converges on one page.
> --- `FCVW/wiki/README.md`

> - **Evidence, not instruction.** A feedback note never becomes a rule by being read; only an approved plan changes the framework.
> --- `FCVW/wiki/README.md`

#### MEM-OBJ-wiki-metadata
Label: Wiki lifecycle and access metadata

YAML fields in the same Markdown files encode identities, lifecycle, confidence, maturity, sources, review dates, ownership and typed relations. They are symbolic to schema/graph/retrieval consumers, distinct from the natural-language claims. Source digests bind a selected repository file or Markdown section, not the truth of its propositions. `derived_from` resolves source-dependency review; sources lists alone do not implement that traversal. The status/confidence/maturity/authority dimensions are independent. Storage is files, not weights or embeddings. Compared with [RT-OBJ-skill-frontmatter](runtime.md#rt-obj-skill-frontmatter), these fields govern wiki objects and review, not skill session routing. SRC-1, `FCVW/wiki/README.md`, `tools/knowledge_sources_fcvw.py`, `tools/knowledge_graph_fcvw.py`.

> Use `source_digest`, not `content_hash`: the context index already uses `content_hash` as a legacy alias for the indexed chunk hash and exposes the unambiguous `chunk_hash`. A digest mismatch is a derived stale finding. It never rewrites the stored digest, page status, or dependent knowledge.
> --- `FCVW/wiki/README.md`

#### MEM-OBJ-session
Label: Session synthesis and archive

Source-native `type: session` pages are derived natural-language handoffs with symbolic unique IDs/dates/status/source links in Markdown. They retain decisions, risks, validation, changed paths and next authorized action; they are not raw chat logs or authoritative current state. Inputs are actual workspace/plan/evidence, not merely prior conversational assertions. The intended later reader is the next host agent/session selected by date, ID and scope, which must verify against disk. Archives remain reachable by search and links; no fixed automatic expiry is implemented by the skill. Distinct from [RT-OBJ-skill](runtime.md#rt-obj-skill): a session is produced during work, not a shipped procedure. SRC-1, `FCVW/skills/wiki-curator/SKILL.md`, `FCVW/AI.md`.

> Capture only the state required to continue work without replaying the full conversation.
> --- `FCVW/skills/wiki-curator/SKILL.md`

> - copying full files or chat transcripts into the handoff;
> - inventing commit, test, publication, or completion evidence;
> - treating the newest or highest sequence as relevant without checking scope;
> - deleting older sessions as part of compaction.
> --- `FCVW/skills/wiki-curator/SKILL.md`

#### MEM-OBJ-context-index
Label: Disposable context index

`context-index.jsonl` contains copied natural-language Markdown chunks and symbolic fields (`chunk_id`, `path`, hashes, metadata and relationships). Storage is caller-selected filesystem JSONL, usually `.fcvw-cache/`; it is not numerical/parametric memory. Builder output is derived from current Markdown reads; the CLI retriever later loads supplied JSONL rather than rebuilding or rehashing source pages. Chunk text can include frontmatter/preamble and is split at level-two/three headings and paragraph boundaries, preserving oversized atomic blocks. It is not model-written semantic synthesis. No supplied operative-object counterpart exists; this is the stored intermediate used by [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery). SRC-1, `tools/build_context_index.py`, `tools/retrieve_context.py`.

> """Keep paragraphs and fenced code atomic; oversized blocks remain complete."""
> --- `tools/build_context_index.py`

> for line in path.read_text(encoding="utf-8").splitlines():
>     if line.strip():
>         records.append(json.loads(line))
> --- `tools/retrieve_context.py`

#### MEM-OBJ-knowledge-graph
Label: Derived typed graph and review findings

`fcvw/knowledge-graph@1` JSON encodes nodes, explicit frontmatter edges and generated inverses. Separate warning JSON can retain due-date/source-impact review candidates. This is symbolic derived access/review state, not new natural-language knowledge and not a dense embedding store. Consumers include the lexical retriever's optional one-hop expansion and a host/reviewer reading findings. A `supports` edge is a declared relation, not independently established support. Distinct from the context index, whose copied text actually supplies excerpts, and from the document graph, which serves navigation/reachability. Closest supplied record is [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery), a route using this optional input rather than the object. SRC-1, `tools/knowledge_graph_fcvw.py`.

> "authority_notice": "Derived from governed Markdown; source artifacts remain authoritative.",
> --- `tools/knowledge_graph_fcvw.py`

#### MEM-OBJ-product-contract
Label: Product inventory and behavior contract

Product-owned `type: component` pages mix natural-language purpose/expectations with symbolic table keys, stable surface/element/case IDs, expectation classes and routes. Inventory/frontier tables retain discovery progress, scope, roles, revision and unresolved access. Files live in the wiki; application-specific content is not shipped in the clean template. Approved expectations require an approved source, not code/live observation alone. Host QA later selects affected pages and cases; the product checker parses them and computes a symbolic contract hash from ID, kind, route, elements and cases. Hashes bind declared contracts, not application behavior. Compared with [RT-RTE-asset-admission](runtime.md#rt-rte-asset-admission), this is product-specific retained input with a stricter divergence gate, not a duplicate general curation route. SRC-1, `FCVW/skills/QA/PRODUCT_WIKI.md`, `tools/qa_wiki_fcvw.py`.

> Classify expectations as approved, provisional or unknown. Approved means supported by an existing approved requirement, acceptance criterion, design decision or owner confirmation. Code and live behavior can support observations or provisional hypotheses; neither can silently approve product intent. Unknown/provisional expectations cannot produce a passing assertion.
> --- `FCVW/skills/QA/PRODUCT_WIKI.md`

#### MEM-OBJ-qa-run
Label: Exact QA run evidence

`type: audit`, `qa_run: "true"`, `retrieval_scope: exact_only` Markdown records preserve selected behavior hashes, application revision, environment/runtime/roles/time, per-case observations/evidence and divergence decisions. Natural-language observations and references coexist with symbolic result/contract/decision tables parsed by the checker. Screenshots/traces/large logs remain external or project-owned evidence reached by links; those payloads were not supplied and their truth is uninspected. Later QA consumers compare current contracts with run hashes, preventing structural reuse of an old pass after contract changes. Earlier run records remain historical. No supplied object counterpart exists; [RT-RTE-local-checks](runtime.md#rt-rte-local-checks) concerns local framework-tool verification rather than application QA runs. SRC-1, `FCVW/skills/QA/PRODUCT_WIKI.md`, `tools/qa_wiki_fcvw.py`.

> if contracts.keys() != surfaces.keys() or any(contracts[k]['sha256'] != p['sha256'] for k, p in surfaces.items()):
>     raise ValueError('run does not match current selected behavior contracts; review and rerun affected cases')
> --- `tools/qa_wiki_fcvw.py`

#### MEM-OBJ-decision-trace
Label: Content-free tool decision trace

`fcvw/decision-trace@1` JSONL rows contain time, caller run ID, component, status/reason labels, optional input digest/duration/provider tokens and token-source label. This is symbolic evidence about tool decisions, not retained claim bodies, conversation or model-call attestation. The append API validates labels/numbers/digest and rejects input/report aliasing; inside the framework it confines trace writes to cache. Retrieval and product-check CLI call sites are inspected writers. Later human/host joins are documented as afforded review, not an automatic trace-to-rule update consumer. Closest supplied record is [RT-RTE-local-checks](runtime.md#rt-rte-local-checks), whose report/logs are a different evidence artifact. SRC-1, `tools/trace_fcvw.py`, `tools/retrieve_context.py`, `FCVW/AI.md`.

> It records a tool decision, not a model call, user message, file
> read or attestation.
> --- `tools/trace_fcvw.py`

### Routes

#### MEM-RTE-session-handoff
Label: Bounded handoff and lifecycle reload

A useful stop, inter-session/agent handoff or completed batch triggers host synthesis from the actual plan, modified files, validation and risks. The host verifies state, writes a unique session using the note template and links canonical files. Later session start selects relevant state by scope/date/ID, checks disk and follows links/context files. Rotation is a related host procedure triggered above 10 active files, 100 KB or project budget: inventory, extract reusable knowledge, archive-index creation, move, preserve 3–10 relevant sessions, repair backlinks and lint. No FCVW model call or transcript eviction implements either step. This is distinct from the general promotion gate in [RT-RTE-asset-admission](runtime.md#rt-rte-asset-admission): its primary retained output is a continuity checkpoint, although it can feed promotion. SRC-1, `FCVW/skills/wiki-curator/SKILL.md`, `FCVW/AI.md`, `FCVW/wiki/README.md`.

Admission is host judgment of useful nontrivial state plus source/link/identity checks; starting a session is not per-content human approval. No separate human approval is required for each synthesis. The host may omit trivial or duplicate handoffs; cleanup is archival, while deletion requires explicit retention policy/approval and no remaining recovery/audit/legal/security need. Recovery is original records plus source links, not reconstruction of the full removed conversation. Operating mode is open work continuity; reference state is disk/plan/validation, not a model-quality answer oracle.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: concise session checkpoint and optional index entry; rotation returns moved-file/archive/promotion/validation accounting.
- Later read-back: next host session reads the latest relevant handoff and plan, then linked files; archived material is searched on demand.
- Delegated visibility: a handoff can target another agent, but isolated context allocation and returned worker payload are host-owned and uninspected.
- Selection predicate: meaningful unfinished/reusable state; resume by date, unique ID and scope rather than sequential maximum; rotation by active-size or noise thresholds.
- Invalidation or expiry: compare summary with disk and evidence; obsolete conclusions remain historical; archive moves preserve evidence and links.
- Activation or effect: requests later work conditioned on verified summary and next authorized action; actual behavior change and completeness of summary are unobserved.
- Evidence limits: instruction-level transformation only; no background compaction, fixed tokenizer budget or automatic deletion is established by these paths.

> 1. Verify actual workspace and plan state.
> 2. Create the page from `governance/TEMPLATE_NOTE.md` (session block).
> 3. Link canonical files rather than copying their contents.
> 4. Record decisions, failures, validation, unresolved risks, and next step.
> --- `FCVW/skills/wiki-curator/SKILL.md`

> 2. Extract validated reusable knowledge and link sources.
> 3. Update existing canonical wiki pages before creating duplicates.
> 4. Create an archive index with date range and source list.
> 5. Move old sessions to `wiki/archive/YYYY/`; do not delete audit evidence.
> --- `FCVW/wiki/README.md`

#### MEM-RTE-index-build
Label: Markdown to disposable chunks

Caller selects root/output and optional inclusion of excluded material. Python scans Markdown, omits disposable paths, derives metadata/default scope, preserves text chunks and writes JSONL. The CLI is a concrete writer; `build_index` itself returns records and leaves persistence to its caller. Later retrieval uses this frozen copy. This route produces an intermediate used by [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery), not the same query-to-return route. Admission is software path/scope selection plus caller flags; no semantic content approval is performed. Source authorship and human identity remain separate. SRC-1, `tools/build_context_index.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: chunk list from API; CLI writes JSONL and prints chunk count/output path.
- Later read-back: retrieval CLI loads this index on a later indexed query and delivers selected copied text to its caller.
- Delegated visibility: inapplicable — there is no worker context or model delegation in the builder.
- Selection predicate: recursive Markdown inventory excluding disposable parts; metadata scope can override defaults; include-excluded affects building, while the normal retriever still filters excluded-by-default records.
- Invalidation or expiry: rebuild after source change; chunk hashes identify copied content but retrieval does not compare them to live sources.
- Activation or effect: deterministic text/metadata derivation and output overwrite, not semantic learning or proof of later model use.
- Evidence limits: stale copies remain possible; explicit metadata precedes role-derived defaults and can undermine the intended non-elevation policy.

> scope = default_scope(relative_path, metadata)
> if scope == "excluded_by_default" and not include_excluded:
>     continue
> --- `tools/build_context_index.py`

#### MEM-RTE-source-review
Label: Source impact and curated lifecycle review

Python compares a selected local source or Markdown section against stored source digest, derives explicit `derived_from` dependents and due-date warnings, and emits graph/findings/review JSON. Host curator then confirms, updates, supersedes or invalidates linked knowledge before refreshing digests/dates. The semantic-review alternative asks a host for source-bounded duplication/contradiction/summary findings but forbids automatic canonical mutation and unmeasured release-gate authority. This is a finer source-impact part of [RT-RTE-asset-admission](runtime.md#rt-rte-asset-admission), not a replacement for its factory/procedural gates.

Part of: [RT-RTE-asset-admission](runtime.md#rt-rte-asset-admission)

Proposer is software for review candidates and host for content revisions; host/reviewer decides changes under plan scope. Missing/broken source provenance yields findings; digest mismatch is warning, not automatic rejection or repair. Human approval of each page change is not established; optional semantic findings request a human decision. Operating mode is source-change/due-date maintenance, not a training curriculum. Oracle is source comparison for bytes/structure, not an expected semantic answer. Rollback relies on versioned sources/history and supersession rather than automatic transactions. What persists is revised text/metadata and plan/session curation accounting; a review report alone remains advisory evidence. SRC-1, `tools/knowledge_sources_fcvw.py`, `tools/knowledge_graph_fcvw.py`, `FCVW/skills/governance-validator/SKILL.md`, `FCVW/skills/wiki-curator/SKILL.md`.

- implementation conclusion status: wired
- curation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: deterministic graph/findings/digest or warning-only review report; host review may return changed, superseded, invalidated or deferred pages.
- Later read-back: reviewer consumes candidates; retriever may consume rebuilt graph; later hosts consume revised canonical/wiki files on demand, not reports as automatically adopted truth.
- Delegated visibility: inapplicable — no isolated model worker or scheduler is implemented by these checks.
- Selection predicate: stored source_path/digest mismatch, explicit non-derived derived_from edge, next_review before today; optional semantic review only declared pages and authoritative sources.
- Invalidation or expiry: source change requests review; reviewer updates lifecycle/digest only after decisions; cache regeneration is needed for updated access structures.
- Activation or effect: deterministic candidate production is wired; semantic revision and downstream reliance remain host-mediated and unobserved.
- Evidence limits: unavailable external contents are not fetched by digest checking; warnings and relation names establish neither truth nor successful revision.

> if edge["derived"] or edge["relation"] != "derived_from":
>     continue
> --- `tools/knowledge_sources_fcvw.py`

> - Never rewrite, validate, supersede, invalidate, or refresh a digest automatically.
> --- `FCVW/skills/governance-validator/SKILL.md`

#### MEM-RTE-product-review
Label: Product evidence and divergence admission

QA host discovers authorized application surfaces/interfaces and writes inventory/behavior pages, keeping approved intent distinct from observations. Later affected-page replay produces exact run records. The checker takes explicit pages/inventory/run, parses declared contracts/results, compares hashes and returns structural/execution/consultation statuses. Host owns actual execution and content truth. This differs from [RT-RTE-local-checks](runtime.md#rt-rte-local-checks), which executes framework-local checks rather than asking application users to decide product divergences. It specializes knowledge admission beyond [RT-RTE-asset-admission](runtime.md#rt-rte-asset-admission).

Proposer: QA host. Decision/veto: approved sources constrain expectations; every expected/actual divergence requires user direction before dependent action. Approved revision still needs a new contract/test. Software rejects structurally mismatched hashes, unapproved passing expectations and incomplete/failed runs; it cannot verify referenced consent. Mode is bounded selected-scope application validation. Expected behavior with approved source supplies a reference outcome; observed code/live behavior cannot silently become that oracle. Recovery: preserve original runs/failures and append dated decisions, checkpoint unresolved discovery/access, obsolete/supersede pages and rerun affected cases. SRC-1, `FCVW/skills/QA/PRODUCT_WIKI.md`, `tools/qa_wiki_fcvw.py`.

- implementation conclusion status: wired
- authoring conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: checker JSON report/hashes or error; optional report and content-free trace write. Host procedure produces product pages, run records or a frontier checkpoint.
- Later read-back: later QA loads compact inventory, affected pages, requirements and recent exact runs; checker compares retained run contracts with current selected pages.
- Delegated visibility: inapplicable — product checker and guide implement no delegated model context.
- Selection predicate: explicit surface/inventory/run arguments for checker; changed routes, controls, permission rules, sources, implementation, defects or due dates for host review.
- Invalidation or expiry: changed declared behavior contracts reject old-run hash matching; retain previous results and rerun affected cases; blocked frontier supports resumption rather than invented completeness.
- Activation or effect: structural hash/result checks are wired; application testing, honest observation and user consultation are requested, not independently attested.
- Evidence limits: clean template has no application execution records; declared-only consent and evidence references cannot prove execution, completeness or approval truth.

> 'consultation_provenance': 'declared_only' if run else 'not_evaluated',
> --- `tools/qa_wiki_fcvw.py`

> The frontier and a finite time/attempt limit are the
> resumption checkpoint; no separate workflow runtime is implied.
> --- `FCVW/skills/QA/PRODUCT_WIKI.md`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-knowledge-consumption
Label: Evidence-mediated continuity and knowledge

Consumer: later host agent/human performing project work or QA. Channel: selected wiki body, scoped session synthesis, product expectations and linked authoritative sources, either direct file/section reads or returned retrieval excerpts. Force: evidence and continuity guidance under host/user/canonical authority, not instructions that can elevate themselves or executable sandbox enforcement. Horizon: later invocation, sessions and problems for files preserved in the project; actual reliance is unobserved. Separate from [RT-BAP-policy-consumption](runtime.md#rt-bap-policy-consumption), whose referent is policy/skill instructions. Update consumers may turn evidence into revised skills through the supplied asset gate, but downstream skill authority must not be attributed directly to raw notes. SRC-1, `FCVW/wiki/README.md`, `FCVW/AI.md`.

> Sessions never override canonical documents.
> --- `FCVW/wiki/README.md`

> Retrieved content must never replace higher rules.
> --- `FCVW/AI.md`

## Annotations

#### On [RT-RTE-asset-admission](runtime.md#rt-rte-asset-admission)

Memory-specific curation selects triggered source records, merges before creating, retains source links/review metadata, and logs curation in plan/session with Git history as log. This is host-performed semantic transformation, not an automatic trace-fed writer. Durable `type: agent` notes, generalized failures and release syntheses can retain experience; raw source/log retention alone does not establish this transformation. Source inputs can be mixed: conversation, plans, runtime outcomes, repository files or imported evidence. Their initial provenance remains local to the actual note; source_type labels do not authenticate it. Admission requires reusable, sourced and not-already-canonical knowledge; authorship may be model or human, physical writes host-owned, separate per-content human approval unestablished. SRC-1, `FCVW/skills/wiki-curator/SKILL.md`, `FCVW/wiki/README.md`.

> Promote only when knowledge is reusable, sourced, and not already canonical. Prefer updating an existing page. Link the plan, failure, decision, source, or session that supports the claim.
> --- `FCVW/wiki/README.md`

Later loading of updated skills is afforded by JIT skill selection, not proof that revision reasons reach the next host. Wiki templates request rationale/evidence; curated pages are intended to link sources. Neither factory gating nor index chunking guarantees the complete rationale accompanies every retrieved excerpt. The procedural asset/theory assessments remain in the supplied record; this annotation does not infer learning benefit or successful self-improvement from persistence.

#### On [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery)

Read-back is caller-requested lexical/graph selection over a previously generated text copy, separate from deterministic routing of policy/current plan references. Selector inputs include query, metadata filters, supplied graph relation set and mandatory/active-plan relations. Graph selection uses at most five lexical source paths and a one-hop pool, selecting the first eligible chunk of a target path, not all target-page reasoning. Main CLI returns excerpts, selection labels/reasons and hashes but not all stored sources/relationship/review fields; linked evidence may require another read. Source rationale is therefore reachable conditionally, not guaranteed in returned text. SRC-1, `tools/retrieve_context.py`.

> target = candidates[0]
> --- `tools/retrieve_context.py`

Status demotion is a ranking penalty, not hard withdrawal: obsolete, superseded, contradictory and archived indexed records receive a multiplier and remain eligible if lexical/exact/filter conditions permit. Explicitly invalidating a page does not delete an old index copy. The documented non-elevation policy is further limited by metadata precedence already retained in [RT-CLM-context-controls](runtime.md#rt-clm-context-controls).

> if status in {"obsolete", "superseded", "contradictory", "archived"}:
>     score *= 0.35
> --- `tools/retrieve_context.py`

Whole-chunk budget selection removes mandatory-path duplicates, repeated IDs/text, empty text, over-limit chunks/files and candidates exceeding the serialized optional-array estimate. Ordinary unbudgeted output slices at 1,200 characters; neither path controls the model's full window. Host request initiates delivery; this is not unsolicited knowledge injection. SRC-1, `tools/context_selection_fcvw.py`, `tools/retrieve_context.py`.

> "estimator": "ceil(Unicode characters in indent=2 JSON result array / 4); not model tokens",
> --- `tools/context_selection_fcvw.py`

#### On [RT-RTE-mcp-checks](runtime.md#rt-rte-mcp-checks)

The absence of writes does not make later read-back inapplicable. `fcvw_read_sections` can reread accumulated wiki/session/QA content; exact named headings plus preamble reach the calling host, with a byte ceiling and missing-heading diagnostics. Empty headings deliver an outline only. `fcvw_routes` rereads active-plan context files and returns references/ranges, not bodies. `fcvw_next_plan` derives queue and recommendation from persistent plan state; it is not a scheduler. `fcvw_digest` reads current source bytes/section and returns digest, not retained claim content. These are caller-requested tools; body content has evidence force. SRC-1, `tools/mcp_server_fcvw.py`, `tools/plan_queue_fcvw.py`.

> return {"authority_notice": NOTICE, "path": path.relative_to(root).as_posix(),
>         "missing": missing, "content": content}
> --- `tools/mcp_server_fcvw.py`

The queue ignores legacy queue files, sorts plans using state/override/blockers/category/priority/date/ID and suppresses recommendation on error findings. This is symbolic selection of persisted work state, not semantic extraction of a session or autonomous execution of the next plan.

#### On [RT-RTE-hook-lifecycle](runtime.md#rt-rte-hook-lifecycle)

Session-start push selects persisted in-progress and pending plan filenames and emits them as additional host context. It includes all active names and at most the first five pending entries, plus static reading/plan instructions. Thus it has a narrow later-read-back path for retained plan identity, although it writes no memory and does not read handoff bodies. Trigger/activation remain the supplied opt-in hook contract; the host is the delivery consumer. SRC-1, `tools/hook_fcvw.py`.

> if pending:
>     lines.append(f"Pending plans: {', '.join(pending[:5])}{' ...' if len(pending) > 5 else ''}.")
> --- `tools/hook_fcvw.py`

## Write side

Acquisition is explicit host work, not background crawling. Imported raw material, selectively tracked sources and work records remain distinct from promoted reusable claims. Initial supplying/admission of arbitrary imports is unspecified; known later promotion, review and session transformations must not be suppressed because of that gap. See [MEM-OBJ-wiki](#mem-obj-wiki) and the asset-admission annotation.

The compaction chain is actual workspace/plan/validation/decisions → host-authored bounded session → later scope-selected session read and disk verification. It is a trace-informed prescribed transformation, but not an automatic implemented transcript-to-derived-memory learner. Archive rotation preserves originals and promotes reusable material separately. The alternative QA checkpoint retains discovered/blocked frontier and next resumption scope rather than a generic conversation summary. Neither mechanism proves improved future capacity. [MEM-RTE-session-handoff](#mem-rte-session-handoff), [MEM-RTE-product-review](#mem-rte-product-review).

Maintenance splits semantic decision from mechanical derivation. Curator chooses merge, update, supersede, invalidate or defer; source/graph checks identify candidates without making those decisions. Optional semantic review cannot mutate knowledge. Rejection ability is procedural in general curation, stronger in the product checker for declared hashes/classes/results, and still dependent on honest evidence. Withdrawal changes lifecycle/canonical links and search weighting; it does not erase historical sessions, runs or stale index copies. Deletion needs explicit retention approval. [MEM-RTE-source-review](#mem-rte-source-review), context-delivery annotation.

Index/graph writes are deterministic extraction and formatting, not new semantic claims. Raw decision traces and validation logs can support a later human/host review, but the inspected trace writer and CLI call sites show no automatic trace→revised skill/wiki→later behavior chain. The supplied self-improvement route is a separate host-mediated procedure. Content memory, access metadata and procedural organization have different consumers and should not be combined into a single learning assertion. [MEM-RTE-index-build](#mem-rte-index-build), [MEM-OBJ-decision-trace](#mem-obj-decision-trace), [RT-RTE-asset-admission](runtime.md#rt-rte-asset-admission).

## Read-back

There are three materially different read-back directions. Session resumption and retrieval are host-requested reads; the caller chooses scope/query/identities before selector code chooses excerpts. MCP section/queue calls likewise answer requests, sometimes returning only references or metadata. The opt-in session-start hook automatically pushes a plan-identity summary at its event, not independently selected wiki content. Its producer is code, selected inputs are persisted plan directory entries, budget is all active names plus five pending names, channel is additionalContext, consumer is configured host. No observed host use follows merely from output construction. See [MEM-RTE-session-handoff](#mem-rte-session-handoff) and the three runtime-route annotations.

Context control preferentially keeps unrelated archive, long evidence, nonmatching skills and unrequested sections out of initial loading. What remains reachable is a path/link/index/outline/summary, not an automatically dereferenced pointer. Reload requires a new file, section or retrieval request. Optional complete-chunk selection skips oversized text instead of evicting existing turns; ordinary output can truncate excerpts. Compaction creates a continuity artifact but does not remove host turns. These are selective-loading protocols and tool-output bounds, not a host memory manager. SRC-1, `FCVW/AI.md`, `tools/context_selection_fcvw.py`, supplied [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery).

Delegation resembles a stack-frame boundary only at the requested work-package level: selected plan/files/constraints go to another executor and reviewed results return. FCVW does not implement allocation or popping of model contexts; inheritance and what escapes are host-specific. File links differ from heap references: they remain readable external artifacts but do not cause automatic reachability-based retention or garbage collection. No full host-window reconstruction follows from FCVW's selective-file instructions. [RT-RTE-work-packages](runtime.md#rt-rte-work-packages).

## Integration issues

1. **Correct the no-write/read-back conflation.** [RT-RTE-mcp-checks](runtime.md#rt-rte-mcp-checks) marks later read-back inapplicable because handlers do not persist memory. Section reads and queue tools can consume accumulated wiki/plan state on later invocations; their output transforms that state. The annotation supplies SRC-1 `tools/mcp_server_fcvw.py` evidence. Similarly [RT-RTE-hook-lifecycle](runtime.md#rt-rte-hook-lifecycle) pushes retained plan filenames at session start despite no writes. Neither correction establishes model use or body-level knowledge delivery through the hook.
2. **Contained source-review part.** [MEM-RTE-source-review](#mem-rte-source-review) is explicitly part of [RT-RTE-asset-admission](runtime.md#rt-rte-asset-admission). Keep its warning-only software derivation separate from host semantic admission. It is not a conflicting duplicate. [MEM-RTE-session-handoff](#mem-rte-session-handoff) overlaps the asset route's optional session-synthesis mention but has a distinct continuity/rotation/reload referent; no supersession is proposed.
3. **Product-specific admission must survive grouping.** [MEM-RTE-product-review](#mem-rte-product-review) adds the every-divergence user gate and hash-bound run reuse from SRC-1 `FCVW/skills/QA/PRODUCT_WIKI.md` and `tools/qa_wiki_fcvw.py`. General curation's lack of mandatory per-content human approval must not erase this specialized gate. Conversely declared consent references are not observed user approval.
4. **No other new-record duplicate identified.** Object records split retained text, access metadata, handoffs, index/graph, product contracts/runs and trace evidence; supplied objects cover skills/frontmatter/model. [MEM-RTE-index-build](#mem-rte-index-build) produces the input to, rather than duplicates, [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery). [MEM-BAP-knowledge-consumption](#mem-bap-knowledge-consumption) has evidence force, distinct from the policy/skill instruction force of [RT-BAP-policy-consumption](runtime.md#rt-bap-policy-consumption).
5. **Unresolved deployment and provenance.** Actual note initialization control, raw/import origin, semantic-review runtime, host context allocation/eviction, successful compliance and deployed rebuild scheduling are not established. Initial provenance remains local to [MEM-OBJ-wiki](#mem-obj-wiki); stale-copy and policy/metadata discrepancies remain local to [MEM-OBJ-context-index](#mem-obj-context-index) and the context-delivery annotation. No cross-system conclusion or observed automatic learning can be drawn. These are faithful limits, not reasons to erase the known curation paths.

## Limitations and checks

Source HEAD equals the boundary revision. Only the registered SRC-1 checkout, supplied boundary/runtime and governing method inputs were used. No target tests, examples, services, providers or live applications were executed. No prior characterization or peer specialist output was read. The complete invocation and required input ranges were read; combined-source delivery truncation was recovered by separate bounded reads before conclusions were settled.

The countercases checked include metadata overriding authority/scope defaults, stale index delivery, obsolete material remaining eligible, graph expansion omitting most target chunks, outline-only versus body MCP delivery, no-write paths consuming retained state, and product-specific human gates differing from general curation. Limits remain for uninspected full validator/navigation/dependency internals and all deployed host behavior. File persistence and requested synthesis establish neither reliable compliance, activation nor measured learning benefit.

Validation: the required role-aware Commonplace content check passed against this report and the supplied artifact (exit 0): “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” It checks form and quotation occurrence, not semantic correctness or job acceptance.
