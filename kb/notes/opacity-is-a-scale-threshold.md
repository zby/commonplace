---
description: Opacity isn't a property of an artifact class; any representation becomes practically opaque at sufficient scale. Classes differ in the scale at which they cross that threshold.
type: kb/types/note.md
tags: [learning-theory]
status: seedling
---

# Opacity is a scale threshold, not a class property

Opacity isn't binary — any [artifact class](./axes-of-artifact-analysis.md) becomes practically opaque at sufficient scale. What distinguishes classes is the scale at which they cross that threshold. Distributed representations cross almost immediately: meaning is smeared across many weights jointly, so even a modestly-sized network resists per-unit inspection. Truly tiny networks can be read by hand (mechanistic interpretability on toy models does this), but the threshold is very low. Localized artifacts stay readable at much larger aggregates — per-unit readability plus search, diffing, and modular revision let you work with scales that would be hopeless in a weight matrix of comparable size.

"Readable" and "opaque" are convenient labels for where a class sits relative to current tooling, not intrinsic properties of the bytes. A prose KB past a certain size becomes practically opaque too; retrieval and filtering exist because unaided reading runs out. The right question is how much scale a class's structural affordances buy you before inspection breaks down.

---

Relevant Notes:

- [Axes of artifact analysis](./axes-of-artifact-analysis.md) — foundation: the artifact class axis this claim qualifies
- [inspectable substrate, not supervision, defeats the blackbox problem](./inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) — tempers: inspectability is real but scale-dependent, not a categorical guarantee
