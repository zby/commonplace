---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "llm-wiki memory: compiled text, operational checkpoints, feedback promotion and bounded later consumption."
run-id: AAS-2026-10-17-llm-wiki-a93f86f698d7-01
source-identity: https://github.com/nvk/llm-wiki
reviewed-boundary: "95a042c68998559305bc69ac8c482c4e1a415ad3"
---

# llm-wiki memory report

## Boundary and evidence

The memory boundary is the whole shipped knowledge system in [boundary](boundary.md), not only its Python helper. It includes source acquisition, synthesized articles, tracking and external-data interfaces, session and research recovery, feedback and lesson extraction, maintenance findings, topic guidance, specialist methods, checkpoints, and evaluation consumers. External host inference, host transcript compaction, provider parameters, private adapters and actual user stores remain outside inspected implementation. Their interfaces are included; their contents and deployed behavior are not established.

All source evidence is SRC-1 at the reviewed commit. Direct reads added here cover `scripts/llm-wiki-session` normalization, redaction, state, feedback, digest, hook, selection, promotion and dispatch; `scripts/llm-wiki` archive, literal retraction and main dispatch; Codex hook declarations; the full skill's principles/workflows/session management; compilation, indexing, sessions, feedback, ideas, audit, librarian and checkpoint references; inventory and dataset boundary/list sections; project rationale sections; and query, refresh, retract and lessons-learned commands. These are implementation or doctrine/design, not observed operation. Supplied runtime findings are used separately for adapters, specialist validation, lint internals, Pi launchers and benchmark delivery. No target code, tests, examples or providers were executed.

### Coverage inventory

Rows distinguish direct inspection (D), supplied runtime findings (R), and included detail not inspected (U). A limitation in a row prevents the named conclusion, not the supported mechanism beside it.

| Entry point or operation | Source paths and inspection | Records / limits |
|---|---|---|
| Single-source and collection ingestion, compilation, conversation authorship | D: `claude-plugin/skills/wiki-manager/references/ingestion.md` opening/collection formats; `claude-plugin/skills/wiki-manager/references/compilation.md`; R: ingest/compile commands | [MEM-RTE-admit-sources](#mem-rte-admit-sources), [RT-RTE-compile-wiki](runtime.md#rt-rte-compile-wiki). U: individual collection adapters and extraction fallback bodies; cannot certify each fetch/dedup implementation. |
| Standard, quick, deep, resume and ambient query; compact Pi/DS4 | D: `claude-plugin/commands/query.md`, `profiles/query-lite/SKILL.md`, full-skill ambient/query sections; R: launcher/extension implementation | [MEM-OBJ-index](#mem-obj-index), [RT-RTE-query-wiki](runtime.md#rt-rte-query-wiki). Policy conflict about query index repair retained below. |
| Hook capture, manual capture/show/rehydrate/promote; pre/post compaction | D: `scripts/llm-wiki-session`, `plugins/llm-wiki/hooks/hooks.json`, sessions reference | [MEM-OBJ-session-state](#mem-obj-session-state), [MEM-OBJ-session-digest](#mem-obj-session-digest), [RT-RTE-session-bridge](runtime.md#rt-rte-session-bridge). External compactor output and retained host tail are opaque. |
| Automatic and manual feedback, list/show and promotion | D: `scripts/llm-wiki-session`, feedback reference | [MEM-RTE-feedback-candidates](#mem-rte-feedback-candidates). Feedback preview, digest display and promotion are different deliveries. |
| Lessons learned and proposed instruction edits | D: `claude-plugin/commands/ll.md` | [MEM-RTE-extract-lessons](#mem-rte-extract-lessons); not equivalent to automatic feedback classification. |
| Parallel research, crash registry, durable provenance, resume | D: full-skill session management, query resume; R: research worker protocol | [RT-RTE-research-paths](runtime.md#rt-rte-research-paths), [MEM-OBJ-session-provenance](#mem-obj-session-provenance). U: every thesis/research round body; no complete replay guarantee. |
| Lint fixes and coverage backlog; librarian, audit, refresh | D: librarian/audit references and refresh command; R: executable lint dispatch | [MEM-RTE-review-memory](#mem-rte-review-memory), [MEM-RTE-refresh-sources](#mem-rte-refresh-sources), [RT-RTE-lint-wiki](runtime.md#rt-rte-lint-wiki). U: each lint fix branch; cannot certify all rewrite semantics. |
| Archive/restore; literal and source-path withdrawal | D: `scripts/llm-wiki` archive/retract functions and `claude-plugin/commands/retract.md` | [MEM-RTE-withdraw-memory](#mem-rte-withdraw-memory); archive policy explained in Write side. History and arbitrary external copies are not erased. |
| Inventory, Ideas, dataset registry, Projects, collect outputs and media | D: inventory/datasets boundary/list sections, ideas reference, project rationale; full-skill collect | [MEM-OBJ-inventory](#mem-obj-inventory), [MEM-OBJ-datasets](#mem-obj-datasets), [MEM-OBJ-projects](#mem-obj-projects). U: migrations, native dataset query/sample/profile bodies, media download internals and portfolio body. No complete transformation/privacy or native-data consumer guarantee for those branches. |
| Topic-guide proposals/adoption and personal specialists | D: compilation/librarian rules; R: CLI schema and specialist controls | [MEM-OBJ-schema](#mem-obj-schema), [RT-RTE-specialist-enable](runtime.md#rt-rte-specialist-enable). Personal package contents absent; effectiveness not established. |
| Private adapter outputs/receipts and wiki-safe promotion | R: execution/registry records; D: full-skill boundary | [RT-RTE-adapter-execute](runtime.md#rt-rte-adapter-execute). Private payload lineage and actual promotion review unavailable; no inference from an adapter label to knowledge admission. |
| Project checkpoint create/refresh/seal/verify/import | D: checkpoint reference; R: CLI seal/verify | [RT-RTE-checkpoint-export](runtime.md#rt-rte-checkpoint-export), annotation below. Import produces pinned raw evidence, not live project replacement. |
| Benchmark fixture reads, grading and report retention | R: benchmark implementation | [RT-RTE-query-evaluation](runtime.md#rt-rte-query-evaluation). U: all promptfoo assertion bodies, shell evaluators and metric-helper internals; no universal evaluation coverage or automatic production update conclusion. |
| Portable/Codex/OpenCode entries and generated packages | R: boundary/runtime entry inventory and helper equivalence | Same routes are exposed through differing hosts; no independently established behavioral equivalence. Package-generation transformations were not directly traced here. |

CLI/parser inspection and supplied runtime dispatch cover lint, archive, schema, retract, specialist, adapter and checkpoint operations. The session parser additionally exposes enable/disable, hook, capture, list, show, rehydrate, promote, feedback and status. No separate target service/library consumer was established by this inventory; this is not an absence claim about every function. Static packaged instructions are context controls, not themselves memory accumulated through use.

## Core ideas

1. **Retained evidence and retained guidance have different authority.** Raw/article bodies supply interpreted knowledge. A topic guide or selected specialist supplies operating instructions. Inventory supplies tracking state, not factual evidence. Query-lite explicitly requests that retained source/article instructions be ignored. Delivery to a model does not prove obedience ([MEM-OBJ-raw](#mem-obj-raw), [MEM-OBJ-schema](#mem-obj-schema), [RT-OBJ-query-profile](runtime.md#rt-obj-query-profile)).
2. **Indexes trade body reads for lossy metadata reads.** Titles, summaries, tags and dates lead to selected files. Quick mode intentionally stops at summaries; standard mode requests exact files. Count agreement cannot detect a same-count edit or stale summary, so the indexing reference's accuracy/concurrency claims exceed that detector alone ([MEM-OBJ-index](#mem-obj-index)).
3. **Operational capture is not semantic transcript compression.** Code selects small event metadata, bounded manual summaries and templated feedback. It renders a digest, then injects only a state-derived summary and digest pointer. Host compaction remains external. Explicit promotion changes the admission plane from operational material to topic raw evidence ([MEM-OBJ-session-digest](#mem-obj-session-digest), [RT-RTE-session-bridge](runtime.md#rt-rte-session-bridge)).
4. **Criticism can persist without silently rewriting knowledge.** Librarian/audit retain findings and proposed actions; refresh and topic-guide adoption introduce separate acceptance steps. In contrast, ordinary compilation and lessons-learned article appends do not require per-content approval. Source immutability is contradicted by refresh's authorized overwrite instruction, not merely by privacy retraction ([MEM-RTE-review-memory](#mem-rte-review-memory), [MEM-RTE-refresh-sources](#mem-rte-refresh-sources)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-raw
Label: Raw source bodies

Source-native identity: topic `raw/{articles,papers,repos,notes,data}/*.md` bodies. Natural-language source/extracted text on the local filesystem; small data can retain structured content whose native reader is not established here. Collection manifests and child provenance distinguish upstream revision/hash from model-produced summaries. External sources and user/session notes have different origins; a source URL alone does not establish trust. Compilation and targeted primary-evidence queries interpret the bodies. This is a distinct retained input object to [RT-RTE-compile-wiki](runtime.md#rt-rte-compile-wiki), not a duplicate route. SRC-1, `claude-plugin/skills/wiki-manager/references/ingestion.md`, `claude-plugin/skills/wiki-manager/references/compilation.md`.

> If the exact
> same upstream item was already ingested, skip it. If the item changed upstream,
> write a new raw source; never overwrite the old one.
> --- `claude-plugin/skills/wiki-manager/references/ingestion.md`

That collection rule conflicts with refresh's overwrite rule; neither establishes filesystem immutability. Original upstream payloads and original conversation turns are not necessarily preserved by the normalized raw note.

#### MEM-OBJ-wiki
Label: Synthesized wiki article bodies

Source-native identity: `wiki/{concepts,topics,references}/*.md` bodies. Natural-language synthesis and readable links on disk, produced/edited by the foreground model from retained evidence or explicitly marked conversation authorship. Consumers are later query, compile, output, librarian/audit and checkpoint synthesis. Their knowledge authority is interpretive, not a fixed rule engine. Distinct output object of [RT-RTE-compile-wiki](runtime.md#rt-rte-compile-wiki); no supplied object counterpart. SRC-1, `claude-plugin/skills/wiki-manager/references/compilation.md`.

> - **Self-contained**: Articles are readable without consulting raw sources
> - **Synthesized**: Draw from multiple sources when possible, not just one
> --- `claude-plugin/skills/wiki-manager/references/compilation.md`

Source links retain evidence lineage, but synthesis does not require a full derivation history. The conversation exception prevents assuming every article can be reconstructed from raw files, qualifying [RT-CLM-concurrent-writes](runtime.md#rt-clm-concurrent-writes).

#### MEM-OBJ-frontmatter
Label: Document access and provenance fields

Source-native identity: YAML fields alongside raw/article bodies, including `sources`, `source`, `ingested`, `updated`, `verified`, `confidence`, `volatility`, tags and aliases. Symbolic path/date/enum fields feed fixed lint and navigation checks; readable summaries and confidence judgments are model-authored interpretations, not machine-certified truth. Storage: Markdown frontmatter. Consumers differ: incremental compile selects dates; lint resolves paths; freshness rules score dates/source presence; model query uses tags/confidence as selection/evidence cues. These are distinct metadata parts, not the article's substantive assertions. Closest supplied record: [RT-RTE-lint-wiki](runtime.md#rt-rte-lint-wiki), a consuming route. SRC-1, compilation and librarian references.

> - **Incremental** (default): Only process sources ingested since the last compilation date (from master `_index.md`). Compare source `ingested` dates against `Last compiled` in master index.
> --- `claude-plugin/skills/wiki-manager/references/compilation.md`

The compilation protocol sets `verified` to today while librarian calls that field last human confirmation. This weakens any inference that its date proves human verification.

#### MEM-OBJ-index
Label: Derived navigation indexes

Source-native identity: `_index.md` tables and master statistics; filesystem Markdown. Readable summaries are natural-language lossy views; exact links/counts/dates supply symbolic access metadata. Files/frontmatter are the upstream authority. Model rebuilding and CLI lint repair differ in implementation, but both feed subsequent index-first consumers. Distinct object shared by [RT-RTE-query-wiki](runtime.md#rt-rte-query-wiki) and [RT-RTE-lint-wiki](runtime.md#rt-rte-lint-wiki). SRC-1, `claude-plugin/skills/wiki-manager/references/indexing.md` and `claude-plugin/commands/query.md`.

> 1. Count `.md` files in the directory (excluding `_index.md`)
> 2. Count rows in the `_index.md` contents table
> 3. If counts differ → index is stale → rebuild inline before proceeding
> --- `claude-plugin/skills/wiki-manager/references/indexing.md`

Equal counts do not establish that titles, links or summaries reflect changed content. Query-lite verifies exact files without repairing; quick query uses index summaries only. No measured context saving is established by the reference's typical 3–8 article estimate.

#### MEM-OBJ-session-state
Label: Session state and redacted event records

Part of: [RT-RTE-session-bridge](runtime.md#rt-rte-session-bridge)

This object is retained data within the enclosing route. Source-native identity: `.sessions/queue/YYYY-MM-DD.jsonl`, `.sessions/state/<harness>/<id>.json`, lifecycle `registry.jsonl` and derived JSON indexes. Filesystem JSON/JSONL symbolic counters, identities, paths and event metadata feed code selection/rendering. Manual summaries and feedback lesson strings embedded in state are natural-language parts consumed through digest/summary rendering, not fixed-code semantic rules. Lineage: host hook JSON or explicit manual capture, redacted and truncated by code; not an original transcript archive. `transcript_path_hash` hashes the path string, not transcript contents. State retains the last 20 event descriptors and last ten manual summaries. Selector sorts states by `last_seen_at`; indexes are not the source of selection in `build_rehydrate_context`. SRC-1, `scripts/llm-wiki-session`.

>     state["last_events"] = last_events[-MAX_LAST_EVENTS:]
> --- `scripts/llm-wiki-session`

Redaction replaces content-key values with omission markers carrying length/hash, limits lists to 20 entries and caps ordinary previews at 1,200 characters. The raw input can be inspected transiently for feedback before this lossy record is written. Metadata omission is not proof of semantic confidentiality; manual summaries take another path.

#### MEM-OBJ-session-digest
Label: Session digest Markdown

Part of: [RT-RTE-session-bridge](runtime.md#rt-rte-session-bridge)

Source-native identity: `.sessions/digests/YYYY/MM/<harness>-<id>.md`. Filesystem natural-language template with YAML identity/selection metadata. Code renders latest state: summary is latest manual summary capped at 240 characters or an automated checkpoint sentence; body includes up to five manual summaries, five feedback candidates and twelve event names/tool names. It is derived operational memory, not an LLM-generated semantic account of all work. `write_digest` writes the computed session path and updates the latest pointer; neither the counter nor repeated checkpoint trigger proves immutable snapshot history. Consumers: explicit show, optional model pointer-following, and explicit promotion, which copies the digest body into raw notes. Automatic rehydration does not deliver that body. SRC-1, `scripts/llm-wiki-session`.

> - This digest is an automated checkpoint generated from redacted hook metadata.
> - Raw transcript text is not copied by default; use the transcript pointer only if the harness still owns a readable transcript and the user approves.
> --- `scripts/llm-wiki-session`

No opaque transcript is made readable by hashing or displaying its path. PostCompact stores an event preview but the renderer does not insert an inspected host compaction summary in place of the conversation. Manual summary strings are appended directly by `update_state`; calling the whole digest redacted does not establish identical sanitation of every field.

#### MEM-OBJ-feedback
Label: Feedback candidates and promotion status

Source-native identity: `.sessions/feedback/candidates.jsonl` and `status.json`. Candidates contain a natural-language redacted preview/templated lesson and symbolic ID/type/confidence/scope/hash/rationale/recommendation; status is separate symbolic promotion metadata. Code appends the candidate, stores a shortened state display and rebuilds list indexes. Model/human review can read the full candidate; digest receives only recent abbreviated fields. Status governs unpromoted listing, not factual validity. Different referent from session digest despite display overlap; closest supplied [RT-RTE-session-bridge](runtime.md#rt-rte-session-bridge) mentions promotion but not this classification/admission route. SRC-1, `scripts/llm-wiki-session`, `claude-plugin/skills/wiki-manager/references/feedback.md`.

> - `feedback/candidates.jsonl` is append-only. Each row is a distilled candidate,
>   not a transcript.
> - `feedback/status.json` records promotions by candidate id.
> --- `claude-plugin/skills/wiki-manager/references/feedback.md`

The word “distilled” here includes fixed regex classification and prefixing a preview, not demonstrated model insight or error diagnosis. The candidate retains a pattern rationale and feedback origin; it need not retain the earlier result being approved.

#### MEM-OBJ-session-provenance
Label: Research crash state and durable provenance

Source-native identities: `.research-session.json` / `.thesis-session.json` crash registries versus `.session-events.jsonl` and `.session-checkpoint.json`. Filesystem symbolic work status/event records plus readable progress summaries. These are not `.sessions/` harness state. Research creates and removes crash registries; the instructions retain event history/checkpoint for resume and audit. Their declared later consumers are query resume, research recovery and audit provenance classification. No complete actual event stream supplied. Distinct data objects from the supplied research route [RT-RTE-research-paths](runtime.md#rt-rte-research-paths). SRC-1, `claude-plugin/skills/wiki-manager/SKILL.md`, `claude-plugin/commands/query.md`.

> The session registry files are ephemeral crash-recovery state. The event log and
> checkpoint are the durable provenance trail.
> --- `claude-plugin/skills/wiki-manager/SKILL.md`

Retained provenance does not itself update a method. Deletion on completion applies to the crash registry, not all research memory.

#### MEM-OBJ-schema
Label: Topic guide and adoption proposals

Source-native identity: topic `schema.md`, optional `.librarian/schema.json` cache and `output/schema-proposal-<topic>-<date>.md`. The guide is natural-language topic-local planning guidance on cardinality, article boundaries and scope; `schema_state` is a symbolic mode marker. All persist as local files. Proposals derive from titles/aliases/tags, links, raw types and other retained structure. Model compilation reads the guide fully before planning; advisory deviations are reported, strict deviations request confirmation. User-owned adoption separates proposal from authority. Distinct object from [RT-RTE-compile-wiki](runtime.md#rt-rte-compile-wiki); not a database schema or [RT-OBJ-query-profile](runtime.md#rt-obj-query-profile). SRC-1, compilation/librarian references.

> The scan must not create or rewrite `schema.md`; applying a proposal is a
> separate, explicit user decision.
> --- `claude-plugin/skills/wiki-manager/references/librarian.md`

Guide rules are individually inspectable/editable in sections. Formulation is afforded; intended consumption is claimed; content-directed criticism of a particular guide and iterative reuse remain uninspected. These are separate theory-builder conditions 1–4, not evidence of exercised learning.

#### MEM-OBJ-inventory
Label: Inventory and Idea records

Source-native identity: `inventory/<kind>/*.md`, including `inventory/ideas/<slug>.md`, plus derived views/indexes. Natural-language tracking reasons, seed, assumptions and decision notes coexist with symbolic status/priority/path/date fields. Storage: filesystem Markdown. Origin: user/model capture and reviewed migrations; source artifacts stay where they are. Consumers: list/query, research follow-up, portfolio and Idea-to-Project promotion. Tracking authority is not factual authority. Closest supplied compile/query routes consume or exclude it; no object counterpart. SRC-1, inventory and ideas references.

> The Idea remains catalog/lineage. The Project owns changing plans,
> implementation decisions, code, data, deliverables, and outcomes. Idea and
> Project archive are independent.
> --- `claude-plugin/skills/wiki-manager/references/ideas.md`

Single small adds with clear fields may write directly on request; larger pivots require sample/explicit apply. Idea shaping stops for explicit choice, and only approval creates its Approved Decision Snapshot. Promotion freezes that snapshot into Project `BRIEF.md`, records lineage and rejects collisions; this is model-operated doctrine, not inspected executable enforcement. Retained rejected alternatives/reasons can inform later project work, but actual use is unobserved.

#### MEM-OBJ-datasets
Label: Dataset registry and external payloads

Source-native identity: `datasets/<slug>/MANIFEST.md`, schema/sample/profile/query notes, and referenced external stores. Manifest text/recipes are natural language; locations, checksums and frontmatter fields are symbolic access metadata. Filesystem notes do not contain the large dataset itself. External bytes may be databases, binary/compressed files or APIs; their actual content, initial provenance and consumer semantics remain uninspected. Metadata cannot establish their encoding or truth. Distinct alternative to [MEM-OBJ-raw](#mem-obj-raw), not an adapter registry. SRC-1, `claude-plugin/skills/wiki-manager/references/datasets.md`.

> - Never open samples, profiles, query notes, or the underlying dataset for a
>   plain list operation.
> --- `claude-plugin/skills/wiki-manager/references/datasets.md`

The list consumer gets index/manifest frontmatter; native-data query, sample and profile transformations are included but not traced here. Their missing execution/selection detail prevents claims about exhaustive data admission or factual grounding from those paths. Migration is prescribed additive and preview-first; that does not copy the dataset into memory context.

#### MEM-OBJ-projects
Label: Outputs and Project rationale

Source-native identity: `output/*.md`, collection outputs/assets and `output/projects/<slug>/WHY.md`, approved `BRIEF.md` and colocated deliverables. Natural-language rationale and reports are distinct from arbitrary code/media/data payloads whose interpretation depends on the consuming tool. Filesystem folders determine membership; `WHY.md` is plain Markdown without required frontmatter. Collect may stage links/media before promotion; staging is not raw evidence for factual claims. Later output synthesis, portfolio, audit, Idea linkage and checkpoint selection can read retained project material. No supplied object counterpart; overlaps the retained inputs to [RT-RTE-checkpoint-export](runtime.md#rt-rte-checkpoint-export). SRC-1, projects/ideas references and full skill.

> The Project keeps delivery truth; the checkpoint is a reviewable snapshot for
> handoff/import and never becomes a second live Project state store.
> --- `claude-plugin/skills/wiki-manager/references/projects.md`

The reasons in `WHY.md` remain readable to a future model, not merely a title in a manifest. Full payload meaning and every tool-native read route are not established by folder membership.

### Routes

#### MEM-RTE-admit-sources
Label: Source admission before compilation

User or model-selected accepted material → host fetch/read/normalization → typed raw source plus provenance/indexes → later compile/query. Owner: foreground model and external host tools; no target-owned semantic extraction service inspected. Single sources and collection manifests/children share an admission plane but preserve different provenance. This is distinct upstream work, not a duplicate of [RT-RTE-compile-wiki](runtime.md#rt-rte-compile-wiki). SRC-1, ingestion reference; supplied runtime ingest account.

> Ingest
> is for accepted source material; inventory is for durable candidates and next
> actions.
> --- `claude-plugin/skills/wiki-manager/references/ingestion.md`

- protocol conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: written raw item/collection and model report/index updates.
- Later read-back: raw bodies are selected by later compile or primary-evidence query; collection revision/hash fields remain provenance.
- Delegated visibility: uninspected — individual collection adapter and fetch branches were not traced end to end; research worker visibility is in the supplied research route.
- Selection predicate: requested source or model-researched accepted source; collections dedupe upstream ID plus revision/hash, not semantic truth.
- Invalidation or expiry: collection changes request new raw versions; explicit retraction can remove/replace content; refresh has an inconsistent overwrite path.
- Activation or effect: requests host writes to raw files; later model interpretation may change knowledge, without observed behavioral activation.
- Evidence limits: instructions establish workflow, not reliable extraction, truthful metadata or exhaustive source acquisition.

Mode: open acquisition or bounded collection import; no expected-answer oracle. User initiates scope, model chooses extraction and ordinary content admission, host performs I/O. This is not per-source human approval for model-researched acquisitions. Rejection can retain a candidate in inventory rather than raw; no universal transactional rollback. Shipped format and provenance rules persist, while imported content carries its own lineage.

#### MEM-RTE-feedback-candidates
Label: Feedback classification and promotion

Hook user turn or explicit capture → deterministic regex/preview/lesson → append candidate/state display → explicit list/show/digest review → explicit promotion into topic raw note → optional compile or rule proposal. Python decides automatic candidate admission; caller selects promotion ID/topic; no interactive approval inside promotion. No closest supplied record with the same referent: [RT-RTE-session-bridge](runtime.md#rt-rte-session-bridge) covers the encompassing hook/digest and separate digest promotion, not feedback selection. SRC-1, `scripts/llm-wiki-session`, feedback reference.

>     if not force and event_name not in {"UserPromptSubmit", "ManualFeedback"}:
>         return None
> --- `scripts/llm-wiki-session`

>         - Use corrections and preferences as candidates for future `AGENTS.md`, skill, or workflow rule updates.
>         - Treat approval/decision candidates as validation of the immediate prior context unless corroborated by session digests.
> --- `scripts/llm-wiki-session`

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: hook capture/state update, candidate list/show output or promotion note path.
- Later read-back: review reads candidates; digest displays up to five recent abbreviated lessons; promotion copies selected lesson, preview and metadata into raw notes for later model use. No automatic instruction rewrite follows.
- Delegated visibility: inapplicable — this helper path is local code, not a worker context.
- Selection predicate: configured feedback enabled/minimum confidence; recognized correction, preference, approval or decision patterns; ignore generic acknowledgement unless forced; ID deduplicates session/turn/event/type/text hash. Promotion names an exact candidate.
- Invalidation or expiry: promotion status filters unpromoted views; existing same destination blocks overwrite unless force; no automatic candidate expiry or semantic correction established.
- Activation or effect: append operational memory, update cache/state, optionally write topic note and log; live rule adoption remains a separate step.
- Evidence limits: regex confidence/scope is a code label, not measured validity; original prompt/result context may be omitted; caller identity does not authenticate a human reviewer.

Mode: automatic operational capture plus explicit open promotion, not an answer-key experiment. User supplies trace text; software proposes a candidate and admits it to the operational plane. Config can reject categories/disable automatic capture; declining promotion keeps it out of topic raw. Manual capture forces classification fallback. Stored pattern rationale explains classification, not why a generalized method is sound. Raw→derived→later-consumer chain exists in code; future capacity improvement, reflection, autonomous theory building and exercised self-improvement are not thereby established.

#### MEM-RTE-extract-lessons
Label: Session lesson extraction

Current conversation → model diagnosis/extraction → structured raw lesson → optional append-only article Rule/back-reference → optional individually approved instruction proposals. This is semantic, model-operated trace transformation, distinct from [MEM-RTE-feedback-candidates](#mem-rte-feedback-candidates). Closest supplied [RT-RTE-compile-wiki](runtime.md#rt-rte-compile-wiki) has a different trigger and permits broader article edits. SRC-1, `claude-plugin/commands/ll.md`.

> 3. Use Edit to append the lesson's **Rule** as a new subsection or bullet, with a back-reference to the raw note
> 4. Do NOT rewrite existing content — only append
> --- `claude-plugin/commands/ll.md`

> Do NOT auto-edit CLAUDE.md/AGENTS.md. Present the proposals and let the user approve each one.
> --- `claude-plugin/commands/ll.md`

- protocol conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: raw note/report, article appends where relevant, or dry-run preview.
- Later read-back: later compile integrates unmatched raw lessons; query can interpret appended Rules and follow the raw-note back-reference to reasons. Approved rule adoption would use a host instruction-loading path, not established merely by the suggestion.
- Delegated visibility: inapplicable — extraction is foreground conversation work.
- Selection predicate: error/fix, user correction, discovery, configuration change and gotcha; model deduplicates/generalizes, targets wiki by request/topic and finds related articles.
- Invalidation or expiry: no automatic expiry; dry-run withholds writes until acceptance; later ordinary edit/recompile or retraction may revise retained material.
- Activation or effect: model-requested raw/article writes; --rules produces proposals, not automatic instruction installation.
- Evidence limits: current conversation may already be host-compacted; source says learned-by-doing but supplies no actual diagnosis/revision trace or outcome comparison.

Admission differs within this route: ordinary raw notes and article appends are model-selected without per-lesson user approval; dry-run requires save confirmation; instruction edits require individual approval. No expected-answer oracle. Recovery is withholding writes or later manual editing/retraction, not an atomic rollback. The raw lesson retains context, symptom, root cause, fix and general Rule; the article receives Rule plus pointer rather than all reasons.

For formulated lesson Rules, theory-builder conditions 1–4: 1 afforded by a whole localized Rule; 2 claimed through later article/rule use; 3 claimed as the prescribed error-assumption-root-cause-fix extraction but uninspected for an actual case; 4 uninspected without retained criticism-to-next-round operation. Addressability is field/section-level; persistence can cross sessions through raw/articles. Learning needs improved future capacity evidence; reflection needs the represented aspect and both causal directions; neither follows from the command name. Autonomous theory building and exercised self-improvement are not established by this instruction-only path.

#### MEM-RTE-review-memory
Label: Memory health review and retained findings

Explicit librarian/audit request → metadata scoring and selected deep reads/research → checkpoint/results/reports/provenance → later resume, audit reuse and proposed corrective actions. Foreground model owns semantic judgments; prescribed formulas/thresholds constrain scoring. Distinct from executable [RT-RTE-lint-wiki](runtime.md#rt-rte-lint-wiki), whose structural repairs do not establish semantic truth. SRC-1, librarian/audit references.

> 5. **Machine-readable first.** `.librarian/scan-results.json` is the source of truth. `REPORT.md` is rendered from it. Other skills read the JSON.
> --- `claude-plugin/skills/wiki-manager/references/librarian.md`

> 3. **Read-only on knowledge artifacts.** Audit writes reports under `.audit/`
>    and may reuse `.librarian/`, but it does not rewrite wiki or output content
>    during a scan.
> --- `claude-plugin/skills/wiki-manager/references/audit.md`

- protocol conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: findings, rankings, trust verdicts and recommended actions; `.librarian/scan-results.json` / `REPORT.md`, `.audit/scan-results.json` / `REPORT.md` and logs persist.
- Later read-back: resumed librarian skips completed articles using `.librarian/checkpoint.json`; audit may reuse fresh librarian JSON; later audit/resume reads durable provenance; accepted proposals can change guides separately.
- Delegated visibility: audit affords support/attack/primary-source workers if host permits; actual packet/return constraints beyond supplied research route remain uninspected.
- Selection predicate: article/scope/pass request; cheap metadata first, escalate hot/stale/thin articles; audit follows output sources and fresh corroborating/adversarial evidence when trust is uncertain.
- Invalidation or expiry: successful scan deletes its in-progress checkpoint after writing results; --fresh bypasses reuse; precise fresh-cache expiry is not established here.
- Activation or effect: reports change available maintenance evidence; knowledge edits require separate confirmed fix/refresh; no silent schema rewrite in scan.
- Evidence limits: prose/formula protocols are not executable scoring guarantees; partial provenance can be reported without rejecting content; report retention alone does not establish later action.

Mode: open maintenance or bounded artifact audit; metadata formulas and quality rubrics are reference criteria, not a general factual oracle. Model proposes findings; user can reject repairs/adoption. Checkpoint resume supports interruption recovery, not rollback of admitted knowledge. Scores/verdicts are symbolic JSON; explanatory factors/investigations and reports retain natural-language reasons. Actual report contents are not supplied, so content-directed criticism and iterative theory revision cannot be claimed from the verdict vocabulary alone.

#### MEM-RTE-refresh-sources
Label: Human-selected source refresh

User selects due/specific article → model re-fetches raw source URL → key-fact comparison and impact report → user skip/update/flag/retract choice → modified source/article state → later queries and freshness checks. Distinct maintenance route from [RT-RTE-compile-wiki](runtime.md#rt-rte-compile-wiki), reused for approved recompilation. SRC-1, `claude-plugin/commands/refresh.md`.

> - **update**: Re-ingest the changed source (overwrite the raw file with new content, preserve frontmatter), then recompile the article following the standard compilation protocol.
> --- `claude-plugin/commands/refresh.md`

- protocol conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: source unchanged/updated/contradicted/unreachable assessment and selected action report/log.
- Later read-back: changed raw/article bodies, reduced confidence/warning or new verified date affect subsequent compile/query/librarian consumers.
- Delegated visibility: uninspected — command declares Agent but inspected protocol does not specify a concrete delegated evidence packet.
- Selection predicate: specific article or volatility/date-based due list with user selection; compare 5–10 stored key claims to fetched evidence.
- Invalidation or expiry: stale dates trigger future review; skip still updates verified; no immutable old raw snapshot is required by the update instruction.
- Activation or effect: user chooses content action; host model performs overwrite/recompile, confidence change or retraction routing.
- Evidence limits: authorized overwrite contradicts broad immutability doctrine; source changes outside selected claims may be missed; no observed human verification or successful refresh.

Mode: human-gated maintenance, no expected-answer oracle. User may skip or flag instead of update; no automatic recompilation. Existing compilation guidance shapes the revised article; overwrite can remove old evidence content while preserving frontmatter. No generic rollback is specified here. “Unreachable” routes to retraction, whose literal-data versus source-path modes must not be conflated.

#### MEM-RTE-withdraw-memory
Label: Local memory withdrawal

Explicit literal-data or named-source request → scoped mapping/dry-run → explicit apply → retained-file rewrite/deletion/reference cleanup → verification and later reads of altered material. Distinct from [RT-RTE-lint-wiki](runtime.md#rt-rte-lint-wiki); no supplied withdrawal record. Literal matching is Python; source-dependent claim deletion/resynthesis is a separate model instruction. SRC-1, `scripts/llm-wiki`, `claude-plugin/commands/retract.md`.

> 4. Delete claims supported only by that source. Rewrite a claim only when the
>    remaining sources independently support it.
> --- `claude-plugin/commands/retract.md`

>     return 2 if report["status"] == "incomplete" else 0
> --- `scripts/llm-wiki`

- implementation conclusion status: wired
- protocol conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: secret-free scan/apply report; literal apply rescans same roots and signals incomplete status nonzero.
- Later read-back: future query/compile/session reads encounter rewritten or removed retained material; source-path protocol also updates derived references/counts. External copies and version history are outside the local scan.
- Delegated visibility: inapplicable — inspected literal operation is local Python; source-path instruction assigns foreground cleanup.
- Selection predicate: hidden/stdin literal, exact/common encoded variants and explicit roots; --everywhere includes configured/registered roots, archive, sessions and present local wiki. Source mode resolves exact raw path and asks on ambiguity.
- Invalidation or expiry: withdrawal immediately changes scoped files; unresolved binary/symlink/error matches prevent a verified result; no automatic expiry policy.
- Activation or effect: --apply replaces text patterns, optionally deletes whole binary matches, renames matched paths and optionally removes matching log entries. Model source cleanup removes unsupported claims or optionally recompiles remaining evidence.
- Evidence limits: literal replacement is not semantic dependency analysis; scans skip version-control metadata and do not follow symlink targets; no provider/backup/history erasure or universal rollback.

Admission is an explicit caller mutation switch; user authority is prescribed but not authenticated in code. Mode: bounded privacy/content withdrawal, not an answer-oracle experiment. Content cannot veto requested removal. Recovery is report/rescan and further explicit remediation; partial effects can remain when verification fails. Retained generic operation log must not reproduce removed content. A source-path command and a literal CLI invocation have different semantics despite sharing “retract.”

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-topic-guide
Label: Topic guide planning authority

Consumer: foreground compilation model. Channel: topic `schema.md` read before survey/planning. Force: interpreted cardinality, article-boundary and scope rules, with advisory override reporting or strict-mode confirmation; not host permission enforcement. Horizon: current compile and later sessions reading the persisted guide. SRC-1, compilation reference; [MEM-OBJ-schema](#mem-obj-schema) retains evidence and scope. Distinct from query profile and specialist authority paths in runtime; a local guide can change without changing shipped model parameters.

## Annotations

#### On [RT-RTE-compile-wiki](runtime.md#rt-rte-compile-wiki)

Storage/form/lineage are separated in [MEM-OBJ-raw](#mem-obj-raw), [MEM-OBJ-wiki](#mem-obj-wiki), [MEM-OBJ-frontmatter](#mem-obj-frontmatter) and [MEM-OBJ-index](#mem-obj-index). Model authorship and host I/O do not imply human per-article approval. Source links preserve evidence pointers, not necessarily compilation reasoning. Conversation-authored articles are a supported alternative lineage; raw-only rebuild claims must keep that exception. SRC-1, compilation reference.

#### On [RT-RTE-session-bridge](runtime.md#rt-rte-session-bridge)

Automatic supply is a push at SessionStart/UserPromptSubmit: code selects current-cwd states with digest paths, newest `last_seen_at` first, limit three, emits a summary and path in `hookSpecificOutput.additionalContext`. Explicit rehydrate is a pull with session/topic/cwd filters and caller limit. `build_rehydrate_context` does not read the digest body. Explicit show or a later host Read can deliver the body; explicit promotion reads it and copies it into raw. SRC-1, `scripts/llm-wiki-session`.

>             f"- {state.get('llm_wiki_session_id')} — {digest_summary(state, 'rehydrate')} "
>             f"Digest: {state.get('last_digest_path')}"
> --- `scripts/llm-wiki-session`

This is a count budget, not a token budget; summaries can still expose manual text. Automatic metadata transformations persist and can reach later invocations without per-event human approval. Promotion is separately selected, not automatic canonicalization. `--if-enabled` honors opt-out; missing config defaults enabled/balanced, contradicting the full skill's “Opt in” phrasing. Manual capture/rehydrate are not disabled merely by the bundled hook's conditional check. Pre/PostCompact capture neither proves host transcript preservation nor controls removal of host turns. Digest rendering, state retention and feedback have separate loss boundaries in the object records.

#### On [RT-RTE-query-wiki](runtime.md#rt-rte-query-wiki)

Selection is model-driven pull from retained material through index → exact file → optional bounded search. Query-lite's one-topic/minimum-files policy is not a byte/token cap; quick query deliberately consumes summaries, deep query has a wider scope. The command itself is read-only even when indexing doctrine asks read operations to rebuild. SRC-1, `profiles/query-lite/SKILL.md`, `claude-plugin/commands/query.md`.

> Read `skills/wiki-manager/references/query-lite.md`, then answer `$ARGUMENTS`
> from the selected wiki. This command is always read-only: do not update indexes
> or append to `log.md`.
> --- `claude-plugin/commands/query.md`

Resume reads active session/checkpoint files, recent log tail, master statistics and three recently updated index entries. It does not bulk reload a transcript. Its briefing changes immediate context; only the pre-existing log/checkpoint is retained read-back. Ambient full-skill retrieval and explicit query command should not be treated as equivalent write policies.

#### On [RT-RTE-research-paths](runtime.md#rt-rte-research-paths)

Selected packets keep unrelated hub context and method bodies out of worker contexts; findings and unique raw artifacts escape the worker frame. Host lifetime/disposal is opaque. Retained raw files are independently readable after the frame, unlike a live reference to removed context. Ephemeral crash state plus durable event/checkpoint records have distinct retention consumers in [MEM-OBJ-session-provenance](#mem-obj-session-provenance). A later resume can reconstruct a briefing without proving the original working window is recoverable. SRC-1, full-skill Session Management; supplied research route supplies worker passage.

#### On [RT-RTE-specialist-enable](runtime.md#rt-rte-specialist-enable)

Selected method Markdown is instruction memory; registry enablement and names/hashes are symbolic access/admission metadata, not method content. User-edited methods are not automatically trace-fed learning. Same bounded evidence packet and minimum selection limit what crosses into each review context. Structural admission cannot establish truth or improvement. The supplied route and [RT-BAP-specialist-methods](runtime.md#rt-bap-specialist-methods) retain its method text, consumers and evidence; no duplicate object is declared.

#### On [RT-RTE-adapter-execute](runtime.md#rt-rte-adapter-execute)

The machine-local registry is symbolic execution policy, external receipts/artifacts are retained outside the wiki, and only separate reviewed wiki-safe promotion can admit their content. A hash-valid receipt is not itself readable topic knowledge. Private input lineage, output encoding and actual later external consumers remain unavailable. This prevents assigning one memory form or trust level to all adapter outputs; the supplied route retains the inspected implementation evidence.

#### On [RT-RTE-checkpoint-export](runtime.md#rt-rte-checkpoint-export)

Natural-language `project-knowledge.md` synthesis and readable `sources.md` ledger are distinct from symbolic `checkpoint.json` scope/input/hashes and `privacy-report.json` attestations. Disk storage does not make them one representational form. Selection starts from project packet/indexes, permits one support hop and excludes raw/session/private material by policy. Model/human semantic review and deterministic seal are separate admissions. Imported five-file collection preserves identity/trust/staleness for later compile; teammate reading `index.md` is an afforded external consumer, not demonstrated deployed wiring. SRC-1, checkpoint reference.

> Ingest all five files as one bounded collection; preserve checkpoint ID,
> audience, source IDs, trust, and staleness; dedupe by ID then path/hash.
> Imported synthesis never overwrites Projects, articles, or prior snapshots.
> --- `claude-plugin/skills/wiki-manager/references/checkpoints.md`

Rationale, rejected alternatives and input-selection reasons are explicitly retained in the bundle. Its later verification/refresh reads hashes/scope and review differences; no observation shows that a teammate actually reads every rationale. Word-retention floor is a structural budget, not semantic completeness.

#### On [RT-RTE-query-evaluation](runtime.md#rt-rte-query-evaluation)

Synthetic retained wiki fixture → guarded exact-file tool → model answer → term/length checks → metrics/report is a distinct evaluation read-back path. The 100,000-character file truncation is a harness delivery limit, not production query's memory budget. Reports may inform maintainer choice, but the inspected path does not install or later load a new query profile. Evaluation definitions and available reports are not an observed improvement trace; supplied route retains source passage and implemented limits.

## Write side

Admission mechanisms cannot be reduced to “human-curated Markdown.” [MEM-RTE-admit-sources](#mem-rte-admit-sources) and ordinary compilation are model-operated semantic writes after a user request. CLI lint fixes are software-selected edits when `--fix` is chosen. Session hooks and feedback classifiers admit operational records automatically under configuration. Digest/feedback promotion requires an explicit selected operation but contains no interactive content approval. Lessons extraction writes raw/article content ordinarily; only dry-run and proposed host rules add explicit approval steps. Larger inventory/dataset migrations and Idea approval/promotion are prescribed preview/choice boundaries, not proof of user inspection of every resulting byte.

Librarian/audit scan reports do not silently replace knowledge. Their persisted findings guide later accepted refresh/fix/adoption. Topic-guide proposals are not authoritative until separately adopted; specialists require validation/enablement, and private adapter candidates stay external until reviewed. Checkpoint seal controls one fixed bundle, not arbitrary publication. These mechanisms and their rejection/recovery limits are recorded above rather than inferred from authorship.

Trace-fed chains differ: hook event → redacted state → templated digest → later summary/pointer; user turn → classified preview/lesson → candidate/digest or explicit raw note; conversation diagnosis → structured lesson → article Rule and raw-note back-reference. The first two are implemented local transformations; the third is model doctrine. Original hook content omitted from state cannot be reconstructed from its hash. Lesson raw notes preserve requested reasons, while the article append may retain only the rule and link. Neither trace capture nor a label such as “learned” demonstrates improved future capacity.

Archive/restore is preservation with changed access metadata, not deletion. Python moves the whole initialized topic, changes `wikis.json` path/status, rebuilds the hub index and logs; restore reverses the move/status and refuses destination collisions (SRC-1, `scripts/llm-wiki`). The full skill excludes archived topics from ordinary synthesis, permits explicit archive maintenance and separately labelled deep index peeks. This is a policy at consumers, not an unreadable store. Source and literal withdrawal instead alter/remove retained material; only literal matching/rescan is deterministic in the inspected helper. Refresh's overwrite and conversation provenance are counterexamples to stronger raw-immutability/rebuild assertions.

## Read-back

Three selection/delivery patterns coexist. User query pulls indexed knowledge through a model relevance decision. Hook code independently pushes cwd-matched summary/path context on configured events. Explicit rehydrate/show/promotion pulls exact operational material or changes its admission plane. A pointer is not body delivery, a source hash is not source text, and a candidate promotion is not activation of a new instruction.

Working-context control is scoped: compact profiles and Pi launcher flags keep ambient instruction bodies out (supplied runtime); index-first selection keeps most article/raw bodies out; inventory/dataset list rules keep payloads out; selected specialists and research packets create bounded review frames. Findings/summary and raw files can survive those frames, but the host controls actual frame disposal. External host compaction removes/replaces accumulated conversation by an uninspected policy; the session bridge surrounds it with metadata checkpoints rather than implementing that policy. The by-value context window has no target-owned live reference mechanism: following a retained path is another read, not automatic resurrection of removed context.

Retained logs/checkpoints support resume and audit, not automatic methodological learning. Librarian results explicitly feed audit and scan-resume; checkpoint inputs feed refresh/import; benchmark fixture reads feed grading/maintainer reports. No hypothetical API caller is used to infer an additional deployed consumer. No route supplies observed activation or demonstrated benefit.

## Integration issues

1. **Raw immutability needs another exception/conflict.** Runtime's selected forcing case names retraction and compile migration. [MEM-RTE-refresh-sources](#mem-rte-refresh-sources) adds an explicit authorized raw overwrite in `claude-plugin/commands/refresh.md`, contrary to collection version preservation and broad normal-workflow immutability. Keep the contradictory policies rather than assert a universal invariant. It can destroy old evidence while leaving original frontmatter.
2. **Default capture is not opt-in at the helper.** `scripts/llm-wiki-session` defaults enabled/balanced and the packaged hooks invoke `--if-enabled`; missing config therefore captures. Full-skill Sessions says “Opt in.” [RT-RTE-session-bridge](runtime.md#rt-rte-session-bridge) should retain the implemented default and distinguish plugin trust/installation from `session enable`. No host execution is supplied.
3. **Query repair/logging policy is entry-specific and internally inconsistent.** Indexing reference requests stale rebuild on read, but explicit `claude-plugin/commands/query.md` forbids writes/logging and supports quick/resume/deep alternatives. [RT-RTE-query-wiki](runtime.md#rt-rte-query-wiki) is valid for compact route; do not extend the full skill's repair/logging account to every query command. [MEM-OBJ-index](#mem-obj-index) also limits count-only freshness and resulting concurrency claims.
4. **`verified` does not prove human confirmation.** Compilation writes today's date, while librarian describes it as last human confirmation. [MEM-OBJ-frontmatter](#mem-obj-frontmatter), [MEM-RTE-review-memory](#mem-rte-review-memory) and [RT-RTE-compile-wiki](runtime.md#rt-rte-compile-wiki) must not make that stronger inference. Dates are selection/scoring inputs, not independent evidence of review.
5. **Canonicality and summary labels do not certify transformations.** [MEM-OBJ-session-digest](#mem-obj-session-digest) is a metadata template, not full semantic compaction; [MEM-OBJ-feedback](#mem-obj-feedback) is regex-derived and may lose prior-result context. [RT-RTE-session-bridge](runtime.md#rt-rte-session-bridge) correctly limits automatic delivery to summary/pointer. Manual summaries bypass the payload redaction function; no blanket privacy proof is warranted.
6. **No duplicate declarations intended.** Session state/digest are explicitly parts of the supplied session route; article/raw/metadata/index objects are distinct inputs/outputs, not copies of compile/query/lint routes. Feedback classification, lessons extraction, health review, refresh, source admission and withdrawal have separate triggers/effects from supplied routes. Topic-guide authority is distinct from static query and specialist instructions. Reconciliation may connect the shared consumers but should not erase these different admission/retention units.
7. **Unresolved included detail is local, not absent.** Dataset native sample/profile/query routes, collection fetch branches, inventory migrations, media payload transformations, complete thesis rounds, generated-package transformations and evaluation assertions beyond supplied benchmark findings remain uninspected as specified in the coverage table. Private payloads, genuine session histories and host compaction state are unavailable. These limits prevent full-route equivalence, exact payload lineage, semantic privacy, complete replay and efficacy conclusions; they do not negate the source-supported paths.

## Limitations and checks

Source HEAD was rechecked against `95a042c68998559305bc69ac8c482c4e1a415ad3`. The supplied invocation, types, worker rules, collection contract and record contract were read with bounded recovery; method identity is those supplied files, not an inferred analysis version. All new source anchors refer to SRC-1 at that frozen checkout. No other run, prior analysis, external repository or live service was used. An initial search named nonexistent memory/session-context/retraction reference files and returned code 2; subsequent listing and direct reads used the shipped sessions, feedback and retract-command paths instead.

No observed-run or causal evidence is supplied. Claims of operation, useful learning, complete confidentiality, actual read-only enforcement, host-wide retention/eviction guarantees and improved judgment remain unestablished where specified. Available but uninspected files are not access gaps or evidenced absences. Deterministic validation: the required `commonplace-run validate-output` command passed with “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” This establishes structural/quotation consistency, not semantic acceptance.
