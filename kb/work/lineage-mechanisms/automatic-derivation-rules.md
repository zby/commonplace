# Automatic derivation rules

This draft names the rule Commonplace needs before increasing automatic derivation throughput. Automation should generate more reports, candidates, cues, reviews, summaries, and edits; git should retain only the artifacts or state that future automation and review actually need.

## Automation Requirement

The goal is not to preserve every LLM output. The goal is to let the system do more work automatically while preserving enough lineage to:

- rerun the producer when inputs change;
- decide whether a generated output is stale;
- merge useful findings into canonical artifacts;
- audit why a canonical artifact changed;
- retire or regenerate derived content when sources move;
- escalate only the parts whose verification is still too judgment-heavy.

The bitter-lesson-compatible posture is: generate broadly, verify cheaply where possible, keep candidate artifacts cheap, and retain the state that lets future runs improve or correct the library.

## Content Files And Lineage State

The review subsystem suggests a general storage split:

- artifact content stays in git-backed files when humans and agents need readable, editable canonical material;
- lineage events and freshness state move to a queryable store when automation needs indexed current-state lookup, append-only events, selectors, queues, or high-churn metadata.

Review markdown files are still useful report outputs, but review acceptance/freshness lineage belongs in SQLite because selectors ask stateful questions. A future artifact-lineage store could apply the same split to notes, source ingests, agent-memory-system reviews, compiled views, cues, and merge-back edits without moving those artifacts' content out of git.

The review-specific storage case is extracted in `review-lineage-storage-case.md`. That document tests whether the same behavior could be implemented with markdown review files, JSON/YAML run manifests, append-only event ledgers, and generated current-state indexes instead of SQLite as the canonical store.

The candidate store would track facts like:

- artifact path, type, and version/hash;
- source dependencies and source versions;
- generated reports or ad-hoc distillations that informed an update;
- accepted merge-back or promotion events;
- stale selectors and refresh reasons;
- regeneration commands or responsible producers;
- retirement, supersession, or direct-edit events.

The open design question is whether this remains review-only, becomes a git-tracked ledger, or becomes a SQLite lineage database for all artifacts.

## Draft Git Retention Rules

| artifact class | save in git? | why |
|---|---|---|
| Source snapshots | Yes, when the source is unstable, not versioned elsewhere, or needed as evidence. | Future derivations need the source material, not only a summary. |
| External git-backed source repos | No, unless there is a special archival reason. | The source is already versioned elsewhere and may be huge; retain reviewed revision, URL, citation format, and quote anchors instead. |
| Report producers and type contracts | Yes. | They define the repeatable derivation process. |
| Cheap candidate reports | Usually no. | Connect reports and many critique/friction reports are working context; rerun beats preserving churn. |
| Durable source analyses | Yes. | Ingest reports and agent-memory-system reviews are derived, but they are independently useful durable analysis. |
| Deterministic generated views | No, unless a runtime needs the file and a validator checks it. | Rebuildable truth should be checked or absent. |
| High-churn operational lineage state | Usually no; use a state store. | Review acceptance/freshness lineage belongs in SQLite because selectors query current state and append events. That may generalize to all artifact lineage. Review prose can still exist as generated markdown report output. |
| Behavior-facing compiled views | Only with explicit source hash, generator, regeneration rule, and direct-edit policy. | A compiled cue, prompt, or skill projection must not drift into independent policy. |
| Merge-back provenance | Maybe not the report, but yes to enough provenance. | If a report causes a note edit, the new note version is canonical; the derivation event still needs to be recoverable. |

The short rule: commit sources, contracts, durable analyses, and canonical artifacts. Do not commit cheap automatic intermediates unless they become evidence, state, or a durable review surface.

## Merge-Back Lineage

The common automatic workflow is:

1. gather or select source context;
2. generate a typed report;
3. merge selected findings into a canonical artifact;
4. discard, regenerate, or archive the report according to its class.

This started with connect reports over immutable source snapshots, but the same pattern applies when running connect or review over a note. If a note is revised from its own connect report, the new note version is derivative from:

- the previous note version;
- the generated report;
- any source artifacts the report loaded or recommended;
- current collection/type rules;
- the merge decision made by an agent or maintainer.

That does not make the note a disposable derivative. The note remains the canonical library artifact. The derivative relation belongs to the update event, not necessarily to the whole file's identity. A mature note may have many derivative update events while still serving as canonical source for future readers.

The mechanism probably needs one of these surfaces:

- commit-message conventions for lightweight derivation events;
- a git-tracked change log for durable merge-back events;
- a SQLite or JSONL lineage ledger for high-volume automatic updates across all artifacts;
- source-side pointers only when a source edit should interrupt downstream derivatives.

The workshop needs to decide which surface is enough for each authority level.

## Updating Derived Content

Derivative content needs an update mechanism before automation scales:

| derivative class | update mechanism |
|---|---|
| Cheap report instance | Regenerate from current inputs; old instance can disappear. |
| Durable analysis derived from source | Re-run or re-distill when source revision, snapshot, or relevant KB context changes; preserve old analysis only if it remains historically useful. |
| Canonical artifact changed by merge-back | Detect stale source/report dependencies, regenerate candidates, apply a new merge-back edit, validate, and record the update event. |
| Review freshness state | Compare current note/gate/model inputs to accepted DB lineage; rerun or acknowledge. |
| Deterministic generated view | Rebuild and validate; do not hand-edit. |
| Behavior-facing compiled view | Regenerate from authoritative sources or mark stale; direct edits must either flow back to source or stay candidate-stage. |
| Ad-hoc distillation | If reused, promote into a typed report, instruction, skill, or workshop artifact with lineage; otherwise discard. |

For judgmental derivatives, update usually means re-distillation, not patching. The new artifact may be better and still not reproduce the old one. That is acceptable if the system preserves the source or a stable pointer to it and records enough lineage to explain why regeneration was triggered.

## Automation Boundary

Automatic derivation should expand where verification exists:

- deterministic validators for recomputable views;
- source hashes, revisions, and timestamps for stale selectors;
- review gates and acceptance ledgers for prose quality;
- quote anchors and pinned citations for source-grounded reviews;
- human or agent review for low-oracle synthesis and merge-back decisions.

Where verification is weak, the system should still automate candidate generation, routing, and queue construction. It should slow down only at promotion, merge-back, activation, or retirement decisions whose errors would become durable behavior.
