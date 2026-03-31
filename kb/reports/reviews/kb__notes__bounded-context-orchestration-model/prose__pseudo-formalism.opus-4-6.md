**WARN** — 1 instance

**`||P||_t ≤ M` notation.** The variables `K`, `t`, `M`, and the cost measure `||P||_t` are introduced with norm-like notation, but `||·||` is explicitly defined as "not a universal size metric" — it depends on task type, compositional difficulty, and unspecified further factors. No quantitative prediction or non-obvious derivation follows from writing `||P||_t ≤ M` rather than the prose statement "the prompt must fit the context budget, where cost depends on task difficulty." The subscript `_t` compactly signals task-dependence, but the same point is immediately restated in prose ("the cost measure absorbs task difficulty, while M stays fixed"). Mentally deleting the notation and re-reading the passage: clarity is unchanged.

The pseudocode blocks (`while not satisfied(K): ...` and the note-selection example) are genuinely more precise than prose — they make the loop structure, state accumulation, and function signatures explicit. These pass.
