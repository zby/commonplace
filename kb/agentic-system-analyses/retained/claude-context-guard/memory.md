---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Claude Context Guard's model-maintained project ledgers, archive selection, lesson admission, code sidecars and incomplete compaction backups."
run-id: AAS-2026-10-13-claude-context-guard-357cd90664df-01
source-identity: https://github.com/atreiou/claude-context-guard
reviewed-boundary: efcd0a1815887483a862b32bfb3fbfd6aac79aa6
---

# Claude Context Guard memory report

## Boundary and evidence

The memory boundary includes first-run initialization, incremental maintenance, `/save`, `/end`, `/start`, `/lessons`, `/itemise`, `/audit`, installation and both hooks. It includes each generated-state format and its specified later consumer. Claude Code owns model execution and conversation compaction; Context Guard supplies instructions and filesystem backup code, not a conversation store implementation. The frozen source is SRC-1 at `efcd0a1815887483a862b32bfb3fbfd6aac79aa6`, registered in [boundary](boundary.md#source-register).

Direct reads covered the complete installer, settings, both hooks, all six command prompts and all eight templates. The supplied runtime establishes the broader invocation baseline; the findings below independently inspect its memory paths. Implementation evidence covers copying and event declarations; doctrine/design covers model-operated writing, selection and repair. No populated consumer history, host implementation, runtime trace or causal experiment is supplied. Comparison images remain excluded. There is no added source or change in functional scope.

| Entry point / operation | Direct source inspection, SRC-1 | Covering records and limits |
|---|---|---|
| Install / initialize | `install.sh`, `.claude/commands/start.md`, all `templates/` files named below | [RT-RTE-install-package](runtime.md#rt-rte-install-package), [RT-RTE-start-session](runtime.md#rt-rte-start-session); package copies are static, first-run files begin consumer state. Host discovery unobserved. |
| Incremental writes / checkpoint / clean end | `templates/CLAUDE.md`, `.claude/commands/save.md`, `.claude/commands/end.md` | [RT-RTE-save-session](runtime.md#rt-rte-save-session), [MEM-OBJ-resume-state](#mem-obj-resume-state), [MEM-OBJ-session-log](#mem-obj-session-log), [MEM-OBJ-task-registry](#mem-obj-task-registry), [MEM-OBJ-comments](#mem-obj-comments), [MEM-OBJ-decisions](#mem-obj-decisions), [MEM-OBJ-learned-behaviour](#mem-obj-learned-behaviour), [MEM-OBJ-feature-list](#mem-obj-feature-list); no completed write trace. |
| Rotate / supersede / resolve / defer | `.claude/commands/end.md`, `templates/DECISIONS.md`, `templates/LEARNED_BEHAVIOUR.md`, `templates/TASK_REGISTRY.md` | Same objects; bodies retained, access metadata changes. Category-specific comments conflict with age-based rotation. |
| Startup and demand reload | `.claude/commands/start.md`, `templates/CLAUDE.md` | [RT-RTE-start-session](runtime.md#rt-rte-start-session), [RT-BAP-project-rules](runtime.md#rt-bap-project-rules); archive relevance is model judgment, not a fixed retrieval algorithm. Custom files are declared consumer inputs whose contents are unavailable. |
| Harvest / reject / install / delete evidence | `.claude/commands/lessons.md` | [RT-RTE-harvest-lessons](runtime.md#rt-rte-harvest-lessons), [MEM-OBJ-learned-behaviour](#mem-obj-learned-behaviour), [MEM-OBJ-helpers](#mem-obj-helpers); no actual script series or caller supplied. |
| Itemise / refine / verify / restore | `.claude/commands/itemise.md`, `templates/CLAUDE.md` | [RT-RTE-itemise-code](runtime.md#rt-rte-itemise-code), [MEM-OBJ-section-markers](#mem-obj-section-markers), [MEM-OBJ-sidecar-index](#mem-obj-sidecar-index); host delegation and semantic preservation unobserved. |
| Plan retention / attribution | `.claude/commands/end.md`, `.claude/commands/audit.md`, `templates/CLAUDE.md` | [MEM-OBJ-plans](#mem-obj-plans), [RT-RTE-save-session](runtime.md#rt-rte-save-session); original host planning process opaque. |
| Audit / retain diagnoses / admit selected repairs | `.claude/commands/audit.md`, `templates/CLAUDE.md` | [RT-RTE-audit-project](runtime.md#rt-rte-audit-project), [MEM-OBJ-audits](#mem-obj-audits); latest-report loading requested by template, not explicit startup list. |
| Commit event | `.claude/hooks/pre-commit-check.sh`, `.claude/settings.json` | [RT-RTE-commit-reminder](runtime.md#rt-rte-commit-reminder); no retained result, validation or blocking gate. |
| PreCompact / backup | `.claude/hooks/pre-compact-save.sh`, `.claude/settings.json`, `install.sh` | [RT-RTE-compact-backup](runtime.md#rt-rte-compact-backup); five-file byte copies, no shipped restoration consumer. Host compaction content and reload remain uninspected. |

Installer dispatch lists precisely the six inspected prompts. Settings declare precisely the two inspected hooks. This package exposes no additional library/service memory API in that inspected dispatch surface. External helpers and custom files are afforded consumer-project extensions, not uninspected package entry points (SRC-1, `install.sh`, `.claude/settings.json`, `.claude/commands/lessons.md`, `templates/CLAUDE.md`).

## Core ideas

1. **The model curates separate records rather than replaying a transcript.** User comments are requested verbatim; session histories, resumable state, decisions, task metadata and tactical lessons are model-authored selections and transformations of conversation/work. The distinctions matter: feature verification has a human admission rule while ordinary logging does not. See the operative objects and [RT-RTE-save-session](runtime.md#rt-rte-save-session) (SRC-1, `.claude/commands/save.md`, `.claude/commands/end.md`).
2. **Rotation changes access, not necessarily authority.** Older decision/LB bodies remain intact behind one-line indexes. A later model reads the main file, judges whether an index line bears on work, then opens the entry. Neither an identifier nor preserved bytes proves successful discovery. Five sessions is an age policy, not a token ceiling; indexes, live backlog and custom files can grow. See [MEM-OBJ-decisions](#mem-obj-decisions), [MEM-OBJ-learned-behaviour](#mem-obj-learned-behaviour) and the startup annotation (SRC-1, `.claude/commands/start.md`, `.claude/commands/end.md`).
3. **Experience can become guidance or callable code, with distinct consumers.** `/lessons` requests script-diff interpretation, explicit human approval, LB/helper/decision installation and only then named deletion of spent scripts. LB reasons can reach a later model; helpers require future integration/calling. The prompt's assertion that every consecutive diff records a false belief is too strong: its own cosmetic-churn exclusion and instrument-fault class require interpretation. This is an afforded criticism path, not evidence of improved future capacity. See [RT-RTE-harvest-lessons](runtime.md#rt-rte-harvest-lessons) and its annotation (SRC-1, `.claude/commands/lessons.md`).
4. **Working-context reduction is selective loading, not implemented window management.** Main files/indexes and sidecar descriptions select later disk reads. Large-file itemisation requests a separate host worker receiving specified insertions; the foreground model already reads the full file. Host compaction is opaque, and its hook only copies disk files. Full bodies remain reachable on disk, but no window pointer/liveness rule or deterministic reload after compaction is implemented by this package. See [RT-RTE-itemise-code](runtime.md#rt-rte-itemise-code), [RT-RTE-compact-backup](runtime.md#rt-rte-compact-backup) and their annotations (SRC-1, `.claude/commands/itemise.md`, `.claude/hooks/pre-compact-save.sh`, `templates/CLAUDE.md`).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-resume-state
Label: RESUME_STATE current handoff

Source-native identity: consumer `RESUME_STATE.md`, initialized from `templates/RESUME_STATE.md`. Storage substrate: local Markdown, optionally Git. Representational form: natural-language handoff with textual session/time/clean-state fields interpreted by the model, not a package parser. Lineage: template → `/save` overwrites with current approach, state, next micro-step and user intent → `/end` replaces with clean marker. It is derived current-state memory, not raw conversation or history. Later `/start` reads it first and surfaces interrupted-state content verbatim; clean state redirects intent retrieval to SESSION_LOG. Admission is foreground-model selection, not approval of each detail; initiating `/save` does not certify completeness. Closest supplied record is [RT-RTE-save-session](runtime.md#rt-rte-save-session): this is its retained output, not a duplicate route or a part of installed CLAUDE instructions. Evidence: SRC-1, `templates/RESUME_STATE.md`, `.claude/commands/save.md`, `.claude/commands/end.md`, `.claude/commands/start.md`.

> - SESSION_LOG.md remains the historical record; RESUME_STATE.md is the current-state slice.
> --- `.claude/commands/save.md`

#### MEM-OBJ-session-log
Label: SESSION_LOG historical records

Source-native identity: consumer `SESSION_LOG.md` and `SESSION_LOG_pageN.md`. Storage substrate: Markdown filesystem and optional Git. Representational form: model-interpreted natural-language summaries, checkpoint markers, errors and next-step intent with session headings. Lineage: conversation/work review → selected historical account → old session bodies moved to pages. This is derived history, not a transcript. `/start` reads recent history, including clean-end intent; `/audit` checks the current entry; task-driven archive access remains possible. Reasons for significant failures are requested, not guaranteed complete. Last five sessions stay in main; no revocation follows solely from moving history. Distinct output of [RT-RTE-save-session](runtime.md#rt-rte-save-session). Evidence: SRC-1, `templates/SESSION_LOG.md`, `.claude/commands/save.md`, `.claude/commands/end.md`, `.claude/commands/start.md`, `.claude/commands/audit.md`.

> - **Errors encountered:** If any significant errors, blockers, or unexpected issues were hit during the session, log what happened and how it was resolved. Skip this if nothing notable occurred, and don't force empty sections. This prevents future sessions from repeating the same mistakes.
> --- `.claude/commands/end.md`

#### MEM-OBJ-task-registry
Label: TASK_REGISTRY task provenance

Source-native identity: consumer `TASK_REGISTRY.md` and numbered pages. Storage substrate: Markdown filesystem, optionally Git. Representational form: structured table whose task/status/notes/IDs receive meaning through model interpretation. It is not an executable scheduler. Lineage: created tasks and status changes → rows; completion adds files/approach/governing decisions; old done rows move to pages. Main reads guide pending work and duplication checks; audits compare plans and archives. Five-session rotation retains non-done rows unless explicitly consolidated or deferred to archives; genuinely actionable old rows move to Live backlog. Deferred archived work remains searchable but is not guaranteed startup-visible. Model classifies dispositions; no per-row human gate is specified. Distinct output of [RT-RTE-save-session](runtime.md#rt-rte-save-session). Evidence: SRC-1, `templates/TASK_REGISTRY.md`, `.claude/commands/save.md`, `.claude/commands/end.md`, `.claude/commands/start.md`, `.claude/commands/audit.md`.

>    Deleting the row, or letting it vanish in a trim, is a project failure. If you cannot classify a row, keep it and flag it in the Step 6 report.
> --- `.claude/commands/end.md`

#### MEM-OBJ-comments
Label: COMMENTS retained user speech

Source-native identity: consumer `COMMENTS.md` and `COMMENTS_pageN.md`. Storage substrate: local Markdown, optional Git. Representational form: natural-language quotations with timestamp/session metadata; this is requested raw user speech, unlike derived decisions and summaries. Foreground model selects/copies conversation comments, so rawness is an instruction rather than demonstrated fidelity. `/start` reads unactioned directives; model-maintained decisions/tasks/changes record their disposition. `/end` moves actioned comments and curiosity questions to pages, retaining unactioned directives in main. The template says actioned comments can be removed; `/end` specifies moving them, leaving a policy ambiguity rather than an implemented deletion procedure. Distinct output of [RT-RTE-save-session](runtime.md#rt-rte-save-session). Evidence: SRC-1, `templates/COMMENTS.md`, `templates/CLAUDE.md`, `.claude/commands/save.md`, `.claude/commands/end.md`, `.claude/commands/start.md`.

> 3. Keep all unactioned project directives in the main file.
> --- `.claude/commands/end.md`

#### MEM-OBJ-decisions
Label: DECISIONS constraints and reasons

Source-native identity: consumer `DECISIONS.md`, its archived-decision index and `DECISIONS_pageN.md`. Storage substrate: Markdown filesystem, optional Git. Representational form: natural-language Decision/Rationale/Source/Affects fields; ID/category/page fields are access and policy metadata interpreted by the model. Lineage: conversation/plan/session/requirement → model-authored decision → full-body archival plus index line. Later project agents receive constraints through `/start` and task-level Governed by pointers; update agents use supersession/category metadata. Rationale survives requested intact archival and can be read when an index line is relevant, but the one-line index does not itself deliver the rationale. Supersession marks the old entry and points to the replacement; physical archival does not revoke active constraints. Explicit approval is required to contradict decisions, distinct from routine model admission of new records. Closest [RT-OBJ-claude](runtime.md#rt-obj-claude) supplies the governing instructions, not this mutable register. Evidence: SRC-1, `templates/DECISIONS.md`, `.claude/commands/save.md`, `.claude/commands/end.md`, `.claude/commands/start.md`.

> 4. Mark `superseded` decisions as such (with a pointer to the D-number that replaced them) before archiving. They still archive, because a superseded decision explains why the current one exists.
> --- `.claude/commands/end.md`

#### MEM-OBJ-learned-behaviour
Label: LEARNED_BEHAVIOUR tactical lessons

Source-native identity: consumer `LEARNED_BEHAVIOUR.md`, archived-LB index and numbered pages. Storage substrate: local Markdown, optional Git. Representational form: natural-language Context/Gotcha/Workaround/Why/Related and optional Enforced by fields; page pointers and resolved labels are interpreted access metadata. Lineage: ordinary debugging/conversation review or approved script-diff harvest → localized lesson → intact archival plus compact index. Source input mixes agent actions, scripts, product behavior and user reports; a script alone does not prove its execution outcome. Ordinary save admission is model-led; `/lessons` additionally gates content on user approval. Later `/start` reads recent bodies and relevant indexed older bodies; `/lessons` compares existing lessons to avoid duplicates. Why is requested only if known. Resolved labels allow readers to skip a formerly relevant bug after platform removal/upgrade; the body remains findable. This is a distinct retained object, not another declaration of [RT-RTE-harvest-lessons](runtime.md#rt-rte-harvest-lessons). Evidence: SRC-1, `templates/LEARNED_BEHAVIOUR.md`, `.claude/commands/save.md`, `.claude/commands/lessons.md`, `.claude/commands/end.md`, `.claude/commands/start.md`.

> 3. An entry whose underlying platform or library has been removed, or upgraded past the bug, can be marked `resolved` in the index, so it stays findable but no longer needs reading.
> --- `.claude/commands/end.md`

#### MEM-OBJ-feature-list
Label: FEATURE_LIST human QA state

Source-native identity: consumer `FEATURE_LIST.json`, from `templates/FEATURE_LIST.json`. Storage substrate: JSON file, optionally Git. Representational form: localized QA fields and natural-language feature names/notes, interpreted by the agent; JSON syntax does not supply a fixed package evaluator. Lineage: human manual end-to-end verification → model sets passes true; reported failure → false plus failing-case notes. Model physically writes; human verification supplies positive admission. Later `/start` reads QA state; `/audit` cross-references task coverage, not correctness. This remains distinct from task completion and is excluded from rotation. No populated verification instance or deployed machine consumer is inspected. Distinct output of [RT-RTE-save-session](runtime.md#rt-rte-save-session), which supplies the load-bearing QA passage. Evidence: SRC-1, `templates/FEATURE_LIST.json`, `.claude/commands/save.md`, `.claude/commands/end.md`, `.claude/commands/start.md`, `.claude/commands/audit.md`.

#### MEM-OBJ-plans
Label: Archived project plans

Source-native identity: consumer `plans/S{session}-{seq}_{description}.md`, copied from host `~/.claude/plans/`. Storage substrate: local Markdown, optionally Git. Representational form: natural-language implementation plans; original host planning provenance is uninspected. Lineage: host-generated plan → model project-attribution by first roughly 500 characters/project name/path → copied archive; ambiguous and foreign plans skipped, agent-plan files excluded from this copy route. `/end` does not execute plans; pending tasks and precise next-step pointers link later work to bodies. `/audit` reads all archived plans and registry archives. Template startup also requests three full plans, conflicting with `/start` prohibition. Closest [RT-RTE-save-session](runtime.md#rt-rte-save-session) describes retention; plans are distinct output objects. Evidence: SRC-1, `.claude/commands/end.md`, `.claude/commands/start.md`, `.claude/commands/audit.md`, `templates/CLAUDE.md`.

> - Copy matched plans to `plans/S{session}-{seq}_{description}.md`
> --- `.claude/commands/end.md`

#### MEM-OBJ-audits
Label: Retained audit diagnoses

Source-native identity: consumer `audits/YYYY-MM-DD_HHMMSS.md`. Storage substrate: Markdown filesystem. Representational form: model-authored natural-language passing checks, severities, details and proposed repairs. Lineage: consistency/provenance/mtime/parity checks → displayed report → full saved copy. It is derived evaluation memory, not independently verified product truth. Latest report is a documented later consumer input under installed CLAUDE instructions; `/start` does not explicitly include it. User chooses repairs and may ignore findings; report retention itself is model admission without a per-report approval requirement. The report format does not require post-choice disposition updates, so later reading cannot be assumed to distinguish already-fixed from still-live diagnoses. Closest [RT-RTE-audit-project](runtime.md#rt-rte-audit-project) is its producer route, not a duplicate object. Evidence: SRC-1, `.claude/commands/audit.md`, `templates/CLAUDE.md`.

> This creates a persistent audit trail that survives context loss and can be read by external tools.
> --- `.claude/commands/audit.md`

#### MEM-OBJ-section-markers
Label: Source section address markers

Source-native identity: numbered start/end comments and same-file `[calls: N.M]` tags inserted into consumer code. Storage substrate: source files, optional Git. Representational form: address strings matched by grep/regex plus model-authored natural-language labels. Code readers locate ranges using markers; executable product code remains separate from navigation comments. Lineage: model reads code, identifies one-job units and inserts labels after human scope approval; re-itemisation may renumber. Ordinary maintenance adds/deletes labels and corresponding sidecar rows. Retained addresses guide later targeted reads and dependency advisories, not automatic execution of the comments. Distinct output of [RT-RTE-itemise-code](runtime.md#rt-rte-itemise-code), separate from sidecar descriptions because code-boundary selection and description validity have different checks. Evidence: SRC-1, `.claude/commands/itemise.md`, `templates/CLAUDE.md`.

> 3. Use `Read(file_path, offset=START_LINE, limit=END_LINE - START_LINE + 1)` to load just that section
> --- `templates/CLAUDE.md`

#### MEM-OBJ-sidecar-index
Label: Sidecar descriptions and dates

Source-native identity: consumer `<source_filename>.index.md`. Storage substrate: Markdown beside source, optionally Git. Representational form: model-interpreted natural-language descriptions plus marker IDs/dates used for parity and freshness comparisons. Description content is a derived code summary, not the source itself; dates/IDs are access metadata, not a correctness warrant. Lineage: model reads each numbered body → describes bodies under 50 lines, leaves larger descriptions blank → subsequent edits maintain row/date/job descriptions. Human-authored descriptions are preserved during regeneration; dead marker rows are deleted without tombstones, relying on Git history. Later coding agents read descriptions, choose IDs and load actual code; `/audit` uses dates only as a warning signal and asks before rewriting. Distinct from [MEM-OBJ-section-markers](#mem-obj-section-markers); closest supplied [RT-RTE-itemise-code](runtime.md#rt-rte-itemise-code) is the producing route. Evidence: SRC-1, `.claude/commands/itemise.md`, `.claude/commands/audit.md`, `templates/CLAUDE.md`.

> 3. **If the section is 50 lines or longer**, leave the description as `_(blank, fill on first edit)_`. This is a **deliberate token-saving choice**: long sections need careful summarisation, and an inaccurate auto-generated description is worse than no description (it misleads agents and corrupts their model of the codebase). Calibration scaffolding is not authoritative, so let the next coding agent fill it in when they touch the section for the first time.
> --- `.claude/commands/itemise.md`

#### MEM-OBJ-helpers
Label: Approved project lesson helpers

Source-native identity: functions exported from the consumer project's helper library. Storage substrate: project source files, optionally Git; none supplied populated. Representational form: executable symbolic code in an unspecified consumer language. Lineage: interpreted script-series change → approved helper proposal → installation/export and requested broken/good self-tests; LB points to the helper. Model authors and writes, human approves content. Later project callers are a documented external consumer role, not inspected call sites; exporting cannot prove future invocation. Helper prose rationale remains in LB Why/Enforced by if authored; the helper body need not itself retain criticism or test evidence. No auto-expiry/revocation mechanism specified by `/lessons`. Distinct output of [RT-RTE-harvest-lessons](runtime.md#rt-rte-harvest-lessons), whose passage supports the self-test requirement. Evidence: SRC-1, `.claude/commands/lessons.md`.

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-OBJ-claude](runtime.md#rt-obj-claude)

Memory lineage and control: first-run template copy plus user project details and Git-mode selection; custom-file declarations and toggles can subsequently change the retained instructions. It is not all use-derived memory: much remains static installed doctrine. The template says auto-read by host, but host delivery is unobserved; `/start` explicitly reads it. Custom file bodies are unavailable consumer inputs, so their trust, derivation and admission cannot be inferred. Credentials are discouraged here, while save/end request complete credential retention elsewhere; no encryption, redaction or secret-store implementation is supplied in these paths. Evidence: SRC-1, `.claude/commands/start.md`, `templates/CLAUDE.md`, `.claude/commands/save.md`, `.claude/commands/end.md`.

> **Security note:** Credentials and secrets should use your platform's secret manager. Plain-text credential files in git are an anti-pattern, so do not declare them here.
> --- `templates/CLAUDE.md`

#### On [RT-RTE-start-session](runtime.md#rt-rte-start-session)

Read-back is human-requested startup, followed by foreground-model file reads, not an unsolicited retrieval-service push. Selector inputs are project pointer/root discovery, clean marker, main ledgers, archive titles/categories/pages and custom-file declarations. Startup delivers recent bodies and compact indexes; task relevance selects older full bodies later. No fixed token budget, index bound or relevance completeness guarantee follows from the five-session window. The pointer is explicitly trusted rather than authenticated; source trust is project-policy trust, not provenance validation. Archived active constraints retain requested authority, but the model can miss a relevant short index line. Evidence: SRC-1, `.claude/commands/start.md`, `.claude/commands/end.md`; source passages also supplied by the runtime.

> **Custom context files:** After reading `CLAUDE.md`, scan its `## Custom Context Files` section. For every declared entry (lines matching `- path/to/file.md: purpose`), read the referenced file. Skip any that don't exist, and don't fail the startup. Skip anything the section marks read-on-demand.
> --- `.claude/commands/start.md`

#### On [RT-RTE-save-session](runtime.md#rt-rte-save-session)

Trace-fed chain: conversation/user reports/project work → foreground-model completeness review and content selection → the distinct objects above → later `/start`, audits and task reads. Verbatim COMMENTS preserves user input; SESSION_LOG, RESUME_STATE, DECISIONS and LB are derived slices. Incremental template triggers are model-operated, not independent software collection. Admission differs from physical I/O: ordinary logs/decisions/LBs are model-admitted, QA true requires human verification, and approved code commit attribution is another gate. Requested reasons survive in decision rationale, LB Why and significant-error history; the later model receives recent reasons in full and older reasons only after relevance selection. `/save` current handoff, `/end` clean marker plus historical intent and copied plans, and optional Git snapshots are alternate checkpoint forms; none is a transaction over all files. Evidence: SRC-1, `templates/CLAUDE.md`, `.claude/commands/save.md`, `.claude/commands/end.md`.

#### On [RT-RTE-harvest-lessons](runtime.md#rt-rte-harvest-lessons)

Curation separates raw scratch script versions from derived LB claims/helpers/decisions. Script diffs can suggest a challenged belief, but the command explicitly ignores cosmetic churn and permits an instrument-fault diagnosis. Input is not solely raw model trace: product observations, tests and human judgments can supply the lesson, and no actual series or outputs are available. Approval may reject proposed content before all writes/install/deletion. Once installed, named scripts may be removed, so minimum reasons must live in LB/decision fields; retaining every original criticism or self-test result is not required. Future LB and decision consumers are specified, whereas helper call sites remain uninspected. The runtime's separately qualified theory conditions, learning and autonomy conclusions remain appropriate; no evidence closes downstream activation or improvement. Evidence: SRC-1, `.claude/commands/lessons.md`.

> Look for a changed selector, wait condition, endpoint, parameter name, assertion, path, encoding, or a guard that suddenly appeared. Ignore cosmetic churn: renamed variables and reformatting are not lessons.
> --- `.claude/commands/lessons.md`

#### On [RT-RTE-itemise-code](runtime.md#rt-rte-itemise-code)

Later read-back chain is sidecar → model-selected marker number → grep start/end → range Read of actual code. This is targeted selection because descriptions and a requested task determine the code range, not merely because a number is present. Blank long-section descriptions limit that initial selector. Larger parent reads include children; missing short-block end markers fall back to a 20-line read. No fixed total budget is specified. Model admission writes descriptions; user scope approval is not row-by-row approval. Large-file worker delivery resembles selected inputs to a separate frame with completion returned, but foreground full-file reading is already required and host isolation/eviction is opaque. Backup source restore does not explicitly restore an already-written sidecar. Evidence: SRC-1, `.claude/commands/itemise.md`, `templates/CLAUDE.md`.

#### On [RT-RTE-audit-project](runtime.md#rt-rte-audit-project)

Audit retains derived diagnostics in [MEM-OBJ-audits](#mem-obj-audits). Index ID/page comparisons and marker parity check access structure, not the truth of decision/LB content or description meaning. Timestamp staleness triggers a suggestion, not automatic summary replacement. Model produces and persists diagnoses; human selection admits only chosen repairs. Ignored diagnoses are not new failures; their subsequent disposition need not be written into the saved report. Latest-audit loading is afforded by template, with startup-list conflict retained. Evidence: SRC-1, `.claude/commands/audit.md`, `templates/CLAUDE.md`.

#### On [RT-RTE-compact-backup](runtime.md#rt-rte-compact-backup)

Retained result: timestamped filesystem copies of current SESSION_LOG, TASK_REGISTRY, COMMENTS, DECISIONS and FEATURE_LIST bytes. This preserves each source representation unchanged, with directory timestamp as backup metadata. The shell decides fixed-list/existence admission, without model summarization or human per-copy approval. It neither reads raw conversation nor derives behavior-shaping memory. RESUME_STATE, LB, instructions, archives and plans are omitted. No shipped later backup consumer or automatic restore is specified. Host compaction's retained summary/tail, selection and later delivery remain uninspected; backup storage must not be mapped to a demonstrated post-compaction memory route. Evidence: SRC-1, `.claude/hooks/pre-compact-save.sh`, `.claude/settings.json`; the runtime supplies the fixed-list quote.

## Write side

The eight templates seed consumer files through `/start`; user project details and Git mode supply initialization choices. Subsequent ordinary admission uses the foreground model's interpretation of task changes, decisions, user messages and debugging events. Model authorship, tool writes and human approval are separate: `/save` is permission to checkpoint, not human certification of each resulting assertion. The feature tracker and `/lessons` have narrower explicit human content gates (SRC-1, `.claude/commands/start.md`, `.claude/commands/save.md`, `.claude/commands/lessons.md`; [RT-RTE-start-session](runtime.md#rt-rte-start-session), [RT-RTE-save-session](runtime.md#rt-rte-save-session)).

Rotation requests moving intact old bodies, generating indexes and explicit stale-task dispositions; it is maintenance of visibility rather than automatic belief validation. Decision supersession and LB resolution change requested reliance while retaining bodies. Comments move when actioned or merely exploratory. Sidecar rows can be deleted when source numbers disappear, with Git offered as history; this protection cannot be assumed in no-Git deployments. Human-chosen audit repairs can alter any implicated retained material, but audit does not silently rewrite descriptions. See [MEM-OBJ-decisions](#mem-obj-decisions), [MEM-OBJ-learned-behaviour](#mem-obj-learned-behaviour), [MEM-OBJ-task-registry](#mem-obj-task-registry), [MEM-OBJ-comments](#mem-obj-comments), [MEM-OBJ-sidecar-index](#mem-obj-sidecar-index) and [RT-RTE-audit-project](runtime.md#rt-rte-audit-project) (SRC-1, `.claude/commands/end.md`, `.claude/commands/itemise.md`, `.claude/commands/audit.md`).

The strongest trace-fed transformation is lesson harvesting: selected script series → criticism/classification → user admission → LB/helper/decision → possible later model/caller use. Reasons can survive in Why/Rationale, but raw scripts can be deliberately discarded after installation. Known-good/broken helper tests are requested; no outcomes are supplied. Ordinary checkpoint transformation also shapes later decisions, whereas the PreCompact byte-copy route performs no new learning transformation. No provider parameter change is established; model mutability remains [RT-CMP-claude-code](runtime.md#rt-cmp-claude-code)'s bounded uncertainty (SRC-1, `.claude/commands/lessons.md`, `.claude/commands/save.md`, `.claude/hooks/pre-compact-save.sh`).

## Read-back

- **Startup:** human `/start` requests model reads of current state and indexes; the later foreground model consumes them as project context and requested constraints. RESUME_STATE clean status selects interrupted handoff versus historical intent. Optional custom files add variable content, skipping missing/on-demand entries. [RT-RTE-start-session](runtime.md#rt-rte-start-session) and its annotation cover selection/delivery/limits (SRC-1, `.claude/commands/start.md`).
- **Task-demand archives and plans:** model compares an intended task with index descriptions, opens relevant full entries, and follows precise task/plan pointers. Active decisions remain policy constraints after archival. Superseded/resolved/deferred metadata changes reliance or access, not physical existence. [MEM-OBJ-decisions](#mem-obj-decisions), [MEM-OBJ-learned-behaviour](#mem-obj-learned-behaviour), [MEM-OBJ-plans](#mem-obj-plans) (SRC-1, `.claude/commands/start.md`, `.claude/commands/end.md`).
- **Code navigation:** future coding agent receives sidecar descriptions, selects a marker and reads a bounded source range. The descriptions supply selection guidance; actual code, not the summary label, supplies implementation content. [RT-RTE-itemise-code](runtime.md#rt-rte-itemise-code) and its annotation (SRC-1, `.claude/commands/itemise.md`, `templates/CLAUDE.md`).
- **Evaluation and deduplication:** `/audit` requests expanded reads of plans/archives/sidecars; `/lessons` reads existing lessons and helpers before proposals. These are update consumers, distinct from future product-work consumers. Latest saved audit is requested by template; external tools are an unspecified capability, not deployed wiring. [RT-RTE-audit-project](runtime.md#rt-rte-audit-project), [RT-RTE-harvest-lessons](runtime.md#rt-rte-harvest-lessons), [MEM-OBJ-audits](#mem-obj-audits) (SRC-1, `.claude/commands/audit.md`, `.claude/commands/lessons.md`, `templates/CLAUDE.md`).
- **Helpers:** a documented future code caller can consume installed exported helpers; no caller, actual invocation or behavioral benefit is supplied. **Backups:** only persistence is inspected, with no later restoration/delivery route. Neither storage capability is upgraded to observed activation. [MEM-OBJ-helpers](#mem-obj-helpers), [RT-RTE-compact-backup](runtime.md#rt-rte-compact-backup) (SRC-1, `.claude/commands/lessons.md`, `.claude/hooks/pre-compact-save.sh`).

The model-visible window holds file contents by value. Disk paths remain addresses for explicit future reads, not live references inside an implemented memory manager. Host sub-agent frames and compaction are described only as requested or opaque mechanisms; no inspection establishes their exact kept/removed material or frame reclamation policy (SRC-1, `.claude/commands/itemise.md`, `.claude/settings.json`; [RT-CMP-claude-code](runtime.md#rt-cmp-claude-code)).

## Integration issues

1. **No duplicate declaration identified.** New records are generated content objects, contrasted above with supplied producer routes and installed instruction objects. Route memory fields are annotations, not new route declarations. [MEM-OBJ-section-markers](#mem-obj-section-markers) and [MEM-OBJ-sidecar-index](#mem-obj-sidecar-index) are separate parts of the source-native paired artifact, not parts of a supplied object record.
2. **Scope correction to a strong source claim, not a supplied-runtime correction:** script differences do not necessarily establish a false belief. Cosmetic churn and instrument faults require interpretation. This supports the runtime's qualified theory account, not literal automatic falsification or demonstrated learning. [RT-RTE-harvest-lessons](runtime.md#rt-rte-harvest-lessons), [MEM-OBJ-learned-behaviour](#mem-obj-learned-behaviour) (SRC-1, `.claude/commands/lessons.md`).
3. **Unresolved instruction precedence:** plan/audit startup reads conflict between installed template and `/start`; old category-specific DECISIONS comments conflict with five-session rotation; actioned-comment removal language conflicts with `/end` archival. Prevented conclusions are deterministic startup budget, rotation schedule and raw-comment retention. Existing runtime notes cover the first two; this report adds the comment ambiguity. [RT-RTE-start-session](runtime.md#rt-rte-start-session), [MEM-OBJ-plans](#mem-obj-plans), [MEM-OBJ-audits](#mem-obj-audits), [MEM-OBJ-decisions](#mem-obj-decisions), [MEM-OBJ-comments](#mem-obj-comments) (SRC-1, `templates/CLAUDE.md`, `templates/DECISIONS.md`, `templates/COMMENTS.md`, `.claude/commands/start.md`, `.claude/commands/end.md`).
4. **Unresolved evaluation consistency:** audit flags an unclean resume with an existing session entry, although `/save` expressly creates/updates that combination. Retain possible false warnings rather than treating audit diagnoses as truth. [RT-RTE-audit-project](runtime.md#rt-rte-audit-project), [MEM-OBJ-resume-state](#mem-obj-resume-state), [MEM-OBJ-audits](#mem-obj-audits) (SRC-1, `.claude/commands/audit.md`, `.claude/commands/save.md`).
5. **Unresolved sidecar correspondence/rollback:** regeneration preserves descriptions by number while re-itemisation can renumber; parity alone cannot prove that preserved descriptions still describe the same bodies. Source restoration is specified after integrity failure, paired sidecar restoration is not. The runtime already limits rollback and semantic preservation; this report adds number-reuse risk. [RT-RTE-itemise-code](runtime.md#rt-rte-itemise-code), [MEM-OBJ-section-markers](#mem-obj-section-markers), [MEM-OBJ-sidecar-index](#mem-obj-sidecar-index) (SRC-1, `.claude/commands/itemise.md`).
6. **Unresolved deployment and trust:** existing settings can leave hooks unwired; prompt CCG_ROOT can differ from hook project root; trusted pointers and custom files do not authenticate content. Backup restore, helper calling, host compaction state, actual model compliance and later authority activation are uninspected. These prevent achieved recovery/completeness/benefit conclusions, not recognition of specified routes. [RT-RTE-install-package](runtime.md#rt-rte-install-package), [RT-RTE-start-session](runtime.md#rt-rte-start-session), [RT-RTE-compact-backup](runtime.md#rt-rte-compact-backup), [MEM-OBJ-helpers](#mem-obj-helpers) (SRC-1, `install.sh`, `.claude/settings.json`, `.claude/hooks/pre-compact-save.sh`, `.claude/commands/start.md`, `.claude/commands/lessons.md`).
7. **Unresolved sensitive-content retention:** template advises secret-manager use, but checkpoint/end instructions request full credentials in designated records and sometimes history. Consumer storage/security and policy precedence are uninspected; no safe secret-handling guarantee follows. [RT-OBJ-claude](runtime.md#rt-obj-claude), [MEM-OBJ-session-log](#mem-obj-session-log) (SRC-1, `templates/CLAUDE.md`, `.claude/commands/save.md`, `.claude/commands/end.md`).

## Limitations and checks

Frozen checkout HEAD was rechecked against the full supplied revision, with no working-tree changes reported. The report uses only SRC-1 and supplied boundary/runtime records; no prior analyses, live web, target execution, tests, installations or delegations were used. The invocation's memory member type and record contract govern identity, annotations and evidence layers. Deterministic validation is a form/quotation check, not proof of operation, activation, fidelity or benefit. Consumer deployment, conflict resolution, initialized contents and host/provider internals remain uninspected.

Validation: the invocation's `commonplace-run validate-output` command passed: "Member content check passes; invocation residue not checked. This is not job acceptance or claim support."
