---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Stash memory: caller observations, model-derived knowledge, typed state and selective reload with non-propagating withdrawal."
run-id: AAS-2026-10-15-stash-7ac5612837a0-01
source-identity: https://github.com/alash3al/stash
reviewed-boundary: d34ed430c4348ef741ef95146b488aea8616f4fb
---

# Stash memory report

## Boundary and evidence

The subject is the self-hosted Stash memory system at SRC-1, commit d34ed430c4348ef741ef95146b488aea8616f4fb. This member includes caller admission, all eight maintenance stages, typed read/write APIs, MCP tools, CLI dispatch, embedded agent instructions, working focus, checkpoints, namespaces, settings and embedding cache. External agents' actual histories, authorship, message-window management and response decisions remain outside the implementation boundary. Provider weights are opaque external state, not the stored vectors. Stash Cloud remains excluded. Source declarations are in [boundary](boundary.md#source-register); no new source was introduced.

Direct implementation reads added to the supplied runtime cover the Brain state modules, consolidation stages, recall and consolidation SQL templates, models, embedding cache, the complete MCP registry and CLI command registry, and reasoner methods for all maintenance transformations. Direct doctrine reads cover the server-description/session protocol in `cmd/cli/mcp_prompts.tmpl`. Migration FK and settings uses were structurally searched. Driver/bootstrap guarantees and model fixity use the supplied runtime findings rather than a repeated dependency audit. Other template descriptions, full schema constraints, provider internals and deployment are not exhaustively inspected. Available but uninspected material is not an access gap. There is no observed-run or causal-experiment evidence.

| Entry point / operation | SRC-1 paths | Coverage and limits |
|---|---|---|
| CLI Before/After, ordinary remember/recall, SSE/stdio | `cmd/cli/main.go`, `cmd/cli/mcp.go`, `internal/brain/episode.go`, `internal/brain/recall.go` | Direct registry and Brain reads; supplied [RT-RTE-remember-write](runtime.md#rt-rte-remember-write), [RT-RTE-recall-read](runtime.md#rt-rte-recall-read). Adapter-specific validation uses runtime. |
| Manual/tool/timer/combined maintenance | `internal/brain/consolidate.go`, `cmd/cli/consolidate.go`, `cmd/cli/serve_all.go`, `cmd/cli/mcp.go` | Direct orchestration and MCP ticker; other drivers supplied by [RT-RTE-consolidation-run](runtime.md#rt-rte-consolidation-run). No exercised scheduling or exclusive ownership conclusion. |
| Episode clustering, fact synthesis, deduplication, inline contradictions | `internal/brain/consolidate.go`, `internal/brain/contradiction.go`, `internal/reasoner/openai.go` | Direct; [MEM-OBJ-fact](#mem-obj-fact), [MEM-RTE-fact-withdrawal](#mem-rte-fact-withdrawal); extraction admission also supplied by runtime. |
| Relationships, causal links, abstractions | `internal/brain/consolidate.go`, `internal/brain/causal.go`, `internal/brain/fact.go`, `internal/reasoner/openai.go` | Direct; [MEM-RTE-edge-extraction](#mem-rte-edge-extraction), [MEM-RTE-pattern-extraction](#mem-rte-pattern-extraction). QueryPatterns exists, but no shipped caller found in the frozen Go tree. |
| Goal creation/edit/completion/abandonment/deletion and progress annotation | `internal/brain/goal.go`, `internal/brain/consolidate_goal.go`, `cmd/cli/main.go`, `cmd/cli/mcp.go` | Direct; [MEM-RTE-goal-maintenance](#mem-rte-goal-maintenance). Individual CLI adapter error handling not audited. |
| Failure creation/deletion/listing, repeats and pattern facts | `internal/brain/failure.go`, `internal/brain/consolidate_failure.go`, `internal/reasoner/openai.go` | Direct; [MEM-RTE-failure-derivation](#mem-rte-failure-derivation). Original failures may be agent-authored reports, not authenticated execution traces. |
| Hypothesis creation/test/refine/confirm/reject/delete and evidence scan | `internal/brain/hypothesis.go`, `internal/brain/consolidate_hypothesis.go`, `internal/reasoner/openai.go`, `cmd/cli/main.go`, `cmd/cli/mcp.go` | Direct; [MEM-RTE-hypothesis-maintenance](#mem-rte-hypothesis-maintenance). Refinement has a source-level timestamp defect; successful revision cannot be claimed. |
| Forget/purge, confidence decay, contradiction resolution | `internal/brain/episode.go`, `internal/brain/fact.go`, `internal/brain/decay.go`, `internal/brain/contradiction.go`, `cmd/cli/main.go` | Direct; [MEM-RTE-fact-withdrawal](#mem-rte-fact-withdrawal). PurgeFact is a library operation with an unregistered CLI adapter, not a demonstrated CLI route. |
| Query/list/ID-based reload and causal traversal | `internal/brain/fact.go`, `internal/brain/causal.go`, `internal/brain/hypothesis.go`, `internal/brain/goal.go`, `internal/brain/failure.go`, `cmd/cli/mcp.go` | Direct; [MEM-RTE-typed-read](#mem-rte-typed-read). Getter alone establishes capability where no caller is wired. |
| Exact-namespace focus | `internal/brain/context.go`, `cmd/cli/mcp.go` | Direct; annotation on [RT-RTE-context-handoff](runtime.md#rt-rte-context-handoff). No host-window eviction control or enforced TTL inferred. |
| Init/create/list namespace; checkpoint persistence | `internal/brain/namespace.go`, `internal/models/models.go`, `cmd/cli/mcp.go` | Direct; [MEM-OBJ-namespace](#mem-obj-namespace), [MEM-OBJ-consolidation-progress](#mem-obj-consolidation-progress). Human initialization approval remains unresolved. |
| Vector/cache/model compatibility, settings | `internal/embedder/cache.go`, `internal/db/db.go`, `internal/db/migrations/` | Cache direct; settings/FKs searched; runtime supplies dimension lock. [MEM-OBJ-embedding-cache](#mem-obj-embedding-cache), [MEM-OBJ-settings](#mem-obj-settings). Full constraints and DB implementation uninspected. |
| Static protocol, release machinery, observability | `cmd/cli/mcp_prompts.tmpl`, `.github/workflows/release.yml`, `internal/observability/metrics.go` | Protocol directly read; release/instrumentation supplied by runtime. Static prompts are not operation-updated memory. Metrics do not establish learning or quality. |

## Core ideas

1. Stash separates caller observations from derived summaries, but not all facts come from observation consolidation. Failure-pattern synthesis and hypothesis confirmation admit facts through different checks. These alternatives prevent treating every recall result labelled `fact` as extraction-validated or episode-provenanced. See [MEM-OBJ-fact](#mem-obj-fact), [MEM-RTE-failure-derivation](#mem-rte-failure-derivation) and [MEM-RTE-hypothesis-maintenance](#mem-rte-hypothesis-maintenance).
2. Read-back is primarily caller-pulled. Semantic recall allocates slots to facts before episodes; typed tools expose material that recall does not select. Row limits are not token budgets. Background consolidation pushes changes into PostgreSQL, not unsolicited context into an external agent. See [RT-RTE-recall-read](runtime.md#rt-rte-recall-read), [MEM-RTE-typed-read](#mem-rte-typed-read).
3. Withdrawal is local, not a general truth-maintenance cascade. Fact expiry/supersession sets validity metadata that recall and later maintenance do not filter. Forgetting an episode does not withdraw its derived facts. Resolving a contradiction hides the unresolved record without changing either fact. See [MEM-RTE-fact-withdrawal](#mem-rte-fact-withdrawal).
4. Retained text has two different authorities: evidence for Stash's maintenance model and knowledge/advice delivered to the external agent. Neither delivery nor a confidence number establishes external compliance, semantic correctness or benefit. See [MEM-BAP-maintenance-input](#mem-bap-maintenance-input), [MEM-BAP-retained-advice](#mem-bap-retained-advice).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-episode
Label: Episode content and event metadata

Source-native identity: `models.Episode` and PostgreSQL `episodes`. Natural-language content is caller-supplied, except automatically generated repeat-failure episodes; timestamp/namespace/ID/deleted state are symbolic event/access metadata. Dense embeddings are a distinct operative part in [MEM-OBJ-memory-vectors](#mem-obj-memory-vectors). The text can be a report or session summary rather than an actual raw execution trace. Human versus agent authorship and initial admission control are unresolved; subsequent Repeat Failure writes are software/model-generated. Recall and consolidation consume the text, while getters can expose deleted rows. Closest supplied record is [RT-RTE-remember-write](runtime.md#rt-rte-remember-write), a write route rather than this retained object. [SRC-1: `internal/models/models.go`, `internal/brain/episode.go`, `internal/brain/consolidate_failure.go`]

> content := fmt.Sprintf("REPEAT FAILURE [failure #%d]: %s", r.FailureID, r.Evidence)
> --- `internal/brain/consolidate_failure.go`

#### MEM-OBJ-fact
Label: Fact text, structure and provenance

Source-native identity: `models.Fact`, `facts`, `fact_sources`. PostgreSQL holds natural-language summary/content, symbolic entity/property/value strings consumed by exact field matching, confidence/validity metadata and episode-source associations. Structured values also require model interpretation when delivered as text. Dense embeddings are separated below. Lineage alternatives are clustered episodes, failure-pattern reasoning, or verbatim confirmed hypothesis content. Source association writes in episode synthesis ignore errors; other two admissions do not create episode associations here. Raw reasons are not generally stored with the summary; association IDs can permit reconstruction through storage APIs, but recall does not deliver sources or validity fields. Later consumers include recall, QueryFacts and maintenance's relationship, causal, pattern, goal and hypothesis models. Confidence is not an independently calibrated truth measure. This object is distinct from supplied [RT-RTE-consolidation-run](runtime.md#rt-rte-consolidation-run), the container maintenance route. [SRC-1: `internal/brain/consolidate.go`, `internal/brain/consolidate_failure.go`, `internal/brain/hypothesis.go`, `internal/brain/recall.go`]

> "INSERT INTO fact_sources (fact_id, episode_id) VALUES ($1, $2) ON CONFLICT DO NOTHING",
> --- `internal/brain/consolidate.go`

#### MEM-OBJ-memory-vectors
Label: Episode and fact embeddings

Source-native identity: `Episode.Embedding`, `Fact.Embedding`, `embedding_model`. Dense vectors are distributed-parametric representations stored as pgvector columns; model labels and IDs are symbolic metadata. Configured embedding calls generate them from admitted text; vectors are not model weights or readable summaries. Numerical similarity selects recall candidates, clusters episodes and deduplicates facts. Repeat-failure episodes are admitted without vectors and are excluded by semantic recall but remain consolidation inputs. Provider fixity is owned by [RT-CMP-openai-embedder](runtime.md#rt-cmp-openai-embedder), not this object. Same-dimension model switching need not preserve vector meaning. [SRC-1: `internal/brain/consolidate.go`, `internal/brain/consolidate_failure.go`, `internal/queries/recall.sql.tmpl`]

> VALUES ($1, $2, NULL, '', $3)
> --- `internal/brain/consolidate_failure.go`

#### MEM-OBJ-relationship
Label: Extracted entity relationship

Source-native identity: `models.Relationship`, `relationships`. PostgreSQL holds symbolic edge fields, confidence, source fact ID and deletion metadata. Edge words obtain semantic meaning when read by the pattern model or external agent; fields are not explanatory theories merely because they form a graph. The reasoner derives edges from fact text; QueryRelationships returns them, and pattern extraction reads checkpoint-selected edges. The source fact pointer is retained, not a derivation explanation. Distinct from the supplied consolidation container. [SRC-1: `internal/brain/fact.go`, `internal/brain/consolidate.go`, `internal/reasoner/openai.go`]

> "relationship entity not found in fact content"
> --- `internal/reasoner/openai.go`

#### MEM-OBJ-causal-link
Label: Asserted or extracted causal link

Source-native identity: `models.CausalLink`, `causal_links`. Symbolic fact-ID edges, confidence, method and deletion state live in PostgreSQL. Lineage is a model classification over supplied fact texts or caller assertion. `extracted`/`asserted` are method labels, not causal-experiment evidence. List and recursive trace tools deliver edges to clients; they do not automatically resolve endpoints into factual explanations. Distinct from entity relationships and from the supplied maintenance route. [SRC-1: `internal/brain/causal.go`, `internal/reasoner/openai.go`]

> VALUES ($1, $2, $3, $4, 'asserted')
> --- `internal/brain/causal.go`

#### MEM-OBJ-pattern
Label: Stored abstraction pattern

Source-native identity: `models.Pattern`, `patterns`. Natural-language abstraction plus symbolic source-ID arrays, coherence/confidence and deletion metadata live in PostgreSQL. A reasoner derives content from fact and relationship display lines. It validates listed IDs, not explanatory warrant. SQL insertion can replace both source arrays with all batch sources if either array is empty, so the retained associations can be broader than the model's selected support. QueryPatterns is an exposed library storage capability; no shipped CLI/MCP/maintenance reader was found in the searched Go tree. External use is unresolved, preventing a wired behavioral-authority claim for pattern rows. No supplied counterpart after comparison; fact-shaped failure patterns are a different object. [SRC-1: `internal/brain/consolidate.go`, `internal/brain/fact.go`, `internal/reasoner/openai.go`]

> if len(sourceFactIDs) == 0 || len(sourceRelIDs) == 0 {
> --- `internal/brain/consolidate.go`

#### MEM-OBJ-contradiction
Label: Conflict and resolution record

Source-native identity: `models.Contradiction`, `contradictions`. PostgreSQL stores symbolic old/new fact identities, entity/property/value snapshots, confidence, classification method and resolved flag; resolution is natural-language text interpreted by clients. A model compares values; admission records a conflict or auto-supersession. The model's explanation is returned by the adapter but not persisted in these inserts. Unresolved listing exposes snapshots/resolution state, not both fact bodies. Generic resolution marks the row resolved without factual repair. No supplied object counterpart; maintenance container overlaps the production route. [SRC-1: `internal/brain/contradiction.go`, `internal/reasoner/openai.go`]

> `UPDATE contradictions SET resolved = TRUE, resolution = $2, resolved_at = $3 WHERE id = $1`,
> --- `internal/brain/contradiction.go`

#### MEM-OBJ-hypothesis
Label: Hypothesis content, plan and disposition

Source-native identity: `models.Hypothesis`, `hypotheses`. PostgreSQL stores natural-language belief, verification plan and optional rejection reason; symbolic status, source-ID array, confidence, timestamps and confirmed-fact link control transitions. Caller creates/refines content; a later model scan changes status/confidence or rejects it. The scan receives content/status/confidence, not the verification plan or stored source IDs/rejection reason. Rejection reasoning persists and can reach list/show clients, but rejected rows leave the automatic open-hypothesis selector. Successful support/weakening reasoning is not retained by this stage. Distinct from supplied maintenance container and created Fact. [SRC-1: `internal/brain/hypothesis.go`, `internal/brain/consolidate_hypothesis.go`, `internal/reasoner/openai.go`]

> hypLines = append(hypLines, fmt.Sprintf("[Hypothesis %d] (status: %s, confidence: %.2f) %s", h.ID, h.Status, h.Confidence, h.Content))
> --- `internal/reasoner/openai.go`

#### MEM-OBJ-goal
Label: Persistent goal and progress notes

Source-native identity: `models.Goal`, `goals`. PostgreSQL holds natural-language intended outcome/notes plus symbolic parent, priority, status, timestamps and deletion metadata. Caller creation, editing and completion coexist with model-generated progress explanations appended to notes. Later list/show clients receive notes; the progress reasoner receives goal content only, not accumulated notes. Completion can automatically complete ancestors through child counts. Distinct from supplied context handoff: this is durable intended outcome, not singular current focus. [SRC-1: `internal/brain/goal.go`, `internal/brain/consolidate_goal.go`, `internal/reasoner/openai.go`]

> `UPDATE goals SET notes = notes || $2, updated_at = now() WHERE id = $1`,
> --- `internal/brain/consolidate_goal.go`

#### MEM-OBJ-failure
Label: Failure explanation and lesson

Source-native identity: `models.Failure`, `failures`. Natural-language content/reason/lesson plus symbolic goal/namespace/ID/deletion metadata persist in PostgreSQL. Caller supplies every substantive field; the system requires nonempty reason and lesson but does not authenticate an execution outcome. A later failure-pattern model receives all three text fields and recent episode texts. List/show deliver the retained explanation to the external caller. Deleting the row does not itself withdraw generated facts or episodes. No supplied counterpart after comparison. [SRC-1: `internal/brain/failure.go`, `internal/reasoner/openai.go`, `internal/brain/consolidate_failure.go`]

> return nil, fmt.Errorf("brain: failure lesson is required")
> --- `internal/brain/failure.go`

#### MEM-OBJ-context
Label: Singular namespace focus

Source-native identity: `models.Context`, `contexts`. Natural-language focus and symbolic expiry/timestamps persist in PostgreSQL under one namespace key. The caller authors a replaceable handoff; later get returns the focus. Expiry metadata is not a TTL enforcement mechanism in the getter. This is the retained payload of [RT-RTE-context-handoff](runtime.md#rt-rte-context-handoff), not a duplicate route. [SRC-1: `internal/brain/context.go`]

> ON CONFLICT (namespace_id) DO UPDATE SET focus = $2, expires_at = $3, updated_at = now()`,
> --- `internal/brain/context.go`

#### MEM-OBJ-namespace
Label: Namespace routing and descriptive metadata

Source-native identity: `models.Namespace`, `namespaces`. PostgreSQL holds symbolic hierarchical slugs and IDs plus natural-language names/descriptions exposed to clients. Caller create or MCP init upserts these records; ancestor creation is automatic. Init overwrites scaffold names/descriptions through the same upsert, rather than authoring self-knowledge. Content origin remains unresolved; the known software scaffold does not resolve later observation authorship. Listing describes possible selection domains; IDs/slugs select actual storage/maintenance scopes, not caller authorization. Closest supplied [RT-OBJ-server-description](runtime.md#rt-obj-server-description) instructs use but is a static different object. [SRC-1: `internal/brain/namespace.go`, `cmd/cli/mcp.go`]

> "INSERT INTO namespaces (slug, name, description) VALUES ($1, $2, $3) ON CONFLICT (slug) DO UPDATE SET name = EXCLUDED.name, description = EXCLUDED.description, updated_at = now() RETURNING id",
> --- `internal/brain/namespace.go`

#### MEM-OBJ-consolidation-progress
Label: Maintenance cursor state

Source-native identity: `models.ConsolidationProgress`, `consolidation_progress`. Symbolic ID watermarks/times stored in PostgreSQL select later maintenance batches. Software initializes/upserts and saves this operational memory; it is not a natural-language episode summary or private reasoning checkpoint. Stages own different watermarks, except causal extraction reuses relationship extraction's `LastFactID`. The declared `LastDecayRun` field is carried but orchestration does not set it. These cursors influence recovery and skipped/replayed inputs; they carry no semantic rationale. Distinct from [RT-RTE-consolidation-run](runtime.md#rt-rte-consolidation-run), which owns the whole invocation. [SRC-1: `internal/brain/namespace.go`, `internal/brain/consolidate.go`, `internal/models/models.go`]

> sql, args, err := b.queries.FetchFacts(nsID, cp.LastFactID, 30)
> --- `internal/brain/consolidate.go`

#### MEM-OBJ-embedding-cache
Label: Persistent embedding memoization

Source-native identity: `embedder.Cached`, `embedding_cache`. PostgreSQL stores text, symbolic SHA-256/model key and dense vector separately. Software caches provider output for remember, recall and derivation calls. A later Embed invocation can receive the vector rather than call the provider; stored text is not delivered as knowledge through this cache. Endpoint/revision is not part of the durable key; no inspected episode/fact withdrawal clears cached text. Closest supplied [RT-CMP-openai-embedder](runtime.md#rt-cmp-openai-embedder) owns adapter/model fixity, not this accumulated store. [SRC-1: `internal/embedder/cache.go`, `internal/brain/episode.go`, `internal/brain/fact.go`]

> VALUES ($1, $2, $3, $4) ON CONFLICT (text_hash, model) DO NOTHING`,
> --- `internal/embedder/cache.go`

#### MEM-OBJ-settings
Label: Dimension lock and embedding model metadata

Source-native identity: `models.Setting`, PostgreSQL `settings`. Symbolic key/value operational state persists across bootstrap invocations. Database initialization reads/writes the dimension lock and upserts embedding model metadata; the latter is audit metadata, not a model-version filter on recall. Supplied runtime's vector-compatibility account supplies the dimension enforcement evidence. Further setting consumers were not exhaustively audited, so this record claims only those keys. No supplied object counterpart; distinct from provider weights and vectors. [SRC-1: `internal/db/db.go`, `internal/models/models.go`]

> // storeEmbeddingModelMetadata records which embedding model is being used, for audit/monitoring purposes.
> --- `internal/db/db.go`

### Routes

#### MEM-RTE-edge-extraction
Label: Relationship and causal edge admission

This record spans automatic edge admission within [RT-RTE-consolidation-run](runtime.md#rt-rte-consolidation-run), direct `DetectCausalLinks` library admission, and caller `CreateCausalLink` admission. Only the automatic subroute is contained in consolidation; the combined referent is neither part of nor a duplicate of that whole invocation. The direct detector accepts a supplied fact batch, while the MCP assertion handler calls `CreateCausalLink` without entering consolidation. [SRC-1: `internal/brain/consolidate.go`, `internal/brain/causal.go`, `cmd/cli/mcp.go`]

> link, err := bc.Brain.CreateCausalLink(ctx, nsIDs[0], int64(causeID), int64(effectID), confidence)
> --- `cmd/cli/mcp.go`

Brain selects facts after the relationship watermark, asks the reasoner for edges, validates/admits them, and persists edge rows. Relationship extraction takes up to 50 facts individually, checks mentioned entity substrings, requires nonempty fields, suppresses matching source-fact edges, and advances its watermark only without collected errors. Causal extraction then fetches up to 30 facts using that same now-advanced watermark, requires at least two, validates source IDs and rejects self-loops; SQL uniqueness suppresses live duplicate pairs. Thus ordinary successful relationship processing can deprive the causal stage of that just-processed batch. Direct `DetectCausalLinks` and caller `CreateCausalLink` remain alternative admissions; the latter bypasses model extraction checks. Model proposes extracted edges, caller proposes asserted ones, code decides insertion; human per-content approval is not wired in the automatic route. Mode: open requests/maintenance, no answer oracle. Guidance requests directly stated relationships/direct causation; retained edges omit reasoning. Failures leave earlier writes, with retry through later maintenance or caller action rather than atomic rollback. [SRC-1: `internal/brain/consolidate.go`, `internal/brain/causal.go`, `internal/reasoner/openai.go`]

- Immediate return: Edge counts/errors within consolidation, or asserted edge for direct creation.
- Later read-back: QueryRelationships feeds pattern extraction and clients; ListCausalLinks/TraceCausalChain feed clients.
- Delegated visibility: MCP serializes edges as text to its caller; ticker only logs counts.
- Selection predicate: Namespace and LastFactID; relationship entity substring tests versus causal supplied-ID membership/self-loop checks; asserted path uses requested IDs.
- Invalidation or expiry: Causal soft delete excludes later list/trace; relationship/fact purge FKs can cascade, but validity updates do not remove edges here.
- Activation or effect: PostgreSQL edge admission is wired; interpreted downstream causal conclusions remain unobserved.
- Evidence limits: Shared cursor limits coverage; identifier validation is not causal verification. No execution or benefit evidence.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if len(errs) == 0 && maxID > cp.LastFactID {
> cp.LastFactID = maxID
> }
> --- `internal/brain/consolidate.go`

#### MEM-RTE-pattern-extraction
Label: Abstraction admission and library read

Part of: [RT-RTE-consolidation-run](runtime.md#rt-rte-consolidation-run)

Brain fetches up to 30 new facts and 50 new relationships; it needs facts and either at least three facts or some relationships. Insufficient batches can still advance watermarks. Model proposes abstractions under source-support guidance; the adapter checks listed IDs and at least two combined references, which is weaker than the prompt's two-of-one-kind condition. Brain admits nonempty content with confidence derived from source minima and coherence, with source-array fallback described above. No per-content human approval or answer oracle; mode is recurring maintenance. Parse/ID/provider/DB failures can reject output; collected errors prevent normal checkpoint advance, not previous inserts. QueryPatterns enables requested read but no shipped consumer wiring was found. This is separate from failure-pattern fact admission. [SRC-1: `internal/brain/consolidate.go`, `internal/reasoner/openai.go`, `internal/brain/fact.go`]

- Immediate return: Pattern count/errors within maintenance.
- Later read-back: QueryPatterns can return rows; a concrete later external caller is uninspected.
- Delegated visibility: inapplicable — no pattern tool/CLI delivery found; maintenance returns counts rather than pattern contents.
- Selection predicate: Per-namespace pattern watermarks; row budgets 30/50; model-selected support IDs with software fallback.
- Invalidation or expiry: QueryPatterns filters deleted rows; source-ID arrays are not an inspected semantic invalidation cascade.
- Activation or effect: Stored abstractions are wired; behavioral use through an actual consumer remains uninspected.
- Evidence limits: No warrant/quality evaluation, deployed reader or exercised result supplied.
- implementation conclusion status: wired
- read-back conclusion status: afforded
- operation conclusion status: uninspected

> if len(validFacts)+len(validRels) < 2 {
> continue
> }
> --- `internal/reasoner/openai.go`

#### MEM-RTE-goal-maintenance
Label: Caller goal edits and automatic progress annotation

The caller supplies/edits goals and completion/abandonment notes; Brain checks nonempty creation, active parent/status, and SQL success. Automatic maintenance separately selects active goals and up to 30 new facts, requests model assessments, validates goal IDs/categories/confidence and appends explanatory notes. Model suggestion does not complete a goal. Explicit completion can cascade to ancestors when all counted children are completed. Caller identity does not establish human approval; automatic note admission has no human veto or independent outcome oracle. Mode: open requests and maintenance. Guidance asks for relevant progress/completion/contradiction explanations; notes persist, but the next model assessment omits them. Errors can leave partial updates, and the fact watermark advances after the update loop even with collected annotation errors. Soft deletion is separate from completion; no general rollback is wired. This spans caller routes absent from the supplied baseline and one part of [RT-RTE-consolidation-run](runtime.md#rt-rte-consolidation-run); not a duplicate of its full referent. [SRC-1: `internal/brain/goal.go`, `internal/brain/consolidate_goal.go`, `internal/reasoner/openai.go`, `cmd/cli/mcp.go`]

- Immediate return: Goal rows on caller edits, counts/errors for annotation.
- Later read-back: List/show delivers outcome and notes; maintenance reads still-active goal content.
- Delegated visibility: Caller receives JSON/tool text; parent completion is a DB update, not unsolicited advice.
- Selection predicate: Namespace, active/nondeleted goals and goal fact watermark; list uses requested status/parent and priority-descending order.
- Invalidation or expiry: Completed/abandoned goals leave active assessment; soft-deleted rows leave listing. Soft-delete of parent does not invoke a hard-delete FK cascade.
- Activation or effect: Notes and status affect later selectors; downstream task behavior unobserved.
- Evidence limits: Model progress judgment is not verified goal achievement; failed annotation retry is not guaranteed by watermark policy.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> note = fmt.Sprintf("\n[SUGGESTED COMPLETE] %s (confidence: %.2f)", a.Note, a.Confidence)
> --- `internal/brain/consolidate_goal.go`

#### MEM-RTE-failure-derivation
Label: Failure lessons to repeat episodes and pattern facts

Caller CreateFailure requires content/reason/lesson and persists the supplied explanation, without judging correctness. Maintenance selects up to 50 new failure rows and 30 new episodes, supplies failure text/reasons/lessons to the reasoner, validates repetition IDs/nonempty evidence and pattern text/confidence, then admits two materially different results: unembedded repeat episodes carrying failure ID/evidence, and embedded pattern facts without source associations. Model proposes classifications; code decides, with no per-content human veto or reference-outcome oracle. Guidance seeks repeated mistakes and broader themes, but source reports are not authenticated traces. Mode: open caller reports plus maintenance. DB/provider failures reject individual writes without rollback; failure/episode watermarks can advance despite later write errors. With no recent episode text, the failure watermark alone advances. This combines an admission not in runtime with a maintenance part of [RT-RTE-consolidation-run](runtime.md#rt-rte-consolidation-run), distinct from the container as a whole. [SRC-1: `internal/brain/failure.go`, `internal/brain/consolidate_failure.go`, `internal/reasoner/openai.go`]

- Immediate return: Failure row for creation; repeat/pattern counts and errors for maintenance.
- Later read-back: Failures through list/show; pattern facts through recall and later fact maintenance; repeat episodes through later consolidation, not semantic recall without embeddings.
- Delegated visibility: Tool list delivers explanations; background derivation only persists/logs.
- Selection predicate: Namespace and two watermarks, row budgets 50/30, model relevance/type, repetition-ID validation.
- Invalidation or expiry: Failure delete hides input from later list/selection; derived episodes/facts remain under their separate withdrawal rules.
- Activation or effect: Raw report → derived explanation → later fact/episode consumer is wired, not demonstrated improved capacity.
- Evidence limits: Pattern facts omit derivation reasons/source links; repeat evidence is retained but not directly recalled. Cursor advancement may skip failed writes.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if maxFailureID > cp.LastFailureID {
> cp.LastFailureID = maxFailureID
> }
> if maxEpisodeID > cp.LastFailureEpisodeID {
> cp.LastFailureEpisodeID = maxEpisodeID
> }
> --- `internal/brain/consolidate_failure.go`

#### MEM-RTE-hypothesis-maintenance
Label: Hypothesis evidence scan, promotion and rejection

Caller creates uncertain content/plan, can mark testing, confirm, reject, refine or delete through relevant API/CLI/tool surfaces. Automatic maintenance selects open hypotheses and up to 30 new facts, asks for support/weakening/contradiction, checks IDs/category/range, and applies configured thresholds. Strong support moves proposed → testing first; only a later eligible assessment of testing can confirm. Confirmation transactionally inserts an embedded fact from current content and links it, without structured extraction validation or episode-source insertion. Rejection keeps a reason; weaker judgments update confidence without retaining reasoning. No independent answer oracle or automatic execution of verification plans is shown. Model proposes assessments; code owns thresholds/transitions; caller can explicitly decide status, with human control unresolved. Mode: open requests/maintenance. Guidance asks for evidence-responsive confidence, but clamping does not ensure support actually raises confidence. Transaction rollback protects confirmation writes, not the whole pipeline. Refinement is exposed yet assigns the UTC method value instead of calling it, limiting the claim to intended editing affordance. Closest supplied container is [RT-RTE-consolidation-run](runtime.md#rt-rte-consolidation-run); this spans its evidence-scan part and distinct caller admissions. [SRC-1: `internal/brain/hypothesis.go`, `internal/brain/consolidate_hypothesis.go`, `internal/reasoner/openai.go`, `cmd/cli/main.go`, `cmd/cli/mcp.go`]

- Immediate return: Hypothesis/fact rows or rejection state; scan counts/errors.
- Later read-back: Next scan receives open content/status/confidence, list/show exposes plan/reason/state, confirmed fact reaches recall and fact maintenance.
- Delegated visibility: Confirmation returns hypothesis plus fact to caller; auto scan returns counters, not unsolicited reasoning.
- Selection predicate: Namespace, proposed/testing/nondeleted state, fact watermark; supplied-ID validation and configured confirm/reject thresholds.
- Invalidation or expiry: Rejected/confirmed leave open scan; delete hides from listing. Delete does not withdraw an already confirmed fact.
- Activation or effect: Retained dispositions change future eligibility; external belief/task changes unobserved.
- Evidence limits: Verification plan is not passed to the scan; support/weakening reasons disappear. Refinement timestamp defect prevents assuming successful revision.
- implementation conclusion status: wired
- refinement conclusion status: afforded
- operation conclusion status: uninspected

> now := time.Now().UTC
> var h models.Hypothesis
> --- `internal/brain/hypothesis.go`

> reason = "Auto-rejected: contradicting evidence detected during consolidation"
> --- `internal/brain/consolidate_hypothesis.go`

Theory account: localized candidate content and optional plan persist across sessions; the scan consumes the candidate's text and can retain criticism as rejection reason. The implementation requests content-directed evidence judgments, but whether a candidate is an explanatory theory and whether a returned criticism places blame adequately remain content-dependent and unobserved. No system-wide theory-builder claim follows from table names.

- theory-builder conditions 1–4: 1 — afforded, caller can state one whole localized theory, but actual theory content is uninspected; 2 — wired, scan decisions use retained candidate text; 3 — claimed, prompt requests contradiction and rejection can retain reasoning, but formulated blame/revision quality is uninspected; 4 — wired, confidence/testing state shapes later scans, while rejected reasons are not read by the automatic selector.
- Addressability: Whole content/plan are addressable through ID-based caller edits; individually addressable assumptions are not established by this schema.
- Persistence: Cross-session PostgreSQL retention; later scan/list/fact consumer depends on disposition.
- learning: Improved future capacity is uninspected; revision, retention and promotion alone do not establish it.

#### MEM-RTE-fact-withdrawal
Label: Local withdrawal and non-propagating validity

Caller semantic forget selects and soft-deletes one episode; purge deletes by ID. Code does not recompute or withdraw derived facts on soft deletion. Fact expiry and auto-supersession set valid_until, not deleted_at. Recall, QueryFacts and FetchFacts ignore validity, so retired content can still reach an agent and downstream models. Explicit contradiction resolution changes only the conflict row. PurgeFact is an internal API with an adapter but no frozen CLI registration; hard-delete FK cascades differ from these metadata updates. Caller proposes manual withdrawal/resolution; code selects/adopts it. Decay is deterministic software; model replacement classification ≥0.9 triggers supersession without human approval. No truth oracle; mode is open correction/maintenance. Guidance classifies replacement versus conflict versus compatibility, but returned explanation is omitted from conflict storage. Errors leave partial changes; purge has no automatic undo. Closest supplied [RT-RTE-remember-write](runtime.md#rt-rte-remember-write) mentions controls; this distinct route establishes their downstream limits and overlaps the decay/contradiction part of [RT-RTE-consolidation-run](runtime.md#rt-rte-consolidation-run). [SRC-1: `internal/brain/episode.go`, `internal/brain/fact.go`, `internal/brain/contradiction.go`, `internal/brain/decay.go`, `internal/queries/recall.sql.tmpl`, `internal/queries/consolidate.sql.tmpl`, `cmd/cli/main.go`]

- Immediate return: Acknowledgement, error, or decay/contradiction counters.
- Later read-back: Deleted episodes leave recall/consolidation; validity-retired facts remain eligible there; resolved conflicts leave unresolved listing.
- Delegated visibility: API/tool caller receives status; later readers may receive retired fact text without validity metadata through recall.
- Selection predicate: Query-vector nearest episode versus explicit IDs; decay uses namespace/age/confidence; contradiction matching uses entity/property and differing values.
- Invalidation or expiry: Only selectors actually checking deletion/validity enact withdrawal; derived content/cache are not comprehensively erased.
- Activation or effect: Metadata/row changes are wired, but general obsolete-knowledge exclusion is not guaranteed.
- Evidence limits: No run of deletion/expiry or full schema recovery audit; cache and derived text retention prevent an erasure guarantee.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> `UPDATE facts SET valid_until = now(), updated_at = now()
> WHERE namespace_id = $1 AND deleted_at IS NULL AND valid_until IS NULL
> AND confidence < $2`,
> --- `internal/brain/decay.go`

#### MEM-RTE-typed-read
Label: Typed requested memory delivery

Caller → MCP/CLI handler → Brain query/list/traversal → PostgreSQL rows → serialized tool text or CLI output. Code selects; caller supplies scope, page, optional status/parent/goal or causal anchor/direction/depth. Distinct from [RT-RTE-recall-read](runtime.md#rt-rte-recall-read): these queries do not use a query embedding or facts-first slot allocation. Facts/relationships/contradictions/causal/hypothesis/goal/failure and namespace reads have shipped callers. ID show getters exist for hypotheses/goals/failures; bare GetFact/GetEpisode and QueryPatterns alone are capabilities without a found shipped caller. Persistence resides in source rows, not the transient serialized result. External client/model is the later consumer, with knowledge/advice rather than code-enforced instruction force. [SRC-1: `cmd/cli/main.go`, `cmd/cli/mcp.go`, `internal/brain/fact.go`, `internal/brain/contradiction.go`, `internal/brain/causal.go`, `internal/brain/hypothesis.go`, `internal/brain/goal.go`, `internal/brain/failure.go`, `internal/brain/namespace.go`]

- Immediate return: Typed rows or edge chains, not generated answers.
- Later read-back: Use-accumulated retained fields delivered on a later requested invocation.
- Delegated visibility: MCP JSON as text to the invoking client; any later delegation is uninspected.
- Selection predicate: Namespace descendants plus type-specific filters/order/pagination; unresolved-only conflicts; causal IDs/depth for traversal. ListGoals without status/parent returns root goals.
- Invalidation or expiry: Lists exclude soft deletion; facts omit validity filtering; ID getters can expose rows not filtered by deletion.
- Activation or effect: Requested delivery wired; interpretation, obedience and answer benefit unobserved.
- Evidence limits: Row/depth controls do not establish model token-budget control; no deployed use trace. Storage-only alternatives do not imply actual read-back.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> facts, err := bc.Brain.QueryFacts(ctx, namespaces, nil, nil, page)
> --- `cmd/cli/mcp.go`

### Claims

#### MEM-CLM-verified-facts
Label: Verified consolidated truths

The shipped protocol calls query_facts “Verified facts” and facts “consolidated truths.” These are doctrine claims, not an independent verifier result. Alternative fact admissions and validity-insensitive read-back make the implied guarantee too strong. Closest supplied [RT-CLM-session-protocol](runtime.md#rt-clm-session-protocol) concerns required session order, not this truth label. [SRC-1: `cmd/cli/mcp_prompts.tmpl`, `internal/brain/consolidate_failure.go`, `internal/brain/hypothesis.go`, `internal/queries/recall.sql.tmpl`]

> - Verified facts (requires consolidation) → query_facts
> --- `cmd/cli/mcp_prompts.tmpl`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-maintenance-input
Label: Retained content authority at maintenance

Consumer: reasoner model methods. Channel: constructed user-message display lines containing episode/fact text, edge fields, candidate goal/hypothesis text or failure reason/lesson. Force: natural-language evidence under static extraction guidance; code subsequently validates/adopts selected responses. Horizon: recurring maintenance and later sessions. Metadata reaches each consumer only when formatter includes it; plans, provenance and previous notes are not automatically present. Distinct from [RT-BAP-extraction-policy](runtime.md#rt-bap-extraction-policy), which owns static instruction authority rather than accumulated input evidence. [SRC-1: `internal/reasoner/openai.go`, `internal/brain/consolidate.go`]

> failureLines = append(failureLines, fmt.Sprintf("[Failure %d] What: %s | Why: %s | Lesson: %s", f.ID, f.Content, f.Reason, f.Lesson))
> --- `internal/reasoner/openai.go`

#### MEM-BAP-retained-advice
Label: Retained knowledge and standing advice to client

Consumer: external MCP client/agent. Channel: requested recall or typed tool text, potentially carrying user preferences, standing instructions, failure lessons or self-description. Force: interpreted content/advice, not Stash-enforced host instruction precedence. Horizon: requested later sessions; activation unobserved. The static protocol affords recall of /self but does not prove self-improvement of Stash or the external agent. Distinct from [RT-BAP-agent-protocol](runtime.md#rt-bap-agent-protocol), which is the static server-description path. [SRC-1: `cmd/cli/mcp_prompts.tmpl`, `cmd/cli/mcp.go`, `internal/brain/recall.go`]

> Self-knowledge is not special infrastructure. It's just you using Stash on yourself. The same tools, the same rules.
> --- `cmd/cli/mcp_prompts.tmpl`

## Annotations

#### On [RT-RTE-remember-write](runtime.md#rt-rte-remember-write)

Retained parts are [MEM-OBJ-episode](#mem-obj-episode) and [MEM-OBJ-memory-vectors](#mem-obj-memory-vectors). Caller author identity/control remains unresolved; software performs embedding/admission, separate from authorship. Plain storage is not automatic trace-derived learning. Physical persistence and later maintenance/retrieval consumers are wired; original input may itself be an already-derived summary. [SRC-1: `internal/brain/episode.go`, `cmd/cli/mcp_prompts.tmpl`]

#### On [RT-RTE-recall-read](runtime.md#rt-rte-recall-read)

Selector inputs are requested query vector and namespace subtree, with default 10/cap 100 rows and no token-length budget in the inspected route. Fact-first allocation can exclude a more relevant episode before final sorting. The displayed fact result includes text/confidence/score/type/IDs/created time but not source links, entity/property/value, validity or embedding-model identity; `ValidFrom` is declared on result but not populated for facts. Thus recall does not deliver the retirement or derivation context needed to interpret all beliefs. No unsolicited push, host trimming or stack-frame isolation is performed by this request path. [SRC-1: `internal/brain/recall.go`, `internal/queries/recall.sql.tmpl`]

> // Search facts first (higher quality, consolidated)
> factLimit := limit
> --- `internal/brain/recall.go`

#### On [RT-RTE-consolidation-run](runtime.md#rt-rte-consolidation-run)

Raw → derived → later-consumer chain: caller episode texts → fact summary/structure/vector plus attempted source associations → later recall and maintenance models. Alternative fact checkpoints include confirmed hypotheses and failure-pattern facts, not only clustered-event summaries. Model-call inputs are batch-selected external memory, not a compaction of the external agent's accumulated window. Episode raw text remains reachable in storage; no verbatim tail, message removal policy or host-summary checkpoint is established. Source provenance writes and contradiction errors can be ignored; factExistsByVector treats query errors as “not duplicate.” Partial writes and cursor differences qualify replay guarantees. See the declared maintenance subroutes for independent budgets, reasons and consumers. [SRC-1: `internal/brain/consolidate.go`, `internal/brain/hypothesis.go`, `internal/brain/consolidate_failure.go`]

#### On [RT-RTE-context-handoff](runtime.md#rt-rte-context-handoff)

Payload is [MEM-OBJ-context](#mem-obj-context), retained caller-authored focus, not a server-generated session compaction. Exact namespace selects one row; get delivers focus plus metadata. Replacement removes the previous stored focus, not any messages in the external model window. The heap analogy is limited: reloading obtains material by value via a tool, not a dereferenceable in-window pointer with liveness tracking. External caller owns whether to drop its window/history and later ask for focus. TTL limit in runtime is confirmed by direct getter inspection. [SRC-1: `internal/brain/context.go`, `cmd/cli/mcp.go`]

## Write side

Caller-controlled content admission includes remember, focus, namespace metadata, uncertain hypotheses/plans, goals/notes, failure explanations and asserted causal links. Admission is not necessarily human-controlled: the MCP caller can be an agent and source authorship is not stored. Software validation/SQL performs physical writes; model judgments are not involved in ordinary remember or these initial object writes. The shipped protocol requests high-signal storage but does not implement that semantic gate. See [RT-RTE-remember-write](runtime.md#rt-rte-remember-write), [MEM-RTE-goal-maintenance](#mem-rte-goal-maintenance), [MEM-RTE-hypothesis-maintenance](#mem-rte-hypothesis-maintenance), [MEM-RTE-failure-derivation](#mem-rte-failure-derivation).

Automatic transformations cover synthesis, extracted edges, abstractions, goal annotations, failure recurrence/patterns, hypothesis dispositions and confidence decay. Starting consolidation is not approval of each admitted result. Code can reject malformed/invalid output and API/DB failures; semantic truth remains a model-guidance claim. Retained reasons differ: goals keep notes for client readers; failure inputs keep explanations and repeat episodes keep evidence; hypothesis rejection keeps reasoning but support/weakening drops it; fact/edge/pattern admission generally retains statements/source IDs rather than model rationale. No model-weight update is performed by inspected adapters. [SRC-1: `internal/reasoner/openai.go`, `internal/brain/consolidate.go`, `internal/brain/consolidate_goal.go`, `internal/brain/consolidate_failure.go`, `internal/brain/consolidate_hypothesis.go`]

Maintenance is not simply “compaction”: it keeps raw episodes and admits additional rows. Row checkpoints can consume empty/deduplicated or insufficient batches without producing derived content. Relationship, pattern and episode checkpoint policies differ from goal/failure/hypothesis post-loop advancement. These details affect what a later round can reconsider, independently of whether the model output was correct. Withdrawal and local recovery are recorded in [MEM-RTE-fact-withdrawal](#mem-rte-fact-withdrawal); no complete derivative erasure or pipeline rollback is established.

## Read-back

The ordinary client selects through semantic recall; typed queries broaden accessible retained parts. Namespace lists expose descriptive routing metadata, not actual recall contents. Exact get_context reloads singular focus. Automatic maintenance separately selects database batches as model input: episode batch configuration, 50 relationship facts, 30 causal facts, 30 goal/hypothesis facts, 50 failures with 30 episodes, and 30 facts/50 relationships for patterns. These are row-count limits; prompt formatting joins the selected text without an inspected token-truncation policy. Fresh model contexts keep the enclosing client's history out because Stash supplies its own messages, but no supplied client transcript proves what escaped or was removed from that client's window. [SRC-1: `internal/brain/consolidate.go`, `internal/brain/consolidate_goal.go`, `internal/brain/consolidate_failure.go`, `internal/brain/consolidate_hypothesis.go`, `internal/reasoner/openai.go`]

The cache is an independent later numerical consumer route: Embed reads a hash/model-keyed vector and avoids provider work. Checkpoints likewise return operational selectors on a later consolidation invocation. Neither is client knowledge read-back. Pattern rows, GetFact and GetEpisode remain storage capabilities without a found concrete shipped consumer; no hypothetical caller is substituted for deployed wiring. The session protocol supplies an afforded external consumer role for /self advice, but adherence and behavior change remain unobserved. See [MEM-BAP-retained-advice](#mem-bap-retained-advice).

## Integration issues

- **Qualification of fact admission:** [RT-RTE-consolidation-run](runtime.md#rt-rte-consolidation-run) correctly scopes its detailed witness to stage one. Do not generalize that witness to every fact: [MEM-RTE-failure-derivation](#mem-rte-failure-derivation) and [MEM-RTE-hypothesis-maintenance](#mem-rte-hypothesis-maintenance) bypass its extraction/provenance checks. Consequence: labels `fact` or “verified” do not establish common warrant.
- **Validity versus withdrawal:** Runtime states recall omits validity filtering; [MEM-RTE-fact-withdrawal](#mem-rte-fact-withdrawal) extends this to expiry, supersession and later maintenance. The decay source comment says soft-delete, but code sets valid_until. Consequence: obsolete facts can remain context and derivation inputs; counters do not prove withdrawal.
- **Shared causal cursor:** [MEM-RTE-edge-extraction](#mem-rte-edge-extraction) shows relationship extraction advancing LastFactID before causal selection uses it. The runtime's ordered-stage account remains true, but does not establish causal processing of the same facts. Deployed causal coverage is unobserved; direct detection/assertion remains available.
- **CLI versus capability:** PurgeFact has a CLI adapter but no command registration in frozen `cmd/cli/main.go`; QueryPatterns has no found shipped Go caller. [MEM-RTE-fact-withdrawal](#mem-rte-fact-withdrawal), [MEM-OBJ-pattern](#mem-obj-pattern) distinguish these capabilities from wired client routes. No correction to a specific runtime claim of CLI fact purge is required because it did not name that route.
- **Refinement defect:** [MEM-RTE-hypothesis-maintenance](#mem-rte-hypothesis-maintenance) finds `time.Now().UTC` passed as an SQL argument, not `UTC()`. Runtime's mention of explicit refinement establishes registration, not successful revision. No target run was authorized; actual error manifestation is unobserved.
- **Rationale and source completeness:** [MEM-OBJ-fact](#mem-obj-fact), [MEM-OBJ-pattern](#mem-obj-pattern), [MEM-OBJ-hypothesis](#mem-obj-hypothesis), [MEM-OBJ-contradiction](#mem-obj-contradiction) distinguish stored associations from reasons and received fields. Pattern fallback can broaden source arrays; supporting hypothesis reasoning is dropped; contradiction explanation is dropped. These prevent uniform retained-rationale or complete-provenance claims.
- **Unresolved external operation:** Human authorship/approval, external agent activation, actual theory content, useful self-advice, and beneficial learning remain unresolved for [MEM-BAP-retained-advice](#mem-bap-retained-advice), [MEM-RTE-hypothesis-maintenance](#mem-rte-hypothesis-maintenance). No execution evidence supplies them; provider/deployment access limits prevent stronger conclusions.
- **Identity review:** New objects have no supplied object counterparts after comparison; context payload and maintenance-only subroutes are material parts/outputs of supplied routes, not replacement referents. No possible duplicate requiring supersession was identified. The two BAPs distinguish retained-content authority from runtime's static-policy BAPs. The false containment relation on [MEM-RTE-edge-extraction](#mem-rte-edge-extraction) has been removed: its automatic subroute overlaps [RT-RTE-consolidation-run](runtime.md#rt-rte-consolidation-run), but its direct detector and caller assertion admissions extend beyond that invocation. SRC-1 `internal/brain/consolidate.go` calls the detector during maintenance; `internal/brain/causal.go` exposes the detector and separate assertion insertion; `cmd/cli/mcp.go` calls assertion directly. The existing ID and all supported mechanisms remain. Relation consumers must not attribute the combined admission mechanism to consolidation. Other spanning caller/automatic routes likewise name overlap rather than asserting containment in exactly one route.

## Limitations and checks

HEAD was rechecked as d34ed430c4348ef741ef95146b488aea8616f4fb and source status reported no changes. The correction rechecked SRC-1 `internal/brain/consolidate.go`'s causal stage, `internal/brain/causal.go`'s detector/assertion implementations, and `cmd/cli/mcp.go`'s direct assertion handler against the refusal. Unrelated findings and carried limits remain from the supplied previous report. Method identity is the supplied invocation, memory member type, worker rules and record contract read for this attempt; no engine-owned metadata was inspected or changed. Source conclusions remain implementation/doctrine findings, not operation or causal benefit. No target tests, commands, providers or services were executed.

Coverage is not a full correctness/security audit. Schema constraints/FKs were searched rather than fully read; individual secondary CLI adapters and remaining tool-description text are not exhaustively audited. These limits prevent comprehensive rollback, erasure, access-control or semantic-quality guarantees, not the positively traced memory mechanisms. Provider weights/deployed model identities, client context policy and actual content-specific theory-builder behavior remain uninspected.

Deterministic validation: passed using this invocation's validate-output command. The correction removes a false containment relation without withdrawing either automatic or caller admission; no source finding was narrowed to satisfy quotation checking. Form/quotation validation does not establish semantic correctness, complete operation or acceptance by reconciliation.
