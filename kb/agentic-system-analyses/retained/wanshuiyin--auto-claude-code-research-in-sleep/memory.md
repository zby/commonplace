---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "ARIS memory: project wiki projections, reviewer continuity, compact recovery and trace-fed instruction maintenance, with source-level selection limits."
run-id: AAS-2026-10-15-auto-claude-code-research-in-sleep-a8abf5f80cbb-01
source-identity: "https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep"
reviewed-boundary: "26b95cfa0d8747078e9e43b42e20952709e561b8"
---

# Auto-claude-code-research-in-sleep memory report

## Boundary and evidence

This report extends SRC-1 inspection at the frozen commit, without changing the [boundary](boundary.md)'s `complete artifact, partial loop` classification. It includes project wiki acquisition, enrichment, evaluation write-back and selection; reviewer-response retention; model-authored compact handoffs; iteration history; and usage events feeding harness maintenance. Phase JSON and bridge option replay are supplied runtime findings, not independently re-audited here. Host context eviction, provider conversation storage and model weights are external opaque dependencies. No target commands, tests, providers or examples were executed; delivery and improvement are not observed.

Direct inspection used the wiki skill in full; helper imports, initialization, edges, projection, paper ingest, claim/idea/experiment renderers and writers, index, sync and complete CLI dispatch; complete wiki-enrich, iteration logger, capture filter and logging hook/template; threat scanner matching/quarantine/CLI; and bounded consumer/producer passages identified below. Network metadata parsing and the scanner's complete pattern catalogue were not audited. The source register remains SRC-1 in boundary; all new paths below are commit-relative paths in that source.

| Entry or operation | Inspected source / evidence basis | Coverage and prevented conclusion |
|---|---|---|
| Wiki init, ingest, sync, direct helper/API writes | SRC-1, `tools/research_wiki.py`; `skills/research-wiki/SKILL.md`, direct | [MEM-RTE-paper-capture](#mem-rte-paper-capture), [MEM-RTE-evaluation-write](#mem-rte-evaluation-write). Manual metadata and direct API are alternatives to paper-reading skills; callers are not authenticated. |
| Paper body enrichment | SRC-1, `skills/wiki-enrich/SKILL.md`, direct, complete | [MEM-RTE-paper-capture](#mem-rte-paper-capture). External content is specified input, not fetched evidence in this analysis. |
| Claims, experiments, idea outcomes | SRC-1, `skills/proof-checker/SKILL.md` Phase 5.5; `skills/result-to-claim/SKILL.md` wiki step and rules, direct | [MEM-RTE-evaluation-write](#mem-rte-evaluation-write). Full proof/experiment auditing machinery uninspected; no judgment-quality conclusion. |
| Wiki query/read gate | SRC-1, `tools/research_wiki.py` projection and dispatch; `skills/idea-creator/SKILL.md` Phase 0, direct | [MEM-RTE-pack-read](#mem-rte-pack-read). Topic-directed graph retrieval is not implemented by the inspected builder. |
| Operational-noise and injection rejection | SRC-1, `tools/capture_filter.py`, complete; `tools/threat_scan.py` matching/quarantine/CLI; wiki writers and idea read gate, direct | [MEM-RTE-evaluation-write](#mem-rte-evaluation-write), [MEM-RTE-pack-read](#mem-rte-pack-read). Pattern coverage and semantic safety unestablished. |
| Wiki update/lint, graph maintenance, withdrawal | SRC-1, wiki skill and helper dispatch, direct | Model-followed update/lint instructions; no corresponding generic CLI subcommands. Claim retraction is an allowed status. Old edges are not retracted by inspected writers. |
| Reviewer memory, resume, backend frames | SRC-1, `skills/auto-review-loop/SKILL.md` initialization, hard review, Phase B.5 and native dispatch, direct; supplied [RT-RTE-codex-call](runtime.md#rt-rte-codex-call) | [MEM-RTE-reviewer-memory](#mem-rte-reviewer-memory). Bridge conversation internals and alternate backend implementations uninspected. |
| Compact checkpoints | SRC-1, `skills/idea-discovery/SKILL.md` Phase 5.5; `skills/experiment-bridge/SKILL.md` compact option and Phase 5.5; auto-review initialization, direct | [MEM-RTE-compact-recovery](#mem-rte-compact-recovery). No ARIS implementation of host eviction established. |
| Phase-state acceptance/resume; thread options | Supplied [RT-RTE-phase-resume](runtime.md#rt-rte-phase-resume), [RT-OBJ-run-state](runtime.md#rt-obj-run-state), [RT-RTE-codex-call](runtime.md#rt-rte-codex-call) | Ordinary recovery/access metadata separated from derived knowledge. No independent reread. |
| Heartbeat and tried directions | SRC-1, `tools/iteration_log.py` complete; `skills/research-pipeline/SKILL.md` heartbeat search/passages | [MEM-RTE-stall-pivot](#mem-rte-stall-pivot). A counter is not a quality oracle. |
| Passive hooks → meta-optimize → edited skills | SRC-1, `templates/claude-hooks/meta_logging.json`, `tools/meta_opt/log_event.sh`, direct; supplied [RT-RTE-meta-landing](runtime.md#rt-rte-meta-landing) | [MEM-OBJ-events](#mem-obj-events) and annotations. Global log consumer unspecified; deployed hooks unobserved. |
| Review traces / acquittal receipts | SRC-1, `skills/shared-references/review-tracing.md` purpose, invocation, identity schemas; review initialization/B.5, direct | [MEM-OBJ-review-traces](#mem-obj-review-traces). `tools/save_trace.sh` and native evidence-validator internals uninspected; cannot independently establish writer fidelity or attestation. |
| Other literature integration, platform mirrors, installers, monitoring, paper-style extraction, output versioning/manifest maintenance | Included but uninspected beyond inventory/search and supplied boundary/runtime | Named unresolved paths include `tools/verify_wiki_coverage.sh`, `tools/meta_opt/check_ready.sh`, `tools/extract_paper_style.py`, `skills/skills-codex/`, and other paper-reading skill hooks. No cross-platform parity, complete corpus audit, global-memory inventory or full-loop closure claimed. |

## Core ideas

ARIS has several distinct retention mechanisms, not one memory store. The project wiki contains model-written research summaries and symbolic outcome/status fields. A deterministic, lossy projection selects a small subset for a later ideation invocation. Reviewer continuity instead retains complete reviewer responses and, in harder modes, supplies the growing file verbatim. Compact summaries deliberately replace fuller logs in selected future reads. Usage-event summaries feed a separate human-gated instruction-maintenance route. These distinctions follow [MEM-RTE-pack-read](#mem-rte-pack-read), [MEM-RTE-reviewer-memory](#mem-rte-reviewer-memory), [MEM-RTE-compact-recovery](#mem-rte-compact-recovery), and [RT-RTE-meta-landing](runtime.md#rt-rte-meta-landing).

The strongest wiki selection claims do not survive inspection unchanged. The builder orders sections and slices text; it does not implement the advertised graph rankings, clusters or protected failed-idea retention. A large project brief can displace failed ideas. Enrichment's reusable ingredients and limitations do not reach ideation through this projection, although the one-line thesis can. Source trust is also path-specific: helper-side scanning can be unavailable without stopping writes, while the ideation read protocol requires a working scanner and skips rejected packs. Neither a clean regex scan nor an accepted status verifies scientific truth ([MEM-CLM-pack-contract](#mem-clm-pack-contract), [MEM-RTE-pack-read](#mem-rte-pack-read)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-papers
Label: Wiki paper pages

Source-native identity: `research-wiki/papers/<slug>.md`. Filesystem UTF-8 Markdown combines natural-language thesis/body/abstract with symbolic bibliographic frontmatter and node IDs. SRC-1, `tools/research_wiki.py` ingest and renderer; `skills/wiki-enrich/SKILL.md`. arXiv metadata/abstract or caller-supplied metadata initializes a scaffold; model enrichment may derive prose from third-party summaries or an abstract rather than a full paper. Raw abstract is distinct from interpreted body. Dedup skips existing pages by default; explicit update regenerates the page and can replace enrichment. Later projection reads title/node ID and thesis, not the full body. No counterpart in runtime after comparison with [RT-RTE-research-pipeline](runtime.md#rt-rte-research-pipeline), which describes artifact flow, not these per-paper pages.

#### MEM-OBJ-ideas
Label: Wiki idea pages

Source-native identity: `research-wiki/ideas/<slug>.md`. Filesystem Markdown has natural-language hypothesis, risks and later lessons, plus symbolic stage, outcome and lineage IDs. SRC-1, `tools/research_wiki.py` idea renderer/writer; `skills/result-to-claim/SKILL.md` wiki update step. Initial model-generated ideas include recommended and killed candidates, initially pending; result judgment later changes outcome through instructed in-place edits. The negative/mixed frontmatter value, not body wording, selects banlist entries. Failure reasons can persist in the body but are read back only through a short line-based extraction. Distinct from the pipeline's broad product route [RT-RTE-research-pipeline](runtime.md#rt-rte-research-pipeline).

#### MEM-OBJ-experiments
Label: Wiki experiment pages

Source-native identity: `research-wiki/experiments/<slug>.md`. Filesystem Markdown contains natural-language metrics/reasoning and symbolic verdict/confidence, idea ID, hardware/date and provenance handle. SRC-1, `tools/research_wiki.py` experiment renderer/writer. These are derived result judgments, not raw execution traces. Rejudging explicitly overwrites a page; the helper checks enum values, not whether experiments ran. Index lists nodes; the inspected query-pack builder does not include experiment bodies. Distinct artifact from [RT-OBJ-run-state](runtime.md#rt-obj-run-state)'s phase metadata.

#### MEM-OBJ-claims
Label: Wiki claim pages

Source-native identity: `research-wiki/claims/<slug>.md`. Natural-language statement, honest scope and evidence chain coexist with symbolic proof status and provenance pointer in UTF-8 Markdown. SRC-1, `tools/research_wiki.py` claim renderer/writer; `skills/proof-checker/SKILL.md` Phase 5.5. Proof audit is the instructed birth source; helper callers can also supply these fields directly. Status permits drafted, unproven, sound-modulo-imports, verified, refuted and retracted. The index displays status; the query-pack builder does not carry claim statements or scope. A provenance path is not evidence that the audit was authentic. Distinct from [RT-OBJ-run-state](runtime.md#rt-obj-run-state)'s acceptance handles.

#### MEM-OBJ-edges
Label: Wiki relationship graph

Source-native identity: `research-wiki/graph/edges.jsonl`. Symbolic JSONL triples and timestamps plus natural-language evidence; stored on disk. SRC-1, `tools/research_wiki.py` add_edge. Dedup keys on from/to/type, so changed evidence for an identical triple is not refreshed. Unknown types warn rather than reject; endpoint existence is not generally enforced. Flagged evidence can be replaced with a placeholder while raw evidence survives in `graph/quarantine.log`. That quarantine log affords human review; no automatic later consumer was established. Pack delivery includes recent triples but omits evidence and timestamps, so supporting reasons do not travel with these relationships. No runtime counterpart after comparison with [RT-RTE-research-pipeline](runtime.md#rt-rte-research-pipeline).

#### MEM-OBJ-query-pack
Label: Wiki query pack

Source-native identity: `research-wiki/query_pack.md`. Derived UTF-8 Markdown: natural-language extracts and symbolic node/relationship displays for interpretation by the ideation model. SRC-1, `tools/research_wiki.py` rebuild_query_pack. It is not an embedding, semantic index or full graph serialization. Its lineage is selected brief sections, gap-map prefix, failed-idea snippets, paper thesis snippets and recent edge triples. Model interpretation supplies downstream authority; selection itself is fixed Python. Distinct from all supplied runtime objects; [RT-RTE-research-pipeline](runtime.md#rt-rte-research-pipeline) is its closest broad context.

#### MEM-OBJ-reviewer-memory
Label: Reviewer memory artifact

Source-native identity: `review-stage/REVIEWER_MEMORY.md`. Natural-language raw reviewer responses and reviewer-authored memory updates in filesystem Markdown; round/score headings are readable display metadata. SRC-1, `skills/auto-review-loop/SKILL.md` Phase B.5. The executor physically appends but is forbidden to rewrite or summarize prior reviewer content. The same file mixes verbatim trace material with reviewer-derived suspicions; it is not solely a summary despite that label elsewhere in the skill. Part of the continuity surface described by [RT-RTE-review-transition](runtime.md#rt-rte-review-transition), but an independently retained object, not a duplicate of the stateless gate.

#### MEM-OBJ-compact-files
Label: Compact recovery artifacts

Source-native identities: `idea-stage/IDEA_CANDIDATES.md`, `EXPERIMENT_LOG.md`, and recovery input `findings.md`. Filesystem Markdown contains model-written natural-language summaries plus tables, metrics and reproduction commands. SRC-1, `skills/idea-discovery/SKILL.md` Phase 5.5; `skills/experiment-bridge/SKILL.md` Phase 5.5; `skills/auto-review-loop/SKILL.md` initialization. Candidates preserve only top 3–5 ideas, active hypothesis and key evidence; experiment log preserves config/result/verdict/reproduction command, not full raw output or review rationale. The complete production path of `findings.md` remains uninspected. Closest supplied record is [RT-RTE-research-pipeline](runtime.md#rt-rte-research-pipeline); these are its concrete compact handoff artifacts, not additional runtime executors.

#### MEM-OBJ-events
Label: Usage event summaries

Source-native identities: project `.aris/meta/events.jsonl` and global `~/.aris/meta/events.jsonl`. Symbolic JSONL event/session/tool/model fields with natural-language prompt/command previews. SRC-1, `tools/meta_opt/log_event.sh`; `templates/claude-hooks/meta_logging.json`. Host events are transformed, not saved as complete transcripts: Bash command 200 characters, Codex prompt 150, ordinary user prompt 100; Write/Edit/Read record file paths, not content. Skill arguments remain a separate field. Project events feed [RT-RTE-meta-landing](runtime.md#rt-rte-meta-landing); a deployed global-log reader is unspecified. The object is a distinct input to that route, not the revised skill itself.

> record["input_summary"] = tool_input.get("command", "")[:200]
> --- `tools/meta_opt/log_event.sh`

#### MEM-OBJ-review-traces
Label: Review trace and acquittal artifacts

Source-native identities: `.aris/traces/<skill-name>/<date-run>/` request/response/metadata files and `review-stage/ACQUITTAL_LOG.jsonl`. SRC-1, `skills/shared-references/review-tracing.md`; `skills/auto-review-loop/SKILL.md` initialization and Phase B.5. The prescribed disk form separates full natural-language prompt/response from symbolic identities, thread ID, memory hash and evidence pointers. A hash describes the pre-call artifact, not actual model attention. Acquittal history is cumulative and run-scoped; stale entries are not current acquittal. Actual helper serialization and native host-event verification are uninspected here. Closest supplied records are [RT-RTE-review-transition](runtime.md#rt-rte-review-transition) and [RT-RTE-meta-landing](runtime.md#rt-rte-meta-landing): these are audit inputs/retained results, not duplicate decision procedures.

### Routes

#### MEM-RTE-paper-capture
Label: Paper capture and enrichment

Endpoints/progression: paper-reading skill or explicit ingest/sync request → metadata/manual fields → helper page → optional wiki-enrich model edits → rebuilt index/pack. Owner: caller model selects papers; Python dedups/renders; enrichment model selects source-derived prose. Context includes project brief/graph and fetched summaries or abstract. Admission is caller-directed, not per-page human approval. A human may choose target/source/force; no mandatory reviewer verdict precedes enrichment edits. The helper's skip-on-exist protects existing pages unless explicitly overridden; enrichment defaults to TODO sections and caps batches at 20, with configurable override. Guidance demands source fidelity and preserves frontmatter, graph section and raw abstract. No reference-answer oracle; this is open research capture. Recovery is skip/fallback/report; explicit helper overwrite can destroy body enrichment, and no transactional rollback was established.

- Immediate return: page path or skip/error; enrichment report and source-labelled log entry.
- Later read-back: rebuild produces the pack; later idea-creator may receive paper titles and thesis via [MEM-RTE-pack-read](#mem-rte-pack-read).
- Delegated visibility: enrichment receives one full page, project context, and first usable source text in its fallback chain; no demonstrated isolated agent frame.
- Selection predicate: ingest arXiv ID/slug dedup; enrichment requested slug, all, or TODO-bearing pages, capped per invocation.
- Invalidation or expiry: no page TTL; default skips preserve prior enrichment; explicit update/force changes replacement behavior.
- Activation or effect: implemented page writes and requested semantic enrichment; influence on later ideation remains unobserved.
- Evidence limits: source only; metadata network parsing and full paper-reading integrations uninspected.
- implementation conclusion status: wired
- enrichment design conclusion status: claimed
- operation conclusion status: uninspected

Evidence: SRC-1, `tools/research_wiki.py`; `skills/wiki-enrich/SKILL.md`.

> **Never** touch the YAML frontmatter, `## Connections`, or `## Abstract (original)`.
> --- `skills/wiki-enrich/SKILL.md`

#### MEM-RTE-evaluation-write
Label: Evaluation-derived wiki write-back

Endpoints/progression: generated ideas/proof audit/experiment verdict → helper node writes and in-place idea outcome edits → edges/index/pack → later ideation or wiki inspection. Owners: foreground model supplies fields; external reviewers are instructed judges for proof/results; helper checks syntax/enums and optional threat patterns, not correctness. Human initiation is not per-content approval, and generic direct helper caller control remains unresolved. Experiment verdicts and proof statuses are separate axes. The instructed reviewer-unavailable path prevents supportive result propagation, but direct helper APIs accept supplied status/verdict without checking audit files. Operating mode: task research evaluation, no general expected-answer oracle. Guidance is audit outcome mapping, empirical scope and failure reasons. Rejection/withdrawal includes invalid-enum refusal, optional quarantine, instructed no-store/rewrite for operational noise, re-audit updates and retracted claim status. No automatic rollback or cascading edge removal was found in inspected writers.

- Immediate return: created/refreshed node paths and graph/log/index/pack updates; result verdict still reports when optional wiki helper fails.
- Later read-back: negative/mixed idea outcome enters failed-idea projection; recent edges enter relationship display; claim statuses enter index, not claim text in the pack.
- Delegated visibility: helper receives caller strings and provenance handles; it does not independently inspect the proof or raw experiment trace.
- Selection predicate: active wiki, helper resolution, explicit node IDs; experiment-edge instructions additionally require successful experiment-node creation.
- Invalidation or expiry: default dedup skips; rejudges use explicit overwrite; idea outcome edits preserve richer body. Existing contradictory edges can remain.
- Activation or effect: fixed-rule persistence/projection is implemented; model-followed evaluation and its later effects are unobserved.
- Evidence limits: full upstream audit mechanisms uninspected; neither status labels nor scan success certify truth.
- implementation conclusion status: wired
- evaluation design conclusion status: claimed
- operation conclusion status: uninspected

Evidence: SRC-1, `tools/research_wiki.py`, `tools/capture_filter.py`, `tools/threat_scan.py`, `skills/research-wiki/SKILL.md`, `skills/result-to-claim/SKILL.md` wiki step/rules, `skills/proof-checker/SKILL.md` Phase 5.5; [MEM-OBJ-ideas](#mem-obj-ideas), [MEM-OBJ-experiments](#mem-obj-experiments), [MEM-OBJ-claims](#mem-obj-claims), [MEM-OBJ-edges](#mem-obj-edges).

> # 3. Update idea outcome (raw markdown, helper-free)
> --- `skills/result-to-claim/SKILL.md`

> if status not in _CLAIM_STATUSES:
> --- `tools/research_wiki.py`

Theory account for the retained research content: ideas carry hypotheses/risks and claim pages carry statements/scope; result judgments can change outcome and later reliance without replacing the hypothesis text. Theory-builder conditions 1–4, assessed separately: **1 localized content — afforded**, renderers expose whole statements/hypotheses; **2 consumption — claimed**, later ideation is instructed to exclude failed directions, without an observed content-dependent decision; **3 content-directed criticism — uninspected**, the bounded reads establish requested failure reasons and audit-to-status mapping, not a complete inspected criticism/blame/revision episode; **4 iteration — claimed**, rebuilt failed-idea memory is requested input to later ideation, but no next cycle was supplied. Addressability is page/field/section-level, not opaque model reasoning. Persistence is designed across project sessions; attained use horizon is unobserved. Learning: improved future capacity is unestablished. Reflection on ARIS's own methods and reflective theory building are not established by research-product retention; the distinct meta route carries its own assessment. Computational writers do not establish an autonomous theory builder because the complete research criticism loop was not inspected. Neither self-improvement nor its absence follows from this product-memory route.

The operational-noise filter is a standalone regex command requested by the wiki skill; inspected helper writers do not invoke `capture_filter.py`. Threat quarantine is different: helper writers call it for selected body fields and edge evidence, retain placeholders plus raw quarantine logs, but leave structural names/titles outside those body checks. Import failure leaves scanner functions unset and writes proceed. The idea read gate separately compensates for untrusted pack content, as below.

> scan_for_threats = None  # type: ignore
> --- `tools/research_wiki.py`

#### MEM-RTE-pack-read
Label: Deterministic wiki projection and ideation read

Endpoints/progression: caller/mutation requests rebuild → Python selects wiki extracts → disk pack → idea-creator's scanner-before-Read procedure → foreground ideation model. The selector is not a model call. It takes parent RESEARCH_BRIEF sections (600-character fallback), first 1200 gap-map characters, filename-sorted negative/mixed ideas (1400 characters), first 12 filename-sorted papers (1800 characters), and last 20 graph edges (900 characters). Final assembly defaults to 8000 characters and stops at the first section that does not fit, optionally appending a truncated prefix. The scanner can prepend a warning banner after this assembly, exceeding that nominal bound; CLI `--max-chars` is configurable. No query/topic argument, graph centrality or semantic retrieval participates in this helper selection.

- Immediate return: regenerated pack and character count; read procedure yields raw pack only after clean scan, otherwise a warning/no wiki context.
- Later read-back: a later idea-creator invocation requests the cached pack; under-seven-day cache is scanned, stale/missing cache rebuilt once when possible, then scanned.
- Delegated visibility: ideation receives the selected projection, not all nodes, abstracts, full hypotheses, claim scope or relationship evidence.
- Selection predicate: fixed extraction order/budgets and filename/recency order; negative/mixed frontmatter gates failed ideas. Consumer gate requires a resolved scanner and clean exit immediately before Read.
- Invalidation or expiry: seven-day freshness is a consumer instruction, not a universal TTL. Any scanner hit/error skips wiki context without modifying/rebuilding the rejected pack.
- Activation or effect: consumer is instructed to use gaps as search seeds, failed ideas as banlist and papers as prior work, while searching recent literature; no observed choice change.
- Evidence limits: no target execution or invocation trace; scanner signature coverage unestablished; pack trust rule is host-followed procedure.
- projection implementation conclusion status: wired
- read design conclusion status: claimed
- operation conclusion status: uninspected

Evidence: SRC-1, `tools/research_wiki.py` rebuild_query_pack/dispatch; `skills/idea-creator/SKILL.md` Phase 0; [MEM-OBJ-query-pack](#mem-obj-query-pack).

> for f in sorted(papers_dir.glob("*.md")):
> --- `tools/research_wiki.py`

> paper_summaries[:12]
> --- `tools/research_wiki.py`

> For a cached pack younger than 7 days, scan it immediately before Read. If
> clean, read the raw pack at once. Treat its gaps as search seeds, failed ideas
> as a banlist, and top papers as known prior work; still run Phase 1 for the
> last 3–6 months.
> --- `skills/idea-creator/SKILL.md`

Admission here is selection of retained context, not approval of research truth: code selects, regex may veto delivery, foreground model interprets. A workflow request does not supply a human verdict on every selected entry. These are knowledge/guidance inputs with potentially exclusionary banlist authority, not higher-priority executable instructions.

#### MEM-RTE-reviewer-memory
Label: Reviewer-response retention and replay

Part of: [RT-RTE-review-transition](runtime.md#rt-rte-review-transition)

This route isolates the parent route's append/read-back suboperation, not its decision computation.

Endpoints/progression: reviewer response → foreground append of verbatim response and reviewer memory → later reviewer prompt/file access. This is the memory-specific continuity route, distinct from [RT-RTE-review-transition](runtime.md#rt-rte-review-transition)'s stop-decision computation. The reviewer authors suspicions and judgments; executor performs append but has no procedural authority to curate prior text. No per-append human approval required. Budget is entire memory file in hard-mode prompt, with no truncation allowed; finite round count bounds rounds, not bytes. Terminal-round append precedes stop evaluation. No reference-answer oracle; future critique is an open judgment task.

- Immediate return: updated reviewer artifact before stop evaluation; pre-call memory hash requested for trace.
- Later read-back: hard prompts paste full memory; native/fresh compatibility contexts get paths; medium Codex/manual routes primarily continue the same thread. Nightmare uses direct CLI rather than the bridge.
- Delegated visibility: reviewer gets selected task/files and prior reviewer material, not automatic foreground context inheritance; notifications/shared file access mean this is not strict isolation.
- Selection predicate: backend/difficulty/round chooses prompt/thread route; memory append is required regardless of difficulty for Copilot continuity.
- Invalidation or expiry: append-only/no truncation protocol; no memory-file TTL/reset specified in inspected initialization. Review-state JSON older than 24 hours is deleted by instruction, not proof that memory was cleared.
- Activation or effect: requests attention to previously unresolved suspicions and comparison with fixes; actual retained-input influence unobserved.
- Evidence limits: natural-language write/replay procedure, not protected storage; provider history and actual host adherence uninspected.
- design conclusion status: claimed
- operation conclusion status: uninspected

Evidence: SRC-1, `skills/auto-review-loop/SKILL.md` initialization, hard mode and Phase B.5; supplied [RT-RTE-codex-call](runtime.md#rt-rte-codex-call).

> **Append-only — never delete, never truncate.** The file is a reviewer-owned audit trail. The executor must never summarize, curate, or edit prior rounds' content. Append the reviewer's full raw response for this round verbatim, then append a memory update section if the reviewer provided one.
> --- `skills/auto-review-loop/SKILL.md`

#### MEM-RTE-compact-recovery
Label: Compact artifacts for later recovery

Part of: [RT-RTE-research-pipeline](runtime.md#rt-rte-research-pipeline)

This route isolates the parent route's optional compact handoff; standalone child-skill entry remains possible.

Endpoints/progression: optional COMPACT → foreground summarizes candidates/results → filesystem checkpoints → later experiment/review invocation selects compact artifacts. The model produces the summaries; no deterministic equivalence verifier or mandatory human approval is specified. Retained compact content can omit eliminated alternatives, detailed criticism and raw logs. It preserves selected evidence/results and reproduction inputs, not necessarily the reasons for every judgment. This is context substitution, not implemented deletion of host turns.

- Immediate return: small candidate summary or appended experiment entry alongside normal artifacts.
- Later read-back: experiment bridge prefers compact candidates when enabled/available; auto-review initialization substitutes findings plus experiment log for full review/raw logs. A recent resume branch also requests full AUTO_REVIEW before this compact preference, so exclusive avoidance of full history is not guaranteed.
- Delegated visibility: downstream model receives summaries rather than raw producer history; originals remain reachable as files, with no inspected ARIS eviction rule.
- Selection predicate: COMPACT flag and file availability; candidates top 3–5, approximately 30 lines; no strict byte/token cap on aggregate experiment log.
- Invalidation or expiry: no uniform summary freshness/TTL; required source/result matching beyond the producer procedure uninspected.
- Activation or effect: requested lower input volume and recovery continuity; actual savings or successful recovery unobserved.
- Evidence limits: host auto-compaction itself external; findings production only partly inspected; summaries are model-authored design, not measured lossless transforms.
- design conclusion status: claimed
- operation conclusion status: uninspected

Evidence: SRC-1, `skills/idea-discovery/SKILL.md` Phase 5.5; `skills/experiment-bridge/SKILL.md` compact option and Phase 5.5; `skills/auto-review-loop/SKILL.md` initialization. Closest supplied route [RT-RTE-research-pipeline](runtime.md#rt-rte-research-pipeline); this route isolates its lossy later-context handoff, not its stage orchestration.

> This file is intentionally small (~30 lines) so downstream skills and session recovery can read it without loading the full `idea-stage/IDEA_REPORT.md` (~200+ lines).
> --- `skills/idea-discovery/SKILL.md`

#### MEM-RTE-stall-pivot
Label: Iteration history to structural pivot

Endpoints/progression: host supplies new-finding count and optional direction → iteration logger appends `.aris/runs/<run_id>.iterations.jsonl` → reads previous stale count → returns pivot → pipeline instructs structural change or human escalation. Owner: Python computes consecutive zeros; host decides what counts and implements next direction. The JSONL contains symbolic counts/pivots and optional natural-language direction. This trace-fed derivation differs from [RT-OBJ-run-state](runtime.md#rt-obj-run-state)'s phase acceptance. It neither updates model parameters nor judges scientific quality.

- Immediate return: stale_count and none/structural/human pivot.
- Later read-back: next note reads the last valid stale_count; show exposes recorded directions, intended to prevent retrying the same frame in subsequent ticks.
- Delegated visibility: no model frame created by the helper; orchestrator receives compact decision fields and can request ledger.
- Selection predicate: positive finding count resets stale count; zero increments; at least two zeros requests structural pivot, at least four human attention.
- Invalidation or expiry: append-only API; garbled lines tolerated; no TTL; advisory locking is best effort and absent without fcntl.
- Activation or effect: implemented derived pivot signal; host-followed structural change remains unobserved.
- Evidence limits: caller-supplied counts are not independently audited; direction-similarity rejection is procedural, not implemented comparison in this logger.
- implementation conclusion status: wired
- consumer design conclusion status: claimed
- operation conclusion status: uninspected

Admission: host supplies the raw count/direction, software rejects negative count/invalid run ID, no per-entry human approval. Open maintenance/research cadence; no answer oracle. Guidance separates structural from tactical changes; prior directions persist, while recovery/escalation is a requested change of direction rather than rollback. SRC-1, `tools/iteration_log.py`, `skills/research-pipeline/SKILL.md` heartbeat.

> stale_count = 0 if new_findings > 0 else _last_stale(path) + 1
> --- `tools/iteration_log.py`

### Claims

#### MEM-CLM-pack-contract
Label: Query-pack ranking and preservation claims

SRC-1, `skills/research-wiki/SKILL.md` advertises ranked gaps/papers, paper clusters, open unknowns and protected failed ideas. `tools/research_wiki.py` contradicts a literal implementation reading: fixed prefixes, sorted files and recent edges, with sequential stop-on-overflow. No cluster/unknown section is assembled in inspected builder. Failed ideas have a local 1400-character slice and can also be omitted after a large earlier section. Enrichment's statement that reusable ingredients/limitations feed later ideation is not established through this pack; only the thesis is extracted from paper bodies. See [MEM-RTE-pack-read](#mem-rte-pack-read), [MEM-RTE-paper-capture](#mem-rte-paper-capture).

> **Failed ideas are the most valuable memory.** Never prune them from query_pack.
> --- `skills/research-wiki/SKILL.md`

> for s in sections:
> --- `tools/research_wiki.py`

> if len(pack) + len(s) <= max_chars:
> --- `tools/research_wiki.py`

This is a source doctrine/implementation mismatch, not a correction to an asserted runtime ranking fact. A hard 8000-character guarantee is also too strong: caller override and post-assembly scan banner are counterexamples. A topic supplied to the skill may guide a model's investigation, but the registered CLI exposes rebuild_query_pack with only root/max-chars, not a topic selector.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-wiki-ideation
Label: Retained wiki to ideation guidance

Consumer: foreground idea-creator model. Channel: immediate Read of scanned query pack. Force: model-interpreted guidance, with failed ideas instructed as a banlist and gaps as search seeds; scanner success does not elevate source content to trusted instructions. Horizon: later ideation calls across sessions while the pack survives and passes freshness/scan procedure. SRC-1, `skills/idea-creator/SKILL.md` Phase 0; [MEM-RTE-pack-read](#mem-rte-pack-read). Distinct from [RT-BAP-skill-instructions](runtime.md#rt-bap-skill-instructions), whose consumer loads changed procedural skill text rather than task knowledge. No observed behavioral dependence or improved future capacity established.

## Annotations

#### On [RT-OBJ-run-state](runtime.md#rt-obj-run-state)

Memory distinction: phase status/policy are symbolic selection metadata. Artifact/verdict handles do not deliver their underlying content. Mainline accepted/skipped and Codex provisional advancement are different resume selectors, as supported by [RT-RTE-phase-resume](runtime.md#rt-rte-phase-resume). This is recovery state, not by itself derived research memory or evidence of learning.

#### On [RT-RTE-codex-call](runtime.md#rt-rte-codex-call)

Memory-specific boundary: saved per-thread options preserve access configuration (symbolic model/config/sandbox/cwd), whereas the external CLI owns opaque conversational retention. Options are not reviewer knowledge. A supplied thread ID requests read-back; this is not unsolicited context push. Missing/malformed option storage weakens configuration continuity. Selected task prompts resemble separate task frames, but shared files and streamed events break strict frame isolation; host eviction remains external. These limits and final-message return are established in the supplied route, not inferred from a fresh source execution.

#### On [RT-RTE-meta-landing](runtime.md#rt-rte-meta-landing)

Trace origin and curation: optional deployed hooks transform host event payloads into [MEM-OBJ-events](#mem-obj-events), not complete execution transcripts. The installed template requests asynchronous logging on tool/prompt/session events, but copying the template is a prerequisite, not evidence of universal activation. SRC-1, `templates/claude-hooks/meta_logging.json`, `tools/meta_opt/log_event.sh`. Project logs become model diagnosis, explanatory patch rationale, pending diffs/report and bottleneck ledger; later cycle reads the ledger/report, and a later host can load landed instruction text. The raw→derived→later-consumer chain is instruction-designed and human-gated; automatic logging alone is not automatic skill adoption. Rationale survives in reports/patches; the live skill consumer need not load that rationale. Provenance sidecars are access/admission receipts, not correctness evidence. Parameter change, improved capacity and exercised self-improvement are not established; the supplied record's separately assessed theory conditions remain bounded accordingly.

## Write side

Acquisition and adoption have different controls. Paper ingest admits metadata and a scaffold; enrichment admits model-derived prose through direct Edit, under source-fidelity rules but without a required fresh jury at every section. Ideation helper creation preserves existing enriched ideas by default. Result-to-claim instead edits idea outcomes in place, and requests explicit experiment overwrite when rejudging. Proof-checker requests claim overwrite on re-audit. These mechanisms do not share a universally enforced admission service: the CLI accepts supplied fields and direct edits remain possible ([MEM-RTE-paper-capture](#mem-rte-paper-capture), [MEM-RTE-evaluation-write](#mem-rte-evaluation-write)).

Maintenance is partly procedural. Generic update/lint and generated Connections are described by `skills/research-wiki/SKILL.md`; the inspected helper dispatch contains ingest, sync, node writers, edges, index, pack, stats and log, but no generic update/lint or Connections regeneration command. The rendered Connections sections remain explanatory placeholders. This prevents treating those advertised maintenance operations as verified executable enforcement. Retraction updates a status; it does not automatically remove a recent refuted/obsolete triple from pack delivery. Duplicate-edge suppression can preserve stale evidence even after a page is rejudged (SRC-1, `tools/research_wiki.py`; [MEM-OBJ-edges](#mem-obj-edges)).

Capture filtering requests dropping or rewriting transient operational failures; threat quarantine instead retains raw text separately while replacing the selected body field. The ideation read gate may reject the entire pack without deleting it. Reviewer retention takes the opposite approach: full response append, including terminal and negative review, without executor curation. Stale review-state cleanup and completed-run receipt isolation do not establish withdrawal of reviewer memory itself ([MEM-RTE-evaluation-write](#mem-rte-evaluation-write), [MEM-RTE-reviewer-memory](#mem-rte-reviewer-memory)).

Trace-fed derived results include the stale-count pivot, projected failed-idea memory, compact summaries and proposed harness instruction changes. Each has a named later consumer; raw usage/review logs alone are not counted as learning. Hypothesis, scope and evidence reasons remain in wiki pages, but the pack can omit them. Compact handoffs retain selected evidence without a losslessness check; full artifacts remain files rather than being demonstrably evicted from the host ([MEM-RTE-stall-pivot](#mem-rte-stall-pivot), [MEM-RTE-pack-read](#mem-rte-pack-read), [MEM-RTE-compact-recovery](#mem-rte-compact-recovery)).

## Read-back

The principal wiki route is requested pull: a later idea-creator invocation asks for a cache, rebuilding only when stale/missing, then scanning immediately before Read. Mutation-triggered rebuild is automatic file production, not unsolicited delivery into an idle model. No semantic query API or background context injector was established. External fetched content has a separate trust surface that the pack gate does not cover ([MEM-RTE-pack-read](#mem-rte-pack-read)).

Reviewer memory has automatic next-round delivery requested by the workflow: completed round triggers append; backend/difficulty selects complete-text prompt injection, a file path, or thread continuation. Budget is not semantic relevance selection. The growing full response history is specifically protected against executor summarization. Harder review can therefore preserve critique at the cost of growing context, while host-side truncation behavior is outside this source boundary ([MEM-RTE-reviewer-memory](#mem-rte-reviewer-memory)).

Compact recovery deliberately selects derived summaries; it does not prove the source window was shortened. A separate reviewer frame keeps the foreground history out by selected prompting, but shared files and provider threads remain reachable. Phase-state reload selects stages, not knowledge. Trace hashes and receipts support audit linkage only to the extent their writers and consumers check them; they do not prove a model read every byte ([MEM-RTE-compact-recovery](#mem-rte-compact-recovery), [RT-RTE-codex-call](runtime.md#rt-rte-codex-call), [MEM-OBJ-review-traces](#mem-obj-review-traces)).

## Integration issues

1. **No supported correction to a supplied runtime fact is required.** Extend its explicitly provisional wiki/maintenance coverage with [MEM-RTE-paper-capture](#mem-rte-paper-capture), [MEM-RTE-evaluation-write](#mem-rte-evaluation-write), and [MEM-RTE-pack-read](#mem-rte-pack-read). The source's ranking/retention claims need qualification as recorded in [MEM-CLM-pack-contract](#mem-clm-pack-contract).
2. **Shared continuity referent, distinct suboperation:** [MEM-RTE-reviewer-memory](#mem-rte-reviewer-memory) intersects [RT-RTE-review-transition](runtime.md#rt-rte-review-transition) at append-before-stop and later review context; it isolates persistence/replay, not a second transition gate. [MEM-RTE-compact-recovery](#mem-rte-compact-recovery) similarly specializes handoffs within [RT-RTE-research-pipeline](runtime.md#rt-rte-research-pipeline). No replaceable duplicate declaration identified after comparison.
3. **Rationale loss and stale relations:** claim scope/experiment reasoning are stored, but not included in pack text; edge evidence is omitted, and existing edges are not withdrawn on rejudge. This prevents concluding that later ideation receives full evaluative warrant or a reconciled current graph ([MEM-OBJ-claims](#mem-obj-claims), [MEM-OBJ-experiments](#mem-obj-experiments), [MEM-OBJ-edges](#mem-obj-edges), [MEM-RTE-pack-read](#mem-rte-pack-read)).
4. **Fresh run versus old reviewer file:** initialization scopes state/receipts by run ID but inspected text does not specify a corresponding memory-file reset/segmentation rule. Prior-run carryover cannot be resolved as guaranteed reuse or guaranteed exclusion ([MEM-RTE-reviewer-memory](#mem-rte-reviewer-memory)).
5. **Maintenance implementation gap:** generic update/lint and Connections regeneration remain model procedures, not established helper operations. Enrichment edits through a different path from body quarantine. Scanner signature completeness and deployment/compliance remain unknown, preventing a uniform trust or curation guarantee ([MEM-RTE-paper-capture](#mem-rte-paper-capture), [MEM-RTE-evaluation-write](#mem-rte-evaluation-write)).
6. **Remaining partial loop:** verification helper, trace writer/native validator, global event-log consumers, style-profile extraction and platform overlays remain uninspected. Their inclusion is not absence; full deployed retention/admission parity is prevented ([MEM-OBJ-events](#mem-obj-events), [MEM-OBJ-review-traces](#mem-obj-review-traces), annotations on [RT-RTE-meta-landing](runtime.md#rt-rte-meta-landing)).

## Limitations and checks

Source HEAD was rechecked as `26b95cfa0d8747078e9e43b42e20952709e561b8`, matching boundary and runtime. Method identity is the supplied invocation, memory type, worker rules and shared records contract; no other attempt, prior characterization or mutable member was used. New source reads are scoped in the coverage table. Available uninspected paths remain uncertainties, not access gaps or absences.

This is implementation/doctrine evidence only. It establishes named persistence/selection capabilities and requested consumer behavior, not deployed compliance, improved capacity, successful memory recall, scientific correctness or causally supported benefit. The strongest source claims were challenged against dispatch/selection and overwrite alternatives, not repeated as guarantees.

Validation: the required `commonplace-run validate-output` check passed: “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” The check establishes deterministic form/quotation checks only.
