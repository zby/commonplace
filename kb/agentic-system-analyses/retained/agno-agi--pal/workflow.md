---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Pal's request-to-wiki compilation workflow, conditional Git delivery, verification limits and push-failure recovery."
run-id: AAS-2026-10-17-pal-e313a0902289-01
reviewed-boundary: 6516b8ede0c085e48f39f3bd04cb85b475a855dc
---

# Pal workflow report

## Workflow account

### Selected workflow and evidence boundary

The representative workflow is **compile newly ingested sources into the wiki, then synchronize the changed files when Git sync is configured**. It is selected because Pal ships both an explicit compile caller and a leader instruction naming the Compiler-to-Syncer chain. It spans model-directed transformation, persistent bookkeeping, a second specialist handoff and an external delivery attempt. Ingestion is a precondition, not an assumed Researcher stage in every compile request. The direct ingest route can populate raw files independently. This account refines [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance), [RT-RTE-team-dispatch](runtime.md#rt-rte-team-dispatch) and [RT-RTE-git-sync](runtime.md#rt-rte-git-sync); it does not declare their referents again.

Evidence is SRC-1 implementation and doctrine/design at the frozen revision. Inspection covered `pal/team.py`, `pal/agents/compiler.py`, `pal/agents/researcher.py`, `pal/agents/syncer.py`, `pal/agents/linter.py`, `pal/tools/build.py`, `pal/tools/ingest.py`, `pal/tools/wiki.py`, `pal/tools/git.py`, `app/router.py`, `app/main.py` and `context/raw/.manifest.json`. The tracked manifest is `[]`: it supplies no completed compilation example. No target code, model, service or evaluator was executed. The following is a source-supported procedure, not an observed successful run.

### 1. Request and first handoff

An HTTP caller can POST `/wiki/compile`; the custom router has an authentication dependency whose implementation is external Agno. For the ordinary request, Python supplies a fixed task to `pal.run`. A daily schedule independently supplies a more detailed compile task to `/teams/pal/runs` at 09:00 America/New_York. It tells the team to confirm that the wiki is up to date if no new documents exist. These are alternate triggers for the same maintenance work, not evidence that either has run. [SRC-1: `app/router.py`, `app/main.py`; RT-RTE-wiki-maintenance above.]

> prompt = "Compile any new raw sources into the wiki."
> --- `app/router.py`

The leader's routing table assigns compilation to Compiler. The leader is instructed to delegate briefly with the question and enough context, then synthesize the specialist output. Compiler has its own model, instructions, knowledge handle, database and tool assembly. The workflow therefore delegates the substantive source-to-article transformation rather than asking the leader to write files itself. Exact forwarded history, member-result filtering and cancellation behavior are not implemented in inspected Pal code; Agno owns that handoff machinery. The leader's five-run history setting is not evidence of a particular isolated-frame implementation. (SRC-1: `pal/team.py`, `pal/agents/compiler.py`; [RT-OBJ-agent-instructions](runtime.md#rt-obj-agent-instructions), [RT-RTE-team-dispatch](runtime.md#rt-rte-team-dispatch).)

### 2. Compiler selection, transformation and admission

Compiler is instructed to read the manifest, select entries with `compiled` false, read each complete raw document, write its summary, create or enrich concept articles, add related links and mark the source compiled. After processing all files it should update the wiki index and state. This is a model-interpreted plan, not a deterministic loop in Pal Python. Source-tracking and additive guidance constrain the requested transformation; the supplied runtime record retains those passages. The model proposes the content and chooses tool calls. No separate human approves each article in the inspected route. Source citations provide provenance, not an expected-answer oracle. (SRC-1: `pal/agents/compiler.py`, `pal/tools/build.py`; [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance).)

The tool assembler gives Compiler context-root FileTools, manifest access, wiki tools and a knowledge-update tool. Its stated raw-read/wiki-write role is not a separate filesystem grant restricted to those operations. File-tool deletion is disabled; overwrite-capable paths remain. The manifest flag update accepts a matching filename without checking whether a summary or concept exists. Index replacement writes the supplied text, and state counts are supplied arguments rather than derived article counts. Thus article content, completion flags, index and state can diverge if the model omits a step or execution stops between writes. The source does not supply a transaction covering the compile. (SRC-1: `pal/tools/build.py`, `pal/tools/ingest.py`, `pal/tools/wiki.py`; [RT-OBJ-manifest](runtime.md#rt-obj-manifest), [RT-CLM-control-scope](runtime.md#rt-clm-control-scope).)

> index_path = wiki_dir / "index.md"
> index_path.write_text(content)
> return "Wiki index updated."
> --- `pal/tools/wiki.py`

There is also an ordering discrepancy worth retaining: Compiler's own plan marks each file before the final index/state update, whereas the daily scheduled prompt lists index/state before manifest marking. Both reach the model as guidance; no inspected Pal controller resolves that order. Neither ordering makes the independent writes atomic. [SRC-1: `pal/agents/compiler.py`, `app/main.py`.]

### 3. Verification is not a release gate

Compiler is asked to cite sources and note contradictions. Those instructions request quality checks but do not independently verify the produced claims. Linter is a separately routed or scheduled health check, not a required acceptance stage before compilation or push. It is asked to inspect the index and articles, flag contradictions and structural problems, write `wiki/lint-report.md`, and update lint state. Its report can identify issues; it does not mechanically reject article admission or automatically invoke Compiler to repair them. (SRC-1: `pal/agents/compiler.py`, `pal/agents/linter.py`, `app/main.py`, `app/router.py`; [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance).)

> - Do not modify concept articles directly — report findings, let the Compiler fix them
> --- `pal/agents/linter.py`

The `force` HTTP option asks for recompilation of already compiled sources, in tension with Compiler's incremental-only guidance. It is an available caller-requested rework path, not a wired recovery policy for lint findings. No inspected handoff guarantees that the model will resolve this conflict in favor of the force request. [SRC-1: `app/router.py`, `pal/agents/compiler.py`; RT-RTE-wiki-maintenance above.]

### 4. Conditional synchronization and failure branch

When Git sync is enabled, the leader is instructed to invoke Syncer last after file changes; the instruction explicitly includes scheduled compilation. Syncer should inspect status, formulate a descriptive commit message, call `sync_push` and confirm its result. Its task concerns pending context changes, not article correctness. The exact leader-to-Syncer payload is model-selected rather than constructed by a Pal handoff function; Syncer can inspect Git status for its own change summary. (SRC-1: `pal/team.py`, `pal/agents/syncer.py`; [RT-RTE-git-sync](runtime.md#rt-rte-git-sync), [RT-CLM-control-scope](runtime.md#rt-clm-control-scope).)

> 1. Use `sync_status` to see what changed
> --- `pal/agents/syncer.py`

The Python push tool checks for an unchanged tree, otherwise stages all context changes, commits and attempts push. It does not select only the files produced by this compile. A failed commit returns without pushing; a successful commit followed by failed push returns a distinct local-only outcome. Git failure rejects a command, not the semantic content. Each Git subprocess has a timeout, but the stage return value is not checked before commit. This is best-effort synchronization, not an invariant that every admitted article is remotely delivered. [SRC-1: `pal/tools/git.py`; RT-RTE-git-sync above.]

The push-failure path has an important retry limit. After a successful local commit, the working tree can be clean while the branch remains ahead of remote. A later `sync_push` can then exit before retrying the push:

> ok, status = run_git(["status", "--porcelain"])
> if ok and not status:
>     return "Nothing to sync — no changes in context/."
> --- `pal/tools/git.py`

The earlier local commit remains available, but calling the same tool again is not a guaranteed recovery when there are no new edits. Syncer's prompt permits pull on reported conflict, yet no inspected automatic retry, rollback or clean-tree outstanding-push repair closes this failure branch. A model may report the error; successful recovery is unobserved. [SRC-1: `pal/tools/git.py`, `pal/agents/syncer.py`.]

### 5. What counts as delivered

Three outcomes must stay separate. First, local files and bookkeeping are admitted by tool calls and may subsequently be consumed through wiki/file retrieval. Second, remote delivery requires a successful push, not merely a local commit or the leader's instruction to synchronize. Third, the request returns a team response, which the HTTP route wraps as `completed`; the wrapper does not inspect article coverage, citations, flags or push status. (SRC-1: `pal/tools/wiki.py`, `pal/tools/ingest.py`, `pal/tools/git.py`, `app/router.py`; [RT-RTE-navigator-work](runtime.md#rt-rte-navigator-work), [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance).)

> content = response.content if response else "No response"
> return {"status": "completed", "force": body.force, "response": content}
> --- `app/router.py`

Without Git configuration, the team does not include Syncer and explains that changes are local. Direct Compiler exposure also bypasses the leader's sync instruction. Therefore the selected chain describes a configured leader workflow, not all ways to change wiki files. A returned response proves neither complete compilation nor durable remote availability; neither is observed here. (SRC-1: `pal/team.py`, `app/main.py`; [RT-RTE-team-dispatch](runtime.md#rt-rte-team-dispatch), [RT-RTE-git-sync](runtime.md#rt-rte-git-sync).)

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

#### On [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance)

Workflow position: Compiler is the transformation stage after leader dispatch. Linter is separate diagnosis, not a compulsory release check. Completion boundary: a returned team response is sufficient for the HTTP wrapper's completion label; semantic completeness remains unchecked there. Recovery ownership: no mandatory lint-to-Compiler transition assigns repair automatically. The caller may request rework, with force versus incremental guidance left to model interpretation.

#### On [RT-RTE-git-sync](runtime.md#rt-rte-git-sync)

Workflow position: conditional final specialist in the selected leader chain. Delivery boundary: remote push is distinct from local admission and local commit. Recovery caveat: the clean-working-tree early return can prevent a repeat `sync_push` from retrying an earlier failed push; remote backlog is not tested by that predicate. Recovery remains unresolved in the inspected workflow rather than guaranteed by repetition.
