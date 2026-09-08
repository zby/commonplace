# Articles

Writing from the Commonplace knowledge base for readers outside the project — researchers and builders of agent and knowledge systems. Each article stands on its own, carries a byline and lifecycle status, and links into the KB it was distilled from.

Articles circulate in three states. A draft may change without notice and carries a visible banner inviting comments. A working paper is revisable on the record: its claims are still open, it carries a version and a revision date, and it invites counterexamples. A published article is frozen — corrections appear as dated annotations or superseding articles, never as silent rewrites.

## Working papers

Nothing circulating yet.

## Published

Nothing published yet.

## In draft

Five drafts comprise three main articles and two supplements. The three main
articles play different roles: the first sets the stage for the second, the
second makes the central proposal, and the third describes Commonplace's
attempt to reach it. Read them in that order, or start with the second if time
is short and go back to the first when a term or condition needs its source.

- [The Automated Software House Conjecture: Open-ended software development with fixed LLMs](./automated-software-houses-with-fixed-llms.md) — sets the stage for the second article. It fixes the terms the proposal is stated in: the software house as the system boundary and program theory as the capacity under test. It states the four conditions a concrete witness house must meet, which the third article and the comparison supplement take as their acceptance criteria. And it argues that the target is not ruled out in advance: Naur's claim that program theory belongs only to people rests on an extra premise, and existing constructions already show parts of the conjecture working, though none shows all four conditions together.
- [The Automated Software House as the Unit of Training: A fixed-model training regime for theory refinement](./the-software-house-as-the-unit-of-training.md) — the central article. It proposes classical theory refinement as the training regime of a software house: the program theory is refined from production consequences and guides later production, while every weight stays fixed. Three things are new: the theory is partly normative, so a failure may be fixed by changing the product to fit it; among revisions that fit the evidence, those with more explanatory reach are preferred; and the refinement machinery is itself revisable. LLMs are the enabling condition, not the claim. The article argues Bitter Lesson compatibility, since computation produces the retained structure, and states the hypotheses that would test the regime against weight adaptation. Its attractions, each still a conjecture: learning is continual, because what is learned is usable at the next request and a contradicting fact forces only a local reconciliation; adaptation may need fewer observations, because a correct theory says which cases matter; and the substrate is legible, so one assumption or test can be inspected and rolled back on its own.
- [Bootstrapping the First Automated Software House: A research program from human-agent production to human-free internal operation](./bootstrapping-the-first-automated-software-house.md) — the attempt. It takes Commonplace as a human-agent seed and transfers production decisions to computation one bounded class at a time, testing separately whether computation now makes each decision and whether the house learns to revise the machinery that makes it. This is the least developed of the three: it has readiness and stop conditions and one worked component trial, but the program beyond that first trial is still a sketch.

The supplements develop two parts of the conjecture:

- [Nearest existing constructions to a witness house](./nearest-existing-constructions-to-a-witness-house.md) — a selective comparison of eighteen constructions against the four conditions, with evidence links and a separate test of explicit project theory.
- [Transition closure and continuation reliability](./transition-closure-and-continuation-reliability.md) — permitted paths from a seed, continuation reliability as the measure of sustained adequacy, and the Gödel-machine comparison.

Six former companion drafts were withdrawn; their addresses redirect to the
draft that absorbed each one. The two most recent were *The decisions that
stay human, and what would move them*, whose selection argument is now the
ordering principle of the third draft, and *The Bitter Lesson does not require
everything to live in weights*, whose rebuttal is a section of the second
draft and whose account of the Commonplace strategy is the third.

---

Authoring and publication conventions live in [COLLECTION.md](./COLLECTION.md); [ADR 057](../reference/adr/057-articles-use-an-editorial-profile-and-excluded-drafts.md) records the design.
