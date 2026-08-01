# Case packet

Neutral case identifier: case-f88ac900b7b30e

The possible directed relationship from Artifact A to Artifact B is under review.

## Artifact A

# An author should fix what the executor can't determine, not what it will

An instruction is written before it runs, and the executor acts later, on the live system. The same gap opens wherever an artifact is authored before execution: a plan, a spec, a workshop frame, the task prompt an orchestrator hands a subagent — in each, an author commits at one time and an executor acts at another. Any detail the artifact fixes is a snapshot taken at authoring time, and it diverges from what the executor actually faces for three reasons: at writing time the author saw only part of the situation; the situation keeps changing — which we *want* it to; and execution itself produces evidence, so the early steps generate exactly the information the later steps should use. The third reason is why plans are systematically worse candidates for detail-fixing than instructions: a plan's executor is guaranteed to know more than its author, even when nothing external changed. So a fixed detail goes stale — by ignorance, by drift, or by the run itself. When it does, the executor is stuck: follow the stale detail and get it wrong, or override the artifact it was handed. Either way the detail meant to help has discarded what the executor can now determine. That is why over-specified instructions — and over-committed plans — are brittle. (It also buries the details that matter among the ones that don't.)

The usual heuristic — *say what you want, not how to do it* — gestures at this, because the *how* is so often the part that depends on the situation. But the real line isn't how-versus-what: a *what* can be a snapshot too (which functions currently call it, what the config already contains), and some *how* is genuinely the author's to fix. The real test is what the executor can determine for itself — by looking, searching, or reasoning from the live situation. Leave that to the executor — its output then tracks the system as it evolves, not a past version of it. Fix only what it can't determine: the goal, the constraints, what *done* means, and any privileged fact the author holds but the executor can't reach. And fixing is not only mandating. An artifact fixes by framing too: a plan's decomposition, a workshop's opening question, a spec's choice of abstraction commit the executor to a method as firmly as a directive would — the commitment is just harder to see, because nothing in it reads as an order.

Arbitrary choices fall on the same side: they too are something the executor can't determine, because the situation itself doesn't determine them — the answer isn't in it at all. They include the obvious conventions — output paths, file names, templates — but also *which of several valid interpretations to follow* when the situation picks out none. One of the many has to be chosen, and only the author can choose it once and the same way. This is the mirror of the situational case: a situational detail goes stale because the situation determines it and then keeps moving, while an arbitrary choice can't, because the situation never determined it — which is just why pinning the first is brittle and pinning the second safe. Safe, though, only while the choice is genuinely decoupled: *arbitrary* means the options are equivalent downstream too, not just at the moment of choosing. A choice whose options differ in what they later allow or block — a method masquerading as a convention to settle — is situational in disguise; the situation will determine it eventually, and it belongs to the executor.

Staleness is also not the only cost. A pinned choice consumes search space: every commitment narrows what stays feasible for the decisions downstream of it, and since [low-degree-of-freedom subproblems should be solved first to avoid blocking better designs], the flexible choices belong late in the sequence. The author occupies the earliest commitment slot and cannot defer to itself — deferral here *means* delegation to the executor. So the ordering rule independently derives the same line: what the test above tells the author to fix — goal, constraints, done-criteria, the genuinely arbitrary conventions — are the low-flexibility commitments, cheap to fix early because they consume little of the executor's feasible space; a pinned method or architecture is a high-flexibility commitment made in the earliest slot, able to block the strong positions before anyone has seen them.

This is not a rival to [frontloading]; it is a cost frontloading's decision has to weigh. Frontloading asks whether inserting a value saves context — but inserting one the executor would be better placed to choose forfeits its runtime advantage, so a value can be worth inserting for context and still be wrong to fix. Both pulls live in the same decision.

Two premises hold the claim up, and dropping either flips it. If the executor isn't [competent enough to decide for itself], fixing the detail is help, not harm. And if the author can fully see the situation when writing *and* it won't change afterward — a static, fully-determined task — there is no snapshot to go stale; that is the one case where a fully specified plan is legitimate. Over-specification bites in the common middle: a capable executor acting on a system the author could only half-foresee and that keeps moving.

---

Relevant Notes:

## Artifact B

# Solve low-degree-of-freedom subproblems first to avoid blocking better designs

When a design problem has interdependent subproblems, the highest-leverage ordering is to commit the least flexible decision first. Christopher Alexander's kitchen example illustrates the mechanism: window placement has very few viable positions, table placement depends on the window's light, and stove placement is comparatively flexible. If you place the stove first, you can accidentally consume the only strong position for the window or table.

This is not domain-specific advice about kitchens; it is a general sequencing rule for constrained search:

1. Identify subproblems by the size of their feasible set ("degrees of freedom").
2. Commit low-degree-of-freedom choices first.
3. Recompute feasible sets for remaining choices.
4. Defer high-flexibility choices until constrained decisions are fixed.

The reason this works is optionality preservation. Early decisions with many alternatives should not be allowed to block decisions with very few alternatives.

In agent workflows, low-degree-of-freedom choices usually correspond to hard constraints: required output schema, tool contracts, file locations, deterministic validation requirements, or precedence rules. High-degree choices are often rhetorical or representational: phrasing, narrative order, or which equivalent summary format to use. This matches [decomposition rules for bounded-context scheduling]: selection and constraint-setting happen first; expensive synthesis calls happen after the constrained frame is established.

The rule also applies when commitments are split across an authoring/execution divide — an orchestrator and its subagents, a plan and the agent that runs it — where the sequence is fixed by role and deferring a choice means delegating it; that application is developed in [fix what the executor can't determine, not what it will].

## Open Questions

- Can degree-of-freedom estimates be made explicit enough for deterministic scheduler heuristics?
- Which "apparently flexible" choices become low-degree once downstream validation is considered?

---

Relevant Notes:

## Under-review context phrase

the ordering rule behind the second cost; the author's slot is earliest, so its commitments must be the least flexible ones
