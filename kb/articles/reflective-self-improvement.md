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
> A second question follows: who improves the improvement machinery? Five recent papers expose different slices of organizational redesign: several revise agent roles or code, while their evaluators and update protocols remain supplied by their research teams. Commonplace records a partial human–agent path for retaining and reusing changes to organizing machinery. The theoretical Gödel machine makes a much broader rewrite space internal, but accepts only changes whose benefit it can prove from its current formalization.

## What changes count

An agent that is corrected today and repeats the mistake tomorrow wastes the correction. The obvious response is to save the lesson and make later runs use it. Saving alone does not establish that path, and a working path can preserve a bad lesson as effectively as a good one.

Suppose a deployment fails on a Tuesday because a credential expired. An agent reviews the trace, mistakes the date for the cause, and edits its own standing deployment policy to say, "Never deploy on Tuesdays." Later runs act through that policy and therefore avoid Tuesday deployments. The failure supplied evidence bearing on the pre-existing objective of reducing deployment failures, and the resulting change is operative. It nevertheless makes the system worse because the evidence did not justify the causal rule. Self-improvement names an improvement-directed pathway, not a guarantee that every adopted update improves the outcome.

An agent does not need to change its model weights to change itself. Prompts, instruction files, retained memories, tests, validators, and scaffolding code can all determine later behavior, and an LLM agent can inspect and revise them. But not every stored fact that influences behavior is a self-representation. A [self-representation](../notes/definitions/reflective-system.md) represents some declared aspect of the same system and participates causally in that aspect's later operation. The edited deployment policy represents part of the agent's own operating policy, and later runs act through it. A note that merely recorded "the credential expired on Tuesday" would remain a claim about the environment, even if the agent later consulted it.

Software that can inspect or act through such a causally connected representation is computationally reflective. **Reflective self-improvement** combines [self-improvement](../notes/definitions/self-improving-system.md) with [reflection](../notes/definitions/reflective-system.md): evidence bearing on [an independently specifiable objective](../notes/self-improvement-is-relative-to-a-declared-objective.md) must causally influence a change to the system's own [behavior-determining organization](../notes/definitions/behavior-determining-organization.md) through a causally connected self-representation, and the changed organization must govern a subsequent operation within the declared horizon.

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

Across either architecture, declare the boundary, objective, and horizon, then trace who supplies the evidence, determines the update, installs the change, and consumes it later.

## What explicit artifacts add

A readable self-representation makes operative content inspectable. With a scope, reliable retrieval path, and governed revision path, this becomes [addressability](../notes/reflection-buys-addressability.md): a commitment can be named, criticized, revised, or retired individually. For example, "pin production dependencies" is inert in a log no deployment agent searches, but operative and individually revisable when loaded before every release and enforced by a check.

Explicit artifacts can also change the improvement process. If repeated false alarms lead a flaky-test detector to require reproduction on two independent runs, and the next proposed rule is judged under that criterion, the earlier change has altered later selection. This is [reflective leverage](../notes/compounding-needs-leverage-to-multiply-and-autonomy-to-scale.md). Its evidence is use in the next episode, not storage alone.

## Where the builder loop lives

Every experimental self-improvement loop sits inside a larger development loop. Research teams choose its components, edit surface, objective, evaluator, and update rule; they inspect results and redesign that machinery between experiments.

Take a harness optimizer allowed to rewrite a system prompt and three tool descriptions while a fixed test suite decides promotion. It can repair a bad prompt because the prompt lies inside its update space. If the suite rewards the wrong behavior, only the researchers can add adversarial cases or change the promotion rule. That intervention improves the improvement loop rather than the task-facing harness.

The important question is whether that intervention remains external development work for the aspect being changed. [The builder loop becomes internal through an operative redesign path](../notes/the-builder-loop-becomes-internal-through-an-operative-redesign-path.md): the relevant organization is represented, evidence can reach an authorized redesign decision, the accepted change is installed, later work depends on it, and the resulting organization remains open to another challenge. A one-off architectural edit can close the path once without internalizing a repeatable builder loop. Repository-wide write access establishes only possible reach.

> If the research teams behind the five experimental systems were included within the system boundary, they could plainly redesign those systems too. The distinction is not who can redesign the system, but whether the redesign pathway itself becomes part of the system: represented explicitly, used to install accepted changes, and available as a target of later revision.

## The reflective self-improvement test

To test and characterize a claimed reflective self-improvement pathway, ask six questions:

> 1. What boundary was declared before the assessment, over what horizon, and which behavior-shaping structures represent aspects of that same system?
> 2. What independently specifiable objective does the evidence bear on?
> 3. Does that evidence causally influence a change to the system's own behavior-determining organization through its self-representation, rather than merely being stored or retrieved?
> 4. Who or what consumes the installed change, how does it reach that consumer, with what authority does it shape behavior, and which subsequent operation actually depends on it?
> 5. Is the update direct or proposal-selected? If proposal-selected, what performs search, reject-capable evaluation, and operative retention, and which of those functions lie outside the loop's update space?
> 6. Which redesigns of the system's roles, interfaces, objectives, evaluators, or update rules does the reported path demonstrate? Is that builder path represented, retained, operative, and reachable by later revision, or does it remain outside the reported loop?

Questions one through four test occurrence. Question five identifies the update architecture. Question six asks whether the system can revise only supplied parts or has demonstrated organizational reach. The Tuesday policy closes the first four questions and is direct, but it leaves the bad evidence-to-policy rule untouched. Occurrence, outcome, and organizational reach therefore receive different answers.

## Five reported systems

The frames below include each paper's optimization machinery rather than only the base model. **Closed** means the paper establishes the four-link causal path for the named update. **Unestablished** means the evidence does not show one link; it does not mean the link was absent. **Supplied** marks machinery the reported loop consumes but cannot revise. The detailed [omitted-versus-frozen comparison](../notes/an-omitted-loop-function-and-a-frozen-one-need-different-repairs.md) carries the full architecture and lifecycle analysis.

The evidence is also asymmetric. The papers describe experiments, not the full version-control, review, and CI practices of their laboratories, while Commonplace is assessed from a longitudinal repository record. The comparison concerns what the published pathways establish; it does not show that the research teams lack comparable development machinery.

| System | Concrete result | Organizational reach and supplied boundary |
|---|---|---|
| [Self-Harness](../sources/self-harness-harnesses-that-improve-themselves.ingest.md) | Failure traces drive several harness edits; split pass counts select promotion; later evaluations execute merged edits. **Closed** for promoted edits over that evaluation horizon. | It can propose subagent and middleware structure. The reported subagent and skill branches were rejected; retained edits include narrower middleware changes. The objective, failure representation, edit surface, and two-split gate stay supplied. |
| [Continual Harness](../sources/continual-harness-online-adaptation-foundation-agents.ingest.md) | Recent Pokémon trajectory failures directly change prompts, sub-agents, skills, or memory for later game steps. **Closed** for changes later exercised, but not for rarely consulted memory or the many skills never invoked. | Its Refiner creates, edits, and deletes sub-agent roles; its deployment record includes a structural rewrite into a master agent. The four-part partition, Refiner, interfaces, schedule, and reward design stay supplied. |
| [Autogenesis](../sources/autogenesis-a-self-evolving-agent-protocol.ingest.md) | Typed operators evaluate and commit prompt or agent versions reused in later refinement rounds. **Closed** for those revisions. Solution-only evolution changes a work product; Environment and Memory uptake is unestablished. | Enabled agent prompts, tools, and code can change, and specialist participants are replaceable. The resource ontology, named specialist arrangement, bus protocol, evaluator, acceptance rule, and orchestration pattern stay supplied. |
| [Accumulated Behavioral Rules](../sources/self-improving-ai-coding-agents-through-accumulated-rules.ingest.md) | Engineers turn accepted review comments into standing rules loaded by two agent interfaces. No recurrence is reported across 74 later exposures, but rule-level causal uptake is **unestablished** without a trace or comparison that isolates it. | Proposal selection leaves human generalization judgment, the loading scheme, abstraction heuristic, and retirement policy supplied. |
| [Darwin Gödel Machine](../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md) | A parent edits descendant code; viable children enter an archive; benchmark score affects later sampling. **Closed** for descendants later selected and run, not for archive admission alone. | One descendant added an inheritable ranker stage. The diagnostician, admission rule, population controller, objective, and evaluator remain outside descendant edits. |

Taken together, these cases rule out a binary internalized-or-not classification. Continual Harness internalizes a builder loop for some sub-agent organization; Autogenesis does so for enabled agent implementations; the Darwin Gödel Machine reaches descendant agent architecture. None of the five demonstrates a retained path for revising its reported objective or evaluator, and their outer update protocols remain supplied. The right question is: *which redesign class became operative, and which machinery still supplies it?*

The cases also separate creation, delivery, and use. Continual Harness creates many artifacts that never run; Accumulated Behavioral Rules guarantees loading without isolating behavioral dependence; the Darwin Gödel Machine retains children that may never execute again. Update architecture varies independently of all this: four systems use proposal selection, while Continual Harness updates directly, so its absent rejection stage is an architectural choice rather than an omitted universal function.

## What Commonplace brings inside

[Commonplace's declared boundary](../reference/commonplace-declared-frame.md) includes designated maintainers, so this is a human-inclusive comparison rather than an autonomy claim. [ADRs](../reference/design-rationale-management.md) make accepted architectural decisions addressable; contracts, checks, configuration, or code make them operative. [Version-control history](../reference/storage-architecture.md) helps reconstruct change episodes but is neither a rationale record nor an obligatory read path.

The strongest closed case concerns topic indexes. A tag README promised a complete list of notes carrying its tag, but the `learning-theory` head had grown to 55 entries and 18.8 KB, beyond reliable inspection by the editing agent. The accepted redesign introduced explicit `complete` and `covered_by` marks, schema support, and validator checks. Later validation found that block-style YAML tags escaped the documented search recipe, which was then corrected. The [tag-README trace](../reference/tag-readme-trace-observed-causal-connection.md) closes the path: evidence about verification strain changed represented checking machinery, and later operation depended on the new check.

A second case shows builder-level reuse. Unadopted designs lacked a durable home, so [the proposal-lifecycle decision](../reference/adr/028-design-proposals-live-in-reference-proposals.md) introduced a stage between investigation and implementation. A later proposal for an external article collection used that stage and became [the article-layer decision](../reference/adr/057-articles-use-an-editorial-profile-and-excluded-drafts.md). The installed design machinery therefore participated in another redesign, although the evidence does not show that it reduced cost or improved the decision.

Together these cases support partial internalization of a human–agent builder path, not technological uniqueness. A research organization whose design records, authority rules, CI checks, and deployment process satisfy the same causal test would be another instance.

## The Gödel machine internalizes redesign differently

The theoretical [Gödel machine](../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md) attacks the same problem — who improves the improvement machinery — through formal self-reference. Its proof searcher and rewrite machinery lie within the rewrite surface, so a licensed rewrite may replace any software component and, under conditions established by the incumbent system, alter axioms or the utility function.

That broad rewrite space has a strict acceptance boundary. The machine switches only after proving, from its current formalization, that doing so is better than continuing the search. It must therefore ignore effective improvements it cannot prove, even given unlimited computation; finite time and space exclude more. The proposal is theoretical, with no reported implementation, so it establishes a possibility and a tradeoff rather than experimental performance.

Commonplace offers no formal counterpart. It brings part of architectural development into a human–agent process and acts on fallible empirical and semantic grounds. The trade is practical permissiveness for formal assurance: Commonplace supplies neither the Gödel machine's guarantee within its formal model nor assurance that an accepted change is good.

## What the evidence does not yet show

The observed reuse is not evidence of compounding. [Reflective leverage is tested in the next episode](../notes/reflective-leverage-is-tested-in-the-next-episode.md): earlier changes would need to make later improvement cheaper, broader, more reliable, or less dependent on human judgment. The proposal-to-article sequence establishes use, not improvement of the later revision.

A fair test would compare matched architectural revisions with and without an explicit, retained builder path. It would measure target identification, coordination, detection and rollback of bad changes, later reuse, maintenance cost, and human judgment. Until then, the evidence supports an architectural affordance and an observed operating path, not superior performance.

## Where to go next

The practical test now has two levels. Did objective-bearing evidence become an operative change, and was that change adequately warranted? When the supplied organization itself becomes the problem, can evidence reach the builder path that defines roles, checks, and update rules, or can the system change only the parts that its builders already exposed?

The [self-improving-systems cluster](../notes/self-improving-systems-README.md) maps the theory behind the six questions, and [the builder-loop note](../notes/the-builder-loop-becomes-internal-through-an-operative-redesign-path.md) develops the organizational criterion in full. If applying them produces a counterexample or disputed classification, [open an issue](https://github.com/zby/commonplace/issues).
