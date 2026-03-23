=== PROSE REVIEW: minimum-viable-vocabulary-is-the-set-of-names-that-maximally-reduces-extraction-cost-for-a-bounded-observer.md ===

Checks applied: 8

WARN:
- [Pseudo-formalism] The title and body frame MVV as an optimization problem ("maximally reduces," "smallest set," "optimal set"), and the note claims "this framing also makes the concept testable in principle." However, no optimization formalism is actually provided — there is no objective function, no constraint specification, no procedure for comparing candidate vocabularies beyond the verbal suggestion that one could use "prequential coding" with "a fixed observer." The optimization language does rhetorical work (it sounds more precise than Kim's "conceptual thresholds") but the note's actual contribution is a reframing in prose, not a formalization. Deleting every optimization-flavored phrase and re-reading: the argument is equally clear.
  Recommendation: Either supply the optimization formulation (objective, constraints, what "maximally" means formally) or soften the framing — e.g., "can be understood as an optimization problem" rather than asserting it is one. The current language claims more precision than the note delivers.

- [Confidence miscalibration] The sentence "Two mechanisms already in the KB explain why a set of names can have this effect" presents the KB's own framework as established explanation. The discovery note and distillation note are themselves the KB's constructions, not externally validated theory. Likewise "naming provides the unit of cost reduction" and "distillation explains why the optimal set varies by observer" assert rather than propose. The note is building a novel synthesis from its own prior notes — that synthesis is proposed, not established.
  Recommendation: Flag the synthesis as the note's own construction. E.g., "Two mechanisms already in the KB offer a candidate explanation" or "On this account, naming provides the unit of cost reduction." This is especially important for a seedling-status note.

INFO:
- [Source residue] The examples "textbooks, codebases, and papers" in the opening paragraph and "a human learning 3D graphics and an agent parsing 3D file formats" in the distillation paragraph are concrete enough to be illustrative but general enough not to constitute residue from Kim's specific tweet thread. The one instance worth checking: "domainmaps.co" is mentioned as Kim's prototype without any description of what it does. A reader unfamiliar with the source gets no context for evaluating the claim that it "provides neither" a measure of extraction nor a fixed observer.
- [Proportion mismatch] The two mechanism paragraphs (naming and distillation) are roughly balanced with each other, but the testability claim in the final sentence of the main body ("Given two candidate vocabularies...") is compressed into a single dense sentence. Testability is arguably the note's strongest differentiator from Kim's original framing — it is what the optimization reframing buys you — yet it receives the least development. This is minor given the note's seedling status, but worth flagging for future expansion.

CLEAN:
- [Source residue] The note cleanly separates Kim's framing ("minimum viable ontology," "conceptual thresholds") from its own reframing ("minimum viable vocabulary," "extraction cost"). The terminological substitution is explicitly justified in paragraph 2. No vocabulary from the source tweet thread leaks in unmarked.
- [Orphan references] All specific claims are attributed. Kim (2026) is sourced. Meyer & Land are named in the Open Questions section and flagged as an open question rather than asserted. The epiplexity framework is linked. "domainmaps.co" is attributed to Kim. No floating empirical claims or unsourced numbers.
- [Unbridged cross-domain evidence] The note applies to both humans and agents and explicitly addresses why the same framework covers both ("a human without domain experience, an agent without domain vocabulary in context"). The bridge is the shared concept of "bounded observer." The Meyer & Land reference in Open Questions is correctly kept as a question rather than asserted as transferring.
- [Redundant restatement] No section re-explains what a prior section established. The summary paragraph ("Together, the two mechanisms ground the optimization claim...") synthesizes rather than restates — it combines the two mechanisms into a testability claim, which is new.
- [Anthropomorphic framing] The note uses "bounded observer" consistently for both humans and agents, avoiding attribution of human mental states to models. "Extract," "reach," "lack" are used for the observer's computational limitations, which is precise rather than anthropomorphic.

Overall: 2 warnings, 2 info
===
