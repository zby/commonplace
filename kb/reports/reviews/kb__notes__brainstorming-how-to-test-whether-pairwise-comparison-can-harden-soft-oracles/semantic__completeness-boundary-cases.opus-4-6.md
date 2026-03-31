The note presents a three-level test ladder (judgment quality, ranking quality, loop-improvement quality), four hardening criteria, five failure modes to rule out, and explicit falsification conditions.

---

**Framework: Three-level test ladder**

- Simplest: Test 1 (offline pairwise vs. scalar agreement with human labels). ✓
- Most extreme: Test 3 (optimization loop comparison — does pairwise selection improve final output quality?). ✓
- Between: Test 2 (ranking quality from aggregated pairwise judgments). ✓
- The ladder structure is explicit: "Each step asks a stricter question than the one before it." Clean progressive design. ✓

**Four hardening criteria** (discrimination, variance, optimization utility, bias behavior). These are well-defined and measurable. ✓

**Five failure modes** (format effect, cost masking, bias trade, overfitting, tournament illusion). Each is specific and addresses a different false-positive risk. ✓

**Falsification conditions** — five concrete outcomes that would count against the thesis. Excellent for a hypothesis-testing note. ✓

**Good/poor benchmark choices** — explicitly reasoned. ✓

No WARN, no INFO. Exceptionally thorough experimental design note.
