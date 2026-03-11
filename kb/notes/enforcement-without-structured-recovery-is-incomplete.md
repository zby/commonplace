---
description: The enforcement gradient covers detection and blocking but has no recovery column — recovery strategies (corrective → fallback → escalation) are the missing layer, and oracle strength determines which are viable at each level
type: note
traits: [has-external-sources]
areas: [kb-design, learning-theory]
status: seedling
---

# Enforcement without structured recovery is incomplete

The [enforcement gradient](./methodology-enforcement-is-constraining.md) captures two dimensions of methodology enforcement — trigger reliability and response determinism — but says nothing about what happens *after* enforcement fires. A blocking hook rejects the operation; a warning hook outputs a signal. In both cases, the next step is left to the agent. [Teaching error messages](./error-messages-that-teach-are-a-constraining-technique.md) narrow the interpretation space, but whether the agent actually applies the fix remains probabilistic. Detection and blocking are systematic; recovery is ad hoc.

## The gap in the current gradient

The enforcement gradient table has columns for trigger, response, and reliability — but no recovery column. At each layer, recovery is unstructured:

- **Instructions** — no structured follow-up; the agent may or may not self-correct.
- **Skills** — the user can re-invoke, but the skill prescribes no failure strategy.
- **Warning hooks** — the agent improvises a response. Teaching messages help, but the correction remains indeterministic.
- **Blocking hooks** — the operation is rejected. The agent retries with no structured strategy for retrying differently.
- **Scripts** — execution succeeds or fails; on failure, the error propagates with no recovery logic.

The gap is sharpest at the warning-hook level. Warning hooks target soft violations — cases where the operation should not be blocked outright but something needs to change. Yet the current design emits a signal and leaves the response entirely to the agent. This is detection without recovery.

## Recovery as a typed strategy

The [ABC framework](../sources/agent-behavioral-contracts-formal-specification-runtime-enforcement.ingest.md) provides vocabulary for this missing layer. ABC distinguishes three recovery strategies for soft constraint violations, ordered by cost and human involvement:

1. **Corrective action** — the agent fixes the violation directly. This requires knowing what "fixed" looks like — a hard oracle for the corrected state.
2. **Fallback chain** — if direct correction fails, the agent falls back to a simpler, safer strategy. This requires pre-specified fallback options.
3. **Escalation** — if fallback also fails, the agent requests human intervention. This acknowledges that the oracle is too weak for automated recovery.

These three strategies extend the enforcement gradient with a recovery column:

| Layer | Detection | Recovery |
|-------|-----------|----------|
| Instruction | agent remembers (unreliable) | agent improvises (unstructured) |
| Skill | user invokes (reliable) | skill could prescribe retry strategy (not currently done) |
| Hook (warn) | event fires (reliable) | teaching message + corrective action; fallback to re-prompt with constraints |
| Hook (block) | event fires, operation rejected (reliable) | corrective action (fix and retry); fallback (simpler approach); escalation (ask user) |
| Script | deterministic check (reliable) | deterministic correction if possible; escalation if not |

Reading the table top to bottom, a pattern emerges: the viable recovery strategy at each layer is constrained by how much the system knows about the correct state. Scripts can sometimes auto-correct because they operate on structured data with hard oracles. Warning hooks can teach the fix but cannot guarantee the agent applies it. Instructions cannot even guarantee the agent notices the problem. Recovery automation tracks oracle strength.

## Oracle strength constrains recovery automation

The previous section's bottom-to-top pattern — scripts auto-correct, hooks teach, instructions hope — reflects the [oracle strength spectrum](./oracle-strength-spectrum.md). Oracle strength determines which recovery strategies are viable:

- **Hard oracle** (deterministic verification) — corrective action can be fully automated. The system knows what "correct" looks like and can generate the fix with certainty. Scripts and structural validators live here.
- **Soft oracle** (proxy score) — corrective action requires the agent to interpret the signal. Teaching error messages narrow the interpretation space, but the correction remains probabilistic. Warning hooks with good messages live here.
- **Interactive oracle** (human feedback) — escalation is the appropriate recovery strategy. The system detects that something is wrong but cannot determine the fix autonomously. Blocking hooks are hard oracles for *detection* (they deterministically reject the operation), but when the violation requires judgment to resolve, the *recovery* is escalation — the human provides the oracle for what the correct output should be.
- **No oracle** — no structured recovery is possible. The system cannot reliably detect the violation, let alone prescribe a fix. Instructions live here; recovery depends entirely on the agent's own judgment.

ABC's Drift Bounds Theorem formalises the cost of missing recovery. Behavioral drift converges to D*=α/γ — the ratio of natural drift rate (α) to recovery rate (γ). Structured recovery increases γ: strong oracles make corrections accurate, and fast escalation ensures humans intervene before drift compounds. Without structured recovery, γ approaches zero and drift is unbounded. This is the formal statement of what happens when warning hooks fire but the agent ignores or misinterprets them.

## Open questions

- Should the enforcement gradient table in [methodology-enforcement-is-constraining](./methodology-enforcement-is-constraining.md) gain a recovery column, or does it stay focused on detection/blocking while this note handles recovery? Adding the column risks overloading a note that's already dense; keeping them separate risks the recovery layer being invisible to anyone reading only the enforcement note.
- What does a concrete recovery-aware hook look like in this KB? A warning hook that outputs a structured JSON with `{violation, fix_instruction, fallback, escalation_threshold}` rather than a prose warning would be a step toward typed recovery — but is the complexity justified at this scale?

---

Relevant Notes:

- [methodology-enforcement-is-constraining](./methodology-enforcement-is-constraining.md) — extends: adds the recovery column missing from the enforcement gradient; the gradient captures detection and blocking but not what happens after
- [error-messages-that-teach-are-a-constraining-technique](./error-messages-that-teach-are-a-constraining-technique.md) — extends: teaching messages are the inform axis of recovery but stop at "teaches the fix" — this note adds the structured follow-through (corrective → fallback → escalation) that turns teaching into recovery
- [oracle-strength-spectrum](./oracle-strength-spectrum.md) — determines: oracle strength constrains which recovery strategies are viable; hard oracles enable auto-correction, soft oracles require agent interpretation, no-oracle means no structured recovery
- [ABC: Agent Behavioral Contracts](../sources/agent-behavioral-contracts-formal-specification-runtime-enforcement.ingest.md) — provides framework: the corrective → fallback → escalation recovery vocabulary and Drift Bounds Theorem that formalise the missing layer
- [error-correction-works-above-chance-oracles-with-decorrelated-checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — mechanism: error correction through repetition is one implementation of automated recovery for soft-oracle domains — amplification converts weak detection into reliable correction
- [reliability-dimensions-map-to-oracle-hardening-stages](./reliability-dimensions-map-to-oracle-hardening-stages.md) — contextualises: the safety dimension ("what happens when it doesn't work?") is the recovery question stated as a reliability property

Topics:

- [kb-design](./kb-design.md)
- [learning-theory](./learning-theory.md)
