Key claims extracted from each section:

- **Opening**: "Any system with an LLM agent layer has two strata: deterministic base + prompt layer. The prompt layer is where new requirements get absorbed without changing the base."
- **Constraining spectrum**: ad hoc prompts = loosest end (instructions); typed callables = other end. "Both are correct for different moments."
- **Maturation trajectory**: write ad hoc first → extract skill when pattern recurs. "The prompt equivalent of 'write the code three times, then extract a function.'"
- **Prompts carry what types can't**: "Prompts carry judgment that type signatures can't express." Sub-agent prompt = clean context boundary, caller does judgment-heavy work.
- **Homoiconicity**: ad hoc extension works because instructions and content share the same representation in LLM context.

---

**Pairwise consistency checks**

*"Both are correct for different moments" vs. "Prompts carry judgment that type signatures can't express"*

These could appear to tension: if prompts are categorically more expressive, why would typed callables ever be correct? The resolution is in the note itself: typed callables are correct for *recurring* operations where the input/output shape is known; ad hoc prompts are correct for novel, one-off, or shapeless requirements. Expressiveness doesn't determine correctness — fitness to context does. Consistent. ✓

*"The prompt layer is where new requirements get absorbed without changing the base" vs. the examples*

All three examples (CI pipeline check, codebase review criterion, deployment safety check) assume the agent already has the relevant capabilities (can read logs, can read code, can check state). None requires a new tool or API. The claim is consistently illustrated within the implicit constraint of "existing capability surface." Consistent. ✓

*"Typed callables sit at the other end" (of the spectrum) vs. enforcement gradient "instructions → skills → hooks → scripts"*

INFO — the gradient has typed callables under "skills" (second position), but the note says they sit at the "other end," implying they're at the scripts end. The gradient actually has hooks and scripts as tighter than skills. This is a positional ambiguity within the spectrum framing: typed callables are at the other end of the *ad hoc vs. formal* dimension, but not at the tightest end of the *enforcement* dimension. These are two overlapping but distinct axes. The note conflates them slightly.

*"Ad hoc instructions sit at the loosest end... zero validation and zero reuse" vs. "Prompts carry judgment that type signatures can't express"*

These are consistent: "zero validation and zero reuse" is a cost; "carries judgment" is a benefit. The note is comparing expressiveness (benefit) vs. reliability/reuse (cost). Both are real. No contradiction. ✓

**Definition drift**

"Ad hoc prompt" — used consistently to mean a markdown/natural language instruction written for a specific context, not extracted or formalized. ✓

"Schema change" — implicitly "change to the deterministic base (code, schemas, APIs)." Consistent across all examples. ✓

"Skill" — used consistently as the formalized, extracted form of a recurring ad hoc prompt. ✓

**Summary/body mismatch**

No explicit compressed summary section. The opening paragraph serves as a thesis statement and is consistent with the body. ✓

---

One INFO (typed callables positioned at "the other end" of the spectrum, conflating the ad-hoc/formal axis with the enforcement-tightness axis). No WARNs.
