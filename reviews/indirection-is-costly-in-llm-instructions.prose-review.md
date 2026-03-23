=== PROSE REVIEW: indirection-is-costly-in-llm-instructions.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The note states "the LLM occasionally gets it wrong: forgetting to substitute, mangling a path, or applying the wrong value" as established fact, but no source or evidence is cited for the frequency or nature of these failures. The opening also asserts the cost model as "fundamentally different" without hedging — this is plausible but is the note's own framework, not a cited finding. Similarly, "Every token competes for context" and the claim that variable substitution requires the LLM to "maintain the mapping in working memory, recognise substitution sites, perform the replacement mentally" presents a specific cognitive model of LLM processing as given, when it is the note's own proposed decomposition.
  Recommendation: Flag the interpretive-overhead decomposition as a proposed model ("plausibly requires..." or "we can model this as..."). The error claim could be strengthened with a link to a concrete example or weakened to "anecdotally."

INFO:
- [Source residue] The note's claimed scope is LLM instructions generally, but the example section ("KB skill portability") and several body references are specific to this project's KB extraction work. Terms like "`kb/instructions/`", "`$CLAW_ROOT/notes/`", and "KB extraction planning" are domain-specific. However, these appear in a clearly labeled "Example" section and the body uses them illustratively, so the framing is adequate. The one borderline case is the opening paragraph's "`kb/notes/`" and "`CONFIG["root"] + "/notes/"`" — these use this project's own paths as the illustrative contrast rather than generic examples, which slightly narrows the feel of a general-principle note.
- [Proportion mismatch] The core claim — that indirection costs interpretation overhead in LLM instructions — is established in the first three paragraphs (~170 words for the mechanism, ~80 words for the bullet list, ~50 words for the fix). The "Where the boundary is" section (~120 words) and "Example" section (~80 words) are appropriately sized relative to the core. No significant mismatch, but the mechanism section could benefit from slightly more development given that it is the load-bearing argument — the decomposition into "maintain mapping, recognise substitution sites, perform replacement, act on result" is asserted in a single sentence and could carry more weight.

CLEAN:
- [Pseudo-formalism] No formal notation, variables, or mathematical apparatus present. The note uses prose throughout. Clean.
- [Orphan references] No specific figures, percentages, named studies, or empirical claims appear without context. The note stays at the level of reasoning rather than citing data. Clean.
- [Unbridged cross-domain evidence] The note draws an explicit analogy between programming (CPU indirection cost) and LLM instructions, and the contrast is the point of the note — it explains *why* the cost model differs rather than assuming transfer. The compiled-languages analogy ("resolve at build time") is framed as a parallel strategy, not as evidence. Clean.
- [Redundant restatement] Each section opens with new material. The "Where the boundary is" section does not re-explain the cost model; it immediately addresses scope limits. The "Example" section introduces a concrete case without restating the principle. Clean.
- [Anthropomorphic framing] The note uses "the LLM" with verbs like "reads," "maintain... in working memory," "recognise," "perform the replacement mentally," and "forgetting." These carry anthropomorphic connotations ("working memory," "mentally," "forgetting"), but in this note they are doing deliberate explanatory work — the note is arguing that these operations are analogous to cognitive tasks and therefore costly. The framing is intentional rather than careless. Clean, though borderline — a reader could reasonably flag "mentally" and "forgetting" as implying human-like processing.

Overall: 1 warning, 2 info
===
