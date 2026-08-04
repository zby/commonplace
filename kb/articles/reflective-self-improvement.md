---
description: "Defines reflective self-improvement, compares revision of authority-bearing machinery across five systems and Commonplace, and separates addressability and reuse from leverage and compounding"
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
  - kb/notes/compounding-needs-leverage-to-multiply-and-autonomy-to-scale.md
  - kb/notes/reflective-leverage-is-tested-in-the-next-episode.md
  - kb/notes/a-proximate-target-is-checked-for-achievement-not-for-warrant.md
  - kb/notes/self-improvement-is-relative-to-a-declared-objective.md
  - kb/notes/warranted-autonomy-is-bounded-by-oracle-domain.md
  - kb/notes/an-omitted-loop-function-and-a-frozen-one-need-different-repairs.md
  - kb/notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md
  - kb/notes/a-retained-operative-path-keeps-improvement-machinery-open-to-revision.md
  - kb/notes/evidence/five-reported-self-improvement-paths-expose-bounded-redesign-surfaces.md
  - kb/reference/commonplace-declared-frame.md
  - kb/reference/commonplace-as-a-reflective-system.md
  - kb/reference/design-rationale-management.md
  - kb/reference/storage-architecture.md
  - kb/reference/tag-readme-trace-observed-causal-connection.md
  - kb/reference/tag-readme-trace-as-self-improving-loop.md
  - kb/reference/adr/028-design-proposals-live-in-reference-proposals.md
  - kb/reference/adr/057-articles-use-an-editorial-profile-and-excluded-drafts.md
  - kb/sources/self-harness-harnesses-that-improve-themselves.ingest.md
  - kb/sources/continual-harness-online-adaptation-foundation-agents.ingest.md
  - kb/sources/autogenesis-a-self-evolving-agent-protocol.ingest.md
  - kb/sources/self-improving-ai-coding-agents-through-accumulated-rules.ingest.md
  - kb/sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md
---

# Reflective self-improvement

> **Draft.** This article is circulating for comments; its claims, structure, and even its central thesis may still change. Comments are welcome below.

> **TL;DR.** Reflective self-improvement occurs when evidence relevant to an objective changes the roles, policies, representations, or machinery that determine a system's later behavior through a self-representation, and later operation depends on that change. A readable retained artifact can make the change addressable. Commonplace's stronger claim is that its repository-defined behavioral authority—including the machinery through which it revises itself—is addressable to the human–agent process. This makes the authority-bearing machinery available for later revision; continuity makes the operative path repeatable, and leverage begins only when using a retained change improves a later revision.
>
> Five reported systems expose different bounded update surfaces. Commonplace records a human–agent path that later reused changes to checking and design methods. Whether an explicit retained path makes later revision cheaper, broader, more reliable, or less dependent on human judgment remains an untested hypothesis. The theoretical Gödel machine supplies a proof-governed limit case.

## What changes count

For this example, the system comprises the agent, its standing deployment policy, and the runtime that loads it; the assessment covers the next several deployments. Suppose a deployment fails on a Tuesday because a credential expired. The agent mistakes the date for the cause and changes its policy to "Never deploy on Tuesdays." Later runs obey. The failure supplied evidence about the objective of reducing deployment failures, and the change became operative, but the causal inference was wrong. Self-improvement names an improvement-directed pathway, not a guarantee that every adopted update helps.

Self-change need not touch model weights: prompts, instructions, memories, tests, validators, and scaffolding can determine later behavior. But not every influential fact is a [self-representation](../notes/definitions/reflective-system.md), which represents some declared aspect of the same system and participates causally in its operation. The standing policy qualifies because the runtime reads it to govern deployments; a note recording only the credential expiry describes the environment.

Reflective [self-improvement](../notes/definitions/self-improving-system.md) combines that structure with improvement-directed change. Evidence bearing on [an independently specifiable objective](../notes/self-improvement-is-relative-to-a-declared-objective.md) must change the system's [behavior-determining organization](../notes/definitions/behavior-determining-organization.md)—the roles, policies, representations, and machinery that determine its later behavior—through the self-representation. The changed organization must then govern a subsequent operation within the declared assessment horizon.

```text
objective-bearing evidence affects the update
                        ↓
the system's organization changes through its self-representation
                        ↓
the change enters a live behavioral path
                        ↓
a subsequent operation depends on the change
```

A stored trace that never affects an updater, an uninstalled proposal, and a loaded but ignored rule each leave the path open. The Tuesday update closes it despite being harmful. It is a **direct update** because the evidence-determined successor becomes incumbent without a rejectable candidate; the error lies in the rule that converts a coincidence into policy. A **proposal-selection update**, by contrast, generates candidates, permits rejection, and makes an accepted change operative through [search, reject-capable evaluation, and operative retention](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md).

## From addressability to leverage

A readable self-representation can make a retained commitment [addressable](../notes/reflection-buys-addressability.md). Given a scope, reliable retrieval path, and governed revision path, the commitment can be named, criticized, revised, or retired individually.

[Behavioral authority](../notes/definitions/behavioral-authority.md) identifies how a retained artifact actually shapes operation: who consumes it, through which channel, and with what force. An evaluator is *meta* to the prompt it judges only within that episode. It is also an authority-bearing part of the system's organization and can be addressed in a later revision like an objective, instruction, validator, or update rule.

The stronger structural property is **complete addressability of behavioral authority**. Within a declared boundary, every repository-defined artifact and relation through which authority is exercised—including those governing revision—is available for inspection, criticism, and revision. Once an installed successor enters a behavioral-authority path, it falls under the same coverage condition. When operative revision also preserves continuity, the process can act again on its own machinery without requiring a permanently higher controller.

When a later improvement episode depends on an earlier retained result, that result is reused. It has [reflective leverage](../notes/compounding-needs-leverage-to-multiply-and-autonomy-to-scale.md) only if that dependence improves how the later episode diagnoses, evaluates, applies, or retains change. The evidence is a productivity difference: the episode becomes cheaper, broader, more reliable, or less dependent on human judgment.

Repeated leverage would constitute compounding only if those gains accumulate rather than saturate. Sustaining such growth would also require evaluation capacity to scale; whether warranted computational checks can carry that load remains untested.

Take a harness optimizer whose update space includes a system prompt and three tool descriptions, while a fixed test suite decides promotion. The prompt and tool descriptions are addressable; an accepted edit becomes operative only when later behavior depends on it. The suite's result has selection force in the promotion path, but the suite remains outside that path's update space. The path therefore does not provide complete addressability of its own behavioral authority.

## The reflective self-improvement test

The argument yields six diagnostic questions:

> 1. What system boundary and assessment horizon are declared, and which structures represent the system within that boundary?
> 2. What independently specifiable objective does the evidence bear on?
> 3. Does that evidence change the system's behavior-determining organization through its self-representation, rather than merely being stored or retrieved?
> 4. How does the installed change reach its consumer? What authority does it have, and which subsequent operation depends on it?
> 5. Is the update direct or proposal-selected? If proposal-selected, what searches, evaluates with the power to reject, and retains accepted changes? Which functions remain outside its update space?
> 6. Which repository-defined artifacts and relations participate in behavioral-authority paths around the revision? Are they addressable—including the machinery governing revision and the installed successors—and does the operative revision path remain usable after installation?

The first four questions test whether reflective self-improvement occurred; the fifth identifies the update architecture; and the sixth tests complete addressability and continuity of the revision path. The Tuesday policy closes the first four and is direct, but leaves its faulty evidence-to-policy rule untouched. Demonstrating leverage requires a separate comparison of later revision productivity.

## A proof-governed limit case

The theoretical [Gödel machine](../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md) places its proof searcher and rewrite machinery inside the rewrite surface. A licensed rewrite may therefore replace the machinery governing later rewrites. The acceptance boundary is strict: the incumbent system must prove that switching is better than continuing its search, so it cannot license beneficial rewrites whose value its current formalization cannot prove. This is a theoretical tradeoff, not an experimental result.

The proof obligation governs admission for one rewrite while the proof searcher remains inside the surface available to later licensed rewrites. Commonplace makes a narrower structural move under fallible empirical and semantic judgment rather than proof.

## Five reported systems

The [detailed evidence inventory](../notes/evidence/five-reported-self-improvement-paths-expose-bounded-redesign-surfaces.md) separates declared editability, installation, and later dependence for five reported paths. **Closed** means objective-relevant evidence changed represented organization and later operation depended on the installed change. **Unestablished** means the record leaves that causal path open. **Supplied** marks authority-bearing machinery outside the reported update surface.

| System | Strongest reported closure | Supplied boundary |
|---|---|---|
| [Self-Harness](../sources/self-harness-harnesses-that-improve-themselves.ingest.md) | Accepted instruction, runtime-control, and tool-handling edits were merged and exercised in later evaluations. | Model and control architecture, edit surface, failure representation, objective, evaluator, task splits, and acceptance rule. |
| [Continual Harness](../sources/continual-harness-online-adaptation-foundation-agents.ingest.md) | Prompt revisions and repaired skills reached later steps or invocations; many created skills and memory entries did not. | Game representation, harness partition, interfaces, Refiner rule and schedule, reward design, models, and task family. |
| [Autogenesis](../sources/autogenesis-a-self-evolving-agent-protocol.ingest.md) | Committed prompt and agent revisions were reused; several other typed surfaces remain affordances or lack independent evaluation. | Resource ontology and mask policy, specialist organization, trace schema, objective, evaluator, acceptance rule, and task interfaces. |
| [Accumulated Behavioral Rules](../sources/self-improving-ai-coding-agents-through-accumulated-rules.ingest.md) | Rules were installed and loaded by two interfaces; behavioral dependence is **unestablished** without a control or per-rule isolation. | Human generalization judgment, rule representation and loading scheme, source taxonomy, and review process. |
| [Darwin Gödel Machine](../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md) | Descendant code became operative when admitted agents were later sampled and run; archive admission alone does not close the path. | o1 diagnostician, viability criterion, archive policy, parent-selection rule, objective, evaluator, weights, and sandbox. |

The classifications attach to reported paths, not whole systems or their research teams. Direct versus proposal-selected updating does not determine breadth: both can change consequential organization while leaving parts of the governing method supplied. The [omitted-versus-frozen comparison](../notes/an-omitted-loop-function-and-a-frozen-one-need-different-repairs.md) develops the update-architecture and lifecycle reading.

## Commonplace records a reusable revision path

> If the five reported systems included the research teams that built them, those teams could plainly redesign the systems too. Commonplace's proposed distinction is the explicit, retained revision machinery through which human–agent redesign can become operative and be revisited. The comparison concerns the operating paths the papers report.

[Commonplace's declared boundary](../reference/commonplace-declared-frame.md) includes designated maintainers acting through repository-defined roles and artifacts. Architecture decision records make accepted decisions [addressable](../reference/design-rationale-management.md), while instructions, checks, configuration, and code install them in behavioral-authority paths. The completeness claim includes those artifacts and relations, including the machinery used for revision. [Version-control history](../reference/storage-architecture.md) helps reconstruct an episode but does not by itself record a rationale or make a result operative.

The clearest case concerns topic indexes. A tag README promised a complete list of notes carrying its tag, but the `learning-theory` head had grown to 55 entries and 18.8 KB, beyond reliable inspection by the editing agent. The recorded strain motivated explicit `complete` and `covered_by` marks, schema support, and validator checks. The installed `covered_by` check later found that block-style YAML tags escaped the documented search recipe and forced a correction. The [tag-README trace](../reference/tag-readme-trace-observed-causal-connection.md) therefore records evidence reaching a redesign, its installation, and later operation depending on the new check. It does not show that the redesign improved later revision productivity.

A second case shows procedural reuse. Unadopted designs lacked a durable home, so [the proposal-lifecycle decision](../reference/adr/028-design-proposals-live-in-reference-proposals.md) introduced a stage between investigation and implementation. A later proposal for an article collection used that stage and became [the article-layer decision](../reference/adr/057-articles-use-an-editorial-profile-and-excluded-drafts.md). This establishes use of the installed design process, not that the process made the later redesign better or cheaper.

## Testing the working claim

The Commonplace cases supply candidate episodes for a leverage test, not its result. No matched baseline currently shows that retained decisions and operative revision machinery make later architectural change easier to initiate, coordinate, check, or revisit. Testing the hypothesis has two parts.

First, audit whether behavioral authority is completely addressable. Map the repository-defined objectives, evaluators, authority rules, theories, validators, and revision methods by consumer, channel, and force. For each one, ask whether the human–agent process can identify and criticize the authority-bearing artifact, revise the artifact and the relations through which it acts, and install the result. Apply the same test after an installed successor enters an authority path. The companion draft develops this [study of complete addressability](./what-makes-human-inclusive-self-revision-non-trivial.md).

Second, measure leverage. Compare matched later revision episodes against a frozen-artifact or simpler-retention baseline. Trace uptake and measure target-identification cost, human decisions, completion time, breadth of supported changes, repair or rollback, and maintenance cost. This separates the contribution of the retained change from task difficulty, model strength, and maintainer experience.

A positive result would show leverage when uptake of a retained change makes a matched later revision cheaper, broader, more reliable, or less dependent on human judgment. Compounding would require those gains to recur without saturating while warranted evaluation capacity scales with them.

The [Bitter Lesson companion](./the-bitter-lesson-does-not-require-everything-to-live-in-weights.md) asks whether search and learning over readable artifacts can scale against weight-based alternatives.

The [self-improving-systems cluster](../notes/self-improving-systems-README.md) maps the underlying theory, and [the retained-operative-path note](../notes/a-retained-operative-path-keeps-improvement-machinery-open-to-revision.md) develops the continuity criterion. If applying them produces a counterexample or disputed classification, leave a comment below.
