---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Claude Context Guard's installation, session recovery, checkpoint, lesson, audit and hook routes at the frozen source revision."
run-id: AAS-2026-10-13-claude-context-guard-357cd90664df-01
reviewed-boundary: efcd0a1815887483a862b32bfb3fbfd6aac79aa6
---

# Claude Context Guard runtime report

## Runtime account

Claude Context Guard ships model-operated procedures, templates and two shell hooks. Claude Code owns invocation, model execution, tools, command discovery, compaction and delegation. Context Guard does not implement a model-call loop or an isolated executor. The claimed work is cross-session recovery through external project files, supplemented by checkpointing, rotation, audits and optional lesson harvesting and code navigation. Source inspection establishes executable shell paths and requested model behavior, not successful use or benefit (SRC-1, `README.md`, `.claude/settings.json`, `.claude/commands/start.md`, `templates/CLAUDE.md`). No execution evidence is supplied; operation and activation are uninspected throughout.

### Ordinary invocation and next-step ownership

1. A human invokes the Bash installer with a target directory. It resolves the directory, obtains consent if `.claude/` already exists, optionally installs commands/hooks in a detected parent, copies six command prompts, two hooks and eight templates, and conditionally copies settings. Its terminal output tells the human to open Claude Code and run `/start`. Existing command/template files can be overwritten; existing settings are not merged. [RT-RTE-install-package](#rt-rte-install-package) separates installation from event activation (SRC-1, `install.sh`).
2. The human invokes `/start` in Claude Code. The foreground model interprets the prompt, trusts a `CCG_LOCATION.md` pointer when present, otherwise locates a qualifying `CLAUDE.md`, and asks the human when several projects match. First run asks for project details and version-control mode, creates safeguard files from templates, offers itemisation and stops. A normal run reads the current files and archive indexes, checks Git, attributes and commits approved orphan work, computes the session number, summarizes and waits for human permission to work. Principal identities are the user and host agent; session/task/decision/LB identifiers live in files rather than a runtime identity service. [RT-RTE-start-session](#rt-rte-start-session) records the recovery and admission path (SRC-1, `.claude/commands/start.md`).
3. During ordinary project work, installed `CLAUDE.md` requests incremental file updates after status changes, decisions, message batches and before risky operations. These are foreground-model decisions, not shell timers or independent background writers. The next step remains with the host model, subject to human instructions. [RT-BAP-project-rules](#rt-bap-project-rules) describes the intended authority channel (SRC-1, `templates/CLAUDE.md`).
4. `/save` requests a current-state snapshot, historical updates, completeness checks and explicit-path commits/pushes according to version-control mode, then returns control to ongoing work. `/end` additionally rotates ledgers, archives attributable plans, wipes current in-flight state to a clean marker, commits/tags/pushes and returns a session summary. [RT-RTE-save-session](#rt-rte-save-session) describes these different terminal states. Local files and optional Git commits/remotes supply persistence; there is no inspected transaction spanning the multi-file updates and Git effects (SRC-1, `.claude/commands/save.md`, `.claude/commands/end.md`).
5. A later `/start` is the intended consumer of those writes. Archive bodies are loaded only when an index entry is relevant to the task. The model decides relevance; identifiers locate entries but do not themselves enforce relevance or compliance. Prompt-defined bounded loading does not establish a fixed token bound: the recent sessions, live backlog, custom files and growing archive indexes have variable size (SRC-1, `.claude/commands/start.md`, `.claude/commands/end.md`, `templates/CLAUDE.md`).

The capability surface in command frontmatter generally includes Read, Grep, Glob, Bash, Write and Edit; `/audit` omits Edit, yet its issue-resolution instructions request chosen fixes. `/lessons` requests `AskUserQuestion`, and `/itemise` requests an Agent tool for large files, neither listed in their allowed-tools headers. Actual tool grants, approval semantics and whether those requests work are uninspected host contracts. Bash can have filesystem/Git effects; no package-level isolation boundary, model-provider pin or permission broker is implemented in the inspected installer, settings, hooks and prompts. This is a bounded observation about this package, not a claim that Claude Code lacks such controls (SRC-1, `.claude/commands/audit.md`, `.claude/commands/lessons.md`, `.claude/commands/itemise.md`, `.claude/settings.json`).

### Alternate routes and forcing cases

Four source-level forcing cases qualify the protection claims; none was executed.

**Existing settings and parent launch.** The installer skips existing settings rather than inserting hook entries. Manual installation is another shipped path that depends on how copied settings coexist with consumer configuration. Even when hooks are installed in a parent, the shell hooks address `$CLAUDE_PROJECT_DIR`, while prompts can locate a different `CCG_ROOT` via a pointer or descendant search. The inspected source provides no synchronization between these roots. Commands may therefore select project files that hooks do not back up. The owning enforcement points are installer copy logic and host event wiring; installation alone does not establish hook coverage (SRC-1, `install.sh`, `README.md`, `.claude/settings.json`, `.claude/commands/start.md`, `.claude/hooks/pre-compact-save.sh`).

**Commit through an alternative channel.** The reminder matches a raw `git commit` substring in Bash hook input and always returns zero. It does not inspect ledger completeness. It may match incidental payload text, and a commit via another host tool, direct external shell, alias or differently spelled command need not match this route. Provider-native tools, extensions and remote workers are not implemented here; their host control paths remain uninspected. The package gives no commit-blocking invariant. See [RT-RTE-commit-reminder](#rt-rte-commit-reminder) (SRC-1, `.claude/settings.json`, `.claude/hooks/pre-commit-check.sh`).

**Compaction after incomplete maintenance.** The backup hook copies only five named files; it omits `CLAUDE.md`, `RESUME_STATE.md`, `LEARNED_BEHAVIOUR.md`, archive pages, plans and conversation state. Copying a stale ledger cannot capture unsaved conversation progress. Missing files are skipped; copy success is not checked before incrementing the count, and final exit is zero. No automatic restore or post-compaction delivery is implemented in that hook. Host compaction itself remains opaque. See [RT-RTE-compact-backup](#rt-rte-compact-backup) and [RT-CLM-progress-protection](#rt-clm-progress-protection) (SRC-1, `.claude/hooks/pre-compact-save.sh`, `templates/CLAUDE.md`, `README.md`).

**Conflicting loading and recovery instructions.** `/start` prohibits plan reading at startup, whereas the installed instruction template asks for the last three plans in full and the latest audit. The template says version-control mode `none` skips all Git steps, but `/start` Step 2 and `/audit` Git checks are unconditional in their local text; only `/start`'s recovery-commit step explicitly checks mode. The decision template also retains old category-specific archival comments alongside newer five-session rotation rules. Which conflicting prompt wins is a host/model interpretation question, not an inspected deterministic policy. These conflicts qualify cheap-startup, no-Git and archival guarantees without negating the existence of the intended routes (SRC-1, `.claude/commands/start.md`, `.claude/commands/audit.md`, `templates/CLAUDE.md`, `templates/DECISIONS.md`).

> 7. **`plans/`**: Archived plans from every session. Read the last 3 in full to cross-reference with TASK_REGISTRY.
> --- `templates/CLAUDE.md`

> **Do NOT read at session start:** archive `_page*.md` files wholesale, or any file in `plans/`. Note that archive pages exist; open a specific entry only when the work needs it, per the binding rule above.
> --- `.claude/commands/start.md`

### Guarantees, maintenance and change admission

| Load-bearing guarantee | Owner and enforcement point | Strength and covered paths | External contract and limits | Separate statuses |
|---|---|---|---|---|
| Startup waits for approval | Foreground agent interpreting `/start` Step 5 | policy; normal `/start` completion, not arbitrary host invocations | Host must deliver prompt; model must wait. It does not forbid recovery commits earlier in `/start`. | design conclusion status: claimed; operation conclusion status: uninspected |
| Retained task/rule discoverability through rotation | Model following `/end` rotation, indexes and `/audit` checks | protocol; model-maintained ledgers and audit, not direct edits or skipped maintenance | Writable files, accurate indexing and relevance selection required; no executable rotation/index validator shipped. | design conclusion status: claimed; operation conclusion status: uninspected |
| Commit checklist | Bash reminder and host PreToolUse event | best effort; literal substring on Bash path only | Settings must be active and host must present output. Always allows commit. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Pre-compaction backup | Hook copy loop and host PreCompact event | best effort; existing five listed files at host project root | Shell/utilities, writable destination, event execution and correct root required. Not a checkpoint of unsaved state. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Lessons precede script deletion | Model following approval/install/cleanup ordering | protocol; `/lessons` only, not direct deletion | User approval and correct classification/installation required. Untracked deleted scripts may be unrecoverable. | design conclusion status: claimed; operation conclusion status: uninspected |
| Itemisation preserves source | Model using Edit, backup, filtered diff, restore | protocol; confirmed `/itemise` files only | Host tools, Bash process substitution, regex/diff and faithful agent execution required. Comparison intentionally ignores numbered-comment and blank-line differences; it is not byte equality or semantic proof. | design conclusion status: claimed; operation conclusion status: uninspected |

SRC-1 supports this table at `.claude/commands/start.md`, `.claude/commands/end.md`, `.claude/commands/audit.md`, `.claude/commands/lessons.md`, `.claude/commands/itemise.md`, `.claude/hooks/pre-commit-check.sh`, `.claude/hooks/pre-compact-save.sh` and `.claude/settings.json`. The associated route records retain passages and decision fields.

Changes to consumer knowledge and instructions are admitted through ordinary model-led logging and explicit user approval for lesson proposals. Changes to product/helper code enter through `/lessons`; code labels and sidecars enter through `/itemise`; chosen audit repairs enter after human selection. The installer admits replacement package prompts/hooks/templates after coarse installation consent, not per-file content approval. There is no inspected package auto-update loop, runtime model-parameter update or production-deployment controller. Git preservation and explicit-path attribution are requested coordination practices, not locks; prompts recognize other agent lanes but do not implement scheduling or concurrency control. The large-file itemisation route delegates specific insertions to a host agent, retaining verification with the foreground agent. [RT-RTE-harvest-lessons](#rt-rte-harvest-lessons), [RT-RTE-itemise-code](#rt-rte-itemise-code) and [RT-RTE-audit-project](#rt-rte-audit-project) cover these admission mechanisms (SRC-1, `install.sh`, `.claude/commands/save.md`, `.claude/commands/end.md`, `.claude/commands/lessons.md`, `.claude/commands/itemise.md`, `.claude/commands/audit.md`).

Working-context control is primarily selective file loading: main ledgers/indexes now, relevant archive bodies and numbered code ranges later. This leaves full bodies reachable on disk rather than evicting or summarizing them in an implemented context manager. Host compaction removes/replaces conversation content by an uninspected policy; the hook merely duplicates disk state. Large-file delegation resembles a separate frame with selected insertions passed in and completion/diff results returned, but host frame contents, isolation and removal are uninspected. Durable files are not pointers with liveness rules inside the model window. [RT-CMP-claude-code](#rt-cmp-claude-code) distinguishes model opacity from inspectable instruction delivery (SRC-1, `.claude/commands/start.md`, `.claude/commands/itemise.md`, `templates/CLAUDE.md`, `.claude/settings.json`).

Coverage: this analyst read all six command prompts, both hooks, settings, installer, README, `.gitignore` and all eight templates at SRC-1's registered revision. These repeat boundary coverage rather than adding sources. Images remain excluded. Generated histories, scripts, helpers, sidecars and host/provider internals are unavailable evidence, not inspected deployments. Memory-specific revision assessment belongs to the memory analyst; this account establishes their callers and admission contracts.

## Shared records

### Components

#### RT-CMP-claude-code
Label: Claude Code host model

Source-native identity: Claude Code and its unspecified Claude model, required by the shipped command prompts. Representational form: distributed-parametric model; host tool dispatch is an external executable service, not part of those weights. Storage substrate: uninspected provider/host model storage. Exact model version is not pinned by this package. Parameter changes during operation are uninspected; endpoint mutability and possible model replacement are uninspected because no provider configuration or host implementation is supplied. The package contains no inspected parameter-update operation. Evidence: SRC-1, `README.md`, `.claude/commands/start.md`, `.claude/commands/itemise.md`.

> Open Claude Code in your project and type `/start`. On first run, it will:
> --- `README.md`

#### RT-CMP-ccg-commands
Label: Context Guard command prompts

Source-native identity: `.claude/commands/{start,save,end,audit,lessons,itemise}.md`. Representational form: natural-language operational instructions; YAML descriptions and allowed-tools declarations are a symbolic host-facing envelope whose enforcement is uninspected. Storage substrate: local Markdown files copied by `install.sh` into consumer `.claude/commands/`. These static shipped texts guide model choices; they are not themselves evidence of compliant execution. Evidence: SRC-1, `install.sh`, `.claude/commands/start.md`, `.claude/commands/save.md`, `.claude/commands/end.md`, `.claude/commands/audit.md`, `.claude/commands/lessons.md`, `.claude/commands/itemise.md`.

> You are starting or resuming a session. Follow these steps EXACTLY:
> --- `.claude/commands/start.md`

### Operative objects

#### RT-OBJ-claude
Label: Installed CLAUDE.md instructions

Source-native identity: consumer `CLAUDE.md`, initialized from `templates/CLAUDE.md`. Representational form: natural-language policies and file pointers interpreted by a host agent, including textual mode/toggle values. Storage substrate: project filesystem, optionally Git. It requests incremental logging, commits, read discipline, cross-session constraints and sidecar maintenance. Static template is inspected; populated consumer instructions and achieved authority are uninspected. Evidence: SRC-1, `templates/CLAUDE.md`, `.claude/commands/start.md`.

> Do NOT wait for /end. Treat safeguard files as a running log, updated incrementally. When saving, capture not just what was completed but what is **in flight**: the current approach, state, and next micro-step. If context is lost, this is the handoff note.
> --- `templates/CLAUDE.md`

#### RT-OBJ-settings
Label: Hook event settings

Source-native identity: `.claude/settings.json`. Representational form: symbolic JSON event/matcher/command rules consumed by Claude Code. Storage substrate: local consumer settings file; installer copies only when absent. Declares Bash PreToolUse and PreCompact command hooks with ten-second timeouts; actual host acceptance is uninspected. Evidence: SRC-1, `.claude/settings.json`, `install.sh`.

> echo "  Skipping settings.json (already exists)"
> --- `install.sh`

### Routes

#### RT-RTE-install-package
Label: Install package into consumer project

Endpoints/progression/owner: human → Bash `install.sh` → target commands/hooks/settings/templates → human `/start` instruction. Script owns copy sequencing; user chooses continuation and optional parent installation. Proposed changes are copied package files, with coarse human consent on an existing `.claude/` directory; no per-file veto after copying begins. Guidance is installer prompts. `set -e` halts failing operations but supplies no rollback of completed copies. Previous commands/hooks/templates may be overwritten; settings survive if already present. Manual folder copying is a documented alternate, without installer checks. Operating mode: bounded installation request. Answer oracle: inapplicable — no comparison against a reference result is performed. Evidence: SRC-1, `install.sh`, `README.md`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: installer completion banner or abort/error.
- Later read-back: inapplicable — copied shipped instructions are static material, not use-derived retained content; consumer files begin on `/start`.
- Delegated visibility: inapplicable — installer creates no agent delegation.
- Selection predicate: explicit target, nearest ancestor `.claude/` if found, user choice of parent installation, and absence of settings files.
- Invalidation or expiry: later copying can replace commands/hooks/templates; no automatic update or expiry is implemented here.
- Activation or effect: source-level file-copy effects; host discovery and execution remain unobserved.
- Evidence limits: no installation trace, host configuration acceptance or consumer environment supplied.

> # Copy settings.json only if it doesn't already exist
> --- `install.sh`

#### RT-RTE-start-session
Label: Recover and begin a session

Endpoints/progression/owner: human slash command → foreground model root discovery → first-run creation or current-ledger reads → Git checks/recovery → summary → wait. Context is current files, archive indexes, custom context declarations and Git history/status. Selection and summary are natural-language model judgments; filesystem/Git effects use host tools. First-run changes derive from shipped templates and human project details/mode. Recovery commits are proposed and attributed by the model using conversation history/registries; unapproved/unattributed files are left or surfaced. Human supplies project choice/details and grants work continuation; the prompt permits attributed recovery commits before that final go-ahead. Operating mode: open session recovery, not experiment. Answer oracle: project records supply provenance checks, not an expected correct model answer. Recovery from missing templates stops with a warning; no files found branches to setup. No modeled rollback of first-run writes or recovery Git failures. Evidence: SRC-1, `.claude/commands/start.md`, `templates/CLAUDE.md`.

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: setup report and stop, or contextual summary awaiting confirmation.
- Later read-back: reads prior `RESUME_STATE.md`, ledgers and indexes; later opens relevant archive entries and specific plan material on task demand.
- Delegated visibility: uninspected — host implicit context delivery to other agents is not specified by this route.
- Selection predicate: trusted pointer first; otherwise valid project instructions within bounded search, user resolves multiple matches; main files plus declared existing custom files, with archive relevance judged by model.
- Invalidation or expiry: clean/unclean snapshot marker selects handoff treatment; archive rotation changes location without revoking constraints; missing custom files are skipped.
- Activation or effect: requests incorporation into current work, summaries and approved orphan commits; actual behavior dependence is unobserved.
- Evidence limits: prompt policy, with conflicting plan-read and no-Git instructions in template/local commands; no consumer recovery trace.

> Do NOT start any work until the user confirms. Wait for their go-ahead.
> --- `.claude/commands/start.md`

#### RT-RTE-save-session
Label: Checkpoint and end-session persistence

Endpoints/progression/owner: human `/save` or `/end`, or template-driven incremental maintenance → foreground model completeness review → file writes → optional Git actions → report. Conversation events supply proposed content; model identifies decisions, gotchas, tasks and comment action status. Logging is model admission without item-by-item human approval; user manual QA is required for positive feature status. Approved product changes are staged by explicit paths; ambiguous changes require asking/leaving alone. Guidance includes fixed record formats, decision categories, five-session rotation and human intent capture. `/save` overwrites in-flight state with `Clean save: false`; `/end` wipes it clean and relies on historical Next step. `/end` archives plans and rotates; `/save` rotates only overgrown files. Git mode governs save/end commit/push steps; no cross-file transaction or automatic rollback is specified. Incremental commits, previous Git history and `/start` orphan recovery are intended recovery paths. Operating mode: open checkpoint/wrap-up. Answer oracle: human end-to-end verification for feature QA; other completeness checks use the model's conversation review, not an independent reference answer. Evidence: SRC-1, `.claude/commands/save.md`, `.claude/commands/end.md`, `templates/CLAUDE.md`, `templates/FEATURE_LIST.json`.

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: update-verification checklist plus checkpoint confirmation or exact session save-point report.
- Later read-back: written current state, history, decisions, learned behaviours, tasks, comments and QA status reach later `/start`; archive indexes lead to older full entries.
- Delegated visibility: uninspected — prompts recognize shared agent lanes but supply no enforced visibility or locking.
- Selection predicate: session changes, explicit decision/gotcha triggers, manual QA, last-five-session cutoff and per-file rotation rules; plan attribution by project names/paths.
- Invalidation or expiry: snapshot replaced on save and wiped on end; superseded decisions linked; resolved learned behaviours marked; old bodies moved rather than silently deleted.
- Activation or effect: requested file/Git durability and later guidance; exercised completeness and downstream influence are unobserved.
- Evidence limits: template/source instructions only; concurrent writes, Git conflicts, secrets handling and multi-step interruptions have no supplied execution evidence.

> - **Semantics:** FEATURE_LIST is a QA tracker, NOT a task-completion mirror. Only flip `passes: true` when the user has **manually verified** the feature works end-to-end. Task completion is tracked in TASK_REGISTRY. Do not confuse the two.
> --- `.claude/commands/save.md`

> **Stage explicit paths only. NEVER `git add -A` or `git add .`.** The working tree may be shared with other agents or with a paused lane of work, and a blanket stage sweeps their files into your commit. Name every path you stage.
> --- `.claude/commands/end.md`

#### RT-RTE-commit-reminder
Label: Bash commit reminder

Endpoints/progression/owner: Claude Code Bash PreToolUse event → shell reads raw input → literal substring branch → stderr checklist → exit zero. Code, not model judgment, selects the branch; the host/model owns any resulting file updates. It does not admit or reject commits. Guarantee owner: hook author for reminder logic, host for event dispatch. Guarantee strength: best effort. Covered path: settings-enabled Bash payloads containing `git commit`. Alternatives: other tools/external shells, indirect command spelling and inactive settings are not covered by this check. External contract: host event/output handling and shell availability. Evidence: SRC-1, `.claude/settings.json`, `.claude/hooks/pre-commit-check.sh`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: optional checklist on stderr and success status; commit is allowed.
- Later read-back: inapplicable — the hook writes no retained file or learned content.
- Delegated visibility: uninspected — whether host forwards reminder output to a delegated agent is not established.
- Selection predicate: raw hook payload contains literal `git commit` substring on Bash-matched event.
- Invalidation or expiry: inapplicable — per-event reminder has no retained lifetime.
- Activation or effect: wired advisory output, not ledger verification or a blocking gate; compliance unobserved.
- Evidence limits: no host event trace or successful checklist response supplied.

> echo "  (This is a reminder. The commit will proceed either way.)" >&2
> --- `.claude/hooks/pre-commit-check.sh`

> # Always allow, because this is a reminder and not a blocker
> exit 0
> --- `.claude/hooks/pre-commit-check.sh`

#### RT-RTE-compact-backup
Label: PreCompact file backup

Endpoints/progression/owner: host PreCompact → Bash timestamped directory creation → copy existing five named root files → stderr count → exit zero. Selection/admission is shell code; there is no human per-copy approval. This preserves current bytes, not revised knowledge or conversation summarization. Guarantee owner: hook copy loop and host event dispatch. Guarantee strength: best effort. Covered path: active PreCompact hook and existing files under `$CLAUDE_PROJECT_DIR`. Alternate project roots, omitted files, stale files and host compaction without active settings are outside that coverage. External contract: correct root/event, available utilities and writable filesystem. Recovery by restoring backups is not implemented in this script. Evidence: SRC-1, `.claude/hooks/pre-compact-save.sh`, `.claude/settings.json`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: stderr backup-count message and zero exit status.
- Later read-back: uninspected — backup copies persist on disk but shipped hook specifies no later consumer or automatic restoration.
- Delegated visibility: inapplicable — this script invokes no model or worker.
- Selection predicate: fixed list and file-existence test at host project root.
- Invalidation or expiry: no retention pruning specified; timestamp resolution is seconds, not a unique transaction identity.
- Activation or effect: executable copy affordance; no conversation checkpoint, model update or restoration evidence.
- Evidence limits: mkdir/copy failures are not checked, count advances after attempted copy, final success is unconditional; host execution and backup validity unobserved.

> FILES=(SESSION_LOG.md TASK_REGISTRY.md COMMENTS.md DECISIONS.md FEATURE_LIST.json)
> --- `.claude/hooks/pre-compact-save.sh`

#### RT-RTE-harvest-lessons
Label: Harvest session scripts into lessons and helpers

Endpoints/progression/owner: human `/lessons` → model finds this session's scripts, reads existing knowledge/helper library, diffs series, classifies lessons → human proposal approval → model installs approved LB/helper/decision → named cleanup → report. Candidate criticism is foreground-model interpretation of changed scripts, not an executable inference that every diff encodes falsification. Human can reject before any write/install/delete; model determines proposals and physical edits. Operating mode: open session evidence harvest, with bounded helper self-tests. Answer oracle: proposed helper's known-broken and known-good cases; inputs/outcomes supplied by agent/project evidence, not a frozen external oracle. Guidance prefers executable helpers where they prevent wrong answers, separates instrument faults and rejects cosmetic churn/duplicates. Rollback: Git only where committed; untracked deletion may be permanent, so untracked/unmined scripts stay and referenced scripts are retained. Evidence: SRC-1, `.claude/commands/lessons.md`.

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: lesson destinations and proof summaries, counts of removed/kept scripts, or nothing-new result.
- Later read-back: approved learned behaviours reach later `/start`; helper code affects future callers only if integrated and called; decision constraints reach later project work.
- Delegated visibility: inapplicable — this prompt describes a foreground harvest, no delegated mining route.
- Selection predicate: current-session prefix or modification time since first commit; consecutive series diffs; deduplicate against main/indexed knowledge and helper library.
- Invalidation or expiry: explicit approval and installation precede named deletion; resolved LB handling belongs to later rotation; no automatic helper expiry.
- Activation or effect: requested knowledge/helper installation and evidence cleanup; exercised installation, helper use and improved performance unobserved.
- Evidence limits: no populated script series, user response, installed helper or self-test result supplied; AskUserQuestion availability is a host uncertainty.

> **Do not write, install, or delete anything before the user answers.**
> --- `.claude/commands/lessons.md`

> - **Helpers**: add to the project's helper library, export it, and **self-test both ways**: prove it fails on a known-broken input and passes on a known-good one. A helper that has only ever been tested on the good case is a guess wearing a function signature.
> --- `.claude/commands/lessons.md`

Theory account: proposed beliefs concern selectors, waits, endpoints, parameters, assertions or guards. The prompt asks what a previous script believed and what later evidence challenged; classifying instrument faults explicitly permits blaming the check rather than the product. Guidance is applied, not automatically revised: the harvest method itself is static. What persists is an approved LB with context/gotcha/workaround/why, helper code and sometimes decision rationale; scripts can then be discarded. No actual formulated candidate or criticism is supplied.

Theory-builder conditions 1–4:
- condition 1 conclusion status: afforded

LB formats and helper replacements can localize whole claims, but no populated instance is inspected.

- condition 2 conclusion status: claimed

`/start` guidance and future helper calls are intended content-dependent consumers; no actual consumption is observed.

- condition 3 conclusion status: claimed

Script-diff interpretation requests explicit challenged belief and separates instrument fault; no executed criticism/revision is supplied.

- condition 4 conclusion status: claimed

Installation is intended to shape later sessions, not an observed criticism-fed second round.

Addressability: named LB fields and localized helpers permit individual inspection/replacement; assumptions and scope are only as explicit as future authored content. Persistence: intended across project sessions through disk and later `/start`/helper consumers; attained use horizon is unobserved. learning: uninspected — no evidence of improved future action or attribution. Reflection: afforded for a consumer agent's recorded debugging beliefs and future guidance, but both causal directions in actual use are unobserved; no demonstrated reflective theory builder of this package's own method. Autonomous theory builder: this route's admission requires human content approval, so computational autonomy of all internal operations is not established. Self-improvement: only a dispositional candidate path for consumer-agent guidance/helper organization, not exercised self-improvement of Context Guard. Evidence may shape proposals (link 1), approved artifacts may change organization (link 2), and future `/start` or helper calls may provide authority (link 3); all remain requested, and subsequent behavior causally depending on that change (link 4) is unestablished. Successful improvement is separately uninspected.

#### RT-RTE-itemise-code
Label: Itemise code and maintain sidecar parity

Endpoints/progression/owner: human `/itemise` → model toggle/scope checks → confirmed file list → backups → Edit-only labels → sidecar creation/update → parity and filtered diff checks → restore failed sources or delete backups → summary. Human approves scope; `force` skips the existing-number warning, not initial scope confirmation. Model proposes numbered units/descriptions; files over 500 lines request host sub-agent insertions with foreground verification, while files under 500 lines use direct editing. The “500+ lines” heading conflicts with those strict inequalities at exactly 500 lines, so the procedure does not unambiguously determine that boundary case. Symbolic marker/number sets and filtered diffs check selected aspects; granularity and descriptions require model judgment. Operating mode: bounded labelling request. Answer oracle: backup source normalized by marker filtering, CRLF and blank-line treatment; marker and sidecar number sets provide parity reference. Proposed changes are labels, index rows and dates; guide says no semantic refactor. Failure restores source from backup; sidecar rollback is not explicitly paired with source restoration. Evidence: SRC-1, `.claude/commands/itemise.md`, `templates/CLAUDE.md`.

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: per-file updated/failed/restored report, counts and navigation advice.
- Later read-back: future coding agents read sidecar descriptions, select section numbers, grep boundaries and load targeted code; static command text alone is not read-back.
- Delegated visibility: large-file worker is requested to receive file and explicit insertion list, use Edit only and return completion; actual worker context and isolation uninspected.
- Selection predicate: enabled/absent toggle, human-confirmed files/exclusions, logical one-job blocks; auto-describe under-50-line units, leave longer descriptions blank; preserve existing descriptions.
- Invalidation or expiry: added/deleted section rows change with markers; dates update on edit; re-itemisation renumbers and may need fresh references; backup deletion ends immediate rollback access.
- Activation or effect: intended navigation and bounded loading plus source/sidecar file edits; exercised token savings and semantic preservation unobserved.
- Evidence limits: verification commands are prompt instructions, not shipped automatic checker execution; filter ignores selected comments/blank lines, host Agent availability and sidecar rollback are unresolved.

> Files over 500 lines MUST be delegated to a sub-agent. Direct editing of large files is error-prone when there are 30+ insertion points. Session 1 confirmed this when `config.py` was corrupted by a mismatched edit boundary.
> --- `.claude/commands/itemise.md`

> ### Large File Handling (500+ lines)
> --- `.claude/commands/itemise.md`

> For files under 500 lines, proceed with direct editing as described above.
> --- `.claude/commands/itemise.md`

> - If `diff` produces output: **FAIL**, actual code was changed
> --- `.claude/commands/itemise.md`

#### RT-RTE-audit-project
Label: Audit project and admit chosen repairs

Endpoints/progression/owner: human `/audit` → model executes listed checks over Git, tasks, comments, decisions, plans, archives, resumes and sidecars → independently listed severities/fixes → saved report → human choice → chosen fixes only. Model proposes diagnoses and repairs, human can veto/ignore; ignored issues are not logged as failures. Operating mode: open project-integrity diagnosis, not curriculum. Answer oracle: registries/plans/archive IDs and marker parity are internal consistency references; manual feature QA is separate, not replaced by audit. Guidance mandates task provenance, intact archive pointers and conservative stale-description warnings; audit reports persist. Recovery/rollback of selected repairs is not specified beyond ordinary project mechanisms. Evidence: SRC-1, `.claude/commands/audit.md`.

- design conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: passing checks and every issue with severity/details/fix, then chosen repairs after user response.
- Later read-back: report saved to `audits/YYYY-MM-DD_HHMMSS.md`; template requests reading latest audit, while `/start`'s explicit read list does not include audits by default.
- Delegated visibility: inapplicable — no audit-worker delegation is specified.
- Selection predicate: all project plans and relevant registry archives, all discovered sidecars, project-attributed global plans; ambiguous foreign plans skipped.
- Invalidation or expiry: stale dates yield suggestions, not automatic semantic rewrites; no report expiry is specified.
- Activation or effect: requested diagnosis, persistent report and human-selected corrections; actual detection accuracy and correction effect unobserved.
- Evidence limits: no audit execution or consumer files supplied; audit's resume-state warning can flag a saved mid-session entry because `/save` also creates/updates a session entry; Git checks conflict with template's no-Git mode; tool grant enforcement uninspected.

> **Do NOT auto-rewrite.** This step is a suggestion only. Surface the row to the user and let them decide:
> --- `.claude/commands/audit.md`

> 3. After the user responds, fix ONLY the issues they chose to fix
> --- `.claude/commands/audit.md`

### Claims

#### RT-CLM-progress-protection
Label: Progress protection before compaction

Claimed operation: automatic pre-compaction saving prevents data loss and makes compaction a non-event. Source: SRC-1, `README.md`, `templates/CLAUDE.md`. Design conclusion status: claimed. Implementation conclusion status: wired for the narrower five-file backup in [RT-RTE-compact-backup](#rt-rte-compact-backup), not for complete progress capture. Operation conclusion status: uninspected. Benefit conclusion status: uninspected. The backup cannot preserve unsaved conversation information or omitted resume/LB files. This corrects guarantee scope, not the existence of backup behavior.

> | Pre-compaction hook | Automatically saves all progress before context compression, so no data loss |
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-project-rules
Label: Installed project rules guide later host work

Consumer: Claude Code foreground agent. Channel: installed `CLAUDE.md` plus command-driven file reads. Force: requested mandatory policy interpreted by model/host, not shell-enforced invariants. Horizon: later project sessions and current session maintenance. Static template delivery is claimed; use-derived instructions/constraints can reach later sessions through `/start`, but activation is unobserved. The update consumer is the model maintaining files; the downstream work consumer may be a later model invocation. Evidence: SRC-1, `templates/CLAUDE.md`, `.claude/commands/start.md`, `.claude/commands/save.md`.

> # This file is auto-read by Claude Code at every session start.
> --- `templates/CLAUDE.md`

> 3. **`DECISIONS.md`**: Every architectural decision made. NEVER contradict these without explicit approval. Each entry has a `Category:` field (forever-active, active-constraint, feature-specific, superseded).
> --- `templates/CLAUDE.md`

## Annotations

none
