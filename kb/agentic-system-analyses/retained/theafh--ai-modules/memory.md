---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "ai-modules memory: raw captures, curated wiki pages, retained audit decisions, task state and context-selection procedures at the frozen commit."
run-id: AAS-2026-10-14-ai-modules-a7044d5627d2-01
source-identity: "https://github.com/TheAFH/ai-modules"
reviewed-boundary: "0cf0227c416f75a79d7317f603a209a63e7a3c8f"
---

# ai-modules memory report

## Boundary and evidence

The subject is ai-modules' filesystem-backed knowledge and work-state machinery at SRC-1, commit `0cf0227c416f75a79d7317f603a209a63e7a3c8f`. The source identity and whole-system functional boundary remain those of [boundary](boundary.md#boundary-and-evidence). The memory account includes wiki admission, retrieval, archival and maintenance; task briefs, close-out and readiness relays; retained evaluation artifacts; installed instructions and standing documents where they constrain later work; and explicit summarization/context controls. It does not treat every file write as memory read-back.

Direct reads below establish implementation or doctrine/design, not execution. The supplied runtime establishes additional interfaces and supplies passages for its records. No target command, test, host or provider was executed. Local corpus instances were not evaluated for factual correctness; their mere presence cannot demonstrate the workflows' compliance. No frozen-source access gap was encountered. Host context assembly, compaction, provider state and actual role isolation remain outside the source boundary.

| Entry point or operation | SRC-1 path and inspection basis | Coverage or remaining limit |
| --- | --- | --- |
| Source import; visible-session extraction | Direct full reads: `plugins/knowledge_management/skills/wiki_import/SKILL.md`, `plugins/knowledge_management/skills/wiki_wrapup/SKILL.md` | Annotation on [RT-RTE-wiki-triage](runtime.md#rt-rte-wiki-triage); raw and page objects below. |
| Direct ingest, query, procedure capture | Direct reads of architecture/page anatomy and operation blocks: `plugins/knowledge_management/skills/wiki/SKILL.md` | [MEM-OBJ-wiki-pages](#mem-obj-wiki-pages), [MEM-RTE-procedure-capture](#mem-rte-procedure-capture); annotation on [RT-RTE-wiki-consume](runtime.md#rt-rte-wiki-consume). |
| Scaffold initialization | Direct full read: `plugins/knowledge_management/skills/wiki/scripts/init_wiki.sh`; hub init instructions | [MEM-OBJ-schema-guidance](#mem-obj-schema-guidance). Template bodies and every discovery branch not inspected; exact generated convention inventory and full walk-up equivalence not established. |
| Source hashing/re-ingest | Direct full read: `plugins/knowledge_management/skills/wiki/scripts/compute_sha256.py`; hub capture block | [MEM-OBJ-raw-body](#mem-obj-raw-body), [MEM-OBJ-raw-frontmatter](#mem-obj-raw-frontmatter). Body hash is not authenticity certification. |
| Lint admission/acceptance | Direct reads: acceptance parser/matcher and main dispatch in `plugins/knowledge_management/skills/wiki/scripts/lint.py` | [MEM-OBJ-lint-acceptance](#mem-obj-lint-acceptance), [MEM-RTE-finding-acceptance](#mem-rte-finding-acceptance). Remaining check bodies, declared-boilerplate and exclusion parsing not fully inspected; no exhaustive correctness verdict. |
| Semantic audit, incremental working set, remediation limits | Direct selected blocks: `plugins/knowledge_management/agents/auto_shaper_wiki.md`; hub archive/audit/log rules | [MEM-OBJ-wiki-log](#mem-obj-wiki-log); maintenance annotation. Correction directly re-read source-drift fix and raw-content constraint: conflicting body-write instructions are retained below. Many other individual fix moves remain uninspected; semantic repair completeness and every provenance migration not established. |
| Task authoring, update, query, archive | Direct archive/query/update reads and scoped searches: `plugins/ai_dev/skills/task/SKILL.md`; full `plugins/ai_dev/skills/task_finish/SKILL.md` | [MEM-OBJ-task-files](#mem-obj-task-files), [MEM-RTE-task-close](#mem-rte-task-close). Full create checks, task-select scoring, task shaper and task lint implementation not read; exhaustive task-family behavior not established. |
| Task implement/audit readiness; rejected repairs | Supplied [RT-RTE-task-implement](runtime.md#rt-rte-task-implement), [RT-RTE-readiness-repair](runtime.md#rt-rte-readiness-repair), [RT-OBJ-relay-files](runtime.md#rt-obj-relay-files) | Memory annotations retain consumers and relay expiry; no new declaration of the same route. |
| Standing project knowledge | Direct scoped search: `AGENTS.md`; task hierarchy search | [MEM-BAP-procedure-guidance](#mem-bap-procedure-guidance) and task annotation. Local `wiki/`, `tasks/`, `CHARTER.md`, companion standing files and their individual histories not substantively inspected; no instance-level truth/compliance claims. |
| Git-derived changelog | Direct full skill read: `plugins/ai_dev/skills/update_changelog/SKILL.md` | [MEM-RTE-changelog-update](#mem-rte-changelog-update). Producer shell implementation and actual changelog not read; evidence-blob completeness and historical accuracy not established. |
| SPR/executive summaries | Direct full reads: `plugins/knowledge_management/skills/spr/SKILL.md`, `plugins/knowledge_management/skills/executive_summary/SKILL.md` | [MEM-CLM-summary-transfer](#mem-clm-summary-transfer). Instructions specify output and intended consumers, not a wired save/reload checkpoint. |
| Generic helper frames and payload trimming | Supplied [RT-RTE-helper-dispatch](runtime.md#rt-rte-helper-dispatch) | Separate contexts at spawned tier, shared window inline; no retained domain artifact owned by generic orchestration. |
| Registration, deployment, charter hook | Supplied [RT-RTE-deploy-artifacts](runtime.md#rt-rte-deploy-artifacts), [RT-RTE-charter-protect](runtime.md#rt-rte-charter-protect), [RT-OBJ-host-config](runtime.md#rt-obj-host-config) | Static instruction delivery and event interception, not learned-memory push. No additional memory admission route inferred from the hook. |
| Evaluator launch/capture/cleanup | Supplied [RT-RTE-evaluator-worker](runtime.md#rt-rte-evaluator-worker) | Retained response/provenance/snapshot consumed by grading/aggregation; next worker is independently restaged. Graders, caching paths and tracked reports uninspected; no training or successful evaluation claim. |
| Remaining formatting, git, editorial, instruction-writing and portability families | Boundary inventory and runtime's stated partial coverage | Detailed retained-output consumers remain uninspected. Prevents a system-wide absence claim or exhaustive memory enumeration beyond the material mechanisms traced here. |

## Core ideas

The wiki separates captured source bodies from model-authored pages, and separates both from navigation and review metadata. Later models orient on schema, index and a bounded recent log, then select page content by question/topic. This is tool-mediated file retrieval governed by instructions, not a demonstrated vector retrieval service. A readable index summary is an access aid, not the underlying source or an opaque payload's complete display ([MEM-OBJ-index](#mem-obj-index), [MEM-OBJ-wiki-pages](#mem-obj-wiki-pages)).

Admission is route-specific. Import permits raw capture before human page selections; wrapup permits no wiki write before selections. Direct hub ingest and trigger-based synthesis filing need not wait for that selection. Semantic maintenance permits autonomous deterministic repairs and preserves contested disagreement for human review. Thus human source curation does not imply human approval of every stored claim ([RT-RTE-wiki-triage](runtime.md#rt-rte-wiki-triage), [RT-RTE-wiki-consume](runtime.md#rt-rte-wiki-consume)).

Two small retained results directly govern later operations: accepted info findings suppress future live lint reports through fixed matching rules, and audit baselines determine which page bodies a later audit cold-reads. They are not interchangeable with knowledge pages. They show how retained experience changes later checking workload without establishing improved accuracy ([MEM-RTE-finding-acceptance](#mem-rte-finding-acceptance), [MEM-OBJ-wiki-log](#mem-obj-wiki-log)).

The label “immutable raw” requires qualification. Hub re-ingest can replace a changed source body after comparison. Maintenance has conflicting instructions: a general raw-content-read-only constraint and a source-drift fix expressly permitting body replacement to re-record the source. Neither instruction's precedence or operational outcome is established. Metadata-only maintenance is therefore not a categorical preservation guarantee. Preserving the previous hash until comparison prevents erasing the drift signal, but refresh afterward does not itself retain every former source version ([MEM-OBJ-raw-body](#mem-obj-raw-body), [MEM-OBJ-raw-frontmatter](#mem-obj-raw-frontmatter)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-raw-body
Label: Captured raw source bodies

Source-native identity: `raw/{articles,papers,meetings,notes}/<slug>.md` body; assets may accompany sources. Storage substrate: ordinary project filesystem, optionally Git. Representational form: natural-language captured/extracted content interpreted by the mining/query model; image assets are not characterized here. Lineage can be published text, extracted paper, spoken transcript, internal memo, pasted material or session-derived writeup. Converted capture is not necessarily the original bytes. Human chooses a source on import; the agent captures and mines it. Body persistence crosses sessions until re-ingest replacement; source revision history depends on project Git practice, not a mandated immutable-version store. Closest supplied record: [RT-RTE-wiki-triage](runtime.md#rt-rte-wiki-triage) describes admission but is a route, not this retained input object. No supplied object counterpart was found.

Evidence: SRC-1, `plugins/knowledge_management/skills/wiki/SKILL.md`, capture and re-ingest blocks. Later consumers are resource mining and pages that cite raw sources; ordinary query does not mandate reopening every source behind every page. This prevents treating source presence as complete source verification at every answer.

> `update` and exit 1 mean drift: rewrite
> the sidecar body to what the source now says, refresh the recorded hash with
> the write-mode command above, and report the drift both to the user and in
> the ingest's `log.md` entry.
> --- `plugins/knowledge_management/skills/wiki/SKILL.md`

Maintenance has a separate, internally conflicting admission contract (SRC-1, `plugins/knowledge_management/agents/auto_shaper_wiki.md`). Its general constraint prohibits content edits, but the source-drift fix permits re-recording the source body while directing page correction and script-based digest refresh. This is a model-interpreted exception, not arbitrary rewrite authority or a mechanical write denial. The helper is instructed to assess source drift and perform the fix without an explicit per-body human approval gate; which instruction controlled actual writes is unobserved. Thus raw-body replacement is contemplated on maintenance as well as hub re-ingest, but the conflicting general constraint prevents a settled maintenance-wide preservation or permission guarantee.

> The `raw/` directory is read-only for content. Update only its
> frontmatter (e.g., `sha256` after a verified re-ingest). All
> corrections live in the wiki layer 2 pages.
> --- `plugins/knowledge_management/agents/auto_shaper_wiki.md`

> Do not edit the raw
> body itself except to re-record what the source now says.
> --- `plugins/knowledge_management/agents/auto_shaper_wiki.md`

#### MEM-OBJ-raw-frontmatter
Label: Raw capture origin and body digest metadata

Source-native identity: `ingested`, `sha256`, `source_url` or repository-relative `source_path` in raw sidecar frontmatter. Storage substrate: same Markdown file as [MEM-OBJ-raw-body](#mem-obj-raw-body), distinct operative part. Representational form: symbolic fields for hash/origin checking, plus natural-language explanations where no eligible path exists. Lineage: source selection/conversion followed by script-computed body digest. Digest records captured-body consistency, not source truth, authenticated authorship or model trust. `source_path` points to an in-repository original; outside-repository local sources instead take excerpts and locality prose. Origin field handling is partially inspected, not fully verified against template and lint implementations.

The hashing utility permits explicit files/directories, no-path raw-tree discovery, check-only and print-only modes. Write mode changes digest frontmatter, not body content. Physical I/O does not decide whether the changed source ought to be admitted: the calling workflow owns that comparison and decision. Maintenance's source-drift fix requests this digest refresh alongside page correction and permits source-body re-recording, in tension with its general content-read-only constraint (passages in [MEM-OBJ-raw-body](#mem-obj-raw-body)). Metadata repair is distinct from body replacement, but is not evidence that maintenance can only change metadata. No supplied object counterpart exists; closest interface is [RT-RTE-wiki-triage](runtime.md#rt-rte-wiki-triage). Evidence: SRC-1, `plugins/knowledge_management/skills/wiki/scripts/compute_sha256.py` and `plugins/knowledge_management/skills/wiki/SKILL.md`.

> actual = hashlib.sha256(body.encode("utf-8")).hexdigest()
> --- `plugins/knowledge_management/skills/wiki/scripts/compute_sha256.py`

#### MEM-OBJ-wiki-pages
Label: Curated typed wiki pages

Source-native identity: entity, concept, comparison, summary, query and procedure pages in flat type directories. Storage substrate: Markdown filesystem files, Git-compatible but no mandatory commit per change. Representational form: natural-language claims, explanations and procedures interpreted by models/humans; frontmatter such as type/tags also supplies symbolic lint inputs. Lineage: raw-source mining, page synthesis, approved visible-session claims, direct authoring and maintenance. This object is distinct from the access metadata in [MEM-OBJ-index](#mem-obj-index) and from raw bodies. Closest supplied record [RT-BAP-wiki-guidance](runtime.md#rt-bap-wiki-guidance) describes its authority path, not its storage object; no duplicate object is proposed.

Consumers: later query, authoring and maintenance models; procedure readers may use instructions for project work. Page confidence, contested flags, dates and sources qualify content but do not enforce truth. Captured-source lineage uses inline claim links and `sources:`; uncaptured derivation can use `## Derived from`. Reason preservation is selective: source evidence/caveats and mechanism explanations can remain, but procedure extraction deliberately strips instances. No claim of complete historical rationale. Evidence: SRC-1, `plugins/knowledge_management/skills/wiki/SKILL.md`, page anatomy, provenance, update and query blocks.

> **Confidence**: opinion-heavy / fast-moving / single-source claims → `confidence: medium` or `low`. Reserve `high` for multi-source support.
> --- `plugins/knowledge_management/skills/wiki/SKILL.md`

#### MEM-OBJ-schema-guidance
Label: Wiki schema and writing conventions

Source-native identity: wiki-owned `SCHEMA.md` domain, page types, tag taxonomy and conventions. Storage substrate: Markdown copied from a shipped template and customized locally. Representational form: natural-language writing guidance to the model; declared enum/taxonomy also parsed as symbolic constraints by lint. Initial authoring agency: script scaffolds, model asks human for domain and starting tags; subsequent maintenance can align scaffold while preserving declared customization. This establishes local initialization instructions, not human authorship of every resulting convention. Consumers: every activated wiki session and lint. Closest supplied [RT-BAP-wiki-guidance](runtime.md#rt-bap-wiki-guidance); distinct object, no supplied object counterpart. Its `## Lint` acceptances are split below because their consumer and enforcement differ.

Evidence: SRC-1, `plugins/knowledge_management/skills/wiki/scripts/init_wiki.sh` and `plugins/knowledge_management/skills/wiki/SKILL.md`. Initializer refuses an existing scaffold or opt-out marker; it does not provide atomic rollback for all initialization errors.

> cp "$REFS/template_schema.md" "$WIKI/SCHEMA.md"
> --- `plugins/knowledge_management/skills/wiki/scripts/init_wiki.sh`

#### MEM-OBJ-lint-acceptance
Label: Accepted info finding declarations

Source-native identity: `- Accepted finding: …` bullets under wiki `SCHEMA.md`'s `## Lint`. Storage substrate: Markdown schema file. Representational form: symbolic category/path plus optional line/message discriminator consumed by fixed `Acceptance.matches` rules. Lineage: reviewed intentional lint finding → maintenance model declaration → future linter partitions matching info out of live issues into acknowledged output. Part distinct from [MEM-OBJ-schema-guidance](#mem-obj-schema-guidance): this is operative checking metadata, not subject knowledge. No supplied counterpart; closest combined maintenance interface [RT-RTE-wiki-consume](runtime.md#rt-rte-wiki-consume).

Authority at consumer: suppress matching info from live report/counts, never matching warn/blocking issues. Path-only matching is limited to whitelisted volatile-message categories; other matches require discriminator. Persistence is across later linter calls while the declaration and matching issue remain. Evidence: SRC-1, `plugins/knowledge_management/skills/wiki/scripts/lint.py`, acceptance matcher/parser and main partition call.

> if issue.severity != SEV_INFO:
>     return False
> --- `plugins/knowledge_management/skills/wiki/scripts/lint.py`

#### MEM-OBJ-index
Label: Wiki page catalog and summaries

Source-native identity: `index.md` sections, page links, one-line summaries and total/update metadata. Storage substrate: Markdown file. Representational form: natural-language summaries for relevance decisions; links/counts have symbolic checking roles. Lineage: model updates after writes, relocations and archives. Consumers: later orientation, query selection, duplicate avoidance and peer discovery. Index summary is access metadata, not a complete page representation; for 100+ pages query adds recursive key-term search. No fixed token budget is specified for index/page reads. Closest supplied [RT-BAP-wiki-guidance](runtime.md#rt-bap-wiki-guidance); distinct object with no supplied counterpart. Evidence: SRC-1, `plugins/knowledge_management/skills/wiki/SKILL.md`, architecture, update-navigation and query blocks; supporting consumption passage in [RT-RTE-wiki-consume](runtime.md#rt-rte-wiki-consume).

#### MEM-OBJ-wiki-log
Label: Wiki action history and audit baselines

Source-native identity: chronological `log.md` entries, including audit baseline and cold-read path metadata. Storage substrate: Markdown action log; rotation guidance names yearly log files. Representational form: natural-language action summaries plus Git baseline/path metadata interpreted by maintenance model for later tool selections. Lineage: actual changed files, with audit/lint zero-change process-record exception. This is a derived action record, not a verbatim conversation/tool trace or the store for domain claims. Closest supplied [RT-RTE-wiki-consume](runtime.md#rt-rte-wiki-consume) describes reading recent log; no supplied log object counterpart.

Consumers: resumed wiki sessions read 20–30 recent entries, roughly 350 lines with roughly 20 lines per entry; later maintenance derives its cold-read set from newest usable audit baseline. First/unknown/noncomparable baseline falls back to full page inventory. New/changed bodies and contradiction peers enter incremental working set; lexical hits can add, not remove, pages. Retained metadata therefore has workload-selection authority at a model consumer, not an executable cache-validity guarantee. Rotation at 500 entries is guidance/info, not demonstrated automatic deletion or universal retrieval of old logs. Evidence: SRC-1, `plugins/knowledge_management/skills/wiki/SKILL.md`, resume/log/pitfall blocks; `plugins/knowledge_management/agents/auto_shaper_wiki.md`, working-set and audit-entry blocks; `plugins/knowledge_management/skills/wiki/scripts/lint.py`, main check dispatch.

> - Audit baseline: <git commit sha used for future diffs, or unavailable>
> - Cold page reads: <comma-separated relative page paths, or none>
> --- `plugins/knowledge_management/agents/auto_shaper_wiki.md`

#### MEM-OBJ-task-files
Label: Durable task intent and lifecycle state

Source-native identity: live `tasks/<scope>_<name>.md` and closed `tasks/archive/<same-name>.md`. Storage substrate: Markdown filesystem files, rename-preserved Git history where tracked. Representational form: natural-language Goal/Approach/Acceptance interpreted by readers; symbolic status/date/provenance/design-extension fields also inspected by lint and workflow rules. Lineage: model-assisted creation, user edits/accepted check findings, computational readiness repair and implementation/audit stamps. Raw helper criticism remains separate in [RT-OBJ-relay-files](runtime.md#rt-obj-relay-files). Durable task body is a current work contract, not an append-only trace of rejected options.

Consumers: implement, gate, audit, finish, search/prior-art readers, including archived precedent. Task content has work-contract authority at model consumers, qualified by standing guardrails and codebase evidence. `design-extended` is produced at implementation, checked at audit, then consumed for architecture refresh; absence reads false without pretending an assessment occurred. Closest supplied [RT-BAP-task-guidance](runtime.md#rt-bap-task-guidance) and [RT-RTE-task-implement](runtime.md#rt-rte-task-implement); distinct object, no supplied task object counterpart. Evidence: SRC-1, `plugins/ai_dev/skills/task/SKILL.md`, hierarchy, body-rationale and archive rules; `plugins/ai_dev/skills/task_finish/SKILL.md`.

### Routes

#### MEM-RTE-procedure-capture
Label: Experience to reusable procedure capture

Endpoints/progression: user workflow request or noticed operational pattern → model states trigger/action/reason → strips instance details → hoists source anecdote and mechanism explanation → bounded procedure page → index update → later operator/model retrieval. Owner/selector: foreground model under wiki procedure rules; host tools perform writes. Operating mode: open operational knowledge authoring. Human supplies a request or later correction, not necessarily per-page approval; imported/session proposals still honor their own selection gate. Reference constraints are source content, wiki schema and three generality tests, not an independent answer oracle. Admission rejects one-off stories without reusable rule; splits overlong content and redirects mechanism description to concepts. No transaction rollback specified.

Distinct from [RT-RTE-wiki-triage](runtime.md#rt-rte-wiki-triage)'s source/session approval and [RT-RTE-wiki-consume](runtime.md#rt-rte-wiki-consume)'s general hub route: this is the specialized instance-stripping derivation, usable through both interfaces. Evidence: SRC-1, `plugins/knowledge_management/skills/wiki/SKILL.md`, capture-procedure block.

- Immediate return: Rule/procedure page and navigation changes with workflow report.
- Later read-back: Procedure persists for subsequent wiki questions and operator work; instance may remain in raw sidecar, mechanism reason on concept page.
- Delegated visibility: inapplicable — this capture block does not require a helper.
- Selection predicate: Reusable trigger/action/reason surviving strip-the-name, future-operator and repeated-trigger tests.
- Invalidation or expiry: Ordinary wiki update/archive and maintenance; no automatic TTL.
- Activation or effect: Requests reusable natural-language guidance with specific instance removed; exercised effect on a later decision unobserved.
- Evidence limits: Prompt contract; no inspected instance-to-procedure execution trace or capacity comparison.
- design conclusion status: claimed
- operation conclusion status: uninspected

> **Name the rule.** State the policy in 1 to 3 sentences using the form
> "When [trigger], do [action], because [reason]."
> --- `plugins/knowledge_management/skills/wiki/SKILL.md`

A trace-fed use is afforded when the noticed pattern comes from operations, but not every procedure has trace origin. The result retains a stated reason; source instances are intentionally omitted and may be hoisted elsewhere. No particular formulated theory or theory-specific criticism cycle is established here; learning remains uninspected because persistence/generality tests do not demonstrate improved future capacity.

#### MEM-RTE-finding-acceptance
Label: Persist intentional lint finding acceptance
Part of: [RT-RTE-wiki-consume](runtime.md#rt-rte-wiki-consume)

Endpoints/progression: maintenance linter finding → model judges intentional info → schema acceptance bullet → later lint parse/match → acknowledged output and reduced live report. Owner: maintenance model admits declaration; fixed Python rules decide suppression at consumer. This is a material subroute of the supplied combined maintenance route, not a duplicate. Context: finding, page intent, schema grammar. Operating mode: open audit with deterministic consumer matching. Human can correct or remove declaration; no per-finding human approval is required by the maintenance instructions. Matching rule/severity is a reference outcome, not a truth oracle for intentionality. Invalid or too-coarse acceptance matches nothing; recovery is correction/removal of the bullet, not rollback of content.

- Immediate return: Schema change and maintenance report; next lint emits acceptance acknowledgement.
- Later read-back: Later linter invocation loads retained [MEM-OBJ-lint-acceptance](#mem-obj-lint-acceptance), changing live issue output.
- Delegated visibility: Maintenance helper reads findings and schema; foreground receives report/files rather than full audit window.
- Selection predicate: Intentional info finding, then category/path and allowed exact line/message matching.
- Invalidation or expiry: Declaration removal or mismatch after path/line/message change; allowed path-only matches intentionally tolerate volatile messages.
- Activation or effect: Fixed matching/partition is wired; changed decisions by a later maintenance model and successful workload reduction remain unobserved.
- Evidence limits: Consumer code inspected; no repeated audit trace or assessment of whether accepted issues were correctly judged.
- design conclusion status: claimed
- implementation conclusion status: wired
- operation conclusion status: uninspected

Evidence: SRC-1, `plugins/knowledge_management/agents/auto_shaper_wiki.md`, verify block; `plugins/knowledge_management/skills/wiki/scripts/lint.py`, acceptance/main blocks; matcher passage in [MEM-OBJ-lint-acceptance](#mem-obj-lint-acceptance).

> The next run drops
> it from the live report, so the decision is made once instead of
> being re-justified in prose and re-logged on every audit.
> --- `plugins/knowledge_management/agents/auto_shaper_wiki.md`

This is an automatic trace-fed update of checking metadata when the helper writes it, not source-content synthesis or model-weight learning. The original input is lint output plus model/human-authored page intent; retained declaration may omit explanatory rationale. Its fixed consumer needs the match key, not the rationale.

#### MEM-RTE-task-close
Label: Archive task and retain durable lessons

Endpoints/progression: user close/park request → read current task/status → finish vs defer decision → audit or trusted audited stamp for finished → terminal status/rename/link repair → optional architecture refresh → scoped lint → lasting lesson through wiki where warranted. Owner: foreground model; host tools execute changes. Open requested close-out, not a benchmark. Human directs finished/deferred; ambiguity asks before writing. Reference outcome is codebase/audit evidence for finished, not task prose or model judgment alone. Admission differs from [RT-RTE-task-implement](runtime.md#rt-rte-task-implement), which stops before close-out. No supplied close-out route counterpart found.

Task preserves delivered body/history while lifecycle/location changes. Finished architecture refresh uses retained `design-extended: true` and doc presence; missing/false declines without requiring full code reread on trusted-stamp path. Deferred asserts no completion and skips verification. Already terminal tasks remain unchanged. Lint findings must be resolved for moved file; no full multi-file rollback promised. Evidence: SRC-1, `plugins/ai_dev/skills/task_finish/SKILL.md`, workflow; `plugins/ai_dev/skills/task/SKILL.md`, archive/lesson blocks.

- Immediate return: Archived task path/status, link repairs, architecture refreshed/declined/absent, verification/lint report.
- Later read-back: Archived tasks remain searchable precedent; refreshed architecture informs task creation/family decisions; captured lessons enter later wiki retrieval.
- Delegated visibility: inapplicable — ordinary close-out does not require isolated helpers.
- Selection predicate: User names task; audited stamp trusted unless fresh changed-code evidence; architecture trigger uses recorded design-extension signal; durable lesson judged from finished work.
- Invalidation or expiry: Archived terminal status retained; fresh code-change evidence invalidates reliance on prior audit for closing; no fixed TTL on lessons/docs.
- Activation or effect: Requests retained task location/status and conditional derived design/lesson knowledge; later influence unobserved.
- Evidence limits: Prompt-governed workflow; audit implementation, individual lessons and actual architecture refresh not inspected as execution.
- design conclusion status: claimed
- operation conclusion status: uninspected

> **Capture a lasting lesson in the wiki when archiving.** Where the finished work taught something durable about the project, record that lesson through the `wiki` skill as the task file moves to `archive/`, so the lesson survives the task that produced it.
> --- `plugins/ai_dev/skills/task/SKILL.md`

Trace origin of a lesson is finished project work, potentially mixed with session evidence and task/code interpretation; this is a requested extraction route, not proof that every archived task produced learning. Procedure form uses [MEM-RTE-procedure-capture](#mem-rte-procedure-capture); other lesson types remain possible.

#### MEM-RTE-changelog-update
Label: Git history to retained changelog update

Endpoints/progression: user request → model selects committed dates using existing latest day → per-day script context blob → ordered complete reads → model logical-change/category/theme summaries → add-only `CHANGELOG.md` → repository lint/report. Owner: foreground model, script supplies evidence, host edits file. Operating mode: open documentation request. Model admits summaries under skill format; human can follow up, with no mandatory prewrite approval. Reference is committed history, not independent summary oracle. Existing entries are preserved; newest day reopened for newly found commits. Lint failures leave delivered file standing, not automatically reverted. No supplied counterpart after comparison with [RT-CLM-persistent-context](runtime.md#rt-clm-persistent-context); unlike task/wiki, consumer is subsequent changelog maintenance and documented human history reading.

- Immediate return: Updated day-grouped Markdown changelog and verification outcome.
- Later read-back: Next incremental invocation reads latest recorded day and compares reopened section to committed history; older sections remain history.
- Delegated visibility: inapplicable — no helper required; per-day file pointer transfers script evidence to foreground model.
- Selection predicate: Latest recorded day plus newer commit dates; cold build all committed dates, oldest to newest.
- Invalidation or expiry: Most recent day provisionally complete, reopened for same-day commits; older entries frozen by policy, not automatically regenerated.
- Activation or effect: Requests derived change history; cold-build day sections flushed to disk between days; no behavioral-learning benefit established.
- Evidence limits: Skill inspected, shell evidence producer not inspected; instructions to release prior context are not a demonstrated host eviction mechanism.
- design conclusion status: claimed
- operation conclusion status: uninspected

Evidence: SRC-1, `plugins/ai_dev/skills/update_changelog/SKILL.md`. Substrate is Markdown; generated day summaries are natural language. Retained output intentionally omits explanation, so it is not a complete rationale store.

> <summary_style>Write summaries in plain English, past tense, describing what was done. Leave why and how out of the summary. Stay concise but specific enough that a reader unfamiliar with the codebase understands the scope.</summary_style>
> --- `plugins/ai_dev/skills/update_changelog/SKILL.md`

### Claims

#### MEM-CLM-summary-transfer
Label: Standalone compression for later readers

Claimed operation: SPR bullet priming allows an otherwise unexposed LLM to reconstruct source meaning; executive summary preserves logic at a 10–15% length target for professional readers. These are model-consumed natural-language transformation contracts, not numerical embeddings or tested reconstruction guarantees. Closest supplied [RT-OBJ-skill-bodies](runtime.md#rt-obj-skill-bodies) covers their installed instruction bodies; this claim concerns output intent rather than duplicate body identity. Evidence: SRC-1, `plugins/knowledge_management/skills/spr/SKILL.md`, `plugins/knowledge_management/skills/executive_summary/SKILL.md`.

> <objective>Convert human-provided input into a compact, structured SPR that lets another LLM, not previously exposed to the input, reconstruct the original material as completely as possible. Maximize semantic recoverability by encoding the deepest structure and nuance of the input with minimal tokens.</objective>
> --- `plugins/knowledge_management/skills/spr/SKILL.md`

No inspected contract specifies saving these outputs into a checkpoint or automatically reloading them into another invocation. The external recipient role affords transfer, not a wired retained-memory route. Self-ratings are model judgments, not independent answer oracles. Alternative host compaction/checkpoint payloads remain uninspected outside SRC-1.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-procedure-guidance
Label: Stored procedural knowledge to project operations

Consumer: later project operator or model working from wiki procedure/standing knowledge. Channel: retrieved procedure text and linked concepts/source evidence; repository-local standing instructions specifically direct index reading before harness work. Force: natural-language operational guidance, not an executable permission grant. Horizon: across sessions/projects' task lifecycles while content remains current and accessible. No automatic broadcast to other repositories: installed skill/reference content travels, repository wiki does not. Closest supplied [RT-BAP-wiki-guidance](runtime.md#rt-bap-wiki-guidance) emphasizes answer/write decisions; this path distinguishes operational procedure consumers and local scope, not a replacement.

Evidence: SRC-1, `plugins/knowledge_management/skills/wiki/SKILL.md`, procedural/declarative split; `AGENTS.md`, local work-state rule.

> Read `wiki/index.md` before starting harness work, and write a newly verified fact back there with its date and source.
> --- `AGENTS.md`

## Annotations

#### On [RT-RTE-wiki-triage](runtime.md#rt-rte-wiki-triage)

Write agency and trace origin differ by entry: import model mines one captured resource end-to-end; wrapup model mines only visible session, excluding abandoned hypotheses/transient/private items. A source-message pointer is not retained access to evicted or unseen turns. Human selects page candidates, not source truth; import raw admission already happened and rejected page proposals can leave raw capture retained. Wrapup rejection leaves wiki unchanged. Session extraction is trace-fed derivation when approved, not mere logging; its later consumers are wiki query/maintenance and potentially procedure users. Full session transcript persistence is not required by this contract. Evidence: SRC-1, `plugins/knowledge_management/skills/wiki_import/SKILL.md`, `plugins/knowledge_management/skills/wiki_wrapup/SKILL.md`.

> <mine_session>Extract durable claims, decisions, definitions, conventions, comparisons, workflows, and named entities. Skip abandoned hypotheses, transient back-and-forth, and user-private ephemera.</mine_session>
> --- `plugins/knowledge_management/skills/wiki_wrapup/SKILL.md`

#### On [RT-RTE-wiki-consume](runtime.md#rt-rte-wiki-consume)

Read-back trigger is user question or activated ingest/audit, not an independent push service. Foreground selector uses schema/domain, index summaries and question keywords; for 100+ pages adds recursive search. Selected page content reaches model by tool reads and informs cited answers and further writes. Budget is bounded recent history (20–30 entries/~350 lines), roughly 200-line page splitting and isolated audit work; no hard global token cap or fixed top-k page count is supplied. Query synthesis retains cross-page reasoning at medium confidence pending user validation, then can be selected in a later query. It does not independently verify every underlying raw claim.

Maintenance consumer instead selects full inventory at unknown baseline or new/changed pages plus discovered contradiction peers at usable baseline ([MEM-OBJ-wiki-log](#mem-obj-wiki-log)). Audit metadata survives even a zero-change run. Retained accepted findings reach fixed lint matching ([MEM-RTE-finding-acceptance](#mem-rte-finding-acceptance)). Archive removes page from index and live inbound links become text; retained `_archive/` remains on disk, but no normal query route specifically reloads it. The generic large-wiki recursive-search wording does not prove archives are unreachable; no hard exclusion from every possible tool search is claimed.

Evidence: SRC-1, `plugins/knowledge_management/skills/wiki/SKILL.md`, orientation/query/archive blocks; `plugins/knowledge_management/agents/auto_shaper_wiki.md`, working-set/remediation/verify blocks. Isolated broad maintenance keeps dozens of reads out of foreground window; per-file report and changed files cross back. This resembles a call frame only where host actually spawns: files are durable/reachable, not live references inside a window. Existing pending syntheses and contested flags have no demonstrated automatic expiry. Raw-content admission is internally conflicted: the general read-only constraint and source-drift re-recording exception both apply to this helper's instructions; the source does not establish which controlled operation ([MEM-OBJ-raw-body](#mem-obj-raw-body)).

> **Contradictions are explicit.** Record both with dates, mark in frontmatter, flag for review.
> --- `plugins/knowledge_management/skills/wiki/SKILL.md`

#### On [RT-OBJ-relay-files](runtime.md#rt-obj-relay-files)

Memory lineage: frozen intent/task snapshots preserve baseline; helper proposals, gate/verifier returns and diffs preserve criticism/evidence used by subsequent helper invocations. These are substantive within-run later-invocation inputs, although expiry at next same-stem run limits cross-run retention. Frozen snapshots are verbatim baselines, returns natural-language derived judgments, and diff/anchor comparison has a symbolic role. Do not classify the entire directory as a learned domain store. Evidence and expiry passage supplied in this record; SRC-1, `plugins/ai_dev/skills/task_auto_check/SKILL.md`. Reasons may remain in helper returns, but their permanent inclusion in final task is not guaranteed.

#### On [RT-RTE-readiness-repair](runtime.md#rt-rte-readiness-repair)

Retained output consumed by later implementation is the repaired task, not all helper history. Within the run, pointer-admitted inputs select different relay subsets; blind gate omits prior returns while verifier intentionally receives them. Criticism can be rejected, approved edits can be reverted after delta failure, and final task must not inherit unverified changes. Relay retention after return enables inspection but not automatic next-run reuse. The next same-stem initialization clears it. This preserves a positive trace-to-repair-to-consumer chain without asserting capacity improvement or model-weight change. Source/passages supplied by runtime; SRC-1, `plugins/ai_dev/skills/task_auto_check/SKILL.md`, `plugins/ai_dev/agents/auto_gate_task.md`.

#### On [RT-BAP-task-guidance](runtime.md#rt-bap-task-guidance)

Retained task admission and downstream authority are separate. User accepted check findings can edit task and declare ready; computational readiness applies verified proposals under fixed intent. Later implement reads work contract but also consults codebase/guardrails. The task hub's ordered evidence can consult archived precedent and wiki, so retained closed work is not merely dead bookkeeping. Rejected-option rationale is directed to commit/PR or wiki, not task body; later rationale access therefore depends on those other records and tools. Evidence: SRC-1, `plugins/ai_dev/skills/task/SKILL.md`, body/open-decision/update rules; later implementation passage supplied in [RT-RTE-task-implement](runtime.md#rt-rte-task-implement).

## Write side

Acquisition, derivation and admission are distinct. Source capture writes converted content plus body digest before import candidate approval; wrapup instead proposes from visible session before writing. Direct ingest can bypass triage and skip takeaway discussion in cron contexts. Re-ingest compares fresh body under old digest before body/hash replacement. Maintenance additionally contains both a general raw-content prohibition and a source-drift body-re-recording exception; no observed precedence resolves that conflict. “Immutable” therefore cannot establish either a content write denial or maintenance-wide body preservation ([MEM-OBJ-raw-body](#mem-obj-raw-body), [MEM-OBJ-raw-frontmatter](#mem-obj-raw-frontmatter)). No provenance signature or trusted-source attestation follows from a matching digest.

Wiki page writes can create, extend, split, flag disagreement, retain synthesis or archive. Newer dates generally supersede older content, but genuine contradictions preserve both positions/dates/sources for human resolution. Maintenance autonomously applies recoverable safe fixes; raw metadata can change, and its explicit source-drift body-re-recording exception conflicts with its general raw-content-read-only constraint. Neither categorical body preservation nor unrestricted replacement follows, and no evidence establishes which instruction won in operation. Page identity is preserved rather than deleting outright. Full supersession withdraws active navigation while keeping archive bytes. There is no atomic rollback or forced semantic approval across all writes ([MEM-OBJ-wiki-pages](#mem-obj-wiki-pages), maintenance annotation).

Trace-fed transformations include approved session mining, conditional completed-task lesson extraction, procedure instance stripping and audit-result metadata updates. Their derived products and later consumers are named separately. Raw logs or evaluation snapshots alone are not enough to establish learned guidance. Procedure reasons can survive while instances move elsewhere; task rationale may live outside task; changelog specifically discards why/how. None warrants a universal claim that all derived decisions retain reasons ([MEM-RTE-procedure-capture](#mem-rte-procedure-capture), [MEM-RTE-task-close](#mem-rte-task-close), [MEM-RTE-changelog-update](#mem-rte-changelog-update)).

Initial schema customizations ask for domain/tags; lineage of every preexisting page, task or standing instruction remains uninspected. Subsequent supported transformations do not depend on resolving all initial authorship. Deployment admits already-authored instruction/config bodies by selection/filtering; uninstall/backup concerns installed artifacts, not removal of accumulated wiki/task knowledge ([RT-RTE-deploy-artifacts](runtime.md#rt-rte-deploy-artifacts)).

## Read-back

There are three distinct channels. Question-driven wiki retrieval supplies selected natural-language knowledge; task lifecycle invocations load named durable briefs and evidence; fixed linter rules consume accepted-finding metadata. Audit baseline selection is prompt-governed model use of Git comparisons rather than fixed cache enforcement. The report does not merge these authorities into one “memory” permission level.

Working-context controls are orientation budgets, topic/index selection, semantic-audit change filtering, spawned audit/helper frames, pointer-only relays, and changelog one-day evidence processing. These determine what enters/remains outside a model window. Changelog flush instructions and SPR transfer intent are not proof of actual context eviction, host compaction or checkpoint reload. Inline generic helper degradation shares the window rather than obtaining isolation ([RT-RTE-helper-dispatch](runtime.md#rt-rte-helper-dispatch), [MEM-CLM-summary-transfer](#mem-clm-summary-transfer)). Host assembly and inaccessible provider state remain opaque; [RT-CMP-host-model](runtime.md#rt-cmp-host-model) supplies the model-form/fixity limits.

No included evidence establishes unsolicited accumulated-memory injection. Skill activation automatically asks orientation reads but remains request/activation-conditioned. Static role/skill delivery is a different channel, already [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance). Evaluator artifacts are read by grading/aggregation and previous benchmark comparison, not wired into future worker prompts as learning; temporary scenario roots are removed after snapshot, retained outputs remain. Exact grader transformations/caches are uninspected ([RT-RTE-evaluator-worker](runtime.md#rt-rte-evaluator-worker)).

## Integration issues

- Corrected maintenance admission boundary: [MEM-OBJ-raw-body](#mem-obj-raw-body) retains both SRC-1 `plugins/knowledge_management/agents/auto_shaper_wiki.md` passages: the general content-read-only constraint and the source-drift exception allowing re-recording what the source now says. The previous categorical maintenance body prohibition is withdrawn. [MEM-OBJ-raw-frontmatter](#mem-obj-raw-frontmatter), Core ideas, Write side and the maintenance annotation now distinguish digest-only physical I/O from the broader conflicting workflow. Which instruction controlled operation remains unresolved; neither guaranteed raw-body preservation nor unrestricted autonomous replacement is justified. Hub re-ingest separately permits replacement after comparison. Neither retained raw nor refreshed digest proves retention of earlier versions. This qualifies [RT-RTE-wiki-consume](runtime.md#rt-rte-wiki-consume)'s maintenance interface without changing its supplied record.
- Added maintenance distinction: [RT-RTE-wiki-consume](runtime.md#rt-rte-wiki-consume)'s broad maintenance description must not be read as full cold page reads every audit. Shaper's explicit working-set rules permit incremental cold reads and retain audit baseline even when no content changes. [MEM-OBJ-wiki-log](#mem-obj-wiki-log) carries evidence and the prevented exhaustive-audit inference.
- Explicit containment: [MEM-RTE-finding-acceptance](#mem-rte-finding-acceptance) is a specialized part of the supplied combined maintenance route. [MEM-OBJ-lint-acceptance](#mem-obj-lint-acceptance) has fixed lint consumer authority, unlike ordinary schema guidance. No replacement/supersession is proposed.
- Possible authority-path overlap: [MEM-BAP-procedure-guidance](#mem-bap-procedure-guidance) and [RT-BAP-wiki-guidance](runtime.md#rt-bap-wiki-guidance) share page/tool delivery. Operational procedure use and repository-local harness work distinguish the narrower path; reconciliation can retain it as a facet rather than assume distinct storage.
- [MEM-RTE-procedure-capture](#mem-rte-procedure-capture) overlaps hub ingest and triage but spans both, not exactly one parent. Its instance-stripping/hoisting consumer chain is the distinct finding. Task-close and changelog-update have no supplied route counterparts.
- Missing facts: individual semantic fix moves, task-family shaper/select/linter details, corpus instance provenance, remaining family output consumers and evaluator graders/caches remain available but uninspected. Coverage table keeps each prevented conclusion local. These limits prevent exhaustive whole-system memory guarantees, not the positive routes above.
- Audit baseline freshness and accepted-finding intentionality have no inspected run evidence. The design supplies fallback/matching rules, but reliable cold-read invalidation, correctly judged suppression and later knowledge influence remain unobserved. No theory-builder, learning or self-improvement result follows from these retained routes alone.

## Limitations and checks

The consequential counterexamples tested by source inspection were direct hub filing against universal human approval, changed-source re-ingest and maintenance's explicit source-drift exception against absolute raw immutability (while retaining its conflicting general constraint), incremental audit against universal full corpus cold-read, symbolic severity matching against arbitrary lint waiver, archived precedent against “closed tasks never read,” and absent save/reload contract against treating every summary as a deployed checkpoint. Conclusions above reflect those qualifications rather than suppressing positive mechanisms.

Source identity was rechecked with Git HEAD at the exact frozen revision; source worktree status was clean. Method identity is the complete supplied invocation, memory type, collection and shared records contract. No other analysis, attempt or engine metadata was read. The records contract's final range was read through its ending; trailing empty-line notices carried no omitted substantive text. Executable checks below concern Commonplace output structure/citations/quotation occurrence, not target execution or truth. Operation, capacity improvement and causal benefit are unobserved; source-native reliability claims remain doctrine, not measurements.

Validation: invocation-specific `commonplace-run validate-output` passed for this correction. The check establishes output form, relation resolution and quotation occurrence, not semantic correctness or acceptance.
