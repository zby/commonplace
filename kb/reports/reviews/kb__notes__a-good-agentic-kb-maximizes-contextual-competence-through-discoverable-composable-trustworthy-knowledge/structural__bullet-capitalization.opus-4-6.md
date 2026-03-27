WARN

Thirteen of the sixteen Relevant Notes bullets begin with lowercase link text. The gate skips items that intentionally begin with code tokens or identifiers, but the inconsistency within this note's own list makes the lowercase hard to read as uniformly intentional.

**Lowercase-start bullets in Relevant Notes:**

```
- [context efficiency is the central design concern](...)
- [claw learning loops must improve action capacity not just retrieval](...)
- [constraining](...)
- [distillation](...)
- [discovery is seeing the particular as an instance of the general](...)
- [first-principles reasoning selects for explanatory reach](...)
- [constraining and distillation both trade generality for compound](...)
- [learning is not only about generality](...)
- [a knowledge base should support fluid resolution-switching](...)
- [title as claim enables traversal as reasoning](...)
- [files beat a database](...)
- [design methodology — borrow widely, filter by first principles](...)
- [sift-kg](...)
```

**Uppercase-start bullets in the same list (for contrast):**

```
- [Siftly](...)
- [Agentic Note-Taking 23: Notes Without Reasons](...)
```

The three uppercase-start entries are proper nouns (`Siftly`) or titled external sources (`Agentic Note-Taking 23`). The rest use prose-style link text that reads as sentence fragments ("a knowledge base should support..." should start as "A knowledge base should support...").

Single-word lowercase entries (`[constraining]`, `[distillation]`, `[sift-kg]`) are borderline — they're close enough to identifiers that they could be skipped. The multi-word, space-separated entries like `[a knowledge base should support fluid resolution-switching]` are clearly prose fragments and should be capitalized.

**Recommendation:** Capitalize the first word of multi-word space-separated link texts in the Relevant Notes list: `[Context efficiency is the central design concern]`, `[A knowledge base should support fluid resolution-switching]`, etc. Single-word and hyphenated entries can remain lowercase as identifiers.

Body-embedded links (within prose sentences) are correctly lowercase and should not be changed — those are intentionally lowercase as part of running text.
