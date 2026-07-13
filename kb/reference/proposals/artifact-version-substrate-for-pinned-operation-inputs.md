---
description: "Proposal: let long-running operations assess one packet-owned text capture while live artifacts remain editable, and block only transitions based on stale inputs"
type: kb/types/note.md
traits: [design-proposal]
tags: [kb-maintenance, evaluation]
---

# Artifact-version substrate for pinned operation inputs

A long-running operation needs a stable input without claiming exclusive ownership of the live artifact. A full-improvement pass may take long enough that a maintainer edits its note before the pass finishes; an asynchronous delete or merge recommendation may be resolved hours later. Those edits should remain possible. What must be prohibited is applying an old recommendation to characters nobody assessed.

The smallest boundary that provides that behavior is operation-local: retain the exact text the operation read inside its output packet, keep the artifact's logical identity separate, and compare the live artifact with the retained capture immediately before any report-driven transition. Concurrent edits are allowed; they make the transition inapplicable rather than corrupting the assessment. This proposal does not introduce a general artifact-version service or lock the workspace.

## Current state (as of 2026-07-13)

The review system already captures note and criterion text in `review_file_snapshots`, embeds that captured text in job prompts, and keys freshness baselines by logical paths. Those rows are review evidence, not operation-owned storage: successful baseline replacement prunes snapshots once no current baseline or review pair references them ([ADR 036](../adr/036-review-acceptance-is-current-state-not-append-only-history.md)). A full-pass packet therefore cannot depend on review snapshot retention for an asynchronous decision.

Outside review, input handling is inconsistent. The compression worker can receive note text alongside its path; composition friction and `cp-skill-connect` ordinarily reopen the live path. The full-improvement pass runs several method families over what it calls "the note" without retaining one operation-owned version, so reports can describe different text if the note changes during the pass.

The full-pass packet is already the natural retention unit. It lives under `kb/reports/full-pass/<note-name>/<pass-id>/`, remains while its findings or disposition are actionable, and is removed when they have been consumed. Keeping its assessed text beside its reports gives the capture the same owner and lifetime as the decision that needs it.

## The design

### Two components, never collapsed

Every captured input carries:

```text
logical identity:  kb/notes/example.md       # what the artifact IS
capture:           source.txt                # packet-owned text the operation READ
content hash:      <sha256 of capture UTF-8 bytes>
```

The logical identity determines collection membership, type resolution, relative-link bases, output naming, and stored keys. The capture supplies the characters every method assesses. **The capture path is never substituted for the logical identity.** Doing so would select the report collection, break relative links, and store review state against the wrong path.

At operation start, the orchestrator reads the live artifact once, writes the resulting Unicode character sequence as UTF-8 to a non-Markdown file inside the packet, and records its SHA-256. The capture is immutable for the operation. A consumer verifies the hash whenever it loads the file; the report and capture are one retention unit.

This duplication is deliberate rather than a second shared store. The packet copy is the operation's authoritative input, not a cache of review state. It requires no review-DB ownership rows, pruning exception, global capture catalogue, or new artifact type. Its `.txt` extension keeps KB link scans, artifact scans, and Markdown validators from treating it as an authored knowledge artifact.

An operation may pin several inputs. A merge recommendation captures both the assessed source and proposed target because the recommendation is a claim about the pair. Each retains its own logical path, packet-relative capture path, and hash.

### Manual edits are allowed; stale transitions are not

The live source and target remain ordinary editable files while the operation runs and while a disposition is pending. Manual edits, other agent edits, Git operations, and unrelated maintenance are not blocked by a lock owned by this design.

Those mutations have different consequences:

- A change to an unrelated artifact has no effect.
- A change to a captured input does not alter reports already running against the capture.
- A transition that consumes those reports — apply, delete, merge, reject, or record an alternative — must not begin unless every guarded live input still matches its capture.
- A mismatch preserves the live edit and follows the consumer's target-owned policy, such as resolving a full-pass disposition to `superseded`. The substrate never rebases, merges, or overwrites the edit.

The distinction is relational, not actor-based. A manual edit is not intrinsically safer than an agent edit; both are allowed, and both invalidate a transition derived from earlier characters.

### Narrow input seams

Every method consumes captured text while retaining the original logical path:

- **Review jobs** accept the captured note text keyed by its logical path. Applicability, reviewed snapshots, prompt rendering, and the resulting freshness baseline all derive from that supplied text. The review DB may store the same text for evidence, but the packet does not rely on that row for retention.
- **Direct methods** receive the logical path plus captured text and perform no live artifact read. Compression already uses this shape; composition friction adopts it.
- **Connection discovery** derives collection rules and relative-link bases from the logical identity, and derives the claim and outbound links from captured text. Its report names the logical identity.
- **Synthesis** reads retained method reports and captures. It never reopens the live artifact to reconstruct what the methods assessed.

These are consumer-facing seams, not a general content-resolver abstraction. If a review command needs a capture-path or text-override option to reach its existing preparation boundary, that option is scoped to job creation. The design does not widen freshness keys or teach the review DB about full-pass ownership.

### One guarded transition

Immediately before the first mutation, the consumer:

1. verifies each packet capture against its recorded hash;
2. reads each current logical path, returning `missing` when absent;
3. compares the current text hash with the capture hash;
4. returns every `matching`, `changed`, or `missing` comparison, including a capture-to-current diff for changed text; and
5. refuses to begin unless every input is `matching`.

After mutation, the consumer verifies its own postconditions and routes incomplete or ambiguous state to reconciliation. A missing artifact never proves that deletion or merge succeeded.

This guard may be a small consumer-local helper or explicit workflow step. No shared module is required for the first consumer. The freshness workshop may extract the hash, comparison, and guard boundary after a second consumer proves which parts are genuinely reusable.

The guard is optimistic, not transactional. A write racing between the final comparison and mutation remains possible. Commonplace accepts that small residual window instead of adding filesystem locks or compare-and-set machinery; postcondition verification catches incomplete or unexpected results but cannot prove that no race occurred.

## Option space and settled defaults

- **Locking versus guarded application.** A repository or artifact lock would reduce concurrency only for cooperating writers; editors, Git, and direct filesystem writes need not honor it. It would also forbid the manual editing this workflow should tolerate. The settled default is no lock: captures isolate assessment, and guards protect report-driven transitions.
- **Packet capture versus review-DB snapshot.** Review snapshots already contain suitable text but have evidence-owned pruning semantics. The settled default is a packet-owned `.txt` capture whose lifetime matches the operation. This adds one checked file rather than changing review storage ownership.
- **Automatic rebase versus supersession.** Applying an editorial packet to a changed note requires semantic three-way reconciliation, not a version check. The settled default is to preserve the live edit and supersede the old operation. A new pass may assess the new text.
- **Shared API now versus later.** One full-pass workflow does not justify a general artifact-version subsystem. The initial implementation adds only its input seams, capture loading, comparison, and guard. Extraction belongs to the freshness workshop when it has a second worked consumer.
- **Capture scope.** Consumers declare their guarded input set. A full pass captures the assessed note and, only if proposed, its merge target. Collection contracts, prompt scaffolding, and other system-definition dependencies remain under their own version or freshness policies.

## Forces and risks

- **The identity/capture invariant is easy to violate.** Passing `source.txt` where `kb/notes/example.md` was expected produces plausible but wrongly routed output. APIs should name the two values distinctly.
- **Packet cleanup becomes load-bearing.** Deleting a pending packet deletes the authoritative assessed text and its diff basis. Cleanup must retain the whole packet while a disposition or rejection remains actionable.
- **The capture is a second copy of the text.** Its hash check makes disagreement detectable, and operation ownership gives the copy a bounded lifetime. An unchecked or independently retained copy would not be acceptable.
- **Concurrent edits cause wasted work.** They are preserved, but a completed packet may become unappliable. That is the accepted cost of allowing edits without implementing semantic rebasing.
- **The optimistic guard is not a transaction.** The small check-to-mutation race remains explicit residual risk.
- **Code proportionality still matters.** A packet file, narrow content seams, one comparison result, and one guard are sufficient. A capture registry, lock manager, general resolver, or freshness policy engine would outgrow the worked case.

## Adoption criteria

Adopt only with the full-improvement pass as an end-to-end worked case:

1. The pass writes one immutable UTF-8 `.txt` capture for the assessed note, records its logical path and SHA-256 separately, and rejects a capture whose hash does not match.
2. Every method consumes that capture while collection rules, type context, relative links, output naming, and review keys continue to derive from the logical path.
3. Review applicability, prompts, reviewed snapshots, and freshness baselines derive from supplied captured text without an intervening live-note read.
4. A manual edit after capture does not change what any method assesses and is never overwritten or automatically merged.
5. Before applying a `keep` packet or resolving a delete or merge, one guard checks the complete input set, returns every `matching`, `changed`, or `missing` result, and refuses the transition unless all match.
6. A merge recommendation owns and guards a separate capture for its target; source-only guarding is insufficient.
7. Changed inputs produce a capture-to-current diff. Missing inputs route to reconciliation rather than implying success.
8. A successful transition verifies target-owned postconditions; incomplete or ambiguous results route to explicit reconciliation.
9. Packet cleanup retains reports and captures as one unit while the operation remains actionable and may remove them together afterward.

The implementation adds **no review-DB schema or retention change, no general capture store, no repository lock, no automatic rebase, and no shared artifact-version module** for this first consumer. If the worked case requires any of those, revisit the boundary rather than hiding the added system behind a small API.

When a second consumer arrives, the freshness workshop first extracts the proven capture/comparison/guard boundary, then evaluates general dependency baselines and reverse selection. The full-pass packet remains one consumer-owned persistence policy, not the universal storage design.

---

Relevant Notes:

- [Report-owned resolution for asynchronous full-pass dispositions](./report-owned-resolution-for-asynchronous-full-pass-dispositions.md) — part-of: owns the first consumer's disposition lifecycle and its `superseded` response to a changed input
- [Review system](../README-REVIEW-SYSTEM.md) — part-of: owns review evidence snapshots and freshness baselines, which remain separate from packet capture retention
- [ADR 036: review acceptance is current state](../adr/036-review-acceptance-is-current-state-not-append-only-history.md) — see-also: explains why review-owned snapshot pruning cannot provide packet retention
- [Full improvement pass closure](../full-improvement-pass-closure.md) — see-also: the multi-method workflow whose long execution window motivates captured input
- [A derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — rationale: why every packet capture is verified against its recorded hash
