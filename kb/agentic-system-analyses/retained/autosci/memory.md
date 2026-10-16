---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "AutoSci memory: filesystem wiki, lossy context compilation, negative-result reuse, recovery checkpoints and Hiera ledger replay."
run-id: AAS-2026-10-15-autosci-430df584df8f-01
source-identity: https://github.com/skyllwt/AutoSci
reviewed-boundary: f5c2fe009c6683b6aa5b668de759a0610c938aaf
---

# AutoSci memory report

## Boundary and evidence

AutoSci retains research knowledge as local files and asks an external coding agent to use them in later invocations. The memory boundary includes raw-to-wiki authoring, derived navigation/context, research and pilot verdicts, user/browser edits, lint/reset, initialization and research recovery, scheduled recommendation, and optional Hiera state. It does not include the host's internal conversation compaction, provider weights or undocumented provider retention. Installed skills and schema guide consumption but are not themselves accumulated experience. The supplied [RT-RTE-setup-skills](runtime.md#rt-rte-setup-skills) establishes installation authority, not experience read-back.

All source findings use SRC-1, the Git source registered in boundary.md, at f5c2fe009c6683b6aa5b668de759a0610c938aaf. HEAD matched that pin and the checkout was clean. Direct reads below add implementation and doctrine/design evidence; no target program, tests, providers or services were run. Actual compliance, later activation and benefit remain unobserved. Runtime findings are provisional inputs, not observed operation.

### Coverage inventory

Each path below belongs to SRC-1. “Direct” means bodies or named bounded source ranges inspected for this report; “supplied” means the runtime account supplies that finding. Available but uninspected bodies are not access failures.

| Entry point or memory operation | Source paths and inspection | Records, limits and conclusions prevented |
|---|---|---|
| Ingest and bootstrap; raw source preparation | Direct `.claude/skills/ingest/SKILL.md` source/authoring ranges; `.claude/skills/init/SKILL.md` checkpoint and fan-out searches; supplied preparation helpers and parallel protocol | [RT-RTE-knowledge-cycle](runtime.md#rt-rte-knowledge-cycle), [RT-RTE-parallel-ingest](runtime.md#rt-rte-parallel-ingest), [MEM-OBJ-wiki-pages](#mem-obj-wiki-pages). Acquisition helper internals not re-audited: cannot establish extraction fidelity or exhaustive source provenance. |
| Foundations admission distinct from paper ingestion | Direct `.claude/skills/prefill/SKILL.md` composition/admission instructions | [MEM-OBJ-wiki-pages](#mem-obj-wiki-pages), [MEM-RTE-foundation-seeding](#mem-rte-foundation-seeding). Wikipedia service internals and model fallback correctness uninspected. |
| CLI dispatch and exposed library operations | Direct `tools/research_wiki.py` complete parser/dispatch, graph projection/load/dedup, context, gap extraction, lifecycle and checkpoint bodies | [RT-CMP-research-wiki](runtime.md#rt-cmp-research-wiki), [MEM-RTE-context-compilation](#mem-rte-context-compilation), [MEM-OBJ-edges](#mem-obj-edges), [MEM-OBJ-citations](#mem-obj-citations), [MEM-OBJ-checkpoints](#mem-obj-checkpoints). `find`, similarity, neighbors, ready/orphan queries are exposed read capabilities; their presence alone does not identify a later consumer. Index/backfill bodies not fully audited; no completeness claim. |
| Ask selection and crystallization | Direct `.claude/skills/ask/SKILL.md` complete | [RT-RTE-knowledge-cycle](runtime.md#rt-rte-knowledge-cycle), [RT-OBJ-context-brief](runtime.md#rt-obj-context-brief), [MEM-OBJ-index](#mem-obj-index). Page selection is agent judgment, not an implemented semantic search service. |
| Idea filtering, pilot rejection and formal evaluation | Direct `.claude/skills/ideate/SKILL.md` searches and eliminated-idea writing; `.claude/skills/exp-pilot-eval/SKILL.md` result-to-verdict/update; `.claude/skills/exp-eval/SKILL.md` verdict/update body | [MEM-RTE-negative-memory](#mem-rte-negative-memory), [RT-RTE-research-verdict](runtime.md#rt-rte-research-verdict). Separate origins survive as prefixes; not every failed idea is an experimental refutation. |
| Review/refine; paper planning and later dissemination | Direct `.claude/skills/refine/SKILL.md` loop, searches in `.claude/skills/review/SKILL.md`, `.claude/skills/paper-plan/SKILL.md`, `.claude/skills/survey/SKILL.md`; remaining drafting/LaTeX/poster internals supplied or uninspected | [MEM-OBJ-wiki-pages](#mem-obj-wiki-pages), [RT-RTE-research-verdict](runtime.md#rt-rte-research-verdict). Review alone suggests; refine edits. Detailed downstream citation preservation/rendering not established. |
| Check, deterministic fixes, explicit edit and destructive reset | Direct `.claude/skills/check/SKILL.md`, `.claude/skills/edit/SKILL.md`, `.claude/skills/reset/SKILL.md`, `tools/lint.py` fixer dispatch/body, `tools/reset_wiki.py` | [MEM-RTE-memory-maintenance](#mem-rte-memory-maintenance). Structural repairs do not certify scientific truth; reset has residual stores. |
| Browser page/graph reads, metadata writes, lint/fix, discovery read-back | Direct `tools/serve.py` graph, lint and checkpoint endpoints/searches; metadata writes supplied | [RT-RTE-browser-write](runtime.md#rt-rte-browser-write), [MEM-OBJ-edges](#mem-obj-edges), [MEM-OBJ-checkpoints](#mem-obj-checkpoints), [MEM-RTE-memory-maintenance](#mem-rte-memory-maintenance). UI rendering internals not fully read; no observed human decision. |
| Scheduled intake and alternate recommender | Direct `tools/daily_arxiv.py` card/profile selection, `.github/workflows/daily-arxiv.yml` writeback, `.gitignore`; provider and CI branches supplied | [RT-RTE-daily-intake](runtime.md#rt-rte-daily-intake). Ignored generated data limits commit-based retention; consumer receives selected previews, not full corpus. |
| Hiera contract, immutable candidates, attempts, replay, scheduling and reporting | Direct `tools/hiera/cli.py` init/propose/loop/status/finalize, `tools/hiera/ledger.py`, `tools/hiera/experience.py`, `tools/hiera/acquisition.py`, `tools/hiera/scheduler.py`; evaluator/remote admission supplied | [RT-OBJ-task-contract](runtime.md#rt-obj-task-contract), [RT-RTE-hiera-search](runtime.md#rt-rte-hiera-search), [MEM-RTE-ledger-replay](#mem-rte-ledger-replay). Proposal/tuner internals not fully inspected; cannot establish exhaustive search policy or reasoned hypothesis revision. |
| Review MCP and hooks/configuration | Direct `.mcp.json`, `config/settings.local.json.example`, tool/thread searches in `mcp-servers/llm-review/server.py`; adapter bodies supplied | [RT-RTE-review-call](runtime.md#rt-rte-review-call). Inspected wiring exposes chat/chat-reply/search, not a wiki-memory tool. These configuration files do not declare a memory hook; no whole-tree absence claim. Host compaction and provider-private state remain opaque. |
| Alternative recovery forms | Direct checkpoint helpers; init/research/discover skill searches and browser checkpoint body | [MEM-OBJ-checkpoints](#mem-obj-checkpoints), [RT-RTE-parallel-ingest](runtime.md#rt-rte-parallel-ingest), [RT-RTE-research-verdict](runtime.md#rt-rte-research-verdict). JSON manifests, task checkpoints, Git commits and progress Markdown have different consumers and deletion rules. |

## Core ideas

1. **Full pages and selection aids are separate memory surfaces.** The brief is a deterministic, purpose-specific, lossy projection. `/ask` then chooses full pages using the question, index and compressed context. Omitted content remains on disk; it is not automatically present in the model window. See [MEM-RTE-context-compilation](#mem-rte-context-compilation) and the annotation on [RT-RTE-knowledge-cycle](runtime.md#rt-rte-knowledge-cycle).
2. **Rejection is retained rather than simply discarded.** Filter eliminations, pilot failures and formal experiment failures can all become failed idea pages. Specific reasons reach later ideation as a banlist, directly and through a bounded brief. This is a requested change in future selection, not evidence of better research performance. See [MEM-RTE-negative-memory](#mem-rte-negative-memory).
3. **Admission is plural.** Ingest, crystallization, foundations seeding, refinement, user-directed edit, browser metadata edits and unattended CI have different control rules. Writer policy does not unify them into enforced role authorization. See [RT-CLM-writer-contract](runtime.md#rt-clm-writer-contract) and [MEM-RTE-memory-maintenance](#mem-rte-memory-maintenance).
4. **Hiera's consequential retained feedback is the replayed ledger.** Best scores, budget use and bout counts affect later execution. The object called an experience snapshot is narrower: counts keyed by semantic point, constructed in memory, with only its digest exposed by the inspected CLI callers. It is not shown feeding the scheduler. See [MEM-RTE-ledger-replay](#mem-rte-ledger-replay).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-wiki-pages
Label: Wiki entity and output pages

Filesystem Markdown under `wiki/papers/`, `concepts/`, `methods/`, `topics/`, `people/`, `ideas/`, `experiments/`, `Summary/`, `foundations/` and `outputs/`. Prose hypotheses, explanations, summaries, criticisms and results are natural-language content. Identifiers, enum statuses, dates and links in frontmatter have symbolic consumption by Python and browser filters. A field such as `failure_reason` is text even when transported in YAML. This is neither a dense embedding store nor inspected model weights.

Lineage differs by part: paper pages are agent-authored interpretations of raw source and literature enrichment; concepts/methods consolidate papers; ideas combine gaps, source papers and model proposals; experiments retain setup/results and verdict updates; crystallized answers retain synthesis, original query and `source_pages`; foundations can combine Wikipedia and explicitly marked LLM analysis. Original raw files and these derived pages are not interchangeable. The generic provenance of an actual deployment's pre-existing pages is unresolved because only a scaffold is supplied. See SRC-1: `.claude/skills/ingest/SKILL.md`, `.claude/skills/ask/SKILL.md`, `.claude/skills/prefill/SKILL.md`, `.claude/skills/exp-eval/SKILL.md`.

> Body sections to populate, in this order: `Problem & Context`, `Key idea`, `Method`, `Experiment & Results`, `Limitations`, `Open questions`, `My take`, `Related`.
> --- `.claude/skills/ingest/SKILL.md`

Later model readers treat page content as evidence, hypotheses and proposed procedures, not as a verified answer oracle. Browser readers receive display content; compiler consumers receive selected metadata. Human authorship cannot be inferred from a generic CLI/browser caller. Local disk persistence is distinct from versioned retention: these generated directories are ignored in the shipped `.gitignore`. This object supplies the page substrate traversed by [RT-RTE-knowledge-cycle](runtime.md#rt-rte-knowledge-cycle) and [RT-RTE-research-verdict](runtime.md#rt-rte-research-verdict); it is distinct from their route identities, from [RT-OBJ-context-brief](runtime.md#rt-obj-context-brief)'s projection and [RT-OBJ-writers](runtime.md#rt-obj-writers)'s static policy. No supplied page-store object counterpart.

#### MEM-OBJ-edges
Label: Semantic and frontmatter-projected edges

Semantic relations persist as JSONL in `wiki/graph/edges.jsonl`. Endpoints/type/confidence/date are symbolic for traversal, deduplication and counts; free-text evidence is natural language for interpretation. Agent/tool callers author semantic assertions. Typed admission checks shape, not truth; malformed JSON is skipped by `load_edges`, whereas dedup preserves malformed lines. Dedup keeps the first canonical endpoint/type occurrence, so later alternative evidence for an identical key is not accumulated by that operation. SRC-1: `tools/research_wiki.py`.

The separately derived frontmatter graph is symbolic link projection, not another scientific judgment. `project_frontmatter_edges` traverses schema-declared link/list fields, skips terminal foundations and the `cited_by` cache, and emits `fm_*` relations. `rebuild-projected-edges` overwrites `wiki/graph/projected_edges.jsonl`; the browser instead computes projection live. Projection may preserve a target even when its file is missing. Browser graph responses combine semantic and projected edges, while compiler connectivity uses only `load_edges` and thus the semantic file. The same-looking graph view and context rank therefore do not necessarily use the same graph. SRC-1: `tools/research_wiki.py`, `tools/serve.py`.

> artifacts; serve.py reads them dynamically and does not need this file.
> --- `tools/research_wiki.py`

This retained graph is an input/output of [RT-RTE-knowledge-cycle](runtime.md#rt-rte-knowledge-cycle) and [RT-RTE-browser-write](runtime.md#rt-rte-browser-write), not a duplicate route or the [RT-CMP-research-wiki](runtime.md#rt-cmp-research-wiki) executor. No supplied graph-object counterpart. Consumers include query/traversal helpers, context ranking and browser display; actual model reliance is unobserved.

#### MEM-OBJ-citations
Label: Bibliographic citations

`wiki/graph/citations.jsonl` stores symbolic paper-to-paper `cites` relations with provenance labels, distinct from semantic claim support. Single/batch helpers append after source/identity checks; batch resolves known arXiv/S2 identities against existing paper pages. Citation dedup retains the first pair occurrence. Ingest requests reverse `cited_by` page metadata. These are bibliographic lineage/access structures, not evidence that the citer endorses a claim. SRC-1: `tools/research_wiki.py`, `.claude/skills/ingest/SKILL.md`.

> - Add a semantic paper-to-paper edge in `graph/edges.jsonl` only when the source text gives a clear cue. Edge-type selection is in `references/cross-references.md`. If no semantic relation cleanly fits, keep only the `cites` row.
> --- `.claude/skills/ingest/SKILL.md`

The browser returns citations separately and moves original citation provenance into `cite_source` when labeling the payload bucket. Context compilation does not read this file through `load_edges`. Distinct from [MEM-OBJ-edges](#mem-obj-edges), and a previously undeclared retained part used in [RT-RTE-knowledge-cycle](runtime.md#rt-rte-knowledge-cycle); no supplied object counterpart. Browser/code consumption is wired, model use remains procedural.

#### MEM-OBJ-open-questions
Label: Open questions gap map

Derived natural-language bullets in `wiki/graph/open_questions.md`, with symbolic source-type/stem labels. `rebuild_open_questions` extracts bullets under papers' `Open questions` and topics'/concepts' `Open problems`, including nested subsection bullets until the next H2. It does not synthesize a complete research-gap analysis, and ignores non-bullet prose and other entity directories. The resulting map is overwritten; source reasons can remain in full pages even where the map keeps only a bullet. SRC-1: `tools/research_wiki.py`.

> _collect_section_items(root / "papers",   "Open questions", gaps, "paper")
> _collect_section_items(root / "topics",   "Open problems",  gaps, "topic")
> _collect_section_items(root / "concepts", "Open problems",  gaps, "concept")
> --- `tools/research_wiki.py`

Ask/ideation and the brief compiler later consume the map as gap evidence/guidance, not enforced exclusion or verified truth. It is a separate precursor to [RT-OBJ-context-brief](runtime.md#rt-obj-context-brief), not a duplicate; [RT-RTE-knowledge-cycle](runtime.md#rt-rte-knowledge-cycle) is the closest supplied route.

#### MEM-OBJ-index
Label: Wiki index

Filesystem `wiki/index.md`: natural-language titles/descriptions and symbolic slugs/categories used as a page catalog. Ingest/crystallize/edit request navigation updates; `rebuild-index` exposes regeneration from entity directories. Ask uses question-keyword matching and model relevance to choose full files. Index membership is access metadata, not scientific acceptance. SRC-1: `.claude/skills/ask/SKILL.md`, `.claude/skills/edit/SKILL.md`, `tools/research_wiki.py`.

> Read `wiki/index.md`, match relevant slugs against question keywords
> --- `.claude/skills/ask/SKILL.md`

Distinct retained navigation input within [RT-RTE-knowledge-cycle](runtime.md#rt-rte-knowledge-cycle), not the [RT-OBJ-context-brief](runtime.md#rt-obj-context-brief) content summary. No supplied index object counterpart. Complete regeneration fidelity was not established by parser inspection alone.

#### MEM-OBJ-checkpoints
Label: Checkpoints and progress snapshots

Separate operative parts must not be conflated:

- `wiki/.checkpoints/{task_id}.json` holds symbolic completed/failed lists and metadata such as stash reference/base commit. Save deduplicates items within each list, not across both lists. Strict load surfaces malformed JSON; writer reads treat corrupt data as empty and can overwrite it on the next save. It preserves coordination state, not a conversation rationale.
- Root `.checkpoints/init-prepare.json`, `init-plan.json`, `init-sources.json` preserve prepared-source identity, shortlist/planning and canonical ingest order. These are not files under the task-checkpoint helper's wiki root. The parent also uses committed worktree branches as durable fan-in artifacts.
- `.checkpoints/discover-*.json` holds proposed paper shortlists. Browser list/read endpoints afford later user selection, sorted by mtime with a 2 MiB individual read cap. Listing is access metadata; full payload is returned separately, not inferred from a display title. It does not itself ingest a paper.
- `wiki/outputs/pipeline-progress.md` retains research stage, selected ideas/experiments and deployment state for `--start-from` in a later session. Malformed progress may be reconstructed from page statuses by instruction, not deterministic proof of the correct prior stage.

SRC-1: `tools/research_wiki.py`, `.claude/skills/init/SKILL.md`, `.claude/skills/discover/SKILL.md`, `.claude/skills/research/SKILL.md`, `tools/serve.py`.

> Creates the checkpoint file if it does not exist. Preserves the existing
> completed/failed lists. Designed for small pieces of cross-step state
> like the `/init` stash ref that must survive an interrupted run.
> --- `tools/research_wiki.py`

These filesystem objects are distinct from [RT-RTE-parallel-ingest](runtime.md#rt-rte-parallel-ingest) and [RT-RTE-research-verdict](runtime.md#rt-rte-research-verdict), which establish their consumer protocols; no supplied checkpoint object counterpart. JSON control fields have symbolic consumers, while manifests/research progress may also carry model-interpreted summaries. No host conversation checkpoint or host compaction payload was supplied. Ignored local retention is not cross-machine recovery.

#### MEM-OBJ-ledger
Label: Hiera ledger

Append-only `ledger.jsonl` in a Hiera run directory, with symbolic schema/versioned event IDs, candidates, reservations/releases, evaluations, tuning bouts and scheduler decisions. Candidate snapshots and attempt artifacts are separate retained payloads bound by IDs/digests; ledger metadata is not the candidate code or full stdout. The CLI initializes candidate/attempt/preflight/draft directories plus manifest, semantic space and contract. SRC-1: `tools/hiera/cli.py`, `tools/hiera/ledger.py`; supplied [RT-RTE-hiera-search](runtime.md#rt-rte-hiera-search) covers execution and receipt production.

> elif kind == "evaluation":
>     state[candidate_id]["evaluations"].append(dict(payload))
>     _update_best(state[candidate_id], payload)
> --- `tools/hiera/ledger.py`

Replay reconstructs best score/attempt and bout counts; reservation history determines used budget. Later scheduler/evaluator calls consume that derived state with executable authority over eligible candidates and resource spending. Status can repair missing attempt-bound deep bouts; immutable candidate replacement requires a new admitted child, rather than mutating the old snapshot. This object is distinct from [RT-OBJ-task-contract](runtime.md#rt-obj-task-contract)'s evaluation specification and [RT-RTE-hiera-search](runtime.md#rt-rte-hiera-search)'s containing route. No supplied ledger object counterpart.

#### MEM-OBJ-experience
Label: Hiera experience snapshot

A symbolic Python dictionary constructed by `build_snapshot`: counts of attempts, successes and failures keyed by candidate semantic `point_id`, plus schema version, `updated_at` and digest. It is derived from evaluation receipts and candidate metadata, not explanatory lessons or model parameters. No durable full-snapshot write is wired in the inspected callers: status prints an `experience_revision`; finalize stores that revision in `FINAL_REPORT.json`, alongside summary and coverage. SRC-1: `tools/hiera/experience.py`, `tools/hiera/cli.py`.

> "successes" if receipt.get("status") == "success" else "failures"
> --- `tools/hiera/experience.py`

The full dictionary is not what the CLI report consumer receives. Moreover, revision hashing includes a newly generated timestamp, so digest equality is not established as a stable ledger-content revision. No inspected scheduler call consumes this snapshot; it consumes replayed ledger candidates instead. Distinct from [MEM-OBJ-ledger](#mem-obj-ledger) and [RT-RTE-hiera-search](runtime.md#rt-rte-hiera-search), with no supplied experience-object counterpart. This narrows the boundary's general wording about experience summaries without denying the implemented counting transformation.

### Routes

#### MEM-RTE-context-compilation
Label: Context compilation and later delivery

Part of: [RT-RTE-knowledge-cycle](runtime.md#rt-rte-knowledge-cycle)

This is the deterministic projection subroute of the supplied knowledge cycle, not its ingest/answer admission route. Trigger: explicit CLI/skill rebuild or purpose compilation. Python reads retained pages, semantic edges and the separately retained gap map, selects metadata/bullets, overwrites the brief, and a later skill asks the model to read it. SRC-1: `tools/research_wiki.py`, `.claude/skills/ask/SKILL.md`.

- implementation conclusion status: wired
- doctrine conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: JSON status, purpose and character count; persisted context brief.
- Later read-back: Later ask/ideate/research/review instructions load the resulting file; Python delivery to those invocations is afforded through file reads, not an internal push service.
- Delegated visibility: Model sees only selected summaries unless it separately reads source pages; compiler itself makes no model call.
- Selection predicate: Purpose-specific section character budgets; methods/papers ranked by semantic-edge degree; at most 15 papers; failed/rejected ideas in filename order; recent 25 semantic edges; experiments and stale pages only for purposes with nonzero allocations.
- Invalidation or expiry: Each compile replaces the same brief path regardless of purpose. No per-purpose cache or automatic dependency-triggered invalidation established. Original pages remain reachable.
- Activation or effect: Code changes delivered context; skill requests use of it. Actual altered model choices and benefit are unobserved.
- Evidence limits: Character bounds are not token bounds. Source completeness, freshness of a pre-existing gap map and actual model loading are not guaranteed by compilation.

Budget tuple order is methods/gaps/failed/papers/experiments/edges/stale. General allocates 2000/1500/1500/2000/0/1000/0 characters. Ideation allocates 1500/2000/2000/1000/500/500/500; experiment, writing and review have different allocations. Assembly uses a global default of 8000 characters, includes headings and may truncate a section then stop. The compiler is an automatic selector *after a requested rebuild*, not unsolicited injection. Admission is the caller's rebuild request plus fixed selection code; no per-summary human approval or truth check. Recovery is rebuilding/re-reading originals. It discards detailed argument, experimental setup and semantic-edge evidence text from the brief, even though sources retain them.

> text = "\n".join(line for _, line in items2[:15])[:b_papers]
> --- `tools/research_wiki.py`

> chain_lines = [f"  {e['from']} --{e['type']}--> {e['to']}"
>                for e in edges[-25:]]
> --- `tools/research_wiki.py`

#### MEM-RTE-foundation-seeding
Label: Foundation seeding and deduplication reuse

No supplied route counterpart after comparison with [RT-RTE-knowledge-cycle](runtime.md#rt-rte-knowledge-cycle): this admits background without paper ingestion. User selects a domain/concept or the agent infers a domain from topics; the agent selects catalog seeds, skips existing files, fetches Wikipedia sections and composes terminal foundation pages. Subsequent ingestion is instructed to link to these rather than create duplicate textbook concepts. SRC-1: `.claude/skills/prefill/SKILL.md`; similarity capability in `tools/research_wiki.py`.

- doctrine conclusion status: claimed
- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: Created/skipped foundation summary, rebuilt index and log.
- Later read-back: Existing foundations are checked during subsequent seeding and candidate-concept deduplication; linked pages remain addressable for later reads.
- Delegated visibility: Foreground agent receives fetched sections or uses its own model knowledge on a missing page; no full external provider state is supplied.
- Selection predicate: Requested/inferred domain plus general catalog, or one explicit concept; selected Wikipedia section names; existing slugs skipped.
- Invalidation or expiry: Procedure never overwrites existing foundation pages. Later explicit editing/reset can change/remove them; no automatic source-refresh mechanism established here.
- Activation or effect: Requested avoidance of duplicate concept creation; actual deduplication outcomes unobserved.
- Evidence limits: Wikipedia and LLM portions have different lineage. Source labels do not establish factual correctness; helper internals and deployment compliance were not exercised.

Admission is model composition after workflow invocation, not per-page human approval; catalog is advisory. Wikipedia absence authorizes model fallback, not rejection of the seed. The page retains source URL or empty URL, plus visible LLM-analysis labels. No expected-answer oracle; this is open knowledge acquisition, not a benchmark.

> Exit code `2` from any call means **page not found** — fall back to LLM knowledge for that seed and set `source_url: ""` in the resulting frontmatter.
> --- `.claude/skills/prefill/SKILL.md`

#### MEM-RTE-negative-memory
Label: Negative-result retention and later ideation

Distinct cross-route memory chain spanning [RT-RTE-research-verdict](runtime.md#rt-rte-research-verdict) and [RT-RTE-knowledge-cycle](runtime.md#rt-rte-knowledge-cycle), not a second declaration of either. Producers include initial idea filtering, pilot evaluation and formal experiment evaluation. The model writes failed pages/reasons; helpers validate selected transitions; compiler selects failed metadata; later ideation reads failed ideas as a banlist. SRC-1: `.claude/skills/ideate/SKILL.md`, `.claude/skills/exp-pilot-eval/SKILL.md`, `.claude/skills/exp-eval/SKILL.md`, `tools/research_wiki.py`.

- doctrine conclusion status: claimed
- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: Filter/pilot/verdict report; retained failed idea and reason; formal evaluation may append an experiment-to-idea invalidates edge.
- Later read-back: Future ideation explicitly loads failures and checks candidate overlap; brief compilation supplies title/reason as additional anti-repetition context.
- Delegated visibility: Formal reviewer receives selected hypothesis, setup, full results and sibling summaries, not the entire execution trace. Later ideator can read full failed pages, while the brief preserves only title/reason subject to budget.
- Selection predicate: Filter similarity/novelty/review judgment, pilot clear-failure criteria, or synthesized formal not-supported verdict; later selection compares proposals against concrete failure reasons.
- Invalidation or expiry: Failed pages persist until explicit edit/delete/reset; lifecycle helper refuses terminal/invalid transitions. Compiler rebuild replaces summaries. No automatic withdrawal of old invalidates edges after manual page correction is established.
- Activation or effect: Intended change is avoidance or reframing of previously rejected approaches. Source wires metadata summarization and offers file writes; actual future dependence and improved capacity are unobserved.
- Evidence limits: A filter rejection is not a failed experiment; pilot failure is not formal confirmation; one-sentence reasons can lose scope and methodological qualifications.

The proposing/deciding agent differs by stage: ideation uses foreground and review judgments; pilot evaluation uses metrics/logs and a pilot spec including baseline expected value; formal evaluation uses model judgments about results. The pilot's reference value is task-supplied, not an independently supplied scientific answer oracle. Formal evaluation pauses for user confirmation unless `--auto`; pilot instructions request confirmation on borderline cases unless auto. Workflow invocation does not equal per-content approval for initial eliminated pages. The lifecycle helper requires a reason for failed transitions but direct metadata/file writes bypass that gate; reasons can still be scientifically wrong. Recovery is explicit editing/new ideas or new experiments, not automatic semantic rollback.

> These failed ideas become the banlist for future ideate runs
> --- `.claude/skills/ideate/SKILL.md`

> - The `[pilot]` prefix distinguishes pilot failures from `[filter]` eliminations (Phase 3) and post-experiment failures from `/exp-eval`
> --- `.claude/skills/exp-pilot-eval/SKILL.md`

Reasons are partly retained: eliminated pages keep motivation/hypothesis, specific failure_reason and brief expected-outcome/risks; formal experiment pages retain results and Idea updates, while the full terminal verdict report is not shown automatically persisted in its entirety. A promised Lessons learned section in ideation is not filled by an explicit common exp-eval step in the inspected body. Theory assessment is inherited only as evidence from [RT-RTE-research-verdict](runtime.md#rt-rte-research-verdict), not inferred from failed status: its separately stated conditions remain source-level affordances/requests. Under learning, retained negative guidance affords later feedback-sensitive action; improved capacity and causal benefit remain uninspected. No exercised self-improvement or automatic revision of AutoSci's own method follows from this chain.

#### MEM-RTE-memory-maintenance
Label: Memory repair and withdrawal

Distinct from initial admission in [RT-RTE-knowledge-cycle](runtime.md#rt-rte-knowledge-cycle); overlaps [RT-RTE-browser-write](runtime.md#rt-rte-browser-write) only where browser endpoints invoke existing helpers. Maintenance includes deterministic lint repairs, model review/refine, user-requested edits and destructive reset. SRC-1: `tools/lint.py`, `tools/serve.py`, `tools/reset_wiki.py`, `.claude/skills/check/SKILL.md`, `.claude/skills/edit/SKILL.md`, `.claude/skills/refine/SKILL.md`, `.claude/skills/reset/SKILL.md`.

- implementation conclusion status: wired
- doctrine conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Lint/fix reports, review/refinement reports, edit summaries or deletion plan/counts; changed page files and optional log records.
- Later read-back: Repaired/edited pages and regenerated aids reach later ask/ideate/review. Deleted files cannot be read through their original paths, but stale projections or separate stores can survive.
- Delegated visibility: Lint code receives local pages/schema; reviewer receives selected artifact/context; caller applies proposed semantic changes. Browser fix returns JSON without a coding-agent review round trip.
- Selection predicate: Lint fixes only marked xref-asymmetry/missing-field issues; refine applies review-recommended categories; edit targets user-requested content; reset enumerates chosen scopes.
- Invalidation or expiry: Fixes/edits persist until replaced. Reset unlinks selected files; derived context refresh is requested in selected workflows, not guaranteed for every direct writer.
- Activation or effect: Actual helper writes/deletions are implemented; successful downstream model correction or forgetting is unobserved.
- Evidence limits: No complete corpus-wide contradiction repair, dependency invalidation or transactional semantic rollback is established. `--yes` expresses a caller decision, not authenticated human consent.

Admission is separate for each mechanism. Lint needs explicit `--fix` or browser fix request; `--dry-run` previews and prevents those writes. It adds reverse links/records and declared defaults, not scientific justifications. `/check` semantic judgments produce recommendations. `/review` alone does not modify wiki; `/refine` authorizes foreground edits of artifact content and mapped wiki changes, leaving external experiments/expert issues unresolved. `/edit` follows user intent and confirms raw deletion. `/reset` instructs a displayed plan and explicit approval; helper code itself gates only on `--yes` and absence of dry-run. None of these is an answer oracle. Modes are requested maintenance, not a controlled learning experiment.

> if issue.category == "xref-asymmetry":
>     fix = _fix_xref(wiki_dir, issue, dry_run)
> --- `tools/lint.py`

> **Category A — Method/content issues (Claude fixes directly):**
> --- `.claude/skills/refine/SKILL.md`

Withdrawal is scoped, not universal erasure. Reset's graph file list contains edges, citations, brief and open questions, but not projected_edges. Its checkpoint scope deletes only `wiki/.checkpoints/*.json`, not root discovery/init manifests; sidecar runs are outside its named scopes. Even `all` does not establish removal of those stores. Removing raw sources through edit also does not retract derived claims automatically. Reasons for prior content may survive in pages, logs or Git artifacts, but the reset helper is deletion, not an archive/retraction protocol. Explicit subsequent edit or separately available version history is recovery; generated data is ignored by default, so history cannot be presumed.

#### MEM-RTE-ledger-replay
Label: Hiera outcome replay into later scheduling

Part of: [RT-RTE-hiera-search](runtime.md#rt-rte-hiera-search)

This isolates the trace-to-decision part of the supplied search route. Evaluator receipts become ledger events; replay derives candidate best scores and tuning-bout state; later loop calls select eligible candidates and record new decisions/bouts. Status can reconcile missing deep bouts without submitting a replacement attempt. SRC-1: `tools/hiera/ledger.py`, `tools/hiera/scheduler.py`, `tools/hiera/cli.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Receipt/state/report JSON; persisted evaluation, decision and tuning-bout events; finalize writes FINAL_REPORT.json.
- Later read-back: Later loop/status/tune invocations replay ledger events. Candidate state and reservation counts feed execution eligibility and budget; report summaries serve a different reporting consumer.
- Delegated visibility: Scheduler sees IDs, scores, bout counts and direction rather than explanatory reasons or full output logs. Status/finalize report coverage and an experience digest, not the complete experience dictionary.
- Selection predicate: Finite best_score and bout cap determine deep eligibility; direction-adjusted best score, bout count and candidate ID break ties. Budget remaining limits loop continuation.
- Invalidation or expiry: Contract/candidate/source checks bound the enclosing execution route; append-only state persists locally. Reconciliation uses attempt IDs to avoid duplicate bouts. No cross-run experience-store import was established.
- Activation or effect: Code rules use retained results to select later execution and avoid duplicate spending; attained execution/use and improved scientific results are unobserved.
- Evidence limits: Score comparison and execution success/failure counts do not establish content-directed theory criticism. Experience snapshots are reporting derivations, not demonstrated scheduler inputs.

Model/user proposes candidates; admission/approval is inherited from the enclosing search route. The replay consumer is code: valid events and reserved-attempt constraints admit receipts; conflicting duplicate receipts are rejected. Human review is specified for contract/source approval, not every derived count. Bounded experiment mode uses task-defined score direction/evaluator, not a guaranteed expected answer. Raw outcome records retain IDs and receipts; replayed best_score omits most unsuccessful history, but original events remain accessible. Reconciliation adds durable attempt-bound bouts so a later process can respect completed work. No learned parameters are produced by the inspected path.

> eligible.sort(
>     key=lambda record: (
>         sign * float(record["best_score"]),
>         len(record.get("tuning_bouts", [])),
>         record["candidate_id"],
>     )
> )
> --- `tools/hiera/scheduler.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-OBJ-context-brief](runtime.md#rt-obj-context-brief)

Memory-specific selection limit: experiment summaries and stale-entity sections are not universal. The general rebuild sets both budgets to zero; ideation/review/experiment/writing have other allocations. All purposes overwrite one file. The brief's anti-repetition section keeps only failed/rejected titles and optional failure_reason, not hypothesis, complete criticism or invalidates-edge evidence. It remains a natural-language evidence input to the model, not an enforced ban. SRC-1: `tools/research_wiki.py`; [MEM-RTE-context-compilation](#mem-rte-context-compilation) owns the transformation details.

> "general":      (2000,  1500, 1500,   2000,   0,           1000,  0),
> --- `tools/research_wiki.py`

#### On [RT-RTE-knowledge-cycle](runtime.md#rt-rte-knowledge-cycle)

Read-back uses two selection stages: requested file compilation uses fixed symbolic ranks/budgets; the foreground model uses the question, index keywords and brief to choose at most 15 full pages. Relationship questions additionally request selected connecting edges. No supplied trace establishes which claims survive model attention. Crystallization retains answer/query/source_pages or appends to an existing entity; it requires flag/confirmation, unlike basic ingest admission. Rebuild is requested only when new pages are created in ask, so append-only enrichment need not refresh compressed context. The later error-handling instruction rebuilds a missing brief even though the main step says to rebuild if both context files are missing. SRC-1: `.claude/skills/ask/SKILL.md`.

> **Rebuild derived graph files** (only if crystallize created new pages):
> --- `.claude/skills/ask/SKILL.md`

#### On [RT-RTE-parallel-ingest](runtime.md#rt-rte-parallel-ingest)

Working-context control: paper-specific worktree/subagent inputs isolate the task; committed artifacts/task return escape, not the complete delegated conversation. On task completion the host may discard that frame, but merged file content persists. Reload uses files/checkpoints/Git commits, not a pointer that automatically restores prior turns. This resembles a task frame only at the delegated input/return boundary; window content is loaded by value. Actual host isolation/eviction is uninspected. Recovery includes root manifests, task metadata and Git fan-in, with different lifetimes; checkpoint API existence alone is not proof the parent resumed successfully. SRC-1: `.claude/skills/init/SKILL.md`, `tools/research_wiki.py`; supplied route supplies the parallel protocol passage.

#### On [RT-RTE-daily-intake](runtime.md#rt-rte-daily-intake)

Additional read-back path: `build_wiki_profile` reads newest-by-mtime paper/topic/concept cards (12 each), methods/ideas (8 each), 500-character previews and the last 20 log lines. It derives at most 40 keywords, removes configured negative-topic tokens and extracts at most 10 question/gap-like strings of at most 240 characters. Explicit positive preferences augment the profile. This is not the context_brief compiler and need not preserve failure reasons or the full gap map. It supplies later recommendation context and scoring inputs; the model/provider sees further compacted evidence under the supplied runtime route, not full pages. This turns selected raw audit text as well as derived pages into later targeting evidence; retaining the log alone would not establish that path. SRC-1: `tools/daily_arxiv.py`.

> recent_log = "\n".join(log_text.splitlines()[-20:])
> --- `tools/daily_arxiv.py`

Persistence qualification: workflow attempts `git add wiki raw/discovered`, commit and push. Generated wiki entities, graph and raw/discovered are ignored in the shipped `.gitignore`, and the command has no force flag. New ignored content is therefore not assured commit retention by that step; tracked index/log changes can persist without the referenced new pages unless files were already tracked or another path staged them. This is not evidence no CI writes ever persist. SRC-1: `.github/workflows/daily-arxiv.yml`, `.gitignore`.

> git add wiki raw/discovered
> --- `.github/workflows/daily-arxiv.yml`

#### On [RT-RTE-review-call](runtime.md#rt-rte-review-call)

Storage/consumer distinction: server `_threads` is process-local turn accumulation, not a durable learned-memory store. Later chat-reply sends that thread's messages; provider-private retention remains opaque. Wiki verdict/status/criticism is separately authored by the foreground caller. Long-artifact section-by-section review and merge is a requested context-control strategy in the review skill, not evidence of implemented host compaction or a preserved compaction checkpoint. SRC-1: `mcp-servers/llm-review/server.py`, `.claude/skills/review/SKILL.md`; supplied route supplies the implementation passage and restart limit.

## Write side

Acquisition and authoring are not a single trusted import. Ingest resolves source/prepared input, uses literature enrichment, composes page text, checks a deliberately narrow shape and chooses merge/create. Low-level graph checks can reject malformed assertions but cannot verify their truth. `/prefill` is a different source-trust route with an explicit LLM-knowledge fallback; `/ask` bars unsupported pretraining-based answers by instruction, not by an enforcement mechanism. See [MEM-OBJ-wiki-pages](#mem-obj-wiki-pages), [MEM-RTE-foundation-seeding](#mem-rte-foundation-seeding) and [RT-CLM-writer-contract](runtime.md#rt-clm-writer-contract).

Automatic transformations include gap extraction, metadata-to-brief compilation, graph projection, edge/citation dedup and Hiera replay/counting. They curate representations but do not establish warrant. Trace-fed chains differ: experiment/pilot outputs can become model-authored failure reasons and then later banlist guidance; audit log tails can become daily targeting evidence; ledger receipts become symbolic eligibility/budget state and durable reconciliation bouts. Reasons remain richest in original pages/results, weaker in failure_reason, absent from a score/count-only summary. See [MEM-RTE-negative-memory](#mem-rte-negative-memory), [MEM-RTE-ledger-replay](#mem-rte-ledger-replay) and the daily-intake annotation.

Maintenance and withdrawal are separate admission mechanisms, with explicit caller flags, model judgments or human instructions as detailed in [MEM-RTE-memory-maintenance](#mem-rte-memory-maintenance). A new content author is not necessarily its approver; a helper performing the write is not the decision principal. Root manifests, wiki task checkpoints, research progress Markdown and Hiera receipts are alternative recovery forms, not interchangeable host conversation compaction. Their reasons and later readers are local to [MEM-OBJ-checkpoints](#mem-obj-checkpoints) and [MEM-OBJ-ledger](#mem-obj-ledger).

## Read-back

The principal knowledge route is pull: user asks; agent loads brief/gaps/index; model selects pages and optionally relationship data; answer or new proposal follows. No automatic unsolicited context-injection service was established. The compiler is code-selected preprocessing under caller-triggered rebuild, and the foreground page cap is instruction-level, not token-perfect enforcement. Stored original content is reachable but not automatically reloaded. See [MEM-RTE-context-compilation](#mem-rte-context-compilation) and [RT-RTE-knowledge-cycle](runtime.md#rt-rte-knowledge-cycle).

Later consumers differ in authority: an ideator interprets failure reasons as avoidance guidance; an evaluator interprets hypothesis/results as evidence; browser users see pages/graph/shortlists; initialization/research agents use checkpoints for resumption; Hiera scheduling code uses scores/counts to choose actions. File IDs alone do not establish question-targeted relevance, and storage APIs alone do not establish use. Read-back is explicit for the supplied ask/research protocols and wired ledger replay, while actual invocation and behavioral activation remain unobserved. SRC-1: `.claude/skills/ideate/SKILL.md`, `.claude/skills/research/SKILL.md`, `tools/serve.py`, `tools/hiera/scheduler.py`.

Working-context control comprises bounded summaries, full-page top-K selection, per-paper delegation and long-artifact section review. Only the first is implemented by AutoSci's compiler; model selection/delegation/merge is requested of the external host. Old-turn eviction, retained verbatim tails, opaque provider summaries and restart recovery of the foreground conversation are uninspected. This prevents claims about host-wide context management while preserving the known filesystem read-back mechanisms.

## Integration issues

1. **Brief content depends on purpose.** Qualify the runtime account's general description that the compiler keeps experiments and stale entities: ordinary `rebuild-context-brief` selects general, whose allocations omit both. [RT-OBJ-context-brief](runtime.md#rt-obj-context-brief) remains the same object; [MEM-RTE-context-compilation](#mem-rte-context-compilation) establishes this limit. Consequence: a general pack cannot be treated as an experiment-result inventory. SRC-1: `tools/research_wiki.py`.
2. **CI commit retention is narrower than attempted writeback.** [RT-RTE-daily-intake](runtime.md#rt-rte-daily-intake)'s wiring exists, but `.gitignore` plus unforced `git add` prevents assuming newly generated entities/raw files enter a commit. See its annotation. Actual deployment may track those files differently; no CI trace is supplied. Consequence: successful local ingestion does not prove cross-run repository persistence. SRC-1: `.gitignore`, `.github/workflows/daily-arxiv.yml`.
3. **Hiera experience summary versus actual consumer.** Boundary wording about derived experience and runtime wording about summaries should not imply durable full experience snapshots guide scheduling. [MEM-OBJ-experience](#mem-obj-experience) is counts constructed in memory; inspected callers expose only revision. [MEM-RTE-ledger-replay](#mem-rte-ledger-replay) establishes the actual feedback path. Timestamp-bearing digest also prevents treating revision as a stable content-only identifier. SRC-1: `tools/hiera/experience.py`, `tools/hiera/cli.py`, `tools/hiera/scheduler.py`.
4. **Admission does not ensure global freshness or withdrawal.** Append-only ask enrichment and direct edit/browser metadata changes do not establish immediate brief refresh; reset omits projected edges, root manifests and sidecars. [MEM-RTE-memory-maintenance](#mem-rte-memory-maintenance), [MEM-OBJ-checkpoints](#mem-obj-checkpoints), [MEM-OBJ-edges](#mem-obj-edges). Consequence: current page state, displayed graph and remembered summaries can disagree until refreshed; reset-all is not a whole-memory erasure guarantee. SRC-1: `.claude/skills/ask/SKILL.md`, `.claude/skills/edit/SKILL.md`, `tools/reset_wiki.py`.
5. **Reasons and theory granularity are not uniform.** Filter/pilot/formal failures share storage but not evidential force; compressed context strips much rationale. Explicit common exp-eval writes do not guarantee the promised full Lessons learned narrative or saved terminal verdict. [MEM-RTE-negative-memory](#mem-rte-negative-memory), [RT-RTE-research-verdict](runtime.md#rt-rte-research-verdict). Consequence: later theory/learning classification must follow what each consumer actually receives. SRC-1: `.claude/skills/ideate/SKILL.md`, `.claude/skills/exp-eval/SKILL.md`, `tools/research_wiki.py`.
6. **Unresolved included operations.** Initialization/source conversion fidelity, full index/topic-backfill regeneration, detailed Hiera proposal/tuner policy, all dissemination transformations and actual host context isolation are not fully inspected here. The coverage table identifies paths and prevented conclusions; source access exists. Existing checkpoint/page provenance in a deployment and provider-private memory are also unknown. These limits do not erase the supported file/replay routes.
7. **Record identity comparison.** New context-compilation and ledger-replay routes are declared parts of their supplied containing routes, not replacements. New page/navigation/graph/checkpoint/ledger/experience objects have no supplied object counterpart; negative-memory spans two routes, foundations and maintenance add distinct admission paths. No possible duplicate requiring supersession was identified after those comparisons. The existing brief, writer policy, model components and principal runtime routes are annotated/cited rather than re-declared.

## Limitations and checks

This is source analysis, not an observed research episode. Source HEAD/clean status were rechecked against the supplied boundary; all newly inspected files remain SRC-1 at that pin. Invocation, member types, collection, worker rules and records contract were read, including supplied bounded ranges and trailing lines. Method authority is the supplied invocation/contracts, not a prior analysis. No new source, host trace or causal experiment was admitted.

Checks cannot establish correctness of paper extraction, source truth, scientific judgment, per-content human approval, deployment permissions, actual later use, learned capacity or measured gains. No target code or tests were executed. Deterministic validation: the required invocation-scoped `commonplace-run validate-output` completed successfully: “Member content check passes; invocation residue not checked.” Form and quote occurrence do not establish analytical acceptance or claim support.
