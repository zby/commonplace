## prose/pseudo-formalism

**Result: WARN**

Three pieces of notation in the note:

1. **Pipeline diagram** (line 33):
   ```
   Spec → choose interpretation → execute on input → output
   ```
   The surrounding prose already says "A natural-language spec admits multiple valid programs. The LLM picks one." The diagram adds "execute on input → output" — which is implicit and obvious. Mentally deleting the diagram leaves the passage equally clear. This is decorative notation: it restates the prose in arrow form without enabling prediction or derivation.

2. **Boundary diagram** (lines 69–71):
   ```
          LLM           →        Tool          →        LLM
   underspecified + indeterministic   precise + deterministic   underspecified + indeterministic
   ```
   This earns its space. It compactly shows the oscillating property profile across boundary crossings — a pattern that would take multiple sentences to convey in prose. The visual layout makes the symmetry immediately legible.

3. **Constraining/relaxing spectrum** (lines 90–91):
   ```
   Underspecified ——constrain——> Precise
   Underspecified <——relax——— Precise
   ```
   Borderline. The bidirectionality is the point, and the diagram makes it visually immediate. But the definitions in the preceding paragraphs already state both directions clearly. Marginal added value.

**Instance 1** is the clearest case of pseudo-formalism. Consider removing it or replacing it with a one-sentence restatement that adds the execution step ("The LLM projects the spec to a concrete program, then executes it on the input"). Instance 3 is marginal.
