The note presents one framework: a test pyramid for text artifacts (deterministic, LLM rubric, corpus compatibility).

---

**Framework: Test pyramid**

Grounding: "Text artifacts can be tested like software if you define contracts per document type."

- Simplest: a deterministic check (is the description field present?). ✓
- Most extreme: a corpus-level contradiction check across all notes. ✓
- Between: an LLM rubric check (does this note have a single clear thesis?). The middle layer is well-positioned between deterministic and corpus. ✓
- Adjacent: **temporal tests** (has this note drifted from its original claim? is it still current?). Not addressed but outside scope for a note that hasn't been built yet.
- Adjacent: **prompt testing vs. artifact testing**. The note explicitly distinguishes these: "testing the prompt (will it produce good notes?) and testing the artifact (is *this* note good?)." ✓

The note is brief and explicitly aspirational ("We haven't built any of this yet"). The framework's boundary cases are limited by the note's brevity, but the principle "build contracts from real failures" defers boundary-case identification to practice.

No WARN, no INFO. Clean for a concise forward-looking note.
