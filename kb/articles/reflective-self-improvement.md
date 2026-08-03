---
description: "Defines the general evidence-to-operativity anatomy of reflective self-improvement, then compares direct and proposal-selection systems without treating a verifier as universal"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/definitions/self-improving-system.md
  - kb/notes/definitions/behavior-determining-organization.md
  - kb/notes/definitions/behavioral-authority.md
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
  - kb/reference/tag-readme-trace-as-self-improving-loop.md
  - kb/sources/knowledge-centric-self-improvement-2607.19592.ingest.md
  - kb/sources/self-harness-harnesses-that-improve-themselves.ingest.md
  - kb/sources/continual-harness-online-adaptation-foundation-agents.ingest.md
  - kb/sources/autogenesis-a-self-evolving-agent-protocol.ingest.md
  - kb/sources/self-improving-ai-coding-agents-through-accumulated-rules.ingest.md
  - kb/sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md
  - kb/sources/sutton-the-bitter-lesson-original-essay.md
---

# Reflective self-improvement

> **TL;DR.** Agents can now revise prompts, memory, skills, and harness code that shape later runs. Reflective self-improvement occurs when objective-bearing evidence causally changes the system's own organization through a self-representation, and a subsequent operation depends on that change. Saving evidence or installing a rule that is never used does not close this path.
>
> Proposal selection is one update architecture: it factors change into search, reject-capable evaluation, and operative retention. Four recent systems use that architecture and hold evaluation frozen outside their own update space; a fifth updates directly and therefore has no required rejection stage. A missing link in the general anatomy defeats the occurrence claim. A frozen proposal-selection function still operates, but needs a governed revision path or a reason to remain fixed. A Commonplace trace shows a human-inclusive instance, not sustained compounding, autonomous semantic evaluation, or advantage over stronger models or simpler memory.

## What changes count

An agent that is corrected today and repeats the mistake tomorrow wastes the correction. The obvious response is to save the lesson and build a path by which later runs use it. Saving alone does not establish that path, and a working path can preserve a bad lesson as effectively as a good one.

Suppose a deployment fails on a Tuesday because a credential expired. An agent reviews the trace, mistakes the date for the cause, and edits its own standing deployment policy to say, "Never deploy on Tuesdays." Later runs act through that policy and therefore avoid Tuesday deployments. The failure supplied evidence bearing on the pre-existing objective of reducing deployment failures, and the resulting change is operative. It nevertheless makes the system worse because the evidence did not justify the causal rule. Self-improvement names an improvement-directed pathway, not a guarantee that every adopted update improves the outcome.

An agent does not need to change its model weights to change itself. Prompts, instruction files, retained memories, tests, validators, and scaffolding code can all determine later behavior, and an LLM agent can inspect and revise them. But not every stored fact that influences behavior is a self-representation. A [self-representation](../notes/definitions/reflective-system.md) represents some declared aspect of the same system and participates causally in that aspect's later operation. The edited deployment policy represents part of the agent's own operating policy, and later runs act through it. A note that merely recorded "the credential expired on Tuesday" would remain a claim about the environment, even if the agent later consulted it.

Software that can inspect or act through such a causally connected representation is computationally reflective. **Reflective self-improvement** combines [self-improvement](../notes/definitions/self-improving-system.md) with [reflection](../notes/definitions/reflective-system.md): evidence bearing on [an independently specifiable objective](../notes/self-improvement-is-relative-to-a-declared-objective.md) must causally influence a change to the system's own [behavior-determining organization](../notes/definitions/behavior-determining-organization.md) through a causally connected self-representation, and the changed organization must govern a subsequent operation within the declared horizon.

```text
objective-bearing evidence affects the update
                        ↓
the system's own organization changes
                        ↓
the change enters a live behavioral path
                        ↓
a subsequent operation depends on the change
```

A stored trace that never affects an updater fails at the evidence-to-update transition. A proposed rule that is never installed fails at installation. A rule that is loaded but ignored fails at behavioral uptake. Each is a missing transition in the general anatomy. The Tuesday update completes the path despite its harmful result.

How the update is determined is a separate architectural question. A **direct update** makes an evidence-determined successor the incumbent without exposing a separately rejectable candidate. A **proposal-selection update** generates candidates, evaluates them with the possibility of rejection, and selectively makes an accepted change operative. That subtype requires [search, reject-capable evaluation, and operative retention](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md).

The Tuesday policy is a direct update. Its lack of a rejection stage is an architectural fact, not an omitted universal function. Its weakness lies in the evidence-to-policy update rule, which turns a coincidence into a standing policy.

Across either architecture, declare the boundary, objective, and horizon, then trace who supplies the evidence, determines the update, installs the change, and consumes it later. Proposal selection further separates search, evaluation, and selective retention. Progress toward [computationally directed self-improvement](../notes/computationally-directed-self-improvement-is-a-reallocation.md) reallocates whichever operations the pathway actually contains while preserving adequate checks. This is **verification-bounded migration**: a decision moves into computation only as far as the available verification warrants.

## What readable artifacts buy

Suppose an agent adopts an operative rule: "always pin dependency versions." Stored as a readable policy, its content can be inspected directly rather than inferred from behavior. Weight changes can be rolled back, trained over, even targeted through [model editing](https://arxiv.org/abs/2202.05262), but the operative content itself remains behind behavior. Readable artifacts provide **legibility**.

When the policy also has a scope, a reliable retrieval path, and a governed revision path, legibility enables [addressability](../notes/reflection-buys-addressability.md): it can be named, criticized, rescoped, revised, or retired individually. A long unindexed instruction log is legible in principle but not operationally addressable.

Now suppose a login test fails intermittently because it reads the real clock. An agent could adopt either "retry this flaky login test" or "when a test depends on time, freeze the clock." The first policy helps with one test; the rationale behind the second can prevent the same failure in tests that have not been written yet. The third benefit is conjectural: [sample efficiency](../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md) — an explanation that survives such a task shift may adapt the system from fewer observations than retraining or fine-tuning would require, though finding, evaluating, and maintaining it still costs compute, tokens, and judgment.

When the revised artifact participates in the improvement pathway itself — a retrieval rule, evaluator, acceptance criterion, or model of the loop — the change can affect how later changes are found and judged. This predicted effect is [reflective leverage](../notes/compounding-needs-leverage-to-multiply-and-autonomy-to-scale.md). Better retrieval may improve the next diagnosis; a better evaluator may improve the next selection. The leverage is not established when the artifact is accepted. It must appear in later episodes.

## Where the pathway breaks

The missing-link diagnosis is architecture-neutral. Retrieval and authority paths explain causal failures. Verification addresses a different question: whether the evidence-to-change rule should be trusted.

Retrieval can break both ends of the path. A saved trace cannot guide an updater that never finds it, and a retained policy cannot affect a later run that never loads it. In a retrieval-mediated system, [failing to retrieve the relevant self-representation is a failure of the reflective pathway itself](../notes/retrieval-failure-is-reflection-failure.md), not a performance detail. Even successful loading may fall short if the model ignores the content.

The write side is an attack surface. The Tuesday case shows why: [a consumption channel delivers behavioral force without the history that produced the content](../notes/a-consumption-channel-delivers-force-without-the-history-that.md). An untrusted tool result can exploit the same path by telling the agent to save a directive — anything allowed to write into the instruction path can modify the system. Provenance, write authority, review, and rollback can govern that path; which controls are required depends on its force and risk.

Completing the general path supplies no warrant that a rewritten instruction is better. In a direct update, trust rests on the objective, evidence signal, and update rule. Proposal selection adds a separate evaluator: it may sit inside the declared system boundary, but its location and its grounds remain different questions. Acceptance cannot reduce to the candidate's unsupported judgment of itself. Tests and proofs can settle mechanically decidable properties, while semantic review can apply a fixed criterion in a fresh context, removing the generation trajectory but not blind spots shared with the generator.

## The reflective self-improvement test

Before calling a system — your own or a published one — reflectively self-improving, ask five questions:

> 1. What boundary was declared before the assessment, over what horizon, and which behavior-shaping structures represent aspects of that same system?
> 2. What independently specifiable objective does the evidence bear on?
> 3. Does that evidence causally influence a change to the system's own behavior-determining organization through its self-representation, rather than merely being stored or retrieved?
> 4. What installs the result on a live consumer–channel–force path, and which subsequent operation actually depends on the change?
> 5. Is the update direct or proposal-selected? If proposal-selected, what performs search, reject-capable evaluation, and operative retention, and which of those functions lie outside the loop's update space?

Questions one through four test the general obligations of an occurrent reflective self-improvement claim. If one is missing, the claimed pathway does not close at that link. Question five identifies the update architecture. Search, reject-capable evaluation, and selective retention become required diagnostics only after the path is identified as proposal selection; a direct update has no omitted evaluator merely because it lacks a rejection stage.

The Tuesday policy passes the first four questions: objective-bearing evidence changes a represented operating policy, and later runs act through it. Question five identifies a direct update. No evaluator is omitted; the evidence-to-policy rule is simply weak enough to retain a false causal inference.

## Applying the test to existing systems

Historical precursors established the update surface: [Reflexion](https://arxiv.org/abs/2303.11366) retained lessons, [Voyager](https://arxiv.org/abs/2305.16291) skills, [Promptbreeder](https://arxiv.org/abs/2309.16797) prompts, and [STOP](https://arxiv.org/abs/2310.02304) scaffolding code.

The original [Gödel machine proposal](../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md) marks the formal pole: it accepts a self-rewrite only after proving from its own axioms that switching is preferable to continuing the search. The proof machinery sits inside the system, illustrating that a verifier's location and the independence of its grounds are different questions; the cost is that unprovable improvements remain out of reach.

The table follows the general path before naming the update architecture. It uses the article's assessed boundaries: the optimization machinery is included, Accumulated Behavioral Rules includes the engineers, and the Darwin Gödel Machine uses the composite archive/population. These are not necessarily the boundaries under which the papers frame their claims.

| System | Evidence-dependent organizational change | Installation; evidence of later use | Architecture and governance |
|---|---|---|---|
| [Self-Harness](../sources/self-harness-harnesses-that-improve-themselves.ingest.md) | Failure traces and verifier-grounded signatures condition proposals that edit bounded harness instructions, tools, and runtime controls; split pass counts determine promotion. | **Installation:** gate-passing edits are merged. **Later use:** subsequent harness evaluations run through them. | **Proposal selection.** The objective and edit surface are fixed; the two-split regression gate is frozen. |
| [Continual Harness](../sources/continual-harness-online-adaptation-foundation-agents.ingest.md) | Recent trajectory windows and failures drive Refiner changes to prompts, sub-agents, skills, and memory. | **Installation:** harness edits enter the next step. **Later use:** prompt and harness changes are exercised, while memory use is sparse and most authored skills are never invoked. | **Direct update.** Refiner judgment, schedule, component partition, and reward design remain fixed; no rejection stage is required by this architecture. |
| [Autogenesis Reflection optimizer](../sources/autogenesis-a-self-evolving-agent-protocol.ingest.md) | Traces and registered resource state feed typed operators. Experiments change prompts and agent code or tool implementations; the protocol also exposes Environment and Memory resources whose evolution is not independently evaluated. | **Installation:** evaluated changes become active versions. **Later use:** prompt and agent experiments reuse them; every resource type is not independently evaluated. | **Proposal selection.** The objective and learnability mask are fixed; the evaluation rule is frozen. Other Autogenesis instantiations may commit directly. |
| [Accumulated Behavioral Rules](../sources/self-improving-ai-coding-agents-through-accumulated-rules.ingest.md) | Accepted review comments and engineer judgment produce generalized rules in a standing file and checklists. | **Installation:** two agent interfaces load the rules in later sessions. **Later use:** no recurrence is reported across 74 post-rule exposures, but without a no-rule control causal dependence is not established. | **Proposal selection.** Human generalization judgment is frozen and the always-loaded delivery scheme is fixed; rules are append-friendly and can be refined, while the paper describes removal inconsistently. |
| [Darwin Gödel Machine](../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md) | Archive scores and child counts select a parent; its logs feed a fixed diagnostician, and the parent implements a descendant edit. | **Installation:** each child is evaluated before viability admission to the archive. **Later use:** admitted non-perfect agents remain eligible for parent sampling, but post-admission execution is not guaranteed. | **Proposal selection.** The viability gate is frozen, benchmark score steers search, and the monotonic archive is deliberate. |

At the general level, a missing link has a literal meaning: the evidence does not affect the updater, no behavior-determining organization changes, the result has no live authority path, or later operation does not depend on it. The sources establish these links unevenly. Accumulated Behavioral Rules reports loading and subsequent non-recurrence without isolating causal uptake; many Continual Harness artifacts are unused; and archive admission does not guarantee later execution in the Darwin Gödel Machine. An unestablished link is not the same as an absent one.

The remaining differences concern update architecture and governance. Four rows use proposal selection and hold evaluation frozen outside their update space. Continual Harness uses a direct update; adding a reject-capable evaluator would introduce proposal selection, not fill an omitted function in its current architecture. A **frozen** function is present but not revisable by the loop. The Darwin Gödel Machine separately hides a hallucination evaluator against objective hacking and freezes its exploration controller as an affordable compute compromise; its ordinary viability gate is fixed, but that concealment does not defend it.

Benchmark gains report the complete configured system's measured performance. They do not by themselves establish every causal link from evidence through organizational change into later behavior, or show whether a fixed proposal-selection gate should become revisable. Those claims require tracing the general path and, for proposal-selection cases, the placement of search, evaluation, and selective retention.

The comparison also exposes a lifecycle question. Rollback restores an earlier version after a bad change; retirement removes or supersedes previously accepted material when it ceases to be useful. Retirement is not required for one occurrent self-improvement episode: a temporary or later-superseded change may already have been operative. None of the five descriptions establishes a system-wide, criterion-driven retirement path across all retained artifact types, although Continual Harness reports limited deletion and demotion and Accumulated Behavioral Rules permits refinement while leaving its removal policy unclear. The Darwin Gödel Machine deliberately retains every viable child to preserve stepping stones. Retirement may belong to continued retention, later evaluation, or a separate lifecycle process.

In these published designs, the account of the general path, the chosen update architecture, and the reasons for each frozen placement is not itself an artifact the running loop consults and changes. Making such an account reliably retrievable and granting the loop governed authority to revise it would make those allocations operationally addressable: a later failure could challenge the model used to diagnose it, not only a prompt or gate. Whether an explicit loop model improves diagnosis relative to model-free search remains open.

## What the Commonplace trace shows

Unlike the five published designs, [Commonplace](../index.md) supplies an observed trace of governed, human-inclusive reflective self-improvement: evidence changed operative system definitions, and later work ran through the changes. That particular trace used proposal selection. It establishes one implementation of the general pathway; it does not establish proposal selection as Commonplace's defining or sole update mechanism.

A topic index both introduced its subject and promised to list every note carrying its tag. Past fifty entries, complete coverage could no longer be verified reliably by hand. The objective — complete coverage that would not mislead a thorough reader — preceded the repair; the repair made that bar mechanically checkable. A maintainer diagnosed the problem, an agent drafted a split between exposition and coverage plus machine-checked coverage marks, code supplied reject-capable checks, and the maintainer accepted the change. Applying the new check then exposed a note that the documented search recipe had missed, so the recipe was corrected. The [commit history records the chain](../reference/tag-readme-trace-observed-causal-connection.md).

Under the general anatomy, prior objective-bearing evidence led to changes in Commonplace's operative self-representations, and later runs acted through those changes. The changed indexes, marks, validator, and recipe describe and control how the knowledge base routes and checks its own work. The [declared system boundary](../reference/commonplace-as-a-reflective-system.md) already includes designated maintainers. Under the proposal-selection decomposition, [search was joint](../reference/tag-readme-trace-as-self-improving-loop.md): a maintainer selected the problem and an agent formulated the candidate. Evaluation combined mechanical checks with maintainer judgment, and adoption installed the result through enforcement, routing, and advice. This establishes that the human-inclusive path closed. It does not establish that the repair made a later improvement episode cheaper, more reliable, or less dependent on human judgment.

The retained [external comparison](../notes/an-omitted-loop-function-and-a-frozen-one-need-different-repairs.md) records three revisions to the diagnostic model: update architecture must be classified before proposal-selection functions are applied, retirement remains an unresolved lifecycle placement, and freezes may be protective or affordable. This shows that the diagnostic artifact is revisable; whether those revisions improve later decisions remains open.

## Does the bitter lesson require weights?

[The bitter lesson](../sources/sutton-the-bitter-lesson-original-essay.md) warns that methods built around human knowledge tend to lose to methods that use increasing computation through search and learning. That challenges how Commonplace currently produces its types, link rules, criteria, and validators; it does not require the resulting knowledge to disappear into model weights. Search and learning are production methods, while natural language, code, and weights are representational forms. A system can search over theories, instructions, tests, and schemas, then retain the selected artifacts for later use and revision. Their readable form [does not by itself conflict with the lesson](../notes/the-bitter-lesson-selects-production-methods-not-representational.md).

Commonplace does not yet run computational search over these artifacts at scale. In the observed proposal-selection path, humans still supply most diagnosis and acceptance, and searching a large, interdependent artifact corpus may fail on credit assignment: a bad outcome rarely identifies which of many interacting artifacts should change. Some information also needs an authoritative current record at any model strength. Model weights might reproduce a [commitment](../notes/commitment-not-derivation-creates-new-ground-truth.md) such as "this deployment retries with backoff," but [reproduction does not establish](../notes/parametric-reproduction-cannot-replace-an-authoritative-record.md) that the policy remains operative or who authorized it.

## What would show compounding

A local gate establishes that its criterion was met, not that the whole improvement pathway became better. Reflective leverage is a claim about the next episode: earlier accepted changes should make later improvement cheaper, broader, more reliable, or less dependent on human judgment. Repeated use must test the end-to-end path from evidence activation, through organizational change, into later behavior, then ask whether earlier results improve a later update episode. Proposal-selection cases additionally expose search, evaluation, and selective retention as local diagnostic points. Missed retrievals, recurring corrections, and manual workarounds count against the system because they consume the judgment it is meant to spare.

A fair test would compare an evolving artifact layer with frozen-artifact, stronger-model, and simpler-memory baselines as the corpus grows, while counting evaluation, maintenance, and human judgment. A [July 2026 preprint](https://arxiv.org/abs/2607.19592) reports that a frozen task-knowledge artifact improves held-out solve rates across model families, supporting [retention and transfer](../sources/knowledge-centric-self-improvement-2607.19592.ingest.md). It does not test representations of the system's own organization, an evolving corpus, or compounding. Whether retrieval, semantic evaluation, credit assignment, and maintenance scale remains open.

## Where to go next

The Tuesday policy passes the general anatomy: evidence changes a represented operating policy and later runs act through it. It also makes the system worse. Can the update path distinguish a causal lesson from a coincidence before that coincidence becomes part of the system?

The [self-improving-systems cluster](../notes/self-improving-systems-README.md) maps the theory behind the five questions, and [the repository](https://github.com/zby/commonplace) contains the framework. If applying the test produces a counterexample or disputed boundary case — a stored memory whose later causal use is unestablished, or a system described as proposal selection despite having no rejectable adoption decision — [open an issue](https://github.com/zby/commonplace/issues).
