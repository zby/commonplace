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

# Brief: prototype standing as revision cost

## Governing question

What makes a theory still cheap to revise or reject — its "prototype standing" — and is that standing set by whether the theory is written in natural language or in symbolic form, or by whether it has been accepted?

## Audience and reader update

Agents and maintainers reasoning about when to codify, bind, or accept theories in a theory-building KB, and readers of the pre-formal-stage and bitter-lesson arguments who have met the intuition that prose is cheap to revise and code is expensive. After reading they should locate revision cost in two components rather than in form or epistemic status, and treat binding a consumer as the act that spends standing.

## Target claim or purpose

A theory's prototype standing is its expected revision cost, the total of two components: external binding (consumers coupled to the current version, to which a revision propagates) and intrinsic reconstruction cost (investment a revision discards). Natural-language versus symbolic form determines neither component; acceptance is a separate axis that adds no consumer and discards nothing. The practical consequence is a warrant rule: binding a consumer before the theory is accepted for that consumer's scope spends standing evidence has not licensed. Current fit, current form, and executable success do not license binding; coordination value or an enduring constraint may still justify it as knowingly spent standing.

## Must keep

- A definition of "theory" tied to the per-part warrant note (inspectable named parts, at least one discriminating implication), so the claim's universal quantifier has a domain.
- Explicit separation from the discovery lifecycle and from the collection-prototype sense of "prototype", with the vocabulary-collision rule as the reason for disambiguating.
- The accumulation mechanism for binding, credited to the current-task-fit note and marked as a transfer from KB structure to theories. Binding need not be machine-readable; a harness-loaded instruction is a maximal-binding natural-language case.
- Why the cost is a total, not a maximum: the two components fall on different parties, so either can be large while the other is zero.
- A faithful rationale lowers reconstruction cost by allowing part-by-part repair.
- The diagnosis of the form error (availability of formal consumption read as coupling), what form does determine (available checks, per-use interpretation cost), and at most a weak, refutable correlation with investment.
- Per-part assessment at the grain consumers bind to, including partial codification.
- The cheap-formalization case: unbound formal models can hold prototype standing; formalization cost is a bundle whose parts fall independently; proofs warrant entailment inside the model, not world fit. The bitter-lesson portfolio note relies on this classification.
- A stated refuter: paired cases equal in both components but differing in revision cost, or a cost driver that reduces to neither (with authority and rollback cost argued to reduce to binding). Say plainly that no paired case has been observed.

## Exclusions

- No formula, weights, or probability model for "expected".
- No claim about distributed-parametric form, where retraining makes form set reconstruction cost; bound it out in Scope.
- No treatment of procedures or state records, which are superseded rather than refuted.
- Do not settle how entrenchment thresholds are chosen; defer to the current-task-fit note.

## Scope, modality, and terminology

Universal over theories in the defined sense, with its refutation condition stated in the body. The form-correlation remark is statistical and must name its refuter. Keep "prototype standing", "external binding", "intrinsic reconstruction cost", "acceptance", and "binding" fixed; do not use "prototype" loosely elsewhere in the note. Scope limits and open measurement questions go in `## Scope` and `## Open Questions`.

## Reserved decisions

- Whether a bounded operative trial counts as binding before acceptance or as acceptance for a trial scope.
- Whether to add a third component or weighting scheme.
- Whether to widen the form bound to include parametric representations.
