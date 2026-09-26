# When to search sessions for evidence

## Commission and working direction

On 2026-09-25 the operator asked to record this question, map the design
space, and look for concrete mechanisms in the systems already reviewed.
The motivating observation is that telemetry needs keep expanding, while
sessions already contain much of the interaction evidence. Commonplace can
search that material for evidence worth retaining instead of anticipating
every future measurement with a dedicated field or event. This does not make
sessions complete: missing timings, unrecorded judgments, and omitted tool or
subagent output cannot be recovered by a better search.

The candidate discussed in the conversation has three purposeful searches:

1. **When a proposal becomes a settled choice:** retain alternatives,
   objections, deciding reasons, human contributions, and expectations before
   implementation outcomes can reshape their explanation.
2. **When implementation closes or is abandoned:** retain departures from the
   choice, verification, failures, costs when available, and what remains
   unmeasured. Workshop deletion is a latest safe point for extracting its
   essential evidence, but a long-running workshop may need earlier capture.
3. **When a later question arises:** search for evidence relevant to an
   evaluation, revision, repeated failure, or disputed explanation, including
   evidence against the current account.

A separate fallback must address source loss even when none of those events
occurs. It could archive sessions, extract a minimum record before expiry,
or combine both. An end-of-session pass is one possible opportunity, not a
complete fallback: sessions can crash, remain open, or end before the work
does. These are candidates to compare, not an adopted hook or schedule.

Selective extraction cannot preserve every unforeseen future inquiry. The
design must either retain a sufficiently complete source archive under our
control or explicitly accept what becomes unknowable after source deletion.
An archive expands future search options; it does not replace the essential
owned records required by the [workshop commission](./README.md).

## Separate the operations

**Capture source material.** Copy or export available session material with
identity, time range, origin, and known omissions. This can be cheap and
deterministic. A copied transcript still needs a retention policy; it is not
automatically a permanent KB artifact.

**Search and extract.** Given a question and a source scope, find relevant
episodes and retain claims with supporting excerpts or artifacts. Record
which question was asked and which sources were examined. Model extraction
can misread an episode; a summary is an interpretation, not the original
evidence. A broad summary and a targeted search serve different purposes.

**Use the retained evidence.** Add it to a decision, implementation account,
or evaluation with an explicit evidential role. Recording an observation
does not by itself justify adopting a rule, accepting a decision, marking an
implementation complete, or claiming improvement. ADR views would consume
the appropriate evidence and lifecycle state from this richer record.

These operations need not share a trigger. In particular, source capture can
precede an expensive search, and new questions can revisit captured sources.

The [2026-09-26 broader scan](./trace-derived-system-scan.md) extends this
map across all positively marked trace-derived entries in both system
collections. It adds exception-driven searches after user corrections,
recurring failures, unexpected results, or retrieval gaps; activity and heat
as prioritization signals; and concrete archival mechanisms that defer
semantic extraction. An execution opportunity (hook, timer, idle period)
and a reason to inspect evidence should be separate design choices.

## Design choices

| Choice | Alternatives and consequences |
|---|---|
| What starts a search? | An explicit question gives a focused scope; a decision or implementation event supplies a recurring question; turn/session hooks supply frequent opportunities; a periodic or age-based sweep covers work without clean closure. Combining these requires deduplication without suppressing new questions. |
| What starts source capture? | Continuous append, compaction, turn end, session end, startup backfill, or a scheduled sweep. Earlier capture reduces loss exposure; more frequent copying costs storage and processing. A hook alone leaves a gap when its process never runs. |
| What is the unit? | A session is convenient for acquisition; a decision or episode can span sessions, branches, agents, and worktrees. One session can also concern several decisions. Linking these is part of the design, not an assumed one-to-one mapping. |
| How much source survives? | Essential excerpts only, bounded transcript windows, complete exports, or raw harness files. Smaller retained sets lose future questions; broader archives increase storage, access-control, and maintenance obligations. Exports and importers may omit tool details or subagents. |
| When does expensive work run? | Synchronously at a decision boundary, queued after capture, at the next startup, or after a backlog threshold. Queues reduce interruption but require visible failures, retries, and a deadline before source loss. |
| What does “processed” mean? | Copied, examined for a named question, extracted, checked, or incorporated into a record. A single done flag cannot stand for all of these. One extraction does not exhaust a session's evidential value. |
| What identifies a scope? | Session identity plus a bounded source version or message range, linked work, extraction question/version, and disposition. An active session can grow after examination; offsets alone may be unsafe across rewritten exports. |
| Who selects and checks evidence? | The working agent, a later extraction pass, the operator, or a combination. Immediate capture has context; later review can challenge hindsight and omissions. Neither alone establishes causal attribution. |
| What survives reversal? | Failed attempts, rejected candidates, abandoned work, and original expectations should remain inspectable even when code or a proposed rule is reverted. A projection can change without deleting its evidence. |

## Mechanisms found in retained system reviews

This is a workshop inventory of mechanisms reported at the retained source
snapshots, not a new upstream review or a ranking of measured effectiveness.
The exact analyses below describe code wiring unless otherwise stated;
wiring does not establish successful operation, crash resilience, or improved
later decisions. The earlier [corpus scan](./corpus-scan.md) covers the
self-improvement articles and ADR-focused search; this pass follows the
session-capture and extraction routes.

| System and retained evidence | Trigger and mechanism | Design implication and limit |
|---|---|---|
| [oh-my-pi, RTE-23](../../reports/retained/agentic-system-analysis/AAS-2026-09-05-oh-my-pi-02/result.md) | Top-level persisted-session startup scans eligible older sessions. Age and budget rules exclude current, too-recent, too-old, or over-budget work. Model extraction and later consolidation have separate job/provenance state. | Startup can recover material without relying on its original session ending cleanly. Excluded old sessions show why a bounded scan is not an expiry guarantee. Its extracted “raw memory” is already model-produced text, not a raw transcript archive. |
| [oh-my-pi, RTE-28 and RTE-29](../../reports/retained/agentic-system-analysis/AAS-2026-09-05-oh-my-pi-02/result.md) | A committed user-message event can extract decision deltas from bounded conversational context; scheduled or forced consolidation consumes pending deltas. A separate enabled autolearn route captures after substantive top-level turns, with tool-count and mode filters. | Offers frequent decision/correction capture and later batching. Short prompts and overlapping extraction can be skipped; autolearn excludes aborted turns. Consolidated decision bullets can lose the original delta's identifiers or literal quotes. Capturing failed work therefore needs explicit coverage. |
| [GBrain, RTE-6 and RTE-24](../../reports/retained/agentic-system-analysis/AAS-2026-09-23-gbrain-01/result.md) | Optional Stop writeback uses a salience/all gate and queues extraction from a saved transcript tail. PreCompact banks a secret-scanned segment and continuation manifest. SessionEnd banks the remaining redacted transcript; a spend-gated maintenance sweep extracts from unprocessed corpus files using sidecars. | Strong example of saving source segments first and processing them later, with a sweep when immediate processing is unavailable. Stop writeback is default off. Compaction protects continuity across a context boundary; it is not itself a guarantee against later deletion of the underlying session. |
| [OpenViking, RTE-2](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-openviking-01/result.md) | Explicit commit or a configured automatic scheduler first persists archive intent, raw conversation, and a queue item; a second phase produces summary/memory material through persistent QueueFS. Automatic processing is best effort, with later write/idle opportunities to retry. | Separates archive acceptance from extraction completion. The returned task ID does not prove useful evidence has been retained. The analyzed protocol depends on storage/queue contracts; actual crash resilience was not demonstrated. |
| [instinctual-memory, RTE-1, RTE-2, and automatic hook route](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-instinctual-memory-01/result.md) | SessionEnd launches detached sync: backfill imports local sessions, then consolidation runs when backlog reaches the default 200 and an LLM extractor is configured. Explicit consolidation also exists; imports deduplicate event IDs and consolidation maintains a journal checkpoint. | Backfill plus a threshold separates acquisition from model cost. Small backlogs can remain unextracted. The Codex importer omits subagent rollouts and non-final assistant messages. A scoped consolidation advances the global checkpoint even over excluded events, so a cursor is not proof of complete examination. |
| [Supermemory, RTE-3 through RTE-5](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-supermemory-02/result.md) | Successful generation or stream flush can initiate an unawaited upload of eligible conversation content and generated text. Upload errors are caught; the inspected streaming route lacks a separate cancellation/error save path. | Convenient completion triggers can leave precisely the failed or interrupted work unrecorded. “Response finished” and “save initiated” do not prove a durable record exists. External storage completion is outside the inspected boundary. |
| [WikiSkill paper, RTE-3 through RTE-6](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-wikiskill-01/result.md) | Learning/evaluation phases turn traces into wiki material and record candidate skill changes, scores, and accept/reject outcomes. Skill rollback leaves the wiki and outcome history intact. | A workflow milestone supplies both the extraction question and a place for rejected attempts. This is a documentation-grounded mechanism, not verified execution. It supports comparison with decision/implementation milestones rather than prescribing session-wide summarization. |
| [Exoharness / Exo](../../agentic-systems/reviews/exo.md) | Messages, tool activity, and lifecycle events are logged continuously. Rebuild requests produce durable update records with reasons and eventual outcomes. Sandbox rewind preserves the event log; failed builds leave failure records while the prior binary continues. | A named consequential operation can require its own evidence record, while broad logs support later inquiry. This is capture and preservation across rollback; the review does not establish an automatic semantic search trigger over old sessions. |
| [kgai, legacy memory review](../../agent-memory-systems/reviews/kgai.md) | A Stop hook checks whether code was edited and whether `kg ingest` already ran; otherwise it blocks turn end with a record-now instruction. Authored decisions enter an append-only log with a rebuildable graph projection. | A deterministic trigger can require recording without interpreting the entire trace. The hook prompts authored capture; it does not mine decisions from transcripts or verify their truth. Its code-edit condition misses deliberation that makes no code change. This evidence is from the separately scoped legacy review. |

The inventory supplies examples of message/turn, session-end, compaction,
startup, idle, backlog, workflow-milestone, and explicit-command triggers.
No inspected mechanism above establishes a search guaranteed to finish
before a third-party harness deletes its sessions. That remains a requirement
to investigate, not a capability to infer from the presence of a timer.

## Candidate combination to test

Use decision settlement, implementation closure/abandonment, and later
evaluation questions to determine **what to search for**. Use session hooks,
startup backfill, or scheduled acquisition to keep the source available.
Use an independently monitored fallback to catch work approaching source
loss. The fallback might archive first rather than force an expensive,
unfocused extraction under a deadline.

The expanded scan adds an exception path: a correction, repeated failure,
unexpected result, or missing answer can justify a focused search before a
planned milestone. Enoch's separate scan records, evidence signals, and
proposals offer one concrete comparison; Pond and Tracecraft offer source
preservation without requiring immediate lesson extraction. These examples
are examined in the linked broader scan, not adopted as Commonplace machinery.

A session inventory would connect sources to work and distinguish captured,
examined-for-question, and retained evidence. It should expose unexamined
ranges and failed jobs. “Already summarized” must not prevent another search
for a new hypothesis. This is a candidate capability, not a selected database,
schema, or implementation task.

For the ADR placement episode, decision settlement would retain the intended
choice and its pre-implementation status. Implementation closure would add
verification and permit the shipped-architecture view to change. A later
failure investigation could search the same sessions for routing confusion
and human correction. Retention supports these distinctions; it does not
itself enforce correct ADR placement.

## Probes before choosing a policy

- **No clean ending:** terminate a session before its end hook and check what
  a later startup or sweep can recover. Also cover a workshop left open past
  the source-retention horizon.
- **Deliberation without edits:** retain a settled choice, rejected option,
  or human correction even when no code was written.
- **Many-to-many scope:** follow one decision through several sessions and
  subagents, then separate two decisions discussed in the same session.
- **New question:** revisit an already examined session for evidence against
  the current explanation. Record a new search scope without duplicating the
  source or claiming the previous search covered it.
- **Long-lived or low-activity work:** capture new material after an earlier
  extraction, and retain a rare consequential decision even when no activity
  threshold is reached. Source capture should survive lack of extraction
  budget or failure of the semantic extractor.
- **Partial and failed processing:** retry an interrupted extraction; check
  that scoped cursors, deduplication, and queue acceptance do not conceal
  unexamined material. A missed job must remain visible.
- **Reversal and hindsight:** reject or revert an implementation while keeping
  its original expectations, failure evidence, and later interpretation
  distinguishable.
- **Source loss:** remove access to sessions and test the essential owned
  record. Separately test which new questions only an archive could answer.
- **Cost:** measure capture, extraction, checking, and retrieval costs against
  the evidence recovered. Compare a focused milestone query with a generic
  session summary on the same episode.

The next design decision needs a chosen retention boundary, a concrete
trigger owner, a failure-recovery route, and evidence from these probes.
Do not select an arbitrary daily interval or backlog size merely because
another system uses one. First establish the available source lifetime,
acceptable loss, ordinary work boundaries, and processing cost.
