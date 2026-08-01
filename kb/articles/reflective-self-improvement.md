---
description: "Examples-first article defining reflective self-improvement, benefits and failure boundaries of readable self-representation, migration of reflective control into computational processes, a five-question test, and the bitter-lesson constraint"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/definitions/self-improving-system.md
  - kb/notes/definitions/reflective-system.md
  - kb/notes/definitions/reach-assessment.md
  - kb/notes/reflection-buys-addressability.md
  - kb/notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md
  - kb/notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md
  - kb/notes/retrieval-failure-is-reflection-failure.md
  - kb/notes/first-principles-reasoning-selects-for-explanatory-reach-over.md
  - kb/notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md
  - kb/notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md
  - kb/notes/methodological-and-computational-closure-track-different-changes.md
  - kb/notes/computationally-directed-self-improvement-is-a-reallocation.md
  - kb/notes/self-improvement-compounds-through-reflective-leverage-not-autonomy.md
  - kb/notes/a-proximate-target-is-checked-for-achievement-not-for-warrant.md
  - kb/notes/self-improvement-is-relative-to-a-declared-objective.md
  - kb/notes/warranted-autonomy-is-bounded-by-oracle-domain.md
  - kb/notes/exact-implementation-does-not-validate-a-requirement.md
  - kb/notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md
  - kb/notes/commitment-not-derivation-creates-new-ground-truth.md
  - kb/notes/a-consumption-channel-delivers-force-without-the-history-that.md
  - kb/notes/parametric-reproduction-cannot-replace-an-authoritative-record.md
  - kb/notes/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md
  - kb/notes/the-bitter-lesson-selects-production-methods-not-representational.md
  - kb/notes/the-bitter-lesson-defense-portfolio-has-one-load-bearing-member.md
  - kb/reference/commonplace-as-a-reflective-system.md
  - kb/reference/tag-readme-trace-observed-causal-connection.md
  - kb/agentic-systems/exo.md
  - kb/sources/knowledge-centric-self-improvement-2607.19592.ingest.md
  - kb/sources/sutton-the-bitter-lesson-original-essay.md
---

# Reflective self-improvement

An agent that is corrected today and repeats the mistake tomorrow wastes the correction. The obvious fix is retention: let the agent write down what it learned, somewhere later runs will read it. This article is about what that fix opens up: a pathway by which an agent changes itself through readable artifacts. The pathway's main benefit is addressability; its hard parts are retrieval, verification, and control over what gets written.

Suppose a deployment fails on a Tuesday because a credential expired. An agent reviewing the trace mistakes the date for the cause and records a standing rule: "Deployments fail on Tuesdays." Later runs consume the rule and avoid Tuesday deployments. The agent has learned from evidence, and it has made itself worse.

An agent does not need to change its model weights to change itself. Prompts and instruction files, retained memories, tests, validators, and scaffolding code all steer later runs, and an LLM agent can read those artifacts, criticize them, and rewrite them. Software that acts on [such a representation of itself](../notes/definitions/reflective-system.md) is computationally reflective — reflection in the computational sense, not simply a model reviewing its mistakes. When evidence bearing on [an objective specified independently of the change](../notes/self-improvement-is-relative-to-a-declared-objective.md) leads such a system to make an [operative change to its own organization](../notes/definitions/self-improving-system.md) through that representation, the pathway is **reflective self-improvement**. The Tuesday agent ran this pathway; what it lacked was any point at which the false lesson could be caught.

A real trace shows the pathway running with those catch points in place. [Commonplace](../index.md), the knowledge-base system that holds this article, had a `learning-theory` index with two jobs: introduce the topic and list every note carrying that tag. The page had to stay short because agents load it into a limited context, and once the notes grew past fifty entries the index was too large to verify by hand — its claim of completeness could no longer be trusted. A maintainer noticed the problem; a recorded decision split the two jobs and introduced machine-checked coverage marks with size limits. While applying the new check, the validator found a note that the documented text-search recipe had missed because of its metadata layout, and the recipe was corrected to parse the metadata instead. The objectives existed before the repair — keep navigation within a context budget, do not mislead a reader who trusts a complete index — and the pages, checks, and recipes that changed were part of the system's operative definition. The [commit history records the chain](../reference/tag-readme-trace-observed-causal-connection.md). Unlike the Tuesday rule, every step was governed: a maintainer diagnosed, an agent drafted, automation enforced. Outcome evidence still decides whether the adopted change actually helped.

An artifact does not become a self-representation just because later behavior depends on it. The Tuesday rule is a claim about deployments that happens to steer behavior; the index pages and validation recipes describe how the system itself routes and checks its work, and they sit on the causal path by which it does so. The subject here is that narrower case, where readable artifacts are both a representation of the system and part of the machinery being revised. Systems of this kind, Commonplace included, often generate candidate changes and select among them, but the definition does not require that loop — a direct evidence-driven update to operative artifacts also qualifies.

The machinery is not what makes such a system special. An agentic software factory already has repositories, tests, review, issue tracking, and deployment loops; applied to an external product, those mechanisms improve the product. Applied to representations of the factory's own operation — its prompts, workflows, evaluators, retrieval rules, schemas — they open a feedback loop, because an accepted change can improve the machinery that produces later changes: better retrieval helps agents diagnose the next failure, a better evaluator improves the next selection, a retained lesson about a recurring error reduces the next round of correction. An improvement of that kind carries [reflective leverage](../notes/self-improvement-compounds-through-reflective-leverage-not-autonomy.md), and the loop compounds through the fraction of accepted changes that carry it — not through the fraction of the workflow that runs unattended.

One consequence of the definition is better granted up front than argued over: include the maintainers in the declared boundary and reflective self-improvement is close to ubiquitous in software engineering — a maintainer who reads a failure trace, interprets it through the system's source, and lands a fix has run the entire pathway. Membership is cheap, and this article does not defend it. The question worth pursuing begins after membership: how the pathway's decision-bearing functions — noticing, diagnosis, choice of change, acceptance — [migrate from human actors into computational processes](../notes/computationally-directed-self-improvement-is-a-reallocation.md), and how far that migration can go while the accepted changes remain adequately verified. LLMs bear on this precisely because they change which kinds of functions can move: earlier automation internalized execution — builds, tests, optimization — while a model can plausibly take over diagnosis, explanation, candidate generation, and the editing of the representations themselves. Reflection creates the feedback loop; autonomy determines where the loop is executed. The program, in one sentence, is the progressive computational internalization of reflective control while preserving warranted improvement, and the benefits, failure points, and governance machinery below all serve it.

## What readable artifacts buy

A self-hosting compiler supplies the basic causal pattern: its source is written in the language it compiles, and the resulting compiler runs the next build. Humans diagnose compiler problems, devise revisions, and choose what to adopt. An LLM agent can perform some of those roles itself, and accepted operative revisions affect later runs without changing the model's weights.

Suppose an agent records a rule: "always pin the dependency versions." As a note, the lesson carries a scope and a rationale, and it can be inspected, revised, or retired individually. Weight changes can be rolled back, trained over, and even targeted through [model editing](https://arxiv.org/abs/2202.05262), but those interventions do not expose the lesson itself as a readable object. This is the first benefit, direct [addressability](../notes/reflection-buys-addressability.md): a retained lesson is a separable object that can be named, criticized, rescoped, and deleted.

The second benefit is legibility: the operative content can be read directly, not only exercised. Weight changes can also carry rationales, logs, and evaluations, but the operative content itself stays behind behavior. Legibility enables addressability without guaranteeing it — a long unindexed instruction log is readable in principle yet unaddressable in operation.

Now suppose a login test fails intermittently because it reads the real clock. An agent could retain either "retry the flaky login test" or "tests that read the wall clock flake, so freeze the clock." The first is a local lesson: it helps with one test. The second explains the failure and can prevent the same problem in tests that have not been written yet. The third benefit is conjectural: [sample efficiency](../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md). An explanation that survives such a task shift may adapt the system from fewer observations of the new situation than retraining or fine-tuning would require. The conjecture concerns those target observations only; finding, evaluating, and maintaining the explanation still costs compute, tokens, and judgment.

## Retrieval failure is reflection failure

A compiler consumes its declared source set. Stored notes or memories affect an agent run only if they are retrieved: a note that would have prevented today's mistake has no effect on a run that never finds it. In a retrieval-mediated system, [failing to retrieve the relevant self-representation is a failure of the reflective pathway itself](../notes/retrieval-failure-is-reflection-failure.md), not a performance detail. Executed code and directly supplied instructions enter a run through other channels; retained knowledge depends on maintained indexes and search to enter at all.

## A writable self-representation is an attack surface

The Tuesday case shows the write-side risk: [a consumption channel delivers behavioral force without the history that produced the content](../notes/a-consumption-channel-delivers-force-without-the-history-that.md). An untrusted tool result can exploit the same path by telling the agent to save a directive — the origins differ, but anything allowed to write into the instruction path can modify the system. Provenance, write authority, review, and rollback are the controls that path needs.

The read side needs verification the loop cannot supply for itself. A self-hosting compiler has a limited fixed-point check: build a new compiler with the existing one, then rebuild from the same source with the new one; if the build is deterministic, differing outputs show the bootstrap has not converged. Ken Thompson [showed](https://dl.acm.org/doi/10.1145/358198.358210) that a corrupted compiler can reproduce its corruption through both builds, so even matching outputs never proved soundness. There is no general equivalent for deciding whether a rewritten instruction is better, and an agent may judge a revision through the very instructions being revised. Reflection needs verification that reflection itself does not supply.

A reflective agent therefore needs controls that do not share all the failure modes of the process that produced a candidate. In Commonplace, [typed artifacts](../notes/why-notes-have-types.md) declare the contract under which an artifact is interpreted, checked, and retrieved. Mechanically decidable rules run as code. Semantic [review gates](../reference/README-REVIEW-SYSTEM.md) assess a candidate against a fixed criterion in a fresh context rather than continuing the conversation that produced it; the fresh context removes the generation trajectory, though the reviewing model can still share the generator's blind spots.

Guarding writes does not decide what is worth retaining. For reusable explanatory claims, Commonplace makes [explanatory reach](../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md) an explicit review target: explaining why something works can support its application beyond the episode that produced it. The supporting episodes remain with the theory so later evidence can overturn it, and review tests [whether the claimed reach is genuine](../notes/definitions/reach-assessment.md) — though whether LLM-mediated review can assess reach reliably is itself an open question. Other artifacts, such as commitments and procedures, have different contracts.

## Existing systems cover parts of the loop

- [Reflexion](https://arxiv.org/abs/2303.11366) retains natural-language lessons for retries of the current task, but not as durable, governed objects.
- [Voyager](https://arxiv.org/abs/2305.16291) retains durable executable skills, while the instructions and scaffolding that run the loop remain outside the improvement target.
- [Promptbreeder](https://arxiv.org/abs/2309.16797) changes steering text through mutation and benchmark selection, but a surviving prompt carries no maintained rationale to inspect or revise.
- [STOP](https://arxiv.org/abs/2310.02304) and the [Darwin Gödel Machine](https://arxiv.org/abs/2505.22954) rewrite scaffolding code, but their benchmark-based evaluation can assess only effects the benchmark measures.
- The original [Gödel machine proposal](../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md) adopts a self-rewrite only after proving from its axioms that switching now has greater expected utility than continuing the search. Changes it cannot prove beneficial remain out of reach.

These systems either retain changes without a governance layer or evaluate them through a narrow channel. The pattern proposed here keeps an artifact layer representing selected aspects of the system in natural language and code, then uses LLMs to propose and criticize changes. Natural-language criticism can consider effects that a proof system cannot establish or a fixed benchmark does not measure, but its judgments need verification outside the text being judged.

The claim, then, is not that systems can reflect, retain lessons, or rewrite themselves — the list above shows they can. It is that an LLM plus a readable artifact layer can serve as an operative reflective surface, that addressability is that surface's distinctive benefit, and that retrieval, reach assessment, and control over write and consumption paths are its characteristic failure points.

The closest comparison is the [reviewed Exo version](../agentic-systems/exo.md), pinned to commit `ef4cfe05` from 2026-07-29: an agent harness and memory system that can change both natural-language and executable artifacts, keeps event history and versioned artifacts, supports deliberate removal, structurally validates installed tools, and blocks activation when validation or a rebuild fails. Its weaker point is semantic governance: individual memory facts lack declared scope, provenance, and review state, and making a candidate memory durable requires no independent semantic review. Commonplace begins with that governance problem and provides far fewer runtime capabilities.

## The bitter lesson concerns production, not form

Commonplace currently relies on hand-designed artifacts: types, link rules, review criteria, and validators. [The bitter lesson](../sources/sutton-the-bitter-lesson-original-essay.md) warns that methods built around human knowledge tend to lose to methods that use increasing computation through search and learning — computer-vision systems built on human-designed features were displaced by systems that learned features from data. Commonplace's types and gates may likewise help now and still become a ceiling. Must prompts, code, and knowledge bases disappear into model weights?

The relevant distinction is between how useful structure is produced and the form in which it is retained. Search and learning are production methods; natural language, code, and model weights are representational forms. A system could search over theories, instructions, tests, schemas, and programs, evaluate the candidates, and retain selected artifacts for later use and revision. Those artifacts would be products of learning rather than fixed knowledge supplied by designers, and their textual or symbolic form would not by itself conflict with [the bitter lesson](../notes/the-bitter-lesson-selects-production-methods-not-representational.md).

Commonplace does not yet implement such a learned search loop. Humans still supply most of the diagnosis and the acceptance, with agents and automated checks assisting, and the human-assisted loop is a bootstrap: it discovers candidate representations and candidate checks for a later search-and-learning loop to use. The deeper conjecture is that the bootstrap compounds — if enough accepted changes carry reflective leverage, the road to a more autonomous loop is itself a self-improving process. Whether search over a large, interdependent artifact corpus scales remains an empirical question, and its hard core is credit assignment without a chain rule: when an artifact-mediated system fails, the failure rarely identifies which of many interacting instructions, theories, schemas, or checks should change.

Some information also requires an authoritative current record regardless of model strength. "Retry with backoff" is general knowledge a stronger model may reliably supply. "This deployment retries with backoff, adopted after the March incident and owned by the platform team" records a [current commitment](../notes/commitment-not-derivation-creates-new-ground-truth.md); a model may reproduce the sentence, but [reproduction alone does not establish](../notes/parametric-reproduction-cannot-replace-an-authoritative-record.md) that the commitment is still operative, who authorized it, or what evidence now supports it. The record can use any representation that preserves currentness, attribution, and authorized revision.

## Use tests the structure

The production-method distinction leaves Commonplace's current types, gates, and indexes to be tested through use. One working bet is that explanation-first selection produces useful, well-supported knowledge per unit of human judgment. Review can [assess an individual explanation's reach, while use must show whether the method earns its maintenance cost](../notes/a-proximate-target-is-checked-for-achievement-not-for-warrant.md).

The opening index episode is one such observation. The [division of work](../notes/methodological-and-computational-closure-track-different-changes.md) was explicit, and because [Commonplace's declared boundary](../reference/commonplace-as-a-reflective-system.md) includes designated maintainers, the loop was human-inclusive: it demonstrates an inspectable causal pathway, not autonomous diagnosis. It also locates Commonplace on the migration the introduction named — noticing and acceptance human, drafting computational, enforcement mechanical. And both accepted changes carried reflective leverage: the coverage check strengthens future verification, the corrected recipe future retrieval, so the episode improved the loop that will run the next episode. The endpoint of the migration is not "an LLM wrote the code": production can be almost entirely computational while every improvement-directing decision stays human. It is reached when removing the maintainer from an episode would no longer break the loop — when the system itself uses evidence and a representation of itself to determine what should change.

A passing gate shows that its criterion was met; the criterion may still be [a poor proxy for the intended capability](../notes/exact-implementation-does-not-validate-a-requirement.md). Use tests how the parts work together: missed retrievals, misleading indexes, recurring corrections, and manual workarounds all count, because workarounds consume the human judgment the system is meant to spare.

A successful use shows that [the current division of work among artifacts, indexes, checks, agents, and maintainers sufficed in that context](../notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md); transfer requires more, and the rationale retained with each design choice is itself a hypothesis that varied use tests. Self-use therefore guards against ossification: it exposes hand-designed structure to evidence and supplies reasons to revise or remove it, which is the empirical burden the bitter lesson raises. Moving an adoption decision to an automated check changes who decides, and counts as improvement only when the [check is reliable enough for what is at stake](../notes/warranted-autonomy-is-bounded-by-oracle-domain.md).

A [July 2026 preprint](https://arxiv.org/abs/2607.19592) reports that a frozen, curated task-knowledge artifact — delivered to the solver through a task-conditioned adapter — improved solve rates on held-out hard tasks the recipient models had initially failed, including across two model families. The system revises task knowledge, not a representation of its own organization, so [the result](../sources/knowledge-centric-self-improvement-2607.19592.ingest.md) supports artifact retention and transfer, not reflective self-improvement.

The loop-level empirical question is whether the human-assisted loop actually exhibits reflective leverage and cumulative improvement, or is merely repeated manual maintenance. The evidence would be earlier accepted changes making later improvement episodes cheaper, broader, more reliable, or less dependent on human judgment — the effect showing up in the next episode's cost, not only in the metric the change was accepted against. The broader question is whether an evolving, addressable artifact layer improves a declared objective — such as adaptation speed, reliability, or governance quality — compared with stronger base models and simpler memory systems. A fair test compares those baselines as corpus size and model strength change, while counting evaluation, maintenance, and human judgment.

## The reflective self-improvement test

Before calling a system — your own or a published one — reflectively self-improving, ask five questions:

> 1. What system boundary is being assessed, over what horizon, and which of its own instructions, code, memory, or other behavior-shaping structures does the self-representation cover?
> 2. What independently specifiable objective does the evidence bear on?
> 3. Does evidence update the operative artifacts directly, or by generating candidate changes and selecting among them?
> 4. If candidates are generated: what produces them, and where can the loop reject one?
> 5. Which artifact carries an accepted change into later runs, and how reliably do those runs consume it?

The first two questions establish the self-reference and evidence-responsiveness that make the pathway reflective and self-improving. The last two apply to the proposal-selection case, where they name the loop's [search, evaluation, and retention functions](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md). Applied to the Tuesday agent: the rule did reach the operative instructions (question five), but no outcome evidence was ever consulted (question two) and nothing could reject it (question four).

## What this article claims

| Status | Claim |
|---|---|
| Observed | Commonplace revised index pages, validation, and a search recipe through a governed, human-inclusive loop, and later runs consume the changes. |
| Argued | Under a human-inclusive boundary, membership is nearly ubiquitous in maintained software; the substantive variable is which decision-bearing functions humans still supply. |
| Argued | Readable operative artifacts provide addressability — selective inspection, revision, and removal — that weight-retained lessons do not expose. |
| Conjectured | Explanatory artifacts may adapt a system from fewer target observations under structured task shifts. |
| Conjectured | With a sufficient fraction of leveraged changes, a partially automated reflective loop bootstraps its own improvement machinery — later improvements become cheaper and less dependent on human judgment. |
| Open | Whether retrieval, semantic evaluation, credit assignment, and maintenance scale over a large, interdependent artifact corpus. |

## Where to go next

The Tuesday rule is worth keeping in view because it sets the real question. It is not whether the agent learned — it did. It is whether the loop could tell a causal lesson from a coincidence before the coincidence became part of the system.

The [self-improving-systems cluster](../notes/self-improving-systems-README.md) maps the theory behind the five questions, and [the repository](https://github.com/zby/commonplace) contains the framework. If applying the test to a system you build or study produces a counterexample or a disputed boundary case — an agent with editable memory but no independent review, a benchmark-selected prompt that looks like a maintained theory — [open an issue](https://github.com/zby/commonplace/issues).
