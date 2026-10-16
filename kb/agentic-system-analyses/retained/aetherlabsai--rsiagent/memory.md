---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "RSIAgent memory: same-Actor bank revision, Actor-directed retrieval, Curriculum state and trace-preserving context recovery."
run-id: AAS-2026-10-14-rsiagent-b11225763c0b-01
source-identity: "https://github.com/AetherLabsAI/RSIAgent"
reviewed-boundary: "4d7ef43770dda341fccd9a5743db92407687c615"
---

# RSIAgent memory report

## Boundary and evidence

The memory boundary includes canonical experience files, their guest copies and publication gates, phase checkpoints/journals, Curriculum notes and diagnosis, Actor WORK LOG/resume handoffs, Verifier history/scratch and decoder recovery, and retained image attachments. It follows the shipped OSWorld and ALE routes in [RT-RTE-task-execution](runtime.md#rt-rte-task-execution), [RT-RTE-curriculum-search](runtime.md#rt-rte-curriculum-search), [RT-RTE-learning-admission](runtime.md#rt-rte-learning-admission) and [RT-RTE-lineage-recovery](runtime.md#rt-rte-lineage-recovery). Static role charters configure these consumers but are not themselves use-derived memory. Provider weights are separate components already declared in runtime; inaccessible provider internals prevent a provider-side memory account.

All source findings use SRC-1, Git revision `4d7ef43770dda341fccd9a5743db92407687c615`. Direct source reads supply implementation evidence; quoted model instructions supply doctrine/design, not evidence of compliance. No target code, tests, examples or model calls were executed. No learned bank, live transcript or causal comparison was supplied. The boundary member supplies the source register and external dependency limits.

| Operation or surface | SRC-1 paths | Coverage and records |
| --- | --- | --- |
| CLI/phase dispatch and frozen evaluation | `run_osworld.py`, `run_ale.py`, `benchmarks/osworld/pipeline.py`, `benchmarks/ale/host.py` | Supplied runtime tracing, not fresh full-file reads; task and ALE upload sites additionally searched. [RT-RTE-task-execution](runtime.md#rt-rte-task-execution), [MEM-OBJ-memory](#mem-obj-memory). No live attachment/use established. |
| Learning and branch serialization | `explore/target_learning.py`, `explore/phase1_wave.py`, `explore/practice_loop.py`, `explore/charter.py` | Direct publication, installer and instruction reads; bounded searches of work-phase reset and checkpoints. [RT-RTE-learning-admission](runtime.md#rt-rte-learning-admission), [MEM-OBJ-memory](#mem-obj-memory), [MEM-OBJ-memory-journal](#mem-obj-memory-journal). |
| Transport, direct replacement API, audit, journal | `explore/commit.py` | Complete direct read. Direct `write_memory` API is a storage capability; repository Python call-site search found its definition only. No later consumer is inferred for an unspecified external caller. [MEM-OBJ-memory-journal](#mem-obj-memory-journal), learning annotation. |
| Actor retrieval and budget | `explore/charter.py`, `benchmarks/osworld/task.py`, `benchmarks/ale/worker.py`, `config/roles/actor.yaml` | Direct preamble/config reads and attachment-site searches; runtime supplies phase-2 details. [RT-BAP-actor-method](runtime.md#rt-bap-actor-method), task annotation. |
| Curriculum notes/outcomes and memory ablation | `explore/unified_evolution.py`, `explore/charter.py` | Direct notes reload, access-selection, diagnosis and outcome construction reads. [MEM-OBJ-curriculum-notes](#mem-obj-curriculum-notes), [MEM-OBJ-learning-diagnosis](#mem-obj-learning-diagnosis). |
| Actor folding and restart | `core/loop.py` | Direct folding, synthesis and restart reads; runtime supplies context assembly. [MEM-RTE-worklog-fold](#mem-rte-worklog-fold), [MEM-OBJ-work-log](#mem-obj-work-log). |
| Verifier filtering, private scratch | `core/verifier.py`, `core/verifier_runtime.py` | Direct checkpoint/replay and scratch-detach reads plus recovery call-site search; executor details supplied by runtime. [MEM-RTE-verifier-replay](#mem-rte-verifier-replay), [MEM-OBJ-verifier-scratch](#mem-obj-verifier-scratch). |
| Multimodal transcript replay | `llm/client.py` | Direct archive/wire conversion reads and bounded search. [MEM-OBJ-durable-images](#mem-obj-durable-images). |
| Alternative recovery admission | `explore/phase2_recovery.py`, `explore/practice_memory_recovery.py`, `explore/practice_evidence_recovery.py`, `explore/post_target_learning_recovery.py`, `explore/ready_target_recovery.py`, `tools/recover_phase1_wave.py` | Dispatch/call-site searches; direct verified-memory continuation read. Other variant bodies remain uninspected, preventing a complete account of every recovery admission check or reconstructed note. [RT-RTE-lineage-recovery](runtime.md#rt-rte-lineage-recovery) annotation retains that limit. |

No separate memory-search service, registered retrieval tool or hook is needed on the inspected routes: Actor-generated Programs perform reads through the same VM action interface. This is a positive account of those routes, not an exhaustive absence claim about all possible filesystem or generated-code access.

## Core ideas

1. **Publication is a phase boundary, not every guest write.** Work-phase edits are discarded; terminal PASS or FAIL opens a same-Actor distillation/reconciliation phase. The host admits a complete candidate tree only after transport and boundary checks. Verifier correctness judgment is not memory certification. See [RT-RTE-learning-admission](runtime.md#rt-rte-learning-admission) and [MEM-OBJ-memory](#mem-obj-memory).
2. **The bank supplies fallible advice, not mandatory executable policy.** The opening supplies names and sizes, not file bodies or a privileged index. The Actor chooses whether, what and how deeply to read through Programs. Delivery does not establish reliance. See [RT-BAP-actor-method](runtime.md#rt-bap-actor-method) and its annotation below.
3. **Different retained products have different readers.** Bank files reach future Actors; diagnosis and private notes reach Curriculum; private scratch reaches Verifier; recovery archives reach admission code. Their common filesystem substrate does not make their authority interchangeable. See the operative objects below.
4. **Context recovery has alternatives to prose summarization.** Actor folding makes a lossy WORK LOG; stalled restart may synthesize a handoff without any prior fold. Verifier decoder recovery instead retains substantive action/observation content, including pixels, and removes actionless exchanges. See [MEM-RTE-worklog-fold](#mem-rte-worklog-fold) and [MEM-RTE-verifier-replay](#mem-rte-verifier-replay).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-memory
Label: Actor-owned durable memory tree

Source-native `~/.memory` in a guest and canonical host memory directories; transported as `{relpath: bytes}`. Content schema, initial content and actual generated contents are not supplied. Natural-language lessons are requested and interpreted by Actors, while files may also contain symbolic programs/data whose force depends on a later reader or execution. Arbitrary bytes must not be classified uniformly as prose or learned knowledge. Storage is filesystem trees, with archive transport and copies for evaluation. Names/sizes are access metadata, not the content itself. Lineage is prior admitted tree plus same-Actor edits grounded in trajectory and terminal evidence; later consumers are fresh practice/target/evaluation Actors, and optionally Curriculum as evidence. This object is distinct from [RT-OBJ-loop-result](runtime.md#rt-obj-loop-result), which is a control/result interface, and from [RT-RTE-learning-admission](runtime.md#rt-rte-learning-admission), which is its update route. SRC-1: `explore/commit.py`, `explore/charter.py`, `explore/target_learning.py`.

> Update your durable memory at {memory_root} in whatever way you judge will make a
> fresh future Actor Agent more capable. You may investigate remaining questions if
> the available project state makes that useful, and you may add, revise, reorganize,
> delete, or leave memory unchanged.
> --- `explore/charter.py`

Reasons are encouraged but not schema-enforced. No supplied generated artifact establishes that explanations, uncertainty or criticism survive revision. A future Actor can read whatever survives; neither full trajectory nor final Verifier report is automatically delivered with each lesson.

#### MEM-OBJ-memory-journal
Label: Memory journal and exact-tree checkpoints

Source-native `memory_journal`, per-episode `tgz` snapshots, `journal.jsonl`, before/after trees and project checkpoints are host filesystem recovery/audit material. File bytes preserve bank content; counts, hashes, timestamps and terminal outcomes are symbolic access/lineage metadata. These are snapshots of derived memory, not raw action trajectories. Host code writes them after admission or at configured committed boundaries; launching the workflow is not human approval of their contents. Archive transport and restore do not themselves create new lessons. Later consumers include recovery admission, which validates memory manifests, and phase orchestration using frozen checkpoint trees. A journal archive alone does not establish an automatically deployed model reader. Distinct from the result interface [RT-OBJ-loop-result](runtime.md#rt-obj-loop-result); related to, not a duplicate of, the broader recovery route [RT-RTE-lineage-recovery](runtime.md#rt-rte-lineage-recovery). SRC-1: `explore/commit.py`, `explore/practice_loop.py`, `explore/phase1_wave.py`.

> """Append-only per-episode snapshot (tgz) + one meta line. Invisible to the
>     agent; pure rollback/audit insurance."""
> --- `explore/commit.py`

The implementation uses an episode-named archive path, so this description does not establish an immutable archive against repeated use of the same episode ID. Whole-tree replacement supports removal from the active bank while historical snapshots can retain removed bytes.

#### MEM-OBJ-work-log
Label: WORK LOG and resume handoff

Natural-language model summary of prior turns, held in `summary`/`LoopResult.worklog` and saved via ArtifactSink. The fallback contains deterministically shortened message text rather than model abstraction. A fresh stalled-attempt handoff can instead be synthesized from the last 60 history messages, with optional strategy review from log and six final messages. Storage is Python state plus host summary artifacts; the raw transcript remains separate. Consumers are subsequent Actor calls and fresh attempts on the same machine. This is a material retained-context part of [RT-RTE-task-execution](runtime.md#rt-rte-task-execution), not a second declaration of that route or the entire [RT-OBJ-loop-result](runtime.md#rt-obj-loop-result). SRC-1: `core/loop.py`.

> tail = history[-60:]
> --- `core/loop.py`

The raw history may contain rationale, but summary selection and input rendering can omit it. No fidelity or causal-learning claim follows from storing the log. See [MEM-RTE-worklog-fold](#mem-rte-worklog-fold).

#### MEM-OBJ-curriculum-notes
Label: Curriculum private notes

Source-native `CURRICULUM_NOTES`/`session.notes`: free-form natural-language, role-authored notes/hypotheses, read from the guest, audited, held in a persistent session and reinserted into later Curriculum charters alongside role history and outcome summaries. Host artifacts retain the associated turns. Their origin is Curriculum reasoning over supplied target/outcome/diagnosis and practice evidence, not an independently verified causal account. A nonempty read replaces the session notes after audit; an empty read in the inspected code does not clear previous notes. Later consumer is Curriculum's project/readiness decision, not the fresh Actor's private context. Distinct material from [MEM-OBJ-memory](#mem-obj-memory) and the route [RT-RTE-curriculum-search](runtime.md#rt-rte-curriculum-search), its closest supplied counterpart. SRC-1: `explore/unified_evolution.py`, `explore/charter.py`.

> curriculum_notes = notes
>                         session.notes = notes
> --- `explore/unified_evolution.py`

#### MEM-OBJ-learning-diagnosis
Label: Actor learning diagnosis

Source-native `learning_diagnosis.md`: natural-language conclusions and causal hypotheses, written by the same Actor after terminal evidence and bank reconciliation, read/audited by host code, archived, and delivered to persistent Curriculum with outcome evidence. It is not a raw transcript or a memory-approval report. Bank contents and diagnosis may differ; no enforced claim-level correspondence or rationale-preservation link was inspected. Distinct from [RT-OBJ-loop-result](runtime.md#rt-obj-loop-result) and from the whole update route [RT-RTE-learning-admission](runtime.md#rt-rte-learning-admission). SRC-1: `explore/charter.py`, `explore/target_learning.py`, `explore/unified_evolution.py`.

> Do not include private chain-of-thought or a
> turn-by-turn transcript: provide only the concise conclusions and hypotheses you
> choose to communicate.
> --- `explore/charter.py`

#### MEM-OBJ-verifier-scratch
Label: Verifier private scratch and archive

Source-native persistent Verifier scratch is a private filesystem, optionally exported into an archive and restored for a new executor. Contents are opaque in the supplied evidence: possible notes, scripts and data cannot be uniformly classified as prose. The archive preserves bytes; it is not a readable summary. Producer and consumer are the Verifier through its protected executor, with host lifecycle code controlling retention and detachment. This differs from the Actor bank and from [RT-OBJ-loop-result](runtime.md#rt-obj-loop-result). Its closest supplied route is [RT-RTE-candidate-verification](runtime.md#rt-rte-candidate-verification), whose persistence field it makes concrete. SRC-1: `core/verifier.py`; executor lifecycle is also supplied in runtime.

> archive = executor.export_scratch()
> --- `core/verifier.py`

Export failure can be tolerated only on the explicit recovery path after executor close/rollback; then a fresh private scratch boundary replaces unavailable scratch. Thus persistent conversation does not guarantee persistent scratch, and old private scratch is not fresh candidate evidence.

#### MEM-OBJ-durable-images
Label: Durable image observations

Source-native `_rsiagent_images` attachments retain MIME type, SHA256 and complete base64 image bytes in JSON-safe user messages. The schema/hash is symbolic metadata; pixels are nontext observations, not a model-generated semantic description or model parameters. The display/wire form is a data URL image attachment plus user text. Source is a supplied image observation in the agent history. Host code creates the archive representation, deduplicates attachment identities, and rehydrates them into later provider messages. A digest identifies bytes rather than selecting relevant evidence. No model-authored OCR summary is substituted on this route. Distinct from [RT-OBJ-loop-result](runtime.md#rt-obj-loop-result), though transcripts can be archived alongside results; supports [MEM-RTE-verifier-replay](#mem-rte-verifier-replay). SRC-1: `llm/client.py`, `core/verifier.py`.

> Images are stored in full, without resizing, truncation, OCR, or interpretation.
>     A digest makes the archived bytes auditable; it does not select or rank evidence.
> --- `llm/client.py`

### Routes

#### MEM-RTE-worklog-fold
Label: WORK LOG folding and restart
Part of: [RT-RTE-task-execution](runtime.md#rt-rte-task-execution)

Endpoints: Actor history → code-selected old batch → completion-generated log or deterministic digest → subsequent Actor context; a stalled resume can send an existing or freshly synthesized log into a fresh attempt. Python owns thresholds, rendering and restart eligibility; a model selects summary meaning and optional strategy advice. Retained state is [MEM-OBJ-work-log](#mem-obj-work-log), not a changed durable bank. SRC-1: `core/loop.py`, `config/roles/actor.yaml`; supplied runtime supplies the task/log/tail assembly passage.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Updated summary and covered-pair count, or factual restart handoff and optional strategy-review text.
- Later read-back: Subsequent calls receive task, summary and uncovered tail; fresh attempts receive handoff while keeping machine state, not the previous complete conversation.
- Delegated visibility: The summarizer receives the current log and selected rendered old turns; strategy review receives worklog and six final messages, not unlimited history.
- Selection predicate: When `history_keep_pairs > 0`, high-water/low-water hysteresis or legacy pair count selects oldest eligible turns outside the protected tail. Effective tail uses character budget with a six-pair floor and configured ceiling. Restart requires stalled result, allowed resumes and remaining iteration/time budget.
- Invalidation or expiry: Folded turns leave the rendered window; `_fold_input` preserves 1500-character head and 2500-character tail, omitting long middles. Summary is character-capped, preferring its top; empty-response digest fallback instead retains newest lines. Restart drops the old Actor frame. Raw archived history is separate, without automatic model dereferencing.
- Activation or effect: Code assembles later prompts with the derived material. Whether the summary changes decisions, preserves all necessary facts or improves capacity is unobserved.
- Evidence limits: Practice Actor config has `history_keep_pairs: 0` and `max_resumes: 0`; this is a conditional route, not every Actor invocation. Budgets are character heuristics and pair counts, not a proof of provider-token fit.

> rendered = "\n\n".join(
>         f"[{'YOU' if m['role'] == 'assistant' else 'ENV'}]\n"
>         + _fold_input(m["content"]) for m in batch)
> --- `core/loop.py`

Admission is automatic software scheduling plus model-authored text, without per-summary human approval or a semantic verifier. Empty output causes a digest fallback, not semantic certification. Static summarizer guidance asks for current state/key values/next steps; it is not a demonstrated revised theory. Theory-builder conditions 1–4 are not assessed as a theory-building claim here: the product may simply be a factual task log. The source supports lossy trace-fed retention for later action, not demonstrated improved capacity.

#### MEM-RTE-verifier-replay
Label: Verifier substantive replay
Part of: [RT-RTE-candidate-verification](runtime.md#rt-rte-candidate-verification)

Endpoints: raw Verifier segment/history → substantive checkpoint or semantic replay → persistent role state plus pending observation/images → next Verifier call. Host Python selects parsed Program/Look actions, excluding actionless replies. This is working-context recovery, not a new correctness verdict or bank-learning admission. SRC-1: `core/verifier.py`, `llm/client.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Recovered history, last observation text, durable images and last substantive action; raw segment remains archived.
- Later read-back: Later Verifier segments receive retained action context and the pending exact observation/pixels via recovery input; reconstructed messages rehydrate images for provider calls.
- Delegated visibility: Private Verifier context remains separate from Actor; this route returns no private scratch or full transcript to the Actor merely by replaying it.
- Selection predicate: Substantive checkpoint keeps history through the last new Program/Look. Configured or recurrent-actionless-transport recovery can rebuild all substantive pairs, joining previous results with original context before the next action.
- Invalidation or expiry: Narration/nudges that caused no machine action are excluded from live replay, not deleted from raw artifacts. No substantive action, trace or valid action reasoning is intentionally summarized by semantic replay. Session identity and executor lifecycle remain separate boundaries.
- Activation or effect: Recovered context is wired into the next Verifier attempt; no observed decoder recovery, improved judgment or factual correctness is established.
- Evidence limits: Source-supported lossless transport applies to selected substantive material, not every raw conversational turn, opaque provider state or unavailable scratch archive.

> This is an event-triggered decoder recovery, not context-length compaction: no
>     Program, Look, program trace, textual look result, or valid action reasoning is
>     truncated or summarized.
> --- `core/verifier.py`

Host code admits checkpoint content by parse/action category, not a human or model semantic vote. Its rejection ability removes actionless pairs from live context; raw artifacts preserve them for inspection. No answer oracle or claim revision is involved in this structural recovery operation.

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-learning-admission](runtime.md#rt-rte-learning-admission)

Memory-specific lineage: raw Actor decisions/actions/observations plus terminal Verifier report → same-context draft → whole-corpus reconciliation → candidate bytes → transport/path/leakage checks → journal/install → inventory and selected files in future Actor calls. Work-phase memory edits are discarded before this phase. In parallel waves each branch first receives the latest canonical tree at its serialized commit, not simply its pre-wave snapshot. This makes a lost-update counterexample less direct; it does not prove the Actor notices every new sibling lesson. SRC-1: `explore/phase1_wave.py`, `explore/target_learning.py`, `explore/practice_loop.py`.

> _push_canonical_memory(hooks, branch.vm, str(canonical_memory_dir))
> --- `explore/phase1_wave.py`

Admission control is split: Actor authors and decides semantic readiness; host enforces physical/path and corpus boundaries; Verifier certifies project state, not explanations or lessons; no per-content human decision is wired. `silent_audit` can return a subset, but the caller rejects the whole terminal candidate when that subset differs. Filtering bytecode at transport is another distinct cleanup, not semantic curation. Corpus overlap uses lowercased eight-word shingles with authorized-target exceptions; it is neither an instruction-execution sandbox nor factual truth checking. SRC-1: `explore/commit.py`, `explore/target_learning.py` and the retained rejection quote in runtime.

> if "__pycache__" in rel or rel.endswith((".pyc", ".pyo")):
>                 continue
> --- `explore/commit.py`

Requested content curation includes revising/removing unsupported causal explanations and stale assumptions. Actual changed meaning is unobserved. Reasons need not be stored in a mandatory structure; diagnosis separately carries selected hypotheses to Curriculum. Whole-tree replacement removes withdrawn advice from the active bank while journals can retain history. The staging installer fsyncs and renames with exception recovery, not an always-visible crash-proof swap. The direct `write_memory` API has weaker destructive replacement semantics and no caller-established admission/read-back route in the inspected call-site search; it must not inherit the staged install guarantee. SRC-1: `explore/practice_loop.py`, `explore/commit.py`, `explore/charter.py`.

> Look for conflicting assertions,
> unsupported causal explanations, stale environment assumptions, and conclusions
> broader than the observed evidence.
> --- `explore/charter.py`

#### On [RT-BAP-actor-method](runtime.md#rt-bap-actor-method)

Bank advice has model-interpreted authority at the later Actor; the upload itself has no fixed rule converting a lesson into action. Inventory contains names/sizes only; there is no body injection, privileged `INDEX.md`, semantic ranking or fixed retrieval count in the inspected preamble. Task/relevance judgments belong to the foreground Actor, who can list/search/preview/read/reread through Programs. No bank-length or mandatory file-read budget is imposed by this prompt; action/context limits still constrain actual reading. Source trust is explicitly fallible. SRC-1: `explore/charter.py`; the fallibility passage is retained in runtime.

> The mechanical listing contains names and sizes only.  No file body is
>     injected into context and no filename, including ``INDEX.md``, is privileged.
> --- `explore/charter.py`

#### On [RT-RTE-task-execution](runtime.md#rt-rte-task-execution)

Read-back direction is mixed: host automatically pushes the complete bank copy and access inventory on attachment; the Actor independently chooses subsequent content reads. The initial inventory is not proof of targeted content selection. After folding or recovery the prompt asks the Actor to reconsider both useful and unread memory; that is an instructed reload opportunity, not automatic restoration of omitted file contents. Phase-3 host freeze and no writeback do not freeze the guest filesystem. OSWorld standalone upload failure can continue memory-OFF, whereas ALE upload failure raises, so planned assignment cannot establish delivery. SRC-1: `explore/charter.py`, `benchmarks/osworld/task.py`, `benchmarks/ale/worker.py`; supplied runtime additionally traces phase-2 behavior.

#### On [RT-RTE-curriculum-search](runtime.md#rt-rte-curriculum-search)

Persistent Curriculum receives accumulated role history, private notes, project PASS/FAIL summaries and complete latest outcome/diagnosis; later search decisions interpret this material. Canonical bank exposure is separately configurable: read-only evidence copy or the `none` ablation's empty tree, while Actor learning remains enabled. Source selection is therefore a software mode decision before Curriculum's discretionary inspection. Private rationale does not automatically cross into a fresh project Actor context. SRC-1: `explore/unified_evolution.py`, `explore/charter.py`.

> curriculum_memory_dir = lineage / "curriculum_empty_memory"
> --- `explore/unified_evolution.py`

Notes are model-authored, then host-audited and retained; the audit can veto a boundary violation but does not validate bottleneck hypotheses. The supplied runtime's theory assessment remains bounded to instructed/model-afforded hypotheses and wired iteration, without an observed generated theory, criticism or capacity gain.

#### On [RT-RTE-candidate-verification](runtime.md#rt-rte-candidate-verification)

Persistent Verifier history, pending exact observations and private scratch have different retention mechanisms. [MEM-RTE-verifier-replay](#mem-rte-verifier-replay) can retain substantive history even when a scratch export fails; [MEM-OBJ-verifier-scratch](#mem-obj-verifier-scratch) may be discarded under explicit recovery tolerance. Persistence does not remove the requirement for fresh candidate inspection, nor make private Actor memory correctness evidence. SRC-1: `core/verifier.py`; current-candidate gating and masking are supplied by runtime.

#### On [RT-RTE-lineage-recovery](runtime.md#rt-rte-lineage-recovery)

Additional direct evidence covers verified-practice memory-filesystem recovery, not every variant. It requires saved terminal verdict, complete same-Actor history and unchanged committed bank; restores fixtures/candidate into a fresh VM; continues failed distillation with charged remaining budgets; and explicitly does not rerun Actor work or Verifier judgment. The recovery handoff discloses that scratch outside the archived candidate is absent. This preserves a distinct checkpoint form: full saved learning history plus material candidate, rather than a prose worklog or bank snapshot alone. SRC-1: `explore/practice_memory_recovery.py`.

> require(plan['partial_guest_memory_written'] is False, 'partial guest memory needs its own recovery')
> --- `explore/practice_memory_recovery.py`

> 'failed learning history are retained. Previous private scratch files '
>                             'outside that candidate are absent. Continue this unfinished learning phase.\n')
> --- `explore/practice_memory_recovery.py`

This route cannot silently adopt partial guest edits as canonical lessons. Dispatch also exposes unverified-practice, post-target-learning and ready-target recovery alternatives; their full reconstruction semantics remain uninspected here. The supplied runtime's broader admission limits remain in force.

## Write side

The operative write/admission mechanisms are separated above rather than conflating generated content with filesystem I/O:

- The same Actor authors the bank and chooses add/revise/delete/no-change; code schedules learning after terminal evidence, audits and installs. Failed projects are valid inputs, but are not to be recorded as verified successes. [RT-RTE-learning-admission](runtime.md#rt-rte-learning-admission) and [MEM-OBJ-memory](#mem-obj-memory).
- Host transport excludes bytecode; the corpus audit can reject a candidate; whole-tree installation can withdraw active content. Snapshotting preserves prior trees for recovery but supplies no semantic undo of a misleading lesson. [MEM-OBJ-memory-journal](#mem-obj-memory-journal).
- Diagnosis is a separate model-authored trace-derived product. Curriculum notes and latest outcomes retain selected reasons for future project selection, not future Actor delivery by default. [MEM-OBJ-learning-diagnosis](#mem-obj-learning-diagnosis), [MEM-OBJ-curriculum-notes](#mem-obj-curriculum-notes).
- WORK LOG folding and restart synthesis are trace-fed transformations retained for later Actor decisions. Verifier filtering and image rehydration preserve selected raw observations without claiming to extract lessons. [MEM-RTE-worklog-fold](#mem-rte-worklog-fold), [MEM-RTE-verifier-replay](#mem-rte-verifier-replay).
- Operator launch, recovery-plan selection and optional initial snapshot attachment are not per-lesson approval. Provenance and control of arbitrary initial supplied bank contents remain unresolved; known subsequent transformations still stand. SRC-1: `benchmarks/osworld/task.py`, `explore/commit.py`, with attachment tracing supplied by runtime.

The distillation/reconciliation instructions explicitly request causal restraint and corpus repair, but there is no supplied generated memory instance establishing compliant criticism, retained rationale or improved future capacity. The independent theory-builder and self-improvement assessments remain those qualified in [RT-RTE-learning-admission](runtime.md#rt-rte-learning-admission), not upgraded by an installed tree or recovery receipt.

## Read-back

Bank read-back has two selectors: software chooses the attached snapshot/mode and sends the complete metadata inventory; the Actor chooses task-relevant file content and receives it as Program output. Curriculum can instead receive an empty bank while still receiving notes/outcomes/diagnosis. Verifier reads its own retained state, not automatically the Actor's bank. Journals and manifests are primarily host admission/recovery inputs. These paths have distinct authority and trust boundaries; see the annotations and object records.

Actor folding replaces visible old turns with a summary and protected tail. Stalled restart keeps the machine and selected handoff while discarding the old context. Fresh project/target/vision/Verifier frames isolate selected inputs and let only explicit reports, outcomes or retained files cross back. That resembles frame allocation/return, but omitted context is not an automatically dereferenceable pointer: the Actor generally must re-probe the machine or explicitly read still-present files. SRC-1: `core/loop.py`, `explore/charter.py`; frame isolation is also traced by [RT-RTE-task-execution](runtime.md#rt-rte-task-execution) and [RT-RTE-curriculum-search](runtime.md#rt-rte-curriculum-search).

> If new evidence changes your understanding,
> you become stalled, or earlier context is compressed, reconsider both previously
> useful and unread memory.
> --- `explore/charter.py`

No automatic ranked retrieval or proven reliance follows from this instruction. Likewise substantive Verifier replay supplies preserved observations but does not establish that a later judgment correctly uses them. No route here has observed activation or causal benefit evidence.

## Integration issues

1. **No supported correction to the supplied runtime's central bank account.** It already separates memory admission from factual certification, host freeze from guest mutability, and instruction from observed learning. This report adds object-level fields and alternative context products rather than superseding that account.
2. **Containment, not duplicate route declarations.** [MEM-RTE-worklog-fold](#mem-rte-worklog-fold) is a part of [RT-RTE-task-execution](runtime.md#rt-rte-task-execution); [MEM-RTE-verifier-replay](#mem-rte-verifier-replay) is a part of [RT-RTE-candidate-verification](runtime.md#rt-rte-candidate-verification). [MEM-OBJ-work-log](#mem-obj-work-log) overlaps the `worklog` field of [RT-OBJ-loop-result](runtime.md#rt-obj-loop-result), but denotes retained text and its derivations, not the complete result interface. Other new objects have no identical supplied declaration after comparison; their closest routes/objects are cited in their records.
3. **Initial memory provenance is not established.** [MEM-OBJ-memory](#mem-obj-memory) can arrive from a supplied host directory. Attachment checks do not identify whether a human authored/approved that initial content. Consequence: no system-wide classification of all memory as autonomous trace-derived content, despite known automatic downstream updates. SRC-1: `benchmarks/osworld/task.py`, `explore/commit.py`.
4. **Recovery coverage remains partial.** [RT-RTE-lineage-recovery](runtime.md#rt-rte-lineage-recovery) has additional verified-memory evidence here, but other dispatched variants and full parallel-wave recovery remain bounded searches rather than full inspection. No exhaustive recovery guarantee or complete lineage reconstruction claim is made. SRC-1: `explore/phase2_recovery.py`, `tools/recover_phase1_wave.py`, `explore/practice_memory_recovery.py`.
5. **Payload and rationale are not supplied.** [MEM-OBJ-memory](#mem-obj-memory), [MEM-OBJ-curriculum-notes](#mem-obj-curriculum-notes) and [MEM-OBJ-verifier-scratch](#mem-obj-verifier-scratch) have known storage/consumers but no actual generated content. This prevents claim-level semantic/form classification, observed theory criticism and benefit attribution; it does not invalidate the known routes. SRC-1: `explore/charter.py`, `explore/unified_evolution.py`, `core/verifier.py`.

## Limitations and checks

HEAD was rechecked as `4d7ef43770dda341fccd9a5743db92407687c615`; source status was clean. The invoked job, member types, worker rules and complete record contract were read; this report preserves their memory-role scope and the supplied run/source identities. Registered source identity was not expanded. Available-but-uninspected files are identified above, not called access gaps or absences. No target execution or provider behavior was observed. All implementation claims are limited to inspected wiring; installed and delivered content is not proven used, true or beneficial.

Deterministic validation: the required `commonplace-run validate-output` check passed: “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” This validates structure and quotation occurrence, not semantic correctness or coordinator acceptance.
