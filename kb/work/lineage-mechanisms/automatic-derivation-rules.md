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

The extracted note `kb/notes/many-to-many-edge-state-is-where-files-yield-to-a-database.md` gives the storage predicate this draft should use. Files remain the default for content and owner-local lineage. Relational structure is earned when automatic dependency maintenance creates churning state on a many-to-many edge with no natural owner file. That structure may begin as edge files, manifests, or generated indexes; a real database is earned when lookup, churn, and consistency demands outgrow the filesystem version.

The review subsystem demonstrates the split:

- artifact content stays in git-backed files when humans and agents need readable, editable canonical material;
- lineage events and freshness state move to an edge-state surface when automation needs indexed current-state lookup over churning many-to-many edge state.

Review markdown files are still useful report outputs, but review acceptance/freshness lineage belongs in SQLite because selectors ask stateful questions about review edges. Future edge-state surfaces should be investigated where other artifact classes develop the same shape: compiled cues over many notes, source-to-derived refresh meshes, or other automatic dependency maintainers.

The review-specific storage case now lives in [src-architecture-alternatives/review-lineage-storage-case.md](../src-architecture-alternatives/review-lineage-storage-case.md). That document tests whether the same behavior could be implemented with markdown review files, JSON/YAML run manifests, append-only event ledgers, and generated current-state indexes instead of SQLite as the canonical store.

The candidate edge-state surface for any future many-to-many dependency mesh would track facts like:

- artifact path, type, and version/hash;
- source dependencies and source versions;
- generated reports or adapted-from source packets that informed an update;
- accepted merge-back or promotion events;
- stale selectors and refresh reasons;
- regeneration commands or responsible producers;
- retirement, supersession, or direct-edit events.

The open design question is not "DB for all artifacts." It is which automatic dependency mechanisms cross the many-to-many/churning-edge boundary and what implementation weight they earn: edge files, generated index, purpose-built DB, or generic lineage DB.

## Model Provenance

Derivations are model-conditioned, but the model belongs to the derivation event or retained derivative, not automatically to the durable artifact being edited. The focused treatment is in `model-provenance.md`. The current review DB placement is not assumed optimal for every derivative type; retained generated artifacts may need model provenance in frontmatter.

The rule for this workshop:

- retained one-shot derivatives should record the model/runner/prompt or generator metadata that produced them;
- generated reports that remain inspectable should carry model provenance in frontmatter, run manifests, or DB rows, with frontmatter especially plausible for typed standalone derivatives;
- review freshness is keyed by `(note_path, criterion_path, model_partition)` because `criterion_path` identifies the assay contract and one model partition's accepted evidence does not transfer to another;
- canonical notes revised from generated reports should not grow a "last edited by model" field; if model provenance matters, record it in the commit message, merge-back event, or lineage ledger;
- deterministic generated views should record the generator/tool version rather than model metadata.

This keeps model provenance where it is useful. A report's model is part of the report's identity as a derivation. A mature note has many edit events and should not pretend its current text is "by" the last model that touched it.

## Draft Git Retention Rules

| artifact class | save in git? | why |
|---|---|---|
| Source snapshots | Yes, when the source is unstable, not versioned elsewhere, or needed as evidence. | Future derivations need the source material, not only a summary. |
| External git-backed source repos | No, unless there is a special archival reason. | The source is already versioned elsewhere and may be huge; retain reviewed revision, URL, citation format, and quote anchors instead. |
| Report producers and type contracts | Yes. | They define the repeatable derivation process. |
| Cheap candidate reports | Usually no. | Connect and friction reports are working context; rerun beats preserving churn. Anchored critique result artifacts are also generated, but their acceptance belongs to the review DB and workflows may copy their bytes for temporary audit retention. |
| Experimental process evidence | Yes while the investigation needs it. | Retain non-regenerable judgments and compared artifacts only until the aggregate conclusion is promoted; delete the temporary evidence when the investigation closes unless a continuing audit consumer justifies a durable event surface. |
| Durable source analyses | Yes. | Ingest reports and agent-memory-system reviews are derived, but they are independently useful durable analysis. |
| Model provenance for retained derivatives | Yes, in the derivative artifact or run manifest. | One-shot generated artifacts need producer provenance; canonical notes need event provenance instead. |
| Deterministic generated views | No, unless a runtime needs the file and a validator checks it. | Rebuildable truth should be checked or absent. |
| High-churn many-to-many edge state | Usually no; use edge files, a generated index, or a database. | Review acceptance/freshness lineage belongs in SQLite because selectors query current state over review edges. Similar automatic dependency meshes should expect relational edge-state, with implementation weight chosen by churn and lookup needs. Review prose can still exist as generated markdown report output. |
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
| Durable analysis derived from source | Re-run or rework when source revision, snapshot, or relevant KB context changes; preserve old analysis only if it remains historically useful. |
| Canonical artifact changed by merge-back | Detect stale source/report dependencies, regenerate candidates, apply a new merge-back edit, validate, and record the update event. |
| Review freshness state | Compare current note/criterion/model inputs to accepted DB lineage; rerun or acknowledge. Verdict pairs carry decisions; report pairs carry current evidence without endorsement. |
| Deterministic generated view | Rebuild and validate; do not hand-edit. |
| Behavior-facing compiled view | Regenerate from authoritative sources or mark stale; direct edits must either flow back to source or stay candidate-stage. |
| Adapted-from artifact | If reused, promote into a typed report, instruction, skill, or workshop artifact with lineage; otherwise discard. |

For judgmental derivatives, update usually means rework, not patching. The new artifact may be better and still not reproduce the old one. That is acceptable if the system preserves the source or a stable pointer to it and records enough lineage to explain why regeneration was triggered.

## Automation Boundary

Automatic derivation should expand where verification exists:

- deterministic validators for recomputable views;
- source hashes, revisions, and timestamps for stale selectors;
- review gates and current accepted baselines for prose quality;
- quote anchors and pinned citations for source-grounded reviews;
- human or agent review for low-oracle synthesis and merge-back decisions.

Where verification is weak, the system should still automate candidate generation, routing, and queue construction. It should slow down only at promotion, merge-back, activation, or retirement decisions whose errors would become durable behavior.
