# Split test: backlinks.md

Boundary test for idea 6 (design-proposal type in `kb/reference/`): split `kb/notes/backlinks.md` — the most ambiguous speculative-status squatter — into a theory half (stays in notes) and a feature-options half (would move to reference). If it parts cleanly, the system-facing/theory-facing line is sound.

## Allocation

| section | theory half | proposal half |
|---|---|---|
| The gap (current link surface, grep exists but isn't read-time) | — | ✓ system state |
| Use cases 1–4 (standing, grounding, impact, tension) | ✓ | ✓ — **the hinge, see below** |
| Non-use-cases (orphan vs hub; discovery ≠ backlinks) | ✓ read-time/batch boundary is transferable | ✓ routing to existing features |
| Design options A–D | — | ✓ pure option space + system precedents + the 13% stat |
| Trade-offs | prose-vs-metadata partially transferable | ✓ maintenance stats and /ingest boundary are system-specific |
| Open questions | — | ✓ all three are design questions |

## Result: it splits, but not along the predicted line

The predicted line was theory vs feature options. The actual line is **requirements vs option space**, and the requirements are dual-use:

- The four use cases are transferable reader needs — any linked, agent-operated KB has them. Generalized, they carry a contestable claim: inbound and outbound links serve **asymmetric reader needs** (outbound shows what a note rests on; inbound shows what rests on it — standing, grounding, impact, tension), and these needs are *read-time orientation* needs, distinct from the *batch maintenance* needs (orphan detection) that also consume inbound-link data. The non-use-cases section already argues this boundary (threshold zero-vs-high, purpose cleanup-vs-orientation).
- The same four use cases are the proposal's acceptance criteria — the R that options A–D are candidate witnesses for. The note is a proposal precisely because it exhibits four candidate witnesses and never commits to one.

So R wants to live on both sides. The resolution is not duplication but citation: the proposal artifact carries a `rationale` edge to the requirements claim in `kb/notes/` — the existing reference→notes edge, used exactly as designed. This suggests a **type-level rule for design-proposal**: requirements that are transferable claims belong in `kb/notes/` and are cited via `rationale`; the proposal inlines only system-specific constraints (here: the /ingest boundary, the 13% footer-coverage stat, the sync-script precedent).

## Draft skeletons

**Theory half** — `kb/notes/` claim note, replacing the use-case and boundary content:

> Title candidate: *Inbound links answer orientation questions outbound links cannot* (or sharper: *read-time backlink needs are orientation needs, not maintenance needs*).
> Body: the asymmetry (rests-on vs rests-on-it); the four reader needs as the argument; the orientation/maintenance boundary with orphan detection as the contrast case; the prose-readability trade-off as a boundary condition (inbound visibility is metadata, not prose — it competes with the inline-links-as-prose principle). Traits: `title-as-claim`.

**Proposal half** — `kb/reference/` design-proposal (type pending this workshop):

> Title: *Backlink surfacing for Commonplace*.
> Body: the gap (current system state); options A–D with pros/cons and precedents; system-specific trade-offs (maintenance stats, /ingest boundary); open questions (cost threshold, run timing, noise floor). Frontmatter: `rationale` → the theory note for requirements. No Decision section — that is what would distinguish it from the ADR it may someday become.

## Verdict for idea 6

- The split is clean **given one rule**: transferable requirements are extracted to notes and cited; the proposal holds option space + system-specific constraints. Without that rule, the use cases would be duplicated or stranded on one side.
- The test strengthens the proposal/ADR boundary from the Decisions section: this artifact visibly holds four witnesses and no decision — unrepresentable as an ADR, natural as a design-proposal.
- Remaining doubt: whether every squatter's requirements generalize as well as these four did. `selector-loaded-review-gates` is the next test case if doubt persists — its "requirements" may be thinner.

Not executed: the actual file moves await the design-proposal type existing. This file records the dry run.

## Addendum (2026-06-12): the proposal half is already stale

Operator correction after the dry run: curated tag READMEs receive no generated links, and complete generated listings are build-time-only — materialized for the web view at deployment, never stored in the repo ([ADR 025](../../reference/adr/025-complete-generated-indexes-are-build-time-only.md), refined by ADR 026: "nothing generated is committed at any size").

Consequences for the proposal half:

- **Option B (generated footers committed into notes) is foreclosed** by the committed-generated-content prohibition; its cited precedent (`sync_topic_links.py`) is now a counter-precedent — that mechanism's family was retired.
- **The live option space reorganizes by consumer**, following ADR 025's access-mode asymmetry. Human web readers: backlinks rendered at mkdocs build time — a second materialization of authored outbound links, one source of truth, nothing committed. Agents in the repo: on-demand inversion (option A / a scoped `rg` recipe), consistent with the curated-heads-plus-scoped-rg read path. Manual semantic backlinks (option C) survive only as curated authoring where semantics matter (e.g. symmetric `contradicts` already gives tension surfacing both ends).
- **The requirements half gains a parameter rather than rotting**: the four needs split by consumer (human web reader vs agent reading repo files), and the design answer differs per consumer. The agent-centric phrasing of the original use cases now reads as one binding of that parameter.

Test implication: the staleness landed almost entirely on the proposal half — current-state description, option space, precedents — while the requirements half survived intact and was arguably *strengthened* by ADR 025's access-cost framing. The two halves age at different rates, which is itself register evidence for the split: descriptive proposals are time-indexed, theoretical requirements are not. The design-proposal type should therefore carry a "current state as of <date>" anchor (as workshop READMEs already do), and staleness against later ADRs is an expected lifecycle event for proposals, not a defect.
