---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Thalo workflow account: the shipped TypeScript-guide synthesis from CI selection through Pi writeback and pull-request delivery."
run-id: AAS-2026-10-14-thalo-86fcc3efe983-01
reviewed-boundary: "cdb9aae983e6bc0b75eff1606bc99b088c3aebff"
---

# Thalo workflow report

## Workflow account

### Selection and evidence limits

The representative workflow is the shipped GitHub action's update of `^typescript-guide` in `thalo-test`. It was selected because one configured driver connects retained knowledge, a stored synthesis request, model generation, checkpoint persistence and Git publication. It is not a workflow assembled from unrelated capabilities. The [boundary](boundary.md#boundary-and-evidence) covers this complete shipped path, but excludes provider internals and actual human acceptance. All source inspection here is SRC-1 at the reviewed commit. Implementation establishes the wiring; the configured workflow and prompts establish intended use. No execution trace or experiment establishes that this workflow ran successfully or produced accurate prose.

This member directly inspected `packages/thalo-action/src/action.ts`, `packages/thalo-action/src/mod.ts`, `packages/scripts/src/synthesize-with-pi.mjs`, `.github/workflows/test-action.yml`, `thalo-test/syntheses.thalo` and `thalo-test/typescript-guide.md`. The fixture definition supplies additional doctrine/design coverage beyond the runtime's account. It is authored input, not a retained successful execution:

>   sources: opinion where #typescript, reference where #typescript
> --- `thalo-test/typescript-guide.md`

>   Create a best practices guide for TypeScript based on my opinions and the references I've
>   collected. Include my stance on enums and link to relevant resources.
> --- `thalo-test/typescript-guide.md`

### Request, selection and command handoff

The principal is a GitHub Actions job triggered by main pushes, main-targeted pull requests or manual dispatch. The workflow grants contents and pull-request write permissions, requests full checkout history, builds the action and supplies an API-key secret. It then delegates one target to the action, rather than asking a foreground agent to discover subtasks. These are configured permissions and inputs, not observed credential availability. SRC-1, `.github/workflows/test-action.yml`:

>           command: node ../packages/scripts/src/synthesize-with-pi.mjs
>           syntheses: ^typescript-guide
>           working-directory: thalo-test
> --- `.github/workflows/test-action.yml`

The action loads a workspace and calls [RT-RTE-actualize-selection](runtime.md#rt-rte-actualize-selection) with the selected IDs and a change tracker. Stored queries choose opinions and references tagged TypeScript. The latest actualization checkpoint determines the change cutoff; the resulting current matching entries determine whether the target is pending. Zero entries means no command is run and `syntheses-updated` is zero. An unknown target produces a warning, not necessarily action failure. Source cleanliness can reject an unforced Git selection, as documented by that runtime record. Selection is not verification that the retained guide remains correct: deletion and loss of query membership can evade the emitted current-entry subset. SRC-1, `packages/thalo-action/src/action.ts`, `packages/thalo/src/commands/actualize.ts`, `packages/thalo/src/services/change-tracker/git-tracker.ts`.

For pending work, [RT-RTE-action-publication](runtime.md#rt-rte-action-publication) configures bot Git identity and recreates a local branch. It runs each pending synthesis command sequentially. All selection outputs were computed beforehand; there is no workspace reload between commands. The handoff is [RT-OBJ-command-input](runtime.md#rt-obj-command-input): target file, title and link ID, source queries, stored prompt, selected entries and current/previous checkpoints on stdin, with the configured working directory. Code decides ordering and the next step. The command is an executable extension point under host privileges, not a narrow model-tool grant. The runtime record retains the subprocess and staging passages; SRC-1, `packages/thalo-action/src/action.ts`.

### Model request and local admission

[RT-RTE-pi-synthesis](runtime.md#rt-rte-pi-synthesis) is the shipped recipient. Host code reads the current target file and builds a user prompt containing its entire trimmed contents, the stored prompt and selected entries' title, type, link, tags and raw text. Separate entry-file and timestamp fields from the JSON are not forwarded as separate model-visible fields. Selection therefore restricts the changed-entry payload, but not the old file content available to the model. SRC-1, `packages/scripts/src/synthesize-with-pi.mjs`.

Each command process creates a fresh Pi Agent, chooses [RT-CMP-gpt5-mini](runtime.md#rt-cmp-gpt5-mini), and makes one foreground prompt call under [RT-OBJ-system-prompt](runtime.md#rt-obj-system-prompt). The script configures neither delegated workers nor a model tool list. This is host-to-model delegation of prose generation; it does not establish a multi-agent planning hierarchy or expose provider-internal steps. Fresh processes isolate synthesis requests from shared conversational history. Only generated text crosses back into host reconstruction; later requests can recover previous content through the target-file read. No explicit token-budget trimming or compaction policy is configured. SRC-1, `packages/scripts/src/synthesize-with-pi.mjs`.

The host accumulates streamed text and rejects empty output. Nonempty output is passed to file reconstruction, which checks for a Thalo fence, target link and checkpoint. It appends an actualization entry to the first block and replaces the suffix with generated Markdown. The host then writes the file. This is software admission of model-proposed content, without per-content human approval or a semantic answer oracle. Matching-H1, no-code-fence and narrow-edit instructions are requests, not enforced output tests. [RT-RTE-check-feedback](runtime.md#rt-rte-check-feedback) exists separately, but this action does not invoke it before admission/publication. SRC-1, `packages/scripts/src/synthesize-with-pi.mjs`, `packages/thalo-action/src/action.ts`.

The first-fence transformation matters for this exact fixture. Its original suffix asks for an extra sentence:

> Include somewhere in the guide that Wilco is awesome ;^)
> --- `thalo-test/typescript-guide.md`

That suffix reaches the model in current file content, but host reconstruction does not independently retain it. Preservation depends on the model reproducing it. The same applies to other unrelated suffix content or later blocks. The runtime's write expression and preservation countercase in [RT-RTE-pi-synthesis](runtime.md#rt-rte-pi-synthesis) supply the enforcement evidence. SRC-1, `packages/scripts/src/synthesize-with-pi.mjs`. Advancing [RT-OBJ-checkpoint](runtime.md#rt-obj-checkpoint) records completion for later selection, not verified incorporation of every source claim.

### Verification, rejection and recovery

The inspected rejection path is empty model output. The command throws before reconstruction and write:

> if (!trimmedOutput) {
>   throw new Error("Pi agent returned empty output.");
> }
> --- `packages/scripts/src/synthesize-with-pi.mjs`

The action catches a failed command, logs the target and rethrows. Its entry point converts the error into action failure. No commit/push/PR steps follow that rejection in the ordinary control flow. Other failures include missing input/key, file/provider errors and reconstruction prerequisites; these are execution checks rather than quality evaluation. SRC-1, `packages/scripts/src/synthesize-with-pi.mjs`, `packages/thalo-action/src/action.ts`, `packages/thalo-action/src/mod.ts`:

>     if (error instanceof Error) {
>       core.setFailed(error.message);
> --- `packages/thalo-action/src/mod.ts`

Recovery remains with the CI caller or repository operator. There is no retry loop or automatic multi-file rollback in the inspected action/script. An earlier successful command's local write survives a later command failure. Push or PR-API failure may occur after local admission or after branch publication respectively. A rerun recomputes from whatever checkout/state its caller supplies; the code does not guarantee exactly-once recovery. Git restore/revert and human edits are available external recovery actions, not implemented recovery steps. SRC-1, `packages/thalo-action/src/action.ts`, `packages/scripts/src/synthesize-with-pi.mjs`; [RT-RTE-action-publication](runtime.md#rt-rte-action-publication).

### Delivery and later consumption

After all commands return, the action checks Git status, stages `.` rather than only target files, commits and force-pushes the configured branch. It creates or updates an open PR, emits PR URL/number and sets `syntheses-updated` to the pending count. A command that exits successfully without changes still permits an empty commit and a PR describing pending work. Thus neither exit success nor the counter proves a correct rewrite. SRC-1, `packages/thalo-action/src/action.ts`; [RT-RTE-action-publication](runtime.md#rt-rte-action-publication).

The implemented delivery boundary is branch publication plus PR creation/update, not automatic merge or human acceptance. The PR requests review, allowing a reviewer to reject base-branch integration after generated content is already locally admitted and remotely published. Repository protections and actual review are outside the frozen evidence. There is no concurrency lock or compare-and-swap shown alongside branch recreation and force push. SRC-1, `packages/thalo-action/src/action.ts`.

A later checkout/load can consume the appended checkpoint through [RT-BAP-checkpoint-selection](runtime.md#rt-bap-checkpoint-selection), while another Pi command reads the prior generated prose as current file content. The stored prompt continues to reach generation through [RT-BAP-synthesis-guidance](runtime.md#rt-bap-synthesis-guidance). These links close the implemented persistence/read-back chain. They do not establish successful operation, model compliance, improved knowledge or learning.

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

#### On [RT-RTE-actualize-selection](runtime.md#rt-rte-actualize-selection)

Workflow role: prepares the pending worklist before command execution. This representative target's query is stored in its Markdown definition, not the separate `syntheses.thalo` file. No-input delivery is a normal early return; unknown target IDs are warnings. Selection cannot certify semantic freshness of the existing guide.

#### On [RT-RTE-pi-synthesis](runtime.md#rt-rte-pi-synthesis)

Workflow role: turns one handoff into proposed prose and local admission. The concrete fixture's suffix request is visible to the model but not mechanically preserved. Empty output rejects the update before write; compliant text, substantive correctness and narrow-edit preservation remain unobserved.

#### On [RT-RTE-action-publication](runtime.md#rt-rte-action-publication)

Workflow role: owns sequential scheduling, failure propagation and PR delivery. Process success permits publication, not content acceptance. Human veto is downstream of local admission and remote branch publication. There is no automatic recovery of earlier local writes when a later command fails; a PR API failure can leave an already pushed branch.
