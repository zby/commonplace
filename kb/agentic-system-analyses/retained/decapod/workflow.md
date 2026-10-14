---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Decapod workflow account: host-owned repository change from task custody through exact-candidate validation and verified branch/PR publication."
run-id: AAS-2026-10-14-decapod-c44705119841-01
reviewed-boundary: "067b8f55071e13dd103779998168b4c9ffd31a79"
---

# Decapod workflow report

## Workflow account

### Selection and evidence basis

The representative workflow is a coding agent carrying a repository change from a human request to a verified workbranch and, on GitHub, a verified pull request. It is selected because the shipped agent contract gives an explicit initialization sequence, connects implementation to proof and specifies repair before delivery. The executable publication path implements the final acceptance boundary. This is one prescribed workflow with inspected enforcement points, not a reconstructed successful task or an autonomous agent scheduler (SRC-1, `AGENTS.md`, `src/decapod/core/workspace.rs`; [RT-RTE-workspace-publish](runtime.md#rt-rte-workspace-publish)).

The boundary is the frozen repository revision in this report's frontmatter. All source evidence is implementation or doctrine/design. No host transcript, remote execution result or experiment establishes that an agent followed this sequence, that its product was correct or that the workflow improved outcomes. The runtime baseline supplies the canonical route records; this member adds workflow sequencing and handoff interpretation without redeclaring them.

### Request, ownership and context handoffs

1. **The human gives intent; the host agent owns continuation.** The source prescribes prompt evaluation, documentation ingestion, session acquisition and agent initialization. A blocked prompt requires human review; that is a host obligation, not universal interception of later tools. The code classifies the supplied prompt, while the host must actually invoke it and stop on rejection ([RT-RTE-prompt-eval](runtime.md#rt-rte-prompt-eval)). Decapod does not itself turn a request into model inference and edits. SRC-1, `AGENTS.md`, states:

> Agents act. Decapod governs accepted work. One task may span many ephemeral Decapod invocations; durable state lives in the repository.
> --- `AGENTS.md`

2. **The host establishes task custody before worktree execution.** The contract sequences todo creation/claim, task orientation and `workspace ensure`, then requires the agent to change into the returned workspace. Task identity and agent assignment supply the coordination input; the workspace route can reject ambiguity or competing custody, or return a prepared branch/worktree and guidance. A session is coordination state, not demonstrated human authorization: local reacquisition and alternate RPC/cloud paths qualify the normative session rule ([RT-RTE-session-custody](runtime.md#rt-rte-session-custody), [RT-RTE-workspace-ensure](runtime.md#rt-rte-workspace-ensure)). The ordered handoff is explicit in SRC-1, `AGENTS.md`:

> decapod todo add "<task>" && decapod todo claim --id <task-id>
> decapod infer orientation --task-id <task-id>
> decapod workspace ensure
> cd .decapod/workspaces/<your-worktree>
> decapod constitution get core/DECAPOD
> decapod rpc --op context.resolve
> --- `AGENTS.md`

3. **Decapod supplies context; the host decides how to act on it.** The resolution route accepts task-related query/operation/path/tag inputs and returns doctrine fragments, authored specifications, authority fields and suggested operations. Selection and truncation happen before delivery; neither the fragment limit nor a returned capsule establishes the host's entire inference context. The host must interpret this material, clarify ambiguity or proceed with explicit assumptions ([RT-RTE-context-resolve](runtime.md#rt-rte-context-resolve), [RT-BAP-context-delivery](runtime.md#rt-bap-context-delivery)). The filesystem handoff is not delegation to a fresh reasoning worker. No model-to-model handoff is established for this selected workflow. Source doctrine explicitly preserves agent-held request meaning across workspace isolation (SRC-1, `AGENTS.md`):

> The workspace is the detached filesystem for execution; todos govern ownership, collision avoidance, lifecycle, and handoff.
> --- `AGENTS.md`

### Implementation, evidence and verification handoffs

The agent writes implementation and semantic living-spec prose in the isolated workspace. The contract requires it to preserve intent, boundaries, assumptions, actions and proof through governed trajectory/checkpoint operations. Generated fingerprint or manifest refresh is not a substitute for authored semantic changes. The candidate passed to validation is therefore repository content plus governance and proof material, not the agent's completion assertion. These are source-prescribed authorship duties, not observed updates (SRC-1, `AGENTS.md`; [RT-RTE-validate-candidate](runtime.md#rt-rte-validate-candidate)).

> Stage material, record `decapod govern artifacts checkpoint --id <id> --summary "..."`, then stage governance.json before each commit.
> --- `AGENTS.md`

The host checkpoints and commits, then invokes full workbranch validation. Decapod owns supported projection healing, prerequisite supervision and exact-candidate readiness; the host owns semantic repair and any necessary human clarification. The checks use configured assertions and protocol expectations, not an independently known answer to the open development request. A passing project prerequisite check is insufficient, and CI-local validation explicitly cannot establish publication readiness. Readiness depends on the current committed candidate, accepted target, profile and supported executor; changed material or accepted-base history requires fresh proof ([RT-RTE-validate-candidate](runtime.md#rt-rte-validate-candidate), [RT-OBJ-accepted-executor](runtime.md#rt-obj-accepted-executor)).

A validation failure returns control to the same host on the same workbranch. Its prescribed recovery is to repair the reported cause, checkpoint/commit the changed candidate and revalidate, not start an unrelated task or weaken the gate. A decision requiring new authority or unavailable access must remain a blocker; unsupported controller contracts cannot be repaired merely by repeating the same invocation. These are explicit host instructions in SRC-1, `AGENTS.md`, rather than proof of automatic semantic repair:

> If the report requires unavailable access or a human decision, preserve its exact blocker and obtain that input before continuing.
> --- `AGENTS.md`

### Publication, rejection and delivery

The final handoff is a publication request carrying the current workspace candidate and optional PR title/description. The publisher checks required artifacts, material specs and reviews, the committed bundle, current governance and mergeability, then invokes full readiness immediately before pushing. Even an optional auto-commit occurs before this readiness call, so an earlier candidate's green result is not sufficient. The route performs a normal push of the resolved commit to the selected network destination; Git and the remote service execute external effects. These checks govern this route, not direct shell/Git commands ([RT-RTE-workspace-publish](runtime.md#rt-rte-workspace-publish), [RT-BAP-readiness-gates](runtime.md#rt-bap-readiness-gates); SRC-1, `src/decapod/core/workspace.rs`).

After push, the route reads the exact remote branch/base identities, verifies the remote candidate and, for GitHub, creates or reuses and verifies the matching PR. It rechecks for remote movement while the PR was being verified. A push exit status is not the acceptance oracle. The terminal result carries branch, commit, redacted remote, remote-verification and PR-verification fields, plus warnings. On a non-GitHub destination it can deliver a verified branch while explicitly withholding a publish-ready PR claim (SRC-1, `src/decapod/core/workspace.rs`; [RT-RTE-workspace-publish](runtime.md#rt-rte-workspace-publish)).

> Branch verified remotely; PR verification is unavailable for this non-GitHub remote. This is not a publish-ready PR.
> --- `src/decapod/core/workspace.rs`

A consequential failure occurs **after the external effect**: a successful push followed by failed remote/PR verification is still incomplete publication. The inspected `after_push` wrapper returns a recovery error rather than rolling the remote branch back. The host must preserve the branch, reconcile exact remote state, repair/revalidate as necessary and retry; matching PR reuse supports recovery without duplication. Remote movement can independently reject verification (SRC-1, `src/decapod/core/workspace_publication.rs`):

> "PUBLICATION_INCOMPLETE: branch was pushed, but publication is not verified. {error}\nRepair the reported condition and retry `decapod workspace publish`; existing matching PRs are reused. Do not force-push, delete the branch, or report the PR ready."
> --- `src/decapod/core/workspace_publication.rs`

> "REMOTE_PUBLICATION_RACE: remote head or base changed during verification; fetch, reconcile, validate, and retry."
> --- `src/decapod/core/workspace_publication.rs`

Thus delivery in this selected workflow means a verified publication result at a particular candidate and remote state, not merged acceptance, deployment, demonstrated semantic correctness or an observed user-facing success. Automatic todo closure and a final conversational response were not traced here; neither is silently treated as part of the verified-publication result.

### Added inspection and limits

Added direct inspection under SRC-1 comprises the complete `AGENTS.md` agent contract (doctrine/design), `src/decapod/core/workspace.rs` publication passage at lines 2100–2237, and `src/decapod/core/workspace_publication.rs` lines 1–115 covering incomplete-publication handling, bounded transport and remote movement detection (implementation). Other mechanisms above rely on the cited supplied runtime records. These reads extend coverage within the registered commit; they add no source or observed-run evidence. Provider internals, complete remote proof/retry state machines and arbitrary host behavior remain outside this selective trace. Their uncertainty prevents end-to-end reliability and universal host-compliance conclusions, not the narrower publication wiring finding.

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

#### On [RT-RTE-workspace-ensure](runtime.md#rt-rte-workspace-ensure)

Workflow role: transfers task custody into an execution location. The host must enter that location and continue the task; preparation alone does not perform implementation or create a separate model conversation.

#### On [RT-RTE-validate-candidate](runtime.md#rt-rte-validate-candidate)

Workflow role: repair boundary between a committed candidate and admissible publication. A recoverable rejection transfers the next semantic action back to the host on the same branch. A human decision or access blocker interrupts progression rather than becoming an implicit pass.

#### On [RT-RTE-workspace-publish](runtime.md#rt-rte-workspace-publish)

Workflow role: terminal external-effect and acknowledgement boundary for this trace. Recovery must distinguish pre-push rejection from post-push incomplete verification: the latter can leave durable remote effects despite a failed invocation. Verified PR publication is the selected endpoint; merge and deployment are not implied.
