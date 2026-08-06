# Detailed argument: from self-rewrite to compounding

## Proposition

Exo already has the central architecture needed for reflective self-improvement: a causally connected, inspectable representation of the organization that determines its behavior; processes that can revise that organization; reject-capable mechanical checks; and retention paths that make accepted changes available to later operation.

The open question is not whether Exo can change itself. It is whether a retained benefit from one change helps produce a later improvement. That is the difference between accumulating improvements and compounding them.

This pitch proposes one candidate mechanism. Represent the theories and machinery behind improvement—how Exo notices problems, forms candidates, evaluates them, promotes results, and routes them back into operation—as explicit, selectively revisable artifacts. Then test whether those artifacts make later improvement cheaper, broader, more reliable, or less dependent on human judgment.

The claim is conditional. Reflection adds control and addressability, not guaranteed improvement. Natural-language theory may be the most practical present form for some unformalized commitments, but it earns its place only if it improves later episodes after its full lifecycle costs are counted.

## What Exo already has

At refreshed main revision `ef4cfe057af0`, canonical Exo supplies:

- a source tree and checked-in self map through which the agent can inspect the organization that determines its behavior;
- an append-only event history preserved across sandbox rewind;
- source, configuration, build, test, restart, observation, rollback, and git paths through which the agent can retain symbolic changes;
- a managed tool registry that installs validated local or commit-pinned sources and makes accepted tools active in later rounds;
- natural-language memory facts, skills, prompts, and an agent-maintainable self map;
- a durable self-update record containing a free-text reason and mechanical outcome; and
- a capable model that can inspect current artifacts and prior episodes before acting.

The separately linked ExoWorker branch makes the learning policy more explicit. Its standing instructions say to persist lasting facts with `remember`, reusable playbooks with `install_skill`, and repeated callable helpers with `install_agent_tool`. Its memory tool specifically names lessons from failures as suitable facts.

This is already a broad, agent-mediated, mixed-form revision path. The proposal does not add learning where none exists, and it does not repair a system that learns only in code. It asks whether Exo should make its current promotion and revision theory more explicit, general, revisable, and testable.

## Occurrence, accumulation, and compounding

Three claims must be kept separate.

**Self-improvement occurs** over a declared boundary, horizon, and objective when evidence bearing on that objective shapes an operative change to the system's own behavior-determining organization and later behavior uses that change. An accepted patch that is never installed, or a memory that is loaded but ignored, does not close the path. The term names an improvement-directed mechanism; it does not guarantee that every accepted change helps.

**Improvements accumulate** when useful retained results build a stock that later operation uses. A new tool can prevent recurring task failures. A skill can guide a later task. A prompt change can shape future behavior. Each can be a real gain while the work of finding, evaluating, and installing the next improvement remains unchanged.

**Improvements compound** when an earlier improvement's benefit feeds into producing a later improvement. The earlier result might improve diagnosis, candidate search, evaluation, installation, or retention directly. It can also free time, compute, or judgment that an allocation mechanism deliberately returns to improvement work. The indirect path must be observed; unused savings establish no feedback.

The accepting metric for the first change cannot establish the third claim. A tool test shows that the tool met its immediate target. It does not show that the next revision became more productive. Compounding evidence therefore comes from a later improvement episode, with a causal trace to the earlier benefit.

One link provides local evidence. Repeated links establish a compounding pathway. The feedback may be modest, irregular, bottlenecked, or eventually saturated; it need not be exponential.

## Reflection makes the revision surface controllable

Compounding does not require reflection. Opaque parameter updates can improve later learning without exposing any individual retained commitment. Reflection adds a different affordance: **addressability**.

Exo's source, prompts, skills, memories, tests, tools, and self map can make behavior-shaping commitments readable to processes inside the system. A represented commitment can be named, criticized, applied to another problem, revised selectively, or retired. A represented evaluator or promotion rule can become the target of a later improvement instead of remaining invisible machinery.

This control is aspect-bounded. The current decomposition determines what Exo can notice and formulate:

- what counts as evidence;
- which failures have names;
- which artifacts and relations are understood to shape behavior;
- which change operations are available; and
- which comparisons can admit or reject a candidate.

A loop can optimize every named component while having no way to say that a responsibility is missing, an authority path was omitted, or the components were divided badly. Repository-wide writability marks an outer envelope, not the revision surface that a particular path can actually reach.

The strongest proposal therefore makes the map itself revisable. If an episode reveals a missing authority path or a bad decomposition, Exo can revise the representation used by later audits. The revised map and the path that changed it must remain available to inspection and revision afterward. This keeps a redesign class open to further revision; it does not show that the path will discover every omission or that its changes will help.

A fixed surface is not automatically a defect. Exo's protected Rust substrate provides identity, history, secrets, and recovery outside the executor it may replace. Tests, budgets, and operator controls may also be warranted boundaries. The diagnostic question is whether each fixed placement is deliberate and whether its scope is appropriate, not whether everything is mutable at once.

## Promotion is part of the improvement machinery

An experience does not arrive labelled with its reusable lesson. A failed integration, successful workaround, or adopted code change may support several incompatible promotions:

- retain the episode because its detail is what a later case needs;
- retain a fact about the local environment;
- state a mechanism and applicability boundary in natural language;
- write a reusable procedure;
- create a test, validator, schema, tool, prompt rule, or code change;
- record a decision among live alternatives; or
- retain nothing because reconstruction is cheap or reuse is unlikely.

The selection is ampliative: observed cases do not uniquely determine which generalization, if any, should govern new cases. A stronger model may choose better, but capability does not remove the choice. If the result is not retained, later calls choose again. If every plausible result is retained, the knowledge layer becomes a lossy second event log.

The selection is also knowledge-laden. Which candidate lessons occur at all depends on background theories of the software, providers, model failures, and the improvement process. A policy that prices only storage can select correctly among an impoverished candidate set.

ExoWorker's “lasting fact,” “reusable playbook,” and “same helper more than once” rules are useful local heuristics. A fuller promotion theory would answer at least four questions:

1. **Value:** What future work is expected to reuse this interpretation or commitment?
2. **Form:** Should the result remain an episode, become a semantic claim or procedure, or cross into a symbolic artifact?
3. **Authority:** Is it evidence, advice, an instruction, a routing rule, or an enforced constraint?
4. **Lifecycle:** What observations or system changes should cause review, rescoping, codification, supersession, or retirement?

Promotion policy belongs inside the proposed revision surface. Later evidence should be able to show that its selection heuristic over-promotes fluent summaries, misses transferable mechanisms, gives weak evidence too much authority, or retains conclusions past their useful life. The system can then revise the policy and test whether the revision helps a subsequent improvement.

## Three retained forms

Exo's event records are mixed artifacts: symbolic envelopes around natural-language messages and tool payloads. The relevant distinction is the work each retained form performs, not its file extension.

| Form | Retains | Later use | Characteristic limit |
|---|---|---|---|
| **Episode/example** — event and execution history | What happened, with local detail and tacit residue | Retrieve a similar case and infer what it teaches now | Semantic work recurs; the inferred lesson can vary and remains unnamed |
| **Natural-language semantic artifact** — claim, rationale, theory, rule, decision, procedure | A prior interpretation with enough identity and scope to be used and contested | Retrieve, apply, criticize, revise, supersede, or codify it | It can be vague, inert, wrong, stale, or over-authoritative |
| **Symbolic policy** — code, tests, tools, configuration, schemas | Exact adopted behavior or check | Execute, test, inspect, or modify it | The implementation underdetermines rationale, intended scope, and rejected alternatives |

None subsumes the other two. Episodes preserve evidence and tacit residue that a generalized rule sheds. Symbolic artifacts enforce what has acquired formal semantics. Natural-language artifacts retain semantic work that remains judgment-shaped.

### Semantic caches and commitments

For a conclusion recoverable from current artifacts and episodes, retained natural language is a **semantic cache** or materialized view. Its expected value grows with recurrence, reconstruction cost or variance, transfer, the need for a shared object of criticism, and the cost of failing to activate relevant parametric knowledge. Its cost grows with formation, review, retrieval, context, maintenance, staleness, distraction, and over-application.

Just-in-time reconstruction should therefore win for one-off cases, cheap and reliable deductions, high-drift conclusions unlikely to be reused before expiry, and competence whose value resides in example detail. Promotion should be favored when a mechanism recurs, transfers across surfaces, is expensive or unstable to reconstruct, or several actors need one named object to contest.

Some conclusions are not caches. A generalization beyond observed cases, a decision among live alternatives, or an adopted applicability boundary adds a resolution that its evidence never determined. Code may embody the selected behavior without recording which rationale was adopted. These are **commitments**. A stale cache can be discarded and rebuilt; a lost commitment is gone.

The limit-of-12 case is minimal. A concurrency cap may be a permanent safety ceiling or temporary tuning for one provider quota. Identical code and identical history support both readings, but a later provider change requires opposite responses. If the decision was not retained, a future model can invent a rationale but cannot recover the adopted one.

## The evaluation boundary cannot be self-authored

Each improvement episode is relative to an objective and a comparison rule identified independently of the candidate change. A candidate cannot establish that it is better by rewriting its own objective, relaxing its evaluator, excluding adverse evidence, or changing cost accounting. A proposal to change any of those is a separate revision requiring separate authority.

This boundary can be time-indexed rather than permanently frozen. An objective, evaluator, scope, or stopping rule may remain addressable and revisable **between** episodes while staying fixed **within** the episode that judges a candidate. Otherwise the active candidate can move the standard that is supposed to judge it.

Exo's present gates expose the oracle boundary. Build success, tests, restart outcome, and logs can reject a mechanically broken change. They can admit a change that degrades judgment while remaining mechanically sound. The managed registry strengthens shape and installation checks without establishing usefulness. Exo's proposed cloned-sandbox canary would create a behavioral comparison path, but any rubric used there would still warrant only the behavior it can assess.

A maintained natural-language theory helps Exo state what its current evaluator misses and propose stronger checks. It does not manufacture a universal improvement criterion. The same model may propose and criticize a change, but the incumbent evaluation contract—not the candidate's preferred contract—must control adoption.

## Concrete Exo-shaped cases

### Managed tool adoption: accumulation or compounding

Exo can install a validated tool from a local directory or exact Git commit. The registry preserves its stable id, source, initialization, and installed code. The event history preserves the failures and requests around installation.

If the tool prevents later task failures, Exo has accumulated a useful retained capability. If the tool or its accompanying lesson also reduces the search, evaluation, or installation cost of a later improvement, that later episode provides local evidence of compounding. The tool's original validation result cannot decide between those readings.

The same episode also poses a promotion question. Is the tool a one-provider workaround, an instance of a general integration mechanism, a temporary bridge, or a capability expected to become standard? The answer may belong in a memory fact, skill, semantic claim, regression test, the tool itself, several linked forms, or nowhere.

### Rebuild reason: a partial semantic annotation

`rebuild_and_restart_exo` asks for a short reason and stores it with the update id, status, timestamps, identities, and exit code. Exo is already retaining meaning that changed code and mechanical outcome do not carry by themselves.

The annotation remains event-local. It has no independent applicability boundary, evidence links, review state, invalidation path, or recorded effect on a later improvement. It is a useful seed for a semantic layer, not evidence that the layer compounds.

### Canary evaluation: revising an oracle

Mechanical operability does not establish semantic improvement. A retained cross-cutting theory can make this limitation addressable and motivate a cloned-sandbox canary with a behavioral comparison.

If the canary later rejects a judgment-degrading rewrite that the old checks would have admitted, then an earlier improvement to evaluation helped produce a better later selection. That is the right evidence shape. Installing the canary, or showing it works on its construction case, is not enough.

### Concurrent memory repair: a commitment behind code

Suppose Exo replaces whole-artifact memory updates with compare-and-swap after observing a lost update. The code records CAS. It does not uniquely state whether the intended guarantee is linearizability, prevention of silent loss, or merely fewer collisions, nor why CAS won over an append-entry design. Those distinctions control a later storage rewrite and cannot be derived from the implementation alone.

## Why natural language is the frontier form

The proposal does not privilege natural language forever. It routes selected content by what currently interprets it reliably:

- **Episodes** preserve experience and tacit residue.
- **Natural-language artifacts** retain mechanisms, reasons, applicability conditions, commitments, and unresolved theories that an LLM can interpret but no formal language yet receives.
- **Symbolic artifacts** codify stable parts with mechanical semantics and tighter oracles.
- **Distributed-parametric state** may absorb stable competence, but Exo does not currently update its base model and current weight-level retention lacks comparable per-commitment identity and revision.

The practical operator is movement among forms. Codify when a rule becomes mechanically statable; relax when the codification overreaches. Preserve the source episodes because [retaining the episode keeps a distilled rule re-derivable](../../notes/retaining-the-episode-keeps-a-distilled-rule-re-derivable.md).

## Minimal proposal for Exo

Commonplace should not enter Exo's protected substrate. At most it is one candidate implementation of a replaceable, agent-editable theory and maintenance policy above it. Commonplace is a hybrid of theory and implementation; this proposal transfers the hypothesis, not its current Markdown, YAML, collection, review, or storage choices.

The minimum capability is:

1. Maintain an explicit, revisable theory for which experiences deserve promotion, into which form, and with what authority.
2. Maintain an aspect-bounded map of the artifacts and relations through which Exo's behavior and improvement process are shaped.
3. Apply the theory selectively while preserving raw episodes and symbolic artifacts as drill-down evidence.
4. Give each retained semantic conclusion enough identity to link it to source episodes, affected artifacts, triggers, mechanism, scope, status, and authority where those distinctions matter.
5. Route retained conclusions into later situations and record whether they were used, ignored, contradicted, revised, codified, superseded, or retired.
6. Hold the objective and comparison contract fixed within an improvement episode; route proposals to revise them through a separately authorized episode.
7. Record causal links between improvement episodes and measure whether retained benefits make later revision cheaper, broader, more reliable, or less human-dependent.
8. Use observed later benefits and failures to revise the promotion theory and revision map themselves.

Exo's existing memory, skills, event records, update records, tool manifests, git repository, or another database and schema could implement this capability.

## What independent verification must decide

The baseline is refreshed Exo with the same episodes, model, free-form memory, skills, managed tools, prompts, tests, and freedom to modify symbolic artifacts.

For one proposed compounding link:

1. Identify an earlier retained gain and the later improvement it is expected to help.
2. Measure the later episode through revision cost, reliability, breadth, human decisions, or another displaced productivity measure.
3. Trace direct use of the earlier benefit, or trace a saving through allocation into later improvement work.
4. Compare against a frozen-artifact, simpler-memory, or absent-theory baseline.
5. Count formation, review, retrieval, context, maintenance, staleness, and repair costs.
6. Repeat across further episodes before claiming a compounding pathway.

The hypothesis predicts an interaction, not a universal win. Explicit theory should help when interpretations recur, cross implementations, require named criticism, change the decomposition of future work, improve an evaluator, or preserve commitments. It should lose or tie on one-off work, complete formal regimes, residue-heavy cases, and rapidly expiring conclusions.

The proposal is weakened or falsified if Exo's existing heuristics and just-in-time reconstruction match or beat the explicit layer on later improvement productivity after full cost accounting. The operational falsifiers and revision triggers are in [evidence.md](./evidence.md#falsifiers-and-revision-triggers).

## Claim boundary

- The proposal strengthens an existing mixed-form revision path; it does not add a missing representational form.
- Reflection makes commitments and machinery addressable. It is neither necessary nor sufficient for compounding.
- Raw episodes remain available. This is not summarize-and-discard.
- Not every trace is promoted, and not every promoted conclusion receives instruction or execution authority.
- Natural language is not the final form for every lesson, and the retained form does not determine who may evaluate it.
- A path can remain open to revision without improving, and it can accumulate improvements without compounding.
- A promotion theory or semantic cache that is vague, inert, stale, or more expensive than reconstruction has failed to earn its place.

## Evaluation boundary

Pinned revisions, per-claim evidence status, and the relation to the earlier pinned reviews live in [evidence.md](./evidence.md#pinned-exo-and-exoworker-facts). Treating ExoWorker's standing instruction as a primitive promotion policy is our interpretation of the checked-in prompt, not a claim that its agent reliably follows it. The claim that a stronger semantic layer may improve later revision is our inference, not a position attributed to the Exo authors.

Out of scope is a universal improvement criterion. Explicit theory can make candidates, evidence, form, scope, authority, revision machinery, and lifecycle legible. It cannot let a candidate become its own judge or solve open-ended evaluation by declaration.
