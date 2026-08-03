---
description: "Defines the causal test for reflective self-improvement, then compares aspect-bounded redesign reach in experimental systems, Commonplace, and the proof-governed Gödel machine"
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
  - kb/notes/the-builder-loop-becomes-internal-through-an-operative-redesign-path.md
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

> **TL;DR.** Reflective self-improvement occurs when evidence bearing on an objective changes the system's behavior-determining organization through a self-representation, and later operation depends on that change. Saving a lesson, installing a rule, or granting write access does not by itself close this causal path.
>
> A second question follows: who improves the improvement machinery? Five recent papers report changes to different parts of agent organization: several revise roles or code, while their evaluators and outer update protocols remain fixed within the reported loop. Commonplace records a partial human–agent path in which architectural changes are explicit, retained, and reused. The theoretical Gödel machine makes a much broader rewrite space internal, but accepts only changes whose benefit it can prove from its current formalization.

## What changes count

Suppose a deployment fails on a Tuesday because a credential expired. An agent reviews the trace, mistakes the date for the cause, and edits its own standing deployment policy to say, "Never deploy on Tuesdays." Later runs act through that policy and therefore avoid Tuesday deployments. The failure supplied evidence bearing on the pre-existing objective of reducing deployment failures, and the resulting change is operative. It nevertheless makes the system worse because the evidence did not justify the causal rule. Self-improvement names an improvement-directed pathway, not a guarantee that every adopted update improves the outcome.

Self-change need not touch model weights: prompts, instructions, memories, tests, validators, and scaffolding can determine later behavior. But not every influential fact is a [self-representation](../notes/definitions/reflective-system.md), which represents some declared aspect of the same system and participates causally in its operation. The Tuesday policy does; a note saying only that the credential expired on Tuesday remains a claim about the environment.

Software that inspects or acts through such a representation is computationally reflective. Combining [self-improvement](../notes/definitions/self-improving-system.md) with [reflection](../notes/definitions/reflective-system.md) yields the causal criterion: evidence bearing on [an independently specifiable objective](../notes/self-improvement-is-relative-to-a-declared-objective.md) must change the system's [behavior-determining organization](../notes/definitions/behavior-determining-organization.md) through that representation. The changed organization must then govern a subsequent operation within a declared assessment horizon—the period or sequence of episodes over which the claim is made.

```text
objective-bearing evidence affects the update
                        ↓
the system's own organization changes
                        ↓
the change enters a live behavioral path
                        ↓
a subsequent operation depends on the change
```

A stored trace that never affects an updater fails at the first transition. A proposed rule that is never installed fails at the second. A rule that is loaded but ignored fails at the last. The Tuesday update completes the path despite its harmful result.

How the update is determined is a separate architectural question. A **direct update** makes an evidence-determined successor the incumbent without exposing a separately rejectable candidate. A **proposal-selection update** generates candidates, evaluates them with the possibility of rejection, and makes an accepted change operative. That subtype requires [search, reject-capable evaluation, and operative retention](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md).

The Tuesday policy is a direct update. Its lack of a rejection stage is an architectural fact, not an omitted universal function. Its weakness lies in the evidence-to-policy update rule, which turns a coincidence into a standing policy.

## What explicit artifacts add

A readable self-representation makes operative content inspectable. With a scope, reliable retrieval path, and governed revision path, this becomes [addressability](../notes/reflection-buys-addressability.md): a commitment can be named, criticized, revised, or retired individually. For example, "pin production dependencies" is inert in a log no deployment agent searches, but operative and individually revisable when loaded before every release and enforced by a check.

Explicit artifacts can also change the improvement process. If repeated false alarms lead a flaky-test detector to require reproduction on two independent runs, and the next proposed rule is judged under that criterion, the earlier change has altered later selection. That closes the causal path through the improvement process: the earlier criterion matters because a later episode uses it. Whether the change improves that episode is a separate question.

## Where the builder loop lives

Apply the same causal test one level up. Every experimental self-improvement loop sits inside a larger development loop. Research teams choose its components, edit surface, objective, evaluator, and update rule; they inspect results and redesign that machinery between experiments.

Take a harness optimizer allowed to rewrite a system prompt and three tool descriptions while a fixed test suite decides promotion. It can repair a bad prompt because the prompt lies inside its update space. If the suite rewards the wrong behavior, only the researchers can add adversarial cases or change the promotion rule. That intervention improves the improvement loop rather than the task-facing harness.

> If the research teams behind the five experimental systems were included within the system boundary, they could plainly redesign those systems too. The distinction is not who can redesign the system, but whether the redesign pathway itself becomes part of the system: represented explicitly, used to install accepted changes, and available as a target of later revision.

The [operative-path criterion](../notes/the-builder-loop-becomes-internal-through-an-operative-redesign-path.md) adds two requirements to that boundary claim: evidence must reach an authorized redesign decision, and later work must depend on the installed result. A one-off edit can meet those requirements once without making the path repeatable; repository-wide write access establishes only possible reach.

The evidence is asymmetric: the papers describe experiments, while Commonplace is assessed from a longitudinal repository record. The comparison therefore concerns only what those records establish.

## The reflective self-improvement test

The causal path and builder-loop question combine into six questions:

> 1. What boundary and horizon were declared before the assessment, and which behavior-shaping structures represent aspects of that same system?
> 2. What independently specifiable objective does the evidence bear on?
> 3. Does that evidence change the system's behavior-determining organization through its self-representation, rather than merely being stored or retrieved?
> 4. How does the installed change reach its consumer, with what authority does it shape behavior, and which subsequent operation depends on it?
> 5. Is the update direct or proposal-selected? If proposal-selected, what performs search, reject-capable evaluation, and operative retention, and which functions lie outside the loop's update space?
> 6. Which redesigns of the system's roles, interfaces, objectives, evaluators, or update rules does the reported path demonstrate? Is the builder path itself represented, retained, operative, and open to later revision?

Questions one through four test occurrence; question five identifies the update architecture; question six measures demonstrated organizational reach. The Tuesday policy closes the first four and is direct, but leaves its bad evidence-to-policy rule untouched. Occurrence, outcome, and organizational reach can therefore differ.

## Five reported systems

The table treats each paper's optimization machinery as part of the assessed system, rather than only the base model. **Closed** means the paper establishes the four-link path for the named update. **Unestablished** means the evidence does not show one link, not that the link was absent. **Supplied** marks machinery fixed by the reported design and outside the loop's demonstrated revision reach. The [omitted-versus-frozen comparison](../notes/an-omitted-loop-function-and-a-frozen-one-need-different-repairs.md) gives the fuller architecture and lifecycle analysis.

| System | Concrete result | Organizational reach and supplied boundary |
|---|---|---|
| [Self-Harness](../sources/self-harness-harnesses-that-improve-themselves.ingest.md) | Failure traces drive several harness edits; split pass counts select promotion; later evaluations execute merged edits. **Closed** for promoted edits over that evaluation horizon. | It can propose subagent and middleware structure. The reported subagent and skill branches were rejected; retained edits include narrower middleware changes. The objective, failure representation, edit surface, and two-split gate stay supplied. |
| [Continual Harness](../sources/continual-harness-online-adaptation-foundation-agents.ingest.md) | Recent Pokémon trajectory failures directly change prompts, sub-agents, skills, or memory for later game steps. **Closed** for changes later exercised, but not for rarely consulted memory or the many skills never invoked. | Its Refiner creates, edits, and deletes sub-agent roles; its deployment record includes a structural rewrite into a master agent. The four-part partition, Refiner, interfaces, schedule, and reward design stay supplied. |
| [Autogenesis](../sources/autogenesis-a-self-evolving-agent-protocol.ingest.md) | Typed operators evaluate and commit prompt or agent versions reused in later refinement rounds. **Closed** for those revisions. Solution-only evolution changes the task output rather than the assessed system's organization; Environment and Memory uptake is unestablished. | Enabled agent prompts, tools, and code can change, and specialist participants are replaceable. The resource ontology, named specialist arrangement, bus protocol, evaluator, acceptance rule, and orchestration pattern stay supplied. |
| [Accumulated Behavioral Rules](../sources/self-improving-ai-coding-agents-through-accumulated-rules.ingest.md) | Engineers turn accepted review comments into standing rules loaded by two agent interfaces. No recurrence is reported across 74 later exposures, but rule-level causal uptake is **unestablished** without a trace or comparison that isolates it. | Proposal selection leaves human generalization judgment, the loading scheme, abstraction heuristic, and retirement policy supplied. |
| [Darwin Gödel Machine](../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md) | A parent edits descendant code; viable children enter an archive; benchmark score affects later sampling. **Closed** for descendants later selected and run, not for archive admission alone. | One descendant added an inheritable ranker stage. The diagnostician, admission rule, population controller, objective, and evaluator remain outside descendant edits. |

These cases resist a whole-system yes-or-no classification. Continual Harness makes parts of sub-agent reorganization internal; Autogenesis does so for enabled agent implementations; the Darwin Gödel Machine reaches descendant agent architecture. None demonstrates a retained path for revising its reported objective or evaluator, and their outer update protocols remain supplied. The useful question is: *which redesign class became operative, and which machinery still supplies it?*

Creation, delivery, and use also differ: Continual Harness creates artifacts that never run; Accumulated Behavioral Rules guarantees loading without isolating behavioral dependence; the Darwin Gödel Machine retains children that may never execute again. Continual Harness uses direct updating while the other four use proposal selection, but that distinction does not determine organizational reach.

## What Commonplace brings inside

[Commonplace's declared boundary](../reference/commonplace-declared-frame.md) includes designated maintainers, so this is a human-inclusive comparison rather than an autonomy claim.

Within that boundary, [architecture decision records (ADRs)](../reference/design-rationale-management.md) make accepted architectural decisions addressable; contracts, checks, configuration, or code make them operative. [Version-control history](../reference/storage-architecture.md) helps reconstruct change episodes but is neither a rationale record nor an obligatory read path.

The strongest closed case concerns topic indexes. A tag README promised a complete list of notes carrying its tag, but the `learning-theory` head had grown to 55 entries and 18.8 KB, beyond reliable inspection by the editing agent. The accepted redesign introduced explicit `complete` and `covered_by` marks, schema support, and validator checks. Later validation found that block-style YAML tags escaped the documented search recipe, which was then corrected. The [tag-README trace](../reference/tag-readme-trace-observed-causal-connection.md) closes the path: evidence about verification strain changed Commonplace's explicit checking machinery, and later validation depended on the new check.

A second case shows builder-level reuse. Unadopted designs lacked a durable home, so [the proposal-lifecycle decision](../reference/adr/028-design-proposals-live-in-reference-proposals.md) introduced a stage between investigation and implementation. A later proposal for an external article collection moved through that stage and became [the article-layer decision](../reference/adr/057-articles-use-an-editorial-profile-and-excluded-drafts.md). The second redesign therefore used machinery installed by the first, though the evidence does not show lower cost or a better decision.

Together they establish the partial human–agent builder path claimed here: an organizational update that became operative, and design machinery reused in a later redesign.

## What the Commonplace evidence does not yet show

The proposal-to-article sequence establishes reuse, not compounding. To demonstrate [reflective leverage](../notes/reflective-leverage-is-tested-in-the-next-episode.md), earlier changes would need to make later improvement cheaper, broader, more reliable, or less dependent on human judgment.

A fair test would compare matched architectural revisions with and without an explicit, retained builder path. It would measure target identification, coordination, detection and rollback of bad changes, later reuse, maintenance cost, and human judgment. No such comparison is reported here.

## The Gödel machine internalizes redesign differently

The theoretical [Gödel machine](../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md) addresses the same meta-level problem through formal self-reference. Its proof searcher and rewrite machinery lie within the rewrite surface, so a licensed rewrite may replace any software component and, under conditions established by the incumbent system, alter its axioms or utility function.

That broad rewrite space has a strict acceptance boundary. The machine switches only after proving, from its current formalization, that doing so is better than continuing the search. It must therefore ignore effective improvements it cannot prove, even given unlimited computation; finite time and space exclude more. The proposal is theoretical, with no reported implementation, so it establishes a possibility and a tradeoff rather than experimental performance.

Commonplace does not require a formal proof before changing its architecture. Its human–agent process acts on fallible empirical and semantic grounds, supplying neither the Gödel machine's guarantee within its formal model nor assurance that an accepted change is good.

## Where to go next

Apply the test at two levels. Did objective-bearing evidence produce an operative, warranted change? When the supplied organization itself becomes the problem, can evidence reach the builder path that defines roles, checks, and update rules, or only the parts that its builders already exposed?

The [self-improving-systems cluster](../notes/self-improving-systems-README.md) maps the theory behind the six questions, and [the builder-loop note](../notes/the-builder-loop-becomes-internal-through-an-operative-redesign-path.md) develops the organizational criterion in full. If applying them produces a counterexample or disputed classification, [open an issue](https://github.com/zby/commonplace/issues).
