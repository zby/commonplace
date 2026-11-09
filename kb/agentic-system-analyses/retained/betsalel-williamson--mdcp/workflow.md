---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "MDCP workflow account: docs-first feature work from scoped request through shard edits, implementation, mechanical rejection and review submission."
run-id: AAS-2026-11-08-mdcp-1e4e8314c1e4-01
reviewed-boundary: "1a198715a4da72dd89bad93f84cf5d4b3ab56b01"
---

# MDCP workflow report

## Workflow account

### Selection and evidence boundary

This account selects the shipped **feature workflow** because it connects a product request to durable documentation, code/tests, validation and review submission in one explicit process. It is not a workflow assembled from unrelated CLI capabilities. Its principal is a host agent following MDCP instructions, not an MDCP scheduler. The underlying route is [RT-RTE-feature-work](runtime.md#rt-rte-feature-work), with deterministic validation supplied by [RT-RTE-compile-check](runtime.md#rt-rte-compile-check).

All source findings use SRC-1 at the frozen commit in [boundary](boundary.md#source-register). Inspection here covers `skills/mdcp/SKILL.md`, the complete `skills/mdcp/references/workflows/feature-level.md`, and the check action in `packages/mdcp-cli/src/cli.ts`. The first two supply doctrine/design; the last supplies implementation. HEAD matched the registered revision. No target, test, example or evaluator was executed. The sequence below is a prescribed workflow with inspected check wiring, not an observed successful feature delivery.

### 1. Request becomes a scoped work item

The host supplies the user request and repository access. The skill chooses the feature-level reference for a feature or bugfix changing product code and asks the agent to load only that workflow. `WORK_ITEM` identifies the task; `WORK_ITEM_LOOKUP` locates repository scope and delivery conventions. The agent inspects acceptance criteria, commands and relevant paths before editing. Acceptance criteria bound the work rather than licensing adjacent issues. SRC-1, `skills/mdcp/SKILL.md`, `skills/mdcp/references/workflows/feature-level.md`; [RT-BAP-skill-host](runtime.md#rt-bap-skill-host).

> 1. Follow `WORK_ITEM_LOOKUP`. Inspect the repository for scope, acceptance criteria, validation commands, and delivery conventions before editing.
> 2. Treat acceptance criteria as the scope boundary — one feature or design at a time; do not expand into adjacent issues unless `WORK_ITEM` explicitly includes them.
> --- `skills/mdcp/references/workflows/feature-level.md`

The agent states a plan with numbered commit groups: one concern, exact files and intended conventional subject per group. It defines who benefits and creates a feature branch from updated main before documentation, tests or code. When a human can review, the process requests approval before committing groups; when nobody can answer, the parent skill permits stated defaults and continued reversible branch edits. It reserves stopping for a requested plan-first interaction, destructive/irreversible work, real scope changes or input only the user can supply. Thus the user supplies scope but is not necessarily approving each admitted paragraph or code edit. These are instruction-mediated choices, not an enforced approval state machine. SRC-1, `skills/mdcp/SKILL.md`, `skills/mdcp/references/workflows/feature-level.md`; decision and admission limits are retained in [RT-RTE-feature-work](runtime.md#rt-rte-feature-work).

### 2. The agent turns scope into a documentation contract

The handoff is from task interpretation to edits in source shards and guide indexes, through host filesystem tools. The agent places content by audience and job. A user-facing feature gets capabilities/contracts in `docs/features/` and value/usage in `docs/client/`; a maintainer-only topic belongs in `docs/developer/`, without invented consumer-facing content. New jargon can require glossary entries and first-use links. Intent and acceptance criteria belong in shards, implementation details in code. SRC-1, `skills/mdcp/references/workflows/feature-level.md`.

> 3. Put intent, contracts, and acceptance criteria in shards — **not** implementation samples.
> --- `skills/mdcp/references/workflows/feature-level.md`

The plan and shards provide the next stage's context. The skill asks the agent to discover relevant shards with host search or an index and open one at a time. This is selective context loading, not implemented eviction or compaction. An optional host fork can isolate the selected workflow, but MDCP does not specify the fork's input envelope, child-result schema or visibility controls. Neither separate workers nor a multi-agent review panel are necessary to this workflow. Its normal owner remains the foreground host agent; whether any isolation actually occurred is unobserved. SRC-1, `skills/mdcp/SKILL.md`; [RT-CLM-context-discipline](runtime.md#rt-clm-context-discipline), [RT-BAP-skill-host](runtime.md#rt-bap-skill-host).

### 3. The contract guides implementation and reconciliation

For a product-code change, the same agent is directed to implement against the documented contract: failing tests first where tests already exist, then passing implementation and refactoring. A documentation-only work item skips this stage. Tests can supply task-specific expected outcomes, but the workflow supplies no universal correct-answer oracle for prose or features. Test choice and semantic review remain agent/repository responsibilities. SRC-1, `skills/mdcp/references/workflows/feature-level.md`.

> 2. Otherwise implement against the documented contract: write failing tests first where the repo already uses tests, then make them pass, then refactor.
> --- `skills/mdcp/references/workflows/feature-level.md`

Next, the agent checks edge cases, performance and design alignment, updates shards to as-built behavior and removes stale references. Removal or renaming invokes the parent skill's repository-wide concept search, including standalone durable guides. Historical records and fixtures have different retention rules; generated-output hits must be repaired in source and recompiled. This is a semantic reconciliation step before submission, not something the compiler can establish from a successful build. SRC-1, `skills/mdcp/SKILL.md`, `skills/mdcp/references/workflows/feature-level.md`; [RT-RTE-feature-work](runtime.md#rt-rte-feature-work).

### 4. Mechanical validation can reject the candidate

The agent runs repository test and documentation commands until they pass. MDCP's parent skill specifies compiling then checking derived documentation and forbids hand-editing generated output. At the tool boundary, shell arguments, config and files enter the deterministic CLI; diagnostics, exit status and written derivatives return. The CLI neither delegates feature design to a model nor verifies that documentation was written before code. SRC-1, `skills/mdcp/SKILL.md`, `skills/mdcp/references/workflows/feature-level.md`, `packages/mdcp-cli/src/cli.ts`; [RT-RTE-compile-check](runtime.md#rt-rte-compile-check).

A concrete rejection path is an orphan finding. Before compilation inside `check`, the CLI checks guide entries and exits nonzero if findings exist. Its diagnostic tells the caller to add shards to an index or remove unused files. Recovery belongs to the agent/caller, which corrects source/indexes and reruns; no automatic semantic repair is performed by this branch. This makes the feature workflow's index-update instruction consequential to the mechanical gate. SRC-1, `packages/mdcp-cli/src/cli.ts`.

> const orphans = checkOrphansForGuides(guideEntries(config, getDocsRoot(opts)));
> --- `packages/mdcp-cli/src/cli.ts`

> if (orphans.length > 0) {
>   console.error('');
>   console.error(
>     `mdcp check failed: ${orphans.length} orphan shard(s). Add them to a guide index or remove unused files.`,
>   );
>   process.exit(1);
> }
> --- `packages/mdcp-cli/src/cli.ts`

If no orphan blocks the check, the CLI compiles, writes outputs and regenerates refs before checking later conditions. Built-in links and configured peers contribute diagnostics; path and coverage policy can also fail. Several failures accumulate, whereas orphan, refs-mismatch and strict-coverage branches exit immediately. In particular, late failure is not transactional rejection of every write: generated files may already have changed. Backup/Git recovery and permissive/disabled-check alternatives are accounted for in [RT-RTE-compile-check](runtime.md#rt-rte-compile-check); a passing result means the selected mechanical checks passed, not that every peer ran or the feature is correct. SRC-1, `packages/mdcp-cli/src/cli.ts`.

> if (failures.length > 0) {
>   reportCheckFailures(failures);
>   process.exit(1);
> }
> console.log('mdcp check passed');
> --- `packages/mdcp-cli/src/cli.ts`

### 5. Delivery is review submission, not proven deployment

The final prescribed handoff records changes under repository communication conventions, creates a changeset if the repository uses Changesets, and submits work for review linked to the work item. Consumer notice of removed behavior goes into release communication rather than perpetuating obsolete instructions in current shards. SRC-1, `skills/mdcp/references/workflows/feature-level.md`.

> 3. Submit work for review and link `WORK_ITEM`.
> --- `skills/mdcp/references/workflows/feature-level.md`

This is the workflow's stated delivery boundary. It does not specify that the reviewer accepted, a merge occurred, a package was published or a user consumed the result. A reviewer may reject the submission under local conventions; MDCP supplies no universal reviewer response protocol or automatic recovery loop after that handoff. The repository's separately wired CI can reject a run through selected checks and a generated-output diff, but actual mandatory merge enforcement remains outside the evidence; see [RT-RTE-release-admission](runtime.md#rt-rte-release-admission).

At workflow end, skill-defined sprawl triggers can require `mdcp review`; findings lead to an offer of doc-review as the next work item, not silent expansion of this feature branch into general cleanup. That maintenance route is distinct from feature delivery and is already retained as [RT-RTE-doc-review](runtime.md#rt-rte-doc-review). Source shards persist for later discovery, but this account establishes neither a later agent's successful read-back nor improved future performance. SRC-1, `skills/mdcp/SKILL.md`.

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

#### On [RT-RTE-feature-work](runtime.md#rt-rte-feature-work)

Workflow role: selected end-to-end representative. Intake, branch isolation, audience-specific shard/index edits, implementation against the documented contract, as-built reconciliation and linked review submission form the prescribed sequence. Handoffs are chiefly between phases owned by one host agent, not between implemented MDCP workers. Delivery ends at submission; reviewer acceptance and deployment are not established. The workflow account above supplies additional doctrine passages without introducing another identity for this route.

#### On [RT-RTE-compile-check](runtime.md#rt-rte-compile-check)

Workflow role: mechanical verification stage, with caller-owned repair. The inspected orphan branch supplies a concrete early rejection, while later failures may occur after output/ref writes. Consequently the feature agent must treat diagnostics as inputs for repair and rerun, not as automatic rollback or semantic acceptance.
