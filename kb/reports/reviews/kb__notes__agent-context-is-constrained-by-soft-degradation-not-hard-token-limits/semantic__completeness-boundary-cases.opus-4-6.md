The note presents one main framework: soft degradation as the binding constraint on agent context, with two confirmed dimensions (volume, complexity) and one candidate dimension (irrelevant context). It also has a three-level enumeration of invisibility (practitioner, benchmarker, market).

---

**Framework: Soft bound dimensions (volume, complexity, irrelevant context)**

Grounding: empirical sources (Liu et al. 2023, Paulsen 2025, GSM-DC, Chung et al. 2025, ConvexBench).

- Simplest instance: a single-sentence prompt. Volume and complexity are both minimal; no degradation expected. ✓
- Most extreme: a maximally long, deeply compositional context filled with distractors. All dimensions degrade simultaneously. ✓
- Between: a short but extremely complex context (few tokens, deep compositional nesting). ConvexBench is cited as exactly this case. ✓
- Adjacent: **task-type sensitivity** — the soft bound may shift not just with volume and complexity but with the *kind* of task. The note acknowledges this ("task-dependent" appears throughout) but doesn't name task type as a dimension — it's treated as a confound rather than a separable axis. INFO — the note correctly identifies task-dependence but doesn't distinguish between task-type as a separate dimension vs. a moderator of existing dimensions.
- The irrelevant-context dimension is explicitly flagged as uncertain: "may be an independent dimension rather than a sub-mechanism of volume." Good intellectual honesty. ✓

**Framework: Three levels of invisibility**

- Practitioner (model doesn't signal degradation). ✓
- Benchmarker (soft bound is not a single number). ✓
- Market (providers advertise hard limits only). ✓
- All three are clean and well-differentiated.

No WARN. One INFO: task-type as dimension vs. moderator distinction.
