---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Hyalo workflow account: explicitly requested Jev-assisted tidy, advisory classification, foreground review, authorized repair and final reporting."
run-id: AAS-2026-10-14-hyalo-ffe11d6a6d56-01
reviewed-boundary: "697f215fe8a90a5c760fceb686f2a321c9db7221"
---

# Hyalo workflow report

## Workflow account

### Selected workflow and responsibility boundary

The representative workflow is an explicitly requested, Jev-assisted tidy of selected knowledgebase documents, ending in either audit proposals or authorized repairs and a health report. It was selected because the shipped tidy instruction explicitly connects local diagnosis, optional remote classification, independent review and ordinary mutation; this is not a workflow inferred by joining unrelated tools. The enclosing agent owns progression. Hyalo supplies instructions and deterministic operations; Jev supplies bounded classification suggestions, not a second general-purpose agent that can repair the vault. The route identities are [RT-RTE-tidy-review](runtime.md#rt-rte-tidy-review), [RT-RTE-jev-suggestions](runtime.md#rt-rte-jev-suggestions) and, for property publication, [RT-RTE-property-write](runtime.md#rt-rte-property-write). SRC-1, `crates/hyalo-cli/templates/skill-hyalo-tidy.md`, `crates/hyalo-cli/templates/jev/jev.md`.

This is a source-supported procedure and implemented helper path, not an observed successful tidy. The evidence boundary and external host/provider exclusions remain those in [boundary](boundary.md). The long tidy template requests forked context through host metadata, but Hyalo does not implement that fork's scheduling, input inheritance, disposal or return channel. Thus the foreground agent named here is the agent conducting the maintenance invocation, whether or not the host places it in a separate context. SRC-1, `crates/hyalo-cli/templates/skill-hyalo-tidy.md`.

> context: fork
> disable-model-invocation: true
> --- `crates/hyalo-cli/templates/skill-hyalo-tidy.md`

### Request, orientation and local evidence

The user supplies the task and its authorization scope. The agent locates the binary and configured vault; if configuration is missing, the instruction sends the decision back to the user rather than choosing a vault. An audit is read-only. A tidy/repair request authorizes relevant edits but not deletion or unrelated changes. Jev additionally requires an explicit request for this session; a credential or repository setting cannot enable it. These are instruction-level consent boundaries, not host filesystem or network isolation. The helper's separate executable gate requires `ask ... --allow-network`, as recorded in [RT-RTE-jev-suggestions](runtime.md#rt-rte-jev-suggestions). SRC-1, `crates/hyalo-cli/templates/skill-hyalo-tidy.md`, `crates/hyalo-cli/templates/jev/jev.md`, `npm/jev/src/cli.ts`.

The agent gathers a baseline summary, views, metadata/task selections and tag vocabulary. Git history supplies evidence about shipped branches and backlog items. Optional Claude memory is a read-only signal for cross-checking, not a Hyalo-owned store to repair. Strict lint, link-fix previews, orphan/dead-end queries and status/task comparisons provide findings. The agent must distinguish legitimate orphans and uncertain stale statuses from defects. The Jev branch keeps all reads live and skips index creation/removal, including in repair mode; the snapshot branch in ordinary tidy is not used here. SRC-1, `crates/hyalo-cli/templates/skill-hyalo-tidy.md`, `crates/hyalo-cli/templates/jev/jev.md`; [RT-RTE-query-read](runtime.md#rt-rte-query-read).

### Delegation to a bounded classifier

Before loading every selected body into its own context, the agent establishes scope and local conventions from configuration, type schemas and compact selections. It supplies at most 25 exact Markdown paths, optional sections and a session policy describing candidate types, tags, existing folders, exclusions and any type-to-folder mapping. Unclear conventions require deferral, not an invented taxonomy. The helper's `prepare` stage uses read-only Hyalo operations to return a manifest; `check` validates it locally; `ask` validates the manifest again before invoking the provider. Files too large for whole-body evidence require a bounded explicit section; unsupported or excluded inputs have explicit outcomes rather than silent truncation. These preparation and selection findings use [RT-OBJ-manifest](runtime.md#rt-obj-manifest), [RT-OBJ-document-content](runtime.md#rt-obj-document-content) and [RT-RTE-jev-suggestions](runtime.md#rt-rte-jev-suggestions). SRC-1, `crates/hyalo-cli/templates/jev/jev.md`, `npm/jev/src/cli.ts`.

The service receives body evidence and described questions under a pinned model identifier, not separate local paths and current-frontmatter fields. Embedded secrets or paths in the body can still travel. The caller receives per-document validated decisions, fingerprints, counts and usage information, not a provider conversation. This reduces the need to load all bodies into the main agent before triage, but does not establish measured context savings or provider-side deletion. Manifests/results persist only if the caller explicitly captures them; the reference places such artifacts outside the vault and allows supplied inputs plus stdout/stdin for strict no-write audits. SRC-1, `crates/hyalo-cli/templates/jev/jev.md`, `npm/jev/src/cli.ts`, `npm/jev/src/provider.ts`; [RT-RTE-jev-suggestions](runtime.md#rt-rte-jev-suggestions).

Jev proposes missing type, approved tag additions or approved filing locations; it does not infer status, completion, dates, deletions or new schemas. Helper code checks model identity, question/answer correspondence, choice labels, probability validity and acceptance thresholds before exposing suggestions. The foreground agent retains the decision to use or reject them. These gates restrict the returned suggestion channel; they do not prove that a confident semantic classification is correct. There is no known-correct answer oracle. Local schemas and conventions are constraints and evidence, not reference classifications. SRC-1, `crates/hyalo-cli/templates/jev/jev.md`, `npm/jev/src/decisions.ts`; [RT-CMP-jev](runtime.md#rt-cmp-jev), [RT-BAP-jev-categories](runtime.md#rt-bap-jev-categories).

### Independent review, rejection and authorized publication

Only suggestions the agent intends to use trigger full-current-evidence inspection. The agent must prepare again and compare document/context fingerprints; a changed body, metadata or policy requires reassessment. This is an instructed freshness check, not an atomic read/write guard, especially for section-only evidence. Review then checks the complete effective schema, global requirements, required sections, destination bindings, collisions and link rewrites. A locally valid assigned property is insufficient to establish a valid resulting document. SRC-1, `crates/hyalo-cli/templates/jev/jev.md`; [RT-RTE-property-write](runtime.md#rt-rte-property-write).

> Before changing type or location, inspect the complete effective schema, including
> global requirements, required sections and destination path bindings. A suggested
> type requiring an unknown status/date/section must defer; do not invent the missing
> value.
> --- `crates/hyalo-cli/templates/jev/jev.md`

This supplies a concrete semantic rejection path: a high-confidence suggested type still defers when required evidence is missing. Ambiguous move rewrites likewise defer. For an audit, even accepted suggestions remain proposals. For an authorized repair, the agent previews relevant `set --dry-run --validate` and `mv --dry-run` operations, inspects previews and then invokes ordinary Hyalo mutations within scope. The helper never publishes repairs itself. Human contribution is initial scope/authorization and later judgment of escalated issues, not demonstrated approval of each routine change. Agent judgment supplies per-content review; CLI code supplies mechanical admission/publication. SRC-1, `crates/hyalo-cli/templates/jev/jev.md`; [RT-RTE-tidy-review](runtime.md#rt-rte-tidy-review), [RT-RTE-property-write](runtime.md#rt-rte-property-write).

### Failure handling and recovery ownership

The helper has a checked failure path independent of semantic deferral. `decisions` rejects invalid response identity/structure/probabilities. `ask` catches per-document failures, marks the row invalid or unavailable, substitutes deferrals for affected bindings and continues to later documents. Overall exit status distinguishes invalid protocol from unavailable service; valid results can contain ordinary deferrals. The agent is instructed to consume successful batches despite other failures and continue useful local tidy, rather than report a failed optimization as an empty successful classification pass. SRC-1, `npm/jev/src/decisions.ts`, `npm/jev/src/provider.ts`, `npm/jev/src/cli.ts`, `crates/hyalo-cli/templates/jev/jev.md`.

> Consume successful batches
> even when another fails. A missing prerequisite or provider failure must not appear
> as an empty successful classification pass. Continue ordinary local tidy where useful.
> --- `crates/hyalo-cli/templates/jev/jev.md`

A failed row is not necessarily devoid of useful output: the helper can still add a folder suggestion from an existing type and explicit local type-to-folder convention after a failed independent classification request. It cannot manufacture a missing type from that failed request. This matters when reviewing mixed failure/results rather than treating process exit status as a complete decision ledger. SRC-1, `npm/jev/src/provider.ts`.

> // Existing local filing conventions remain usable when independent tag
> // questions fail. A failed classification never supplies a missing type.
> --- `npm/jev/src/provider.ts`

The provider wrapper bounds requests and configures one retry only for HTTP 429/529, within a total per-document deadline. The reference prohibits changing runtimes to retry a possibly transmitted request. A missing prerequisite is a visible skipped optimization. None of this establishes service availability or actual retry behavior in a deployed SDK. Downstream write failure belongs to the ordinary mutation owner: [RT-RTE-property-write](runtime.md#rt-rte-property-write) reports surviving effects and index disposition, not batch rollback. Consequently, the agent must inspect partial effects and report/repair failures; helper no-write behavior does not make subsequent repairs transactional. Other mutation handlers' complete recovery contracts were not independently traced here. SRC-1, `npm/jev/src/provider.ts`, `crates/hyalo-cli/templates/jev/jev.md`.

### Verification and delivery

After repair, the Jev reference requires lint on changed files and rechecking links and original findings; failures go into the report. The ordinary tidy final phase requires a fresh non-indexed summary compared with the baseline. These are requested postconditions and diagnostics, not a code-enforced all-green barrier before a response. Schemas, link checks and summary deltas cannot establish that every semantic maintenance judgment was correct. SRC-1, `crates/hyalo-cli/templates/jev/jev.md`, `crates/hyalo-cli/templates/skill-hyalo-tidy.md`; [RT-RTE-tidy-review](runtime.md#rt-rte-tidy-review).

Delivery is the agent's final report: actual changes with reasons, unresolved issues for human attention and health-dashboard deltas. Jev-assisted reporting adds selected/transmitted counts, suggestions, deferrals/unavailable batches, elapsed time and returned usage, with cost/unknown-usage qualifications. Audit delivery contains proposals instead of writes. The source specifies neither guaranteed host delivery nor durable storage of that final report. Repairs, when applied, persist as vault changes available to later reads; successful adoption, verification and user receipt remain unobserved. SRC-1, `crates/hyalo-cli/templates/skill-hyalo-tidy.md`, `crates/hyalo-cli/templates/jev/jev.md`; [RT-RTE-query-read](runtime.md#rt-rte-query-read).

### Added source coverage and limits

Workflow inspection read the complete long tidy template and Jev reference as doctrine/design, and complete Jev CLI, decision validator and provider wrapper as implementation, all within SRC-1 at the frozen revision. No target command, evaluator, example or model call was executed. The account adds handoff and stopping details to existing runtime referents rather than declaring duplicate routes. Host context semantics, actual tool grants, model compliance, provider internals, completed repairs and operational benefit remain unobserved; source wiring and policy alone establish none of those outcomes.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-tidy-review](runtime.md#rt-rte-tidy-review)

Workflow-specific handoff: the agent retains phase progression and final delivery responsibility. In the selected Jev branch, live reads replace the ordinary snapshot option throughout. Audit proposals, uncertain findings and schema/rule-tuning proposals stop short of unilateral publication. Completion is a report with reasons and fresh-summary deltas, not a demonstrated all-clear condition. Verification failures remain reportable unresolved issues rather than proof that the workflow never reached its reporting phase.

#### On [RT-RTE-jev-suggestions](runtime.md#rt-rte-jev-suggestions)

Workflow-specific acceptance boundary: validated suggestions are returned to agent review, not forwarded directly to mutation. Intended suggestions require current-evidence re-preparation and complete-schema/destination checks before previews. Missing required values or ambiguous link rewrites cause deferral even after high-confidence classification. Per-document invalid/unavailable results do not cancel successful sibling batches; locally mapped folder suggestions require separate consideration from failed model answers. Recovery rejoins ordinary local diagnosis within original scope rather than escalating the helper into an editor.
