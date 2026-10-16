---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "kgai decision memory: immutable reasons and mutations, current-head recall, historical read-back and optional trace extraction."
run-id: AAS-2026-10-14-kgai-54bcae52e039-01
source-identity: "https://github.com/kgaidev/kgai"
reviewed-boundary: "0ac7f1fae4528805c1d5f504c1bfd6cc34ac953b"
---

# kgai memory report

## Boundary and evidence

The memory boundary is kgai's shipped decision acquisition, admission, revision, storage and later consumption at the frozen revision above. It includes foreground capture, optional side-model extraction, approved capture conventions, synchronization, graph rebuild, CLI recall, editor replay and evaluation tooling. It does not attribute the external coding host's context compaction or model-parameter management to kgai. External hosts, native database internals and remote services have the exclusions in [boundary](boundary.md#boundary-and-evidence); their deployed behavior and the exact session context copied into a fork remain unknown.

Evidence is SRC-1 implementation and doctrine/design, not an observed execution. Supplied runtime findings order the inspection but are not an inspection limit. Direct reads added `src/internal/event/event.go`, `src/internal/engine/search.go`, context/history/search/as-of/export/doctor portions of `src/internal/engine/reads.go`, decision construction and replay portions of `src/internal/engine/engine.go`, store resolution/read/append portions of `src/internal/store/store.go`, mutation application in `src/internal/graph/graph.go`, in-memory replay in `src/internal/replay/projection.go`, decision detail in `src/internal/view/view.go`, the complete skill, ask/history commands, hook manifest, injection script and optional capture mod, plus the verdict portion of `tests/host-smoke.sh`. All concern the registered frozen source; newly inspected paths do not introduce sources.

| Entry point or operation | Source paths (SRC-1) | Coverage and remaining limits |
|---|---|---|
| CLI dispatch and ingest; initialization | `src/main.go`, `src/internal/engine/engine.go`, `src/internal/store/store.go` | Dispatch directly checked; [RT-RTE-foreground-capture](runtime.md#rt-rte-foreground-capture), [MEM-OBJ-decision](#mem-obj-decision), [MEM-OBJ-event](#mem-obj-event). Generic shell/library caller does not establish human admission. |
| Skill/ask/history/review/decision command policies | `skills/knowledge-graph/SKILL.md`, `commands/kg-ask.md`, `commands/kg-history.md`, `commands/kg-review.md`, `commands/kg-decision.md` | Skill/ask/history directly read; review/decision consent differences supplied by [RT-RTE-foreground-capture](runtime.md#rt-rte-foreground-capture). Policy is not compliance. |
| Lifecycle wiring, turn markers and Stop capture | `hooks/hooks.json`, `hooks/turn-state.sh`, `hooks/auto-capture-stop.sh`, `src/internal/turn/turn.go` | Manifest directly read; marker/nudge implementation supplied by [RT-RTE-foreground-capture](runtime.md#rt-rte-foreground-capture). Markers are transient access/control state, not derived engineering reasons. |
| Optional fork, confirmation, compact display | `mods/kgai-mod/hooks/register.tsx` | Direct read; [RT-RTE-fork-capture](runtime.md#rt-rte-fork-capture) annotation. Copied host input is opaque; UI hiding does not establish model-window trimming. |
| Configuration/prompt/trust and store relocation | `hooks/inject-prompt.sh`, `src/internal/store/settings.go`, `src/internal/store/trust.go` | Injection directly read; loader/approval supplied by [RT-RTE-config-admission](runtime.md#rt-rte-config-admission). [MEM-OBJ-prompt](#mem-obj-prompt) separates content from approval metadata. |
| Context, path/topic selection and bounded reasons | `src/internal/engine/reads.go`, `src/internal/engine/search.go` | Direct read; [MEM-RTE-context-recall](#mem-rte-context-recall). Item/count and text budgets, not a total token budget. |
| Search, history, alias repair and conflicts | `src/internal/engine/reads.go`, `src/internal/engine/search.go` | Direct read; [MEM-RTE-search-history](#mem-rte-search-history). Search can return unattached decisions; history cannot. |
| Query, resolve, export, temporal reconstruction | `src/main.go`, `src/internal/engine/reads.go` | Dispatch/direct scoped reads plus [RT-RTE-query-read](runtime.md#rt-rte-query-read); [MEM-RTE-asof-recall](#mem-rte-asof-recall). Export is a structural diagnostic, not a full rationale archive. Detailed resolve branches remain supplied by runtime, not independently audited. |
| Supersession, retirement, rebuild, bulk/incremental replay | `src/internal/engine/engine.go`, `src/internal/graph/graph.go`, `src/internal/replay/projection.go` | Direct reads; [MEM-OBJ-graph](#mem-obj-graph), write-side account. Full bulk-loader implementation not independently inspected; prevents universal equivalence claims. |
| Sync, rotate, remote and autosync diagnostics | `src/internal/engine/engine.go`, `src/internal/remote/objectsync.go`, `hooks/auto-sync.sh` | [RT-RTE-team-sync](runtime.md#rt-rte-team-sync) supplies transport admission/reconciliation. Complete Git/cloud/S3 internals not independently inspected; no transport-wide security/convergence claim. |
| Editor reader/service methods and decision details | `src/cmd/kgread/server.go`, `src/internal/view/model.go`, `src/internal/view/view.go`, `src/internal/replay/projection.go` | Protocol method inventory searched, replay/detail directly read; [RT-RTE-editor-read](runtime.md#rt-rte-editor-read) annotation. Full rendering/extension integration remains uninspected. |
| Evaluation, doctor/status, deterministic export | `tests/host-smoke.sh`, `src/internal/engine/reads.go` | [MEM-CMP-host-smoke](#mem-cmp-host-smoke). No evaluated run or feedback-to-reasons loop established. |
| Installation and opaque provider parameters | `scripts/install.sh`, `mods/kgai-mod/hooks/register.tsx` | [RT-RTE-engine-install](runtime.md#rt-rte-engine-install), [RT-CMP-host-model](runtime.md#rt-cmp-host-model). Capability replacement and external parameters, not demonstrated trace learning. |

No tracked-text access gap was encountered. Uninspected branches above remain eligible frozen evidence, not absent behavior. The command surface exposes shell-invoked operations and a reader protocol; the inspected hook/mod registrations do not supply a separate semantic memory-admission service independent of ingest (SRC-1: `src/main.go`, `hooks/hooks.json`, `mods/kgai-mod/hooks/register.tsx`, `src/cmd/kgread/server.go`).

## Core ideas

1. **Reasons and graph authority have different consumers.** Natural-language decision titles/rationales inform a later model or human. Symbolic mutations, attachment and supersession determine the graph's current state and which reasons count as heads. Hash integrity establishes neither the truth of a rationale nor the legitimacy of a remote author's engineering choice. See [MEM-OBJ-decision](#mem-obj-decision), [MEM-OBJ-event](#mem-obj-event), [RT-RTE-team-sync](runtime.md#rt-rte-team-sync).
2. **Ordinary recall is deliberately narrower than retained history.** Context selects elements using paths, lexical scores and recency, then includes only current authority heads, up to four per element, with shortened rationale. Superseded and provenance-only decisions may help select the element without appearing in its delivered `why`. Full history is a separate demand read, not guaranteed context. See [MEM-RTE-context-recall](#mem-rte-context-recall), [MEM-RTE-search-history](#mem-rte-search-history).
3. **Capture extracts decisions, not a resumable task transcript.** The foreground model or optional fork turns task experience into title, rationale and mutations; only admitted events are durable decision memory. The optional fork's entire answer is not returned to the foreground transcript, and compact tool rendering is a human display transformation. The host's actual copied fork context is unspecified. See [RT-RTE-fork-capture](runtime.md#rt-rte-fork-capture) and its annotation.
4. **Revision changes live authority without erasing reasons.** Retirement removes live edges; new authority decisions supersede existing heads. Dead-end notes can attach without taking authority. Thus retained negative experience need not displace the current recommendation, but its later use requires search/history rather than head-only context. See [MEM-OBJ-graph](#mem-obj-graph) and [RT-RTE-foreground-capture](runtime.md#rt-rte-foreground-capture).

## Shared records

### Components

#### MEM-CMP-host-smoke
Label: Host smoke evaluator

Source-native identity: `tests/host-smoke.sh`. Representational form: symbolic shell evaluator and JSON/count parsing; storage substrate: shipped script and its prospective per-run files (`out.txt`, `err.txt`, `rc`, hook logs and store). Distinct from [RT-RTE-foreground-capture](runtime.md#rt-rte-foreground-capture): this is an evaluator of capture presence, not its producer. SRC-1 implementation: `tests/host-smoke.sh`, `src/internal/engine/reads.go`.

The evaluator inspects `doctor`'s decision count after a structural or trivial task. It expects one or zero respectively, and prints hook/host diagnostics. A passing count does not judge rationale truth, attachment relevance, later recall or downstream behavior. Its attempt to collect titles uses empty-text search, but `scoreDocs` returns no hits for no query tokens; this display is not a dependable inventory (SRC-1: `src/internal/engine/search.go`, `src/internal/engine/reads.go`). No execution results are supplied. Nothing in the inspected verdict code submits evaluation results as new decision memory.

> want=1; [ "$TASK_TYPE" = trivial ] && want=0
> verdict=FAIL
> [ "$decisions" = "$want" ] && verdict=ok
> --- `tests/host-smoke.sh`

### Operative objects

#### MEM-OBJ-decision
Label: Decision title and rationale

Source-native identity: `Decision.Title`, `Decision.Rationale`, with caller references and author/date provenance. Representational form: natural language for model/human interpretation; `refs` and author labels supply attribution, not executable permission. Storage substrate: fields within `log/<installId>.ndjson`, projected into Kuzu decision nodes and reader Go structures. Lineage: model/human/API-supplied text, optionally extracted by a model from task work; reasons are not reconstructed by replay. Initial authorship and truth remain caller-dependent. The rationale can be empty; the engine requires a title, not a justification or test record. SRC-1: `src/internal/event/event.go`, `src/internal/engine/engine.go`.

This is a distinct retained content part used across [RT-RTE-foreground-capture](runtime.md#rt-rte-foreground-capture), [RT-RTE-fork-capture](runtime.md#rt-rte-fork-capture) and [RT-RTE-editor-read](runtime.md#rt-rte-editor-read), not a duplicate of their route identities. It is not the shipped policy [RT-OBJ-knowledge-graph](runtime.md#rt-obj-knowledge-graph). The content and its symbolic envelope [MEM-OBJ-event](#mem-obj-event) share storage but differ in authority and consumer rules.

> Title:     di.Title,
> Rationale: di.Rationale,
> --- `src/internal/engine/engine.go`

Consumers: context/search receive shortened rationale; history and editor decision detail receive full rationale; arbitrary query may select it. Delivery informs future work under [RT-BAP-decision-recall](runtime.md#rt-bap-decision-recall), but does not itself enforce source-code choices. Reasons remain retained after supersession; default head recall can omit them. See [MEM-RTE-context-recall](#mem-rte-context-recall), [MEM-RTE-search-history](#mem-rte-search-history).

#### MEM-OBJ-event
Label: Event identity and decision mutation envelope

Source-native identity: `Event` and the symbolic fields of `Decision`: IDs, hashes, actor/install, Lamport/recorded time, parents, mutations, shapes, targets, supersession and `ProvenanceOnly`. Representational form: symbolic JSON consumed deterministically, not a parametric embedding. Storage substrate: append-only per-install NDJSON shards; canonical replay orders by Lamport then hash. Lineage: engine reference resolution and authority computation plus store-assigned metadata/hash around caller proposals. Distinct from the reasons in [MEM-OBJ-decision](#mem-obj-decision); closest supplied records are [RT-RTE-foreground-capture](runtime.md#rt-rte-foreground-capture) and [RT-RTE-team-sync](runtime.md#rt-rte-team-sync), which transport/admit these objects rather than identify the retained envelope. SRC-1: `src/internal/event/event.go`, `src/internal/store/store.go`, `src/internal/engine/engine.go`.

> ev.InstallID = s.Config.InstallID
> ev.Actor = s.Config.Actor
> --- `src/internal/store/store.go`

> d.Supersedes = sortedKeys(supSet)
> d.Shapes = sortedKeys(shapes)
> d.Targets = sortedKeys(targets)
> --- `src/internal/engine/engine.go`

`Shapes` records provenance; `Targets` determines authority. A link governs its `from` element, not automatically its `to`; bare upsert of an existing element is provenance-only unless other changes take authority. Decision ID hashes normalized title/author, rationale and mutations, excluding supersession and other event metadata. Event hash covers the enclosing event. These are integrity/dedup identities, not signatures authenticating human permission. A repeated identical decision is an ingest no-op when already projected. The persisted event is already derived engineering memory, not a raw transcript; the model's full trace and deliberation are not fields of this schema. Consumers include engine replay, sync validation, as-of reconstruction and the reader, with different gates. See [RT-RTE-team-sync](runtime.md#rt-rte-team-sync), [RT-RTE-editor-read](runtime.md#rt-rte-editor-read), [MEM-RTE-asof-recall](#mem-rte-asof-recall).

#### MEM-OBJ-graph
Label: Live element graph and projected decision history

Source-native identity: `graph.kuzu` and its `Element`, `Decision`, `LINK`, `SHAPES`, `SUPERSEDES`, `_Applied` tables; the reader separately builds `replay.Projection` in Go maps. Representational form: symbolic structural state plus the separately assessed natural-language fields in [MEM-OBJ-decision](#mem-obj-decision). Storage substrate: rebuildable Kuzu files, or transient reader maps. Lineage: ordered event application from [MEM-OBJ-event](#mem-obj-event), not an independent source of justification. Its distinct identity is the projection, not the invocation routes [RT-RTE-query-read](runtime.md#rt-rte-query-read) or [RT-RTE-editor-read](runtime.md#rt-rte-editor-read). SRC-1: `src/internal/graph/graph.go`, `src/internal/replay/projection.go`, `src/internal/store/store.go`.

> case event.MutRetireLink:
> delete(p.Links, LinkKey(m.FromID, m.LinkKind, m.ToID))
> p.RetiredLinks++
> --- `src/internal/replay/projection.go`

Current edges/properties govern structural query answers; head predicates govern default rationale selection and conflicts. Retirement changes this live view, not the event history. Rebuild deletes derived Kuzu state and replays the log. Engine replay verifies event hash and decision ID; reader replay deduplicates by event hash without doing those verification checks. Projection presence therefore does not establish uniformly validated content across consumers. `Export` emits structural state, decision ID/title/Lamport and authority shapes, not full reasons or all provenance; its digest is not a complete content archive (SRC-1: `src/internal/engine/reads.go`, `src/internal/engine/engine.go`; [RT-RTE-editor-read](runtime.md#rt-rte-editor-read)).

#### MEM-OBJ-prompt
Label: Configured capture conventions

Source-native identity: `prompt` setting from session/project/global layers. Representational form: natural-language selection/naming requirements interpreted by the foreground model. Storage substrate: `.kgairc`, store-local `kg.config.json` or machine config; selected text is delivered as SessionStart context or via `kg prompt --raw`. Lineage: configuration author supplies text, loader selects the effective approved layer, injection bounds and frames it. No automatic derivation from captured decisions is established. Exact initial author/human approval depends on the caller; authorship, approval and file writing are separate. SRC-1: `hooks/inject-prompt.sh`; supplied loader findings in [RT-RTE-config-admission](runtime.md#rt-rte-config-admission).

Part of: [RT-RTE-config-admission](runtime.md#rt-rte-config-admission)

This content object is a material input/output of that configuration route, distinct from the approval registry [RT-OBJ-trusted](runtime.md#rt-obj-trusted). The registry stores access/admission metadata, not the convention text. Static shipped skill policy is a different object [RT-OBJ-knowledge-graph](runtime.md#rt-obj-knowledge-graph).

> max=8000
> if [ "${#prompt}" -gt "$max" ]; then
> --- `hooks/inject-prompt.sh`

Injection truncates the selected shell string at 8000 units as measured by Bash string length; the script labels its limit bytes, but that should not be generalized to a model token budget or encoding-independent byte guarantee. Random framing and surrounding policy restrict intended use to capture conventions, not arbitrary tool authority. Approval makes the text eligible for delivery, not semantically safe or reliably followed. Revocation disables future loading, not necessarily already delivered session text. Re-query through `kg prompt --raw` affords reload; its raw return is distinct from the injection cap. See [RT-RTE-config-admission](runtime.md#rt-rte-config-admission).

### Routes

#### MEM-RTE-context-recall
Label: Bounded element context recall

A later task, explicit ask or model-chosen recall → `Engine.Context` → path/topic/recency scoring → bounded elements with current links/properties → `attachWhy` → CLI JSON → foreground model/user. Code owns selection; caller supplies topic/paths/max; host owns the receiving window and next decision. This standalone read can occur without capture, so it overlaps but is not contained by [RT-RTE-foreground-capture](runtime.md#rt-rte-foreground-capture); it specifies the selection stage within [RT-BAP-decision-recall](runtime.md#rt-bap-decision-recall). SRC-1 implementation: `src/internal/engine/reads.go`, `src/internal/engine/search.go`; doctrine/design: `commands/kg-ask.md`, `skills/knowledge-graph/SKILL.md`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Selected elements, links, props, score, head `why`, and shown/omitted/total counts; errors can prevent delivery.
- Later read-back: Previously admitted decision state/reasons reach a subsequent model invocation through tool JSON; no automatic task-sensitive memory push is implemented by this read itself.
- Delegated visibility: Caller model/human sees JSON; forwarding to host subagents is uninspected — the host controls it.
- Selection predicate: Path overlap adds 10 per matching requested path; about scoring adds weighted element and best attached-decision text matches, plus 0.001 times latest authority Lamport. Filtered results below score 1 are excluded. Default maximum is 15 elements; `why` is only current authority heads, at most four per selected element.
- Invalidation or expiry: New mutations change live state and authority; superseded/provenance-only decisions remain stored but lose or lack default `why` eligibility. Reads do not expire the log.
- Activation or effect: JSON delivery is wired; dependence of later coding choices on these reasons is unobserved. The skill prescribes respect or conscious supersession, not enforced code changes.
- Evidence limits: Count caps are not a global token budget; all links/properties of selected elements can still be large. Historical text can affect element rank without itself reaching the consumer.

> if len(byEl[eid]) >= 4 {
> continue
> }
> --- `src/internal/engine/reads.go`

> Rationale: oneLine(asStr(r["rationale"])),
> --- `src/internal/engine/reads.go`

`oneLine` collapses CR/LF and trims; above 160 bytes it returns the first 157 plus `...`. It can omit scope conditions or rejected alternatives, so full historical rationale must not be inferred from a short context result (SRC-1: `src/internal/engine/reads.go`). Authority and content relevance differ: all attached decisions, including superseded/provenance-only material, feed about ranking. Also, the unbounded Lamport term can reach the filtered inclusion threshold independently of topic/path overlap; “filtered” is not a strict relevance guarantee. The code is the basis for this countercase, not a measured retrieval failure.

#### MEM-RTE-search-history
Label: Search and historical reasons recall

User/model request → lexical ranked search for candidates → caller optionally chooses element and requests History → full decision timeline → caller's subsequent explanation or coding context. Search and History are independently invocable; the shipped ask/history procedures compose them. Code scores/resolves; caller chooses query reformulation and any follow-up. This expands the historical branch of [RT-RTE-foreground-capture](runtime.md#rt-rte-foreground-capture) and [RT-BAP-decision-recall](runtime.md#rt-bap-decision-recall), not a second capture route. SRC-1: `src/internal/engine/reads.go`, `src/internal/engine/search.go`, `commands/kg-history.md`, `commands/kg-ask.md`, `skills/knowledge-graph/SKILL.md`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Search returns up to 20 default ranked element/decision hits, decision IDs/titles, shortened rationale and shaped element names; History returns full rationale/summary, author/time and head markers, or ambiguous-name candidates/error.
- Later read-back: Historical and rejected/superseded reasons can reach later model or human consumers, including unattached decisions through search and full element histories through History. Follow-up execution is prescribed, not guaranteed.
- Delegated visibility: CLI caller receives JSON; command prompt asks the model to present a timeline to the user. Wider propagation remains host-dependent.
- Selection predicate: Search tokenizes, removes stopwords and uses IDF-weighted lexical/fuzzy field matches, then caps hits. History resolves element name/kind/ID, expands explicit ALIAS_OF closure, deduplicates decisions and orders recorded time then Lamport; identical names alone never silently merge histories.
- Invalidation or expiry: Supersession does not remove old search/history content. Live ALIAS_OF changes affect merged history; different same-name facets remain separate. Empty query tokens yield no search hits, not a complete inventory.
- Activation or effect: Retained reasons and rejected approaches are accessible beyond default head recall; actual influence or benefit is unobserved.
- Evidence limits: No semantic embedding selector is implemented in these inspected functions; the skill delegates synonym bridging to the model. Search snippets are shortened, and a caller need not request History. Unattached decisions cannot enter element History; raw query can explicitly retrieve full fields through [RT-RTE-query-read](runtime.md#rt-rte-query-read).

> if len(qToks) == 0 {
> return nil
> }
> --- `src/internal/engine/search.go`

> Rationale: asStr(r["rationale"]),
> --- `src/internal/engine/reads.go`

History's full text contrasts with context/search shortening; neither delivery establishes that an explanation governed action. The appropriate theory/learning limits remain those of [RT-RTE-foreground-capture](runtime.md#rt-rte-foreground-capture), not new learning conclusions derived from retrieval.

#### MEM-RTE-asof-recall
Label: As-of structure reconstruction

Caller timestamp → `Engine.AsOf` reads and sorts retained events → filters by parseable recorded time and event hash → ephemeral Kuzu projection (bulk or incremental) → element names/current links as of cut → CLI caller. Code owns reconstruction; caller selects date. This is a distinct historical structural read, not [RT-RTE-query-read](runtime.md#rt-rte-query-read)'s arbitrary current-graph query. SRC-1: `src/internal/engine/reads.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Cut timestamp, element names and link triples, or error; bare dates mean end of day.
- Later read-back: Earlier retained mutations determine a later invocation's reconstructed shape. Rationale is not included in this return.
- Delegated visibility: JSON to caller/model/human; no automatic forwarding to other sessions.
- Selection predicate: All events at or before the timestamp with parseable RFC3339 time and a valid event hash; canonical replay order. No topic or token budget.
- Invalidation or expiry: Temporary directory is removed after the call; retained events remain. Backdated imports can change a later reconstruction of the same calendar cut.
- Activation or effect: Produces historical structural information; no observed coding behavior dependence.
- Evidence limits: This gate checks event hashes, not the explicit decision-ID recomputation used by engine rebuild. Names/link triples are not a full checkpoint or full decision explanation. Full bulk internals were not independently audited.

> if !ev.Verify() {
> continue
> }
> kept = append(kept, ev)
> --- `src/internal/engine/reads.go`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-foreground-capture](runtime.md#rt-rte-foreground-capture)

Write agency: foreground model interprets current work under structural DO/DON'T rules and proposes [MEM-OBJ-decision](#mem-obj-decision) plus mutations. Human can supply/edit content via CLI; routine automatic capture has no per-content human approval, whereas the explicit decision prompt requests confirmation. Generic API/shell authorship leaves human control unresolved. Engine schema/reference checks veto invalid proposals, not false reasons. Rationale is optional and attachment is warned about rather than enforced. These distinctions are supported by the supplied route's retained passages and direct SRC-1 `src/internal/engine/engine.go` reads.

Curation: reference resolution, kind/name guard, automatic provenance/authority/supersession, generated mutation summary and idempotent admission transform the submission before persistence. These are symbolic transformations, not evidence that the engine criticized its content. The skill requests a consolidated choice and 2–3 sentence why, excluding unacted recommendations and volatile analysis data (SRC-1: `skills/knowledge-graph/SKILL.md`). Resulting event memory is cross-session and potentially cross-install; raw host context remains host-managed. New operative-part records identify that memory without replacing this route.

#### On [RT-RTE-fork-capture](runtime.md#rt-rte-fork-capture)

Trace-fed update: eligible edited foreground work → external host's session fork plus [RT-OBJ-capture-prompt](runtime.md#rt-obj-capture-prompt) → model-generated NONE or decision JSON → parse/dry-run/admission → [MEM-OBJ-event](#mem-obj-event) → later CLI/editor readers. Input origin is mixed task/session/tool experience, but exact copied trace and provenance remain opaque under the host API. The derived record retains the model's proposed rationale and structural changes, not the whole task trace or a verified explanation of the extraction itself. SRC-1: `mods/kgai-mod/hooks/register.tsx`.

The update is automatic in auto mode and headless confirm fallback; supported confirm surfaces give the human Record/Skip over the payload, not content authorship. NONE, parse failure, dry-run failure and Skip do not create an engineering-memory event. Pending proposal is host-session atom state and is cleared on a new prompt; it is not an alternative durable checkpoint. No later recall of skipped raw proposals is established. Engine acceptance and later eligibility establish a trace-to-memory path, not improved future capacity.

Working-context control: host forks isolate the side answer from the foreground transcript; only parsed payload, diagnostics/status or confirmation state escape. Exact fork input/window limit is not specified by kgai. Successful `ToolResult` rendering becomes an empty Box under compact mode, but that hook changes UI output, not demonstrably model input. Its 500-entry ID set is display bookkeeping, not a retained summary budget. Source evidence:

> on('ui.render', { component: 'ToolResult' }, ($, e, next) => {
> if (e.props.isErrored || !compacted.has(e.props.tool_use_id)) {
> return next(e)
> }
> const { Box } = $.ui.resolve(e)
> return <Box />
> })
> --- `mods/kgai-mod/hooks/register.tsx`

This resembles a separate working frame with a selected return, but no pointer in the foreground window automatically reloads the discarded fork answer. Durable selected decisions are reloaded through explicit memory reads, not by resuming that frame.

#### On [RT-RTE-team-sync](runtime.md#rt-rte-team-sync)

Storage/lineage: remote events become local retained shards and graph eligibility, rather than model-authored summaries. Other installations' actor/install metadata and reasons survive as content/provenance. No per-reason human approval is requested by synchronization. Object integrity and own-shard checks from the supplied route govern admission, not source trust in engineering conclusions. Retired-shard reconciliation can rewrite retained envelopes and require rebuild; it is not semantic criticism. Autosync timestamps/errors are local diagnostic state read by later status/control calls, not recalled structural reasons (supplied SRC-1 passages in this route).

#### On [RT-RTE-editor-read](runtime.md#rt-rte-editor-read)

Read-back content: reader rows deliver title/state/author/time; `view.Model.Decision` delivers full rationale, summary, references, mutation descriptions, shaped-element roles, supersedes/superseded-by and installation/event metadata. Thus the editor is a real later human-facing reason consumer, not merely a store API with an unspecified caller. SRC-1: `src/internal/view/view.go`, `src/internal/replay/projection.go`.

> out := &Decision{Row: m.row(d), Rationale: d.Rationale, Summary: d.Summary, Refs: parseRefs(d.Refs),
> --- `src/internal/view/view.go`

Display labels are readable derivations of typed mutations and head predicates, not independent learning or replacement memory. Full reasons remain available in detail despite compact list rows. Protocol filtering and filesystem reload select delivery; no model context injection is established. The supplied integrity difference is confirmed by the direct `replay.Apply` read: deduplication is not event verification. Human interpretation remains unobserved.

#### On [RT-RTE-config-admission](runtime.md#rt-rte-config-admission)

The memory-specific content part is [MEM-OBJ-prompt](#mem-obj-prompt). SessionStart pushes effective conventions without a topic request: trigger is session start, selector is deterministic configuration precedence plus approval lookup, selected part is effective prompt text, channel is plain host context or JSON `additionalContext`, budget is the injection shell-string cap. It does not push decision history. The content persists in configuration; injected copies live in host context under host retention. Config author proposes, local trust caller admits, skill prescribes human consent; the registry proves approval state, not who consented. No evidence that reason capture automatically revises this policy. SRC-1: `hooks/inject-prompt.sh`; supplied settings/trust findings in the route.

## Write side

**Acquisition and admission.** Foreground capture can originate from current work, explicit user decisions or manual/API import. Optional capture extracts from task experience rather than preserving raw traces. In both cases the caller authors natural-language reasons and proposed mutations; the engine resolves and validates symbolic content, and the store stamps/writes the event. Human supply, semantic approval and physical append are different operations. The two supplied capture routes and their annotations retain the mode-specific admission gates. A dry run returns resolution/validation results without appending an event; it is not a semantic quality trial or durable memory candidate. It may still open/initialize derived infrastructure. SRC-1: `src/internal/engine/engine.go`, `src/main.go`; [RT-RTE-foreground-capture](runtime.md#rt-rte-foreground-capture), [RT-RTE-fork-capture](runtime.md#rt-rte-fork-capture).

**Maintenance, rejection and withdrawal.** Invalid mutation operations/references and empty titles can reject ingest. Exact duplicate content is a projected-state no-op; unknown-field rejection belongs to the CLI decoder and is not a universal imported-event check. New authority computes supersession; a dead-end attached through a bare existing-element upsert does not unseat heads. Link retirement changes live structure while preserving its event and reasons. Conflicts expose competing authority heads, not a truth-evaluation score. Skill-directed resolution must take authority again and re-express intended state; bare provenance is insufficient. See [MEM-OBJ-event](#mem-obj-event), [MEM-OBJ-graph](#mem-obj-graph), [RT-RTE-foreground-capture](runtime.md#rt-rte-foreground-capture); SRC-1 `src/internal/engine/engine.go`, `skills/knowledge-graph/SKILL.md`.

The skill says the user can “adjust or retract” a recorded decision. In the inspected dispatch, mutation enum and revision paths, this means corrective subsequent decisions/live-edge changes, not a demonstrated destructive erase API. Old reasons remain in search/history and synced logs; supersession is not confidentiality withdrawal. This is a bounded finding about these surfaces, not a repository-wide assertion that file editing cannot remove anything. SRC-1: `skills/knowledge-graph/SKILL.md`, `src/main.go`, `src/internal/event/event.go`, `src/internal/graph/graph.go`.

**Repair and alternative projections.** Append precedes graph projection; failure can leave an admitted log prefix requiring rebuild rather than an all-or-nothing batch. Rebuild deletes only derived Kuzu state, sorts retained events and filters invalid hashes/decision IDs. At the default threshold of 1000 events, a fresh rebuild uses bulk replay; the reader instead constructs maps without opening Kuzu. These are alternative materializations, not model context checkpoints. The reader and AsOf have weaker/different integrity gates, as the records retain. Malformed JSON lines are skipped by `readShard` before consumers see them; consequently doctor cannot report every skipped malformed line merely by verifying parsed events. SRC-1: `src/internal/store/store.go`, `src/internal/engine/engine.go`, `src/internal/engine/reads.go`, `src/internal/replay/projection.go`; [MEM-OBJ-graph](#mem-obj-graph), [MEM-RTE-asof-recall](#mem-rte-asof-recall).

**Evaluation and retained outcomes.** [MEM-CMP-host-smoke](#mem-cmp-host-smoke) describes artifact-count evaluation; no supplied run supports success. Doctor reports parsed-event hash/local-chain problems and graph counts/conflicts; status is cheaper metadata, not the same integrity evaluation. Export/digest tests structural replay agreement on selected fields, not reason truth. None of these inspected evaluators automatically rewrites rationale, capture conventions or a model. Raw evaluation output is not, by its existence, trace-fed engineering memory. SRC-1: `src/internal/engine/reads.go`, `tests/host-smoke.sh`.

## Read-back

Demand reads have known later consumers: skill/ask/history procedures tell the foreground model to call CLI reads before changes and present reasons; the editor requests retained-log views for humans. [MEM-RTE-context-recall](#mem-rte-context-recall) and [MEM-RTE-search-history](#mem-rte-search-history) distinguish selection from delivery, and full reasons from clipped snippets. [MEM-RTE-asof-recall](#mem-rte-asof-recall) delivers old structure without reasons. Arbitrary query is an additional caller-selected current-graph view, not an automatic recall policy ([RT-RTE-query-read](runtime.md#rt-rte-query-read)). Export's immediate structural return establishes diagnostic capability; no separately wired later memory consumer of an export file was found in these inspected call paths, so no export re-import loop is asserted.

Automatic supply is narrower: SessionStart pushes configured capture conventions and status, Stop pushes a static capture reminder, and synchronization makes remote events locally available. The first is retained authored policy; the second is shipped instruction plus current-turn markers, not recalled prior engineering content; the third changes availability but does not itself deliver a task-relevant rationale to a model. The fork selects a durable extraction from current task work; it does not automatically recall stored history into its copied host context. SRC-1: `hooks/hooks.json`, `hooks/inject-prompt.sh`, `mods/kgai-mod/hooks/register.tsx`; [RT-RTE-foreground-capture](runtime.md#rt-rte-foreground-capture), [RT-RTE-team-sync](runtime.md#rt-rte-team-sync).

The shipped sources here establish selective external-memory reload and side-context isolation, not kgai-owned foreground trimming, resumable session summaries or model parameter revision. Such host/provider mechanisms remain uninspected, not evidenced absences. Actual recall compliance, relevance and behavioral activation remain unobserved; retrieval capacity alone does not establish improved future action.

## Integration issues

- **Qualification of supplied ordinary recall description:** [RT-RTE-foreground-capture](runtime.md#rt-rte-foreground-capture) says historical decisions remain reachable, correctly, but this must not imply all their reasons reach ordinary context. [MEM-RTE-context-recall](#mem-rte-context-recall) establishes four-head caps and byte-shortened text; superseded/provenance-only decision text can influence rank but not be delivered in `why`. Analytical consequence: history availability and delivered explanatory content are separate.
- **Relevance countercase:** the Lamport addition in [MEM-RTE-context-recall](#mem-rte-context-recall) can overcome the filtered threshold without topic/path overlap. SRC-1 `src/internal/engine/reads.go` supports the formula; no execution quantifies its operational effect. Avoid treating filtered context as strict domain targeting.
- **Integrity is consumer-local:** [MEM-RTE-asof-recall](#mem-rte-asof-recall) verifies event hash but not the explicit decision ID check of rebuild; [RT-RTE-editor-read](runtime.md#rt-rte-editor-read) does not perform either verification. SRC-1 `src/internal/engine/reads.go`, `src/internal/engine/engine.go`, `src/internal/replay/projection.go`. This extends rather than contradicts runtime's reader qualification. Doctor sees parsed events, not discarded malformed lines.
- **Policy cap precision:** the supplied [RT-RTE-config-admission](runtime.md#rt-rte-config-admission) correctly calls capture conventions capped; [MEM-OBJ-prompt](#mem-obj-prompt) identifies Bash string length as the actual injection measurement. Locale/encoding-dependent byte behavior is not established; neither is a model token cap. Revocation affects future loads, not proven removal from an existing host window.
- **Retraction scope:** skill/review promises of adjustment/retraction must be interpreted against permanent history and successor authority, not an inspected destructive erase route. [MEM-OBJ-event](#mem-obj-event), [MEM-OBJ-graph](#mem-obj-graph), SRC-1 `skills/knowledge-graph/SKILL.md`, `src/main.go`, `src/internal/event/event.go`. This limits privacy/withdrawal claims without asserting inability to edit storage externally.
- **Potential identity overlap:** the three new read routes detail operations mentioned by [RT-RTE-foreground-capture](runtime.md#rt-rte-foreground-capture) and [RT-BAP-decision-recall](runtime.md#rt-bap-decision-recall), but have standalone callable read identities, not the capture loop's whole identity. New objects distinguish retained reasons, symbolic event envelope, derived graph and configured content; no supplied object declares those exact referents. [MEM-OBJ-prompt](#mem-obj-prompt) is explicitly part of the supplied configuration route. No replacement or supersession is requested.
- **Unresolved integration/operation limits:** exact fork-context selection, host-window management and deployed semantic admission/compliance remain opaque; full bulk-loader equivalence, transport branches and editor rendering are not independently audited here. These prevent universal integrity/context completeness and observed-learning conclusions, not the positive source-grounded routes. See [RT-RTE-fork-capture](runtime.md#rt-rte-fork-capture), [MEM-OBJ-graph](#mem-obj-graph), [RT-RTE-team-sync](runtime.md#rt-rte-team-sync), [RT-RTE-editor-read](runtime.md#rt-rte-editor-read).

## Limitations and checks

The source checkout HEAD was rechecked as `0ac7f1fae4528805c1d5f504c1bfd6cc34ac953b`; its worktree had no reported changes. Method checkout identity was rechecked as `ff452f2f7cf4b88c40b33747df7b987fb5be2f1f`. Mandatory prompt/contracts and supplied member ranges were read completely. Inspection used source reads/searches, not target execution, dependency installation or services. No observed-run or causal-experiment evidence was introduced. Stronger alternative cases were checked against the actual consumers: historical ranking versus head-only delivery, display hiding versus model context, envelope hashes versus semantic trust, and different replay integrity gates.

Validation: `commonplace-run validate-output` on the supplied invocation passed: “Member content check passes; invocation residue not checked.” This is not job acceptance or claim support. The check does not establish analytical completeness, deployed operation or benefit.
