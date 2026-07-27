# The lifecycle model — discussion summary (2026-07-25)

Consolidated record of the session that produced [ADR 056](../../reference/adr/056-adopted-and-retired-proposals-archive-out-of-the-frontier.md). The ADR states the rules; this file keeps the reasoning that produced them, the order the reframings arrived in, and what is still open. The companion [disposal survey](./disposal-and-retirement-survey.md) holds the raw audit data.

## How it started

The question was why adopted proposals were not being deleted. The investigation found no rule requiring deletion: `proposals/README.md` and ADR 028 name the lifecycle *transition* (a converged proposal becomes an ADR and is superseded by it) but never say what that does to the file. The workshop contract states its disposal operation explicitly; the proposals contract had no disposal clause at all, so every adoption improvised.

The audit then corrected itself twice, and both corrections mattered:

- **First pass:** three behaviors, one deletion (ADR 046) versus two ad-hoc retention banners (ADRs 044, 045).
- **Second pass** (found via `properdocs.yml`, not `rg`): **six** deletions — ADR 046 plus three under ADR 050 and two under ADR 051 — each with a site redirect to the adopting ADR. Deletion was the settled practice, not the outlier, and it *post-dated* the two retentions. All eight decisions fell inside three days.

Two lessons, both about method. Searching `kb/` alone missed a real convention living in a config file at the repository root. And a shallow clone cannot see deleted content: this session's clone began 2026-07-18, so none of the six deletions were visible in git history — which is itself an argument against relying on git history as the archive.

## The reframings, in order

Each of these came from the maintainer and changed the design; recording the sequence because the *later* ones invalidate reasoning that looked settled at the time.

1. **The cost is search surface, not storage.** Texts are cheap to store; indexing them and receiving them as irrelevant search results is not. The goal is therefore quick location of the **frontier** — what is still open. This flipped the design axis: not "delete versus keep" but "in the frontier versus out of it, and still citable versus not."
2. **Archive rather than delete.** Deletion loses the design object — option space, forces, free choices — which an ADR does not preserve and which supports later audit or re-opening.
3. **Directory separation beats in-place marking.** This overturned an earlier lean recorded in the survey. In-place marking (a banner or status field) was judged adequate when only link breakage was priced; once the search surface is the cost, it fails, because marked files stay inside every default listing and `rg` sweep. `ls` on the directory should itself be the frontier.
4. **The archive is a link sink, with an extraction obligation.** Archiving is gated on removing everything current; incomplete extraction is repaired by **re-extraction**, never by linking in, because a live link makes the archived document load-bearing again. This is the workshop layer's own sinks-not-sources rule, so the KB now has two sink layers — one before the frontier (deleted after extraction), one after it (retained after extraction).
5. **Provenance is a tag, not a pointer.** An ADR names its proposal by title, not by link. A typed provenance-link exemption was considered and rejected: any exempt category is where the boundary leaks, since an agent follows a link regardless of its label.
6. **Then the ADR is incomplete** — a commitment is not meaningful without its alternatives. Tag-not-pointer removed the ADR's ability to borrow completeness, so the ADR contract had to absorb the decision-relevant subset of the proposal. This is the clearest instance of the session's pattern: each rule created the debt the next one paid.
7. **ADRs archive too, eventually.** Nothing is frontier-forever; an ADR's attention tier decays as its decision entrenches or is superseded.

## The model as it stands

**Tiers are coordinates, not categories.** The proliferation worry — frontier, archive, and ADRs as history-carrying frontier artifacts, with more to come — resolves if placements are read as points on generating axes rather than as kinds: standing attention cost (always-loaded → indexed → default-swept → on-demand), link-graph role (source or sink), and relation to ground truth. This is the same taxonomy-to-dimensions move the KB made in ADR 042 (registers became open profiles) and ADR 045 (a closed genre enum became an open field). The lifecycle is a trajectory through that space, which is why ADRs eventually archiving needs no special pleading.

**The cache analogy is mostly already built.** Re-extraction is refill-on-miss (a cache holds copies, not pointers into the backing store — exactly the link-sink discipline); the extraction obligation is writeback-before-eviction; freshness baselines are invalidation; the marks doctrine is coherent-or-absent; `theory-methodology-derivation` is designing derived-fast-path-with-fallback.

**One refinement the analogy needs.** Two different derived-artifact relations exist and only one is a cache:

- **Recomputable cache** — marks, generated indexes. Deterministically re-derivable; maintenance rule is checked-or-absent; repair is recompute.
- **Committed compression** — ADRs, notes promoted from workshops. Lossy and judgment-laden; re-running the process would not reproduce them. At commitment they *become* the new ground truth and their raw material demotes to provenance. So an ADR is not a cache of its proposal — it is the original record of a decision whose subject is historical, which is why it sits in the frontier while the proposal archives, and why its maintenance operation is supersession rather than invalidation.

("Committed compression" is a placeholder label. ADR 053 retired *distillation* without a successor; this is not a bid to re-mint it.)

## What shipped

ADR 056, plus the contracts it changed: `proposals/README.md` (archiving clause), `proposals/archive/README.md` (the archive-operating instruction — the one door through the boundary), `kb/reference/COLLECTION.md` (proposal exception), and `kb/reference/types/adr.md` (the considered-alternatives requirement and template).

Landing in parallel, from a different line of work: the `design-proposal` trait became a collection-local type (`kb/reference/types/design-proposal.md`). It absorbed the archiving rules on its own surface and sanctioned the `Proposal (adopted):` description lead one of the two migrated proposals had already been carrying ad hoc — so an archived-and-adopted proposal stays distinguishable in a description sweep, which still reaches `archive/`.

Worked migrations: ADR 045 absorbed the source-genre proposal's alternatives and resolved free choices; ADR 044 absorbed the assertion-force decomposition as a considered-and-rejected option; both proposals moved to the archive with inbound links re-pointed at the ADRs.

Two decisions during implementation that the discussion had not settled:

- **The alternatives requirement is prose and date-scoped, not schema-enforced.** The intent was a one-line schema addition; the corpus audit killed it — 4 of 56 ADRs carry alternatives prose, none as a heading, so a required heading fails the whole corpus at fail-by-default severity, and warning instead leaves 52 standing warnings, which is the noise the decision exists to remove. It follows the operativity-path precedent instead, with the template as the operative channel.
- **The workshop layer may link into the archive.** Surfaced when the move rewrote this workshop's own links. Permitted as a named exception: archive work (re-extraction, audit, re-opening) is what workshops are *for*, and workshop files are deleted rather than accumulated, so they cannot durably re-admit archived content to the library. The constraint stays checkable — no links into `archive/` except from `archive/` and `kb/work/`.

## Still open

- **Note retirement — mechanics shipped, trigger still missing.** ADR 044 answered maturation by removing the field. Decay now has a *procedure* — [retire-artifact.md](../../instructions/retire-artifact.md), shipped 2026-07-26 from an ops trigger rather than from this line of work — but no *signal*: nothing routes staleness to it. Proposals have a crisp eligibility rule (adopted or retired); notes have none. That gap is what remains of question 4.
- ~~**Source snapshot retirement.**~~ **Closed 2026-07-27 — not a disposal gap.** Snapshots are standing inputs to ADR 046's fail-severity quote check, and `cp-skill-connect` already routes to the matching ingest rather than the snapshot, so retention is load-bearing and standing cost is near zero. Revisit if a sweep starts struggling with the volume; an erroneous capture is a re-capture, not a retirement. See the per-kind directions in [the disposal survey](./disposal-and-retirement-survey.md).
- **ADR archiving.** Designed in the survey, deliberately unbuilt: superseded and deprecated ADRs are eligible immediately, accepted ones once inbound frontier citations go cold. No cohort exists yet.
- **Enforcement.** The validator now enforces the archive boundary as the KB's first genuinely mechanical lifecycle rule. Nothing else here — banners, status fields, extraction completeness — is checkable without judgment.
- **Whether any of this generalizes.** Candidate promotions to `kb/notes/`, each needing a second worked case first: ~~the recomputable-cache versus committed-compression distinction (the strongest candidate)~~ — **promoted 2026-07-25**, see the abstraction below; tiers-as-coordinates; and the workshop deletion bet — that the residue's expected retrieval value does not cover its standing search cost. The [disposal survey](./disposal-and-retirement-survey.md) carries these in full — the tier axes, the cache-mechanism correspondences, and the ADR-archiving sketch — and is the file to mine when a second case arrives.

## Follow-up session (2026-07-27)

Two things this session's output got wrong, found by re-reading it against the ADR type contract.

**The archiving justification was self-falsifying.** Reframing 2 above ("archive rather than delete — deletion loses the design object, which an ADR does not preserve") is contradicted by reframing 6, which made the ADR preserve exactly that. The sequence was recorded here as a virtue — "each rule created the debt the next one paid" — without anyone checking whether the debt, once paid, spent the earlier reasoning. It did. ADR 056 carries the false premise twice in its own body, and has been amended in place at both sites plus the extraction gate, where "accumulated dialectic" was named as legitimate residue in contradiction of the alternatives requirement three paragraphs below it. The decision stands; its grounds changed. The corrected test is in [the disposal survey](./disposal-and-retirement-survey.md#the-archive-versus-delete-test-2026-07-27).

**The instruction sprawl this predicted had already happened.** One archiving rule was stated in four places — `kb/reference/COLLECTION.md`, `proposals/README.md`, `proposals/archive/README.md`, and the `design-proposal` type spec — each mixing what must be true with how to do it. This is the recurrence that [where subtree-scoped write-time contracts live](../../reference/proposals/where-subtree-scoped-write-time-contracts-live.md) names as the only evidence that would warrant a general mechanism: *"the pull toward area READMEs re-emerging after instances have been absorbed case-by-case."* `proposals/archive/README.md` appeared one day after the collection-local type absorbed the proposals area — absorbed, and re-emerged immediately, one level deeper. That proposal's current-state anchor predates the archive directory and does not mention it.

The fix applied was a **contract/procedure split**: contract states what must hold and lives on an enforced surface; procedure states how and lives in `kb/instructions/`; neither restates the other. That deduplicates but adds no teeth — an instruction file is not a gate for the proposals cohort — so it does not settle the proposal's real question. `kb/reference/COLLECTION.md`'s restatement was deliberately left alone, since whether it should be a routing summary or a checked derived copy is exactly what that proposal is deciding.

## What would close the workshop

Unchanged from the README: a lifecycle map naming each stage and its valid transitions, plus an updated `kb/work/COLLECTION.md` closure section. The disposal half now exists for two kinds — proposals (archive) and everything else (delete) — under one procedure with a type-declared destination. What the map still needs is note retirement *eligibility*, and one more worked case before the archive-versus-delete test is safe to promote.

---

Abstracted into:

- [Commitment, not derivation, creates new ground truth](../../notes/commitment-not-derivation-creates-new-ground-truth.md) — the "one refinement the analogy needs" section above, generalized and restated in the KB's narrow derivation vocabulary: the discriminator is what a production adds beyond its source rather than lossiness, the committer is generalized past LLM output to human acceptance and attestation, and the maintenance split is derived rather than observed. The second worked case is the ADR 025 / ADR 056 disposal contrast.
