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
The slides show the terminology changes with strikeouts. An [alternate
hosted copy](https://claude.ai/code/artifact/1b676774-3fa9-4539-a05e-023f25a747a6)
is also available.

## In draft

Five drafts make one series: a lead article and four supplements. The lead
states the idea and stands on its own. Each supplement develops one part of
it, so read the lead first and then whichever supplement answers your next
question. Nothing in the series reports a result; no test has been run.

- [Learning by Theory Refinement with Fixed Models: A research program for systems that learn outside their weights](./learning-by-theory-refinement-with-fixed-models.md) — the lead. It proposes a learning paradigm for systems built around large language models: let the system learn by refining written theories that it retains outside the model and consults on later work, with weights held fixed for the study. It works through one case, says how this departs from classical theory refinement, argues that the Bitter Lesson does not rule it out, and states three conjectured attractions: learning is continual, it may need fewer observations, and learned parts can be inspected and candidates for rollback identified along with their dependencies. The system that carries the paradigm, the hypotheses that would test it, and the system proposed for the first test appear in outline, each pointing to a supplement.

The supplements, in the order a reader is likely to want them:

- [How the Theory-Refinement Program Would Be Tested](./testing-the-theory-refinement-program.md) — develops the lead's testing section. It defines the system under test, states the three hypotheses with what would refute each, says what has to come from outside that system for outcomes to be comparable, gives the shape of the first protocol, and specifies component experiments that can run before a whole system exists. It is a first design that needs much more testing before a scored run.
- [Bootstrapping an Autonomous Theory Builder](./bootstrapping-an-autonomous-theory-builder.md) — develops the lead's first arrangement. It takes Commonplace as a human-staffed starting point and transfers internal decisions to computation one bounded class at a time, testing separately whether computation now makes each decision and whether the system learns to revise the machinery that makes it. It has readiness and stop conditions and one worked trial; the program beyond that trial is still a sketch.
- [An Automated Software House as a Second Test of Theory Refinement](./an-automated-software-house-as-a-second-test-of-theory-refinement.md) — develops the alternative arrangement the lead mentions. A software house that learns by refining Naur's program theory would give the paradigm a stronger falsifier than a knowledge base does, at the price of a harder claim. It keeps the conjecture, the argument that Naur does not rule it out, the four conditions a witness house must meet, and a comparison of the two arrangements.
- [Nearest existing constructions to a witness house](./nearest-existing-constructions-to-a-witness-house.md) — the survey behind two claims in the series: that the paradigm's parts have precedents, and that no existing system meets the software-house supplement's four conditions together. It grades eighteen constructions against those conditions, with evidence links, and closes on what the survey shows for the paradigm: the reviewed evidence does not test its central mechanism, a retained explanation guiding later decisions.

One draft stands outside the series:

- [What an Automated Reviewer Should Measure](./what-an-automated-reviewer-should-measure.md) — a proposal for automated article review. It scores an article by how much it improves a declared model reader's answers to independently written questions, per token, and pairs that measurement with a five-part reading of the text as an untested proxy. It says how a venue could declare the reader for a scientific literature, and it rates value, not correctness. Nothing in it has been run.

## Superseded

These drafts stay at their addresses so that existing links resolve. Each
opens with a banner naming its successor and is no longer maintained.

- [The Automated Software House Conjecture](./automated-software-houses-with-fixed-llms.md) — replaced by the software-house supplement above.
- [The Automated Software House as the Unit of Training](./the-software-house-as-the-unit-of-training.md) — replaced by the lead, with its experiments now in the testing supplement.
- [Transition closure and continuation reliability](./transition-closure-and-continuation-reliability.md) — its path definition, continuation reliability, and Gödel-machine comparison now form a section of the testing supplement, stated for any system and without the formal notation.

Six earlier companion drafts were withdrawn; their addresses redirect to the
draft that absorbed each one, which in some cases is now one of the
superseded drafts above. The two most recent were *The decisions that
stay human, and what would move them*, whose selection argument is now the
ordering principle of the bootstrap supplement, and *The Bitter Lesson does
not require everything to live in weights*, whose rebuttal is now a section
of the lead.

---

Authoring and publication conventions live in [COLLECTION.md](./COLLECTION.md); [ADR 057](../reference/adr/057-articles-use-an-editorial-profile-and-excluded-drafts.md) records the design.
