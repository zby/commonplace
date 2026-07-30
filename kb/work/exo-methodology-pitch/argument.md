# Detailed argument: Exo's theory of promotion

## Proposition

Before a self-improving agent needs a semantic cache, it needs a theory of what is worth caching. That theory must decide whether an experience should shape future behavior, which part is reusable, which representational form should retain it, how much authority it should receive, and what would invalidate it.

Exo already retains raw episodes, natural-language memory and skills, and symbolic policy. A more explicit natural-language layer adds value only for selected conclusions: those that will be reused, transferred, or contested often enough to repay their upkeep, and those that record commitments the evidence cannot give back. The full value and cost terms are spelled out in the economic theory below.

This is a conditional value claim, not a theorem that every trace should become a natural-language artifact or that every self-improving system requires the same retention policy.

## What Exo already has

At refreshed main revision `ef4cfe057af0`, canonical Exo supplies:

- an append-only event history preserved across sandbox rewind;
- source, configuration, build, test, restart, observation, rollback, and git paths through which the agent can retain symbolic changes;
- a managed tool registry that installs validated local or commit-pinned sources and makes accepted tools active in later rounds;
- natural-language memory facts, skills, prompts, and an agent-maintainable self map;
- a durable self-update record containing a free-text reason and mechanical outcome; and
- a capable model that can inspect current artifacts and prior episodes before acting.

The separately linked ExoWorker branch makes the learning policy more explicit. Its standing instructions say to persist lasting facts with `remember`, reusable playbooks with `install_skill`, and repeated callable helpers with `install_agent_tool`. Its memory tool specifically names lessons from failures as suitable facts.

That is already an agent-mediated, mixed-form promotion path. It rules out two caricatures: that Exo learns only in symbolic form, and that it rejects retained natural-language lessons.

The current policy is nevertheless fragmentary. “Lasting fact,” “reusable playbook,” and “same helper more than once” are useful local heuristics, but they do not form a general theory of when an interpretation deserves retention, how to choose between an episode and a generalized claim, how much authority a conclusion has earned, or when a system change should invalidate it. Canonical main also still has no automatic trace miner that extracts and evaluates lessons from the log. ExoWorker delegates the decision opportunistically to the acting model under a standing prompt.

The proposal is therefore not to add learning where none exists. It is to make promotion policy and the semantic relationship among experience, conclusion, and behavioral change explicit, agent-editable, and open to improvement.

## Promotion precedes storage

An experience does not arrive labelled with its reusable lesson. A failed integration, successful workaround, or adopted code change may support several incompatible promotions:

- retain the episode because its detail is what a later case needs;
- retain a fact about the local environment;
- state a mechanism and applicability boundary in natural-language;
- write a reusable procedure;
- create a test, validator, schema, tool, prompt rule, or code change;
- record a decision among live alternatives; or
- retain nothing because reconstruction is cheap or reuse is unlikely.

The selection is ampliative: observed cases do not uniquely determine which generalization, if any, should govern new cases. A stronger model may make the choice better, but capability does not remove the choice. If the result is not retained, later calls must choose again; if every plausible result is retained, the cache becomes a lossy second event log.

The selection is also knowledge-laden rather than domain-neutral. Which candidate promotions occur at all depends on background theories — of the software, the providers, the model's own failure modes — so the quality of selection is bounded by the breadth of conjecture generation that precedes it. A promotion theory that only prices retention will under-invest in generating candidates and then correctly select among impoverished ones.

A promotion theory supplies the missing policy. It can begin as a natural-language heuristic and itself evolve with evidence. It should answer at least four questions:

1. **Value:** What future work is expected to reuse this interpretation or commitment?
2. **Form:** Should the reusable result remain an example, become a semantic claim or procedure, or cross into a symbolic artifact?
3. **Authority:** Is it evidence, advice, an instruction, a routing rule, or an enforced constraint?
4. **Lifecycle:** What observations or system changes should cause review, rescoping, codification, supersession, or retirement?

## Three retained forms

Exo's event records are mixed artifacts: symbolic envelopes around natural-language messages and tool payloads. The relevant distinction is therefore the work each retained form performs, not its file extension.

| Form | Retains | Later use | Characteristic limit |
|---|---|---|---|
| **Episode/example** — event and execution history | What happened, with local detail and tacit residue | Retrieve a similar case and infer what it teaches now | Semantic work recurs; the inferred lesson can vary and remains unnamed |
| **Natural-language semantic artifact** — claim, rationale, theory, rule, decision, procedure | A prior interpretation with enough identity and scope to be used and contested | Retrieve, apply, criticize, revise, supersede, or codify it | It can be vague, inert, wrong, stale, or over-authoritative |
| **Symbolic policy** — code, tests, tools, configuration, schemas | Exact adopted behavior or check | Execute, test, inspect, or modify it | The implementation underdetermines rationale, intended scope, and rejected alternatives |

None subsumes the other two. Episodes keep evidence and tacit residue that a generalized rule sheds. Symbolic artifacts enforce what has acquired formal semantics. Natural-language artifacts retain semantic work that remains judgment-shaped.

## An initial economic theory

For a conclusion recoverable from current artifacts and episodes, a retained natural-language conclusion is a **semantic cache** or materialized view. Its expected value grows with:

- how often later work needs the same interpretation;
- the amount of evidence selection and reasoning it avoids;
- variance or error in repeated reconstruction;
- transfer across implementations, components, tasks, or models;
- the benefit of giving several agents one named object to contest or revise; and
- the cost of acting without a stable record of the adopted interpretation.

Its expected cost grows with:

- the work and error involved in forming and reviewing it;
- retrieval and context overhead;
- loss of useful residue during generalization;
- maintenance and invalidation work;
- distraction from irrelevant but retrieved claims; and
- damage from a stale or overgeneralized lesson carrying authority.

Reconstruction variance has a mechanism worth naming: activation failure. Parametric knowledge is applied only when the situation summons it, and summoning is itself knowledge-dependent — a regress that must terminate in something matched against raw context. A retained conclusion's trigger terminates it externally: a routing layer matches surface features of the situation and forces the relevant content into context. The advantage is comparative, not absolute — trigger matching can also fail — but a trigger that fails leaves a named artifact that did not fire, which is inspectable and fixable, while a failed internal recall leaves nothing to point at. It follows that a lesson can be valuable while adding little the model does not know: its content may be nearly redundant with the weights while its trigger is not.

This predicts that just-in-time interpretation should win for one-off cases, cheap and reliable deductions, domains with complete formal oracles, high-drift conclusions unlikely to be reused before expiry, and competence whose value resides in example detail rather than an articulable rule.

It predicts promotion when a mechanism recurs, the same interpretation transfers across surfaces, reconstruction is costly or unstable, several actors need a common object of criticism, or the system must preserve a decision the evidence cannot recover.

## When “cache” is too weak

Some conclusions are not recoverable from symbolic artifacts and episodes because those sources never determined them.

A generalization beyond observed cases, a decision among live alternatives, or an adopted applicability boundary adds a resolution to the evidence. Under [commitment, not derivation](../../notes/commitment-not-derivation-creates-new-ground-truth.md), retaining that resolution creates new ground truth. Code can embody the selected behavior without uniquely recording why it was selected; the same implementation may satisfy several incompatible intentions.

The [pitch's](./README.md) limit-of-12 case is the minimal example: identical implementation, identical history, opposite correct responses to a provider change, and no way for a later model to recover which rationale was adopted.

The natural-language artifact is therefore sometimes a disposable semantic cache and sometimes the authoritative record of a semantic commitment. A promotion theory must distinguish them because they require different rules: a stale cache can be discarded and rebuilt from its sources; a lost commitment is gone.

## Concrete Exo-shaped cases

### Managed tool adoption: choosing what the tool means

The refreshed Exo can install a validated tool from a local directory or exact Git commit. The registry preserves its stable id, source, initialization, and installed code. The event history can preserve the failures and requests surrounding installation.

Those artifacts do not uniquely say whether the tool is a one-provider workaround, an instance of a general integration rule, a temporary bridge, or a capability expected to become standard. A promotion theory must first decide whether any of those interpretations is worth retaining and then choose between the source episode, a memory fact, a skill, a semantic claim, a regression test, and the tool itself.

### Rebuild reason: a partial semantic annotation

The refreshed `rebuild_and_restart_exo` path asks for a short reason and stores it with the update id, status, timestamps, identities, and exit code. Exo is already retaining meaning that the changed code and mechanical outcome do not carry by themselves.

That annotation is valuable but remains event-local. It has no independent applicability boundary, evidence links, review state, or invalidation path. It demonstrates the need for semantic annotation without yet supplying a maintained semantic conclusion.

### Canary evaluation: an oracle boundary

Build success, tests, and restart observation can accept a change that degrades judgment without breaking mechanics. Prior traces may let a model rediscover this each time it evaluates a prompt, skill, tool policy, or executor change. A retained conclusion can state the cross-cutting conjecture: mechanical operability does not establish semantic improvement, so judgment-bearing changes may require behavioral comparison.

No single current test receives that open-ended claim. It belongs in natural-language until a concrete canary and rubric codify a narrower part. Exo still identifies that canary as future work.

### Concurrent memory repair: a commitment behind code

Suppose Exo replaces whole-artifact memory updates with compare-and-swap after observing a lost update. The code records CAS. It does not uniquely state whether the intended guarantee is linearizability, prevention of silent loss, or merely fewer collisions, nor why CAS won over an append-entry design. Those distinctions control a later storage rewrite and are not derivable from the implementation alone.

## Why natural language is the frontier form

The proposal does not privilege natural language forever. It routes selected content by what currently interprets it reliably:

- **Episodes** preserve experience and tacit residue.
- **Natural-language artifacts** retain mechanisms, reasons, applicability conditions, commitments, and unresolved theories that an LLM can interpret but no formal language yet receives.
- **Symbolic artifacts** codify stable parts with mechanical semantics and tighter oracles.
- **Distributed-parametric state** may absorb stable competence, but Exo does not currently update its base model and present weight-level retention lacks comparable per-commitment identity and revision.

The practical operator is movement among forms. Codify when a rule becomes mechanically statable; relax when the codification overreaches. Keep source episodes available either way, because [retaining the episode keeps a distilled rule re-derivable](../../notes/retaining-the-episode-keeps-a-distilled-rule-re-derivable.md).

## Minimal proposal for Exo

Commonplace should not enter Exo's protected substrate. At most it is one candidate implementation of a replaceable, agent-editable promotion and semantic-maintenance policy above it. Commonplace is itself a hybrid of theory and implementation — claims meant to hold beyond the cases where they were developed — and this proposal transfers the claims, not the choices.

The minimum capability is smaller than adopting Commonplace wholesale:

1. Maintain an explicit, revisable theory for which experiences deserve promotion, into which form, and with what authority.
2. Apply it selectively rather than summarizing every trace.
3. Give each retained semantic conclusion enough identity to link it to source episodes and affected symbolic artifacts.
4. Record its trigger, mechanism, scope, epistemic status, authority, and current or superseded state where those distinctions matter.
5. Route it into relevant later situations and revise, rescope, codify, supersede, or retire it as evidence and the system change.
6. Use observed benefits and failures to revise the promotion theory itself.

YAML frontmatter, Markdown collections, type contracts, review pairs, and a freshness store are Commonplace's current witnesses, not requirements. Exo's existing memory, skills, event records, tool manifests, or another database and schema could implement the capability.

## What independent verification must decide

The relevant baseline is no longer symbolic policy plus episodes alone. It is refreshed Exo with the same episodes, model, free-form memory, skills, managed tools, prompts, and freedom to modify symbolic artifacts.

The open question is whether making promotion policy explicit and giving selected conclusions a governed lifecycle adds enough value to repay its full costs. Readers should test that with their own agents and methods rather than inheriting a protocol from this workshop.

The hypothesis predicts an interaction, not a universal win. Explicit promotion and semantic maintenance should help when interpretations recur, cross implementations, require named criticism, or preserve commitments. It should lose or tie on one-off work, complete formal regimes, residue-heavy cases, and rapidly expiring conclusions.

In short: the pitch is weakened or falsified if Exo's existing heuristics and just-in-time reconstruction match or beat the explicit layer after full cost accounting. The operational list of falsifiers and revision triggers is at the end of [evidence.md](./evidence.md#falsifiers-and-revision-triggers).

## Claim boundary

- The proposal strengthens selection and maintenance rather than adding a missing form: Exo already learns in both natural-language and symbolic forms, and ExoWorker already contains a primitive promotion theory. The question is whether a more explicit, general, and revisable one earns its cost.
- Raw episodes remain available. This is not summarize-and-discard.
- Not every trace is promoted, and not every promoted conclusion receives instruction authority.
- Natural language is not the final form for every lesson, and who evaluates a conclusion is separate from the retained form.
- A promotion theory or semantic cache that is vague, inert, stale, or more expensive than reconstruction has failed to earn its place.

## Evaluation boundary

Pinned revisions, per-claim evidence status, and the relation to the earlier pinned reviews live in [evidence.md](./evidence.md#pinned-exo-and-exoworker-facts). Two interpretive caveats belong here: treating ExoWorker's standing instruction as a primitive promotion policy is our reading of the checked-in prompt, not a claim that its agent reliably follows it; and the claim that a stronger semantic layer may pay is our inference, not a position attributed to the Exo authors.

Out of scope is a universal improvement criterion: promotion policy can make candidates, form, evidence, scope, authority, and lifecycle legible; it cannot manufacture an oracle for open-ended self-change.
