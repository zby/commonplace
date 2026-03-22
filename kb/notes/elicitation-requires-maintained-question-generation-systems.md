---
description: Four elicitation strategies ordered by user expertise required, composable into review architectures with maintenance loops that prevent ossification
type: note
traits: [has-external-sources]
tags: [llm-interpretation-errors, failure-modes, evaluation]
status: seedling
---

# Elicitation requires maintained question-generation systems

Since [knowledge storage does not imply contextual activation](./knowledge-storage-does-not-imply-contextual-activation.md), reliability depends on whether the workflow asks questions that activate relevant knowledge. The user who needs the model's knowledge most is least equipped to cue it — the expertise gap makes the activation problem self-reinforcing. Viable strategies must either externalize expert knowledge into the workflow or use general-purpose probes that activate domain-specific reasoning without requiring domain-specific questions.

## Strategies ordered by expertise required

The following strategies are ordered from most to least expertise required of the user. Each lowers the barrier differently.

### 1. Direct targeted probes

The user supplies the specific question that targets the knowledge directly. Activation is near-perfect, but only because the user already knows what to ask. This demonstrates that the knowledge exists. It does not solve the activation problem.

### 2. Perspective assignments

Assign the model a role that carries implicit concerns: "review this as the on-call engineer at 2AM," "review this as opposing counsel," "review this as the end user who will encounter this at scale." The mechanism: a perspective carries its own retrieval cues, narrowing the activation space without requiring the user to name specific failures. In human code review, McConnell's *Code Complete* found that perspective-assigned reviewers uncover more defects than undirected review — the same principle applies to LLMs, where the role assignment shapes which stored knowledge gets activated. "What happens with 1,000 concurrent users?" is a perspective assignment. "Any concerns?" is not.

The user needs to know *which perspectives matter*, not *which specific problems to look for*. This reduces the expertise requirement from "know the failure mode" to "know the stakeholder."

### 3. Domain checklists

Externalized expert knowledge: codified lists of failure families that the model must address regardless of what the user asks. This makes the experienced practitioner's hard-won pattern recognition explicit and reusable. Examples: "for any network-calling code, address thundering herd, connection exhaustion, timeout propagation" or "for any contract review, address jurisdiction conflicts, liability caps, termination triggers."

Expertise is supplied once by the checklist author and reused by every user. The risk: checklists ossify — they cover known failure families but not novel ones.

### 4. Structured adversarial prompts

General-purpose probes that do not require domain-specific knowledge: "what breaks at 100x scale?", "what happens when two instances of this run simultaneously?", "what fails when this runs for a year?", "what does an adversary do with this?" These are parameterized templates. The user fills in scale, concurrency, or duration without needing to know which specific failure they are probing for.

This has the lowest expertise barrier among the probe types. Activation is weaker than with targeted probes but substantially better than with undirected review, because the prompt narrows the retrieval space without naming the failure.

## Composing strategies: two-pass review

The strategies compose into a review architecture. Pass 1: unconstrained self-review, which catches the issues the model activates on its own. Pass 2: mandatory probes from strategies 2–4 across dimensions the model systematically misses — scale, concurrency, failure cascades, second-order effects. The second pass constructs the oracle the first pass fails to be.

## Beyond known failure families

Strategies 1–4 address *known unknowns*: failure families we know exist and need to test for here. The harder regime is *unknown unknowns*: failure families we have not yet learned to ask about.

Converting unknown unknowns into known unknowns requires mechanisms that *generate questions*: incident analysis, cross-model disagreement, adversarial scenario generation, and periodic expert audits. The operational goal is to discover new failure families, then convert them into cheap mandatory probes.

## Checklist lifecycle

To absorb discoveries and prevent ossification, checklists need a maintenance loop:

1. **Seed** from incidents, failure analyses, and known failure literature.
2. **Enforce** probes in mandatory review pass(es).
3. **Log misses** — problems that escaped because no probe existed, or probe wording was too weak.
4. **Distill updates** into new or rewritten probes.
5. **Prune stale probes** that no longer discriminate in practice.

This lifecycle is what distinguishes a maintained question-generation system from a static checklist. Without it, checklists decay: they cover yesterday's failures while tomorrow's slip through.

## Measurement

To evaluate whether the system is working, track both the activation gap and the question system's health.

**Activation gap measurement:** For any target insight class, evaluate under two conditions — probed (explicitly query for the insight) and open (broad task where the insight is valuable but unrequested). The gap between probed and open performance is the activation gap.

**System health metrics:**

- **Question coverage:** fraction of reviews where the workflow includes at least one probe for each critical failure family.
- **Discovery rate:** new high-utility failure families found per N reviews.
- **Probe staleness rate:** fraction of probes that never trigger actionable findings over a rolling window.

## Open questions

- Which mechanisms best generate new high-value questions when we do not already know what to ask?
- How often should checklist sets be refreshed to balance drift, churn, and context budget?
- Which perspective assignments give the best activation coverage per cost?
- What is the right granularity for adversarial prompt templates — too broad misses, too narrow requires expertise again?

---

Relevant Notes:

- [knowledge-storage-does-not-imply-contextual-activation](./knowledge-storage-does-not-imply-contextual-activation.md) — foundation: the activation gap and expertise gap that this note addresses
- [oracle-strength-spectrum](./oracle-strength-spectrum.md) — enables: elicitation strategies are oracle-hardening moves for activation-limited settings
- [the-augmentation-automation-boundary-is-discrimination-not-accuracy](./the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) — complements: question coverage is a prerequisite for the per-instance discrimination that automation requires
- [the-bug-that-shipped-2035319413474206122](../sources/the-bug-that-shipped-2035319413474206122.md) — evidence: deployment-failure insights retrievable on probe but absent in undirected review; motivates structured elicitation
- [professional-software-developers-dont-vibe-they-control](../sources/professional-software-developers-dont-vibe-they-control.md) — complement: expert practitioners compensate for activation limits through explicit planning, narrow tasking, and supervision — a human version of two-pass review
- [towards-a-science-of-ai-agent-reliability](../sources/towards-a-science-of-ai-agent-reliability.md) — context: reliability dimensions motivate the measurement framework
