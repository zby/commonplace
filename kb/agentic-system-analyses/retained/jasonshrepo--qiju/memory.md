---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Qiju memory: intentional process records, deterministic tiered retrieval and host-mediated retrospective use."
run-id: AAS-2026-11-08-qiju-1a12c31c13d1-01
source-identity: https://github.com/jasonshrepo/qiju
reviewed-boundary: a5ea9db29262ce7ec514cdc1dc5c5d017a6a3f89
---

# Qiju memory report

## Boundary and evidence

Qiju retains deliberately composed session records, not an automatically captured conversation. This account covers the whole shipped memory loop at SRC-1 commit `a5ea9db29262ce7ec514cdc1dc5c5d017a6a3f89`: capture instructions and admission, tier storage, search/show and alternative renderings, maintenance, repair/import, retrospective guidance and withdrawal. External host windows, platform memories, provider internals and actual skill loading remain outside the inspectable implementation. No session store, execution trace or causal experiment was supplied. Source supports wiring and requested behavior, not exercised recall or improvement.

Direct reads: SRC-1 `src/qiju/schema.py`, `src/qiju/capture.py`, `src/qiju/paths.py`, `src/qiju/storage.py`, `src/qiju/search.py`, `src/qiju/archive.py`, `src/qiju/maintain.py`, `src/qiju/retro_redact.py`, `src/qiju/cleanup.py`; relevant prompt bodies in `src/qiju/init_cmd.py`, redaction transformations in `src/qiju/redact.py`, deduplication in `src/qiju/util.py`, CLI rendering and parser/dispatch in `src/qiju/cli.py`; doctrine in `docs/architecture.md`. Migration, staging guards and remaining installer/update details below rely on supplied runtime findings, not fresh full-file inspection. Those are available source, not access gaps. All newly read paths are within SRC-1. Implementation and doctrine/design are distinguished below.

| Entry point or operation | Source path (SRC-1) | Coverage and limits |
| --- | --- | --- |
| User checkpoint, temp-entry, log; direct body/stdin/library admission | `src/qiju/init_cmd.py`, `src/qiju/capture.py`, `src/qiju/schema.py` | Direct reads plus [RT-RTE-record-capture](runtime.md#rt-rte-record-capture); [MEM-OBJ-body-md](#mem-obj-body-md), [MEM-OBJ-address-metadata](#mem-obj-address-metadata), [MEM-OBJ-staging-record](#mem-obj-staging-record). Human trigger is not per-content approval. |
| Storage reload and archive conversion | `src/qiju/paths.py`, `src/qiju/storage.py`, `src/qiju/archive.py` | Direct reads; shared substrate of all record parts. ID-first merge and archive validation do not establish semantic equivalence. |
| Search, exact show, session ordering, scope/project listing | `src/qiju/search.py`, `src/qiju/cli.py`, `src/qiju/storage.py` | Direct reads; [RT-RTE-record-retrieval](runtime.md#rt-rte-record-retrieval) annotation. No independent unsolicited selector. |
| Summary, IDs, fields, actions alternatives | `src/qiju/cli.py`, `src/qiju/search.py` | Direct reads; [MEM-OBJ-search-descriptors](#mem-obj-search-descriptors), [MEM-OBJ-next-steps](#mem-obj-next-steps). Actions is not a completion-state resolver. |
| Retention and staging cleanup | `src/qiju/maintain.py`, `src/qiju/archive.py`, `src/qiju/staging.py` | Maintenance/archive direct; staging guard supplied by [RT-RTE-store-maintenance](runtime.md#rt-rte-store-maintenance) and [RT-RTE-record-capture](runtime.md#rt-rte-record-capture). No observed fault recovery. |
| Regex/entropy capture redaction; literal retrospective scrub | `src/qiju/redact.py`, `src/qiju/retro_redact.py` | Transformation direct; configuration/allowlist details supplied by [RT-RTE-record-capture](runtime.md#rt-rte-record-capture); [MEM-OBJ-redaction-metadata](#mem-obj-redaction-metadata), [MEM-OBJ-redaction-log](#mem-obj-redaction-log). No privacy-completeness claim. |
| Normalize, retag, legacy import | `src/qiju/migrate.py` | Supplied [RT-RTE-store-migration](runtime.md#rt-rte-store-migration); detailed normalization helpers not independently read, preventing a stronger field-preservation assessment. Imported initial narratives/provenance unknown. |
| Review and optional skill edits | `src/qiju/init_cmd.py` | Direct prompt read; [RT-RTE-skill-review](runtime.md#rt-rte-skill-review) and annotation. Recommendations need not persist and do not themselves update behavior. |
| Init/update instructions | `src/qiju/init_cmd.py`, `src/qiju/update_cmd.py` | Prompt bodies direct; installation/replacement supplied by [RT-RTE-skill-install](runtime.md#rt-rte-skill-install), [RT-OBJ-qiju-skills](runtime.md#rt-obj-qiju-skills). Bundled replacement is not trace-derived revision. |
| Uninstall and explicit purge | `src/qiju/cleanup.py`, `src/qiju/cli.py` | Cleanup direct, confirmation supplied by [RT-CLM-lossless-records](runtime.md#rt-clm-lossless-records). Long/archive removal leaves other copies possible. |
| Hook/tool/service surface | `src/qiju/cli.py`, `src/qiju/init_cmd.py`, `src/qiju/search.py`, `src/qiju/storage.py` | Parser/dispatch and supplied runtime inventory checked against routes: CLI plus importable operations and installed skill instructions; no additional Qiju provider-tool or startup memory-injection route identified here. External host tool registration/discovery uninspected. |

## Core ideas

1. **Process narrative, not a second code copy.** The shipped log skill asks for anchors, decision status and reasons that files do not recover. It asks not to turn rejected/undecided items into plans. This is a model composition request; schema admission cannot verify adherence. The retained narrative can carry reasons across sessions, but does not ensure that later retrieval returns them. See [MEM-OBJ-body-md](#mem-obj-body-md).
2. **Explicit retrieval with optional delayed hydration.** Search selects by fixed metadata/text rules and returns caller-chosen shapes. Summary is timestamp/project/ID/title, not a generated body summary. An omitted body remains reachable by exact ID; default search and direct show bypass the suggested two-phase economy. No token budget, automatic host compaction or Qiju isolated worker frame is implemented by these routes. See the annotation on [RT-RTE-record-retrieval](runtime.md#rt-rte-record-retrieval).
3. **Tier movement is not forgetting.** Short-tier rotation removes a recent copy; long/archive remain normal search inputs. Archives compress storage, not the narrative into a semantic summary. Rewrite, conflicting-ID precedence and purge qualify the lossless label. See [RT-RTE-store-maintenance](runtime.md#rt-rte-store-maintenance), [RT-CLM-lossless-records](runtime.md#rt-clm-lossless-records).
4. **Trust comes from instructions, not factual validation.** The host is instructed to treat records as source of truth, while capture only enforces shape, routing and best-effort redaction. The actual record-to-host channel is [MEM-BAP-record-history](#mem-bap-record-history). Review can derive lessons from this history and propose changed guidance, but there is no automatic promotion or demonstrated beneficial loop.

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-body-md
Label: body_md process narrative

Identity: the record's Markdown process narrative. Representational form: natural language, possibly containing code, file anchors and record references interpreted by a host. Storage substrate: JSON string in project `.qiju/short.jsonl` and user-home `long/<project>.jsonl`; after maintenance, fields in monthly `archive/project=<project>/month=<month>/entries.parquet`. Paths are SRC-1 `src/qiju/paths.py`; storage merge is `src/qiju/storage.py`. These locations apply also to the next four record-field objects below. They are ordinary local files, not embeddings or provider state.

Lineage: external host composes from the current session, according to bundled log instructions; direct callers can supply other content. This is derived intentional history, not a raw transcript by default. Initial caller provenance is not authenticated by `source` or `agent`. The schema accepts a string, including an empty default, without semantic corroboration (SRC-1 `src/qiju/schema.py`, `src/qiju/capture.py`). Write-time redaction can change the text. The requested rationale survives in body_md when actually authored, and full show or default full search can return it. Summary/actions do not return it. Anchors are stored text, not automatic file dereferencing.

> - **Why** — the reasoning not recoverable from the files themselves: why the change,
>        file, or update was made and what constraint or alternative drove it.
> --- `src/qiju/init_cmd.py`

Closest supplied referents: output of [RT-RTE-record-capture](runtime.md#rt-rte-record-capture), input of [RT-RTE-record-retrieval](runtime.md#rt-rte-record-retrieval). Neither declares the retained record as an object. This object is distinct from static [RT-OBJ-qiju-skills](runtime.md#rt-obj-qiju-skills). Later consumers are the answering host and reviewing host, with requested informational authority; actual use is unobserved.

#### MEM-OBJ-next-steps
Label: next_steps retained action text

Identity: list of action strings within each stored record. Representational form: natural-language plans; list structure is symbolic serialization, not an executable scheduler. Storage substrate: the same JSONL/Parquet record tiers as [MEM-OBJ-body-md](#mem-obj-body-md). Lineage: caller/host-authored agreed next steps, then capture redaction. The log instruction rejects model suggestions as agreed plans; code validates a list of strings, not agreement or task completion (SRC-1 `src/qiju/init_cmd.py`, `src/qiju/schema.py`).

Distinct from the full narrative and from [RT-OBJ-qiju-skills](runtime.md#rt-obj-qiju-skills); its closest supplied consumer route is [RT-RTE-record-retrieval](runtime.md#rt-rte-record-retrieval). Full retrieval exposes it and the actions renderer emits unchecked boxes, source date and title. `rollup_next_steps` strips text, collapses whitespace/case for deduplication and keeps the first occurrence in supplied result order. Default search is newest-first, but caller sorting and limits affect this. It does not inspect later body narratives for completion or retraction. Thus the label open next steps is not evidence of current open status.

> key = " ".join(text.split()).casefold()
> --- `src/qiju/search.py`

> print(f'- [ ] {_cell(text)}  (from: {date} "{title}")')
> --- `src/qiju/cli.py`

The actions view omits rationale and exact record ID; title/date can assist another search but are not equivalent to exact-ID hydration. No automatic task execution or delivery compliance is established.

#### MEM-OBJ-search-descriptors
Label: title tags and search_terms

Identity: authored title, category tags and aliases/search terms. Representational form: natural-language descriptors at the host; symbolic strings at exact tag/substring consumers. Storage substrate: record JSONL/Parquet tiers. Lineage: requested host composition, caller alternatives and redaction. These are not automatically inferred embeddings or generated narrative summaries. SRC-1 `src/qiju/schema.py`, `src/qiju/search.py`, `src/qiju/cli.py`, `src/qiju/init_cmd.py`.

Closest supplied route: [RT-RTE-record-retrieval](runtime.md#rt-rte-record-retrieval); no supplied object counterpart. Distinct from addressing metadata below: these describe content and influence matching/candidate assessment. Query text searches title and aliases along with body, plans and host/model strings; tags require every requested tag. Summary prints the stored title without testing whether it adequately represents the omitted body. ID-only output still includes project/title. Thus those smaller views preserve a locator and an authored display description, not a guaranteed complete account of the record.

> print(f"{entry.get('ts', '')} {entry.get('project', '')} {entry.get('id', '')} {entry.get('title', '')}")
> --- `src/qiju/cli.py`

#### MEM-OBJ-address-metadata
Label: Record identity and provenance metadata

Identity: `id`, `ts`, `project`, `source`, `agent`, optional `model`/`model_effort` and schema version. Representational form: symbolic values used by fixed selection/validation rules; their display can also inform host interpretation. Storage substrate: record tiers; project marker `.qiju/config.json` supplies canonical project addressing, not session narrative. Lineage: supplied fields plus capture overrides/defaults and ID generation; optional model metadata remains caller-asserted. Missing/malformed timestamps become current time, so a valid timestamp need not be independently witnessed event time (SRC-1 `src/qiju/capture.py`, `src/qiju/schema.py`, `src/qiju/paths.py`).

> if util.try_parse_iso(entry.get("ts")) is None:
>         entry["ts"] = util.utcish_now_iso()
> --- `src/qiju/capture.py`

Distinct from [MEM-OBJ-search-descriptors](#mem-obj-search-descriptors). Closest supplied routes are [RT-RTE-record-capture](runtime.md#rt-rte-record-capture), [RT-RTE-record-retrieval](runtime.md#rt-rte-record-retrieval), [RT-RTE-store-migration](runtime.md#rt-rte-store-migration). The metadata affects deduplication, scope, filtering and ordering, not authentication or factual endorsement. Generated IDs conventionally encode a session UUID and sequence; arbitrary nonempty explicit IDs remain admissible. Neither the manual source label nor exact-model field proves human authorship or model pinning. Unknown extra keys survive normalization; their original provenance, encoding and downstream interpretation cannot be classified without supplied records. Full JSON can expose them, while the fixed query text and small renderings need not use them.

#### MEM-OBJ-redaction-metadata
Label: Per-record redactions

Identity: record `redactions` list containing dictionaries for capture substitutions and retrospective markers. Representational form: symbolic field/type/offset/placeholder data; preexisting caller dictionaries are not strongly typed beyond dictionary membership. Storage substrate: the record tiers. Lineage: supplied metadata is extended by the redactor, not a complete proof of all sensitive content or all prior edits. SRC-1 `src/qiju/redact.py`, `src/qiju/schema.py`.

> existing = list(result.get("redactions", []))
>     result["redactions"] = existing + all_redactions
> --- `src/qiju/redact.py`

Closest supplied route: [RT-RTE-privacy-repair](runtime.md#rt-rte-privacy-repair), distinct from that operation's separate audit file below. Full retrieval can deliver these dictionaries to the host; `_entry_text` in `src/qiju/search.py` does not query them, and no later decision gate over them appears in inspected search/rendering. Retained placeholders/offsets identify substitutions, not restored secret values or semantic warrants. Retroactive replacement may also change metadata string values, including IDs, while dictionary keys are not traversed as values.

#### MEM-OBJ-redaction-log
Label: redaction_log audit events

Identity: separate `redaction_log.jsonl` under Qiju home. Representational form: symbolic event dictionaries with natural-language caller reason and replacement text. Storage substrate: local JSONL. Lineage: literal scrub creates timestamp/reason/placeholder/counts and changed-path entries, then applies redaction before append; the immediately returned event is not that scrubbed copy. SRC-1 `src/qiju/retro_redact.py`, `src/qiju/paths.py`.

> redacted_event, _ = redact.redact_value(event, "redaction_log")
>         util.append_jsonl(qiju_paths.redaction_log, redacted_event)
>     return event
> --- `src/qiju/retro_redact.py`

Closest supplied referent: [RT-RTE-privacy-repair](runtime.md#rt-rte-privacy-repair), not a duplicate object declaration. This is an operational audit trace, not a derived lesson store. `src/qiju/storage.py` loads short/long/archive records, not this audit; no search/show read-back consumer of audit reasons is wired by those inspected paths. An external manual file reader is possible but no particular later consumer was supplied. Cleanup preserves audit data; that is retention, not learning.

#### MEM-OBJ-staging-record
Label: Temporary entry file

Identity: workspace `.qiju/tmp/` entry written before ingestion. Representational form: JSON with narrative and symbolic metadata, initially empty at allocation. Storage substrate: local file. Lineage: skill instructs the host to Read then Write; direct log can instead read an arbitrary body path or stdin. Capture reads/normalizes/redacts that input before retained admission. SRC-1 `src/qiju/init_cmd.py`, `src/qiju/capture.py`; guarded deletion details are supplied by [RT-RTE-record-capture](runtime.md#rt-rte-record-capture).

> value = json.loads(text)
> --- `src/qiju/capture.py`

Distinct from retained body/metadata objects: staging is a pre-redaction transient source, not a search tier. The immediate consumer is log; failed capture can leave it for retry, while successful guarded cleanup or stale sweep can remove it. No later history-search consumer is wired. A temporary file's existence is not a raw-session capture or a verified record. It can contain sensitive values before admission.

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-record-history
Label: Retained history to external host

Consumer: external answering/reviewing host model. Channel: search/show CLI output from retained narrative, descriptors and action fields. Force: natural-language history/evidence, with the bundled priority instruction asking for source-of-truth treatment. Horizon: later invocations within or across sessions/hosts sharing the filesystem and calling retrieval. SRC-1 `src/qiju/init_cmd.py`, `src/qiju/search.py`, `src/qiju/cli.py`; supporting supplied route [RT-RTE-record-retrieval](runtime.md#rt-rte-record-retrieval).

> Use them as the source of truth for previous session progress, unresolved bugs,
> implementation decisions, next steps, and what actually happened. Platform memories are
> weak background unless the user explicitly verifies them.
> --- `src/qiju/init_cmd.py`

This is distinct from [RT-BAP-host-guidance](runtime.md#rt-bap-host-guidance), whose payload is the installed skill itself. That path supplies the trust instruction; this one supplies use-written history. Material receipt depends on query/format/hydration. A title-only result cannot establish receipt of narrative reasons. Delivery is wired through CLI output, but actual host selection, compliance, changed behavior and improvement remain unobserved. Schema shape and the word verified do not supply a factual oracle.

## Annotations

#### On [RT-RTE-record-capture](runtime.md#rt-rte-record-capture)

Write agency is the host/caller composing content; code normalizes, overwrites routing/source metadata, redacts and admits by schema. Human per-content approval is unresolved for generic direct callers and not wired into the shipped model-authored path. A user initiating capture is not sentence-by-sentence admission. Capture can transform a session account into later behavior-shaping history, but it does not directly ingest raw tool traces or automatically compact the host window. Initial narrative trace origin is host/caller-selected and potentially mixed; source labels alone do not resolve it. [MEM-OBJ-body-md](#mem-obj-body-md) retains requested reasons; [MEM-OBJ-staging-record](#mem-obj-staging-record) does not become a retrieval tier.

#### On [RT-RTE-record-retrieval](runtime.md#rt-rte-record-retrieval)

Read-back is host-requested, not independent unsolicited supply. Trigger: history question or review. Selector inputs: project scope, session, dates, exact metadata, tags, literal/regex terms and sort/limit; retained parts: full dictionary or caller-selected rendering. Delivery: stdout through the external host's tool channel. Budget: caller's record limit and field/format choices, no inspected token-budget controller. Persistence: source records remain; selection itself writes no new memory. Authority: [MEM-BAP-record-history](#mem-bap-record-history).

Storage read-back merges short before long before archive, with first-ID wins. SRC-1 `src/qiju/storage.py`, `src/qiju/util.py`:

> entries.extend(util.read_jsonl(qiju_paths.long_jsonl))
>     entries.extend(read_archive_entries(qiju_paths))
>     return util.stable_unique(entries)
> --- `src/qiju/storage.py`

Working-context control is output selection: omit bodies via summary/IDs/fields, then recover a chosen body through show. This resembles external addressable storage, not a Qiju-managed stack frame: no separate model context is pushed/popped and no accumulated host turns are evicted. No summary replaces current-run state. A record ID is usable through an explicit tool call, not an automatically followed model-window reference. Direct full search can bring all selected bodies at once; limit is optional. Actions performs presentation-level deduplication of [MEM-OBJ-next-steps](#mem-obj-next-steps), not semantic reconciliation. A stale plan can therefore remain visible despite a later body saying it was completed. That is a code-supported risk, not an observed failure.

#### On [RT-RTE-store-maintenance](runtime.md#rt-rte-store-maintenance)

Curation is threshold-controlled placement and deletion of copies, not meaning revision. Short older than 14 days is removed; archival writes retain record dictionaries and then prune long IDs. Retained narratives remain reachable through normal search across tiers. Archive read removes null optional model keys introduced by mixed schemas, a representational adjustment rather than a new lesson. SRC-1 `src/qiju/archive.py`:

> for field in ("model", "model_effort"):
>                 if entry.get(field) is None:
>                     entry.pop(field, None)
> --- `src/qiju/archive.py`

The archived row-count/ID-set check in the supplied record does not verify every field. Invalid timestamps stay in place, not expire. Rotation does not check each short entry has a surviving long/archive copy before pruning it (SRC-1 `src/qiju/maintain.py`); combined with the supplied partial-append failure limit, universal no-loss recovery cannot be inferred. No actual loss was observed.

#### On [RT-RTE-privacy-repair](runtime.md#rt-rte-privacy-repair)

Literal replacement revises retained parts, and subsequent search/show sees the new values. It is caller-selected administrative curation, not content-directed factual criticism. Admission is nonblank input plus deterministic matching, not a human approval queue over every rewritten occurrence. [MEM-OBJ-redaction-log](#mem-obj-redaction-log) keeps the reason separately but the normal retrieval route does not read it. Record redaction metadata is not a full historical diff or automatic rollback. Current short plus all home long/archive are visited; other workspaces' short copies and external host context can retain the old text.

#### On [RT-RTE-skill-review](runtime.md#rt-rte-skill-review)

The requested trace-to-guidance chain is retained session narratives → date-bounded summaries → selected full records → host diagnosis and proposed wording → user-requested targeted skill edits → possible later host loading. This is an afforded transformation, not raw logging alone; the automatic computational part is host-requested interpretation, while the application policy requires user authorization. No supplied actual review or applied text establishes that this chain ran. Narrative reasons can reach the reviewer only on hydration; the summary does not include them. The prompt asks for evidence/why/confidence in recommendations, but it does not wire persistent recommendation storage. Copy-ready imperative wording may omit its supporting rationale when applied. No later rationale reader is guaranteed.

> If the user asks to apply recommendations, edit only the targeted skill files, validate any changed skills, and record the change with Qiju when appropriate.
> --- `src/qiju/init_cmd.py`

This permits a new record of an applied edit, but does not ensure it or establish the next round consumed it. No improved future capacity follows merely from trace-fed guidance proposals.

#### On [RT-OBJ-qiju-skills](runtime.md#rt-obj-qiju-skills)

These start as static bundled method text, not use-written memory. Optional review edits could make a particular installed file a trace-derived behavior-shaping result; actual modified bytes, reasons and loading remain uninspected. Package init/update can independently replace installed content with bundled text and keep backups as supplied by [RT-RTE-skill-install](runtime.md#rt-rte-skill-install); a backup is not evidence the local lesson remains active. Different write/admission mechanisms must not be combined into one autonomous learning loop.

## Write side

The ordinary acquisition path is deliberate host composition into staging, followed by capture. Its content admission is schema/redaction/routing code, separate from model authorship and append I/O. [MEM-OBJ-body-md](#mem-obj-body-md) is derived selected history, [MEM-OBJ-next-steps](#mem-obj-next-steps) plans, and [MEM-OBJ-address-metadata](#mem-obj-address-metadata) selection/provenance assertions. Raw transcripts exist only if deliberately written into a record; Qiju itself does not acquire the host session. The requested decision process includes rejected and undecided alternatives and reasons; actual compliance and completeness are unobserved.

Maintenance changes placement; it does not synthesize distilled knowledge. Regex/entropy capture redaction and literal scrub change content under deterministic rules. These transformations retain metadata but no guarantee of complete semantic history. Explicit IDs reject duplicate copies by skipping append, not by revising the old payload; callers cannot use a changed same-ID body as an ordinary update. See [RT-RTE-record-capture](runtime.md#rt-rte-record-capture). A new record can describe changed decisions, but search/actions does not universally reconcile the old one.

Administrative admission differs by route. Maintain uses fixed thresholds and caller invocation/dry-run; literal scrub uses caller literal/reason and code matching; migration uses explicit mode and mode-specific preflight/deduplication; init/update uses bundled bytes and eligible installation targets. None supplies an expected-answer oracle or factual content endorsement. Legacy import can bypass capture redaction and rebrand content; its initial authorship/trace lineage stays unresolved, even though its later file transformations and consumers are known. This limit follows [RT-RTE-store-migration](runtime.md#rt-rte-store-migration), not an inference from the manual/agent label.

Withdrawal is not one operation. Staging cleanup removes a transient source; short rotation removes a copy; archive movement retains read-back; scrub replaces matched strings; uninstall removes instructions and metadata while preserving records by default. In SRC-1 `src/qiju/cleanup.py`, project cleanup with nonempty short preserves that file but removes other project `.qiju` children, including the marker. Retention therefore does not guarantee unchanged project addressing after uninstall. Explicit purge deletes home long/archive, not all workspace short records or host copies. It does not implement a per-record rejection ledger or factual retraction resolver. Default preservation and purge scope are also bounded in [RT-CLM-lossless-records](runtime.md#rt-clm-lossless-records).

The review chain is the relevant potential trace-fed method update. Its stored input is an authored session account rather than a guaranteed raw execution trace. The model proposes recommendations; policy leaves application to explicit user request, and no durable critique queue or subsequent affected session was supplied. It must stay separate from deterministic package skill refresh. Neither durable history alone nor recommendation production demonstrates learning or self-improvement.

## Read-back

The normal later consumer is the external answering host, reached by requested CLI tool output. The review host is an additional instructed consumer of the same history, not another storage API. Query predicates operate on retained record content and metadata; they are not semantic relevance ranking. The automatic part is code filtering/sorting after a request, not unsolicited context push. Caller/model chooses scope, terms, date range, count and shape. No automatic activation measurement exists in the supplied evidence.

A stored ID enables exact read-back, but IDs-only is not semantic targeting by itself. Targeting comes from query inputs and host choice among candidates. Summary omits body, next steps, tags, reasons and redaction details. Actions exposes retained plans without completion-state analysis or body reasons. Full JSON/show can return those omitted parts and arbitrary extra keys. These delivery differences prevent assuming that a retrieved candidate's entire history reached the host. See [RT-RTE-record-retrieval](runtime.md#rt-rte-record-retrieval) and [MEM-BAP-record-history](#mem-bap-record-history).

There is no Qiju-managed conversation compaction, eviction or worker-frame isolation in the inspected routes. Two-phase retrieval can keep external record bodies out until requested; it cannot remove them from the host after hydration. Budgets are output-shaping controls rather than a measured window budget. The audit and staging files are not read by search/show. Skill backups and migration source backups afford external recovery but no supplied automatic later read-back consumer. Actual provider-held state and external platform-memory cleanup are uninspected, not absent.

## Integration issues

- **No supported correction to a supplied record is required.** The source reads agree with the supplied runtime's trust, capture, retrieval and scope qualifications. This member adds material object identities and memory-specific limits rather than changing route identity.
- **No candidate duplicate after comparison.** The seven MEM objects are retained field parts, audit or staging, while the supplied object is installed skill text. [MEM-BAP-record-history](#mem-bap-record-history) carries use-written records; [RT-BAP-host-guidance](runtime.md#rt-bap-host-guidance) carries the instructions that tell the host how to treat them. The two channels interact but are not identical.
- **Open-action interpretation:** [MEM-OBJ-next-steps](#mem-obj-next-steps) and [RT-RTE-record-retrieval](runtime.md#rt-rte-record-retrieval) establish string rollup, not current task status. No store/trace supplies actual completion/retraction cases. This prevents treating the actions display as verified pending work.
- **Trust and rationale reach:** [MEM-OBJ-body-md](#mem-obj-body-md), [MEM-OBJ-search-descriptors](#mem-obj-search-descriptors), [MEM-BAP-record-history](#mem-bap-record-history) distinguish authored reasons from summaries. No supplied invocation establishes which full bodies the host actually read, so source-of-truth guidance cannot establish informed reliance or factual accuracy.
- **Alternative initial provenance:** [MEM-OBJ-address-metadata](#mem-obj-address-metadata) and [RT-RTE-store-migration](runtime.md#rt-rte-store-migration) leave caller extras and legacy original input unresolved. Known transformations must not be suppressed because original provenance is unknown; no raw-trace-only lineage classification is justified.
- **Recovery and lifecycle:** [RT-RTE-store-maintenance](runtime.md#rt-rte-store-maintenance), [RT-CLM-lossless-records](runtime.md#rt-clm-lossless-records) do not establish field-equivalent archive conversion, guaranteed surviving copies under prior append failure, or unchanged addressing after marker cleanup. Source allows a bounded implementation account, but runtime durability and universal losslessness remain unestablished.
- **Applied method revisions:** [RT-RTE-skill-review](runtime.md#rt-rte-skill-review), [RT-OBJ-qiju-skills](runtime.md#rt-obj-qiju-skills) leave actual applied changes, retained reasons and later consumers unknown. This prevents attributing exercised trace learning, improved capacity or a completed self-improvement loop. It does not negate the afforded recommendation/edit path.

## Limitations and checks

Frozen HEAD was rechecked as `a5ea9db29262ce7ec514cdc1dc5c5d017a6a3f89`. Source identity remains the boundary's SRC-1 repository. Required job, member/peer types, collection, worker rules and records contract were read completely, recovering trailing reads. No target execution, dependencies, models, tests, prior analyses or new sources were used. Consequential countercases checked include default full retrieval versus two-phase guidance, explicit-ID collisions versus revision, actions versus semantic completion, field validation versus factual trust, and short rotation versus guaranteed surviving copies.

Evidence remains source-only. Available migration helper details and external host behavior were not independently inspected beyond the supplied record limits. No actual record content authenticates provenance, validates narrative reasons or proves improvement. Archive serialization and filesystem durability rely on external implementations; no field-equivalence or failure-injection experiment was performed.

Validation: passed using the invocation's role-specific commonplace-validate command; this establishes deterministic content/reference/quotation checks, not semantic acceptance or operational benefit.
