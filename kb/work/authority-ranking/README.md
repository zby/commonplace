# Authority ranking

Workshop for designing how sources get ranked by authority — and first, for testing whether "rank" is even the right shape. Opened 2026-07-12 on the maintainer's direction after the genre unification shipped ([ADR 045](../../reference/adr/045-source-genre-is-a-single-open-field-on-the-snapshot.md)): genre is one entry point into authority, authors carry additional impact, and authority is suspected to be **more complicated than a linear rank**.

## What this workshop is for

The composition sketch already exists as a menu candidate — "ranking by authority: identity is a field, track record is a dossier, rank is derived" — and the guard rails are settled doctrine: no stored authority scalars ("confidence must be attributed, never a mark"), ranking stays a downstream, replaceable adjudication output ("adjudication as a separate layer"). These were catalogued in the `epistack-framework-additions` design menu, deleted with the epistack workshops on 2026-07-23 (recoverable from git history). What is *not* settled, and what this workshop owns, is the structure of the thing being computed:

- **Order shape.** Is authority a total order at all? Plausibly it is a partial order — genre gives a weak ordering only within a question domain; two sources can be incomparable rather than tied.
- **Domain conditionality.** An author's weight is conditional on the question (an epidemiologist on virology vs. on lab security procedures). Does a ranking function take the question as an argument, and what does that do to any precomputation?
- **Time variation.** Track record accrues and decays; a dossier is a history, not a state. What does "authority as of the snapshot's capture date" mean, and does any consumer need it?
- **Relational effects.** Independence discounting (shared-authorship/shared-dataset clustering) makes the authority of a *set* of sources non-additive in its members. A per-source rank may be the wrong type entirely — the meaningful object may be the weighted evidence set for one claim.
- **Consumer inventory.** What actually reads a ranking? Candidates: triage (what to read first), adjudication weighting (Rootclaim-style), over-reliance flags (dashboard: "this case leans on one cluster"). Different consumers may need different orders — which would settle the shape question in favor of per-consumer ranking functions over any shared rank.

## Evaluation boundary

Framework-side design only. Author dossiers and any concrete ranking experiment happen casebook-first in `epistack-casebooks` per that repo's `backlog-to-commonplace.md` protocol; this workshop consumes what that casework proves and designs the transferable mechanism. Doctrine constraints are inputs, not open questions: no stored scalars, adjudication downstream, frontmatter semantics stay type-owned ([collections never own frontmatter semantics](../../reference/collections-never-own-frontmatter-semantics.md)).

## What closes it

A proposal in `kb/reference/proposals/` that names: the order shape (total, partial, per-consumer), what a ranking function's inputs are (genre, dossier, independence, question), where ranking functions live (code, criteria, dashboards), and at least one worked consumer from the casework — or a documented conclusion that no consumer needs more than ad-hoc judgment, retiring the thread as YAGNI. Then this workshop is deleted.
