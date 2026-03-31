The note presents three main frameworks: the two-phenomena distinction (semantic underspecification vs. execution indeterminism), the spec-to-program projection model, and the constraining/relaxing spectrum with LLM/code boundaries.

---

**Framework 1: Two phenomena**

Grounding definition: "LLM-based systems differ from traditional programs in two ways that are often conflated but are conceptually distinct."

- Simplest: "return the number 42" at temperature=0. Both phenomena minimized. ✓
- Most extreme: "do something creative" at high temperature. Both maximized. ✓
- Between: precise prompt with high temperature (indeterminism without underspecification). The note handles this — temperature variation within a single interpretation. ✓
- Between: vague prompt at temperature=0. The note explicitly addresses this: "At temperature=0 the LLM still picks one interpretation from the space the spec admits; you just get the same one every time." ✓
- Adjacent: **structured output constraints** (JSON schemas, tool definitions). The note mentions "output schemas" and "tool definitions" in the narrowing section. These constrain both phenomena simultaneously. ✓
- Adjacent: **multi-turn context accumulation**. Each turn narrows the interpretation space. The note mentions "conversation history" as a narrowing mechanism but doesn't develop how accumulating context progressively reduces underspecification. INFO — multi-turn narrowing is mentioned but not analyzed; it's a dynamic process where the two phenomena interact differently over time.

**Framework 2: Spec-to-program projection**

Clean and well-bounded. The compiler vs. projector distinction holds. ✓

**Framework 3: Constraining/relaxing spectrum with boundaries**

- Simplest: moving one function from LLM to code. ✓
- Most extreme: replacing the entire pipeline with code. ✓
- Between: partial constraining (format constrained, interpretation flexible). The note handles this through "progressive constraining" and the file-renaming example. ✓
- The boundary model (LLM → Code → LLM) is clean. The note correctly identifies that both phenomena change simultaneously at boundaries. ✓

No WARN. One INFO on multi-turn narrowing dynamics.
