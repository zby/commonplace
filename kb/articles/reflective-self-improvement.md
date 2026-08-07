---
description: "Distinguishes accumulation from recurrent compounding, examines reflective control over revision decompositions, and presents Commonplace's natural-language theory layer as an unmeasured testbed"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/definitions/self-improving-system.md
  - kb/notes/definitions/behavior-determining-organization.md
  - kb/notes/definitions/behavioral-authority.md
  - kb/notes/definitions/reflective-system.md
  - kb/notes/reflection-buys-addressability.md
  - kb/notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md
  - kb/notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md
  - kb/notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md
  - kb/notes/theory-and-methodology-form-a-two-layer-execution-system.md
  - kb/notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md
  - kb/notes/accumulation-counts-dependence-through-the-retained-result.md
  - kb/notes/improvements-can-accumulate-without-compounding.md
  - kb/notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md
  - kb/notes/self-improvement-is-relative-to-a-declared-objective.md
  - kb/notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md
  - kb/notes/a-repeatable-operative-path-keeps-a-redesign-class-open-to-revision.md
  - kb/notes/evidence/six-reported-self-improvement-paths-expose-bounded-redesign-surfaces.md
  - kb/notes/evidence/six-commonplace-paths-establish-broad-addressability-not-completeness.md
  - kb/reference/commonplace-declared-frame.md
  - kb/reference/proposals/ablation-baselines-for-the-declared-objective.md
  - kb/reference/proposals/revise-behavioral-authority-decomposition.md
  - kb/reference/tag-readme-trace-observed-causal-connection.md
  - kb/sources/self-harness-harnesses-that-improve-themselves.ingest.md
  - kb/sources/continual-harness-online-adaptation-foundation-agents.ingest.md
  - kb/sources/autogenesis-a-self-evolving-agent-protocol.ingest.md
  - kb/sources/self-improving-ai-coding-agents-through-accumulated-rules.ingest.md
  - kb/sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md
  - kb/sources/hyperagents.ingest.md
  - kb/sources/co-harness-co-evolving-harness-and-model-weights.ingest.md
  - kb/sources/agent-optimizers-compound-terminal-bench.ingest.md
  - kb/sources/knowledge-centric-self-improvement-2607.19592.ingest.md
---

# Reflective self-improvement

> **Draft.** This article is circulating for comments; its claims, structure, and central thesis may still change. Counterexamples and disputed classifications are welcome below.

> **TL;DR.** Improvements compound when their benefits feed into further improvements. One such link is local evidence; repeated links establish a compounding pathway.
>
> Compounding can occur without reflection, and reflection alone does not produce it. But reflection can give a system more control over improvement by making its underlying theories and machinery revisable, including what counts as evidence, what counts as a problem, and which changes it can consider. Each candidate must still be judged against an objective and comparison rule that it cannot change. Commonplace is our attempt to test whether retained natural-language theory can provide this control across heterogeneous changes without retraining model weights. We can show that it installs and reuses revisions. We have not yet traced a case in which a retained theory-layer improvement helped produce a later improvement, let alone shown that this feedback recurs. This is a limit of our current evidence, not a finding that Commonplace cannot compound.

## Compounding is the payoff

Suppose an agent maintains a deployment policy. A deployment fails on a Tuesday because a credential expired. The agent mistakes the date for the cause and installs “Never deploy on Tuesdays”; later runs obey. The example shows that [*self-improving*](../notes/definitions/self-improving-system.md) describes the process's objective, not the result of every update: the agent changes its own policy in pursuit of improvement but installs a bad rule.

A correct policy that reduced failures would be a retained gain. If the system instead installed a causal-evidence check and later used it to diagnose another failure and install a better policy, the second improvement would depend on the earlier check. This is local evidence of *compounding*: an improvement's benefit helped produce a later improvement. The feedback must recur to establish a compounding pathway, but need not produce exponential growth or continue indefinitely.

A system can retain many useful task rules even if each new rule remains just as hard to find, evaluate, and install. Unless it reinvests the time or resources those rules save, task performance improves but the process that produces the next improvement does not: [improvements accumulate without compounding](../notes/improvements-can-accumulate-without-compounding.md).

By contrast, a validator that measurably reduces the cost of a later beneficial revision is local evidence of compounding. A task-facing gain can feed back indirectly if it frees capacity, an allocation mechanism directs that capacity to improvement work, and a later episode uses it to produce an improvement. That path must be shown, not assumed.

A change's acceptance metric shows whether it met its target, not whether it made the next revision more productive. The [later-episode protocol](../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) therefore asks whether the retained benefit made a subsequent revision cheaper, broader, more reliable, or less human-dependent. It also requires a causal trace between the episodes.

## Three diagnostic tests

Apply three tests to a named improvement path:

| Test | Questions |
|---|---|
| **Occurrence** | What system boundary, time horizon, and objective are in scope? Did relevant evidence change the system's own organization? Did later behavior use that change? |
| **Revision surface** | Which behavior-shaping artifacts and relations could this path revise? Which did it actually revise, which stayed fixed, and could the path still be used afterward? |
| **Compounding** | Did a later improvement measurably depend on the retained benefit? How were the episodes connected, and has this happened repeatedly? |

The harmful Tuesday rule passes the occurrence test, but not the compounding test.

## Why reflection matters: the revision surface

Consider a harness optimizer that can rewrite a system prompt and three tool descriptions while a fixed test suite determines which edits are promoted. The prompt and tool descriptions lie inside its revision surface; the suite controls promotion but remains outside it. If the suite rewards the wrong proxy, prompt-and-tool search can optimize that proxy but cannot repair the selection criterion.

In an artifact system, [reflection](../notes/definitions/reflective-system.md) represents behavior-shaping commitments in inspectable, revisable artifacts: prompts, instructions, memories, tests, validators, and scaffolding. A revision becomes operative only when a later operation uses it through a live path; stored evidence or a proposal is not enough.

[Opaque retained learning can compound too](../notes/accumulation-counts-dependence-through-the-retained-result.md). Reflection adds addressability: agents can [name, criticize, revise, or retire](../notes/reflection-buys-addressability.md) individual commitments. [Behavioral authority](../notes/definitions/behavioral-authority.md) maps how retained artifacts shape operation. Addressability gives agents control over individual commitments, but it does not cause compounding; a later improvement must still depend on a represented change.

A candidate cannot set its own judging standard. Each improvement episode needs an [objective](../notes/self-improvement-is-relative-to-a-declared-objective.md) and comparison rule fixed before evaluation. Changing the standard is another revision and must be authorized independently. Reflection can expose more of the system to revision, but it cannot make a change its own judge.

The system's current [decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) determines what it can notice and change: what counts as evidence, which failures it can represent, and which revisions it can propose. A loop can optimize every named component yet lack a way to represent that a responsibility is missing or that the components were divided badly.

At its strongest, this control lets the system revise the map of what shapes behavior. If experience reveals a missing authority path or a bad division of responsibilities, the system can update the map and use it in later audits. Any replacement must remain open to inspection and revision. None of this guarantees that every omission will be found.

## Evidence from reported systems

The table compares six recent systems whose reported paths revise readable artifacts. It asks what each path changed, what evidence shows later use, and what the path could not revise. This is neither a representative survey nor an account of each system's full capabilities.

Here, *supplied* means that researchers provided an element and the reported path left it fixed. That is not necessarily a defect: an evaluator may serve as an experimental control or safety boundary. The table records the boundary, not whether it was warranted. The [detailed evidence inventory](../notes/evidence/six-reported-self-improvement-paths-expose-bounded-redesign-surfaces.md) documents editability, installation, and later dependence.

| System | Strongest reported revision evidence | Distinctive supplied boundary |
|---|---|---|
| [Self-Harness](../sources/self-harness-harnesses-that-improve-themselves.ingest.md), a same-model harness optimizer | Accepted instruction, runtime-control, and tool-handling edits were merged and exercised in later evaluations. | Control architecture and permitted edit surface. |
| [Continual Harness](../sources/continual-harness-online-adaptation-foundation-agents.ingest.md), an online embodied-agent refiner | Prompt revisions and repaired skills reached later steps or invocations; many created skills and memory entries did not. | Game interface, Refiner rule, and reward design. |
| [Autogenesis](../sources/autogenesis-a-self-evolving-agent-protocol.ingest.md), a typed agent-evolution protocol | Committed prompt and agent revisions were reused; several other typed surfaces remain affordances or lack independent evaluation. | Resource ontology and specialist organization. |
| [Accumulated Behavioral Rules](../sources/self-improving-ai-coding-agents-through-accumulated-rules.ingest.md), a coding-agent rule learner | Rules were installed and loaded by two interfaces; their behavioral effect remains unestablished without a control or per-rule isolation. | Human generalization judgment and loading scheme. |
| [Darwin Gödel Machine](../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md), an archive-based coding-agent evolution method | Archive admission installed a descendant, but only descendants later selected and executed provide evidence that the changed code affected later behavior. | Archive, parent selection, and viability criterion. |
| [HyperAgents](../sources/hyperagents.ingest.md), a joint task/meta-agent evolution method | Selected patch lineages revise task code and the meta-agent code that modifies future agents, then replay those changes into later generations. | Main-run evaluators, parent selection, archive controller, and budget. |

### What later episodes establish

Among these six systems, HyperAgents has the closest later-episode test. Transferred evolved hyperagents, with their agent-modifying components frozen, generated stronger agents for an unseen math-grading task than the initial hyperagent did. However, the result does not isolate the causal changes because each hyperagent bundles prompts, insight files, and code. Continued evolution from transferred rather than fresh hyperagents showed no significant advantage. This shows that retained changes improved one later agent-generation episode, not that the feedback recurred.

Three other systems provide related but incomplete evidence:

| System | What the evidence establishes | Missing comparison |
|---|---|---|
| [RELAI-VCL](../sources/agent-optimizers-compound-terminal-bench.ingest.md), a continual harness optimizer | Retention, transfer to an expanded task set, and further optimization. | An equally budgeted second phase from a fresh artifact, needed to show that Phase 1 made Phase 2 more productive. |
| [Co-Harness](../sources/co-harness-co-evolving-harness-and-model-weights.ingest.md), a harness-and-model co-evolution method | Two rounds in which checked harness edits produce training trajectories and the updated model returns for the next harness round. | A matched controlled comparison that separates feedback from additional training or harness search. |
| [Knowledge-Centric Self-Improvement](../sources/knowledge-centric-self-improvement-2607.19592.ingest.md) | Natural-language bundles that accumulate and transfer across tasks and model families. | A later curation episode in which retained bundles, rather than supplied curation machinery, improve revision productivity. |

None of these results establishes recurrent compounding.

## A proof-governed limit case

A theoretical [Gödel machine](../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md) can rewrite even the machinery that chooses later rewrites, but only after proving that switching to the candidate now has greater expected utility than keeping its current code running while the search for other rewrites continues. Beneficial changes it cannot prove are excluded. It therefore has a broad formal revision surface, but no empirical evidence of compounding. Commonplace studies a narrower surface under fallible semantic judgment.

## Commonplace as a human-inclusive testbed

The six systems look narrower partly because the comparison excludes their research teams. [Commonplace's boundary](../reference/commonplace-declared-frame.md) includes maintainers, so revision-surface breadth is not directly comparable; those teams could redesign their systems too. Commonplace claims more than human editability: retained procedures and artifacts make human–agent redesign an explicit operating path whose installed changes remain available for later use and revision.

Commonplace bets that linked natural-language theory can be both [interpreted and retained](../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md). Its claims, assumptions, and scopes remain separately revisable while an LLM applies them to heterogeneous evidence. Because notes are [routed individually](../notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md), agents can load selected theory instead of the whole layer. This design is intended to limit competition for context. Separate notes also keep theory out of Python strings and executable lineages. More strongly, such theories may change how later work is decomposed, not merely supply matching rules.

Commonplace's [six-path audit](../notes/evidence/six-commonplace-paths-establish-broad-addressability-not-completeness.md) identified many behavior-shaping artifacts that could be inspected and revised, but could not show that it found them all. It also exposed a flaw in its model of behavioral authority: the model could not express when different authority paths apply. That model is now a revision target. A [live proposal](../reference/proposals/revise-behavioral-authority-decomposition.md) considers replacements, but none has been installed.

Separately, the [topic-index case](../reference/tag-readme-trace-observed-causal-connection.md) installed validator machinery that later work reused. Neither case shows that the natural-language theory layer causes compounding.

## What remains to test

Two experiments remain.

First, the [objective-level ablation](../reference/proposals/ablation-baselines-for-the-declared-objective.md) would compare the full framework with variants that remove or replace parts of it, testing whether Commonplace earns its total lifecycle cost. The [cost-focused companion](./the-bitter-lesson-does-not-require-everything-to-live-in-weights.md) provides the broader text-versus-weight context.

Second, the later-episode experiment would compare Commonplace with frozen-artifact and simpler-memory variants. It must trace how a later revision depends on an earlier benefit, either directly or through resources that are freed and deliberately reinvested. Tasks should require heterogeneous changes that include revising the problem decomposition, not merely a mix of local edits; otherwise matched rules may mimic theory-mediated reinterpretation. Using outside operators—or assigning maintainers to conditions before any episode—would help separate the artifacts' effects from what an experienced maintainer remembers.

Both experiments should measure revision effort, outcome quality, transfer, and full lifecycle costs, including human judgment, training, and maintenance.

## Where to go next

The companion draft develops the [human-inclusive revision affordance and audit result](./what-makes-human-inclusive-self-revision-non-trivial.md), while the [self-improving-systems cluster](../notes/self-improving-systems-README.md) maps the underlying theory.
