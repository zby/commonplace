=== PROSE REVIEW: capability-placement-should-follow-autonomy-readiness.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The decision rule section presents a three-tier taxonomy ("Ready for autonomous use," "Reusable but not autonomous-ready," "Exploratory or unstable") as if it were established methodology: "The organizing variable is **autonomy readiness**." This is the note's own proposed framework, but nothing flags it as proposed. The language asserts rather than proposes ("Capability placement is a separate decision," "The organizing variable is," the imperative arrows in the decision rule).
  Recommendation: Add hedging that marks this as a proposed heuristic, e.g., "A useful organizing variable is autonomy readiness" rather than "The organizing variable is autonomy readiness." The decision rule could open with "A workable placement heuristic:" rather than presenting the three tiers as the canonical answer.

INFO:
- [Proportion mismatch] The core claim is in the title: placement should follow autonomy readiness. The "Decision rule" section (the load-bearing section that operationalizes this claim) gets three bullet points totaling roughly 40 words. The "Consequence for AGENTS.md" section, which is a downstream implication rather than the core argument, gets comparable space. The "Migration path," which is also a consequence, gets the most developed treatment (four numbered steps plus a summary sentence). The note's center of gravity sits on consequences rather than on justifying or developing the placement principle itself. This is mild — the note is short and reads clearly — but worth flagging.

CLEAN:
- [Source residue] The note operates at its claimed generality level throughout. It discusses capabilities, skills, instructions, and AGENTS.md — all terms native to the knowledge-base methodology domain. No leaked vocabulary from an unrelated source domain.
- [Pseudo-formalism] No formal notation or mathematical apparatus is present. The decision rule uses plain-language bullet points with arrow notation, which is appropriately informal.
- [Orphan references] No specific figures, data points, named studies, or empirical claims appear. All claims are framework-level assertions within the KB methodology.
- [Unbridged cross-domain evidence] No cross-domain evidence is cited. The note stays within its own domain (agent knowledge-base design) throughout.
- [Redundant restatement] Each section opens with new material. The "Consequence for AGENTS.md" section does not re-explain the decision rule before stating its point. The "Migration path" section does not restate the consequence. The note is compact enough that restatement would be obvious, and none is present.
- [Anthropomorphic framing] The note uses "the agent runtime exposes it through skills" and "the agent can execute a capability" — these attribute execution and exposure to the agent/runtime, which is appropriate mechanical language for software systems. No terms imply mental states or human-like cognition.

Overall: 1 warning, 1 info
===
