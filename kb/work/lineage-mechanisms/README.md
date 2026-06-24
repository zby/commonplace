# Lineage mechanisms workshop

## Purpose

Create a more universal lineage mechanism for Commonplace's growing set of derived materials: source ingests, connect reports, critique reports, review state, generated indexes, compiled views, skills, cue surfaces, source-to-source comparisons, agent-memory-system reviews over external repositories, ad-hoc distillations, and future automatic derivations.

The critical requirement is automation. Commonplace should get more bitter-lesson-compatible by making discovery, extraction, review, synthesis, cue generation, report generation, refresh, and merge-back increasingly automatic. The lineage mechanism should be the substrate that makes that safe: it should say what a derived artifact depends on, what role it plays, whether it can be regenerated, when it should be refreshed or retired, whether it belongs in git, and why the source material remains necessary even when a derived artifact is more useful for a particular consumer.

## Why now

Commonplace is already accumulating more kinds of derived material, and that trend should accelerate. A more bitter-lesson-compatible KB should use more automatic processes for discovery, extraction, review, synthesis, cue generation, report generation, compiled views, update proposals, merge-back edits, and stale-content refresh. That increases the need for lineage rather than reducing it: automatic generation is cheap only if the system can tell what to rerun, what not to commit, what state to preserve, and what canonical artifact must be updated.

The existing theory is strong but scattered:

- `lineage` is already defined as the dependency information needed for invalidation, regeneration, retirement, rollback, and review.
- Artifact analysis treats lineage as one axis beside storage substrate, representational form, and behavioral authority.
- `many-to-many-edge-state-is-where-files-yield-to-a-database.md` is now the main basis for storage investigations: files remain right for owner-local content, but churning dependency state on ownerless many-to-many edges practically wants a relational store.
- Distillation theory says shaped artifacts often suppress their own provenance, so dependency records must live where source changes can interrupt maintainers.
- Distillation is transformation into a new shape, not selection. A distillate is not a subset that can replace its source.
- No universal distillation preserves every future task-relevant distinction, so source material or pointers back to it must survive unless the downstream query family is known and narrow.
- Ad-hoc prompts and one-off source packets are also derivations when retained or reused: they frontload caller judgment before there is a stable type, schema, or skill.
- Some derived materials depend on source that should not be snapshotted into the KB. Code-grounded agent-memory-system reviews derive from external git repositories, often large ones, and preserve source identity through reviewed revisions, citations, and quote anchors instead.
- Merge-back workflows make canonical artifacts derivative at the update-event level. A note revised from a connect report or review remains the canonical note, but the edit depends on the previous note version, the generated report, the current KB/source context, and the operator's merge decision.
- Generated reports, reviews, connect reports, ingests, snapshots, and generated indexes all make different local decisions about what is tracked, ignored, regenerated, or promoted.

The moved rows from `kb/work/connect-maintenance-observations/` are opportunistic test cases. They are useful because they expose awkward lineage shapes, but the workshop is not primarily a cleanup queue.

## Working Hypothesis

Many Commonplace operations are already a three-surface pipeline:

1. gather or select source material;
2. generate a typed report over that material;
3. promote, commit, or act on selected report findings.

The type often owns the generated report's contract, while the skill or command owns execution, and the collection owns durable linking authority. A revised lineage model should make that split explicit instead of treating every artifact relation as an ordinary content link.

The automation target is not "commit every generated artifact." It is a controlled loop: generate automatically, keep intermediate reports out of git when they are cheap working context, preserve canonical lineage state where automation needs selectors and freshness, and merge selected findings back into durable artifacts with enough provenance to rerun or audit the update later.

The review system may be the prototype for the broader mechanism. Review prose remains markdown, but review lineage and freshness moved to SQLite because automation needed keyed current-state lookup, append-only acceptance events, and stale selectors over `note × gate × model` edge state. The extracted theory note names the structural reason: churning state on a many-to-many edge has no natural owner file. Further investigations should start from that predicate. Bare markdown plus JSON/YAML manifests may preserve evidence and history, but once the system needs automatic dependency maintenance over churning many-to-many edges, the practical query surface is a database or a database-equivalent generated index.

The source should not be replaced by the derivation by default. Derived artifacts are target-shaped, lossy, and often non-repeatable in the strong sense: a later agent may be able to produce another useful report, summary, cue, note, or skill from the same inputs, but not the same artifact with the same omissions, emphases, interpretation choices, and surrounding KB state. Losing a derivation usually means re-deriving. Losing the source means losing the material from which other future derivations could be made.

Not every derivation starts as a formal report. Ad-hoc distillation packages a task-local source bundle, current judgment, or one-off prompt into a consumable artifact before the KB has a stable type for that work. This is useful because it avoids premature schema changes, but if the artifact is retained, reused, or promoted, it needs lineage: which sources and judgments it packages, what validity window it assumes, and what future promotion would make it a durable note, instruction, report type, or skill.

`kb/agent-memory-systems/types/agent-memory-system-review.md` is a useful non-snapshot case. A code-grounded review is derived from an external git repository prepared as a local checkout, but the KB does not snapshot that repository. The source may be very large, and it is already versioned elsewhere. The durable review instead records source identity, reviewed revision, commit-pinned citations, and optional quote anchors so later readers can verify the derivation without treating the review as a replacement for the source repository.

There are exceptions. Mechanical derived copies with cheap deterministic checks can be regenerated or validated; generated complete indexes are the clear case. But most prose, report, review, and synthesis derivations sit in the judgmental regime. Their lineage mechanism should preserve sources, record dependencies, and make refresh/re-distillation possible rather than pretending the derived form is the new ground truth.

## Transferred Triage Items

These items were moved from `kb/work/connect-maintenance-observations/` because they exercise the mechanism. They are not the goal of the workshop by themselves.

| source item | lineage question |
|---|---|
| Claude dynamic-workflows docs and practitioner article | When do parallel source snapshots get direct `compares-with` links, and when should their relationship live only in a synthesis note or ingest prose? |
| `how-to-build-your-own-agent-harness...` | Does `kb/sources/COLLECTION.md` need source-to-note labels for contrast or parallel mechanism, distinct from `evidence` and `derived-from`? |
| `the-log-is-the-agent...` | How should near-duplicate ingests cross-reference each other, and when should the relationship produce a sovereignty/lock-in synthesis? |
| Text-optimization source | How should an external-cognition lineage be recorded when no note currently names the lineage, and how should future Meta-Harness snapshots cross-reference it? |
| Where-it-lives source | How should lineage direction be represented when an external paper appears downstream of internal KB vocabulary, making note-to-paper `derived-from` wrong? |

## Closure Conditions

Close this workshop when it produces one or more durable artifacts that settle the operational questions:

- a general lineage model for derived artifacts that distinguishes source material, generated reports, durable analysis, compiled views, canonical state, and promoted library artifacts;
- an investigation plan that uses `kb/notes/many-to-many-edge-state-is-where-files-yield-to-a-database.md` as the storage predicate for future automatic dependency-maintenance mechanisms;
- a revised source/linking policy, probably in `kb/sources/COLLECTION.md` and/or `kb/reference/link-vocabulary.md`;
- a report-lineage policy for generated reports, tracked report specs, ignored report instances, and promotion from reports into durable artifacts;
- explicit rules for which automatic derivations are saved in git, which are gitignored, which move to a state store, and which are only recorded as merge-back provenance;
- a decision on which future mechanisms cross the many-to-many/churning-edge threshold and therefore need a database-backed dependency-maintenance substrate;
- a decision on where "gather source -> generate typed report -> promote selected findings" belongs in the methodology, including the split between skill/command execution, type-owned report contract, collection-owned link authority, and promotion;
- a merge-back lineage model for cases where an automatic report over a note leads to revising that same note, making the new note version derivative from the old note version plus the report/source context without demoting the note from canonical status;
- mechanisms for updating derivative content: stale detection, regeneration, re-distillation, merge-back, retirement, and escalation when automatic verification is too weak;
- a source-preservation rule explaining when derived artifacts may replace, regenerate from, or only point back to their sources;
- a rule for external git-backed sources, especially code-grounded reviews where the KB should preserve revision-pinned verification handles instead of snapshotting a whole repository;
- an ad-hoc distillation rule for one-off prompts, source packets, and workshop artifacts that may later be reused, promoted, or extracted into skills;
- explicit handling for inverse or parallel lineage cases such as Where-it-lives and Meta-Harness/Text-optimization;
- updates or follow-up proposals for any transferred triage item that remains unresolved after the mechanism decision.

## Working Files

- [current-practices-and-theory.md](./current-practices-and-theory.md) - inventory of current mechanisms, existing theory, and open design tensions.
- [automatic-derivation-rules.md](./automatic-derivation-rules.md) - draft policy for git retention, merge-back lineage, and derivative refresh mechanisms.
- [review-lineage-storage-case.md](./review-lineage-storage-case.md) - review lineage case study and file-backed port options.
- [storage-weight-across-cases.md](./storage-weight-across-cases.md) - comparison of review and future automatic-dependency cases against the many-to-many edge-state database predicate.
