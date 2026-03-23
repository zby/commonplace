=== SEMANTIC REVIEW: why-notes-have-types.md ===

Claims identified: 12

1. "The type system serves six distinct roles" (opening line) -- enumeration: exactly six
2. Navigation: "Types give agents structural hints before opening documents" -- causal
3. Metadata enforcement: "The type system enforces metadata that navigation depends on" -- causal/dependency
4. Verification: "Types must assert verifiable structural properties, not subject matter" -- definition/scope
5. Extensibility: "Directory-scoped types are cheaper than global types" -- causal/comparative
6. Output quality: "Types don't just organise -- they shape what gets written" -- causal
7. Output quality sub-claim: "three independent arguments" -- enumeration of exactly three
8. "The arguments are independent and complementary. Each stands alone; together they cover the full chain: the LLM might reason better, the output will be shaped better, and the human reader can evaluate it better" -- scope claim ("the full chain")
9. Maturation: "Content starts as text ... and gains type information as it develops -- gradual typing applied to documents" -- definition/analogy
10. Maturation: "This mirrors the broader constraining pattern: practices start stochastic and harden as they prove out" -- analogy/causal
11. Free-form not enum: "The type field is a string, not validated against a list. This is deliberate" -- design claim with three reasons
12. "Nothing breaks if a type is wrong or novel" -- scope claim ("nothing")

WARN:
- [Completeness] The six roles are presented as the complete set ("serves six distinct roles"), but the note itself contains a seventh functional role -- "Why free-form, not enum" -- which describes a design property (tolerance/flexibility) that is not reducible to any of the six. Tolerance of misclassification is not navigation, not enforcement, not verification, not extensibility, not output quality, and not maturation. It is a distinct design property: graceful degradation. The note implicitly treats it as a subsection rather than a role, but structurally it is doing the same work as the other six sections -- justifying a design choice in the type system. A reader relying on "six roles" as the complete inventory would miss this.

- [Completeness] Boundary case: communication between humans. The six roles are framed around agent needs (navigation, enforcement for agents, verification by scripts/agents, extensibility for agents, output quality for LLMs, maturation as gradual typing). But types also serve a human-to-human communication role -- a contributor scanning a directory listing can use type labels to orient themselves without opening files, and types signal editorial intent ("I claim this is a structured argument, not a sketch"). This is adjacent to the Navigation role but not identical: Navigation is specifically about stateless agents making routing decisions, while human orientation happens via different mechanisms (scanning, recognition, editorial convention). The six roles may undercount by being agent-centric.

- [Completeness] The "full chain" claim for the three output quality arguments -- "the LLM might reason better, the output will be shaped better, and the human reader can evaluate it better" -- presents this as covering the complete chain from production to consumption. Boundary case: what about the *maintenance* stage? A structured note is easier to update, split, or merge than an unstructured one, because the sections provide stable handles for editing. This falls between "output will be shaped better" (which describes initial writing) and "human reader can evaluate it better" (which describes reading). The maintenance benefit is plausible but not clearly covered by any of the three arguments as stated.

INFO:
- [Grounding] The Maturation section claims this pattern "mirrors the broader constraining pattern: practices start stochastic and harden as they prove out," linking to methodology-enforcement-is-constraining.md. That note's domain is methodology enforcement (instructions, skills, hooks, scripts), not document types. The parallel is reasonable -- both involve gradual hardening -- but the source note explicitly draws the analogy itself ("document type maturation ... follows the same gradual-typing pattern as methodology maturation"), so the attribution is self-reinforcing rather than independently grounded. The note is on solid ground citing the parallel, but a reader might mistake this for an established independent principle rather than two notes citing each other.

- [Internal consistency] The Verification section says "Types must assert verifiable structural properties, not subject matter," and the Extensibility section says "the global layer stays thin (text and note)." But `note` is the base type that, per the linked document-types-should-be-verifiable.md, "makes no structural claim -- like Any in a gradually typed language." If types should assert verifiable structural properties, and `note` asserts no structural property beyond "has frontmatter," then `note` satisfies the verification principle only trivially. This is not a contradiction -- the note accommodates this via the maturation gradient -- but the Verification section's strong "must assert verifiable structural properties" is in tension with the Extensibility section's acceptance that most documents will be typed `note`, which asserts almost nothing structural. The tension is acknowledged in the linked source but not in this note.

- [Completeness] The "Why free-form, not enum" section gives three reasons (new domains, user adaptation, tolerance of fuzziness). Boundary case: what about migration cost? Even if the three reasons were absent, a free-form string is cheaper to change than an enum because no code needs updating when a value is added. This is an engineering reason distinct from the three given, though it could be folded into "new domains" with some strain.

PASS:
- [Grounding] Navigation section accurately attributes its claim to types-give-agents-structural-hints-before-opening-documents.md. The source develops the same claim with the same examples (spec, structured-claim, index) and the same framing (stateless agents, finite context). No vocabulary or scope mismatch.
- [Grounding] Metadata enforcement section accurately reflects type-system-enforces-metadata-that-navigation-depends-on.md. The source's central claim -- descriptions exist because the note base type requires them, and without enforcement the KB degrades -- is faithfully represented. The dependency relationship (enforcement enables navigation) is correctly stated.
- [Grounding] Verification section accurately reflects document-types-should-be-verifiable.md. The source's verifiability principle, the "design note" counter-example, and the verification gradient are all faithfully represented.
- [Grounding] Extensibility section accurately reflects directory-scoped-types-are-cheaper-than-global-types.md. The economic argument (global types tax every session; directory types load on demand) and the thin global layer proposal are faithfully represented.
- [Internal consistency] The six sections are internally consistent with each other. Navigation depends on enforcement (stated correctly), verification shapes what types can be (consistent with navigation claims), extensibility manages the cost of the type vocabulary (consistent with verification's structural requirement), output quality operates through a different mechanism than navigation (no confusion between the two), and maturation provides the temporal dimension. No pairwise contradictions found.
- [Internal consistency] The "Why free-form, not enum" section is consistent with the Extensibility section. Both argue for lightweight, locally extensible type definitions. The free-form design enables the directory-scoped extension model.

Overall: 3 warnings, 3 info
===
