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

> **TL;DR.** Reflective self-improvement occurs when evidence relevant to an objective changes a system's behavior-determining organization through a self-representation, and later operation depends on that change. When the change is retained in a readable, addressable artifact, it can be inspected and selectively revised. *Meta* is a role, not a fixed layer; recursive targetability is the additional property that lets an artifact governing one revision become the target of a later one. If reusing an earlier retained change causes a later revision to become cheaper, broader, more reliable, or less dependent on human judgment, the change has leverage.
>
> Five reported systems expose different bounded update surfaces, with evidence ranging from closed operative paths to artifacts that were only created, retained, or loaded. In Commonplace, later work reuses earlier changes to checking and design methods, making leverage testable. The working hypothesis is that making human–agent architectural revision explicit, retained, and repeatable raises later revision productivity. Repeated leverage can compound when warranted computational checks carry the growing evaluation load. The theoretical Gödel machine places its software rewrite machinery inside a proof-governed update surface, but cannot license beneficial changes its incumbent formalization cannot prove.

## What changes count

For this example, the system comprises the agent, its standing deployment policy, and the runtime that loads it; the assessment covers the next several deployments. Suppose a deployment fails on a Tuesday because a credential expired. The agent mistakes the date for the cause and changes its policy to "Never deploy on Tuesdays." Later runs obey. The failure supplied evidence about the objective of reducing deployment failures, and the change became operative, but the causal inference was wrong. Self-improvement names an improvement-directed pathway, not a guarantee that every adopted update helps.

Self-change need not touch model weights: prompts, instructions, memories, tests, validators, and scaffolding can determine later behavior. But not every influential fact is a [self-representation](../notes/definitions/reflective-system.md), which represents some declared aspect of the same system and participates causally in its operation. The standing policy represents the system's deployment rule because the runtime reads it to govern deployments; a note recording only the credential expiry describes the environment.

A system is computationally reflective when its own processes inspect or act through such a representation. Reflective [self-improvement](../notes/definitions/self-improving-system.md) combines that structure with improvement-directed change: evidence bearing on [an independently specifiable objective](../notes/self-improvement-is-relative-to-a-declared-objective.md) changes the system's [behavior-determining organization](../notes/definitions/behavior-determining-organization.md) through the representation, and the changed organization governs a subsequent operation within a declared assessment horizon.

```text
objective-bearing evidence affects the update
                        ↓
the system's organization changes through its self-representation
                        ↓
the change enters a live behavioral path
                        ↓
a subsequent operation depends on the change
```

A stored trace that never affects an updater fails at the first transition. A proposed rule that is never installed fails at the second. A rule that is loaded but ignored fails at the last. The Tuesday update completes the path despite its harmful result.

Two update architectures fit this causal criterion. The Tuesday policy is a **direct update**: it makes an evidence-determined successor incumbent without exposing a separately rejectable candidate. Its failure lies in the evidence-to-policy rule, which turns a coincidence into standing policy. A **proposal-selection update** instead generates candidates, permits rejection, and makes an accepted change operative. That subtype requires [search, reject-capable evaluation, and operative retention](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md).

## From addressability to leverage

A readable self-representation can make a retained commitment [addressable](../notes/reflection-buys-addressability.md). Given a scope, reliable retrieval path, and governed revision path, the commitment can be named, criticized, revised, or retired individually.

*Meta* names a role within an improvement episode, not a permanent architectural layer: an evaluator is meta to the prompt it judges. **Recursive targetability** is stronger. It obtains when an artifact governing one episode can become the target of a later governed episode, and its installed successor remains inside the addressable revision domain. Each transition is still judged under an incumbent objective, criterion, or method; any of those may become a later target. No permanently higher controller is required.

When a later improvement episode depends on an earlier retained result, the result is reused. It has [reflective leverage](../notes/compounding-needs-leverage-to-multiply-and-autonomy-to-scale.md) if that dependence improves the later episode's diagnosis, evaluation, updating, or retention, making the episode cheaper, broader, more reliable, or less dependent on human judgment. When such gains recur, revision productivity compounds. Sustaining that growth requires evaluation capacity to scale with it; warranted computational checks can carry an increasing share of that load.

Take a harness optimizer whose update space includes a system prompt and three tool descriptions, while a fixed test suite decides promotion. This gives possible reach over those artifacts; demonstrated reach begins only when an accepted edit becomes operative and later behavior depends on it. The suite occupies the meta role for those edits but remains outside the path's update space, so it cannot become a target within the same path.

## The reflective self-improvement test

The argument yields six diagnostic questions:

> 1. What system boundary and assessment horizon are declared, and which structures represent the system within that boundary?
> 2. What independently specifiable objective does the evidence bear on?
> 3. Does that evidence change the system's behavior-determining organization through its self-representation, rather than merely being stored or retrieved?
> 4. How does the installed change reach its consumer? What authority does it have, and which subsequent operation depends on it?
> 5. Is the update direct or proposal-selected? If proposal-selected, what searches, evaluates with the power to reject, and retains accepted changes? Which functions remain outside its update space?
> 6. Which represented parts changed? What later work uses their successors? Can both the governing artifacts and the installed successors become targets of later governed revision?

The first four questions test whether reflective self-improvement occurred; the fifth identifies the update architecture; the sixth maps revision reach, recursive targetability, and later reuse. The Tuesday policy closes the first four and is direct, but leaves its faulty evidence-to-policy rule untouched. Demonstrating leverage requires a separate comparison of later revision productivity.

## A proof-governed limit case

The theoretical [Gödel machine](../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md) addresses the same revision problem through formal self-reference. Its proof searcher and rewrite machinery lie within the rewrite surface, so a licensed rewrite may replace any software component and, under conditions established by the incumbent system, alter its axioms or utility function.

That broad rewrite space has a strict acceptance boundary. The machine switches only after proving, from its current formalization, that doing so is better than continuing the search. It therefore cannot license beneficial rewrites whose value the incumbent formalization cannot prove, even with unlimited computation; finite resources exclude more. This is a theoretical possibility and tradeoff, not an experimental result.

The Gödel machine is the formal limit case for role-relative reach: its proof searcher governs rewrites in one episode yet remains eligible for a later licensed rewrite. Commonplace makes the analogous structural move under a different acceptance regime. In proposal-selected architectural revisions such as those discussed below, a candidate is judged against continuing with the incumbent arrangement on fallible empirical and semantic grounds rather than formal proof.

## Five reported systems

The five reported systems expose narrower, empirically observed update surfaces. The table applies the six questions to each reported path, treating its optimization machinery—not only the base model—as part of the assessed system. **Closed** means the record shows objective-relevant evidence changing a represented part of the assessed system's organization, with a later operation depending on the installed change. **Unestablished** means the record does not close that path. **Supplied** marks machinery fixed by the reported design and outside the path's demonstrated revision reach. In role terms, supplied gates, evaluators, Refiners, and controllers govern the reported updates without themselves becoming demonstrated targets.

| System | Reported causal path | Demonstrated revision reach and supplied machinery |
|---|---|---|
| [Self-Harness](../sources/self-harness-harnesses-that-improve-themselves.ingest.md) | Failure traces drive several harness edits; pass counts on two splits determine promotion; later evaluations execute merged edits. **Closed** for promoted edits over that evaluation horizon. | Its proposal surface includes subagent, skill, and middleware structure. Because the subagent and skill proposals were rejected, demonstrated operative reach is limited to narrower middleware edits. The objective, failure representation, edit surface, and two-split gate stay supplied. |
| [Continual Harness](../sources/continual-harness-online-adaptation-foundation-agents.ingest.md) | Recent Pokémon trajectory failures directly change prompts, sub-agents, skills, or memory for later game steps. **Closed** for changes later exercised, but not for rarely consulted memory or the many skills never invoked. | Its Refiner creates, edits, and deletes sub-agent roles; its deployment record includes a structural rewrite into a master agent. The four-part partition, Refiner, interfaces, schedule, and reward design stay supplied. |
| [Autogenesis](../sources/autogenesis-a-self-evolving-agent-protocol.ingest.md) | Typed operators evaluate and commit prompt or agent versions reused in later refinement rounds. **Closed** for those revisions. Solution-only evolution changes the task output rather than the assessed system's organization; Environment and Memory uptake is unestablished. | Reported revisions reach enabled agent prompts, tools, and code. Specialist replacement is possible but not demonstrated in the experiments. The resource ontology, named specialist arrangement, bus protocol, evaluator, acceptance rule, and orchestration pattern stay supplied. |
| [Accumulated Behavioral Rules](../sources/self-improving-ai-coding-agents-through-accumulated-rules.ingest.md) | Engineers turn accepted review comments into standing rules loaded by two agent interfaces. The paper reports no recurrence across 74 later exposures, but does not isolate whether any individual rule caused that result, so causal uptake is **unestablished**. | The reported path installs rules in the standing layer, but behavioral dependence is unestablished. Human generalization judgment, the loading scheme, abstraction heuristic, and retirement policy stay supplied. |
| [Darwin Gödel Machine](../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md) | A parent edits descendant code; viable children enter an archive; benchmark score affects later sampling. **Closed** for descendants later selected and run, not for archive admission alone. | One descendant added an inheritable ranker stage. The diagnostician, admission rule, population controller, objective, and evaluator remain outside descendant edits. |

The classifications attach to reported paths, not whole systems. The useful question is: *which redesign became operative, and which governing artifacts remained outside demonstrated reach?*

The cases also separate creation from use. Continual Harness creates some artifacts that never run; Accumulated Behavioral Rules guarantees loading without isolating behavioral dependence; the Darwin Gödel Machine retains children that may never execute again. Continual Harness uses direct updating while the other four use proposal selection, but that distinction does not determine revision reach. The [omitted-versus-frozen comparison](../notes/an-omitted-loop-function-and-a-frozen-one-need-different-repairs.md) develops the lifecycle analysis.

## Commonplace makes architectural revision reusable

> If the five experimental systems included the research teams that built them, those teams could plainly redesign the systems. Commonplace makes part of this human–agent architectural revision explicit, retained, and repeatable rather than leaving it as an unrecorded intervention by researchers.

The five systems expose bounded revision surfaces over supplied machinery. Commonplace instead treats the meta role as temporary: repository-defined artifacts that govern one episode remain eligible as targets in another. It represents theory, architecture, evaluators, and revision methods alongside the instructions, checks, configuration, and code that make decisions operative; some artifacts both describe and govern the system. An operative change demonstrates reach to one target. A later governed challenge to its successor demonstrates recursive targetability. The [declared substrate boundary](../reference/commonplace-declared-frame.md) bounds the claim; coverage inside it remains empirical.

The papers report bounded experiments; Commonplace offers a longitudinal repository record whose boundary includes designated maintainers. [Architecture decision records (ADRs)](../reference/design-rationale-management.md) make accepted decisions addressable, while operative artifacts carry them into later work. [Version-control history](../reference/storage-architecture.md) helps reconstruct a change episode but does not by itself record its rationale or make the result operative.

The clearest case concerns topic indexes. A tag README promised a complete list of notes carrying its tag, but the `learning-theory` head had grown to 55 entries and 18.8 KB, beyond reliable inspection by the editing agent. The redesign introduced explicit `complete` and `covered_by` marks, schema support, and validator checks. Later validation found that block-style YAML tags escaped the documented search recipe, which was then corrected. The [tag-README trace](../reference/tag-readme-trace-observed-causal-connection.md) closes an operative redesign and its later reuse: verification strain changed the checking machinery; that machinery then exposed the search blind spot and prompted the correction.

A second case shows reuse of revision machinery. Unadopted designs lacked a durable home, so [the proposal-lifecycle decision](../reference/adr/028-design-proposals-live-in-reference-proposals.md) introduced a stage between investigation and implementation. A later proposal for an article collection moved through that stage and became [the article-layer decision](../reference/adr/057-articles-use-an-editorial-profile-and-excluded-drafts.md). The later redesign therefore depended on machinery installed by the earlier one, establishing reuse. The leverage study asks whether that reuse made the later redesign more productive.

## Testing the working claim

The Commonplace cases make leverage testable. The working hypothesis is that retained decisions and operative revision machinery make later architectural change easier to initiate, coordinate, check, and revisit. Testing it has two parts.

First, map role-relative reach. Choose artifacts that currently govern revision—an objective, evaluator, authority rule, theory, validator, or revision method—and follow each through criticism, operative successor installation, later use, and a further challenge to the successor. The companion draft develops this [recursive-targetability study](./recursive-targetability.md).

Second, measure leverage. Compare matched later revision episodes against a frozen-artifact or simpler-retention baseline. Trace uptake and measure target-identification cost, human decisions, completion time, breadth of supported changes, repair or rollback, and maintenance cost. This separates the contribution of the retained change from task difficulty, model strength, and maintainer experience.

A positive result would show leverage when uptake of a retained change makes a matched later revision cheaper, broader, more reliable, or less dependent on human judgment. Repeated leverage, sustained as warranted computational checks absorb rising evaluation work, would show compounding.

The [self-improving-systems cluster](../notes/self-improving-systems-README.md) maps the underlying theory, and [the retained-operative-path note](../notes/a-retained-operative-path-keeps-improvement-machinery-open-to-revision.md) develops the coverage criterion. If applying them produces a counterexample or disputed classification, leave a comment below.
