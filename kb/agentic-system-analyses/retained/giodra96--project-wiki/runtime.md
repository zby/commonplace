---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Project Wiki runtime baseline: host-interpreted project-memory workflows, deterministic intake helpers and bounded controls at the frozen commit."
run-id: AAS-2026-11-08-project-wiki-b055e5c71dc7-01
reviewed-boundary: "3af1e28d0a3ed3daeb9f923102cd5cefb51b0f41"
---

# Project Wiki runtime report

## Runtime account

### What runs, and who owns the next step

Project Wiki supplies instructions and local Python helpers, not a model-serving agent runtime. Its claimed work is durable, traceable project memory beside source code. A host coding agent interprets the request, loads the skill, chooses a workflow, calls helpers, reads results, makes semantic decisions and writes canonical records. The Python programs implement structural and byte-level operations; they do not drive the whole semantic loop. The host owns continuation after each helper return. The claimed automatic behavior is therefore conditional on host instruction loading and adherence, not a scheduler supplied by this repository (SRC-1, `README.md`, `SKILL.md`; [RT-CLM-project-memory](#rt-clm-project-memory)).

The shipped entry surface is an agent skill: `init`, `scan`, `update`, `sync`, `maintain`, `config` and `help`, plus ordinary coding-task preflight and post-implementation updates. Slash commands are invocation hints, not a central executable dispatcher. Help is routed before preflight, calls `wiki_help.py` without positional arguments and returns the bundled English guide verbatim; the helper reads only its packaged guide and errors if unavailable or empty. Configuration reads/changes only a project preference file and does not itself synchronize documentation. These exceptional returns matter: neither is an ordinary wiki-content edit requiring reconciliation or audit logging (SRC-1, `SKILL.md`, `scripts/wiki_help.py`, `references/configuration.md`, `scripts/wiki_config.py`).

Semantic execution is through an externally supplied model ([RT-CMP-host-agent](#rt-cmp-host-agent)). Workflow bodies are natural language; CLI options, IDs, YAML contracts and validation rules are symbolic ([RT-OBJ-skill](#rt-obj-skill), [RT-OBJ-project-wiki](#rt-obj-project-wiki)). The current grant set is not supplied: supported hosts can read/write repository files and run helpers, but this does not prove any deployed host's shell permissions, approval settings or isolation. The skill requests two instruction blocks outside `.project-wiki/`, so a grant limited to that directory would not complete bootstrap. There is no basis here for attributing provider controls, subprocess isolation or host extensions to Project Wiki. Python dependencies and Git execute under the host's permissions (SRC-1, `README.md`, `references/initialization-workflows.md`, `scripts/requirements.txt`, `scripts/wiki_scope.py`).

### Ordinary invocation, end to end

Assume initialization has completed and the user asks the coding agent to modify an API. The prescribed trigger is an existing `.project-wiki/INDEX.md` plus a code-related task. The foreground agent reads the root index, obtains effective configuration, chooses the relevant section index and linked pages, and uses registry/traceability fallback only if needed. It summarizes relevant facts and proceeds with the requested coding work. The decision policy is a task-relative natural-language routing procedure, not vector retrieval or a deterministic relevance score. Task state resides in the host context; persistent inputs are repository Markdown/YAML. The source helper supplies filtered source reads/search/diffs, not an isolated executor of the coding task (SRC-1, `references/automatic-workflows.md`, `SKILL.md`; [RT-RTE-coding-cycle](#rt-rte-coding-cycle)).

After agent-made source changes, the foreground agent refreshes possibly changed configuration, then decides whether the coherent task changed durable knowledge, evidence, recorded work state, a wiki claim or an open question. It updates only affected records and required catalog/routing/traceability metadata, reconciles questions and logs meaningful changes. Observed implementation belongs in `technical/`; confirmed product intent is required before treating a behavior as a requirement. Terminal output names wiki files updated alongside code changes. A no-impact decision returns without metadata churn or skip logging. Disabled/invalid automatic configuration stops even the impact assessment, but not context preflight or the requested code work (SRC-1, `references/automatic-workflows.md`, `references/configuration.md`).

This loop returns later to the stored wiki through generated always-on instructions ([RT-BAP-project-protocol](#rt-bap-project-protocol)). It is a designed cross-session read-back path, not supplied evidence that a host exercised it. Selection happens before loading pages; there is no inspected host-window trimming or compaction implementation here. Reusing already-read, still-current pages limits redundant loading. Intake review additionally offers source-section views; these are selective reads into the same agent context, not subagent frames. `view --all` remains a potentially large full-document path. Source preservation and a reload helper do not imply that the host evicts earlier context or enforces a token budget (SRC-1, `references/automatic-workflows.md`, `references/document-ingestion.md`, `scripts/review_progress.py`).

### Material alternate paths and change admission

* Initialization/scan generates a validated scaffold, then the host captures project identity or repository findings and installs the two always-on instruction blocks. Structural generation alone explicitly reports incomplete semantic initialization ([RT-RTE-initialize-wiki](#rt-rte-initialize-wiki)).
* Pasted notes and durable answers bypass document extraction and chunk-ledger review. The agent classifies them directly, with question reconciliation and evidence/intent rules; automatic answer filing shares the write gate, explicit update does not ([RT-RTE-note-update](#rt-rte-note-update)).
* External document intake runs inbox preflight when applicable, snapshot extraction, complete chunk disposition, comparison against existing wiki state, direct conservative integration or a narrowly scoped human decision, then audit/validation and lifecycle updates ([RT-RTE-source-intake](#rt-rte-source-intake)).
* Explicit sync examines external/accumulated changes, including committed changes from a documented baseline. Maintain validates, migrates and semantically checks retained material; it requests confirmation for high-impact canonical meaning changes. Neither is reduced by the automatic-write toggle ([RT-RTE-explicit-reconcile](#rt-rte-explicit-reconcile)).

Knowledge admission is thus distributed across agent judgments, deterministic structural checks and conditional human approval. Starting `update` authorizes conservative integration; it is not human approval of every resulting assertion. Human review is reserved for the blocking decisions enumerated in the intake workflow or high-impact maintenance changes. No inspected route modifies model weights. Bootstrap and maintenance can replace the marked behavioral instruction blocks; schema migration can alter the wiki's structure and version metadata. These are separate from improving the installed skill's own code. CI runs helper tests and schema-contract drift checking, but no supplied run demonstrates admission of a new production skill version or model capability (SRC-1, `references/document-ingestion.md`, `references/maintenance-workflows.md`, `.github/workflows/tests.yml`).

### Load-bearing guarantees and challenges

The following are bounded controls, not a system-wide safety envelope. Three forcing cases were traced through consumers, rather than inferred from labels.

**1. Automatic writes disabled or invalid.** Owner: foreground agent, supported by `wiki_config.py`. Enforcement point for type/shape validity is `validate_config` plus strict duplicate-key YAML loading; the CLI returns effective JSON or exit 2 with an instruction to suspend automatic writes. Enforcement of the write decision itself is natural-language policy in automatic workflows and generated blocks. Missing files deliberately default to enabled; false and invalid values suspend automatic assessment/writes but retain preflight. Explicit `sync`, `update`, `maintain`, user overrides and direct helper calls remain reachable alternatives, not prohibited writes. `ingest_document.py` does not consume this option; it is not a universal write lock. Required external contract: the host must read the setting and honor its scope (SRC-1, `scripts/wiki_config.py`, `scripts/schema_contract.py`, `references/configuration.md`, `assets/core-templates.md`).

- Guarantee strength: policy
- implementation conclusion status: wired
- operation conclusion status: uninspected

**2. Source exclusions.** Owner: source helpers, with host adherence required to avoid raw alternative reads. Enforcement point: `WikiScope` prunes excluded directories, checks lexical and resolved targets on `read_source`, and filters candidate filenames before generating a no-renames Git diff. The search branch calls `read_source`; it does not merely filter displayed filenames. External aliases are suppressed by `read_source`. Intake checks both lexical and resolved in-repository source paths; however its supported positional local-file input can resolve outside the repository, where those conditional ignore checks do not apply. That is a different supported intake shape, not proof of a host permission bypass. Existing extracted history remains readable, and raw host filesystem access is not mediated. Thus the bounded guarantee is source filtering on named helper paths, not secrecy, deletion of earlier knowledge or a filesystem sandbox. Required external contracts include Git's matcher/diff behavior and host use of the helpers (SRC-1, `scripts/wiki_scope.py`, `scripts/ingest_document.py`, `scripts/check_inbox.py`, `references/repository-scope.md`).

> These helpers govern wiki source access, not filesystem permissions or unrelated coding work.
> --- `references/repository-scope.md`

- Guarantee strength: invariant
- implementation conclusion status: wired
- operation conclusion status: uninspected

**3. Review completion and audit digest.** Owner: review helper/validator for structural facts, agent for review and final mutation. `view` loads validated extraction data and emits complete selected text; `apply` accepts classifications and skip reasons and calculates completion without requiring proof of prior viewing. `audit` compares an optional digest to exact ledger bytes, checks ledger state and returns immediately; unlike `view` it does not load the full intake snapshot. An incomplete ledger produces `review-incomplete` rather than necessarily a nonzero exit. The caller must inspect the status, not only command success. The validator checks complete coverage for `reviewed`/`integrated`, registered integrated targets and bidirectional atomic requirement-evidence edges. None of these checks proves that classifications or canonical claims accurately reflect source meaning. The final intake status is changed by the agent after the audit, not atomically by that read-only checkpoint, so the digest does not lock later writes (SRC-1, `scripts/review_progress.py`, `scripts/validate_wiki.py`, `references/document-ingestion.md`).

> if args.command == "audit":
>     validate_ledger_state(ledger, contract)
>     print_audit(build_ledger_audit(args.intake_id, ledger, ledger_sha256), args.format)
>     return 0
> --- `scripts/review_progress.py`

- Guarantee strength: protocol
- implementation conclusion status: wired
- operation conclusion status: uninspected

Additional local transactional controls have narrower effects. Scaffold publication validates same-filesystem staging, uses platform-specific exclusive publication and refuses an unsupported unsafe fallback. It cannot establish semantic completion or authorize later host edits. Intake snapshots source bytes, optionally checks the preflight hash, extracts and optionally copies that snapshot, checks snapshot/source consistency, validates staged artifacts, renames the directory and updates the index. Failure cleanup removes staged and newly published incomplete output. Unlike scaffold publication, intake uses `Path.rename` after existence checks; this inspection does not establish an equivalent concurrent no-replace guarantee. Its optional `--expected-sha256` is mandatory by inbox protocol, not by the general extraction CLI. Direct explicit document intake is therefore not covered by inbox deduplication merely because it shares extraction code (SRC-1, `scripts/wiki_scaffold.py`, `scripts/ingest_document.py`; [RT-RTE-initialize-wiki](#rt-rte-initialize-wiki), [RT-RTE-source-intake](#rt-rte-source-intake)).

### Evidence and coverage limits

All source findings use SRC-1 at the boundary commit. Added depth includes the helper control flow for configuration and duplicate-key loading; source list/read/search/diff; ingestion arguments, hash/staging/publication and format dispatch; review inspect/view/apply/audit; scaffold exclusive publication; validator completion/evidence checks; help; schema state/action maps; and generated protocol blocks. These are implementation evidence. Routed procedures and templates are doctrine/design evidence. The CI workflow describes automated checks of helpers, not supplied successful CI results or a model-task evaluation (SRC-1, `.github/workflows/tests.yml`).

No target code, tests, fixtures, provider calls or examples were executed. No observed run or experiment was supplied. Model compliance, cross-session activation, semantic accuracy, speed and benefits remain unobserved. Dependency internals, host callbacks/extensions, shell approval, provider-native tools, remote workers, actual parallel edit coordination and context-window policies are outside the supplied host evidence; this prevents attributing control over them to the skill. Detailed memory transformation and epistemic assessments belong to the later members, not an inferred universal absence from this runtime account.

## Shared records

### Components

#### RT-CMP-host-agent
Label: Host coding agent

The external host agent supplies model-dependent interpretation, semantic classification, task relevance judgments, canonical writing and user interaction. Its model is a distributed-parametric component; the repository supplies no parameter storage or provider implementation. Exact model version pinning: uninspected — no deployed host/model configuration is supplied. Parameter changes during operation: uninspected — no provider implementation or run evidence is supplied. Mutable endpoint resolving to another model: uninspected — endpoint identity is not specified. These limits do not imply fixed weights, online weight learning or absent learning through retained text. The host's ordinary context and persistence implementation are external, while repository-file consumers are prescribed by the skill (SRC-1, `README.md`, `SKILL.md`).

> Project Wiki is an IDE-neutral agent skill for creating and maintaining an agent-readable knowledge base in `.project-wiki/`. It works with chat-based coding agents such as GitHub Copilot in VS Code, Claude Code, Antigravity, Codex, Cursor, and other compatible tools that can read and write repository files.
> --- `README.md`

### Operative objects

#### RT-OBJ-skill
Label: SKILL and workflow references

Source-native entry is `SKILL.md`, stored with Markdown reference procedures in the installed/repository skill directory. Representational form: natural-language operational instructions interpreted by the host, with symbolic path and CLI identifiers embedded. It selects modes, limits context loading, delegates byte-level work to helpers and supplies admission policy. This is the shipped driver, not accumulated project memory; generated project instruction blocks are a distinct downstream authority surface. Evidence: SRC-1, `SKILL.md`, `references/automatic-workflows.md`, `references/document-ingestion.md`.

> Select one primary mode for an explicit wiki request and load only its workflow:
> --- `SKILL.md`

> Follow the selected workflow completely. Prefer the supplied deterministic scripts over reproducing structural, validation, duplicate, extraction, or ledger logic in model reasoning.
> --- `SKILL.md`

#### RT-OBJ-project-wiki
Label: project-wiki schema contract

The machine contract is `schema/project-wiki.yml`, a symbolic YAML file consumed through `schema_contract.py`. It defines schema version 1.7.0, artifact names, review states, complete dispositions, classification names, canonical paths, source reason/action mapping and template contracts. Fixed consumers validate and render against these fields; human references explain but are not an independent schema source. This record refers to the shipped contract, not to a consuming project's retained wiki contents (SRC-1, `schema/project-wiki.yml`, `scripts/schema_contract.py`, `references/maintenance-workflows.md`).

> complete_entry_statuses:
>   - classified
>   - skipped
> --- `schema/project-wiki.yml`

> historical-path-with-new-content: review
> ambiguous-processable-history: review
> --- `schema/project-wiki.yml`

### Routes

#### RT-RTE-initialize-wiki
Label: Initialize or scan wiki

The user triggers init/scan; the host invokes `wiki_scaffold.py create` only for an absent wiki, then continues semantic initialization or source scan. Scaffold code loads contracts/templates, validates staging and publishes exclusively. The host supplies identity, confirmed/inferred/unknown findings, registry/status, traceability and baseline audit; it preserves placeholder/unknown state until evidence exists. It also installs marked blocks in both root instruction files. Scan reads only included sources and migrates older wikis before new scan artifacts. The output report is explicitly structural, not completed project understanding (SRC-1, `references/initialization-workflows.md`, `scripts/wiki_scaffold.py`).

- Immediate return: scaffold report and host summary of initialized/scanned files and unresolved project questions.
- Later read-back: generated wiki routes and instructions direct future tasks to project records.
- Delegated visibility: inapplicable — no separate worker invocation is specified; the host calls local helpers.
- Selection predicate: explicit init/scan; source scope and targeted repository evidence determine scan inputs.
- Invalidation or expiry: existing wikis use maintenance/migration, never mechanical scaffold merge; findings retain uncertainty until revised.
- Activation or effect: local directory publication is implemented; later semantic capture and instruction installation are prescribed host writes, not observed execution.
- Evidence limits: no initialized project or host trace was supplied; platform syscall behavior is an external contract.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: the user requests setup; code rejects occupied targets and invalid scaffolds, while the host chooses project-specific content. No answer oracle is supplied; source inspection is evidence, not a reference expected answer. Operating mode is an open project task, not a controlled experiment. Recovery removes staging on helper failure and routes existing/legacy state to maintain; migration preserves authored content and requests confirmation for risky actions. No semantic whole-wiki transaction is specified.

> "project_initialization_complete": False,
> "semantic_content_captured": False,
> --- `scripts/wiki_scaffold.py`

> exclusive directory publication is unavailable on {system}; refusing unsafe fallback
> --- `scripts/wiki_scaffold.py:480-480`

#### RT-RTE-coding-cycle
Label: Automatic coding task cycle

An existing index and ordinary code-related request trigger the foreground agent's preflight. Index-to-section-to-page routing, configuration, current source inspection, coding and post-change impact assessment lead to affected wiki writes or a no-write return. The host owns semantic selection and execution; no helper centrally controls the full loop. Guidance differentiates observed implementation from confirmed product intent and applies updates once per coherent task (SRC-1, `references/automatic-workflows.md`, `references/configuration.md`, `assets/core-templates.md`).

- Immediate return: relevant wiki facts before work; final coding response includes wiki files updated, or disabled auto-sync/remaining impact uncertainty where applicable.
- Later read-back: persistent affected records and routing/catalog metadata are available through subsequent preflight.
- Delegated visibility: inapplicable — this procedure specifies foreground-agent work, not delegated context frames.
- Selection predicate: task relevance first; writes require enabled/overridden gate and durable knowledge, evidence or recorded work-state impact.
- Invalidation or expiry: refresh changed configuration and relevant evidence; invalidated claims require affected-record correction, with sync/maintain recovery for missed drift.
- Activation or effect: instructions request use of selected context and durable corrections; neither actual compliance nor benefit is observed.
- Evidence limits: host context eviction, instruction priority and semantic correctness are not established by shipped policy.
- implementation conclusion status: afforded
- operation conclusion status: uninspected

Admission: the host proposes and admits automatic knowledge changes subject to preference and semantic impact policy. The user can disable/override automation; initiating a coding task is not per-content approval. No answer oracle is supplied. The mode is ordinary open-ended coding, not benchmark-driven improvement. Meaningful changes persist as project records and audit entries, not model parameters. Explicit sync/maintain recover drift; no automatic rollback of a semantic write set is shown.

> With `automation.auto_sync: false` or invalid configuration, stop before step 1: skip the assessment and all automatic wiki writes and logs. Explicit wiki requests remain available.
> --- `references/automatic-workflows.md`

> If the assessment establishes that none applies, stop here: do not load broader wiki context, edit metadata, or log the skip.
> --- `references/automatic-workflows.md`

#### RT-RTE-note-update
Label: Notes and durable answers

An explicit update supplies pasted notes or planning conversation; the host checks inbox first, routes explicit documents to intake, then classifies useful notes into requirements, CRs, decisions, technical documentation, work items, questions, glossary or status. It reconciles existing questions, checks whether plans changed, writes appropriate records, links IDs/evidence and updates affected registry/traceability/log state. Durable answer filing prefers existing canonical files; significant non-canonical synthesis can enter `analysis/`, but routine chat does not (SRC-1, `references/update-workflows.md`, `references/common-policies.md`).

- Immediate return: list of updates and unresolved ambiguities.
- Later read-back: canonical records or linked durable analysis are selected in future tasks through indexes/registry.
- Delegated visibility: inapplicable — classification and writing are host-agent responsibilities without a specified worker handoff.
- Selection predicate: useful explicit notes or lasting-value answers; automatic filing additionally requires the write gate.
- Invalidation or expiry: preserve history and stable IDs; reconcile affected questions and update affected records rather than silently replace original intent.
- Activation or effect: direct file-edit procedure is afforded; later use and semantic correctness are unobserved.
- Evidence limits: pasted notes do not receive the document chunk-ledger control; host compliance is not supplied.
- implementation conclusion status: afforded
- operation conclusion status: uninspected

Admission: the agent interprets user-supplied content and chooses representation; explicit update authorizes conservative integration, not arbitrary changes to confirmed intent. Human decisions remain necessary where the intake blocking policy applies. No expected-answer oracle is supplied. The operating mode is an open update/question task. Guidance persists project facts, analysis, questions and audit history. Corrections use reconciliation and history preservation, not an implemented atomic semantic rollback.

> Do not file routine chat answers, generic explanations, transient debugging notes, duplicated content, or unapproved speculation.
> --- `references/update-workflows.md`

#### RT-RTE-source-intake
Label: Source preflight and intake

Explicit update with local documents or discovered inbox files triggers this path. `check_inbox.py` loads and validates registry/intake history before discovering/hash-classifying included sources; its reason/action mapping determines process/skip/review. Quarantine rechecks skip hashes, moves duplicates and attempts reverse moves on failure; registry lifecycle remains the agent's responsibility. Authorized inbox ingestion passes `--expected-sha256`; direct explicit file ingestion supports omission of that option. Extraction uses PDF text, DOCX paragraphs/tables or text/Markdown; unsupported/unextractable input errors instead of inventing content. Snapshot-based generation publishes provenance, chunk files and a pending ledger. The host then uses inspect/view, classifies every chunk, compares candidates with canonical state and records dispositions through apply (SRC-1, `scripts/check_inbox.py`, `scripts/ingest_document.py`, `scripts/review_progress.py`, `references/source-inbox.md`, `references/document-ingestion.md`).

- Immediate return: preflight decisions, extraction location/report, complete selected source text, review summary and audit digest; host reports integration or the exact blocking decision.
- Later read-back: mutable ledger/checkpoint state supports resumed review; integrated canonical results support later normal tasks, while terminal intake is provenance-only except explicit investigation.
- Delegated visibility: inapplicable — helpers return source/structural data to the same host; no remote semantic reviewer is specified.
- Selection predicate: process action or resolved review/reprocessing override; then all reliable source sections or full document, with selected chunks reserved by policy for rereading.
- Invalidation or expiry: changed preflight hash requires rerunning preflight; changed ledger digest requires reaudit; materially bad extraction is rejected/superseded and regenerated before integration.
- Activation or effect: helpers implement artifact and ledger writes; the host admits canonical knowledge and mutates final status under a procedural audit/validation gate.
- Evidence limits: neither final ledger disposition nor valid target edges proves faithful reading or source entailment; source execution and later use are unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: code owns byte-level duplicate and structure decisions; the agent proposes classifications/canonical writes and normally integrates directly. A human decides only blocking authority/scope/baseline/binding choices or requested review-only work; a resolved decision resumes the same integration once. No answer oracle is supplied; model judgment against source and wiki state is not one. Operating mode is open document integration. Persisted guidance/results include provenance, chunk-to-record edges, canonical records, optional decision-focused review and audit evidence. Failure cleanup covers helper publication, not the entire multi-file semantic update. Agent policies require rejection/supersession or canonical correction plus audit when extraction is bad.

> An explicit `update` request authorizes conservative canonical integration of supplied information and processable inbox sources unless the user asks for review-only output.
> --- `references/document-ingestion.md`

> expected_source_hash = args.expected_sha256.lower() if args.expected_sha256 else None
> --- `scripts/ingest_document.py`

> if status == "classified" and not classifications:
>     raise ReviewProgressError(f"classified update for {chunk_id} requires classifications")
> --- `scripts/review_progress.py`

> if intake_status in {"reviewed", "integrated"} and not all_complete:
>     self.add("error", "intake-review-progress-incomplete", progress_relative, f"Intake status '{intake_status}' requires complete chunk review coverage.")
> --- `scripts/validate_wiki.py`

#### RT-RTE-explicit-reconcile
Label: Explicit sync and maintain

User-requested sync reconciles current included code with stored claims; maintain migrates structure, runs deterministic validation before semantic lint and checks stale claims, contradictions, questions, alerts and relationships. These are distinct branches sharing explicit authorization independent of auto-sync. The host owns progress and semantic decisions. Sync uses a reliable documented/user baseline including committed changes, or compares included source with documentation when none exists; maintain records validator status and reviewed scope (SRC-1, `references/synchronization-workflow.md`, `references/maintenance-workflows.md`, `scripts/validate_wiki.py`).

- Immediate return: synchronization or maintenance result, reviewed scope, structural findings and unresolved semantic decisions.
- Later read-back: revised records, migration/lint reports, status and audit entries inform subsequent work and checks.
- Delegated visibility: inapplicable — deterministic validation reports to the host, which performs semantic lint.
- Selection predicate: explicit sync/maintain; affected included sources for sync, structural coverage then context-sensitive semantic checks for maintain.
- Invalidation or expiry: current evidence can supersede stale claims; migration updates version only after success and preserves authored content/history.
- Activation or effect: validator reports deterministic findings; host revisions and renewed instruction blocks are prescribed rather than observed.
- Evidence limits: validation cannot determine semantic adequacy; a clean diff without a reliable baseline cannot establish freshness.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: low-risk structural fixes are applied directly; high-impact contradictions, canonical meaning changes and risky migration actions require user confirmation. Code can reject structural validity, while the human can withhold consequential semantic changes. No expected-answer oracle is supplied. The mode is an open audit/reconciliation request; drift and schema mismatch trigger proposed changes, not a measured curriculum. Persisted results are corrected project records, evidence-linked findings, migration metadata and marked protocol blocks. Recovery retains blocked findings/history, reruns validation and uses sync for broader drift; no whole-update transaction is specified.

> Apply low-risk fixes directly. For high-impact contradictions, stale claims, alert resolutions, or canonical meaning changes, write the lint finding and ask for user confirmation before changing canonical docs.
> --- `references/maintenance-workflows.md`

> If no reliable baseline is available, compare current included sources against relevant technical docs and traceability; a clean diff alone does not establish that the wiki is current.
> --- `references/synchronization-workflow.md`

### Claims

#### RT-CLM-project-memory
Label: Durable project memory

The README claims a repository-local wiki remains useful across agent sessions through progressive disclosure and traceability. This is doctrine/design and attributed intended benefit, not observed recall, improved capacity or reliable automatic maintenance. SRC-1, `README.md`.

> Turn requirements, decisions, code knowledge, and project history into an indexed wiki that lives beside the source code and stays useful across agent sessions.
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-project-protocol
Label: Generated Project Wiki Protocol

Consumer: future host coding agent that loads repository instructions. Channel: natural-language marked block in root `AGENTS.md` and `.github/copilot-instructions.md`, prescribed by init/scan and refreshed during maintenance/migration. Force: instructional policy, not a filesystem or model-runtime interlock; it requests index-first reads, dynamic configuration, helper-mediated source access, selective automatic updates, reconciliation and logging. Horizon: later tasks/sessions in the consuming repository, conditional on host loading and adherence. The skill preserves unrelated instruction content and replaces only its delimited block. This is a live intended behavioral-authority path but no activation trace is supplied (SRC-1, `assets/core-templates.md`, `references/initialization-workflows.md`, `references/maintenance-workflows.md`).

> In each file, insert or replace only the block delimited by `<!-- PROJECT-WIKI:BEGIN -->` and `<!-- PROJECT-WIKI:END -->`.
> --- `references/initialization-workflows.md`

> Before implementing, modifying, debugging, refactoring, testing, documenting, or planning code, read it and only the linked context needed for the task.
> --- `assets/core-templates.md`

## Annotations

none
