=== PROSE REVIEW: legal-drafting-solves-the-same-problem-as-context-engineering.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The note asserts "The parallel is not metaphorical" in its opening paragraph, then throughout treats the mapping as structural identity rather than strong analogy. Whether the legal and LLM domains share the same problem or merely isomorphic problems is itself a substantive philosophical claim, but the note presents it as obvious fact. Similarly, "This is the exact structure of the underspecified instructions framing" asserts identity without qualification. The note's own open questions section implicitly acknowledges the mapping is partial (e.g., "Does the common law / civil law distinction map to anything?"), which undercuts the categorical framing in the opening.
  Recommendation: Soften the identity claim to "structural" or "non-trivial" parallel rather than asserting it is "not metaphorical." The note's actual content supports a strong structural analogy — it does not need to overclaim into identity to be compelling.

- [Confidence miscalibration] The table in "Techniques that transfer" presents six mappings as established correspondences with no hedging. Some are tight (defined terms -> glossaries), but others are loose (precedent -> "constrained conventions, few-shot examples" conflates two quite different mechanisms). The table format itself implies clean one-to-one mappings where the actual relationship is messier.
  Recommendation: Add a sentence before or after the table acknowledging that the mappings vary in tightness, or annotate the looser ones. Alternatively, a brief caveat column would preserve the table's utility while calibrating confidence.

- [Proportion mismatch] The section "Law is rich in constraining but largely lacks codification" is substantially longer than "The structural parallel," which carries the note's core claim (the title). The constraining/codification mapping is a secondary consequence of the main parallel, yet it receives the most detailed treatment — likely because the vocabulary-mapping exercise was easier to develop than the structural argument itself.
  Recommendation: Develop "The structural parallel" further (e.g., spell out what makes the parallel structural rather than metaphorical — shared formal properties, not just surface similarity), or extract the constraining/codification analysis into a separate note that this one links to.

WARN/INFO:
- [Pseudo-formalism] Not formal notation, but the note uses quasi-technical phrasing that functions similarly: "projected onto a concrete outcome by a processor that selects one interpretation from the space the spec admits." This phrase appears in both the opening and the "structural parallel" section, doing the work of a definition without being presented as one. It reads as precise but is actually metaphorical — "projection" and "space" are spatial/mathematical terms used loosely.
  Recommendation: Either define these terms explicitly (what constitutes the "space"? what operation is "projection"?) or use plainer language. The argument doesn't need the apparatus — "a judge resolves ambiguity by choosing one reading" is equally clear.

INFO:
- [Source residue] The note was prompted by "a social media post observing that context engineering is close to law." The framing is clean — legal vocabulary is appropriate since law IS the subject. However, the phrase "claws are a kind of software system" in the "Why this matters" section appears to be a typo or autocorrect artifact for "CLAs" or "LLMs" or possibly "Claude" — it doesn't match any term used elsewhere in the note or the KB vocabulary.
  Recommendation: Verify what "claws" was intended to mean and correct. This is likely a transcription error rather than source residue, but it disrupts the reader.

- [Redundant restatement] The opening paragraph of "Why this matters for knowledge system design" partially restates the structural parallel ("law operates in natural language — the actual medium of prompts and knowledge bases") which was already established in the opening and in "The structural parallel." The restatement is brief enough (one sentence of setup) that it functions as a transition, but it is the third time the reader encounters this point.
  Recommendation: Borderline — the restatement is short and serves a transitional purpose. If trimming, replace with a forward reference: "Given that law works in the same medium as prompts (established above), it offers..."

CLEAN:
- [Source residue] Despite originating from a social media observation, the note's framing is appropriately general. Legal vocabulary is used because law is the subject, not because it leaked from an unacknowledged source domain. The note correctly positions legal drafting as a source discipline rather than importing legal jargon unreflectively.

- [Orphan references] No unattributed specific figures, data points, or named studies appear. The ABC reference is properly sourced via link. The "centuries of methodology" claim is a general characterization, not a specific empirical assertion requiring citation.

- [Unbridged cross-domain evidence] The note's entire thesis IS about cross-domain transfer, and it explicitly argues for why the transfer is valid (shared structural properties: natural language spec, judgment-exercising interpreter, irreducible ambiguity). The bridge is the note's core argument rather than something omitted. The ABC case study is properly framed as independent validation rather than direct evidence.

- [Anthropomorphic framing] The note avoids attributing mental states to LLMs. It describes LLMs as "processors exercising judgment" — which could be read as anthropomorphic, but the note explicitly parallels this with judges, making "judgment" a functional descriptor (selecting among valid interpretations) rather than a cognitive claim. The framing is deliberate and consistent.

Overall: 3 warnings, 2 info
===
