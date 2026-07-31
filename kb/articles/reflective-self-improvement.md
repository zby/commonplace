---
description: "Examples-first article defining reflective self-improvement, the benefits and limits of readable self-representation, its verification and use tests, and the bitter-lesson constraint"
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

[Commonplace](../index.md), the knowledge-base system that holds this article, had a `learning-theory` index with two jobs: introduce the topic and list every note carrying that tag. The page also had to stay short because agents load it into a limited context. As that body of notes grew past fifty entries, the index became too large to verify by hand. Its claim of completeness could no longer be trusted.

A maintainer noticed the problem, and a recorded decision split the two jobs and introduced machine-checked marks. The validator checks coverage in either form: every tagged note is linked from the index, or every note with the broad tag also carries at least one listed narrower tag. The decision also set warning and failure limits on page size. While applying the new coverage check, the validator found a note whose multiline YAML tag list had been missed by the documented text-search recipe. The validator parsed the metadata instead of relying on that one textual layout. The recipe was corrected, and the marks now change what validation accepts and which searches an agent needs to run. The [commit history records the chain](../reference/tag-readme-trace-observed-causal-connection.md).

Three smaller hypothetical examples isolate the other parts of the pattern.

Suppose an agent records a rule: "always pin the dependency versions." As a note, the lesson can carry a scope and rationale, and it can be inspected, revised, or retired. Weight changes can be rolled back, trained over, and even targeted through [model editing](https://arxiv.org/abs/2202.05262), but those interventions do not expose the lesson itself as a readable object.

Suppose a login test fails intermittently because it reads the real clock. An agent could retain either "retry the flaky login test" or "tests that read the wall clock flake, so freeze the clock." The first is a local lesson: it helps with one test. The second explains the failure and can prevent the same problem in tests that have not been written yet.

Now suppose a deployment fails on Tuesday because a credential expired. An agent reviewing the trace mistakes the date for the cause and records, "Deployments fail on Tuesdays." The rule is false, but once written into standing instructions it can influence later runs. An untrusted tool result can exploit the same path by telling the agent to save a directive. The origins differ, but anything allowed to write into the instruction path can modify the system.

The dependency rule shows why retained knowledge should be addressable. The wall-clock diagnosis shows why reusable claims should explain the mechanism behind an episode. The Tuesday rule and the tool directive show why every write path should be guarded. The index episode adds self-reference: the pages, checks, and recipes being changed were part of the system's operative definition. When evidence bearing on an objective leads a system to make an operative change to its own organization through such a representation of itself, the pathway is **reflective self-improvement**.

An artifact does not become a self-representation just because later behavior depends on it. The wall-clock lesson is knowledge about tests; the index pages and validation recipes describe how the system itself routes and checks its work, and they sit on the causal path by which it does so. This article is about that narrower case, where readable artifacts are both a representation of the system and part of the machinery being revised. Systems of this kind, Commonplace included, often generate candidate changes and select among them, but the definition does not require that loop — a direct evidence-driven update to operative artifacts also qualifies.

## The pattern

An agent can read the artifacts that steer it: prompts and instruction files supplied to the model, plus scaffolding code such as its harness, tools, and validators. It can interpret those artifacts, criticize them, and propose changes that later runs consume. Software that acts on [such a representation of itself](../notes/definitions/reflective-system.md) is computationally reflective. With LLM agents, part of the interpretation and rewriting can occur inside the system. This is reflection in the computational sense, not simply a model reviewing its mistakes.

A reflective loop has an [improvement-directed pathway](../notes/definitions/self-improving-system.md) when operative changes respond to evidence about an objective [specified independently of those changes](../notes/self-improvement-is-relative-to-a-declared-objective.md). In the index episode, the objectives existed before the repair: keep navigation within a context budget and do not mislead a reader who trusts a complete index. Outcome evidence determines whether the adopted change actually helped.

## Benefits and limits of readable artifacts

A self-hosting compiler supplies the basic causal pattern: its source is written in the language it compiles, and the resulting compiler runs the next build. Humans diagnose compiler problems, devise revisions, and choose what to adopt. An LLM agent can perform some of those roles and propose revisions itself. Accepted operative revisions can then affect later runs without changing the model's weights.

The first benefit is direct [addressability](../notes/reflection-buys-addressability.md). A retained lesson can be inspected, explained, revised, or deleted individually.

The second benefit is legibility: the operative content can be read directly, not only exercised. Weight changes can also carry rationales, logs, and evaluations, but the operative content itself stays behind behavior. Legibility enables addressability without guaranteeing it — a long unindexed instruction log is readable in principle yet unaddressable in operation.

A third conjectured benefit is [sample efficiency](../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md). The wall-clock explanation illustrates the claim: if it captures the cause, it can prevent a failure in a different time-dependent test, while "retry this test" cannot. An explanation that survives such a task shift may adapt the system from fewer observations of the new situation than retraining or fine-tuning would require. The conjecture concerns those target observations only; finding, evaluating, and maintaining the explanation still costs compute, tokens, and judgment.

A compiler consumes its declared source set. Stored notes or memories affect an agent run only if they are retrieved. A note that would have prevented today's mistake has no effect on a run that never finds it. In that setting, [retrieval failure is reflection failure](../notes/retrieval-failure-is-reflection-failure.md). Executed code and directly supplied instructions enter a run through other channels.

A compiler also has a limited fixed-point check. Use the existing compiler to build a new compiler, then use the new compiler to build another from the same source. If the build is deterministic, different outputs show that the bootstrap has not reached a fixed point. Ken Thompson [showed](https://dl.acm.org/doi/10.1145/358198.358210) that a corrupted compiler can reproduce the same corruption in both builds, so matching outputs never proved soundness. There is no general equivalent for deciding whether a rewritten instruction is better. Because an agent may judge a revision through the instructions being revised, reflection needs verification that reflection itself does not supply.

## What the structure must cover

A reflective agent needs controls that do not share all the failure modes of the process that produced a candidate. In Commonplace, [typed artifacts](../notes/why-notes-have-types.md) declare the contract under which an artifact is interpreted, checked, and retrieved. Mechanically decidable rules run as code. Semantic [review gates](../reference/README-REVIEW-SYSTEM.md) assess a candidate against a fixed criterion in a fresh context rather than continuing the conversation that produced it; the fresh context removes the generation trajectory, though the reviewing model can still share the generator's blind spots. Maintained indexes support retrieval.

The Tuesday case shows why [a writable self-representation is an attack surface](../notes/a-consumption-channel-delivers-force-without-the-history-that.md). Provenance, write authority, review, and rollback are controls the instruction path needs.

Guarding writes does not decide what is worth retaining. For reusable explanatory claims, Commonplace makes [explanatory reach](../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md) an explicit review target: explaining why something works can support its application beyond the episode that produced it. The supporting episodes remain with the theory so later evidence can overturn it, and review tests [whether the claimed reach is genuine](../notes/definitions/reach-assessment.md) — though whether LLM-mediated review can assess reach reliably is itself an open question. Other artifacts, such as commitments and procedures, have different contracts.

## Existing systems cover parts of the loop

- [Reflexion](https://arxiv.org/abs/2303.11366) retains natural-language lessons for retries of the current task, but not as durable, governed objects.
- [Voyager](https://arxiv.org/abs/2305.16291) retains durable executable skills, while the instructions and scaffolding that run the loop remain outside the improvement target.
- [Promptbreeder](https://arxiv.org/abs/2309.16797) changes steering text through mutation and benchmark selection, but a surviving prompt carries no maintained rationale to inspect or revise.
- [STOP](https://arxiv.org/abs/2310.02304) and the [Darwin Gödel Machine](https://arxiv.org/abs/2505.22954) rewrite scaffolding code, but their benchmark-based evaluation can assess only effects the benchmark measures.
- The original [Gödel machine proposal](../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md) adopts a self-rewrite only after proving from its axioms that switching now has greater expected utility than continuing the search. Changes it cannot prove beneficial remain out of reach.

These systems either retain changes without a governance layer or evaluate them through a narrow channel. The pattern proposed here keeps an artifact layer representing selected aspects of the system in natural language and code, then uses LLMs to propose and criticize changes. Natural-language criticism can consider effects that a proof system cannot establish or a fixed benchmark does not measure, but its judgments need verification outside the text being judged.

The claim, then, is not that systems can reflect, retain lessons, or rewrite themselves — the list above shows they can. It is that an LLM plus a readable artifact layer can serve as an operative reflective surface, that addressability is that surface's distinctive benefit, and that retrieval, reach assessment, and control over write and consumption paths are its characteristic failure points.

The [reviewed Exo version](../agentic-systems/exo.md), pinned to commit `ef4cfe05` from 2026-07-29, is an agent harness and memory system that can change both natural-language and executable artifacts. It keeps event history and versioned artifacts, supports deliberate removal, structurally validates installed tools, and provides a fixed rebuild tool that blocks activation when validation or a build fails. Its documented adoption practice calls for running relevant tests first. This makes it the closest comparison here.

Exo's weaker point is semantic governance: individual memory facts lack declared scope, provenance, and review state; making a candidate memory durable requires no independent semantic review; and later evidence does not automatically mark stale facts or remove them. Commonplace begins with that governance problem and provides far fewer runtime capabilities.

## The bitter lesson concerns production, not form

Commonplace currently relies on hand-designed artifacts: types, link rules, review criteria, and validators. [The bitter lesson](../sources/sutton-the-bitter-lesson-original-essay.md) warns that methods built around human knowledge tend to lose to methods that use increasing computation through search and learning. Sutton gives computer vision as one example: systems built around human-designed edge, shape, and keypoint features were displaced by deep-learning systems that learned useful features from data. Commonplace's types and gates may likewise help now and still become a ceiling. This history raises a direct question: must prompts, code, and knowledge bases disappear into model weights?

The relevant distinction is between how useful structure is produced and the form in which it is retained. Search and learning are production methods; natural language, code, and model weights are representational forms. A system could search over theories, instructions, tests, schemas, and programs, evaluate the candidates, and retain selected artifacts for later use and revision. Those artifacts would be products of learning rather than fixed knowledge supplied by designers. Their textual or symbolic form would not by itself conflict with [the bitter lesson](../notes/the-bitter-lesson-selects-production-methods-not-representational.md).

Commonplace does not yet implement such a learned search loop. Humans still diagnose many failures, decide which artifact may be responsible, and accept changes; agents and automated checks assist them. The human-assisted loop is a bootstrap: it discovers candidate representations and checks that a later search-and-learning loop could use. Whether search over a large, interdependent artifact corpus scales remains an empirical question, and its hard core is credit assignment without a chain rule: when an artifact-mediated system fails, the failure rarely identifies which of many interacting instructions, theories, schemas, or checks should change.

Stable guidance can be retired once a stronger model reliably supplies and applies it where needed. Some information still requires an authoritative current record. "Retry with backoff" is general knowledge. "This deployment retries with backoff, adopted after the March incident and owned by the platform team" records a [current commitment](../notes/commitment-not-derivation-creates-new-ground-truth.md). A model may reproduce the sentence, but [reproduction alone does not establish](../notes/parametric-reproduction-cannot-replace-an-authoritative-record.md) that the commitment is still operative, who authorized it, or what evidence now supports it. The record can use any representation that preserves currentness, attribution, and authorized revision.

## Use tests the structure

The production-method distinction leaves Commonplace's current types, gates, and indexes to be tested through use. One working bet is that explanation-first selection produces useful, well-supported knowledge per unit of human judgment. Review can [assess an individual explanation's reach, while use must show whether the method earns its maintenance cost](../notes/a-proximate-target-is-checked-for-achievement-not-for-warrant.md).

The opening index episode supplies use evidence about one part of that methodology. Commonplace stores and governs its methodology in the same knowledge base whose rules it is testing. The [division of work](../notes/methodological-and-computational-closure-track-different-changes.md) was explicit: a maintainer noticed the problem, initiated the repair, and accepted it; an agent drafted a candidate change; automation enforced the new marks and found the omitted note. Because [Commonplace's declared boundary](../reference/commonplace-as-a-reflective-system.md) includes designated maintainers, this was a human-inclusive loop.

A passing gate shows that its criterion was met; the criterion may still be [a poor proxy for the intended capability](../notes/exact-implementation-does-not-validate-a-requirement.md). Use tests how the parts work together through missed retrievals, misleading indexes, recurring corrections, and effort repeatedly spent on the same problem. Manual workarounds count too, because they consume the human judgment the system is meant to spare.

A successful use shows that [the current division of work among artifacts, indexes, checks, agents, and maintainers sufficed in that context](../notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md); transfer requires more. A rationale retained when the design is chosen records whether each boundary answers an inherited constraint, answers a local requirement, or is a free choice made for convenience. The rationale is itself a hypothesis: repeated use in varied contexts tests the transfer claim, while changing a condition such as the review budget or retrieval load tests whether the rationale identified a boundary that matters.

Self-use therefore guards against ossification: it exposes hand-designed structure to evidence and supplies reasons to revise or remove it. In this way it addresses the empirical burden raised by the bitter lesson.

Moving an adoption decision to an automated check changes who decides. For Commonplace, this counts as improvement only when the [check is reliable enough for what is at stake](../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) and the change produces more useful, better-warranted knowledge work per unit of human judgment.

A [July 2026 preprint](https://arxiv.org/abs/2607.19592) reports that a frozen, curated task-knowledge artifact — delivered to the solver through a task-conditioned adapter — improved solve rates on held-out hard tasks the recipient models had initially failed, including across two model families. The system revises task knowledge, not a representation of its own organization, so [the result](../sources/knowledge-centric-self-improvement-2607.19592.ingest.md) supports artifact retention and transfer, not reflective self-improvement.

The broader empirical question is whether an evolving, addressable artifact layer improves a declared objective — such as adaptation speed, reliability, or governance quality — compared with stronger base models and simpler memory systems. A fair test compares those baselines as corpus size and model strength change, while counting evaluation, maintenance, and human judgment. Self-use supplies observations about Commonplace's current design.

## Where to go next

Before calling a system reflectively self-improving, ask five questions:

- What system boundary is being assessed, over what horizon, and which of its own instructions, code, memory, or other behavior-shaping structures does the self-representation cover?
- What independently specifiable objective does the evidence bear on?
- Does evidence update the operative artifacts directly, or by generating candidate changes and selecting among them?
- If candidates are generated: what produces them, and where can the loop reject one?
- Which artifact carries an accepted change into later runs, and how reliably do those runs consume it?

The first two questions establish the self-reference and evidence-responsiveness that make the pathway reflective and self-improving. The last two apply to the proposal-selection case, where they name the loop's [search, evaluation, and retention functions](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md).

The [self-improving-systems cluster](../notes/self-improving-systems-README.md) maps the theory behind the questions, and [the repository](https://github.com/zby/commonplace) contains the framework.
