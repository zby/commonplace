---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "OKF Harness runtime baseline tracing agent-owned wiki work, deterministic retrieval, alternate control paths and change admission at the frozen commit."
run-id: AAS-2026-10-15-okf-harness-6bf5507fbdbf-01
reviewed-boundary: "0dd4f806c454a68088c5a3e64b4cbebbe2c216be"
---

# OKF Harness runtime report

## Runtime account

### Work and responsibility split

OKF Harness registers sources, guides an enclosing agent's wiki synthesis and maintenance, checks workspace structure and lineage, and supplies bounded wiki evidence for later answers. It is not the enclosing agent runtime. The agent owns semantic reading, claim synthesis, contradiction judgment and the final answer. Deterministic TypeScript owns registration, metadata planning, snapshots, diagnostics, evidence selection, guidance installation and Git recovery. The source-grounded routes below describe implementation and delivered obligations, not successful execution. No target commands, tests, models or installers were executed. SRC-1: `packages/agent-pack/templates/okf-harness/SKILL.md`, `packages/core/src/source/ingest.ts`, `packages/cli/src/index.ts`.

> The CLI does not synthesize wiki content.
> --- `packages/agent-pack/templates/okf-harness/SKILL.md`

The policy/executor distinction is consequential. A natural-language workflow tells a host agent what to do; the CLI cannot compel that agent to load a reference, respect a file-count limit, answer faithfully or stop appropriately. [RT-CMP-host-agent](#rt-cmp-host-agent) isolates the uninspected model component. [RT-CMP-core](#rt-cmp-core) is the inspected symbolic executor. [RT-BAP-workflow-guidance](#rt-bap-workflow-guidance) and [RT-BAP-evidence-context](#rt-bap-evidence-context) distinguish instruction delivery from evidence delivery.

### Ordinary shipped invocation

Take a user asking an agent to make a workspace useful with a local source and then answer from it. The installed workspace skill classifies the request, selects setup/ingest/check/answer in user order, and loads each reference only when its workflow starts. This is a host-agent decision under text guidance, not a code scheduler. The workspace identity is the root resolving to `okfh.config.yaml`; source IDs and concept paths identify retained inputs and outputs. SRC-1: `packages/agent-pack/templates/okf-harness/SKILL.md`.

> Load only the reference needed for the current workflow; for combined requests, load the next reference only when that workflow starts.
> --- `packages/agent-pack/templates/okf-harness/SKILL.md`

There are two materially distinct entry surfaces. Workspace-local guidance uses local-shell `okfh --json`. Native Pi/OpenCode/OpenClaw host guidance instead directs every operation through `npx @okf-harness/setup@latest launch`, which resolves the workspace and dispatches its pinned CLI package. That host skill initializes with `--agents none` and expressly does not install workspace-local guidance. Consequently its delivery cannot be assumed to include every detailed obligation in the workspace Answer Workflow. Both ultimately reach the shipped CLI/core, but their instruction payloads differ. [RT-RTE-runtime-launch](#rt-rte-runtime-launch) and [RT-RTE-guidance-install](#rt-rte-guidance-install) trace those boundaries. SRC-1: `packages/native-integration/skills/okf-harness/SKILL.md`, `packages/setup/src/index.ts`, `packages/agent-pack/templates/okf-harness/SKILL.md`.

The CLI registers init, workspace, query, recovery, doctor, source, agent and bootstrap commands. Initialization calls workspace creation, optional adapter installation and recovery initialization. For normal defined commands, the driver resolves the root, invokes core, emits `{ok, command, workspace, data, warnings, next}` and sets an exit code. Handled errors become failure envelopes; unhandled errors go to the top-level handler. The agent is instructed to inspect JSON and stop the workflow sequence on command failure. This protocol does not equate a successful envelope with semantically adequate knowledge: no-match and withheld evidence can be successful returns. SRC-1: `packages/cli/src/index.ts`, `packages/cli/src/commands/init.ts`, `packages/cli/src/define-command.ts`, `packages/cli/src/commands/query.ts`.

During ingest, registration locks source additions, hashes the file bytes, reuses an existing same-hash registration or exclusively creates a raw copy and appends its manifest entry. A failed append removes the newly written raw copy. The metadata plan identifies a recommended reference path and up to five mechanically matched concepts; it is not source-body synthesis. The agent reads the registered material, makes bounded wiki edits, runs check and reports source ID, changed paths, status and unknowns. Source bytes/manifest and wiki prose persist on local disk. The semantic update is not transactional with checking: a failed check reports a problem after files have changed. Git checkpoint/restore is a separate explicit recovery route, not an automatic rollback on lint failure. [RT-RTE-source-ingest](#rt-rte-source-ingest), [RT-RTE-workspace-recovery](#rt-rte-workspace-recovery). SRC-1: `packages/core/src/source/index.ts`, `packages/core/src/source/ingest.ts`, `packages/agent-pack/templates/okf-harness/references/ingest.md`, `packages/core/src/recovery/index.ts`.

The answer request reloads retained workspace state. Evidence planning loads a snapshot, runs the common check pipeline, blocks on OKF conformance failures, applies source-risk seals, ranks eligible wiki concepts and emits up to three evidence items plus thin candidates, provenance, limits and continuation cues. The agent should make at most one automatic cue-following read, then judge sufficiency and conflicts and answer with paths/source IDs or state limits. Character budgeting controls returned excerpt text, not total host tokens or the host's accumulated conversation. The target implements neither host compaction nor an isolated model frame here; just-in-time reference loading and bounded retrieval limit additions by policy and code respectively. [RT-RTE-evidence-answer](#rt-rte-evidence-answer). SRC-1: `packages/core/src/evidence/index.ts`, `packages/core/src/lineage/index.ts`, `packages/cli/src/commands/query.ts`, `packages/agent-pack/templates/okf-harness/references/answer.md`.

### Guarantees and forcing cases

The following cases challenge overbroad readings of the ordinary path. They are inspected branches, not experiments or observed outcomes.

1. **URL registration does not acquire a page body.** It writes URL metadata and hashes that metadata. Later synthesis still needs accessible source content. Same-URL reuse cannot establish that a changing webpage was resnapshotted. [RT-RTE-source-ingest](#rt-rte-source-ingest). SRC-1: `packages/core/src/source/index.ts`, `SECURITY.md`.
2. **Evidence exclusion is not universal read denial.** Source loss/hash drift can seal directly linked concepts and citation dependents in `evidence`; standalone `search` passes an empty exclusion set and `read` directly resolves wiki targets without the evidence check/seal pipeline. The enclosing agent can also use its shell to read files. The two computed hops do not establish semantic contamination closure. [RT-RTE-direct-retrieval](#rt-rte-direct-retrieval), [RT-CLM-evidence-boundary](#rt-clm-evidence-boundary). SRC-1: `packages/core/src/evidence/index.ts`, `packages/core/src/search/index.ts`, `packages/core/src/read/index.ts`, `packages/agent-pack/templates/okf-harness/references/answer.md`.
3. **Acknowledgment is not proof of reconciliation.** The reconcile command validates registered IDs, a suspected edge, a nonempty note and ledger validity, then appends acknowledgment. It does not inspect affected wiki edits before clearing that edge. The workflow, not the verb, requires reading both revisions and actually updating prose. [RT-RTE-source-reconcile](#rt-rte-source-reconcile). SRC-1: `packages/core/src/source/reconciliation.ts`, `packages/agent-pack/templates/okf-harness/references/reconcile.md`.
4. **Recovery is broader than ordinary wiki-only edits.** Checkpoint stages all Git-visible workspace changes, not a per-workflow wiki allowlist. Restore rejects pending changes and uses Git tree restoration plus a new commit, preserving history rather than deleting successors. This is a durable alternate route affecting source records, instructions and configuration as well as wiki files; ignored/untracked-file behavior is governed by Git and workspace ignore rules, not by the answer workflow. [RT-RTE-workspace-recovery](#rt-rte-workspace-recovery). SRC-1: `packages/core/src/recovery/index.ts`.

| Load-bearing guarantee | Owner, enforcement and strength | Covered paths and counterpaths | External contract and conclusions |
|---|---|---|---|
| Registration does not overwrite an existing raw destination | Core `addFileSource`/`addUrlSource` use exclusive creation; **invariant** at that creation point. SHA-256 identifies recorded bytes; source-add lock coordinates cooperating writers. | Covered: these registration APIs and their CLI caller. Not covered: host shell edits, filesystem writes outside these APIs, restoration of old Git trees. Abrupt process death can leave a diagnostic lock. | Requires filesystem exclusive-create semantics and cooperative mutation. implementation conclusion status: wired. operation conclusion status: uninspected. This is not deployed filesystem immutability. SRC-1: `packages/core/src/source/index.ts`. |
| Selected evidence omits sealed concepts and blocks conformance failures | Core evidence planner and common check pipeline; **invariant** within that planner's return construction. | Covered: `evidence` and API `planEvidenceBrief`. Not covered: direct search/read, shell access, arbitrary host tools; graph propagation is bounded. | Requires source records/wiki links to represent the relevant dependencies. Agent must honor withholding and widen semantic exclusions. implementation conclusion status: wired. operation conclusion status: uninspected. SRC-1: `packages/core/src/evidence/index.ts`. |
| Ingest file-count ceiling, one follow-up read and provenance disclosure | Host agent, at decisions after receiving workflow text; **policy**. | Detailed workspace workflow delivery; native host entry has a smaller payload. CLI read permits repeated calls; ordinary host file editing is not intercepted. | Requires correct host instruction loading and adherence. delivery conclusion status: afforded. operation conclusion status: uninspected. SRC-1: `packages/agent-pack/templates/okf-harness/references/ingest.md`, `packages/agent-pack/templates/okf-harness/references/answer.md`, `packages/native-integration/skills/okf-harness/SKILL.md`. |
| Launcher selects the workspace runtime version | Setup launcher builds the versioned npm package invocation; **protocol**. | Covered: launcher dispatch. Not covered: direct `okfh`, direct core API, manually changed pin, moving setup `@latest` itself. | Requires npm/npx package resolution and artifact integrity; source pin is not registry-content authentication. implementation conclusion status: wired. operation conclusion status: uninspected. SRC-1: `packages/setup/src/index.ts`, `packages/core/src/config/index.ts`. |

Capability surface, grant set and isolation are separate. The shipped capability surface includes local filesystem writes, guidance installation, graph report generation, npm/npx launch and Git subprocess recovery. Workspace mutation APIs apply path checks at inspected points, but this is not a host sandbox. No actual host permission set, approval configuration, provider tool grant or deployed isolation envelope was supplied. The target's text restrictions cannot be promoted to a grant set. Remote workers, provider-native tool routes and host scheduling remain external/unobserved; none is needed to explain the inspected CLI route. SRC-1: `packages/core/src/paths/index.ts`, `packages/agent-pack/src/index.ts`, `packages/setup/src/index.ts`, `packages/core/src/recovery/index.ts`, `packages/cli/src/commands/query.ts`.

Added selective coverage under SRC-1 consists of implementation in `packages/core/src/read/index.ts`, `packages/core/src/search/index.ts`, `packages/core/src/source/ingest.ts`, `packages/core/src/source/reconciliation.ts`, `packages/core/src/paths/index.ts`, `packages/core/src/config/index.ts`, `packages/cli/src/define-command.ts`, and additional launcher, evidence, recovery and adapter-install branches; `SECURITY.md` supplies doctrine/design. All are at the registered revision. Other integration distributions, all file-mutation call sites and adversarial filesystem races were not exhaustively audited. This prevents universal security, distribution-parity or reliability claims, not the scoped mechanisms below. No new source or observed-run layer is added.

## Shared records

### Components

#### RT-CMP-core
Label: Core library

The source-native `@okf-harness/core` component supplies symbolic TypeScript procedures executed in Node, stored as source/package code. CLI callers use its source, check, query and recovery exports. No distributed parameters are involved in the inspected ranking/registration/check code. This says nothing about the enclosing host model. SRC-1: `packages/core/src/index.ts`, `packages/cli/src/commands/query.ts`, `packages/core/src/source/ingest.ts`.

> const maxEvidenceItems = 3;
> --- `packages/core/src/evidence/index.ts`

#### RT-CMP-host-agent
Label: Enclosing host Agent

The workflows assign synthesis and sufficiency judgment to an external Agent. Its model is a distributed-parametric component; exact weights, storage substrate, provider and selected version are outside the frozen source. Whether parameters change during operation is uninspected. An exact model version is not established as pinned by these instructions. Whether a mutable endpoint resolves to another model is also uninspected; runtime package pinning pins software, not the model. The inspected route reaches this component through host-consumed instructions and tool results, not a target-owned model API call. SRC-1: `packages/agent-pack/templates/okf-harness/references/ingest.md`, `packages/agent-pack/templates/okf-harness/references/answer.md`.

> Judge sufficiency and conflicts yourself. Evidence sufficiency and conflict judgment belong to the agent, not the CLI.
> --- `packages/agent-pack/templates/okf-harness/references/answer.md`

### Operative objects

#### RT-OBJ-workflow-guidance
Label: Workspace and host workflow guidance

Source-native skills and reference Markdown are natural-language instructions on disk, rendered or copied into host/workspace discovery locations. Workspace skill plus detailed references and native host entry skill are distinguishable payloads, not assumed equivalent. Fixed filenames/managed markers serve symbolic installation checks; this record concerns the prose consumed by the agent. Newly installed static guidance is instruction provisioning, not experience-derived read-back. SRC-1: `packages/agent-pack/templates/okf-harness/SKILL.md`, `packages/agent-pack/src/index.ts`, `packages/native-integration/skills/okf-harness/SKILL.md`, `packages/native-integration/src/opencode.ts`.

> This host skill supports daily operations but does not install workspace-local guidance. Do not claim otherwise.
> --- `packages/native-integration/skills/okf-harness/SKILL.md`

#### RT-OBJ-runtime-pin
Label: Workspace runtime pin

`runtime.version` in `okfh.config.yaml` is a symbolic version string stored in local YAML. The launcher consumes it to choose the CLI npm package. `recordRuntimePin` fills a missing version, preserves an existing pin and supports dry-run; it does not offer an automatic upgrade of an existing version. This operative part is configuration, separate from natural-language guidance and wiki prose. SRC-1: `packages/core/src/config/index.ts`, `packages/setup/src/index.ts`.

> if (pinned !== undefined) {
>     return { version: pinned, state: "already-pinned" };
>   }
> --- `packages/core/src/config/index.ts`

### Routes

#### RT-RTE-source-ingest
Label: Source registration and agent-owned ingest

Endpoints: user-supplied file/URL or registered source → CLI registration/plan → agent source reading and wiki edits → check and final report. User supplies the problem/input; core proposes metadata candidates; agent decides semantic content. Local source IDs, hashes, concept paths and the workspace root coordinate state. File registration and wiki authorship are separate physical I/O paths. SRC-1: `packages/core/src/source/index.ts`, `packages/core/src/source/ingest.ts`, `packages/agent-pack/templates/okf-harness/references/ingest.md`.

- Immediate return: registration source/action and metadata plan return JSON; final agent response names source, edits, check result and unresolved questions.
- Later read-back: persisted raw bytes/URL metadata, manifest and agent-authored wiki files reach later planning, checking and evidence invocations.
- Delegated visibility: enclosing agent receives CLI JSON and reads selected registered source material; no isolated worker handoff is implemented in this route.
- Selection predicate: file reuse by hash, URL reuse by normalized URL; ingest candidates use metadata-token overlap or suggested-topic-path equality, ranked and capped at five; agent confirms relevance after source reading.
- Invalidation or expiry: changed material should become a new source; hash drift and revision edges are maintenance signals, not automatic prose correction.
- Activation or effect: registration writes raw/manifest; agent editing can change future wiki evidence. Actual semantic compliance and use are unobserved.
- Evidence limits: source inspection establishes deterministic registration/planning and requested synthesis; no actual model-produced page or benefit is supplied.
- implementation conclusion status: wired
- agent-protocol conclusion status: claimed
- operation conclusion status: uninspected

Admission: open user requests trigger proposed reference/concept edits. Agent authors/adopts claims under the ingest guidance; the user is asked before exceeding the configured file ceiling and can resolve intended truth under the stop contract, but starting ingest is not per-content approval. Core rejects invalid manifests and unsupported inputs; post-edit check can report structural failures but does not reject semantic writes before persistence. Recovery is separate Git checkpoint/restore, not automatic undo. No expected-answer/reference-outcome oracle is furnished by this route; source material is evidence for agent judgment, not a scored answer key. Human rejection ability beyond these requested stops depends on the external host. SRC-1: `packages/agent-pack/templates/okf-harness/SKILL.md`, `packages/agent-pack/templates/okf-harness/references/ingest.md`, `packages/core/src/source/index.ts`.

> This limit is agent-enforced guidance; the CLI does not enforce it yet.
> --- `packages/agent-pack/templates/okf-harness/references/ingest.md`

> await writeFile(absoluteRawPath, contents, { flag: "wx" });
> --- `packages/core/src/source/index.ts`

#### RT-RTE-evidence-answer
Label: Evidence brief and agent answer

Endpoints: user question → evidence planner/snapshot/check/seals/search/excerpts → host agent judgment → answer, optionally accepted wiki write-back. Core rules select/budget context; agent decides relevance, sufficiency, conflict and semantic widening. The question, root, concept IDs and source IDs carry identities. SRC-1: `packages/core/src/evidence/index.ts`, `packages/cli/src/commands/query.ts`, `packages/agent-pack/templates/okf-harness/references/answer.md`.

- Immediate return: evidence JSON includes excerpts, candidates, provenance, limits, warnings, seals and guidance; the host returns the natural-language answer.
- Later read-back: existing wiki content is reloaded from prior writes; an explicitly accepted answer write-back produces one concept and index link for future retrieval.
- Delegated visibility: host sees excerpt text and thin candidate metadata; candidate cards are not delivered as supporting evidence bodies. No target-managed separate model context is established.
- Selection predicate: lexical metadata/body scoring, seal exclusions, top three evidence items, question-aware excerpt selection and character budget; workflow permits at most one automatic continuation-cue read.
- Invalidation or expiry: each command reloads current workspace facts; source risks/conformance can change evidence eligibility. The ephemeral write-back offer is not persisted without acceptance.
- Activation or effect: code controls returned evidence; agent is requested to ground/disclose/withhold. Accepted write-back can change later available knowledge; compliant answering remains unobserved.
- Evidence limits: budget is excerpt characters, not a whole-window/token bound; computation of seals is bounded and is not proof of semantic dependency closure or truth.
- implementation conclusion status: wired
- agent-protocol conclusion status: claimed
- operation conclusion status: uninspected

Admission and mode: open wiki questions, not a benchmark curriculum. The agent proposes a write-back only on the no-match permission branch, never on withheld/truncated results or after continuation reading. User explicit yes admits keeping one concept plus its index link; silence/no rejects persistence. Yes does not certify correctness. The agent authors prose and any unanchored derivation links; check follows the edit. No outcome oracle is supplied. Recovery is the separate Git route. Guidance shapes a deliberately citation-empty retained answer, not an invented raw source. SRC-1: `packages/agent-pack/templates/okf-harness/references/answer.md`.

> A yes writes one ordinary concept page and its index link, and means only that the answer is worth keeping, not that the user certified it.
> --- `packages/agent-pack/templates/okf-harness/references/answer.md`

#### RT-RTE-direct-retrieval
Label: Direct search and read

Endpoints: caller query/target → standalone core search/read → cards or bounded wiki document JSON. Owner: deterministic selector/reader under the caller's request; host decides subsequent action. These are alternate lower-level paths, not aliases for the checked Evidence Brief. SRC-1: `packages/core/src/search/index.ts`, `packages/core/src/read/index.ts`, `packages/cli/src/commands/query.ts`.

- Immediate return: search cards or read metadata, outline, citations, content and truncation cues; no final model answer is generated by core.
- Later read-back: caller-selected retained wiki files from earlier edits are loaded anew.
- Delegated visibility: host receives selected card/document fields through CLI; shell or API consumers need not obey the workspace answer reference.
- Selection predicate: search uses lexical scoring and filters with an empty exclusion set; read resolves explicit concept ID/path and optional section/range/full mode.
- Invalidation or expiry: next invocation loads a new snapshot; the inspected path does not apply evidence seals as an authorization gate.
- Activation or effect: read-only document delivery; whether the host uses returned text as evidence or violates its workflow is unobserved.
- Evidence limits: config/scan readability checks are not semantic sufficiency, currency or universal evidence-withholding enforcement.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> return searchWorkspaceFromSnapshot(snapshot, options, new Set());
> --- `packages/core/src/search/index.ts`

> return readWorkspaceDocumentFromSnapshot(snapshot, options);
> --- `packages/core/src/read/index.ts`

#### RT-RTE-source-reconcile
Label: Agent reconciliation and edge acknowledgment

Endpoints: check reports suspected revision → agent reads both registered revisions/affected wiki → prose update/check → `source reconcile` acknowledgment. The agent owns semantic change judgment; core owns pair validation and ledger append. IDs name the exact prior→revision edge. SRC-1: `packages/agent-pack/templates/okf-harness/references/reconcile.md`, `packages/core/src/source/reconciliation.ts`.

- Immediate return: exact edge acknowledgment and ledger path after a nonempty judgment note is accepted.
- Later read-back: later snapshots consume ledger acknowledgments to derive pending edges; later answers consume edited wiki prose independently.
- Delegated visibility: host reads both registered sources and affected concepts; core acknowledgment receives IDs and note, not a proof of those reads/edits.
- Selection predicate: suspected edge derived from manifest, registered endpoints and valid ledger; agent selects every actually affected wiki claim by reading.
- Invalidation or expiry: acknowledgment applies to the exact pair; another revision edge needs its own acknowledgment. Semantic adequacy is not revalidated by the ledger append.
- Activation or effect: append changes derived dangling-edge facts; semantic wiki changes are agent-owned writes and remain unobserved.
- Evidence limits: a valid nonempty note establishes recorded acknowledgment, not factual reconciliation or a correct judgment.
- implementation conclusion status: wired
- agent-protocol conclusion status: claimed
- operation conclusion status: uninspected

Admission: an open maintenance request/diagnostic triggers agent proposal and adoption of prose changes. Text guidance says positive textual signal, not mere omission, warrants suspected removal; user intent is requested only when the stop predicate holds. Computational rejection covers unregistered endpoints, unknown edge, empty note and invalid ledger, not substantive wiki correctness. Direct CLI callers can acknowledge without the semantic workflow. No answer oracle or experiment comparator is supplied. Git recovery can restore a prior retained workspace; no automatic prose rollback accompanies rejection. SRC-1: `packages/agent-pack/templates/okf-harness/references/reconcile.md`, `packages/core/src/source/reconciliation.ts`.

> Reconcile means the wiki reflects the revision; reviewing it is not reconciliation.
> --- `packages/agent-pack/templates/okf-harness/references/reconcile.md`

> await appendFile(absoluteLedgerPath, `${JSON.stringify(acknowledgement)}\n`, "utf8");
> --- `packages/core/src/source/reconciliation.ts`

#### RT-RTE-workspace-recovery
Label: Git checkpoint and restore

Endpoints: init or caller checkpoint/restore → core Git subprocesses → retained commit/history or restored working tree. Owner: caller chooses judgment/completion; core decides mechanical validity; Git executes. Local commit-derived completion IDs coordinate identity. SRC-1: `packages/core/src/recovery/index.ts`, `packages/cli/src/commands/init.ts`, `packages/cli/src/commands/recovery.ts`.

- Immediate return: checkpoint completion ID/judgment; history list; restore returns the selected completion.
- Later read-back: commits and judgment bodies are read by history; restored files become input to later CLI/host invocations.
- Delegated visibility: Git subprocess receives command arguments and workspace cwd; host gets completion records, not an isolated model's findings.
- Selection predicate: checkpoint requires nonempty judgment; restore selects an existing completion and requires clean pending Git state.
- Invalidation or expiry: history is bounded by the initialization baseline; restore commits are omitted from completion listing while prior completions stay reachable.
- Activation or effect: initialize/checkpoint stage all Git-visible changes; restore applies a selected tree and records the move as a commit.
- Evidence limits: filesystem/Git execution and outcome are unobserved; checkpoint records do not certify semantic quality or establish trace-fed learning.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: caller supplies judgment and selected completion; caller's human versus model identity is unresolved. Core can reject empty judgment, missing completion, pending changes or Git failures. The change can replace knowledge, instructions and configuration together, rather than only a wiki part. Operating mode is explicit recovery, not an improvement experiment; completion state is the requested restore target, not an answer oracle. Guidance is the explicit command contract. Rollback/recovery consists of subsequent restoration to another completion; it is not a semantic evaluator. SRC-1: `packages/core/src/recovery/index.ts`.

> await runRecoveryCommand(workspaceRoot, ["add", "--all"], "write");
> --- `packages/core/src/recovery/index.ts`

> await runRecoveryCommand(workspaceRoot, ["read-tree", "--reset", "-u", revision], "write");
> --- `packages/core/src/recovery/index.ts`

#### RT-RTE-guidance-install
Label: Guidance provisioning and host synchronization

Endpoints: init/agent/bootstrap installation or OpenCode plugin load → generated/copied skill and reference files → later host discovery. Installer core and OpenCode synchronization own mechanical writes; an external host owns loading and interpreting the result. Natural-language guidance is the admitted content; managed markers/path rules are symbolic controls. SRC-1: `packages/agent-pack/src/index.ts`, `packages/native-integration/src/opencode.ts`, `packages/cli/src/commands/init.ts`.

- Immediate return: adapter installation reports planned/written/replaced/skipped files/conflicts; OpenCode plugin synchronizes the host skill and returns an empty plugin object.
- Later read-back: newly installed shipped text is static provisioning, not use-accumulated memory; later host discovery can load it. Subsequent overwrites/repairs may replace the provisioned payload.
- Delegated visibility: hosts receive installed guidance only if their discovery/loading contract is honored; OpenCode copies the host skill, not all workspace references.
- Selection predicate: chosen adapter/bootstrap destination and rendered template; managed ownership/placeholder checks, root managed-block merge; OpenCode leaves user-owned skill untouched.
- Invalidation or expiry: reinstall can replace managed content; malformed root blocks conflict; OpenCode removes managed legacy skill after synchronization.
- Activation or effect: writes change available instructions; actual host loading/compliance is unobserved.
- Evidence limits: copying/equality checks establish intended delivery mechanics, not model adherence, package authenticity or parity among integrations.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: caller selects installation/repair and can supply force for managed-file conflict handling. Agent-pack first plans writes and returns without writing if conflicts exist or dry-run is chosen; root prose outside managed blocks is preserved. OpenCode proposes no model-authored change: it copies package text automatically on plugin load and declines user-owned destinations. Content authors are shipped template authors, not an online self-revision loop. No answer oracle, performance-based proposal selection or improvement experiment is wired in these inspected functions. Recovery for workspace writes can use the Git route; general host-skill rollback is not established by that workspace route. SRC-1: `packages/agent-pack/src/index.ts`, `packages/native-integration/src/opencode.ts`.

> if (dryRun || plan.conflicts.length > 0) {
>     return plan;
>   }
> --- `packages/agent-pack/src/index.ts`

> if ((await readSkillOwnership(target)) === "user-owned") {
>     return;
>   }
> --- `packages/native-integration/src/opencode.ts`

#### RT-RTE-runtime-launch
Label: Runtime pin admission and launcher dispatch

Endpoints: host runtime request → setup resolves root/config/pin → npx versioned CLI invocation → command result. Missing-pin branch returns a proposed adoption command; `adopt-runtime` records the running CLI version only if absent. Owner: setup dispatch rules and caller follow-through, not a model-based package selector. SRC-1: `packages/setup/src/index.ts`, `packages/core/src/config/index.ts`, `packages/cli/src/commands/workspace.ts`.

- Immediate return: launcher failure/outcome or delegated CLI stdout/stderr/exit code; adopt returns recorded/already-pinned/would-record state.
- Later read-back: recorded version affects future launcher invocations; package installation/cache state is external npm machinery, not target knowledge memory.
- Delegated visibility: npx/runtime subprocess receives arguments, environment and workspace cwd; host receives forwarded result and failure details.
- Selection predicate: resolved workspace config runtime version; missing pin proposes adoption using the launcher's package version.
- Invalidation or expiry: adoption preserves existing pins; manual config edits or workspace restoration can change the selected version; setup `@latest` is separately moving.
- Activation or effect: adoption can write YAML; launch requests execution of selected package. Actual fetched content and execution remain unobserved.
- Evidence limits: a versioned package specification is not proof of byte identity with the reviewed repository; direct CLI/API paths bypass launcher selection.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: missing pin triggers a concrete software-generated proposal; caller runs or declines it. Invalid config rejects adoption; existing pins veto replacement in the inspected function; dry-run avoids writes. This is configuration admission, not autonomous improvement or an automatic version upgrade. No answer oracle or experimental improvement mode is furnished. The persisted change is the version field, shaped by the current runtime's version constant and launcher failure guidance. Workspace Git recovery can restore config; supply-chain recovery is external. SRC-1: `packages/setup/src/index.ts`, `packages/core/src/config/index.ts`.

> `${runtimePackageName}@${config.config.runtime.version}`,
> --- `packages/setup/src/index.ts`

### Claims

#### RT-CLM-evidence-boundary
Label: Bounded withholding claim

The Answer Workflow claims the Harness computes two provable hops and asks the agent to widen withholding where prose indicates further contamination. Implementation builds seals from source-linked concept IDs plus incoming citation edges, then excludes sealed IDs during evidence search. It does not provide universal read authorization or semantic closure. SRC-1: `packages/agent-pack/templates/okf-harness/references/answer.md`, `packages/core/src/evidence/index.ts`; see [RT-RTE-direct-retrieval](#rt-rte-direct-retrieval).

> The Harness computes only two provable hops. Inspect concepts beyond that boundary when their prose may carry the same contamination.
> --- `packages/agent-pack/templates/okf-harness/references/answer.md`

> if (edge.kind === "citation" && referenceIds.has(edge.to)) {
>       sealed.add(edge.from);
>     }
> --- `packages/core/src/evidence/index.ts`

#### RT-CLM-delivery-ceiling
Label: Delivered obligations are not enforced compliance

The workspace Answer Workflow explicitly limits its guarantee to delivery, not obeyed provenance disclosure/lineage prose. This ceiling is consistent with agent-owned writes and direct lower-level retrieval, rather than proof that disclosure is reliably produced. SRC-1: `packages/agent-pack/templates/okf-harness/references/answer.md`; see [RT-BAP-workflow-guidance](#rt-bap-workflow-guidance).

> Accepted ceiling: an Agent that skips the disclosure or the lineage prose is not caught by anything. Harness can prove the obligation was delivered, never that it was honored.
> --- `packages/agent-pack/templates/okf-harness/references/answer.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-workflow-guidance
Label: Workflow guidance to host decisions

Consumer: enclosing host agent. Channel: skill discovery, root guidance and just-in-time reference reads. Force: natural-language policy requests; loading/adherence depends on the external host. Horizon: deployed workspace/host sessions while guidance remains available. Installed text can shape routing, edits, stops and answers, but operation/activation is unobserved. Native host guidance and detailed workspace guidance must not be conflated. SRC-1: `packages/agent-pack/templates/okf-harness/SKILL.md`, `packages/native-integration/skills/okf-harness/SKILL.md`, `packages/agent-pack/src/index.ts`.

> Run harness operations through local-shell `okfh --json` commands and read their JSON before deciding the next step.
> --- `packages/agent-pack/templates/okf-harness/SKILL.md`

#### RT-BAP-evidence-context
Label: Retained wiki evidence to later answers

Consumer: answering host agent. Channel: CLI Evidence Brief tool result, with at most one workflow-permitted cue-following read. Force: natural-language evidence interpreted by the agent, alongside symbolic selection/provenance fields and requested withholding rules. Horizon: later questions/sessions after retained wiki writes. This establishes an available behavior-shaping route, not demonstrated improved capacity or exercised self-improvement. Host context isolation/compaction and actual dependence on changed evidence are uninspected. SRC-1: `packages/core/src/evidence/index.ts`, `packages/agent-pack/templates/okf-harness/references/answer.md`.

> "Use selected evidence excerpts as the bounded answer context.",
> --- `packages/core/src/evidence/index.ts`

## Annotations

none
