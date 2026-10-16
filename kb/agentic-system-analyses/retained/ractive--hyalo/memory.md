---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Hyalo memory mechanisms: mutable Markdown, derived snapshots, agent-directed maintenance and bounded Jev evidence supply."
run-id: AAS-2026-10-14-hyalo-ffe11d6a6d56-01
source-identity: "https://github.com/ractive/hyalo"
reviewed-boundary: "697f215fe8a90a5c760fceb686f2a321c9db7221"
---

# Hyalo memory report

## Boundary and evidence

Hyalo retains knowledge primarily in caller-owned Markdown files. Its optional binary snapshot retains mechanically extracted access state, not a second authored knowledge corpus. This report includes CLI persistence and retrieval, configuration and installed guidance, profile-generated navigation, Pi delivery and feedback, and Jev's bounded evidence preparation. The enclosing agent owns conversation history and judgment. Claude auto-memory is a read-only external signal in the tidy instruction, not a Hyalo-managed write destination. Provider state, deployed vault contents and host context retention are not captured; this prevents conclusions about their lineage, activation or effectiveness. The source and exclusions are those of [boundary](boundary.md).

All additional inspection below is SRC-1 implementation or doctrine/design at the reviewed commit. HEAD equals the boundary pin and Git status was clean. No target code, tests, examples or provider calls were executed. Supplied runtime findings are distinguished from direct reads; positive code witnesses do not establish operational use.

| Entry point / operation | Source paths and inspection basis | Coverage and prevented conclusions |
|---|---|---|
| Find, read, backlinks, task reads | Direct dispatch, prepared refresh and read section extraction: `crates/hyalo-cli/src/dispatch.rs`, `crates/hyalo-cli/src/prepared.rs`, `crates/hyalo-cli/src/commands/read.rs`; supplied find findings | [RT-RTE-query-read](runtime.md#rt-rte-query-read), [MEM-OBJ-frontmatter](#mem-obj-frontmatter), [MEM-OBJ-body](#mem-obj-body). Detailed ranking and all output projection branches not reread; no completeness or token-window guarantee. |
| Create/reuse/repair/drop snapshot | Direct `crates/hyalo-cli/src/commands/create_index.rs`, `crates/hyalo-core/src/index.rs`, `crates/hyalo-cli/src/prepared.rs`, `crates/hyalo-cli/src/commands/drop_index.rs`; supplied journal findings | [MEM-RTE-snapshot-lifecycle](#mem-rte-snapshot-lifecycle), snapshot parts below. Encoding loader branches and all race conditions not audited; freshness remains heuristic. |
| Set, append, remove, scaffold new | Supplied set route; direct append dispatch/validation search, remove preparation/apply and new preflight: `crates/hyalo-cli/src/commands/append.rs`, `crates/hyalo-cli/src/commands/remove.rs`, `crates/hyalo-cli/src/commands/new.rs` | [RT-RTE-property-write](runtime.md#rt-rte-property-write), [MEM-RTE-metadata-withdrawal](#mem-rte-metadata-withdrawal). New scaffolds use schema defaults; human authorship of initial corpus and per-value human approval remain unknown. New/append full publication paths not audited. |
| Task mutation, tag rename, move | Direct dispatch inventory; supplied Pi/task and tidy findings: `crates/hyalo-cli/src/dispatch.rs`, `pi-package/extensions/hyalo.ts` | [RT-RTE-tidy-review](runtime.md#rt-rte-tidy-review), [RT-RTE-pi-feedback](runtime.md#rt-rte-pi-feedback). Detailed handlers not inspected here; no universal rollback or link-rewrite guarantee inferred. |
| Lint repair, link fix/auto | Direct dispatch and links planner/apply searches: `crates/hyalo-cli/src/commands/links.rs`, `crates/hyalo-cli/src/dispatch.rs`; complete tidy instruction | [RT-RTE-tidy-review](runtime.md#rt-rte-tidy-review). Preview/apply and fuzzy opt-in are identified; detailed repair algorithms and all rejected-output paths remain uninspected. No semantic correctness conclusion. |
| Summary, properties/tags summary, terms | Direct summary aggregation, dispatch and API: `crates/hyalo-cli/src/commands/summary.rs`, `npm/hyalo/src/api.ts` | [RT-RTE-summary-injection](runtime.md#rt-rte-summary-injection), [MEM-OBJ-index-entry](#mem-obj-index-entry). Other aggregators' exact bounds remain uninspected; results are access summaries, not retained criticisms. |
| Schema/views/lint rules and install/deinit | Direct dispatch inventory; supplied config/install findings: `crates/hyalo-cli/src/dispatch.rs`, `crates/hyalo-cli/src/commands/init.rs` | [RT-RTE-config-install](runtime.md#rt-rte-config-install). Lint-rule publication and deinit removal details not traced; withdrawal of already loaded host instructions cannot be established. |
| MADR TOC / OKF index | Direct MADR generation and common splice/publication: `crates/hyalo-cli/src/commands/madr.rs`, `crates/hyalo-cli/src/commands/managed_region.rs`; OKF entry search | [MEM-RTE-navigation-generation](#mem-rte-navigation-generation). MADR is traced; OKF's separate selector/rendering details remain uninspected. |
| OKF log / changelog add and release | Direct function/dispatch inventory: `crates/hyalo-cli/src/commands/okf.rs`, `crates/hyalo-cli/src/commands/changelog.rs` | Included caller-authored log/release write surfaces. Detailed admission, lineage and later specialized consumers not inspected; their names establish neither automatic trace learning nor evaluation-driven updates. Ordinary Markdown reads remain available. |
| npm library operations / Pi registered tools and hooks | Direct exported functions, registration inventory and hooks: `npm/hyalo/src/api.ts`, `pi-package/extensions/hyalo.ts` | [RT-RTE-query-read](runtime.md#rt-rte-query-read), [RT-RTE-pi-feedback](runtime.md#rt-rte-pi-feedback), [RT-RTE-summary-injection](runtime.md#rt-rte-summary-injection). API capability alone is not a deployed consumer; Pi is shipped consumer wiring. |
| Jev prepare/ask/review | Complete preparation and protocol limits directly read: `npm/jev/src/prepare.ts`, `npm/jev/src/protocol.ts`; supplied provider, threshold and review findings | [RT-RTE-jev-suggestions](runtime.md#rt-rte-jev-suggestions), [RT-OBJ-manifest](runtime.md#rt-obj-manifest). Saved outputs are caller-retained, not automatic write-back; provider internals remain outside boundary. |
| Tidy, Git signals, optional Claude memory, distributed skill copies | Complete template directly read: `crates/hyalo-cli/templates/skill-hyalo-tidy.md`; supplied Codex comparison | [RT-RTE-tidy-review](runtime.md#rt-rte-tidy-review), [RT-OBJ-hyalo-tidy](runtime.md#rt-obj-hyalo-tidy). Other distributed copies and native evaluators not independently compared; no compliance, passing tests or cross-host equivalence inferred. |

## Core ideas

1. **Separate content from access state.** Frontmatter has fixed schema/filter consumers; prose has agent/human interpretation consumers. The snapshot stores extracted properties, outline/tasks/links and lexical search state. Ranking can select prose but does not turn it into instructions or verified knowledge. [MEM-OBJ-frontmatter](#mem-obj-frontmatter), [MEM-OBJ-body](#mem-obj-body), [MEM-OBJ-index-entry](#mem-obj-index-entry), [MEM-OBJ-bm25](#mem-obj-bm25).
2. **Read repair and persistent maintenance differ.** Prepared reads can repair snapshot drift in memory or fall back to disk without writing the snapshot. Explicit create-index and loaded-index mutation reconciliation can persist refreshed access state. Compatibility checks are not freshness proofs, and metadata-based detection is not byte authentication. [MEM-RTE-snapshot-lifecycle](#mem-rte-snapshot-lifecycle).
3. **Maintenance judgment lives with the agent.** Tidy prescribes trace-informed status/link/tag repairs, previews, restraint and explanations. Those instructions do not enforce a file-write veto or require reasons to be embedded in each repaired note. Jev emits advisory labels from bounded evidence; adopting them requires another route. [RT-RTE-tidy-review](runtime.md#rt-rte-tidy-review), [RT-RTE-jev-suggestions](runtime.md#rt-rte-jev-suggestions).
4. **Context is selected, not autonomously compacted here.** Explicit file/section queries, the Pi session summary, requested forked tidy context and separate Jev requests regulate what reaches models. No inspected extension/helper mechanism replaces old conversation turns with retained summaries. That is a scoped implementation limit, not a claim about external hosts. [RT-RTE-query-read](runtime.md#rt-rte-query-read), [RT-RTE-summary-injection](runtime.md#rt-rte-summary-injection), [RT-RTE-tidy-review](runtime.md#rt-rte-tidy-review).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-frontmatter
Label: Markdown frontmatter

Source-native YAML frontmatter persists in vault Markdown; parsers expose properties as JSON values and extracted tags. This object is the symbolic metadata consumption path, not the body. `type`, status, tags and configured properties influence deterministic schema checking and selection. Free-text values may also be interpreted by agents, but are not thereby hard policy. Initial author/ingest lineage is caller-owned and unobserved. Set, append, remove and scaffold defaults supply inspected subsequent transformations. Closest supplied record is [RT-RTE-property-write](runtime.md#rt-rte-property-write), a write route rather than this stored part; no supplied object counterpart was found. SRC-1, `crates/hyalo-core/src/index.rs`, `crates/hyalo-cli/src/commands/remove.rs`, `crates/hyalo-cli/src/commands/new.rs`.

> /// Raw frontmatter properties.
> pub properties: IndexMap<String, serde_json::Value>,
> /// Extracted tags (from properties).
> pub tags: Vec<String>,
> --- `crates/hyalo-core/src/index.rs`

#### MEM-OBJ-body
Label: Markdown body

Natural-language knowledge text persists in Markdown files. Headings, task checkboxes and link syntax also have symbolic extraction consumers; their extraction products belong to [MEM-OBJ-index-entry](#mem-obj-index-entry). Human/agent authorship and imported-content trust are not authenticated by Hyalo. Source may contain raw logs, explanations or guidance, depending on the user's corpus; this frozen implementation does not establish which. Later explicit reads deliver selected content to the agent; Jev receives a bounded body/section string. This is the durable source of [RT-OBJ-document-content](runtime.md#rt-obj-document-content), not that request-local copy. Source-native note meaning can change under external body edits, while the inspected metadata removal preserves the body via frontmatter rendering. SRC-1, `crates/hyalo-cli/src/commands/read.rs`, `npm/jev/src/prepare.ts`, `crates/hyalo-cli/src/commands/remove.rs`.

> const readArgs = selected.section === null ? ["--lines", "1:"] : ["--section", selected.section];
> --- `npm/jev/src/prepare.ts`

#### MEM-OBJ-index-entry
Label: Snapshot extracted entries and graph

Source-native `IndexEntry` and link graph are symbolic access state stored in process memory and the binary snapshot, normally `.hyalo-index`. Metadata is copied from frontmatter; outlines, tasks, link targets/anchors, paths, timestamps, sizes and coverage/skip metadata are mechanically extracted. They are derived corpus state, not agent interaction traces or a learned explanatory theory. Consumers include find, summary, backlinks and link resolution. File identity remains meaningful even when parsing fails; skip/attachment identity is not readable note content. A positive indexed field can direct selection, not establish truth of the note's claims. Closest supplied [RT-RTE-query-read](runtime.md#rt-rte-query-read) describes consumption but declares no index object. This record excludes lexical postings, assessed separately below. SRC-1, `crates/hyalo-core/src/index.rs`, `crates/hyalo-cli/src/dispatch.rs`.

> /// Document outline sections.
> pub sections: Vec<OutlineSection>,
> /// Task checkboxes with section context.
> pub tasks: Vec<FindTaskInfo>,
> /// Outbound links with 1-based line numbers.
> pub links: Vec<(usize, Link)>,
> --- `crates/hyalo-core/src/index.rs`

#### MEM-OBJ-bm25
Label: BM25 lexical postings

Source-native `Bm25InvertedIndex` is symbolic token/posting state in memory and the persisted snapshot. Numerical scores/statistics are localized deterministic retrieval data, not distributed model parameters or embeddings. Tokens derive from title/body/headings/tags; language and tokenizer-version metadata control reuse and live re-tokenization. Persisted entry token lists may be stripped because postings reconstruct them. Consumer is ranked retrieval; authority is ordering candidate results under an explicit query, not deciding admissible knowledge. It shares the snapshot substrate with [MEM-OBJ-index-entry](#mem-obj-index-entry) but has a different consumer and invalidation input. Closest supplied [RT-RTE-query-read](runtime.md#rt-rte-query-read) mentions BM25, not a competing object declaration. SRC-1, `crates/hyalo-core/src/index.rs`, `crates/hyalo-cli/src/commands/create_index.rs`.

> /// Pre-tokenized, field-aware BM25 tokens (title + body stream, heading
> /// runs, tag tokens; DEC-337). Populated by `create-index` and by
> /// incremental re-scans of a snapshot that carries a BM25 index. Stripped
> /// from the persisted entries when the inverted index is saved beside
> /// them (the postings reconstruct it).
> --- `crates/hyalo-core/src/index.rs`

#### MEM-OBJ-managed-region
Label: Generated navigation managed region

Source-native MADR TOC and OKF index managed regions persist in Markdown between HTML comment markers. Markers have symbolic splice authority; displayed headings/tables supply human/agent-readable navigation. The traced MADR content derives from ADR records, not conversation traces. Links provide a reload route to the underlying notes; the generated display is not a complete rationale store. Prose outside markers has separate authorship and preservation rules. Closest supplied [RT-RTE-config-install](runtime.md#rt-rte-config-install) mentions profile generators only as an uninspected surface; no supplied object counterpart. SRC-1, `crates/hyalo-cli/src/commands/managed_region.rs`, `crates/hyalo-cli/src/commands/madr.rs`.

> //! A *managed region* is the span of a generated file that a `hyalo`
> //! generator owns, delimited by a pair of HTML-comment markers
> //! (`<!-- <prefix>:begin -->` / `<!-- <prefix>:end -->`). Prose outside the
> //! markers is preserved verbatim across regenerations.
> --- `crates/hyalo-cli/src/commands/managed_region.rs`

### Routes

#### MEM-RTE-snapshot-lifecycle
Label: Snapshot creation refresh and withdrawal

Explicit create-index request → discovered Markdown/attachments → scan or compatible reuse → BM25 build/patch → binary publication. A later indexed invocation loads those derived parts; prepared selection can refresh named targets and repair drift in memory. Mutation journal finalization supplies a separate persistent update path. Drop-index explicitly removes the snapshot, not corpus knowledge. CLI code owns mechanical selection/publication; the caller decides whether to request creation, force rebuild or removal. This route is distinct from [RT-RTE-query-read](runtime.md#rt-rte-query-read) and [RT-RTE-property-write](runtime.md#rt-rte-property-write): it concerns the derived persistence lifecycle those routes can consume/maintain. SRC-1, `crates/hyalo-cli/src/commands/create_index.rs`, `crates/hyalo-cli/src/prepared.rs`, `crates/hyalo-cli/src/commands/drop_index.rs`, `crates/hyalo-core/src/index.rs`; journal recovery passage in [RT-RTE-property-write](runtime.md#rt-rte-property-write).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Index path/counts, reused/refreshed/removed/written indicators, warnings and publication effects; drop returns removal outcome.
- Later read-back: Persisted entries, graph and lexical postings feed subsequent CLI queries; transient read repair is not saved and may be repeated later.
- Delegated visibility: Callers receive formatted results/diagnostics, not automatically the complete binary state; selected content reaches agents via query/read or summary delivery.
- Selection predicate: Discovered corpus and configured exclusions; reuse checks compatible snapshot, tokenization/language and file metadata. Force bypasses previous snapshot loading. Prepared refresh uses effective explicit selection and command class.
- Invalidation or expiry: Rebuild drops removed entries; drift repair drops deleted/unscannable entries locally; compatibility failures or repair failure can use disk. Drop removes the named snapshot; journal failure attempts persistent invalidation, which can fail.
- Activation or effect: Derived-state persistence and later lookup are wired; no observed retrieval benefit or changed model behavior.
- Evidence limits: Metadata heuristics do not authenticate unchanged bytes; no all-writer coherence or batch rollback established. A read repairs in process only, and index removal does not retract already delivered text.

Admission is an open caller request, not a scored improvement experiment. Code decides reusable products and rejects invalid path/encoding/publication conditions; human per-entry approval is not required. No answer oracle judges note truth. Kept state contains extracted content/access metadata, not a record explaining why a knowledge claim was accepted. Recovery includes forced rebuild, disk fallback and effect reporting; no universal automatic undo is inferred.

> let mut previous = if force || !replacing_existing {
>     None
> } else {
>     SnapshotIndex::load_for_reuse(&index_path)
>         .filter(|prev| prev.validate(&vault_dir_str, site_prefix))
> };
> --- `crates/hyalo-cli/src/commands/create_index.rs`

> // DEC-339: a read repairs drifted entries in memory for this
> // run — re-scanning only those files and patching the BM25
> // postings — instead of answering from a stale snapshot. The
> // snapshot file is never written by a read.
> --- `crates/hyalo-cli/src/prepared.rs`

> let effect = root.remove_artifact(&name, &mut session)?;
> --- `crates/hyalo-cli/src/commands/drop_index.rs`

#### MEM-RTE-metadata-withdrawal
Label: Property and tag withdrawal

Caller remove request → selected captured documents → parsed frontmatter/where filters → key, list-value or tag removal → rendered replacements → preview or prepared apply/journal. The deterministic handler decides mechanical admissibility; the caller proposes what to withdraw. This is a separate operation from supplied [RT-RTE-property-write](runtime.md#rt-rte-property-write), whose set-specific validation must not be extended to remove. It changes [MEM-OBJ-frontmatter](#mem-obj-frontmatter), not document-body claims. SRC-1, `crates/hyalo-cli/src/commands/remove.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Per-property/tag modified/skipped results, dry-run marker and apply effects.
- Later read-back: Removed metadata no longer supplies later live filters/aggregations; when journal reconciliation succeeds, the loaded snapshot reflects surviving file effects.
- Delegated visibility: Caller receives mutation results; generic Pi Hyalo removal is not covered merely by the typed set/task feedback path.
- Selection predicate: Explicit file/glob or where-property/tag scope; parsed files and matching existing key/value/tag.
- Invalidation or expiry: Dry-run does not publish. Later set/append can restore values, but automatic rollback is not promised. Previously returned metadata is not retracted from host context.
- Activation or effect: Prepared frontmatter withdrawal is wired; actual withdrawals and subsequent model reliance are unobserved.
- Evidence limits: Removal is not claim-level epistemic rejection, corpus-file deletion or a complete schema-validation gate; caller identity does not establish per-value human approval.

Mode is open mutation. There is no answer oracle or semantic evaluator; the caller can withhold the command or preview it. Parsing, scope and prepared publication supply software rejection. Reasons for withdrawal are not required stored fields. Recovery follows prepared apply/effects and caller repair, not enforced restoration. Unlike a strict knowledge-admission system, a property can be removed without the set handler's active assigned-property constraint test; dispatch exposes no remove validation argument. SRC-1, `crates/hyalo-cli/src/dispatch.rs`, `crates/hyalo-cli/src/commands/remove.rs`.

> let report = if dry_run {
>     preparation.preview()
> } else {
>     preparation.apply(journal, "removing properties")
> };
> --- `crates/hyalo-cli/src/commands/remove.rs`

#### MEM-RTE-navigation-generation
Label: MADR navigation generation

Caller MADR TOC request → collect ADRs → render navigation → classify existing markers → splice → optional apply → reconcile generated-note effects. This traced route uses [MEM-OBJ-managed-region](#mem-obj-managed-region); OKF shares splice machinery but its exact selection is not transferred to this route. Closest supplied [RT-RTE-config-install](runtime.md#rt-rte-config-install) is installation/configuration, not this derived note update. SRC-1, `crates/hyalo-cli/src/commands/madr.rs`, `crates/hyalo-cli/src/commands/managed_region.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Generated-file action/drift payload and publication effects; preview detects divergence without applying.
- Later read-back: Persisted Markdown TOC can be read as a note by later agent/human invocations; contained links make source ADRs reachable. No special autonomous TOC consumer is inferred.
- Delegated visibility: Caller receives action/results; source ADR rationale is not copied wholesale into the navigation table.
- Selection predicate: Configured or default ADR directory, collected ADR entries and existing generated README; marker classification controls ownership of bytes.
- Invalidation or expiry: Regeneration replaces the owned region. Marker-less bodies are preserved by default; explicit replace can discard them. Malformed markers reject generation and concurrent changed destination bytes reject replacement.
- Activation or effect: Deterministic navigation publication and index reconciliation are wired; deployed agent use and improved navigation are unobserved.
- Evidence limits: This is content-derived navigation, not automatically learned guidance or retained evaluation criticism. Shared machinery does not establish every OKF behavior.

Mode is open caller-driven generation, with no answer oracle. The caller authorizes apply and can choose replacement; there is no required human review of each generated row. Code owns generation and vetoes malformed markers/path/source conflicts. Recovery reports finalization errors, reconciles effects and permits subsequent regeneration; it does not promise universal rollback. Output retains links and display summaries, not reasons for accepting each source ADR.

> let entries = collect_adrs(&adr_full, adr_rel, schema)?;
> let body = render_toc_body(&entries);
> --- `crates/hyalo-cli/src/commands/madr.rs`

> // No markers. Non-destructive adopt: keep the existing body and append
> // the managed region. Only Replace discards a marker-less body.
> --- `crates/hyalo-cli/src/commands/managed_region.rs`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-metadata-selection
Label: Metadata selection authority

Consumer: deterministic CLI filter/schema/aggregation code. Channel: parsed frontmatter or compatible extracted snapshot entries. Force: rule-based scope and validation effects under configured consumer options; these values are not universal agent instructions. Horizon: subsequent commands until metadata/config changes or snapshot invalidation/refresh. This complements [RT-BAP-tidy-guidance](runtime.md#rt-bap-tidy-guidance), whose consumer and policy force are different. SRC-1, `crates/hyalo-cli/src/commands/remove.rs`, `crates/hyalo-cli/src/commands/summary.rs`.

> if !filter::matches_frontmatter_filters(&props, where_property_filters, where_tag_filters) {
>     continue;
> }
> --- `crates/hyalo-cli/src/commands/remove.rs`

## Annotations

#### On [RT-OBJ-manifest](runtime.md#rt-obj-manifest)

Persistence is optional caller-captured JSON/stdin, not an automatic helper-owned knowledge store. Policy candidate labels, selection, fingerprints and context hashes are symbolic controls. Category descriptions are natural-language model guidance; their source is supplied local policy, not learned parameters. Context hash derives from raw config and selected type schemas. Initial policy author and human approval remain unresolved. Preparation requires declared candidate types and existing permitted folders. Evidence/policy/context consistency does not establish trusted initial provenance or unchanged live files. SRC-1, `npm/jev/src/prepare.ts`, `npm/jev/src/protocol.ts`; supporting fingerprint limit in [RT-RTE-jev-suggestions](runtime.md#rt-rte-jev-suggestions).

> const contextHash = hash({ config, schemas });
> --- `npm/jev/src/prepare.ts`

#### On [RT-OBJ-document-content](runtime.md#rt-obj-document-content)

Lineage is the selected Markdown body/section copied through read-only Hyalo into a manifest and provider input. The helper keeps separate current-frontmatter state for eligibility, but the remote classification state is body evidence. Source trust remains explicitly limited by the untrusted-data preamble retained in [RT-RTE-jev-suggestions](runtime.md#rt-rte-jev-suggestions). Direct preparation establishes at most 25 explicit distinct Markdown selections; each body/section must be nonempty and at most 18,000 bytes. Protocol caps request at 24,000 bytes, questions at 48 and manifest input at 1 MiB. These are byte/count budgets, not host-context token budgets. Too-large evidence defers rather than automatically summarizes. Raw prose is neither a conversation trace nor a derived learned memory merely because it is passed to Jev. SRC-1, `npm/jev/src/prepare.ts`, `npm/jev/src/protocol.ts`.

> insist(bytes <= 18_000, `${what} too large (${bytes} bytes > 18000)`);
> --- `npm/jev/src/prepare.ts`

#### On [RT-OBJ-hyalo-tidy](runtime.md#rt-obj-hyalo-tidy)

Installed natural-language method text is static package guidance, not read-back accumulated through use. It nevertheless can shape later agent decisions when a host loads it. The prescribed repairs can change retained metadata/links based on Git merges, task counts and recent knowledgebase activity. This is a claimed trace-informed curation path, not an implemented autonomous trace-to-guidance learner. The report asks for reasons per change, but neither the instruction nor mutation route establishes that those reasons are written into notes or consumed in a later round. Host/caller report retention is uninspected. SRC-1, `crates/hyalo-cli/templates/skill-hyalo-tidy.md`.

> - **Explain every change**: include the evidence (commit hash, task counts, etc.).
> --- `crates/hyalo-cli/templates/skill-hyalo-tidy.md`

#### On [RT-RTE-summary-injection](runtime.md#rt-rte-summary-injection)

The selected retained inputs are vault metadata, task/structural scan results and recent-file identities; summary aggregates them rather than retaining full source rationale. Direct summary code caps tracked distinct string values at 50 per text property and selects recent files by descending modification time with `recent`; this is not semantic relevance selection. Extension delivery has a configured once-per-process trigger and no explicit token-budget guard in the inspected injection block. The summary is request-local derived output delivered unsolicited to the host, not persisted as an extension-owned checkpoint. Later host transcript persistence is external. Explicit find/read is the reload path; no automatic retraction of stale injected text is established. SRC-1, `crates/hyalo-cli/src/commands/summary.rs`, `pi-package/extensions/hyalo.ts`.

> content:
>   `Knowledgebase snapshot (${config.vaultDir}/) for this session:\n\n` +
>   summaryText +
>   "\n\nUse this to orient yourself; refine with the hyalo tool.",
> display: false,
> --- `pi-package/extensions/hyalo.ts`

## Write side

**Acquisition and authorship.** Existing corpus content originates outside the traced commands; Hyalo does not authenticate authorship. New scaffolding derives defaults from the selected declared schema, with path and generated-frontmatter preflight. Metadata assignments/additions/removals and host prose edits are separate admission mechanisms: set/append can activate assigned-property schema checks; remove has no corresponding dispatch validation option; external body edits use host authority. Generic caller identity leaves human content control unresolved. Software publication is not human approval. SRC-1, `crates/hyalo-cli/src/commands/new.rs`, `crates/hyalo-cli/src/commands/append.rs`, `crates/hyalo-cli/src/dispatch.rs`; [RT-RTE-property-write](runtime.md#rt-rte-property-write), [MEM-RTE-metadata-withdrawal](#mem-rte-metadata-withdrawal).

**Transformation and maintenance.** Snapshot extraction, lexical tokenization and navigation generation derive access products from the corpus. Their durable outputs feed later queries or ordinary Markdown reads. They do not establish changed knowledge meaning, warranted criticism or learned model parameters. Tidy prescribes metadata/link/tag changes and relocation based on local signals; lint/link algorithms supply additional deterministic repair proposals. Agent review and apply flags are distinct from mechanical preparation/publication. Full algorithmic coverage remains limited as the table states. SRC-1, `crates/hyalo-cli/templates/skill-hyalo-tidy.md`; [MEM-RTE-snapshot-lifecycle](#mem-rte-snapshot-lifecycle), [MEM-RTE-navigation-generation](#mem-rte-navigation-generation), [RT-RTE-tidy-review](runtime.md#rt-rte-tidy-review).

**Evaluation and rejection.** Lint returns structural diagnostics; Pi appends them after covered writes, not as a publication veto. Tidy asks for fresh summary comparison after repairs. Neither count deltas nor lint success are an oracle for note truth. Jev confidence/label gates admit suggestions to output only; failed/conflicting evidence defers and the foreground agent can reject suggestions before ordinary mutations. No helper result automatically updates the corpus or installed method. SRC-1, `pi-package/extensions/hyalo.ts`, `npm/jev/src/prepare.ts`; [RT-RTE-pi-feedback](runtime.md#rt-rte-pi-feedback), [RT-RTE-jev-suggestions](runtime.md#rt-rte-jev-suggestions).

**Withdrawal.** Remove changes metadata; archive moves retain body content; drop-index removes derived access state. Tidy forbids deleting files/body and modifying Claude memory, while profile generation's explicit replace can discard a marker-less generated destination body. Thus tidy's policy cannot be promoted to a system-wide no-deletion invariant. Index reconciliation and snapshot repair can remove unusable access entries while preserving underlying files; an old model-visible result can survive all these operations in the host transcript. SRC-1, `crates/hyalo-cli/templates/skill-hyalo-tidy.md`, `crates/hyalo-cli/src/commands/managed_region.rs`; [MEM-RTE-metadata-withdrawal](#mem-rte-metadata-withdrawal), [MEM-RTE-snapshot-lifecycle](#mem-rte-snapshot-lifecycle).

**Trace-fed outputs and rationale.** The instructed chain is Git/task/recent-history signals → agent diagnosis → authorized retained metadata/link repairs → later query/read. Reasons are requested in the report; durable report retention and later reason consumption remain unknown. Raw Git history and Claude memory remain external read inputs. Indexes derive from document state, not these operational traces. Changelog/OKF log entry points are included but their detailed lineage is uninspected; they cannot support an autonomous learning conclusion here. No inspected extension/helper compaction path supplies an alternative learned checkpoint. This does not establish absence of trace learning in every available but uninspected shipped branch. SRC-1, `crates/hyalo-cli/templates/skill-hyalo-tidy.md`, `crates/hyalo-cli/src/dispatch.rs`; [RT-RTE-tidy-review](runtime.md#rt-rte-tidy-review).

## Read-back

**Requested delivery.** Explicit find/read and npm/Pi adapters select corpus parts through file, metadata, glob, ranked-query, section/line and result-limit inputs. A path requested directly is selection by identifier, not proof of semantic relevance targeting. BM25 ordering is an implemented relevance mechanism, not evidence that delivered content changed behavior. The registered Pi tools are generic hyalo, find, read, set and task; generic/API raw access leaves additional commands reachable. The npm API also exposes summary, terms, tags and backlinks. APIs with unspecified callers establish capabilities; the Pi hooks and instructed foreground agent establish shipped consumers. SRC-1, `npm/hyalo/src/api.ts`, `pi-package/extensions/hyalo.ts`; [RT-RTE-query-read](runtime.md#rt-rte-query-read).

**Independent supply.** Pi's opt-in summary injection runs on session start under code rules, aggregates retained vault state and supplies a hidden custom message with orientation advice. It sets its once flag before fetching, so failure need not yield retry; configured state is cached. There is no automatic freshness lease on previously delivered text. This is unsolicited context supply, not automatic durable summary-memory maintenance. [RT-RTE-summary-injection](runtime.md#rt-rte-summary-injection).

**Isolated work and reload.** Long tidy metadata requests a fork; what inputs stay out of the foreground window, what survives the fork and what crosses back are host-defined. The supplied shorter Codex version lacks the same declaration. Jev preparation keeps selected bodies out of the main agent window until intended-suggestion review: explicit bounded inputs go into a separate service call and decisions/deferrals escape back, while optional saved JSON can remain reachable. This resembles a separate computation frame, not an implementation of host stack disposal. Provider retention is unknown, and copied evidence is by value, not a dereferenceable context pointer. Section selection excludes other body material; rejected oversized evidence is deferred, not condensed. Explicit read/re-preparation can reload excluded material. None of these mechanisms establishes eviction of old turns or a verbatim-tail/summary compaction checkpoint inside Hyalo. SRC-1, `npm/jev/src/prepare.ts`; [RT-RTE-tidy-review](runtime.md#rt-rte-tidy-review), [RT-RTE-jev-suggestions](runtime.md#rt-rte-jev-suggestions).

**Authority at consumers.** Parsed metadata and snapshot fields control deterministic selection; prose and installed skills can inform host-model decisions but loading/delivery is not semantic compliance. Jev category descriptions request interpretation, then symbolic output checks govern the suggestion channel. Structural diagnostics have post-publication advisory authority. No inspected provenance mechanism makes retrieved document prose a higher-trust instruction source. [MEM-BAP-metadata-selection](#mem-bap-metadata-selection), [RT-BAP-tidy-guidance](runtime.md#rt-bap-tidy-guidance), [RT-BAP-jev-categories](runtime.md#rt-bap-jev-categories), [RT-RTE-pi-feedback](runtime.md#rt-rte-pi-feedback).

## Integration issues

- **Runtime refinement, not a contradiction:** [RT-RTE-query-read](runtime.md#rt-rte-query-read) discusses selected refresh and freshness limits. Direct `crates/hyalo-cli/src/prepared.rs` inspection adds the material read-only in-memory drift repair/disk-fallback path in [MEM-RTE-snapshot-lifecycle](#mem-rte-snapshot-lifecycle). Reconciliation should not infer that every fresh indexed read persists its repairs, or that compatibility alone is the only stale-state handling.
- **Overlapping routes, distinct referents:** [MEM-RTE-snapshot-lifecycle](#mem-rte-snapshot-lifecycle) overlaps index portions of [RT-RTE-query-read](runtime.md#rt-rte-query-read) and [RT-RTE-property-write](runtime.md#rt-rte-property-write) but describes creation/removal and derivative persistence, not either complete invocation. [MEM-RTE-metadata-withdrawal](#mem-rte-metadata-withdrawal) is remove rather than set. [MEM-RTE-navigation-generation](#mem-rte-navigation-generation) is generation rather than [RT-RTE-config-install](runtime.md#rt-rte-config-install). No replacement or duplicate object is proposed.
- **Known partial loop detail:** OKF-specific selection/logs, changelog add/release, task/tag/move full mutation handlers, lint/link detailed repairs, lint-rule/deinit publication and distribution-copy/evaluator checks remain available but uninspected as the coverage table states. Their existence is established, not their complete lineage, rollback or later specialized consumer behavior. These limits prevent a system-wide admission/trace-learning guarantee; the positive traced routes remain intact. SRC-1, `crates/hyalo-cli/src/dispatch.rs`, `crates/hyalo-cli/src/commands/okf.rs`, `crates/hyalo-cli/src/commands/changelog.rs`.
- **External unknowns:** Corpus initial authorship, human per-content approval, saved Jev/report retention, model response calibration, host fork/compaction and activation of installed instructions remain unestablished. These concern [MEM-OBJ-frontmatter](#mem-obj-frontmatter), [MEM-OBJ-body](#mem-obj-body), [RT-OBJ-manifest](runtime.md#rt-obj-manifest), [RT-OBJ-hyalo-tidy](runtime.md#rt-obj-hyalo-tidy), [RT-RTE-tidy-review](runtime.md#rt-rte-tidy-review) and [RT-RTE-jev-suggestions](runtime.md#rt-rte-jev-suggestions). Provider/model internals cannot be inferred from helper labels.
- No supplied fact is contradicted by the additional source reads. No new record is identified as the same referent as a supplied declaration; closest counterparts and intersections are retained above.

## Limitations and checks

Implementation and doctrine establish capacities and prescribed roles only. No observed run or intervention establishes semantic repair correctness, activated recall, learning benefit, host compliance or provider reliability. Source-native labels such as “reflective consolidation” do not substitute for an evidenced theory-revision process. Available but uninspected branches remain explicit rather than being promoted to absences.

Source identity was rechecked against SRC-1: HEAD `697f215fe8a90a5c760fceb686f2a321c9db7221`, clean checkout. Governing job, supplied types, complete boundary/runtime inputs, collection, worker rules and record contract were read; supplied oversized ranges were recovered to EOF. Worker model and effort were taken from Pi environment, not requested profile. Frozen source stayed read-only; output writes stayed within the invocation scope.

Validation: invocation-specific `commonplace-run validate-output` passed: “Member content check passes; invocation residue not checked.” This is not job acceptance or claim support. The deterministic check does not establish analytical support or observed effectiveness.
