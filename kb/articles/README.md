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
are explained in [representational form](../theory/definitions/representational-form.md).
The slides show the terminology changes with strikeouts.

## In draft

- [Deployment-Time Machine Learning: LLM-Selected Updates Without a Single Score](./deployment-time-machine-learning-llm-selected-updates.md) — asks whether a deployed agent can use an LLM to select revisions to its own instructions without a single score. It distinguishes the decision to try an edit from evidence that the edit improved later work. No end-to-end automated run is reported.
- [Testing Autonomous Selection-Based Learning](./testing-autonomous-selection-based-learning.md) — the research program companion to the lead. It separates human-assisted membership, whether a particular edit improved the system, and autonomous fixed-weight model judgment; sets out discriminating comparisons for admission, targeted correction, criterion revision, and whole-loop net gain; proposes a first experiment repairing a misleading routing check; and records the current evidence and scoped rival predictions. It links the earlier [testing supplement](./testing-whether-a-theory-builder-learns.md) for additional experimental designs while that supplement awaits re-anchoring on selection-based learning.
- [Bootstrapping Autonomous Selection-Based Learning with Commonplace](./bootstrapping-autonomous-selection-based-learning.md) — how Commonplace builds toward the lead's automated loop. What it builds is a reflective self-improver that learns by selection. It starts human-assisted, with an operator inside the boundary making many update decisions; it retains selected updates, lets the system build the software its method needs, and moves decisions to computation one kind at a time, by codifying them or delegating them to an LLM, recording what stays with the operator. Progress is judged by the kinds of update that still complete when the operator's decisions are withheld; whether those updates improve later work is left to the testing article. No decision transfer has been tested this way yet.
- [What an Automated Reviewer Should Measure](./what-an-automated-reviewer-should-measure.md) — a proposal for automated review of explanatory articles, especially theory revisions. The reviewer assesses *explanatory reach* and *explanatory economy*, relative to a declared reader's prior account, as evidence of compression progress: capturing more of a domain's structure, or the same structure more simply. It gives the reviewer's procedure: recover five parts of a revision, derive consequences beyond the motivating cases, check them, and record the extra assumptions each extension needed. That leaves two claims to test separately: whether the assessment tracks compression progress, measured by predictive coding where that is feasible, and whether that progress improves the reader's performance on relevant tasks. A favourable assessment does not certify an article's evidence or reasoning. Nothing in it has been run.

- [What Does a Learning System Gain by Retaining a Theory Rather Than Just the Fix?](./what-does-a-learning-system-gain-by-retaining-a-theory.md) — uses a build failure to distinguish three possible benefits: a diagnosis can guide search, a faulty premise can be revised separately, and a tested explanation can save work on the next job.

### Earlier drafts awaiting rewriting

Four earlier drafts remain from one series: a lead article and three
supplements. They were written before
[selection-based learning](../theory/definitions/selection-based-learning.md) was
defined, and they state their claims in terms of the theory builder. The
series' bootstrapping supplement has been rewritten and is listed above. Two
of the remaining drafts need rewriting:

- **The earlier lead** carried the definition of learning and the argument
  for the theory builder at once. The new lead replaces it. What the theory
  builder adds is to be worked out again as a narrower piece.
- **The software house supplement** rests on the argument that a house which
  states and criticizes its program theory is a theory builder.

The testing and survey supplements still use the theory builder's
vocabulary and are to be re-anchored on selection-based learning. The
series proposes Commonplace's experiments; it reports no completed
experimental result from that program. The survey discusses results reported
by other systems.


The supplements, in the order a reader is likely to want them:

- [Testing Whether a Theory Builder Learns](./testing-whether-a-theory-builder-learns.md) — sets a modest first testing goal: show under controlled conditions that retained revisions causally improve later capacity and stay revisable. Gives seven tests that expose the causal role of retained state (retention, use, withholding, perturbation, reconstruction, transfer, revision), separates task success from learning, sketches controlled task families in which the revised builder is run against its declared seed on fresh instances whose answers are fixed outside it, with a declared evidence interface and controls, records what people contribute operation by operation, defers long-horizon accumulation and compounding, and quotes the three adopted whole-program hypotheses with their refuters. No run has been performed.
- [An Automated Software House as a Second Test of a Theory Builder](./an-automated-software-house-as-a-second-test-of-a-theory-builder.md) — to be rewritten. A companion arrangement to the lead's knowledge base. It states the conjecture that an automated software house capable of open-ended coherent change can operate practically with models available by 2026-09-02 and held fixed; argues that a house which states, criticizes, and revises its program theory (Naur's term) is a theory builder, and how that squares with Naur's view that the theory cannot be fully written down; explains why software supplies a stronger falsifier than a knowledge base at the price of a harder claim; and defines four conditions a witness run must meet, each with what would fail it.
- [Which Existing Self-Improving Systems Are Theory Builders](./which-existing-self-improving-systems-are-theory-builders.md) — historical draft comparison of eighteen systems, starting with reported tests of retained knowledge and skill improvement. Places each against the four theory-builder conditions and judges reported learning separately: five builders (two with reported gains, three human-staffed without a measured gain), one outside, and twelve unsettled, mostly because the evidence shows an outcome gate rather than criticism of what a retained unit says; no placement turns on how far results persist. Then proposes comparisons that would settle the placements and isolate what criticism contributes.

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
