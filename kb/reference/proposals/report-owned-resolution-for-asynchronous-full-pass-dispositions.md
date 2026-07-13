---
description: "Proposal: keep asynchronous full-pass dispositions and their human resolutions in structured reports without mutating reviewed notes or widening the review DB"
type: kb/types/note.md
traits: [design-proposal]
tags: [evaluation, kb-maintenance]
---

# Report-owned resolution for asynchronous full-pass dispositions

A full improvement pass can conclude that a note should be deleted or merged without having authority to perform that operation immediately. The recommendation therefore needs an asynchronous handoff. Writing the handoff into the reviewed note makes an operational recommendation look like note content: it invalidates review freshness, enters the link graph, changes link-health results, can preserve an invalid [`user-verified` attestation](../adr/044-user-verification-replaces-global-note-status.md), and contaminates a later pass that reads the marker as prose.

This proposal keeps the handoff in `kb/reports/`, where the review workflow already writes its generated output. The full-pass report becomes the authoritative record of both the proposed disposition and its later resolution. The note remains byte-identical until somebody accepts an operation that actually changes or removes it.

It assumes, and does not respecify, the [packet-owned capture proposal](./packet-owned-captures-for-guarded-operation-transitions.md): capture of an operation's start state, comparison of that capture against current state, and a guard that refuses a report-driven transition when they differ. This proposal is that design's first consumer and supplies one target-owned response to a changed input — `superseded`. Where the two overlap, the capture proposal is authoritative on capture, comparison, and guarding; this one is authoritative on what a disposition means and who resolves it.

## Current state (as of 2026-07-13)

The operative [full-improvement-pass instruction](../../instructions/run-full-improvement-pass-on-note.md) runs critique and semantic review against the initial note and records a note-level `keep`, `delete`, or `merge` Disposition in its packet. Its interim containment behavior now leaves the note byte-identical for a non-`keep` result, returns the packet path, and skips the edit and closing cycle. It does not yet provide durable discovery, re-entrancy, or resolution state.

Before that containment fix, the short circuit conflicted with the shipped [full-improvement-pass closure](../full-improvement-pass-closure.md): a `TODO(full-pass)` marker changed final note bytes after the initial freshness baselines were written, but no closing review re-pinned them. Semantic gates watch body content, and critique effectively watches the whole note, so trivial-change acknowledgement could not carry the initial evidence across the insertion.

The removed marker had no lifecycle consumer: no selector, validator, sweep, or fix instruction found it, and a repeated pass could insert another marker. Its merge-target link was also parsed as a real graph edge and checked for link health even though it represented a proposed maintenance operation rather than a knowledge relationship. Removing the marker stops those defects immediately; it does not make the retained packet discoverable or resolved, which is the remaining problem this proposal addresses.

Full-pass packets already live under `kb/reports/full-pass/<note-name>/<pass-id>/`. They are gitignored inspection artifacts retained while their findings remain in use. The review database separately stores snapshot-anchored `(note, criterion, model partition)` evidence and freshness baselines; it has no full-pass run, note-level disposition, or human-resolution entity. Although an initial assay may leave a matching note snapshot in that database, the packet neither names nor owns it, so the asynchronous handoff can currently detect a hash mismatch but cannot independently show what changed.

## Proposed design

### The report is the authority

Give full-pass reports a report type with machine-readable frontmatter. The type-spec path is `kb/reports/types/full-pass-report.md`, and its minimum state is:

```yaml
type: kb/reports/types/full-pass-report.md
source: kb/notes/example.md
source_capture: source.txt
source_sha256: <sha256 of the source start-state capture>
pass_id: <pass-id>
disposition: keep | delete | merge
merge_target: null | kb/notes/target.md
merge_target_capture: null | merge-target.txt
merge_target_title: null | <title from the captured merge target>
merge_target_sha256: null | <sha256 of the proposed merge target>
resolution: not-required | pending | accepted | rejected | alternative-applied | superseded
resolved_at: null | <timestamp>
resolution_authority: null | user | version-guard
resolution_summary: null | <what happened>
resolution_rationale: null | <why>
resulting_paths: []
```

The type spec is a tracked [system-definition artifact](../../notes/definitions/system-definition-artifact.md), not generated full-pass output. It follows the shipped `kb/reports/types/connect-report.md` precedent catalogued in [available types](../available-types.md): report-type contracts and schemas live under `kb/reports/types/`, while ignore and replacement semantics apply to generated per-kind instances such as `kb/reports/full-pass/*`. The full-pass type's novel human state changes the retention rules for its instances; it does not require moving the contract away from the established report-type surface.

`source` and `merge_target` are repository-relative logical identifiers. They are code-valued fields, not Markdown links, so they do not assert graph relationships. `source_capture` and `merge_target_capture` are normalized packet-relative `.txt` paths: never absolute, never containing `..`, and required to resolve to regular non-symlink files inside the packet. Each capture is the authoritative guard and diff basis for this pass, immutable, and verified against its recorded SHA-256 whenever loaded. The report and its captures are one retention unit; review snapshot retention is irrelevant to their lifetime.

A merge disposition requires `merge_target`, `merge_target_capture`, `merge_target_title`, and `merge_target_sha256`; other dispositions require all four to be null. Step 7 treats a synthesized merge as provisional: the orchestrator captures the target's current text and finalizes the recommendation only after confirming the rationale against that target under the active pass's cooperative no-edit rule. `merge_target_title` records the captured target's H1 so the recommendation reads standalone once the packet outlives its method reports. The report body records the source finding, standalone rationale, what a replacement would need, and any unresolved routed attention that must survive loss of those reports.

The orchestrator writes `source_capture` before running the pass and treats it as the pass's guard and diff basis. Assessment methods continue to read the logical source normally; they do not receive the capture as an input override. The orchestrator does not reconstruct the capture later from the then-current note or depend on a review snapshot with the same path and hash. Report resolution may mutate the report's state; a capture, once written, is never rewritten.

### What this workflow guards

The capture, comparison, diff, and guard mechanics are the [packet-owned capture proposal](./packet-owned-captures-for-guarded-operation-transitions.md)'s. A capture path is never substituted for the logical path or passed to an assessment method. This proposal fixes which artifacts a full pass guards and what a failed guard means.

A pass may guard two artifacts, both under their unchanged logical identities:

- **The source note** (`source` / `source_capture` / `source_sha256`). The orchestrator captures its start state. Every method continues to receive `source` and may reopen the live note, so collection rules, type context, relative-link bases, report naming, and review keys need no new input seam.
- **The merge target, when one is proposed** (`merge_target` / `merge_target_capture` / `merge_target_sha256` / `merge_target_title`). Step 7 treats a synthesized merge as provisional: the orchestrator captures the target's then-current text before finalizing the recommendation. The capture supplies the later diff and target-side guard; methods continue to use the logical target path.

Guarding both is what makes an asynchronous merge recommendation checkable later: a recommendation is a claim about a *pair* of artifacts, so a guard over the source alone would let the target drift out from under it unnoticed.

The active pass has a cooperative precondition: other actors do not edit the source from capture until the pass finishes, or the proposed merge target from its capture until report finalization. This substitutes for pinned method inputs in the first version. After a `delete` or `merge` packet becomes pending, ordinary edits are allowed again. Before applying a `keep` packet, step 8 must compare the live note to `source_sha256` and abort without editing if they differ. Before resolving a `delete`, the asynchronous consumer performs the same comparison. Before resolving a `merge`, it compares both the source and target to their recorded hashes. Rejection and `alternative-applied` resolution use that same complete-input guard before recording or beginning the decision. A changed readable input follows the supersession rules below; a missing or relocated input routes to reconciliation and is not permission to find a substitute implicitly.

A `keep` packet starts with `resolution: not-required` and follows the existing edit, flow, and closing-review path. A `delete` or `merge` packet starts with `resolution: pending`, leaves the note unchanged, skips the edit and closing cycle because the workflow produced no note transformation, and hands back the report path.

The report, not a second queue file or database row, is ground truth. A generated listing may project pending reports for convenience only if it is recomputed or validated against them. The initial persistence boundary is deliberately local: packets remain gitignored and support asynchronous resolution across sessions in one working copy, but do not claim to carry decisions across cleanup, clones, or machines.

### Resolution state

The resolution section in the report body gives the human-readable decision record:

```markdown
## Resolution

**Status:** pending
**Resolved at:** —
**Authority:** —
**Outcome:** —
**Rationale:** —
**Resulting paths:** —
```

Structured frontmatter is canonical. Resolving a disposition updates its fields first and deterministically renders this section from them; validation rejects disagreement between the two representations. `not-required` and `pending` require null resolution metadata and empty `resulting_paths`. Every terminal resolution requires `resolved_at`, `resolution_authority`, `resolution_summary`, and `resolution_rationale`; its `resulting_paths` records every artifact left by the operation. `accepted`, `rejected`, and `alternative-applied` require explicit user authority. `superseded` uses `version-guard` authority when a deterministic source or target precondition fails.

| Resolution | Meaning |
|---|---|
| `accepted` | The source was deleted or merged into the proposed target. |
| `rejected` | The note stays; the record states why the proposed operation was declined. |
| `alternative-applied` | A different operation resolved the concern, such as merging the proposed target into the source. |
| `superseded` | A guarded input changed, so the recommendation no longer applies without reassessment. |

The actor first verifies each packet capture against its recorded hash, then compares `source_sha256` with the live source and, for a merge, `merge_target_sha256` with the live target. Capture verification failure means the packet is corrupted: stop and reconcile without changing its resolution to `superseded`. A changed readable live input is explained with a diff from the corresponding packet capture; it does not silently reject or accept the recommendation. The actor resolves that drift as `superseded` or starts a new pass. An accepted operation is recorded only after the filesystem change succeeds and its resulting paths are verified. If a pending report names a source that is already absent, the consumer must ask for reconciliation rather than infer acceptance; deletion, relocation, and partial merge failure are observationally ambiguous. The retained capture may show the removed content, but it cannot prove whether deletion, relocation, or a partial merge was intended. The same reconciliation rule applies when a merge target is absent or has moved.

Rejection is a human judgment over one recommendation against its guarded inputs: the assessed-note capture and, for a merge, the target capture. A later pass over the same text may run when explicitly requested, but its synthesis must load the prior rejection and may not repeat the same disposition without materially new evidence. Review workers do not receive the prior resolution, since it would bias the independent assays; only the orchestrator sees it during reconciliation. A changed guarded-input hash removes that constraint while retaining the earlier decision as history.

### Discovery and re-entrancy

The asynchronous consumer locates work by parsing full-pass reports and selecting `resolution: pending`; it does not scan note bodies. Its minimum operations are list, inspect, and resolve. The initial consumer is an instruction-driven workflow; a command is deferred until volume, concurrency, or exact transition enforcement demonstrates the need.

Before starting a new full pass, the orchestrator checks report state for the target:

- A pending disposition whose guarded inputs still match stops the new pass and returns the existing report. If any guarded input differs or is absent, the consumer surfaces the old report for supersession before a new pass proceeds.
- A rejected disposition over the same guarded inputs is supplied to step 7 reconciliation, not to the reviewers.
- A superseded or resolved disposition does not block a new pass.
- At most one pending disposition may exist for a logical source path.

These rules prevent stacked recommendations and prevent the recommendation's rationale from becoming assay input.

### Review-system consequences

The review database remains authoritative only for assay evidence and freshness. Full-pass resolution does not add a review result kind, freshness-baseline event, acknowledgement, or disposition table: compression, composition friction, connection discovery, synthesis, and the human decision all lie outside a `(note, criterion)` pair.

Each resolution has ordinary review consequences:

- **Pending:** critique and semantic baselines follow their ordinary review snapshots independently of the packet's start-state capture. A source mismatch supersedes the recommendation rather than acknowledging the change; a source match does not assert that every method read the capture.
- **Rejected:** user rejection may be recorded only after the source still matches `source_sha256`, so its baselines are fresh at resolution. Later source edits stale them through the ordinary whole-file comparison. For a proposed merge, target drift also prevents recording a rejection against a recommendation whose inputs no longer match.
- **Accepted deletion:** selectors no longer enumerate the absent source. Its old review rows and snapshots follow ordinary review pruning. The packet owns the start-state text needed for its resolution record, so review cleanup has no full-pass retention obligation.
- **Accepted merge:** source reviews do not transfer to the target. The target's substantive edit removes any `user-verified` attestation and stales its existing review pairs through the normal whole-file hash comparison.
- **Alternative applied:** each surviving edited artifact follows its normal validation, verification, and review-freshness rules. A reverse merge is not evidence that the original source remained unchanged.

Executing merge contents remains a human- or agent-owned editing operation. `commonplace-relocate-note` cannot substitute for it: relocation moves a file and rewrites backlinks but does not reconcile two artifacts' claims or prose.

## Option space, settled defaults, and promotion thresholds

- **Report versus review DB authority.** Report authority keeps the complete basis and human resolution together and preserves the review DB's factored-pair semantics. The proposed state has one natural owner—the pass report—rather than the churning ownerless many-to-many edge for which [files yield to a database](../../notes/many-to-many-edge-state-is-where-files-yield-to-a-database.md). But [ADR 010](../adr/010-review-state-should-move-to-sqlite-once-reviews-leave-git-and.md) is a real counterprecedent: it moved review state after gitignored files accumulated structured metadata, current-state queries, and acknowledgement transitions, all of which this proposal could recreate at smaller scale. Report ownership is justified only while scans stay small and the human-readable packet remains the operation's primary object; if indexed transitions become the primary use, the ADR 010 threshold has been crossed. DB authority would then make pending queries direct but would still need a report for methods the DB does not execute and for the rationale. Mirroring both creates a [derived copy that must be checked](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md); this proposal avoids the mirror.
- **Packet frontmatter versus a resolution sidecar.** Frontmatter gives one authoritative artifact and cheap parsing. A sidecar preserves the generated packet byte-for-byte but creates a join and a second file whose identity and cleanup must remain synchronized. The settled default is canonical packet frontmatter plus a deterministically rendered body resolution section.
- **Global versus report-local type spec.** The settled default is `kb/reports/types/full-pass-report.md`, matching the tracked connect-report type and schema. `kb/reports/types/` is a contract surface, not one of the ignored per-kind output directories. The fact that full-pass instances acquire non-regenerable human resolution state is handled by instance retention and validation; it does not by itself justify diverging from the only shipped report-type precedent. A global type would become warranted only if the same contract were shared by artifacts outside the reports subsystem.
- **Where captured text lives.** Delegated to the [packet-owned capture proposal](./packet-owned-captures-for-guarded-operation-transitions.md), whose settled default gives the packet an authoritative `.txt` guard/diff basis for each guarded input. The report records each packet-relative capture path and hash. This duplicates text already present in some review snapshots, but avoids changing review-DB ownership and makes the packet independently inspectable and diffable. Capture hash verification and packet-level retention are the bounded price.
- **Instruction versus command consumer.** The settled initial default is an instruction that lists and resolves the small number of reports without new runtime machinery. A deterministic command becomes warranted when exact transition validation, concurrent actors, or report volume makes prose orchestration unreliable.
- **Local versus portable persistence.** The settled initial default keeps complete full-pass packets gitignored, matching the local review DB and supporting asynchronous work across sessions in one working copy. It does not preserve human rejection across cleanup, clones, or machines. Portable decisions could later unignore resolution-bearing packets or commit a compact resolution report, but that would change the current rule that reports are replaceable generated snapshots.
- **Resolution authority.** The settled default requires explicit user authority for accepting, rejecting, or applying an alternative disposition. Agents may deterministically mark a report superseded when its version guard fails, but may not infer a substantive human decision from filesystem state.
- **Resolved-report retention.** Pending reports must never be pruned. Rejected and alternative resolutions remain load-bearing while all guarded-input hashes are current. Accepted delete/merge reports may be retained for audit or pruned after Git history durably records the operation. No cleanup command may touch full-pass reports until it has an explicit resolution-aware retention policy.

## Forces and risks

- **Generated output acquires human state.** A resolution cannot be regenerated from the KB. This is a deliberate exception to [ADR 007's](../adr/007-reports-directory-for-generated-snapshots.md) stateless-snapshot model and must be documented if adopted.
- **Capture dependency.** A hash alone cannot reconstruct a diff or preserve the basis of an asynchronous recommendation. The packet-owned capture supplies those needs without changing review-job or direct-method input paths.
- **Cooperative active-pass ownership.** Methods may disagree about what they assessed if another actor edits the live note despite the no-edit rule. Net drift at the pre-application guard is a hard stop and preserves the live edit, but an exact edit-then-revert can escape detection. Evidence that the convention is unreliable would justify revisiting pinned inputs.
- **Two representations inside one report.** Structured frontmatter supports scripts while the body supports review. The body renders from the canonical structured fields, and type-level validation rejects disagreement.
- **Crash consistency.** Report mutation and delete/merge edits are not one filesystem transaction. Verification and explicit reconciliation are required; absence of the source is not enough to infer success.
- **Repeated rejection.** A rejection should constrain identical future synthesis without permanently immunizing the note from new evidence. Hash anchoring and orchestrator-only loading provide that boundary.
- **Local data loss.** A gitignored human resolution can disappear even though it is no longer regenerable. This is an accepted limit of the initial same-working-copy asynchronous boundary and the main reason to revisit portable persistence if cross-machine continuity becomes a requirement.
- **No automatic merge semantics.** Recording a merge recommendation does not define how claims, backlinks, verification, or conflicting prose are reconciled. Automating that operation is separate work.

## Adoption criteria

Adopt this design only with an end-to-end case covering each non-`keep` resolution:

1. A pending delete or merge leaves the source note byte-identical. Its packet retains and hash-verifies the start-state text used by the version guard and later diff.
2. The operative instruction prohibits other actors from editing the source during the active pass and applies the same rule to a proposed merge target from capture through report finalization.
3. Assessment methods continue to use their existing logical-path inputs; implementing this proposal adds no captured-content seam to review selection, job creation, direct methods, or agent instructions.
4. The pending selector finds the report without reading note bodies or treating target paths as graph edges.
5. A repeated pass over the same guarded inputs returns the pending report rather than running new assays.
6. A live-source mismatch prevents automatic application of a `keep` packet, execution of an old delete/merge recommendation, rejection, and alternative application; a live-target mismatch prevents the same transitions for a merge recommendation. The consumer preserves the live edit and can show each mismatch against the corresponding packet capture.
7. Accepted delete and accepted merge record resolution and verify resulting paths; merge edits stale only the surviving target's relevant reviews.
8. Rejection requires matching guarded inputs, keeps the note unchanged, records user authority and a rationale, and prevents unsupported repetition of the same recommendation during later synthesis. An opposite-direction merge or other alternative also requires matching guarded inputs before mutation and can be recorded as `alternative-applied` only after its postconditions succeed.
9. The report resolves `type: kb/reports/types/full-pass-report.md`; ignore rules and report cleanup preserve `kb/reports/types/` while applying resolution-aware retention only to instances under `kb/reports/full-pass/`.
10. Validation rejects incomplete or inconsistent capture and merge-target fields; an absolute, escaping, or non-regular capture path; a missing capture; a capture whose content does not match its recorded hash; incomplete terminal-resolution metadata; invalid resolution authority; and disagreement between structured report state and the rendered Resolution section.
11. Report cleanup cannot silently delete pending or still-load-bearing rejected resolutions or their packet-owned captures.
12. The local persistence boundary covers the packet and its captures as one retention unit and is tested across sessions in one working copy.

If these cases require the review DB to understand full-pass synthesis or human editorial authority, revisit the boundary rather than adding a partial mirror. If report scanning proves too fragile or slow at demonstrated scale, promote the consumer to a deterministic command before adding a database index.

---

Relevant Notes:

- [Packet-owned captures for guarded operation transitions](./packet-owned-captures-for-guarded-operation-transitions.md) — part-of: supplies the capture, comparison, diff, and guard contract this design consumes
- [Full improvement pass closure](../full-improvement-pass-closure.md) — part-of: defines why transformed final note bytes require closing evidence and why an unchanged pending note does not
- [Review system](../README-REVIEW-SYSTEM.md) — part-of: owns snapshot-anchored assay evidence and freshness, which this proposal keeps separate from disposition resolution
- [ADR 007: reports directory for generated snapshots](../adr/007-reports-directory-for-generated-snapshots.md) — see-also: current report lifecycle that resolution-bearing packets would deliberately qualify
- [ADR 010: review state moves to SQLite after accumulating operational metadata](../adr/010-review-state-should-move-to-sqlite-once-reviews-leave-git-and.md) — see-also: accepted storage threshold this proposal must not recreate unnoticed in report files
- [Churning state on a many-to-many edge is where files yield to a database](../../notes/many-to-many-edge-state-is-where-files-yield-to-a-database.md) — rationale: distinguishes one report-owned disposition from the review edge-state that earned a relational store
- [Run a full improvement pass on one note](../../instructions/run-full-improvement-pass-on-note.md) — procedure: workflow whose non-`keep` branch this proposal would replace
