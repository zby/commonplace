=== SEMANTIC REVIEW: baseline.md ===

Claims identified: 18

WARN:
- [completeness] The three trace types (conversation transcripts, tool/action traces, reasoning traces) omit **planning/goal traces** — structured plans, sub-goal decompositions, and task state that are neither chain-of-thought reasoning nor tool execution records nor conversational exchanges. The bounded-context orchestration model note explicitly describes planning calls whose results enter K. A plan artifact sits between reasoning traces and tool traces and does not map cleanly to any of the three enumerated types.

- [completeness] The five costs of trace-preserving handoff omit **hard context-window exhaustion** — the case where accumulated history literally exceeds the token limit and truncation occurs. The note frames costs as quality degradation (soft), but the hard limit is also a real failure mode. This is especially relevant given that the note's framework is built on bounded context.

INFO:
- [grounding] "This is the return-value problem from the scoping note in architectural form." The scoping note's return-value discussion focuses on progressive typing of return values (untyped natural language → structured data) and on what sub-agents expose across frame boundaries. The baseline uses "return-value problem" to mean "transcripts rather than declared objects cross frame boundaries." These are related but not identical — the scoping note emphasizes typing, the baseline emphasizes selection. The identity claim ("this IS the return-value problem") slightly overstates the correspondence.

- [grounding] The baseline presents `select(K)` as the alternative to history inheritance, which is accurate per the orchestration model note. However, the orchestration model note emphasizes that `select` is "where the optimisation lives" and describes it as a hard sequential decision problem. The baseline's framing — "letting `select(K)` choose what the next call should see" — understates the difficulty, making the alternative sound more straightforward than it is.

- [consistency] The note uses "trace" in two senses: (1) as a generic term for accumulated session state in the opening, and (2) as a specific category in the three-type taxonomy. The transition is implicit. The opening's "trace-preserving state" covers all three types; the taxonomy then splits it. The shift is navigable but could cause confusion about whether opening claims apply uniformly to all three types.

- [grounding] The Slate tension section honestly hedges ("What we cannot tell from public evidence is the policy around episodes"), which is appropriate. However, the hedging weakens the four-system pattern claim — three of the four examples are internal KB notes, and the fourth (Slate) is acknowledged as uncertain. The pattern is real but its evidential base is thinner than the enumeration implies.

PASS:
- [consistency] The temporal framing is internally coherent: transcript inheritance is "a sensible exploratory default" early, becomes costly later. The practical principle preserves this arc: "use trace-preserving storage early... move toward artifact-first loading once the caller's real consumption pattern is understood." No contradiction.

- [grounding] Attribution to the chat-history model note is accurate. That note confirms: "Chat is a strong exploratory default" and describes the baseline as a "downstream claim."

- [grounding] Attribution to the tool-loop index is accurate. The index confirms it defines the framework-owned loop pattern and lists the baseline note as a downstream consequence.

- [consistency] The Slate tension section's epistemic posture ("What we cannot tell...") is honest and appropriate.

- [completeness] The practical principle's four guidelines are framed as practical advice, not an exhaustive framework. They do not overclaim.

Overall: 2 warnings, 4 info
===
