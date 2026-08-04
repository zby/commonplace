---
description: "Separates accumulated gains and single cross-episode contributions from recurrent compounding, compares bounded revision surfaces across six systems, and presents Commonplace as an unmeasured human-inclusive testbed"
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
  - kb/notes/retrieval-failure-is-reflection-failure.md
  - kb/notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md
  - kb/notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md
  - kb/notes/methodological-and-computational-closure-track-different-changes.md
  - kb/notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md
  - kb/notes/theory-and-methodology-form-a-two-layer-execution-system.md
  - kb/notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md
  - kb/notes/accumulation-counts-dependence-through-the-retained-result.md
  - kb/notes/improvements-can-accumulate-without-compounding.md
  - kb/notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md
  - kb/notes/a-proximate-target-is-checked-for-achievement-not-for-warrant.md
  - kb/notes/self-improvement-is-relative-to-a-declared-objective.md
  - kb/notes/warranted-autonomy-is-bounded-by-oracle-domain.md
  - kb/notes/an-omitted-loop-function-and-a-frozen-one-need-different-repairs.md
  - kb/notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md
  - kb/notes/a-repeatable-operative-path-keeps-a-redesign-class-open-to-revision.md
  - kb/notes/evidence/six-reported-self-improvement-paths-expose-bounded-redesign-surfaces.md
  - kb/notes/evidence/six-commonplace-paths-establish-broad-addressability-not-completeness.md
  - kb/agent-memory-systems/reviews/hyperagents.md
  - kb/reference/commonplace-declared-frame.md
  - kb/reference/commonplace-as-a-reflective-system.md
  - kb/reference/design-rationale-management.md
  - kb/reference/storage-architecture.md
  - kb/reference/tag-readme-trace-observed-causal-connection.md
  - kb/reference/tag-readme-trace-as-self-improving-loop.md
  - kb/reference/adr/056-adopted-and-retired-proposals-archive-out-of-the-frontier.md
  - kb/reference/adr/057-articles-use-an-editorial-profile-and-excluded-drafts.md
  - kb/reference/adr/063-all-article-drafts-circulate-behind-a-banner.md
  - kb/sources/self-harness-harnesses-that-improve-themselves.ingest.md
  - kb/sources/continual-harness-online-adaptation-foundation-agents.ingest.md
  - kb/sources/autogenesis-a-self-evolving-agent-protocol.ingest.md
  - kb/sources/self-improving-ai-coding-agents-through-accumulated-rules.ingest.md
  - kb/sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md
  - kb/sources/hyperagents.ingest.md
  - kb/sources/knowledge-centric-self-improvement-2607.19592.ingest.md
---

# Reflective self-improvement

> **Draft.** This article is circulating for comments; its claims, structure, and even its central thesis may still change. Comments are welcome below.

> **TL;DR.** Improvements can accumulate without creating a compounding pathway. A retained benefit contributes when it measurably helps produce a later improvement—through better diagnosis, evaluation, or revision, or through time, compute, or judgment demonstrably reinvested in that work. Repeated contributions establish recurrent compounding.
>
> Reflection is neither required for this feedback nor sufficient to make it productive. It makes improvement theory, revision machinery, and the resulting paths inspectable and revisable. Six reported systems expose different bounded update surfaces. HyperAgents, an agent-evolution framework that can revise both task and agent-modification code, provides the closest external evidence of one cross-episode contribution. Commonplace, an agent-operated knowledge-base framework, provides a human-inclusive testbed with a first-class natural-language theory layer, but its payoff remains unmeasured. The theoretical Gödel machine supplies a proof-governed limit case.

## Improvement, accumulation, and compounding

Suppose a system comprises an agent, its standing deployment policy, and the runtime that loads it. A deployment fails on a Tuesday because a credential expired. The agent mistakes the date for the cause and changes its policy to "Never deploy on Tuesdays." Later runs obey the new policy. The failure supplied evidence relevant to the objective of reducing deployment failures, and the change became operative, but the causal inference was wrong. Self-improvement names an improvement-directed pathway, not a guarantee that every adopted update helps. Had the diagnosis been correct, later runs depending on the new policy would establish a retained gain. They would not yet show that the gain helped produce another improvement.

Self-change need not touch model weights: prompts, instructions, memories, tests, validators, and scaffolding can determine later behavior. But not every influential fact is a [self-representation](../notes/definitions/reflective-system.md), which represents some declared aspect of the same system and participates causally in its operation. The standing policy qualifies because the runtime reads it to govern deployments; a note recording only the credential expiry describes the environment.

Reflective [self-improvement](../notes/definitions/self-improving-system.md) combines self-representation with improvement-directed change. Evidence bearing on [an independently specifiable objective](../notes/self-improvement-is-relative-to-a-declared-objective.md) must change the system's [behavior-determining organization](../notes/definitions/behavior-determining-organization.md)—the roles, policies, representations, and machinery that determine its later behavior—through the self-representation. The change must then enter a live behavioral path and affect a subsequent operation. A stored trace or uninstalled proposal does not close this path.

When retained changes are useful, their benefits can accumulate as later operation depends on them. But [improvements can accumulate without compounding](../notes/improvements-can-accumulate-without-compounding.md). A retained benefit contributes to a compounding path only when it helps produce a later improvement. A single transition establishes that contribution; a pathway-level claim requires the feedback to recur. A validator that saves ten minutes on a later revision contributes directly by making that revision cheaper. A task-facing gain contributes indirectly when the time, compute, or judgment it frees is demonstrably reinvested in improvement work.

This distinguishes contribution from ordinary reuse. Consulting a static manual shows accumulation. The retained guidance contributes only if it measurably makes later improvement cheaper, broader, more reliable, or less dependent on human judgment. Evidence therefore comes from later episodes and uses a measure other than the one that accepted the earlier change. The [later-episode protocol](../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) pairs that measure with a causal trace. A sequence of such transitions tests whether the feedback recurs, saturates, or stops at an evaluation bottleneck.

## Which parts of the improvement process can change?

Consider a harness optimizer that can rewrite a system prompt and three tool descriptions while a fixed test suite decides which edits are promoted. The prompt and tool descriptions are inside its update surface. The suite controls promotion but remains outside that surface. The system can improve behavior without revising all the machinery that governs improvement.

Compounding does not require reflection: [opaque retained learning can shape later updates without an inspectable self-representation](../notes/accumulation-counts-dependence-through-the-retained-result.md). Reflection supplies a different property. A readable self-representation can make a retained commitment [addressable](../notes/reflection-buys-addressability.md). Given a reliable retrieval and revision path, an agent can name, criticize, revise, or retire the commitment individually. [Behavioral authority](../notes/definitions/behavioral-authority.md) describes how such an artifact shapes operation: who consumes it, through which channel, and with what force.

The stronger structural target is **complete addressability of behavioral authority**. Within a declared boundary, every repository-defined artifact and relation through which authority is exercised is available for inspection, criticism, and revision. This coverage includes evaluators, objectives, update rules, and other machinery governing revision. *Meta* is a role within an episode, not a permanently higher layer. If an installed successor enters an authority-bearing path, it falls under the same coverage target. Continuity keeps that revision path usable for another change.

These properties expose feedback paths to inspection and selective revision. Whether they make improvement more productive remains an empirical question.

## Three diagnostic tests

Apply the three tests to a named revision path:

| Test | Questions |
|---|---|
| **Occurrence** | What boundary, horizon, and objective are declared? Did objective-relevant evidence change the represented behavior-determining organization, and did a later operation depend on the installed change? |
| **Revision surface** | At the named target, is the update direct, or are proposals generated and then accepted or rejected by a separate selection step? Which authority-bearing artifacts and relations can the path revise, which remain supplied, and does the path remain usable after installation? Mixed systems may answer differently for different targets. |
| **Compounding** | Did the retained benefit measurably help produce a later improvement? What causal trace connects the episodes, and has the feedback recurred? |

The Tuesday example passes the occurrence test. The harness optimizer has a bounded revision surface because its promotion suite remains supplied. The compounding test requires a separate later comparison.

## Six reported systems

The table applies the occurrence and revision-surface tests to six reported paths; it does not describe each system's total capabilities. The [detailed evidence inventory](../notes/evidence/six-reported-self-improvement-paths-expose-bounded-redesign-surfaces.md) records the underlying editability, installation, and later-dependence evidence.

| System | Strongest reported operative change | Decisive supplied machinery |
|---|---|---|
| [Self-Harness](../sources/self-harness-harnesses-that-improve-themselves.ingest.md), a same-model harness optimizer | Accepted instruction, runtime-control, and tool-handling edits were merged and exercised in later evaluations. | Control architecture, edit surface, objective, evaluator, and acceptance rule. |
| [Continual Harness](../sources/continual-harness-online-adaptation-foundation-agents.ingest.md), an online embodied-agent refiner | Prompt revisions and repaired skills reached later steps or invocations; many created skills and memory entries did not. | Game interface, harness partition, Refiner rule, reward design, and models. |
| [Autogenesis](../sources/autogenesis-a-self-evolving-agent-protocol.ingest.md), a typed agent-evolution protocol | Committed prompt and agent revisions were reused; several other typed surfaces remain affordances or lack independent evaluation. | Resource ontology, specialist organization, objective, evaluator, and acceptance rule. |
| [Accumulated Behavioral Rules](../sources/self-improving-ai-coding-agents-through-accumulated-rules.ingest.md), a coding-agent rule learner | Rules were installed and loaded by two interfaces; their behavioral effect remains unestablished without a control or per-rule isolation. | Human generalization judgment, rule representation, loading scheme, and review process. |
| [Darwin Gödel Machine](../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md), an archive-based coding-agent evolution method | Descendant code became operative when admitted agents were later sampled and run; archive admission alone does not close the path. | Diagnostician, viability criterion, archive and parent-selection rules, objective, and evaluator. |
| [HyperAgents](../sources/hyperagents.ingest.md), a joint task/meta-agent evolution method | Selected patch lineages revise task code and the meta-agent code that modifies future agents, then replay those changes into later generations. | Main-run objectives and evaluators, parent selection, archive controller, resource budget, and sandbox. |

The comparison shows that both direct and proposal-selected paths can change consequential organization while leaving governing machinery supplied. It does not by itself establish compounding. HyperAgents supplies the closest later-episode test because it revises the procedure that generates future agents.

HyperAgents lineages use mixed forms: descendants revise prompt text and sometimes install files of synthesized insights and plans. Selection, however, promotes the bundled executable lineage and does not isolate the contribution of those artifacts. In the transfer experiment, researchers moved whole hyperagents evolved in paper-review and robotics runs into unseen math grading. With their agent-modifying meta components frozen, the transferred hyperagents generated task agents for 50 later iterations and significantly outperformed the initial hyperagent under the same protocol.

This result shows, at the whole-program level, that an earlier retained improver contributed to later improvement. It does not isolate which bundled changes caused the gain. Continued evolution from transferred rather than fresh hyperagents also failed to produce a statistically significant advantage. The experiment therefore establishes one cross-episode contribution, not recurrent compounding.

## A proof-governed limit case

The theoretical [Gödel machine](../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md) places its proof searcher and rewrite machinery inside the rewrite surface, so a licensed rewrite may replace the machinery governing later rewrites. Its acceptance rule is strict: the incumbent system must prove that switching is better than continuing its search, excluding beneficial rewrites whose value its current formalization cannot prove. This gives the Gödel machine a broad formal rewrite surface, not empirical evidence of compounding. Commonplace makes a narrower structural move under fallible empirical and semantic judgment.

## Commonplace as a human-inclusive testbed

Commonplace is not distinctive merely because people can redesign it; the research teams behind the six reported systems can also revise their systems. The comparison covers only the operating paths reported in the papers. Commonplace's narrower proposal is to retain the repository-defined roles and artifacts through which human–agent redesign can become operative and be revisited. This article does not establish that other research systems lack analogous machinery.

[Commonplace's declared boundary](../reference/commonplace-declared-frame.md) includes designated maintainers acting through those roles and artifacts. Its [six-path audit](../notes/evidence/six-commonplace-paths-establish-broad-addressability-not-completeness.md) found broad, path-relative addressability. Because the audit was not exhaustive, it did not establish completeness. Separately, generic maintainer admission was unrepresented, and requested model bindings were not reliably realized in execution.

Commonplace is designed to make a linked, selectively loadable natural-language theory layer available to operating agents. [Improvement theories often arrive before formalization and need separable claims, assumptions, and scopes](../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md). Keeping them as individually routable notes avoids burying them in Python strings or bundled executable lineages. Under [soft effective-context limits](../notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md), [instructions, validators, and code can provide narrower fast paths](../notes/theory-and-methodology-form-a-two-layer-execution-system.md). Whether this theory layer improves later redesign remains unmeasured.

[Knowledge-Centric Self-Improvement](../sources/knowledge-centric-self-improvement-2607.19592.ingest.md) provides the closest external comparison for this natural-language layer. It retains scoped guidance in a shared knowledge base, and frozen generation-10 bundles improved held-out task performance across tasks and model families. This establishes useful accumulation and transfer in an addressable semantic artifact. It does not isolate whether retained knowledge made a later curation episode more productive: the transfer experiment froze the artifact, while the forum, distillation, adapter, and evaluation machinery remained supplied. Recurrent compounding therefore remains unestablished.

One trace concerns topic indexes. A tag README promised a complete list of notes carrying its tag, but the `learning-theory` head had grown beyond the editing agent's capacity for reliable inspection. That strain motivated two validator-checked cache fields and the checks that maintained them. The installed validator later found that one documented search recipe missed block-style YAML tags, forcing a correction. The [trace](../reference/tag-readme-trace-observed-causal-connection.md) connects observed failure, redesign, installation, and later operative use.

## What remains to test

No matched baseline yet shows that Commonplace's retained decisions and operative revision machinery make later architectural change easier to initiate, coordinate, check, or revisit. A test should compare matched later episodes against a frozen-artifact or simpler-retention baseline, trace direct uptake or reinvested savings, and measure target-identification cost, human decisions, completion time, breadth of supported changes, repair or rollback, and maintenance cost. One positive transition would establish a retained contribution to a later improvement. A sequence would show whether the feedback recurs enough to warrant a pathway-level compounding claim.

The companion draft develops the [human-inclusive revision affordance and audit result](./what-makes-human-inclusive-self-revision-non-trivial.md), while the [self-improving-systems cluster](../notes/self-improving-systems-README.md) maps the underlying theory. Counterexamples and disputed classifications are welcome below.
