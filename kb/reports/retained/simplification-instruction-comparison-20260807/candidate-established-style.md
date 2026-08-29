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

> **Draft.** This article is circulating for comments; its claims, structure, and even its central thesis may still change. Comments are welcome below.

> **TL;DR.** Improvements compound when their benefits feed into further improvements. A single such link is local evidence; repeated links establish a compounding pathway.
>
> Compounding can occur without reflection, and reflection alone does not produce it. But reflection's proposed advantage is control: it can make the theories and machinery behind improvement visible and revisable, including how the system defines evidence, problems, and possible changes. Each episode still needs an objective and comparison rule that the candidate cannot change. Commonplace tests whether retained natural-language theory can provide this control across heterogeneous changes without retraining model weights. It can install and reuse revisions, but has not yet shown compounding through its theory layer.

## Compounding is the payoff

Suppose an agent maintains a deployment policy that its runtime loads. A deployment fails on a Tuesday because a credential expired. The agent mistakes the date for the cause and installs “Never deploy on Tuesdays”; later runs obey. The change is objective-directed and operative, but wrong. Calling this process self-improving describes its objective, not the outcome of every update.

A correct policy that reduced failures would be a retained gain. If the system instead installed a causal-evidence check and later used it to diagnose another failure and install a better policy, the second improvement would depend on the check. The key distinction is *compounding*: an improvement's benefit feeds back into producing later improvements. The feedback need not be exponential or continue indefinitely.

A system can retain many useful task rules even when each new rule remains just as hard to find, evaluate, and install. If the system does not reinvest the time or resources those rules save, the rules improve task performance without changing how the next improvement is produced: [improvements accumulate without compounding](../notes/improvements-can-accumulate-without-compounding.md).

By contrast, a validator that measurably reduces the cost of a later beneficial revision is local evidence of compounding. A task-facing gain can feed back indirectly if three things happen: it frees capacity, an allocation mechanism directs that capacity to improvement work, and a later episode uses the capacity to produce an improvement. That path must be shown, not assumed.

The acceptance metric tells us whether a change met its target, not whether that change made the next revision more productive. The [later-episode protocol](../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) therefore asks whether the retained benefit made a subsequent revision cheaper, broader, more reliable, or less human-dependent. It also requires a causal trace between the two episodes.

## Three diagnostic tests

Apply three tests to a named improvement path:

| Test | Questions |
|---|---|
| **Occurrence** | What system boundary, time horizon, and objective are in scope? Did relevant evidence change the system's own organization? Did later behavior use that change? |
| **Revision surface** | Which behavior-shaping artifacts and relations could this path revise? Which did it actually revise, which stayed fixed, and could the path still be used afterward? |
| **Compounding** | Did a later improvement measurably depend on the retained benefit? How were the episodes connected, and has this happened repeatedly? |

The harmful Tuesday rule passes the occurrence test, but not the compounding test.

## Why reflection matters: the revision surface

Consider a harness optimizer that can rewrite a system prompt and three tool descriptions. A fixed test suite determines which edits are promoted. The prompt and tool descriptions lie inside the optimizer's revision surface; the suite controls promotion but remains outside that surface. If the suite rewards the wrong proxy, prompt-and-tool search can optimize that proxy but cannot repair the selection criterion.

In an artifact system, [reflection](../notes/definitions/reflective-system.md) represents commitments that shape the system's own operation in inspectable, revisable artifacts: prompts, instructions, memories, tests, validators, and scaffolding. A revision becomes operative only when it enters a live path and affects later behavior; storing evidence or a proposal is not enough.

[Opaque retained learning can also compound](../notes/accumulation-counts-dependence-through-the-retained-result.md). Reflection adds addressability: agents can [name, criticize, revise, or retire](../notes/reflection-buys-addressability.md) individual commitments. [Behavioral authority](../notes/definitions/behavioral-authority.md) maps how retained artifacts shape operation. Addressability gives agents more control over revision, but it does not cause compounding; a later improvement must still depend on a represented change.

A candidate cannot set the standard by which it is judged. Each improvement episode needs an [objective](../notes/self-improvement-is-relative-to-a-declared-objective.md) and a comparison rule, both fixed before evaluation. Changing that standard requires a separate revision and separate authority. Reflection can expose more of the system to revision, but it cannot make a change its own judge.

The system's current [decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) determines what it can notice and change: what counts as evidence, which failures it can represent, and which revisions it can propose. A loop can optimize every named component yet have no way to say that a responsibility is missing or that the components were divided badly.

The strongest form of this control also lets the system revise its map of what shapes behavior. If experience reveals a missing authority path or a bad division of responsibilities, the system can update the map and use the revised version in later audits. The revised map must remain open to later inspection and revision. This does not guarantee that every omission will be found.

## Evidence from reported systems

The table asks what each of six recent systems changed, what evidence shows later use, and what remained outside the reported revision path. All six revise readable artifacts. This is a comparative case set, not a representative survey or an account of each system's full capabilities.

Here, *supplied* means that researchers provided an element and the reported revision path left it fixed. A supplied element is not automatically a defect: an evaluator may serve as an experimental control or safety boundary. The table records the fixed boundary, not whether it was warranted. The [detailed evidence inventory](../notes/evidence/six-reported-self-improvement-paths-expose-bounded-redesign-surfaces.md) documents editability, installation, and later dependence.

| System | Strongest reported revision evidence | Distinctive supplied boundary |
|---|---|---|
| [Self-Harness](../sources/self-harness-harnesses-that-improve-themselves.ingest.md), a same-model harness optimizer | Accepted edits to instructions, runtime control, and tool handling were merged and exercised in later evaluations. | Control architecture and permitted edit surface. |
| [Continual Harness](../sources/continual-harness-online-adaptation-foundation-agents.ingest.md), an online embodied-agent refiner | Prompt revisions and repaired skills reached later steps or invocations; many created skills and memory entries did not. | Game interface, Refiner rule, and reward design. |
| [Autogenesis](../sources/autogenesis-a-self-evolving-agent-protocol.ingest.md), a typed agent-evolution protocol | Committed prompt and agent revisions were reused; several other typed surfaces remain affordances or lack independent evaluation. | Resource ontology and specialist organization. |
| [Accumulated Behavioral Rules](../sources/self-improving-ai-coding-agents-through-accumulated-rules.ingest.md), a coding-agent rule learner | Rules were installed and loaded by two interfaces; their behavioral effect remains unestablished without a control or per-rule isolation. | Human generalization judgment and loading scheme. |
| [Darwin Gödel Machine](../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md), an archive-based coding-agent evolution method | Archive admission installed a descendant. Only descendants selected and executed later provide evidence that the changed code affected later behavior. | Archive, parent selection, and viability criterion. |
| [HyperAgents](../sources/hyperagents.ingest.md), a joint task/meta-agent evolution method | Selected patch lineages revise task code and the meta-agent code that modifies future agents, then replay those changes into later generations. | Main-run evaluators, parent selection, archive controller, and budget. |

### What later episodes establish

Among these six systems, HyperAgents provides the closest later-episode test. Transferred evolved hyperagents, with their agent-modifying components frozen, generated stronger agents for an unseen math-grading task than the initial hyperagent did. However, because each hyperagent bundles prompts, insight files, and code, the result does not isolate the causal changes. Continued evolution from transferred hyperagents showed no significant advantage over continued evolution from fresh ones. This shows that retained changes improved one later agent-generation episode, not that the feedback recurred.

Three other systems provide related but incomplete evidence:

| System | What the evidence establishes | Missing comparison |
|---|---|---|
| [RELAI-VCL](../sources/agent-optimizers-compound-terminal-bench.ingest.md), a continual harness optimizer | Retention, transfer to an expanded task set, and further optimization. | An equally budgeted second phase from a fresh artifact, needed to show that Phase 1 made Phase 2 more productive. |
| [Co-Harness](../sources/co-harness-co-evolving-harness-and-model-weights.ingest.md) | Two rounds in which checked harness edits produce training trajectories and the updated model returns for the next harness round. | A matched controlled comparison that separates feedback from additional training or harness search. |
| [Knowledge-Centric Self-Improvement](../sources/knowledge-centric-self-improvement-2607.19592.ingest.md) | Natural-language bundles that accumulate and transfer across tasks and model families. | A later curation episode in which retained bundles, rather than supplied curation machinery, improve revision productivity. |

None of these results establishes recurrent compounding.

## A proof-governed limit case

A theoretical [Gödel machine](../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md) can rewrite even the machinery that chooses later rewrites, but only after proving that the candidate is better than continuing. Even beneficial changes are excluded when the machine cannot prove that adopting them is better than continuing. It therefore has a broad formal revision surface, but no empirical evidence of compounding. Commonplace studies a narrower surface under fallible semantic judgment.

## Commonplace as a human-inclusive testbed

The six systems' revision surfaces look narrower partly because the comparison excludes their research teams. [Commonplace's boundary](../reference/commonplace-declared-frame.md) includes maintainers, so revision-surface breadth is not directly comparable: those teams could plainly redesign their systems too.

Commonplace's claim is not merely that humans can edit it. It is that retained procedures and artifacts make human–agent redesign an explicit operating path whose installed changes remain available for later use and revision.

Commonplace's specific bet is that linked natural-language theory can be both [interpreted and retained](../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md). Its claims, assumptions, and scopes remain separately revisable while an LLM applies them to heterogeneous evidence. Because notes are [routed individually](../notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md), agents can load selected theory instead of the whole layer. This routing is intended to limit competition for context. Storing theory in notes also separates it from Python strings and executable lineages. The hypothesis is that such theories can change how later work is decomposed, not merely supply matching rules.

Whether this text layer earns its full lifecycle cost relative to code or weight updates is a separate question. The [cost-focused companion](./the-bitter-lesson-does-not-require-everything-to-live-in-weights.md) and the [objective-level comparison proposal](../reference/proposals/ablation-baselines-for-the-declared-objective.md) develop it further.

Commonplace's [six-path audit](../notes/evidence/six-commonplace-paths-establish-broad-addressability-not-completeness.md) identified many behavior-shaping artifacts that could be inspected and revised, but could not show that it found them all. The audit also exposed a flaw in Commonplace's own model of behavioral authority: the model could not express when different authority paths apply. That model is now a revision target. A [live proposal](../reference/proposals/revise-behavioral-authority-decomposition.md) considers replacements, but none has been installed.

Separately, the [topic-index case](../reference/tag-readme-trace-observed-causal-connection.md) installed validator machinery that later work reused. Neither case shows that the natural-language theory layer causes compounding.

## What remains to test

Two experiments remain.

First, the [objective-level ablation](../reference/proposals/ablation-baselines-for-the-declared-objective.md) would compare the full framework with variants that remove or replace parts of it, testing whether Commonplace earns its total lifecycle cost.

Second, the later-episode experiment would compare Commonplace with frozen-artifact and simpler-memory variants. It must trace how a later revision depends on an earlier benefit, either directly or through resources that are freed and deliberately reinvested. Tasks should require heterogeneous changes so that local rule reuse cannot easily stand in for theory-mediated reinterpretation. Using outside operators—or assigning maintainers to conditions before any episode—would help separate the artifacts' effects from what an experienced maintainer remembers.

Both experiments should measure revision effort, outcome quality, transfer, and full lifecycle costs, including human judgment, training, and maintenance.

## Where to go next

The companion draft develops the [human-inclusive revision affordance and audit result](./what-makes-human-inclusive-self-revision-non-trivial.md), while the [self-improving-systems cluster](../notes/self-improving-systems-README.md) maps the underlying theory. Counterexamples and disputed classifications are welcome below.
