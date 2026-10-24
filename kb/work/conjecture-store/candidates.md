# Candidate conjectures

Conjectures raised while planning the store, written in the draft type's
shape as plain text because the collection does not exist yet. Each becomes a
conjecture record at stage 0 seeding or is dropped.

## Every project builds its theory from its own choices plus general knowledge

- **Conjecture:** every project holds two kinds of commitments, choices it
  made and theory it built, and its working knowledge is theory stated with
  some variables bound to those choices and the rest to general knowledge.
  The transferable part of a project's knowledge is what survives when its
  choices are quantified out. Posed by the operator on 2026-10-24.
- **problem:** How should a knowledge system separate what a project
  believes because of what it chose from what it believes about any system?
- **Reach:** if true, the conjecture store and its two projections are a
  framework feature, not a Commonplace-local one: every consuming KB has its
  own choices (its ADRs, or decisions never written down) and its own theory
  (`kb/notes/`), and the same `choices` field sorts them. It also explains
  why Commonplace's theory collection has a high bar: it tries to hold only
  the quantified-out part, which is the smallest part of any project's
  working knowledge, so most of what a project knows has nowhere to go
  without a store for bound conjectures. It predicts that the bound/unbound
  split is relative to the system boundary: a choice made by a parent
  project is general knowledge to a subproject.
- **Analogues to check, not yet read for this purpose:** Carnap's external
  and internal questions (choosing a framework is a practical decision;
  questions inside it are theoretical), already touched in
  [philosophy borrowing](../philosophy-borrowing/carnap-explication.md);
  Lakatos's hard core and protective belt; architecture decision records as
  the practice that writes choices down without theory.
- **refuters:**
  - a project whose working knowledge cannot be factored this way: a claim
    that is neither about any system nor conditional on a nameable choice
  - a consuming KB where sorting by declared bindings misroutes most
    conjectures, because the choices cannot be named at the grain the
    arguments use
- **missing:** a second project, not Commonplace, whose working notes factor
  into bound and unbound claims when read with this lens
- **trigger:** `free variable|bound variable|residual selection|hard core`
  across `kb/`, and any consuming-project KB ingested into
  `kb/agentic-system-analyses/`
- **choices:** none; this is a theory conjecture

## Contradictions loaded into one context get silently averaged

- **Conjecture:** when an agent holds a claim and its contradiction in one
  context without structure that keeps them apart, its outputs drift toward
  a blend of the two rather than representing either. Carried from the
  deleted epistack menu (2026-07-08), where it justified separating the
  neutral map from the verdict layer and rejecting a case root that carries
  a bottom line; see [prior work](./prior-work-epistack.md).
- **problem:** Must rival conjectures and their criticism be kept
  structurally separate from the surface an agent writes from, or can one
  context hold both without distortion?
- **Reach:** if true, it is the mechanism behind three of the store's
  rules: rivals are separate records under one problem, the projection is
  computed rather than written into the store, and no conjecture is a
  premise. It also bears on review design generally: a reviewer given the
  verdict drifts toward it. If false, some of the separation is cheaper
  than assumed and could be relaxed.
- **refuters:**
  - the designed experiment run and showing no drift: one agent extends a
    neutral map from a case root that carries a bottom line, another from
    a verdict-free root, and the bottom-line arm's edits do not move toward
    the verdict
  - an agent shown two contradicting notes that reliably reports the
    contradiction instead of blending, across models and prompts
- **missing:** one run of the designed experiment, on any case with a
  stated bottom line and a neutral map
- **trigger:** `silently averag|averaged away|blend.*contradict` across
  `kb/`; any experiment record under `kb/theory/evidence/` whose arms differ
  by whether a verdict was in context
- **choices:** none; this is a theory conjecture
