---
description: "Proposal: retain a packet-owned start-state capture for diffing and transition guards without threading captured text through operation methods"
type: kb/types/note.md
traits: [design-proposal]
tags: [kb-maintenance, evaluation]
---

# Packet-owned captures for guarded operation transitions

A long-running operation needs to detect when its live artifact has moved without claiming exclusive ownership of it indefinitely. The first full-improvement implementation asks other actors not to edit its note while the active pass runs. An asynchronous delete or merge recommendation may then wait for hours; edits during that pending period should remain possible. The first implementation needs only to refuse a report-driven transition when the current artifact no longer matches the operation's start state.

The smallest boundary that provides that behavior is operation-local: copy the live text into the output packet at operation start, record its hash beside the artifact's logical identity, and compare the live artifact with that capture immediately before a report-driven transition. Methods continue to read the logical path normally, so the first version adds a cooperative precondition: other actors must not edit guarded artifacts while the active pass runs. The final guard protects later application and asynchronous resolution; it is not in-flight isolation. This proposal does not introduce captured-input seams, a general artifact-version service, or a workspace lock.

## Current state (as of 2026-07-13)

The review system captures note and criterion text in `review_file_snapshots`, embeds that text in job prompts, and keys freshness baselines by logical paths. Those rows are review evidence, not operation-owned storage: successful baseline replacement prunes snapshots once no current baseline or review pair references them ([ADR 036](../adr/036-review-acceptance-is-current-state-not-append-only-history.md)). A full-pass packet therefore cannot depend on review snapshot retention for an asynchronous decision.

The full-improvement pass already records the initial note hash, but that hash cannot show a later operator what changed. Its methods ordinarily reopen the live path, so reports can describe different text if the note changes during the pass. No worked case yet shows that this inconsistency is costly enough to justify threading supplied content through review selection, applicability, snapshots, direct methods, and agent instructions.

The full-pass packet is already the natural retention unit. It lives under `kb/reports/full-pass/<note-name>/<pass-id>/`, remains while its findings or disposition are actionable, and is removed when they have been consumed. Keeping its start-state text beside its reports gives the capture the same owner and lifetime as the decision that needs it.

## The design

### Two components, never collapsed

Every captured input carries:

```text
logical identity:  kb/notes/example.md       # what the artifact IS
capture:           source.txt                # packet-owned text the operation READ
content hash:      <sha256 of capture UTF-8 bytes>
```

The logical identity continues to determine collection membership, type resolution, relative-link bases, output naming, method input, and stored keys. The capture supplies the start-state characters used by the guard and diff. **The capture path is never substituted for the logical identity or passed to an assessment method.** Doing so would select the report collection, break relative links, and store review state against the wrong path.

At operation start, the orchestrator reads the live artifact once, writes the resulting Unicode character sequence as UTF-8 to a non-Markdown file inside the packet, and records its SHA-256. The capture is immutable for the operation. A consumer verifies the hash whenever it loads the file; the report and capture are one retention unit.

A capture path is a normalized packet-relative `.txt` path. It must not be absolute, contain `..`, or resolve through a symlink or other indirection outside the packet; loading requires a regular file whose resolved path remains inside that packet. These constraints keep a report field from turning capture verification into an arbitrary filesystem read.

This duplication is deliberate rather than a second shared store. The packet copy is the operation's authoritative guard and diff basis, not an input transport or cache of review state. It requires no review-DB ownership rows, pruning exception, global capture catalogue, or new artifact type. Its `.txt` extension keeps KB link scans, artifact scans, and Markdown validators from treating it as an authored knowledge artifact.

An operation may guard several inputs. A merge recommendation captures both the source and proposed target because the recommendation is a claim about the pair. Each retains its own logical path, packet-relative capture path, and hash.

### Cooperative run isolation; guarded later transitions

The first implementation relies on an operating rule rather than a lock: from the source capture until the active pass finishes, no actor other than the orchestrator performing the prescribed transformation may edit the source. If a merge target is inspected and captured while finalizing a recommendation, the same rule applies to that target until the report is finalized. Do not start the pass when this cooperative ownership cannot be maintained.

After the active pass stops with a pending disposition, the live source and target return to being ordinary editable files. Manual edits, other agent edits, Git operations, and unrelated maintenance are allowed while the disposition waits; they make the old transition inapplicable when the guard runs.

Those mutations have different consequences:

- A change to an unrelated artifact has no effect.
- An edit during the active pass violates the operating precondition and may make later methods assess different text from earlier methods.
- A transition that consumes those reports — apply, delete, merge, reject, or record an alternative — must not begin unless every guarded live input still matches its capture.
- A mismatch preserves the live edit and follows the consumer's target-owned policy, such as resolving a full-pass disposition to `superseded`. The substrate never rebases, merges, or overwrites the edit.

The distinction is phase-based, not actor-based. During the active pass, both manual and agent edits by other actors are prohibited by convention. While a disposition is pending, both are allowed and both invalidate a transition derived from earlier characters.

### One guarded transition

Immediately before the first mutation, the consumer:

1. verifies each packet capture against its recorded hash;
2. reads each current logical path, returning `missing` when absent;
3. compares the current text hash with the capture hash;
4. returns every `matching`, `changed`, or `missing` comparison, including a capture-to-current diff for changed text; and
5. refuses to begin unless every input is `matching`.

Failure classes remain distinct. A capture that does not match its recorded hash is a corrupted packet: the consumer stops and routes it to reconciliation, never to `superseded`. A readable live input whose hash differs from the verified capture is version drift and follows the consumer's target-owned mismatch policy. A missing live input also routes to reconciliation because absence cannot prove which transition, if any, occurred.

After mutation, the consumer verifies its own postconditions and routes incomplete or ambiguous state to reconciliation. A missing artifact never proves that deletion or merge succeeded.

This guard may be a small consumer-local helper or explicit workflow step. No shared module is required for the first consumer. The freshness workshop may extract the hash, comparison, and guard boundary after a second consumer proves which parts are genuinely reusable.

The guard is optimistic, not transactional. A write racing between the final comparison and mutation remains possible. Commonplace accepts that small residual window instead of adding filesystem locks or compare-and-set machinery; postcondition verification catches incomplete or unexpected results but cannot prove that no race occurred.

## Option space and settled defaults

- **Capture versus pinned input.** A capture used only for comparison and diffing adds one packet file and no method-facing API. Pinning every method to it would make the pass internally consistent across concurrent edits, but requires content overrides through review selection, applicability, snapshot creation, direct methods, and agent instructions. The settled default is capture without pinning plus a documented no-edit precondition for the active pass. Revisit pinning only after that operating rule proves materially restrictive or unreliable.
- **Locking versus guarded application.** A repository or artifact lock would reduce concurrency only for cooperating writers; editors, Git, and direct filesystem writes need not honor it. The settled default is no lock: a cooperative no-edit rule covers the active pass, and guards protect later report-driven transitions from net drift.
- **Packet capture versus review-DB snapshot.** Review snapshots already contain suitable text but have evidence-owned pruning semantics. The settled default is a packet-owned `.txt` capture whose lifetime matches the operation. This adds one checked file rather than changing review storage ownership.
- **Automatic rebase versus supersession.** Applying an editorial packet to a changed note requires semantic three-way reconciliation, not a version check. The settled default is to preserve the live edit and supersede the old operation. A new pass may assess the new text.
- **Shared API now versus later.** One full-pass workflow does not justify a general artifact-version subsystem. The initial implementation adds only packet capture plus an explicit comparison-and-guard workflow. Extraction belongs to the freshness workshop when it has a second worked consumer.
- **Capture scope.** Consumers declare their guarded input set. A full pass captures the source note and, only if proposed, its merge target. Collection contracts, prompt scaffolding, and other system-definition dependencies remain under their own version or freshness policies.

## Forces and risks

- **The identity/capture invariant is easy to violate.** Passing `source.txt` where `kb/notes/example.md` was expected produces plausible but wrongly routed output. The capture is only a guard/diff basis; methods keep receiving the logical path.
- **Packet cleanup becomes load-bearing.** Deleting a pending packet deletes the authoritative start-state text and its diff basis. Cleanup must retain the whole packet while a disposition or rejection remains actionable.
- **The capture is a second copy of the text.** Its hash check makes disagreement detectable, and operation ownership gives the copy a bounded lifetime. An unchecked or independently retained copy would not be acceptable.
- **The no-edit rule is cooperative.** Methods reopen the live artifact, so an actor that violates the rule can make a completed packet combine findings over different versions. If the live text remains changed, the guard supersedes the work; an edit followed by an exact revert is not detectable. The first implementation accepts this low-concurrency limitation instead of paying for pinned-input seams or locking.
- **The optimistic guard is not a transaction.** The small check-to-mutation race remains explicit residual risk.
- **Code proportionality still matters.** A packet file and an explicit compare-and-guard step are sufficient. Captured-input overrides, a capture registry, lock manager, general resolver, or freshness policy engine would outgrow the worked case.

## Adoption criteria

Adopt only with the full-improvement pass as an end-to-end worked case:

1. The pass writes one immutable UTF-8 `.txt` capture for the source note's start state, records its logical path and SHA-256 separately, and rejects a capture whose hash does not match. Every capture path is normalized, packet-relative, confined to the packet, and resolves to a regular non-symlink file.
2. The operative instruction tells other actors not to edit the source while the active pass runs, and applies the same rule to a proposed merge target from capture through report finalization.
3. Assessment methods continue to receive the logical path and may read the live artifact; the implementation adds no capture-path or text-override seam to review or direct methods.
4. Before applying a `keep` packet, executing a delete or merge, rejecting a recommendation, or recording an alternative operation, one guard checks the complete input set, returns every `matching`, `changed`, or `missing` result, and refuses the transition unless all match.
5. A merge recommendation owns and guards a separate capture for its target; source-only guarding is insufficient.
6. Changed inputs produce a capture-to-current diff and follow the consumer's mismatch policy. Missing inputs and corrupted captures route to reconciliation rather than implying success or supersession.
7. A successful transition verifies target-owned postconditions; incomplete or ambiguous results route to explicit reconciliation.
8. Packet cleanup retains reports and captures as one unit while the operation remains actionable and may remove them together afterward.

The implementation adds **no review-DB schema or retention change, no general capture store, no repository lock, no automatic rebase, and no shared artifact-version module** for this first consumer. If the worked case requires any of those, revisit the boundary rather than hiding the added system behind a small API.

When a second consumer arrives, the freshness workshop first extracts the proven capture/comparison/guard boundary, then evaluates general dependency baselines and reverse selection. Pinned method input is not part of that proven boundary. The full-pass packet remains one consumer-owned persistence policy, not the universal storage design.

---

Relevant Notes:

- [Report-owned resolution for asynchronous full-pass dispositions](./report-owned-resolution-for-asynchronous-full-pass-dispositions.md) — part-of: owns the first consumer's disposition lifecycle and its `superseded` response to a changed input
- [Review system](../README-REVIEW-SYSTEM.md) — part-of: owns review evidence snapshots and freshness baselines, which remain separate from packet capture retention
- [ADR 036: review acceptance is current state](../adr/036-review-acceptance-is-current-state-not-append-only-history.md) — see-also: explains why review-owned snapshot pruning cannot provide packet retention
- [Full improvement pass closure](../full-improvement-pass-closure.md) — see-also: the multi-method workflow whose long execution window motivates captured input
- [A derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — rationale: why every packet capture is verified against its recorded hash
