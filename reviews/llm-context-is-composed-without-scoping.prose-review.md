=== PROSE REVIEW: llm-context-is-composed-without-scoping.md ===

Checks applied: 8

WARN:
- [Proportion mismatch] The core claim is that LLM context lacks scoping. The section that carries the most weight for this claim is the opening + the three pathologies (spooky action at a distance, name collision, inability to reason locally), which together run roughly 200 words. The "Sub-agents as the scoping mechanism" section (~200 words) and "Undeveloped directions" section (~300 words, dominated by the ConvexBench paragraph) each match or exceed it. The "Undeveloped directions" section — which is explicitly flagged as not yet having concrete examples — is the longest single section in the note, with the ConvexBench recursion paragraph alone running ~150 words. The speculative material outweighs the established argument.
  Recommendation: Trim the ConvexBench paragraph in "Undeveloped directions" to its essential claim (flat accumulation destroys compositional reasoning; clean frames recover it) and move the detailed numbers to a parenthetical or footnote. Alternatively, promote "Recursion with clean frames" to its own note where the empirical evidence can be developed fully, and link from here.

- [Confidence miscalibration] The "Undeveloped directions" header signals speculation, but the ConvexBench paragraph inside it switches to assertive language: "provides direct empirical validation," "confirms the prediction." If the direction is undeveloped, the empirical result should be framed as preliminary support, not confirmation. The tension is between the section framing ("don't yet have concrete examples") and the paragraph's actual content (a detailed concrete example with specific F1 numbers).
  Recommendation: Either move the ConvexBench material out of "Undeveloped directions" (since it IS a concrete example, contradicting the section's own claim) or relabel the section to reflect that some directions now have evidence while others remain speculative.

INFO:
- [Source residue] The programming-language analogy (dynamic scoping, lexical scoping, Lisp, Scheme, Common Lisp, hygienic macros, tail-call optimisation, stack unwinding, condition/restart systems) is pervasive and deliberate — the note's thesis IS the analogy. However, a few terms assume PL fluency without gloss: "special variable" (line 29: "dynamic binding of a `*tone*` special variable"), "hygienic macros" (line 35: "the same problem Scheme's hygienic macros solve"), "tail-call optimisation" (line 86), and "condition/restart systems" (line 89). A reader who knows LLM systems but not Lisp would lose the thread at these points.
  Recommendation: Worth checking whether the target audience is assumed to know PL theory. If not, one-sentence glosses for "special variable," "hygienic macros," and "condition/restart" would prevent the analogy from becoming opaque.

- [Anthropomorphic framing] Line 17: "the model conflates them" — "conflates" implies a cognitive act of confusion. The mechanism is closer to attention-weighted token similarity failing to disambiguate. This is minor because the note is generally precise about mechanism vs. agency.
  Recommendation: Consider "the model merges them" or "the model fails to disambiguate them" if precision matters here.

CLEAN:
- [Pseudo-formalism] No formal notation, equations, or symbolic apparatus appears. The structural parallel in the bullet list (lines 22-25) is prose, not formalism. Clean.
- [Orphan references] The one specific empirical claim (ConvexBench F1 numbers: 1.0 at depth 2, ~0.2 at depth 100, 5,331 tokens) is cited with author, year, and a link to the source snapshot. The Anthropic source is similarly cited with URL. Clean.
- [Unbridged cross-domain evidence] The PL-to-LLM transfer is the note's central thesis and is explicitly argued throughout — the note explains WHY dynamic scoping pathologies apply (flat concatenation, global visibility, no stack). The ConvexBench evidence is from LLM experiments applied to LLM claims — same domain. No unbridged transfers found. Clean.
- [Redundant restatement] Sections are distinct and progressive: pathologies -> benefits of flatness -> capture problem -> within-frame hygiene -> sub-agents as solution -> return value problem -> existing implementations -> undeveloped directions. No section re-explains a prior section's conclusion. Clean.

Overall: 2 warnings, 2 info
===
