---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "DocMason runtime baseline: host-owned reasoning, canonical ask closure, staged publication and local change admission."
run-id: AAS-2026-10-13-docmason-deba9ae199d5-01
reviewed-boundary: f3970939593194a158ab7ea1d49995f06cbccc86
---

# DocMason runtime report

## Runtime account

DocMason supplies a local evidence application and an authored operating contract for a host agent, not its own model scheduler. Its consequential work is compiling documents into a published evidence surface, helping the host retrieve and trace that evidence, and admitting answers and enriched knowledge under file-backed control state. The host performs semantic framing, image interpretation, synthesis and user communication. Python owns deterministic extraction, routing normalization, turn records, checks and publication. This is implementation and doctrine/design evidence from SRC-1, not a supplied execution trace. No target program or tests were executed; host compliance, actual activation, output quality and benefit remain unobserved.

The entry split is concrete. Installed/module CLI dispatch handles public prepare, doctor, status, sync, retrieve, trace, validate-kb, sync-adapters, update-core and workflow commands. Hidden `_ask` accepts JSON on stdin and hidden `_hook` handles host events (SRC-1, `src/docmason/cli.py`). Canonical `ask` is a skill-driven host protocol rather than a public answer command. Explicit operator setup, maintenance and evaluation are shipped alternate paths, not excluded enclosing applications. The enclosing host's model, tool grants, sandbox and network policy remain outside this application's ownership ([RT-CMP-host-agent](#rt-cmp-host-agent)).

### Ordinary invocation and ownership transfers

An ordinary corpus question is intended to follow [RT-RTE-canonical-ask](#rt-rte-canonical-ask). The host reads the canonical skill and opens `_ask` with the user's question, a thin semantic work brief and host identity. The wrapper calls `prepare_ask_turn`, requires stable conversation/turn IDs, persists host context, and returns the active run, canonical answer path, log context, support contract, route and status. Native thread capture alone does not create canonical ownership. `execute` hands next-step reasoning to an inner workflow; waiting, confirmation and blocked states retain the same governed task instead (SRC-1, `skills/canonical/ask/SKILL.md`, `src/docmason/host_integration.py`).

For an answer-eligible workspace question, the host uses published KB evidence first. `retrieve` reloads records, resolves source scope and ranks evidence; the host inspects text/structure and, when material, published render assets. `trace` evaluates the exact answer file and returns support diagnostics. These are tool results, not a model's independent truth oracle. The host writes or supplies the answer and invokes `finalize`; the wrapper can atomically write supplied `answer_text` and recover an exact trace. Completion calls an admissibility gate before `commit_run`. The terminal result separates clean business answer text from status/governance detail. Persistence includes answer Markdown, turn/run state, retrieval sessions and trace records; identifiers bind those surfaces ([RT-OBJ-canonical-turn](#rt-obj-canonical-turn)).

Evidence consumption and model context are deliberately narrower than the full stored corpus: compact retrieve/trace payloads are the default; full nested outputs should go to files for selective inspection. Published renders are inspected only when the answer needs them. These are authored context-management instructions, not observed host trimming. Read-only side research is permitted for large synthesis, but main-agent integration, sync and publication remain prescribed. The source does not supply an inspected host implementation of isolated sub-agent windows, compaction, eviction or provider context caching. Such host machinery and what crosses its delegation boundary remain uninspected (SRC-1, `AGENTS.md`, `skills/canonical/grounded-answer/SKILL.md`).

If publication does not yet exist or freshness truly matters, the ask path may route to prepare/sync rather than answer from staging. [RT-RTE-sync-publish](#rt-rte-sync-publish) stages physical evidence and deterministic conservative semantics, validates, and conditionally switches the current publication. Multimodal semantic gaps can outlive deterministic publication. Sync-time bounded follow-up (Lane B) and ask-time narrowed refresh (Lane C) select agent work packets; the host authors additive overlays and returns to repository settlement ([RT-RTE-hybrid-refresh](#rt-rte-hybrid-refresh)). This report establishes those runtime admission edges, not the detailed memory transformations or trust of every retained part.

### Four forcing comparisons and guarantee scope

1. **Canonical closure versus side paths.** The ordinary wrapper rejects already-committed turns, waits on paused turns and rejects disallowed truth overrides. Lower-level completion gates canonical commits. However public retrieve/trace are explicitly legal operator tools, and evaluation directly calls lifecycle helpers with evaluation log origin. The snippet guard only recognizes compatible-host identity plus selected Python snippet stack filenames; it is not an OS access boundary. Host shell/file writes and an answer returned outside the protocol are not intercepted by these Python checks. Thus canonical legality is a protocol, while checking an invoked canonical commit is implemented control, not universal mediation of host behavior (SRC-1, `src/docmason/ask.py`, `src/docmason/evaluation.py`, `src/docmason/host_integration.py`, `skills/canonical/ask/SKILL.md`).
2. **Corpus grounding versus other evidence bases.** `workspace-corpus`, external factual, stable general knowledge and composition do not all demand the same evidence. KB/mixed commits require ask-owned trace/version truth; external/mixed commits need a bound support manifest, and local corpus evidence cannot simply be relabelled external. Model-knowledge and governed-boundary outcomes are legal. Consequently “all answers are KB-grounded” would be false; legality is relative to a declared support basis, not a universal factual-correctness guarantee (SRC-1, `src/docmason/admissibility.py`, `skills/canonical/ask/SKILL.md`).
3. **Validation/publication versus arbitrary filesystem mutation.** The sync branch publishes only validation statuses `valid` or `warnings`; unchanged state can skip publication. The publishing helper checks the copied report's status/signature against the passed report and rolls back pointer/ledger failures. It is not an independent full semantic validator, and its check does not itself demand a successful status. Filesystem leases are explicitly best effort, reclaim stale locks by mtime, and require cooperating callers. These mechanisms cannot establish protection against arbitrary host edits, all races, crashes or malicious parser behavior (SRC-1, `src/docmason/knowledge.py`, `src/docmason/versioning.py`, `src/docmason/coordination.py`).
4. **Remote versus local core replacement.** Explicit `update-core` admits shipped executable/prompt changes. Remote bundle handling checks a downloaded checksum and expected version; the local-bundle branch validates clean-channel/version metadata without that remote checksum comparison. Replacement preserves named top-level private/runtime paths and restores moved files on application exceptions. This is separate from KB validation and is not a model-generated self-revision loop or proof of deployed release authenticity (SRC-1, `src/docmason/update_core.py`).

Load-bearing guarantees are scoped in [RT-CLM-commit-gate](#rt-clm-commit-gate) and the publication, hook and updater routes below. Required external contracts are host adherence, genuine user decisions where approval is needed, stable filesystem semantics and capable parsers/renderers. The **capability surface** includes local read/write, shell commands, JSON and image inspection; the **current grant set** is not supplied; the **deployed isolation envelope** is not supplied. LibreOffice conversion is a subprocess with timeout/error capture, not evidence of a sandbox. Provider-native tools, unrestricted shell, remote workers and opaque host callbacks cannot be ruled out in the external host; none is needed to explain the inspected local loop (SRC-1, `AGENTS.md`, `src/docmason/libreoffice_runtime.py`).

Optional hooks add advisory continuation context and a bounded one-shot trace/finalize reminder, not an alternate answer executor ([RT-RTE-host-hooks](#rt-rte-host-hooks)). Generated adapters project canonical instructions into host-consumed files ([RT-RTE-adapter-sync](#rt-rte-adapter-sync)). The operator evaluator can replay hand-authored answer plans and promote runtime candidates to regression cases; it does not itself establish generated-answer quality or modify production code on a score threshold ([RT-RTE-operator-eval](#rt-rte-operator-eval)).

Added inspection within SRC-1 supplies implementation evidence from `src/docmason/admissibility.py`, `src/docmason/coordination.py`, `src/docmason/versioning.py`, `src/docmason/hooks.py`, `src/docmason/update_core.py`, `src/docmason/libreoffice_runtime.py`, and additional bounded ask, wrapper, command, retrieval and evaluation passages. Additional doctrine/design inspection covers complete canonical ask, grounded-answer, knowledge-base-sync and knowledge-construction skills, `AGENTS.md`, configuration and the README privacy paragraph. This extends initial path coverage, not the frozen source boundary. Ancillary release-service deployment remains excluded; only the shipped local updater admission mechanism is characterized. Detailed parser fidelity, sample extraction, test assertions, preparation installer internals, projection-worker execution and interaction-memory revisions remain for other accounts or uninspected here; no efficacy or exhaustive audit conclusion is drawn from them.

## Shared records

### Components

#### RT-CMP-host-agent
Label: Host agent and inference model

The source-native agent is the reasoning executor. The host consumes natural-language contracts and selected evidence; its inference component is distributed-parametric, stored in external provider/host model weights, not in the file-only KB. Provider internals and any provider state are uninspected. No exact operational model/version is pinned by the inspected contract; model parameter changes during operation are uninspected. A host/provider choice can resolve to another model, but endpoint alias mutability is not specified in this repository boundary. These statements concern the external model, not the agent's mutable files. SRC-1, `AGENTS.md`, `README.md`.

> DocMason is a repo-native application workspace. The agent is the runtime.
> --- `AGENTS.md`

> **All AI inference traffic** is handled by your chosen host agent (Codex, Claude Code, etc.) — DocMason itself makes zero model API calls. The network behavior of your AI agent is governed by that agent's own privacy and telemetry policy.
> --- `README.md`

This is a declared inference boundary, not an audited absence of every possible network or third-party model call.

### Operative objects

#### RT-OBJ-canonical-turn
Label: Canonical ask turn binding

A file-backed symbolic control record: conversation ID, turn ID, active/committed run, front-door state, answer path, support basis, selected session/trace IDs and wait/gate state. Fixed Python consumers interpret those fields; the answer Markdown's natural-language meaning is a distinct consumption path, not identical to its symbolic binding. Runtime directories persist turn/run records and answers. This record denotes the control binding, not the full retained conversation-memory store. SRC-1, `src/docmason/host_integration.py`, `src/docmason/ask.py`.

>     committed_run_id = _nonempty_string(turn.get("committed_run_id"))
>     if committed_run_id is not None:
>         return {
>             "status": "blocked",
>             "user_reply_allowed": False,
> --- `src/docmason/host_integration.py`

#### RT-OBJ-publish-pointer
Label: Current publication pointer and ledger

Symbolic filesystem control state selects the published KB root, accompanied by a pointer and logical publication ledger. Python owns switching, consistency bookkeeping and cleanup. The pointer/ledger are not the natural-language claims inside the selected corpus. The implementation keeps a single current hidden root after successful pruning rather than an indefinite full-snapshot rollback archive. SRC-1, `src/docmason/versioning.py`.

>         keep_roots = {target_root}
>         cleanup: dict[str, Any]
>         try:
>             deleted_roots = _prune_published_roots(paths, keep_roots=keep_roots)
>             cleanup = {"status": "completed", "deleted_roots": deleted_roots}
> --- `src/docmason/versioning.py`

### Routes

#### RT-RTE-canonical-ask
Label: Canonical ask open, evidence loop and finalization

Endpoints are an ordinary user message, host `_ask open`, repository preanswer state, inner workflow evidence work, `_ask finalize`, then committed answer/boundary. The host proposes semantic analysis, evidence selection and answer; repository normalization and admissibility decide legal progression. User decisions can pause work; starting ask is not approval of every generated sentence. The policy is natural-language skill guidance plus symbolic Python state transitions. Context includes the question, brief, support contract, selected records and optional renders, not necessarily the complete corpus. Owner of next reasoning step is the host on `execute`, the user on decision/confirmation waits, or shared-job settlement on a wait. SRC-1, `skills/canonical/ask/SKILL.md`, `src/docmason/host_integration.py`, `src/docmason/ask.py`, `src/docmason/admissibility.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: JSON status, stable identity, answer path, route, support contract and log context; terminal response returns answer text and separate closure status.
- Later read-back: Continuing invocations reload persisted turn/gate/scope truth; exact `revision_of` or gate identifiers govern explicit continuation rather than adjacency alone.
- Delegated visibility: Inner workflows receive canonical ownership and selected evidence; read-only sidecars are prescribed for bounded research. Actual host sub-agent input/return isolation is uninspected.
- Selection predicate: User goal and host semantic hinting, normalized question class/domain, workspace readiness, reference resolution and support basis select the workflow.
- Invalidation or expiry: Current-run ownership, version truth, explicit revisions and dependency drift affect reuse; already-committed wrapper finalization is rejected.
- Activation or effect: Implemented opening/persistence and commit checks; actual behavioral effect of delivered instructions on a host is unobserved.
- Evidence limits: Source wiring is not a supplied ask execution or proof of truthful model synthesis.

Operating mode is open user requests. There is no independent answer oracle: corpus evidence, support diagnostics and host judgment contribute, not expected answers. Answer admission can reject/repair before commit; the authored contract permits a bounded rewrite/retrace rather than unbounded repair. Pending turn state remains available for same-turn continuation. Guidance preserves honest source scope and uncertainty; what persists is the answer, linkage and governance state, not model parameters.

> - Completion rule:
>   - only `completed` or `boundary` permits a final business reply to the user
>   - `execute`, `awaiting-confirmation`, `awaiting-user-decision`,
>     `waiting-shared-job`, and `blocked` do not
> --- `skills/canonical/ask/SKILL.md`

#### RT-RTE-evidence-tools
Label: Public retrieve and trace, bound or operator-direct

The public CLI dispatches deterministic retrieval and provenance tools independently of canonical ask; inside ask, environment log context binds their results to the live turn. Retrieval loads the selected target, reference resolution and source-scope policy, may merge pending interaction evidence for current-target queries under a predicate, then executes lexical-plus-graph retrieval. The host receives a projection of evidence and diagnostics, not an automatically written answer. This route denotes reader/tool delivery, not the memory write mechanisms. SRC-1, `src/docmason/cli.py`, `src/docmason/retrieval.py`, `skills/canonical/grounded-answer/SKILL.md`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Query results or trace/support state, references, identifiers and diagnostics; compact output is available to constrain model-visible payload.
- Later read-back: Logged sessions/traces can be selected for subsequent canonical finalization and session tracing; corpus is reloaded on later calls.
- Delegated visibility: Selected units, artifact references and renders can be handed to the inner workflow; no host-wide visibility enforcement is established.
- Selection predicate: Query, top limit, graph hops, type/source filters, inherited turn scope and reference resolution constrain results; pending-overlay merge is separately conditional.
- Invalidation or expiry: Target/version and exact-answer binding matter at later closure; inspectable code does not make a previously delivered tool result disappear from host context.
- Activation or effect: Implements evidence delivery and optional logs; host use and changed answer behavior remain unobserved.
- Evidence limits: Direct retrieval/trace does not by itself satisfy the canonical ordinary-answer protocol or validate every semantic claim.

> - Direct evidence commands such as public `retrieve` or `trace` remain legal operator tools, but they do not complete the ordinary ask contract by themselves.
> --- `skills/canonical/ask/SKILL.md`

#### RT-RTE-sync-publish
Label: Deterministic staging, validation and publication

Operator sync or governed ask freshness triggers a shared-workflow build. Python detects physical changes, rebuilds/reuses staged sources, writes conservative semantic outputs where needed, repairs and validates, then publishes or reports pending/blocked work. Main-agent publication sign-off is prescribed; software performs the actual publish decision. State includes source signatures, validation/rebuild telemetry and shared jobs. SRC-1, `src/docmason/knowledge.py`, `src/docmason/versioning.py`, `src/docmason/coordination.py`, `skills/canonical/knowledge-base-sync/SKILL.md`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Sync status, validation outcome, publication/skipped state, costs and remaining enrichment work packet.
- Later read-back: Readers reload current published artifacts; sync reloads signatures/state; successful publication also marks eligible interaction entries promoted.
- Delegated visibility: Bounded per-source enrichment may be delegated; main path retains shared mutation, rerun and publication judgment.
- Selection predicate: Source delta, repair/drift and pending-state checks determine rebuild versus reuse; validation statuses valid/warnings admit publication.
- Invalidation or expiry: Source/configuration changes and contract/cache drift can force work; unchanged state can skip publication. Successful pruning removes old physical roots.
- Activation or effect: Current-root switch makes newly published material available to later readers; actual answer influence is unobserved.
- Evidence limits: Structural admission and current selection do not establish extraction fidelity, semantic correctness, corpus confidentiality or improved answers.

Admission roles: deterministic code proposes conservative outputs and repairs, host enrichment can propose additions, validation can reject, and confirmation-required shared jobs defer to the user; `sync --yes` is the public approval continuation, not universal per-content review. Mode is maintenance of an open corpus. No independent answer oracle applies; schema/evidence checks are validators, not expected business answers. Guidance requests supported semantics and explicit gaps. Persisted results are staged/published evidence, semantics, indexes and publish control state. Recovery includes transactional staging machinery and restoration of current/pointer/ledger on handled publication bookkeeping failures; full crash-atomic multi-file durability is not established.

Owner of the validation guarantee is the sync driver; enforcement is its branch, strength **protocol** across cooperating entry paths. Implementation conclusion status is wired; operation conclusion status is uninspected. The helper additionally checks copied status/signature, not a new full validation. Required external contract: callers use the driver with authentic validated staging and do not mutate it concurrently.

>         if validation_report["status"] in {"valid", "warnings"}:
>             if (
>                 not rebuild_required
> --- `src/docmason/knowledge.py`

>             raise ValueError("Publish candidate validation does not match validated staging.")
> --- `src/docmason/versioning.py`

Coordination strength is **best effort**, owned by cooperating Python callers, enforced by directory creation, timeout and stale-lock cleanup. It is not a deployment isolation guarantee:

>     """Acquire a best-effort filesystem lease for one shared workspace resource."""
> --- `src/docmason/coordination.py`

#### RT-RTE-hybrid-refresh
Label: Bounded multimodal semantic follow-up

Sync-time Lane B packets or ask-time Lane C sufficiency gaps select bounded source/unit work. A host reads work-item/evidence manifests and relevant render assets, proposes supported semantic overlays, then returns to sync or hidden progress/closure. Deterministic conservative semantics and agent enrichment are alternate producers; successful deterministic publication alone need not mean hybrid coverage. SRC-1, `skills/canonical/knowledge-construction/SKILL.md`, `skills/canonical/knowledge-base-sync/SKILL.md`, `skills/canonical/grounded-answer/SKILL.md`, `src/docmason/knowledge.py`, `src/docmason/admissibility.py`.

- implementation conclusion status: wired
- host-authoring conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Bounded work packet, coverage/blocker summary and rerun or progress handoff; not independent final publication authority.
- Later read-back: Admitted semantic sidecars enter published evidence and can be retrieved/traced later; Lane C requires post-settlement evidence tools before legal closure.
- Delegated visibility: Work packet limits sources/units and render targets; the main host integrates outcomes. These are authored write-scope rules, not host sandbox restrictions.
- Selection predicate: Sync's pending hard-artifact work or query-aware recommended hybrid targets; target artifacts/focus renders refine the scope.
- Invalidation or expiry: Overlay guidance binds source and unit fingerprints and freshness; Lane C closure checks settled job/snapshot scope and post-settlement session/trace timing.
- Activation or effect: Supported overlays can be admitted through the ordinary publication route; interpreted authoring and downstream benefit are unobserved.
- Evidence limits: Render inspection is requested/auditable, not verified model comprehension. Full overlay invalidation internals are not assessed here.

Host proposes content under guidance to preserve deterministic sidecars, cite real evidence and expose uncertainty. Software validation/settlement and final main-path rerun can reject or block. Human initiation or a shared-job approval is not per-overlay approval. Mode is bounded maintenance or an open ask's bounded repair, not an experimental curriculum; no expected-answer oracle. Recovery is same-turn wait/block or honest partial/boundary closure, not repeated unbounded refresh. What persists is evidence-derived natural-language/symbolic semantic content and coverage state; detailed memory revision is left to the memory account.

>    - overlays must remain additive
>    - do not rewrite deterministic sidecars such as `artifact_index.json`, `visual_layout/*.json`, `spreadsheet_*`, or `pdf_document.json`
> --- `skills/canonical/knowledge-construction/SKILL.md`

>                 "Covered governed multimodal refresh turns require a post-refresh "
>                 "trace recorded after the shared job settled."
> --- `src/docmason/admissibility.py`

#### RT-RTE-host-hooks
Label: Optional continuation sensing and one-shot closure

Host hook events reach `_hook`. Python logs supported native events and constructs host-neutral decisions. Prompt submission can deliver advisory continuation IDs, open gate options and accepted scopes; Stop can request one bounded continuation. The executor is still the host, not the hook. SRC-1, `src/docmason/hooks.py`, `skills/canonical/ask/SKILL.md`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Host-specific additionalContext or Stop block/reason for a one-shot continuation; otherwise no intervention.
- Later read-back: A subsequent prompt can receive latest linked canonical turn/gate/scope state. Persisted closure-continuation claim limits repeated attempts.
- Delegated visibility: Host event protocol receives only selected reminders; actual injection and host compliance are external.
- Selection predicate: Bound session/turn, matching current prompt, prepared uncommitted turn, existing artifact, sufficient support and no blocking/gate/refresh conditions; an active stop hook is excluded.
- Invalidation or expiry: Committed, waiting, at-risk, stale or unresolved state disqualifies closure continuation; one-shot claim prevents repeated continuation for the same governed claim.
- Activation or effect: Requests trace/finalize completion only; it does not sync, retrieve, broaden scope or alter the business deliverable itself.
- Evidence limits: Optional hook installation/activation and resulting host actions are unobserved; this is not enforcement over an unbound native reply.

Owner of one-shot eligibility is hook code; strength **protocol** requiring the host to honor the serialized event response. Implementation conclusion status is wired; operation conclusion status is uninspected. It does not turn ledger capture into canonical answer authority.

>             "Complete only the pending DocMason trace/finalize closure for the existing "
>             "answer. Do not sync, retrieve, broaden scope, or alter the business deliverable."
> --- `src/docmason/hooks.py`

#### RT-RTE-operator-eval
Label: Replay evaluation and regression-case admission

The operator workflow reads a request and dispatches run-suite, review-regressions, promote-candidate or freeze-baseline. Suite execution consumes the current published corpus, rubric, optional supplied judge trials and baseline. Ask replay can call lifecycle helpers with a configured answer plan rather than having a live model generate an answer. Candidate promotion writes drafts and appends proposed cases; baseline freezing writes a selected run's baseline. SRC-1, `src/docmason/operator_eval.py`, `src/docmason/evaluation.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Run/scorecard, comparison/review, promotion or baseline action result; malformed requests become action-required.
- Later read-back: Regression suites, baselines and run artifacts feed later replay/comparison; this is evaluator-state change, not automatic production-code revision.
- Delegated visibility: Judge packets expose case/reference/output information for external judgment; supplied judge-trial files are consumed, not evidence of a live judge call.
- Selection predicate: Validated action, requested candidate/run/case IDs and matching corpus signature; duplicate promoted case IDs are skipped.
- Invalidation or expiry: Corpus-signature mismatch blocks suite execution; explicit freeze replaces baseline expectations. No automatic expiry is established by these passages.
- Activation or effect: Writes evaluation assets and evaluates deterministic expectations; actual successful replay and subsequent product benefit are unobserved.
- Evidence limits: Manual answer plans and supplied judge scores do not demonstrate autonomous answer generation, causal improvements or automatic production adoption.

Mode is bounded replay/evaluation. Oracles include suite-authored expected status, source/support/answer-state fields and structural expectations; reference facts enter judge packets and supplied rubric judgments. The operator request selects promotion/freezing; code derives/appends the case and writes files. Human authorship/approval of each candidate's contents is unresolved by a generic request file. Validators can reject malformed inputs; duplicates are skipped. Guidance comes from candidate records, suites and rubric; persisted changes are drafts, cases, scores and baselines. Full rollback of overwritten evaluation assets is uninspected; source-control/private backups cannot be presumed. No live product-change proposal/admission mechanism follows merely from a regression score.

>         existing_cases.append(draft_payload["proposed_case"])
>         existing_case_ids.add(case_id)
>         promoted.append(candidate_id)
>     suite_payload["cases"] = existing_cases
>     write_json(paths.eval_suite_path("regression"), suite_payload)
> --- `src/docmason/operator_eval.py`

>             answer_text = str(answer_override or answer_plan["answer_text"])
> --- `src/docmason/evaluation.py`

#### RT-RTE-adapter-sync
Label: Canonical-instruction projection to generated adapters

Explicit adapter maintenance invokes `sync_adapters`. The implementation supports the Claude generation target, checks canonical inputs and workflow metadata, writes project memory/routing connectors and refreshes repo-local skill shims. Canonical text is the guidance source; generated natural-language imports plus symbolic connectors are the persisted proposal. Host loading gives the result its downstream behavioral channel. SRC-1, `src/docmason/commands.py`, `AGENTS.md`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Generated file list or unsupported-target/missing-input/metadata failure.
- Later read-back: Compatible host loading of generated project memory/imports can deliver canonical skills on later invocations; actual loading is unobserved.
- Delegated visibility: Host-specific generated guidance is a projection of canonical inputs, not a separate publication authority.
- Selection predicate: Explicit supported target, present source inputs and successfully parsed workflow metadata.
- Invalidation or expiry: Canonical input drift motivates regeneration; host caches/reload timing are uninspected.
- Activation or effect: Writes generated adapter files and shims; file creation alone establishes no host adherence.
- Evidence limits: No generated user installation or active host trace is supplied.

Mode is explicit maintenance, not oracle-scored improvement. Software generates and admits the projection after checks; user initiation is not per-line approval. There is no expected-answer oracle. Recovery is error reporting and regeneration; transactional rollback across partially written generated files is not established by the inspected function.

>         "It imports the vendor-neutral canonical skills so the generated adapter stays thin.",
> --- `src/docmason/commands.py`

#### RT-RTE-core-update
Label: Explicit local production-core replacement

An explicit operator update enters a workspace lease and updater. A generated bundle context is required; remote download or an explicit local clean ZIP supplies replacement core files. Manifest validation rejects wrong channel/missing version; remote additionally compares downloaded SHA-256 and expected version. The replacement moves unprotected existing children aside, applies new children and restores on application exception. SRC-1, `src/docmason/commands.py`, `src/docmason/update_core.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Applied/already-current version, preserved/applied paths or governed update error; post-update state errors can be reported as degraded by the command wrapper.
- Later read-back: Later CLI/host invocations can load replaced core code and contracts; preserved runtime/corpus/KB directories remain available.
- Delegated visibility: No delegated model work is required; external release metadata/download supply the candidate in the remote branch.
- Selection predicate: Explicit request, valid generated-bundle context, clean-channel/version metadata and branch-specific checks.
- Invalidation or expiry: Selected core files are replaced; protected paths include original_doc, knowledge_base, runtime, adapters, .docmason, .venv, .agents and .git.
- Activation or effect: Replacement changes available local production machinery; execution of changed code/prompts in a later invocation is unobserved.
- Evidence limits: Backend/deployment is excluded, local ZIP authenticity is not established by manifest metadata, and process-crash recovery is not demonstrated.

Admission roles: release producer or supplied local bundle proposes content; explicit operator initiates, code checks reject invalid candidates and applies valid ones. No human per-file approval or model-selected successor is implied. Mode is operator maintenance; answer oracle is inapplicable to bundle installation. Persisted guidance includes replaced core contracts/code; private state is protected by top-level names. Rollback covers handled move/apply exceptions and discards its temporary backup afterward, not indefinite version restoration. Guarantee strength is **best effort**, owned by local updater code with filesystem and trusted-distribution external contracts. Implementation conclusion status is wired; operation conclusion status is uninspected.

>     if channel != "clean":
>         raise UpdateCoreError(
>             "invalid-bundle",
>             "Explicit core updates require a generated clean bundle payload.",
>         )
> --- `src/docmason/update_core.py`

>             manifest = _validated_extracted_clean_bundle(
>                 extracted_root,
>                 expected_version=None,
>             )
>             applied_names = _replace_workspace_core(extracted_root, paths.root)
> --- `src/docmason/update_core.py`

### Claims

#### RT-CLM-commit-gate
Label: Canonical commits require admissibility, not universal correctness

Claimed operation: only legal canonical closure permits the final ordinary answer. Owner is the canonical ask implementation plus the host honoring its response. Enforcement point is `complete_ask_turn` calling `evaluate_commit_admissibility` before `commit_run`; the wrapper also rejects waiting/duplicate/illegal-override cases. Strength is **protocol** over the whole host-mediated path; invoked completion has a code gate. SRC-1, `skills/canonical/ask/SKILL.md`, `src/docmason/ask.py`, `src/docmason/admissibility.py`, `src/docmason/host_integration.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected

The gate checks current-run ownership, attached-job settlement, selected artifact identity/version, source-scope/support-state consistency, manifest bindings, illegal work-area citations and accepted-scope integrity. Enforcement varies by support basis. It is not a universal answer oracle or OS mediation: standalone tools, evaluator helpers and arbitrary host filesystem/shell behavior are alternate paths. Required external contract: the host actually uses canonical closure and does not return an out-of-band final answer. The scope is legal admission to canonical state, not correct reasoning or confidentiality.

>     if not admissibility_gate_result["allowed"]:
>         update_conversation_turn(
> --- `src/docmason/ask.py`

>         raise ValueError(
>             str(admissibility_gate_result.get("reason") or "The turn is not commit-admissible.")
>         )
> --- `src/docmason/ask.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-canonical-skills
Label: Repository contracts to host workflow decisions

Consumer: enclosing host agent. Channel: `AGENTS.md`, canonical skill files and generated adapter imports, augmented by returned support contracts and status instructions. Force: prescribed routing, evidence scope, mutation ownership and closure protocol; model adherence is external, while invoked Python operations enforce their own checks. Horizon: successive workflow steps and later host invocations that reload those files. Static contracts are not themselves accumulated memory; generated projections can deliver changed canonical guidance later. SRC-1, `AGENTS.md`, `skills/canonical/ask/SKILL.md`, `src/docmason/commands.py`.

> - The main agent owns critical-path reasoning, shared-state mutation, publication, final answers, and final operator conclusions.
> - Delegation does not transfer responsibility:
>   - use read-only sidecar delegation only when it materially helps large many-source synthesis or bounded side research
>   - keep sync, publication, control-plane settlement, and final integration on the main agent
> --- `AGENTS.md`

This is an explicit behavioral-authority channel, not evidence that any particular host obeyed it or that persisted knowledge improved the model's future capacity.

## Annotations

none
