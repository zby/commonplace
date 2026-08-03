---
description: "Defines the causal test for reflective self-improvement, then compares externally redesigned experimental loops, Commonplace's retained human–agent redesign path, and the proof-governed Gödel machine"
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
  - kb/notes/a-consumption-channel-delivers-force-without-the-history-that.md
  - kb/notes/an-omitted-loop-function-and-a-frozen-one-need-different-repairs.md
  - kb/notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md
  - kb/reference/commonplace-declared-frame.md
  - kb/reference/commonplace-as-a-reflective-system.md
  - kb/reference/storage-architecture.md
  - kb/reference/tag-readme-trace-observed-causal-connection.md
  - kb/reference/tag-readme-trace-as-self-improving-loop.md
  - kb/reference/adr/007-reports-directory-for-generated-snapshots.md
  - kb/reference/adr/028-design-proposals-live-in-reference-proposals.md
  - kb/reference/adr/057-articles-use-an-editorial-profile-and-excluded-drafts.md
  - kb/sources/self-harness-harnesses-that-improve-themselves.ingest.md
  - kb/sources/continual-harness-online-adaptation-foundation-agents.ingest.md
  - kb/sources/autogenesis-a-self-evolving-agent-protocol.ingest.md
  - kb/sources/self-improving-ai-coding-agents-through-accumulated-rules.ingest.md
  - kb/sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md
---

# Reflective self-improvement

> **TL;DR.** For reflective self-improvement to occur, objective-bearing evidence must change the system's behavior-determining organization through a self-representation, and a later operation must depend on that change. Establish this causal structure before classifying the update as direct, proposal-selected, or a composition.
>
> Every self-improvement loop also sits inside a builder loop that chooses its parts, objectives, evaluators, and update rules. The five papers examined here mostly report agents improving within organizations supplied by their research teams. The papers generally do not establish that the teams' redesign work enters a retained pathway that the reported system later uses and can revise again.
>
> Commonplace demonstrates a partial alternative: parts of its human–agent redesign path are explicit, retained, and operative, so roles and checks introduced through that path can become later revision targets. Whether this improves outcomes remains untested. The theoretical Gödel machine addresses the same meta-level problem more broadly through formal self-reference, but can adopt only rewrites whose benefit it can prove from its current formalization.

## What this article argues

| Claim | Standing |
|---|---|
| Reflective self-improvement requires a closed causal path from objective-bearing evidence, through self-representation and operative organizational change, into later behavior; direct and proposal-selected updates implement that path differently. | Core criterion |
| The important architectural question is where redesign of the improvement machinery occurs: in an external builder loop, or in a represented path whose accepted changes govern later work and can themselves become revision targets. | Core thesis |
| The five papers mostly demonstrate adaptation inside supplied organizations. Commonplace records partial internalization of its human–agent builder loop, including repeated organizational revisions and one later reuse of newly installed design machinery. This is a comparison of reported evidence, not proof that the research teams lack comparable development machinery. | Source-grounded comparison |
| The Gödel machine internalizes broad redesign behind a proof requirement. Commonplace accepts fallible empirical and semantic grounds without such a proof; whether that path improves diagnosis, maintenance cost, or outcomes remains open. | Theoretical contrast and open question |

## What changes count

An agent that is corrected today and repeats the mistake tomorrow wastes the correction. The obvious response is to save the lesson and build a path by which later runs use it. Saving alone does not establish that path, and a working path can preserve a bad lesson as effectively as a good one.

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

A stored trace that never affects an updater fails at the evidence-to-update transition. A proposed rule that is never installed fails at installation. A rule that is loaded but ignored fails at behavioral uptake. Each is a missing transition in the general anatomy. The Tuesday update completes the path despite its harmful result.

How the update is determined is a separate architectural question. A **direct update** makes an evidence-determined successor the incumbent without exposing a separately rejectable candidate. A **proposal-selection update** generates candidates, evaluates them with the possibility of rejection, and makes an accepted change operative. That subtype requires [search, reject-capable evaluation, and operative retention](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md).

The Tuesday policy is a direct update. Its lack of a rejection stage is an architectural fact, not an omitted universal function. Its weakness lies in the evidence-to-policy update rule, which turns a coincidence into a standing policy.

Across either architecture, declare the boundary, objective, and horizon, then trace who supplies the evidence, determines the update, installs the change, and consumes it later. Proposal selection further separates search, evaluation, and operative retention.

## What explicit artifacts buy

A readable self-representation makes operative content inspectable rather than leaving it to be inferred from behavior. When it also has a scope, a reliable retrieval path, and a governed revision path, that legibility becomes [addressability](../notes/reflection-buys-addressability.md): the represented commitment can be named, criticized, rescoped, revised, or retired individually. A long unindexed instruction log is readable but not operationally addressable.

Consider two ways to retain the instruction "pin production dependencies." In the first, it is appended to a log that no deployment agent searches. The sentence is readable but inert. In the second, it is placed in the deployment policy loaded before every release, scoped to production packages, and covered by a check that rejects unpinned manifests. The policy can now be inspected and revised as one commitment, and later releases demonstrate its behavioral path. The artifact's value comes from the combination of readable content, a known consumer, a delivery channel, and enough authority to affect action.

An explicit artifact can also change the improvement process rather than only task behavior. Suppose a flaky-test detector initially promotes a new rule after one failure. After repeated false alarms, the team changes the acceptance criterion to require reproduction on two independent runs. If the next proposed rule is judged under that new criterion, the earlier change has altered how later changes are selected. This is [reflective leverage](../notes/compounding-needs-leverage-to-multiply-and-autonomy-to-scale.md). Saving the new criterion is not enough; its use in the next selection episode is the evidence.

## Where the builder loop lives

Every experimental self-improvement loop sits inside a larger development loop. Research teams choose the components, edit surface, objectives, evaluators, and update rules; they inspect results and redesign that machinery between experiments. Those are real changes made in pursuit of improvement, but across the five papers compared here they are generally treated as work done by the builders around the reported loop, not as changes produced and retained by that loop.

Take a harness optimizer allowed to rewrite a system prompt and three tool descriptions. A test suite decides which rewrite is promoted. When failures come from a bad prompt, the optimizer can repair them. When failures come from the test suite rewarding the wrong behavior, the optimizer cannot repair the evaluator that defines success. Researchers may add adversarial cases, change the promotion rule, or expose a new editable component. That second intervention improves the improvement loop rather than the task-facing harness. The architectural question is whether this intervention remains external development work or enters a represented path that future operation can inspect, apply, and revise.

Put as a ladder, these pathways usually add one improvement level above task behavior: the loop can revise the agent, while researchers at the next level revise the loop. Adding another fixed controller only moves the boundary upward. The stronger goal is to make the upward move repeatable: when current roles, routes, checks, or update machinery become the problem, they can become explicit revision targets through a path whose resulting organization remains open to later challenge.

> If the research teams behind the five experimental systems were included within the system boundary, they could plainly redesign those systems too. The distinction is not who can redesign the system, but whether the redesign pathway itself becomes part of the system: represented explicitly, used to install accepted changes, and available as a target of later revision.

The available evidence is asymmetric. The papers were written to explain experiments, not the full version-control, review, and CI practices of their laboratories; Commonplace is assessed from its own longitudinal repository record. The comparison therefore concerns what the published improvement pathways establish. A laboratory workflow could meet the same criterion if its design rationale, authority, installation path, and later use were retained as revisable parts of the claimed system. Nothing here establishes that the five research teams lack such a workflow.

Merely expanding the declared boundary or granting repository-wide write access does not establish this property. The builder's intervention must enter a recognized path: the relevant organization is represented; the participants and authority are identifiable; the rationale and decision remain inspectable; the accepted change is installed in instructions, configuration, checks, or code that later operation uses; and later evidence can challenge it again. This path need not use proposal selection in every episode.

Architectural changes are also harder to control than many changes within an existing part. The current decomposition shapes diagnosis and credit assignment, so a mistaken parts list [constrains which causes and repairs become visible](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md). A reorganization may require coordinated edits across prompts, schemas, routing, code, tests, and documentation, while its value may appear only across later tasks. Raw mutability therefore says less than demonstrated ability to diagnose, formulate, evaluate, install, and later use such a change.

## Where the pathway breaks

Bringing the builder path inside does not remove failures of causation or warrant. Retrieval and authority paths can break the causal path; verification asks whether the evidence-to-change rule should be trusted.

Retrieval can break both ends of the path. A saved trace cannot guide an updater that never finds it, and a retained policy cannot affect a later run that never loads it. In a retrieval-mediated system, [failing to retrieve the relevant self-representation is a failure of the reflective pathway itself](../notes/retrieval-failure-is-reflection-failure.md), not a performance detail. Even successful loading may fall short if the model ignores the content.

The write side is an attack surface. The Tuesday case shows why: [a consumption channel delivers behavioral force without the history that produced the content](../notes/a-consumption-channel-delivers-force-without-the-history-that.md). An untrusted tool result can exploit the same path by telling the agent to save a directive — anything allowed to write into the instruction path can modify the system. Provenance, write authority, review, and rollback can govern that path; which controls are required depends on its force and risk.

Nothing must remain outside the loop forever, but something must stand outside each particular change. A change must be determined or admitted under controls whose authority and scope were in place before it and that the change could not rewrite on its way in. In a direct path this may be an incumbent update law and scope boundary; in proposal selection it includes the incumbent acceptance rule. Those controls can themselves be replaced later under controls that predate that later change, so no evaluator must remain permanently frozen.

Passing that structural test establishes control, not benefit. In a direct update, improvement warrant rests on the objective, evidence signal, update rule, and their domain assumptions. Proposal selection adds the question of why the evaluator deserves weight. Tests and proofs can settle mechanically decidable properties, while semantic review can apply an incumbent criterion in a fresh context, removing the generation trajectory but not blind spots shared with the generator. Following an authorized procedure, making a good change, and being safe enough to experiment are three different claims.

## The reflective self-improvement test

To test and characterize a claimed reflective self-improvement pathway, ask six questions:

> 1. What boundary was declared before the assessment, over what horizon, and which behavior-shaping structures represent aspects of that same system?
> 2. What independently specifiable objective does the evidence bear on?
> 3. Does that evidence causally influence a change to the system's own behavior-determining organization through its self-representation, rather than merely being stored or retrieved?
> 4. Who or what consumes the installed change, how does it reach that consumer, with what authority does it shape behavior, and which subsequent operation actually depends on it?
> 5. Is the update direct or proposal-selected? If proposal-selected, what performs search, reject-capable evaluation, and operative retention, and which of those functions lie outside the loop's update space?
> 6. Which redesigns of the system's roles, interfaces, objectives, evaluators, or update rules does the reported path demonstrate? Is that builder path represented, retained, operative, and reachable by later revision, or does it remain outside the reported loop?

Questions one through four test an observed reflective self-improvement claim. If one is missing, the claimed pathway does not close at that link. Question five identifies the update architecture. Search, reject-capable evaluation, and operative retention become required diagnostics only after the path is identified as proposal selection; a direct update has no omitted evaluator merely because it lacks a rejection stage. Question six locates the builder loop and asks about demonstrated organizational reach rather than technical writability.

The Tuesday policy shows how the questions work together. Take the boundary to include the deployment agent, its updater, and its standing policy, and assess the next 30 days. The objective is fewer failed deployments. The expired-credential trace affects the updater, which replaces the current policy with "Never deploy on Tuesdays." The release agent loads that policy as a binding instruction and skips the next scheduled Tuesday release, so the causal path closes. The update is direct because no separately rejectable candidate was evaluated. But question six finds no builder-level change: the rule that converted one co-occurrence into policy remains untouched. The case therefore qualifies as an observed, harmful, direct reflective self-improvement episode with no demonstrated redesign of its improvement machinery. Membership, outcome, and organizational reach receive different answers.

## Applying the test to five reported systems

The assessment needs a frame before it needs a verdict. The boundaries below include each paper's optimization machinery rather than treating only the base model as the system. Accumulated Behavioral Rules also includes the engineers who decide whether feedback becomes a rule, and the Darwin Gödel Machine uses the composite archive-and-population process. These are this article's assessed frames, not necessarily the frames under which the papers state their claims.

| System | Assessed boundary | Objective | Horizon |
|---|---|---|---|
| [Self-Harness](../sources/self-harness-harnesses-that-improve-themselves.ingest.md) | The target model, harness, candidate generator, two-split gate, and merge path | Increase task pass count without regressing either split | From failure collection through promotion and subsequent harness evaluations |
| [Continual Harness](../sources/continual-harness-online-adaptation-foundation-agents.ingest.md) | The acting agent, Refiner, mutable prompt/sub-agent/skill/memory harness, and persistent game episode; the separate weight loop is reported separately | Improve progress through the Pokémon episode, measured through milestones, reward signals, and button efficiency | From one refinement window into later steps of the same continuous episode |
| [Autogenesis Reflection optimizer](../sources/autogenesis-a-self-evolving-agent-protocol.ingest.md) | The resource substrate, reflection optimizer, enabled resources, evaluator, and commit path | Improve correctness under the configured task evaluator | Across the configured refinement rounds and reuse of committed resource versions |
| [Accumulated Behavioral Rules](../sources/self-improving-ai-coding-agents-through-accumulated-rules.ingest.md) | The coding agents, engineers, standing rule file, checklists, and loading path | Prevent recurrence of accepted code-review problem classes | From rule promotion through later sessions in the four-week deployment |
| [Darwin Gödel Machine](../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md) | The archive, population controller, diagnostician, parent agent, descendant code, viability check, and benchmark scoring | Improve coding-benchmark performance while retaining compilation and code-editing ability | Across the reported 80 archive iterations and descendant lineages |

With those frames fixed, the causal question can be answered separately from the reported outcome. **Closed** below means the source establishes all four links for at least the named update path: evidence affects the update, the system's organization changes, the change enters a live path, and a later operation depends on it. **Unestablished** means the source does not show one of those links; it does not mean the link was absent.

| System | Concrete evidence-to-change path | Result of questions 1–4 | Update architecture and builder boundary |
|---|---|---|---|
| **Self-Harness** | Failed execution traces become verifier-grounded signatures; several bounded edits to instructions, tools, and runtime controls are proposed; split pass counts decide promotion; accepted edits are merged and exercised in later harness evaluations. | **Closed for promoted harness edits.** Later evaluations execute the changed harness. The study does not establish generalization beyond its repeatedly consulted benchmark splits. | **Proposal selection.** The objective, failure-signature representation, edit surface, two-split gate, and wider harness architecture remain builder-supplied. |
| **Continual Harness** | Recent trajectory failures cause the Refiner to edit prompts, sub-agents, skills, or memory; edits enter the next game step without a separate acceptance decision. A repaired navigation skill can therefore affect the next attempted route. | **Closed for prompt and harness edits that later steps exercise.** Not closed for every created artifact: memory is rarely consulted and most authored skills are never invoked. | **Direct update.** The Refiner rule, schedule, four-part component scheme, observation/action interface, and reward design remain builder-supplied. Adding a reject-capable gate would create proposal selection, not repair a missing universal component. |
| **Autogenesis Reflection optimizer** | Traces and registered resource state feed typed Reflect/Select/Improve/Evaluate/Commit operators. Accepted prompt or agent versions become active and are reused in later refinement rounds. | **Closed for demonstrated prompt and agent-resource revisions.** Solution-only evolution changes an external work product, not the improving system's organization. Environment and Memory are exposed as mutable resources but their later causal use is not independently evaluated. | **Proposal selection.** The resource ontology, learnability mask, evaluator, acceptance rule, orchestration, and task interfaces remain builder-supplied. Other protocol configurations may commit directly. |
| **Accumulated Behavioral Rules** | An accepted review comment is generalized by an engineer into a standing rule; two coding-agent interfaces load the rule file in later sessions; the study reports no recurrence across 74 post-rule exposures. | **Causal uptake unestablished.** Loading proves delivery, and non-recurrence is consistent with use, but without a no-rule comparison the study does not isolate dependence on the new rule. | **Proposal selection.** Engineer judgment can reject promotion, while the always-loaded file, abstraction heuristic, review process, and retirement policy remain outside the reported revision path. |
| **Darwin Gödel Machine** | Archive score and child count select a parent; a fixed external model diagnoses its logs; the parent edits descendant code; compilation and retained editing ability decide archive admission; benchmark score affects later parent sampling. | **Closed for descendant lineages in which an admitted child is later selected and run.** Admission alone is insufficient because many archived children may never execute again. | **Proposal selection.** Descendant code is broad, but the diagnostician, viability rule, parent-selection formula, archive policy, objective, and evaluator remain outside its edit surface. |

The verdicts prevent three easy overstatements. Creating an artifact is not the same as using it, as Continual Harness shows. Mandatory loading is not the same as causal dependence, as Accumulated Behavioral Rules shows. Archive admission is not later execution, as the Darwin Gödel Machine shows. Conversely, an unestablished link should not be rewritten as an absent link.

Update architecture also does not determine where the builder loop sits. Four systems use proposal selection and leave their evaluators outside the reported revision scope. Continual Harness adopts updates directly and instead leaves its evidence-to-edit machinery, component partition, and reward design outside. Against question six, the papers mostly demonstrate adaptation inside supplied organizations, not retained revision of the machinery that supplied them.

The Darwin Gödel Machine also supplies the important exception. One retained descendant added multi-candidate generation and a ranker, introducing a new stage and component role. Yet archive admission established only that the child still ran and retained code-editing ability; it did not establish that the restructuring was beneficial, and the diagnosis came from a fixed external model. The reported evidence therefore shows broad mutability and one weakly evaluated restructuring, not a general path for controlled architectural self-revision.

Fixed placements need not all be mistakes. The Darwin Gödel Machine conceals one evaluator to limit objective hacking and freezes its exploration controller as a compute compromise. Independent checks may warrant protection; the requirement is to make their scope and reason explicit, not to make everything mutable at once.

## What Commonplace brings inside

[Commonplace's declared boundary](../reference/commonplace-declared-frame.md) includes designated maintainers, so this is a human-inclusive comparison rather than an autonomy claim. Commonplace makes part of that builder-mediated path explicit: a diagnosed organizational problem can move through inspectable reasoning and an authorized update into system definitions that later agents and maintainers use, while the roles and checks governing the path remain available as later revision targets. Different episodes can search for and determine changes differently; proposal selection is one path, not Commonplace's defining update mechanism.

ADRs make builder-level redesign addressable by retaining an accepted architectural decision, its context, and its consequences. An ADR is not operative merely because it was saved. The decision becomes machinery when it is carried into contracts, instructions, configuration, validators, or code that later work consumes.

Three episodes show different parts of the path.

**A validator took over a verification duty.** A topic README was expected both to introduce its subject and to list every note carrying its tag. The `learning-theory` README had grown to 55 entries and 18.8 KB, beyond what an editing agent could reliably verify by inspection. The objective was concrete: a head presented as complete must not mislead a reader by omitting members. The accepted change introduced explicit `complete` and `covered_by` marks, schema support, and validator checks. Later validation caught a note whose block-style YAML tags had escaped the documented search recipe; the recipe was then corrected. This [tag-README episode](../reference/tag-readme-trace-observed-causal-connection.md) closes the causal path: evidence about verification strain changed Commonplace's represented checking machinery, and later operation depended on the new check. It changed who performed verification rather than splitting the artifact into different components.

**A missing design stage became reusable machinery.** Unadopted designs had no honest home: putting them among theory notes treated a choice as a truth claim, while putting them in temporary workshops forced finished proposals into a workspace meant to close. [The proposal-lifecycle decision](../reference/adr/028-design-proposals-live-in-reference-proposals.md) introduced a durable stage between investigation and implementation: workshop, then proposal, then implemented ADR or retirement. That path was not merely documented and forgotten. The later proposal for an external article collection moved through it and became [the article-layer decision](../reference/adr/057-articles-use-an-editorial-profile-and-excluded-drafts.md). The second episode therefore depended on machinery introduced by the first. This establishes reuse; it does not establish that the new stage reduced cost or produced a better decision.

**A new artifact role changed routing.** Generated orphan lists, coverage scans, and promotion candidates fit neither durable knowledge notes nor temporary workshops. [The reports-layer decision](../reference/adr/007-reports-directory-for-generated-snapshots.md) introduced a replace-in-place home for such computed snapshots, with regeneration rather than accumulation or workshop completion as its lifecycle. Review jobs, connection scans, fix reports, and promotion-candidate generation now write under `kb/reports/` instead of presenting their outputs as authored knowledge. This is evidence of an installed organizational role. By itself it is not evidence that the role improved knowledge-work outcomes.

The episodes support different conclusions and should not be collapsed. The tag-README trace is the strongest observed reflective self-improvement case because it names an objective, records the evidence-responsive organizational change, and shows later causal use. The proposal-to-article sequence demonstrates that newly installed builder machinery was reused in a later redesign. The reports layer demonstrates a new role becoming operative. Together they show partial internalization of architectural development, not three equivalent outcome experiments.

Version control made these before-and-after states and adoption sequences reconstructible. Commonplace [expects versioned operation](../reference/storage-architecture.md), but assigns no portable architectural meaning to a commit, branch, or merge; history is evidence about a change, not automatically a rationale record or obligatory read path. What makes the episodes relevant is that their accepted decisions were installed in later-consumed machinery.

These cases support partial internalization: repeated revisions of organizing machinery and one later reuse of an installed design process. They establish an explicit and inspectable path through which human–agent architectural revisions repeatedly became operative, with some machinery introduced through that path becoming a premise or target of later work. They do not establish that Commonplace is technologically unique. A research organization whose issue tracker, design records, review rules, CI checks, and deployment process satisfy the same causal test would be another instance.

## The Gödel machine closes the ladder differently

The theoretical [Gödel machine](../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md) attacks the same meta-level problem through formal self-reference. Because its proof searcher and rewrite machinery lie within the rewrite surface, the construction needs no separately fixed controller at every higher level. Once licensed, a rewrite may replace any software component and, under conditions established by the incumbent system, alter axioms or the utility function.

That broad rewrite space has a strict acceptance boundary. The machine switches only after proving, from its current formalization, that doing so is better than continuing the search. It must therefore ignore effective improvements it cannot prove, even given unlimited computation; finite time and space exclude more. The proposal is theoretical, with no reported implementation, so it establishes a possibility and a tradeoff rather than experimental performance.

Commonplace does not close the ladder formally. It brings part of architectural development into a declared human–agent process and can act on fallible empirical and semantic grounds without proving that a change is better. The trade is practical permissiveness for formal assurance: Commonplace supplies neither the Gödel machine's guarantee within its formal model nor assurance that an accepted change is good.

## What the evidence does not yet show

The observed reuse is not evidence of compounding. [Reflective leverage is tested in the next episode](../notes/reflective-leverage-is-tested-in-the-next-episode.md): earlier accepted changes would need to make later improvement cheaper, broader, more reliable, or less dependent on human judgment. The proposal-to-article sequence establishes that the machinery was used, not that it improved the later revision.

A fair outcome test would compare matched architectural-revision episodes with and without an explicit, retained builder path. It would measure whether the path improves target identification, coordination across artifacts, detection and rollback of bad changes, and later reuse, while counting maintenance and human judgment. Until such evidence exists, the comparison supports an architectural affordance and an observed operating path, not superior performance.

## Where to go next

The practical test now has two levels. Did objective-bearing evidence become an operative change, and was that change adequately warranted? When the supplied organization itself becomes the problem, can evidence reach the builder path that defines roles, checks, and update rules, or can the system change only the parts that its builders already exposed?

The [self-improving-systems cluster](../notes/self-improving-systems-README.md) maps the theory behind the six questions, and [the repository](https://github.com/zby/commonplace) contains the framework. If applying the test produces a counterexample or disputed boundary case — a stored memory whose later causal use is unestablished, a system described as proposal selection despite having no rejectable adoption decision, or a published pathway that already makes its builder loop explicit, operative, retained, and revisable — [open an issue](https://github.com/zby/commonplace/issues).
