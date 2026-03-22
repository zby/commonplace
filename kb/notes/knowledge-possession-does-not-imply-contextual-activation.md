---
description: A model can possess knowledge yet fail to activate it; reliability depends on generating the right questions, so elicitation must evolve from static prompts into maintained review systems
type: note
traits: [has-external-sources]
tags: [llm-interpretation-errors, failure-modes, evaluation]
status: seedling
---

# Knowledge possession does not imply contextual activation

A model can contain relevant knowledge and still fail to surface it when it matters. Possession and activation are distinct.

## The expert-witness failure mode

The model behaves like an expert witness, not a reviewer: full, accurate answers to whatever you ask, without ever raising the questions you didn't ask — even when the answer would change everything. A human reviewer sees a retry function without jitter and says "where's the jitter?" — no prompt needed. Twenty years of 2AM pages is their checklist. The model has equivalent knowledge and proves it the moment someone asks. It just doesn't volunteer it.

More precisely: for candidate insight `x` and context `c`, distinguish retrievability `R_x` (will the model produce `x` when explicitly asked?) from spontaneous activation `A_x(c)` (will `x` surface without explicit request?). Activation failure is the regime where `R_x` is high, `A_x(c)` is low, and the utility `U_x(c)` of surfacing `x` is high. The operative distinction is not *knows* vs. *does not know* — it is *stored* vs. *elicited in this context*.

## Why activation fails

Activation requires more than stored capability:

1. **Cue match** -- current context must hit the right retrieval cues.
2. **Priority arbitration** -- activated candidates compete for limited reasoning budget.
3. **Commitment** -- the model must decide to externalize the candidate insight.

Most "model can do X" demonstrations pre-supply all three stages by asking directly for `X`. They test execution after activation, not activation itself.

This is not uniquely an LLM pathology — humans show the same structure ("I knew this, but it didn't occur to me"), and "inspiration" is often a cue-arrival event: the knowledge existed, but the right trigger did not occur in time. LLM systems make the control surface explicit: prompt context is where cue match succeeds or fails, which makes the gap both more visible and more tractable.

Empirically, the initiative gap scales with distance from the code. Models reliably catch syntax and logic errors, less reliably catch runtime failure patterns, and rarely catch deployment-topology failures unprompted. The further the failure mode lives from the code under review, the less likely the context provides adequate cues.

## The question-generation bottleneck

Let `Q(c)` be the set of questions a workflow actually asks in context `c` — user prompts, harness prompts, checklist probes. If no question in `Q(c)` cues `x`, high retrievability is operationally irrelevant.

The detection probability for insight `x` in context `c` decomposes as:

`D_x(c) ≈ P(x ∈ Q(c)) × P(x activates | queried, c) × P(x externalized | activated, c)`

The three terms map to the three stages above: whether the right question is asked at all (cue match), whether it triggers activation (priority arbitration), and whether the model commits to externalizing the result (commitment). For many high-impact deployment failures, the first term dominates — the question is never asked.

## The expertise gap constraint

The person who most needs activation scaffolds is the one least able to construct them. The developer who prompts "build me a retry function" is probably not the developer who knows to ask about thundering herds — that's the whole reason they're using the model. The safety net gets a hole shaped exactly like the thing it is supposed to catch.

## Elicitation strategies

Viable strategies must either externalize expert knowledge or use general-purpose probes that activate domain-specific reasoning without requiring domain-specific questions. The following are ordered from most to least expertise required of the user:

### 1. Direct targeted probes

The user supplies the specific question: "what about the thundering herd?" Near-perfect activation (`R_x` ≈ 1.0), but only available when the user already knows what failure mode to probe. This is the baseline that demonstrates the knowledge exists — not a solution to the activation problem.

### 2. Perspective assignments

Assign the model a role that carries implicit failure concerns: "review this as the on-call engineer at 2AM," "review this as the maintenance programmer," "review this as the customer." McConnell's *Code Complete* found that perspective-assigned reviewers uncover more defects than general review. "What happens with 1,000 clients?" is a perspective assignment; "any concerns?" is not.

The user needs to know *which perspectives matter*, not *which specific bugs to look for*. The perspective carries its own retrieval cues.

### 3. Domain checklists

Externalized expert knowledge: codified lists of failure families that the model must address regardless of what the user asks. The human reviewer's "twenty years of 2AM pages" made explicit. Examples: "for any network-calling code, address thundering herd, connection exhaustion, timeout propagation" or "for any data pipeline, address data volume scaling, idempotency, partial failure."

Expertise is supplied once by the checklist author and reused by every user. The risk: checklists ossify — they cover known failure families but not novel ones.

### 4. Structured adversarial prompts

General-purpose probes that don't require domain-specific knowledge: "what breaks at 100x scale?", "what happens when two instances run behind a load balancer?", "what fails when this runs for a year?" These are parameterized templates — the user fills in scale/topology/duration without needing to know *which* failure they're probing for.

Lowest expertise barrier among the probe types. Activation rate is lower than targeted probes but substantially higher than undirected review, because the prompt narrows the retrieval space without naming the specific failure.

### Composing strategies: two-pass review

The strategies above can be composed into a review architecture. Pass 1: unconstrained self-review (catches code-level bugs the model activates on its own). Pass 2: mandatory probes from strategies 2–4 across dimensions the model systematically underweights — scale, concurrency, deployment topology, data volume. The second pass constructs the oracle the first pass fails to be.

## Beyond known failure families

Strategies 1–4 address *known unknowns*: we know the failure family exists and need to test whether it applies here. The harder regime is *unknown unknowns* — failure families we have not yet learned to ask about.

Converting unknown unknowns into known unknowns requires mechanisms that *generate questions*: incident mining, cross-model disagreement analysis, adversarial scenario generation, and periodic expert audits. The operational goal is to discover new failure families, then convert them into cheap mandatory probes.

### Checklist lifecycle

To absorb discoveries and prevent ossification, checklists need a maintenance loop:

1. **Seed** from incidents, postmortems, and known failure literature.
2. **Enforce** probes in mandatory review pass(es).
3. **Log misses** — bugs that escaped because no probe existed, or probe wording was too weak.
4. **Distill updates** into new or rewritten probes.
5. **Prune stale probes** that no longer discriminate in practice.

This makes elicitation a continuing investigation process, not a one-time prompt template.

## Measurement

For any target insight class `x`, evaluate both:

1. **Probed condition:** explicitly query for `x` (estimates `R_x`).
2. **Open condition:** broad task where `x` is useful but unrequested (estimates `A_x(c)` when `U_x(c)` is high).

Report the activation gap: high probe success with low open emergence.

To track the elicitation system itself:

- **Question coverage:** fraction of reviews where `Q(c)` includes at least one probe for each critical failure family.
- **Discovery rate:** new high-utility failure families found per `N` reviews.
- **Probe staleness rate:** fraction of probes that never trigger actionable findings over a rolling window.

## Open questions

- Which mechanisms best generate new high-value questions when we do not already know what to ask?
- How often should checklist sets be refreshed to balance drift, churn, and context budget?
- Which perspective assignments give the best activation coverage per token cost?
- Does the initiative gap gradient (code → runtime → deployment) hold across non-coding domains?
- Can memory close the gap, or does the 13% spontaneous detection rate mean memory just filters for what was already activated?
- What is the right granularity for adversarial prompt templates — too broad misses, too narrow requires expertise again?

---

Relevant Notes:

- [the-augmentation-automation-boundary-is-discrimination-not-accuracy](./the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) — complements: distinguishes per-instance correctness discrimination from aggregate accuracy; this note adds the prior activation requirement
- [evaluation-automation-is-phase-gated-by-comprehension](./evaluation-automation-is-phase-gated-by-comprehension.md) — parallels: both require stage separation instead of aggregate score reading
- [oracle-strength-spectrum](./oracle-strength-spectrum.md) — enables: retrieval scaffolds are oracle-hardening moves for activation-limited settings
- [agentic-systems-interpret-underspecified-instructions](./agentic-systems-interpret-underspecified-instructions.md) — foundation: prompt context determines which interpretations are activated
- [silent-disambiguation-is-the-semantic-analogue-of-tool-fallback](./silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) — example: low activation of critical branches can be masked by superficially successful outputs
- [the-bug-that-shipped-2035319413474206122](../sources/the-bug-that-shipped-2035319413474206122.md) — evidence: deployment-failure insights retrievable on probe but often absent in undirected review
- [professional-software-developers-dont-vibe-they-control](../sources/professional-software-developers-dont-vibe-they-control.md) — complement: experts compensate for activation limits by explicit planning, narrow tasking, and supervision
- [towards-a-science-of-ai-agent-reliability](../sources/towards-a-science-of-ai-agent-reliability.md) — context: reliability dimensions motivate separating stored capability from operationally activated behavior
