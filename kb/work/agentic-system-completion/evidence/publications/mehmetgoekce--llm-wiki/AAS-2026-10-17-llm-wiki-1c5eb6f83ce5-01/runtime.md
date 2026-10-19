---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "llm-wiki runtime baseline: Claude Code skill dispatch, wiki initialization, retrieval and human-gated maintenance at the frozen revision."
run-id: AAS-2026-10-17-llm-wiki-1c5eb6f83ce5-01
reviewed-boundary: "11538c1195666db24e25e23cc64bb1d70587aef9"
---

# llm-wiki runtime report

## Runtime account

### Ownership and evidence

llm-wiki supplies a natural-language maintainer procedure, configuration and templates, plus executable setup scripts. Claude Code supplies the agent, model, tool execution and session. The target is not an enclosing runtime. Its consequential work is transforming sources into linked retained pages, selecting those pages for later answers, and maintaining routing and L1 rules. These are prescribed model behaviors, not executable maintenance algorithms (SRC-1, `SKILL.md`, `scripts/init-wiki.sh`).

> Wiki maintainer for a personal or team knowledge base. You process source material and distribute extracted knowledge across wiki pages, maintain cross-references, and ensure structural integrity.
> --- `SKILL.md`

All findings below use SRC-1 at the boundary's pin. Implementation inspection covers `setup.sh`, `scripts/init-wiki.sh` and both plugin manifests. Doctrine inspection covers the complete `SKILL.md`, both Schema templates and README Privacy section; the latter supplies attributed privacy claims, not execution evidence. The manifests and schema paths extend or confirm the boundary's initial inspection. No traces, provider outputs, experiments or deployed permissions were supplied or generated. Operation, reliable compliance and benefit remain uninspected. Supporting specifications and diagrams are not needed to establish the shipped prompt's behavior and are not used as conformance evidence.

### Entry, ordinary invocation and return

The plugin manifest requires a wiki-root directory; marketplace source `./` selects the repository root. The alternate shell installer copies the same skill into `.claude/commands/wiki.md`, substitutes the wiki and repository paths, and exposes `/wiki` instead of `/llm-wiki`. This copy does not update with plugin releases. Skill loading and automatic L1 loading are external host contracts, not independently enforced here (SRC-1, `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `setup.sh`, `SKILL.md`; [RT-BAP-skill-dispatch](#rt-bap-skill-dispatch)).

Consider a user issuing `/llm-wiki ingest <file>`. The host foreground agent owns progression. First it resolves the configured root, reads `llm-wiki.yml`, selects Logseq or Obsidian conventions and reads the schema. An unresolved placeholder or absent config is a prescribed stop; a conflicting `wiki_path` in the config only produces a warning, and the plugin/copied root wins. The agent reads the source, extracts facts and entities, scans candidate existing pages, decides which pages and cross-references to change, writes state/history and hub routing lines, checks required properties, links and credentials, and reports page changes and warnings. Structural changes require a Git commit. The skill does not insert a human approval for each ingest fact; the user's invocation starts an open-ended transformation, while model judgment supplies content and placement (SRC-1, `SKILL.md`; [RT-RTE-source-ingest](#rt-rte-source-ingest)).

Logseq state is flat `pages/Wiki___...md` with block properties; Obsidian state is hierarchical `Wiki/...md` with YAML. The shell initializer creates Obsidian hubs as `Wiki/<namespace>/_index.md`, whereas examples in the skill use logical `[[Wiki/NS]]` hub names. No real vault was inspected, so actual resolution between logical names and these files is not established. Both schemas are retained, model-interpreted instructions rather than a validating parser (SRC-1, `scripts/init-wiki.sh`, `templates/logseq/Schema.md`, `templates/obsidian/Schema.md`; [RT-OBJ-schema](#rt-obj-schema)).

A later query takes the user's question, reads candidate namespace hubs, ranks their routing descriptions/tags, loads three relevant pages with a maximum of five, and synthesizes an attributed answer with confidence/staleness warnings. It logs actual full-page reads before synthesis. No subagent, separate task frame or target-owned compactor is specified. “Max 3 loaded simultaneously” and JIT batching request context restraint but supply no host mechanism for removing already-read text from the model window. The mechanism demonstrably described is preferential admission of small routing indexes and selected pages, not guaranteed eviction of prior context (SRC-1, `SKILL.md`; [RT-RTE-wiki-query](#rt-rte-wiki-query)).

### Forcing cases and limits of guarantees

Three source-supported cases materially qualify an idealized account:

1. **Empty or ineffective routing.** Query explicitly falls back to grep across all pages and can rediscover archived pages. Thus index demotion changes preferred selection, not read access or graph membership. Re-promotion is offered rather than automatic. The same query also appends the access log without confirmation, so “User must confirm before any writes” belongs to its optional content write-back phase, not a universally read-only query guarantee (SRC-1, `SKILL.md`; [RT-RTE-wiki-query](#rt-rte-wiki-query), [RT-RTE-index-prune](#rt-rte-index-prune)).

> - L3 fallback when routing yields nothing useful (namespace unclear, hub index missing/empty, no
>     routing line matches): classic grep across all wiki pages -> top 3-5. This is the slow
>     backing-store scan and should be the exception, not the default
> --- `SKILL.md`

2. **Setup through a different entry.** The initializer skips existing paths; skill setup stops on existing config unless the user requests missing pages. But `setup.sh` can delete an existing config after confirmation and then invoke initialization with newly collected settings. Consequently non-overwrite is an initializer behavior, not an invariant across the installer. Partial writes are not transactionally rolled back. Git failure leaves created files uncommitted; staging only created paths does not prove the commit contains only those paths if unrelated files were already staged (SRC-1, `setup.sh`, `scripts/init-wiki.sh`; [RT-RTE-wiki-setup](#rt-rte-wiki-setup)).

3. **Stale L1 or credentials.** L1 verification uses local read-only evidence and per-item confirmation, but the skill explicitly disclaims action-time interception. Rules still load through Claude Code outside this target. Credential exclusion and read-only checking are policies interpreted by the same agent with host tool access, not target-owned filesystem or network isolation. Credential rules cannot be demoted to a git-tracked wiki; existence checks must not print values (SRC-1, `SKILL.md`; [RT-RTE-l1-verification](#rt-rte-l1-verification), [RT-ABS-action-gate](#rt-abs-action-gate)).

> Out of scope: warning at the moment a due rule is about to justify an action. Claude Code loads L1, not
> llm-wiki — there is no hook to enforce that gate, so do not claim one.
> --- `SKILL.md`

The capability surface includes host Read/Glob/search, URL WebFetch, file edits and shell/Git. The current grant set, approval configuration and deployed sandbox are uninspected. No wrapper around all host tool calls is supplied by the inspected skill, manifests or setup scripts. Direct user edits, another host command, or a copied older skill are not covered by the current skill's policies. The target does not specify provider-native tool execution, remote workers, dynamic extension dispatch or manual execution-graph APIs; these host possibilities cannot be classified as safely mediated by llm-wiki. The executable shell paths are separately traced, not assumed subject to the model's page-quality gate (SRC-1, `SKILL.md`, `setup.sh`, `scripts/init-wiki.sh`, `.claude-plugin/plugin.json`).

### Guarantee ownership and change admission

| Claim and owner | Enforcement and strength | Coverage and required external contract | Conclusion statuses |
|---|---|---|---|
| Existing pages/config preserved by initializer | `write_file` checks `os.path.exists`; implementation guard, not race-proof or transactional storage | Single initializer path; installer can first remove config; filesystem supplies ordinary path/I/O behavior | implementation conclusion status: wired; operation conclusion status: uninspected |
| Credentials excluded; non-wiki pages untouched; JIT limit | Maintainer reads constraints and performs quality/lint checks; policy | Skill-mediated work only; needs host/model compliance, no independent isolation demonstrated | design conclusion status: claimed; operation conclusion status: uninspected |
| L1 edits approved per item; evidence read-only/local | Agent asks user and interprets response; protocol | `prune --l1`; no universal host approval interceptor or action-time freshness gate | design conclusion status: claimed; operation conclusion status: uninspected |
| History retained and demotion reversible | Agent moves old state into History or routing lines into Archive; protocol | Ingest/L2 prune and compliant repairs; L1 deletion is explicitly different and lacks Git undo | design conclusion status: claimed; operation conclusion status: uninspected |
| Structural changes committed | Agent instruction; initializer attempts Git with warning on failure; best effort | Wiki Git repository and working Git identity required; access-log writes deferred; L1 excluded by doctrine, not automatically protected by these scripts | implementation conclusion status: wired; operation conclusion status: uninspected |

The anchors and passages for these guarantees are in the route records below. None is an observed deployment guarantee. README's local/no-backend privacy account must be read with its explicit acknowledgment of Claude processing; local files do not establish local-only model inference (SRC-1, `README.md`, `SKILL.md`, `scripts/init-wiki.sh`).

> - Claude reads the content you work with in order to do the work. That processing is covered by your own Claude plan and Anthropic's terms, not by this plugin.
> --- `README.md`

Product behavior changes through plugin releases or replacing a copied skill; this source supplies installation/copy mechanisms, not a demonstrated updater implementation or self-editing loop. Retained knowledge changes through ingest/import, optional query write-back, pruning, lint repairs and user-approved L1 verification. Status reads recent Git activity, access reasons and hot/cold counts; lint updates the Dashboard and may repair content with `--fix`. These are source-native feedback/admission mechanisms, not evidence that future answers improve. The host model's distributed parameters and deployment resolution remain external ([RT-CMP-claude-code](#rt-cmp-claude-code)).

## Shared records

### Components

#### RT-CMP-claude-code
Label: Claude Code model and executor

Source-native identity is Claude Code, described as powering the persistent wiki in SRC-1, `SKILL.md`. The model supplies distributed-parametric interpretation; provider-side weight storage and any other provider state are uninspected. Host session/tool execution is external machinery, not numerical state shipped in this repository. Parameters changing during operation: uninspected — no provider implementation supplied. Exact model version pinned: uninspected — target skill and plugin manifest name no exact model version. Mutable endpoint resolving to another model: uninspected — host/provider resolution is outside the frozen source. This prevents conclusions about fixed weights, host learning or model-level reproducibility, not about the inspectable prompt procedure.

> Persistent knowledge management powered by Claude Code. Maintains a structured wiki in Logseq or Obsidian using the L1/L2 cache architecture.
> --- `SKILL.md`

### Operative objects

#### RT-OBJ-skill
Label: SKILL maintainer procedure

`SKILL.md` is a natural-language decision procedure stored as Markdown in the plugin checkout, or copied to a project command file. Frontmatter names the skill; its body gives dispatch, safety and maintenance instructions to the host model. Copied path placeholders are substituted symbolically by Python; the procedure remains model-interpreted. SRC-1, `SKILL.md`, `setup.sh`, `.claude-plugin/plugin.json`.

> This step copies the skill to one project's .claude/commands/wiki.md. The copy is invoked as /wiki and does not update.
> --- `setup.sh`

#### RT-OBJ-schema
Label: Wiki Schema conventions

Generated Wiki/Schema is natural-language guidance with symbolic-looking property examples, stored in the selected vault's Markdown. It supplies required page properties, naming, cross-reference and L1/L2 rules to the maintainer and lint consumer. It is not an executable schema validator. The initializer replaces date/namespace placeholders. SRC-1, `scripts/init-wiki.sh`, `templates/logseq/Schema.md`, `templates/obsidian/Schema.md`.

> - Every wiki page MUST have at least one `[[Wiki/...]]` link to another wiki page
> - Hub pages MUST list ALL child pages in their namespace
> --- `templates/obsidian/Schema.md`

### Routes

#### RT-RTE-wiki-setup
Label: Wiki setup and skill installation

The principal is the user, supplying tool, namespaces, memory path and Git choices through the skill or interactive installer. The host runs the shared Bash/Python initializer; a caller may also invoke that non-interactive script directly. It validates required arguments/tool/namespace syntax before creating directories, renders templates, skips existing targets, writes config, optionally initializes Git and commits created paths. Direct script invocation requires caller-supplied flags, not an internal approval dialog. Tool/path/namespace/config fields are symbolic inputs; templates are text. SRC-1, `SKILL.md`, `setup.sh`, `scripts/init-wiki.sh`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Created/skipped file messages, config path, commit success or warning; skill adds next-step guidance.
- Later read-back: Generated config/schema and initial hubs/Dashboard/Access-Log are consumed by later commands; copied skill is consumed by later /wiki invocations.
- Delegated visibility: Host agent sees script output; script receives flags and templates, not an isolated model task.
- Selection predicate: User-selected tool/namespaces choose template directory and paths; existing targets are skipped.
- Invalidation or expiry: No automatic expiry; copied skill remains until replaced; plugin updating depends on host.
- Activation or effect: Implementation writes the skeleton/config and optionally command copy; no supplied run establishes successful host activation.
- Evidence limits: Source inspection only; no real vault, Git state or plugin loading observed.

Admission: user answers shape setup, the script admits syntactically valid namespaces and the supported tool. User can refuse directory/Git creation or copying. Installer offers existing-config overwrite and removes the old file before invoking the initializer. Recovery is rerun to fill missing paths, not a transaction or config backup. Optional Git commit failure is explicitly tolerated. No answer oracle or improvement experiment is used; operating mode is user-requested setup.

> if [ -f "$CONFIG_FILE" ]; then
>     echo -e "${YELLOW}llm-wiki.yml already exists. Overwrite? [y/n]${NC}"
>     read -p "" overwrite_config
>     if [ "$overwrite_config" = "y" ] || [ "$overwrite_config" = "Y" ]; then
>         rm "$CONFIG_FILE"
> --- `setup.sh`

>     if os.path.exists(path):
>         print(f"Skipped (already exists): {label}")
>         return
> --- `scripts/init-wiki.sh`

>         echo "Warning: git commit failed, files are left uncommitted." >&2
> --- `scripts/init-wiki.sh`

#### RT-RTE-source-ingest
Label: Source ingest and import admission

Ingest accepts a user URL/file/text; host agent fetches or reads it, extracts facts, classifies L1/L2 suitability, reads schema and target pages, writes page state/history and routing descriptions, performs a quality gate and reports. Import is a bulk alternate entry: inventory Markdown, classify namespaces, convert format/links/properties, create hubs then pages, run lint, report and commit. Import does not explicitly repeat ingest's routing-description maintenance, so its child-link instruction alone does not establish every imported page has a usable routing description. Lint is the prescribed verification/repair path. These are distinct input/transformation paths grouped by model-managed wiki admission, not asserted equivalent outputs. SRC-1, `SKILL.md`, both Schema templates.

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Page creation/update/cross-reference counts and warnings; import adds issue counts.
- Later read-back: Written wiki state and hub entries enter later query, lint and prune invocations; dated superseded wording remains in History.
- Delegated visibility: inapplicable — no separate worker is specified; foreground host agent sees source and selected target content.
- Selection predicate: Agent identifies entities, namespaces and existing targets using config/schema and Glob/Read; routing danger rule recommends L1 rather than wiki for quick rules.
- Invalidation or expiry: New facts can supersede current state; old wording is retained; dates/confidence feed later stale checks.
- Activation or effect: Prescribed wiki writes and structural commits; future use is afforded, not observed.
- Evidence limits: No source ingestion trace, measured correctness or credential-filter enforcement supplied.

Admission: model proposes and writes content under schema, cross-reference, no-credential and page-touch checks. Ingest and import requests are not specified as per-content human approval. User can steer inputs; no independent rejector or expected-answer oracle is supplied. Operating mode is open source processing, not a bounded experiment. Guidance consists of schema and skill rules; both updated pages and history persist. Git/history support manual recovery, but no automatic rollback on failed quality gate or multi-file write is specified. L1 recommendation is not evidence that this route actually writes L1.

> - A new fact that supersedes a stated state -> REWRITE the block's headline, properties and
>       "Next step" in place; move the superseded wording, dated, into the block's collapsed `History`
>       child (newest first). Never append "Status <date>: ..." sentences to running prose
> --- `SKILL.md`

> Phase 4 - Quality Gate:
>   - All new pages have required properties (per Schema)?
>   - All pages have at least 1 [[cross-reference]]?
>   - Every new/updated active page has a routing line in its hub `### Index`? (else it is unroutable)
>   - No credentials in wiki content?
>   - Count page touches (warn if < 5 or > 20)
> --- `SKILL.md`

#### RT-RTE-wiki-query
Label: Wiki query and optional write-back

User question -> namespace hubs -> model-ranked child pages -> full-page reads -> Access-Log append -> synthesis -> optional confirmed knowledge write-back. Agent owns selection/synthesis using natural-language descriptions/tags and retained pages; tool execution/persistence is host-owned. Default request is open-ended QA, not expected-answer testing. Model judgment is not an answer oracle. SRC-1, `SKILL.md`.

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Attributed answer, stale/low-confidence flags and related-page suggestions.
- Later read-back: Access entries feed later prune/status; confirmed write-back pages become later query material.
- Delegated visibility: inapplicable — no child model context is specified; the foreground agent receives hubs and selected full pages, optionally L1.
- Selection predicate: Match question to candidate namespaces and hub descriptions/tags; choose three relevant children, maximum five; unsuccessful routing invokes grep across wiki pages for top three to five.
- Invalidation or expiry: Dates/confidence qualify answers; archived pages remain greppable; log has no specified expiry.
- Activation or effect: Policy requests selected content to inform synthesis; append-only reads log use, not demonstrated behavioral activation or answer benefit.
- Evidence limits: No retrieval trace, actual context eviction, ranking evaluation or compliance measurement.

Admission: the model offers gap-filling/summary pages; user confirmation is required for that content write-back. Access-Log append is separately prescribed without per-query commit; archived re-hit prompts an offer to re-promote. Guidance is schema/skill plus selected page content. Retained outputs are pages, routing changes if accepted, and log records. Git/history afford recovery for content, not guaranteed rollback. The answer's citations and confidence labels are not independent truth checks.

> Phase 3 - Optional Write-Back:
>   - If query reveals a wiki gap -> offer to create/update pages
>   - If synthesis produces a useful summary -> offer to file as new page
>   - User must confirm before any writes
> --- `SKILL.md`

> - Append-only, NO per-query git commit (non-structural — see Constraints)
> --- `SKILL.md`

#### RT-RTE-index-prune
Label: Access-profile index demotion

User or external scheduler triggers prune; target does not self-schedule. Agent reads config and Access-Log, computes latest access (created date if never logged), compares N months, exempts hubs/Schema/Dashboard/Access-Log/active projects, lists candidates and awaits confirmation. Confirmed writes mark archived and move routing lines verbatim to hub Archive, then report and commit. SRC-1, `SKILL.md`.

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Demoted list, live-index sizes, hot-page contrast and next-due recommendation.
- Later read-back: Modified live/archive routing affects subsequent preferred query selection; archived files remain available through grep and links.
- Delegated visibility: inapplicable — scheduling is external and no worker delegation protocol is supplied.
- Selection predicate: No access for threshold months with exemptions; missing access uses creation proxy, not evidence of zero actual use.
- Invalidation or expiry: Threshold drives demotion, not data deletion; query can offer re-promotion.
- Activation or effect: Requested structural index mutation; no run demonstrates subsequent selection changing.
- Evidence limits: No actual log/profile or effectiveness comparison; confirmation and policy compliance unobserved.

Admission: model profiles/proposes, user confirms individual candidates and can reject; no expected-answer oracle. Mode is periodic/requested maintenance. Guidance is access threshold and exemptions; persisted routing/archive markers reshape future selection. Recovery is re-promotion and Git, not automatic rollback. This is a trace-fed selection update, not proof of improved retrieval capacity.

> - List candidates (page -- last access -- age in months) and SHOW the user before any write
>   - For each confirmed candidate:
> --- `SKILL.md`

#### RT-RTE-l1-verification
Label: L1 claim verification and revision admission

User triggers `prune --l1`; missing memory path aborts. Agent scans non-index L1 files, proposes claim classes, gathers local evidence for due behavior claims, issues per-claim verdicts and lets the user re-verify, correct, demote, delete or skip. Batch/window controls limit each run. L1 index references are maintained alongside corrected/removed rules. This account covers control/admission; detailed retained-memory semantics belong to the memory analysis. SRC-1, `SKILL.md`.

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Classification/re-verification/demotion/deletion/skip counts and remaining due work.
- Later read-back: Modified rule body/description/index can reach later host L1 loading; demoted history reaches later L2 retrieval. Actual loading is external/unobserved.
- Delegated visibility: inapplicable — no model worker is specified; user receives verdicts and carry-over summaries, never credential values.
- Selection predicate: Up to batch of unclassified files; then due true behavior claims, never-verified first and oldest verified next; index excluded as a rule but maintained as a reference consumer.
- Invalidation or expiry: Verification age sets due status, not automatic refusal to use a rule; skip stays due.
- Activation or effect: User-approved edits/deletions are requested; no source-supplied run shows revised rules steering later action.
- Evidence limits: Host loading, real L1 contents, actual evidence checks and later dependence uninspected; no action-time gate.

Admission: computation proposes classification/verdict/correction and gathers evidence; user confirms each write and can override/reject/skip. Evidence sources are local file existence/content, implementing source or read-only `--version`/`--help` commands, not a universal expected-answer oracle. Remote claims stay inconclusive; user knowledge can authorize re-verification. Operating mode is requested bounded batches of open rule checks, not an experimentally validated curriculum. Demotion must write wiki history successfully before deleting L1; credentials cannot be demoted. L1 lacks Git undo, so summaries/reference checks and confirmation are preventive recovery measures, not rollback.

> - READ-ONLY and LOCAL: check existence, read files, search contents, read dependency manifests, run
>     commands only with `--version` / `--help`. NEVER run commands with side effects, write, deploy, or
>     touch remote state. NEVER fetch remote content
> --- `SKILL.md`

> - The verdict is input for the user, not an action
> --- `SKILL.md`

> - **Re-verify:** set `verified: <today>`. On `contradicts`, offer it ONLY together with a corrected rule
>     text; write both together. Correct every place the claim appears: body, frontmatter `description`
>     (loaded via the index), and the rule's index line
> --- `SKILL.md`

Theory account: localized behavior claims can be criticized against named local evidence and revised rather than merely rescored. The guidance is the claim-class/verdict policy; persisted results are corrected rule text, verification metadata, references or L2 history, not model weights. Claim content and scope may vary; actual rule formulations were not supplied.

- theory-builder conditions 1–4: condition 1 design conclusion status: afforded — files can hold whole localized behavior claims; actual theories uninspected. Condition 2 design conclusion status: claimed — claim meaning determines checks and recommended action; operation uninspected. Condition 3 design conclusion status: claimed — per-claim support/contradiction and correction policy expose criticism of a rule, but no actual blame/revision episode supplied. Condition 4 design conclusion status: afforded — corrected retained rules and due metadata can shape later checks; actual iteration uninspected.
- Addressability: per-file classification and per-claim evidence are requested; finer assumptions/auxiliaries depend on uninspected user rules.
- Persistence: files/index/history can survive sessions; later host consumption uninspected.
- learning: improved future-action capacity is unestablished; no outcome or attribution evidence.
- Reflection: L1 rule content/metadata represents behavior-steering claims and the route can modify them; correspondence with actual operation and closed-loop causal use remain uninspected.
- Reflective theory builder: unestablished — no demonstrated criticism of llm-wiki's own method against its operation.
- Autonomous theory builder: not established for this route — user performs required admission decisions.

#### RT-RTE-health-maintenance
Label: Lint repair and status feedback

Agent scans pages/properties/link graph and schema rules; lint reports severity/counts, optionally fixes with `--fix`, commits repairs and updates Dashboard metrics/timestamp. Status instead performs lightweight no-modification lint, reads access hot/cold/matched reasons, Git activity and optional prior Dashboard, then returns metrics. Thus status is not a content writer while plain lint still prescribes Dashboard update. SRC-1, `SKILL.md`.

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Issue/fix report or status dashboard, health/activity/cache profile and recommendations.
- Later read-back: Dashboard metrics and repairs can be consumed by later commands; repaired routing descriptions change query inputs.
- Delegated visibility: inapplicable — no independent checker process or worker is specified; the foreground model performs scan and assessment.
- Selection predicate: All wiki pages for lint; rule-specific age/property/link/credential-pattern tests; status reads recent access/Git periods and counts.
- Invalidation or expiry: Stale high confidence can be downgraded; broken links and routing drift repaired; no automatic expiry of Dashboard.
- Activation or effect: Prescribed repairs and retained metrics, not demonstrated quality improvement or independent safety enforcement.
- Evidence limits: No evaluator executable or supplied lint run; credential regex patterns are requested, not concretely implemented in this source.

Admission: `--fix` is caller authorization for enumerated model repairs, not per-fix confirmation. Model diagnoses/proposes/decides repairs; caller can omit the flag. L1 is explicitly unwritable even with `--fix`; oversized blocks require judgment and are not auto-restructured. Answer oracle: none; schema/rule checks supply structural criteria rather than known-correct content answers. Operating mode is requested maintenance/status. Guidance is schema plus lint rules; repairs/Dashboard persist. Git affords manual recovery; no multi-file rollback is specified.

> - NEVER write to L1 files, not even with --fix (L1 Verification Due has no auto-fix)
>   - Git commit after fixes
> --- `SKILL.md`

### Claims

#### RT-CLM-cache-precision
Label: Cache precision objective

The source claims routing and demotion keep L2 precise as it grows. Implemented prompt structure affords bounded preferred retrieval and archive fallback, but no supplied trace or comparison establishes accuracy, latency, context savings or precision benefit. SRC-1, `SKILL.md`.

> **Two cache mechanisms keep L2 precise as it grows:**
> --- `SKILL.md`

### Evidenced absences

#### RT-ABS-action-gate
Label: No llm-wiki action-time freshness gate

- design conclusion status: absent

Searched boundary: complete `SKILL.md`, plugin manifests, `setup.sh`, `scripts/init-wiki.sh` at SRC-1 revision 11538c1195666db24e25e23cc64bb1d70587aef9. Inspection question: does shipped llm-wiki intercept an action justified by a due L1 rule? The explicit disclaimer quoted in Runtime account and the shipped entry paths support absence of a target-owned gate. This does not establish absence of unrelated host hooks or warnings in a deployed installation. Periodic lint/prune checks are not that gate. SRC-1, `SKILL.md`, `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `setup.sh`, `scripts/init-wiki.sh`.

### Behavioral-authority paths

#### RT-BAP-skill-dispatch
Label: Skill instructions to foreground maintainer

Consumer: Claude Code foreground agent. Channel: plugin skill loading or copied project command Markdown. Force: natural-language maintainer instructions, dependent on host loading and model interpretation, not a hard tool interceptor. Horizon: the invocation and later invocations while that plugin/copy remains installed. The same file can be persistently installed but supplies static procedure, not use-derived read-back. Paths/root config are interpreted before dispatch; copies can diverge from plugin releases. SRC-1, `SKILL.md`, `setup.sh`, `.claude-plugin/plugin.json`.

> Read `llm-wiki.yml` from the wiki root FIRST (every command except `setup`, which creates it).
> --- `SKILL.md`

#### RT-BAP-schema-guidance
Label: Retained Schema to page maintenance

Consumer: foreground ingest/lint maintainer. Channel: configured Wiki/Schema read from vault Markdown. Force: model-interpreted content/property/naming constraints, not a parser-enforced schema. Horizon: later maintenance commands while that retained schema is used. The initializer supplies initial conventions; runtime edits to this page are not an independently specified product self-modification procedure. SRC-1, `SKILL.md`, `scripts/init-wiki.sh`, `templates/logseq/Schema.md`, `templates/obsidian/Schema.md`.

> - Read Schema page for current conventions
> --- `SKILL.md`

## Annotations

none
