# Articles

Writing from the Commonplace knowledge base for readers outside the project — researchers and builders of agent and knowledge systems. Each article stands on its own, carries a byline and lifecycle status, and links into the KB it was distilled from.

Articles circulate in three states. A draft may change without notice and carries a visible banner inviting comments. A working paper is revisable on the record: its claims are still open, it carries a version and a revision date, and it invites counterexamples. A published article is frozen — corrections appear as dated annotations or superseding articles, never as silent rewrites.

## Working papers

Nothing circulating yet.

## Published

Nothing published yet.

## Presentations

- [Where It Lives Is Not What It Is — ASISAS 2026 slides](./asisas-2026-talk.html) — HTML deck prepared for a 10-minute talk and 2 minutes of questions, based on the [June 23 position paper](../sources/where-it-lives-retained-adaptation-2026-06-23.ingest.md). Use arrow keys, space, or click to navigate.

The deck uses *memory* for the audience-facing term and *natural-language*
in place of the paper's *prose*. It derives the three representational forms
from assigned consequences and localization; the terminology and derivation
are explained in [representational form](../notes/definitions/representational-form.md).
The slides show the terminology changes with strikeouts.

## In draft

Five drafts make one series: a lead article and four supplements. The lead
states the idea and stands on its own. Each supplement develops one part of
it, so read the lead first and then whichever supplement answers your next
question. Nothing in the series reports a result; no test has been run.

- [Conjectural Learning with Today's LLMs](./conjectural-learning-with-fixed-models.md) — the lead. It states the bet: a fully automated conjectural learner, a Popperian cycle of problem, tentative solution, error elimination, and revised problem over explicit revisable theories, can be built with today's fixed-weight LLMs. It gives the conjectured payoff of explicit learned state and its costs, argues compatibility with the Bitter Lesson, and states the two-part test that would count as learning. Testing, bootstrapping from Commonplace, and the software-house arrangement each point to a supplement.

The supplements, in the order a reader is likely to want them:

- [Testing Conjectural Learning](./testing-the-conjectural-learning-program.md) — sets a modest first testing goal: show under controlled conditions that retained revisions causally improve later capacity and stay revisable. Gives seven tests that expose the causal role of retained state (retention, use, withholding, perturbation, reconstruction, transfer, revision), separates task success from learning, sketches a controlled task-family design with the outcome fixed outside the system, defers long-horizon accumulation, and quotes the three adopted whole-program hypotheses with their refuters. No run has been performed.
- [Bootstrapping a Fully Automated Learner with Commonplace](./bootstrapping-an-autonomous-theory-builder.md) — develops the lead's first arrangement. A fully automated learner need not be built in one step: start from a partially automated system in which operator and machinery learn together, retain what is learned in the system, apply it reflectively to the learning machinery, let the learner build the software that operationalizes its knowledge, and move functions from the operator to that machinery one at a time with the residue recorded. Commonplace is the implementation.
- [An Automated Software House as a Second Test of Conjectural Learning](./an-automated-software-house-as-a-second-test-of-conjectural-learning.md) — currently a rewrite plan, not an article. The replacement will state the software-house conjecture as adopted, why a house that revises its program theory is a conjectural learner, why software supplies a stronger falsifier than a knowledge base at the price of a harder claim, and the four conditions a witness must meet. It stays a companion arrangement. The superseded draft stays in git history.
- [How existing self-improving systems relate to conjectural learning](./nearest-existing-constructions-to-a-witness-house.md) — work in progress. Eighteen systems sorted by how what they retain is admitted: by people, by a score or oracle or gate, by versioning alone, or by a supplied model. The parts of a conjectural learner have precedents; in the reviewed evidence no system tests its mechanism, a retained explanation guiding a later decision it did not state and criticism of the explanation improving later ones. It says what one reviewed run would have to show.

One draft stands outside the series:

- [What an Automated Reviewer Should Measure](./what-an-automated-reviewer-should-measure.md) — a proposal for automated review of explanatory articles, especially theory revisions. The reviewer assesses *explanatory reach* and *explanatory economy*, relative to a declared reader's prior account, as evidence of compression progress: capturing more of a domain's structure, or the same structure more simply. It gives the reviewer's procedure: recover five parts of a revision, derive consequences beyond the motivating cases, check them, and record the extra assumptions each extension needed. That leaves two claims to test separately: whether the assessment tracks compression progress, measured by predictive coding where that is feasible, and whether that progress improves the reader's performance on relevant tasks. A favourable assessment does not certify an article's evidence or reasoning. Nothing in it has been run.

## Superseded

Nine earlier drafts have been withdrawn. Each address redirects to the draft
that absorbed it: the three earliest software-house drafts to the
software-house supplement, the lead, and the testing supplement; *The
decisions that stay human, and what would move them* to the bootstrap
supplement, whose ordering principle its selection argument became; and
*The Bitter Lesson does not require everything to live in weights* to the
lead, which carries its rebuttal as a section.

---

Authoring and publication conventions live in [COLLECTION.md](./COLLECTION.md); [ADR 057](../reference/adr/057-articles-use-an-editorial-profile-and-excluded-drafts.md) records the design.
