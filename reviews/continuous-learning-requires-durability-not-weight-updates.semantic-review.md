=== SEMANTIC REVIEW: continuous-learning-requires-durability-not-weight-updates.md ===

Claims identified: 11

1. "When AI labs discuss 'continuous learning,' they usually mean weight updates during or after deployment" (scope claim, paragraph 1)
2. "That is a real form of continuous learning, but it is not the only one" (scope claim, paragraph 1)
3. "continuous learning requires durable adaptive change, not specifically weight change" (title claim, paragraph 2)
4. Simon's definition is "the key test: learning is any change that produces a more or less permanent change in a system's capacity for adapting to its environment" (definition, attributed via linked note, paragraph 2)
5. "a system also learns when it accumulates durable symbolic artifacts that change future behavior: tips mined from trajectories, prompts revised from experience, schemas that reject previous failures, tests that catch recurring mistakes, rules and procedures that guide later runs" (causal/scope claim, paragraph 2)
6. "The unexamined assumption is that 'capacity change' requires parameter change" (claim about the field, paragraph 3)
7. "If the artifact persists and later behavior depends on it, capacity has changed -- Simon's definition is satisfied regardless of the medium" (inference from Simon, paragraph 3)
8. "A better next answer caused by something still sitting in the current context window is not continuous learning, because the change evaporates when the session ends" (boundary claim, paragraph 4)
9. "The important boundary is ephemeral vs durable, not weights vs not-weights" (definitional claim, paragraph 4)
10. "both produce durable capacity change through inspectable artifacts -- which is the only thing the definition requires" (scope claim with "only thing," paragraph 5)
11. "Weight updates and symbolic artifacts are two learning substrates, not a real case and a metaphorical one" (enumeration -- two substrates, paragraph 6)

WARN:
- [Completeness] The note claims "the important boundary is ephemeral vs durable, not weights vs not-weights" and that durability is "the only thing the definition requires." But Simon's definition says "more or less permanent change in its capacity for adapting to its environment." The note operationalizes "permanent" as "durable" and drops "capacity for adapting to its environment." A durable artifact that persists but never actually changes behavior (e.g., a tip that is stored but never retrieved, or a schema that is committed but never loaded into context) satisfies the note's durability criterion but not Simon's full definition. The note acknowledges "later behavior depends on it" in paragraph 3 but the title claim and boundary claim (claim 9) reduce the requirement to durability alone. The gap between "durable" and "durable AND causally active" is elided.

- [Completeness] The enumeration of "two learning substrates" (claim 11: weight updates and symbolic artifacts) omits at least one plausible boundary case: learned retrieval/routing configurations that are neither weight updates nor symbolic artifacts in the note's sense. A system that learns to rank documents differently by updating an index or retraining an embedding model has made a durable capacity change, but the result is a hybrid -- it's not an inspectable symbolic artifact and it's not a change to the primary model's weights. The linked note "Learning substrates, backends, and artifact forms" actually handles this more carefully by distinguishing "subsymbolic substrate" from "symbolic artifact substrate," but the reviewed note's phrasing ("weight updates and symbolic artifacts are two learning substrates") presents these as exhaustive without qualification.

- [Grounding] The note says the two cited systems "differ in mechanism, oracle strength, and artifact form, but both produce durable capacity change through inspectable artifacts -- which is the only thing the definition requires." But Simon's definition (as relayed through the linked note) requires "capacity for adapting to its environment," not merely "durable capacity change through inspectable artifacts." The word "inspectable" is an additional property the note quietly attaches to the definition's requirements. Simon's definition would be equally satisfied by durable but opaque artifacts -- the inspectability is a desirable property of the symbolic artifact substrate, not something "the definition requires."

INFO:
- [Completeness] The boundary case of environmental/infrastructure changes probes the ephemeral-vs-durable line. Consider: upgrading to a faster GPU, switching to a better base model, or deploying to a region with lower latency. These are durable changes that improve the system's capacity for adapting to its environment. They satisfy the note's stated criterion (durable, behavior depends on them) but feel categorically different from "learning." The note's framework has no way to exclude them except by implicitly restricting "change" to knowledge-bearing changes, which is a constraint it never states.

- [Grounding] The note attributes to AI labs that continuous learning "usually" means weight updates. This is a reasonable characterization of the ML literature, but the note does not cite a specific source for this claim. It functions as an unstated premise. Given that the entire argument pivots on redefining continuous learning against this conventional meaning, the lack of citation is notable though not disqualifying -- the characterization is broadly accurate.

- [Internal consistency] Claim 10 says inspectable artifacts producing durable capacity change is "the only thing the definition requires." But paragraph 3 says "If the artifact persists and later behavior depends on it, capacity has changed." The second formulation adds a causal condition ("later behavior depends on it") that the first omits. These two formulations of what the definition requires are not identical -- the paragraph 3 version is more careful.

PASS:
- [Grounding] Simon's definition, as attributed via the linked note "learning is not only about generality," checks out. The linked note quotes Simon: "learning is any change in a system that produces a more or less permanent change in its capacity for adapting to its environment." The reviewed note's use of this definition is faithful to the source.

- [Grounding] The characterization of in-context learning as ephemeral (paragraph 4) aligns with the linked note "in-context learning presupposes context engineering," which makes the same distinction: in-context adaptation is session-scoped and evaporates. No scope mismatch.

- [Grounding] The characterization of the trajectory-informed memory generation system as producing "durable capacity change through inspectable artifacts" is accurate per the ingest report, which describes tips as "durable, inspectable artifacts that persist across sessions and improve behavior without weight updates."

- [Grounding] The link to "constraining during deployment is continuous learning" with the relationship "exemplifies" is accurate. That note explicitly describes itself as "a subset claim, not the umbrella claim" and positions the reviewed note as its foundation. The directionality is consistent in both directions.

- [Internal consistency] The note's central argument is internally coherent: it defines a criterion (durability), applies it to draw a boundary (ephemeral vs durable), and uses that boundary to reclassify symbolic-artifact systems as continuous learning. No section contradicts another. The definition drift noted in INFO above (between "only thing the definition requires" and "persists and later behavior depends on it") is a precision gap, not a contradiction.

- [Internal consistency] The note's self-positioning as an umbrella claim is consistent with how linked notes reference it. "Constraining during deployment" calls this note its "foundation" and describes itself as "one concrete non-weight case." "Learning substrates, backends, and artifact forms" also calls this note "foundation." The reviewed note appropriately occupies the general-claim position in the network.

Overall: 3 warnings, 3 info
===
