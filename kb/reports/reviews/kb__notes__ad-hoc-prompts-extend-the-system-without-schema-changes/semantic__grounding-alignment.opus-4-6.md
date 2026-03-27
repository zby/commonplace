The note's central causal chain: ad hoc prompts absorb requirements without schema changes because (a) the system has two strata and (b) the prompt layer is homoiconic with content. I trace the major citations.

---

**Claim: instructions → skills → hooks → scripts as the enforcement gradient**

Cited to [methodology-enforcement-is-constraining.md] as "foundation: the gradient from instructions to scripts." The note uses this gradient to position ad hoc prompts at the loosest end. Attribution seems correct per the link semantics. ✓

**Claim: typed callables sit at the "other end" of the spectrum**

Cited to [instructions-are-typed-callables.md] as "the typed end of the spectrum: skills should declare signatures." The note contrasts ad hoc instructions (untyped, zero infrastructure) with typed callables (declared signatures, validated inputs). The contrast is presented as one dimension of the same gradient, with typed callables at the far end. INFO — the enforcement gradient ends at "scripts," but typed callables are classified under "skills" (second in the gradient), not at the script end. The note treats typed callables as the maximally constrained form, but the gradient it cites has hooks and scripts as tighter still. The positioning is slightly misaligned with the cited source's structure.

**Claim: "lowest-friction capture, then progressive refinement" applied to the skill layer**

Cited to [wikiwiki-principle-lowest-friction-capture-then-progressive-refinement.md]. The claim is that writing ad hoc prompts first, then extracting skills, is this principle applied to a new domain. This is an analogy: the wikiwiki principle says "capture first, refine later"; the current note applies it to skill development. The citation is used as a grounding analogy, not a direct application. ✓ — the scope is appropriate.

**Claim: "the extraction step itself is distillation"**

Cited to [skills-derive-from-methodology-through-distillation.md]. The note says the extraction from ad hoc prompt to skill is distillation — keeping the procedure, factoring out the discursive reasoning. Attribution seems correctly scoped. ✓

**Claim: "the sub-agent inherits nothing beyond what the caller explicitly passed" / sub-agent provides a lexically scoped frame**

Cited to [llm-context-is-composed-without-scoping.md] as "grounds: ad hoc instructions notes are effective sub-agent interfaces because they provide lexically scoped frames."

INFO — scope mismatch. The cited note's argument (per its use elsewhere in the KB) is that LLM context *lacks* scoping — you cannot selectively isolate what a model sees. The current note cites it as grounding for the *positive* claim that ad hoc prompts provide clean sub-agent scoping. The logical connection exists: because context has no internal scoping mechanism, the only reliable scope boundary is the lexical edge of the sub-agent's prompt (what the caller writes is what the sub-agent sees). But the cited note grounds the problem (no scoping), not the solution (caller-controlled boundary as substitute). The inference is valid but the citation implies a more direct grounding relationship than the source provides.

**Claim: homoiconicity is why ad hoc extension works**

Cited to [llm-context-is-a-homoiconic-medium.md]. The claim: instructions and content share the same representation, enabling a markdown file to be both readable content and executable instruction. Per the link description "mechanism: because LLM context is homoiconic." This seems correctly cited as the mechanism enabling the phenomenon. ✓

---

One INFO about typed-callable positioning relative to the enforcement gradient, one INFO about [llm-context-is-composed-without-scoping.md] grounding a positive claim from a negative premise. No WARNs.
