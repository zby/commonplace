---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "OKF Harness workflow account tracing source-revision reconciliation through agent edits, structural checking, edge acknowledgment and later evidence use."
run-id: AAS-2026-10-15-okf-harness-6bf5507fbdbf-01
reviewed-boundary: "0dd4f806c454a68088c5a3e64b4cbebbe2c216be"
---

# OKF Harness workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is **reconciling a registered source revision with the wiki**. It is selected because one shipped procedure connects a concrete diagnostic, source reading, model-owned knowledge changes, deterministic verification and an explicit completion acknowledgment. It also exposes a consequential failure boundary: mechanical acknowledgment does not certify the preceding semantic work. This is the workspace-local guidance route, not an assertion that every host integration delivers the same procedure. Its canonical route is [RT-RTE-source-reconcile](runtime.md#rt-rte-source-reconcile); the instruction-delivery limit is [RT-CLM-delivery-ceiling](runtime.md#rt-clm-delivery-ceiling).

The account uses SRC-1 at the boundary's frozen commit. Additional selective inspection covers the full reconciliation implementation and procedure, workspace skill, Check Workflow, check pipeline and CLI maintenance-loop test: `packages/core/src/source/reconciliation.ts`, `packages/agent-pack/templates/okf-harness/references/reconcile.md`, `packages/agent-pack/templates/okf-harness/SKILL.md`, `packages/agent-pack/templates/okf-harness/references/check.md`, `packages/core/src/check/index.ts`, and `packages/cli/test/maintenance-loop.test.ts`. Code and test definitions supply implementation evidence; shipped instructions supply doctrine/design. No target commands, tests, host agents or models were executed. No successful model-authored reconciliation or downstream answer is observed.

### 1. Request routing and diagnostic handoff

The user supplies the maintenance request. The enclosing agent classifies it as reconciliation, resolves the workspace through `okfh.config.yaml`, and loads that workflow's reference. For a combined request, the workspace skill requires one workflow at a time in user order, inspection of command JSON before choosing the next action, and stopping before the next workflow on command failure. This is instruction-governed sequencing by the same host agent, not a target-owned scheduler or a separate worker invocation. SRC-1: `packages/agent-pack/templates/okf-harness/SKILL.md`; [RT-BAP-workflow-guidance](runtime.md#rt-bap-workflow-guidance).

The precondition is a suspected-revision edge reported by check, or an unsealed currency report with a dangling prior/revision pair. The pair is a **mechanical revision suspicion**, not a model-verified equivalence: core groups registered file sources by original filename and compares each earlier differing-hash sibling with the latest entry. Check exposes pending edges that have a promoted reference on either endpoint, including the promoting paths. The handoff therefore carries source IDs and affected-reference pointers, not a source-body comparison or a proposed semantic patch. SRC-1: `packages/core/src/source/reconciliation.ts`, `packages/core/src/check/index.ts`.

> * File sources sharing an original filename form a group in added order; the latest
> * entry is the suspected revision of each earlier sibling with a different hash.
> --- `packages/core/src/source/reconciliation.ts`

The workspace root scopes operations; the exact prior and revision source IDs identify the obligation. The agent can list sources to resolve their recorded paths. Nothing here creates an isolated model context: the skill asks for just-in-time reference loading, while the host retains responsibility for its own context and tools. SRC-1: `packages/agent-pack/templates/okf-harness/references/reconcile.md`, `packages/agent-pack/templates/okf-harness/SKILL.md`.

### 2. Semantic work remains with the enclosing agent

The agent must read both registered revisions and inspect every affected wiki document. It must edit the affected reference, concept, index or log files, leaving raw copies and the harness-managed ledger untouched. Reading the two versions supplies the semantic evidence missing from the diagnostic. No model sub-agent receives a bounded task packet and returns a review: the handoff is from deterministic diagnostic output to the enclosing agent's reading and editing decisions. SRC-1: `packages/agent-pack/templates/okf-harness/references/reconcile.md`; [RT-RTE-source-reconcile](runtime.md#rt-rte-source-reconcile).

> Reconcile means the wiki reflects the revision; reviewing it is not reconciliation.
> --- `packages/agent-pack/templates/okf-harness/references/reconcile.md`

The procedure requires direct revision of all affected concept prose. It says omission alone does not establish removal: a positive textual signal is needed to treat removal as suspected. Destructive replacement is not by itself grounds to stop; the agent should complete the update and disclose which prior claim will no longer be served. The workspace stop contract reserves questions for information that, after reading available source and wiki evidence, exists solely in the user's head. If the information is unavailable both in the workspace and to the user, the agent should preserve the unknown rather than guess or ask an unanswerable question. These are decision policies, not code-enforced semantic admission checks. SRC-1: `packages/agent-pack/templates/okf-harness/references/reconcile.md`, `packages/agent-pack/templates/okf-harness/SKILL.md`.

### 3. Verification precedes acknowledgment, but does not gate the writes

After editing, the procedure requires check and resolution of edit-caused findings before acknowledgment. At this point prose should reflect the revision while the known edge remains pending. The check implementation reloads a workspace snapshot and composes lint, currency and the check verdict. It separates OKF conformance failures (`blocked`) from Harness findings (`needs_attention`); absence of either produces `ready`. This verifies represented structure and integrity facts, not whether the agent correctly interpreted every source claim. No reference answer or semantic outcome oracle is supplied. SRC-1: `packages/agent-pack/templates/okf-harness/references/reconcile.md`, `packages/core/src/check/index.ts`, `packages/agent-pack/templates/okf-harness/references/check.md`.

> Run `okfh check --workspace <workspace> --json` after the edits and resolve edit-caused findings before continuing.
> --- `packages/agent-pack/templates/okf-harness/references/reconcile.md`

Because edits precede check, a check failure is not rejection before persistence. The same agent must repair its edits and recheck under the procedure; the workflow does not wire an automatic rollback. Explicit Git checkpoint/restore is a separate caller-selected recovery path, with the clean-state and scope limits in [RT-RTE-workspace-recovery](runtime.md#rt-rte-workspace-recovery). The procedure does not automatically create a checkpoint before semantic changes. SRC-1: `packages/agent-pack/templates/okf-harness/references/reconcile.md`.

### 4. Mechanical rejection and recovery ownership

The final command receives only the workspace, prior source ID, revision source ID and judgment note. Core validates the manifest, confirms both registered IDs, trims and rejects an empty note, checks that the exact suspected edge exists, and rejects invalid ledger rows before appending an acknowledgment. It also rejects a configured ledger destination beneath an immutable raw root. These are computational vetoes. They do not review the changed wiki or receive evidence of the agent's source reading. SRC-1: `packages/core/src/source/reconciliation.ts`; [RT-RTE-source-reconcile](runtime.md#rt-rte-source-reconcile).

> "Reconciliation requires a non-empty judgment note."
> --- `packages/core/src/source/reconciliation.ts`

For example, a whitespace-only judgment note throws `RECONCILIATION_NOTE_REQUIRED` before the append. The agent must supply a substantive note and retry; no automatic retry policy is implemented in this function. Earlier wiki edits remain a separate effect. Invalid IDs or an unknown pair likewise require correcting the requested pair rather than treating the prior check as completion. If a failure leaves needed user intent unresolved, the stop contract governs escalation; it is not permission to invent a revision identity. SRC-1: `packages/core/src/source/reconciliation.ts`, `packages/agent-pack/templates/okf-harness/SKILL.md`.

There is no separate reviewer or mandatory per-claim human approval in the shipped procedure. The host agent proposes and adopts prose under the open maintenance request; core can veto acknowledgment format and identity but not the semantic replacement. Actual user approval controls beyond the specified stop contract depend on the external host. SRC-1: `packages/agent-pack/templates/okf-harness/references/reconcile.md`; [RT-RTE-source-reconcile](runtime.md#rt-rte-source-reconcile).

### 5. Delivery and later consumption

Success appends a JSONL acknowledgment containing the exact prior/revision IDs and note beside the manifest, then returns the workspace, ledger path and acknowledgment. The procedure makes receipt of the same edge-specific acknowledgment its terminal condition, not merely a successful review or a check result. The workspace skill separately requires reviewing and naming changed files before the final response, and reporting the post-edit check status. SRC-1: `packages/core/src/source/reconciliation.ts`, `packages/agent-pack/templates/okf-harness/references/reconcile.md`, `packages/agent-pack/templates/okf-harness/SKILL.md`.

> The reconciliation is complete only when the final reconcile verb returns the edge-specific acknowledgment.
> --- `packages/agent-pack/templates/okf-harness/references/reconcile.md`

Two retained outputs have different consumers. The ledger acknowledgment removes that exact pair from subsequent dangling-edge calculations. The edited wiki prose reaches later retrieval and answering through [RT-RTE-evidence-answer](runtime.md#rt-rte-evidence-answer). Clearing an edge is not itself rewriting the wiki, and an unacknowledged revision is not the same as a missing-source evidence seal. SRC-1: `packages/core/src/source/reconciliation.ts`, `packages/core/src/check/index.ts`, `packages/cli/test/maintenance-loop.test.ts`.

The maintenance-loop test makes this distinction concrete as a test definition: after registering a changed source it expects an unsealed currency report and unchanged eligible evidence; it then calls reconciliation with a note, without an intervening wiki rewrite in that test body, expects currency to become sealed, and expects the evidence concept IDs to remain unchanged. Separately, its missing-source branch expects affected concepts to be withheld. This corroborates the intended difference between acknowledgment bookkeeping and source-damage withholding; it does not demonstrate a semantically correct update, model compliance or a passing test run. SRC-1: `packages/cli/test/maintenance-loop.test.ts`.

> expect(sealedCurrency.result.data.currency).toMatchObject({ sealed: true, dangling: [] });
> --- `packages/cli/test/maintenance-loop.test.ts`

Thus delivery has a precise protocol marker, but semantic completion still depends on the enclosing agent having honored the preceding read/edit/check obligations. The source establishes a coordinated workflow and a mechanical completion receipt, not verified end-to-end knowledge correctness or demonstrated downstream benefit.

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

#### On [RT-RTE-source-reconcile](runtime.md#rt-rte-source-reconcile)

Workflow role: the representative maintenance workflow, with diagnostic-to-agent, agent-to-check and agent-to-acknowledgment handoffs. Semantic completion is requested before the terminal command; mechanical delivery is the returned acknowledgment matching both endpoint IDs. The agent owns repair of edit-caused check findings and correction of rejected acknowledgment requests. There is no separate reviewer handoff in this selected procedure. A nonempty note permits recording a judgment, not validating its truth.

#### On [RT-RTE-workspace-recovery](runtime.md#rt-rte-workspace-recovery)

Workflow role: an available explicit recovery alternative, not a step automatically invoked by the selected reconciliation procedure. A rejected acknowledgment does not automatically invoke restore or remove the agent's already-persisted wiki edits.
