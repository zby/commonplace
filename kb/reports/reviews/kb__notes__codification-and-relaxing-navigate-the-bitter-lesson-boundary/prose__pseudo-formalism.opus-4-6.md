## Result: PASS

No pseudo-formalism found.

The only formal-looking notation in the note is the sharing factor κ (κ ≈ 1, κ < 1, κ = 0.28 for CoT). This notation is not the note's invention — it comes from the cited Ebrahimi et al. source and carries specific quantitative meaning:

- κ ≈ 1 means no cross-length generalization.
- κ < 1 means training diversity actively hurts.
- κ = 0.28 is a specific measured value for a specific condition (CoT supervision).

Deleting the κ values and restating in prose would lose precision — "sharing factor is approximately one" is less compact and no clearer than "κ ≈ 1" when the reader can follow the source link. The notation does genuine informational work: it conveys three distinct quantitative findings concisely. Someone could use these values to compare against results in other architectures or task types.
