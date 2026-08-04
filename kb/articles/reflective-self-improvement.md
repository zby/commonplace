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

> **TL;DR.** A system does not compound merely because it retains improvements. Evidence begins when an earlier benefit measurably helps produce a later improvement; repeated contributions establish a compounding pathway.
>
> Reflection is neither necessary nor sufficient for that feedback. Its proposed advantage is control: explicit theories and revision machinery can expose how improvements are found, judged, and installed—including the decomposition that defines available evidence, problems, and revision targets. Commonplace is a testbed for whether retained natural-language theory can make that surface usable across heterogeneous changes without retraining model weights. Commonplace has operative revision paths, but their compounding payoff remains unmeasured.

## Compounding is the payoff

Suppose a system comprises an agent, its standing deployment policy, and the runtime that loads it. A deployment fails on a Tuesday because a credential expired. The agent mistakes the date for the cause and changes its policy to "Never deploy on Tuesdays." Later runs obey the new policy. The failure supplied evidence relevant to the objective of reducing deployment failures, and the change became operative, but the causal inference was wrong. Self-improvement names an improvement-directed pathway, not a guarantee that every adopted update helps. Had the diagnosis been correct and the resulting policy reduced later failures, dependence on that policy would establish a retained gain. If the system instead installed a causal-evidence check that later supported a useful policy revision, the first improvement would have helped produce a second.

Useful retained changes can accumulate as later operation depends on them. But [improvements can accumulate without compounding](../notes/improvements-can-accumulate-without-compounding.md): a benefit contributes only when it helps produce a later improvement. A validator that makes a later revision cheaper qualifies; consulting a static manual during ordinary operation shows only accumulation. A task-facing gain contributes indirectly only when saved time, compute, or judgment demonstrably returns to improvement work.

Evidence for compounding therefore comes from later episodes and uses a measure other than the one that accepted the earlier change. The [later-episode protocol](../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) pairs a measure of cheaper, broader, more reliable, or less human-dependent improvement with a causal trace.

## Three diagnostic tests

Apply three tests to a named improvement path:

| Test | Questions |
|---|---|
| **Occurrence** | What boundary, horizon, and objective are declared? Did objective-relevant evidence produce an operative change to the system's own organization, and did a later operation depend on it? |
| **Revision surface** | Which behavior-shaping artifacts and relations form the declared revision surface? Which did the path actually revise, which remain supplied, and does the path remain usable after installation? |
| **Compounding** | Did the retained benefit measurably help produce a later improvement? What causal trace connects the episodes, and has the feedback recurred? |

The harmful Tuesday change passes occurrence, not compounding. A later use of the causal-evidence check could provide local evidence, but not recurrence.

## Why reflection matters: the revision surface

Consider a harness optimizer that can rewrite a system prompt and three tool descriptions while a fixed test suite decides which edits are promoted. The prompt and tool descriptions are inside its revision surface; the suite controls promotion but remains outside it. If the suite rewards the wrong proxy, prompt-and-tool search can optimize that proxy but cannot repair the selection criterion.

Self-change need not touch model weights: prompts, instructions, memories, tests, validators, and scaffolding can determine later behavior. A [self-representation](../notes/definitions/reflective-system.md) describes some declared aspect of the same system and participates causally in its operation. Reflective [self-improvement](../notes/definitions/self-improving-system.md) routes objective-relevant evidence into the system's [behavior-determining organization](../notes/definitions/behavior-determining-organization.md) through such a representation. The change must enter a live path and affect a subsequent operation; a stored trace or uninstalled proposal does not close the path.

Compounding does not require reflection: [opaque retained learning can shape later updates](../notes/accumulation-counts-dependence-through-the-retained-result.md). Reflection can make a represented commitment addressable. Given a reliable retrieval and revision path, an agent can [name, criticize, revise, or retire](../notes/reflection-buys-addressability.md) it individually. [Behavioral authority](../notes/definitions/behavioral-authority.md) records how the commitment shapes operation: who consumes it, through which channel, and with what force. Addressability is an upstream affordance, not evidence of compounding; it matters only when a represented change is retrieved and measurably helps produce a later improvement.

A particularly consequential fixed choice is the [decomposition that defines the effective update space](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md): what counts as evidence, which failures can be represented, and which changes can be proposed. A loop can optimize every exposed component yet remain unable to express that a responsibility is missing or that the components were divided wrongly.

For a reflective artifact system, its account of behavioral authority is itself one consequential decomposition. **Complete addressability of behavioral authority** asks whether every repository-defined authority artifact and relation identified by the current account can be inspected, criticized, and revised. The account's inventory and organizing distinctions must also remain revisable. An artifact may govern one episode and become a target in another; when its successor enters an authority-bearing path, it falls under the same coverage test. Revisability lets discovered omissions alter later audits. It does not make unknown omissions addressable or turn the current account into a final ontology.

## Evidence from reported systems

The table profiles evidence bearing on occurrence and revision surface in six recent systems whose reported paths revise readable artifacts. It is a comparative case set, not a representative survey, and does not describe each system's total capabilities. The [detailed evidence inventory](../notes/evidence/six-reported-self-improvement-paths-expose-bounded-redesign-surfaces.md) records the underlying editability, installation, and later-dependence evidence.

| System | Strongest reported revision evidence | Key supplied machinery |
|---|---|---|
| [Self-Harness](../sources/self-harness-harnesses-that-improve-themselves.ingest.md), a same-model harness optimizer | Accepted instruction, runtime-control, and tool-handling edits were merged and exercised in later evaluations. | Control architecture, edit surface, objective, evaluator, and acceptance rule. |
| [Continual Harness](../sources/continual-harness-online-adaptation-foundation-agents.ingest.md), an online embodied-agent refiner | Prompt revisions and repaired skills reached later steps or invocations; many created skills and memory entries did not. | Game interface, harness partition, Refiner rule, reward design, and models. |
| [Autogenesis](../sources/autogenesis-a-self-evolving-agent-protocol.ingest.md), a typed agent-evolution protocol | Committed prompt and agent revisions were reused; several other typed surfaces remain affordances or lack independent evaluation. | Resource ontology, specialist organization, objective, evaluator, and acceptance rule. |
| [Accumulated Behavioral Rules](../sources/self-improving-ai-coding-agents-through-accumulated-rules.ingest.md), a coding-agent rule learner | Rules were installed and loaded by two interfaces; their behavioral effect remains unestablished without a control or per-rule isolation. | Human generalization judgment, rule representation, loading scheme, and review process. |
| [Darwin Gödel Machine](../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md), an archive-based coding-agent evolution method | Descendant code became operative when admitted agents were later sampled and run; archive admission alone does not close the path. | Diagnostician, viability criterion, archive and parent-selection rules, objective, and evaluator. |
| [HyperAgents](../sources/hyperagents.ingest.md), a joint task/meta-agent evolution method | Selected patch lineages revise task code and the meta-agent code that modifies future agents, then replay those changes into later generations. | Main-run objectives and evaluators, parent selection, archive controller, resource budget, and sandbox. |

### What later episodes establish

Among these six systems, HyperAgents supplies the closest later-episode test. Researchers transferred evolved whole hyperagents into unseen math grading, froze their agent-modifying components, and used them to generate agents for 50 iterations. The resulting task agents significantly outperformed those produced by the initial hyperagent. Because selection bundles prompt text, insight files, and executable edits, the result does not isolate which changes caused the gain. Continued evolution from transferred rather than fresh hyperagents showed no significant advantage. This establishes one contribution from a retained whole program, not recurrent compounding.

Beyond this six-system case set, three studies sharpen the compounding question through phased re-optimization, cross-form feedback, and transfer of natural-language knowledge.

[Do Agent Optimizers Compound?](../sources/agent-optimizers-compound-terminal-bench.ingest.md) offers a direct vocabulary test. RELAI's Verifiable Continual Learning (RELAI-VCL) alone transferred positively to the expanded task set and then improved again after the new tasks entered the objective. The paper calls this compounding. Under this article's criterion, the experiment establishes retention, transfer, and another successful optimization, but the missing equally budgeted fresh-start Phase-2 control leaves open whether the first benefit made the second episode more productive.

[Co-Harness](../sources/co-harness-co-evolving-harness-and-model-weights.ingest.md) offers a different feedback design: regression-checked harness edits produce trajectories for supervised fine-tuning, and the updated model enters the next harness round. Two rounds improved reported accuracy, but no matched ablation separates the coupling from additional training or harness search, and larger structural redesign remains human-supplied. The authors also flag significant multi-round training compute. This is a plausible recurrent path under a training-intensive cost profile, not yet a clean causal estimate of compounding.

[Knowledge-Centric Self-Improvement](../sources/knowledge-centric-self-improvement-2607.19592.ingest.md) is the closest comparison considered here for a retained natural-language layer. Its scoped bundles improved held-out task performance across tasks and model families, establishing useful accumulation and transfer. The experiment froze the artifact and did not isolate whether retained knowledge made later curation more productive; its forum, distillation, adapter, and evaluation machinery remained supplied. Recurrent compounding remains unestablished.

## A proof-governed limit case

The theoretical [Gödel machine](../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md) places its proof searcher inside the revision surface, so a licensed rewrite may replace the machinery governing later rewrites. The incumbent must prove that switching is better than continuing, excluding beneficial changes its formalization cannot prove. This is a broad formal surface, not empirical evidence of compounding; Commonplace explores a narrower surface under fallible semantic judgment.

## Commonplace as a human-inclusive testbed

If their research teams were included within the system boundaries, the six systems could also be redesigned by their builders. The table excludes those teams, whereas [Commonplace's declared boundary](../reference/commonplace-declared-frame.md) includes designated maintainers, so breadth is not directly comparable. Commonplace's narrower claim is that retained repository roles, procedures, and artifacts make human–agent redesign part of an explicit operating path whose installed results can be used and later revisited, rather than an unrecorded builder intervention.

Commonplace's specific bet is a linked natural-language layer that combines [interpretation and retention](../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md). It keeps claims, assumptions, and scopes separately revisable while an LLM uses them to interpret heterogeneous evidence. [Individually routable notes keep that theory available under soft context degradation](../notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md), rather than burying it in Python strings or executable lineages. The hypothesis is that such theories can change how later work is decomposed, rather than only supply matching rules.

This medium does not imply a simple cost ranking: [readable-artifact and weight updates have different cost curves](./the-bitter-lesson-does-not-require-everything-to-live-in-weights.md). When a change touches few components and its downstream effects are bounded, a text or code artifact can be patched, checked, deployed, and rolled back without a training cycle. Weight training adds data preparation, accelerator time, checkpoint evaluation, and deployment. Artifact search and evaluation can erase that advantage; parametric updates may amortize dense changes across many calls and avoid artifact-retrieval and context-loading costs. Comparisons must count both over a declared later-use horizon.

Commonplace's [six-path audit](../notes/evidence/six-commonplace-paths-establish-broad-addressability-not-completeness.md) found broad path-relative addressability and several operative, repeatable paths, not completeness. It also exposed a defect in its own preliminary decomposition: consumer, channel, and force did not distinguish the cohort and trigger to which the same force applied. A [live proposal](../reference/proposals/revise-behavioral-authority-decomposition.md) leaves open whether applicability becomes a fourth component or a required qualifier. This brought the audit theory under challenge; it did not expand the effective update space or install a successor.

A separate [topic-index trace](../reference/tag-readme-trace-observed-causal-connection.md) establishes operative redesign and later use. Neither case shows that the natural-language theory layer causes compounding.

## What remains to test

Two different experiments remain. First, no matched baseline shows that Commonplace earns its total cost. The [objective-level ablation](../reference/proposals/ablation-baselines-for-the-declared-objective.md) compares the operated framework with raw repository history and documentation, episodic examples without distilled theory, the same artifacts without reach-oriented review, and a stronger model without Commonplace. The stronger-model arm is an economic substitution baseline and needs equivalent repository and tool access.

Second, the later-episode protocol asks whether a named retained benefit helped produce a subsequent improvement. It compares matched episodes against frozen-artifact or simpler-memory variants, with a stronger-model baseline where useful, and requires a direct-uptake or reinvestment trace. Episodes should require heterogeneous or structurally shifted revisions so that local rule reuse cannot stand in for theory-mediated reinterpretation. In a human-inclusive system, replay with the same experienced maintainer cannot fully remove internalized learning; outside-operator or frozen-artifact transfer is stronger where feasible.

Across both experiments, measure resource use (proposal and evaluator calls, context and retrieval costs, and intervention-specific training compute), human decisions and completion time, transfer and collateral regressions, rollback granularity, and maintenance over a declared horizon. One causally traced positive transition would provide local evidence of compounding. Repeated traced contributions are needed for a pathway-level claim.

## Where to go next

The companion draft develops the [human-inclusive revision affordance and audit result](./what-makes-human-inclusive-self-revision-non-trivial.md), while the [self-improving-systems cluster](../notes/self-improving-systems-README.md) maps the underlying theory. Counterexamples and disputed classifications are welcome below.
