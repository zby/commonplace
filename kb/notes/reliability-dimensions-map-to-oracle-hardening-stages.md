---
description: The four reliability dimensions from Rabanser et al. (consistency, robustness, predictability, safety) each harden a different oracle question — mapping empirical agent evaluation onto the oracle-strength spectrum
type: note
traits: [has-external-sources]
areas: [learning-theory]
status: seedling
---

# Reliability dimensions map to oracle-hardening stages

The [oracle-strength spectrum](./oracle-strength-spectrum.md) describes a gradient from hard oracles (cheap deterministic checks) to no oracle (vibes). The engineering move is to harden oracles — convert no-oracle into some-oracle, then tighten. But *which* oracle are you hardening? The Rabanser et al. reliability framework ([source](../sources/towards-a-science-of-ai-agent-reliability.md)) decomposes agent reliability into four dimensions, and each one targets a distinct verification question:

| Dimension | Oracle question | Hardening move |
|-----------|----------------|----------------|
| **Consistency** | "Does this work?" | Run it again. Same input, same output? Converts interactive oracle to hard oracle via repetition. |
| **Robustness** | "Does this still work?" | Perturb the input. Paraphrase, inject faults, change context. Converts soft oracle ("it usually works") to hard oracle ("it works under these perturbations"). |
| **Predictability** | "Will this work next time?" | Calibrate confidence. If the system says 80% and it's right 80% of the time, the confidence score *is* a soft oracle. Discrimination (assigning higher confidence to correct answers) would push it toward hard. |
| **Safety** | "What happens when it doesn't work?" | Bound the damage. Not a continuous score but a hard constraint — a gate, not a gradient. This is the only dimension that's already a hard oracle by design: either the failure is bounded or it isn't. |

## Why this mapping matters

The oracle-strength note says "invest in telemetry and eval harnesses *before* investing in capability, because guidance is the bottleneck." The reliability framework shows exactly where to invest: each dimension is a separate oracle that can be hardened independently. You don't need to solve all four at once.

The empirical finding that capability gains have outpaced reliability gains over 18 months of model releases is the oracle-strength prediction confirmed at scale: the bottleneck is verification quality, not generation quality. [MAKER's million-step zero-error result](../sources/meyerson-maker-million-step-llm-zero-errors.md) demonstrates what happens when you take this seriously for consistency: decompose to minimal subtasks, vote across independent samples, discard red-flagged outputs. The entire MDAP framework is architectural oracle hardening — and it works precisely because per-step oracle strength is hard (each Towers of Hanoi move has a deterministic correct answer).

## Connection to spec mining

[Spec mining](./spec-mining-as-crystallisation.md) is the operational mechanism for consistency and robustness hardening. You watch failures, extract patterns, write deterministic checks. The Rabanser framework's Table 3 — mapping real-world failures to reliability metrics — is spec mining applied to evaluation itself: each failure class becomes a testable property.

The workflow becomes: observe failure → classify by reliability dimension → mine a spec for that dimension → the oracle hardens.

## The predictability gap

Predictability is the hardest dimension to harden because discrimination (not just calibration) requires the model to know *what it doesn't know* at the individual-task level. The paper finds calibration improving but discrimination stagnant — models get better at aggregate confidence but not at per-instance confidence. This suggests predictability will be the last oracle to harden, and the augmentation strategy (human-in-the-loop for uncertain cases) remains the pragmatic answer.

This connects to the [approval system's value](./approvals-guard-against-llm-mistakes-not-active-attacks.md): a 90%-accurate agent with poor discrimination is fine as an augmentation (human catches the 10%) but dangerous as an automation (nobody catches it). The approval gate converts a weak predictability oracle into an interactive one.

---

Relevant Notes:
- [oracle-strength-spectrum](./oracle-strength-spectrum.md) — foundation: the gradient from hard to no oracle that this note maps reliability dimensions onto
- [spec-mining-as-crystallisation](./spec-mining-as-crystallisation.md) — the operational mechanism for hardening consistency and robustness oracles
- [approvals-guard-against-llm-mistakes-not-active-attacks](./approvals-guard-against-llm-mistakes-not-active-attacks.md) — augmentation as a workaround for weak predictability oracles
- [stabilisation-is-learning](./agentic-systems-learn-through-three-distinct-mechanisms.md) — reliability hardening as deploy-time learning, not training-time learning
- [softening-signals](./softening-signals.md) — indicators for where a component sits on the spectrum; prompt robustness (R_prompt) is a softening signal measured at scale
- [MAKER: Solving a Million-Step LLM Task with Zero Errors](../sources/meyerson-maker-million-step-llm-zero-errors.md) — concrete architectural hardening: decomposition + voting hardens consistency, red-flagging hardens predictability, both enabled by hard per-step oracles

Topics:
- [learning-theory](./learning-theory.md)
