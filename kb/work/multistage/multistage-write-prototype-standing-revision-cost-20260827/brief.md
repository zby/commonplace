# Brief

## Governing question

What determines whether a theory has *prototype standing* — the lifecycle standing in which it is still cheap to revise or reject — and how does that standing relate to representational form (natural-language vs symbolic) and to epistemic status (accepted vs conjectural)?

## Audience and intended effect

Agents and maintainers deciding how an agent-operated system should retain, test, codify, and revise theories (the notes-collection default audience). After reading, the reader should be able to: (1) assess a theory's prototype standing from its expected revision cost rather than from its form or its acceptance status; (2) know which act (binding) to withhold before acceptance for a bound scope; (3) predict when two theories differ in standing.

## Target, mode, collection, type

- Target: `kb/notes/a-natural-language-theory-is-a-prototype-codified-or-rejected.md` (edit mode; incumbent preserved as `original.md` in this workshop).
- After promotion: relocate with `commonplace-relocate-note` to `kb/notes/prototype-standing-is-revision-cost-binding-plus-lost-investment.md` (filename ≤ 70 characters) so the old path redirects.
- Collection: `kb/notes/` under `kb/notes/COLLECTION.md`. Type: `kb/types/note.md`. Trait `title-as-claim`.

## Target claim (user-supplied; authoritative; do not expand)

A theory's prototype standing is its expected revision cost, which has two components:

1. **External binding** — consumers coupled to the current version, so a change propagates: procedures, training, certification, validators, executables.
2. **Intrinsic reconstruction cost** — the investment discarded on revision: a large proof development, an approved safety case, a trained model.

Representational form (natural-language vs symbolic) correlates weakly with the second component and determines neither. Epistemic status (accepted vs conjectural) is a separate axis. This makes the prior review residual — that internal proof/model dependencies and lost evidential investment count even before external adoption — part of the mechanism rather than an exception.

Working title (title-as-claim): "A theory's prototype standing is its revision cost: external binding plus lost investment".

## Must be kept in the rebuilt note (user direction; each follows from the axis)

- (a) Prototype standing defined as a lifecycle standing, not an epistemic status; with the engineering-gloss disclaimer that this is not the collection-prototype sense (clone-once creation-time contract text, see `kb/reference/collection-prototypes.md`) nor the exemplar sense.
- (b) The warrant rule, reframed: **binding is the act not to perform before acceptance for the bound scope**; link `kb/notes/exact-implementation-does-not-validate-a-requirement.md`.
- (c) The grain point: standing is assessed at the grain consumers bind to; partial codification creates mixed standing only where binding differs.
- (d) One paragraph on cheap formalization: a symbolic artifact can exist unbound, so cheap construction/proof/checking lets formal models be experiments inside the prototype loop. Keep conditional (only where formalization cost was the bottleneck). Keep the cost-bundle caveat (translation, construction, proof generation, checking vary independently). This paragraph must survive; the user states `kb/notes/the-bitter-lesson-defense-portfolio-has-one-load-bearing-member.md` relies on it.
- (e) A testable consequence: two theories of the same form and same epistemic status should differ in prototype standing when their binding or reconstruction cost differs; two of different form should not differ when those are equal.

## Must move out (user direction; disposition recorded in the workshop, never silently deleted)

1. The "Formal checking moves, but does not erase, interpretation" branch (scheduler example, Eigenius, DiscoverPhysics, purely-formal exception) — a separable claim about the model-to-world correspondence boundary. Dispose as either a new note (working title "Codification relocates interpretation to the correspondence boundary") or an extension to `kb/notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md`, whichever the reconstruction supports.
2. "Codification and acceptance are independent" — `kb/notes/definitions/codification.md` already separates form from adoption; reduce to one sentence plus a link.
3. The prevalence hypothesis (codification pressure rises with invocation frequency and misreading cost, falls with volatility) — no evidence; demote to an Open Question or drop.

## Local copy findings to address where the text survives

Ground "distributed-parametric" at first use (link `kb/notes/definitions/representational-form.md`); ground the collection-prototype sense at first use; fix the two parsing ambiguities the packet flagged (competing pronoun referents); split the packed opening sentence.

## Links

Keep the existing footer edges that still fit the one-axis claim: `superseded-choices-are-retained-superseded-beliefs-are-not.md`, `selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md`, `treat-continual-learning-as-representational-form-coevolution.md`, `the-bitter-lesson-defense-portfolio-has-one-load-bearing-member.md`, `goedel-machines-are-a-proof-governed-case-of-self-modification.md`. Add `current-task-fit-alone-does-not-warrant-costly-entrenchment.md` as the binding mechanism (label `mechanism` or inline). Use only labels authorized in `kb/notes/COLLECTION.md`.

## Sources and evidence available to this run

Library notes (read as evidence for the mechanisms they state):

- `kb/notes/current-task-fit-alone-does-not-warrant-costly-entrenchment.md` — entrenchment and reversibility cost.
- `kb/notes/exact-implementation-does-not-validate-a-requirement.md` — executable success does not validate a requirement.
- `kb/notes/definitions/codification.md` — codification is a form crossing, separate from adoption.
- `kb/notes/definitions/representational-form.md` — natural-language, symbolic, distributed-parametric, mixed.
- `kb/notes/definitions/discovery-lifecycle.md` — acceptance as a lifecycle stage.
- `kb/notes/theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md` — the sense of "theory" used (inspectable named parts).
- `kb/notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md` — proof warrants entailment inside a model, not correspondence.
- `kb/notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md` — codify-and-relax trajectory.
- `kb/notes/unformalized-improvements-need-a-pre-formal-stage-in-the-loop.md` — the pre-formal stage; currently what the defense-portfolio note cites for the cheap-formalization objection.
- `kb/notes/the-bitter-lesson-defense-portfolio-has-one-load-bearing-member.md` — the citer named by the user.
- `kb/notes/vocabulary-collisions-prevented-at-write-time-not-read-time.md` — why the prototype senses are separated at write time.
- `kb/reference/collection-prototypes.md` — the collection-prototype sense.
- Footer-edge targets: `kb/notes/superseded-choices-are-retained-superseded-beliefs-are-not.md`, `kb/notes/selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md`, `kb/notes/treat-continual-learning-as-representational-form-coevolution.md`, `kb/notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md`.

External-case material (only relevant to the correspondence branch being moved out):

- `kb/agentic-systems/eigenius.md` — Lean proof checking with a separate correspondence check.
- `kb/sources/discoverphysics-benchmarking-llms-out-of-the-box-scientific.ingest.md` — accuracy/explanation split.

Review record (available to the architect after the source-first pass, and to the auditor; not to reconstruction): `kb/reports/state/full-pass/a-natural-language-theory-is-a-prototype-codified-or-rejected/20260826T111746Z-e1ae52/full-pass-report.md`, `closing/critique.md`, `closing/premises.md`.

## Retained intent and memory inputs

- User brief of 2026-08-27 (this run's commission): authoritative; selects the central contribution, the keep/move-out list, links, and the relocation follow-up.
- Full-pass packet of 2026-08-26 (`20260826T111746Z-e1ae52`): advisory review evidence; its Open items motivated the commission (closing critique: internal proof/model dependencies and lost evidential investment weaken "downstream coupling alone"; closing premises: premise 5 DOUBTFUL — loose downstream coupling may not make a large exploratory proof development cheap to revise). It cannot select intent beyond what the user brief adopts.
- No other retained intent supplied.

## Scope, exclusions, terminology

- "Theory" keeps the inspectable-parts sense (`theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md`).
- "Codification" keeps the KB technical sense (form crossing into a symbolic artifact with formal semantics or assigned consequences).
- "Prototype" is an engineering gloss, not canonical vocabulary.
- Claim modality (ADR 066, `kb/notes/COLLECTION.md`): state the mode in the text; the central claim is intended as universal over theories within the stated "theory" sense. The form–cost correlation is a tendency and must be stated as such with what would refute it, or omitted.
- Exclude the relaxed-Gödel-machine application (already removed by the prior pass; keep only the footer contrast link).
- Do not reintroduce the prevalence claim that formalization is already an ordinary agent operation.

## Known uncertainties and reserved decisions

- The correspondence branch's home (new note vs extension of `formal-systems-assess-…`) is decided by the reconstruction/disposition; executing it is a handoff unless the user authorizes it inside this run.
- The user names `the-bitter-lesson-defense-portfolio-…` as the only library citer, but it currently links `unformalized-improvements-need-a-pre-formal-stage-in-the-loop.md` for the cheap-formalization objection and does not link this note. Reconciling that citer may therefore be a no-op or a wording check; record what is found.
- No ingest-grounded claims are retained in the rebuilt note by design; if the correspondence branch is promoted as its own note, its Eigenius and DiscoverPhysics uses must pass the grounding route (`cp-skill-ground`) or carry the `(snapshot required)` marker.
- Do not commit.
