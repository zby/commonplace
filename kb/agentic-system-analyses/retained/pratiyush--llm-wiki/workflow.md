---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "llm-wiki workflow: deferred source-page synthesis from backend request through foreground-agent completion and rejection"
run-id: AAS-2026-10-16-llm-wiki-6786c5985cdc-01
reviewed-boundary: b1088890ee0743810a92577aecad946c6b3eb2d2
---

# llm-wiki workflow report

## Workflow account

### Selection and evidence

This account selects deferred source-page synthesis: a configured `agent` backend stages work, and a later `/wiki-sync` turn supplies the synthesized body and completes the page. It is representative of the system's consequential coordination boundary: Python can deliver a durable task without running a model, while an external foreground agent must finish the semantic work. It is not representative of every backend. The workflow connects [RT-RTE-backend-synthesis](runtime.md#rt-rte-backend-synthesis) and [RT-RTE-agent-completion](runtime.md#rt-rte-agent-completion); their identities and evidence remain in the runtime member.

The evidence is implementation plus shipped host instructions, not an executed workflow. Inspection at SRC-1 extends/checks `llmwiki/synth/pipeline.py` backend selection and synthesis loop, `llmwiki/synth/agent_delegate.py` staging/completion, `llmwiki/synth/cli_helpers.py` completion return handling, `llmwiki/synth/prompts/source_page.md`, `.claude/commands/wiki-sync.md`, and `CLAUDE.md`. No target command, test, provider or external host was executed. The [boundary](boundary.md) fixes the revision and external-host limits. Successful completion, host compliance and semantic correctness remain unobserved.

### 1. Request and staging

The caller selects agent synthesis through configuration and invokes synthesis on retained raw sessions. The pipeline resolves the backend, checks availability, loads the selected template and mtime state, and selects raw files with no current state entry or a newer mtime; force bypasses that state selection. The agent-availability check is an environment heuristic, not proof of a scheduled worker. An unavailable backend produces an error summary before file processing. SRC-1: `llmwiki/synth/pipeline.py`, `llmwiki/synth/agent_delegate.py`; [RT-RTE-backend-synthesis](runtime.md#rt-rte-backend-synthesis).

For each selected file, Python passes raw body, metadata and the unrendered template to the backend. The backend replaces the body slot with the first 8,000 characters and the metadata slot with key/value text. It writes a prompt under `.llmwiki-pending-prompts/<uuid>.md`, including slug/project/date headers, and returns a placeholder with the UUID sentinel. The pipeline wraps that placeholder in page metadata and writes the project/date/slug source-page path. It advances synthesis state and counts this write as synthesized before any foreground generation occurs. The resulting source page and index can therefore exist while the content is still pending. SRC-1: `llmwiki/synth/pipeline.py`, `llmwiki/synth/agent_delegate.py`; [RT-OBJ-pending-prompts](runtime.md#rt-obj-pending-prompts).

This is durable task staging, not a subagent launch:

> The backend itself never calls the agent — that loop lives outside
> this module.  This file is pure file-I/O + sentinel handling.
> --- `llmwiki/synth/agent_delegate.py`

The backend reuses a UUID by searching pending prompt headers for the slug alone. Project and date distinguish the output path but not this reuse lookup. A matching sentinel later establishes association with a UUID, not uniqueness of source identity across projects. That is a coordination limit, not an observed collision. SRC-1: `llmwiki/synth/agent_delegate.py`; [RT-RTE-agent-completion](runtime.md#rt-rte-agent-completion).

### 2. Foreground pickup and semantic work

The next-step owner changes from the synthesis loop to the external foreground agent. `/wiki-sync` instructs that agent to run conversion first and, when new files exist, perform ordinary host ingest before scanning pending prompts. When conversion finds nothing new, it still proceeds to the pending scan. This does not mean `/wiki-sync` itself creates the staged synthesis requests: the selected workflow starts with a separate backend synthesis invocation. SRC-1: `.claude/commands/wiki-sync.md`; [RT-RTE-session-conversion](runtime.md#rt-rte-session-conversion), [RT-RTE-host-ingest](runtime.md#rt-rte-host-ingest).

> 2. **If `N == 0`**: report "wiki is already up to date" and continue to step 6 (pending-prompt scan). Don't run ingest.
> --- `.claude/commands/wiki-sync.md`

The procedure asks the agent to list pending prompts, read each prompt, generate a body, write it to a scratch file, and call completion with UUID, target page and body-file path. The list exposes UUID, slug, project and date; the agent supplies the target path rather than receiving an automatically scheduled continuation. Processing is explicitly serial:

> Process all pending prompts serially — the agent is single-conversation.
> --- `.claude/commands/wiki-sync.md`

The handoff supplies a rendered task and a truncated raw-body prefix, not a separate model frame or the complete wiki. The full raw file remains separately readable. The bundled template requests summary, claims, quotes, links, contradictions and suggested tags; a user template override can replace this guidance. A request to compare against known wiki content does not establish that the pending task delivers those pages. Ordinary host ingest separately instructs reading index and overview, but that should not be credited as guaranteed context for every pending completion. SRC-1: `llmwiki/synth/agent_delegate.py`, `llmwiki/synth/prompts/source_page.md`, `llmwiki/synth/pipeline.py`, `CLAUDE.md`; [RT-OBJ-source-page](runtime.md#rt-obj-source-page).

### 3. Verification, admission and rejection

The foreground model proposes the semantic body. Completion code decides whether that string can replace the selected page by checking page existence, presence of a pending sentinel and equality of its UUID with the supplied UUID. These checks reject an absent target, a completed/nonsentinel page or a mismatched association before the write. They do not verify claim provenance, quotations, contradictions or answer quality. No expected-answer oracle or bounded improvement experiment participates. User initiation and permission to run tools do not amount to human approval of each generated claim. SRC-1: `llmwiki/synth/agent_delegate.py`, `llmwiki/synth/cli_helpers.py`; [RT-RTE-agent-completion](runtime.md#rt-rte-agent-completion).

> if found_uid is None:
>         raise ValueError(
>             f"page has no pending sentinel: {target_page}"
>         )
> --- `llmwiki/synth/agent_delegate.py`

The requested semantic standard remains instruction-mediated:

> 2. Every claim must be traceable to something said in the session
> --- `llmwiki/synth/prompts/source_page.md`

Thus the workflow has an implemented association gate and best-effort content guidance, not an implemented content-correctness gate. The optional candidate admission mechanism is not on this direct completion path. SRC-1: `llmwiki/synth/agent_delegate.py`; [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission).

### 4. Recovery and delivery

For the selected rejection path, a UUID mismatch raises before replacement. The CLI helper catches that `ValueError`, prints an error and returns 1. Existing page and prompt are left available by this pre-write branch. The caller/foreground agent must resolve the association and resubmit; neither the completion helper nor `/wiki-sync` specifies an autonomous repair loop. SRC-1: `llmwiki/synth/agent_delegate.py`, `llmwiki/synth/cli_helpers.py`, `.claude/commands/wiki-sync.md`; [RT-RTE-agent-completion](runtime.md#rt-rte-agent-completion).

On acceptance, completion preserves recognized frontmatter, writes the supplied body in place, then attempts prompt deletion. The helper prints the completed page path and returns 0. This is the implementation's delivery boundary: a retained source page replaces the placeholder and is available for later reads. It is not evidence that a later answer used it. The helper does not itself rerun all host-ingest maintenance of entities, concepts and overview. Fresh HTML is a further caller-requested step, not part of successful source-page completion. SRC-1: `llmwiki/synth/agent_delegate.py`, `llmwiki/synth/cli_helpers.py`, `.claude/commands/wiki-sync.md`; [RT-RTE-host-ingest](runtime.md#rt-rte-host-ingest), [RT-RTE-reader-build](runtime.md#rt-rte-reader-build).

Recovery is not transactional. Prompt deletion is best effort: a completed page can coexist with a stale pending file, and retrying against that now-nonsentinel page reaches rejection. The write preserves frontmatter, not arbitrary prior body edits, despite the docstring's preservation claim. The existing runtime record documents that discrepancy; no automatic restoration of the replaced body is established. SRC-1: `llmwiki/synth/agent_delegate.py`; [RT-CLM-append-preservation](runtime.md#rt-clm-append-preservation). Serial host instructions do not establish a lock or cross-file transaction. The inspected functions expose staging, admission, errors and completion, but no execution evidence establishes that a full request reached delivery.

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

#### On [RT-RTE-backend-synthesis](runtime.md#rt-rte-backend-synthesis)

- Workflow role: Producer phase of the selected deferred workflow. Its synthesized counter marks placeholder persistence in agent mode, not completion of the delegated semantic task.
- Handoff boundary: Durable prompt plus sentinel page transfer next-step responsibility to a later foreground turn; the backend does not schedule that turn.

#### On [RT-RTE-agent-completion](runtime.md#rt-rte-agent-completion)

- Delegation: Existing foreground agent receives a rendered task through disk and is instructed to process pending work serially; no separate worker identity or isolated model context is supplied by this mechanism.
- Verification: UUID/sentinel association is accepted or rejected by code; factual and formatting compliance remain model-guided rather than admission predicates.
- Recovery owner: Caller/foreground agent handles rejected associations and retry. A pre-write rejection preserves the staged files; successful body replacement has no automatic body rollback, and best-effort cleanup can leave a stale prompt.
- Delivery criterion: Completion writes the retained body and the CLI helper reports the page path. Later retrieval, host use and publication are separate from that return, and remain unobserved.
