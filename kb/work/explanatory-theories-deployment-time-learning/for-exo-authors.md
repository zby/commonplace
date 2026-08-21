# Exo can rewrite itself. Can one improvement help produce the next?

> **Exo-facing track:** This is the Exo invitation within the [explanatory-theories deployment-time-learning workshop](./README.md). It applies the workshop's distinction between an episode's working theory and a retained theory to Exo's unusually broad self-revision surface. It is a proposal for criticism, not a claim about what Exo already implements.

Exo has built an unusually strong substrate for reflective self-improvement. Its source tree is an inspectable representation of the system that determines its behavior. The agent can edit the mutable executor and policy, rebuild, restart, and preserve the record of failed attempts outside the state it rewinds. It can also retain facts, skills, tools, prompts, tests, and code.

Those capabilities make self-change possible, reversible, and reusable. They do not yet show that Exo's improvements **compound**.

An improvement compounds when its benefit helps produce a later improvement. A better evaluator might reject a bad rewrite. A better retrieval rule might surface the evidence needed for a later diagnosis. A better promotion policy might prevent the next useful lesson from becoming an inert memory. One such dependency is local evidence; repeated dependencies establish a compounding pathway.

## A concrete case

Suppose Exo hits the same integration failure twice and installs a managed tool that prevents it. The tool preserves exact behavior. The registry records its source at an exact commit. The event log preserves the failures and the installation.

That may be a real retained gain. But if the next improvement remains just as hard to notice, diagnose, judge, and install, Exo has accumulated another useful capability without improving how it improves.

Now suppose Exo also retains the causal lesson behind the repair, its scope, and the evidence that would overturn it. A later provider failure triggers that lesson. Exo uses it to reject a superficial retry patch, identifies a shared failure mechanism, and installs a broader fix with less search or stronger evaluation. The later improvement depends on the earlier one. That is local evidence of compounding.

The distinction cannot be read from the first tool's test result. It appears only in the later improvement episode and needs a causal trace between the two.

## The opportunity: make the improvement process a revision surface

The separately linked ExoWorker branch already supplies a primitive promotion policy: keep lasting facts as memory, reusable playbooks as skills, and repeated helpers as tools. The open question is whether a more explicit and revisable policy would earn its cost.

The proposal is not another memory store. It is to represent the machinery that turns experience into change:

- what the system treats as evidence and which problems it can notice;
- how it searches for candidate changes;
- which objective and comparison rule evaluate them;
- what becomes an episode, lesson, skill, test, tool, prompt, or code change;
- how much behavioral authority each retained result receives; and
- what later evidence should revise, rescope, codify, supersede, or retire it.

Reflection's advantage here is control, not guaranteed improvement. Explicit commitments can be named, criticized, and selectively revised. The policy that chooses lessons can itself become a lesson and later a revision target. But an addressable artifact that no later improvement retrieves and uses does not compound.

## Working theories, retained theories, and the policy between them

The workshop separates three objects that this pitch previously called “theory” too loosely:

- `tau_n` is the working theory active in improvement episode `n`: an explicit explanation of a failure or system behavior, with scope, assumptions, and predictions. Exo could construct it fresh from the current source, traces, and task evidence.
- `T_n` is the retained, addressable body of system theories available before episode `n`. A relevant part of `T_n` can be retrieved and applied to produce `tau_n`, then be revised separately after the episode.
- the **promotion and revision theory** is meta-level: it governs which episode-local conclusions should enter `T_n`, in which form and with what authority, and what later evidence should revise or retire them. It is not identical to the object-level theories of providers, tools, prompts, evaluators, or routing that it governs.

Fresh construction of `tau_n` can improve one episode's diagnosis, candidate search, or evaluation without creating cumulative theory-mediated learning. The stronger Exo claim begins only when a retained `T_n` changes a later improvement episode and the meta-level policy remains separately criticizable and revisable.

## Three tests for an Exo improvement path

| Test | Questions |
|---|---|
| **Occurrence** | What Exo boundary, time horizon, and objective are in scope? Did relevant evidence change Exo's behavior-determining organization? Did later behavior use the change? |
| **Revision surface** | Which prompts, tools, memories, tests, evaluators, policies, and relations could the path revise? Which did it revise, which stayed fixed, and could the same path revise its successor? |
| **Compounding** | Did a later improvement measurably depend on the retained benefit? How were the episodes connected, and did the feedback recur? |

This separates three claims that are easy to blur. Exo can support self-improvement without every accepted change being beneficial. It can accumulate useful changes without making later improvement more productive. And it can expose a broad revision surface without discovering every omission in its own decomposition.

## The evaluation boundary must remain outside the candidate

Each improvement episode needs an objective and comparison rule fixed independently of the candidate being judged. A candidate cannot prove itself better by rewriting its own test or redefining success. Changing the objective, evaluator, scope, or stopping rule is a separate revision that needs separate authority.

This is where Exo's current mechanical gates stop. Build success, tests, restart success, and logs can reject a broken change. They can still admit a change that makes the agent's judgment worse. A maintained natural-language theory can expose that gap and propose a behavioral canary; it cannot manufacture a trustworthy oracle for open-ended self-change.

## What we'd add

The minimum capability is smaller than adopting Commonplace:

1. Maintain an explicit, agent-editable theory of promotion and a map of the artifacts and relations that shape Exo's behavior.
2. Let an episode construct a scoped working theory `tau_n`, while preserving raw episodes and promoting only selected conclusions into a retained `T_n`, procedures, checks, or code.
3. Give retained conclusions enough identity to record their evidence, trigger, mechanism, scope, status, authority, and affected artifacts where those distinctions matter.
4. Route them into later work and record whether they were retrieved, used, contradicted, revised, or ignored.
5. Keep the evaluation contract fixed within an episode and revise it, when needed, through a separately judged episode.
6. Measure whether retained benefits make later improvement cheaper, broader, more reliable, or less dependent on human judgment.
7. Use those later outcomes to revise the promotion and revision theory itself.

The representational rule remains simple:

> **episodes for evidence · natural language for reusable meaning · code for exact behavior**

Retain a natural-language conclusion when it is likely to recur and re-deriving it costs more than keeping it current, or when it records a decision the evidence cannot recover. Codify the part that can be stated and checked mechanically. Keep the episode because the conclusion may be wrong.

## The proposal can lose

The relevant baseline is Exo as it already exists: the same model, episodes, free-form memory, skills, tools, prompts, tests, and freedom to modify symbolic artifacts.

The proposal loses if that baseline makes later improvements as cheaply, reliably, and broadly as the explicit layer after counting retrieval, context, review, staleness, maintenance, and human judgment. It also loses if retained theories are not activated, cannot be kept current, or merely give fluent rationales more authority.

The decisive experiment therefore compares later improvement episodes with the relevant theory frozen, absent, or replaced by simpler memory. It measures the later revision—not the metric that accepted the earlier change—and traces direct use or actual reinvestment of saved resources.

## Think first, then verify it your way

You have the pitch; form your own view before opening the supporting documents. Then use your own agents, tools, and preferred methods to verify or attack it:

- [Detailed Exo case](./exo-case.md) — Exo's present revision path, accumulation versus compounding, promotion economics, evaluation boundary, concrete cases, and minimal proposal
- [Exo evidence and counterevidence](./exo-evidence.md) — pinned Exo and ExoWorker facts, later-episode evidence, supporting theory, adverse results, open gaps, and falsifiers

This pitch comes out of [Commonplace](https://github.com/zby/commonplace), a framework for agent-operated knowledge bases. Commonplace is itself testing whether retained natural-language theory can make heterogeneous revision more controllable and eventually compounding. It has installed and reused revisions, but it has not shown compounding through its theory layer. Exo is a sharper computational case of the same question. The proposal transfers the hypothesis, not Commonplace's Markdown, schemas, review system, or protected-boundary choices.

---

*Track status and independent exit: this Exo invitation is ready for author contact once its pinned Exo facts and claim boundaries have been rechecked and an outreach message links this page. Contact need not wait for the workshop's general experiments. The track closes when scoped criticism has been handled, durable conclusions have been extracted or explicitly declined, and contact has been made or deliberately declined. An author reply would be welcome but is not required.*
