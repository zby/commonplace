## prose/bridge-paragraph-duplication

**Result: PASS**

Checked every section boundary for preview-then-enumerate duplication:

- **Before "Spec-to-Program Projection"**: The preceding subsection ends with "The indeterminism lets you avoid that question by explaining everything as noise." This discusses indeterminism's masking effect — it does not preview the projection model. No duplication.

- **Before "Narrowing the Interpretation Space"**: "This reframes prompt engineering: it's about narrowing the space of valid interpretations, not debugging a fixed program." One sentence that names the concept. The section then enumerates specific mechanisms (system prompts, few-shot, schemas, temperature). The transition is a pivot, not a preview of the enumeration. Passes the gate's one-sentence exception.

- **Before "Boundaries"**: "So real systems don't just manage underspecification within LLM components — they manage the transitions between LLM and code." One sentence shifting scope. The section then develops the boundary model with a diagram and crossing rules. No duplication.

- **Before "Constraining and Relaxing"**: "But boundaries aren't fixed. As systems evolve, logic moves across them." Two sentences. The section introduces constrain/relax as specific operations with definitions, benefits, and examples — substantially more than what the transition previews.

- **Before "Testing and Debugging"**: "The system breathes." Metaphor, not a preview.

- **Before "Design Implications"**: The debugging section ends with diagnostic advice. No preview of the implications list.

No bridge-paragraph duplication found.
