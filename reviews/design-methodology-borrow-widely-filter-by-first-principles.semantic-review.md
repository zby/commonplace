<!-- REVIEW-METADATA
note-path: kb/notes/design-methodology-borrow-widely-filter-by-first-principles.md
last-full-review-note-sha: 26d97df3e874dd729ee718f8a554db6c4318e297
last-full-review-note-commit: 5d0771d0710a683a620be574bcc3f3b86bbdb60b
last-full-review-at: 2026-03-23T09:32:55+01:00
last-accepted-note-sha: 26d97df3e874dd729ee718f8a554db6c4318e297
last-accepted-note-commit: 5d0771d0710a683a620be574bcc3f3b86bbdb60b
last-accepted-at: 2026-03-23T09:32:55+01:00
last-acceptance-kind: full-review
review-type: semantic-review
-->
=== SEMANTIC REVIEW: design-methodology-borrow-widely-filter-by-first-principles.md ===

Claims identified: 14

1. "Any source is valid" — no source discipline is excluded a priori (The adoption filter)
2. "First principles reasoning is the main filter" — adoption confidence comes from derivation from domain constraints (The adoption filter)
3. Four enumerated first principles: "finite context windows, no import/resolution mechanism, agents reason over text, everything loaded must compete for attention" (The adoption filter)
4. "Programming patterns get a fast pass" — adopted without complete transfer theory (The adoption filter)
5. The fast-pass bet: "agents interpreting prompts are doing something structurally similar to interpreters interpreting programming languages" (The adoption filter)
6. Thalo's convergence is "stronger evidence than any single design argument" (The adoption filter)
7. Legal drafting is "a candidate source — untested" (The adoption filter)
8. "Everything else earns its way in" — non-programming borrowed patterns require first-principles support (The adoption filter)
9. The asymmetry between programming and cognitive science is about "the nature of the target system," not field quality (Why the asymmetry)
10. "Human cognition is associative, embodied, affective. LLM agents process text in a fixed-size window with no persistent state between sessions. The mechanisms are different enough that cognitive science analogies need independent justification" (Why the asymmetry)
11. "Empirical observation is the second strongest source — but weaker than first principles" (Why the asymmetry)
12. Empirical observation "doesn't go through the borrowing/adoption filter at all. It's evidence from this system, not transferred from another domain" (Why the asymmetry)
13. "First principles are scarce... but each one is strong because it's derived from real constraints that won't change" (Why the asymmetry)
14. "Observations accumulate into confidence through repetition; first principles carry confidence immediately" (Why the asymmetry)

WARN:
- [Completeness] The adoption filter presents what reads as four tiers: (1) first-principles derivation, (2) programming fast pass, (3) legal drafting (untested), (4) "everything else." But tier 4 explicitly says "these get adopted when first-principles reasoning supports them" — which is exactly what tier 1 says. The "everything else" tier is not a distinct adoption mechanism; it collapses into tier 1 applied to non-programming domains. The four-tier presentation overstates the framework's dimensionality. There are really three distinct paths: first-principles derivation, programming fast pass (reduced evidential bar), and empirical observation (which the note itself says bypasses the filter entirely). Legal drafting sits between: the note correctly marks it as hypothesis-only and does not claim it as a distinct tier, but its prominent subsection heading gives it visual parity with the others.

- [Completeness] The note enumerates four first principles — "finite context windows, no import/resolution mechanism, agents reason over text, everything loaded must compete for attention" — but uses a fifth in the asymmetry argument: "no persistent state between sessions." Statelessness is load-bearing for the central claim that cognitive science analogies need independent justification ("LLM agents process text in a fixed-size window with no persistent state between sessions. The mechanisms are different enough that cognitive science analogies need independent justification"). If statelessness is a constraint that "won't change" and that shapes design conclusions, it belongs in the enumerated set. Its absence from the enumeration but presence in the argument is a gap — a reader trusting the enumerated list as complete would miss a principle the note itself relies on.

- [Grounding — domain coverage] The note claims "Convergence across independent projects is stronger evidence than any single design argument" and cites Thalo as the sole instance. But the evidence from Thalo — building a compiler for knowledge management — supports the narrower claim that programming patterns transfer to knowledge systems. It does not support the broader claim embedded in the note's argument: that programming patterns deserve a methodological fast pass *over* cognitive science patterns. Thalo did not test cognitive science patterns and reject them in favor of programming ones. The convergence evidence validates one half of the asymmetry (programming transfers) but is presented in the context of the whole asymmetry argument (programming deserves privileged treatment relative to other sources). The note should either narrow the convergence claim to what Thalo actually evidences, or acknowledge that the asymmetry's negative half (cognitive science does not get a fast pass) rests on the mechanistic argument alone, not on convergence.

INFO:
- [Completeness] Boundary case: formal/mathematical reasoning as a source discipline. Mathematics is formal and compositional like programming, but operates on abstract structures rather than text-based interpreter systems. Category theory for composability, information theory for context budgets, and graph theory for link networks are all plausible sources. The note's fast-pass criterion — "bounded processors composing text under constraints" — does not clearly include or exclude mathematics. Math shares the "formal and compositional" properties listed in "Why the asymmetry" but is not "text-based" in the same sense as programming systems. The framework leaves this edge case unaddressed.

- [Completeness] Boundary case: what happens when first principles conflict? The enumerated principles can pull in opposite directions. "Agents reason over text" favors verbose, explicit context; "everything loaded must compete for attention" favors compression. The methodology note provides a filter for adopting ideas (derive from first principles) but no method for resolving tensions between the principles themselves. This is an edge of the framework the note does not address.

- [Grounding] The note states legal drafting is "untested" — "we haven't yet borrowed a concrete technique from law and applied it successfully." The linked legal-drafting note, however, documents a detailed table of six legal techniques with context engineering analogues (defined terms, structural conventions, enumeration, canons of interpretation, precedent, statute codification) and explicitly maps tightness of each analogue. It also discusses ABC (Agent Behavioral Contracts) as independently reinventing legal enforcement patterns. The methodology note's characterization of law as entirely untested is doing work — it distinguishes "identified the conceptual mapping" from "borrowed a technique and validated it in practice" — but this distinction is implicit. The legal-drafting note's detailed mappings suggest the source is more developed than "untested" conveys, even if no technique has completed the full borrow-apply-validate cycle.

- [Internal consistency] The note says "Empirical observation is the second strongest source — but weaker than first principles" and places it in a ranked hierarchy. But two paragraphs later, it says empirical observation "doesn't go through the borrowing/adoption filter at all. It's evidence from this system, not transferred from another domain." If observation bypasses the adoption filter entirely, ranking it "second strongest" within that filter's hierarchy creates a category mismatch. The note partially resolves this with the quantity-vs-weight distinction, but the initial ranking framing ("second strongest source") invites the reader to place observation on the same scale as first-principles and programming patterns, which the subsequent text explicitly denies. The tension is mild — the reader can reconstruct the intended meaning — but the framing could be cleaner.

PASS:
- [Grounding] The claim that Thalo "independently arrived at building an actual compiler for knowledge management — Tree-Sitter grammar, typed entities, 27 validation rules" is accurately attributed. The programming-practices-apply-to-prompting note confirms the same specifics and describes Thalo as independently developed convergent evidence.

- [Grounding] The characterization of Arscontexta — "249 research claims grounded in cognitive psychology" acknowledged but not adopted wholesale, with the spreading activation concern — is consistent with how other notes in the KB reference Arscontexta. The skepticism about spreading activation transferring to 200k-token context windows aligns with the asymmetry argument.

- [Grounding] The linked programming-practices-apply-to-prompting note supports the fast-pass claim with consistent vocabulary. Both notes frame the transfer as mechanistic ("the same mechanisms operating on different substrates"), not merely analogical. The vocabulary alignment — "bounded processors composing text under constraints" in the methodology note, "both domains solve the same problems: making behaviour predictable, making systems composable, making artifacts verifiable" in the programming note — is tight.

- [Grounding] The instruction-specificity-should-match-loading-frequency note confirms the first-principles derivation pattern claimed in the methodology note. It derives the loading hierarchy directly from finite context constraints without borrowing from external disciplines, validating the note's claim that "they follow directly from the constraints without needing analogies."

- [Grounding] The directory-scoped-types note explicitly frames directory-scoping as "a workaround for" the absence of an import mechanism, confirming the methodology note's citation of it as a first-principles design example. The derivation chain (no import mechanism -> directory-scoped types are cheaper) is present and traceable.

- [Grounding] The first-principles-reasoning-selects-for-explanatory-reach note provides a coherent theoretical grounding for the methodology note's filter. It frames the first-principles filter as "selecting for explanatory reach over adaptive fit" and the programming fast pass as "a reach bet." The two notes are mutually reinforcing and use consistent vocabulary.

- [Internal consistency] The core structure — adoption filter (what gets in) followed by asymmetry argument (why programming is privileged) followed by observation's role (a different evidence type) — is internally coherent. Each section addresses a distinct question and the answers do not contradict each other. The asymmetry section provides the theoretical justification for the fast pass described in the adoption filter.

- [Internal consistency] The distinction between first principles (scarce, individually strong, carry confidence immediately) and empirical observation (plentiful, individually weak, accumulate through repetition) is maintained consistently. The wikiwiki principle reference at the end ("capture observations freely, then refine") is consistent with this framing.

Overall: 3 warnings, 4 info
===
