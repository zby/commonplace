---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Signet workflow account: a Dreaming content pass from admitted maintenance work to finalized memory head and conditional host delivery."
run-id: AAS-2026-10-14-signetai-64f703d83203-01
reviewed-boundary: "12dba1ce753babda735f2ba7b6f150c6c0b7f95e"
---

# Signet workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is one admitted Dreaming **incremental-content** pass. It is selected because it joins model-directed evidence inspection, audited semantic writes, a required retained-head submission, daemon finalization and later context supply. It is an internal maintenance workflow, not the external host's complete task-to-answer loop. Its requested result is maintained semantic understanding and a current memory head; the model's completion summary alone does not deliver that result.

The source is SRC-1 at the [frozen boundary](boundary.md). This account uses implementation text and identifies prompt requirements as instructions rather than observed compliance. No execution trace, model response, test result or causal comparison establishes that this workflow ran successfully. Added inspection covers content-pass prompt and staging/finalization branches in `platform/daemon/src/pipeline/dreaming.ts`, head capability definitions in `platform/daemon/src/pipeline/dreaming-capabilities.ts`, head validation, retention and publication in `platform/daemon/src/memory-head-owner.ts`, owner-side finalization in `platform/daemon/src/db-owner-worker.ts`, and working-memory selection in `platform/daemon/src/hooks.ts`.

### 1. Admit work and hand off a scoped task

The scheduler's rule-driven enablement, capacity, pressure, trigger and scope leasing precede the model, as established by [RT-RTE-dreaming-pass](runtime.md#rt-rte-dreaming-pass). A scheduled pass can receive installation scopes; a user-requested pass receives only the requested agent's scope. The daemon supplies a pass ID, selected maintenance guidance, scoped history, pending attention, clock, tool definitions, timeout and output budget. The routed executor receives these inputs and owns the model's subsequent tool choices, not scheduling or acceptance of writes. [RT-OBJ-pass-prompt](runtime.md#rt-obj-pass-prompt) and [RT-CMP-inference-router](runtime.md#rt-cmp-inference-router) establish those existing referents.

This is delegation to one bounded maintenance agent, not an evidenced critic-author team. In the inspected Pi path, resource discovery is disabled and calls cross back to parent-side daemon handlers; [RT-CLM-tool-boundary](runtime.md#rt-clm-tool-boundary) supplies the enforcement evidence and its dependency limits. The alternate ACPX executor has a different resource envelope, so these Pi restrictions do not become a whole-workflow sandbox guarantee.

### 2. Inspect evidence and propose semantic changes

The content instructions ask the agent to handle source-change and temporal review work, inspect exploration hints, and process unreviewed evidence by pages. They direct it to check existing claims before adding or superseding them. Evidence identifiers and exact quotes travel with proposed operations; the daemon, not the model's prose, can admit or reject mutations. Existing operation validation and uncommitted-suffix retry evidence is in [RT-RTE-dreaming-pass](runtime.md#rt-rte-dreaming-pass) and the structured effect channel in [RT-BAP-maintenance-tools](runtime.md#rt-bap-maintenance-tools).

The prompt explicitly treats an ambiguous relationship as a proposal for user review rather than an immediate settled change (SRC-1, `platform/daemon/src/pipeline/dreaming.ts`):

> The daemon will place it in the user's review queue for confirmation, not treat the queue as a work-deferral mechanism.
> --- `platform/daemon/src/pipeline/dreaming.ts:1109-1109`

This establishes requested handling, not inspected execution of the separate user-review queue. It does not warrant saying that every maintenance write receives human approval. There is no independent expected-answer oracle at this seam: scope, schema and quotation checks constrain admissibility, not interpretive truth. The model's actual choice of sources and quality of interpretation remain unobserved.

### 3. Submit the retained result, not merely a summary

The content prompt requires `memory_head_read` followed by submission of the complete set of retained entries with source/quote support. The read capability returns supported entries from the last published revision even when current head state is stale. This keeps prior supported material available for a replacement proposal rather than silently starting from an empty head. The tool description instructs the agent to condense or drop entries to fit the rendered budget. These are requested model decisions; the staging handler independently enforces input bounds.

The submission and acceptance path is [WF-RTE-head-finalization](#wf-rte-head-finalization). A successful tool reply initially means **staged**, not durable. The daemon retains the proposed input in pass-local state. It checks provenance and head currency during finalization, after the executor returns. Thus the agent can see staging success and still have its pass fail later.

### 4. Verify, recover or fail

Three rejection points have different owners and remedies:

- An oversized head is rejected before staging. The daemon returns a bounded-input error; the model may shorten or drop entries and resubmit before ending the pass.
- A second submission after an accepted stage does more than reject the extra call: it clears the previous staged input. If the model then ends without another accepted stage, finalization fails. This inspected behavior is stronger than the tool description's simple warning that a second commit is rejected.
- The database finalizer rechecks the running pass, agent, base revision and evidence support. An externally changed head yields `STALE_HEAD`; missing or non-exact current scoped evidence can reject a changed head. These are post-executor vetoes, not a successful tool-return guarantee.

On a thrown error, the pass runner calls `failDreamingPass`, finishes live reporting as failed or cancelled, records error telemetry and rethrows (SRC-1, `platform/daemon/src/pipeline/dreaming.ts`). Scheduler retry and halt controls remain daemon responsibilities described in the runtime baseline. No inspected mechanism promises autonomous repair of every finalization failure. Earlier ontology batches may already have committed; failure of this final delivery seam does not establish rollback of the entire pass.

### 5. Define delivery and its downstream limit

Successful finalization records a completed pass and the accepted head result. A changed head creates a retained revision and a pending publication record. A valid no-change result can complete without producing a new revision. The file projection is a separate delivery surface: owner code attempts publication after finalization, and a later read can retry it. A user-authored `MEMORY.md` is preserved rather than overwritten. Therefore database completion, filesystem projection and eventual model receipt are distinct outcomes, not one success bit.

For later session startup, `currentWorkingMemory` inspects the file against current database head state, redacts and budgets selected content, and withholds it when freshness cannot be verified. Explicit identity-file configuration or disabled recent context can omit this path. These details qualify the downstream read-back of the finalized head; [RT-RTE-pi-lifecycle](runtime.md#rt-rte-pi-lifecycle) and [RT-BAP-host-context](runtime.md#rt-bap-host-context) establish subsequent Pi hidden-message wiring. The external foreground agent's task execution, verification and final answer are outside this selected workflow. Model uptake or improved answers are not established by the retained head or its delivery wiring.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-head-finalization
Label: Memory head finalization
Part of: [RT-RTE-dreaming-pass](runtime.md#rt-rte-dreaming-pass)

This is the content pass's distinct output-admission seam, not a duplicate of the entire maintenance route. Endpoints: model head submission → pass-local committer → executor return → database finalizer → retained head/publication queue. Model decisions choose natural-language entries; symbolic support records, pass IDs and fixed daemon checks determine admission. The staged input is in-memory; accepted head revisions, entry provenance and publication state are in SQLite. SRC-1, `platform/daemon/src/pipeline/dreaming.ts`, `platform/daemon/src/memory-head-owner.ts`, `platform/daemon/src/db-owner-worker.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: valid staging returns STAGED_FOR_FINALIZATION; failures return codes; after successful finalization the runner returns pass ID, applied/skipped/failed counts and summary.
- Later read-back: a later content-pass read can return supported committed entries; session-start inspection can supply the current head subject to identity configuration, freshness, redaction and budget.
- Delegated visibility: the agent receives scoped head information and staging errors; the finalizer receives proposed entries, exact supports, active agent/pass IDs and current database state. A foreground host receives selected text, not the full provenance ledger.
- Selection predicate: incremental-content mode, matching active agent/pass, bounded input, current base revision, permitted source references and exact current scoped evidence; an unchanged current content hash has a NOOP branch before commitEntries.
- Invalidation or expiry: duplicate staging clears the staged input; changed base revision rejects finalization; stale generated heads are withheld from startup inspection. Pass failure does not imply undo of earlier ontology writes.
- Activation or effect: finalization can create a retained head revision and pending publication; later input supply is wired but changed model behavior is unobserved.
- Evidence limits: source establishes staged and final acceptance branches, not exercised success or semantic correctness. The unchanged-content NOOP branch means this is not a claim that every finalization revalidates every support item.

Operating mode is open content maintenance, triggered by an admitted content pass. The model proposes a complete replacement entry set under shipped guidance and prior supported entries. The daemon can veto staging and final acceptance; no human per-entry approval or independent answer oracle appears in this seam. Exact matching establishes provenance rather than truth. A failed bounded proposal can be revised in the same model session. A late finalizer failure is accounted as pass failure; publication failure is retriable separately and need not invalidate the database result.

The staging boundary (SRC-1, `platform/daemon/src/pipeline/dreaming.ts`):

> memoryHeadCommitInput = input;
> return { ok: true, code: "STAGED_FOR_FINALIZATION" };
> --- `platform/daemon/src/pipeline/dreaming.ts`

The duplicate-call branch invalidates the existing stage:

> if (memoryHeadCommitInput !== null) {
> memoryHeadCommitInput = null;
> memoryHeadCommitRejection = {
> code: "MULTIPLE_COMMIT_ATTEMPTS",
> error: "a content pass may stage only one memory-head commit",
> };
> return { ok: false, ...memoryHeadCommitRejection };
> }
> --- `platform/daemon/src/pipeline/dreaming.ts`

The database can veto a stage that has become stale (SRC-1, `platform/daemon/src/memory-head-owner.ts`):

> if (pass.head_base_revision !== revision)
> return {
> ok: false,
> code: "STALE_HEAD",
> error: "evidence or head changed outside this content pass since it started",
> revision,
> hash: currentHash,
> };
> --- `platform/daemon/src/memory-head-owner.ts`

Changed entries encounter an exact scoped-evidence check:

> if (rendered === null || !rendered.includes(quote))
> return { code: "INVALID_PROVENANCE", error: `entry ${entryId} quote is not exact scoped evidence` };
> --- `platform/daemon/src/memory-head-owner.ts`

Publication can preserve an authored file instead of completing projection:

> if (!isGenerated(db, existing))
> throw new Error("User-authored MEMORY.md preserved; remove or move it to allow generated projection");
> --- `platform/daemon/src/memory-head-owner.ts`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-dreaming-pass](runtime.md#rt-rte-dreaming-pass)

Workflow delivery criterion: executor completion is insufficient for an incremental-content pass. An accepted stage must survive finalizer admission. The finalizer records completed status even when some earlier operations failed; useful-effect outcome accounting separately distinguishes partial failure. The runner's final return contains pass ID, counts and summary, not proof that all requested changes succeeded (SRC-1, `platform/daemon/src/pipeline/dreaming.ts`). [WF-RTE-head-finalization](#wf-rte-head-finalization) supplies the distinct final output seam and its retained passages.

#### On [RT-RTE-pi-lifecycle](runtime.md#rt-rte-pi-lifecycle)

Workflow-specific downstream selection: startup does not simply inject the bytes of a generated MEMORY.md file. Inspection returns current database content for generated material, null for a stale generated head, or authored content for an authored file. Startup budgets and redacts that result; exceptions withhold working memory. This prevents a finalized head from implying unconditional delivery (SRC-1, `platform/daemon/src/memory-head-owner.ts`, `platform/daemon/src/hooks.ts`).

> content: generated ? (head?.is_current === 1 ? head.content : null) : request.content,
> --- `platform/daemon/src/memory-head-owner.ts`

> return inspected.content ? budgetIdentityContent(redactCredentials(inspected.content), budget) : undefined;
> --- `platform/daemon/src/hooks.ts`
