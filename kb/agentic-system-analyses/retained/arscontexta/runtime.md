---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Ars Contexta runtime baseline: conversational generation, queue-driven model work, hook effects and approval-based evolution at the frozen commit."
run-id: AAS-2026-10-12-arscontexta-f9e5f2f34166-01
reviewed-boundary: "2acfd5cc4473c4d06c46be63df748e77e00e2746"
---

# Ars Contexta runtime report

## Runtime account

Ars Contexta supplies a Claude Code plugin and instructions for generating and operating a Markdown knowledge vault. It does not supply an enclosing model scheduler. The consequential work is deriving a domain-specific system, processing sources into linked notes, maintaining older notes, and revising the instructions and architecture from operational evidence. Model interpretation performs most of that work; registered shell hooks have narrower, inspectable effects. SRC-1: `.claude-plugin/plugin.json`, `skills/setup/SKILL.md`, `skill-sources/pipeline/SKILL.md`, `hooks/hooks.json`.

### Entry and ordinary invocation

The plugin manifest identifies version 0.8.0. Plugin commands live in `skills/`; processing procedures live in `skill-sources/`. Setup selects a platform, elicits the user's needs, derives dimensions and vocabulary, presents a proposal, and generates folders, context, templates, configuration, skills and hooks. It writes `ops/derivation.md` first so later generation can reread the derivation after compaction. The setup route is [RT-RTE-setup-generation](#rt-rte-setup-generation); the resulting instructional surface is [RT-OBJ-claude-md](#rt-obj-claude-md). SRC-1: `skills/setup/SKILL.md`.

The ordinary operating invocation traced here is `/pipeline [source-file]`. The initiating user supplies a source; the model reads vocabulary from the derivation manifest and drives seed, extraction, claim processing, completion checking and archiving. Seed detects duplicates, relocates the source to its batch archive, creates an extract-task file, and appends queue state. The queue identifies tasks and their files; `current_phase` and `completed_phases` determine the next action. The lead requests extraction with `/ralph 1 --batch {batch_id} --type extract`, then requests processing of pending claims. Eligibility for that initial extraction is not established by seed's templates: they omit `batch` and `current_phase`, while ralph filters by those fields and dispatches by current phase. Neither seed's full procedure nor pipeline's seed/extract steps nor ralph's queue/filter/dispatch instructions specify an additional field-production or extraction-selection rule resolving this mismatch. The downstream account is conditional on an eligible extraction entry, not a demonstrated connection from the supplied seed output. [WF-CLM-extract-selection](workflow.md#wf-clm-extract-selection) retains the matching template/filter evidence. In serial ralph, the lead reads the queue, selects the first eligible pending entry, builds a phase prompt, calls Task, waits for its return, parses a handoff, advances the queue, and rereads it. The worker performs the file operation; the lead owns subsequent serial scheduling. SRC-1: `skill-sources/pipeline/SKILL.md`, `skill-sources/seed/SKILL.md`, `skill-sources/ralph/SKILL.md`.

Create writes a note; reflect adds connections and topic-map membership; reweave updates older notes; verify predicts note content from title and description before reading the body, then checks schema and graph health. Reflect/reweave prompts receive already-created sibling claim titles, not an assertion that all sibling bodies were supplied. Once an extraction worker is reached, extraction additionally writes new claim/enrichment tasks for the lead to discover on reread; that later producer does not resolve initial seed-to-extract eligibility. A completed batch with multiple claims gets a cross-connect pass. The pipeline checks remaining queue entries before archiving and reports note titles, counts, quality results and archive paths. This is the requested protocol, not an observed execution. Its admission, evaluation and recovery details are in [RT-RTE-source-processing](#rt-rte-source-processing). SRC-1: `skill-sources/ralph/SKILL.md`, `skill-sources/verify/SKILL.md`, `skill-sources/pipeline/SKILL.md`.

There are unresolved instruction-level integration issues. Pipeline passes the pending claim count to ralph and describes completing whole claim pipelines. Serial ralph counts iterations that advance one phase and reselect the first pending entry. Thus the wrapper's count does not by itself warrant completion of every phase for every claim. Its completion check may instead return pending tasks. Reduce retains a user-approval requirement even with handoff enabled, while ralph requests worker `mode: dontAsk`. The shipped `/enrich` reference and `/archive-batch` reference name additional entry paths; this account inspected their callers, not a standalone implementation of either command. No claim of executable availability follows from those names. SRC-1: `skill-sources/pipeline/SKILL.md`, `skill-sources/ralph/SKILL.md`, `skill-sources/reduce/SKILL.md`.

### Material forcing routes and guarantees

Four forcing cases qualify the ordinary account:

1. **Parallel ralph:** one worker processes a claim through its remaining phases and updates its queue entry; up to five workers share vault state. This contradicts any system-wide claim of one phase per worker. The lead waits for all worker returns, including errors, before cross-connecting. Sibling lists and a later repair pass address missing-yet sibling notes, not general transactional isolation. [RT-RTE-parallel-claims](#rt-rte-parallel-claims).
2. **Missing handoff or failed verification:** ralph permits continuation when a handoff or task-file section is missing, whereas verify says failures must remain at verify. A done queue entry is not a reliable proof of verification success. [RT-CLM-completion-gate](#rt-clm-completion-gate).
3. **Alternate filesystem writes:** the plugin's PostToolUse matcher is Write, not Edit or Bash. Its validator emits warnings after the write and exits successfully. Direct edits, shell writes and other host tools are not covered by this registration. Async auto-commit stages all pending changes, so even an unvalidated alternate-path change can be included in a later Write-triggered commit. [RT-RTE-write-hooks](#rt-rte-write-hooks).
4. **Generated deployment versus plugin:** setup specifies copied, vocabulary-transformed skills and a generated Stop hook; the platform generator instead says processing skills are inherited. The registered plugin has no Stop event. SessionStart writes a fresh current-session record before printing the section labelled previous session context. The printed record is therefore not necessarily the prior session. [RT-RTE-session-orientation](#rt-rte-session-orientation), [RT-CLM-generation-paths](#rt-clm-generation-paths).

Fresh-context isolation is a **protocol** owned by ralph's model lead, requested at Task construction and checked by reported spawn counts. Serial coverage requires the host's Task context contract and model compliance; parallel claim workers deliberately span multiple phases. Implementation conclusion status: claimed. Operation conclusion status: uninspected. SRC-1: `skill-sources/ralph/SKILL.md`; [RT-RTE-parallel-claims](#rt-rte-parallel-claims).

Schema protection is **best effort**, owned by the post-write hook and semantic verification procedure. The hook's enforcement point is after a matching Write in a detected vault, covering only limited presence tests in hard-coded note paths; it cannot prevent the original effect. Host event delivery, current directory and tool JSON are external contracts. Implementation conclusion status: wired. Operation conclusion status: uninspected. SRC-1: `hooks/hooks.json`, `hooks/scripts/write-validate.sh`; [RT-RTE-write-hooks](#rt-rte-write-hooks).

Human approval for architecture and skill changes is a **policy** owned by the relevant conversational procedure, enforced only by instructions before file changes. Architect, rethink, reseed and upgrade specify it. They also allow filesystem-writing tools; no enclosing permission enforcement was inspected. The policy does not cover every retained-content write: explicit remember and session-mining modes have different admission instructions, and hooks can migrate a marker or commit without a proposal dialog. Implementation conclusion status: claimed. Operation conclusion status: uninspected. SRC-1: `skills/architect/SKILL.md`, `skill-sources/rethink/SKILL.md`, `skills/reseed/SKILL.md`, `skills/upgrade/SKILL.md`, `skill-sources/remember/SKILL.md`, `hooks/scripts/vaultguard.sh`; [RT-RTE-architecture-evolution](#rt-rte-architecture-evolution), [RT-RTE-skill-upgrade](#rt-rte-skill-upgrade).

Git persistence is **best effort**, owned by auto-commit. Its enforcement point is an async Write callback after checking configuration, vault detection and repository presence. It silently tolerates commit failure and bypasses Git verification hooks. It neither guarantees rollback nor remote durability. Implementation conclusion status: wired. Operation conclusion status: uninspected. SRC-1: `hooks/scripts/auto-commit.sh`; [RT-RTE-write-hooks](#rt-rte-write-hooks).

### Host boundary, changes and evidence strength

The capability surface includes Read, Write, Edit, Bash and Task in ralph/pipeline metadata, and optional qmd/MCP retrieval. Architect has model label opus; pipeline has sonnet; ralph says workers inherit the session model. These are host-facing declarations, not the current grant set. No actual project permission state, provider selection, deployed isolation envelope or host implementation was supplied. `mode: dontAsk` is a requested worker mode, not evidence of either unrestricted execution or a host sandbox. Provider-native tools, callbacks, external extensions, remote workers and direct provider calls remain outside inspected implementation; no universal guarantee over those paths is asserted. Model fixity is in [RT-CMP-session-model](#rt-cmp-session-model). SRC-1: `skill-sources/ralph/SKILL.md`, `skill-sources/pipeline/SKILL.md`, `skills/architect/SKILL.md`, `platforms/claude-code/generator.md`.

Architecture evolution compares health, friction and research with retained design intent. Rethink explicitly challenges quoted assumptions; architect proposes ranked changes; reseed re-derives dimensions and restructures files; upgrade changes skill text and archives previous versions. These alter the generated system's behavior instructions or production machinery, subject to their distinct approval and recovery procedures. They do not establish a deployed improvement. Memory-specific revision mechanisms remain for the memory analyst; this report retains only admission and runtime authority distinctions needed to avoid attributing every change to the same approval gate. SRC-1: `skill-sources/rethink/SKILL.md`, `skills/architect/SKILL.md`, `skills/reseed/SKILL.md`, `skills/upgrade/SKILL.md`, `skill-sources/remember/SKILL.md`.

Added inspection within SRC-1 covers hook bodies and registration, ralph's serial and parallel scheduling/return/recovery instructions, pipeline's complete procedure, setup's proposal/context/skill/hook generation sections, reduce's findings/approval and handoff rules, verify's chaining rules, architect's entry/approval/rejection, upgrade's application/archive/validation, reseed's approval/implementation, rethink's proposal/admission rules, and the platform generator and capture template. These supply implementation or doctrine/design, not observed run evidence. The first portion of `reference/validate-kernel.sh` shows a structural evaluator with sampled dangling-link checks; it does not provide a semantic answer oracle or prove full-vault correctness. No target execution, supplied installed vault, successful run, activation trace or causal comparison was inspected. Benefits, actual continuity and actual model compliance remain unobserved.

## Shared records

### Components

#### RT-CMP-session-model
Label: Session model and Task workers

Source-native identity: the Claude Code session model and inherited subagent model described by ralph; model labels sonnet and opus occur in pipeline and architect metadata. Representational form: distributed-parametric model state. Storage substrate: external provider/host model service, uninspected. These labels do not pin weights, provider or exact model revision. Parameter change during operation is uninspected; no target-side weight update is established by the inspected scheduling procedures. Whether the host's mutable model endpoint resolves to another model is uninspected. The shipped labels and session inheritance leave exact version unpinned at this boundary. SRC-1: `skill-sources/ralph/SKILL.md`, `skill-sources/pipeline/SKILL.md`, `skills/architect/SKILL.md`.

> Subagents inherit the session model. Users running opus get opus quality on processing phases. Users running sonnet get sonnet everywhere. Fresh context per phase already ensures efficiency — every phase gets full capability in the smart zone.
> --- `skill-sources/ralph/SKILL.md`

This is a design assertion about selection and efficiency, not supplied evidence of improved quality or stable weights.

### Operative objects

#### RT-OBJ-queue
Label: Queue phase state

Source-native identity: `ops/queue.yaml`, `ops/queue/queue.yaml` or `ops/queue/queue.json`, selected in that order by ralph. Representational form: symbolic task identifiers, phase order, statuses and file pointers encoded as YAML/JSON; consumed through model interpretation and tool operations, not a compiled scheduler. Storage substrate: vault filesystem, optionally Git. It is distinct from natural-language task-file instructions; the queue points to those files. SRC-1: `skill-sources/ralph/SKILL.md`.

> The queue uses `current_phase` and `completed_phases` per task entry:
> --- `skill-sources/ralph/SKILL.md`

#### RT-OBJ-claude-md
Label: Generated context and skill instructions

Source-native identity: generated `CLAUDE.md` plus separately loaded `.claude/skills/[domain-skill-name]/SKILL.md`. Representational form: natural-language rules, rationale and workflows; metadata has symbolic host-facing fields. Storage substrate: project Markdown files. These are a container of generated instructional surfaces, not a claim that every instruction has the same loading path. Setup composes context from selected feature blocks with model-based vocabulary transformation and exclusion-reference cleanup; separately transformed skill bodies retain quality gates and handoff formats. SRC-1: `skills/setup/SKILL.md`.

> b. Apply vocabulary transformation (Section 9 algorithm -- LLM-based contextual replacement, NOT string find-replace)
> --- `skills/setup/SKILL.md`

### Routes

#### RT-RTE-setup-generation
Label: Setup derivation and generation

Endpoints/progression/owner: a user invokes setup; its model conducts conversation, derives dimensions and vocabulary using bundled guidance, presents a proposal and writes the generated project. The user may override dimensions; the model reruns affected coherence checks. `ops/derivation.md` is persisted first and reread during generation. Effects include context, skills, hooks/settings and optional search wiring; executor is the host's file/shell tools. SRC-1: `skills/setup/SKILL.md`.

- Immediate return: generation summary, validation findings and restart guidance.
- Later read-back: persisted derivation supplies later generation steps and architecture changes; generated instructions are loaded on subsequent sessions/invocations.
- Delegated visibility: uninspected — no executed generation or delegated setup context was supplied.
- Selection predicate: detected platform, user conversation, derived dimensions, active feature blocks and vocabulary determine emitted artifacts.
- Invalidation or expiry: subsequent overrides, reseed or upgrade can replace generated text; skill discovery requires a host restart according to setup.
- Activation or effect: instructions request actual filesystem generation and host loading after restart; neither completed installation nor changed model behavior was observed.
- Evidence limits: prompt procedure plus templates, not generated artifacts or execution evidence; platform generator disagrees about copied skills.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

Admission: the model proposes configuration; the user adjusts or accepts at the proposal stage. This is not per-file human authorship. Operating mode: open conversational derivation with prescribed coherence checks. Answer oracle: no independent expected semantic answer; generated structure is checked against the kernel and coherence requirements. Recovery: derivation-first persistence supports compaction; full rollback of partial generation is not established by the inspected sections. Guidance retained: derivation rationale, selected vocabulary/configuration and composed operating texts. Source support:

> The init wizard runs conversation (Phases 1-4) + generation (Phase 5) + validation (Phase 6) in one session. Phase 5 generates 15+ files, which can exhaust the context window. To survive context compaction:
> --- `skills/setup/SKILL.md`

> 1. Read `${CLAUDE_PLUGIN_ROOT}/skill-sources/[name]/SKILL.md`
> 2. Apply vocabulary transformation — rename and update ALL internal references using the vocabulary mapping from `ops/derivation.md`
> 3. Adjust skill metadata (set `context: fork` for fresh context per invocation)
> 4. Write the transformed SKILL.md to the user's skills directory
> --- `skills/setup/SKILL.md`

#### RT-RTE-source-processing
Label: Serial source-to-note pipeline

Endpoints/progression/owner: requested progression is source path → seed/archive/extract task → reduce → claim/enrichment queue entries → phase workers → batch archive/report. The seed-to-reduce edge is unresolved: pipeline supplies batch/type filters, but seed's YAML and JSON extract-entry templates omit the `batch` and `current_phase` fields required by ralph's filters and phase dispatch. Subsequent steps remain specified conditional on an eligible extraction entry; later reduce-created claim entries cannot repair this initial selection gap. The pipeline model owns outer sequencing; serial ralph owns selection and advancement; Task workers execute note/connection changes. Queue entry identity, batch, phase and task-file path identify work. Workers receive phase instructions and sibling titles, then read the designated task file and skill/context as requested. SRC-1: `skill-sources/pipeline/SKILL.md`, `skill-sources/seed/SKILL.md`, `skill-sources/ralph/SKILL.md`, `skill-sources/reduce/SKILL.md`, `skill-sources/verify/SKILL.md`.

- Immediate return: phase handoffs and progress reports; outer pipeline returns created-note list, quality counts and archive/summary location.
- Later read-back: queue and task sections support later ralph resumption; resulting notes and connections become later vault inputs.
- Delegated visibility: workers receive task identity/path, one phase instruction and selected sibling titles; extraction may add queue entries; lead receives handoff or completion text, not guaranteed complete reasoning.
- Selection predicate: first pending queue entry in array order after batch/type filters; `--batch` requires matching `batch`, `--type` requires matching `current_phase`, and current phase selects the worker procedure. Seed's emitted extract entries do not establish eligibility for pipeline's `/ralph 1 --batch {batch_id} --type extract` request.
- Invalidation or expiry: phase advancement changes eligibility; done entries are later archived/removed; no automatic expiration of resulting notes is established here.
- Activation or effect: requested note creation, enrichment, graph updates, task-section writes and queue advancement; model compliance and downstream knowledge use remain unobserved.
- Evidence limits: no execution; seed-to-extract eligibility is unresolved under the stated filters, not an observed selection failure. Wrapper count versus serial phase count, missing-handoff tolerance and approval versus dontAsk tension also limit end-to-end completion claims.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

Admission/decision roles: seed's duplicate check asks the user before reprocessing; reduce proposes findings and requires approval before creating files, including when handoff adds queue management. The model writes approved content and later workers revise links/notes. Starting pipeline is not demonstrably per-content approval. Verify evaluates cold-read prediction, schema and links; this is model judgment and local structural references, not a semantic truth oracle. Operating mode: open source processing, with config-dependent verification and serial batch/type/dry-run modes. Rejection/recovery: declined duplicate processing stops; outer phase failures stop and report queue state; rerunning ralph is intended to resume at the failed phase; malformed queue must not be auto-repaired. Git is not a transactional rollback of worker side effects. Guidance: domain vocabulary, extraction criteria and note/connection/verification procedures; seed specifies source/task retention, while downstream notes and summary depend on reaching their workers and completion. A model could infer missing fields or special-case extraction, but the inspected instructions do not specify that reconciliation. The workflow finding [WF-CLM-extract-selection](workflow.md#wf-clm-extract-selection) concerns this route's initial eligibility, not a distinct processing route.

SRC-1: `skill-sources/seed/SKILL.md`, `skill-sources/ralph/SKILL.md`, `skill-sources/pipeline/SKILL.md` supply doctrine/design evidence:

> - id: {SOURCE_BASENAME}
>   type: extract
>   status: pending
>   source: "{FINAL_SOURCE}"
>   file: "{SOURCE_BASENAME}.md"
>   created: "{UTC timestamp}"
>   next_claim_start: {NEXT_CLAIM_START}
> --- `skill-sources/seed/SKILL.md`

> Apply filters:
> - If `--batch` specified: keep only tasks where `batch` matches
> - If `--type` specified: keep only tasks where `current_phase` matches (e.g., `--type reflect` finds tasks whose `current_phase` is "reflect")
> --- `skill-sources/ralph/SKILL.md`

> The `current_phase` determines which skill to invoke.
> --- `skill-sources/ralph/SKILL.md`

> The pipeline is the convenience wrapper. /ralph is the engine. /seed is the entry point.
> --- `skill-sources/pipeline/SKILL.md`

> **Wait for user approval before creating files.** Never auto-extract.
> --- `skill-sources/reduce/SKILL.md`

> **Critical:** The handoff mode adds queue management ON TOP of the standard reduce workflow. Do the full extraction workflow first, then create task files, update queue, and output handoff.
> --- `skill-sources/reduce/SKILL.md`

#### RT-RTE-parallel-claims
Label: Parallel full-claim workers

Endpoints/progression/owner: ralph `--parallel` selects pending claims, starts up to five Task workers, waits for every success/error return, then runs one cross-connect worker. Unlike serial scheduling, a worker executes remaining phases and marks its own queue entry done. Workers share filesystem/queue effects; prompt coordination is not an inspected lock implementation. SRC-1: `skill-sources/ralph/SKILL.md`.

- Immediate return: worker note title/path/claim ID, error or learning reports, cross-connect results and final ralph report.
- Later read-back: updated queue permits later resumption; notes/links remain in the vault.
- Delegated visibility: each worker receives sibling target titles/task paths, its current/completed phases and its own task path; not all siblings' completed contents at launch.
- Selection predicate: pending claims, N and concurrency cap five; --type is rejected with --parallel.
- Invalidation or expiry: completed phases are skipped on resumption; changing queue state changes later eligibility.
- Activation or effect: requested end-to-end claim writes and shared queue updates, followed by backward/sibling connection repair.
- Evidence limits: no run, lock protocol or host isolation proof; returning errors satisfies the completion barrier without proving all claims succeeded.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

Decision roles/admission: model workers propose and execute connections using genuineness criteria; the lead interprets returns. No additional per-link human veto is specified in this worker prompt. Answer oracle: no independent expected link set. Mode: bounded concurrent batch processing, not an experimental treatment/comparison. Recovery is prompted phase resumption and reporting of resource conflicts; cleanup says to remove lock files if created, not how locks prevent lost queue writes. Guidance and retained result otherwise follow [RT-RTE-source-processing](#rt-rte-source-processing).

> Read the task file for full context. Execute phases from current_phase onwards.
> If completed_phases is not empty, skip those phases (resumption mode).
> --- `skill-sources/ralph/SKILL.md`

> **Completion gate:** Phase B CANNOT start until ALL spawned workers have reported back (either success or error). Track completions:
> --- `skill-sources/ralph/SKILL.md`

#### RT-RTE-session-orientation
Label: SessionStart state and context injection

Endpoints/progression/owner: registered SessionStart invokes shell orientation in the host working directory, guarded by vault detection. It reads stdin session ID, optionally archives a different previous ID, writes active `current.json`, optionally commits session/goals state, exports session ID, prints tree/goals/identity and recent methodology headers, counts maintenance signals, and invokes an existing project reconcile script. Host owns event delivery; shell owns these file/output effects. SRC-1: `hooks/hooks.json`, `hooks/scripts/session-orient.sh`, `hooks/scripts/vaultguard.sh`.

- Immediate return: stdout supplies workspace/context/maintenance text to the conversation; state writes and optional Git commit also occur.
- Later read-back: goals, identity and up to five recently modified methodology files' first three lines are printed on later starts; prior session records are archived but current.json can already have been overwritten before printing.
- Delegated visibility: uninspected — whether host Task workers inherit this hook output is outside the source.
- Selection predicate: detected vault; session_capture/git flags; file existence; modification order for methodology; count thresholds for suggested maintenance.
- Invalidation or expiry: current session state is overwritten on enabled tracking; previous differing ID is timestamp-archived; no expiry of retained records is specified.
- Activation or effect: executable output and file effects are wired; actual host delivery or consequent model action is unobserved.
- Evidence limits: hook registration is not a run; injected methodology is a header excerpt, not the full directive body; capture template and plugin are separate deployments.
- implementation conclusion status: wired
- operation conclusion status: uninspected

The generated Stop template writes only ID/end time/status, copies that record to current.json and commits selected directories. It does not itself retain a conversation transcript. Consequently comments calling its result a mining target do not establish transcript availability. SRC-1: `platforms/claude-code/hooks/session-capture.sh.template`.

> for f in $(ls -t ops/methodology/*.md 2>/dev/null | head -5); do
>   head -3 "$f"
> done
> --- `hooks/scripts/session-orient.sh`

#### RT-RTE-write-hooks
Label: Post-Write warnings and async Git persistence

Endpoints/progression/owner: matching host Write event → guarded schema-warning script and async auto-commit. Validator extracts tool_input.file_path and tests file existence, hard-coded notes/thinking path, first-line delimiter and first-20-line description/topics presence. It emits additionalContext but always exits zero. Commit hook changes to project directory, checks guard/config/Git, stages all changes and attempts commit. SRC-1: `hooks/hooks.json`, `hooks/scripts/write-validate.sh`, `hooks/scripts/auto-commit.sh`.

- Immediate return: validation warning JSON when checks fail; async persistence has no dependable task-specific return.
- Later read-back: committed files remain available to future vault work; warnings alone are not a retained revised directive.
- Delegated visibility: uninspected — host handling of worker Write events and warning injection was not inspected.
- Selection predicate: Write matcher; vault guard; file/path presence and limited note paths for warnings; git configuration and repository state for committing.
- Invalidation or expiry: future edits supersede content; Git retains committed history, subject to user repository management.
- Activation or effect: post-effect warnings and broad staging/commit attempt are wired, not a pre-write rejection gate.
- Evidence limits: no run; Edit/Bash writes do not match this registration; commit failure can be swallowed and concurrent async invocations have no inspected transaction protocol.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: no per-content human approval occurs in these scripts; they diagnose limited shape and persist whatever is already pending. The vault guard can itself rewrite old marker formats or create a marker for legacy config/hook detection. Oracle: grep presence tests, not full YAML parsing or semantic judgment. Mode: automatic host callback. Rejection/rollback: invalid content is not rejected or undone; Git history is an available substrate, not automatic recovery. SRC-1: `hooks/scripts/vaultguard.sh`.

> # Async hooks don't reliably receive tool input — commit all pending changes.
> --- `hooks/scripts/auto-commit.sh`

> git commit -m "$MSG" --no-verify 2>/dev/null || true
> --- `hooks/scripts/auto-commit.sh`

#### RT-RTE-architecture-evolution
Label: Evidence-based architecture proposals

Endpoints/progression/owner: user invokes rethink or architect (or follows a maintenance signal); model reads retained design/configuration, operational evidence and methodology, proposes specific file changes, human approves/selects/modifies/declines, model implements and logs changes. Architect uses health/friction/research and rank-by-impact-to-effort; rethink quotes challenged assumptions and scales proposal scope with evidence. These are related proposal paths, not the same command. Reseed is the larger alternative: drift → re-derivation proposal → approval → archived derivation, folder/schema/context/skill/hook/navigation changes → validation. SRC-1: `skill-sources/rethink/SKILL.md`, `skills/architect/SKILL.md`, `skills/reseed/SKILL.md`.

- Immediate return: proposals, evidence, risks and approval dialog; after approval, before/after changes and validation results.
- Later read-back: updated context/skills/configuration, derivation rationale and changelog can inform later operations; feeding observations receive resolution references.
- Delegated visibility: uninspected — no executed delegation or generated context was supplied.
- Selection predicate: operational patterns, challenged assumptions and research backing; human selects recommendations; reseed triggered by systemic drift or explicit request.
- Invalidation or expiry: rejected recommendations are deferred and must not be re-proposed without new evidence; later revisions replace instructions.
- Activation or effect: requested changes to behavior-determining project instructions and architecture, not established exercised behavioral improvement.
- Evidence limits: prompt policy; human approval and downstream compliance unobserved; no causal outcome comparison supplied.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

Admission: model proposes and performs computational diagnosis; human decides and can veto implementation. Rethink also requires confirmation before triage execution. Architect post-change checks include links/schema/navigation/session orientation. Reseed records per-change rollback plans, archives derivation, uses Git moves and preserves self/memory; neither provides a demonstrated atomic rollback. Guidance: bundled methodology/research and retained operational evidence; retained outputs: literal revised files, evidence/risk/rationale logs, and resolution references. Answer oracle: local structural contracts plus model assessment; research references are guidance, not independently supplied correct answers. Operating mode: open diagnosis/revision; not a causal experiment or bounded curriculum.

> **NEVER auto-implement proposals.** Changes to system assumptions require human judgment. This is the invariant that makes rethink safe — it can analyze aggressively because it cannot act unilaterally.
> --- `skill-sources/rethink/SKILL.md`

> Current assumption:
>     [Quote the specific section of context file, skill, or template
>      that embodies the assumption being challenged.
>      Include the file path and section heading.]
> --- `skill-sources/rethink/SKILL.md`

Theory account: the subject is the generated system's explicit operating assumptions. Rethink asks for a named challenged assumption, evidence, expected benefit, risks and literal successor content. Architect likewise treats workflows as design choices to test against operational records. The procedure requests localized criticism and later retention, rather than merely selecting variants by a score. This establishes a specified criticism path, not successful criticism in a run.

theory-builder conditions 1–4:

- condition 1 conclusion status: claimed
  Localized assumption passages are required.
- condition 2 conclusion status: claimed
  Proposal scope/content is requested to depend on those assumptions and operational evidence.
- condition 3 conclusion status: claimed
  Challenged placement, evidence and revision are requested, but performed blame assignment is unobserved.
- condition 4 conclusion status: claimed
  Changes/rationale/resolution are retained for later rounds, but their actual next-round influence is unobserved.
- Addressability: specified at file/section and quoted-assumption granularity; actual generated assumptions may be less separable, uninspected.
- Persistence: instructed across problems/sessions through operating files, derivation and changelog; realized horizon unobserved.
- learning: uninspected — future capacity improvement and attribution cannot be established from this procedure without outcome evidence.
- Reflection: claimed — config/context and methodology represent system operation; drift evidence can update that representation and approved representation changes can reach later behavior. Neither causal direction was observed in operation.
- Reflective theory builder: claimed — the specified method-criticism loop uses its own operational records; execution of conditions 1–4 is unobserved.
- Autonomous theory builder: human veto/selection is an internal admission step in the described route; computational performance of every internal operation is not established.

Self-improvement attribution, narrowly scoped to the generated operating system across future sessions: the objective is reducing named operational friction/quality failures, independently of any particular file change. There is a claimed, dormant pathway from evidence to proposed change, approved instruction change and future context/skill consumption. None of the four causal links is demonstrated in a run, particularly subsequent operation causally depending on the update. This supports only an attributed improvement-directed self-change design, not exercised or successful self-improvement.

#### RT-RTE-skill-upgrade
Label: Approved skill replacement with archive

Endpoints/progression/owner: upgrade compares installed skill methodology with bundled guidance, presents a plan, waits for approval, archives current versions, generates approved successors, updates version/manifests and validates references/vocabulary/handoffs. User-modified skills receive preservation/merge choices. Executor: model with host file/shell tools. SRC-1: `skills/upgrade/SKILL.md`.

- Immediate return: plan/selection dialog, then applied/skipped/archive counts and validation findings.
- Later read-back: revised SKILL.md instructions govern later invocations; generation manifest records versions/source/changes.
- Delegated visibility: uninspected — no executed delegated upgrade or worker consumption was supplied.
- Selection predicate: identified upgrades and explicit user selection; vocabulary, dimensional positions and selected customizations constrain generation.
- Invalidation or expiry: approved successor replaces live skill; previous skill copied to date-labelled archive, with no inspected archive expiration.
- Activation or effect: requested replacement of capability instructions, not model-weight modification or proven activation.
- Evidence limits: archival/validation are prompt-directed shell examples, not observed backups or compatibility tests.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

Admission/decision roles: model detects and drafts; human approves, selects or keeps user modifications. Operating mode: open advisory improvement, not controlled experiment. Oracle: structural existence/reference/vocabulary/handoff checks; no reference answer for methodology quality. Rejection/rollback: unapproved changes are skipped; archived files support explicitly manual rollback if validation fails. Guidance retained: transformed methodology plus version and change metadata. This path differs from purported automatic plugin-wide inheritance in the platform generator.

> Wait for user response. Do NOT proceed without explicit approval.
> --- `skills/upgrade/SKILL.md`

> Previous versions available in ops/skills-archive/
>   for manual rollback.
> --- `skills/upgrade/SKILL.md`

### Claims

#### RT-CLM-completion-gate
Label: Completion versus verification success

Claimed operation: verify says a failed note must remain at verify; outer pipeline must not archive pending tasks. Serial ralph nevertheless advances after evaluating a return, tolerates missing handoff and merely warns about empty task sections. These instructions do not warrant a hard semantic gate linking success to advancement. SRC-1: `skill-sources/verify/SKILL.md`, `skill-sources/ralph/SKILL.md`, `skill-sources/pipeline/SKILL.md`.

> If verification FAILS (recite score < 3 or any FAIL-level issue), do NOT mark done. Instead:
> - Output what failed and what needs fixing
> - Keep task at `current_phase: "verify"` for re-run after fixes
> --- `skill-sources/verify/SKILL.md`

> Every subagent SHOULD return a RALPH HANDOFF block. If missing: log warning, mark task done, continue.
> --- `skill-sources/ralph/SKILL.md`

- implementation conclusion status: claimed
- operation conclusion status: uninspected

Supported consequence: inspect task/verification results rather than treating done as sufficient evidence of quality; this is an instruction conflict, not an observed corrupt queue.

#### RT-CLM-generation-paths
Label: Copied versus inherited processing skills

Claimed operation: setup copies transformed skills to the user's project, while the platform generator says they are inherited and receive plugin updates without regeneration. These imply materially different update-admission and freshness paths. The inspected checkout does not reconcile them; actual deployed selection remains unobserved. SRC-1: `skills/setup/SKILL.md`, `platforms/claude-code/generator.md`; [RT-RTE-setup-generation](#rt-rte-setup-generation), [RT-RTE-skill-upgrade](#rt-rte-skill-upgrade).

> Processing skills (/reduce, /reflect, /reweave, /verify, /validate) are inherited from the plugin's `skills/` directory -- they are NOT copied to user projects. Skills read `ops/derivation-manifest.md` at runtime for domain vocabulary transformation, so a therapy system's `/surface` resolves to the canonical `/reduce` skill automatically.
> --- `platforms/claude-code/generator.md`

- implementation conclusion status: claimed
- operation conclusion status: uninspected

Automatic update reach cannot be asserted for installed copied skills from this platform paragraph alone.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-context-instructions
Label: Project instruction authority

Consumer: host-loaded session model and invoked skill workers. Channel: generated CLAUDE.md/session context and separate skill loading; SessionStart stdout provides an additional, narrower retained-content channel. Force: natural-language operating guidance mediated by model interpretation, not a filesystem invariant. Horizon: later sessions and skill invocations while live project files remain selected. The host loading contract is external; delivery does not establish compliance. SRC-1: `platforms/claude-code/generator.md`, `skills/setup/SKILL.md`, `hooks/scripts/session-orient.sh`.

> The primary context file, auto-loaded at every session start. Composed from selected feature blocks (see `platforms/shared/features/`) with domain vocabulary applied. Contains:
> --- `platforms/claude-code/generator.md`

The session hook does not deliver full methodology directives merely by printing their first three lines. Later full-body consumption is requested by meta-skills, not guaranteed by this excerpt channel. Explicit remember treats newly written methodology as specification; contextual remember additionally waits for human confirmation. That admission distinction prevents interpreting architecture approval as a universal gate on behavior-shaping guidance. SRC-1: `skill-sources/remember/SKILL.md`.

> **Wait for user confirmation.** Do not create notes from inferred corrections without approval — the agent might misinterpret what the user meant.
> --- `skill-sources/remember/SKILL.md`

## Annotations

none
