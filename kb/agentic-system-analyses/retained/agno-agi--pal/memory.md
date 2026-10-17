---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Pal memory: raw-to-wiki compilation, routing metadata, operational learnings and dependency-mediated conversational continuity."
run-id: AAS-2026-10-17-pal-e313a0902289-01
source-identity: https://github.com/agno-agi/pal
reviewed-boundary: 6516b8ede0c085e48f39f3bd04cb85b475a855dc
---

# Pal memory report

## Boundary and evidence

Pal retains content in context files and SQL, routes retrieval through metadata, and configures separate operational learnings and conversational memory. This report covers all those surfaces within the whole-system boundary in [boundary](boundary.md). The frozen source is SRC-1, `https://github.com/agno-agi/pal` at `6516b8ede0c085e48f39f3bd04cb85b475a855dc`. HEAD was rechecked against that revision and the checkout was clean. Source code and instruction strings provide implementation and doctrine/design evidence; no observed run or experiment was supplied. No target code was executed.

Direct reads covered `pal/instructions.py`, the relevant leader configuration/instructions in `pal/team.py`, Navigator, Researcher, Compiler, Linter and shared settings, `pal/tools/build.py`, `pal/tools/ingest.py`, `pal/tools/wiki.py`, `pal/tools/knowledge.py`, `pal/tools/git.py`, `context/load_context.py`, `context/preferences.md`, `db/session.py`, `app/router.py`, `app/main.py`, `pal/config.py`, the memory-tier passage of `docs/SPEC.md`, and cleanup in `evals/extended_smoke.py`. Scoped source searches covered memory/learning/compaction/removal terms in `pal/`, `context/`, `app/`, `scripts/` and `docs/SPEC.md`, plus evaluator session/result handling. Other evaluation details below are supplied findings from runtime, not fresh full-file inspection.

Agno's memory algorithms, session serialization, search ranking, injection budgets and generated tools are outside SRC-1. Live PostgreSQL, remote context repositories and populated user content were not supplied. These limits prevent conclusions about actual remembered contents, successful activation, tenant isolation, compaction output or measured improvement. They do not erase Pal's visible configuration and explicit file transformations. Provider model and embedder identity/fixity limits remain those of [RT-CMP-openai-responses](runtime.md#rt-cmp-openai-responses) and [RT-CMP-openai-embedder](runtime.md#rt-cmp-openai-embedder).

### Coverage inventory

| Included entry/operation | Source paths and inspection basis | Records / conclusion limit |
|---|---|---|
| Direct text/URL ingest; Researcher acquisition | Direct: `app/router.py`, `pal/tools/ingest.py`, `pal/agents/researcher.py`, `pal/tools/build.py` | [RT-RTE-raw-ingest](runtime.md#rt-rte-raw-ingest), [MEM-OBJ-raw](#mem-obj-raw); URL stubs and model-curated raw are alternatives to full source copies. |
| Compile, force compile, index/state/manifest mutation | Direct: `pal/agents/compiler.py`, `pal/tools/wiki.py`, `pal/tools/ingest.py`, `app/router.py`, `app/main.py` | [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance), [RT-OBJ-manifest](runtime.md#rt-obj-manifest), wiki objects below; force prompt is not deterministic invalidation. |
| Lint, criticism and suggested research | Direct: `pal/agents/linter.py`, `pal/tools/build.py` | [MEM-OBJ-lint-report](#mem-obj-lint-report); retained criticism has no mandatory repair consumer. |
| CLI loader, reload service, daily refresh, recreate | Direct: `context/load_context.py`, `app/router.py`, `app/main.py` | [RT-RTE-context-refresh](runtime.md#rt-rte-context-refresh), [MEM-OBJ-pal-knowledge](#mem-obj-pal-knowledge); metadata is not document content; vector deletion is not proven contents-table deletion. |
| Model-authored routing metadata | Direct: `pal/tools/knowledge.py`, `pal/tools/build.py`, `pal/instructions.py` | [MEM-RTE-knowledge-update](#mem-rte-knowledge-update); insertion alone does not establish replacement semantics. |
| Query-directed wiki/raw/files/SQL retrieval, drafting and captures | Direct: `pal/instructions.py`, `pal/agents/navigator.py`, `pal/tools/build.py`, `db/session.py` | [RT-RTE-navigator-work](runtime.md#rt-rte-navigator-work), [MEM-OBJ-user-files](#mem-obj-user-files), [MEM-OBJ-pal-tables](#mem-obj-pal-tables); SQL predicates are instructions, not inspected row-level enforcement. |
| LearningMachine on leader, Navigator and conditional Researcher; Monday summary | Direct: `pal/team.py`, `pal/agents/navigator.py`, `pal/agents/researcher.py`, `app/main.py` | [MEM-RTE-learning-reuse](#mem-rte-learning-reuse); exact trace extraction and automatic selection opaque. |
| User memory, history trimming and past-session recall | Direct: `pal/team.py`, `pal/agents/navigator.py`, `pal/agents/settings.py` | [MEM-RTE-conversation-reuse](#mem-rte-conversation-reuse); opaque personal-memory payload is not interchangeable with session transcript or learning text. |
| Delegation working contexts and return | Direct configuration/instructions: `pal/team.py`; supplied runtime dependency limits | [RT-RTE-team-dispatch](runtime.md#rt-rte-team-dispatch); brief input and synthesized return requested, exact frame filtering unknown. |
| Scheduled briefing/review/lint/compile/refresh and sync; startup and pull | Direct: `app/main.py`, `app/router.py`, `pal/tools/git.py` | [RT-RTE-git-sync](runtime.md#rt-rte-git-sync), maintenance annotations; Git transfers files, not database memories. |
| Exposed agents and knowledge services | Direct: `app/main.py`, `pal/tools/build.py` | [MEM-CLM-service-boundary](#mem-clm-service-boundary); both knowledge stores registered, external service operation schemas/admission unknown. |
| Evaluator calls, cleanup and session reuse | Direct cleanup and scoped search: `evals/extended_smoke.py`, `evals/smoke.py`, `evals/run.py`; supplied runtime evaluation findings | [RT-RTE-evaluation-driver](runtime.md#rt-rte-evaluation-driver); no scores observed or automatic score-to-policy adoption established. |

External email/calendar/web results are acquisition inputs, not a demonstrated separate Pal-retained store unless saved through the included routes. Static shipped templates, voice guides and preferences are working-context inputs; edits and generated files become retained content through the file routes. No alternative checkpoint or summary-compaction implementation was identified in the scoped Pal search; external Agno checkpoint forms remain uninspected, not absent.

## Core ideas

1. **Routing and content have different lifecycles.** `pal_knowledge` carries resource descriptions, while file tools and SQL retrieve substantive content. File refresh derives only path, size, tags and indexing time. A stale pointer can survive a removed file; a model-written Discovery can survive source changes. The loader's recreate clears vector routing entries indiscriminately, not a verified full rollback of the data graph. See [MEM-OBJ-pal-knowledge](#mem-obj-pal-knowledge) and [RT-RTE-context-refresh](runtime.md#rt-rte-context-refresh).
2. **The wiki is an interpreted, derived layer, not a verified cache.** Compiler is asked to summarize, connect concepts and retain source links. Navigator is asked to read it first, with raw fallback. Neither compiled flags nor timestamps certify faithful transformation. Lint can retain criticism without forcing rejection or repair. See [MEM-OBJ-wiki-articles](#mem-obj-wiki-articles), [MEM-OBJ-lint-report](#mem-obj-lint-report) and [RT-OBJ-manifest](runtime.md#rt-obj-manifest).
3. **Experience has a separate behavioral channel.** Learnings are intended to encode retrieval strategies, patterns and explicit corrections. Navigator is instructed to apply them during recall; leader and Researcher additionally request automatic context inclusion. These are stronger intended behavioral roles than ordinary source facts, but actual extraction, delivered text and compliance are not observed. Personal memory and historical turns are additional, distinct channels. See [MEM-RTE-learning-reuse](#mem-rte-learning-reuse) and [MEM-RTE-conversation-reuse](#mem-rte-conversation-reuse).
4. **Context control combines explicit requests with opaque host selection.** Wiki-first file selection, intent-scoped recall, per-source summarization, bounded history and delegation all aim to avoid indiscriminate context loading. File identifiers alone do not prove targeted selection; the prompt's index scan and intent classification explain the intended targeting. No token budget or inspected host compaction algorithm guarantees the eventual window. SRC-1: `pal/instructions.py`, `pal/team.py`, `pal/agents/navigator.py`; [RT-RTE-team-dispatch](runtime.md#rt-rte-team-dispatch).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-raw
Label: Raw source files

Source-native identity: context `raw/*.md`. Substrate: filesystem, optionally Git replicated. Body is natural language interpreted by Compiler or Navigator; frontmatter is descriptive metadata, while the independently stored manifest has the compile selector. Lineage includes caller text, full URL extraction, extraction-failure/pending stubs, and Researcher-curated summaries. Thus “raw” does not guarantee verbatim original evidence. Admission and later consumers are those of [RT-RTE-raw-ingest](runtime.md#rt-rte-raw-ingest); this object is distinct from its access/status metadata [RT-OBJ-manifest](runtime.md#rt-obj-manifest). Source trust is a prompt preference, not validation of submitted content. SRC-1: `pal/tools/ingest.py`, `pal/agents/researcher.py`.

> - For multi-page sources, summarize and save key sections
> --- `pal/agents/researcher.py`

Same-title slugs overwrite content while appending manifest records. The compile-marking tool updates the first matching manifest entry, not the raw file's frontmatter flag. These divergent states prevent treating either label as verified provenance or output completeness. SRC-1: `pal/tools/ingest.py`; [RT-OBJ-manifest](runtime.md#rt-obj-manifest).

#### MEM-OBJ-wiki-articles
Label: Wiki summaries and concept articles

Source-native identities: `wiki/summaries/{doc-name}.md` and `wiki/concepts/{concept}.md`. Substrate: filesystem/Git. Natural-language summaries and explanations, with model-interpreted source/related/tag metadata and links. Compiler is asked for 200–500-word source summaries and additive concept synthesis from raw, existing articles and links. Navigator later consumes selected content as preferred knowledge evidence, not as a hard instruction channel. These are derived content, unlike [RT-OBJ-manifest](runtime.md#rt-obj-manifest); their write/read route is [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance). Source links are requested reasons/provenance; preservation and later source verification are not enforced. SRC-1: `pal/agents/compiler.py`, `pal/instructions.py`.

> - **Source-tracked**: Every claim links back to the raw source that supports it.
> --- `pal/agents/compiler.py`

#### MEM-OBJ-wiki-index
Label: Wiki index

Source-native identity: `wiki/index.md`. Substrate: filesystem/Git. Natural-language titles and one-line summaries plus path strings interpreted by a model to choose article reads. Compiler supplies the full replacement string; tool writes it without checking article existence. Navigator and Linter read the full index. This is a navigation display, not the opaque contents of the article corpus or a verified inventory. Distinct from [RT-OBJ-manifest](runtime.md#rt-obj-manifest), which inventories raw sources. SRC-1: `pal/tools/wiki.py`, `pal/agents/compiler.py`, `pal/instructions.py`.

> index_path.write_text(content)
> return "Wiki index updated."
> --- `pal/tools/wiki.py`

#### MEM-OBJ-wiki-state
Label: Wiki state counters and timestamps

Source-native identity: `wiki/.state.json`. Substrate: filesystem/Git. Symbolic count/timestamp fields written by fixed tool rules from caller arguments; readable JSON returned to model consumers. Compiler/Linter can request timestamps and counts; Navigator can read them. They report workflow state without verifying articles, unlike the natural-language content of [MEM-OBJ-wiki-articles](#mem-obj-wiki-articles). Closest supplied object [RT-OBJ-manifest](runtime.md#rt-obj-manifest) has different fields, scope and selector role. SRC-1: `pal/tools/wiki.py`, `pal/tools/build.py`.

> if mark_linted:
>     state["last_lint"] = now
> --- `pal/tools/wiki.py`

#### MEM-OBJ-lint-report
Label: Retained wiki lint findings

Source-native identity: `wiki/lint-report.md`. Substrate: filesystem/Git; natural-language criticisms and suggested actions. Linter is asked to derive it from article comparisons, age/thinness/link checks and optional web research. Severity headings and counts are model reports, not deterministic evaluation results. No generic object counterpart in supplied runtime; complements [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance). The prompt names Compiler as intended fixer but Compiler's ordinary selector is uncompiled raw, not lint findings. File capability permits a later reader; no mandatory report-to-repair consumer is wired. SRC-1: `pal/agents/linter.py`, `pal/agents/compiler.py`.

> - Do not modify concept articles directly — report findings, let the Compiler fix them
> --- `pal/agents/linter.py`

#### MEM-OBJ-pal-knowledge
Label: Routing knowledge contents

Source-native identity: `pal_knowledge`, with `pal_knowledge_contents` configured contents storage. Substrate: PostgreSQL contents and hybrid PgVector index. Operative text consists of natural-language resource descriptions with paths/tags/schema names; title prefixes are conventions, not enforced namespaces. Derived dense retrieval representations are separately covered by [RT-CMP-openai-embedder](runtime.md#rt-cmp-openai-embedder); text and vectors are not identical content. Lineage includes deterministic file metadata and model-authored Schema/Source/Discovery/Wiki/Raw entries. Consumers include knowledge-enabled specialists and downstream file/SQL selection. Distinct from raw compile metadata [RT-OBJ-manifest](runtime.md#rt-obj-manifest). SRC-1: `pal/agents/settings.py`, `db/session.py`, `context/load_context.py`, `pal/tools/knowledge.py`.

> f"File: {rel_path} in context directory.\n"
> f"Size: {size_kb:.1f} KB\n"
> f"Intent tags: {', '.join(tags)}\n"
> f"Indexed: {datetime.now(UTC).isoformat()}\n"
> --- `context/load_context.py`

Routing entries do not carry source body text through this loader. Model insertion accepts arbitrary content despite the metadata-only instruction; it is not a content-type enforcement boundary. Recreate calls vector deletion only. Contents-table cleanup, ordinary upsert internals and stale-record pruning are not established by Pal's wrapper.

#### MEM-OBJ-pal-learnings
Label: Operational learnings

Source-native identity: `pal_learnings`, with `pal_learnings_contents` configured contents storage and separate hybrid vector index. Intended representational form: natural-language Retrieval/Pattern/Correction entries, interpreted by models; dense representations follow [RT-CMP-openai-embedder](runtime.md#rt-cmp-openai-embedder). Framework serialization and initially retained contents are uninspected. Lineage can include interaction strategies, user corrections and behavioral patterns, not just imported documents. Retained behavioral guidance differs from static [RT-OBJ-agent-instructions](runtime.md#rt-obj-agent-instructions) and routing-only [MEM-OBJ-pal-knowledge](#mem-obj-pal-knowledge). Storage configuration is implementation evidence; trace extraction details and entry hygiene are not thereby proven. SRC-1: `pal/agents/settings.py`, `db/session.py`, `pal/instructions.py`.

> - Strategy worked → `save_learning("Retrieval: ...", "...")`
> - User corrected you → `save_learning("Correction: ...", "...")`
> - Behavioral pattern → `save_learning("Pattern: ...", "...")`
> --- `pal/instructions.py`

The requested reasons include which strategies worked and corrections. No enforced schema requires input/outcome evidence or complete rationale to accompany each behavioral rule. Later readers search learnings, not an inspected linked trace/rationale archive.

#### MEM-OBJ-user-memory
Label: Framework personal user memory

Source-native identity: agentic memory enabled on leader and Navigator; leader instructions refer to `update_user_memory`. Configured substrate: shared `agent_db` PostgreSQL handle. Exact table schema, opaque payload representation, scope keys, extraction process and readable prompt display are external Agno behavior. The leader requests personal preferences only; those are intended natural-language behavioral guidance, not proven contents. This is not [MEM-OBJ-pal-learnings](#mem-obj-pal-learnings) or raw session history and has no supplied object counterpart. SRC-1: `pal/team.py`, `pal/agents/navigator.py`, `pal/agents/settings.py`, `db/session.py`.

> enable_agentic_memory=True,
> search_past_sessions=True,
> num_past_sessions_to_search=10,
> --- `pal/team.py`

#### MEM-OBJ-session-history
Label: Persisted conversational history

Source-native identity: shared database-backed team/agent sessions, with history and past-session search configured. Substrate: PostgreSQL through `agent_db`; exact payloads and inclusion of raw tool results are external/uninspected. Intended material is prior conversational traces, not a demonstrated derived strategy store. Models interpret delivered history; IDs and configured run/session limits are symbolic control inputs. Complements but does not duplicate [RT-RTE-team-dispatch](runtime.md#rt-rte-team-dispatch), which describes the containing invocation route. SRC-1: `pal/team.py`, `pal/agents/navigator.py`, `pal/agents/settings.py`.

> add_history_to_context=True,
> read_chat_history=True,
> num_history_runs=10,
> --- `pal/agents/navigator.py`

#### MEM-OBJ-user-files
Label: Editable user guidance and generated files

Source-native identities: `about-me.md`, `preferences.md`, `voice/`, `templates/`, `meetings/`, `projects/` and proposed `wiki/outputs/` in the context directory. Filesystem/Git substrate; natural-language guidance, scaffolds and saved products, with filenames/tags serving navigation. Static shipped copies alone are not acquired memory. User edits, model-generated notes/reviews/exports and saved substantive answers can survive later invocations. Navigator is asked to read preferences on first interaction, matching voice guide before drafting, and templates as structure. Guidance has model-interpreted behavioral force; saved products have evidential force when later selected. Distinct from the static instruction strings [RT-OBJ-agent-instructions](runtime.md#rt-obj-agent-instructions). Acquisition/read behavior is within [RT-RTE-navigator-work](runtime.md#rt-rte-navigator-work). SRC-1: `pal/instructions.py`, `context/preferences.md`, `app/main.py`.

> - **User → Pal**: Read voice guides, briefs, templates to shape behavior.
> - **Pal → User**: Write summaries, exports via `save_file`. Deletion disabled.
> --- `pal/instructions.py`

The configuration does not split read-only user guidance from writeable generated content at the filesystem grant. Existing source-authored guidance is not proof that a human approved later replacements.

#### MEM-OBJ-pal-tables
Label: Structured user facts

Source-native identity: on-demand `pal_*` tables in PostgreSQL schema `pal`. Symbolic schemas, user IDs and tag arrays support SQL operations; free-text notes/facts remain natural language interpreted after query delivery. Navigator proposes schema and data mutations under conventions, including user-scoped predicates. No populated schema or contents were supplied. These retain entity facts rather than framework preferences or routing descriptions; no supplied object counterpart. Consumers are Navigator SQL queries for retrieve/connect and later synthesis, with optional Discovery entries guiding targeting. SRC-1: `pal/instructions.py`, `pal/tools/build.py`, `db/session.py`; [RT-RTE-navigator-work](runtime.md#rt-rte-navigator-work).

> The user's structured data: notes, people, projects, decisions. You own the schema. Tables are created on demand.
> --- `pal/instructions.py`

### Routes

#### MEM-RTE-knowledge-update
Label: Model-authored routing update and reuse

Navigator, Researcher, Compiler or Linter model → bound `update_knowledge` tool → PostgreSQL/PgVector contents/index → later knowledge search → model → targeted file/SQL retrieval. Distinct from deterministic [RT-RTE-context-refresh](runtime.md#rt-rte-context-refresh); both write [MEM-OBJ-pal-knowledge](#mem-obj-pal-knowledge). Owners: specialist proposes title/content; Python calls insertion; external Knowledge implements admission/storage/search. Trigger: meaningful discovery or schema/file/source change in an open request. Metadata-only instructions shape proposal, but there is no inspected semantic validator, per-entry human veto or title-prefix check. No answer oracle. Failure propagates through external insertion; no wrapper rollback. Updating/replacing prior entries is instructed for learnings, but this tool does not pass the loader's `upsert=True`. SRC-1: `pal/tools/knowledge.py`, `pal/tools/build.py`, `pal/instructions.py`.

> knowledge.insert(name=title, text_content=content)
> return f"Knowledge updated: {title}"
> --- `pal/tools/knowledge.py`

- Immediate return: Confirmation string following insertion; not evidence of unique replacement.
- Later read-back: Knowledge-enabled specialists can search descriptions, then use described files/tables; Discovery guidance requests direct targeting.
- Delegated visibility: Leader receives specialist output under external team propagation; full inserted payload visibility to leader is uninspected.
- Selection predicate: Model uses topic/intent to formulate search; hybrid index retrieval is dependency-owned; fixed title alone is not a targeting algorithm.
- Invalidation or expiry: No explicit per-entry TTL/retraction in this wrapper; loader recreate removes the shared vector index, including these non-file entries.
- Activation or effect: Store insertion is wired; improved targeting and actual downstream reliance remain unobserved.
- Evidence limits: No live contents, ranking trace, token budget or identity enforcement supplied; metadata directive does not constrain arbitrary inserted strings.
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### MEM-RTE-learning-reuse
Label: Operational learning write and reuse

Interaction/history or explicit correction → configured AGENTIC LearningMachine / requested `save_learning` → `pal_learnings` → requested learning search or automatic context addition → later leader, Navigator or conditional Researcher model. Compared with [RT-RTE-navigator-work](runtime.md#rt-rte-navigator-work) and [RT-RTE-team-dispatch](runtime.md#rt-rte-team-dispatch), this is a cross-invocation update/consumer chain rather than one action/delegation episode. No single supplied route has exactly this referent. SRC-1: `pal/team.py`, `pal/agents/navigator.py`, `pal/agents/researcher.py`, `pal/instructions.py`, `app/main.py`.

> learning=LearningMachine(
>     knowledge=pal_learnings,
>     learned_knowledge=LearnedKnowledgeConfig(mode=LearningMode.AGENTIC),
> ),
> add_learnings_to_context=True,
> --- `pal/agents/researcher.py`

Pal wires the dependency, while doctrine says the agent chooses what to learn from interactions. Requested explicit writes include successful retrieval strategies, recurring behaviors and user fixes. This gives known subsequent transformation intent despite unknown initial contents and opaque extraction. A user supplying a correction contributes content, not necessarily approval of the eventual stored formulation. No universal per-learning approval gate is visible. Search-before-save, dates, recency and Correction precedence are model instructions, not inspected database constraints. Proposer/decider are the model/framework as configured; exact extraction, rejection and revision capabilities are uninspected. Operating mode: open interactions and a fixed Monday summary request; no reference-outcome oracle supplied. Recovery is requested updating/verification, not a demonstrated rollback route.

- Immediate return: Framework learning-tool result or model answer; exact write acknowledgement format is uninspected.
- Later read-back: Navigator is instructed to search strategies/corrections; leader and conditional Researcher explicitly request added learnings; Monday request asks the team to query and summarize recent learnings.
- Delegated visibility: Leader and Researcher each configure learning independently; specialist-return filtering remains external; shared store does not establish shared complete prompt contents.
- Selection predicate: Foreground Navigator uses intent/topic and requested search; automatic addition uses dependency-owned selector/inputs and budget, uninspected. Pal does not specify a token/count budget for learnings.
- Invalidation or expiry: Prompt asks search-before-save, update rather than duplicate, prefer corrections then recent, verify missing references. Exact replacement, expiry and automatic deletion are uninspected.
- Activation or effect: Behavioral guidance can influence later retrieval/response generation; actual changed decisions or improved capacity are unobserved.
- Evidence limits: No retained learning sample, input-to-derived-entry trace, injected payload or measured outcome. AGENTIC label alone proves neither autonomous quality control nor learning benefit.
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### MEM-RTE-conversation-reuse
Label: Personal memory and session continuity

Leader/Navigator invocation → shared PostgreSQL-backed framework persistence → later same agents' configured memory/history/session interfaces → generation context. This cross-invocation retention route complements the immediate delegation route [RT-RTE-team-dispatch](runtime.md#rt-rte-team-dispatch). Personal derived memory [MEM-OBJ-user-memory](#mem-obj-user-memory) and historical traces [MEM-OBJ-session-history](#mem-obj-session-history) are distinct parts, not interchangeable forms of one summary. SRC-1: `pal/team.py`, `pal/agents/navigator.py`, `pal/agents/settings.py`, `db/session.py`.

> enable_agentic_memory=True,
> search_past_sessions=True,
> num_past_sessions_to_search=5,
> --- `pal/agents/navigator.py`

Trigger/owner: external Agno manages configured persistence and context building; foreground model can request history/session search and memory tools. Leader instructions constrain `update_user_memory` to preferences, sending facts/entities to Navigator SQL instead. That is policy, not an inspected storage partition. Admission: framework/model updates without a visible per-memory human gate; exact extracted content and veto/rejection/rollback controls are external. Operating mode: open conversations; no answer oracle. Guidance is [RT-OBJ-agent-instructions](runtime.md#rt-obj-agent-instructions), not evidence of actual data segregation.

- Immediate return: Current response; external framework owns persistence acknowledgements and memory tool results.
- Later read-back: Requested history injection, history read tools and past-session search; agentic personal-memory inclusion details remain dependency-internal.
- Delegated visibility: Requested brief question/context and leader synthesis do not prove isolated member windows or that only a final return escapes.
- Selection predicate: Leader history five runs / past-session search ten; Navigator history ten / past-session search five. Exact turn/tool filtering, user/session scoping, search query algorithm and personal-memory selection are uninspected.
- Invalidation or expiry: Configured history limits restrict inclusion, not demonstrated deletion from storage. Past-session search affords later access to older material; no explicit Pal summary/checkpoint, eviction TTL or personal-memory rollback is supplied.
- Activation or effect: Database/context interfaces are wired; exact loaded payload, downstream reliance and continuity quality are unobserved.
- Evidence limits: No supplied sessions; raw traces, derived preferences and any host checkpoint forms cannot be reconstructed from flags. Neither compaction nor verbatim full-history persistence is established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

### Claims

#### MEM-CLM-service-boundary
Label: Knowledge service and memory-tier limits

Claimed operation: source doctrine calls Researcher a datetime-only stateless worker alongside Compiler/Linter/Syncer, but its actual conditional constructor configures LearningMachine and `add_learnings_to_context=True`. This qualifies the source claim; it does not establish Researcher chat-history/session memory. The positive configuration passage is retained in [MEM-RTE-learning-reuse](#mem-rte-learning-reuse). SRC-1: `docs/SPEC.md`, `pal/agents/researcher.py`.

> - **Researcher, Compiler, Linter, Syncer**: Datetime context only. No memory, no session search. These are stateless workers that get fresh context per invocation.
> --- `docs/SPEC.md`

AgentOS registers both knowledge handles, independently of custom tool wrappers:

> knowledge=[pal_knowledge, pal_learnings],
> --- `app/main.py`

This is an included alternative service surface. Exact exposed ingestion/search/deletion API operations, caller authority and admission rules depend on uninspected Agno. Registration is not proof of a concrete external read-back consumer or of unrestricted writes. Closest supplied control claim [RT-CLM-control-scope](runtime.md#rt-clm-control-scope) concerns configured grants; this record concerns the unresolved service/learning coverage and conflicting source doctrine.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-retained-guidance
Label: Retained operational guidance authority

Consumer: leader, Navigator and conditional Researcher generation calls for learnings; leader/Navigator for personal memory; Navigator for edited preference/voice files. Channel: requested automatic learning addition or tool-mediated read/search results, plus external memory injection. Force: model-interpreted guidance, including requested Correction precedence and voice/style constraints; no hard semantic precedence enforcement is inspected. Horizon: persisted database entries/files can reach later sessions until revised/removed or no longer selected. Distinct from static shipped instruction authority [RT-BAP-agent-guidance](runtime.md#rt-bap-agent-guidance). Evidence: [MEM-RTE-learning-reuse](#mem-rte-learning-reuse), [MEM-RTE-conversation-reuse](#mem-rte-conversation-reuse), [MEM-OBJ-user-files](#mem-obj-user-files). SRC-1: `pal/instructions.py`, `pal/team.py`, `pal/agents/researcher.py`.

> If recall returns conflicts, `Correction:` wins, then most
> recent.
> --- `pal/instructions.py`

Derived guidance can be intended to shape later choices without preserving full reasons. Neither delivery nor priority language establishes activation or benefit.

## Annotations

#### On [RT-OBJ-manifest](runtime.md#rt-obj-manifest)

Storage is context `raw/.manifest.json`, independently written from raw frontmatter. Ingest appends descriptive title/source/time and symbolic filename/boolean; Compiler's requested compiled-false scan interprets tool-returned JSON through its model. The update tool marks the first matching filename true without rewriting raw `compiled: false`. Provenance/correctness and freshness of derived articles are not validated. Raw overwrites can invalidate derived content without resetting every old entry or article. SRC-1: `pal/tools/ingest.py`, `pal/agents/compiler.py`; quotation support is in the supplied record and [MEM-OBJ-raw](#mem-obj-raw).

#### On [RT-RTE-raw-ingest](runtime.md#rt-rte-raw-ingest)

Retention includes complete content, a Researcher summary, or an extraction stub, not merely source metadata. Direct API fixed writes admit supplied text or fetched content without model selection or content-level human approval; the generic API caller is not necessarily a human. Researcher selects/curates under a preference for official sources. Source labels and URL citations do not authenticate correctness. Later Compiler reads full selected raw; Navigator can read raw before compilation. Persistence is filesystem/Git when sync occurs; metadata indexing is separate. Quotes in the supplied route and [MEM-OBJ-raw](#mem-obj-raw) support these distinctions. SRC-1: `pal/tools/ingest.py`, `pal/agents/researcher.py`, `app/router.py`.

#### On [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance)

Write-side material is separated into [MEM-OBJ-wiki-articles](#mem-obj-wiki-articles), [MEM-OBJ-wiki-index](#mem-obj-wiki-index), [MEM-OBJ-wiki-state](#mem-obj-wiki-state), [MEM-OBJ-lint-report](#mem-obj-lint-report) and the supplied manifest. Tool calls persist model proposals without checking source fidelity or mandatory lint. Compiler's full raw read and 200–500-word summary are instructions, not observed transformations. Navigator receives selected articles after index scan, not automatically every article/source/rationale. Index has no explicit token bound. Linter receives articles via reads and writes criticism; later Compiler consumption of that criticism is not mandatory. Force compile changes a team prompt while ordinary Compiler guidance remains incremental. SRC-1: `pal/agents/compiler.py`, `pal/agents/linter.py`, `pal/tools/wiki.py`, `app/router.py`; quotations in the supplied route and objects above.

#### On [RT-RTE-context-refresh](runtime.md#rt-rte-context-refresh)

Selector is deterministic sorted recursive discovery of md/txt/yaml/yml/json files, including hidden JSON metadata files if matched. It reads frontmatter tags or uses general-context, and retains path/size/tags/indexed-time rather than body content. No content token budget is needed for the omitted body, but embeddings/search and total result budgets remain external. Insertion requests upsert; ordinary refresh has no explicit removed-path pruning. Recreate warns about all routing types then calls vector deletion, not explicit contents-table deletion. If no files are discovered it returns before recreate. Thus “clear and reload” is conditional, and no-source discovery does not prove an emptied index. SRC-1: `context/load_context.py`; metadata quotation in [MEM-OBJ-pal-knowledge](#mem-obj-pal-knowledge), insertion quotation in supplied route.

#### On [RT-RTE-navigator-work](runtime.md#rt-rte-navigator-work)

Read-back has several distinct consumers: article content informs an answer; voice/preferences guide drafting; SQL retrieves entity facts; routing metadata chooses subsequent sources; learnings guide retrieval behavior. Query intent and model-interpreted index/Discovery descriptions perform intended targeting, while `read_file` only fetches the requested identifier. Recall/read instructions request structure-first relevant sections, per-source summaries, SQL pattern summaries and email thread segments. These manage current context, not necessarily retained summary checkpoints. SQL/FileTools permit updates admitted by model tool choices; input authorship and user request do not constitute per-generated-content approval. Offer-to-file substantive answers is a conditional retention path, not automatic storage of every answer. Source support: [MEM-OBJ-user-files](#mem-obj-user-files), [MEM-OBJ-pal-tables](#mem-obj-pal-tables), [MEM-BAP-retained-guidance](#mem-bap-retained-guidance); SRC-1: `pal/instructions.py`, `pal/tools/build.py`.

#### On [RT-RTE-team-dispatch](runtime.md#rt-rte-team-dispatch)

Requested brief delegation and synthesis can bound working inputs/returns, but exact separate-frame context filtering is external. Configured history limits exclude older runs from requested recent context, without proving their deletion; session search is a reload path. The stack-frame analogy is therefore partial: selected handoff and return are requested, but wholesale frame eviction and return-only escape are unestablished. File paths are pointers for later explicit tool reads; content delivered to a model is by value, not an automatically dereferenced persistent reference. The actual retained memory objects and continuity selector limits are in [MEM-RTE-conversation-reuse](#mem-rte-conversation-reuse). SRC-1: `pal/team.py`, `pal/agents/navigator.py`; handoff quotation in [RT-OBJ-agent-instructions](runtime.md#rt-obj-agent-instructions).

#### On [RT-RTE-git-sync](runtime.md#rt-rte-git-sync)

Git transports context files, including editable guidance, raw/wiki products and access metadata, not `pal_learnings`, user memories or PostgreSQL sessions. Push stages all context changes; pull can admit remotely authorized replacements/deletions without semantic review. Remote authorship is unresolved. Pulled file contents become available to later file reads; vector routing metadata is refreshed by a separate loader/schedule, not automatically as part of pull. Git history permits external manual recovery but no inspected semantic retraction propagation to articles/index/knowledge entries. Local commit survival after push failure is supported by the supplied route. SRC-1: `pal/tools/git.py`, `app/main.py`, `context/load_context.py`.

#### On [RT-RTE-evaluation-driver](runtime.md#rt-rte-evaluation-driver)

Dependent tests can reuse session IDs, so later tests are shipped consumers of prior conversational state, not hypothetical API callers. Cleanup removes raw/wiki files, including manifest/index/state/report, then recreates wiki subdirectories. It does not visibly clear SQL, learned knowledge or sessions; “clean state” is restricted to those files. Stale vector pointers and memories can therefore remain possible after file cleanup. This is a destructive software admission path initiated by running the evaluator, not model-approved withdrawal or a file-tool grant. Evaluation outputs are reported to the operator; no retained score-to-policy consumer is established. SRC-1: `evals/extended_smoke.py`, `evals/smoke.py`, `evals/run.py`; supplied route contains evaluation quotation.

## Write side

| Mechanism | Authorship/transformation | Admission and human contribution | Retained result and recovery limit |
|---|---|---|---|
| Direct ingest | Caller text or URL extractor; fixed frontmatter/slug generation | API validates presence of text/URL, not truth. Generic caller identity unresolved; no per-content approval of fetched text | [MEM-OBJ-raw](#mem-obj-raw), manifest; stubs admitted, same slug overwrites; no multi-file transaction. |
| Researcher ingest | Model selects sources, may summarize multi-page material | Model tool decision plus ordinary ingest writes; official-source preference is policy | Raw and optional routing entry; user initiating research does not approve each summary. |
| Compiler | Model transforms raw into summaries, concepts, links and index | Model judgment admitted by broad FileTools and custom setters; no oracle or mandatory human/lint veto | Wiki articles/index/state and manifest flags; source links requested, not verified; overwrite/manual Git recovery. |
| Linter | Model compares articles and optionally searches for gaps | Model admits findings/report and state update; recommendation is not article rejection | Lint report/Discovery entries; no automatic withdrawal/repair transition. |
| Routing loader | Code derives metadata, remote embedder derives vectors | CLI/API/schedule authorizes batch operation; no per-entry human decision | Routing index; recreate can discard non-file discoveries; no-file return avoids deletion. |
| Specialist routing update | Model writes descriptions from file/schema/source discoveries | Tool accepts arbitrary title/content; no semantic check | [MEM-RTE-knowledge-update](#mem-rte-knowledge-update); replacement semantics external. |
| LearningMachine and requested learning writes | Model/framework derives operational material from interactions/corrections | AGENTIC configuration, not explicit per-entry human approval; precise extraction/rejection external | [MEM-RTE-learning-reuse](#mem-rte-learning-reuse); no guaranteed input/outcome reasons retained. |
| Personal memory/history | Framework persistence/extraction; leader preference-only rule | Model/framework admission; user contribution differs from approval of formulation | [MEM-RTE-conversation-reuse](#mem-rte-conversation-reuse); exact payload/update/deletion opaque. |
| File/SQL captures, review and drafting | Navigator writes notes/facts/files from requests and sources | Model tools admit; some requested actions ask confirmation, not a universal retention gate | User files/SQL; no Pal-wide rollback or cross-store retraction. |
| User edits/remote Git | Human or remote actor can replace guidance/content; exact author unknown | Filesystem/remote permission boundary and Git operation, not content review | File consumers see subsequent reads; vectors may lag. |
| Evaluation cleanup | Fixed deletion of raw/wiki | Software driver admits deletion; launching suite is not per-file content approval | Files withdrawn without clearing all other memory stores. |

The source passages and route annotations above support these mechanisms. Raw traces and derived behavioral material remain separate: history/session persistence is not itself an operational strategy; `pal_learnings` is the intended trace-to-guidance result. Source compilation is a raw-document-to-derived-knowledge route, not automatically trace learning. Current-context summarization instructions do not establish a durable compaction result delivered at a later invocation. Unknown framework initialization and trace serialization remain local to conversational/learning objects rather than negating known file transformations.

## Read-back

The ordinary knowledge chain is request → Navigator index scan → selected article tool result → synthesis, with manifest/raw fallback and then live sources. The routing chain is request/intent → knowledge or learning search → resource/strategy description → file/SQL/live retrieval → synthesis. Both are foreground-requested selection; only configured history/learning additions are automatic context-supply requests. None proves that supplied text changed a decision. See [RT-RTE-navigator-work](runtime.md#rt-rte-navigator-work), [MEM-RTE-knowledge-update](#mem-rte-knowledge-update), [MEM-RTE-learning-reuse](#mem-rte-learning-reuse).

Automatic selection has different budgets: five/ten recent history runs and ten/five past sessions for leader/Navigator, but no specified learning token budget, memory entry count or exact injected payload. Compiler summary length is guidance for derived content, not an enforced context ceiling. File structure-first and per-source summarization are instructions for foreground selection, not an inspected host compactor. External session checkpoints and selection algorithms remain uninspected. SRC-1: `pal/team.py`, `pal/agents/navigator.py`, `pal/agents/compiler.py`, `pal/instructions.py`.

The scheduled Monday query names an actual later learning consumer role; scheduled weekly review asks the team to derive a saved file from conversations/decisions/action items. Scheduling wires those requests, not successful execution. Compiler/Linter/Navigator are concrete later file consumers, while a lint report's intended Compiler repair remains only an afforded/instructed possibility, not a forced loop. File storage and exposed knowledge handles alone are not additional consumer routes. SRC-1: `app/main.py`, `pal/agents/compiler.py`, `pal/agents/linter.py`; [MEM-CLM-service-boundary](#mem-clm-service-boundary).

## Integration issues

- **Source doctrine correction:** Researcher is not wholly memory-free in the constructor: conditional LearningMachine plus context inclusion contradicts the datetime-only description. This adds a learning producer/consumer to any tier summary without asserting history/session search for Researcher. [MEM-CLM-service-boundary](#mem-clm-service-boundary), [MEM-RTE-learning-reuse](#mem-rte-learning-reuse); SRC-1: `pal/agents/researcher.py`, `docs/SPEC.md`.
- **Refine supplied refresh wording:** runtime says recreate can delete the entire knowledge vector index. Direct inspection confirms that scoped statement, but not deletion of contents tables, and discovers that no-files return precedes recreate. Ordinary refresh has no explicit pruning. Consequence: neither logical full reset nor guaranteed stale-pointer withdrawal follows. [RT-RTE-context-refresh](runtime.md#rt-rte-context-refresh), [MEM-OBJ-pal-knowledge](#mem-obj-pal-knowledge); SRC-1: `context/load_context.py`.
- **Manifest/frontmatter divergence:** update marks the first filename match only in manifest; raw frontmatter stays false and same-slug admissions append duplicate entries. Consequence: compiled labels are control requests, not verified complete or synchronized provenance. [RT-OBJ-manifest](runtime.md#rt-obj-manifest), [MEM-OBJ-raw](#mem-obj-raw); SRC-1: `pal/tools/ingest.py`.
- **Repair consumer unresolved:** lint instructions name Compiler as fixer, but Compiler's ordinary route selects uncompiled raw. No mandatory lint-result consumption, article rejection or corrective iteration is established. [MEM-OBJ-lint-report](#mem-obj-lint-report), [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance); SRC-1: `pal/agents/linter.py`, `pal/agents/compiler.py`.
- **Opaque but included routes:** framework learning extraction, personal-memory payload, history serialization/selection and knowledge-service operations cannot be fully assessed from local wrappers. Consequence: exact trace origin mix, rationale retention, prompt delivery, budget and per-user authority remain unresolved, not absent. [MEM-RTE-learning-reuse](#mem-rte-learning-reuse), [MEM-RTE-conversation-reuse](#mem-rte-conversation-reuse), [MEM-CLM-service-boundary](#mem-clm-service-boundary); SRC-1: `pal/team.py`, `pal/agents/navigator.py`, `app/main.py`.
- **No duplicate declarations identified after comparison with supplied runtime.** Existing routes/manifest/model components receive annotations or citations rather than new identities. New knowledge-update and continuity/learning routes overlap Navigator/team activity but span different cross-invocation transformations; individual retained objects are not replacement declarations for those containing invocation routes. Peer epistemic/workflow records were not supplied, so cross-specialist identity reconciliation remains open.

## Limitations and checks

This is source-grounded implementation/configuration and doctrine analysis, not a run report. No populated corpus proves faithful compilation, no remembered correction proves later reliance, and no evaluation result proves improved future capacity. Explicit correction-priority and source-tracking instructions do not close those evidence gaps. Framework/provider internals, live grants, database/remote content, exact model-visible payloads and actual history/learning budgets remain outside the available evidence.

Source identity and clean HEAD were rechecked against the supplied boundary. The method inputs were read completely, including bounded continuation reads. Counterexamples tested consequential generalizations: direct ingest bypasses agent selection/sync; Researcher can curate “raw”; stubs survive admission; manifest marking does not certify articles; recreate is vector-only and conditional; evaluation cleanup bypasses deletion-disabled tools; Researcher learning contradicts the stateless-worker description. These checks narrow attribution without converting unavailable execution evidence into absence.

Deterministic validation: the invocation-specific `commonplace-run validate-output` check passed. This establishes structural/quotation checks only, not semantic acceptance or observed operation.
