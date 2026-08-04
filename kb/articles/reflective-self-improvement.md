---
description: "Defines reflective self-improvement, compares addressable revision of improvement machinery across five systems and Commonplace, and separates reuse from leverage and compounding"
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

> **TL;DR.** Reflective self-improvement occurs when evidence relevant to an objective changes the roles, policies, representations, or machinery that determine a system's later behavior through a self-representation, and later operation depends on that change. A readable retained artifact can make the change addressable. If an artifact governing one revision can become the target of a later governed revision, it is recursively targetable. These properties establish revision reach and reuse, not that the revision process improved.
>
> Five reported systems expose different bounded update surfaces. Commonplace records a human–agent path that later reused changes to checking and design methods; the same test could classify a research laboratory's workflow, but the papers do not document those workflows. Whether an explicit retained path makes later revision cheaper, broader, more reliable, or less dependent on human judgment remains an untested hypothesis. The theoretical Gödel machine supplies a proof-governed limit case.

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

*Meta* names a role within an improvement episode, not a permanent architectural layer: an evaluator is meta to the prompt it judges. **Recursive targetability** is stronger. It obtains when an artifact governing one episode can become the target of a later governed episode and its installed successor remains inside the addressable revision domain. Each transition is still judged under an incumbent objective, criterion, or method; any of these may become a later target. No permanently higher controller is required.

When a later improvement episode depends on an earlier retained result, that result is reused. It has [reflective leverage](../notes/compounding-needs-leverage-to-multiply-and-autonomy-to-scale.md) only if that dependence improves how the later episode diagnoses, evaluates, applies, or retains change. The evidence is a productivity difference: the episode becomes cheaper, broader, more reliable, or less dependent on human judgment.

Repeated leverage would constitute compounding only if those gains accumulate rather than saturate. Sustaining such growth would also require evaluation capacity to scale; whether warranted computational checks can carry that load remains untested.

Take a harness optimizer whose update space includes a system prompt and three tool descriptions, while a fixed test suite decides promotion. This gives possible reach over those artifacts; demonstrated reach begins only when an accepted edit becomes operative and later behavior depends on it. The suite occupies the meta role for those edits but remains outside the path's update space, so it cannot become a target within the same path.

## The reflective self-improvement test

The argument yields six diagnostic questions:

> 1. What system boundary and assessment horizon are declared, and which structures represent the system within that boundary?
> 2. What independently specifiable objective does the evidence bear on?
> 3. Does that evidence change the system's behavior-determining organization through its self-representation, rather than merely being stored or retrieved?
> 4. How does the installed change reach its consumer? What authority does it have, and which subsequent operation depends on it?
> 5. Is the update direct or proposal-selected? If proposal-selected, what searches, evaluates with the power to reject, and retains accepted changes? Which functions remain outside its update space?
> 6. Which represented parts changed? What later work uses their successors? Can both the governing artifacts and the installed successors become targets of later governed revision?

The first four questions test whether reflective self-improvement occurred; the fifth identifies the update architecture; and the sixth maps revision reach, recursive targetability, and later reuse. The Tuesday policy closes the first four and is direct, but leaves its faulty evidence-to-policy rule untouched. Demonstrating leverage requires a separate comparison of later revision productivity.

## A proof-governed limit case

The theoretical [Gödel machine](../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md) places its proof searcher and rewrite machinery inside the rewrite surface. A licensed rewrite may therefore replace the machinery governing later rewrites. The acceptance boundary is strict: the incumbent system must prove that switching is better than continuing its search, so it cannot license beneficial rewrites whose value its current formalization cannot prove. This is a theoretical tradeoff, not an experimental result.

The proof searcher is meta to one rewrite yet eligible for a later licensed rewrite. Commonplace makes a narrower structural move under fallible empirical and semantic judgment rather than proof.

## Five reported systems

The five reported systems expose narrower, empirically observed update surfaces: a bounded agent-harness optimizer (Self-Harness), an online harness refiner (Continual Harness), a typed resource-evolution protocol (Autogenesis), a review-derived rule-retention method (Accumulated Behavioral Rules), and an evolutionary coding-agent system (Darwin Gödel Machine). The table applies the six questions to each reported path, treating its optimization machinery—not only the base model—as part of the assessed system. **Closed** means objective-relevant evidence changed represented organization and later operation depended on the installed change. **Unestablished** means the record does not close that path. **Supplied** marks governing machinery outside demonstrated revision reach.

| System | Reported causal path | Demonstrated revision reach and supplied machinery |
|---|---|---|
| [Self-Harness](../sources/self-harness-harnesses-that-improve-themselves.ingest.md) | Failure traces drive several harness edits; pass counts on two splits determine promotion; later evaluations execute merged edits. **Closed** for promoted edits over that evaluation horizon. | Its proposal surface includes subagent, skill, and middleware structure. Because the subagent and skill proposals were rejected, demonstrated operative reach is limited to narrower middleware edits. The objective, failure representation, edit surface, and two-split gate stay supplied. |
| [Continual Harness](../sources/continual-harness-online-adaptation-foundation-agents.ingest.md) | Recent Pokémon trajectory failures directly change prompts, sub-agents, skills, or memory for later game steps. **Closed** for changes later exercised, but not for rarely consulted memory or the many skills never invoked. | Its Refiner creates, edits, and deletes sub-agent roles; its deployment record includes a structural rewrite into a master agent. The four-part partition, Refiner, interfaces, schedule, and reward design stay supplied. |
| [Autogenesis](../sources/autogenesis-a-self-evolving-agent-protocol.ingest.md) | Typed operators evaluate and commit prompt or agent versions reused in later refinement rounds. **Closed** for those revisions. Solution-only evolution changes the task output rather than the assessed system's organization; Environment and Memory uptake is unestablished. | Reported revisions reach enabled agent prompts, tools, and code. Specialist replacement is possible but not demonstrated in the experiments. The resource ontology, named specialist arrangement, bus protocol, evaluator, acceptance rule, and orchestration pattern stay supplied. |
| [Accumulated Behavioral Rules](../sources/self-improving-ai-coding-agents-through-accumulated-rules.ingest.md) | Engineers turn accepted review comments into standing rules loaded by two agent interfaces. The paper reports no recurrence across 74 later exposures, but does not isolate whether any individual rule caused that result, so causal uptake is **unestablished**. | The reported path installs rules in the standing layer, but behavioral dependence is unestablished. Human generalization judgment, the loading scheme, abstraction heuristic, and retirement policy stay supplied. |
| [Darwin Gödel Machine](../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md) | A parent edits descendant code; viable children enter an archive; benchmark score affects later sampling. **Closed** for descendants later selected and run, not for archive admission alone. | One descendant added an inheritable ranker stage. The diagnostician, admission rule, population controller, objective, and evaluator remain outside descendant edits. |

These classifications attach to reported paths, not whole systems. Creation, retention, and loading also remain weaker than later use: Continual Harness creates artifacts that never run, Accumulated Behavioral Rules guarantees loading without isolating dependence, and DGM retains children that may never execute again. Continual Harness updates directly while the other four use proposal selection, but neither architecture determines revision reach. The useful question is: *which redesign became operative, and which governing artifacts remained outside demonstrated reach?* The [omitted-versus-frozen comparison](../notes/an-omitted-loop-function-and-a-frozen-one-need-different-repairs.md) develops the lifecycle analysis.

## Commonplace records a reusable revision path

> The inclusion rule is symmetric. People count as part of a reflective path only when they occupy identifiable roles in a retained process whose accepted outputs enter behavioral paths that later system operation consumes. A research laboratory can satisfy that rule too; the five papers describe their experimental pathways, not their full development workflows.

[Commonplace's declared boundary](../reference/commonplace-declared-frame.md) includes designated maintainers acting through repository-defined roles and artifacts. Architecture decision records make accepted decisions [addressable](../reference/design-rationale-management.md), while instructions, checks, configuration, and code make them operative. [Version-control history](../reference/storage-architecture.md) helps reconstruct an episode but does not by itself record a rationale or make a result operative. The repository supplies evidence for some Commonplace paths; it does not establish that comparable laboratory paths are absent.

The clearest case concerns topic indexes. A tag README promised a complete list of notes carrying its tag, but the `learning-theory` head had grown to 55 entries and 18.8 KB, beyond reliable inspection by the editing agent. The recorded strain motivated explicit `complete` and `covered_by` marks, schema support, and validator checks. The installed `covered_by` check later found that block-style YAML tags escaped the documented search recipe and forced a correction. The [tag-README trace](../reference/tag-readme-trace-observed-causal-connection.md) therefore records evidence reaching a redesign, its installation, and later operation depending on the new check. It does not show that the redesign improved later revision productivity.

A second case shows procedural reuse. Unadopted designs lacked a durable home, so [the proposal-lifecycle decision](../reference/adr/028-design-proposals-live-in-reference-proposals.md) introduced a stage between investigation and implementation. A later proposal for an article collection used that stage and became [the article-layer decision](../reference/adr/057-articles-use-an-editorial-profile-and-excluded-drafts.md). This establishes use of the installed design process, not that the process made the later redesign better or cheaper.

## Testing the working claim

The Commonplace cases supply candidate episodes for a leverage test, not its result. No matched baseline currently shows that retained decisions and operative revision machinery make later architectural change easier to initiate, coordinate, check, or revisit. Testing the hypothesis has two parts.

First, map role-relative reach. Choose artifacts that currently govern revision—an objective, evaluator, authority rule, theory, validator, or revision method—and follow each through criticism, operative successor installation, later use, and a further challenge to the successor. The companion draft develops this [recursive-targetability study](./recursive-targetability.md).

Second, measure leverage. Compare matched later revision episodes against a frozen-artifact or simpler-retention baseline. Trace uptake and measure target-identification cost, human decisions, completion time, breadth of supported changes, repair or rollback, and maintenance cost. This separates the contribution of the retained change from task difficulty, model strength, and maintainer experience.

A positive result would show leverage when uptake of a retained change makes a matched later revision cheaper, broader, more reliable, or less dependent on human judgment. Compounding would require those gains to recur without saturating while warranted evaluation capacity scales with them.

The [Bitter Lesson companion](./the-bitter-lesson-does-not-require-everything-to-live-in-weights.md) asks whether search and learning over readable artifacts can scale against weight-based alternatives.

The [self-improving-systems cluster](../notes/self-improving-systems-README.md) maps the underlying theory, and [the retained-operative-path note](../notes/a-retained-operative-path-keeps-improvement-machinery-open-to-revision.md) develops the coverage criterion. If applying them produces a counterexample or disputed classification, leave a comment below.
