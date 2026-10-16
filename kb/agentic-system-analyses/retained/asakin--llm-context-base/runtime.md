---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Runtime baseline of llm-context-base's instruction-driven session, capture, query and maintenance paths at the frozen template revision."
run-id: AAS-2026-10-14-llm-context-base-f63a7c0fb5f2-01
reviewed-boundary: "6d01cba8e2c22f9ca2519c70073a05cd54378a8c"
---

# llm-context-base runtime report

## Runtime account

### Boundary and consequential work

llm-context-base prescribes work for an external file-capable assistant; it does not enclose model inference or tool execution. The shipped product is a knowledge-base template whose prompts ask the assistant to capture, file, retrieve and revise durable files. The boundary's source register supplies SRC-1 and the overall doc-grounded tier ([boundary](boundary.md#source-register)). This account inspects source text, not a supplied run: adherence, activation, recovery success and user benefit remain unobserved. The Python metadata converter provides a narrow executable maintenance path, not an internal agent runtime.

> **The repo stays dumb. The intelligence lives outside it.**
> --- `PHILOSOPHY.md`

SRC-1, `PHILOSOPHY.md`, distinguishes instruction/template extensions inside the substrate from separately deployed code extensions. No model, provider endpoint, embedding index, scheduler or remote worker is selected by the inspected loop. The external assistant is [RT-CMP-ai-assistant](#rt-cmp-ai-assistant); its weights and host behavior cannot be inferred from the files.

### Ordinary personal-instance invocation

Consider an already initialized personal instance receiving “capture this deployment process.” The principal is the user; the external host discovers its bootstrap and the foreground assistant owns subsequent steps. The generic bootstrap first checks for `_config/.framework-mode`. Without that flag, it requires configuration and general instructions before engaging the request. Configuration supplies profile, training history, conventions and phase; general instructions add personal context, phase-dependent philosophy/README loading, tool status and an inbox-age check. The assistant prints the session gate, then loads the write module and document standard because this request creates a file. These steps are prescribed natural-language decisions, not a code state machine ([RT-RTE-session-start](#rt-rte-session-start)).

The assistant drafts a dated inbox file with source attribution and draft metadata, offers filing, and follows the user's disposition. If filed, it checks source-preservation settings, selects a destination/template, updates relevant indexes/logs and uses completion criteria before an active/complete status. The physical executor is the host's filesystem tools; effects are local file creation, moves and edits, with Git persistence when committed. Terminal output is a capture/filing response plus the retained files, not a model-produced value returned by a repository API ([RT-RTE-capture-file](#rt-rte-capture-file)).

The human supplies the request and can reject filing or restructuring; this is not universal per-content approval. The same general module tells the assistant to write newly established rules immediately, including edits to its own instruction files ([RT-BAP-instruction-load](#rt-bap-instruction-load)). Later sessions reload these files. No lock, transaction, multi-writer arbitration or durable job-resume protocol is specified in the inspected session/write modules. Git provides an available history/revert recovery mechanism; uncommitted content and ignored files do not acquire that protection merely by being written (SRC-1, `docs/claude-code-setup.md`, `.gitignore`).

### Four forcing cases and control coverage

1. **Framework-mode and bootstrap variation:** the local flag bypasses personal initialization and prohibits personal-data retention; this refutes an unconditional “every invocation initializes a personal KB” claim. Claude's bootstrap also permits a first-message `/init` or setup-meta question before session start, unlike the generic bootstrap inspected here. Actual host discovery and flag deployment remain unobserved (SRC-1, `AGENTS.md`, `.claude/CLAUDE.md`).
2. **Inbox/review bypass:** explicit user destinations and append-only wiki-log writes are documented exceptions to inbox-first. General instructions also prescribe immediate edits to preferences and instructions, while the clipper supplies independently admitted inbox text in a legacy metadata shape. Therefore “human-reviewable before becoming operational” is a policy objective, not a universal approval invariant ([RT-CLM-review-policy](#rt-clm-review-policy)).
3. **Host permission boundary:** committed Claude settings recommend automatic edits and broad command families. The capability surface includes file access, shell, Git/GitHub and optional web/rendering tools; the actual grant set is host-dependent. Unlisted bash commands are documented as prompting, but broad Python execution can itself write files and launch other work. The same setup page allows a bypass-permissions mode. No repository-local policy monitor covers all those routes ([RT-CLM-host-permissions](#rt-clm-host-permissions)).
4. **Non-model rewrite:** the standalone converter writes matching Markdown files directly under the caller's current directory, without inbox admission or human review. It has neither a dry-run gate nor transactional rollback in its inspected implementation. A converter's output label is not evidence of valid YAML or semantic preservation ([RT-RTE-metadata-migrate](#rt-rte-metadata-migrate)).

These are static forcing cases, not executed tests. They cover prompt branches, independent ingestion, external tool control and direct software mutation. Provider-native tools, callbacks, subprocess behavior inside an actual host, hosted connectors and external automation remain uninspected external implementations; no security or isolation guarantee is attributed to them.

### Consumption and working context

Query selection proceeds from question type to a starting directory, directory README, summaries/tags, then 1–3 files. The assistant synthesizes an answer with file/date citations and freshness warnings. Cross-type queries repeat routing for several directories. Decision contexts proactively search past decisions with outcomes and surface failure constraints. This is relevance selection by a model following text, not a shipped vector-search implementation or answer oracle ([RT-RTE-knowledge-query](#rt-rte-knowledge-query)). A retained outcome is evidence offered to a decision-maker, not an independent correctness reference.

Startup phase loading and task-triggered module loading preferentially keep irrelevant static instruction bodies out of the window. Query selection limits loaded content; files longer than 500 lines may be reduced to their first major section. Full files remain on disk for possible later reads, so citations do not establish that every relevant detail reached the model. Neither plain text routing nor file paths are live memory pointers: the host must read content into its context again. There is no inspected separate-context worker/frame mechanism in these prescribed paths (SRC-1, `_config/config.md`, `_meta/instructions/general.md`, `_meta/instructions/knowledge-query.md`).

The Claude setup page supplies an optional compaction/reload recipe, not a tracked installed hook. The host compresses conversation; the recipe writes a `/tmp` sentinel after manual compaction, then the next user-prompt hook removes it and injects an instruction to rerun startup. It does not restore discarded turns verbatim, specify host summary contents or recover unsaved conversation discoveries. A second recipe logs Markdown read paths, not token counts or dependency correctness (SRC-1, `docs/claude-code-setup.md`). No observed deployment of either recipe is supplied.

### Admission and maintenance

Knowledge lint and definition-of-done are assistant procedures, not independent executable validators. Lint asks for seven checks and a report/log entry; completion asks for type-specific criteria before status/filing changes. The metadata standard says required fields are enforced, but the inspected lint's metadata check only asks whether `type:` exists in the first 20 lines of selected content roots. This cannot establish full metadata validity or universal coverage (SRC-1, `_config/standard.md`, `_meta/instructions/knowledge-lint.md`, `_meta/instructions/definition-of-done.md`).

Instruction optimization is a distinct approval-controlled path: inspect sizes/repeated reads, propose splitting/conditional loading/compaction, get user approval, edit, then retain review date and log. Its objective is lean session context, not an empirically established improvement ([RT-RTE-context-review](#rt-rte-context-review)). It differs from the immediate rule-capture path: the latter does not state the same explicit restructuring approval gate. Upstream code or instruction changes are also possible through ordinary engineering in framework mode; personal-to-framework contributions must be genericized and proposed by PR, not pushed directly to main (SRC-1, `AGENTS.md`, `_meta/instructions/general.md`). No target-owned deployment engine is implied.

All sources used here are SRC-1 at the frozen commit. No source register expansion or boundary change is required; the cited paths fall within the boundary's inspected coverage. Evidence layers are doctrine/design except the converter's bounded implementation and declarative configuration. No target command, example, hook or test was executed.

## Shared records

### Components

#### RT-CMP-ai-assistant
Label: External AI assistant

Source-native identity: the external AI layer called “AI assistant” in `_config/config.md` and “agentic tools” in `docs/supported-tools.md`. Representational form: distributed-parametric model processing, with natural-language instructions as input; storage substrate: external provider/host, not the repository. Parameters changing during operation: uninspected; exact model version pinned: no model version selected by these source files; mutable endpoint resolving to another model: uninspected because no endpoint is specified. Provider internals and actual host isolation are outside the frozen source. The files support substitutable consumers, not identical behavior across consumers (SRC-1, `docs/supported-tools.md`).

> This repo works with any LLM that can read files. Agent-specific bootstrap files are included:
> --- `docs/supported-tools.md`

### Operative objects

#### RT-OBJ-instruction-modules
Label: Instruction modules

Source-native identity: `_meta/instructions/*.md`, particularly general, write, query, lint and optimization modules. Form: natural-language policy interpreted by the assistant; embedded command examples do not become executable merely by being stored. Storage: Markdown on the local filesystem, versionable in Git. This record identifies operating guidance, not the personal facts, knowledge corpus or training log. It has no supplied peer-record counterpart: boundary is the only supplied member and declares no shared records. SRC-1, `_meta/instructions/general.md`:

> These modules define specific behaviors. Load them when triggered:
> --- `_meta/instructions/general.md`

### Routes

#### RT-RTE-session-start
Label: Session start and initialization

Endpoints: discovered tool bootstrap → config/general/context reads → initialization or ordinary startup → gate → user task. Owner/next-step decision-maker: foreground external assistant following natural-language branch and phase rules. State effects: first init asks four profile questions, writes config/personal README and requests a Git commit; ordinary sessions inspect existing state. Framework mode goes instead to engineering assistance; Claude setup questions have an additional bootstrap exception. No independent scheduler or delegated worker participates. SRC-1, `AGENTS.md`, `.claude/CLAUDE.md`, `_config/config.md`, `_meta/instructions/general.md`.

- Immediate return: Personal-session summary before ordinary request handling; init can first ask profile questions, while framework mode omits the gate.
- Later read-back: Profile, conventions and learned context are prescribed inputs to subsequent sessions; not every static startup file is accumulated memory.
- Delegated visibility: inapplicable — no delegated worker is specified; host context visibility is external.
- Selection predicate: Framework flag, init completeness, manually overridden phase or date calculation, and task-triggered module routing.
- Invalidation or expiry: Phase transitions reduce loaded files and proactive questions; source edits replace future loaded instructions. No token-cache invalidation rule is shipped.
- Activation or effect: Prescribes startup output and behavior changes by phase; successful adherence is unobserved.
- Evidence limits: Prompt branches, not an inspected host driver or execution trace; unset template dates do not demonstrate a completed init.
- design conclusion status: claimed
- operation conclusion status: uninspected

Admission: user supplies initial profile answers; assistant writes them and generates the personal README. User can decline answers or alter phase; no separate validation oracle is specified. Mode: open user requests with a date-bounded adaptation period, not a measured curriculum. Rollback is file editing or available Git history, not an automatic recovery step.

> - **Skip the Session Start Protocol entirely.** Do not run init. Do not print a session summary. Do not treat this as a personal knowledge base.
> --- `AGENTS.md`

#### RT-RTE-capture-file
Label: Capture and file admission

Endpoints: user content or existing inbox clip → assistant draft/extraction → inbox → optional final destination/source preservation → later query. Owner: assistant proposes content and routing; user is asked whether to file, can veto new directories, and supplies explicit destination exceptions. Host tools execute I/O. Metadata, templates, config and clip intent shape proposals. Completion checklists guide status changes; no answer oracle establishes factual truth. Mode: open capture, including raw “just park this” and intent-sensitive clip triage. SRC-1, `_meta/instructions/agent-write.md`, `_meta/instructions/general.md`, `_meta/instructions/definition-of-done.md`, `assets/clipper-template.json`.

- Immediate return: Capture acknowledgment and offer to file; idea throws can include a short take unless overridden.
- Later read-back: Filed knowledge, decisions, project content and optionally original sources remain available for later file consumers.
- Delegated visibility: inapplicable — no delegated agent handoff; external clipper writes inputs independently.
- Selection predicate: User intent, content type, target directory/template, source-preservation setting and model judgment of source importance.
- Invalidation or expiry: Filing may discard the inbox original when preservation is off; archived/superseded status changes later reliance, but no automatic expiry is specified.
- Activation or effect: Prescribed creation/move/edit and status/index/log updates; observed activation is not established.
- Evidence limits: Draft/inbox are advisory admission surfaces, not executable barriers. Clipper format differs from the canonical YAML shape.
- design conclusion status: claimed
- operation conclusion status: uninspected

Recovery: append preference, explicit restriction on deleting/overwriting existing files, and possible Git revert; preserving originals is optional, and uncommitted/ignored originals may lack Git recovery. Human review of every admitted sentence is not required by the selected exceptions.

> **Exceptions — agents MAY write directly to final locations:**
> - `WIKI-LOG.md` — append-only evolution log
> - Files the user explicitly says to create in a specific location
> --- `_meta/instructions/agent-write.md`

#### RT-RTE-knowledge-query
Label: Knowledge query and precedent delivery

Endpoints: user question or decision context → assistant routing/search → selected disk content → cited synthesis or missing-document offer. Owner: foreground assistant selects by type, domain tags, summary and status. Context: directory index, selected files and their update dates; no persistent index implementation is selected. Human decides whether to save a synthesis or create missing content; any resulting capture follows the write route. SRC-1, `_meta/instructions/knowledge-query.md`, `_config/standard.md`.

- Immediate return: Synthesized answer with paths/update dates, freshness warnings, or an explicit nothing-found response.
- Later read-back: Existing retained files are consumed; a saved synthesis may become future query input, with the general module requiring a log entry.
- Delegated visibility: inapplicable — no delegate or remote retrieval worker is specified.
- Selection predicate: Query classification, directory README, summary/tag match, 1–3 relevant files; archived files are usually deprioritized. Decision triggers select relevant records with filled outcomes.
- Invalidation or expiry: More than 30 days for time-sensitive content or 90 for references prompts a warning, not eviction. Source edits affect subsequent reads.
- Activation or effect: Requests synthesis and proactive precedent/failure-constraint use; actual decision dependence is unobserved.
- Evidence limits: Relevance and factual synthesis depend on model interpretation; older bold-field search wording coexists with YAML-first standard. No retrieval-quality result is supplied.
- design conclusion status: claimed
- operation conclusion status: uninspected

Decision roles: assistant surfaces past outcomes; user remains the decision principal, with no universal automatic successor-selection rule. Answer oracle: none specified; citations and past outcomes are evidence, not expected answers. Mode: open queries and decisions.

> Read the 1-3 most relevant files in full. For very large files (500+ lines), focus on the first major section.
> --- `_meta/instructions/knowledge-query.md`

#### RT-RTE-context-review
Label: Context optimization review

Endpoints: user request, lint recommendation or repeated/large reads → size analysis → recommendations → approved restructuring → revised instructions/date/log. Owner: assistant diagnoses and proposes; user approves and can reject restructuring; host tools apply changes. Guidance favors conditional loading, splitting and compaction only when useful. Mode: periodic/event-triggered maintenance, not an experimental comparison with expected answers. Answer oracle: none; line counts are indicators, not correctness references. SRC-1, `_meta/instructions/optimization-review.md`, `_meta/instructions/knowledge-lint.md`.

- Immediate return: Review report with sizes and recommendations, including no-change recommendation.
- Later read-back: Revised instruction text is loaded through startup/task routing; review date triggers future cadence and wiki log records the review.
- Delegated visibility: inapplicable — no separate reviewer or worker context is specified.
- Selection predicate: User optimization request, overdue 30-day marker, large instruction/core files, repeated reads or perceived slowness.
- Invalidation or expiry: Review becomes overdue after 30 days; removed/split instructions require altered loading rather than automatic cache eviction.
- Activation or effect: Prescribes approval before editing behavior-shaping text; subsequent successful activation is unobserved.
- Evidence limits: Static maintenance recipe; sizes do not demonstrate speed, correctness or improved capacity.
- design conclusion status: claimed
- operation conclusion status: uninspected

Rollback/recovery: no automatic rejected-change rollback or regression test is specified; user rejection prevents proposed restructuring and Git revert is externally available for committed edits.

> Always get user approval before restructuring instruction files.
> --- `_meta/instructions/optimization-review.md`

Theory account: the exposed guidance says growing, redundantly loaded instructions consume context; split or conditionally load material while avoiding needless optimization. Localized content is addressable by section/file, but arbitrary model reasoning is opaque. The proposal applies this guidance, and may replace instruction content; retained products are revised Markdown, a date and a review log, not model parameters. `theory-builder conditions 1–4`: condition 1 conclusion status: afforded — whole textual guidance units are inspectable/revisable; condition 2 conclusion status: claimed — the protocol requests decisions based on thresholds and usefulness; condition 3 conclusion status: uninspected — no source-supplied criticism episode establishes challenged claim, blame and resulting change; condition 4 conclusion status: claimed — cadence and retained edits permit later rounds, without observed criticism-fed iteration. Persistence horizon: intended across sessions. Learning: improved future capacity and causal benefit uninspected. Reflection: a prescribed loop measures its instruction organization and can change that organization, but exercised two-way dependence is unobserved. Reflective theory builder and autonomous theory builder: uninspected; no completed criticism cycle is supplied, and approval explicitly contributes human selection. Self-improvement boundary is the template's operating instructions, horizon later sessions, objective lean useful context; this supports only a claimed dispositional improvement-directed path. Evidence-shaped update, installation into later loading, and especially subsequent behavior depending on the change are not observed; successful self-improvement cannot be attributed.

#### RT-RTE-metadata-migrate
Label: Metadata migration utility

Endpoints: operator invokes Python in a directory → recursive Markdown scan → deterministic conversion/skip/error classification → direct file rewrite and printed counts. Owner and decision policy: operator chooses invocation/current directory; Python uses fixed regex and formatting rules. Form: symbolic program, regex and emitted YAML strings on filesystem. It skips dot directories, `.obsidian`, `.git`, `node_modules`, `_tools`; existing leading frontmatter is skipped. Matching metadata must follow an H1 after blanks; preceding material is not carried into rebuilt output. It is not a general Markdown/YAML parser. SRC-1, `migrate-to-yaml-frontmatter.py`.

- Immediate return: Printed converted/skipped/error counts and file names; exceptions are collected per file.
- Later read-back: Converted metadata and bodies become later assistant/Obsidian inputs; no model is called by this utility.
- Delegated visibility: inapplicable — local loop, no delegation implementation.
- Selection predicate: `*.md` under current directory excluding selected/hidden directories, then leading-frontmatter and H1/legacy-bullet checks.
- Invalidation or expiry: No expiry; reruns skip files now beginning with frontmatter. No semantic invalidation mechanism is specified.
- Activation or effect: Direct overwrite of converted files; static implementation establishes the write path, not successful execution.
- Evidence limits: No execution supplied; printed conversion is not YAML validation, atomicity or semantic equivalence. Exceptions do not undo earlier writes.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: caller initiates bulk mutation; code decides individual conversions without per-file approval or model/human content assessment. Oracle inapplicable to mechanical conversion: no expected-output comparator is implemented. Mode: fixed batch maintenance. Recovery: no backup, dry-run or transaction in this file; operator may use available Git history.

> filepath.write_text(new_content, encoding='utf-8')
> --- `migrate-to-yaml-frontmatter.py`

### Claims

#### RT-CLM-review-policy
Label: Human-reviewable admission policy

Claimed operation: agent writes should be auditable and human-reviewable before operational use. Owner: assistant following write instructions; enforcement point: natural-language inbox/draft rules and user interaction. Guarantee strength: policy. Covered path: ordinary new captures. Alternatives: explicit destinations, log writes, immediate instruction/preference updates, external clips and direct migration. Required external contract: host loads prompts, model obeys, human actually reviews. These sources establish an intended review opportunity, not mandatory review of all downstream behavioral content. SRC-1, `_meta/instructions/agent-write.md`, `_meta/instructions/general.md`, `migrate-to-yaml-frontmatter.py`.

> 3. Human-reviewable before becoming operational
> --- `_meta/instructions/agent-write.md`

- design conclusion status: claimed
- operation conclusion status: uninspected

#### RT-CLM-host-permissions
Label: Host permission policy

Claimed operation: Claude accept-edits removes file-edit prompts while unlisted bash commands still prompt. Owner/enforcement point: external Claude host; committed settings are recommendations/configuration input, not a deployed sandbox. Guarantee strength: policy. Covered path: host-mediated actions honoring that configuration; alternatives include allowed Python/Git command families, user-selected bypass mode, other agent hosts, clipper and manually invoked converter. Exact deployed grant set and isolation envelope remain uninspected. `.gitignore` affects ordinary Git inclusion, not model readability, filesystem access or public-output filtering. SRC-1, `.claude/settings.json`, `docs/claude-code-setup.md`, `.gitignore`.

> `acceptEdits` auto-approves file reads and edits, but **bash commands that aren't in the allow list still prompt**.
> --- `docs/claude-code-setup.md`

- design conclusion status: claimed
- deployment conclusion status: uninspected

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-instruction-load
Label: Retained instructions to later assistant behavior

Consumer: future foreground assistant. Channel: bootstrap → config/general → triggered module file reads. Force: requested operating policy, contingent on host delivery and model adherence; not code-enforced permission. Horizon: later tasks and sessions sharing the files. General instructions admit new behavior directly into operating guidance; optimization separately requires approval for restructuring. This is a live-by-design route from retained text to requested future behavior, not evidence that any revision changed a real run. SRC-1, `_meta/instructions/general.md`, `_config/config.md`, `AGENTS.md`.

> The rule: **when something new is established in conversation, update the relevant file immediately.**
> --- `_meta/instructions/general.md`

The routing table names `_meta/instructions/general.md` for new behavior/convention and the relevant module for new module behavior. This content is both editable output and later instruction input. The source does not make the draft status of ordinary knowledge a prerequisite for loading these instruction files.

## Annotations

none
