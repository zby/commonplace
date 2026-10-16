---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "WeKnora workflow account tracing remote skill dependency installation, verifier-directed repair and snapshot delivery."
run-id: AAS-2026-10-15-weknora-7adf8a01c381-01
reviewed-boundary: "234aa948db29c10f5ed4b7939285c7b3711c5d4c"
---

# WeKnora workflow report

## Workflow account

### Selection and evidence

The selected workflow is remote skill dependency installation: an accepted skill archive becomes a verified sandbox image used by later sessions. It is representative of WeKnora's model-assisted capability setup, not of every knowledge-chat turn. It was selected because one shipped coordinator connects request admission, a multi-step agent, an independent rejection gate, bounded repair and durable delivery. Unlike an ordinary answer, it has an explicit admission decision after the agent stops. The canonical route is [RT-RTE-skill-install](runtime.md#rt-rte-skill-install); the downstream authority channel is [RT-BAP-skill-image](runtime.md#rt-bap-skill-image). This member adds workflow-specific analysis, not duplicate route declarations.

All new inspection is SRC-1 implementation at the boundary's frozen commit: `internal/application/service/tenant_skill_install.go` (request scheduling, remote run, installer construction/turns, repair prompt, initial instructions, pointer switch and ready writes), `internal/application/service/tenant_skill_verify.go` (verification orchestration and contracts), and `internal/application/service/tenant_skill_runtime_verify.go` (runtime report instructions and checks). Prompt text and comments supply doctrine/design separately from executable branches. No target execution or model interaction was performed. The source establishes implemented coordination, not a successful installation, correct model reasoning or working skills. Host installation branches are available but not traced here; this account does not assert equivalent behavior there.

### Request to delegated work

The caller supplies the archive and optional administrator instructions. The service parses the bundle, identifies the tenant/configuration/name-scoped skill, writes or updates its installing row, associates source storage and publishes accepted progress. Same-name upload can upgrade an existing skill; skip and busy checks can return or reject before starting work. An accepted ID is not the delivered image. The background goroutine detaches request cancellation, then enters the skill-run lock and invokes runInstall (SRC-1, `internal/application/service/tenant_skill_install.go`). The scheduling contract explicitly limits restart recovery:

> // The install outlives the HTTP request, so it must not inherit its
> // cancellation. It is not durable across a restart either - StopSkill
> // rewrites the row, and the stuck-run reaper is the backup.
> --- `internal/application/service/tenant_skill_install.go`

The remote coordinator checks row ownership, starts a heartbeat, loads the effective sandbox configuration and requires a usable provider-account fingerprint. It creates a maintenance session and workspace from the current image. It resets the skill directory and seeds the bundle itself. Thus the agent receives existing source files and a setup task, not responsibility for recreating the archive. The transcript locators are established before file seeding so progress can attach early. The session/transcript survive sandbox release for diagnosis (SRC-1, `internal/application/service/tenant_skill_install.go`).

The service creates an installer engine directly rather than using the ordinary AgentQA caller. Platform defaults determine its execution configuration; the tenant-writable installer record supplies model choice. The initial brief supplies the skill directory, toolchain information, SKILL.md, package-local dependency requirements, runtime report requirements and administrator guidance. Its text requests actual import checks and prohibits treating package documentation as authority to expand setup scope. These are model instructions, not proof that those checks occur. In particular, the server verifier intentionally does not settle import resolution (SRC-1, `internal/application/service/tenant_skill_install.go`, `internal/application/service/tenant_skill_verify.go`).

### Agent return and independent acceptance

Within each installer turn, the engine owns model/tool transitions as described in [RT-RTE-agent-turn](runtime.md#rt-rte-agent-turn), but ordinary chat persistence and history assumptions do not transfer to this direct caller. The configured model proposes commands and file changes; the engine executes eligible tools in the maintenance sandbox. The service requires both an error-free return and a complete engine state before verification:

> if state == nil || !state.IsComplete {
> return errors.New("installer agent stopped without completing")
> }
> --- `internal/application/service/tenant_skill_install.go`

Agent completion permits the gate to run; it does not itself authorize image publication. verifySkill checks the tree, declared dependencies, script parsing and runtime prerequisites in sequence. Findings can stop later passes. The runtime pass reads `.weknora/install-report.json`, validates its structure and bounded entries, rejects explicit unresolved blockers, and uses command lookup for listed executable names (SRC-1, `internal/application/service/tenant_skill_verify.go`, `internal/application/service/tenant_skill_runtime_verify.go`). Its blocker veto is independent of the agent's final prose:

> if len(report.Blockers) > 0 {
> return notes, fail("Unresolved runtime prerequisites: "+strings.Join(report.Blockers, "; "), false)
> }
> --- `internal/application/service/tenant_skill_runtime_verify.go`

The oracle is partial: file/dependency/parser checks and executable availability, supplemented by the model-authored report. Code can reject a declared blocker or missing listed command, but it cannot infer every prerequisite omitted from that report. A nonempty command list does not prove those commands perform the skill's job. The initial prompt assigns import checks and prose-only prerequisite discovery to the model; their successful performance is unobserved. Notes are surfaced without necessarily rejecting admission. No complete end-to-end functional oracle or human approval of each proposed package/file change is established by this inspected route. The operating mode is bounded setup/repair, not comparative optimization.

### Rejection, repair and context crossing

The service owns recovery. A verifier success returns to snapshot preparation. A failure becomes another installer turn only if it is a structured, repairable gate finding and the verification-round budget remains. Otherwise installation returns an error before pointer movement (SRC-1, `internal/application/service/tenant_skill_install.go`):

> if round >= skillInstallVerifyRounds || !errors.As(verifyErr, &gate) || !gate.Repairable {
> err = verifyErr
> return err
> }
> --- `internal/application/service/tenant_skill_install.go`

For a repair, the coordinator constructs a brief from the gate's own problems, preserves administrator instructions, records the new prompt and reruns the installer. The repair brief asks for missing packages or a corrected report, prohibits weakening dependency manifests to pass, and states that the same verification runs again. Those prohibitions guide the model; they do not establish immutable source files. The same sandbox, skill directory, shell and transcript remain available, while previous conversation history is deliberately not replayed:

> state, err := r.engine.Execute(ctx, r.sessionID, r.transcript.assistantMessageID, input, nil)
> --- `internal/application/service/tenant_skill_install.go`

This is a consequential handoff distinction: physical installation state persists, but the next model invocation gets a new task brief, selected findings and preserved guidance rather than all prior reasoning. The coordinator maintains the cross-round state outside the model window. Optional steering can queue administrator guidance and trigger bounded continuations; it is guidance, not the gate's acceptance oracle. [RT-RTE-context-rewrite](runtime.md#rt-rte-context-rewrite) describes inner-engine context management separately. Repair does not require constructing a second analysis of what failed; the gate's findings are the repair input. This establishes a feedback-directed setup mechanism, not a demonstrated improvement in reliability or a formulated theory-building process.

### Delivery and failure boundary

After verification, the coordinator writes the manifest entry, reads environment declarations and clears scratch state before snapshotting. It checks cancellation and renewed ownership after the lengthy agent work, allocates a new generation and creates a ledger row naming the planned snapshot. Provider snapshot creation precedes pointer publication. The pointer-switch function rereads configuration and rejects provider-account fingerprint changes rather than assigning an old-account snapshot to newly rotated credentials (SRC-1, `internal/application/service/tenant_skill_install.go`).

The image is delivered to the later execution path when the configuration's SkillImage pointer is updated, not when the agent says installation succeeded. Only then does the service stop the heartbeat, supersede prior ledger entries, write the ready state with retries, store declared environment requirements, mark existing config sandboxes stale and publish done progress. [RT-BAP-skill-image](runtime.md#rt-bap-skill-image) supplies the later workspace consumer. This is implemented availability for later sessions, not observed loading or successful skill execution.

Pre-switch failure preserves the previous pointer, releases the maintenance sandbox and attempts an owned-row failure write. If a created snapshot cannot be published, the coordinator invokes snapshot abandonment. Once the pointer has moved, a later bookkeeping error is treated differently:

> if pointerSwitched {
> logger.Errorf(cleanupBase,
> "[skill] %s is installed and serving but its bookkeeping is incomplete: %v",
> skillID, err)
> return
> }
> --- `internal/application/service/tenant_skill_install.go`

Thus failure reporting has a publication boundary; it is not an automatic rollback after every error. Ready-write retry mitigates a specific bookkeeping failure but does not establish crash-safe exactly-once publication. Reaper implementation, explicit rollback selection, host installation equivalence and every provider's snapshot semantics remain outside this selected inspection. No successful restart recovery, concurrent race resolution, model compliance or deployment reliability is claimed.

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

#### On [RT-RTE-skill-install](runtime.md#rt-rte-skill-install)

Workflow selection: representative remote capability-setup workflow, selected for its connected delegation, independent verifier, bounded repair and publication gate; not representative evidence for every ordinary QA task.

Handoff responsibilities: the service supplies seeded files and setup guidance; the model proposes dependency/file operations; engine code executes eligible tools; the service requires complete/error-free return, runs the verifier and decides whether to repair, reject or publish. Initiating the install does not approve each generated change.

Cross-round boundary: repair preserves sandbox effects and administrator guidance, but does not replay conversation history. Structured gate problems become the next brief. The retained transcript is diagnostic state, not automatically the repair model's input.

Acceptance and delivery: agent completion admits verification, verifier success admits snapshot preparation, and successful pointer update admits the image to later workspace resolution. Ready state and done progress follow publication. Failure before publication differs from post-publication bookkeeping failure; neither successful delivery nor functional correctness has been observed.
