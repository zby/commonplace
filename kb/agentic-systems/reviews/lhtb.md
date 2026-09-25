---
type: note
description: LHTB bundled continuation preserves work and feeds verifier outcomes
  into later attempts, with narrower feedback and isolation guarantees than its documentation
generated-by: analyse-agentic-system
analysis-run: AAS-2026-09-25-lhtb-01
source-identity: https://github.com/zli12321/LHTB
reviewed-revision: d78f5eb52ad754c5ee9154741af73130a85a65b8
analysis-result: kb/reports/retained/agentic-system-analysis/AAS-2026-09-25-lhtb-01/result.md
analysis-result-sha256: f63209fb543736769ca89768228a4b2beaa60cd24e705f5e51e43b2d61549d07
---

# LHTB bundled continuation mechanism

LHTB's bundled Harbor single-step scheduler can continue agent work after failed verification within a time budget. It keeps the same environment and agent object, supplies outcome-derived instructions to later calls, and accepts completion when the verifier's `reward` value reaches one. This is a source-grounded subsystem review of the bundled implementation with process rewards disabled; concrete agents, provider isolation, task tests, multi-step tasks and the newer drop-in patch are excluded.

The caller chooses restart or same-conversation continuation. Restart calls the agent again with fresh metrics context; it does not prove that the concrete agent discards its conversation. Same-conversation requires an optional resume method and reuses one context. The timeout bounds agent-phase continuation, while setup, verification and finalization have separate controls. The task author supplies the external outcome test; a passing scalar does not establish full requirement coverage or improved agent capability. See [phase loop](https://github.com/zli12321/LHTB/blob/d78f5eb52ad754c5ee9154741af73130a85a65b8/harbor/src/harbor/trial/trial.py#L867-L988).

The feedback distinction matters. Same-conversation supplies a binary rejection. Restart reads diagnostic files and can insert a failure string, serialized JSON or reward text into its next instruction. This conflicts with documentation describing binary-only feedback by default. Verifier reward parsing and feedback selection also use different file precedence, so diagnostics are not a verified synchronized phase history. See [feedback selection](https://github.com/zli12321/LHTB/blob/d78f5eb52ad754c5ee9154741af73130a85a65b8/harbor/src/harbor/trial/trial.py#L245-L297) and [delivery](https://github.com/zli12321/LHTB/blob/d78f5eb52ad754c5ee9154741af73130a85a65b8/harbor/src/harbor/trial/trial.py#L1127-L1140).

Grader visibility controls are conditional. Shared Linux mode freezes selected tmux descendants and attempts cleanup; failures can warn and continue. Verifier-log clearing depends on provider. Separate verification creates a fresh environment, but the default agent mount list still includes the verifier log directory. The inspected code therefore does not establish universal hidden-test isolation. See [cleanup](https://github.com/zli12321/LHTB/blob/d78f5eb52ad754c5ee9154741af73130a85a65b8/harbor/src/harbor/trial/trial.py#L625-L687) and [mounts](https://github.com/zli12321/LHTB/blob/d78f5eb52ad754c5ee9154741af73130a85a65b8/harbor/src/harbor/trial/trial.py#L1279-L1331).

Memory operates across attempts through workspace persistence and generated continuation text. The verifier event becomes guidance retained for the next agent invocation, which qualifies as per-task online trace learning under the comparison method. Actual use of that guidance, its benefit, and content-directed criticism of a formulated theory remain unobserved. Arbitrary project files and diagnostic payloads prevent complete representation and lineage classifications. Context metrics and result JSON are not proof of restored conversation memory.

The strongest supported contribution is an outcome-gated opportunity to revise artifacts under an external test. Narrow scheduler reflection is wired through phase/time/termination state; conjectural learning and self-improvement remain uninspected. No model, container or benchmark was run. Candidate-linked traces, controlled feedback-dependence checks and provider-specific exposure tests would resolve different remaining questions.

The [exact analysis](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-lhtb-01/result.md) retains the runtime map, evidence quotes, memory profile, epistemic analysis and limitations.
