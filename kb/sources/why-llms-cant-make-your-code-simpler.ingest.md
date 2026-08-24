---
description: "Answer.AI's complexity argument is a bounded case of maintainability receiving weaker selection pressure than correctness, with ADRs able to supply the missing design context"
source: https://www.answer.ai/posts/2026-08-19-llms-code-simpler.html
captured: "2026-08-20"
capture: web-fetch
genre: practitioner-report
snapshot_sha256: f42d4546182cc58aeb741b4383eb809ba02228a66a249e5f7c897efe29188c30
ingested: "2026-08-20"
type: kb/sources/types/ingest-report.md
domains: [agentic-coding, maintainability, evaluation, design-rationale]
---

# Ingest: Why LLMs can’t make your code simpler

## Classification

Pol Alvarez Vecino develops a conceptual argument from Peter Naur, but the source's distinctive evidence is his firsthand account of Answer.AI's Solveit billing redesign and launch-day payment constraint.
Author: Alvarez Vecino writes as a participant in the reported design exploration, Stripe integration, and launch response. That gives the account useful operator signal about the team's reasoning, while the implementation, prompt, alternatives, and outcomes remain self-reported and unaudited.

## Summary

Alvarez Vecino adapts Peter Naur's “Programming as Theory Building” to argue that the complexity worth reducing is the team's situated understanding of a program, not a property recoverable from lines of code, cyclomatic complexity, duplication, or the Maintainability Index alone. He therefore doubts that adding those metrics as penalties to reinforcement learning can solve LLM-generated complexity. An invented provider-client example shows how the metrics can favor an abstraction even when an expected provider removal makes separated code easier to change. The article then reports Answer.AI replacing a subscription-and-credits billing design with a roughly 300-line credits-only system whose manual and automatic top-ups share one path. Launch exposed that Indian cards could not use its off-session auto-top-up flow; although Stripe subscriptions handled that case and an LLM recommended restoring them, the team accepted manual top-ups for those users to preserve its preferred simplicity. The case makes code structure depend on future changes, operational constraints, and product priorities that may not appear in the code.

## Claims

No claims have been grounded yet.

## Connections Found

The source is best treated as a bounded practitioner application of [Weakly discriminated qualities tend to be underselected](../notes/weakly-discriminated-qualities-tend-to-be-underselected.md). Code candidates can vary in both correctness and future change cost; tests strongly discriminate correctness, while static complexity metrics discriminate code shape without necessarily discriminating maintainability. At reject-capable training stages such as preference filtering or rejection sampling, retaining those choices in training data or weights can propagate the asymmetry into later candidates. The article illustrates that mechanism but reports no candidate cohort, operative training oracle, or enrichment comparison, so it is not prevalence evidence for the note's statistical conjecture. [Brainstorming: maintainability oracles for agentic development](../notes/brainstorming-maintainability-oracles-for-agentic-development.md) supplies the specific operational target: maintainability is relative to a future-change distribution. Compared with [Why Software Factories Fail](why-software-factories-fail-2080697380379427275.ingest.md), which emphasizes a delayed oracle, this source adds an information problem: the evaluator may never receive the change expectations and trade-off policy that define the target. That information need not remain tacit. The [Commonplace ADR contract](../reference/types/adr.md) can retain context, deciding forces, alternatives, and consequences, making project-specific design theory available as process evidence rather than treating an ADR as an inevitably incomplete substitute for it.

## Extractable Value

1. **Maintainability can receive weaker selection pressure at both development and training gates** -- Candidate outputs can vary in correctness and future change cost while tests, benchmarks, or preference labels distinguish correctness more reliably. Where a reject-capable stage retains the selected outputs in a codebase, training corpus, or model weights, that unequal enrichment can shape later candidates. The source makes this mechanism plausible but does not measure it. [deep-dive]
2. **Weak discrimination and information omission need different repairs** -- If expected changes and trade-offs are present but the evaluator cannot rank future cost, the maintainability oracle is weak. If training or runtime context omits those variables, observationally identical cases can require opposite designs and no learner can acquire the conditional choice; that is the information-omission case in [learning inside a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md). [deep-dive]
3. **ADRs can strengthen the oracle by making design theory addressable** -- Expected changes, priorities, rejected alternatives, and consequences can be recorded rather than left in human memory. Training can teach the general policy of seeking and conditioning on such rationale, while runtime ADRs provide the project-specific premises. The relevant threshold is sufficient decision context, not complete transfer of every experience that formed it. [quick-win]
4. **Static complexity can reverse the relevant maintainability ranking** -- The provider example isolates why fewer lines, less duplication, or a better complexity index is not decisive: the preferred structure changes when the anticipated removal of one provider enters the objective. This is a compact illustration of a hard oracle for its proxy becoming negatively discriminating for the target in the constructed case. [quick-win]
5. **Simplification can be purchased by narrowing product behavior** -- Answer.AI preserved one billing path partly by withholding automatic top-ups from Indian-card users. The case prevents “simpler code” from being treated as a free architectural improvement: the comparison must include which user outcomes and revenue risks were removed from the objective. [just-a-reference]
6. **Preference reversal is a direct evaluation target** -- Hold two behaviorally correct implementations fixed, vary only an ADR-like premise such as “Anthropic will probably be removed next month,” and test whether the evaluator or trained policy reverses its ranking. Later change cost can then test whether the contextual preference was aligned, separating context use from generic DRY or low-LoC reflexes. [experiment]

## Limitations (our opinion)

This is one team's retrospective account. It provides no repository revision, before-and-after maintenance data, defect rate, engineering-time comparison, revenue effect, or user-impact measurement beyond a rough final line count. The billing intervention also changed the product policy: automatic top-up ceased to be a requirement for one user group. The resulting system may be locally preferable, but the report does not establish a generally simpler architecture under a constant objective.

The LLM evidence is especially weak: one model response is recalled without the prompt, supplied context, full output, rival models, or repeated trials. Recommending subscriptions or both systems is not demonstrably wrong under a revenue or accessibility objective. The team's implementation history, Stripe experience, launch feedback, discussions, and simplicity preference were accessible to the humans, while the model received an unspecified subset; the considered designs and the decision to tolerate manual Indian top-ups were also fixed outside the comparison. Under the lens of [learning inside a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), the episode supports this compound configuration only. It does not validate the input decomposition, exclude unconsidered responses, or establish that LLMs categorically cannot simplify code.

The training-stage interpretation is also untested. The article inspects no corpus, preference data, reward model, candidate filter, or weight update, so it does not show that maintainability is underselected during LLM training. Preference filtering, rejection sampling, and similar reject-capable stages can instantiate the KB's registered underselection mechanism. A direct reward-gradient update without candidate non-adoption is not a [proposal-selection loop](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md), even if unequal reward sensitivity produces an analogous optimization imbalance; extending the claim to that regime requires a separate argument.

The article's Naur framing is secondary exposition rather than evidence from the original paper, and “code and documentation can never capture the Theory” is stronger than the billing case tests. A sufficiently rich ADR can record a causal model, expected changes, priorities, alternatives, and consequences. It may become stale or omit a later surprise, but that is a capture, freshness, or discrimination problem rather than evidence that design theory is inherently unrepresentable. [The deployed system rather than the model alone is the unit of learning](../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md): an agent system can retain user feedback and revise design records without changing model weights. Static metrics may still contribute weak diagnostic evidence, as the author also concedes; the source only shows that they cannot decide the trade-off alone.

## Recommended Next Action

Update [Weakly discriminated qualities tend to be underselected](../notes/weakly-discriminated-qualities-tend-to-be-underselected.md) with this snapshot as a bounded application: add maintainability selection at code-review and reject-capable training stages, show ADR-supplied change expectations and trade-offs as oracle-strengthening evidence, and state that the source illustrates the mechanism without supplying prevalence evidence or establishing the direct-gradient extension.
