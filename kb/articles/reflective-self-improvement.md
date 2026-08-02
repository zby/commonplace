---
description: "Defines reflective self-improvement and claims its diagnostic frame: the loop decomposition, the omitted/frozen distinction read against four 2026 systems, verification-bounded migration, a five-question test, and the bitter-lesson constraint"
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
  - kb/notes/compounding-needs-leverage-to-multiply-and-autonomy-to-scale.md
  - kb/notes/reflective-leverage-is-tested-in-the-next-episode.md
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
  - kb/notes/an-omitted-loop-function-and-a-frozen-one-need-different-repairs.md
  - kb/reference/commonplace-as-a-reflective-system.md
  - kb/reference/tag-readme-trace-observed-causal-connection.md
  - kb/agentic-systems/exo.md
  - kb/sources/knowledge-centric-self-improvement-2607.19592.ingest.md
  - kb/sources/self-harness-harnesses-that-improve-themselves.ingest.md
  - kb/sources/continual-harness-online-adaptation-foundation-agents.ingest.md
  - kb/sources/autogenesis-a-self-evolving-agent-protocol.ingest.md
  - kb/sources/self-improving-ai-coding-agents-through-accumulated-rules.ingest.md
  - kb/sources/sutton-the-bitter-lesson-original-essay.md
---

# Reflective self-improvement

**TL;DR.** Agents that rewrite their own prompts, memory, skills, and harness code now exist. Read against a functional decomposition of the improvement loop — search, evaluation, operative retention — each of the recent systems leaves some function either *omitted* (nothing performs it) or *frozen* (performed by machinery the loop cannot revise); the placements are mostly inherited rather than argued, and reported benchmark gains cannot reveal which condition holds. The claim of this article is the diagnostic frame, not the surface: a theory of the loop's own functions, retained as governed, revisable artifacts; the distinction between omitted and frozen functions, which need different repairs; and verification-bounded migration as the rule for which decisions move from humans into computation. The loop can start before autonomy — Commonplace runs it human-inclusively, and applying its own decomposition to the recent systems has already forced revisions of that decomposition. Not yet shown: sustained compounding, autonomous semantic evaluation, or advantage over stronger models and simpler memory.

An agent that is corrected today and repeats the mistake tomorrow wastes the correction. The obvious fix is retention: let the agent write down what it learned, somewhere later runs will read it. This article is about what that fix opens up: a pathway by which an agent changes itself through readable artifacts. Systems that run the pathway now exist; what they still lack is a revisable theory of their own loop. The pathway's main benefit is addressability; its hard parts are retrieval, verification, and control over what gets written. Diagnosing any particular loop means asking which of its functions nothing performs — and which are performed by machinery the loop itself cannot revise.

Suppose a deployment fails on a Tuesday because a credential expired. An agent reviewing the trace mistakes the date for the cause and records a standing rule: "Deployments fail on Tuesdays." Later runs consume the rule and avoid Tuesday deployments. The agent has learned from evidence, and it has made itself worse.

An agent does not need to change its model weights to change itself. Prompts and instruction files, retained memories, tests, validators, and scaffolding code all steer later runs, and an LLM agent can read those artifacts, criticize them, and rewrite them. Software that acts on [such a representation of itself](../notes/definitions/reflective-system.md) is computationally reflective — reflection in the computational sense, not simply a model reviewing its mistakes. When evidence bearing on [an objective specified independently of the change](../notes/self-improvement-is-relative-to-a-declared-objective.md) leads such a system to make an [operative change to its own organization](../notes/definitions/self-improving-system.md) through that representation, the pathway is **reflective self-improvement**. The Tuesday agent ran the retention machinery of this pathway with none of the rest: its rule describes deployments rather than the system, no objective evidence was ever consulted, and no point existed at which the false lesson could be caught.

A real trace shows the pathway running with those catch points in place. [Commonplace](../index.md), the knowledge-base system that holds this article, had a topic index that both introduced its subject and promised to list every note carrying its tag; past fifty entries the promise could no longer be verified by hand. A recorded decision split the two jobs and introduced machine-checked coverage marks, and while applying the new check the validator exposed a note the documented search recipe had missed, so the recipe was corrected too. The objectives existed before the repair, the changed pages and checks were part of the system's operative definition, and the [commit history records the chain](../reference/tag-readme-trace-observed-causal-connection.md). Unlike the Tuesday rule, every step was governed — a maintainer diagnosed, an agent drafted, automation enforced — though outcome evidence still decides whether the change helped.

An artifact does not become a self-representation just because later behavior depends on it. The Tuesday rule is a claim about deployments that happens to steer behavior; the index pages and validation recipes describe how the system routes and checks its own work, and sit on the causal path by which it does so. That narrower case — readable artifacts that are both a representation of the system and part of the machinery being revised — is the subject here.

The machinery is not what makes such a system special. An agentic software factory already has repositories, tests, review, and deployment loops; applied to an external product, they improve the product. Applied to representations of the factory's own operation — its prompts, workflows, evaluators, retrieval rules — they open a feedback loop, because an accepted change can improve the machinery that produces later changes: better retrieval helps diagnose the next failure, a better evaluator improves the next selection, and — highest on this ladder — a revised theory of the loop itself changes how every later failure is diagnosed. An improvement of that kind carries [reflective leverage](../notes/compounding-needs-leverage-to-multiply-and-autonomy-to-scale.md): it is what turns a growing stock of retained lessons into compounding, where earlier changes make later improvement episodes cheaper. Leverage alone does not sustain the loop — every accepted change must still be tested, and the volume a compounding loop generates outgrows fixed human attention — so compounding also needs evaluation at computational scale, as far as its checks warrant.

One consequence of the definition is better granted up front than argued over: include the maintainers in the declared boundary and reflective self-improvement is close to ubiquitous in software engineering. The question worth pursuing begins after membership: how the pathway's decision-bearing functions — noticing, diagnosis, choice of change, acceptance — [migrate from human actors into computational processes](../notes/computationally-directed-self-improvement-is-a-reallocation.md), and how far that migration can go while the accepted changes remain adequately verified. LLMs matter here because they change which functions can move: earlier automation internalized execution, while a model can plausibly take over diagnosis, candidate generation, and the editing of the representations themselves. Reflection makes the system's organization addressable; leveraged changes create the feedback; autonomy determines where the loop is executed. The program, in one sentence, is the progressive computational internalization of reflective control while preserving warranted improvement.

## What readable artifacts buy

A self-hosting compiler supplies the basic causal pattern: its source is written in the language it compiles, the resulting compiler runs the next build, and humans diagnose, revise, and choose what to adopt. An LLM agent can perform some of those roles itself, and accepted operative revisions affect later runs without changing the model's weights.

Suppose an agent records a rule: "always pin the dependency versions." As a note, the lesson carries a scope and a rationale, and it can be inspected, revised, or retired individually. Weight changes can be rolled back, trained over, and even targeted through [model editing](https://arxiv.org/abs/2202.05262), but those interventions do not expose the lesson itself as a readable object. This is the first benefit, direct [addressability](../notes/reflection-buys-addressability.md): a retained lesson is a separable object that can be named, criticized, rescoped, and deleted.

The second benefit is legibility: the operative content can be read directly, not only exercised. Weight changes can also carry rationales, logs, and evaluations, but the operative content itself stays behind behavior. Legibility enables addressability without guaranteeing it — a long unindexed instruction log is readable in principle yet unaddressable in operation.

Now suppose a login test fails intermittently because it reads the real clock. An agent could retain either "retry the flaky login test" or "tests that read the wall clock flake, so freeze the clock." The first helps with one test; the second explains the failure and can prevent it in tests that have not been written yet. The third benefit is conjectural: [sample efficiency](../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md) — an explanation that survives such a task shift may adapt the system from fewer observations than retraining or fine-tuning would require, though finding, evaluating, and maintaining it still costs compute, tokens, and judgment.

## Where the pathway breaks

Stored notes or memories affect an agent run only if they are retrieved: a note that would have prevented today's mistake has no effect on a run that never finds it. In a retrieval-mediated system, [failing to retrieve the relevant self-representation is a failure of the reflective pathway itself](../notes/retrieval-failure-is-reflection-failure.md), not a performance detail — retained knowledge depends on maintained indexes and search to enter a run at all.

The write side is an attack surface. The Tuesday case shows why: [a consumption channel delivers behavioral force without the history that produced the content](../notes/a-consumption-channel-delivers-force-without-the-history-that.md). An untrusted tool result can exploit the same path by telling the agent to save a directive — anything allowed to write into the instruction path can modify the system. Provenance, write authority, review, and rollback are the controls that path needs.

The read side needs verification the loop cannot supply for itself: there is no general test for whether a rewritten instruction is better, and an agent may judge a revision through the very instructions being revised. Reflection needs verification that reflection itself does not supply. In Commonplace, [typed artifacts](../notes/why-notes-have-types.md) declare the contract under which an artifact is interpreted, checked, and retrieved; mechanically decidable rules run as code; semantic [review gates](../reference/README-REVIEW-SYSTEM.md) assess a candidate against a fixed criterion in a fresh context, which removes the generation trajectory though not the blind spots a reviewing model may share with the generator. For reusable explanatory claims, [explanatory reach](../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md) is an explicit review target: the supporting episodes remain with the theory so later evidence can overturn it, and review tests [whether the claimed reach is genuine](../notes/definitions/reach-assessment.md) — though whether LLM-mediated review can assess reach reliably is itself an open question.

## Existing systems cover parts of the loop

The lineage is real but partial: [Reflexion](https://arxiv.org/abs/2303.11366) retained natural-language lessons within a task, [Voyager](https://arxiv.org/abs/2305.16291) durable executable skills, [Promptbreeder](https://arxiv.org/abs/2309.16797) benchmark-selected prompts, [STOP](https://arxiv.org/abs/2310.02304) its own scaffolding code — each without a governance layer or with evaluation through a narrow channel. The original [Gödel machine proposal](../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md) marks the far pole: a self-rewrite only after proof from its own axioms that switching beats continuing to search — acceptance held inside the update space, at the price that unprovable improvements stay out of reach. Natural-language criticism can weigh effects a proof system cannot establish or a fixed benchmark does not measure — but its judgments need verification outside the text being judged.

The claim, then, is not that an LLM plus a readable artifact layer can serve as an operative reflective surface — by 2026 that is demonstrated territory. [Self-Harness](../sources/self-harness-harnesses-that-improve-themselves.ingest.md) has a fixed model mining its own failure traces and editing its own harness through a regression gate; [Autogenesis](../sources/autogenesis-a-self-evolving-agent-protocol.ingest.md) evolves prompts, tools, agents, and memory as versioned resources with lineage and rollback; [Continual Harness](../sources/continual-harness-online-adaptation-foundation-agents.ingest.md) improves a harness first with humans in the loop and then with an automated refiner; a production team has turned [accepted review comments into version-controlled behavioral rules](../sources/self-improving-ai-coding-agents-through-accumulated-rules.ingest.md) consumed across sessions; and the [Darwin Gödel Machine](../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md) evolves an archive of self-modifying coding agents, admitting every viable child and letting benchmark score steer only which parent is tried next. What none of them supplies is a theory of the loop they are running.

Such a theory is not commentary from outside. Retained as a governed artifact, it sits inside the loop it describes — it is what gets consulted when the next failure is diagnosed — so a revision to it carries more leverage than a revision to any single gate or index: it redirects every later episode's diagnosis. Each of these systems has a theory of its loop; it lives in the paper, frozen at publication, where the running system cannot revise it.

The freeze shows in the loops themselves. Read against the loop's [functional decomposition](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md), [each leaves a function either omitted — nothing performs it — or frozen outside the loop's own update space](../notes/an-omitted-loop-function-and-a-frozen-one-need-different-repairs.md): an edit nothing could refuse, or a gate the loop it governs cannot revise. Only the Darwin Gödel Machine defends any of its placements, and the two conditions need different repairs that reported benchmark gains cannot tell apart. The claim this article defends is that diagnostic frame: the decomposition of the loop, the omitted/frozen distinction, and verification-bounded migration as the criterion for which frozen functions may be lifted — held as a revisable map rather than a finished one, and already revised twice by its own application: mapping the systems exposed retirement as a function the decomposition lacks a slot for, and the Darwin Gödel Machine's defended freezes split frozen into protective and affordable.

The closest comparison to Commonplace is the [reviewed Exo version](../agentic-systems/exo.md) (commit `ef4cfe05`, 2026-07-29): a harness and memory system that changes both natural-language and executable artifacts, with event history, versioned artifacts, deliberate removal, and rebuild-gated activation. Its weaker point is semantic governance — memory facts lack declared scope, provenance, and review state, and durability requires no independent semantic review. Commonplace begins with that governance problem and provides far fewer runtime capabilities.

## The bitter lesson concerns production, not form

Commonplace currently relies on hand-designed artifacts: types, link rules, review criteria, and validators. [The bitter lesson](../sources/sutton-the-bitter-lesson-original-essay.md) warns that methods built around human knowledge tend to lose to methods that use increasing computation through search and learning — must prompts, code, and knowledge bases disappear into model weights? The reply is a distinction: search and learning are production methods, while natural language, code, and weights are representational forms. A system can search over theories, instructions, tests, and schemas, and retain the selected artifacts for later use and revision — products of learning whose textual form [does not by itself conflict with the lesson](../notes/the-bitter-lesson-selects-production-methods-not-representational.md). Commonplace does not yet implement that learned search loop; humans still supply most diagnosis and acceptance, and the human-assisted loop is a bootstrap discovering candidate representations and checks for a later search-and-learning loop. The deeper conjecture is that the bootstrap compounds — if enough accepted changes carry reflective leverage, the road to a more autonomous loop is itself a self-improving process. Whether search over a large, interdependent artifact corpus scales remains open, and its hard core is credit assignment without a chain rule — a failure rarely identifies which of many interacting artifacts should change.

Some information also requires an authoritative current record regardless of model strength: "retry with backoff" is general knowledge a stronger model may supply, but "this deployment retries with backoff, adopted after the March incident" records a [current commitment](../notes/commitment-not-derivation-creates-new-ground-truth.md), and [reproduction alone does not establish](../notes/parametric-reproduction-cannot-replace-an-authoritative-record.md) that it is still operative, who authorized it, or what evidence now supports it.

## Use tests the structure

The production-method distinction leaves Commonplace's current types, gates, and indexes to be tested through use. The working bet is that explanation-first selection produces useful, well-supported knowledge per unit of human judgment — review can [assess an individual explanation's reach, while use must show whether the method earns its maintenance cost](../notes/a-proximate-target-is-checked-for-achievement-not-for-warrant.md).

The index episode from the introduction is one such observation. The [division of work](../notes/methodological-and-computational-closure-track-different-changes.md) was explicit, and because [Commonplace's declared boundary](../reference/commonplace-as-a-reflective-system.md) includes designated maintainers, the loop was human-inclusive — an inspectable causal pathway, not autonomous diagnosis: noticing and acceptance human, drafting computational, enforcement mechanical. Both accepted changes carried predicted reflective leverage — the coverage check strengthens future verification, the corrected recipe future retrieval — though whether the next episode actually runs cheaper has not been measured. The endpoint of the migration is not "an LLM wrote the code": it is reached when removing the maintainer from an episode would no longer break the loop — when the system itself uses evidence and a representation of itself to determine what should change.

A passing gate shows that its criterion was met; the criterion may still be [a poor proxy for the intended capability](../notes/exact-implementation-does-not-validate-a-requirement.md). Use tests how the parts work together: missed retrievals, misleading indexes, recurring corrections, and manual workarounds all count, because workarounds consume the human judgment the system is meant to spare. A successful use shows only that [the current division of work sufficed in that context](../notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md); the rationale retained with each design choice is itself a hypothesis that varied use tests, and moving an adoption decision to an automated check counts as improvement only when the [check is reliable enough for what is at stake](../notes/warranted-autonomy-is-bounded-by-oracle-domain.md).

The loop-level empirical question is whether the human-assisted loop actually exhibits reflective leverage — earlier accepted changes making later improvement episodes cheaper, broader, more reliable, or less dependent on human judgment — or is merely repeated manual maintenance. [Leverage is tested in the next episode, not in the metric that accepted the change](../notes/reflective-leverage-is-tested-in-the-next-episode.md): a fair test compares an evolving artifact layer against frozen-artifact, stronger-model, and simpler-memory baselines as corpus size grows, while counting evaluation, maintenance, and human judgment. (Artifact retention alone is already evidenced: a [July 2026 preprint](https://arxiv.org/abs/2607.19592) shows a frozen task-knowledge artifact improving held-out solve rates across model families — [retention and transfer](../sources/knowledge-centric-self-improvement-2607.19592.ingest.md), but not of a representation of the system's own organization.)

## The reflective self-improvement test

Before calling a system — your own or a published one — reflectively self-improving, ask five questions:

> 1. What system boundary is being assessed, over what horizon, and which of its own instructions, code, memory, or other behavior-shaping structures does the self-representation cover?
> 2. What independently specifiable objective does the evidence bear on?
> 3. Does evidence update the operative artifacts directly, or by generating candidate changes and selecting among them?
> 4. If candidates are generated: what produces them, and where can the loop reject one?
> 5. Which artifact carries an accepted change into later runs, and how reliably do those runs consume it?

These questions are the diagnostic frame made operational — the readings of the recent systems above are their application. The first two establish self-reference and evidence-responsiveness; the last two name the loop's [search, evaluation, and retention functions](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) for the proposal-selection case. Applied to the Tuesday agent: the rule reached the operative instructions (question five), but no outcome evidence was consulted (question two) and nothing could reject it (question four).

## What this article claims

| Status | Claim |
|---|---|
| Observed | Commonplace revised index pages, validation, and a search recipe through a governed, human-inclusive loop, and later runs consume the changes. |
| Observed | Applying the loop decomposition to external systems exposed a gap it cannot yet express — retirement — recorded as evidence against the model, and forced a refinement it adopted: frozen splits into protective and affordable. |
| Argued | Each of five recent self-improving-agent systems leaves a loop function either omitted (nothing performs it) or frozen (performed by machinery the loop cannot revise), and reported benchmark gains cannot distinguish the two conditions. |
| Argued | Under a human-inclusive boundary, membership is nearly ubiquitous in maintained software; the substantive variable is which decision-bearing functions humans still supply. |
| Argued | Readable operative artifacts provide addressability — selective inspection, revision, and removal — that weight-retained lessons do not expose. |
| Conjectured | Explanatory artifacts may adapt a system from fewer target observations under structured task shifts. |
| Conjectured | With a sufficient fraction of leveraged changes, a partially automated reflective loop bootstraps its own improvement machinery — later improvements become cheaper and less dependent on human judgment. |
| Open | Whether retrieval, semantic evaluation, credit assignment, and maintenance scale over a large, interdependent artifact corpus. |

## Where to go next

The Tuesday rule is worth keeping in view because it sets the real question. It is not whether the agent learned — it did. It is whether the loop could tell a causal lesson from a coincidence before the coincidence became part of the system.

The [self-improving-systems cluster](../notes/self-improving-systems-README.md) maps the theory behind the five questions, and [the repository](https://github.com/zby/commonplace) contains the framework. If applying the test to a system you build or study produces a counterexample or a disputed boundary case — an agent with editable memory but no independent review, a benchmark-selected prompt that looks like a maintained theory — [open an issue](https://github.com/zby/commonplace/issues).
