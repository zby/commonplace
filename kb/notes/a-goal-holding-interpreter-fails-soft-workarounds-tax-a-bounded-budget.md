---
description: "A procedure compiles its goal away, so a blocked step fails loud and hard; an interpreter holds the goal and re-routes, so failures are absorbed as a per-encounter tax on bounded capacity — silent, accumulating, and softly saturating"
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, llm-interpretation-errors]
---

# A goal-holding interpreter fails soft, and its workarounds tax a bounded budget

A procedure is a goal compiled away: the artifact holds one path, the end is no longer in the representation, and a blocked step has nothing to re-plan from — fail-stop is structural, not a design choice. An interpreting agent holds the *end* and derives means at runtime, so a blocked path triggers re-derivation, [navigation of an admissible space rather than a line](./agentic-systems-interpret-underspecified-instructions.md). The two execution styles therefore have inverted failure economics. In the exact layer, failure cost is a step function and detection is free — the failure announces itself. In the interpreted layer, failure cost is amortized into workarounds and detection is destroyed by the very mechanism that makes the system robust: the workaround consumes the failure event, often leaving a *successful outcome* on top, which is why [semantic recovery breaks traditional debugging intuitions](./traditional-debugging-intuitions-break-when-tool-loops-can-recover.md).

## One property, two faces

The robustness is not a separate mechanism from the interpreted layer's characteristic error. [Underspecification](./llm-interpretation-errors-README.md) — the interpreter's freedom to choose among readings — is the deviation source [the error-correction asymmetry charges against semantic work](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md), and it is *the same property* that supplies path multiplicity when a route is blocked. Interpretive freedom has two faces: deviation from intent, and resilience under partial breakage. Codification's trade restates itself accordingly: removing the freedom buys exactness *and loud failure* at the price of brittleness; keeping it buys survival at the price of silence.

## The tax and the ceiling

Workarounds spend context, attention, and reasoning steps from a bounded pool, so an unfixed defect in the interpreted layer behaves like **debt taxed per encounter**: every traversal that meets it pays again. Accumulation does not produce a crash; it produces load — and because [context degrades silently under volume, complexity, and interference](./agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md), the approach to saturation is as quiet as the failures themselves. The interpreted layer's ceiling is workaround load crowding out task work, reached gradually and invisibly, where the exact layer's ceiling is one wrong transition, reached instantly and loudly.

A system like this KB exhibits the pattern directly: its linking contracts accumulated contradictions over a year of normal operation, surfaced only when a review was commissioned, and [an index's completeness promise degraded quietly](../reference/tag-readme-trace-observed-causal-connection.md) until a validator made the breakage loud. Operation continued throughout — which is the point, in both directions.

## Design consequences

- **Detection must be engineered where failure is absorbed.** The exact layer gets its tripwires free; the interpreted layer needs deliberately scheduled semantic checks — sampled audits over subsystems — because nothing else fires. This is the failure-economics rationale for periodic review of machinery that "works."
- **Maintenance is budget reclamation, not crash prevention.** Fixing an interpreted-layer artifact retires a recurring tax rather than averting a catastrophe — and it harvests the failure event before a workaround consumes it, since a worked-around failure is [a donated oracle never collected](./oracle-accumulation-improves-the-selection-environment.md) and a triggering observation never recorded.
- **The codification boundary gains a failure-economics criterion.** Codify where failures should be loud — converting a silent tax into a tripwire, which is what the tag-readme validator did — and keep interpretation where survival under partial breakage matters more than exactness; [relaxing](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) trades back the other way. This is a lens the [codify-versus-LLM heuristics](./codify-versus-llm-decision-heuristics.md) do not currently list.

## Scope

- The soft-failure claim covers *detected-blockage* failures — the agent notices the obstruction and re-routes. Failures the agent does not notice — a false rule believed, a poisoned instruction followed — are not worked around; they propagate, and they ride [the authority boundary](./a-consumption-channel-delivers-force-without-the-history-that.md) rather than this one. An interpreted system can still fail catastrophically; it fails *softly at blockage*, not softly in general.
- The budget claim is qualitative: per-encounter cost and soft saturation are asserted from mechanism and worked instances, not measured. Which defects tax heavily versus negligibly is unmodeled.

## Open Questions

- Is the workaround tax measurable — workaround events per session as a debt gauge — and could that same signal serve as the trigger for sampled audits, closing the detection loop the first consequence calls for?
- Does saturation arrive as gradual degradation or does the interpreted layer have its own phase transition once re-routing dominates the context budget?
- Can workaround events be cheaply captured at occurrence — turning the lossy repair into a recorded signal — without taxing the very budget they spend?

---

Relevant Notes:

- [Scheduler-LLM separation exploits an error-correction asymmetry](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — contrasts: the same layer split read from the correction-cost side; this note reads it from the failure-presentation side
- [Agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — grounds: interpretation as navigation of an admissible space, the source of path multiplicity
- [Traditional debugging intuitions break when tool loops can recover](./traditional-debugging-intuitions-break-when-tool-loops-can-recover.md) — extends: supplies the mechanism and the economics behind that note's false-confidence phenomenon
- [Agent context is constrained by soft degradation, not hard token limits](./agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md) — grounds: the silent saturation mechanism the workaround budget rides on
- [Oracle accumulation improves selection for later candidates in its maintained domain](./oracle-accumulation-improves-the-selection-environment.md) — extends: why harvesting failure events before workarounds consume them feeds the selection environment
- [Codification and relaxing navigate the bitter lesson boundary](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) — extends: the failure-economics criterion added to the boundary decision
- [Codify versus LLM decision heuristics](./codify-versus-llm-decision-heuristics.md) — extends: a failure-economics lens beside the four it lists
- [A consumption channel delivers force without the history that earned it](./a-consumption-channel-delivers-force-without-the-history-that.md) — contrasts: the boundary carrying the failures this note's soft-failure claim excludes — believed errors, not noticed blockages
- [The tag-readme change as an observed causal-connection trace](../reference/tag-readme-trace-observed-causal-connection.md) — evidenced-by: a quiet degradation absorbed by readers until a validator converted the silent tax into a tripwire
