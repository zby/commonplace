---
description: "Distinguishes accumulation from recurrent compounding, examines reflective control of revision decompositions, and presents Commonplace's natural-language theory layer as an unmeasured testbed"
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

> **TL;DR.** A system does not compound merely because it retains improvements. One retained benefit that helps produce a later improvement provides local evidence of compounding. A compounding pathway requires this feedback to recur.
>
> Reflection is neither necessary nor sufficient for compounding. Its proposed advantage is control: explicit theories and revision machinery can expose how improvements are found, judged, and installed—including the decomposition that defines available evidence, problems, and revision targets. Commonplace is a testbed for whether retained natural-language theory can make this machinery usable as a revision surface across heterogeneous changes without retraining model weights. It has paths that install revisions and use them later, but their compounding payoff remains unmeasured.

## Compounding is the payoff

Suppose an agent maintains a deployment policy that its runtime loads. A deployment fails on a Tuesday because a credential expired. The agent mistakes the date for the cause and installs "Never deploy on Tuesdays"; later runs obey. The change is objective-directed and operative, but wrong. Self-improvement describes an improvement-directed process; it does not guarantee that every adopted update helps. A correct policy that reduced failures would be a retained gain. If the system instead installed a causal-evidence check and later used it to diagnose another failure and install a better policy, the check would have helped produce a second improvement.

Useful retained changes can accumulate as later operation depends on them. But [improvements can accumulate without compounding](../notes/improvements-can-accumulate-without-compounding.md). If a system retains useful task rules while each new rule remains just as difficult to find, evaluate, and install, and no saved capacity is reinvested, the gains accumulate while improvement does not compound. A validator that measurably reduces the cost of a later beneficial revision provides local evidence of compounding. A task-facing gain can contribute indirectly, but the path must be specified: the gain frees capacity, an allocation mechanism directs it to improvement work, and a later episode uses it.

The metric used to accept the earlier change cannot by itself show compounding. The [later-episode protocol](../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) asks whether the retained benefit made a subsequent revision cheaper, broader, more reliable, or less human-dependent, and requires a causal trace between the episodes.

## Three diagnostic tests

Apply three tests to a named improvement path:

| Test | Questions |
|---|---|
| **Occurrence** | What boundary, horizon, and objective are declared? Did objective-relevant evidence produce an operative change to the system's own organization, and did a later operation depend on it? |
| **Revision surface** | Which behavior-shaping artifacts and relations form the declared revision surface? Which did the path actually revise, which remain supplied, and does the path remain usable after installation? |
| **Compounding** | Did the retained benefit measurably help produce a later improvement? What causal trace connects the episodes, and has the feedback recurred? |

The harmful Tuesday rule passes occurrence, not compounding.

## Why reflection matters: the revision surface

Consider a harness optimizer that can rewrite a system prompt and three tool descriptions while a fixed test suite decides which edits are promoted. The prompt and tool descriptions are inside its revision surface; the suite controls promotion but remains outside it. If the suite rewards the wrong proxy, prompt-and-tool search can optimize that proxy but cannot repair the selection criterion.

[Reflection](../notes/definitions/reflective-system.md) matters here when a system uses inspectable and revisable artifacts—such as prompts, instructions, memories, tests, validators, and scaffolding—to represent commitments that shape its own operation. A revision becomes operative only after it enters a live path and affects later operation; stored evidence and uninstalled proposals do not.

Compounding does not require reflection: [opaque retained learning can shape later updates](../notes/accumulation-counts-dependence-through-the-retained-result.md). But reflection can make such commitments individually addressable: agents can [name, criticize, revise, or retire](../notes/reflection-buys-addressability.md) them. [Behavioral authority](../notes/definitions/behavioral-authority.md) describes the paths through which retained artifacts shape operation. Addressability is only an affordance; compounding still requires a represented change to help produce a later improvement.

A particularly consequential fixed choice is the [decomposition that defines the effective update space](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md): what counts as evidence, which failures can be represented, and which changes can be proposed. A loop can optimize every exposed component yet remain unable to express that a responsibility is missing or that the components were divided wrongly.

For a reflective artifact system, **complete addressability** asks whether every repository-defined artifact and relation identified by the current account as carrying behavioral authority can be inspected and revised—including the account's own inventory and distinctions. A replacement installed through one revision must remain inspectable and revisable in later episodes. This lets discovered omissions change later audits; it neither makes unknown omissions addressable nor makes the current account final.

## Evidence from reported systems

The table profiles evidence bearing on occurrence and revision surface in six recent systems whose reported paths revise readable artifacts. It is a comparative case set, not a representative survey, and does not describe each system's total capabilities. Here, *supplied* means provided by researchers and left outside the reported revision path. The [detailed evidence inventory](../notes/evidence/six-reported-self-improvement-paths-expose-bounded-redesign-surfaces.md) records the underlying editability, installation, and later-dependence evidence.

| System | Strongest reported revision evidence | Key supplied machinery |
|---|---|---|
| [Self-Harness](../sources/self-harness-harnesses-that-improve-themselves.ingest.md), a same-model harness optimizer | Accepted instruction, runtime-control, and tool-handling edits were merged and exercised in later evaluations. | Control architecture, edit surface, objective, evaluator, and acceptance rule. |
| [Continual Harness](../sources/continual-harness-online-adaptation-foundation-agents.ingest.md), an online embodied-agent refiner | Prompt revisions and repaired skills reached later steps or invocations; many created skills and memory entries did not. | Game interface, harness partition, Refiner rule, reward design, and models. |
| [Autogenesis](../sources/autogenesis-a-self-evolving-agent-protocol.ingest.md), a typed agent-evolution protocol | Committed prompt and agent revisions were reused; several other typed surfaces remain affordances or lack independent evaluation. | Resource ontology, specialist organization, objective, evaluator, and acceptance rule. |
| [Accumulated Behavioral Rules](../sources/self-improving-ai-coding-agents-through-accumulated-rules.ingest.md), a coding-agent rule learner | Rules were installed and loaded by two interfaces; their behavioral effect remains unestablished without a control or per-rule isolation. | Human generalization judgment, rule representation, loading scheme, and review process. |
| [Darwin Gödel Machine](../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md), an archive-based coding-agent evolution method | Archive admission installed a descendant, but only descendants later selected and executed provide evidence that the changed code affected later behavior. | Diagnostician, viability criterion, archive and parent-selection rules, objective, and evaluator. |
| [HyperAgents](../sources/hyperagents.ingest.md), a joint task/meta-agent evolution method | Selected patch lineages revise task code and the meta-agent code that modifies future agents, then replay those changes into later generations. | Main-run objectives and evaluators, parent selection, archive controller, resource budget, and sandbox. |

### What later episodes establish

Among these six systems, HyperAgents supplies the closest later-episode test. Transferred evolved hyperagents, with their agent-modifying components frozen, generated stronger agents for an unseen math-grading task than the initial hyperagent did. Because each hyperagent bundles prompts, insight files, and code, the result does not isolate the causal changes. Continued evolution from transferred rather than fresh hyperagents showed no significant advantage. This establishes one case in which retained changes helped a later agent-generation episode, not recurring feedback.

[Do Agent Optimizers Compound?](../sources/agent-optimizers-compound-terminal-bench.ingest.md) reports that RELAI's Verifiable Continual Learning retained gains after transfer to an expanded task set and improved again during a second optimization phase. The paper calls this compounding. Here it establishes retention, transfer, and further optimization; without an equally budgeted Phase-2 run from a fresh artifact, it cannot show that Phase 1 made Phase 2 more productive.

[Co-Harness](../sources/co-harness-co-evolving-harness-and-model-weights.ingest.md) uses regression-checked harness edits to produce fine-tuning trajectories, then returns the updated model to the next harness round. Accuracy improved across two rounds, but no matched ablation separates this feedback from additional training or harness search alone; larger redesign remains human-supplied. The design could support recurrent compounding under a training-intensive cost profile, but the experiment does not provide a clean causal estimate.

[Knowledge-Centric Self-Improvement](../sources/knowledge-centric-self-improvement-2607.19592.ingest.md) retained natural-language bundles that improved held-out performance across tasks and model families. This establishes accumulation and transfer, but not that the bundles made later curation more productive: transfer froze them, while curation and evaluation machinery remained supplied. Recurrent compounding remains unestablished.

## A proof-governed limit case

The theoretical [Gödel machine](../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md) lets a proof-authorized rewrite replace the machinery governing later rewrites. It must prove that the candidate is better than continuing, excluding beneficial changes its formalization cannot prove superior. This gives it a broad formal revision surface but no empirical evidence of compounding; Commonplace explores a narrower surface under fallible semantic judgment.

## Commonplace as a human-inclusive testbed

If their research teams were inside the six systems' boundaries, they too could plainly redesign their systems. The table excludes those teams, while [Commonplace's boundary](../reference/commonplace-declared-frame.md) includes maintainers, so revision-surface breadth is not directly comparable. Commonplace's claim is not raw human editability, but that retained procedures and artifacts make human–agent redesign part of an explicit operating path whose installed changes remain available for later use and revision.

Commonplace's specific bet is a linked natural-language layer that combines [interpretation and retention](../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md). It keeps claims, assumptions, and scopes separately revisable while an LLM uses them to interpret heterogeneous evidence. By [routing notes individually](../notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md), the system can load only the relevant theory, reducing competition for context as it grows instead of embedding it in Python strings or executable lineages. The hypothesis is that such theories can change how later work is decomposed, rather than only supply matching rules.

[Readable-artifact and weight updates have different cost curves](./the-bitter-lesson-does-not-require-everything-to-live-in-weights.md). Localized text or code changes can avoid a training cycle, while parametric updates may amortize dense changes across many calls and avoid retrieval costs. Comparisons must count training, artifact search, retrieval, evaluation, and maintenance over a declared later-use horizon.

Commonplace's [six-path audit](../notes/evidence/six-commonplace-paths-establish-broad-addressability-not-completeness.md) found broad path-relative addressability, not completeness. It also found that its preliminary behavioral-authority decomposition could not distinguish paths with different applicability conditions. The defect makes that decomposition a revision target. A [live proposal](../reference/proposals/revise-behavioral-authority-decomposition.md) considers replacements, but none has been installed. Separately, the [topic-index case](../reference/tag-readme-trace-observed-causal-connection.md) installed validator machinery that later work reused. Neither case shows that the natural-language theory layer causes compounding.

## What remains to test

Two experiments remain. First, the [objective-level ablation](../reference/proposals/ablation-baselines-for-the-declared-objective.md) asks whether Commonplace earns its total cost by comparing the full framework with raw documentation, episodic examples, the same artifacts without reviews that test whether claims generalize beyond their source cases, and a stronger model. The stronger-model arm needs equivalent repository and tool access.

Second, the later-episode protocol asks whether a retained benefit helps a subsequent improvement, against frozen-artifact or simpler-memory variants. Evidence needs either direct use or a specified path from freed resources, through allocation, to later revision. Tasks should require heterogeneous changes, making it harder for local rule reuse to stand in for theory-mediated reinterpretation. Because an experienced maintainer carries internalized learning across replays, cleaner designs use outside operators or prospectively assigned frozen-artifact controls.

Both experiments should measure revision effort, outcome quality, transfer, and full lifecycle costs, including human judgment, training, and maintenance. One traced case in which an earlier benefit helps produce a later improvement provides local evidence of compounding; a pathway-level claim needs recurring cases.

## Where to go next

The companion draft develops the [human-inclusive revision affordance and audit result](./what-makes-human-inclusive-self-revision-non-trivial.md), while the [self-improving-systems cluster](../notes/self-improving-systems-README.md) maps the underlying theory. Counterexamples and disputed classifications are welcome below.
