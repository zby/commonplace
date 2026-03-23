=== SEMANTIC REVIEW: first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md ===

Claims identified: 14

1. [Intro] Deutsch distinguishes two kinds of knowledge: adaptive information and explanatory knowledge.
2. [Intro] Adaptive information helps a system cope but doesn't explain why it works, can't be deliberately varied, and doesn't transfer beyond its training distribution.
3. [Intro] Explanatory knowledge says why the world works, can be deliberately varied and criticized, and supports transfer to new contexts.
4. [Intro] The distinguishing property is "reach": explanatory knowledge applies beyond its original context because the explanation captures structure that isn't context-dependent.
5. [Why this matters for the KB] The KB's first-principles methodology is a filter that selects for explanatory reach over adaptive fit.
6. [Why this matters for the KB] A derivation from constraints is explanatory because it says why the pattern works, which means it predicts where the pattern will fail.
7. [Why this matters for the KB] "X works in practice" is adaptive — useful but brittle to context change.
8. [Why this matters for the KB] The computational-model area exemplifies reach: PL concepts reach into KB design because they capture structure that isn't programming-specific.
9. [Why this matters for the KB] "LLM context is composed without scoping" identifies the same mechanism producing the same pathologies (as dynamic scoping), and predicts the same remedies.
10. [The negative test] Three tests: Can you vary the explanation? Does it reach? Can it be criticized?
11. [The negative test] These three tests map to the three depths in discovery: shared feature (adaptive), shared structure (partially explanatory), generative model (fully explanatory with reach).
12. [The programming fast-pass] Programming patterns get a fast pass because agents interpreting prompts are structurally similar to interpreters interpreting programming languages.
13. [The programming fast-pass] Thalo's convergent evolution is evidence for this structural similarity.
14. [Relevant Notes] The "complements" link to information-value-is-observer-relative claims reach means the explanation makes structure accessible to observers in multiple contexts.

---

## Step 2: Completeness and boundary cases

### Framework: Adaptive vs. explanatory binary (Claims 1-4)

**Grounding definition:** Deutsch's distinction. Adaptive information = structures that help cope but don't explain why. Explanatory knowledge = captures why, can be varied and criticized, transfers.

**Boundary cases tested:**

1. **Simplest instance: a lookup table.** A lookup table mapping inputs to outputs is paradigmatically adaptive — it works but explains nothing. Maps cleanly to "adaptive."

2. **Between-item case: a statistical model with interpretable coefficients.** A linear regression with meaningful coefficients (e.g., "price increases 3% per unit of distance") gives *some* "why" — the coefficients are interpretable and can be varied. But the model doesn't capture the deeper mechanism generating the relationship. It's more than adaptive (you can reason about what happens if distance changes), less than fully explanatory (you don't know *why* distance matters). The note presents the distinction as binary; this case suggests a gradient.

3. **Adjacent concept: heuristics developed through deliberate practice.** A chess grandmaster's intuition was developed through years of deliberate study and can be articulated post-hoc ("I saw the knight fork pattern"). It transfers to new positions. It *can* be criticized ("that fork doesn't work because the bishop covers the escape square"). By the note's criteria, this should count as explanatory — yet Deutsch would likely classify it as closer to adaptive (it's a refined instinct, not a theory of chess). The note's three criteria (vary, reach, criticize) would classify expert intuition as explanatory, but the original Deutsch framing might not.

4. **Extreme instance: a mathematical proof.** A proof is maximally explanatory — it says exactly why a conclusion follows from premises, can be varied (change an axiom, see what breaks), and transfers to any domain where the axioms hold. Maps cleanly to "explanatory."

5. **Between-item case: engineering rules of thumb with known derivations.** "Don't exceed 80% of context window" — this is adaptive if treated as a rule, but the underlying reasoning (soft degradation, attention dilution) is explanatory. The same artifact can be read as either. The note acknowledges this partially ("X works in practice" is adaptive) but doesn't address the case where a practitioner *knows* the derivation behind a pattern but records only the conclusion.

### Framework: The three negative tests (Claim 10)

**Grounding definition:** The note's own framing — three tests for whether a note is explanatory: vary, reach, criticize.

**Boundary cases tested:**

1. **A definitional note (e.g., "context engineering is X").** Can you vary it? Not meaningfully — changing the definition changes the subject. Does it reach? Definitions don't transfer; they scope. Can it be criticized? Only by proposing a better definition. The three tests don't distinguish good definitions from bad ones, and the note doesn't address definitional claims.

2. **A negative result note ("X doesn't work because Y").** Can you vary it? Yes — change Y, and the conclusion changes. Does it reach? Maybe — the mechanism of failure could apply elsewhere. Can it be criticized? Yes. This maps well to the framework.

3. **A meta-methodological note (like this one).** "First-principles filtering selects for reach" — can you vary it? The note itself is partially self-referential: it argues for the method the KB uses to evaluate notes, including this one. This doesn't break the framework, but the self-reference means the "criticize" test requires stepping outside the KB's epistemological commitments.

### Enumeration: Three depths mapping (Claim 11)

The note claims the three tests map to the three discovery depths: shared feature = adaptive, shared structure = partially explanatory, generative model = fully explanatory with reach. This is a three-to-three mapping.

**Boundary case:** The mapping direction is one-way in the note (discovery depths -> reach levels), but the axes appear orthogonal. Discovery depth is about *abstraction level of a connection between phenomena*. Reach is about *transfer range of an explanation*. A shared-feature observation could have high reach (e.g., "all these systems fail under load" is a surface observation that transfers widely), while a generative model could have narrow reach (a detailed causal model of one specific failure mode). The note asserts the mapping without arguing for it.

---

## Step 3: Grounding alignment

### Source 1: design-methodology-borrow-widely-filter-by-first-principles.md

**Attribution check:** The note claims "The KB's first-principles methodology is, in Deutsch's terms, a filter that selects for explanatory reach over adaptive fit." The design-methodology note describes first-principles reasoning as "the main filter" and the programming fast-pass as a "bet" on structural similarity. It does not use Deutsch's vocabulary (reach, adaptive, explanatory). The reviewed note is making an interpretive move: reframing the design methodology in Deutsch's terms. This is a reasonable inference — the design methodology does emphasize "why something works from constraints" which aligns with Deutsch's explanatory knowledge — but it is the reviewed note's own synthesis, not something the methodology note claims.

**Domain coverage:** The methodology note discusses source selection and adoption criteria. The reviewed note claims the methodology *is* a specific epistemological filter (Deutsch's). The methodology note's concerns are broader (it also discusses empirical observation, programming fast-pass pragmatics, legal drafting as candidate source). The Deutsch reframing covers the first-principles portion but not the full adoption methodology.

### Source 2: discovery-is-seeing-the-particular-as-an-instance-of-the-general.md

**Attribution check:** The note claims the three tests "map to the three depths in discovery: shared feature (adaptive), shared structure (partially explanatory), generative model (fully explanatory with reach)." The discovery note defines three depths: shared feature (descriptive), shared structure (structural), generative model (explanatory). It does not connect these to Deutsch's adaptive/explanatory distinction or to reach. The mapping is the reviewed note's own contribution.

**Vocabulary mismatch:** The discovery note uses "descriptive / structural / explanatory" for its three levels. The reviewed note translates these to "adaptive / partially explanatory / fully explanatory with reach." The first translation (shared feature = adaptive) is a stretch — the discovery note says shared features "organize but don't explain," which is weaker than "adaptive" (which implies functional fitness). Something can be descriptive without being adapted.

### Source 3: mechanistic-constraints-make-popperian-kb-recommendations-actionable.md

**Attribution check:** The note claims "Deutsch and Popper are allied — explanatory knowledge is the kind criticism can test; falsifier blocks operationalize one of the three tests." The Popperian note does discuss criticism as structural practice and falsifier blocks. The connection between Deutsch's explanatory knowledge and Popper's falsifiability is a well-established philosophical position (Deutsch explicitly builds on Popper). The reviewed note's claim that falsifier blocks operationalize the "can it be criticized?" test is a reasonable and well-grounded connection.

### Source 4: computational-model-index.md

**Attribution check:** The note claims the computational-model area "exemplifies reach" because PL concepts "reach into KB design because they capture structure that isn't programming-specific." The computational-model index lists PL concepts applied to LLM instructions. The reviewed note's interpretation — that this transfer happens because PL concepts capture non-programming-specific structure — is consistent with the design methodology note's "bounded processors composing text under constraints" argument. The exemplification claim is reasonable.

### Source 5: llm-context-is-composed-without-scoping.md

**Attribution check:** The note claims this note "doesn't just analogize to dynamic scoping — it identifies the same mechanism producing the same pathologies, and predicts the same remedies (lexically scoped sub-frames)." The scoping note does claim "the pathologies are the same ones that dynamic scoping produces" and proposes sub-agents as lexical scoping. However, the scoping note itself hedges: "This is not even dynamic scoping, which at least has a stack with push and pop. It is flat concatenation." So the scoping note says the mechanism is *not the same* as dynamic scoping (it's worse — no stack), but the *pathologies* are similar. The reviewed note's claim that it "identifies the same mechanism" slightly overstates — the scoping note identifies *analogous pathologies from a different (worse) mechanism*.

---

## Step 4: Internal consistency

1. **Pairwise contradiction check:** No contradictions found between sections. The intro defines the framework, the KB section applies it, the negative test operationalizes it, and the fast-pass section connects to prior work. The flow is coherent.

2. **Definition drift check:** "Reach" is used consistently throughout — always meaning "applies beyond original context because it captures non-context-dependent structure." No drift detected.

3. **Summary faithfulness:** The note has no compressed summary section. The description ("Deutsch's adaptive-vs-explanatory distinction...") accurately represents the body content.

4. **Tension between binary framing and three-test gradient:** The intro presents adaptive vs. explanatory as a binary distinction. The negative test section introduces three tests that each admit degrees (you can *partially* vary an explanation, a note can reach *somewhat*). This creates an implicit gradient within what was introduced as a dichotomy. The note doesn't acknowledge this tension, though the discovery-mapping paragraph partially addresses it by introducing "partially explanatory" as a middle category.

---

WARN:
- [Completeness] The adaptive/explanatory distinction is presented as binary, but the three negative tests each admit degrees, and the mapping to discovery depths introduces a middle category ("partially explanatory"). The note silently shifts from binary framing to gradient framing without acknowledging the tension. Boundary case: an engineering rule of thumb whose derivation is known but unrecorded straddles both categories.
- [Grounding] "LLM context is composed without scoping" is cited as identifying "the same mechanism" as dynamic scoping, but the source note explicitly says it is "not even dynamic scoping" — it identifies analogous pathologies from a structurally different (worse) mechanism. The reviewed note overstates the source's claim.
- [Grounding] The three-to-three mapping between discovery depths and reach levels (Claim 11) is asserted without argument. The axes appear potentially orthogonal: discovery depth measures abstraction level of connections, reach measures transfer range of explanations. A shared-feature observation can have wide reach; a generative model can have narrow reach. The discovery note does not make this mapping, so it is the reviewed note's own contribution and the link text ("parallels: the generative model depth maps to explanatory knowledge with reach") presents it as established rather than conjectured.

INFO:
- [Completeness] The three negative tests (vary, reach, criticize) don't cleanly handle definitional notes. Definitions can't be meaningfully "varied" (changing the definition changes the subject), don't "reach" in the transfer sense, and can only be "criticized" by proposing alternatives. The note is implicitly scoped to causal/explanatory claims, but this scope is unstated.
- [Grounding] The reviewed note reframes the design methodology as "a filter that selects for explanatory reach over adaptive fit." The design-methodology note does not use Deutsch's vocabulary; this is the reviewed note's interpretive synthesis. The reframing is reasonable but covers only the first-principles portion of the methodology, not the empirical-observation or fast-pass portions.
- [Completeness] The note does not address cases where explanatory knowledge *lacks* reach — where a correct causal explanation is specific to a narrow domain and doesn't transfer. Deutsch's framework allows for this (an explanation can be hard-to-vary yet domain-specific), but the note equates explanatory status with reach, potentially conflating two properties that can come apart.

PASS:
- [Internal consistency] No contradictions found between sections. The framework definition, KB application, negative tests, and fast-pass discussion form a coherent argument.
- [Internal consistency] "Reach" is used with stable meaning throughout the note — no definition drift detected.
- [Grounding] The connection between Deutsch's explanatory knowledge and Popper's falsifiability (via the Popperian note) is well-grounded — Deutsch explicitly builds on Popper, and the falsifier blocks practice does operationalize the "can it be criticized?" test.
- [Grounding] The claim that the computational-model area exemplifies reach is well-supported — the PL-to-KB-design transfer is documented across multiple notes in that index.
- [Grounding] The programming fast-pass framing accurately reflects the design-methodology note's description of the programming bet and Thalo's convergent evolution as evidence.

Overall: 3 warnings, 3 info
===
