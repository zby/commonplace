---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "deja-vu memory: explicit decisions, trace-mined retrieval state and bounded continuation packets, with distinct historical and standing-instruction consumers."
run-id: AAS-2026-10-14-deja-vu-22137d4d39a5-01
source-identity: "https://github.com/vshulcz/deja-vu"
reviewed-boundary: "4c08fb26ad8a8b8e656a120f06ca4175a7078148"
---

# deja-vu memory report

## Boundary and evidence

This account covers the shipped memory operations inside the supplied whole-system boundary, not the host's inference scheduler. The frozen source is SRC-1 at `4c08fb26ad8a8b8e656a120f06ca4175a7078148`; its identity and evidence layers are registered in [boundary](boundary.md#source-register). HEAD was rechecked against that revision and the source checkout had empty short status. No target code, tests, examples, hosts or providers were executed.

Included are transcript acquisition/indexing, notes and lifecycle corrections, query-independent conventions, trace-mined sidecars, dense embeddings, hook/MCP/CLI read-back, compaction capture, standing-rule distribution, import/export, forgetting and restoration. Raw host stores and external provider state are inputs/dependencies, not evidence of an implemented deja host model. Host context removal, inference, tool execution and actual acceptance of delivered text remain external. Product updating and wiring maintenance are in the system boundary but are not experience-derived memory; their runtime records remain applicable without relabelling them as learning.

Direct source reads added implementation evidence in the paths below. Supplied runtime evidence is distinguished from those reads. Source comments about historical measurements remain attributed reported operation; no scores or benefits are adopted as observations of this run. Available but uninspected variants are not access gaps.

| Entry point or operation | SRC-1 paths and inspection basis | Covering records or unresolved limit |
|---|---|---|
| Frozen CLI dispatcher | Direct: `cmd/deja/main.go`, commands map and forgetting cleanup slices | [MEM-RTE-forget-cleanup](#mem-rte-forget-cleanup), [MEM-RTE-session-recovery](#mem-rte-session-recovery); dispatch also names `view`, `wip`, `files`, `friction`, `secrets`, `tests`, `recap`, `fix`, `how`, `check`, `log`, `share`, `resume`, `handoff`, `sync` and hooks. Naming does not establish every branch's semantics. |
| Registry/transcript admission, full and incremental indexing | Supplied: `internal/sources/registry.go`, `internal/index/ingest.go`; direct: ingest redaction/write/sidecar slices | [RT-OBJ-index-db](runtime.md#rt-obj-index-db), [MEM-OBJ-records](#mem-obj-records), [MEM-OBJ-session-meta](#mem-obj-session-meta). Individual host parsers and compressed/database variants remain uninspected; exact source completeness and per-host import fidelity cannot be asserted. |
| CLI/MCP remember, promotion, correction and exported promotion | Direct: `internal/sources/notes.go`, `cmd/deja/promote.go`, `cmd/deja/mcp.go`; supplied: `cmd/deja/remember.go` | [MEM-OBJ-notes](#mem-obj-notes), [RT-RTE-note-admission](runtime.md#rt-rte-note-admission). Export rendering implementation beyond the traced admission call remains uninspected; no exact exported-format guarantee. |
| Conventions and lifecycle read-back | Direct: `cmd/deja/hook_conventions.go`, `cmd/deja/lifecycle.go`; supplied: `cmd/deja/hook_context.go` | [MEM-RTE-convention-delivery](#mem-rte-convention-delivery), [MEM-OBJ-notes](#mem-obj-notes). Imported accepted notes use index metadata rather than local notes JSONL. |
| Trace-mined fixes and candidate maintenance | Direct: `internal/index/fixpair.go`, ingest build calls, `cmd/deja/fix.go`, `cmd/deja/hook_plan.go` | [MEM-OBJ-fixraw](#mem-obj-fixraw), [MEM-OBJ-fixes](#mem-obj-fixes), [MEM-RTE-trace-mining](#mem-rte-trace-mining). Full incremental repair implementation remains uninspected; no all-update equivalence guarantee. |
| Co-occurrence, commands, failures and session facts | Direct: `internal/index/cooccur.go`, `commands.go`, `commandfails.go`, `sessionfacts.go`, ingest build calls | [MEM-OBJ-cooccur](#mem-obj-cooccur), [MEM-OBJ-commands](#mem-obj-commands), [MEM-OBJ-commandfails](#mem-obj-commandfails), [MEM-OBJ-sessionfacts](#mem-obj-sessionfacts). Detailed retrieval of every table remains uninspected. |
| Requested CLI/MCP recall and semantic reranking | Direct: `cmd/deja/mcp.go` dispatch; supplied: `cmd/deja/main.go`, `embed.go`, `internal/embed/client.go`, `sidecar.go` | [RT-RTE-requested-recall](runtime.md#rt-rte-requested-recall), [RT-RTE-embedding-records](runtime.md#rt-rte-embedding-records), [RT-CMP-embed-client](runtime.md#rt-cmp-embed-client). Exact numerical provenance and provider retention uninspected. |
| MCP resources, orient/how/fix/handoff and prompt dispatch | Direct: `cmd/deja/mcp.go`, `cmd/deja/mcp_resources.go` list/read slices | Resource list selects recent sessions; resource read resolves a URI-derived prefix and reapplies MCP policy. Generic tool routes overlap [RT-RTE-requested-recall](runtime.md#rt-rte-requested-recall). Full resource rendering, prompts/get and mode adapter internals uninspected; no universal framing/budget claim. |
| Startup, prompt, file/tool/failure and spawned-input recall | Supplied: `cmd/deja/hook_context.go`, `hook_prompt.go`, `hook_tool.go`, `hook_spawn.go`, `extensions/pi/index.ts`; direct: hook plan and conventions slices | [RT-RTE-auto-delivery](runtime.md#rt-rte-auto-delivery), [RT-RTE-spawn-context](runtime.md#rt-rte-spawn-context), [MEM-RTE-convention-delivery](#mem-rte-convention-delivery). Other extension and generated installer variants remain uninspected; host parity not established. |
| Plan submission and `check` | Direct: `cmd/deja/hook_plan.go` | [MEM-RTE-trace-mining](#mem-rte-trace-mining): shared plan selector consumes recurrence evidence and confirmed remedies. Full `check` CLI output and admission behavior remain uninspected. |
| Compaction/precompact/catch-up and alternative summary forms | Direct: `cmd/deja/hook_compaction.go`, `internal/index/compaction.go`, `internal/digest/compaction_context.go`, `compaction_carry.go`, `compaction_rules.go`, `internal/sources/compaction_registry.go`; supplied: pi consumer | [MEM-OBJ-compaction-data](#mem-obj-compaction-data), [MEM-OBJ-compaction-state](#mem-obj-compaction-state), [RT-RTE-compaction-recovery](runtime.md#rt-rte-compaction-recovery). Summary role and user-role host summaries are recognized; full host-summary parsers and Antigravity checkpoint-reset integration uninspected. |
| Rules candidate review, source edit and sync | Supplied: `cmd/deja/rules_candidates.go`, `rules.go`, `skills/deja-search/SKILL.md` | [RT-OBJ-rules](runtime.md#rt-obj-rules), [RT-RTE-rules-sync](runtime.md#rt-rte-rules-sync), [RT-BAP-standing-rules](runtime.md#rt-bap-standing-rules). Source edit/approval is prescribed model/user work, not a deja model synthesis call. |
| Forget, tombstones, unforget and secondary cleanup | Direct: `internal/index/privacy.go`, `cmd/deja/main.go`, compaction storage/forget slices; supplied: promotion warnings | [MEM-RTE-forget-cleanup](#mem-rte-forget-cleanup). Tombstone removal/rebuild dispatch is supplied; complete unforget internals and every cache purge remain uninspected, preventing atomic/global erasure claims. |
| Sync admission and peer/export retention | Supplied: `internal/index/sync.go`, `cmd/deja/sync.go`; direct: imported conventions reader | [RT-RTE-import-records](runtime.md#rt-rte-import-records), [MEM-OBJ-session-meta](#mem-obj-session-meta). Full export, relay, watermarks and SSH path uninspected; no remote revocation/security guarantee. |
| Handoff, native resume/write-back and replaced-span restore | Direct: `cmd/deja/handoff.go`, `resume.go`, `resume_writeback.go`, `restore.go`, `internal/index/writeback.go` | [MEM-RTE-session-recovery](#mem-rte-session-recovery). Source-native write-back renderers and full restore-span scanner remain uninspected; no byte-identical reconstruction guarantee. |
| Delivery ledgers, cached digests and usage snapshots | Supplied: hook/cache/usage references; direct: forget snapshot cleanup call and compaction failure/delivery references | Annotations on [RT-RTE-auto-delivery](runtime.md#rt-rte-auto-delivery) and [RT-RTE-compaction-recovery](runtime.md#rt-rte-compaction-recovery). Storage format/rotation and all consumers of usage history remain uninspected; no adaptive ranking from usage is established. |
| Retrieval evaluation and other evaluators | Supplied: `scripts/longmemeval/main.go` | [RT-RTE-retrieval-evaluation](runtime.md#rt-rte-retrieval-evaluation). Other shipped evaluator drivers, bench corpora and retained artifacts uninspected; no score-driven production update established. |
| Stop/deferred, Antigravity, CodeWhale and other specialized hooks | Dispatcher direct: `cmd/deja/main.go`; available paths include `cmd/deja/hook_deferred.go`, `hook_antigravity_prompt.go` | Uninspected included alternatives. Their queue/checkpoint semantics and admission/read-back chains remain unresolved; ordinary pi/Go findings do not stand in for them. |

## Core ideas

1. **The index is a derivative, not the source of every retained decision.** Explicit notes reload from JSONL; indexed historical text is normalized/redacted/clipped. Sidecars retain counts, associations, commands and outcomes rather than a complete transcript. Compaction data live in the index directory but are deliberately not searchable records. Different parts therefore have different reconstruction and forgetting semantics ([MEM-OBJ-notes](#mem-obj-notes), [MEM-OBJ-records](#mem-obj-records), [MEM-OBJ-compaction-data](#mem-obj-compaction-data)).
2. **Memory is both requested and independently supplied.** Queries/prefixes request history; startup conventions arrive without a topical query. Prompt/file/error/plan events select history using current-task signals. Retained state is not inherently useful context: ranking, project policy, novelty, framing and byte budgets determine what the later consumer receives ([RT-RTE-requested-recall](runtime.md#rt-rte-requested-recall), [RT-RTE-auto-delivery](runtime.md#rt-rte-auto-delivery), [MEM-RTE-convention-delivery](#mem-rte-convention-delivery)).
3. **A lifecycle mark affects consumers differently.** Accepted conventions exclude withdrawn states. Historical recall can still show the transcript, with a rejection/replacement/staleness annotation; rejection also has a demotion mechanism. Local marks cannot retract peer copies. The distinction prevents equating “rejected” with deletion or global loss of authority ([MEM-OBJ-notes](#mem-obj-notes), [MEM-RTE-forget-cleanup](#mem-rte-forget-cleanup)).
4. **Automatic trace transformation has substantive gates but not a truth oracle.** Fix mining retains sequence-and-outcome evidence, holds weak sightings, and judges them by term relation, corrected/substitute commands or repetition. Requested fixes can still return labelled unconfirmed candidates. Plan remedy delivery rejects candidates. Thus “candidate” is not a universal never-delivered state ([MEM-RTE-trace-mining](#mem-rte-trace-mining)).
5. **Continuation preserves selected evidence, not the host window.** Fixed extraction carries objectives, conclusions, commands/outcomes, constraints and unresolved work across compactions, with provenance and repository fingerprints. It neither reconstructs all reasoning nor chooses what the host discards ([MEM-OBJ-compaction-data](#mem-obj-compaction-data), [RT-RTE-compaction-recovery](runtime.md#rt-rte-compaction-recovery)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-notes
Label: Explicit and promoted notes JSONL

Identity: `sources.NotesFile()` and its plain/promoted JSONL rows. This is the retained input of [RT-RTE-note-admission](runtime.md#rt-rte-note-admission), not another declaration of that route or the derived index. Natural-language note text/title and symbolic project, timestamps, tags, source-session and lifecycle fields share a local filesystem file. Local caller text can be human- or model-authored; exact authorship is not encoded by the API. Promotion either uses `--note` or deterministic session distillation. SRC-1, `internal/sources/notes.go`, `cmd/deja/promote.go`.

Plain notes reload as project/day sessions. Promoted notes reload by source-session identity, append corrections, reverse messages newest-first and track the latest display state. The separate promoted-note loader keeps the latest row per source for conventions/conflict surfacing. Evidence time can differ from filing time; that matters for retrieval ordering. Tags are topical metadata, not warrants.

> // One session per promoted source session; corrections append as
> // further messages and the title tracks the latest state.
> --- `internal/sources/notes.go`

> if strings.HasPrefix(key, "promoted\x00") && len(s.Messages) > 1 {
> 			reverseMessages(s.Messages)
> 		}
> --- `internal/sources/notes.go`

Write admission is structural validation plus caller choice and filesystem permission; no semantic approval gate requires a human per note. Exact re-promotions can be skipped. Topic conflict surfacing is advisory and occurs after writing; overlap is not automatically resolved. Reasons persist only if supplied text/distilled content contains them, not as a required criticism schema. Later recall/context can read that prose; convention rendering usually reduces it to the first sentence. Historical hits receive lifecycle annotations through local or imported state lookup, not only a query matching the correction's words (SRC-1, `cmd/deja/lifecycle.go`; [MEM-RTE-convention-delivery](#mem-rte-convention-delivery)).

> // deja never auto-resolves; it puts the disagreement in front of the user
> // with dates so the human can promote one and supersede the other.
> --- `internal/sources/notes.go`

#### MEM-OBJ-records
Label: Normalized historical text records

Part of: [RT-OBJ-index-db](runtime.md#rt-obj-index-db)

Identity: `Record` rows in the binary record log, with text plus key, source path, role and time. Natural-language historical prose/code reaches model readers through snippets/digests; symbolic identities/roles/times govern fixed retrieval. Local filesystem storage. Lineage is host parser output or reloaded notes/imports, not a full original transcript. Direct ingest writes already-redacted/clipped text and omits empty plumbing; self-recall stripping reduces recursive reinforcement. SRC-1, `internal/index/ingest.go`; parent's quotations cover the normalization/redaction mechanism.

> off, err := rw.write(Record{Key: key, SourcePath: s.Path, Role: msg.Role, Text: text, Time: msg.Time})
> --- `internal/index/ingest.go:1754-1754`

Consumers include search/digest rendering, sidecar builders, session recovery and later agents through those channels. These records are evidence about prior work, not commands automatically executed by deja. Rehydration/write-back must not imply original byte fidelity or restoration of the host's complete action state ([MEM-RTE-session-recovery](#mem-rte-session-recovery)).

#### MEM-OBJ-session-meta
Label: Session metadata and imported lifecycle material

Part of: [RT-OBJ-index-db](runtime.md#rt-obj-index-db)

Identity: manifest/session metadata used by retrieval, imported conventions and lifecycle lookup. Symbolic session IDs, project/origin labels, times, ownership/path/file-state information and lifecycle selectors control fixed code. Natural-language title/lifecycle-note fields are display summaries that can reach models. Local filesystem/gob storage is identified by the supplied index account; exact file layout for every field remains uninspected. SRC-1, `internal/index/ingest.go`, `cmd/deja/hook_conventions.go`, `cmd/deja/lifecycle.go`.

Metadata are derived from parsed/reloaded/imported content; imported origin is not authenticated authorship. Imported conventions consume `LifecycleNote`, falling back to `Title`, rather than assuming local JSONL exists. Display text is not the entire opaque provider payload or original transcript. This part is distinct from text records because fixed selector rules can act on it even without serving the body.

> text := meta.LifecycleNote
> 		if strings.TrimSpace(text) == "" {
> 			text = meta.Title
> 		}
> --- `cmd/deja/hook_conventions.go`

#### MEM-OBJ-fixraw
Label: Per-session fix-mining evidence

Part of: [RT-OBJ-index-db](runtime.md#rt-obj-index-db)

Identity: `fixraw.gob`, retained per-session mined `FixPair` inputs before judging. Symbolic signatures, keys, times and flags associate natural-language error/command/edit strings. Filesystem gob sidecar. Lineage is redacted normalized transcript observations; it is already a mined derivative, not a raw host log despite “raw” in the filename. Update code is its stated consumer, allowing a changed session's contribution to be withdrawn and the served table rejudged. Later models consume the judged table, not this file directly. SRC-1, `internal/index/fixpair.go`, `internal/index/ingest.go`.

> // fixRawFile holds every pair mined from the corpus before judging, one row
> // per session that produced it.
> --- `internal/index/fixpair.go`

> // promotion back. Judged again from this, an update leaves what a rebuild
> // leaves. Read by updates only.
> --- `internal/index/fixpair.go`

That equivalence is design/comment evidence, not verified across the uninspected incremental implementation. Retaining session lineage supports re-evaluation; it does not establish an explanatory reason why a command fixes an error.

#### MEM-OBJ-fixes
Label: Judged fix pairs and held candidates

Part of: [RT-OBJ-index-db](runtime.md#rt-obj-index-db)

Identity: `fixes.gob` containing judged/deduplicated `FixPair` rows, including held candidates. This is distinct from [MEM-OBJ-fixraw](#mem-obj-fixraw): served rows collapse repeated evidence and have separate pair/candidate retention budgets. Symbolic error signatures, candidate/repaired/substitute flags and provenance fields govern selection; error/command/edit text reaches models/humans as historical evidence. Local gob sidecar. SRC-1, `internal/index/fixpair.go`, `cmd/deja/fix.go`.

Lineage is trace mining and fixed judging, not model-generated remedies. Admission and consumers are in [MEM-RTE-trace-mining](#mem-rte-trace-mining). The struct comment says candidates are never served; executable `FixesFor` instead falls back to them when no confirmed pair survives. The renderer labels them “unconfirmed”; plan remedies reject them. Reasons preserved include error, remedy, failing command where available, source/time and judging flags, not full causal explanations or all repeated witnesses.

> if len(out) == 0 {
> 		for _, p := range held {
> --- `internal/index/fixpair.go`

> ran := "ran next"
> 		if p.Candidate {
> --- `cmd/deja/fix.go`

#### MEM-OBJ-cooccur
Label: Trace-derived token neighbor map

Part of: [RT-OBJ-index-db](runtime.md#rt-obj-index-db)

Identity: `cooccur.gob`. Symbolic token associations/count-derived neighborhoods, not dense model weights; local gob filesystem storage. It is derived from per-session distinct informative tokens, document frequency and repeated pairs, with token/neighborhood/session bounds. The source documents regeneration on full rebuild and intentionally stale incremental appends. This is an automatic trace-fed selector input; full rescue consumer implementation remains uninspected, preventing an exact end-to-end query-expansion guarantee. SRC-1, `internal/index/cooccur.go`, `internal/index/ingest.go`. Distinct from [RT-CMP-embed-client](runtime.md#rt-cmp-embed-client): localized token rules, no model call.

> // personal, deterministic, no models. The map regenerates on every full
> // rebuild and is intentionally left stale by incremental appends.
> --- `internal/index/cooccur.go`

#### MEM-OBJ-commands
Label: Recurring command usage table

Part of: [RT-OBJ-index-db](runtime.md#rt-obj-index-db)

Identity: `commands.gob` / `CommandUse` / `ProjectUse`. Symbolic run/session counts, last-use time and per-project/latest-session links summarize natural-language command strings. Local gob sidecar derived from prior transcript commands. More than one session is the kept-practice threshold; table/text/project caps constrain retained scope. Fixed code can retrieve a linked session's settled decision; model-facing `how`/tool pathways interpret returned commands, not execute the table. The supplied auto/request routes cover broad delivery; exact behavior of every command-table caller remains uninspected. SRC-1, `internal/index/commands.go`, `internal/index/ingest.go`, supplied `cmd/deja/hook_tool.go`.

> // LastSession is the key of the newest session in this project that ran the
> // command, so a caller can reach what that session settled — SessionMeta
> // carries it — without ranking candidates and loading whole sessions.
> --- `internal/index/commands.go`

The count encodes recurrence, not endorsement or correctness. Per-project splits permit filtering both counts and recency; a globally aggregated date would not be equivalent evidence.

#### MEM-OBJ-commandfails
Label: Command failure warning table and update evidence

Part of: [RT-OBJ-index-db](runtime.md#rt-obj-index-db)

Identity: `commandfails.gob` / `CommandFailure`, with `commandfails-state.gob` retaining update state. Symbolic normalized command heads, session counts and projects determine warnings; natural-language failure lines are rendered evidence. Local gob sidecars derived from transcript commands/outcomes. The table requires two sessions and caps at 500 entries. Command shape matching is deliberately broader than command endorsement. SRC-1, `internal/index/commandfails.go`, `internal/index/ingest.go`.

> // commandFailsMax bounds the table. It is read whole on the per-action
> // hook, which fires before every tool call an agent makes.
> --- `internal/index/commandfails.go`

> // commandFailAcc gathers the failures command shapes have ended in, session by
> // session. Per session so an update can take back what a replaced session
> // held and read only that session again, rather than every output in the
> // index (#4288). Exported fields: it is also the state kept between updates.
> --- `internal/index/commandfails.go`

The update consumer and warning consumer have different authority: one regenerates selector state, the other offers evidence before action. Complete incremental invalidation of the private update part remains uninspected; no all-edit equivalence or warning accuracy claim follows.

#### MEM-OBJ-sessionfacts
Label: Bounded recorded commands and outcomes per session

Part of: [RT-OBJ-index-db](runtime.md#rt-obj-index-db)

Identity: `sessionfacts.gob` / `SessionFact` / `SessionCommand`. Natural-language command strings plus symbolic known/exit flags, keyed by session, in a local gob file. Transcript-derived, bounded to four recent commands per session and 40,000 sessions. Fixed code distinguishes a recorded run from a known zero exit. Later display consumers can describe recorded checks without scanning the entire log; exact set of downstream renderers remains uninspected. SRC-1, `internal/index/sessionfacts.go`, `internal/index/ingest.go`.

> func (c SessionCommand) Passed() bool { return c.Known && c.Exit == 0 }
> --- `internal/index/sessionfacts.go`

This records an outcome, not whether the check establishes overall task correctness. The part is distinct from recurring aggregate tables: it can retain one session's latest commands and missing-outcome uncertainty.

#### MEM-OBJ-compaction-data
Label: Extracted continuation content

Part of: [RT-OBJ-index-db](runtime.md#rt-obj-index-db)

Identity: `CompactionState.Data`, a `model.CompactionContext` retained only in `manifest.gob`. Natural-language objective/goal, standing constraints, conclusions, tests, gaps/conflicts and carry lines have symbolic provenance and recorded-outcome fields. Local filesystem storage. This is a material non-searchable part of the index container, distinct from [MEM-OBJ-records](#mem-obj-records). SRC-1, `internal/index/compaction.go`, `internal/digest/compaction_context.go`, `compaction_carry.go`, `compaction_rules.go`, `cmd/deja/hook_compaction.go`.

> // session in one workspace. The packet is stored in manifest.gob only; it is
> // never turned into a synthetic searchable session or a record-log row.
> --- `internal/index/compaction.go`

Lineage: fixed extraction from normalized host messages, plus previous carry/rules/goal where the truncated input no longer reaches their source. The extractor's ordinary window defaults to 64 records/32 KiB/eight items; scans have separate bounds. Host summary-role or recognized user-role summaries mark the carry segment boundary. Standing constraints come from selected user turns, not every pasted “never”; commands pair with recorded outcomes. Carry has finite age/count/text limits, not literal immortality until closure.

> data.Carry = digest.ExtractCarry(transcript.Session.Messages, prev)
> --- `cmd/deja/hook_compaction.go`

> return m.Role == sources.RoleSummary ||
> 		(m.Role == "user" && IsCompactionSummary(strings.TrimSpace(m.Text)))
> --- `internal/digest/compaction_carry.go`

The storage pass redacts and bounds content again. Later capture reads prior rules/carry, and recovery rendering passes selected material to the model within a 4 KiB hook budget. Provenance is retained, but source transcript context/reasons can be omitted or clipped; an assistant “conclusion” is recorded prose, not an independently validated conclusion. The host decides actual window deletion. See [RT-RTE-compaction-recovery](runtime.md#rt-rte-compaction-recovery).

#### MEM-OBJ-compaction-state
Label: Continuation identity and freshness metadata

Part of: [RT-OBJ-index-db](runtime.md#rt-obj-index-db)

Identity: `CompactionState` fields outside `Data`: session/harness/workspace, source path/digest/header/boundary fingerprints, sizes/times, capture revision and last tool-call ID. Symbolic fixed-rule metadata in local `manifest.gob`; distinct from the natural-language continuation payload. SRC-1, `internal/index/compaction.go`, `cmd/deja/hook_compaction.go`.

The metadata select one session/workspace packet and coordinate duplicate/old-capture rejection, revalidation and delivery tokens. They are not readable summaries of an opaque model state. Source fingerprints establish source identity/change signals, not semantic correctness. A duplicate source digest keeps revision; mismatch in harness identity or older snapshot can reject admission. Storage caps complete packets at 24 KiB and retains at most 32 states. Recovery warns about Git changes instead of proving continued validity.

> if next.SourceDigest != "" && next.SourceDigest == current.SourceDigest {
> 			return current, nil
> 		}
> --- `internal/index/compaction.go`

### Routes

#### MEM-RTE-convention-delivery
Label: Query-independent accepted decision delivery

This is a material selector branch of startup delivery, not a replacement for the entire host route.

Part of: [RT-RTE-auto-delivery](runtime.md#rt-rte-auto-delivery)

Startup code requests `projectConventions(allowedNames, 6, 800)`. Fixed Go selects local latest promoted rows plus imported accepted metadata, scoped to the current project and automatic policy for imported reads. It sorts newest-first, deduplicates display lines, and returns a bounded convention block for the enclosing digest/cache/host channel. SRC-1, `cmd/deja/hook_conventions.go`, supplied `cmd/deja/hook_context.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Convention block or empty string to the startup digest builder.
- Later read-back: Latest accepted notes and imported lifecycle summaries reach later startup invocations, without a topical query.
- Delegated visibility: Foreground startup channel via the enclosing host route; automatic child inheritance is not established.
- Selection predicate: Project membership, accepted latest state, origin policy on imported metadata, recency, display-line deduplication, count and byte budgets.
- Invalidation or expiry: Non-accepted latest states are excluded on rebuild of the block; the enclosing digest cache may serve an older matching entry, so immediate withdrawal of all cached text is not established.
- Activation or effect: Directive-bearing reminders enter host-facing history; changed decisions or user override behavior unobserved.
- Evidence limits: Local notes and imported metadata use different read paths; host loading, cache revocation and obedience are not observed.

The selector's output is the first sentence or shortened decision text, not a complete rationale. Comparison/admission mode here is fixed selection, not content approval: note writers supplied the state/content earlier, software chooses what fits now, and the model/user can disregard/override it downstream. Answer oracle: inapplicable — accepted is a caller-chosen lifecycle state, not a gold answer.

> b.WriteString("standing decisions in this project (promoted and still accepted — follow them unless the user overrides):\n")
> --- `cmd/deja/hook_conventions.go`

> // reminder of what was decided, not the reasoning, which recall_context carries.
> --- `cmd/deja/hook_conventions.go`

#### MEM-RTE-trace-mining
Label: Trace evidence admission and later remedy delivery

No supplied route accounts for the distinct automatic raw-to-judged fix update and its candidate gates. It shares transcript inputs with [RT-OBJ-index-db](runtime.md#rt-obj-index-db) and delivery channels with [RT-RTE-requested-recall](runtime.md#rt-rte-requested-recall) and [RT-RTE-auto-delivery](runtime.md#rt-rte-auto-delivery), but is not identical to any of them.

Index build calls fixed mining/judging functions after transcript redaction. For fixes, the producer extracts error/next-command-or-edit sequence and outcome evidence; judging sets candidate flags, deduplicates and bounds rows. Per-session pre-judgment evidence persists separately for subsequent re-evaluation. Later `FixesFor` matches error signatures, excludes self-failure/irreversible remedies, applies origin/ignore filters and returns confirmed pairs first; only if none survive does it return held sightings. SRC-1, `internal/index/ingest.go`, `internal/index/fixpair.go`, `cmd/deja/fix.go`, `cmd/deja/hook_plan.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Sidecar files on build; requested fix output or advisory history on a later matching request/event, not an executed repair.
- Later read-back: Derived error/remedy rows shape later CLI/MCP fix and automatic plan-remedy selection; per-session evidence shapes future judging.
- Delegated visibility: Returned text reaches the invoking reader or host hook context; no separate child result propagation is established.
- Selection predicate: Error signatures, relation/repaired/substitute evidence or permitted repetition, candidate state, policy/ignore checks and destructive-remedy exclusion; plan remedy additionally rejects candidates.
- Invalidation or expiry: Rejudging can withdraw changed-session contributions; pair and candidate counts are bounded separately. Full incremental equivalence remains uninspected.
- Activation or effect: New derived retrieval/advisory material is retained and later served; successful fixes or improved future capacity are not demonstrated.
- Evidence limits: Sequence, silence and repetition are heuristic evidence, not causal identification; source-native measurements are reported operation only. Detailed non-fix sidecar consumers have separate coverage limits.

Admission mode: automatic transformation of accumulated trace inputs. Computational proposer: miner. Computational decider: fixed judge/filter/storage code. Human contribution: users may choose rebuilding, edit sources or forget sessions, but no per-pair approval is required; original transcript authors may be models or users. Veto: structural/source filters, evidence gates, storage errors and later consumer/user refusal. Answer oracle: inapplicable — recorded outcome and absence of recurrence are not an independent expected-answer provider. Rejection can hold a candidate rather than delete it; rollback/recovery uses retained per-session evidence, rebuild and forgetting. The guidance is fixed extraction/judging logic, not a retained explanatory theory automatically criticized by a model.

> p.Candidate = !selfEvidentPair(p) && (!repetitionConfirms(p) || repeats[fixKey(p)] < 2)
> --- `internal/index/fixpair.go`

> if len(fixes) == 0 || fixes[0].Candidate {
> --- `cmd/deja/hook_plan.go`

The trace chain is original command/output/edit messages → normalized/redacted corpus → mined sightings and judged sidecars → signature/plan matching → displayed evidence. Co-occurrence, command practice/failure and session-fact sidecars are other automatic derivatives, assessed under their distinct object records rather than assumed to share the fix judge. Retained evidence gives code selector authority at update/read time, and text offers knowledge to the model. Neither proves behavioral activation or improved capacity.

#### MEM-RTE-forget-cleanup
Label: Local withdrawal and secondary content cleanup

No supplied route declares this local erasure/re-admission-control chain. It affects notes/index/import/recovery objects but is distinct from [RT-RTE-import-records](runtime.md#rt-rte-import-records) and lifecycle admission in [RT-RTE-note-admission](runtime.md#rt-rte-note-admission).

A CLI caller selects session/project/time or dry-run. Fixed code resolves matches, records tombstones before rebuild, removes matching continuation packets and rebuilds without dead sessions. The dispatcher additionally removes matching stored digest snapshots and borrowed promoted titles; explicit promoted-note targeting can remove the note body. SRC-1, `internal/index/privacy.go`, `cmd/deja/main.go`, `internal/index/compaction.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Dry-run counts, removal/tombstone counts and cleanup warnings/errors, or no-match refusal.
- Later read-back: Tombstones block subsequent source/index/import/recovery admission; rebuilding changes future search/sidecars. Unforget can lift suppression and request rebuild.
- Delegated visibility: Local retained/search state changes; existing remote exports and separately retained fork copies are not silently erased.
- Selection predicate: Session exact match preferentially, otherwise supported selector scope; compaction packets share privacy selectors despite not being searchable sessions.
- Invalidation or expiry: Tombstones persist until explicit lifting. Removing suppression cannot recreate a missing raw source or a note body physically removed from JSONL.
- Activation or effect: Future local admission and delivery eligibility change; global erasure, atomic cleanup and actual execution unobserved.
- Evidence limits: Secondary cleanup can report partial failure; full cache purges and unforget internals uninspected. Raw host transcript deletion is not established by index withdrawal.

Admission mode: explicit caller-directed privacy maintenance. Caller proposes scope; code resolves/decides through checks and filesystem operations; user can inspect dry-run/decline invocation. Generic caller identity does not require human approval of each selected row. Answer oracle: inapplicable — identity/scope checks are not truth assessment. Recovery: retry reported failures or explicitly unforget while sources survive. What persists is symbolic suppression plus remaining content, not a semantic correction theory.

> // Persist tombstones before the rebuild: a crash between the two must
> // leave sessions forgotten, not resurrect them on the next index pass.
> --- `internal/index/privacy.go`

> // same reason (#690, #841). The usage log stays — an event is what
> // happened, not what was said (#2325).
> --- `cmd/deja/main.go`

Forgetting a transcript and forgetting its promoted decision are different. Broad project/time withdrawal can suppress the note's index row while keeping authored prose in JSONL; forgetting the source clears its borrowed title, not automatically its decision text. Local lifecycle rejection likewise annotates/demotes history, rather than performing physical deletion. Peer warnings explicitly limit propagation.

#### MEM-RTE-session-recovery
Label: Handoff and retained session restoration

No supplied route separately declares these material alternative consumers. They overlap requested history in [RT-RTE-requested-recall](runtime.md#rt-rte-requested-recall), but additionally deliver a new host prompt or write a native-store file.

CLI `handoff` selects an explicit/newest-project session, applies policy/exclusion checks and packages a 6 KiB digest; print/paste and `--exec` are separate delivery branches. `resume --write-back` reconstructs an absent source-native transcript and adopts its file state before native resumption. `restore` outputs a caller-selected recorded replaced span or writes it to a different destination. These recovery routes share explicit caller control but retain different fidelity limits. SRC-1, `cmd/deja/handoff.go`, `resume.go`, `resume_writeback.go`, `restore.go`, `internal/index/writeback.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Handoff digest, native resume command/execution, transcript write-back status, or listed/output/written recorded span.
- Later read-back: Retained prior session material reaches a new model prompt, native reopened session or recovery reader/file; adopted file metadata guides later incremental ingestion.
- Delegated visibility: Handoff may launch another host with selected prompt text; deja does not define that host's subsequent tools or model decisions.
- Selection predicate: Session prefix/current project for handoff/resume, policy/exclusion checks, missing native transcript and supported renderer for write-back; requested path/span for restore.
- Invalidation or expiry: Write-back refuses existing transcript paths and escapes from store root; restore refuses the original file and existing destination unless forced. Missing inputs/unsupported renderer can prevent recovery.
- Activation or effect: Prompt delivery/file reconstruction/native launcher are wired; successful host continuation and application restoration unobserved.
- Evidence limits: Handoff is a lossy digest; write-back is conversation only, not original tool calls/output; restore is a recorded span, not a complete file. Renderer/scanner variants remain uninspected.

Admission mode: open explicit recovery request. Caller proposes selection/destination; fixed policy/path/existence checks decide whether to write or launch. Human per-content approval is not required. Caller can veto by not invoking execution/write; storage errors/refusal abort. Answer oracle: inapplicable — records and path checks are not expected outcomes. Failed new-file writes are removed in the inspected helper; the native host owns post-launch recovery. Guidance persists as source records and a reconstructed conversation, not a new accepted rule.

> fmt.Fprintf(stderr, "deja: wrote %s back to %s — the conversation only; tool calls and their output stay in deja\n",
> 		short, f.Path)
> --- `cmd/deja/resume_writeback.go`

> // less. Recorded as read, the next pass sees it unchanged, and once the agent
> // appends to it, reads only what was appended.
> --- `internal/index/writeback.go`

The write-back metadata prevents a thinner reconstruction from immediately replacing richer indexed tool evidence. This is a source-supported countercase to assuming all recovery reconstructs a complete original session.

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-OBJ-index-db](runtime.md#rt-obj-index-db)

Raw trace origin is mixed host user/assistant/command/output/edit content, plus explicit notes and imported history. Physical local storage does not make every contained part the same representational form. Parts declared here distinguish text records, metadata, mined sidecars and continuation data. Admission can retain useful prior corpus data even after native sources disappear; restoration intentionally preserves richer index evidence than its recreated transcript. Full deleted-source preservation/rebuild semantics remain uninspected (SRC-1, `internal/index/ingest.go`, `internal/index/writeback.go`).

#### On [RT-CMP-embed-client](runtime.md#rt-cmp-embed-client)

Numerical sidecar outputs are dense retained representations consumed by later similarity code, not natural-language reasons or knowledge directly delivered to the model. They derive from record/query text and an unpinned mutable provider. The component's supplied quotation establishes name/dimension reuse checks, not stable weight provenance. Text hits still require their own activation policy after ranking ([RT-RTE-embedding-records](runtime.md#rt-rte-embedding-records); SRC-1, supplied `internal/embed/sidecar.go`, `cmd/deja/embed.go`). Parameters changing inside the provider remain uninspected; provider retention cannot be inferred from local sidecar storage.

#### On [RT-RTE-auto-delivery](runtime.md#rt-rte-auto-delivery)

Selected retained content is independently pushed on host events. Startup uses project/task files/recency and accepted conventions; prompt and tool/error events use present-request signals and novelty/delivery history. Persisted caches contain rendered text, while ID/digest ledgers are symbolic access/selection metadata. Usage snapshots can retain actually served digest text; event usage logs are separate. None is interchangeable with raw transcript memory (SRC-1, supplied `cmd/deja/hook_context.go`, `hook_prompt.go`, `hook_tool.go`; direct `cmd/deja/main.go` snapshot cleanup).

The selector has working-context authority over what deja supplies, not the entire host window. It can omit self lineage, children where alternatives exist, old/unrelated material, repeated deliveries and policy-hidden origins. Stale cache service and recorded-before-output tool tokens limit both freshness and exactly-once receipt claims. The complete pi consumer was supplied, not reread independently; all-host propagation is unestablished.

#### On [RT-RTE-note-admission](runtime.md#rt-rte-note-admission)

[MEM-OBJ-notes](#mem-obj-notes) supplies reload and curation detail. MCP's successful append precedes its nonblocking search admission; a later index error can occur after the note is on disk. Promotion changes lifecycle by appending, not replacing the raw session. User-authored/requested rationale may remain readable through context, while automatic convention reminders reduce it. SRC-1, direct `cmd/deja/mcp.go`, `cmd/deja/promote.go`, `internal/sources/notes.go`.

#### On [RT-RTE-compaction-recovery](runtime.md#rt-rte-compaction-recovery)

Raw-to-derived chain: normalized transcript → fixed context/rule/carry extraction and command outcome pairing → redacted bounded `Data` plus symbolic capture metadata → exact session/workspace recovery selector → freshness-aware framed packet → later host/model invocation. Previous carry/rules/goal can feed the next capture. This is retained memory within a session as well as across process invocations; it does not require a new project/session to qualify (SRC-1, `cmd/deja/hook_compaction.go`, `internal/index/compaction.go`, `internal/digest/compaction_context.go`).

Alternative source forms include parser-native summary records and recognized user-role host summary text. The registry fallback calls the registered source parser and matches native session identity, yielding no byte offsets and `MetricComplete: false`; thus ordinary recovery capacity can coexist with unavailable compaction-to-edit metrics (SRC-1, `internal/sources/compaction_registry.go`). Full variant parsers remain uninspected. Host removal is opaque; only selected extracted state remains reachable through deja. The window is copied text, not a by-reference object with heap-style liveness.

#### On [RT-RTE-spawn-context](runtime.md#rt-rte-spawn-context)

Selected indexed history crosses into the rewritten child instruction field; it does not imply the parent's full memory window is shared. Parent-plus-prompt-hash reader identity separates dedupe, not model permissions. The host owns the isolated context/frame and return value; no inspected deja route restores the child's entire internal window to the parent. SRC-1, supplied `cmd/deja/hook_spawn.go` and `hook_tool.go`.

#### On [RT-OBJ-rules](runtime.md#rt-obj-rules)

The source text is authored/adopted instruction material, distinct from extracted compaction `Rules` and promoted conventions despite similar names. Its content/rationale schema is unrestricted natural language; the sync command requires structural marker/size validity, not a criticism record. The prescribed correction-candidate workflow can yield human-approved prose rules without preserving the rationale in the source file. Later host loaders read the marked rule copies, not the original candidate listing as such. SRC-1, supplied `cmd/deja/rules.go`, `rules_candidates.go`, `skills/deja-search/SKILL.md`.

#### On [RT-BAP-recall-reference](runtime.md#rt-bap-recall-reference)

Automatic convention prose says to follow accepted decisions, then crosses the enclosing framed-history channel. Its effective authority is therefore still model interpretation, not a fixed permission gate. Reducing a decision to its first sentence can drop rationale/scope qualifications. This sharpens the supplied tension between rule-priority doctrine and untrusted-history framing; it does not prove either is obeyed (SRC-1, `cmd/deja/hook_conventions.go`; supplied framing quotation in this record).

## Write side

**Acquisition and raw trace.** The host creates transcripts; deja registry/parser/index code discovers, parses and admits derivatives. Original host generation and actual transcript completeness remain external. Raw text retention alone is not an automatic experience-derived update. The trace-mined sidecars and compaction packet are the qualifying transformations with durable later consumers, under their particular limits ([MEM-RTE-trace-mining](#mem-rte-trace-mining), [MEM-OBJ-compaction-data](#mem-obj-compaction-data)). Fixed normalization/redaction/clipping remove or change retained bytes; these are not automatically semantic criticism.

**Explicit decisions and maintenance.** CLI/MCP writers admit caller-chosen note content with structural rather than truth validation. Promotion records source identity, state and optional text/tags, appends real corrections, and reports overlap without blocking admission. Rules candidates instead support prescribed model synthesis and human selection before source edit/sync; code copying does not prove that approval happened. Authorship, admission control and physical file writing must remain separate ([RT-RTE-note-admission](runtime.md#rt-rte-note-admission), [MEM-OBJ-notes](#mem-obj-notes), [RT-RTE-rules-sync](runtime.md#rt-rte-rules-sync)).

**Automatic derived memory.** Index builders use sanitized corpus text for postings/sidecars. Fix pairs retain error/remedy/provenance and evidence flags, plus a separate pre-judgment per-session pool that can support taking a judgment back. Counts or flags are not a retained explanation of mechanism. Co-occurrence uses symbolic token association, while embedding produces dense vectors through the unpinned endpoint. Sidecar derivation may be best effort without failing the index build; cache hits can outlive a nominal freshness interval. Neither endpoint success nor benefit is observed ([MEM-RTE-trace-mining](#mem-rte-trace-mining), [MEM-OBJ-cooccur](#mem-obj-cooccur), [RT-RTE-embedding-records](runtime.md#rt-rte-embedding-records)).

**Compaction.** The event-driven writer can reject off/ignored/disallowed input, missing identity, workspace mismatch, busy storage, older captures or forgotten sessions. No human per-packet approval is required. Bounded extraction omits old/tool-heavy material while separately finding objectives/constraints and carrying unresolved items. Storage redacts again and caps complete state. A failed capture records a failure token so an older packet cannot masquerade as the new continuation. Previous packet content can feed a later capture, but original reasons may no longer be in the reachable tail ([MEM-OBJ-compaction-data](#mem-obj-compaction-data), [MEM-OBJ-compaction-state](#mem-obj-compaction-state), [RT-RTE-compaction-recovery](runtime.md#rt-rte-compaction-recovery)).

**Rejection, withdrawal and recovery.** Lifecycle rejection is semantic metadata supplied by the caller; readers annotate/demote the historical decision and conventions omit non-accepted latest states. Forgetting changes local admission through tombstones/rebuild and secondary cleanup, but authored promoted text can deliberately survive source withdrawal. Explicit note deletion, raw transcript survival, already-sent peer copies and fork copies remain separate. File restoration and write-back consume retained data without claiming complete originals ([MEM-RTE-forget-cleanup](#mem-rte-forget-cleanup), [MEM-RTE-session-recovery](#mem-rte-session-recovery)).

**Evaluation.** The supplied LongMemEval route builds temporary haystacks/indexes, scores gold session-ID membership and removes the temporary index. Its inspected result has no automatic production adoption consumer. Other evaluator modes remain uninspected. Evaluation output therefore cannot be silently inserted into a feedback-to-memory-update chain ([RT-RTE-retrieval-evaluation](runtime.md#rt-rte-retrieval-evaluation)).

## Read-back

| Direction and trigger | Selector and retained input | Budget, delivery and actual consumer | Authority and limit |
|---|---|---|---|
| Requested recall/context/browse | Caller query/prefix/URI, project/harness/offset and lexical/semantic ranking; indexed text/metadata/vector sidecar | MCP bounded framed text; CLI text; resource list/read; invoking agent or human | Historical reference; URI identity is targeting, not topical relevance. Shell route can be unframed. Supplied [RT-RTE-requested-recall](runtime.md#rt-rte-requested-recall); direct SRC-1 `cmd/deja/mcp.go`, `cmd/deja/mcp_resources.go`. |
| Independent startup supply | Project/task files/recency/policy and latest accepted conventions; excludes asking lineage | Cached/new digest to host-facing context; six convention lines within 800 bytes before enclosing budget | Directive-bearing history through model interpretation; not guaranteed compliance. [MEM-RTE-convention-delivery](#mem-rte-convention-delivery), [RT-RTE-auto-delivery](runtime.md#rt-rte-auto-delivery). |
| Event-selected prompt/tool/plan/failure supply | Current prompt terms/file/error/plan steps, novelty and delivery metadata; sidecars and prior sessions | Prompt hook budget 1536 bytes; plan framed budget 2048 bytes; other tool budgets remain covered only by supplied account. Foreground context/tool-result text | Fixed selection, not deja action execution. Candidate remedies withheld on plan path. SRC-1 `cmd/deja/hook_prompt.go`, `cmd/deja/hook_plan.go`; [MEM-RTE-trace-mining](#mem-rte-trace-mining). |
| Spawned-input supply | Recognized spawn and first prompt/instructions/task field, synthetic child reader and prompt recall | Appended input text to child host invocation; host owns frame/return | No full-parent-window inheritance or tool grant. [RT-RTE-spawn-context](runtime.md#rt-rte-spawn-context). |
| Compaction continuation | Exact native session/workspace, policy, capture revision, failure/delivery ledgers, freshness | 4 KiB recovery packet, marked delivered only after successful complete stdout write | Reachable extracted state, not host window restoration or host receipt proof. [RT-RTE-compaction-recovery](runtime.md#rt-rte-compaction-recovery). |
| Standing-rule distribution | Explicit edited source and installed-host selection | Marked global instruction-file copies read by future host loaders | Intended standing instruction, distinct from framed recall. Actual loader priority/obedience unobserved. [RT-BAP-standing-rules](runtime.md#rt-bap-standing-rules). |
| Cross-host/session recovery | Explicit/newest project session or path/span; retained session records | 6 KiB handoff prompt; native conversation write-back; recorded-span output/file | Handoff can launch a host, but action authority remains there; recovery is partial. [MEM-RTE-session-recovery](#mem-rte-session-recovery). |
| Update-only read-back | Retained per-session mined evidence and prior packet carry/rules | Fixed code rejudges tables or composes new packet | Retained evidence shapes future selectors before a model sees output; not demonstrated improved capacity. [MEM-OBJ-fixraw](#mem-obj-fixraw), [MEM-OBJ-compaction-data](#mem-obj-compaction-data). |

Compaction resembles discarding an accumulated host frame while leaving a small copied continuation reachable. Spawn input resembles pushing selected inputs into a separate host frame; deja does not own popping it or selecting the return to the parent. The analogy stops at by-value text: IDs and stored packets are lookup keys outside the model window, not live pointers a model can dereference automatically. The known reload routes are explicit context retrieval, recovery hooks, handoff and native resume; none proves by-reference shared memory.

## Integration issues

- **Candidate label contradicted by operative code.** [MEM-OBJ-fixes](#mem-obj-fixes) and [MEM-RTE-trace-mining](#mem-rte-trace-mining) retain the mismatch between the struct comment (“never served”) and actual fallback plus labelled rendering. SRC-1, `internal/index/fixpair.go`, `cmd/deja/fix.go`, `cmd/deja/hook_plan.go`. Consequence: rejection/admission cannot be assigned one system-wide candidate gate. This corrects a source comment, not a supplied runtime fact.
- **No supported correction to the supplied runtime's scoped facts.** Added findings refine it: imported conventions have a metadata path; continuation storage is not searchable; write-back restores only conversation; broad forgetting does not necessarily remove authored note prose. These concern [RT-OBJ-index-db](runtime.md#rt-obj-index-db), [RT-RTE-note-admission](runtime.md#rt-rte-note-admission), [RT-RTE-compaction-recovery](runtime.md#rt-rte-compaction-recovery), with supporting parts/routes declared here. No re-declaration of those referents is intended.
- **Possible overlap, not record duplication by prefix.** [MEM-RTE-session-recovery](#mem-rte-session-recovery) overlaps generic requested recall by input corpus but adds native-store/file/launcher consumers; [MEM-RTE-forget-cleanup](#mem-rte-forget-cleanup) overlaps note/import invalidation but declares the privacy route. [MEM-RTE-trace-mining](#mem-rte-trace-mining) adds a transformation/admission chain, not another ordinary recall route. All object parts and the convention selector use explicit `Part of` relations to the supplied containers/routes. Reconciliation should retain containment rather than supersede valid containers solely because parts exist.
- **Authority tension remains unresolved.** [MEM-RTE-convention-delivery](#mem-rte-convention-delivery) emits imperative reminders and reduces their reasons; [RT-BAP-recall-reference](runtime.md#rt-bap-recall-reference) frames history as untrusted data. No observed consumer evidence resolves whether a model interprets an accepted decision correctly. [RT-BAP-standing-rules](runtime.md#rt-bap-standing-rules) has a different intended instruction channel and must not be conflated with this branch.
- **Included uninspected alternatives remain local limits.** Coverage rows retain missing facts for specialized stop/deferred/checkpoint hooks, other integrations, parser variants, sidecar consumers, full incremental invalidation, export/SSH, usage formats, recovery renderers and evaluator variants. Their consequences are respectively unknown delivery/admission semantics, parity/fidelity, selector fidelity, revocation, adaptive use, reconstruction and evaluation feedback. No universal closure, completeness, atomic erasure or absence finding depends on leaving these parts out.
- **Rationale and latest-state limits.** [MEM-OBJ-notes](#mem-obj-notes) can retain caller reasons, but [MEM-RTE-convention-delivery](#mem-rte-convention-delivery) usually reads a one-line reduction; cached older digests complicate immediate lifecycle revocation. [MEM-OBJ-compaction-data](#mem-obj-compaction-data) preserves selected provenance/outcomes, not complete reasoning. Whether every full-context renderer exposes all surviving reasons remains uninspected; no complete rationale-preservation classification follows.

## Limitations and checks

This is source-grounded architectural wiring, not observed operation or demonstrated benefit. No supplied execution traces establish activation, recovery success, host obedience, durable erasure under real crashes or retrieval improvement. Unpinned providers and external hosts limit lineage and behavioral-authority conclusions without making inspectable local transformations indeterminate. The frozen register is unchanged; all added reads use SRC-1 paths at the pinned checkout. The method contract and report/input types were read completely, including bounded tails.

Load-bearing source comments were challenged against executable consumer paths: candidate serving, non-searchable compaction state, partial write-back, note-surviving forget and cached read-back are retained countercases. No theory-builder, reflection, autonomy or self-improvement conclusion is inferred from storage, a rule filename, evaluation presence or trace-derived revision alone.

Validation: the invocation-specific deterministic content and relation check passed after quotation attribution repairs. It establishes form, identities and quotation occurrence, not analytical correctness or acceptance.
