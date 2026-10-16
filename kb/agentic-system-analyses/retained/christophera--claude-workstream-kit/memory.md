---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Claude Workstream Kit memory: Git-backed work records, selective reload, extraction, condensation, rotation and handoff admission."
run-id: AAS-2026-10-15-claude-workstream-kit-103204afa1ab-01
source-identity: https://github.com/ChristopherA/claude-workstream-kit
reviewed-boundary: "15705c38a4fffb206b868b3e6bc5ffb4fd8b9d64"
---

# Claude Workstream Kit memory report

## Boundary and evidence

The memory boundary includes the kit's installed state producers and consumers, not only its rewrite API: creation, work, capture, review, extraction, closure, handoff, status, installation, hook injection, telemetry and evaluation retention. The source is SRC-1 at the revision above, as registered in [boundary](boundary.md#source-register). Repository files hold cross-session work memory; native Tasks, plan mode, account memory and host compaction remain external. Their existence is acknowledged, but their storage, selection, initialization and actual loading are not inspected. This prevents conclusions about complete host memory or exact context reconstruction after clear/compact. SRC-1, `docs/design.md`, `.claude/rules/workstreams-rule.md`.

Direct inspection adds the full create/work/capture/review/extract/close/status/handoff skills, workstreams rule, both SessionStart ranges, settings, status-line script, forwarding shim, seed PROJECT.md, evaluator and selected shared-parser/rewrite/record/installer ranges. Frozen HEAD and clean source status were checked. The runtime baseline supplies installation, Stop, delegation and model-boundary findings where not independently traced here. Implementation evidence supports deterministic selection and rewriting; skill text supports requested model behavior. Comments about earlier failures are attributed reported operation, not observed episodes in this run. No target code or tests were executed.

| Entry point or operation | Source scope and reading basis | Coverage and limit |
|---|---|---|
| Install/upgrade, seed and instruction admission | Direct `install.sh` seed/status-line/stamp range; supplied upgrade baseline | [RT-RTE-install-upgrade](runtime.md#rt-rte-install-upgrade); no consumer installation inspected; initial project-list choice belongs to user |
| Creation and routine capture/work | Direct three skills and rule | [RT-RTE-state-lifecycle](runtime.md#rt-rte-state-lifecycle), [RT-RTE-work-goal](runtime.md#rt-rte-work-goal), annotations below; session traces are selected by model, not exhaustively copied |
| Review, supersession, extraction, notes disposition | Direct review/extract/close/rule | [RT-RTE-state-lifecycle](runtime.md#rt-rte-state-lifecycle), [MEM-OBJ-notes](#mem-obj-notes), [MEM-BAP-artifact-adoption](#mem-bap-artifact-adoption); semantic admission is model/user policy |
| Records/Decisions condensation and legacy CLI | Direct rewrite `finish`, records, Decisions, dispatch and shim; split-record internals not fully read | [RT-RTE-rewrite-state](runtime.md#rt-rte-rewrite-state), [RT-CLM-rewrite-preservation](runtime.md#rt-clm-rewrite-preservation); exact handling of every completion-note shape not established |
| Learning condensation and rotation | Direct `condense_learning`, `learning_loss`, `condense_learnings`, `rotate`, `sweep_removed`, `stale_claims`, `cmd_rotate`; shared disposition/fingerprint | [MEM-RTE-learning-condense](#mem-rte-learning-condense), [MEM-RTE-state-rotate](#mem-rte-state-rotate), [MEM-CLM-marker-reopening](#mem-clm-marker-reopening); checks do not establish semantic preservation |
| Automatic SessionStart delivery | Direct settings and entire hook | [RT-RTE-session-reload](runtime.md#rt-rte-session-reload); pointer is printed, full workstream is not; no fixed total-output token budget |
| Detailed work/status/history read | Direct work/status/close skills, seed PROJECT.md; supplied runtime | [MEM-OBJ-project](#mem-obj-project), [MEM-OBJ-archive](#mem-obj-archive), [RT-BAP-resume-state](runtime.md#rt-bap-resume-state); external project truth is not verified by status |
| Handoff filing, receiving, decline/deletion | Direct handoff and rule | [MEM-OBJ-handoffs](#mem-obj-handoffs), lifecycle annotation; destination confirmation is not receiver acceptance |
| `record`, `cites`, `refs`, `paths`, `decay`, `git`, `fires`, `bare-ids`, `self-check`; shared library | Direct CLI dispatch, Learning scoring, shared file enumeration; targeted source searches; supplied runtime | Read-only record/diagnostic capabilities, not additional durable-memory writes. Full per-command parsing not audited; cannot assert exhaustive detection of stale state |
| Telemetry writer and `--context` reader | Direct entire status-line script and installer registration | [MEM-OBJ-context](#mem-obj-context); automatically derived access metadata, not a learned work summary; installation preserves existing status line |
| Stop hook, agents and evaluator | Supplied Stop/agent findings; direct full evaluator; direct targeted damage-test assertions and searches of acceptance drivers | [RT-RTE-stop-gloss](runtime.md#rt-rte-stop-gloss), [RT-RTE-agent-packet](runtime.md#rt-rte-agent-packet), [RT-RTE-acceptance-driver](runtime.md#rt-rte-acceptance-driver); not evidence of an executed run or automatic upstream repair |
| Native memory, native compaction, provider state | External per direct `docs/design.md` and supplied runtime | Opaque alternative checkpoint forms: host summary, native plan/task/account memory. No kit-defined schema or read-back contract for their contents; no claim of their absence |

The registered script/CLI surface contains no exposed service or vector-store API in the inspected dispatch and settings: it is shell/Python callbacks plus file-oriented skills. This is a description of inspected entry points, not an exhaustive negative about host plugins or tools. SRC-1, `.claude/settings.json`, `.claude/scripts/workstream-record.py`, `.claude/scripts/workstream-rewrite.py`.

## Core ideas

1. **A small automatic index precedes requested full-state reads.** The hook injects ACTIVE.md, roster and diagnostics. Work then requests the active workstream; status requests every workstream and the project-declared context. Selection is path/format based, not semantic similarity. Read cost is managed by extraction, compact packets, a 65,536-byte warning and telemetry rather than kit-side truncation of model context. See [RT-RTE-session-reload](runtime.md#rt-rte-session-reload) and [MEM-OBJ-project](#mem-obj-project).
2. **A record is not its own warrant.** Stored Decisions and Learnings guide work, but the work/review/extract instructions require checking their named artifacts. Markers and counts are deterministic index facts, not evidence that an insight reached its governing home. See [MEM-OBJ-workstream-content](#mem-obj-workstream-content), [MEM-CLM-marker-reopening](#mem-clm-marker-reopening).
3. **The kit separates live reading from historical recoverability.** Condensation preserves selected statements, reasons and references; in-file archive moves completed phases out of Backlog; rotation removes spent blocks into tagged history; closure removes the directory. These operations have different preservation checks and later consumers. Merely keeping Git history does not automatically deliver removed detail. See [MEM-RTE-state-rotate](#mem-rte-state-rotate), [MEM-OBJ-archive](#mem-obj-archive).
4. **Transfer requires adoption, not just retention.** Capture derives Decisions/Learnings from session experience, and extraction requests actual edits to governed files or receiver-owned backlog. This is a model-mediated trace-to-artifact pathway, not a demonstrated improvement or parameter update. See [MEM-BAP-artifact-adoption](#mem-bap-artifact-adoption).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-active-selector
Label: ACTIVE symbolic selectors

Part of: [RT-OBJ-active](runtime.md#rt-obj-active)

The `workstream` and `task` fields are symbolic parts of the Markdown file, intended to persist through Git. The hook uses the workstream value to locate active detail and mark the roster; the task value supplies the next work reference, not a native goal handle. Creation/capture/work update these through the foreground model. Formatting is operational: comments can become path text. Distinct from the prose part below. SRC-1, `.claude/rules/workstreams-rule.md`, `.claude/hooks/session-start.sh`.

> Nothing follows a value on its line: the session-start hook reads each with `cut`, and a trailing comment becomes part of the path.
> --- `.claude/rules/workstreams-rule.md`

#### MEM-OBJ-active-prose
Label: ACTIVE resume prose

Part of: [RT-OBJ-active](runtime.md#rt-obj-active)

Now/Next/Blockers are natural-language session checkpoints in the same local file/Git lineage. The model derives them from completed work and remaining scope; SessionStart prints the entire file to the host. Their consumer is a later foreground model, with planning authority by instruction, not enforced factual authority. Prior chat, precise goal wording and goal-armed state are not reconstructed by the pointer. SRC-1, `.claude/skills/workstream-work/SKILL.md`.

> If a condition was drafted but never armed, record the SCOPE it covered — the task or phase, and the turn bound — not "the drafted goal", since the draft dies with the session and scope is what re-deriving the condition needs anyway.
> --- `.claude/skills/workstream-work/SKILL.md`

#### MEM-OBJ-workstream-index
Label: Workstream symbolic structure and markers

Part of: [RT-OBJ-workstream](runtime.md#rt-obj-workstream)

IDs, headings, checkbox states, frontmatter and dated markers in local Markdown/Git provide symbolic inputs to hook counters, record diagnostics, reference checks and rewrites. These are distinct from the prose's truth and meaning. The file's author may be model or human; creation has a wording gate, routine capture does not. `disposition` scores sentence/clause-start dated terminal markers and whole-struck entries; terminal presence takes precedence over deferred markers. A later EXTENDED does not undo that score. The read/transform consequence is in [MEM-CLM-marker-reopening](#mem-clm-marker-reopening). SRC-1, `.claude/scripts/workstream_state.py`, `.claude/scripts/workstream-record.py`.

> if marker_counts(body, TERMINAL_RE):
>         return 'terminal'
> --- `.claude/scripts/workstream_state.py`

#### MEM-OBJ-workstream-content
Label: Workstream retained claims and reasoning

Part of: [RT-OBJ-workstream](runtime.md#rt-obj-workstream)

Purpose, task descriptions, completion evidence, Decision reasoning, Learning insights/targets and Open Questions are natural-language content in local Markdown and intended Git snapshots. Their lineage is interviewed intent, work evidence, session findings and model synthesis, not a raw transcript archive. Later work reads this content to choose/execute tasks; review compares it with artifacts and newer decisions; extraction routes or condenses it. Reasons are expressly required in Decisions, but retaining a paragraph does not certify that all reasons survived. Resolved Open Questions that become standing constraints are promoted into Decisions because unresolved-question presentation invites skimming. SRC-1, `.claude/rules/workstreams-rule.md`, `.claude/skills/workstream-work/SKILL.md`.

> **Decisions record reasoning**, not just outcomes.
> --- `.claude/rules/workstreams-rule.md`

> A resolution that became a standing constraint is also promoted to a Decision — this section reads as what is NOT yet settled and is skimmed that way, while Decisions are read before work; strike-through alone is for a question that resolved into an action already taken.
> --- `.claude/rules/workstreams-rule.md`

#### MEM-OBJ-notes
Label: Optional session research notes

`.state/workstreams/<type>/<name>/notes.md` is optional natural-language research in a local file, not a permanent product home. No counterpart distinct from the general lifecycle is declared in runtime. It is not a part of the single workstream.md file. Extraction selects each section for summary into the workstream, routing to a named artifact, or explicit drop. Actual initial authorship and completeness depend on the session; no automatic transcript-to-notes writer is established. Later consumption is through that extraction, not automatic full-note injection. SRC-1, `.claude/rules/workstreams-rule.md`.

> Optional `notes.md` beside workstream.md holds session-scoped research only; `/workstream-extract` dispositions every notes.md section (summarized into workstream.md, routed to a named home, or dropped by declaration) and moves anything durable to its permanent home, so nothing load-bearing dies with the archive.
> --- `.claude/rules/workstreams-rule.md`

#### MEM-OBJ-project
Label: PROJECT context selection list

`.state/PROJECT.md`, seeded only if missing, is local Markdown/Git. Unique skill directory names and context paths are symbolic selectors; the chosen files and skill descriptions supply natural-language project framing. The list is user-editable, not inferred by scanning every installed skill. Status reads listed skill descriptions only and whole listed context files; when sections are empty it may derive a draft from authored CLAUDE.md for confirmation/editing. This is a separate selector from [RT-OBJ-active](runtime.md#rt-obj-active), not its duplicate. Initial list contents and later human edits in consumer projects are unavailable. SRC-1, `.state-seed/PROJECT.md`, `.claude/skills/workstream-status/SKILL.md`, `install.sh`.

> It is a list
> rather than a scan because a scan of `.claude/skills/` cannot tell a skill
> unique to this project from one copied in from a shared source, and only
> what is unique to this project frames its status.
> --- `.state-seed/PROJECT.md`

#### MEM-OBJ-handoffs
Label: Receiver inbox transfer files

`.state/handoffs/from-<source>-<YYYYMMDD-HHMMSS>.md` in the receiving project stores natural-language self-contained items plus symbolic source/date/blocking/items/about/class/committed metadata. This is a distinct file class from runtime's workstream and ACTIVE objects. Sender derives the content, reads receiver state to avoid duplication, records the substance in its own task, confirms destination/visibility and files the item. Receiver verifies adopted claims and triages to action/backlog/decline, then deletes processed files. The hook injects count/age only; detailed content requires a receiver read. Git filing retains the arrival even after inbox deletion; a sender filename alone is not enduring evidence. SRC-1, `.claude/skills/handoff/SKILL.md`.

> Commit each file in `.state/handoffs/` that arrived uncommitted, before anything else
> --- `.claude/skills/handoff/SKILL.md`

> Correcting an item still in flight is an edit in place
> --- `.claude/skills/handoff/SKILL.md`

#### MEM-OBJ-archive
Label: Archive ledger and tagged snapshots

`.state/workstreams/ARCHIVE.md` has natural-language outcomes and symbolic `ws/<name>` tag locators; Git tags point to historical state, not an opaque payload or readable summary of all its content. Ledger and snapshot differ in granularity and delivery. Closure writes done status and ledger, commits, tags, deletes directory, conditionally resets ACTIVE and commits again. Work reads the ledger to avoid rebuilding closed work; status resolves closed references against it; an explicit `git show` can retrieve the original record. Rotation uses dated tags and in-file pointers instead. These are historical products of [RT-RTE-state-lifecycle](runtime.md#rt-rte-state-lifecycle), not duplicate declarations of that route or the current workstream object. Remote reach needs separate tag publication. SRC-1, `.claude/skills/workstream-close/SKILL.md`, `.claude/skills/workstream-work/SKILL.md`.

> The status edit is what makes the tagged snapshot read as closed: a `git show ws/<name>:...` reader otherwise gets a file claiming to be live.
> --- `.claude/skills/workstream-close/SKILL.md`

#### MEM-OBJ-context
Label: Context telemetry checkpoint

`/tmp/claude-{session_id}-context.json` (or `WORKSTREAM_KIT_CONTEXT_DIR`) is a local symbolic numerical/access-metadata record, not work content or a distributed-parametric representation. The status-line callback derives percentages from host JSON and the same session's first saved remaining percentage; an atomic temporary-file/move replaces it. `--context <project-dir>` normalizes project paths and selects the newest matching updated record. Capture requests its two displayed numbers to inform the user's clear/compact decision; this is metadata read-back, not semantic recall or automatic compaction. The inspected reader has no freshness cutoff; the storage's eventual cleanup/lifetime is external. Distinct from all runtime-declared objects; overlaps runtime's budgeting discussion only. SRC-1, `.claude/scripts/status-line.sh`, `install.sh`, `.claude/skills/workstream-capture/SKILL.md`.

> [.[]|select((.project_dir|norm)==($p|norm))]|sort_by(.updated)|last
> --- `.claude/scripts/status-line.sh`

### Routes

#### MEM-RTE-learning-condense
Label: Learning sentence condensation

Part of: [RT-RTE-rewrite-state](runtime.md#rt-rte-rewrite-state)

A distinct rewrite subroute with content-specific checks: caller selects `learnings <file>`; code folds Learning blocks, selects terminal entries, retains the first statement (two sentences if leading provenance), integration-target sentences and latest terminal-marker sentence, wraps the result and checks losses/count/fingerprint. A later dated EXTENDED causes this subroute to leave the entry whole, unlike rotation. Owner: code for sentence selection/rejection; model/caller for semantic eligibility and `--write`. Admission: dry-run by default, actual replacement only with the flag; generic caller identity does not establish human per-content approval. Extract guidance requests citation checks and artifact verification first. Recovery depends on committed original text. No semantic answer oracle is supplied; sentence preservation is a limited structural/content predicate. SRC-1, `.claude/scripts/workstream-rewrite.py`, `.claude/skills/workstream-extract/SKILL.md`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: condensed counts, byte savings, entry reports, refusal, NO CHANGE or WRITTEN.
- Later read-back: replaced workstream text reaches later work/review/status and another condensation invocation; detailed removed reasoning requires Git retrieval.
- Delegated visibility: inapplicable — the deterministic script invokes no model; a caller may separately delegate its review.
- Selection predicate: Learning block with terminal disposition, parseable prefix, useful shortening and no EXTENDED after latest terminal marker; statement/target/disposition loss check.
- Invalidation or expiry: original live block overwritten with --write; refused transformation leaves it unchanged; history retention is caller-dependent.
- Activation or effect: selected text is rewritten, but downstream model behavior and benefit are unobserved.
- Evidence limits: sentence heuristics and fingerprints do not certify semantic completeness or truth of adoption; manual edits bypass them.

> if any(a.start() > last.start() for a in marker_counts(blanked, ADDENDUM_RE)):
>         return None
> --- `.claude/scripts/workstream-rewrite.py`

#### MEM-RTE-state-rotate
Label: Live record rotation

Part of: [RT-RTE-rewrite-state](runtime.md#rt-rte-rewrite-state)

Caller selects file/tag/keep phrases; code constructs a new live record and checks removed-block references, selected stale numerical claims and retained open/gate/standing structure. Trigger by policy is persistent SIZE after drain; direct CLI invocation does not enforce that trigger. Producer/selector is deterministic code; model/caller decides drain completion, tags and keep/repoint edits. CLI checks tag existence, not that its snapshot equals all current file bytes. Admission is `--write` following checks; `--allow-stale-claims` explicitly weakens one refusal. User per-content review is not enforced. Recovery requires the intended pre-rotation snapshot actually to have been committed/tagged. No semantic oracle. SRC-1, `.claude/scripts/workstream-rewrite.py`, `.claude/skills/workstream-extract/SKILL.md`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: drop/size report, unresolved-reference refusals or warnings, stale claims, NO CHANGE or WRITTEN.
- Later read-back: hook/model see reduced live file; Purpose rotation paragraph and Learning numbering note direct requested historical retrieval to tags.
- Delegated visibility: inapplicable — rotation invokes no subagent; semantic review remains caller responsibility.
- Selection predicate: preserve frontmatter/Purpose, open Backlog, critical path, criteria, unknown sections, unstruck Open Question item shape, nonterminal Learnings, live-cited Decisions and explicit keep matches; remove in-file Archive and other spent blocks.
- Invalidation or expiry: removed blocks leave the live file; dated history pointer replaces prior rotation paragraphs; IDs in retained open structure must remain.
- Activation or effect: executable context reduction by rewriting future input; not an observed context reload or improvement.
- Evidence limits: reference sweep covers surviving text and selected live content in other workstreams/ACTIVE, not every repository dependency; home-less other-file IDs warn rather than refuse; explanation without citation can be lost. Terminal-before-EXTENDED entries can leave, unlike Learning condensation.

> if kind == 'item' and LEARNING_RE.match(raw[0]) and disposition(text) == 'terminal' and not keep_by_phrase(text):
> --- `.claude/scripts/workstream-rewrite.py`

> rebuilt[heading] = list(body)  # a section the kit does not know is carried verbatim
> --- `.claude/scripts/workstream-rewrite.py`

### Claims

#### MEM-CLM-marker-reopening
Label: Reopening claim differs across consumers

Claimed operation: the rule says a later EXTENDED reopens an entry; source SRC-1, `.claude/rules/workstreams-rule.md`. Closest supplied record is [RT-CLM-rewrite-preservation](runtime.md#rt-clm-rewrite-preservation), but this claim concerns marker interpretation, not heading/checkbox preservation.

> EXTENDED is not a disposition: `EXTENDED <date>: ...` appends to a Learning that is still open, and one written after the last terminal marker reopens the entry, so a condensation leaves it whole.
> --- `.claude/rules/workstreams-rule.md`

Assessment: the condensation-specific protection is implemented in [MEM-RTE-learning-condense](#mem-rte-learning-condense). Shared `disposition`, record scoring and [MEM-RTE-state-rotate](#mem-rte-state-rotate) still treat an earlier terminal marker as terminal, even with later EXTENDED. The damage suite explicitly expects that scoring; this is not an inferred accidental omission. Therefore the general reopening language does not establish retention under rotation or an undispositioned drain signal. This qualifies the runtime baseline without contradicting its already bounded preservation finding. Source inspection supplies the implementation countercase, not an observed loss. SRC-1, `.claude/scripts/workstream_state.py`, `.claude/scripts/workstream-record.py`, `.claude/scripts/workstream-rewrite.py`, `tests/damage-acceptance.sh`.

> check "ROUTED then EXTENDED still scores terminal (the ROUTED marker)" "printf '%s\n' \"\$DISP\" | grep -qx 'routed_ext terminal'"
> --- `tests/damage-acceptance.sh`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-artifact-adoption
Label: Extracted insight to governed artifact

Consumer: later readers/executors of named permanent files, or receiver model reading the adopted backlog/instruction. Channel: actual file edit or verified handoff adoption, not a Learning's APPLIED marker alone. Force: document-specific normative guidance, task planning, or executable product behavior; destination authority must be established there. Horizon: later sessions/projects until revision; remote reach additionally requires publication. Closest supplied records [RT-BAP-resume-state](runtime.md#rt-bap-resume-state) and [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance) cover resume planning and installed skills; this path crosses from experienced work into the governing artifact. A governed skill edit could subsequently enter the latter path, but an arbitrary product edit need not do so. SRC-1, `.claude/skills/workstream-extract/SKILL.md`, `.claude/rules/workstreams-rule.md`, `.claude/skills/handoff/SKILL.md`.

> Applied to a file is terminal only for a file this project governs; where something else writes the file — an installer, a generator, a vendored copy, an upstream template — the disposition is provisional until the change reaches whatever governs the file
> --- `.claude/rules/workstreams-rule.md`

This is an afforded/prescribed authority path, not demonstrated learning or exercised self-improvement. Writing a fixture's installed skill copy does not establish adoption into the kit's source or future installations.

## Annotations

#### On [RT-OBJ-active](runtime.md#rt-obj-active)

Memory parts are [MEM-OBJ-active-selector](#mem-obj-active-selector) and [MEM-OBJ-active-prose](#mem-obj-active-prose). Git is the intended durability substrate; publication, not merely commit, gives other machines reach. Content is derived checkpoint state rather than the original session trace. Retained scope cannot verify goal arming. SRC-1, `.claude/skills/workstream-work/SKILL.md`, `.claude/skills/workstream-capture/SKILL.md`.

#### On [RT-OBJ-workstream](runtime.md#rt-obj-workstream)

Memory parts are [MEM-OBJ-workstream-index](#mem-obj-workstream-index) and [MEM-OBJ-workstream-content](#mem-obj-workstream-content). Substantive review edits need user approval; routine capture and mechanical fixes do not. Supersession marks old Decisions in place, preserving reasons and preventing them from reading as current; shared-artifact retirement requests a wider sweep. Live records, condensed records, in-file Archive and tagged snapshots are alternative retention forms with different default visibility. SRC-1, `.claude/rules/workstreams-rule.md`, `.claude/skills/workstream-review/SKILL.md`, `.claude/skills/workstream-extract/SKILL.md`.

#### On [RT-RTE-state-lifecycle](runtime.md#rt-rte-state-lifecycle)

Trace origin is the session's conversation/work findings, user choices, artifact evidence and incoming handoffs. Capture asks the model to compare that experience with durable files, route missing items and synthesize general patterns extending/superseding Decisions or Learnings. This is model-mediated derived-memory writing; completeness and actual improvement are unobserved. Initial creation content is interviewed and wording-approved. Capture authors and commits content without a new per-item human gate; review gates substantive restructuring. Extraction admits applied content only through a named governed destination, handed-off content through its own destination/visibility gate, or drops with stated rationale. Receiver adoption separately verifies claims and can decline. Reasons for dropped material are requested in place; incoming originals survive receiver Git filing even after deletion. SRC-1, `.claude/skills/workstream-create/SKILL.md`, `.claude/skills/workstream-capture/SKILL.md`, `.claude/skills/workstream-review/SKILL.md`, `.claude/skills/handoff/SKILL.md`.

> write any synthesis-level pattern where it extends or supersedes an existing Decision or Learning.
> --- `.claude/skills/workstream-capture/SKILL.md`

#### On [RT-RTE-rewrite-state](runtime.md#rt-rte-rewrite-state)

Records condensation extracts dates/status, existing local Decision references and commit hashes from completion notes; Decisions condensation uses caller-named IDs and a resolvable release/tag/commit, keeps heading plus first paragraph and writes provenance. These are automatic text transformations of retained state, not independently generated semantic learning. The first paragraph is expected to carry reasoning, but the code does not test that expectation. Legacy `condense-completed-records.py` forwards to the same `run_condense`, so it is another entry point, not another algorithm. Standard fingerprint checks headings and checkbox state/ID sequence, not descriptions or all evidence. Learning and rotation checks differ as the two declared subroutes show. SRC-1, `.claude/scripts/workstream-rewrite.py`, `.claude/scripts/condense-completed-records.py`, `.claude/scripts/workstream_state.py`.

> cond = [head] + para + [tail]
> --- `.claude/scripts/workstream-rewrite.py`

#### On [RT-RTE-session-reload](runtime.md#rt-rte-session-reload)

Push selector: host SessionStart triggers hook code, using current ACTIVE, all matching workstreams, ledger, inbox, Git history and optional record diagnostics. Selected content is the entire ACTIVE file plus derived summaries/signals, not all workstream prose. At 65,536 bytes it warns rather than truncates; roster size scales with workstreams, and ACTIVE length is conventional. Hook output is transient, recomputed metadata; original source remains in files. Model work requests the full record separately. Host delivery after compact is intended, but event semantics remain external, including the capture/hook clear discrepancy already identified by runtime. SRC-1, `.claude/hooks/session-start.sh`, `.claude/settings.json`, `.claude/skills/workstream-work/SKILL.md`.

#### On [RT-RTE-agent-packet](runtime.md#rt-rte-agent-packet)

Working-context control isolates a bounded task's work from foreground context by host subagent calls. The foreground selects verbatim specification plus scope/checks; findings and limitations return for verification. The temporary-frame analogy fits selected inputs and a compact return, not shared-addressable memory: returned text is by value and host eviction details are uninspected. A return becomes durable memory only if adopted into files/checkpoints; the packet itself is not specified as later cross-session recall. SRC-1, `.claude/skills/workstream-work/SKILL.md`; agent-tool/capability details remain supplied runtime findings.

#### On [RT-RTE-acceptance-driver](runtime.md#rt-rte-acceptance-driver)

Raw output is retained in temporary session-A/B/C.txt files, separate from fixture-derived Learnings, changed installed guidance and Git/tag history. The driver derives closing-paragraph display summaries and transcript-reference-read observations; those summaries are not the whole trace. A maintainer is explicitly asked to read Session C and historical Learnings before deleting the fixture. This affords later manual inspection/adoption, not an automatic kit-source update. No run outputs were supplied; comments reporting discoveries are not observed traces for this analysis. SRC-1, `tests/va3-acceptance.sh`.

> # fixture's own Learnings and applies them to its installed skill copies. Read
> # Session C's output and the fixture's Learnings (in its git log, since the
> # closure archives the workstream file) before deleting the fixture -- both
> --- `tests/va3-acceptance.sh`

## Write side

Admission and physical writing differ. Installation seeds missing state without interviewing the user about its empty contents; caller target/force choices admit payload changes, not individual learned facts. Creation obtains approval of exact workstream wording. Routine work/capture uses model judgment to admit evidence notes, Decisions, Learnings and pointer updates; a user starting the session is not per-content approval. Review allows mechanical correction directly but presents substantive restructures for user decision. Source authority checks and reasons are prescribed, not a mandatory filesystem filter. See lifecycle and install records above.

The trace-fed chain is session instances → capture detection/cascade/synthesis → Decision/Learning/backlog/pointer or permanent-file edit → committed state → later work/review/extract consumer. This is not raw transcript retention. Native compaction's history-to-summary transformation is external and opaque; kit capture provides a second, manually/model-selected checkpoint before the boundary. Notes can be summarized, routed or explicitly discarded. Reasons survive by policy in Decisions and drop rationales; automatic condensation retains only selected sentences/paragraphs. Neither history existence nor a reference guarantees a later model requests all those reasons. SRC-1, `.claude/rules/workstreams-rule.md`, `.claude/skills/workstream-capture/SKILL.md`, `.claude/scripts/workstream-rewrite.py`.

Cleanup has several distinct consumers and rejection points. Extraction verifies every disposition against its target rather than trusting a marker, routes external findings, and only then condenses. A superseded Decision remains visibly marked. A completed phase can move in-file, preserving IDs without shrinking bytes. Rotation changes the actual live reader's input and can refuse unresolved references or changed live structure; its terminal marker selection has the documented reopening countercase. Closure refuses unsatisfied criteria or missing user approval, requests per-task successor mapping and inward dependency sweeps, and removes the directory only after a final tagged state. Withdrawal is therefore a file/status/reference operation plus historical retention, not an access revocation system. Manual writes can bypass all these policies/checks. SRC-1, `.claude/skills/workstream-extract/SKILL.md`, `.claude/skills/workstream-close/SKILL.md`; [MEM-RTE-state-rotate](#mem-rte-state-rotate).

Handoffs add two admission boundaries: sender destination/visibility confirmation, then receiver claim verification and do/route/decline judgment. In-flight corrections replace conflicting text; after triage corrections are new items. Sender substance persists independently of an ephemeral inbox filename. Declined items can leave a rationale and optional reply; processed files leave the inbox but should remain in receiver history. A commit gives local durability; push separately decides reach/publication. SRC-1, `.claude/skills/handoff/SKILL.md`.

## Read-back

Automatic supply and requested retrieval are separate. SessionStart pushes the small pointer and computed signals to the foreground; its selectors are paths, statuses and patterns. `/workstream-work` requests full active state and checks actual artifacts, archive ledger and other live ownership before choosing a goal. `/workstream-status` requests all statuses, ledger, inbox, record JSON, Git metadata and PROJECT-listed context, but returns chat rather than durable memory. Status's source restrictions mean its asserted premises remain unverified there; actionable disagreements must be captured/routed by another operation. SRC-1, `.claude/hooks/session-start.sh`, `.claude/skills/workstream-work/SKILL.md`, `.claude/skills/workstream-status/SKILL.md`.

There is no inspected relevance-ranking/budget allocator for work memory. The pointer targets one current workstream, roster/status widen coverage, `cites` searches literal/ID references, and rotation preferentially removes completed/terminal history. Fresh-context subagents reduce foreground exposure and return selected findings; model packet selection governs what is kept out. Context telemetry reports a budget but neither chooses the user's clear/compact action nor executes eviction. Full history remains reachable by explicit Git/tag lookup, not automatically dereferenced from every citation. See [MEM-OBJ-context](#mem-obj-context), [MEM-OBJ-archive](#mem-obj-archive), agent-packet annotation.

Behavioral authority is consumer-relative. Hook parsers give symbolic fields fixed selection/count consequences. Foreground models interpret prose as planning context subject to rechecking against the world. Receiver models do not have sender conversation context and require self-contained items. Permanent artifact consumers receive the actually adopted edit, not the full Learning or its rationale unless those were included. Host plan/task/native memory consumers, exact compaction tail/summary and delegate receipt of hook output remain uninspected. No delivery here establishes activation or benefit.

## Integration issues

- **Marker reopening is consumer-specific.** [MEM-CLM-marker-reopening](#mem-clm-marker-reopening) adds a source-supported countercase to the broad lifecycle/rewrite account: condensation protects a later EXTENDED, shared scoring and rotation do not. Reconciliation should preserve that distinction when connecting [RT-RTE-rewrite-state](runtime.md#rt-rte-rewrite-state) and [RT-OBJ-workstream](runtime.md#rt-obj-workstream). The source suite explicitly expects terminal scoring, so whether prose or rotation should change is unresolved; this report does not prescribe a repair.
- **No referent duplication intended.** Pointer and workstream parts have explicit Part of relations; the two rewrite subroutes partition different code paths/checks within the runtime route. New objects are side files, selector/telemetry records and archive products, not replacements for runtime containers. [MEM-BAP-artifact-adoption](#mem-bap-artifact-adoption) may join [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance) when an insight changes governed instructions, but arbitrary permanent artifacts are not identical to installed skill guidance.
- **History fidelity depends on caller discipline.** Rotation checks that a tag exists, not byte identity with the current pre-rewrite state; condensation does not commit the old file itself. Therefore [MEM-OBJ-archive](#mem-obj-archive) and both rewrite subroutes cannot support unconditional full-text recovery. This qualifies preservation rhetoric consistently with [RT-CLM-rewrite-preservation](runtime.md#rt-clm-rewrite-preservation).
- **Host event contract remains unresolved.** The hook includes clear among intended SessionStart events, while capture says clear fires no hook. This prevents a guarantee of post-clear injection, not the implemented file retention/reload capability. Concerns [RT-RTE-session-reload](runtime.md#rt-rte-session-reload).
- **Opaque external memory and artifact adoption remain local unknowns.** Native memory/compaction contents and exact model versions are external. No consumer deployment shows extracted guidance reaching a later invocation. Evaluator fixture edits/logs afford inspection but do not prove kit-source adoption or improved capacity. Concerns [RT-CMP-claude](runtime.md#rt-cmp-claude), [RT-RTE-acceptance-driver](runtime.md#rt-rte-acceptance-driver), [MEM-BAP-artifact-adoption](#mem-bap-artifact-adoption).

## Limitations and checks

Source HEAD equals the boundary's full revision; source status was clean. This job used only registered SRC-1, pinned supplied members and current governing method files, with no target execution, external acquisitions or prior-analysis reads. Method inputs were read completely, recovering the bounded runtime continuation; supplied type wins where job phrasing differs.

Code-path inspection establishes architectural selection, mutation and refusal predicates, not compliant model behavior, deployed context contents, truthful markers, full recovery after interruption, or learning benefit. Remaining parsing branches, consumer project contents, host event semantics and account memory remain bounded uncertainties above. No claim of exhaustive host-memory coverage or causal improvement follows.

Deterministic validation: the invocation's `commonplace-run validate-output` check passed after correcting two quotation transcriptions (Markdown emphasis and shell-comment prefixes). This establishes content/relation form and quote occurrence, not semantic acceptance.
