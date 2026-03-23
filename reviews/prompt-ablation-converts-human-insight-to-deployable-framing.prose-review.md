=== PROSE REVIEW: prompt-ablation-converts-human-insight-to-deployable-framing.md ===

Checks applied: 8

WARN:
- [Source residue] The note claims general applicability ("the pattern") but nearly every concrete element is from a single source: the curiosity-prompts experiment reviewing a Decapod system. References to "constitution embedding," "codification claim," "cost/benefit reliably reached the target finding (2/2)," "Decapod finding," and "six genuinely different approaches: broad curiosity, cost/benefit analysis, impossibility checking, implication tracing, adversarial assumption, and mechanistic tracing" all come from that one experiment. The Design Constraints and Why It Works sections read more like retrospectives on the curiosity-prompts experiment than descriptions of a general methodology. The Deployments section is exclusively about curiosity-prompts outputs.
  Recommendation: Either frame the curiosity-prompts material explicitly as a worked example throughout (not just in the link annotation), or add a second example from a different domain to demonstrate the pattern's generality. The Design Constraints section in particular would benefit from examples that are not all from the same experiment.

- [Proportion mismatch] The core claim is the 8-step conversion pattern (title: "converts human insight into deployable framing"). The pattern section (steps 1-8) gets roughly 220 words. The Why It Works section, Design Constraints section, and Deployments section together get roughly 350 words, much of which re-explains the curiosity-prompts experiment rather than developing the pattern itself. Steps 6 (bonus findings) and 7 (mechanism analysis) — arguably the most intellectually distinctive parts of the pattern — get one sentence each in the pattern section, then are developed only through the curiosity-prompts lens in later sections.
  Recommendation: Develop steps 6 and 7 within the pattern section itself. They carry the note's distinctive contribution (this is not just "try multiple prompts and pick the winner" — it is "understand why each framing works"). The current single-sentence treatment undersells them.

INFO:
- [Confidence miscalibration] "At least 2 runs per framing" in step 4 is stated as a minimum requirement, and the Open Questions section immediately acknowledges "2 is minimum for detecting consistency; it may be insufficient for close calls." This is honest, but the step itself reads as prescriptive ("At least 2 runs") when the evidence base is a single experiment that used exactly 2 runs. The note could be clearer that this threshold is empirically underexplored.

- [Anthropomorphic framing] "cognitive moves agents can reliably execute" appears twice (steps 2 and 7). "Cognitive moves" is a human-cognition term. In context, the note means something like "reasoning strategies" or "analysis approaches" — which are already prompt-level constructs, not claims about agent internals. The usage is borderline: it is evocative and arguably precise enough in this context, but it could be read as claiming agents have cognition.

CLEAN:
- [Pseudo-formalism] No formal notation, variables, or equations. The note stays in prose throughout. Clean.
- [Orphan references] All specific claims (2/2 score, six framings, "constitution embedding is verbatim copying") are traceable to the linked curiosity-prompts experiment report. No unsourced data points or numbers.
- [Unbridged cross-domain evidence] The note stays within the LLM/agent domain throughout. The human reviewer's insight is explicitly framed as the oracle, not as evidence about human cognition. No cross-domain transfer without bridge.
- [Redundant restatement] Each section opens with new material. The "Why it works" section introduces the oracle-strength framing and the lossiness observation — both new to that section. No restating preambles detected.

Overall: 2 warnings, 2 info
===
