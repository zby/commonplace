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

> **TL;DR.** Improvements compound when their benefits help produce further improvements. One such link is local evidence; repeated links establish a compounding pathway.
>
> Reflection is neither necessary nor sufficient for compounding. Its proposed advantage is control: explicit theories and revision machinery can expose how improvements are found, judged, and installed, including the decomposition that defines the available evidence, problems, and revision targets. Within any claimed improvement episode, however, the objective and comparison rule must remain fixed independently of the candidate change. Commonplace is a testbed for whether retained natural-language theory can make this machinery a usable revision surface across heterogeneous changes without retraining model weights. It has paths that install revisions and use them later, but their compounding payoff remains unmeasured.

## Compounding is the payoff

Suppose an agent maintains a deployment policy that its runtime loads. A deployment fails on a Tuesday because a credential expired. The agent mistakes the date for the cause and installs “Never deploy on Tuesdays”; later runs obey. The change is objective-directed and operative, but wrong. Self-improvement describes an improvement-directed process; it does not guarantee that every adopted update helps.

A correct policy that reduced failures would be a retained gain. If the system instead installed a causal-evidence check, then later used that check to diagnose another failure and install a better policy, the check would have helped produce a second improvement. That dependence is the key distinction. Here, *compounding* means positive feedback from a retained improvement into the production of later improvements; it need not be exponential or unbounded.

Useful retained changes can accumulate as later operation comes to depend on them. But [improvements can accumulate without compounding](../notes/improvements-can-accumulate-without-compounding.md). Suppose a system retains useful task rules, yet each new rule remains just as difficult to find, evaluate, and install, and the system reinvests none of the saved capacity. Its gains accumulate, but its improvement process does not compound.

By contrast, a validator that measurably reduces the cost of a later beneficial revision provides local evidence of compounding. A task-facing gain can also contribute indirectly, but the full path must be specified: the gain frees capacity, an allocation mechanism directs that capacity to improvement work, and a later episode uses it.

The metric used to accept the earlier change cannot establish compounding by itself. The [later-episode protocol](../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) instead asks whether the retained benefit made a subsequent revision cheaper, broader, more reliable, or less human-dependent. It also requires a causal trace between the two episodes.

## Three diagnostic tests

Apply three tests to a named improvement path:

| Test | Questions |
|---|---|
| **Occurrence** | What boundary, horizon, and objective are declared? Did objective-relevant evidence produce an operative change to the system's own organization? Did a later operation depend on that change? |
| **Revision surface** | Which behavior-shaping artifacts and relations form the declared revision surface? Which did the path actually revise, which remain supplied, and does the path remain usable after installation? |
| **Compounding** | Did the retained benefit measurably help produce a later improvement? What causal trace connects the episodes, and has the feedback recurred? |

The harmful Tuesday rule passes the occurrence test, but not the compounding test.

## Why reflection matters: the revision surface

Consider a harness optimizer that can rewrite a system prompt and three tool descriptions while a fixed test suite determines which edits are promoted. The prompt and tool descriptions lie inside its revision surface; the suite controls promotion but remains outside it. If the suite rewards the wrong proxy, prompt-and-tool search can optimize that proxy but cannot repair the selection criterion.

[Reflection](../notes/definitions/reflective-system.md) matters when a system represents commitments that shape its own operation in inspectable, revisable artifacts such as prompts, instructions, memories, tests, validators, and scaffolding. A revision becomes operative only when it enters a live path and affects later operation. Stored evidence and uninstalled proposals do not qualify.

Compounding does not require reflection: [opaque retained learning can shape later updates](../notes/accumulation-counts-dependence-through-the-retained-result.md). Reflection can, however, make commitments individually addressable: agents can [name, criticize, revise, or retire](../notes/reflection-buys-addressability.md) them. [Behavioral authority](../notes/definitions/behavioral-authority.md) describes the paths through which retained artifacts shape operation. Addressability is only an affordance; compounding still requires a represented change to help produce a later improvement.

This affordance also needs a stable adjudication boundary. An improvement claim is relative to an [antecedently declared objective](../notes/self-improvement-is-relative-to-a-declared-objective.md). During a comparison, a candidate cannot rewrite the objective, evidence semantics, safety constraints, or cost accounting by which it is judged. Changing those terms requires separate authority; the change cannot license itself as an improvement under the old terms. Reflection can broaden the revisable surface below that boundary, but it cannot eliminate the boundary.

One particularly consequential fixed choice is the [decomposition that defines the effective update space](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md): what counts as evidence, which failures can be represented, and which changes can be proposed. A loop can optimize every exposed component yet remain unable to express that a responsibility is missing or that the components were divided incorrectly.

Addressability is therefore relative to the system's current map of behavioral authority and to its adjudication boundary. The strongest form of this control keeps even that map revisable: if experience reveals a missing authority path or a bad division of responsibilities, the map can be changed and used in later audits. Installed changes must remain inspectable and revisable in later episodes. This does not guarantee that every omission will be discovered or let a candidate redefine the standard by which it is judged.

## Evidence from reported systems

The following table profiles evidence about occurrence and revision surfaces in six recent systems whose reported paths revise readable artifacts. This is a comparative case set, not a representative survey, and it does not describe each system's full capabilities.

Here, *supplied* means provided by researchers and left outside the reported revision path. Supplied machinery is not automatically a defect: an evaluator may serve as an experimental control or safety boundary. The table records what each reported path cannot revise; whether a fixed element is warranted is a separate question. The [detailed evidence inventory](../notes/evidence/six-reported-self-improvement-paths-expose-bounded-redesign-surfaces.md) records the underlying evidence about editability, installation, and later dependence.

| System | Strongest reported revision evidence | Distinctive supplied boundary |
|---|---|---|
| [Self-Harness](../sources/self-harness-harnesses-that-improve-themselves.ingest.md), a same-model harness optimizer | Accepted instruction, runtime-control, and tool-handling edits were merged and exercised in later evaluations. | Control architecture and permitted edit surface. |
| [Continual Harness](../sources/continual-harness-online-adaptation-foundation-agents.ingest.md), an online embodied-agent refiner | Prompt revisions and repaired skills reached later steps or invocations; many created skills and memory entries did not. | Game interface, Refiner rule, and reward design. |
| [Autogenesis](../sources/autogenesis-a-self-evolving-agent-protocol.ingest.md), a typed agent-evolution protocol | Committed prompt and agent revisions were reused; several other typed surfaces remain affordances or lack independent evaluation. | Resource ontology and specialist organization. |
| [Accumulated Behavioral Rules](../sources/self-improving-ai-coding-agents-through-accumulated-rules.ingest.md), a coding-agent rule learner | Rules were installed and loaded by two interfaces; their behavioral effect remains unestablished without a control or per-rule isolation. | Human generalization judgment and loading scheme. |
| [Darwin Gödel Machine](../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md), an archive-based coding-agent evolution method | Archive admission installed a descendant, but only descendants later selected and executed provide evidence that the changed code affected later behavior. | Archive, parent selection, and viability criterion. |
| [HyperAgents](../sources/hyperagents.ingest.md), a joint task/meta-agent evolution method | Selected patch lineages revise task code and the meta-agent code that modifies future agents, then replay those changes into later generations. | Main-run evaluators, parent selection, archive controller, and budget. |

### What later episodes establish

Among these six systems, HyperAgents provides the closest later-episode test. Transferred evolved hyperagents, with their agent-modifying components frozen, generated stronger agents for an unseen math-grading task than the initial hyperagent did. Because each hyperagent bundles prompts, insight files, and code, however, the result does not isolate the causal changes. Continued evolution from transferred rather than fresh hyperagents showed no significant advantage. The result therefore establishes one case in which retained changes helped a later agent-generation episode, but not recurrent feedback.

Other reported later-episode results reach the same boundary through different mechanisms:

| System | What the evidence establishes | Missing comparison |
|---|---|---|
| [RELAI-VCL](../sources/agent-optimizers-compound-terminal-bench.ingest.md), a continual harness optimizer | Retention, transfer to an expanded task set, and further optimization. | An equally budgeted second phase from a fresh artifact, needed to show that Phase 1 made Phase 2 more productive. |
| [Co-Harness](../sources/co-harness-co-evolving-harness-and-model-weights.ingest.md) | Two rounds in which checked harness edits produce training trajectories and the updated model returns for the next harness round. | A matched controlled comparison that separates feedback from additional training or harness search. |
| [Knowledge-Centric Self-Improvement](../sources/knowledge-centric-self-improvement-2607.19592.ingest.md) | Natural-language bundles that accumulate and transfer across tasks and model families. | A later curation episode in which retained bundles, rather than supplied curation machinery, improve revision productivity. |

None of these results establishes recurrent compounding.

## A proof-governed limit case

The theoretical [Gödel machine](../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md) permits a proof-authorized rewrite to replace the machinery governing later rewrites. It must prove that a candidate is better than continuing, which excludes beneficial changes that its formalization cannot prove superior. This gives the Gödel machine a broad formal revision surface, but no empirical evidence of compounding. Commonplace explores a narrower surface under fallible semantic judgment.

## Commonplace as a human-inclusive testbed

If the research teams behind the six systems were included within their systems' boundaries, those teams could plainly redesign the systems. The table excludes them, whereas [Commonplace's boundary](../reference/commonplace-declared-frame.md) includes maintainers. Revision-surface breadth is therefore not directly comparable.

Commonplace's claim is not merely that humans can edit it. The claim is that retained procedures and artifacts make human–agent redesign part of an explicit operating path, and that installed changes remain available for later use and revision.

Commonplace's specific bet is on a linked natural-language layer that combines [interpretation and retention](../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md). It keeps claims, assumptions, and scopes separately revisable while an LLM uses them to interpret heterogeneous evidence. By [routing notes individually](../notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md), the system can load only the relevant theory. This reduces competition for context as the system grows, rather than embedding the theory in Python strings or executable lineages. The hypothesis is that such theories can change how later work is decomposed, not merely supply matching rules.

Whether this text layer earns its full lifecycle cost relative to code or weight updates is a separate question. The [cost-focused companion](./the-bitter-lesson-does-not-require-everything-to-live-in-weights.md) and the [objective-level comparison proposal](../reference/proposals/ablation-baselines-for-the-declared-objective.md) develop it further.

Commonplace's [six-path audit](../notes/evidence/six-commonplace-paths-establish-broad-addressability-not-completeness.md) found many artifacts that could be inspected and revised along the audited paths, but it did not establish that every behavior-shaping artifact was covered. The audit also found that the preliminary behavioral-authority decomposition could not represent the applicability conditions needed to distinguish when different paths can operate. That limitation makes the decomposition itself a revision target. A [live proposal](../reference/proposals/revise-behavioral-authority-decomposition.md) considers replacements, but none has been installed.

Separately, the [topic-index case](../reference/tag-readme-trace-observed-causal-connection.md) installed validator machinery that later work reused. Neither case shows that the natural-language theory layer causes compounding.

## What remains to test

Two experiments remain.

First, the [objective-level ablation](../reference/proposals/ablation-baselines-for-the-declared-objective.md)—a controlled comparison that removes or replaces parts of the framework—would test whether Commonplace earns its total lifecycle cost. Its proposed comparison arms belong in that experimental design, not in this article.

Second, the later-episode protocol would test whether a retained benefit helps produce a subsequent improvement, compared with frozen-artifact or simpler-memory variants. The evidence must show either direct use of the benefit or a specified path from freed resources, through allocation, to later revision. Tasks should require heterogeneous changes so that local rule reuse cannot easily stand in for theory-mediated reinterpretation. Because an experienced maintainer carries internalized learning across replays, cleaner designs would use outside operators or prospectively assigned frozen-artifact controls.

Both experiments should measure revision effort, outcome quality, transfer, and full lifecycle costs, including human judgment, training, and maintenance.

## Where to go next

The companion draft develops the [human-inclusive revision affordance and audit result](./what-makes-human-inclusive-self-revision-non-trivial.md), while the [self-improving-systems cluster](../notes/self-improving-systems-README.md) maps the underlying theory. Counterexamples and disputed classifications are welcome below.
