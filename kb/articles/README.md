# Articles

Writing from the Commonplace knowledge base for readers outside the project — researchers and builders of agent and knowledge systems. Each article stands on its own, carries a byline and lifecycle status, and links into the KB it was distilled from.

Articles circulate in three states. A draft may change without notice and carries a visible banner inviting comments. A working paper is revisable on the record: its claims are still open, it carries a version and a revision date, and it invites counterexamples. A published article is frozen — corrections appear as dated annotations or superseding articles, never as silent rewrites.

## Working papers

Nothing circulating yet.

## Published

Nothing published yet.

## Presentations

- [Where It Lives Is Not What It Is — ASISAS 2026 slides](./asisas-2026-talk.html) — HTML deck prepared for a 10-minute talk and 2 minutes of questions, based on the [June 23 position paper](../sources/where-it-lives-retained-adaptation-2026-06-23.ingest.md). Use arrow keys, space, or click to navigate.

The paper is published as Zbigniew Łukasiak, ["Where It Lives Is Not What It Is: An Architectural Vocabulary for Retained Adaptation in Agentic Systems"](https://link.springer.com/chapter/10.1007/978-3-032-39143-8_24), in *Software Architecture. ECSA 2026 Tracks and Workshops*, Lecture Notes in Computer Science, Springer, 2026, pp. 286–295, doi:[10.1007/978-3-032-39143-8_24](https://doi.org/10.1007/978-3-032-39143-8_24).

The deck uses *memory* for the audience-facing term and *natural-language*
in place of the paper's *prose*. It derives the three representational forms
from assigned consequences and localization; the terminology and derivation
are explained in [representational form](../notes/definitions/representational-form.md).
The slides show the terminology changes with strikeouts.

## In draft

Five drafts make one series: a lead article and four supplements. The lead
states the idea and stands on its own. Each supplement develops one part of
it, so read the lead first and then whichever supplement answers your next
question. The series proposes Commonplace's experiments; it reports no
completed experimental result from that program. The survey discusses results
reported by other systems.

- [Building a Theory Builder from Today's LLMs](./building-a-theory-builder-from-todays-llms.md) — the lead. It introduces the theory builder, a system that runs Popper's cycle of problem, tentative solution, error elimination, and revised problem over explicit theories, defined by four conditions: stated theories, acted on, criticized for what they say, with the result shaping the next conjecture. It states the bet that a fully automated theory builder that learns can be built with today's fixed-weight LLMs, argues that an LLM can apply precise definitions where formal proof cannot reach, gives the payoffs and costs of explicit learned state and three conjectured advantages, argues compatibility with the Bitter Lesson, and states the two-part test that would count as learning. Testing, bootstrapping from Commonplace, the software-house arrangement, and the survey each point to a supplement.

The supplements, in the order a reader is likely to want them:

- [Testing Whether a Theory Builder Learns](./testing-whether-a-theory-builder-learns.md) — sets a modest first testing goal: show under controlled conditions that retained revisions causally improve later capacity and stay revisable. Gives seven tests that expose the causal role of retained state (retention, use, withholding, perturbation, reconstruction, transfer, revision), separates task success from learning, sketches controlled task families in which the revised builder is run against its declared seed on fresh instances whose answers are fixed outside it, with a declared evidence interface and controls, records what people contribute operation by operation, defers long-horizon accumulation and compounding, and quotes the three adopted whole-program hypotheses with their refuters. No run has been performed.
- [Bootstrapping an Autonomous Theory Builder with Commonplace](./bootstrapping-an-autonomous-theory-builder.md) — develops the lead's first arrangement. An autonomous theory builder need not be built in one step: start from a partially automated system in which operator and machinery learn together, retain what is learned in the system, apply it reflectively to the learning machinery, let the builder build the software that operationalizes its knowledge, and move functions from the operator to that machinery one at a time with the residue recorded. Commonplace is the implementation.
- [An Automated Software House as a Second Test of a Theory Builder](./an-automated-software-house-as-a-second-test-of-a-theory-builder.md) — a companion arrangement to the lead's knowledge base. It states the conjecture that an automated software house capable of open-ended coherent change can operate practically with models available by 2026-09-02 and held fixed; argues that a house which states, criticizes, and revises its program theory (Naur's term) is a theory builder, and how that squares with Naur's view that the theory cannot be fully written down; explains why software supplies a stronger falsifier than a knowledge base at the price of a harder claim; and defines four conditions a witness run must meet, each with what would fail it.
- [Which Existing Self-Improving Systems Are Theory Builders](./which-existing-self-improving-systems-are-theory-builders.md) — compares eighteen systems, starting with reported tests of retained knowledge and skill improvement. Places each against the four theory-builder conditions and judges reported learning separately: five builders (two with reported gains, three human-staffed without a measured gain), one outside, and twelve unsettled, mostly because the evidence shows an outcome gate rather than criticism of what a retained unit says; no placement turns on how far results persist. Then proposes comparisons that would settle the placements and isolate what criticism contributes.

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
