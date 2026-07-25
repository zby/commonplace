# Disposal and retirement across artifact kinds — survey (2026-07-25)

Working file for question 4 (retirement protocol), widened from notes to every artifact kind. Trigger: an investigation into why adopted proposals are not deleted found that the proposal contract specifies the lifecycle *transition* (proposal → ADR) but not the *disposal operation* — and that the rest of the KB handles end-of-life with five different operations, only some of them written down.

## The trigger case: adopted proposals

[`kb/reference/proposals/README.md`](../../reference/proposals/README.md) says a converged proposal "becomes an ADR and the proposal is superseded by it," and its lifecycle line ends in "ADR (decided and implemented) — or retirement." Neither the README nor [ADR 028](../../reference/adr/028-design-proposals-live-in-reference-proposals.md) says what supersession or retirement does to the file. Compare the workshop contract, which is explicit ("extract durable conclusions … delete the workshop directory"). Practice went three ways:

1. **Deleted once.** [ADR 046](../../reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md) "supersedes and retires the verifiable-quotes proposal, whose content has shipped" — and no such file exists anywhere in the repo. (The deletion itself predates the visible history; the current clone's history starts 2026-07-18.)
2. **Kept with an ad-hoc banner, twice.** [source-genre](../../reference/proposals/source-genre-is-one-open-field-on-the-snapshot.md) (adopted by ADR 045) and [assertion-force](../../reference/proposals/assertion-force-separate-from-lifecycle-status.md) (retired by ADR 044) both carry blockquote banners — "this document remains as design history." The source-genre description was hand-edited to "Proposal (adopted):", a prefix outside the contract's vocabulary.
3. **Partial adoption, per the written rule.** [factored-dependency-pairs](../../reference/proposals/factored-dependency-pairs-for-review-freshness.md) (one item adopted by ADR 041) and [gate-learning](../../reference/proposals/gate-learning-from-accepted-edits.md) follow the partial-adoption clause (shipped content moves out, adoption noted) — the one disposal path the contract does define.

Three forces keep the kept ones in place:

- **ADRs link back.** ADR 045 carries a `supersedes:` edge — "the proposal this decision adopts" — and cites the proposal in its Context. The [link vocabulary](../../reference/link-vocabulary.md) defines `supersedes`/`superseded-by` by the reader-need "wants the current or prior version," which presupposes the prior version exists. Other library artifacts also cite retired proposals as history ([collections-never-own-frontmatter-semantics](../../reference/collections-never-own-frontmatter-semantics.md) cites assertion-force explicitly as "the retired proposal").
- **The ADR doesn't preserve the design object.** An ADR records the decision and consequences, not the option space, forces, and rejected alternatives. Both retention banners were written by operators who judged that deletion loses information.
- **Nothing enforces the directory's claim.** The README opens with "Finished but *unadopted* designs" and requires that "nothing in this directory describes shipped behavior," but no validator or gate checks lifecycle state; the `design-proposal` trait routes review to design quality only. Drift is silent.

The defect is therefore not "deletion isn't happening" — it's that two of the three observed behaviors are unlicensed, and the directory's contract now disagrees with its contents.

## Survey: end-of-life per artifact kind

| Artifact kind | Contract says | Practice shows | Gap |
|---|---|---|---|
| Workshop (`kb/work/`) | Delete on close; remove index entry ([COLLECTION.md](../COLLECTION.md)) | Deletions happen (epistack workshops deleted 2026-07-23); citing docs leave a "recoverable from git history" pointer | Works. But the git-history pointer is fragile — see tensions below |
| Proposal (`kb/reference/proposals/`) | Transition named ("superseded by" the ADR; "retirement"), disposal operation undefined; partial adoption defined | Split three ways (above) | **The live defect.** Disposal clause missing; directory claim contradicted; no enforcement |
| ADR (`kb/reference/adr/`) | Status enum `accepted` / `superseded` / `deprecated` on the type; files never deleted | Superseded ADRs stay in place, status flipped, chained by `supersedes` edges | None — this is the proven archive-in-place model. ADR 028 killed the one stale state (`proposed`) by removing it from the enum |
| Note (`kb/notes/`) | No lifecycle field since [ADR 044](../../reference/adr/044-user-verification-replaces-global-note-status.md) removed the fused global `status`; optional user verification replaces maturation. Retirement/deletion: nothing | Notes get revised in place; full-pass machinery has delete/merge branches gated on human authority; no written staleness→disposal protocol | Question 4's original target, still open. ADR 044 answered the *maturation* half (question 3) and left the *retirement* half untouched |
| Vocabulary / term | No general contract | Terms are retired by ADR ([ADR 053](../../reference/adr/053-retire-distillation-without-a-successor-term.md) retired "distillation" with no successor; [ADR 042](../../reference/adr/042-register-becomes-a-default-profile-under-open-ended-text-contracts.md) retired register-as-closed-taxonomy) | Works case-by-case; retirement-by-ADR is the de facto operation |
| Source snapshot / ingest (`kb/sources/`) | Nothing — no retirement, supersession, or refresh language in the collection contract | No observed retirements | Latent. Captures are treated as permanent; a wrong or dead capture has no defined exit |
| Review state (store) | `commonplace-freshness-retire` removes a registered baseline "when an artifact or target should leave global status" ([commands.md](../../reference/commands.md)); [ADR 036](../../reference/adr/036-review-acceptance-is-current-state-not-append-only-history.md) makes acceptance current-state | Codified and idempotent | None — the one *codified* retirement operation in the system, but it covers DB targets, not documents |
| Tag-README / tag | Marks (`complete` / `covered_by`) maintained per type contract | — | Tag retirement (a tag emptying out, a README orphaned) undefined; low pressure |
| Instruction / skill (system-definition artifacts) | Behavioral authority names consumer/channel/force; promotion by copying (ADR 037) | Retirement = removal from runtime surfaces | Un-promotion / decommissioning not written, but the behavioral-authority frame at least makes "inert" detectable |

## The disposal-operation inventory

Five distinct operations are in live use; only 2 and 5 are fully licensed by a contract where they occur:

1. **Delete, pointer in git history** — workshops (licensed there), one proposal (unlicensed there).
2. **Archive in place with a status flip** — ADRs (`superseded` / `deprecated`), licensed by the type spec.
3. **Archive in place with an ad-hoc banner** — two proposals; imitates the ADR model without a license.
4. **Retire a DB target** — freshness baselines, licensed and codified.
5. **Content moves out, residual stays** — partial proposal adoption, licensed by the proposals README.

## Design tensions

- **Delete vs. inbound links.** Deletion breaks `supersedes` edges and design-history citations; the link vocabulary's supersession semantics *require* a surviving target. Any kind whose successors must cite it (proposals cited by ADRs) cannot use operation 1 without breaking the graph.
- **Archive-in-place vs. directory contract.** A directory that promises "only live X here" (proposals: "finished but unadopted") cannot archive in place unless the contract names the archived state. ADRs solve this: the type contract anticipates `superseded`, so a superseded ADR in the directory is *conforming*, not drift. Proposals imitated the mechanism (banner) without amending the contract.
- **Git history is not an archive.** The "recoverable from git history" pointer assumes deep history. This session's clone starts 2026-07-18 — everything deleted before that is invisible here. Deletion is fine for value-consumed layers (workshops), but for anything a durable artifact cites as history, in-repo retention is the only navigable archive.
- **Enforcement gap is general.** No lifecycle state anywhere is validator-checked (ADR status values are schema-checked, but nothing checks that a `superseded` ADR names its successor, or that a proposal cited by an ADR `supersedes` edge is marked adopted). Marks doctrine (enforced-or-omitted, per [tag-readme](../../types/tag-readme.md)) suggests: if lifecycle state is worth recording, it's worth checking; otherwise omit it.

## Working direction (updated 2026-07-25 with maintainer input)

Maintainer reframing: the operative cost of retaining a stale artifact is not storage but the search surface — texts are cheap to store, expensive to index and to receive as irrelevant search results. The KB's theory already carries this claim: [flat memory predicts specific cross-contamination failures](../../notes/flat-memory-predicts-specific-cross-contamination-failures-that-are.md) (operational debris pollutes search; signal-to-noise degrades as volume grows) and [knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) (cue dilution). The design goal is therefore **quick location of the current frontier**: the live, undecided set must be readable at a glance, and disposal is the operation that removes an artifact from the frontier. Preservation is a separate, secondary question — which is why "delete vs. keep" was the wrong axis; the axis is "in the frontier vs. out of it, and still citable vs. not."

Per kind:

- **Workshops — delete, unchanged.** The early decision stands and works. It can never be guaranteed that nothing useful remains; the bet is that the expected retrieval value of the residue does not cover its standing search-surface cost, and practice has borne this out. (Transferable claim candidate for `kb/notes/` when the map is extracted.)
- **Proposals — archive by directory separation, not delete and not in-place marking.** `ls kb/reference/proposals/` should itself be the frontier. In-place marking (banner or frontmatter field) keeps stale files inside every default listing and scoped `rg` sweep and taxes every search with a filter; deletion breaks the ADR's `supersedes` edge and loses the design object. A subtree — e.g. `kb/reference/proposals/archive/` — removes archived proposals from the frontier while keeping them citable. The inbound-link cost of moving is already covered: the note-move command rewrites backlinks across the KB, and the [relocation-move-map-engine](../relocation-move-map-engine/README.md) workshop is generalizing exactly this. (This flips the earlier lean here that an `archive/` subtree "probably buys nothing over in-place marking" — that lean priced only link breakage and ignored the search surface.)
- **ADRs — the tension is real and now named.** ADRs read as historical, self-contained records, but in practice they do not carry the full decision data: they link back to the proposal for the option space and forces (ADR 045's `supersedes` edge plus its Context citation). The de facto record of such a decision is the *pair* (ADR + retained proposal). Two clean resolutions: (a) fold the design object into the ADR at adoption — self-contained history, fatter ADRs, the proposal becomes safely deletable; (b) accept the pair as the record — lighter ADRs, with the archive as a first-class citable location. (Resolved by the link-sink rule below: (a), strengthened.)
- **State in the store** → `commonplace-freshness-retire` and kin; already right.

### The archive is a link sink (maintainer rule, 2026-07-25)

The frontier does not link casually into the archive. Archiving carries an **extraction obligation**: all current knowledge leaves the artifact first — shipped behavior to reference docs and the ADR, transferable requirements to notes (both already in the proposals contract), and whatever decision data the ADR needs, inlined into the ADR. Extraction will occasionally prove incomplete; the repair is **re-extraction** — mine the archived artifact and promote what was missed — never a link into the archive. A live link would make the archived document load-bearing again, re-entering the frontier through the back door and defeating the separation. The only admissible frontier→archive links are from instructions for working with the archive itself.

This is the rule the workshop layer already has: "Library collections do not link **into** `kb/work/` — workshops are sinks, not sources of durable references. If a workshop produces something the library should cite, extract it first" ([COLLECTION.md](../COLLECTION.md)). The KB ends up with two sink layers under one rule — pre-frontier (`kb/work/`, deleted after extraction) and post-frontier (the archive, retained after extraction as re-extraction substrate: navigable history that does not depend on git depth). The only difference between them is whether the residue is worth on-demand retrieval.

Two consequences:

- **The decision record is the ADR alone.** The archived proposal is not part of the record; it is raw material for repair. ADR 045's `supersedes` edge and Context citation into the proposal, and [collections-never-own-frontmatter-semantics](../../reference/collections-never-own-frontmatter-semantics.md)'s citation of the retired assertion-force proposal, become non-conforming under this rule. The amendment's worked examples should re-extract or inline what those links currently carry, and refer to archived proposals by title, not path.
- **The rule is deterministically checkable.** "No live artifact links into the archive except designated archive instructions" is a validator-grade constraint — no semantic judgment needed, unlike lifecycle status fields. That gives the disposal contract the enforcement handle the tensions section above found missing everywhere else.

Open free choices for the proposals amendment: the adoption-time procedure (extraction checklist; the move; handling of existing inbound links — re-extract vs. inline, per the rule, not rewrite-and-keep); how an ADR refers to the proposal it adopted (title-only mention, or nothing); whether adopted-into-ADR and retired-as-YAGNI share one archive; whether archived files keep a banner pointing out to the superseding ADR (archive→frontier links are unproblematic — sinks may cite sources); whether the proposals README lists the archive beyond the working-with-archives instruction.

## What this file feeds

- Question 4's answer for the library kinds, and a new closure item: a disposal clause for `kb/reference/proposals/` (README amendment, possibly recorded as an ADR since it amends ADR 028's contract).
- The final life-cycle map note should carry the operation inventory and the citation-driven matching rule, if it survives the next worked case.
