# Edit task

You are editing one Commonplace KB document in a sandbox. Purpose: produce the edited document the request below asks for, as a careful maintainer of this KB would.

The document is `document.md` in this directory. Treat it as the document located at `kb/notes/prototype-standing-is-revision-cost-binding-plus-lost-investment.md`: that path determines its collection (the `COLLECTION.md` of its collection) and, with its frontmatter `type:`, its type spec.

Read and follow `kb/instructions/cp-skill-write/SKILL.md` in edit mode, with these deviations:

- Write the complete edited document to `candidate.md` in this directory. Never modify `document.md` or any file outside this directory.
- Skip Step 7 (source grounding) and Step 9 (validation), and add no new external-source dependency. Do not invoke other skills.
- For the backlinks lookup, use `backlinks.md` in this directory; read the files it lists with `git show <commit>:<path>` exactly as given.
- If the skill would have you ask the user a question, write the question to `question.md` in this directory and stop without writing `candidate.md`.
- Do not read the file currently at `kb/notes/prototype-standing-is-revision-cost-binding-plus-lost-investment.md` or at any other path this document had, do not use git history (other than the `git show` reads above), and do not read anything under `kb/work/`, `kb/reports/`, or `kb/messages/` outside this directory. You may read other library documents as the skill needs.
- Finish with a two-line report: what you changed, and anything in the request you did not do, with the reason.

## Request

Give the point that codification and acceptance are independent its own short paragraph, with one example of a codified theory that has not been accepted and one of an accepted theory that stays in prose.

## Retained intent

Source: retained commission for this document. Subject: `kb/notes/prototype-standing-is-revision-cost-binding-plus-lost-investment.md`. Scope: this document. Force: authoritative for intent; the request above is current user direction and prevails where the two conflict.

# Brief

## Governing question

What determines whether a theory has *prototype standing* — the lifecycle standing in which it is still cheap to revise or reject — and how does that standing relate to representational form (natural-language vs symbolic) and to epistemic status (accepted vs conjectural)?

## Audience and intended effect

Agents and maintainers deciding how an agent-operated system should retain, test, codify, and revise theories (the notes-collection default audience). After reading, the reader should be able to: (1) assess a theory's prototype standing from its expected revision cost rather than from its form or its acceptance status; (2) know which act (binding) to withhold before acceptance for a bound scope; (3) predict when two theories differ in standing.

## Target, mode, collection, type

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

## Must move out (user direction) 1. The "Formal checking moves, but does not erase, interpretation" branch (scheduler example, Eigenius, DiscoverPhysics, purely-formal exception) — a separable claim about the model-to-world correspondence boundary.
2. "Codification and acceptance are independent" — `kb/notes/definitions/codification.md` already separates form from adoption; reduce to one sentence plus a link.
3. The prevalence hypothesis (codification pressure rises with invocation frequency and misreading cost, falls with volatility) — no evidence; demote to an Open Question or drop.

## Links

Keep the existing footer edges that still fit the one-axis claim: `superseded-choices-are-retained-superseded-beliefs-are-not.md`, `selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md`, `treat-continual-learning-as-representational-form-coevolution.md`, `the-bitter-lesson-defense-portfolio-has-one-load-bearing-member.md`, `goedel-machines-are-a-proof-governed-case-of-self-modification.md`. Add `current-task-fit-alone-does-not-warrant-costly-entrenchment.md` as the binding mechanism (label `mechanism` or inline). Use only labels authorized in `kb/notes/COLLECTION.md`.

## Scope, exclusions, terminology

- "Theory" keeps the inspectable-parts sense (`theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md`).
- "Codification" keeps the KB technical sense (form crossing into a symbolic artifact with formal semantics or assigned consequences).
- "Prototype" is an engineering gloss, not canonical vocabulary.
- Claim modality (ADR 066, `kb/notes/COLLECTION.md`): state the mode in the text; the central claim is intended as universal over theories within the stated "theory" sense. The form–cost correlation is a tendency and must be stated as such with what would refute it, or omitted.
- Exclude the relaxed-Gödel-machine application (already removed by the prior pass; keep only the footer contrast link).
- Do not reintroduce the prevalence claim that formalization is already an ordinary agent operation.

## Known uncertainties and reserved decisions

- No ingest-grounded claims are retained in the rebuilt note by design.
