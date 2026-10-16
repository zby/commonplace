---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Gnosis memory: caller-curated repository entries, disposable lexical index, explicit read-back and advisory agent consumption."
run-id: AAS-2026-10-15-gnosis-5bfb42422ce3-01
source-identity: "https://github.com/skorokithakis/gnosis"
reviewed-boundary: "429528bf98e424b40837d2dbe3631d0fb42da6fd"
---

# Gnosis memory report

## Boundary and evidence

This report covers Gnosis's repository-local retained entries, derived search state, embedded selection doctrine and shipped caller instructions at SRC-1 commit `429528bf98e424b40837d2dbe3631d0fb42da6fd`. The source identity and evidence layers are registered in [boundary](boundary.md#source-register). The supplied runtime routes organize the account; their implementation was checked against direct source reads rather than assumed complete.

The included memory boundary spans acquisition, write, body/metadata editing, removal, index refresh/rebuild, search, complete-entry reload and browsing. It includes the external-agent role explicitly instructed by shipped README and AGENTS text. It excludes the host's actual model window, hidden reasoning, session compaction, shell permissions and deployment behavior. Those exclusions prevent claims about what an agent actually remembers, obeys or improves. Local JSONL persistence is implementation evidence; the checked-in corpus is attributed retained content, not an observed session trace. No target commands, tests or examples were executed.

Direct inspection covered full command dispatch, storage and index implementations; write, edit, removal, search, show, latest, topics and reindex commands; plan/review doctrine; README, AGENTS, paths and the complete ten-entry shipped corpus. Added evaluator inspection covered `internal/index/index_test.go` lines 176–258 and `internal/commands/reindex_test.go` lines 90–184. These are test assertions, not observed results. Supplied runtime findings cover author resolution and platform locking helper internals without a new full read here. SRC-1: `cmd/gn/main.go`, `internal/storage/storage.go`, `internal/index/index.go`, `.gnosis/entries.jsonl`.

### Coverage inventory

All paths below are SRC-1 commit-relative. “Direct” means source inspected by this member; “supplied” distinguishes runtime evidence. No included material path was unavailable.

| Entry point or operation | Source path and inspection | Covering records or bounded limit |
|---|---|---|
| Startup instructions, plan/review help | `README.md`, `AGENTS.md`, `internal/doctrine/plan.txt`, `internal/doctrine/review.txt`, `cmd/gn/main.go` — direct | [RT-OBJ-doctrine](runtime.md#rt-obj-doctrine), [RT-RTE-doctrine-delivery](runtime.md#rt-rte-doctrine-delivery), [RT-BAP-agent-guidance](runtime.md#rt-bap-agent-guidance); compliance unobserved |
| Caller admission through positional or piped text | `internal/commands/write.go`, `internal/storage/storage.go` — direct | [RT-RTE-entry-admission](runtime.md#rt-rte-entry-admission), [MEM-OBJ-entry-text](#mem-obj-entry-text), [MEM-OBJ-entry-metadata](#mem-obj-entry-metadata); content's original author/control unresolved |
| Attribution and reference resolution | `internal/commands/author.go`, `internal/commands/resolve.go` — supplied; call sites direct | [RT-RTE-entry-admission](runtime.md#rt-rte-entry-admission); attribution is not origin authentication |
| Editor-buffer and non-interactive replacement | `internal/commands/edit.go` — direct, including final locked validation | [RT-RTE-entry-maintenance](runtime.md#rt-rte-entry-maintenance); metadata changes and body-only edits have different checks |
| Removal and related replacement | `internal/commands/rm.go`, `internal/commands/write.go`, `internal/doctrine/review.txt` — direct | [RT-RTE-entry-maintenance](runtime.md#rt-rte-entry-maintenance); no automatic precedence from a related link |
| Reload, legacy topic normalization, direct JSONL/manual merge path | `internal/storage/storage.go`, `internal/commands/reindex.go` — direct | [MEM-OBJ-entry-metadata](#mem-obj-entry-metadata), [RT-RTE-entry-maintenance](runtime.md#rt-rte-entry-maintenance); external file editors and Git merge decisions unobserved |
| Search and automatic refresh | `internal/commands/search.go`, `internal/index/index.go`, `internal/paths/paths.go` — direct | [RT-RTE-knowledge-read](runtime.md#rt-rte-knowledge-read), [MEM-OBJ-entries-fts](#mem-obj-entries-fts), [MEM-OBJ-metadata](#mem-obj-metadata) |
| Full entry/topic reads, recent browsing, topic counts | `internal/commands/show.go`, `internal/commands/latest.go`, `internal/commands/topics.go` — direct | [RT-RTE-knowledge-read](runtime.md#rt-rte-knowledge-read); complete body versus excerpts/counts distinguished below |
| Forced rebuild | `internal/commands/reindex.go`, `internal/index/index.go` — direct | [RT-RTE-entry-maintenance](runtime.md#rt-rte-entry-maintenance), [MEM-OBJ-entries-fts](#mem-obj-entries-fts); cache recovery does not validate entry meaning |
| Alternative storage operations | `internal/storage/storage.go` — direct; usage search in `cmd/`, `internal/` | Plain Append and Rewrite are capabilities, not additional deployed consumer routes; Append usage found in tests, production dispatch uses AppendNew/Update |
| Hooks, tools and services check | `cmd/gn/main.go` full dispatch; `cmd/`, `internal/`, `AGENTS.md`, `docs/PRODUCT_STRATEGY.md` searched for hooks/MCP, subprocess and storage calls | No additional automatic memory delivery route identified in that inspected surface. Editor subprocess and Git attribution are not an agent scheduler. The external host's registrations are excluded, not proved absent |
| Evaluation and retained examples | `.gnosis/entries.jsonl`, selected freshness/reindex tests above — direct | [MEM-OBJ-entry-text](#mem-obj-entry-text), [MEM-OBJ-entries-fts](#mem-obj-entries-fts); no observed recall quality, semantic evaluation or downstream benefit |

## Core ideas

1. **Preserve reasons that a later agent cannot reconstruct.** Doctrine favors human context and empirical observations over repeatable code analysis, and diverts locally anchored explanations to code comments. This is semantic selection by the caller, not a software truth check. [RT-OBJ-doctrine](runtime.md#rt-obj-doctrine), [RT-RTE-entry-admission](runtime.md#rt-rte-entry-admission). SRC-1: `internal/doctrine/plan.txt`, `internal/doctrine/review.txt`.
2. **Keep the durable corpus separate from disposable access machinery.** Entry prose and structural fields persist together as JSONL, but the FTS projection omits author, related IDs and time. Its freshness metadata controls rebuilding, not evidential warrant. [MEM-OBJ-entry-text](#mem-obj-entry-text), [MEM-OBJ-entry-metadata](#mem-obj-entry-metadata), [MEM-OBJ-entries-fts](#mem-obj-entries-fts), [MEM-OBJ-metadata](#mem-obj-metadata). SRC-1: `internal/storage/storage.go`, `internal/index/index.go`.
3. **Request-driven retrieval bounds output, not the host window.** The caller chooses a query or browse command. Code selects ranked snippets or recent prefixes; full entries remain reloadable. There is no automatic injection established by this source account. Delivery is advisory at the later agent, not a veto on its actions. [RT-RTE-knowledge-read](runtime.md#rt-rte-knowledge-read), [RT-BAP-agent-guidance](runtime.md#rt-bap-agent-guidance). SRC-1: `internal/commands/search.go`, `internal/commands/latest.go`, `internal/commands/show.go`.
4. **Maintenance is explicit, and withdrawal is not uniform across surfaces.** A prose replacement with a related link leaves both records readable. Removal deletes JSONL records, but missing-file refresh and unchanged timestamps can leave stale indexed snippets. Semantic supersession and cache freshness therefore must not be equated. [RT-RTE-entry-maintenance](runtime.md#rt-rte-entry-maintenance), [MEM-OBJ-metadata](#mem-obj-metadata). SRC-1: `internal/commands/rm.go`, `internal/doctrine/review.txt`, `internal/index/index.go`.

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-entry-text
Label: Entry text

Identity: the `Entry.Text` body of each retained knowledge entry. Representational form: natural-language reasons, constraints, rejected alternatives and guidance interpreted by a later coding agent or human. Storage substrate: `text` strings in repository `.gnosis/entries.jsonl`, loaded into Go Entry values, optionally projected into the FTS table and rendered to stdout. This is accumulated content, distinct from static [RT-OBJ-doctrine](runtime.md#rt-obj-doctrine). The closest supplied records are the producer [RT-RTE-entry-admission](runtime.md#rt-rte-entry-admission) and consumer [RT-RTE-knowledge-read](runtime.md#rt-rte-knowledge-read), not duplicate object declarations. SRC-1: `internal/storage/storage.go`, `internal/commands/write.go`, `internal/commands/show.go`.

Lineage: the caller supplies or pipes authored text; write trims it, stores it without a model transformation and later edit replaces it. Doctrine asks the caller to extract unreconstructable human/empirical knowledge from a session. The retained body is not a raw conversation log. No original conversation, causal execution trace or authenticated origin accompanies the shipped entries. Attribution strings do not resolve this gap. SRC-1: `internal/commands/write.go`, `internal/commands/edit.go`, `internal/doctrine/review.txt`, `.gnosis/entries.jsonl`.

> Reach for gnosis only when the knowledge originated from the human or from
> empirical observation that isn't reconstructable from the codebase.
> --- `internal/doctrine/review.txt`

Rationale can persist in the body. The shipped corpus includes entry `rpydfz` rejecting an MCP server, with audience, maintenance cost and reconsideration conditions; `bzxhhs` records a platform-support boundary and links to a locking entry. These are retained assertions, not proof of their correctness or downstream use. `show` delivers their complete bodies, whereas a search or latest excerpt can omit the rationale. The intended cross-session authority is advisory knowledge at the external agent; neither JSON parsing nor lexical matching confers semantic authority. SRC-1: `.gnosis/entries.jsonl`, `internal/commands/show.go`, `internal/commands/search.go`, `internal/commands/latest.go`.

#### MEM-OBJ-entry-metadata
Label: Entry metadata

Identity: Entry ID, Topics, Author, Related, CreatedAt and UpdatedAt fields stored alongside text in JSONL. Representational form: symbolic identifiers, category keys, attribution string and timestamps; Author is displayed to a reader but not authenticated by the CLI. Storage substrate: JSONL fields and loaded Go structures. Unlike [MEM-OBJ-entry-text](#mem-obj-entry-text), these fields affect fixed lookup, grouping, sorting and display rules. Closest supplied records are [RT-RTE-entry-admission](runtime.md#rt-rte-entry-admission), [RT-RTE-entry-maintenance](runtime.md#rt-rte-entry-maintenance) and [RT-RTE-knowledge-read](runtime.md#rt-rte-knowledge-read); this object spans those routes rather than being a duplicate or a part of exactly one. SRC-1: `internal/storage/storage.go`, `internal/commands/topics.go`, `internal/commands/show.go`.

Lineage/control: write generates a six-letter ID and UTC times, normalizes/deduplicates topics and resolves related prefixes. Attribution is caller flag or Git identity with an unknown fallback, as established by [RT-RTE-entry-admission](runtime.md#rt-rte-entry-admission). Interactive edit can revise topics and related IDs but not author or creation time through its buffer; body-only edit preserves metadata except UpdatedAt. Legacy topic spelling is normalized on ReadAll without immediately rewriting disk. That is representation normalization, not reasoning revision. SRC-1: `internal/storage/storage.go`, `internal/commands/write.go`, `internal/commands/edit.go`.

> // Normalize topics on read so that legacy JSONL with non-normalized
> // topics self-heals without requiring an explicit migration step.
> --- `internal/storage/storage.go`

Consumers: show uses target length to choose ID-prefix versus normalized-topic lookup; topics aggregates memberships; latest sorts by creation time while displaying update date; search indexes topics but looks up displayed primary topic/date from a separate JSONL read. Related IDs display navigation pointers, not typed supersession, automatic exclusion, traversal or truth priority. Removal warns but preserves dangling references. Metadata has access/organization authority at these code consumers, not approval authority at a later agent. SRC-1: `internal/commands/show.go`, `internal/commands/topics.go`, `internal/commands/latest.go`, `internal/commands/search.go`, `internal/commands/rm.go`.

#### MEM-OBJ-entries-fts
Label: Entries FTS table

Identity: SQLite `entries_fts` table with unindexed entry ID, text and joined topics, using porter/unicode61 tokenization and prefix indexes. Representational form: symbolic lexical search representation over copied natural-language bodies and topic keys; BM25 ranks are retrieval scores, not dense learned parameters or truth scores. Storage substrate: `index.db` under the root-keyed user cache, not alongside the JSONL inside `.gnosis`. Closest supplied records are [RT-RTE-knowledge-read](runtime.md#rt-rte-knowledge-read) and rebuild within [RT-RTE-entry-maintenance](runtime.md#rt-rte-entry-maintenance); neither separately declares this retained projection. SRC-1: `internal/index/index.go`, `internal/paths/paths.go`.

> CREATE VIRTUAL TABLE IF NOT EXISTS entries_fts USING fts5(
> entry_id UNINDEXED,
> text,
> topics,
> tokenize = 'porter unicode61',
> prefix = '2 3 4'
> );
> --- `internal/index/index.go`

Lineage: Rebuild reads JSONL plus its timestamp under a shared store lock, then transactionally replaces the table contents and timestamp metadata. It copies text and space-joined topics; it neither summarizes reasons nor imports original session traces. The later Index.Search invocation consumes this projection, returns matching IDs and at most the requested number of snippets, and the command formats them for the external caller. Full canonical metadata is not in this projection. SRC-1: `internal/index/index.go`, `internal/commands/search.go`.

Search's snippet uses the best matching column, possibly topics, with a 12-token budget. Subsequent command formatting collapses whitespace and highlights matches. This readable display is an excerpt, not an opaque underlying payload or complete retained reasoning. The complete body remains in JSONL and is reachable through show. Test source asserts rebuild-to-search and stale-index replacement, but no supplied run establishes those outcomes or decision improvement. SRC-1: `internal/index/index.go`, `internal/commands/search.go`, `internal/commands/show.go`, `internal/commands/reindex_test.go`.

#### MEM-OBJ-metadata
Label: Index metadata

Identity: SQLite `metadata` table's `mtime` key/value used by EnsureFresh. Representational form: symbolic RFC3339Nano timestamp comparison. Storage substrate: the same cache database as [MEM-OBJ-entries-fts](#mem-obj-entries-fts), with a distinct consumer and invalidation role. The closest supplied account is freshness within [RT-RTE-knowledge-read](runtime.md#rt-rte-knowledge-read), not an existing object declaration. SRC-1: `internal/index/index.go`.

Lineage/authority: Rebuild captures the JSONL mtime with its entry snapshot and commits that value with projected rows. Later search invokes EnsureFresh; equality suppresses rebuild and inequality triggers it. This is access metadata, not retained content, semantic confidence or an expiry date. If the JSONL path is absent, EnsureFresh returns without clearing an existing projection; if contents change with equal mtime, they evade automatic refresh. Forced reindex rebuilds even then, but Open errors can prevent reaching Rebuild. SRC-1: `internal/index/index.go`, `internal/commands/reindex.go`.

> if os.IsNotExist(err) {
> // No JSONL file means nothing to index; the index is trivially fresh.
> return nil
> }
> --- `internal/index/index.go`

The stronger claim that removal always withdraws every later-visible copy is therefore unsupported. A missing JSONL can leave old snippets searchable even while show returns no corresponding entry. A normal successful rm rewrite changes the file, and ordinary refresh can remove the deleted rows; this countercase also prevents describing withdrawal as generally ineffective. SRC-1: `internal/commands/rm.go`, `internal/index/index.go`, `internal/commands/search.go`, `internal/commands/show.go`.

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-OBJ-doctrine](runtime.md#rt-obj-doctrine)

Curation and source trust: plan/review instruct an external agent to omit reconstructable analysis, prefer human context or otherwise unavailable empirical observations, and put locally anchored explanations in comments. This is a requested source-selection policy, not a classifier run by Gnosis. The human's control over each admitted item remains unresolved. The directive to record decisions during work is qualified by the source filter and full review criteria; it is not permission to treat all session reasoning as durable memory. SRC-1: `internal/doctrine/plan.txt`, `internal/doctrine/review.txt`.

> Each entry
> should carry enough context that someone encountering it months later
> understands why it matters without needing the original conversation.
> --- `internal/doctrine/review.txt`

#### On [RT-RTE-entry-admission](runtime.md#rt-rte-entry-admission)

Memory result: [MEM-OBJ-entry-text](#mem-obj-entry-text) and [MEM-OBJ-entry-metadata](#mem-obj-entry-metadata) persist across CLI processes; sharing is requested through version control, not automatic remote replication. The caller authors/selects the prose. Go code performs structural admission and physical append; no per-content human approval follows from a Git author name. Author identity and original observation provenance are independent unknowns. SRC-1: `internal/commands/write.go`, `internal/storage/storage.go`, `internal/doctrine/review.txt`.

Trace-fed scope: doctrine describes a caller-mediated session-to-entry transformation, with reasons ideally retained in prose. The executable write path receives already selected text; it does not itself ingest raw session logs or automatically derive memory from an execution trace. The FTS projection is an automatic transformation of the retained corpus, not a second source of empirical experience. Its later consumer is search; actual agent use of extracted experience remains unobserved. SRC-1: `internal/doctrine/review.txt`, `internal/commands/write.go`, `internal/index/index.go`.

#### On [RT-RTE-entry-maintenance](runtime.md#rt-rte-entry-maintenance)

Curation differs by path. Interactive edit proposes body/topics/related together and validates changed content against the locked store, including excluding self-reference. Non-interactive positional or piped input changes body only; it requires nonempty text but does not revalidate surviving topic/link semantics. Both update UpdatedAt and retain the current author. Changed text can lose earlier rationale; there is no built-in prior-body history. External Git history may preserve it but no restoration execution is supplied. SRC-1: `internal/commands/edit.go`, `internal/storage/storage.go`.

Withdrawal/adoption: review recommends deletion or a new linked explanation. The latter leaves the old entry available to search/show; Related does not carry an executable superseded status. rm removes selected records and warns about incoming references without removing those references. Reindex changes only the access projection. The consequences for stale cache consumers are recorded in [MEM-OBJ-metadata](#mem-obj-metadata). SRC-1: `internal/doctrine/review.txt`, `internal/commands/rm.go`, `internal/commands/reindex.go`.

#### On [RT-RTE-knowledge-read](runtime.md#rt-rte-knowledge-read)

Read-back direction and targeting: a later caller requests delivery, choosing plan-derived keywords, ID prefix, topic or recent browsing. Search code selects matching retained text/topics through a sanitized expression and BM25 order, with default 20 hits and positive caller override. Uppercase OR is instructed to broaden coverage; bare terms become an implicit conjunction. The selector has no captured task state beyond the supplied query. No independent unsolicited push is established. SRC-1: `internal/doctrine/plan.txt`, `internal/commands/search.go`, `internal/index/index.go`.

Budget and persistence: latest selects up to 20 by creation time by default, returns a whitespace-collapsed first 200 runes plus ellipsis, and is not an update-order review feed. Topics supplies names/counts rather than bodies. Show reloads one unique-prefix entry or every exact-normalized-topic match in creation order, with no corresponding result-count or body-snippet cap. Search can excerpt topics instead of the explanatory body. All are stdout delivery, not proof of host-window admission or changed behavior. SRC-1: `internal/commands/latest.go`, `internal/commands/topics.go`, `internal/commands/show.go`, `internal/index/index.go`.

Working-context control: Gnosis limits what enters a requested result, not what is later evicted from an agent's accumulated window. Material omitted by a snippet remains reachable through explicit show; no sub-agent frame, host compaction summary, verbatim tail or checkpoint reload protocol appears in these command implementations. The external host could supply such mechanisms, but its operation is excluded. The classical pointer analogy stops at the printed ID: it enables another CLI request, not automatic dereferencing inside a model window. SRC-1: `cmd/gn/main.go`, `internal/commands/show.go`, `internal/commands/search.go`, `internal/commands/latest.go`.

#### On [RT-BAP-agent-guidance](runtime.md#rt-bap-agent-guidance)

Authority of accumulated material: retained entry bodies reach the external agent as advisory natural language through requested stdout. Doctrine asks it to surface conflict to the user, explicitly allowing that a decision might be stale. Stored reasons can shape later planning if the caller reads and applies them; delivery alone does not establish that dependency. Entry metadata controls code-level access, not the force of a prose instruction on the host. SRC-1: `internal/doctrine/plan.txt`, `internal/commands/show.go`, `internal/commands/search.go`.

## Write side

Acquisition is caller-mediated. Plan asks for immediate recording of decisions before context can be lost; review asks the caller to scan the session and select information unavailable from code/docs. The original session is not retained by these commands. The corpus offers concrete rationale-bearing results but leaves original evidence and human-versus-agent authorship unresolved. This is a durable knowledge-writing affordance, not demonstrated automatic trace learning. [RT-RTE-entry-admission](runtime.md#rt-rte-entry-admission), [MEM-OBJ-entry-text](#mem-obj-entry-text). SRC-1: `internal/doctrine/plan.txt`, `internal/doctrine/review.txt`, `.gnosis/entries.jsonl`.

Admission controls must be separated from physical I/O. The caller can decline a candidate on semantic grounds. Write code rejects malformed/empty text, invalid topics and unresolved related references, then AppendNew generates the ID under its exclusive lock and writes JSONL. These checks do not authenticate origin, check empirical support or enforce the doctrine's relevance filter. The warning for unresolved attribution does not veto admission. The supplied runtime also identifies post-append read failure as a failure without automatic rollback. [RT-RTE-entry-admission](runtime.md#rt-rte-entry-admission). SRC-1: `internal/commands/write.go`, `internal/storage/storage.go`.

Maintenance changes future readable content, not the static binary's doctrine. The caller selects and proposes edits/removal; software checks structure and serializes update I/O. Interactive editor execution is not evidence of per-content human approval because the environment chooses the executable. The locked Update preserves unrelated additions but does not compare the earlier editor buffer's version against the current same-entry body. Plain Append and whole-snapshot Rewrite expose weaker library capabilities, not an additional semantic admission process or a known later agent consumer. Manual JSONL edits/merges can bypass CLI checks; ReadAll performs JSON decoding and topic normalization rather than replaying all write validation. [RT-RTE-entry-maintenance](runtime.md#rt-rte-entry-maintenance), [MEM-OBJ-entry-metadata](#mem-obj-entry-metadata). SRC-1: `internal/commands/edit.go`, `internal/storage/storage.go`, `internal/commands/reindex.go`.

Cleanup is caller-directed removal or replacement with a related explanation. No typed supersession automatically suppresses contradictory entries. Raw-to-derived processing inside the executable is JSONL text/topics → FTS rows/tokenization → later ranked snippets; metadata mtime gates regeneration. It preserves the full body only in the source corpus and does not add evidential reasons. Alternative compacted session checkpoints are outside this target's inspected dispatch, not a hidden second retention route inferred from the term “memory.” [MEM-OBJ-entries-fts](#mem-obj-entries-fts), [MEM-OBJ-metadata](#mem-obj-metadata), [RT-RTE-entry-maintenance](runtime.md#rt-rte-entry-maintenance). SRC-1: `internal/index/index.go`, `cmd/gn/main.go`.

The inspected evaluator tests assert freshness-driven appearance of a newly appended entry and forced-rebuild searchability. Their input/output expectations concern storage-to-retrieval behavior; they do not produce retained semantic verdicts that later agents consume. Test passage, recall quality and downstream decision quality remain unobserved. SRC-1: `internal/index/index_test.go`, `internal/commands/reindex_test.go`.

## Read-back

The supported consumer chain is a later shell-capable coding agent, instructed by shipped setup/doctrine, requesting search or browsing; code selects retained material and prints it; the agent may request show and then interpret the entry. That is more than a hypothetical storage API, but less than observed agent compliance. [RT-RTE-doctrine-delivery](runtime.md#rt-rte-doctrine-delivery), [RT-RTE-knowledge-read](runtime.md#rt-rte-knowledge-read), [RT-BAP-agent-guidance](runtime.md#rt-bap-agent-guidance). SRC-1: `README.md`, `AGENTS.md`, `internal/doctrine/plan.txt`.

The main omission risks are lexical query mismatch, result-count truncation, short body/topic excerpts, and stale projection state. Full rationale remains available through explicit ID/topic reads while its entry survives. Related IDs are displayed but do not recursively load supporting entries. A successful delivery therefore does not imply the later agent received the whole reason chain or the newest account. [MEM-OBJ-entry-text](#mem-obj-entry-text), [MEM-OBJ-entry-metadata](#mem-obj-entry-metadata), [MEM-OBJ-entries-fts](#mem-obj-entries-fts), [MEM-OBJ-metadata](#mem-obj-metadata). SRC-1: `internal/commands/show.go`, `internal/commands/search.go`, `internal/index/index.go`.

## Integration issues

- No correction to the supplied runtime facts was established. Newly declared objects distinguish durable body, structural entry fields, derived lexical rows and freshness metadata; they are not duplicate routes or replacement declarations for supplied records. Their nearest supplied records and distinct identities are stated in each declaration.
- Original provenance/control remains unresolved for [MEM-OBJ-entry-text](#mem-obj-entry-text) and [MEM-OBJ-entry-metadata](#mem-obj-entry-metadata): the checked-in corpus and supplied attribution route do not establish who approved each item or the authenticity of the originating human/empirical information. This prevents equating intended human knowledge with authenticated human-controlled admission. SRC-1: `.gnosis/entries.jsonl`, `internal/commands/write.go`; see [RT-RTE-entry-admission](runtime.md#rt-rte-entry-admission).
- Later activation remains unresolved for [RT-BAP-agent-guidance](runtime.md#rt-bap-agent-guidance) and [RT-RTE-knowledge-read](runtime.md#rt-rte-knowledge-read): shipped instructions establish an afforded caller workflow, but no supplied trace shows an entry changing a later decision. This prevents claims of demonstrated learning or benefit. SRC-1: `README.md`, `AGENTS.md`, `internal/doctrine/plan.txt`.
- Rationale availability and withdrawal must remain consumer-specific. [MEM-OBJ-entry-text](#mem-obj-entry-text) may retain reasons that [MEM-OBJ-entries-fts](#mem-obj-entries-fts) excerpts omit; [MEM-OBJ-metadata](#mem-obj-metadata) can preserve old snippets after file disappearance. These qualify memory completeness and withdrawal without contradicting normal successful refresh/removal. SRC-1: `internal/index/index.go`, `internal/commands/search.go`, `internal/commands/show.go`.

## Limitations and checks

The frozen checkout HEAD was rechecked as `429528bf98e424b40837d2dbe3631d0fb42da6fd`; Git status reported no tracked changes. The method used is the supplied memory job, member type and shared records/worker contracts. Source-path coverage is distinguished from supplied runtime evidence above. No external sources, prior analyses, target executions or runtime fixtures were used.

Available but not fully inspected helper/rendering/test implementations do not support exhaustive portability, concurrency or presentation guarantees. The inspected search/edit/storage countercases bound claims about rationale delivery, authorship, freshness and semantic supersession. Missing original session evidence prevents reconstructing authentic trace origin; missing later runs prevents claiming actual compliance or improved capacity. Host context eviction, summaries and isolation remain outside the source boundary.

Validation: the required invocation-specific `validate-output` command passed (exit 0): “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” This establishes the checker result, not semantic acceptance.
