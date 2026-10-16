---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Instinctual Memory runtime baseline: journal consolidation, validated changes, retrieval, host context delivery and alternate maintenance paths."
run-id: AAS-2026-10-12-instinctual-memory-af48437aa60c-01
reviewed-boundary: "6acb13dc35765bf5ccfc87e445dd09c480f1c28a"
---

# Instinctual Memory runtime report

## Runtime account

### Claimed work and execution boundary

Instinctual Memory is a memory service and CLI, not the enclosing coding agent. It ingests sessions and project instruction files, publishes curated facts to a bare Git repository, searches facts alongside raw events, and delivers context to agents. Its model calls propose facts, judge cleanup candidates or score retrieval candidates; they do not run a general-purpose agent tool loop. The frozen scope and external dependencies are in [boundary](boundary.md). All findings below use SRC-1 at the frozen revision. Implementation and shipped instructions establish wiring and requested behavior, not exercised operation or benefit. No supplied observed run or causal experiment establishes accuracy, host compliance, successful recovery or improvement.

`src/main.rs` parses CLI arguments, resolves a store and calls `cli::run`; errors terminate with status 1. Stores can be explicit, local or global. The shipped CLI includes ingestion/backfill, consolidation, change, retrieval, writeback, cleanup, erasure, evaluation, model-cache administration, setup, hooks, shell and servers (SRC-1, `src/main.rs`, `src/cli.rs`). MCP stdio, loopback HTTP and the memory shell dispatch to `ops::execute`; the CLI also has direct handlers for production and maintenance. The Rust library exports the repository, validator, operation, change, journal, consolidation and maintenance APIs, so the transport layer is not the sole capability boundary (SRC-1, `src/lib.rs`).

> //! One operation layer for the CLI, the shell, HTTP, and MCP.
> --- `src/ops.rs`

### Ordinary invocation, end to end

The ordinary shipped `/mem` procedure makes memory ready, syncs when needed, then answers a question or applies a requested change. The principal is the host agent acting for a user. The skill instructs it to run `mem status`, create a store if missing, backfill local sessions and instruction files, consolidate new events, search a plain-language question and cite returned fact IDs. The host owns the next choice of command and the final answer. Its Bash/Read permissions and user approval policy are external, not granted or enforced by the Rust executable (SRC-1, `skills/mem/SKILL.md`).

Backfill opens a bulk journal writer, adapts local transcript and host-history files, tags events with project identity and skips already-seen event IDs. Named project files include AGENTS.md, CLAUDE.md, CODEX.md and README.md. The bulk journal writer uses framed JSONL in day files, an exclusive sequence lock, tail recovery and buffered writes; disabling fsync changes durability, not the logical event interface. Completion differs by entry path: `cmd_ingest`, `cmd_backfill` and `cmd_backfill_all` explicitly call `flush()?` before reporting completion, propagating final-flush failure. The ordinary local path, `cmd_backfill_local`, prints completion and returns without that call. Its final flush is best effort in `BulkWriter::drop`: failure is logged to stderr, not propagated as a command error. Thus local backfill's completion message does not establish successful final flushing, including when hooks invoke it (SRC-1, `src/cli.rs`, `src/journal.rs`). File/source IDs, journal sequence numbers, project tags, scope/session strings, entity/fact IDs, request IDs and Git revision IDs have different jobs: lookup, selection, provenance, replay or coordination. They are not interchangeable identities or authenticated principals.

> if let Err(err) = self.flush_inner_locked(&mut handles) {
>     eprintln!("mem: bulk writer drop flush failed: {err}");
> }
> --- `src/journal.rs`

[RT-RTE-journal-consolidation](#rt-rte-journal-consolidation) owns the next computational step. Each batch reloads the published revision, checkpoint, existing entities and suppression/deletion controls. Rules or the LLM propose facts. Software filters proposals, constructs entity/index/checkpoint/disposition changes, validates the candidate tree and compare-and-swaps the published branch. Without an explicit request ID, the CLI repeats until caught up. The terminal CLI output is a consolidation summary and revision; the durable result is a Git snapshot and batch dispositions, not a model answer. The LLM receives bounded event text and an existing-entity summary, not all raw store contents.

[RT-RTE-memory-retrieval](#rt-rte-memory-retrieval) reloads that snapshot and independently scans the journal. It interleaves lexical fact and journal candidates, optionally reranks and truncates, then returns IDs, statements, scores, source locations and ranker metadata. The host interprets the returned text to answer. Search delivery is not evidence that the host used it correctly. Later hooks and writeback are distinct consumption channels: [RT-RTE-host-hooks](#rt-rte-host-hooks) and [RT-RTE-instruction-writeback](#rt-rte-instruction-writeback).

### Control coverage and four forcing cases

**1. A quoted fragment does not guarantee a warranted statement.** Consolidation's evidence gate belongs to `check_llm_fact` and `quote_found`. It requires a model `lasting` flag, statement bounds, an evidence minimum, matching source fragments and a usable predicate/entity. Matching normalizes Markdown and whitespace, splits at ellipses, discards normalized fragments shorter than eight characters, and requires at least one remaining fragment. Every remaining fragment must appear in source order; short unmatched fragments do not cause rejection. Thus “verbatim” is an ordered normalized occurrence invariant only for qualifying fragments, not every submitted fragment, exact byte equality, semantic entailment or verified lasting usefulness. Direct caller assertions do not use this gate. The owning route records the distinction rather than extending the extraction gate to all memory writes (SRC-1, `src/consolidate.rs`, `src/change.rs`, `src/ops.rs`).

**2. Publication and replay checks differ by entry path.** `GitRepo::publish` validates the candidate before `update-ref ... candidate base`; its compare-and-swap prevents a cooperating publisher from overwriting a changed base. Receipt digests reject request-ID reuse with different canonical changes at this API. But `ops::request_change` returns early whenever a receipt with that ID exists, without comparing the incoming payload to its digest. A different request with a used ID can receive a replay result without applying its new content. This does not defeat CAS, but it narrows the replay contract exposed by MCP, HTTP and shell. The library also accepts a caller-supplied `Validator`; public `FnValidator` permits a weaker policy than shipped `DomainValidator`. External Git/filesystem access is outside the publisher's enforcement (SRC-1, `src/repo.rs`, `src/ops.rs`, `src/lib.rs`).

DomainValidator parses eligible entities and changed controls/checkpoints, checks supported fact kinds, summary fact references and known suppression targets. Its comments claim checkpoint non-regression and parent-only supersession, but the inspected validator does not compare candidate and parent checkpoints or supersession targets; it merely parses the checkpoint and then discards it. Consolidation itself advances a checkpoint. This report does not attribute those broader invariants to generic publication (SRC-1, `src/validate.rs`, `src/consolidate.rs`).

**3. Human review is skill policy, not a universal executable gate.** The skill says to confirm forgetting/erasure and show tidy findings before applying. Direct CLI erase and `tidy --apply` call the implementation without a confirmation exchange. Tidy recomputes candidates on apply, including new model judgments; a previous preview is not an immutable approved candidate list. Human keep-ID exclusions are supported, but actual per-content human approval is unresolved unless the external host follows the procedure. Forget suppresses curated fact reads; it does not redact raw source events or remove Git history. Combined search still searches raw events. Erase is the separate destructive path (SRC-1, `skills/mem/SKILL.md`, `src/cli.rs`, `src/tidy.rs`, `src/ops.rs`, `src/erasure.rs`).

**4. Git atomicity does not cover every durable effect.** Task updates use a separate lock and expected-version check but truncate/write `tasks.json` in place. Writeback writes the target file outside the repository publisher and `--force` replaces the whole file. Erasure publishes current-tree deletion first, then redacts the journal, rewrites history and removes intents; these are sequential effects, not one cross-substrate transaction. The deletion is marked completed before the later stages finish. If a later stage fails, re-running after the fact has left the current tree cannot reconstruct its original source references from that tree. Successful irreversible cleanup and crash recovery for that partial state are not established (SRC-1, `src/ops.rs`, `src/cli.rs`, `src/erasure.rs`).

### Guarantees, grants and isolation

| Guarantee and owner | Enforcement and strength | Covered paths and required contract | Alternate path or limit | Conclusion statuses |
|---|---|---|---|---|
| No stale-base overwrite; GitRepo | Candidate validation followed by Git ref CAS; invariant of cooperating publication | Shipped change, consolidation, tidy and current-tree erasure use the publisher. Requires Git ref-update atomicity and callers honoring returned conflicts. | Direct external ref/file mutation is not mediated; erasure's later substrate changes are not transactional. | implementation: wired; operation: uninspected |
| Domain checks; shipped callers/DomainValidator | Parser, reference and suppression checks before publication; protocol | Shipped calls explicitly pass DomainValidator. Requires parser and Git behavior. | Library custom validators can change policy; checks do not prove truth, parent-only supersession or checkpoint monotonicity. | implementation: wired; operation: uninspected |
| Interrupted immediate-change recovery; change module | Durable intent, receipt replay or stale set-aside; protocol | CLI and shared operation change handlers recover before applying another change. Requires surviving filesystem/Git state. | Direct `change::apply` does not automatically call recovery; consolidation/tidy lack that immediate-change intent step. | implementation: wired; operation: uninspected |
| HTTP local exposure; HTTP server | Reject non-loopback bind address; invariant of `bind_listen` | HTTP bind through Server. Requires host networking boundaries. | No authentication; local callers can issue writes. MCP, CLI and library are different access channels. | implementation: wired; operation: uninspected |
| Memory-shell command confinement; shell | Finite dispatch; no host-shell execution of input; invariant of this interpreter | `mem shell` command lines. | Host Bash, Git wrapper, hook subprocesses and library extension code are not confined by this interpreter. | implementation: wired; operation: uninspected |
| Hooks do not intentionally block on ordinary returned errors; hook module | Swallow Result errors, optional debug output; best effort | Hook run catches implementation errors; setup requests 10-second host hook timeouts. | Panics, process hangs and host timeout enforcement are not proved covered. Sync is detached and child status is ignored. | implementation: wired; operation: uninspected |

HTTP's local trust requirement is explicit:

> - HTTP binds loopback only and has no other authentication; run it only on machines you trust.
> --- `README.md`

The capability surface includes host-file reads, bare-Git publication, journal writes, task writes, instruction-file writes, remote model requests, history rewriting, model downloads and host configuration changes. Current grants are the OS permissions, environment credentials, chosen root and host tool permissions of a particular process; no deployed grant set is supplied. The deployed isolation envelope is uninspected. Loopback binding, path validation and shell parsing are not an OS sandbox. The Git wrapper strips inherited GIT variables, disables global/system config, hooks and signing for its commands, but it does not isolate the entire process (SRC-1, `src/git.rs`, `src/cli.rs`, `src/http_serve.rs`, `src/setup.rs`). Its timeout field and comments also do not establish a deadline: inspected `run_raw` calls `wait_with_output` without using that field (SRC-1, `src/git.rs`).

Material alternate paths inspected were direct CLI/model handlers, shared operations behind MCP/HTTP/shell, public library/custom-validator entry, detached hook subprocesses and durable maintenance/file writes. There is no inspected provider-native tool execution in the chat request: the payload contains model, temperature, response format and messages. This is a statement about that request, not about inaccessible provider internals (SRC-1, `src/consolidate.rs`).

Added source coverage beyond the boundary's initial tracing includes `src/git.rs` command construction/waiting, `src/validate.rs` actual checks, `src/repo.rs` validator extension and receipt/CAS implementation, `src/ops.rs` replay short-circuit and task I/O, `src/search/laya.rs` model selection/pull, detailed cleanup/erasure sequencing, and `src/evaluation.rs` oracle scoring. These are implementation evidence under SRC-1, not newly registered sources. Supporting source tests were not executed; all supplied execution, concurrency, latency and benefit evidence remains unobserved.

Change admission is captured in the routes below. Knowledge content changes through extraction, assertions, cleanup and erasure; instruction and host-integration changes through writeback/setup; inference component selection through environment/cache configuration. Public Rust APIs afford embedding and custom validation, not a demonstrated dynamic plugin loader. Product source/binary revision is supplied externally; no inspected route here justifies attributing autonomous product revision to the target. Memory-revision semantics and wider theory mappings remain for the specialist reports.

## Shared records

### Components

#### RT-CMP-llm-config
Label: Extraction and cleanup chat model

Source-native identity: `LlmConfig`, shared by consolidation and tidy. Representational form: distributed-parametric model; accessed through symbolic JSON chat requests carrying natural-language guidance and event/fact text. Storage substrate: unfrozen provider model state; configuration comes from environment/dotenv. Default is `anthropic/claude-haiku-4.5` at an OpenRouter-compatible chat URL; model and base URL are replaceable. Parameters are not trained or updated by the inspected client; provider-side changes are uninspected. Exact weights/version are not pinned. A mutable endpoint/model name can resolve to another implementation. Provider internals and service retention remain uninspected (SRC-1, `src/consolidate.rs`, `src/tidy.rs`).

> model: std::env::var("MEM_LLM_MODEL")
>     .ok()
>     .filter(|v| !v.is_empty())
>     .unwrap_or_else(|| "anthropic/claude-haiku-4.5".into()),
> --- `src/consolidate.rs`

#### RT-CMP-jev-reranker
Label: JEV remote relevance scorer

Source-native identity: `JevReranker`. Representational form: distributed-parametric provider model; symbolic score response consumed by ranking code. Storage substrate: external provider; URL, credentials and model selected from environment/dotenv. Default `~typesafe/jev-latest` is explicitly an alias, not an exact weight pin. Inspected scoring performs inference, not parameter updates; provider mutation remains uninspected. URL/model substitutions can resolve to another model. Query and candidate statement are clipped and sent in one Decisions call per document (SRC-1, `src/jev.rs`, `src/search/rerank.rs`).

> const DEFAULT_MODEL: &str = "~typesafe/jev-latest";
> --- `src/jev.rs`

#### RT-CMP-laya-reranker
Label: Cached local cross-encoder

Source-native identity: `LayaReranker`, wrapping fastembed `TextRerank`. Representational form: distributed-parametric weights; symbolic numerical ranks/scores are returned. Storage substrate: local `.models` cache and an in-process mutex-protected inference object. BGE base, Jina turbo English and BGE v2 m3 are selectable. The inspected client does not train parameters. Model family names are specified, but exact weight revisions/digests are not pinned in the inspected initialization; dependency/provider resolution is unfrozen. No remote mutable inference endpoint is used for local scoring; downloads and environment/selected-file changes can replace the chosen model (SRC-1, `src/search/laya.rs`).

> RerankInitOptions::new(model.fastembed())
>     .with_cache_dir(cache_dir.to_path_buf())
>     .with_show_download_progress(false),
> --- `src/search/laya.rs`

### Operative objects

#### RT-OBJ-mem-skill
Label: Shipped host-agent memory procedure

Source-native identity: `skills/mem/SKILL.md`, embedded and installed by setup. Representational form: natural-language procedure and examples interpreted by a host model, with symbolic skill metadata interpreted by the host. Storage substrate: tracked Markdown, embedded binary string and installed skill file. Its review/confirmation statements are procedural guidance, not an executable approval token. Static shipped guidance is not later read-back accumulated through use (SRC-1, `skills/mem/SKILL.md`, `src/setup.rs`).

> **Clean up** (`/mem tidy`, or when memory looks noisy): run `mem --output-format text tidy`. It lists duplicates and facts that only described one session. Show the list to the user, ask which (if any) to keep, then run `mem tidy --apply --keep <ids to keep>`. Never apply without the user seeing the list.
> --- `skills/mem/SKILL.md`

#### RT-OBJ-tasks
Label: Separate versioned task file

Source-native identity: `TaskFile` in `tasks.json`. Symbolic JSON version/ID fields govern concurrency; natural-language titles are returned for host interpretation. Storage substrate: ordinary file in the memory root, outside `memory.git`, with `tasks.lock`. Source lineage is caller-provided titles, not consolidation. The separate task state is not subject to Git candidate validation/receipts (SRC-1, `src/ops.rs`).

> let path = root.join("tasks.json");
> let mut out = OpenOptions::new()
>     .create(true)
>     .write(true)
>     .truncate(true)
>     .open(&path)
> --- `src/ops.rs`

### Routes

#### RT-RTE-journal-consolidation
Label: Journal events to published facts

Owner/endpoints: CLI consolidation loop or library caller → Consolidator → rules or [RT-CMP-llm-config](#rt-cmp-llm-config) → Git publisher. Trigger: new journal events beyond checkpoint, manual command or hook threshold. Each batch owns the next step, with CLI repetition until caught up. Context is a base revision, existing entities, controls and scope-filtered bounded event window. Model inputs use user text and Note-role memory files, stripping known harness injection and excluding other roles; software handles IDs, statement bounds, ordered source matching of normalized evidence fragments of at least eight characters (discarding shorter fragments and rejecting an empty qualifying set), suppression and duplicate placement. LLM batches run in parallel using a pre-batch existing-entity summary.

Proposal guidance is the shipped lasting-fact extraction prompt. Model proposes sentences and judges `lasting`; regex rules propose a narrower set when selected. Software decides admission; no per-fact human approval is required. The caller can choose extractor/high-water/scope or not start the process, but that is not per-content approval. No answer oracle supplies a reference true fact. Operating mode is open extraction over accumulated events, triggered by lag, not a bounded experiment. Candidate failures are rejected/quarantined; model/API failures retry three times with a 120-second request timeout, then abort without publishing that batch. Oversized entity-change batches fail and request a smaller high-water. CAS conflicts require re-read/reconciliation; no automatic concurrent merge is established. Facts, index, dispositions and advanced checkpoint persist in one published candidate. Previously committed batches remain after a later failure. Historical Git snapshots provide retained prior state; the loop does not automatically undo a committed batch (SRC-1, `src/cli.rs`, `src/consolidate.rs`, `src/repo.rs`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Batch report/revision; CLI totals when caught up or revision after an explicitly named single batch.
- Later read-back: Later batches reload facts, controls and checkpoint; retrieval/hooks/writeback consume published entity statements.
- Delegated visibility: Provider sees bounded selected event text and known-entity summary; host readers see published facts and dispositions through applicable interfaces, not internal provider processing.
- Selection predicate: Events after checkpoint within high-water, then scope; extractor role/text eligibility and candidate gates. The global window checkpoint advances even when scope drops events.
- Invalidation or expiry: Suppression/deletion IDs block placement; updated memory files can supersede facts sourced only from older versions; candidate failures do not enter the snapshot.
- Activation or effect: Code wires validated publication and later delivery; actual changes to host behavior are uninspected.
- Evidence limits: Implementation/requested model judgment only; occurrence of qualifying normalized fragments does not prove every submitted fragment occurs, statement entailment, lasting usefulness or model compliance.

> if !quote_found(&event.content, evidence) {
>     return Err("evidence not found in the cited event");
> }
> --- `src/consolidate.rs`

The every-fragment comment overstates the actual gate: the implementation below discards short normalized fragments before ordered matching (SRC-1, `src/consolidate.rs`).

> .map(normalise)
>         .filter(|f| f.chars().count() >= 8)
>         .collect();
> --- `src/consolidate.rs`

For example, source `Alpha beta gamma` and evidence `Alpha beta gamma...NO` pass this occurrence check despite unmatched `NO`; this is a code deduction, not an observed model output.

#### RT-RTE-memory-retrieval
Label: Shared facts and journal search

Owner/endpoints: Caller question → shared operation/combined_search → lexical facts and raw journal → optional remote/local ranking → result to caller. Scope/session supplied to operation dispatch are not an authorization filter on every search. A project filter is optional. The fact query is condensed to 200 characters; candidate retrieval is capped before project filtering, so filtering can discard otherwise useful shortlist slots rather than search the whole project corpus. The journal uses the original query and its own filters. Candidates interleave; ranker errors/declines fall through JEV → cached local model → lexical baseline. Direct callers can turn reranking off, and hooks use facts-only lexical search (SRC-1, `src/ops.rs`, `src/search/rerank.rs`).

Computational selection belongs to lexical/ranking code and [RT-CMP-jev-reranker](#rt-cmp-jev-reranker) or [RT-CMP-laya-reranker](#rt-cmp-laya-reranker). Human/agent caller supplies query/filter, then decides how to use results; there is no answer oracle here. Operating mode is open retrieval, not evaluation. No retained knowledge admission occurs in this read route. Error recovery is fallback for rerank failure; base loading or journal failure returns an error rather than proving no relevant memory.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Hit IDs, entity IDs, statements, scores, source locations, revision, ranker and judged metadata; read/history return selected content with status labels.
- Later read-back: Explicit query or ID lookup reloads retained entities/journal in a later invocation; this route itself accumulates no new durable result.
- Delegated visibility: Remote JEV receives clipped query and candidate statements; caller/host receives a truncated hit list, not the full memory corpus.
- Selection predicate: Lexical shortlist, status/suppression eligibility on facts, optional project/source filters, journal selection, then ranker and limit.
- Invalidation or expiry: Reloading uses current published controls and snapshot; fact read/history omit suppressed/deleted IDs. Raw journal is a separate source not redacted by soft forget.
- Activation or effect: Delivered text can inform a host answer; exercised influence and answer quality are uninspected.
- Evidence limits: Ranking scores are judgments, not verification; separate fact and journal scores/order plus truncation bound what reaches the consumer.

> if let Some(project) = p.project {
>     let project_id = format!("w_{}", crate::consolidate::slug(project));
>     fact_hits.retain(|h| project_entity_includes(&h.entity_id, &project_id));
> }
> --- `src/ops.rs`

#### RT-RTE-immediate-change
Label: Caller assertion, correction or soft forget

Owner/endpoints: CLI or MCP/HTTP/shell caller → ChangeRequest → durable intent → validated publication → result. Requests carry entity, fact/target, request ID, scope/session and reason. Caller proposes actual content; software decides structural admissibility. A generic live-agent/caller label does not prove human authorship or approval. Guidance comes from the host skill and caller problem, not a new model decision inside change::apply. No answer oracle is consulted. Operating mode is open user/agent requests. Correction supersedes an old fact, remembering upserts a fact, forgetting retracts and adds suppression. Shared ops creates explicit assertions without source refs; CLI constructs a user-role source ref from the supplied statement. Neither performs the extraction evidence-matching check (SRC-1, `src/ops.rs`, `src/cli.rs`, `src/change.rs`).

Admission/rejection: request validation, path/change budgets, DomainValidator and publisher CAS on shipped calls. Recovery before the next CLI/shared change retries durable intents, accepts already-published receipts or renames conflicting ones stale. Previous Git state remains available; no automatic semantic rollback is implemented by this route. Core publisher receipts compare canonical digests, but the shared operation's early receipt lookup bypasses that comparison. Public library callers can call apply without prior recover_in_dir (SRC-1, `src/change.rs`, `src/repo.rs`, `src/lib.rs`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Revision, request/change/target and replay outcome; shared operations additionally report supplied statement and stored count, including their early replay shortcut.
- Later read-back: Updated entity/index/controls are reloaded by retrieval, consolidation, hooks and writeback; intents are consumed by later recovery.
- Delegated visibility: Transport client receives outcome; no internal model delegation occurs in this route.
- Selection predicate: Caller-selected entity and fact/target ID; current snapshot lookup and request-ID receipt lookup.
- Invalidation or expiry: Correction supersedes; soft forget retracts/suppresses current fact reads while preserving raw journal and Git history.
- Activation or effect: Candidate enters published memory; subsequent host reliance remains uninspected.
- Evidence limits: Structural acceptance is not claim verification. Incoming-content equality on replay is not established by shared ops' receipt-only short-circuit.

> // Persist a durable intent so retries can recover the original base.
> let intent = Intent::new(&request.request_id, base, &change_set)?;
> repo.write_intent(&intent)?;
> --- `src/change.rs`

> validator.validate(self, &candidate, &changed_paths)?;
> 
> // Compare-and-swap on the published branch.
> let update_result = self
>     .git
>     .run_args(&["update-ref", MEMORY_REF, &candidate, base], None, None);
> --- `src/repo.rs`

#### RT-RTE-host-hooks
Label: Unsolicited context and detached sync

Owner/endpoints: Host SessionStart/UserPromptSubmit/SessionEnd callback → hook → context JSON or detached `mem hook sync`. Cwd chooses store/project; Start reads pref_user and a status count, Prompt uses up to 600 query characters and lexical facts-only candidates. Sync launches shipped backfill-local, then consolidation when waiting count reaches configured threshold and LLM extraction is configured. Default threshold is 200; zero disables auto-consolidation. Subprocess outcomes are ignored. Host owns callback timing, context interpretation and continuation; hook does not own the agent's action loop (SRC-1, `src/hook.rs`, `src/setup.rs`). Knowledge admission by background sync is [RT-RTE-journal-consolidation](#rt-rte-journal-consolidation); invocation requires no per-content human approval. Operating mode is automatic callbacks. No answer oracle.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Start/Prompt can emit hookSpecificOutput.additionalContext; End launches sync and returns without waiting for completion; errors yield no ordinary context.
- Later read-back: Start reloads up to 20 preference statements; Prompt selects previously published statements; sync can produce facts consumed in later sessions.
- Delegated visibility: Host model receives a context preamble and selected statements; background subprocesses share cwd/environment/root, not a demonstrated separate sandbox.
- Selection predicate: Prompt skips slash commands and fewer than three words, then requires meaningful-word overlap and caps delivery at six facts; Start requires active-fact count and reads pref_user.
- Invalidation or expiry: Each callback reloads current state; no independent delivered-context revocation after a host has received it is established.
- Activation or effect: JSON delivery and sync launch are wired; host scheduling, actual context activation and completion are uninspected.
- Evidence limits: Hook errors are swallowed; debug output is optional, and detached child's output/status is not a successful-sync trace. Its local-backfill child relies on best-effort drop flushing rather than propagating final-flush failure.

> let out = json!({"hookSpecificOutput": {"hookEventName": name, "additionalContext": text}});
> --- `src/hook.rs`

#### RT-RTE-instruction-writeback
Label: Published statements to project instruction file

Owner/endpoints: Caller writeback command → current entities → formatted managed block → caller-chosen file, usually AGENTS.md. Proposed content comes from retained fact statements. Software selects/forms the block; human/agent chooses target, project/all/include-file-facts/force options. No individual fact approval or truth oracle is enforced. Guidance is the shipped writeback convention; persistence is a project file outside the Git memory publisher. Open maintenance request mode (SRC-1, `src/cli.rs`, `skills/mem/SKILL.md`).

Selection omits superseded/retracted/expired statuses, filters by visibility, and by default avoids facts sourced only from instruction files. Local-store default can include all entities; shared-store default selects project/spills and pref_user. Formatting merges humanized bucket headings and copies fact IDs/statements. Default splicing preserves text outside a recognized marker pair or appends a block; force skips existing text and replaces the file. I/O errors reject completion, but no atomic rename, automatic rollback or publisher validation protects this target write. A user/source-control system may recover the previous file externally.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Count and target path after file write.
- Later read-back: A later host instruction-file load can receive the generated statements; backfill may also ingest the changed instruction file.
- Delegated visibility: Any host/file reader with access receives the written block; actual host loading is external and uninspected.
- Selection predicate: Store/project/all options, status/visibility and file-only source exclusion; include-file-facts overrides the latter.
- Invalidation or expiry: Re-running replaces the managed block; no automatic revocation of already loaded instructions. Force replaces the whole file.
- Activation or effect: Writes natural-language instruction/context content to a future host consumption surface; behavior change is not observed.
- Evidence limits: Neither atomic Git publication nor skill promises about outside-block preservation apply to the force path; generated text is not independently verified.

> // An existing file keeps its hand-written content; only the managed
> // block between the markers is replaced. `--force` replaces the whole file.
> --- `src/cli.rs`

#### RT-RTE-tidy-maintenance
Label: Recomputed cleanup and optional suppression

Owner/endpoints: Caller tidy → current active unsuppressed facts → duplicate rules plus optional [RT-CMP-llm-config](#rt-cmp-llm-config) session-only judgments → findings or one suppression commit. Trigger is manual cleanup/noisy memory. Software compares word overlap/containment with longest statements first; model flags session-only IDs in batches of 60. The cleanup prompt defines lasting usefulness and tells the model to leave uncertain IDs out. These are judgment criteria, not an answer oracle. Open maintenance mode, not a held-out experiment (SRC-1, `src/tidy.rs`).

Computation proposes IDs; caller chooses apply and keep exclusions. [RT-OBJ-mem-skill](#rt-obj-mem-skill) requests human review but direct CLI/library applies without proving that review happened. Apply recomputes, not loads a saved preview. Rejection comes from keep IDs, parse/model errors and DomainValidator/CAS. Model failures use shared chat retries; no publication occurs before findings are ready. Retraction reasons, controls, entities and index persist together; Git history preserves prior facts, but no automatic rollback follows. No durable-intent recovery equivalent to immediate change is wired here (SRC-1, `src/tidy.rs`, `src/cli.rs`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Findings/counts, whether session-only checking was performed and optional applied revision.
- Later read-back: Later retrieval/cleanup/consolidation reload suppression and retracted facts; a preview report alone is not reloaded as the apply candidate.
- Delegated visibility: LLM sees remaining fact IDs/statements, not their full original evidence records; caller sees findings and duplicates' kept IDs.
- Selection predicate: Active unsuppressed/undeleted facts; duplicate family/overlap; returned session-only IDs limited to the current batch; caller keep exclusions.
- Invalidation or expiry: Apply suppresses/retracts selected facts; later cleanup works from a newly read head.
- Activation or effect: Durable read eligibility changes; correctness of removed/kept distinctions and downstream benefit are uninspected.
- Evidence limits: No key skips session-only checks; requesting lasting judgments does not prove reliable semantic classification or preview/apply identity.

> if apply && !report.findings.is_empty() {
>     report.applied_at = Some(forget_all(repo, &head, entities, controls, &report.findings)?);
> }
> --- `src/tidy.rs`

#### RT-RTE-erasure-maintenance
Label: Sequential destructive erasure

Owner/endpoints: CLI/library target fact/entity → current-tree deletion/control publication → journal source-event redaction → branch-history rewriting/pruning → intent deletion. Caller proposes target/reason and owns the decision to invoke. Skill requests prior confirmation, but implementation has no confirmation exchange. No answer oracle/model decision. Operating mode is open destructive maintenance; objective is removal of identified content, not model improvement (SRC-1, `src/erasure.rs`, `src/cli.rs`, `skills/mem/SKILL.md`).

Software rejects empty/unknown targets, invalid candidates and failed I/O/Git operations. It stores Completed deletion records before later stages and derives source-event IDs from removed current facts. History scrubbing matches IDs/statements/evidence material through its scrubbers, expires reflogs and prunes unreachable objects. Effects are irreversible by design within the store; external backups/host copies/source files are outside that guarantee. Failure after tree publication can leave partially completed cleanup. Retry is afforded, but original source facts/references may already have disappeared, preventing an unqualified crash-recovery guarantee for all stages (SRC-1, `src/erasure.rs`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: On completion, erased fact IDs, counts for journal/history/intents and final revision; errors can follow earlier durable effects.
- Later read-back: Deleted/suppressed IDs affect future consolidation and fact reads; later journal/history consumers can receive scrubbed content if those stages complete.
- Delegated visibility: Git subprocesses perform history rewrite; external agent transcripts, prior returned results and previously written instruction blocks are not updated by this route.
- Selection predicate: Caller target matches fact or entity; associated source-event IDs and scrub needles derive from removed current facts.
- Invalidation or expiry: Deletes current facts, redacts cited source events, rewrites memory-branch history and removes matching pending intents; no general expiry rule.
- Activation or effect: Removal is wired across these sequential stores; successful complete destruction and downstream effects are uninspected.
- Evidence limits: No observed irreversible-erasure/crash/concurrency result; completion flag is not proof of all later stages, and external copies remain outside scope.

> // Step 2: journal.
> let events_redacted = journal.redact(&source_events)?;
> 
> // Step 3: history.
> --- `src/erasure.rs`

#### RT-RTE-task-update
Label: Separate task admission

Owner/endpoints: MCP/HTTP/shell operation → locked tasks.json version check → append title/new ID → return task list. Caller supplies title and expected version; software admits only matching versions. Generic caller identity does not resolve human approval. Guidance is operation schema; no model or answer oracle. Open requests add task content outside curated knowledge (SRC-1, `src/ops.rs`, `src/mcp.rs`).

Rejection: missing arguments/stale version/I/O errors. Lock coordinates reads and updates, but in-place truncation/write/fsync is not an atomic file replacement. No Git receipt, durable intent or automatic rollback is supplied for tasks.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: New version/list, or conflict with current version/list.
- Later read-back: Later tasks_read reloads retained titles/version under the same lock.
- Delegated visibility: Transport client/host receives task list; no internal model delegate.
- Selection predicate: Caller expected_version must equal current file version; no content relevance selector.
- Invalidation or expiry: No expiry/removal operation in this inspected append path; version advances on admitted updates.
- Activation or effect: Durable task title can inform later host work; exercised task execution is uninspected.
- Evidence limits: Version concurrency is wired, not crash-atomic multi-store publication or verified human task approval.

> file.version += 1;
> file.tasks.push(TaskItem {
>     id: format!("t_{}", file.version),
>     title: title.clone(),
> });
> --- `src/ops.rs`

#### RT-RTE-integration-admission
Label: Host setup and inference component configuration

Owner/endpoints: Caller setup target/remove → host config/installed skill; caller models pull → cached cross-encoder/selected-model file; environment model/URL overrides → next model client. These are distinct effects grouped as caller-controlled deployment/configuration admission, not a model-driven self-modification loop. Source-native setup registers Claude hooks/MCP/skill and Codex MCP. Setup invokes host CLI for Claude MCP registration. Model pull restricts names to supported families and initializes the downloaded model before recording its selection (SRC-1, `src/setup.rs`, `src/cli.rs`, `src/search/laya.rs`, `src/consolidate.rs`, `src/jev.rs`).

Caller chooses changes; software validates/parses supported settings and handles I/O/provider load failure. Setup backs up changed configuration files where implemented and supports remove; model selection can be changed again through environment/pull. Installation is not authenticated per-content human approval, and no automatic independent quality comparison gates a model replacement. Guidance is shipped integration configuration/model family mapping, not learned method text. Mode is explicit configuration; no answer oracle. Actual product source/binary updates and provider training lie outside these routes.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Setup action report or model download/status message; environment configuration is read when constructing clients.
- Later read-back: Host later loads installed configuration/skill; search reads selected-model file/cache on subsequent invocations. Environment changes affect later client creation, not retained experience-derived memory.
- Delegated visibility: Host gets executable hook/MCP configuration and skill; weight loading is delegated to fastembed/provider dependencies.
- Selection predicate: Caller target/remove/model choice, supported model-name parser, environment precedence and cached-model availability.
- Invalidation or expiry: Remove uninstalls configured integration; env/selection changes replace chosen inference component; no automatic cache expiry is established.
- Activation or effect: Enables future callbacks/tools and changes which inference component can score/propose content; actual host/model operation remains uninspected.
- Evidence limits: Installed configuration is not proof of host execution; family labels/load success are not exact weight pinning or measured quality admission.

> let selected = cache_dir.join(SELECTED_FILE);
> std::fs::write(&selected, model.name()).map_err(|e| Error::io(&selected, e))
> --- `src/search/laya.rs`

#### RT-RTE-search-evaluation
Label: Rubric comparison without automatic promotion

Owner/endpoints: Caller evaluate/rubric → lexical and reranked shared search → expected-ID/string checks → comparative report. Caller supplies a JSON rubric, whose authorship and independence are unresolved; software decides each pass by expected IDs and required/forbidden strings in returned statements. This is an actual answer oracle for a bounded retrieval test, not model judgment of truth. The operating mode is caller-specified bounded cases. Trigger is manual evaluation, not an automatic production update (SRC-1, `src/evaluation.rs`, `src/cli.rs`).

No candidate knowledge/model/product change is admitted by evaluation. It reports results but does not install a winner or alter memory. Missing/empty/invalid rubric or search failures reject report completion. Reranked is omitted when no ranker actually judges. The comparison operates over search calls and does not itself independently authenticate a held-out dataset or isolate every component effect.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Lexical and optional reranked case scores, passes, recall and ranks.
- Later read-back: inapplicable — evaluator does not write a retained comparison consumed by a later production decision in the inspected route.
- Delegated visibility: Search providers receive query/candidate text as in retrieval; caller receives aggregate/case report.
- Selection predicate: Caller rubric questions/project filters and hit limit; expected IDs, required and prohibited strings determine pass.
- Invalidation or expiry: inapplicable — transient evaluation report has no production expiry/admission state.
- Activation or effect: Comparative scoring is wired; no automatic model promotion, knowledge revision or observed quality improvement follows.
- Evidence limits: No supplied evaluated run, provenance proof or causal experiment; report logic alone establishes neither effective retrieval nor component-specific benefit.

> passed: recall && includes_ok && excludes_ok,
> --- `src/evaluation.rs`

### Claims

#### RT-CLM-validated-publication
Label: Model never writes directly and concurrent writer cannot overwrite

Claimed operation: published changes pass validation and compare-and-swap. Source is product trust documentation. Implemented support and alternate-path limits are [RT-RTE-journal-consolidation](#rt-rte-journal-consolidation) and [RT-RTE-immediate-change](#rt-rte-immediate-change). Strong support applies to the cooperating Git publisher, not all file effects or custom library policies (SRC-1, `README.md`, `src/repo.rs`, `src/lib.rs`).

> - The model never writes memory directly: changes go through `memory_request_change` or consolidation, are validated, and publish with compare-and-swap on the `memory` branch, so a concurrent writer can never overwrite another's commit.
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-host-context
Label: Selected memory as host context

Consumer: external host model. Channel: requested search/read result or unsolicited hook additionalContext. Force: natural-language information and procedural suggestions interpreted by the host; no target-level guarantee of compliance. Horizon: subsequent invocations/sessions can receive retained statements, with callback timing and loading determined externally. [RT-RTE-memory-retrieval](#rt-rte-memory-retrieval) and [RT-RTE-host-hooks](#rt-rte-host-hooks) establish selection/delivery boundaries, not activation or benefit (SRC-1, `src/ops.rs`, `src/hook.rs`).

> let mut text = String::from(
>     "Relevant project memory (mem; recorded from earlier sessions and AGENTS.md, so check against the code if it may have changed):\n",
> );
> --- `src/hook.rs`

#### RT-BAP-instruction-file
Label: Generated memory through project instructions

Consumer: external agent that reads the target instruction file. Channel: persisted managed block with fact IDs/statements. Force: natural-language instruction/context, conditional on host loading and interpretation. Horizon: later sessions on that project until replacement or external editing. [RT-RTE-instruction-writeback](#rt-rte-instruction-writeback) establishes file creation and selection, not automatic loading or exercised reliance (SRC-1, `src/cli.rs`).

> out.push_str(&format!("- [{id}] {statement}{vis_tag}\n"));
> --- `src/cli.rs`

## Annotations

none
