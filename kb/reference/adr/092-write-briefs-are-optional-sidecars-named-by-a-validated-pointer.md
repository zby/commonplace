---
description: "Decision that a document may carry an optional write brief, its preface for writers kept in a sibling <stem>.brief.md, declared by a validated brief: pointer and read by cp-skill-write as binding intent"
type: reference/types/adr.md
tags: []
status: accepted
---

# 092-Write briefs are optional sidecars named by a validated pointer

**Status:** accepted
**Date:** 2026-09-26
**Amends:** [ADR 084](./084-kind-rules-live-in-type-specs-and-operations-in-instructions.md), only in that authoring composition for a document with a brief reads one artifact-specific file beyond the writing skill, `COLLECTION.md` and the type spec. Kind rules and location rules stay where ADR 084 puts them.

## Context

Collection and type contracts say what may live in a collection and what shape an artifact takes. They do not record why one particular artifact exists. A writer editing a document later has only the document, the live request and its backlinks. The forces that would recur if this decision were reverted:

- **Commissioned content is lost in rewrites.** Ten documents were traced from the version their commission produced to 2026-09-26. Of 350 realized commission items, 83 had been weakened or removed. Most of the losses came from broad rewrites whose records named the overall change but not the items it dropped.
- **An explicit brief measurably reduces that loss.** A pre-registered pilot ran 95 edits on the same ten documents. Under pressure edits, writers holding the full brief broke about a third as many unguarded commission items as writers with none. A one-sentence brief did no better than none ([evidence](../../notes/evidence/full-write-briefs-cut-edit-drift-one-line-briefs-did-not.md)).
- **`cp-skill-write` already had a slot and no supplier.** Its Step 4 accepts retained intent that names its source, subject, scope and force. It forbids ad hoc history search, so without a declared mechanism nothing could fill the slot.
- **A stored text binds nobody unless a runtime loads it** ([Commonplace doctrine](../definitions/commonplace-doctrine.md)). A brief needs a declared, checkable route into the writer's context.

## Decision

**A document may have one write brief, as a sidecar.** The brief is the sibling file `<stem>.brief.md` with `type: types/write-brief.md`. The document declares it with `brief: <stem>.brief.md`, a bare filename resolved relative to the document's own directory. The [write-brief type spec](../../types/write-brief.md) defines the brief's form: intent first, then must-keep and must-exclude items, as directive text.

**The pairing is validated in both directions.** The `.brief.md` suffix is the single identity of a brief, and one predicate function answers it for every consumer. `commonplace-validate` rejects all of the following:

- a `brief:` value other than the document's own `<stem>.brief.md`;
- a missing brief;
- a suffix and type that disagree;
- a `.brief.md` file that its sibling does not declare;
- a brief that itself carries `brief:` or `tags:`.

**Writers load it; agents may write it.** `cp-skill-write` reads a target's brief as retained intent. It may write a brief when commissioning a write whose boundaries a later writer could not infer. The brief binds as intent until a user amends it, and current user direction always prevails. A conflicting request is followed with the amendment stated, and the brief is updated in the same write, or the writer asks when the conflict cannot be resolved from the request. Editing a brief affects only the next write of its target.

**A brief is part of its document.** It is the document's preface for writers. It is kept in a sibling file for two reasons only: to stay outside the text a write edits, and to stay out of the reader's view. Everything else follows from being part of the document:

- links point to the document, never to the brief, and a search hit on a brief counts as a hit on its document;
- a brief carries no tags of its own;
- `commonplace-relocate-note` moves a brief together with its document, renames it to the new stem and rewrites the pointer, and refuses to move a brief on its own;
- retiring a document retires its brief.

Commands need no special case for briefs. Searches, listings, the site and review sweeps may include them.

**Operativity path.**

- **Writing procedure.** `cp-skill-write` reads the brief when the target declares one, with the force stated above.
- **Validator.** `commonplace-validate` enforces the pairing and the forbidden fields.
- **Relocation command.** It keeps each pair together.
- **Retirement procedure.** Retiring a document deletes its brief with it.

## Considered alternatives

**Keep intent transient.** Keep reconstructing each document's purpose from the request and the document itself. This lost because the drift trace showed commissioned content being lost with no record, and the pilot showed an explicit brief preventing most of that loss.

**Put the intent in the document.** A frontmatter field such as `goal:`, or a body section. The operator rejected a frontmatter field. It would be edited in the same write as the document, so it cannot resist that write's drift, and it would compete with `description`. The pilot also showed that a one-sentence statement carries only the claim, which writers keep anyway. The must-keep and exclusion items do not fit in one sentence.

**A dedicated brief collection instead of sidecars.** This keeps briefs out of every collection's scans, but separates the commission from its document. The operator chose sidecars for locality.

**Exclude briefs from every artifact scanner.** Teaching the directory index, the site build, the review selector and link discovery to skip briefs would keep them out of listings. It lost because it would put a new special case in each command, and a brief found by a search or listing costs little. Revisit it if briefs cause concrete harm, such as noisy review sweeps.

**Require a brief for every substantive document.** This would make every commission explicit and reviewable. It lost because most documents' commissions are already carried by their title and opening, and the pilot showed a statement of intent alone adds nothing. A mandatory brief would add a file and a maintenance duty to documents that gain nothing from it.

**Delivery through a context assembler.** A named role in a coded write-context assembler would keep brief lookup out of skill prose. It lost for now. There is one consumer, and a validated pointer read by the writing skill follows the direct-pointer design `type:` already uses (ADR 018). The [assembler proposal](../proposals/deterministic-write-context-assembly.md) remains open as a later route that would not change the brief or its association.

**Require human acceptance before a brief binds.** Rejected. The pilot's briefs rebuilt from a document still faithful to its commission preserved it nearly as well as the originals, which suggests that agent-written briefs made at commissioning time are adequate. Current user direction always overrides a brief, which bounds the cost of a wrong one.

**Brief edits stale the target for review.** Rejected under YAGNI. No evidence yet shows briefs drifting from their targets unnoticed. The freshness store would need a new dependency kind for it.

**Pointer form.** A KB-root-relative path like `type:` values was considered. The sibling-relative bare filename was chosen because it survives directory moves without rewriting and admits only one legal value.

## Consequences

- A document whose commission has non-obvious boundaries can carry them to every later writer through a checked route.
- The retained-intent slot in `cp-skill-write` now has a supplier.
- Adding a brief is an ordinary write: it creates one sidecar and adds one frontmatter line to the target.
- Briefs appear in searches, listings and review sweeps alongside the documents they commission. The validator's pairing rule makes stray or mismatched briefs visible.
- A brief can go stale when a user deliberately reframes a document without amending it. The drift trace found such cases. The writing procedure requires a conflicting request to amend the brief, but a direct edit made outside `cp-skill-write` bypasses that.

**Left open.** What happens to a brief when its document is split or merged: whether each resulting document needs its own angle or one brief can commission several. Settle it the first time a split or merge meets a brief.

**Where this stops applying.**

- **Later edits only.** The evidence covers preservation through later edits of a document that still realized its commission. It does not cover new-note writing.
- **Rebuilt briefs.** A brief rebuilt from a document that has already drifted would encode the drift, so rebuilding briefs for old documents is outside this decision.
- **Small evidence base.** The pilot had ten documents and used one model family. Treat the effect size as indicative only.
