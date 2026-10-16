---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Smriti MCP memory: caller-authored Markdown, raw trace review, lexical recall and use-reinforced access metadata."
run-id: AAS-2026-10-14-smriti-mcp-14f6928f9817-01
source-identity: "https://github.com/Deepak-Bhardwaj-PS/smriti-mcp"
reviewed-boundary: "8264bf9103477d9521e57b27c81dcc2e943a3230"
---

# Smriti MCP memory report

## Boundary and evidence

This member covers the shipped durable-note, trace, recall and maintenance mechanisms at the revision registered as SRC-1 in [boundary](boundary.md). The enclosing agent decides what is worth retaining, authors consolidated prose and decides whether returned text enters its next prompt. Smriti owns deterministic file, metadata, ranking and formatting operations, not that enclosing decision loop. External host implementation, production memories and observed execution are unavailable; that prevents conclusions about actual model consumption or benefit, not source-wired storage and selection.

Direct reads covered all of `src/smriti_mcp/store.py`, `src/smriti_mcp/server.py`, `src/smriti_mcp/cli.py`, `src/smriti_mcp/frontmatter.py` and `src/smriti_mcp/fix_frontmatter.py`. Focused reads covered the library examples in `README.md`, maintenance/user workflows in `QUICKSTART.md` and trace/recall/consolidation/health tests in `tests/test_smriti_store.py`. These are implementation and doctrine/design evidence, not observed runs. The supplied runtime additionally covers package dispatch and the stdio integration test. No target code was executed.

| Entry point or memory operation | SRC-1 source path | Coverage and conclusion limit |
|---|---|---|
| CLI server, fix-frontmatter, rebuild; MCP registrations | `src/smriti_mcp/cli.py`, `src/smriti_mcp/server.py` | Direct reads confirm the supplied [RT-RTE-store-maintenance](runtime.md#rt-rte-store-maintenance) and tool routes; no shipped host hook or recall scheduler is registered here. Host scheduling remains external. |
| Create, append, update, remember; direct library writes and raw-file reload | `src/smriti_mcp/store.py`, `src/smriti_mcp/frontmatter.py`, `README.md` | [RT-RTE-memory-write](runtime.md#rt-rte-memory-write), [MEM-OBJ-memory-body](#mem-obj-memory-body), [MEM-OBJ-memory-meta](#mem-obj-memory-meta); direct reads. Filesystem admission differs from API admission. |
| Archive, delete, supersede | `src/smriti_mcp/store.py` | [RT-RTE-memory-write](runtime.md#rt-rte-memory-write); direct reads traced preserved historical content and optional reason, without automatic undo. |
| List, search, get, recall; snippets and graph expansion | `src/smriti_mcp/store.py`, `src/smriti_mcp/server.py` | [RT-RTE-context-recall](runtime.md#rt-rte-context-recall) annotation; direct reads. Requested delivery is wired; external prompt insertion uninspected. |
| Access reinforcement and later affinity ranking | `src/smriti_mcp/store.py` | [MEM-RTE-access-reinforcement](#mem-rte-access-reinforcement); direct reads. Durable numerical access metadata is distinct from prose synthesis. |
| Record/load traces, suggest groups, consolidate | `src/smriti_mcp/store.py`, `src/smriti_mcp/server.py` | [RT-RTE-trace-consolidation](runtime.md#rt-rte-trace-consolidation), [MEM-OBJ-trace-events](#mem-obj-trace-events); direct reads. No factual validation of trace references. |
| Health diagnostics; frontmatter repair; wikilink insertion | `src/smriti_mcp/store.py`, `src/smriti_mcp/fix_frontmatter.py` | [RT-RTE-store-maintenance](runtime.md#rt-rte-store-maintenance) annotation; direct reads. Health returns transient diagnostics, not an automatically applied rejection decision. |
| Build/load Markdown index; write YAML index; fresh in-memory retrieval index | `src/smriti_mcp/store.py` | [MEM-OBJ-markdown-index](#mem-obj-markdown-index), [MEM-OBJ-machine-index](#mem-obj-machine-index); direct reads. YAML persistence does not establish a shipped YAML reload consumer. |
| Shipped library and agent-facing workflow examples; tests | `README.md`, `QUICKSTART.md`, `tests/test_smriti_store.py` | Focused direct reads; doctrine and test intent only. Integration-test behavior additionally supplied by runtime, not independently observed. |

No included opaque provider memory is established: these inspected routes expose text, YAML/JSON and fixed Python selectors. Arbitrary initial file authorship and generic caller identity remain unresolved locally. Dependency internals and external model state are excluded as in boundary; they prevent an end-to-end authority account.

## Core ideas

1. Durable prose and retrieval controls coexist in each Markdown file but have different consumers. The host interprets prose; Smriti interprets metadata, terms and links. A confidence label changes a score without verifying a claim. See [MEM-OBJ-memory-body](#mem-obj-memory-body) and [MEM-OBJ-memory-meta](#mem-obj-memory-meta).
2. Recall is a caller-requested, lossy display of retained notes, not autonomous supply. Code chooses compact snippets, metadata and one-hop wikilink neighbors. Bodies remain recoverable by ID; no owned conversation is trimmed or summarized. See the annotation on [RT-RTE-context-recall](runtime.md#rt-rte-context-recall).
3. Trace review retains raw events, then asks a caller to supply derived prose. By contrast, recall itself automatically updates durable access counters and salience that later ranking consumes. Neither path establishes improved future capacity. See [MEM-OBJ-trace-events](#mem-obj-trace-events) and [MEM-RTE-access-reinforcement](#mem-rte-access-reinforcement).
4. Maintenance changes discoverability and graph reachability, not source truth. Archive and supersession normally suppress recall but preserve alternate retrieval; generated indexes can preserve stale displays until refreshed. See [RT-RTE-store-maintenance](runtime.md#rt-rte-store-maintenance) and [MEM-OBJ-markdown-index](#mem-obj-markdown-index).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-memory-body
Label: MemoryDocument body

Source-native identity: `MemoryDocument.body`, serialized beneath YAML frontmatter in root-relative `.md` files. Representational form: natural-language Markdown for human/model interpretation; embedded wikilinks also have symbolic graph consumers. Storage substrate: local filesystem, reloaded as Python text. Lineage: supplied create/update content, appended observations, caller-supplied consolidation, optional supersession reason and deterministic wikilink rewriting. Initial externally edited file provenance is unresolved. SRC-1, `src/smriti_mcp/frontmatter.py`, `src/smriti_mcp/store.py`.

Closest supplied record is [RT-RTE-memory-write](runtime.md#rt-rte-memory-write), a route producing this object, not the body itself. Its executor is [RT-CMP-memory-store](runtime.md#rt-cmp-memory-store), which is distinct from retained data. Later consumers are full get/search callers and lossy recall callers; ranking separately reads body terms. Reasons persist only when supplied as content; no required rationale field exists. Bodies are readable rather than opaque, but snippets are not a complete display. Authority in Smriti is lexical/graph influence; behavioral instruction force at a later agent is possible but unobserved.

> def get_memory(self, id: str) -> str:
>     return self._load(id).to_markdown()
> --- `src/smriti_mcp/store.py`

#### MEM-OBJ-memory-meta
Label: MemoryDocument metadata

Source-native identity: `MemoryDocument.meta`, the YAML mapping in the same note. Representational form: symbolic fields for fixed code rules, with natural-language title/description values displayed to readers. Substrate: local Markdown frontmatter and transient parsed dictionaries. Lineage includes supplied metadata, deterministic title/description/default/timestamp derivation, repair and access reinforcement. Distinct operative part from [MEM-OBJ-memory-body](#mem-obj-memory-body): replacing prose need not replace controls. Closest supplied [RT-RTE-memory-write](runtime.md#rt-rte-memory-write) produces both; [RT-RTE-context-recall](runtime.md#rt-rte-context-recall) reads these fields rather than declaring their identity. SRC-1, `src/smriti_mcp/store.py`, `src/smriti_mcp/frontmatter.py`.

Code uses title, aliases, tags, descriptions and body terms for ranking; scope/visibility/source-agent are exact-match filters, not authenticated permissions. Status, expiry, confidence, salience and access count change selection. Dates such as `last_verified_at` and references in `sources` are retained assertions, not checked verification results. `related`, `supersedes` and `superseded_by` are retained associations, but one-hop expansion uses body wikilinks/backlinks, not those metadata associations. Retrieval authority is local to the actual field consumer, not implied by names such as semantic or procedural.

> confidence = str(note.get("confidence") or "").lower()
> score += {"high": 1.0, "medium": 0.5, "low": -0.5}.get(confidence, 0.0)
> --- `src/smriti_mcp/store.py`

#### MEM-OBJ-trace-events
Label: Raw trace events

Source-native identity: events from `record_trace`, written to `.smriti/traces/<date>/<agent-or-shared>.ndjson` under the ordinary trace-path construction. Symbolic JSON envelopes hold natural-language `content` and arbitrary metadata; readable raw events are not derived memory prose. The filesystem is persistent substrate. Lineage: caller observations, remembered-content copies after note writes, and generated consolidation bookkeeping. Human/model/application origin is unresolved for generic callers; agent and event-type labels do not authenticate origin. SRC-1, `src/smriti_mcp/store.py`.

Closest supplied [RT-RTE-trace-consolidation](runtime.md#rt-rte-trace-consolidation) declares the production/review route, not this payload. Later consumer `_load_traces` filters by filename-agent, timestamp and exact scope, skips malformed JSON lines, and supplies grouped raw events to the review caller. The grouping heuristic reads content terms, but the caller determines final meaning. Store scanning excludes `.smriti`, so raw traces do not directly enter ordinary note recall. No automatic trace deletion follows consolidation. Trace-path containment limits remain as in [RT-CLM-file-controls](runtime.md#rt-clm-file-controls).

> key = " ".join(terms[:3]) if terms else str(trace.get("type") or "trace")
> group = groups.setdefault(
>     key,
>     {"topic": key, "traces": [], "related_memories": [], "recommendation": "review"},
> )
> group["traces"].append(trace)
> --- `src/smriti_mcp/store.py`

#### MEM-OBJ-markdown-index
Label: Generated Markdown index

Source-native identity: root `index.md` generated by `build_memory_index` and returned by `load_memory_index`. Natural-language titles/descriptions and rendered navigation links are a human/agent display; deterministic grouping and link construction are symbolic production rules. Substrate: filesystem. Lineage: current scanned note summaries, up to 10000 list entries, optionally grouped by category, with descriptions and tags. Closest supplied [RT-RTE-store-maintenance](runtime.md#rt-rte-store-maintenance) is its producing route, not this artifact. SRC-1, `src/smriti_mcp/store.py`, `QUICKSTART.md`.

A later MCP or library caller explicitly loads the saved display; the guide asks users to review it. This is a shipped afforded external consumer role with wired delivery, not observed agent action. Generated content is not new factual criticism or adoption. Index freshness is invocation-controlled; note creation/deletion does not automatically refresh it. Store scanning excludes `index.md`, so stale display text does not itself become a recalled note.

> if refresh or not path.exists():
>     self.build_memory_index()
> return path.read_text(encoding="utf-8")
> --- `src/smriti_mcp/store.py`

#### MEM-OBJ-machine-index
Label: Derived machine index

Source-native identity: `_build_machine_index` dictionaries and their `index.yaml` serialization. Representational form: symbolic note summaries, alias mappings, term frequencies and directed link/backlink mappings. Substrate: transient Python dictionaries for retrieval and a filesystem YAML export. Lineage: current Markdown scan/reload; persisted export omits bodies but retains term counts and metadata. Closest supplied [RT-RTE-context-recall](runtime.md#rt-rte-context-recall) consumes the freshly derived form; [RT-RTE-store-maintenance](runtime.md#rt-rte-store-maintenance) exports the saved form. Distinct from [MEM-OBJ-markdown-index](#mem-obj-markdown-index), with different consumer and freshness semantics. SRC-1, `src/smriti_mcp/store.py`.

Search, recall and health rebuild the transient representation. No YAML loading path is implemented in the directly read store/server/CLI; saved YAML establishes export capacity, not an independent later consumer route. Alias collisions overwrite the mapping according to scan order, whereas link insertion declines ambiguous phrases: these are different admission rules. Ordinary Markdown links are collected as metadata but graph edges for recall are generated from wikilinks. Fixed consumer rules give these fields selector authority, not evidence of note truth.

> for target in note["wikilinks"]:
>     target_id = index["aliases"].get(target.lower(), target)
>     index["links"].setdefault(note_id, []).append(target_id)
>     index["backlinks"].setdefault(target_id, []).append(note_id)
> --- `src/smriti_mcp/store.py`

### Routes

#### MEM-RTE-access-reinforcement
Label: Access reinforcement

Part of: [RT-RTE-context-recall](runtime.md#rt-rte-context-recall)

This route isolates the durable write-back portion of requested recall, also exposed directly by `mark_accessed`. The supplied recall route is a larger read/write container. Trigger: a selected recalled note when `mark_accessed=True`, or an explicit caller request. Producer/decider: fixed Python rules; caller can disable recall marking or withhold the direct call. Input is the selected ID and existing metadata. Persisted result is a new access timestamp, incremented count and salience increased by 0.02 up to 1.0. Later `_memory_affinity_score` reads salience and counts in subsequent search/recall/remember candidate searches. No model authors the numerical update; generic caller identity leaves human initiation unresolved. This is open-request, automatic post-selection admission with no answer oracle or per-update human approval. Invalid IDs/load errors reject the write; restoration or metadata patch is external recovery. Guidance is the tool's declared access-reinforcement purpose, not a correctness judgment. SRC-1, `src/smriti_mcp/store.py`, `src/smriti_mcp/server.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: direct marking returns ID/status/access count; recall returns its selected context after writes, with summaries based on its pre-mark index.
- Later read-back: later file scans obtain changed salience/count; ranking adds salience times 2 and count times 0.05 capped at 2.
- Delegated visibility: inapplicable — no delegated agent frame or worker is created.
- Selection predicate: explicit ID or IDs surviving requested recall ranking, limit and approximate word-budget gate.
- Invalidation or expiry: patches can replace controls, deletion removes them, and salience saturates; no automatic decay is implemented in this update.
- Activation or effect: durable ranking inputs change; a changed selection is possible, not observed. No source-truth or improved-capacity conclusion follows from increased use.
- Evidence limits: implementation only, with no supplied retrieval outcome or causal intervention. A recalled event-type label is not needed; the numerical feedback path does not write a raw trace.

> doc.meta["last_accessed_at"] = _now()
> try:
>     doc.meta["access_count"] = int(doc.meta.get("access_count") or 0) + 1
> except (TypeError, ValueError):
>     doc.meta["access_count"] = 1
> salience = _clamp_float(doc.meta.get("salience"))
> doc.meta["salience"] = min(1.0, (salience if salience is not None else 0.5) + 0.02)
> self._atomic_save(doc)
> --- `src/smriti_mcp/store.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-memory-write](runtime.md#rt-rte-memory-write)

Retained results split into [MEM-OBJ-memory-body](#mem-obj-memory-body) and [MEM-OBJ-memory-meta](#mem-obj-memory-meta). Direct create/update/append permit caller-authored content with shape/path checks, not source assessment. Raw filesystem edits provide alternative initial admission, with no API cleaning; scans tolerate scalar list metadata but skip unparseable or untitled notes. Append preserves prior prose; update replaces it if content is supplied. `remember` append adds an Observation heading but ignores newly supplied metadata; update replaces body without applying its assembled metadata. API-mediated authorship can be human or model; starting a request does not establish per-content human approval. SRC-1, `src/smriti_mcp/store.py`.

Archive keeps text; supersession retains both files and optionally appends a reason to the old one. That reason is reachable through get/search or explicitly included recall, but normally excluded recall does not deliver the superseded body. It is not automatically copied to the new note. Delete removes the note with no owned undo; generated displays and raw traces may still retain stale references/content. These differences prevent a universal withdrawal claim. The supplied route's file guarantees and bounded failures remain intact.

#### On [RT-RTE-context-recall](runtime.md#rt-rte-context-recall)

The selector reloads current notes and derived terms/graph; it operates on caller query, filters, metadata and body content. All positive-score seeds can contribute one-hop neighbors before the top limit; neighbor expansion is not restricted to already budget-selected seeds. Metadata `related` associations do not participate. Returned context contains a title/ID, description when present, status/confidence/source-agent display and at most two three-line body snippets. Full `sources`, verification dates, supersession rationale and complete bodies are not routinely delivered. A source-agent display is not the underlying evidence. SRC-1, `src/smriti_mcp/store.py`.

> snippets = self._snippets(doc.body, query_terms, note)
> lines = [f"- [[{title}]] (`{note_id}`)"]
> --- `src/smriti_mcp/store.py`

The word budget is `max(80, int(token_budget * 0.75))`; it counts summaries rather than all response metadata/headings and admits the first item regardless. After one item, an oversized next item stops selection rather than trying smaller later notes. Request delivery is wired, unsolicited push is not this route. Search can return whole serialized Markdown or omit it; list offers metadata; get reloads full Markdown by ID. These are on-demand re-entry, not a frame/pop or host-window eviction mechanism. `mark_accessed` controls independent durable feedback, assessed in [MEM-RTE-access-reinforcement](#mem-rte-access-reinforcement). No supplied host trace establishes behavioral instruction authority or actual prompt budgeting.

#### On [RT-RTE-trace-consolidation](runtime.md#rt-rte-trace-consolidation)

Raw [MEM-OBJ-trace-events](#mem-obj-trace-events) reach a caller through topic groups plus related note metadata/snippets. Suggestions select groups by event count and maximum salience; related-memory searches do not inherit the trace scope as note filters. The caller reviews and supplies final prose. No deterministic content summary is synthesized by grouping. Create/update retain `trace:<id>` source strings; append retains only supplied body addition, while its separate consolidation event still records trace IDs. Raw and derived results are not transactional. SRC-1, `src/smriti_mcp/store.py`; supplied record retains the append-branch quotation.

> if trace_ids:
>     clean_meta["sources"] = [f"trace:{trace_id}" for trace_id in trace_ids]
> --- `src/smriti_mcp/store.py`

IDs need not resolve to events and need not warrant the prose. The content can retain reasons, but no required criticism/reason transformation or subsequent reason-directed consumer is established. A later get can expose references and complete prose, whereas compact recall often omits them. Trace review is an implemented experience-to-prose affordance with caller synthesis; improved capacity and exercised theory revision remain unestablished independently.

#### On [RT-RTE-store-maintenance](runtime.md#rt-rte-store-maintenance)

Repair deterministically infers missing title/category, adds compatibility/default/display fields and normalizes scalar list fields. It physically writes only when its modification flag is set. Missing initial metadata authority remains unresolved, but known repair operations need not be suppressed by that uncertainty. Invocation admits rule-based changes without per-content approval; dry-run/skip flags withhold writes. Parse failures and I/O failures limit completion. Body text is preserved except serialization whitespace; malformed YAML is not necessarily repaired merely because the tool is called repair. SRC-1, `src/smriti_mcp/fix_frontmatter.py`, `src/smriti_mcp/frontmatter.py`.

Wikilink insertion changes retained text and graph reachability from title/alias matches, longest-first, rejecting ambiguous/self targets and protecting code/existing links. It preserves display text where canonical targets differ. No supporting reason for an inserted association is retained beyond the deterministic matching rule; later recall consumes the association as graph adjacency. Health reports duplicates, staleness, oversize and unresolved links without admitting rejection or deleting memories. Diagnostics remain transient unless the external caller retains them. Index refresh derives displays/exports; no semantic claim correction follows from regenerated indexes. The supplied record already retains repair's hidden-path and dry-run limits.

## Write side

The retained pathways are ordinary caller prose/metadata writes, raw trace appends, caller-authored consolidation, automatic access reinforcement, and invoked deterministic maintenance. Each has a different admission mechanism: API shape/path and branch checks; accepted event envelope; selected consolidation mode; selected recall IDs or explicit access request; and repair/link rules after invocation. Human versus model authorship is unresolved for generic requests. Only the numerical reinforcement and maintenance transformations are automatic at these update points, not autonomous semantic criticism. SRC-1, `src/smriti_mcp/store.py`, `src/smriti_mcp/server.py`, `src/smriti_mcp/fix_frontmatter.py`; see the route annotations and [MEM-RTE-access-reinforcement](#mem-rte-access-reinforcement).

The raw-to-derived chain is event → filtered group → external review/content → note → get/search/compact recall. Provenance is retained unevenly across consolidation branches; caller reasoning can persist in prose but is not mandatory. Lower-level writes bypass trace recording entirely. Alternative retained forms are raw NDJSON, consolidated Markdown, metadata controls and generated indexes, not automatic checkpoints of a model conversation. Rejection/withdrawal retain different results: withheld calls leave nothing new, API errors may leave earlier composite effects, archive/supersession preserve notes, delete removes one file, health only reports. No automatic pruning of trace evidence follows note withdrawal.

## Read-back

Requested retrieval dominates: callers ask for ID reload, metadata browsing, ranked search, recall, grouped traces or generated index load. Code selects and formats retained material; the external caller owns eventual model injection. Compact recall preferentially leaves whole bodies out, preserving IDs and filesystem copies for explicit get. Search's `include_content=False` likewise omits complete content without removing it from durable storage. These mechanisms control response supply, not an accumulated host conversation. Storage capability is not confused with consumption: persisted YAML has no inspected reload route, whereas Markdown index load and trace grouping have explicit later consumers. SRC-1, `src/smriti_mcp/store.py`, `src/smriti_mcp/server.py`; see [MEM-OBJ-machine-index](#mem-obj-machine-index), [MEM-OBJ-markdown-index](#mem-obj-markdown-index) and route annotations.

Ranking trusts caller-controlled metadata only as selector inputs. It does not authenticate author/visibility or verify confidence. Expiry penalizes rather than evicts; archive/supersession are recall defaults with overrides, not universal read denial. A later caller can explicitly request historical content and rationale. Access feedback may bias later selections even when no semantic content changes. No actual compliance or downstream benefit is established by these channels.

## Integration issues

- No correction to a supplied runtime finding is required. New objects are retained payloads produced/consumed by supplied routes, not duplicate route/executor identities. [MEM-RTE-access-reinforcement](#mem-rte-access-reinforcement) is explicitly a part of [RT-RTE-context-recall](runtime.md#rt-rte-context-recall), with an additional direct trigger. No possible duplicate remains after this comparison.
- Documentation contradicts the create branch on derived descriptions. `README.md` says remember leaves an omitted summary omitted; `RememberMetaInput` likewise says Smriti does not derive it. But remember's create branch delegates to create, which derives a 160-character collapsed-body prefix. This changes lineage/display interpretation for [MEM-OBJ-memory-meta](#mem-obj-memory-meta), not the supplied runtime route. SRC-1, `README.md`, `src/smriti_mcp/server.py`, `src/smriti_mcp/store.py`.

> If `short_description` is omitted,
> Smriti leaves it omitted instead of deriving a partial summary from the body.
> --- `README.md`

> if not meta.get("description") and not meta.get("short_description"):
>     summary = self._short_description_from_content(content)
>     meta["description"] = summary
>     meta["short_description"] = summary
> --- `src/smriti_mcp/store.py`

- `related` is described as an explicit association beyond wikilinks in `src/smriti_mcp/server.py`, but direct inspection finds graph expansion consuming only wikilinks/backlinks. Retained association metadata in [MEM-OBJ-memory-meta](#mem-obj-memory-meta) therefore has no established recall expansion force. Do not infer a second traversal mechanism from its label.
- Unresolved generic caller identity, initial externally edited file provenance and external host context consumption prevent claims of per-content human approval, authenticated experience origin or exercised behavioral authority. They concern [RT-RTE-memory-write](runtime.md#rt-rte-memory-write), [RT-RTE-trace-consolidation](runtime.md#rt-rte-trace-consolidation) and [RT-RTE-context-recall](runtime.md#rt-rte-context-recall). Source implementation supports bounded mechanisms without resolving these facts; no peer member is needed to complete this report.

## Limitations and checks

The checkout HEAD recheck returned `8264bf9103477d9521e57b27c81dcc2e943a3230` and status was clean. Findings use SRC-1 only, distinguish direct reads from supplied passages, and keep source implementation separate from observed operation. Instruction, type, collection and record-contract inputs were read completely. No external source, target execution, prior characterization or autonomous worker was used.

No supplied memory corpus, host trace, retrieval evaluation or causal experiment supports actual activation or task benefit. Implemented maintenance and feedback alone do not establish learning, autonomous reflection or theory-builder iteration. Thin/omitted recall displays prevent assuming that retained reasons or provenance reach every later consumer. Validation: deterministic validate-output passed; this establishes form and quotation occurrence, not semantic acceptance or demonstrated behavior.
