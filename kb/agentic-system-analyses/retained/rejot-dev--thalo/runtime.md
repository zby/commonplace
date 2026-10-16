---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Thalo runtime baseline: deterministic context selection, shipped Pi synthesis writeback, Git publication and alternate authoring paths."
run-id: AAS-2026-10-14-thalo-86fcc3efe983-01
reviewed-boundary: "cdb9aae983e6bc0b75eff1606bc99b088c3aebff"
---

# Thalo runtime report

## Runtime account

### Evidence and claimed work

Thalo supplies structured plain-text knowledge, schema feedback, queries and synthesis context preparation. Its CLI is not itself an autonomous model loop. Its shipped action and Pi command extend preparation into model-generated file changes and a pull request. This account covers those paths within the [frozen boundary](boundary.md#boundary-and-evidence). All source evidence below is SRC-1 at the reviewed commit: executable text supplies implementation evidence; README, skill and prompt text supply declared guidance. No execution trace or experiment was supplied or performed. Operation, model compliance, synthesis quality and benefit remain uninspected, not established negatives.

The source's feedback-loop claim is [RT-CLM-agent-feedback](#rt-clm-agent-feedback). The concrete feedback surface is [RT-RTE-check-feedback](#rt-rte-check-feedback); it checks structure, not the truth of knowledge. Authored instructions ask a collaborating agent to run it, but the synthesis action does not call it before committing. Thus a diagnostics facility is not a universal admission gate.

Additional inspected coverage beyond the boundary's initial reads includes the complete Node tracker factory and Git tracker, loader, query command, action entry point and Pi script; checker rule-dispatch code; CLI check/init/merge commands; bounded formatter writeback and LSP lifecycle ranges; and the complete playground runner. Anchors are SRC-1, `packages/thalo/src/services/change-tracker/create-tracker.ts`, `packages/thalo/src/services/change-tracker/git-tracker.ts`, `packages/thalo/src/vfs/loader.ts`, `packages/thalo/src/commands/query.ts`, `packages/thalo/src/checker/check.ts`, `packages/thalo-action/src/mod.ts`, `apps/thalo-cli/src/commands/format.ts`, `packages/thalo-lsp/src/server.ts`, and the paths in the records below. These are implementation inspection, not successful test or deployment evidence. Individual checker-rule correctness, parser internals and merge semantics are not exhaustively audited here.

### Ordinary shipped synthesis invocation

The supplied workflow triggers on main pushes, pull requests and manual dispatch. Its principal is a GitHub Actions job, not a human approving each generated passage. It grants contents and pull-request write permissions, checks out full history, builds the action and selects `^typescript-guide` in `thalo-test`. The model API key is supplied through the job environment. These are configured grants, not evidence that credentials were present or the job ran. SRC-1, `.github/workflows/test-action.yml`.

The action entry point reads caller configuration. Node file loading recursively discovers `.thalo` and `.md`, ignoring hidden segments, node_modules and symlinks, and parses them into a workspace. A scratch workspace is populated before replacing the target workspace's derived maps; this is a load-time state commit, not a transaction around later disk writes. SRC-1, `packages/thalo-action/src/mod.ts`, `packages/thalo/src/files.ts`, `packages/thalo/src/vfs/loader.ts`.

The action calls [RT-RTE-actualize-selection](#rt-rte-actualize-selection). Code owns the next step: find definitions, optionally match target IDs, find the latest actualization by target ID and formatted timestamp, parse its checkpoint, then ask the tracker for matching changed entries. Synthesis queries and checkpoints are symbolic decisions; the synthesis prompt is natural-language guidance. `isUpToDate` means zero returned entries, not that the existing prose remains correct. The action computes all selected outputs before running update commands; it then processes pending syntheses sequentially. It does not reload after each command. SRC-1, `packages/thalo/src/services/synthesis.ts`, `packages/thalo/src/commands/actualize.ts`, `packages/thalo-action/src/action.ts`.

[RT-RTE-pi-synthesis](#rt-rte-pi-synthesis) receives JSON on stdin. Its host, rather than a model-selected tool, reads the target file and supplies its entire trimmed content, the synthesis prompt, and selected entry raw text plus title/type/link/tags. The JSON also carries provenance fields such as file and timestamp, but the Pi user-prompt formatter does not forward them as separate fields. The current file can contain material outside the changed-entry subset. This is host-driven context selection, not model retrieval, compaction or a demonstrated token-budget policy. Each process creates a new Agent and makes one foreground prompt call; Thalo does not configure a delegated worker or a tool list in that constructor. Pi/provider internal behavior remains outside the frozen source.

The distributed-parametric component is [RT-CMP-gpt5-mini](#rt-cmp-gpt5-mini). The model proposes Markdown under the stored prompt and fixed system guidance. Host code collects streamed text deltas, rejects an empty result, reconstructs the file around its first Thalo fence, appends a checkpoint and writes the result. This admits nonempty model text without a schema recheck or per-content human approval. Stored content subsequently reenters synthesis through the host's existing-file read; checkpoint state reenters through workspace reload. These are wired read-back paths, not observed activation or learning.

[RT-RTE-action-publication](#rt-rte-action-publication) owns coordination and terminal publication. It recreates a local branch, executes each configured command, stages the whole working tree, commits, force-pushes the branch and creates or updates a PR. A command failure aborts publication, but earlier local writes are not rolled back. Git history offers external recovery; automatic content rollback is not implemented in this path. PR review can reject base-branch integration, but it happens after local admission and branch publication. The action's terminal outputs are PR URL/number and a count of pending syntheses, not an independently verified count of correct rewrites.

### Alternate and forcing routes

Three forcing cases delimit the ordinary path's guarantees.

1. **Changed is not complete dependency invalidation.** The Git tracker compares current matching entries against a checkpoint commit and can detect in-place edits. Deleted entries have no current entry to return. Existing entries that cease matching a query are also excluded by the current-query predicate. The ignored-revision branch uses blame/ancestry instead of entry equality; missing checkpoint commits replay all matching entries. Timestamp fallback instead selects entries strictly newer than its checkpoint and explicitly cannot detect in-place edits. These alternatives prevent an unconditional claim that every knowledge change triggers an accurate synthesis refresh. SRC-1, `packages/thalo/src/services/change-tracker/git-tracker.ts`, `packages/thalo/src/services/change-tracker/timestamp-tracker.ts`.

2. **Update scope is weaker than the prompt requests.** The Pi system prompt says to preserve unrelated content, but `updateSynthesisFile` preserves only the prefix before the first Thalo block and that block with an appended actualization. It replaces everything after the first closing fence with generated Markdown. It neither locates the definition by target ID nor preserves later Thalo blocks. Existing-file inclusion may encourage the model to reproduce unrelated content, but does not enforce preservation. Multiple blocks or unrelated suffix content therefore force a materially different result from the stated narrow-edit guidance. SRC-1, `packages/scripts/src/synthesize-with-pi.mjs`.

3. **The configured command is broader than a model tool grant.** Any caller-supplied command receives stdin and runs in the working directory with host process privileges. The action stages `.` rather than only selected synthesis files. There is no Thalo path allowlist or content-approval gate on this extension route. The shipped Pi command performs host filesystem I/O and a model request; a replacement command can have different effects. External OS/GitHub isolation and credential policies determine the actual envelope. SRC-1, `packages/thalo-action/src/action.ts`, `packages/thalo-action/action.yml`, `.github/workflows/test-action.yml`.

The CLI alternate prints prompts, changed entries and customizable instructions; it stops before model execution or file admission. It supports `--force`, bypassing the Git tracker's source-file cleanliness check. Direct library `runActualize` calls can provide a tracker or receive timestamp fallback. The browser runner uses that fallback and displays instructions containing `updated: <current-timestamp>` rather than the `checkpoint` metadata the actualize command reads. This mismatch prevents assuming that following those display instructions advances the selector's checkpoint. These alternatives are part of [RT-RTE-actualize-selection](#rt-rte-actualize-selection), not guarantees inherited from the action. SRC-1, `apps/thalo-cli/src/commands/actualize.ts`, `apps/docs/app/components/playground/thalo-runner.ts`, `packages/thalo/src/commands/actualize.ts`.

Direct edits, schema changes, initialization, formatting and Git merge-driver writes are additional admission mechanisms, described in [RT-RTE-local-authoring](#rt-rte-local-authoring). They need not pass through the model, tracker or action. LSP and browser hosts maintain derived workspaces and expose feedback but do not establish author approval or durable disk saves. LSP open-buffer changes take precedence over external create/change notifications; closing a document reloads disk content. No general model-output guarantee follows from editor diagnostics. SRC-1, `packages/thalo-lsp/src/server.ts`, `apps/docs/app/components/playground/thalo-runner.ts`.

### Load-bearing guarantee boundaries

| Mechanism and owner | Strength and enforcement point | Covered paths and exceptions | Required external contract | Conclusion status |
| --- | --- | --- | --- | --- |
| Source cleanliness, Git tracker | Invariant of the guarded call: throws on uncommitted files currently containing query matches when force is false | Action's default Git tracker and unforced CLI Git path; not forced CLI, timestamp, arbitrary tracker or direct file write | Git status and workspace/file correspondence | implementation conclusion status: wired; operation conclusion status: uninspected |
| Structural feedback, checker/CLI | Protocol: active rule visitors and syntax diagnostics; CLI exits 1 on errors | Explicit checks and editor feedback; rules can be disabled or regraded; not automatically required by action/Pi writeback | Parsed workspace and caller choosing/obeying feedback | implementation conclusion status: wired; operation conclusion status: uninspected |
| Preserve unrelated synthesis content, Pi prompt | Policy: natural-language request; host reconstruction has narrower preservation than requested | Shipped model request only; first-fence suffix replacement is the countercase; arbitrary commands are separate | Model compliance, correct input layout and appropriate output | request conclusion status: wired; preservation conclusion status: claimed; operation conclusion status: uninspected |
| Publish only after commands return, action | Protocol: sequential awaited subprocesses before commit/push | Ordinary action; local writes before failure remain; successful exit is not content validation | Subprocess exit semantics, Git, GitHub token/API | implementation conclusion status: wired; operation conclusion status: uninspected |
| Human review before base-branch integration | Policy: PR body asks review; action does not merge PR | Branch publication is already automatic; manual/local paths do not require PR | Repository protection and human decisions are external | request conclusion status: wired; deployment conclusion status: uninspected |

The capability surface is therefore filesystem-backed text and schema manipulation, deterministic selection, configured subprocess execution, model generation and Git publication. The current shipped grant configuration enables write-capable CI and supplies an API key, with no per-content approval before branch publication. Deployed isolation and actual permissions remain uninspected. This distinction avoids treating either a prompt restriction or an unconfigured model-tool list as an OS sandbox. Supporting records below retain the enforcement passages.

## Shared records

### Components

#### RT-CMP-gpt5-mini
Label: Shipped OpenAI gpt-5-mini synthesis model

Source-native identity: provider `openai`, model name `gpt-5-mini`, resolved through imported `getModel`. Representational form: distributed-parametric. Storage substrate: external provider parameters; the repository stores the selector strings, not the weights. SRC-1, `packages/scripts/src/synthesize-with-pi.mjs`.

> const provider = "openai";
> const modelName = "gpt-5-mini";
> --- `packages/scripts/src/synthesize-with-pi.mjs`

Parameters changing during operation: uninspected — no Thalo training/update call appears in the inspected script, but provider internals are outside the source. Exact parameter version pinned: no exact immutable weight/version identity is supplied by these selector strings. Whether a mutable endpoint resolves to another model: uninspected — provider resolution behavior is external; the name is not evidence of immutable weights. Activation and quality remain unobserved.

### Operative objects

#### RT-OBJ-system-prompt
Label: Pi synthesis system prompt

Source-native identity: `systemPrompt` in the shipped synthesis command. Representational form: natural-language instructions, consumed by the model. Storage substrate: static JavaScript strings joined in the script and passed as initial Agent state. It requests Markdown, a matching H1, in-place updating and unrelated-content preservation. It is not use-produced read-back. SRC-1, `packages/scripts/src/synthesize-with-pi.mjs`.

> "Update the current synthesis entry in-place based on the existing file content.",
> "Do not replace unrelated content outside the synthesis entry.",
> --- `packages/scripts/src/synthesize-with-pi.mjs`

#### RT-OBJ-command-input
Label: Action synthesis command JSON

Source-native identity: `SynthesisCommandInput`, materialized by `formatSynthesisForCommand`. Representational form: symbolic fields interpreted by the command, carrying natural-language prompt/raw text as payload. Storage substrate: transient serialized JSON on subprocess stdin. The model does not receive this JSON unchanged: the shipped command reformats entries and adds current file content. SRC-1, `packages/thalo-action/src/action.ts`, `packages/scripts/src/synthesize-with-pi.mjs`.

> const synthesisJson = JSON.stringify(formatSynthesisForCommand(synthesis), null, 2);
> --- `packages/thalo-action/src/action.ts`

#### RT-OBJ-checkpoint
Label: Actualization checkpoint metadata

Source-native identity: `checkpoint` metadata in `actualize-synthesis` entries; serialized `git:` or `ts:` marker. Representational form: symbolic selector state. Storage substrate: plain text inside retained Thalo entries, including fenced Markdown. The script appends it; subsequent actualize calls parse it after latest-entry lookup. Detailed memory revision semantics are left to the memory analyst. SRC-1, `packages/thalo/src/commands/actualize.ts`, `packages/scripts/src/synthesize-with-pi.mjs`.

> const checkpoint = actualize.entry.metadata.find((m) => m.key.value === "checkpoint");
> return parseCheckpoint(checkpoint?.value.raw);
> --- `packages/thalo/src/commands/actualize.ts`

### Routes

#### RT-RTE-actualize-selection
Label: Actualization context selection

Endpoints/progression: loaded workspace → synthesis definitions → optional target IDs → latest actualization/checkpoint → tracker/query matches → structured output. Code is the next-step owner. Caller supplies workspace and optional tracker/targets; stored definitions supply queries and prompt. Queries are symbolic filters; prompt content is delivered without a semantic truth check. SRC-1, `packages/thalo/src/commands/actualize.ts`, `packages/thalo/src/services/synthesis.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Synthesis outputs with entries, prompt, file/title/link identity, checkpoints, zero-entry up-to-date flags and unknown target IDs; CLI prints them, action serializes pending outputs.
- Later read-back: Retained actualization metadata selects a later cutoff; stored definitions are reloaded; the Pi caller additionally reloads prior file prose.
- Delegated visibility: Action commands receive the JSON payload; CLI readers receive changed entry raw text and instructions; provider visibility depends on caller transformation, established for the shipped Pi script only.
- Selection predicate: Optional normalized synthesis link IDs, OR across source queries, and tracker-specific change/newness predicate. Git returns current matching instances; timestamp returns instances after its cutoff. Entries lacking a located workspace file are not emitted.
- Invalidation or expiry: Latest actualization supplies checkpoint; missing Git commit or switched marker type replays matching entries; timestamp cannot invalidate old in-place edits. Deleted or no-longer-matching entries do not reach the output.
- Activation or effect: Determines emitted context and whether action runs a command; reliable semantic incorporation by the model remains unobserved.
- Evidence limits: Implementation selection only; no supplied run establishes completeness, quality or operational success; custom trackers can differ.

Decision roles/mode: open caller requests bounded by explicit query and cutoff, not an experimental curriculum. Caller chooses target and tracker; code decides membership. No expected-answer oracle is used. This is selection rather than content admission.

> const tracker = providedTracker ?? new TimestampChangeTracker();
> --- `packages/thalo/src/commands/actualize.ts`

> isUpToDate: entries.length === 0,
> --- `packages/thalo/src/commands/actualize.ts`

> * Note: This method only returns entries that exist in the current version of the file.
> --- `packages/thalo/src/services/change-tracker/git-tracker.ts`

> * Simple but limited - can't detect in-place edits, only new entries.
> --- `packages/thalo/src/services/change-tracker/timestamp-tracker.ts`

The two last comments are implementation design descriptions corroborated by loops over current entries and strict timestamp filtering. Git source cleanliness is limited to current matching-source files:

> if (!this.force && sourceFiles.length > 0) {
>   const uncommitted = await getUncommittedFiles(this.cwd, sourceFiles);
>   if (uncommitted.length > 0) {
>     throw new UncommittedChangesError(uncommitted);
>   }
> }
> --- `packages/thalo/src/services/change-tracker/git-tracker.ts:90-95`

CLI `--force` and custom instructions are runtime-client controls, not overrides of provider behavior. The browser offers display-only preparation using timestamp fallback. Its displayed metadata differs from the parsed checkpoint:

> lines.push({ type: "dim", text: `   with metadata: updated: <current-timestamp>` });
> --- `apps/docs/app/components/playground/thalo-runner.ts`

#### RT-RTE-pi-synthesis
Label: Pi model synthesis and file admission

Endpoints/progression: stdin JSON → target-file read → assembled user prompt → fresh Agent using [RT-CMP-gpt5-mini](#rt-cmp-gpt5-mini) and [RT-OBJ-system-prompt](#rt-obj-system-prompt) → text deltas → first-fence reconstruction → filesystem write plus [RT-OBJ-checkpoint](#rt-obj-checkpoint). Host code owns execution and file effects; model supplies proposed Markdown. SRC-1, `packages/scripts/src/synthesize-with-pi.mjs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Log messages and process completion after file write; failures throw for empty stdin/output, missing key, missing fence/link/checkpoint or I/O/provider errors.
- Later read-back: Updated Markdown is included as existing file content on later script invocations; appended checkpoint is loaded by later actualization selection.
- Delegated visibility: The model receives prompt, selected entries and entire trimmed current file; the script creates a new Agent but configures no tools or nested worker. Provider retention and internal processing are uninspected.
- Selection predicate: Parent chooses synthesis and entries; script resolves `file` relative to cwd and reads all its content. Text deltas, not structured validated fields, become output.
- Invalidation or expiry: A later invocation replaces suffix prose again; source/checkpoint gates only pending selection. No context trimming, expiry or immutable model-version rule is configured here.
- Activation or effect: Nonempty model text is installed in the target file; semantic obedience and downstream behavioral change are unobserved.
- Evidence limits: Prompt requests do not establish compliant narrow edits; provider/Pi internals and actual outcomes are external or unsupplied.

Admission: trigger is pending synthesis execution (or direct script input); model proposes prose; host software admits it after nonempty-output and fence/link/checkpoint checks. No human decides individual content before disk write. Human can later edit/revert or reject PR integration. Failure before write stops that update; file write is not a multi-file transaction and automatic rollback is not provided. Open synthesis mode has no answer oracle or independent quality evaluator. Persisted guidance is the stored synthesis definition; static system guidance stays in code. The route requests generation under guidance, not a codified cycle of content-directed criticism of that guidance; no theory-builder, reflection, learning or self-improvement property is inferred from this write.

> const agent = new Agent({
>   initialState: {
>     systemPrompt,
>     model: getModel(provider, modelName),
>   },
> });
> --- `packages/scripts/src/synthesize-with-pi.mjs`

> await agent.prompt(userPrompt);
> --- `packages/scripts/src/synthesize-with-pi.mjs`

> await writeFile(absoluteFilePath, updated);
> --- `packages/scripts/src/synthesize-with-pi.mjs`

The prompt is policy; the host write transformation is the actual effect boundary:

> return `${before}${blockWithActualize}${closingFence}\n\n${markdown}\n`;
> --- `packages/scripts/src/synthesize-with-pi.mjs`

`before` ends at the first Thalo fence; `closingFence` contains only its closing-fence line. The original suffix is not retained by this expression. No target-ID search chooses the block.

#### RT-RTE-action-publication
Label: Configured command execution and Git publication

Endpoints/progression: caller inputs → loaded workspace/selection → pending list → fresh local branch → sequential command stdin → Git status/add/commit/force-push → PR create/update. Action code owns coordination; a configured command owns intermediate effects. Principal is CI under supplied credentials. SRC-1, `packages/thalo-action/src/action.ts`, `packages/thalo-action/src/mod.ts`, `.github/workflows/test-action.yml`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Up-to-date path sets zero and returns; pending path outputs PR URL/number and pending count after publication.
- Later read-back: Published file/checkpoint changes become input when a later caller checks out and loads that branch or its merged successor; the action itself does not merge.
- Delegated visibility: Each configured subprocess receives one synthesis JSON on stdin and cwd; process/environment access is governed by host permissions, not a Thalo isolation policy.
- Selection predicate: Pending outputs where `!isUpToDate`; after commands, all Git working-tree changes can be staged, not only target files.
- Invalidation or expiry: Local branch is deleted/recreated; remote branch is force-pushed; existing open PR is updated. No compare-and-swap or concurrent-writer lock is shown.
- Activation or effect: Runs subprocesses, commits and publishes branch changes; successful subprocess return does not validate content or establish base-branch integration.
- Evidence limits: Configured permission grants are inspected; actual credentials, successful pushes, human review and deployment isolation are uninspected.

Admission/mode: open requests over query-selected work, not candidate experiments. Caller chooses command; command proposes/adopts local changes; action admits every staged file after subprocess completion. No content oracle checks them. PR reviewers can veto integration but not the already published branch. Configured PR text asks review; command contract says it should update files. Static action inputs/workflow govern machinery; dynamic command replacement is the capability extension surface. Thalo does not verify or approve that replacement's implementation. Failures set action failure; partial local writes survive and Git recovery is external. A no-file-change command causes an empty commit, so the pending count is not proof of performed rewrites.

> await exec.exec(inputs.command, [], {
>   input: Buffer.from(synthesisJson),
>   cwd,
> });
> --- `packages/thalo-action/src/action.ts`

> await exec.exec("git", ["add", "."]);
> --- `packages/thalo-action/src/action.ts`

> await exec.exec("git", ["push", "-u", "origin", inputs.branchName, "--force"]);
> --- `packages/thalo-action/src/action.ts`

> Please review the generated syntheses and merge when ready.`;
> --- `packages/thalo-action/src/action.ts`

#### RT-RTE-check-feedback
Label: Structural diagnostics and caller feedback

Endpoints/progression: user/agent edits or caller workspace → syntax diagnostics and configured rule visitors → diagnostic output/editor messages → caller's possible revision. Checker code decides diagnostic membership; the agent/human decides whether to change content. Symbolic schemas/rules are checked against parsed entries; natural-language entry meaning has no truth oracle here. SRC-1, `apps/thalo-cli/src/commands/check.ts`, `packages/thalo/src/checker/check.ts`, `packages/thalo-lsp/src/server.ts`, `skills/thalo/SKILL.md`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Diagnostic records and counts; CLI prints chosen format and exits nonzero on errors or configured warning threshold; LSP publishes diagnostics.
- Later read-back: inapplicable — diagnostics are not persisted by these inspected producers; later edited files are loaded by their callers.
- Delegated visibility: CLI stdout/stderr reaches its caller; LSP diagnostics reach the editor, not automatically a model invocation. Agent skill requests explicit checking.
- Selection predicate: Parsed files in caller scope, syntax errors and active rules; rule severity overrides can turn semantic rules off. Display severity filters differ from CLI error-count failure.
- Invalidation or expiry: Watch mode reruns after filesystem events; LSP changes refresh affected workspaces and open-document diagnostics; closed documents reload disk and clear displayed diagnostics.
- Activation or effect: Supplies structural feedback and CLI exit control; compliant correction or increased quality is not observed.
- Evidence limits: Rule dispatch and caller lifecycle are inspected, not exhaustive rule correctness or exercised agent correction; action/Pi publication bypass this feedback producer.

Decision roles/mode: caller-requested or watch/event-driven structural diagnosis. Schemas and rule predicates are structural references, not independently verified expected semantic answers. Runtime-client controls include path/file types, severity overrides, warning budget and watch. This route diagnoses; it does not own file admission or guarantee that another writer obeys diagnostics.

> const activeRules = allRules.filter((r) => getEffectiveSeverity(r, config) !== "off");
> --- `packages/thalo/src/checker/check.ts:113-113`

> if (runResult.result.errorCount > 0) {
>   process.exit(1);
> }
> --- `apps/thalo-cli/src/commands/check.ts`

#### RT-RTE-local-authoring
Label: Local text authoring and maintenance admission

Endpoints/progression: human or external editor/agent writes entries/schemas/prompts → files → workspace reload. Shipped init writes starter files; formatter writes formatted content on its write path; Git invokes merge driver on base/ours/theirs and driver writes merge result to ours. Different callers own proposal decisions; host filesystem writes admit local content. SRC-1, `apps/thalo-cli/src/commands/init.ts`, `apps/thalo-cli/src/commands/format.ts`, `apps/thalo-cli/src/commands/merge-driver.ts`, `skills/thalo/SKILL.md`, `thalo-test/AGENTS.md`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Init creation/skipping output; formatting output; merge-driver result and exit 0/1/2. General external editor save behavior is uninspected.
- Later read-back: Saved text reenters Node workspace loads, editor reload and browser snapshot synchronization; changed schemas govern subsequent checking and changed synthesis definitions govern selection/generation.
- Delegated visibility: Shipped skill/KB instructions can guide an external agent; the repository does not establish their runtime delivery or compliance. Git driver receives three file contents, not a model prompt.
- Selection predicate: Init's two named files; formatter's caller-selected files/write mode; merge driver's explicit base/ours/theirs arguments. External editor content selection is uninspected.
- Invalidation or expiry: Init skips existing files unless forced and supports dry run; merge result can contain unresolved conflicts with nonzero exit; later text replacement changes future loaded content.
- Activation or effect: Persists symbolic schema/entry changes and natural-language content/guidance, including merge output even on conflict; consumers operate on later loaded state.
- Evidence limits: Local write mechanisms are inspected; human authorship, external model generation and successful resolution of conflicting content are not supplied observations. Full merge algorithm and formatter semantics remain outside this bounded mechanism trace.

Admission/mode: caller-triggered local maintenance, not an improvement experiment. Init and formatting use software proposals; merge computes from supplied alternatives, with Git/user resolving conflicts. Human contribution is definite only when a human supplies/edits content; caller identity alone does not prove this. No universal content veto or semantic oracle is imposed. Guidance asks validation and formatting; text and schemas persist, but no automatic criticism-driven method revision is established. Recovery is later edit or Git restore/revert under caller control, not a shared automatic transaction.

The skill claims init creates AGENTS.md and personal-bio.md; inspected implementation instead lists entities.thalo and references.thalo. This is a documentation/implementation divergence, not a missing input or a change in frozen scope:

> const files = [
>   { path: "entities.thalo", content: ENTITIES_THALO.replace(/\{\{TIMESTAMP\}\}/g, timestamp) },
>   {
>     path: "references.thalo",
>     content: REFERENCES_THALO.replace(/\{\{TIMESTAMP\}\}/g, timestamp),
>   },
> ];
> --- `apps/thalo-cli/src/commands/init.ts`

Formatter write and merge-driver write are not the action's admission path:

> await fs.writeFile(fileResult.file, fileResult.formatted, "utf-8");
> --- `apps/thalo-cli/src/commands/format.ts`

> await fs.promises.writeFile(oursPath, result.content, "utf-8");
> --- `apps/thalo-cli/src/commands/merge-driver.ts`

### Claims

#### RT-CLM-agent-feedback
Label: Agent feedback loop for knowledge structure

Claimed operation: Thalo supplies schema/reference/link validation to help agents produce higher-quality entries. This is source-native design and claimed benefit; the implemented feedback route is [RT-RTE-check-feedback](#rt-rte-check-feedback). Benefit is not demonstrated by source inspection. SRC-1, `README.md`.

> The Thalo CLI provides this by validating the schema of entries (e.g. `rating` in the example above)
> and by checking references and links.
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-synthesis-guidance
Label: Retained synthesis prompt to later model request

Consumer: the shipped Pi model invocation. Channel: definition prompt extracted from workspace → action JSON → userPrompt text, alongside selected entries and existing file. Force: natural-language guidance interpreted by the model; not a deterministic enforcement constraint. Horizon: repeated invocations across repository loads; prompt text remains editable in retained definitions. Consumer-side activation remains unobserved. SRC-1, `packages/thalo/src/services/synthesis.ts`, `packages/thalo-action/src/action.ts`, `packages/scripts/src/synthesize-with-pi.mjs`. This authority path connects [RT-RTE-actualize-selection](#rt-rte-actualize-selection) and [RT-RTE-pi-synthesis](#rt-rte-pi-synthesis), without claiming that file persistence proves compliance.

> "Prompt:",
> prompt?.trim() ?? "(no prompt provided)",
> --- `packages/scripts/src/synthesize-with-pi.mjs`

#### RT-BAP-checkpoint-selection
Label: Retained checkpoint to future context membership

Consumer: actualize command and selected change tracker. Channel: parsed actualization metadata → marker → changed-entry selection. Force: symbolic cutoff/base-commit comparison, subject to fallback and override paths described in [RT-RTE-actualize-selection](#rt-rte-actualize-selection). Horizon: later repository/workspace invocations until a newer actualization supersedes the marker or its commit becomes unavailable. The retained checkpoint determines future emitted context even though it does not establish completed semantic incorporation. SRC-1, `packages/thalo/src/commands/actualize.ts`.

> const { entries: changedEntries, currentMarker } = await tracker.getChangedEntries(
>   workspace,
>   synthesis.sources,
>   lastCheckpoint,
> );
> --- `packages/thalo/src/commands/actualize.ts`

## Annotations

none
