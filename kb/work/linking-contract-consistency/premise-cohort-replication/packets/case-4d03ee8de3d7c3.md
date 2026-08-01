# Case packet

Neutral case identifier: case-4d03ee8de3d7c3

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

# Design for the first-time human, except on access cost

A useful default when designing any system an LLM agent consumes is to treat the agent as a competent human using the system for the first time. Most of what makes a system good for a newcomer — clear naming, discoverable organization, orientation cues, honest labels, readable prose — serves the agent equally well, and human ergonomics are easier to reason about than agent behaviour. So the newcomer human is a cheap, reliable proxy for the agent: a default, not a law, holding where the two consumers share a profile and breaking where their profiles diverge.

The sharpest divergence, and the one with a clean fix, is **access cost**. A competent human reads a large artifact *sublinearly* — skim the headings, scroll to the region, Ctrl-F to the few lines that matter — so a large but well-organized artifact stays cheap. An agent reading that same artifact pays *linearly*: every byte enters [bounded context] whether it is relevant or not, and the irrelevant bulk adds interference, not just volume. So an artifact that is cheap for a newcomer human can be context debt for the agent, and you cannot read the agent's cost off human ergonomics.

The real divider is access *mode*, not human versus agent: sublinear, paying only for the slice you consult, versus linear, paying for every byte. Humans default to sublinear because their tooling makes it the path of least resistance; agents default to linear because the cheapest primitive is "read the whole thing into context." But that pairing is not fixed — an agent given a query or search interface reads sublinearly, and a human handed an unstructured blob reads linearly.

So the fix is not to pick a winner between the consumers. Give each a **materialization** with sublinear access over the slice it needs, behind a single source of truth: a human gets a rendered, browsable view with find-in-page; an agent gets a scoped query or search path. A large reference index, for instance, need not sit on the agent's default read path to earn its keep — it can be materialized for the human and reached by the agent through a query instead, routed to the consumer whose access mode makes it cheap, not deleted.

Access cost is not the only place the proxy breaks: agents also treat read text as possible instruction where a human treats it as inert, and confabulate where a human would ask. This note isolates access cost because it has a clean structural fix — not because it is the most frequent exception.

---

Relevant Notes:

## Under-review context phrase

the competent-executor premise this claim rests on
