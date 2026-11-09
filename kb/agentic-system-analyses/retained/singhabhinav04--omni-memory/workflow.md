---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Omni-Memory workflow: installed session retrieval, source-use checking, transcript capture and delivery to a later session."
run-id: AAS-2026-11-08-omni-memory-09378abbfe6b-01
reviewed-boundary: "20f9f9ffd7ece0c6514542677ba6a549841f5536"
---

# Omni-Memory workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is one installed coding session's memory lifecycle: session start → task-specific retrieval → source-use checking → pre-compaction/end capture → retained context for a later session. It was selected because the shipped hooks connect its stages and the packaged skill explains the foreground agent's responsibilities. This is a multi-step memory workflow, not evidence that Omni-Memory delegates or completes a coding task. The host owns the user request, tools, compaction and final answer; Omni-Memory owns its CLI transitions and returned memory products. SRC-1: `hooks/hooks.json`, `omni_memory/skills/omni-memory/SKILL.md`; [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery), [RT-RTE-capture-admission](runtime.md#rt-rte-capture-admission).

All findings below concern implementation or shipped instructions at the frozen revision. No observed execution or causal experiment is registered in [the boundary](boundary.md). Source inspection adds detailed coverage of the transcript window/cursor handoff in `omni_memory/cli.py` and `omni_memory/session_memory.py`, and candidate filtering in `omni_memory/cleanup.py`. Those are SRC-1 implementation evidence, not new sources. Host behavior and provider internals remain outside the inspected implementation.

### 1. Start and retrieve

SessionStart invokes `hook start`. The CLI checks enabled state, clears session read/witness state, imports eligible shared memory, refreshes repository-derived state and rewrites the managed AGENTS.md block. In default session mode it prints recent events and a ranked seed; manual mode suppresses the seed, not the managed-file update. The host must deliver the hook output or load the file for the model to see it. [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) supplies the source evidence and selection limits.

For a particular user task the skill asks the foreground agent to run `inject` before making architectural assumptions. Python selects and renders stored claims using query, branch, file and graph context. The handoff supplies selected text, IDs and source/status markers, not the full database or an independently established answer. Truncation and duplicate suppression control what enters the host window; later retrieval can access retained rows again. The foreground agent, not the injector, decides how to use the block and whether to inspect code. Its ordinary coding actions and final answer remain external. [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery), [RT-BAP-agent-context](runtime.md#rt-bap-agent-context).

The packaged skill also requests foreground extraction at task end; this is not an automatic delegation to another worker:

> **Capture the memories yourself at the end of a task** — the SessionEnd hook's
> automatic capture is a FREE heuristic pass (no `claude -p`, to save tokens), so the
> high-quality extraction must come from you, the agent, running
> --- `omni_memory/skills/omni-memory/SKILL.md`

This is doctrine/design from SRC-1. Actual hook extraction can instead use an allowed API provider or opted-in agent backend, so the instruction does not establish that all automatic capture is heuristic. [RT-RTE-capture-admission](runtime.md#rt-rte-capture-admission).

### 2. Check source movement, without a task acceptance gate

PostToolUse can record file digests. Injection pins sources, and explicit `used <id>` compares those pins against current files. Capture later scans cited IDs and performs retrospective checks. Changed or missing sources produce diagnostics; zero bound sources does not count as clean verification. These checks can reject reliance on unchanged-source assumptions, but cannot establish the semantic truth of a claim. The caller must revalidate or re-source the memory. No inspected route makes a successful digest check a prerequisite for the host's tool action or final answer. The existing record carries the minimum implementation passages: [RT-RTE-use-check](runtime.md#rt-rte-use-check).

Thus verification ownership is divided: software diagnoses source movement; the foreground agent interprets warnings and decides corrective work. A delivered memory block or a citation is not proof that the model complied or that the coding task passed verification. [RT-BAP-agent-context](runtime.md#rt-bap-agent-context).

### 3. Extract and admit

PreCompact and SessionEnd invoke the capture branch with a transcript path. The CLI resumes that path's persisted line cursor, flattens textual message content and passes it to `capture_from_json`. This supplies conversation text rather than arbitrary tool-result payloads. In the model branch the backend receives a static extraction prompt and a shorter prefix of that text; it proposes JSON candidates, not task actions. JSON supplied directly by the foreground agent bypasses the extraction model. [RT-RTE-capture-admission](runtime.md#rt-rte-capture-admission); the unequal windows are detailed in [WF-RTE-window-handoff](#wf-rte-window-handoff).

The extractor prompt asks for durable one-sentence project claims, file/symbol anchors and stated/inferred evidence. Cleanup then rejects noise; source-sensitive clamping prevents machine capture from self-declaring verified evidence. The admitted result is text plus provenance/status fields in SQLite, not hidden model reasoning. Software admits content without a required human per-item approval. Neither digest binding nor cleanup supplies an answer oracle for the claim's meaning. [RT-RTE-capture-admission](runtime.md#rt-rte-capture-admission).

A concrete rejection path is cleanup of question-shaped candidates. It applies before `remember` and therefore before storage, rather than merely adding a warning. SRC-1 implementation:

> if t.endswith("?"):                       # questions aren't durable facts
>         return True
> --- `omni_memory/cleanup.py`

> if is_noise(text, it.get("files"), it.get("symbols"), source):
>             dropped += 1
>             continue
> --- `omni_memory/cleanup.py`

This syntactic rejection is not semantic review. Other cleanup predicates reject scaffolding, fragments and metrics; strict sources additionally need concrete naming/anchors. Inspection establishes these checks, not their precision or recall on genuine sessions. SRC-1: `omni_memory/cleanup.py`.

### 4. Recovery and delivery

If allowed model extraction raises, capture switches to local heuristic extraction with the stricter source label; an empty successful extraction need not trigger fallback. Malformed JSON-looking explicit input rejects rather than being shredded into heuristic facts. These are different failure policies, not a general retry-until-correct mechanism. [RT-RTE-capture-admission](runtime.md#rt-rte-capture-admission).

The capture hook increments valid cited IDs' use counts, attempts retrospective source checking, writes the digest and attempts AGENTS.md regeneration, records a capture event when candidates were counted, and optionally updates the author's team shard. It then saves the transcript cursor. Some subsidiary failures are swallowed, while a digest failure can reach the outer hook catch before cursor persistence. There is no single transaction establishing consistent delivery across all rows, projections, feedback and offset state. SRC-1: `omni_memory/cli.py`; [RT-RTE-shared-import](runtime.md#rt-rte-shared-import).

> except Exception:  # noqa: BLE001 — a broken hook must not break the session
>         return 0
> --- `omni_memory/cli.py`

The outer hook policy preserves host continuation, not successful memory delivery. Next-session refresh or explicit retrieval supplies the read-back path, but does not prove that every candidate or every transcript segment was retained. In particular, the window handoff below can advance past text never presented to the extraction model. This qualifies capture completeness without denying the implemented retention route.

The workflow's terminal products are CLI context/status, stored memory and generated digest/managed context. Delivery means writing or returning those products through the named paths, not correctness of their content, host consumption, successful coding work or measured improvement. [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery), [RT-RTE-capture-admission](runtime.md#rt-rte-capture-admission).

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-window-handoff
Label: Transcript cursor to extraction window

Part of: [RT-RTE-capture-admission](runtime.md#rt-rte-capture-admission)

This is the internal input-window/cursor subroute of capture, not a second end-to-end admission route. Owner: CLI reader and capture adapter. Endpoints: JSONL path plus saved line offset → flattened text → optional model prefix → updated offset in store metadata. The line cursor and budgets are symbolic controls; the flattened conversation is natural-language input. SRC-1: `omni_memory/cli.py`, `omni_memory/session_memory.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Reader returns flattened text and the consumed line position to the hook; model extraction receives only the first 30000 characters of that text.
- Later read-back: The saved per-path cursor selects where a later PreCompact or SessionEnd read resumes. Accepted candidates enter the parent route's later memory retrieval.
- Delegated visibility: Optional model sees EXTRACTION_PROMPT and the prefix, not all text over which the reader cursor advances. Local heuristic fallback receives the full flattened batch.
- Selection predicate: Reader skips lines before the saved offset, keeps string text and text-type blocks, and stops before another line once its accumulated budget has reached 140000 characters. A single included line can exceed that budget. Model slicing separately caps input at 30000 characters.
- Invalidation or expiry: Subsequent hooks resume at the returned line position after cursor persistence. No compensating cursor adjustment for the shorter model input is present in this inspected path.
- Activation or effect: Long batches can leave flattened text after the model prefix unexamined by that model while the cursor moves beyond it. Citation scanning still sees the full flattened batch; it does not recover omitted extraction input.
- Evidence limits: This is a reachable source-level mismatch, not an observed loss incident. Exact loss depends on transcript size, selected backend and successful processing. It does not imply loss on short batches or on full-batch heuristic extraction, nor preclude separate foreground JSON capture of the same knowledge.

The reader's budget and returned position:

> _TRANSCRIPT_BUDGET = 140_000
> --- `omni_memory/cli.py`

> return "\n".join(out), used
> --- `omni_memory/cli.py`

The adapter's separate cap:

> _LLM_WINDOW = 30_000
> --- `omni_memory/session_memory.py`

> items = llm.extract_memories(EXTRACTION_PROMPT, raw[:_LLM_WINDOW])
> --- `omni_memory/session_memory.py`

The hook saves the reader's position, not a model-consumption position:

> offsets[tpath] = total
>             s.set_meta("capture_offsets", offsets)
> --- `omni_memory/cli.py`

The route controls extraction context, not the host's compaction summary. It retains selected claims through its parent admission path; it does not preserve a model-visible verbatim tail or establish an isolated task frame. Missing complete input can constrain later memory content even when all downstream writes succeed.

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-capture-admission](runtime.md#rt-rte-capture-admission)

Workflow role: durable handback from a coding session to later memory consumers. Foreground JSON capture is requested by the skill; unattended hook capture is a separate implemented attempt, not proof that the foreground agent followed that instruction. Recovery differs by failure point: provider exceptions can fall back, noise candidates can be rejected, and the outer hook can silently stop. Completion of the hook is therefore not a reliable all-products acceptance signal. The internal window subroute above bounds completeness independently of admission quality.

#### On [RT-RTE-use-check](runtime.md#rt-rte-use-check)

Workflow role: source-movement diagnostic during use and retrospective citation processing. It does not accept or reject the external coding task. Corrective revalidation belongs to the foreground consumer; no observed recovery or task outcome is established.
