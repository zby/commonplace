---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Cortex memory: Git notes, database working state, usage-derived selection, bounded context and optional answer replay."
run-id: AAS-2026-11-07-cortex-6101286707a0-01
source-identity: "https://github.com/obelyth/cortex"
reviewed-boundary: "65d449a3275eee51efd6ce0c275572806ee9d553"
---

# Cortex memory report

## Boundary and evidence

Cortex retains Markdown knowledge and deliberate working state for later clients. It also retains access events from which software derives future selection metadata. This report includes the trusted and guest MCP routes, shipped console consumers, local import/curation drivers, groundskeeper instructions, and retrieval/prediction evaluators. It excludes no material memory surface deliberately. The surrounding assistants' conversation histories, compaction policies, scheduler execution and provider internals remain outside the supplied evidence. The frozen source and source register are in [boundary](boundary.md): SRC-1 at `65d449a3275eee51efd6ce0c275572806ee9d553`, implementation and doctrine/design only. No target execution was performed.

The supplied runtime is provisional evidence, not an inspection limit. Direct reads added `lib/access.ts`, `lib/bubble.ts`, `lib/working-state.ts`, `lib/heat.ts`, `lib/prediction.ts`, `lib/lifecycle.ts`, `lib/pins.ts`, `lib/edges.ts`, `lib/select.ts`, `lib/narrow.ts`, `lib/frontmatter.ts`, `lib/hop.ts`, `lib/mirror.ts`, `lib/anscache.ts`, the relevant database migrations, curation scripts and attention-write route. Reads of larger files were bounded to the mechanisms discussed. The following inventory separates supplied accounts from directly inspected additions; an available but uninspected detail is not an absence.

| Entry point / operative part | Source paths, SRC-1 | Coverage and limits |
| --- | --- | --- |
| MCP registration and trusted/guest dispatch | `lib/tools.ts`, `package.json` | Registration inspected; supplied [RT-RTE-reader-answer](runtime.md#rt-rte-reader-answer), [RT-RTE-guest-mediation](runtime.md#rt-rte-guest-mediation). No independent host hooks or host window history supplied. |
| Durable write, capture, exact read, index regeneration | `lib/brain.ts`, `lib/tools.ts` | Direct reads; [MEM-OBJ-notes](#mem-obj-notes), [MEM-OBJ-router](#mem-obj-router); annotate [RT-RTE-trusted-write](runtime.md#rt-rte-trusted-write). |
| Corpus process cache, tarball and database mirror | `lib/corpus.ts`, `lib/mirror.ts` | Direct reads of assembly, reconciliation and fallback; [MEM-OBJ-mirror](#mem-obj-mirror). Complete deployed SQL ordering/permissions not verified; prevents installation recovery guarantees. |
| Boot, explicit/query/paged corpus, direct read | `lib/brain.ts`, `lib/select.ts`, `lib/narrow.ts`, `lib/frontmatter.ts`, `lib/tools.ts` | Direct selection/packing reads and [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery). No host compliance or activation evidence. |
| Project handoff and preview | `lib/handoff.ts`, `lib/heat.ts` | Direct ranking/gather/logging reads; same runtime context route. Render details rely partly on supplied runtime; does not establish all edge inputs share corpus freshness. |
| Deliberate bubble and console management | `lib/bubble.ts`, `lib/tools.ts`, `lib/working-state.ts` | Direct reads; [MEM-OBJ-bubble-body](#mem-obj-bubble-body), [MEM-OBJ-bubble-state](#mem-obj-bubble-state). Console uses versioned RPCs, MCP uses unversioned item operations; deployed database unobserved. |
| Usage events, temperatures, pins | `lib/access.ts`, `lib/heat.ts`, `lib/pins.ts`, `supabase/migrations/20260807050000_case_decay_seed.sql` | Direct reads; [MEM-OBJ-note-access](#mem-obj-note-access), [MEM-OBJ-note-scores](#mem-obj-note-scores), [MEM-RTE-usage-selection](#mem-rte-usage-selection). Pin HTTP validation inspected by scoped search, not full route audit. |
| Structural and coaccess graph; inbox consumers | `lib/edges.ts`, `lib/inbox.ts`, `supabase/migrations/20260909032252_structural_edge_identity.sql` | Direct reads; [MEM-OBJ-note-edges](#mem-obj-note-edges). Full inbox heuristic inventory not re-audited; notifications are not proof of correct semantic relationships. |
| Answer cache and learning settings | `lib/anscache.ts`, `lib/learning.ts`, `lib/tools.ts` | Direct reads of identity, admission, replay and knob defaults; [MEM-OBJ-cached-answer](#mem-obj-cached-answer). Console clear/settings recovery not fully inspected; no operational cache-hit evidence. |
| Pending/rejected/accepted proposal payloads and receipts | `lib/proposals.ts`, `lib/proposal-git.ts` | Supplied [RT-RTE-proposal-admission](runtime.md#rt-rte-proposal-admission), annotated below. No private queue or reviewer rationale supplied. |
| Groundskeeper log absorption, drift correction and digest | `ops/groundskeeper/SKILL.md` | Direct complete read; [RT-RTE-groundskeeper-maintenance](runtime.md#rt-rte-groundskeeper-maintenance), annotated below. Template is not deployed scheduler evidence. |
| Ingest, description backfill, project-page split | `scripts/ingest.mjs`, `scripts/backfill-descriptions.ts`, `scripts/split-project-page.ts` | Direct reads; [MEM-RTE-local-curation](#mem-rte-local-curation). Local file publication is separate from tool admission. Input authorship is unresolved, not necessarily human. |
| Retirement nomination | `scripts/lifecycle-sweep.ts`, `lib/lifecycle.ts` | Direct reads including `supabase/migrations/20260807000000_deletion_age.sql`; [MEM-RTE-retirement-nomination](#mem-rte-retirement-nomination). Predicate consumes the bounded score view rather than lifetime history. No deletion consumer inferred. |
| Edge build/force refresh and dating maintenance | `scripts/build-edges.ts`, `lib/edges.ts`, `lib/mirror.ts` | Edge service directly read; CLI wiring searched. Per-file dating loop directly read: bounded batch, unknown/failed dates retained explicitly. Precise dating sweep scheduling remains uninspected, preventing a freshness bound for age scores. |
| Reader, retrieval, prediction evaluation; graph-hop alternative | `scripts/eval.ts`, `scripts/eval-retrieval.ts`, `scripts/eval-prediction.ts`, `lib/hop.ts` | Reader evaluation supplied by [RT-RTE-reader-evaluation](runtime.md#rt-rte-reader-evaluation); retrieval contract and prediction replay directly read; [MEM-CLM-evaluation-gate](#mem-clm-evaluation-gate). No labels/results supplied. Hop helper is not a serving route merely because exported. |
| Device, call, Ops, configuration and production receipts | `lib/tools.ts`, `lib/access.ts`; supplied runtime's Ops/configuration records | Access events are analyzed separately from operational receipts. [RT-RTE-production-jobs](runtime.md#rt-rte-production-jobs), [RT-RTE-capability-configuration](runtime.md#rt-rte-capability-configuration), [RT-RTE-local-update](runtime.md#rt-rte-local-update) cover later administrative consumers. Full event payload retention and dashboard trend aggregation uninspected: no claim that those traces train the reader or become note content. |
| Setup seed and private corpus initialization | `brain-template/`, `scripts/onboard.mjs` | Included but bodies not inspected here; upstream initial content and per-content admission remain unresolved. Prevents attributing every stored note to a particular author or trace origin; does not negate subsequent inspected write paths. |

## Core ideas

1. **Notes, working state and derived access metadata have different authority.** Git Markdown supplies evidence/text to a reader or external conversation. Postgres bubble bodies supply deliberate session-resumption material. Access events are not transcripts; software uses them to determine which descriptions and neighboring notes later appear. None establishes that the host follows the delivered material or improves its work. See [MEM-OBJ-notes](#mem-obj-notes), [MEM-OBJ-bubble-body](#mem-obj-bubble-body), [MEM-RTE-usage-selection](#mem-rte-usage-selection).
2. **Context is a bounded projection, not an always-loaded copy of memory.** Code admits a profile head, router summaries, working-state snippets and recent material. Cold notes and over-budget text remain reachable by exact read or corpus selection. A usable unscoped bubble suppresses raw-log expansion; scoped boot still selects project log entries. The host receives text by value, not references with automatic liveness or reload. [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery), [MEM-OBJ-router](#mem-obj-router).
3. **Usage learning is deterministic metadata adaptation, not a reader weight update.** The retained event-to-score/graph-to-later-context chain is inspectable. Scores are explicit scalar arithmetic and edge rows have fixed consumer rules, so those objects are symbolic, not distributed-parametric merely because numerical. Provider inference remains the separate [RT-CMP-reader](runtime.md#rt-cmp-reader). Benefit, historical activation and improved capacity are unestablished. [MEM-RTE-usage-selection](#mem-rte-usage-selection).
4. **Direct authoring is stronger than semantic admission.** Trusted tools admit caller text under shape/path/size checks without requiring per-note human review. Guest proposals instead cross a review gate; groundskeeper conservatism is prompt policy, not a veto on every trusted writer. Local import and file-reorganization scripts have still other admission paths. [RT-RTE-trusted-write](runtime.md#rt-rte-trusted-write), [RT-RTE-proposal-admission](runtime.md#rt-rte-proposal-admission), [MEM-RTE-local-curation](#mem-rte-local-curation).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-notes
Label: Durable Markdown notes and captures

Source-native identity: private brain repository's live Markdown, including `profile.md`, project/notes pages, dated logs and monthly history parts. Storage substrate: GitHub Git blobs/commits; loaded bodies also inhabit an in-process corpus and optional mirror. Form: natural-language body interpreted as knowledge by reader/host; descriptions are separately considered in [MEM-OBJ-router](#mem-obj-router). Structured paths, tags and correction markers have symbolic parser consumers. Closest supplied records are [RT-RTE-trusted-write](runtime.md#rt-rte-trusted-write) and [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery): this declares their retained content, not duplicate routes.

Lineage: caller-authored `brain_write` content, caller `brain_capture` text wrapped with date/time/tags, accepted guest proposals, local imports and host-requested maintenance. Initial private authorship and whether a particular body contains raw conversation, distilled facts or instructions are uninspected. Capture does not automatically collect the host transcript. Git commits retain change lineage, not necessarily the justification for a change. A groundskeeper is asked to retain previous wording, but ordinary replace/edit does not enforce that convention.

Consumers: future direct reads/context/handoff and provider Ask. At the reader the content is declared evidence/data, not authoritative instructions; at external hosts its actual force is unresolved. Arbitrary notes may contain rules interpreted by those hosts, but that cannot be inferred from a note type or path alone. SRC-1, `lib/brain.ts`, `lib/corpus.ts`, `ops/groundskeeper/SKILL.md`.

> const heading = tags && tags.length > 0 ? `## ${time} · ${tags.join(", ")}` : `## ${time}`;
> const entry = `${heading}\n\n${text}\n`;
> --- `lib/brain.ts`

#### MEM-OBJ-mirror
Label: Notes mirror and corpus snapshots

Source-native identity: `notes`, `sync_state`, `Corpus`; storage: optional Postgres plus process-local cached map/in-flight promises, with Git tarball fallback. Note content keeps the natural-language form of [MEM-OBJ-notes](#mem-obj-notes); SHA/path/date/CAS envelopes are symbolic access and consistency metadata. Closest supplied [RT-RTE-reader-answer](runtime.md#rt-rte-reader-answer) already establishes corpus loading; this is its storage object, not a new consumer route.

Lineage: read-time reconciliation from pinned Git files, patching a complete ahead diff of at most 25 changes/removals or full rebuilding otherwise. Whole-batch CAS publication prevents a losing sync overwriting a newer head under the store contract. NUL scrubbing means mirror bytes can differ from historical Git bytes; not every mirrored byte is a pristine verbatim archive. Full sync sends unknown dates, with content-aware preservation/dating downstream; a read does not universally establish original authorship time. Missing/empty mirror is not taken as an empty brain. The corpus's live predicate excludes archive and index/system paths; removed content can remain in Git history without entering Ask.

Later consumers: corpus-based tools, Ask, graph derivation; head failure may serve an older complete cached corpus, and mirror races can serve the winner's head. Direct `readNote` instead fetches a path through GitHub, so context/read surfaces need not use one common snapshot. SRC-1, `lib/mirror.ts`, `lib/corpus.ts`, `lib/brain.ts`.

> const corpus = assemble(new Map(after.rows.map((row) => [row.path, row.content])), head);
> return corpus;
> --- `lib/corpus.ts`

> for (const [path, content] of files) rows.push({ path, content: storableText(content), commit_sha: sha, last_commit_at: null });
> --- `lib/mirror.ts`

#### MEM-OBJ-router
Label: Router descriptions and log digests

Source-native identity: frontmatter descriptions/tags, `RouterEntry`, `logDigest`, month rows. Storage: descriptions in Git notes; generated router/digests transient at response assembly. Forms: natural-language description snippets interpreted by host, symbolic tags/date/counts/temperature used by selector. Derived display summaries are not replacement payloads for the full notes. Closest supplied [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) names the delivery route; this declares its distinct projection.

Lineage: authored/backfilled descriptions and deterministic tag/count extraction from logs. Boot collapses dated log rows by month irrespective of individual log temperature. For other notes, cold means omitted from router rendering, not deleted. Hot rows precede warm then unscored rows; month discovery rows lead a bounded budget walk. Boot router budget is 28,000 UTF-8 bytes; profile section 8,000, recent section 4,000, whole response 50,000. A large profile is head-only with a direct-read pointer. Thus even profile presence is not full-body delivery. If scoring is unavailable the router stays bounded but unranked. The generated bare `INDEX.md` is a human GitHub catalogue, not a server boot dependency.

Consumers: requesting external conversation uses summaries to choose fuller reads; software consumes tags/counts and temperatures to select. Descriptions carry no semantic verification guarantee. SRC-1, `lib/frontmatter.ts`, `lib/brain.ts`.

> if (entry.temperature === "cold") {
>       cold.push(entry);
>       continue;
>     }
> --- `lib/frontmatter.ts`

> const note = `\n\n_(PROFILE HEAD ONLY · ${utf8Bytes(safeProfile)} UTF-8 bytes total · brain_read profile.md for the full note)_`;
> --- `lib/brain.ts`

#### MEM-OBJ-bubble-body
Label: Working-state body

Source-native identity: `BubbleItem.body`; substrate: Postgres `bubble_items`, separate backup/recovery from Git. Form: deliberate natural-language focus, decision, question or handoff text; not passively recorded transcript. Distinct from [MEM-OBJ-bubble-state](#mem-obj-bubble-state)'s lifecycle metadata. Closest supplied [RT-RTE-trusted-write](runtime.md#rt-rte-trusted-write) groups mutations but does not declare this object.

Lineage: credentialed caller add/update or console-supplied content; exact upstream authorship unknown. Update corrects in place; no automatic distillation from host conversation is shown. Boot renders at most 300 characters per body under a 6,000-byte section budget. Listing permits larger but still sanitized text; omitted text is not a model-generated summary. Handoff uses project-specific working state. Immediate save confirmation may identify an item without returning its complete body. Later host interpretation supplies practical knowledge/continuation cues, not a software-enforced command. SRC-1, `lib/bubble.ts`, `lib/tools.ts`, `lib/working-state.ts`.

> const line = `- [#${it.id} ${KIND_LABEL[it.kind]}${safeText(it.project, 40) ? ` · ${safeText(it.project, 40)}` : ""} · ${age(it.touched_at)}] ${safeText(it.body, 300)}`;
> --- `lib/bubble.ts`

#### MEM-OBJ-bubble-state
Label: Working-state lifecycle and routing metadata

Source-native identity: item ID, kind, project, status, `filed_into`, surface, timestamps and console version. Form: symbolic routing/state controls; substrate: same Postgres item records as [MEM-OBJ-bubble-body](#mem-obj-bubble-body), but independently operative from prose. This is a part of the working-state responsibility in [RT-RTE-trusted-write](runtime.md#rt-rte-trusted-write), not a duplicate of its route.

Lineage: caller chooses action/project; software stamps or validates state. Open read requests one RPC sweep/count/page, at most 200 rows, aging items untouched for 14 days. Filed/aged records remain history but leave open context. MCP filing sets a destination, not a transfer of the body: caller must separately write the note; existence check fails open when corpus cannot load and never proves semantic incorporation. Console management adds request-key/version checks and refuses fallback to old management contracts; MCP's original add/update/file/drop remains another write path. Thus versioned management is not universal optimistic concurrency.

Consumers: deterministic open/project filters and render budget determine later inclusion; human history views can inspect retired state. Filing/drop changes later context availability, not truth. SRC-1, `lib/bubble.ts`, `lib/tools.ts`, `lib/working-state.ts`; [RT-RTE-trusted-write](runtime.md#rt-rte-trusted-write).

> body: JSON.stringify({ status: "filed", filed_into: notePath, touched_at: new Date().toISOString() }),
> --- `lib/bubble.ts`

#### MEM-OBJ-note-access
Label: Served-note access events

Source-native identity: `note_access` rows carrying path/tool/surface/mode and database time. Form: symbolic raw access trace, not note meaning, model reasoning or full conversation. Substrate: optional Postgres. Closest supplied [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) concerns delivered content; these are distinct observations about delivery.

Producer: `logNoteAccess`, called for served direct text, boot expanded profile/logs, handoff served notes and Ask candidate paths. It records provision, not evidence the model cognitively used a note; timed-out Ask can still have candidate metadata. Failed event writes log/drop rather than failing the product. Console heat and handoff previews deliberately log nothing. Cache hits return before Ask logging. Origin is system serving telemetry, with human/agent requests mixed and upstream principals not reconstructed from a `surface` label. Consumers: SQL temperature calculation, coaccess derivation, prediction replay. SRC-1, `lib/access.ts`, `lib/tools.ts`, `lib/brain.ts`, `lib/handoff.ts`, `lib/heat.ts`.

> const write = store
>     .access(paths.map((path) => ({ path, tool, surface, mode })))
>     .catch((e) => console.error(`[access] dropped ${paths.length} row(s): ${String(e)}`));
> --- `lib/access.ts`

#### MEM-OBJ-note-scores
Label: Temperatures and operator pins

Source-native identity: `note_scores` view and `note_pins` table. Form: symbolic explicit arithmetic, categorical temperature and path-keyed override; operator reason is natural-language explanatory metadata displayed by console. Substrate: Postgres view/table, with score rows loaded into selectors. Not an embedding and not changed provider weights. Distinct from supplied [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery)'s final bundle and [MEM-OBJ-note-access](#mem-obj-note-access)'s raw events.

Derivation: the inspected view restricts access aggregation to 180 days, uses 30-day half-life access decay normalized to busiest note, 21-day write decay and a directory prior, weighted 0.45/0.30/0.25. Hot threshold 0.45, warm 0.20, with seven-day write grace and overriding pins in either direction. Despite console comments calling reads all-time, the view's `reads` and `last_read` come from this bounded aggregation. The private deployment's schema may differ; no lifetime-read inference follows here.

Consumers: router bands, handoff ranking, heat display and retirement nominations. Router uses bands/path order, not a complete sort by raw score; handoff neighbors use numeric scores first. Operator pins alter selection without rewriting a note; clearing restores computed bands. Pin reasons persist/display, but score arithmetic consumes temperature, not reasons. SRC-1, `supabase/migrations/20260807050000_case_decay_seed.sql`, `lib/frontmatter.ts`, `lib/handoff.ts`, `lib/pins.ts`, `lib/heat.ts`.

> from note_access
>   where at > now() - interval '180 days'
>   group by path
> --- `supabase/migrations/20260807050000_case_decay_seed.sql`

#### MEM-OBJ-note-edges
Label: Derived note graph

Source-native identity: `note_edges`, `edges_state`; form: symbolic endpoints/kind/weight/head/algorithm/usage identity plus natural-language evidence strings. Substrate: Postgres. Structural link/tag/lexical/correction rows derive from note contents; coaccess rows derive from served-note events. These are distinct from source bodies and raw access events; closest supplied [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) names their later handoff consumer, not this object.

The current rebuild derives coaccess from the preceding 90 days of completed UTC hours; excludes boot/handoff/maintenance, rejects hours with more than six distinct paths, requires two shared hours and live endpoints. It refuses more than 100,000 eligible events rather than silently truncating training. Coaccess evidence records the policy/count, not a retained explanation of why two notes matter. Structural evidence is bounded/scrubbed; it is displayable lineage, not proof of a semantic relationship. Versioned rebuild locks and expected head/watermark/cutoff/structure identity can refuse stale inputs. Read-time corpus returns schedule refresh, with process cooldown; this is not a periodic scheduler guaranteeing completion.

Consumers: handoff neighborhood selection/explanation, console graph and coaccess-gap inbox. `edgesFor` reads rows without the freshness confirmation that `allEdges` performs; a handoff cannot be assumed to use a fresh graph just because its corpus has a SHA. Current-source membership and render budget further constrain which neighbor bodies reach a host. SRC-1, `lib/edges.ts`, `lib/handoff.ts`, `lib/inbox.ts`, `supabase/migrations/20260909032252_structural_edge_identity.sql`.

> if exists(select 1 from jsonb_to_recordset(edges) x(kind text) where x.kind='coaccess') then
>     raise exception 'coaccess must be derived from eligible history';
>   end if;
> --- `supabase/migrations/20260909032252_structural_edge_identity.sql`

#### MEM-OBJ-cached-answer
Label: Rendered answer replay

Source-native identity: `CachedAnswer`; substrate: optional environment-namespaced KV. Mixed parts: natural-language reply and quoted evidence interpreted by caller; symbolic stamp/model/commit/token estimate/time and key controlling replay. Closest supplied [RT-RTE-reader-answer](runtime.md#rt-rte-reader-answer) and [RT-RTE-guest-mediation](runtime.md#rt-rte-guest-mediation) already declare replay routes; no new route is declared here.

Lineage: Ask model output parsed/verified/rendered, then redacted and asynchronously stored if the rendered stamp is not UNVERIFIED. A verified quotation does not establish correct inference; caching does not upgrade its warrant. Replay identity includes pipeline version, normalized question preserving case, corpus SHA, resolved model, k/full, door, sorted scope and citation policy. Default TTL seven days, configurable one to thirty. Explicit clear scans the environment namespace and deletes in batches of 200; failure is not reported as successful clearing. Malformed/unreachable/slow KV is a miss. Code does not regenerate or reverify the stored answer on a hit; it returns redacted stored prose and cache marker, bypassing provider and guest spend. Source changes alter identity, not a semantic purge of every old cache object. Consumer is the requesting caller, not later reader training. SRC-1, `lib/anscache.ts`, `lib/tools.ts`, `lib/learning.ts`.

> if (key && stampOf(reply) !== "UNVERIFIED") {
> --- `lib/tools.ts:303-320`

### Routes

#### MEM-RTE-usage-selection
Label: Usage traces shaping later context

Endpoints/progression: note-serving tools → asynchronous `note_access` append → SQL score view and versioned coaccess rebuild → router/handoff/inbox selection → later caller context or console findings. Owner: code/database, with operator-selected pins/knobs. This extends, rather than duplicates, the delivery progression in [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery): its distinct subject is automatic access-trace transformation. SRC-1, `lib/access.ts`, `lib/corpus.ts`, `lib/edges.ts`, `lib/frontmatter.ts`, `lib/handoff.ts`, relevant migrations in [MEM-OBJ-note-scores](#mem-obj-note-scores) and [MEM-OBJ-note-edges](#mem-obj-note-edges).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Product result does not wait for access observation; derivation can report current/rebuilt/busy/capacity/stale-input rather than guarantee an updated graph.
- Later read-back: Later boot consumes temperature bands; later handoff selects graph neighbors ordered first by live score, then blend and path; inbox consumes coaccess to propose gaps, not automatically insert links.
- Delegated visibility: External conversation receives bounded note text and display explanations, not full access log; prediction evaluator can read event history through its own database credential.
- Selection predicate: Score components and pins for router; project-page adjacency for handoff, eight-neighbor shortlist and byte budget; coaccess admission excludes pushed/maintenance modes and high-fanout windows, as specified in the object records.
- Invalidation or expiry: Time decay and history windows; corpus/usage/structure identity gate graph rebuild. Old graph rows may remain after refusal or refresh failure. No uniform read-time freshness invariant on edgesFor.
- Activation or effect: Symbolic selectors wire changed metadata into later packing. Actual host behavioral change and benefit are unobserved.
- Evidence limits: A served-note event is not a successful-use reward. Private event history, deployed schema and run outcomes are unavailable; capacity refusals and dropped observation writes prevent assuming complete usage learning.

Admission control: software records events without per-event human approval; fixed SQL/code transforms them. Operator may override pin/threshold/budget independently. Starting Ask is not human approval of each derived edge. No expected-answer oracle or semantic quality gate admits each metadata update. Maintenance-mode exclusion depends on the caller declaring maintenance=true: direct reads default to read mode, and the groundskeeper template does not explicitly pass that flag. Its sweep can therefore enter coaccess if a host omits the declaration; the mode filter is not a reliable classifier of actual work origin. Recovery retains last graph on refused publication and retries via later requests/explicit rebuild; clearing a pin is reversible metadata change, not model rollback. This is a trace-fed durable behavior-shaping path even without changes to note prose. Its retained reasons are shallow provenance strings/counts and explicit score components; handoff can expose edge evidence while code consumes weights. Under `learning`, improved future capacity is unestablished: wiring selection changes does not demonstrate improvement.

> return out
>     .sort((a, b) => b.score - a.score || b.blend - a.blend || byName(a.path, b.path))
>     .slice(0, k);
> --- `lib/handoff.ts`

#### MEM-RTE-local-curation
Label: Operator-invoked import and local reorganization

Endpoints/progression: local invocation/input files → preview/validation → explicit commit/apply/write flag → GitHub import or local note files → separately published brain revision → later corpus/router/Ask. Owner: invoking operator chooses inputs/flags; deterministic scripts transform content. Distinct from [RT-RTE-trusted-write](runtime.md#rt-rte-trusted-write): these callers bypass the MCP handler, and two operate on local files rather than `writeNote`. SRC-1, `scripts/ingest.mjs`, `scripts/backfill-descriptions.ts`, `scripts/split-project-page.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Planned/applied file counts, split verification/refusal, or per-import failures; a later failure need not undo earlier successful files.
- Later read-back: Committed imported notes enter later corpus. Backfilled descriptions and split status/history affect later router and bounded retrieval only after local changes are published to the configured notes repository.
- Delegated visibility: No model call in inspected transformations; no host transcript implicitly imported. Imported prose gets a provenance/unverified-history line; split preserves section bodies and writes new descriptions/pointers.
- Selection predicate: Ingest nonrecursive md/markdown/txt files up to 256 KiB into notes/projects, slug collision rejection; backfill supplied path/description/tag JSON skipping existing descriptions; split caller page and last matching kept headings, dated monthly history, byte caps.
- Invalidation or expiry: Existing import target can fail; backfill won't overwrite a description; split refuses dirty source/history or occupied destinations. No automatic expiry of imported knowledge.
- Activation or effect: Changes durable content or its organization, not merely access metadata. Semantic trust is not conferred by successful import, round-trip checks or byte-preservation verification.
- Evidence limits: Input authorship, actual private files and publication events uninspected. A local write is not proof a production corpus consumed it.

Admission: operator selects a batch and enables writes; this establishes human workflow initiation, not individual content approval or human authorship. Code vetoes file/shape/collision/preservation/budget conditions, not false claims. No answer oracle; open import and deterministic migration mode. Ingest can partially commit; backfill writes sequentially; split requires clean paths to make Git recovery possible but does not automatically publish or roll back every interrupted multi-file write. Split is relocation of retained bodies, not trace summarization or learned rules. Backfill retains original body as suffix; generated history descriptions need not carry the reasons for an original decision, though the preserved body may.

> `\n\n_Ingested ${today} from ${f.name}. Review before trusting: ingested text has no verification history._\n`;
> --- `scripts/ingest.mjs`

> if (!write) {
>     console.log("\ndry run — nothing written. Add --write to apply.");
>     return 0;
>   }
> --- `scripts/split-project-page.ts`

#### MEM-RTE-retirement-nomination
Label: Cold-note retirement nomination

Endpoints/progression: service-credentialed local sweep → optional propose_deletions RPC → deletion_candidates → printed path/reason list for person. Owner: caller selects --propose and age; database nominates, human decision remains outside this command. No supplied counterpart after comparison with [RT-RTE-groundskeeper-maintenance](runtime.md#rt-rte-groundskeeper-maintenance): this is a separate CLI/database mechanism, not guest-proposal review. SRC-1, `scripts/lifecycle-sweep.ts`, `lib/lifecycle.ts`, `supabase/migrations/20260807000000_deletion_age.sql`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Temperature counts and undecided candidate reasons; without --propose it only reports existing state.
- Later read-back: Subsequent sweep reads undecided candidate path/reason records; console's lifecycle summary is described by source comments, not independently traced here.
- Delegated visibility: Human receives nomination text, not automatic disappearance of note content.
- Selection predicate: SQL selects cold temperature, reads=0, no pin and written_at older than --days (default 180), suppressing duplicate path nominations. The current score view's reads cover only 180 days: this means no reads in that window, not necessarily never read in the note's life.
- Invalidation or expiry: Nomination decision remains null until external human action; expiry or downstream deletion/recovery uninspected — this command supplies no delete operation.
- Activation or effect: Optional RPC creates review candidates; no inferred removal from later corpus.
- Evidence limits: Inspected SQL and caller establish nomination capability, not actual nominations, human decisions or deleted content. The rendered reason says never read more strongly than its current view warrants. Older module comments saying never called are not a current caller inventory.

Admission: software proposes metadata under age/score criteria after a caller opts in; command does not approve retirement. No answer oracle. The proposal is an administrative aid, not learned knowledge or evidence of semantic obsolescence. No rollback of notes is needed for this command because it does not mutate note bodies; downstream human action is uninspected.

> if (propose) {
>     const rawN = await rest<unknown>("rpc/propose_deletions", {
>       method: "POST",
>       body: JSON.stringify({ min_age_days: days }),
>     });
> --- `scripts/lifecycle-sweep.ts`

> where s.temperature = 'cold'
>     and s.reads = 0
>     and s.pinned is null
>     and s.written_at < now() - make_interval(days => min_age_days)
> --- `supabase/migrations/20260807000000_deletion_age.sql`

### Claims

#### MEM-CLM-evaluation-gate
Label: Evaluation does not automatically promote a ranker

Claimed operation: source says usage-blend and graph-hop alternatives must beat incumbents. Implementation retains candidate methods and evaluation callers, while production handoff ranks numeric temperatures first and ordinary Ask uses lexical narrowing. Closest supplied [RT-RTE-reader-evaluation](runtime.md#rt-rte-reader-evaluation) is the separate model-answer evaluator, not prediction replay or automatic promotion.

Prediction replay reads access rows, forms completed-hour windows and compares recency/frequency against a graph blend at recall@5/10. Its own output explicitly disclaims promotion, uses current local corpus structure/endpoints rather than historical structure, and admits that upper-ID pinning is not a transactional history snapshot. Retrieval evaluation tests expected source inclusion and optional normalized phrase presence under production caps; NONE labels are excluded. `hopNarrow` supplies an exported candidate capability and evaluator input, not an established reader consumer route. Model-free evaluation is not itself demonstrated benefit.

Source comments reporting that a gate lost are attributed reported history, not supplied run evidence. Source-native policy guidance can shape maintainers' later decisions, but no score-to-installed-successor automatic route is established from these commands. SRC-1, `lib/prediction.ts`, `lib/hop.ts`, `lib/handoff.ts`, `scripts/eval-prediction.ts`, `scripts/eval-retrieval.ts`.

> console.log(`Learning policy: ${LEARNING_POLICY}. Coaccess uses only the preceding 90 days of completed UTC hours. Structural links/tags and coaccess endpoint availability use the current local corpus, not a historical snapshot. Historical baseline scores and scored-window targets remain unfiltered. The log upper ID is pinned; concurrent history edits are not a transactional snapshot. No ranking is promoted by this command.`);
> --- `scripts/eval-prediction.ts`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-selection-metadata
Label: Access-derived metadata reaching context selectors

Consumer: deterministic router and handoff selectors. Channel: Postgres score/edge rows loaded by server. Force: fixed filtering/ordering/budget rules, unlike a model-interpreted request. Horizon: future requests/sessions until new scores, pins, graph publication or corpus change. Distinct from [RT-BAP-answer-instructions](runtime.md#rt-bap-answer-instructions), whose consumer is the reader model and whose content is the shipped answer contract. The metadata path does not make source-body instructions authoritative and does not establish later host action. SRC-1, `lib/frontmatter.ts`, `lib/handoff.ts`; [MEM-RTE-usage-selection](#mem-rte-usage-selection).

> const rank = (t?: Temperature) => (t === "hot" ? 0 : t === "warm" ? 1 : 2);
> --- `lib/frontmatter.ts`

## Annotations

#### On [RT-RTE-trusted-write](runtime.md#rt-rte-trusted-write)

Memory-specific admission and curation: trusted caller has semantic authorship/admission; code checks path, mode, uniqueness and size. Physical I/O is GitHub or Postgres, not itself a reviewer. `writeNote` runs storable-byte sanitization on final merged content, preserving fresh-content edit uniqueness on retry. `brain_capture` adds time/tags but performs no meaning extraction. `readNote` applies redaction/footer only at egress; server-side edits use `readNoteRaw` to avoid persisting a lossy display. Source comments describe prior corruption, not an independently authenticated incident. SRC-1, `lib/brain.ts`.

Console attention actions are another material consumer/editor: settled sets decays=false, queue adds reverify date, verified refreshes an existing verification stamp and refuses to invent one. A human action chooses that status; the server does not verify the external fact before storing its stamp. The route writes a full replacement through `writeNote`; it is not an automatic semantic correction. Actual groundskeeper consumption of reverify requests remains unresolved: parser comments describe it but the supplied template does not explicitly instruct this queue. SRC-1, `app/s/[secret]/console/attention/verify/route.ts`, `lib/frontmatter.ts`.

> const res = await writeNote(b.path, next, "replace");
> --- `app/s/[secret]/console/attention/verify/route.ts`

#### On [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery)

Read-back direction: client requests boot/handoff; code independently selects bundled retained parts inside the requested operation. This is not unsolicited server initiation. Explicit corpus paths are caller selection, query corpus is lexical selection, listing is pagination; none proves a host accessed omitted text. Exact `brain_read` can fetch a note independently of corpus packing and supports a maintenance flag for telemetry mode. `brain_corpus` ceiling is 100,000 bytes including envelope, advances continuation in every mode, and provides direct-read recovery for oversized or envelope-refused notes. Ask default is separately k=15 and 400,000 body bytes per supplied runtime. These are bytes, not a demonstrated model token-window limit. SRC-1, `lib/tools.ts`, `lib/select.ts`, `lib/narrow.ts`; [RT-RTE-reader-answer](runtime.md#rt-rte-reader-answer).

Working-context control: boot preferentially withholds cold descriptions, elides logs when usable working state exists, truncates large profile and bubble bodies, and retains pointers/coverage instead of sharing all memory. Scoped boot still emits matching project log sections even with a bubble; general bubble items can join scoped boot, while project handoff requests includeGeneral=false. Handoff default is 24,000 bytes, clamped 4,000–100,000, with excerpts/omission receipts. No Cortex subagent stack frame or host compaction is established: this is service-side selection before an independent host receives a value. Removed/withheld notes remain independently reachable; nothing automatically follows a pointer or decides host-window liveness. SRC-1, `lib/brain.ts`, `lib/bubble.ts`, `lib/handoff.ts`.

> if (bubbleRendered.usableItems === 0) {
> --- `lib/brain.ts`

#### On [RT-RTE-proposal-admission](runtime.md#rt-rte-proposal-admission)

Retained proposal content is untrusted prose in KV, delivered with nonce fencing to a trusted reviewer; it is not already in the notes corpus. Its path/mode/reason/ID and durable Git operation receipt are symbolic admission/replay state, not equivalent knowledge bodies. Accept can admit the note without preserving reviewer reasoning; rejection/expiry prevents that pending payload entering the ordinary corpus, but does not revoke previously committed text or every cached historical answer. Queue expiry and Git receipt replay have different horizons. Filing proposal text and retaining its receipt are distinct consumers. These findings use the supplied record's passages and SRC-1 `lib/proposals.ts`, `lib/proposal-git.ts`; no independent reread of those modules was required here.

#### On [RT-RTE-groundskeeper-maintenance](runtime.md#rt-rte-groundskeeper-maintenance)

Trace-fed write is requested, not observed: daily activity log text → host interpretation selecting durable decisions/status/facts → page edits plus absorption marker → later corpus/context/Ask. Another branch checks live-state claims, retains old wording and updates verification/unverified annotations; a final digest re-enters the log. It preserves both raw log and selected derived knowledge instead of replacing the only raw trace with a summary. Whether a particular log's original text came from a human, model, tool or mixed session is unresolved. It is not an automatic dump of every conversation. Source reasons may survive in bodies, but the procedure only demands preservation conventions, not a complete causal rationale or a mandatory future rationale reader. SRC-1, `ops/groundskeeper/SKILL.md`.

> Leave the log intact; append
> `[groundskeeper: absorbed <date>]` when done.
> --- `ops/groundskeeper/SKILL.md`

Memory admission is the host's model judgment under conservative instructions, with health-check veto requested by prompt. A user starting a scheduled task is not per-content approval. Proposal accept/reject is separately reserved for a human in this template; the server trusted route has broader authority. The runtime already distinguishes that policy from enforcement. No claim of successful trace learning, theory criticism or improvement follows from the prompt alone.

## Write side

The authoritative content writes are in [RT-RTE-trusted-write](runtime.md#rt-rte-trusted-write); pending-to-admitted guest content uses [RT-RTE-proposal-admission](runtime.md#rt-rte-proposal-admission). Their author, deciding principal, software veto and physical writer are not interchangeable. Local ingest/backfill/split are separately admitted in [MEM-RTE-local-curation](#mem-rte-local-curation). Initial seed/private content remains unresolved without suppressing these known subsequent transformations.

Automatic transformations include read-time mirror healing and stale-row removal, storable-byte sanitization, deterministic router/log projection, access logging and score/edge derivation. They do not all change meaning: mirror copying and sanitization are storage operations; snippet/digest rendering changes delivered coverage; usage derivation changes selection policy inputs. [MEM-OBJ-mirror](#mem-obj-mirror), [MEM-OBJ-router](#mem-obj-router), [MEM-RTE-usage-selection](#mem-rte-usage-selection). No automatic conversation compaction/checkpoint mechanism was established in the inspected service; explicit bubble bodies and log absorption are not substituted for an uninspected host's checkpoint variants.

Withdrawal is layer-specific. Exact note edit/replace can remove stale wording, while groundskeeper policy requests keeping it as was/SUPERSEDED history. Filing/drop/aging withdraws a working item from open context but retains row history. Corpus exclusion omits archive/index/system paths without erasing Git history. Retirement command nominates rather than deleting. Guest rejection/expiry prevents admission from that queue. Cache key changes make old entries ineligible for the new identity; TTL eventually expires them. None is a universal semantic revocation across hosts that already received text. SRC-1, `lib/brain.ts`, `lib/bubble.ts`, `lib/corpus.ts`, `lib/anscache.ts`; [MEM-RTE-retirement-nomination](#mem-rte-retirement-nomination), [RT-RTE-proposal-admission](runtime.md#rt-rte-proposal-admission).

Evaluation remains measurement, not write admission. Reader labels/judges, retrieval labels/phrase checks and prediction future-window targets provide different comparison bases. Their outputs do not automatically update note contents, reader weights or production rankers. The comments asserting past wins/losses do not replace retained measurements. [MEM-CLM-evaluation-gate](#mem-clm-evaluation-gate), [RT-RTE-reader-evaluation](runtime.md#rt-rte-reader-evaluation).

## Read-back

| Retained part | Later actual consumer and delivery | Selection, budget and authority |
| --- | --- | --- |
| Note bodies | Provider reader through Ask; external conversation through read/context/corpus/handoff | Scope, lexical k/log/part/body-byte admission or explicit path/paging; model gets data under answer contract. Direct tool text is not subject to Ask's quote verdict. [RT-RTE-reader-answer](runtime.md#rt-rte-reader-answer), [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery). |
| Description/digest projection | External host choosing follow-up reads | Boot code bands/month rows and fixed section budgets. Derived display is not the full underlying retained body. [MEM-OBJ-router](#mem-obj-router). |
| Open working bodies and state | Later boot, handoff, list and console management | Fresh/project/general/status filters, read-path aging, body clipping and byte limits. Requested output interpreted by host; status consumed by software. [MEM-OBJ-bubble-body](#mem-obj-bubble-body), [MEM-OBJ-bubble-state](#mem-obj-bubble-state). |
| Raw access events | SQL scoring/rebuild and prediction replay | Fixed temporal/mode/fanout filters, not a model training request; no semantic success label. [MEM-OBJ-note-access](#mem-obj-note-access). |
| Temperatures/pins/edges | Router/handoff/inbox and human diagnostic displays | Automatic selectors inside caller-requested bundle; content availability and budget still intervene. Reasons can be shown, weights/bands decide code. [MEM-RTE-usage-selection](#mem-rte-usage-selection). |
| Rendered cached answer | Later matching MCP caller | Exact policy/version identity and TTL; no new model or verification. [MEM-OBJ-cached-answer](#mem-obj-cached-answer). |
| Pending proposals / operation receipts | Trusted reviewer / retry protocol | ID/queue policy and fencing versus Git receipt recovery; not interchangeable with durable note recall. [RT-RTE-proposal-admission](runtime.md#rt-rte-proposal-admission). |
| Maintenance results | Later context/Ask and future groundskeeper sessions | Preserved page bodies, absorption markers and daily digest; afforded by template, actual recurrent execution unknown. [RT-RTE-groundskeeper-maintenance](runtime.md#rt-rte-groundskeeper-maintenance). |
| Retirement candidates | Sweep operator | Undecided path/reason query; no inferred automatic destructive consumer. [MEM-RTE-retirement-nomination](#mem-rte-retirement-nomination). |
| Ops/configuration/job receipts | Subsequent console recovery/admission/status decisions | Administrative symbolic state, not demonstrated reader memory or knowledge extraction. Supplied [RT-RTE-production-jobs](runtime.md#rt-rte-production-jobs), [RT-RTE-capability-configuration](runtime.md#rt-rte-capability-configuration). |

An exported store/helper alone is not another consumer route. In particular, graph-hop candidate generation and the SQL search alternative remain capabilities/evaluation arms unless an actual caller delivers their result onward. Likewise provider prefix caching of stable prompt bytes does not establish retained host knowledge or updated weights. The provider's opaque storage policies are outside this source boundary. [MEM-CLM-evaluation-gate](#mem-clm-evaluation-gate), [RT-CMP-reader](runtime.md#rt-cmp-reader).

## Integration issues

- **No declaration duplicates a supplied referent.** New objects identify material inputs/results of the supplied routes; route-specific memory detail is annotated instead of redeclaring those routes. Usage transformation, local curation and retirement are additional progressions, not replacements for the runtime's writer/context/groundskeeper records. The selection-metadata authority path differs from model prompt authority.
- **Refine broad context wording, not the supplied route identity.** [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) correctly notes a complete router candidate set and budgeted result. [MEM-OBJ-router](#mem-obj-router) adds that boot output is not one row per note: month aggregation, cold omission, section budgets and profile truncation intervene. No full-profile/full-router delivery inference should be drawn from the generic component names.
- **Freshness is heterogeneous.** [MEM-OBJ-mirror](#mem-obj-mirror) can serve cached or reconciliation-winner SHA; [MEM-OBJ-note-edges](#mem-obj-note-edges) notes that handoff edgesFor lacks allEdges-style freshness confirmation. Do not combine [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery)'s corpus commit with graph/bubble into a universal snapshot guarantee. Actual inconsistent delivery remains unobserved.
- **Lifetime-read labels are misleading in source.** [MEM-OBJ-note-scores](#mem-obj-note-scores) retains the 180-day view restriction despite heat comments saying all-time and lifecycle prose saying ever read. This does not correct a supplied runtime assertion. The SQL interaction is directly established in [MEM-RTE-retirement-nomination](#mem-rte-retirement-nomination): reads=0 is drawn from that view, so a note last read outside the window is not protected by a lifetime-read test. Nomination is still not deletion.
- **Reverify queue consumption is not established by parser documentation.** The console persists a request, but the read template does not explicitly prioritize/consume it. Annotation on [RT-RTE-trusted-write](runtime.md#rt-rte-trusted-write) names the known write; [RT-RTE-groundskeeper-maintenance](runtime.md#rt-rte-groundskeeper-maintenance) should not be silently expanded to an implemented request-consumption guarantee.
- **Maintenance classification is caller-declared.** [MEM-RTE-usage-selection](#mem-rte-usage-selection) excludes rows tagged maintenance, not all actual maintenance reads. The groundskeeper template does not explicitly request maintenance=true, while the tool defaults to read. Do not infer sweep-origin purity of coaccess from the SQL filter alone; no contaminated live graph is observed either.
- **Alternative admission and measurement remain distinct.** Local scripts bypass MCP, while graph-hop/prediction candidates and evaluation results do not automatically replace serving rankers. [MEM-RTE-local-curation](#mem-rte-local-curation), [MEM-CLM-evaluation-gate](#mem-clm-evaluation-gate). Historical quality claims in source comments lack supplied traces; no exercised learning conclusion follows.
- **Unresolved included details remain local.** Setup seed authorship, deployed schema/dating tick guarantees, full inbox heuristics, exact operational-log payload retention and console administrative recovery are not fully inspected here, as inventory states. These prevent exhaustive provenance/retention and deployment conclusions, not the positive access-derived and deliberate-memory paths established above.

## Limitations and checks

Only source-level capacity/wiring and attributed procedure are established. No private corpus, live database, labels, scheduler runs, provider execution or later host actions are supplied. Thus delivery is not observed activation; updated ranking inputs or retained corrections do not establish improved capacity. Provider memory, model adaptation and external-host trimming/checkpoint behavior are uninspected. Setup/default authorship gaps do not erase known caller-authored writes; graph refresh failure does not erase the implemented trace-derived update path.

Frozen source HEAD was rechecked as `65d449a3275eee51efd6ce0c275572806ee9d553`. Method identity is the supplied memory job, member type, worker rules and shared records contract; no other analysis or prior characterization was consulted. All source claims resolve within SRC-1; bounded source searches/read errors for nonexistent helper guesses were corrected by listing the frozen lib directory, not treated as absences. Validation: deterministic role/content check passed with the invocation's prepared command; this establishes form and quotation occurrence, not semantic acceptance or observed operation.
