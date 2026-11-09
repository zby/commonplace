---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Kherad workflow account tracing requested knowledge compilation through staged writes, human review, conflict recovery and published consumption."
run-id: AAS-2026-11-08-kherad-ac3e4da97ac6-01
reviewed-boundary: "2a8d6992b87a33760688e1f956653c21a6292294"
---

# Kherad workflow report

## Workflow account

### Selected workflow and evidence limits

The representative workflow is an authorized request to compile an LLM-compiled bundle, followed by review and publication of the resulting knowledge proposal. It is selected because one shipped orchestrator connects source selection, model work, staging, a merge request (MR) and publication. It is not an invented composition of unrelated agents. The compilation result is a proposed Git change, not the model's final chat message. Later bundle chat is a consumer of published files, not a subordinate task automatically launched by compilation. See [RT-RTE-indexer-compile](runtime.md#rt-rte-indexer-compile), [RT-RTE-review-merge](runtime.md#rt-rte-review-merge) and [RT-RTE-bundle-chat](runtime.md#rt-rte-bundle-chat).

This account describes implementation and instructions at the frozen revision, not a successful execution. No supplied trace establishes that a model followed the compilation rules, a reviewer inspected a diff, conflicts were resolved successfully, or publication improved answers. Added inspection within SRC-1 covers the full compile-panel component, full indexer run and prompt, full compile endpoints and the review endpoint's approval/rejection/conflict-resolution range. The UI and endpoint bodies supply implementation evidence; prompt text supplies doctrine/design. Newly inspected material remains at the registered commit. [SRC-1] `apps/web/src/components/compile/compile-panel.tsx`, `apps/api/src/agents/indexer/run.ts`, `apps/api/src/agents/indexer/prompt.ts`, `apps/api/src/routes/indexer.ts`, `apps/api/src/routes/merge-requests.ts`.

### Request and delegation

The manager-facing compile panel calls the compile API and retains the returned run ID. The API requires review permission, an existing bundle in compiled mode and configured AI settings. An existing recent running row yields 409 instead of a new run. A successful start yields 202 plus the run ID; that response means work was started, not that knowledge was delivered. The browser polls the per-run endpoint every 2.5 seconds, stops polling when the row is no longer running, and retries polling errors without a noisy alert. This is browser-side observation, not execution ownership. [RT-RTE-indexer-compile](runtime.md#rt-rte-indexer-compile); [SRC-1] `apps/api/src/routes/indexer.ts`, `apps/web/src/components/compile/compile-panel.tsx`.

> if (run.status !== "running") setActiveRunId(null);
> --- `apps/web/src/components/compile/compile-panel.tsx`

The API's background orchestrator owns progression. It hands one newly constructed indexer agent bundle-specific instructions, a configured model and tools bound to the bundle and a per-run pending map. The kickoff supplies source paths/titles, existing document names and either the full source inventory or an added/changed/deleted delta with linked document names. Bodies are available through tools rather than all being inserted initially. The model decides which reads, writes and deletions to request within a 64-step generation bound. This is application-to-agent delegation, not a foreground agent spawning independent reviewers or specialist workers. [RT-RTE-indexer-compile](runtime.md#rt-rte-indexer-compile), [RT-OBJ-pending](runtime.md#rt-obj-pending); [SRC-1] `apps/api/src/agents/indexer/run.ts`, `apps/api/src/agents/indexer/prompt.ts`.

The natural-language task asks the model to preserve accurate content, express ambiguity, keep an index and append history. For incremental compilation it asks for only related documents to change. The tool surface is not correspondingly limited to an allowlist of delta-related output paths, so the requested editing discipline is not a code-enforced guarantee. The same distinction applies to factual fidelity and citation quality. [RT-RTE-indexer-compile](runtime.md#rt-rte-indexer-compile); [SRC-1] `apps/api/src/agents/indexer/prompt.ts`.

> Do not invent facts that are not in the source pages. If a source page is ambiguous, represent the ambiguity rather than resolving it yourself.
> --- `apps/api/src/agents/indexer/prompt.ts`

Source selection is consequential: the compiler can read unmerged user-branch content through latest-source selection. Therefore the upstream material is not necessarily already approved raw knowledge. The published mirror, rather than an unmerged previous compilation proposal, supplies the comparison baseline. An unchanged-source run can succeed without a model call and without an MR. These are implemented selection and no-op rules, not evidence of optimal selection or measured savings. [RT-RTE-indexer-compile](runtime.md#rt-rte-indexer-compile); [SRC-1] `packages/core/src/git/source.ts`, `apps/api/src/agents/indexer/run.ts`.

### Verification and proposal delivery

Tool writes enter the pending map after path/frontmatter validation. They do not directly publish files. When generation returns, code requires pending writes and a root index. On an incremental run it can reuse the published index; on a first compile a missing index fails. Code synthesizes a missing log, rewrites resource URLs, builds source mirror writes and commits the combined result to the long-lived agent branch. Untouched compiled paths on that branch are overlaid from the default branch, so the proposal is assembled from published state plus this run's delta rather than blindly preserving all earlier unmerged work. A nonempty diff creates or refreshes an OKF-scoped MR; a zero diff returns success without one. [RT-OBJ-pending](runtime.md#rt-obj-pending), [RT-RTE-indexer-compile](runtime.md#rt-rte-indexer-compile).

These checks accept structurally admissible proposals, not verified truth. In particular, copying an existing index does not establish coverage of newly written concepts; synthesizing a log only when missing does not validate the history of a model-supplied log. The verifier of meaning remains the model under instructions and subsequently the human reviewer, with no reference-answer oracle established. See [RT-RTE-indexer-compile](runtime.md#rt-rte-indexer-compile).

The run's success state means the orchestration completed. The UI distinguishes success with an MR from success without one: the former offers a review link, while the latter displays its up-to-date message. This is the first delivery boundary: a proposal or no-change outcome delivered to the requester, not published knowledge. [SRC-1] `apps/web/src/components/compile/compile-panel.tsx`.

> {latest?.status === "succeeded" && latest.mrId ? (
> --- `apps/web/src/components/compile/compile-panel.tsx`

> href={`/bundles/${bundleId}/merge-requests/${latest.mrId}`}
> --- `apps/web/src/components/compile/compile-panel.tsx`

### Review, recovery and final delivery

The reviewer can approve an open MR or reject an open/conflicted one. Approval checks review permission, uses the branch's live head and requests a scoped squash merge into the default branch. This is not an immutable approval token binding the action to exactly the previously viewed diff. A successful Git change is followed by search synchronization and only then the merged database status. Publication and status recording are therefore distinct effects; the source does not establish one atomic cross-store transaction. [RT-RTE-review-merge](runtime.md#rt-rte-review-merge).

The rejection path returns the MR to draft on the same branch, clearing stored conflicts rather than permanently closing the proposal. A later compilation can reopen a draft/open/conflicted MR on the reused agent branch; `finalizeMr` replaces its base/head references and clears old conflicts when necessary. Thus rework retains the proposal identity but does not promise preservation of every rejected candidate as the next candidate. [RT-RTE-review-merge](runtime.md#rt-rte-review-merge), [RT-RTE-indexer-compile](runtime.md#rt-rte-indexer-compile); [SRC-1] `apps/api/src/agents/indexer/run.ts`, `apps/api/src/routes/merge-requests.ts`.

> const openStatuses = ["draft", "open", "conflict"] as const;
> --- `apps/api/src/agents/indexer/run.ts`

Two other failure paths have different owners. A compile exception becomes a failed run row, which the panel displays; a subsequent request marks abandoned running rows older than 30 minutes failed before starting new work. This is failure reporting and later rerun admission, not a durable queue or automatic replay. A merge conflict becomes stored marker text and conflict status; a review-authorized caller can submit resolutions and invoke the dedicated merge helper. That narrower recovery route is [WF-RTE-conflict-resolution](#wf-rte-conflict-resolution). Neither route establishes exercised recovery. A no-op approval instead returns 409 and leaves the MR open, explicitly avoiding a misleading merged outcome. [RT-RTE-indexer-compile](runtime.md#rt-rte-indexer-compile), [RT-RTE-review-merge](runtime.md#rt-rte-review-merge); [SRC-1] `apps/web/src/components/compile/compile-panel.tsx`, `apps/api/src/routes/merge-requests.ts`.

The second delivery boundary is the admitted default-branch content, made available to wiki/retrieval consumers with search synchronization in the ordinary merge path. A later chat request can read default-branch compiled documents or retrieve indexed snippets and stream an answer. This does not prove that a particular proposed fact was retrieved, believed or used. It also does not make this workflow universal: compiled remote pulls can bypass local MR review, and chat attachments can introduce raw pages outside the compiled tool surface. The ordinary workflow's human gate is real but scoped, not a guarantee that every downstream input was reviewed through it. [RT-RTE-review-merge](runtime.md#rt-rte-review-merge), [RT-RTE-bundle-chat](runtime.md#rt-rte-bundle-chat), [RT-RTE-remote-pull](runtime.md#rt-rte-remote-pull), [RT-BAP-attached-pages](runtime.md#rt-bap-attached-pages).

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-conflict-resolution
Label: Review-authorized conflict resolution

Part of: [RT-RTE-review-merge](runtime.md#rt-rte-review-merge)

This is the dedicated conflicted-MR resolution subroute of the supplied admission route, not a second declaration of ordinary approval. Endpoints/progression: stored conflict state → review-authorized GET of marker text → caller-supplied path/content array → resolution helper → search synchronization → merged MR and conflict cleanup; another detected conflict replaces conflict rows and retains conflict status. Owner: authorized reviewer supplies resolutions, API validates and invokes Git. Context/state/action effects: symbolic MR/status/path checks, natural-language resolved file content, persisted conflict marker text and resulting Git/database/search effects. [SRC-1] `apps/api/src/routes/merge-requests.ts`.

- Immediate return: updated MR on success; 400 for malformed input or missing expected paths; 409 for wrong state, missing branch or a new merge conflict.
- Later read-back: merged default-branch content reaches later wiki/retrieval consumers; remaining conflict rows can be fetched for another resolution attempt.
- Delegated visibility: inapplicable — caller/API/Git recovery, not a delegated model context.
- Selection predicate: bundle/MR identity, review permission, conflict status, submitted string path/content fields and inclusion of every stored conflicting path.
- Invalidation or expiry: success deletes conflicts and sets merged status; another detected conflict replaces stored markers; rejection through the parent route returns the MR to draft.
- Activation or effect: the API calls the Git resolution helper, synchronizes search if a prior default-branch OID exists, and records completion; actual operation and downstream behavioral changes remain unobserved.
- Evidence limits: inspected endpoint wiring only; caller identity does not establish human inspection, required-path coverage does not validate semantic correctness, and dependency/helper behavior and cross-store atomicity are not established by this endpoint.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission/recovery: the authorized caller proposes and admits resolved text through this endpoint; software can reject malformed/missing resolutions or another merge conflict. This is ongoing open-content recovery, not a scored experiment. No expected-answer oracle is supplied. Guidance available to the caller is the stored marker text; its interpretation and correctness remain unobserved. Resolution content persists in Git on success; conflicts/status persist for further attempts on another detected conflict. The route does not show automatic rollback if synchronization fails after the Git effect.

> const missing = [...expectedPaths].filter((p) => !submittedPaths.has(p));
>     if (missing.length > 0) {
>       return reply.code(400).send({ error: `Missing resolution for: ${missing.join(", ")}` });
>     }
> --- `apps/api/src/routes/merge-requests.ts`

> const result = await git.resolveMergeConflict(
>         mr.branchName,
>         bundle.defaultBranch,
>         `Merge request ${mr.id} (conflict resolved)`,
>         files,
>         mrPathPrefix(bundle, mr),
>       );
> --- `apps/api/src/routes/merge-requests.ts`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-indexer-compile](runtime.md#rt-rte-indexer-compile)

Workflow completion has two distinct outcomes: an MR for review, or success without an MR when sources/diff provide no work. Neither is equivalent to publication. The requester receives a pollable run outcome, while the model's semantic work is mediated through staged tool writes. A generation that produces no writes is a code-rejected outcome, not a request for another automatic model attempt. [SRC-1] `apps/api/src/agents/indexer/run.ts`.

> if (pending.size === 0) {
>     throw new Error("The indexer agent finished without writing any documents");
>   }
> --- `apps/api/src/agents/indexer/run.ts`

#### On [RT-RTE-review-merge](runtime.md#rt-rte-review-merge)

Workflow recovery is split between reviewer rejection/rework, no-op approval feedback and the dedicated conflicted-state subroute [WF-RTE-conflict-resolution](#wf-rte-conflict-resolution). The workflow does not automatically retry compilation after review rejection. Final publication is a Git effect followed by search/status effects, not the earlier run-success flag.
