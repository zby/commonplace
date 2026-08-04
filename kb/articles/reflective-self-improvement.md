---
description: "Argues that improvements can accumulate without compounding, compares bounded redesign across six systems, and presents Commonplace as a human-inclusive testbed"
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
---

# Reflective self-improvement

> **Draft.** This article is circulating for comments; its claims, structure, and even its central thesis may still change. Comments are welcome below.

> **TL;DR.** Improvements can accumulate without compounding. A pathway compounds when benefits from retained changes help produce later improvements—directly through better diagnosis, evaluation, or revision, or indirectly through time, compute, or judgment reinvested in that work.
>
> Reflection and complete addressability are neither necessary nor sufficient for compounding. They make improvement theory, revision machinery, and the resulting feedback paths inspectable and revisable. Six reported systems expose different bounded update surfaces. HyperAgents provides the closest external evidence of compounding; Commonplace provides a human-inclusive testbed with a first-class natural-language theory layer, but its payoff remains unmeasured. The theoretical Gödel machine supplies a proof-governed limit case.

## Improvement, accumulation, and compounding

Suppose a system comprises an agent, its standing deployment policy, and the runtime that loads it. A deployment fails on a Tuesday because a credential expired. The agent mistakes the date for the cause and changes its policy to "Never deploy on Tuesdays." Later runs obey. The failure supplied evidence about the objective of reducing deployment failures, and the change became operative, but the causal inference was wrong. Self-improvement names an improvement-directed pathway, not a guarantee that every adopted update helps.

Self-change need not touch model weights: prompts, instructions, memories, tests, validators, and scaffolding can determine later behavior. But not every influential fact is a [self-representation](../notes/definitions/reflective-system.md), which represents some declared aspect of the same system and participates causally in its operation. The standing policy qualifies because the runtime reads it to govern deployments; a note recording only the credential expiry describes the environment.

Reflective [self-improvement](../notes/definitions/self-improving-system.md) combines that structure with improvement-directed change. Evidence bearing on [an independently specifiable objective](../notes/self-improvement-is-relative-to-a-declared-objective.md) must change the system's [behavior-determining organization](../notes/definitions/behavior-determining-organization.md)—the roles, policies, representations, and machinery that determine its later behavior—through the self-representation.

```text
objective-bearing evidence affects the update
                        ↓
the system's organization changes through its self-representation
                        ↓
the change enters a live behavioral path
                        ↓
a subsequent operation depends on the change
```

A stored trace or uninstalled proposal does not close this path; a subsequent operation must depend on the installed change.

When retained changes are useful, their benefits can accumulate as later operation depends on them. But [improvements can accumulate without compounding](../notes/improvements-can-accumulate-without-compounding.md): a pathway compounds only when an earlier benefit also helps produce a later improvement. A validator that saves ten minutes on every later revision contributes directly by making those revisions cheaper. A task-facing gain contributes indirectly when the time, compute, or judgment it frees is reinvested in improvement work.

Evidence therefore comes from later episodes: improvement becomes cheaper, broader, more reliable, or less dependent on human judgment because an earlier change contributed. The effect may be modest and may saturate; evaluation capacity may limit its scale. The [later-episode protocol](../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) separates this claim from the metric that accepted the earlier change.

## Which parts of the improvement process can change?

Consider a harness optimizer that can rewrite a system prompt and three tool descriptions while a fixed test suite decides which edits are promoted. The prompt and tool descriptions are inside its update surface. The suite controls promotion but remains outside that surface. The system can improve behavior without revising all the machinery that governs improvement.

A readable self-representation can make a retained commitment [addressable](../notes/reflection-buys-addressability.md). Given a reliable retrieval and revision path, the commitment can be named, criticized, revised, or retired individually. [Behavioral authority](../notes/definitions/behavioral-authority.md) describes how such an artifact shapes operation: who consumes it, through which channel, and with what force.

The stronger structural target is **complete addressability of behavioral authority**. Within a declared boundary, every repository-defined artifact and relation through which authority is exercised—including an evaluator, objective, update rule, or other machinery governing revision—is available for inspection, criticism, and revision. *Meta* is a role within an episode, not a permanently higher layer. If an installed successor enters an authority-bearing path, it falls under the same coverage target; continuity keeps that revision path usable for another change.

These properties expose feedback paths to inspection and selective revision. Whether they make improvement more productive remains an empirical question.

## Three diagnostic tests

Apply the three tests to a named revision path:

| Test | Questions |
|---|---|
| **Occurrence** | What boundary, horizon, and objective are declared? Did objective-relevant evidence change represented behavior-determining organization, and did a later operation depend on the installed change? |
| **Revision surface** | Is the update direct or [proposal-selected](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md)? Which authority-bearing artifacts and relations can the path revise, which remain supplied, and does the path remain usable after installation? |
| **Compounding** | Did the retained benefit help produce a later improvement? What comparison shows a cheaper, broader, more reliable, or less human-dependent episode, and what causal trace connects the two? |

The Tuesday example passes the occurrence test. The harness optimizer has a bounded revision surface because its promotion suite remains supplied. The compounding test requires a separate later comparison.

## Six reported systems

The table applies the occurrence and revision-surface tests to six reported paths; it does not describe each system's total capabilities. The [detailed evidence inventory](../notes/evidence/six-reported-self-improvement-paths-expose-bounded-redesign-surfaces.md) records the underlying editability, installation, and later-dependence evidence.

| System | Strongest reported operative change | Fixed or externally supplied machinery |
|---|---|---|
| [Self-Harness](../sources/self-harness-harnesses-that-improve-themselves.ingest.md) | Accepted instruction, runtime-control, and tool-handling edits were merged and exercised in later evaluations. | Model and control architecture, edit surface, failure representation, objective, evaluator, task splits, and acceptance rule. |
| [Continual Harness](../sources/continual-harness-online-adaptation-foundation-agents.ingest.md) | Prompt revisions and repaired skills reached later steps or invocations; many created skills and memory entries did not. | Game representation, harness partition, interfaces, Refiner rule and schedule, reward design, models, and task family. |
| [Autogenesis](../sources/autogenesis-a-self-evolving-agent-protocol.ingest.md) | Committed prompt and agent revisions were reused; several other typed surfaces remain affordances or lack independent evaluation. | Resource ontology and mask policy, specialist organization, trace schema, objective, evaluator, acceptance rule, and task interfaces. |
| [Accumulated Behavioral Rules](../sources/self-improving-ai-coding-agents-through-accumulated-rules.ingest.md) | Rules were installed and loaded by two interfaces; their behavioral effect remains unestablished without a control or per-rule isolation. | Human generalization judgment, rule representation and loading scheme, source taxonomy, and review process. |
| [Darwin Gödel Machine](../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md) | Descendant code became operative when admitted agents were later sampled and run; archive admission alone does not close the path. | o1 diagnostician, viability criterion, archive policy, parent-selection rule, objective, evaluator, weights, and sandbox. |
| [HyperAgents](../sources/hyperagents.ingest.md) | Selected patch lineages revise task and meta-agent code and are replayed into later generations. | Main-run task distribution, objectives, evaluators, parent selection, archive controller, model and tool dependencies, resource budget, and sandbox. The appendix makes parent selection editable, but not evaluation or the outer archive loop. |

HyperAgents is the strongest external boundary case because it revises the procedure that generates future agents. Its lineages are mixed-form: descendants revise prompt text and sometimes install files of synthesized insights and plans, but selection promotes the bundled executable lineage and does not isolate those artifacts' contribution.

The [transfer experiment](../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md#hyperagents-shows-a-cross-domain-contribution-to-compounding) also supplies the closest evidence of compounding. Whole hyperagents evolved in paper-review and robotics runs were transferred into unseen math grading, their meta-agent components were frozen, and they generated agents for 50 later iterations. Under the same fixed-meta protocol, Improvement@50 was 0.630 for transferred hyperagents and 0 for the initial hyperagent, a significant difference. This is evidence that an earlier retained improver helped produce later improvements at the whole-program level. The experiment does not isolate which bundled changes caused the gain, and continued evolution from transferred rather than fresh hyperagents reached 0.640 versus 0.610 without a statistically significant difference. Sustained compounding therefore remains unestablished.

Direct and proposal-selected paths can both change consequential organization while leaving governing machinery supplied.

## A proof-governed limit case

The theoretical [Gödel machine](../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md) places its proof searcher and rewrite machinery inside the rewrite surface, so a licensed rewrite may replace the machinery governing later rewrites. Its acceptance rule is strict: the incumbent system must prove that switching is better than continuing its search, excluding beneficial rewrites whose value its current formalization cannot prove. This gives the Gödel machine a broad formal rewrite surface, not empirical evidence of compounding. Commonplace makes a narrower structural move under fallible empirical and semantic judgment.

## Commonplace as a human-inclusive testbed

> If the six reported systems included the research teams that built them, those teams could plainly redesign the systems too. Commonplace's proposed distinction is the explicit, retained revision machinery through which human–agent redesign can become operative and be revisited. The comparison concerns the operating paths the papers report.

[Commonplace's declared boundary](../reference/commonplace-declared-frame.md) includes designated maintainers acting through repository-defined roles and artifacts. Its [six-path audit](../notes/evidence/six-commonplace-paths-establish-broad-addressability-not-completeness.md) found broad, path-relative addressability but was not exhaustive, so it did not establish completeness. Separately, generic maintainer admission was unrepresented and requested model bindings were not reliably realized in execution.

Commonplace also makes a linked, selectively loadable natural-language theory layer part of its operating substrate. [Improvement theories often arrive before formalization and need separable claims, assumptions, and scopes](../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md). Keeping them as individually routable notes avoids burying them in Python strings or bundled executable lineages; under [soft effective-context limits](../notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md), [instructions, validators, and code can provide narrower fast paths](../notes/theory-and-methodology-form-a-two-layer-execution-system.md).

One trace concerns topic indexes. A tag README promised a complete list of notes carrying its tag, but the `learning-theory` head had grown beyond reliable inspection by the editing agent. The recorded strain motivated explicit `complete` and `covered_by` marks, schema support, and validator checks. The installed check later found that block-style YAML tags escaped the documented search recipe and forced a correction. The [trace](../reference/tag-readme-trace-observed-causal-connection.md) therefore connects evidence, redesign, installation, and later operative use.

A second trace shows revision machinery being reused and revised. [ADR 056](../reference/adr/056-adopted-and-retired-proposals-archive-out-of-the-frontier.md) changed the proposal lifecycle and required later ADRs to retain considered alternatives. [ADR 057](../reference/adr/057-articles-use-an-editorial-profile-and-excluded-drafts.md) used that requirement while creating the article lifecycle; [ADR 063](../reference/adr/063-all-article-drafts-circulate-behind-a-banner.md) later challenged and revised the installed lifecycle. Together, the two traces establish operative redesign, reuse, and continuity.

## What remains to test

No matched baseline yet shows that Commonplace's retained decisions and operative revision machinery make later architectural change easier to initiate, coordinate, check, or revisit. Compare matched later episodes against a frozen-artifact or simpler-retention baseline; trace direct uptake or reinvested savings, and measure target-identification cost, human decisions, completion time, breadth of supported changes, repair or rollback, and maintenance cost. One positive transition would be local evidence of compounding; a sequence would show whether compounding is sustained across episodes.

The companion draft develops the [human-inclusive revision affordance and audit result](./what-makes-human-inclusive-self-revision-non-trivial.md); the [Bitter Lesson companion](./the-bitter-lesson-does-not-require-everything-to-live-in-weights.md) asks whether learning over readable artifacts can scale against weight-based alternatives. The [self-improving-systems cluster](../notes/self-improving-systems-README.md) maps the underlying theory, and the [repeatable-path note](../notes/a-repeatable-operative-path-keeps-a-redesign-class-open-to-revision.md) develops continuity. Counterexamples and disputed classifications are welcome below.
