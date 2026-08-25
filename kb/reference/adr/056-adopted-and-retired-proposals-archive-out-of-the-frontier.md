---
description: "Adopted and retired proposals move to a link-sink archive after extraction; provenance becomes a title tag, so ADRs from 2026-07-25 must carry a Considered alternatives section"
type: ../types/adr.md
tags: []
status: accepted
---

# 056-Adopted and retired proposals archive out of the frontier

**Status:** accepted
**Date:** 2026-07-25
**Amended by:** [ADR 074](./074-git-is-the-change-history-layer.md) — narrows the git-history argument to consumers without history; decision-audit measurements may live in git

## Context

[ADR 028](./028-design-proposals-live-in-reference-proposals.md) gave proposals a home and named their lifecycle transition — a converged proposal "becomes an ADR and the proposal is superseded by it" — but never said what that does to the file. The workshop layer states its disposal operation explicitly ("extract durable conclusions, delete the workshop directory"); proposals had no equivalent clause, so each adoption improvised. Practice split: six proposals were deleted when decided, with the documentation-site redirect map pointing their old URLs at the adopting ADR, while two stayed in place under hand-written design-history banners. The residue is decided proposals in `kb/reference/proposals/` describing shipped behavior, which the directory's own contract forbids.

The operative cost of keeping a decided proposal in place is not storage but standing search surface. This KB already argues the point — [flat memory predicts specific cross-contamination failures](../../notes/flat-memory-predicts-specific-cross-contamination-failures-that-are.md) (operational debris pollutes search; signal-to-noise degrades with volume) and [knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) (cue dilution) — and the workshop layer was built on it. What a maintainer needs from `kb/reference/proposals/` is a fast answer to "what is still open," which any directory holding both live and decided designs cannot give without a filter.

Deletion is the wrong instrument here, though it is right for workshops. Git history is not a substitute for a deleted proposal: a shallow clone cannot see it, and the KB's own convention of pointing at deleted content "recoverable from git history" degrades with clone depth. Deletion is unrecoverable in practice, so the choice is between retaining retrievably and destroying. The ground for retaining is stated with the extraction gate below.

## Decision

**Adopted and retired proposals move to `kb/reference/proposals/archive/`.** The frontier directory holds only live, undecided designs, so listing it answers "what is open" directly. Partially adopted proposals stay in the frontier; they still hold undecided content.

**Archiving is gated on extraction.** Everything still current leaves the proposal first: shipped behavior into reference docs, the decision-relevant reasoning into the superseding ADR, transferable requirements into `kb/notes/`. Design texture — dated current-state anchors and corpus statistics — stays behind. Deliberation is not residue: this decision routes it to the ADR, so an archived proposal whose only residue is dialectic has an incomplete extraction, not an archiving case.

The residue that justifies retention is **dated current-state anchors and corpus statistics — irreproducible observations of a system state that no longer exists.** Nobody can re-derive "4 of 56 ADRs carry alternatives prose" at any price once the corpus has moved on, and those measurements are the evidentiary warrant for a commitment that is now load-bearing. Auditing whether a live decision was justified means reaching the evidence it rested on, which the ADR compresses rather than reproduces. That is the standing need an archive serves, and it is why workshops still delete: their observations warranted no shipped commitment, so nothing has a claim on them once the investigation closes.

**The archive is a link sink.** No library artifact links into it. Two exceptions: `archive/README.md`, the instruction for working with archived proposals, which links its own contents freely; and the workshop layer, since re-extraction, decision audit, and re-opening are what workshops are for, and workshop files are deleted rather than accumulated, so they cannot durably re-admit archived content to the library. Archived files may link out. This is the rule `kb/work/COLLECTION.md` already applies to workshops ("sinks, not sources of durable references"), so the KB now has two sink layers — one before the frontier, deleted after extraction, one after it, retained after extraction — differing only in whether the residue is worth keeping for on-demand retrieval.

**Provenance is a tag, not a pointer.** An ADR names the proposal it adopted or retired by title in prose, with no path and no link. Under the prose-versus-registered-identifier rule in `AGENTS.md`, a spaced prose mention asserts no formal edge, so this needs no exemption from the sink rule and creates no edge for link tooling, connect runs, or a reading agent to follow. `supersedes` edges between live artifacts are untouched.

**Incomplete extraction is repaired by re-extraction.** When something current turns out to have been left behind, it is mined from the archived proposal and promoted into the frontier — never reached by a live link, which would make the archived document load-bearing again.

**ADRs dated 2026-07-25 or later must carry a `## Considered alternatives` section** naming the options weighed and why each lost, the deciding forces, and free choices resolved or left open. Tag-not-pointer removes the ADR's ability to borrow completeness from its proposal, so the ADR must own it: a commitment recorded without its alternatives cannot be audited or revisited. Compression is the discipline — a paragraph per option, not the option's text. Earlier ADRs are not retrofitted, except 044 and 045, whose proposals this decision archives.

## Considered alternatives

**Delete adopted proposals, as workshops are deleted.** Not merely a candidate but the incumbent: six of the eight recently decided proposals were deleted, with a site redirect carrying their URLs to the adopting ADR. It is the simplest rule and it keeps the frontier clean. Rejected because deletion makes git history the archive, which fails at shallow clone depth (this decision was drafted in a clone unable to see any of the six), and because the two disposal cases are not alike: a workshop's observations warranted no shipped commitment, while a decided proposal's corpus measurements are the evidentiary warrant for a live decision and cannot be re-derived. The frontier clarity that motivates deletion is fully delivered by directory separation, at no information cost; the redirect convention carries over unchanged, now pointing at the archived file.

**Archive in place with a status marker** — a banner or a frontmatter lifecycle field, on the ADR model where a `superseded` ADR conforms because its type contract anticipates that state. This was the leading option until the search-surface cost was priced. Rejected because in-place marking leaves decided proposals inside every default listing and scoped `rg` sweep, taxing each with a filter and defeating the goal; a frontmatter field would also add lifecycle state that nothing validates, which the marks doctrine (enforced or omitted) warns against. The banner survives as an archive-internal convenience, not as the mechanism.

**Keep the ADR's link to its proposal, exempting typed provenance links from the sink rule.** Attractive because it preserves one-click navigation and needs no ADR expansion. Rejected because any exempt link category is where the boundary leaks: load-bearing links dress themselves as provenance, and mechanically a link is a link — an agent follows it regardless of its label. The asymmetry covers the need anyway, since the archived file links out to its ADR, so a reader browsing the archive keeps one-click connectivity in the direction that costs no frontier attention.

**Enforce `## Considered alternatives` in `adr.schema.yaml`.** Intended, and abandoned on audit: 4 of 56 existing ADRs carry alternatives prose and none carry it as a heading, so a required heading fails the corpus at the schema's fail-by-default severity ([ADR 024](./024-schema-severity-is-per-constraint-fail-by-default.md), which explicitly says to audit before flipping), and opting down to `warn` would leave 52 standing warnings — the same noise this decision exists to remove. The requirement is therefore prose and date-scoped, exactly like the operativity-path requirement added a day earlier, with the template carrying it into new ADRs. It becomes schema-enforceable if the corpus is ever retrofitted, or through an imperative dated type rule ([ADR 048](./048-imperative-type-rules-dispatch-by-canonical-path.md)) if the prose requirement proves insufficient; neither is built now.

**Free choices left open.** Whether adopted and retired proposals should eventually separate into distinct archive states (one archive suffices at two members); whether the frontier README should list archive contents (it does not — the archive README owns that); and when ADRs themselves should archive, which is the same trajectory one tier up. That last is deferred deliberately: superseded and deprecated ADRs are eligible immediately and accepted ones once their inbound frontier citations go cold, but no such cohort exists yet, and the mechanism should not be built ahead of its first real case.

## Consequences

`ls kb/reference/proposals/` is now a frontier listing: every entry is a live design question. Decided designs stay navigable at a stable path instead of depending on clone depth, and the boundary is deterministically checkable — "no artifact outside the archive links into it, except its README" needs no semantic judgment, which no other lifecycle rule in this KB can say.

ADRs get heavier. A decision now carries its own option space, which is the point — the record becomes self-contained and auditable rather than a pointer into design work that has moved out of view. The bound is per-option compression, not accumulation, and ADRs load on demand.

Harder: archiving is now a multi-step operation (extract, expand the ADR, repair inbound links, move) rather than a file move, and the extraction step is a judgment call that can be got wrong. Re-extraction is the designed repair, but it costs more than following a link would have. Readers of an ADR who want the full design object must go to the archive by title rather than by click; that reader is doing archive work, which the archive README exists to serve.

Operativity path: the rules are consumed by agents through three contract documents they already read before writing — `kb/reference/proposals/README.md` (the collection's routing and authoring contract), `kb/reference/proposals/archive/README.md` (archive operations), and `kb/reference/types/adr.md` (the ADR type contract, whose template carries the new section into every new ADR) — with binding force in each case, since a collection contract and a type spec are what conformance is judged against. The deterministic validator now enforces the archive boundary for library artifacts, including bare Markdown; the alternatives section remains prose-enforced because its corpus trigger has not been met.

---

Relevant Notes:

- [Flat memory predicts specific cross-contamination failures](../../notes/flat-memory-predicts-specific-cross-contamination-failures-that-are.md) — rests-on: the search-surface cost that makes separation, not deletion, the operation
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) — rests-on: cue dilution — why retained-but-indexed content still costs
- [A functioning KB needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — rests-on: the sinks-not-sources rule this decision extends to a second, retained sink layer
- [ADR 028: design proposals live in kb/reference/proposals](./028-design-proposals-live-in-reference-proposals.md) — supersedes: adds the disposal clause its lifecycle left undefined
- [ADR 024: schema severity is per-constraint, fail by default](./024-schema-severity-is-per-constraint-fail-by-default.md) — see-also: the audit-before-flipping rule that kept the alternatives requirement out of the schema
- [A derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — see-also: the marks doctrine that ruled out an unvalidated lifecycle frontmatter field
