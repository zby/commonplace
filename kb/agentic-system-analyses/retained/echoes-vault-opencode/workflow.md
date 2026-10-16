---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "EchoesVault for OpenCode workflow: explicit session distillation, hash-checked page admission, rejection recovery and local delivery."
run-id: AAS-2026-10-15-echoes-vault-opencode-239c6738bb9e-01
reviewed-boundary: "875c45aa45559529b87a7481b0c21e6dfd8c5eb0"
---

# EchoesVault for OpenCode workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is explicit end-of-session memory saving in an initialized workspace: user request → host-agent distillation → page inspection/hash acquisition → guarded tool invocation → portable writer admission → local acknowledgement and later restoration. This is selected because it connects the shipped command prompt to a concrete multi-page persistence handler and exposes a consequential rejection path. It is not a general software-development workflow or a multi-agent planning system. The enclosing agent's earlier task and reasoning remain external.

Evidence is SRC-1 at the revision fixed in [boundary](boundary.md), implementation and doctrine/design only. Focused inspection covers `prompts/commands/echoes-end.md`, command registration/authorization and finalization in `index.ts`, process transport/error handling in `runtime.ts`, and `prepare_page`, `cmd_end`, `cmd_hash` and generated recovery guidance in `scripts/echoes_vault.py`. This adds workflow-focused coverage within the registered source, not another source or evidence layer. No target execution or tests were performed. The existing referents are [RT-RTE-session-save](runtime.md#rt-rte-session-save), [RT-RTE-page-upsert](runtime.md#rt-rte-page-upsert) and [RT-RTE-context-restore](runtime.md#rt-rte-context-restore); no duplicate workflow records are needed.

### Request, delegation and proposal

1. **User to host agent.** The plugin registers `/echoes-end` with the bundled prompt's `agent: build`. Its command hook records the `end` action under the host session ID. The prompt supplies the distillation objective and page metadata requirements; the enclosing host supplies the session conversation. The package does not construct a separate worker context or transfer the conversation to another agent. Actual host context assembly is uninspected (SRC-1, `index.ts`, `prompts/commands/echoes-end.md`).

2. **Host agent to read/hash tools, then writer.** The host chooses the final summary and optional complete page bodies. Guidance asks for durable outcomes, verified decisions, blockers and next steps rather than a transcript. Replacing a page requires a requested read and a hash call. Reading and semantic verification are instructions to the agent, not mechanically checked prerequisites. A matching hash checks current bytes, not whether those bytes were understood. SRC-1, `prompts/commands/echoes-end.md`, `scripts/echoes_vault.py`:

> Before replacing an existing page, read it and call `echoes_hash_vault_page`; include the returned
> SHA-256 as `expectedSha256`. Then call `commit_memory_to_echoes_vault` exactly once. Never edit
> `EchoesVault/index.md`; the shared runtime generates it.
> --- `prompts/commands/echoes-end.md`

3. **Agent to plugin to engine.** The finalization tool receives `dailySummary` and optional `pages`, with each page carrying filename, complete content and optional expected hash. It checks the session's `end` authorization, passes `--confirm-explicit-user-end`, and sends JSON on stdin. The bridge supplies workspace, `opencode` agent label, adapter version and abort signal, then waits for the Python child. This is delegation to a deterministic executor, not another model. The session grant is not included in the JSON and is not shared across agents. Compatible project-runtime delegation remains the executable-trust condition described by [RT-RTE-runtime-install](runtime.md#rt-rte-runtime-install) (SRC-1, `index.ts`, `runtime.ts`, `scripts/echoes_vault.py`).

### Acceptance, rejection and recovery

The host proposes meaning; the server can veto an unauthorized tool call; Python can veto the payload or proposed page set. `cmd_end` requires explicit confirmation, an initialized vault, a nonempty summary, a page-object array, no obsolete index updates, distinct destinations, valid prepared pages and a renderable prospective index. `prepare_page` checks existing-page hashes. All proposed pages and the prospective index are prepared before the handler starts replacing pages (SRC-1, `scripts/echoes_vault.py`; [RT-RTE-session-save](runtime.md#rt-rte-session-save)).

These are structural and concurrency checks, not an answer oracle. A user requesting finalization does not thereby approve each retained claim. No semantic reviewer is invoked by this handler; whether the host actually verifies its proposed decisions is unobserved. The operating mode is open session distillation, not a bounded experiment.

**Selected rejection: stale replacement hash.** Suppose another cooperating writer changes a page after its hash was obtained. If the submitted hash differs from current content when `prepare_page` checks it, Python raises the concurrency error retained in [RT-RTE-page-upsert](runtime.md#rt-rte-page-upsert). In this preflight rejection, `cmd_end` has not begun its page/index/final-log write sequence. The bridge rejects a nonzero child exit using runtime diagnostics. Because the server deletes authorization only after its awaited call succeeds, this failure leaves the end grant available, unless another lifecycle command supersedes it (SRC-1, `scripts/echoes_vault.py`, `runtime.ts`, `index.ts`).

Recovery belongs to the calling agent or human, not an automatic retry controller. Generated guidance prescribes rereading and reconciling the current page before acquiring a new hash and retrying. Conflict markers or unsupported protocol instead require stopping and reporting (SRC-1, `scripts/echoes_vault.py`):

> 10. On a concurrency error, reread, reconcile, obtain a new hash, and retry. On conflict markers or
>     an unsupported protocol, stop and report the problem.
> --- `scripts/echoes_vault.py`

The prompt's “exactly once” instruction does not establish exactly-once execution: recovery can require another attempt, and the map does not synchronize concurrent calls. Later I/O failure is different from preflight rejection. Page, index, final log and local state are separate replacements; earlier effects can survive a later failure. The package supplies no multi-file rollback here. Recovery then requires checking installed files, refreshing hashes and reconciling before retry, rather than assuming the failed call changed nothing ([RT-RTE-session-save](runtime.md#rt-rte-session-save); SRC-1, `scripts/echoes_vault.py`, `index.ts`).

### What counts as delivered

On the success path, `cmd_end` writes prepared pages, the generated index, a uniquely named final daily entry, and local saved-state metadata, then returns paths, page count and `memorySaved: true`. The bridge resolves stdout only on exit code zero; the tool returns trimmed output and consumes the session grant. This establishes a wired local persistence-and-acknowledgement boundary, not a verified Git commit, remote publication, truthful memory or guaranteed later reliance. The host's subsequent user-facing response is not implemented by this handler (SRC-1, `scripts/echoes_vault.py`, `runtime.ts`, `index.ts`).

Retained results become available to a later session through recent-daily selection and the regenerated page-summary index; targeted search and host-directed full-page reads supply detail. No automatic broadcast transfers the original conversation or private model reasoning to other agents. Delivery into later context is wired, but selection of these particular results, actual consumption and benefit remain unobserved ([RT-RTE-context-restore](runtime.md#rt-rte-context-restore), [RT-BAP-project-context](runtime.md#rt-bap-project-context)). Direct CLI callers can supply the confirmation flag without the plugin grant, and independent upsert/append tools remain separate write paths; this workflow's human-request gate is therefore path-local, not a vault-wide approval guarantee ([RT-CLM-explicit-save](runtime.md#rt-clm-explicit-save)).

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

#### On [RT-RTE-session-save](runtime.md#rt-rte-session-save)

Workflow role: terminal persistence handoff after host-agent distillation. The external host owns proposal quality and any user-facing completion message; Python owns mechanical preflight and write sequencing; the plugin owns its session-local grant. The selected stale-hash branch rejects before this handler's persistence sequence, whereas later I/O failure can leave partial delivery. Thus successful acknowledgement and safe recovery are distinct concerns. No new runtime identity or evidence is asserted here.

#### On [RT-RTE-context-restore](runtime.md#rt-rte-context-restore)

Workflow role: later-session continuation, not part of the finalization acknowledgement. Saved summaries/pages cross the session boundary through selective reload, without carrying the original conversation or automatically resuming its task. Actual continuation remains unobserved.
