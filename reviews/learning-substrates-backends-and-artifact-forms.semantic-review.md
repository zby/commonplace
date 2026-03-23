=== SEMANTIC REVIEW: learning-substrates-backends-and-artifact-forms.md ===

Claims identified: 12

1. "Weights," "tips," and "repo artifacts" name things at three different levels (substrate class, artifact form, storage backend). [Opening paragraph]
2. The primary split is substrate class: subsymbolic vs symbolic artifact. [Section: intro enumeration]
3. Subsymbolic substrate — the learned result lives in model parameters or other latent state. [Enumeration item 1]
4. Symbolic artifact substrate — the learned result lives in discrete, inspectable symbolic objects. [Enumeration item 2]
5. Symbolic artifacts can live in different backends without changing substrate class. [Backend section]
6. "Repo artifacts" is too narrow as the umbrella term for the symbolic artifact substrate. [Backend section]
7. Within the symbolic artifact substrate, systems can produce many different artifact forms — tips, notes, reflections, rules, prompts, schemas, tests, playbooks, ranked memories. [Artifact form section]
8. These artifact forms differ in granularity, retrieval mode, and how directly they constrain later behavior, but they belong to one family. [Artifact form section]
9. The three-level split prevents category mistakes that keep recurring in comparisons across this KB. [Why the distinction matters]
10. Files-not-database is a claim about which backend to pick within the symbolic artifact substrate, not about whether to use symbolic artifacts at all. [Why the distinction matters]
11. Subsymbolic learning usually buys tighter optimization and gives up inspectability. [Final paragraph]
12. Symbolic artifact learning usually buys inspectability, diffability, and composability, while depending more heavily on retrieval design, lifecycle management, and governance. [Final paragraph]

---

WARN:
- [Completeness] The two-item substrate enumeration (subsymbolic / symbolic artifact) claims to be "the primary split," but hybrid-substrate systems are not accounted for. AgeMem is described in the companion note (memory-management-policy-is-learnable-but-oracle-dependent.md) as a "split substrate" — facts in a symbolic store, policy in weights. The taxonomy table in this note lists AgeMem as purely "Subsymbolic" with backend "Model parameters," which is inaccurate per the KB's own analysis. The companion note explicitly says: "AgeMem accepts a substrate split: facts go into a memory store (somewhat inspectable key-value pairs), but the policy for managing them goes into model weights." If the primary split is binary, hybrid cases must be addressed — either as belonging to one side, or as a third category. Currently the table forces a clean assignment that the KB's own evidence contradicts.

- [Grounding alignment — scope mismatch] The note claims AgeMem is a "clean example" of the subsymbolic substrate class. The companion note (memory-management-policy-is-learnable-but-oracle-dependent.md) uses the same phrase — "the clean weight-side case" — but then spends an entire section ("How it stores what it learns: split substrate") explaining that AgeMem is actually a split case with facts in a somewhat inspectable key-value store and only the policy in weights. The "clean example" characterization in this note overstates the simplicity that the cited source itself qualifies.

- [Completeness] The note's artifact-form list ("tips, notes, reflections, rules, prompts, schemas, tests, playbooks, ranked memories") is presented as illustrative but uses phrasing ("many different artifact forms") that implies broad coverage. A boundary case that strains the "symbolic artifact" framing: learned retrieval indexes, embedding databases, or compiled code. A vector embedding derived from symbolic artifacts is not itself inspectable in the way tips or rules are, yet it is durable and changes future behavior. If a system learns by building a FAISS index from its notes, the index is neither a subsymbolic weight nor a "discrete, inspectable symbolic object." The note's two-class split has no place for derived computational artifacts that lose inspectability while remaining non-parametric.

INFO:
- [Completeness] The note claims backend and artifact form are "separate axes," which implies a full combinatorial space. But some combinations may be incoherent or impractical. For instance, can "tests" (an artifact form) live in a "vector store" (a backend)? The note does not need to enumerate all valid combinations, but the claim that these are independent axes would be stronger with an acknowledgment that not all cells in the cross-product are occupied or meaningful.

- [Grounding alignment — domain coverage] The note cites "inspectable substrate, not supervision, defeats the blackbox problem" to ground "the core benefit of the symbolic artifact side is inspectability." The cited note (inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) argues specifically about codification — LLM-generated code, prompts, schemas — and the argument depends on those artifacts being not just inspectable but also testable and diffable. This note generalizes "inspectability" to the entire symbolic artifact substrate, including artifact forms like "ranked memories" or "reflections" that may be inspectable (you can read them) but not testable or diffable in the same actionable sense. The grounding covers the core claim but the generalization to all artifact forms is the note's own move.

- [Internal consistency] The table lists "Commonplace constraining" with artifact forms "Prompts, rules, schemas, tools, tests." The artifact-form section lists "tips, notes, reflections, rules, prompts, schemas, tests, playbooks, ranked memories." These two lists partially overlap but are not consistent — the section list includes "notes," "reflections," "playbooks," and "ranked memories" which are absent from the table's Commonplace row, while the table includes "tools" which is absent from the section list. This is not a contradiction (the table is illustrative, not exhaustive), but it could create confusion about whether the note considers "tools" an artifact form or not.

- [Completeness] The "or other latent state" qualifier in the subsymbolic substrate definition opens the category beyond model parameters but is not elaborated. What other latent state qualifies? Learned retrieval embeddings? Cached activations? Without examples, this qualifier is a loose end that could encompass almost anything non-symbolic.

PASS:
- [Grounding alignment] The note claims "Files beat a database for agent-operated knowledge bases argues that a database schema forces premature commitment to access patterns — a claim about which backend to pick within the symbolic artifact substrate." The source note (files-not-database.md) confirms this: its argument is explicitly about storage choice ("files as source of truth, derived indexes for capabilities files alone can't provide") and never claims files are the only way to do symbolic learning. The re-framing is accurate.

- [Grounding alignment] The note cites Cognee as a counterexample showing "database-backed symbolic artifacts show that files are not the only artifact backend." The Cognee review confirms this: "Databases are the primary substrate, not a derived layer" and its DataPoints are Pydantic models — discrete, inspectable symbolic objects stored in a poly-store. The attribution is accurate.

- [Grounding alignment] The note cites "continuous learning requires durability, not weight updates" as foundation for the claim that non-weight adaptation counts as learning. The source note makes exactly this argument, grounded in Simon's definition: "learning is any change that produces a more or less permanent change in a system's capacity for adapting to its environment." The dependency is clean.

- [Internal consistency] The note's core conceptual structure — substrate class as the primary split, with backend and artifact form as independent downstream choices — is maintained consistently throughout. The opening paragraph defines the three levels, each section elaborates one level, the "why it matters" section applies the framework, and the table demonstrates it. No definition drift detected in the key terms.

- [Internal consistency] The trade-off summary in the final paragraph ("Subsymbolic learning usually buys tighter optimization and gives up inspectability. Symbolic artifact learning usually buys inspectability, diffability, and composability") is hedged with "usually" and does not contradict anything in the body. The hedge is appropriate given the hybrid cases discussed in linked notes.

Overall: 3 warnings, 4 info
===
