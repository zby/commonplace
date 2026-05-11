---
description: Opacity is not a representational form; any representation becomes practically opaque at sufficient scale, though distributed-parametric artifacts cross that threshold earliest.
type: kb/types/note.md
tags: [learning-theory]
status: seedling
---

# Opacity is a scale threshold, not a class property

Opacity isn't binary. Any [representational form](./definitions/representational-form.md) (how an operative part is encoded and consumed) becomes practically opaque at sufficient scale. What distinguishes forms is the scale at which they cross that threshold. Distributed-parametric representations cross almost immediately: meaning is smeared across many weights or dense dimensions jointly, so even a modestly-sized network resists per-unit inspection. Truly tiny networks can be read by hand (mechanistic interpretability on toy models does this), but the threshold is very low. Localized artifacts stay readable at much larger aggregates — per-unit readability plus search, diffing, and modular revision let you work with scales that would be hopeless in a weight matrix of comparable size.

"Readable" and "opaque" are convenient labels for where a form sits relative to current tooling, not intrinsic properties of the bytes. A prose KB past a certain size becomes practically opaque too; retrieval and filtering exist because unaided reading runs out. The right question is how much scale a form's structural affordances buy you before inspection breaks down.

---

Relevant Notes:

- [Axes of artifact analysis](./axes-of-artifact-analysis.md) — foundation: the representational-form field this claim qualifies
- [inspectable artifact, not supervision, defeats the blackbox problem](./inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md) — tempers: inspectability is real but scale-dependent, not a categorical guarantee
