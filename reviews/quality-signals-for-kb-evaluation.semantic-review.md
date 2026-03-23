=== SEMANTIC REVIEW: quality-signals-for-kb-evaluation.md ===

Claims identified: 18

## Step 1: Claims extracted

1. "No single signal is reliable, but many weak signals combined might provide enough guidance to drive a learning loop without waiting for usage data." (Intro)
2. "A mesh suggests genuine integration; hub-and-spoke suggests cataloguing without understanding." (Static signals — Graph topology)
3. "Titles starting with verbs or containing 'is/are/should/enables' are likely claims." (Content quality proxies — Title-as-claim ratio)
4. The static signals section enumerates three sub-categories: graph topology, content quality proxies, structural health. (Implicit scope claim: these cover the static signal space.)
5. Six metamorphic relations are enumerated: split invariant, synthesis test, connection test, rename consistency, deletion impact, link articulation. (Implicit scope claim: these are the relevant mutation-testable properties.)
6. "This is the same move as ensemble methods in ML: individual weak learners combined into a strong one." (The "many weak signals" hypothesis — analogy claim)
7. "The question is whether the signals are independent enough. If they all correlate... the ensemble doesn't add much." (Many weak signals)
8. The four-step learning loop: propose mutation, measure composite score before/after, accept/reject, learn over time. (What could drive a learning loop)
9. "This doesn't require usage data — it runs on structure alone." (What could drive a learning loop)
10. Neighborhood evaluation "regularly surfaces actionable edits." (Neighborhood evaluation)
11. "The graph structure determines *what context to load*; the LLM does the *judgment* that structural signals can't." (Neighborhood evaluation — complementarity claim)
12. Structural signals and neighborhood evaluation are complementary: each catches what the other misses. (Neighborhood evaluation — two enumerated lists)
13. Four LLM critique calibration strategies: relative comparison, cross-note baseline, fix-and-re-critique, structured rubrics. (LLM critique)
14. "The fix-and-re-critique approach is itself metamorphic." (LLM critique)
15. Four agent-centric navigability signals: hop cost, pruning accuracy, trust calibration, reasoning chain coherence. (Agent-centric signals)
16. "A-MEM's benchmark success with embedding-based linking shows that retrieval accuracy and navigability are distinct evaluation dimensions." (Agent-centric signals — attribution to A-MEM)
17. Credibility erosion is "qualitatively different from having too few links — it's worse than no linking infrastructure." (Credibility erosion)
18. "This is Goodhart's law applied to link generation." (Credibility erosion)

## Step 2: Completeness and boundary cases

### Enumeration: Static signal categories (graph topology / content quality proxies / structural health)

Grounding definition: The note's own framing — "structural, semantic, or hybrid" signals that "could serve as soft oracles for KB quality." The three sub-categories are presented under the header "Static signals (measurable at any point)."

Boundary cases tested:

- **Temporal/historical signals** (e.g., edit frequency, note age distribution, velocity of link creation): These are measurable at any point from git history and are static in the sense of not requiring an agent in the loop, yet they don't clearly fit graph topology, content quality, or structural health. The note mentions "note age vs connection count" under structural health, but broader temporal patterns (acceleration/deceleration of writing, time-to-first-link) are absent. INFO — these could be forced under structural health but the fit is strained.

- **Tag/metadata consistency signals** (e.g., tag vocabulary drift, tag co-occurrence patterns): The note mentions "frontmatter completeness" but not whether the tag vocabulary itself is well-structured — are tags reused consistently, or do synonymous tags proliferate? This is a content-level signal that doesn't fit neatly into any of the three sub-categories. INFO — adjacent to content quality proxies but distinct enough to note.

### Enumeration: Metamorphic relations (6 items)

Grounding definition: "Instead of testing 'is this KB good?', test 'did this change make it better or worse?'" — testable properties over mutations.

Boundary cases tested:

- **Merge invariant** (the inverse of split): The note covers split but not merge. When two notes are merged, total outbound links should be preserved or simplified, and the merged note should subsume both claim spaces. This is the natural dual of the split invariant and its absence is notable given that the boiling cauldron in the linked note explicitly includes merge-like operations (regroup). INFO — likely an oversight rather than a principled exclusion.

- **Regroup/re-index invariant**: Moving a note from one area to another should preserve its connections within the new area. The note covers connection test (adding to an area) but not the case of moving between areas. INFO — could be derived from connection test but not explicitly covered.

### Enumeration: LLM critique calibration strategies (4 items)

Grounding definition: The problem stated is that "LLMs tend to always find fault, so you can't use 'number of faults' as a quality score."

Boundary cases tested:

- **Grounding against external reference** (compare LLM critique against human expert judgment on a sample): This is the most direct calibration method — use a labeled set of known-good and known-bad notes to measure the LLM's discrimination. The note's four strategies are all internal (compare notes to each other, compare across corpus, compare before/after fix, constrain rubric), but none anchor against a ground-truth quality label. INFO — the note acknowledges "no oracle" as the problem context, so the absence of this strategy may be deliberate, but it's worth noting that even a small labeled sample could calibrate the other strategies.

### Enumeration: Agent-centric navigability signals (4 items)

Grounding definition: "Navigability signals measure whether an agent can use the link structure to reason, not just retrieve."

Boundary cases tested:

- **Context cost** (total tokens loaded during a traversal to answer a question): The note mentions "hop cost" (number of links) but not the token cost of loading content along the path. An agent might reach the answer in 2 hops but load 50K tokens of irrelevant surrounding content, or reach it in 4 hops loading only 5K tokens total. Token efficiency per traversal is a navigability signal distinct from hop count. INFO — could be subsumed under hop cost if "informative hops" is interpreted broadly, but the note's operationalization ("counting traversal steps") suggests it means link count, not token cost.

### Enumeration: Complementarity lists (what neighborhood evaluation catches vs. what structural signals catch)

Grounding definition: The two enumerated lists claim to show what each approach catches that the other misses.

Boundary cases tested:

- **False connections** (links that exist between notes that shouldn't be connected): The structural-signals-miss list says neighborhood evaluation catches "a link exists but the relationship isn't articulated," which partially covers this. But there's a stronger case: two notes that are linked and the link is articulated, but the articulated relationship is wrong (e.g., "extends" when it actually contradicts). This requires content-level judgment and isn't clearly covered by either list. INFO — likely falls under neighborhood evaluation but the lists frame the catch as "articulation missing," not "articulation incorrect."

## Step 3: Grounding alignment

### A-MEM attribution (Agent-centric signals section)

The note claims: "A-MEM's benchmark success with embedding-based linking shows that retrieval accuracy and navigability are distinct evaluation dimensions: a system can score well on QA benchmarks while its link structure is unusable for reasoning."

The A-MEM ingest source confirms A-MEM achieves benchmark success on LoCoMo and DialSim QA benchmarks with embedding-based linking and untyped "connected to" associations. The ingest also notes: "Links are untyped 'connected to' associations, not typed relationships with articulated reasons."

However, the claim that A-MEM's link structure is "unusable for reasoning" is the note's own inference, not something the A-MEM paper demonstrates. A-MEM's evaluation never tests navigability or reasoning-by-traversal — it tests retrieval accuracy. The note is correct that retrieval and navigability are distinct, but it frames A-MEM as evidence for the distinction when A-MEM only demonstrates one side (retrieval works). The other side (navigability fails) is inferred from the link design, not measured. INFO — the inference is reasonable given the untyped link structure, but the attribution presents inference as demonstration.

### Agentic Note-Taking source (Credibility erosion section)

The note claims the source "describes this from the consumer side — an agent experiencing qualitative degradation as link trust erodes."

The source (Cornelius's thread) does describe exactly this: "If enough connections lead nowhere useful, the infrastructure loses credibility. The genuine connections that judgment created get buried under the noise that automation generated." The attribution is accurate. PASS.

### Oracle-strength-spectrum (framing)

The note claims: "Framed on the oracle-strength spectrum, the question is whether combining many no-oracle or weak-oracle signals can manufacture a usable soft oracle."

The oracle-strength-spectrum note defines the spectrum (hard/soft/interactive/delayed/no oracle) and proposes "harden the oracle" as the engineering move. The quality-signals note accurately uses this framework: combining weak signals is an oracle-hardening strategy. PASS.

### Spec-mining link (Metamorphic relations section)

The note claims: "This is spec mining applied to KB structure: observe the invariants that hold across mutations, then extract them as testable properties."

The spec-mining note defines the pattern as: "Watch the system do tasks... Identify repeated micro-actions... Extract those regularities into deterministic artifacts." The quality-signals note extends this from system behavior to KB structure. The term "spec mining" in the source means extracting deterministic verifiers from observed stochastic behavior, while the quality-signals note applies it to extracting testable invariants from KB mutations. The analogy holds — both extract deterministic checks from observed patterns. PASS.

### Text-testing-framework (Neighborhood evaluation section)

The note claims: "In the text testing pyramid, this is Level B (LLM rubric grading) applied to note clusters rather than individual notes."

The text-testing-framework note defines Level B as: "LLM rubric graders (medium cost, high coverage)" with examples like checking for clear thesis, source attribution, internal contradiction. The quality-signals note maps neighborhood evaluation to Level B, which is a reasonable mapping — LLM judgment applied with structured criteria. However, the neighborhood evaluation as described is more open-ended than Level B rubric grading. The text-testing-framework's Level B uses structured prompts with rubrics and examples yielding structured JSON. The neighborhood evaluation loads a note's 1-hop neighborhood and asks the LLM to "evaluate the ensemble" — this is closer to Level C (adversarial/cross-model checks) in its open-endedness, or a hybrid of B and C. INFO — the mapping to Level B specifically is a simplification; the practice described is less constrained than the framework's Level B definition.

### Domain coverage check (whole-note pass)

The note cites the oracle-strength-spectrum as its theoretical grounding. The oracle-strength-spectrum is about verification difficulty as a gradient — how cheaply you can check correctness. The quality-signals note stays within this domain: it proposes signals that serve as cheap-but-imperfect verification proxies (soft oracles) and discusses combining them (oracle hardening). The ensemble-methods analogy in "many weak signals" is the note's own addition — the oracle-strength-spectrum does not discuss ML ensemble methods. The analogy is apt but it's the note's contribution, not something grounded in the source. PASS — the note's domain is consistent with its grounding sources; the extensions are clearly the note's own.

## Step 4: Internal consistency

### Definition drift check: "signal"

The note uses "signal" consistently throughout to mean a measurable proxy for quality. No drift detected. PASS.

### Cross-section consistency: Goodhart risk

The "Open questions" section warns: "Is there a risk of Goodhart's law — optimising structural signals at the expense of actual quality? A note linking to everything would score well on connectivity but poorly on precision."

The "Credibility erosion" section describes exactly this Goodhart dynamic for embedding-based systems: "connection count measures vocabulary overlap, not understanding." These two sections are consistent — the open question generalizes the credibility erosion observation to the note's own proposed composite signal. The note is admirably self-aware about this risk. PASS.

### Cross-section consistency: "doesn't require usage data" vs. agent-centric signals

The "What could drive a learning loop" section claims: "This doesn't require usage data — it runs on structure alone."

The "Agent-centric signals" section later says: "These signals require an agent in the loop (or an LLM simulating one), making them more expensive than structural signals." Agent-in-the-loop is not the same as usage data (query logs, retrieval failures), but it's also not "structure alone." The learning loop claim precedes the agent-centric signals section and appears to apply to the composite of static + metamorphic signals. The agent-centric signals are introduced later as a separate dimension. WARN — the "runs on structure alone" claim is made about the learning loop before the agent-centric signals section introduces a category that doesn't run on structure alone. A reader following the argument linearly could mistake the "structure alone" claim as covering the full signal catalogue. The note would benefit from scoping the claim explicitly to static + metamorphic signals, or acknowledging that the agent-centric signals expand the learning loop's requirements.

### Summary faithfulness check

The description reads: "Catalogues graph-topology, content-proxy, and LLM-hybrid signals that could be combined into a weak composite oracle to drive a mutation-based KB learning loop without requiring usage data."

This omits the agent-centric signals section and the credibility erosion section — both substantial contributions. The description's "without requiring usage data" claim inherits the same tension noted above: the agent-centric signals section introduces signals that, while not usage data per se, require more than structural measurement. INFO — the description is not inaccurate but it underrepresents the note's scope by omitting two of its eight sections.

---

WARN:
- [Internal consistency] The "What could drive a learning loop" section claims "This doesn't require usage data — it runs on structure alone," but the later "Agent-centric signals" section introduces signals that require an agent in the loop, not just structural measurement. The claim's scope is ambiguous — it could refer to just static + metamorphic signals, but it reads as covering the entire proposal.

INFO:
- [Completeness] Temporal/historical signals (edit frequency, velocity of link creation, time-to-first-link) are static and measurable but don't map cleanly to the three sub-categories of graph topology, content quality proxies, or structural health.
- [Completeness] Tag vocabulary consistency (synonym proliferation, co-occurrence patterns) is absent from content quality proxies.
- [Completeness] Merge invariant — the natural dual of the split invariant — is absent from the metamorphic relations, despite merge being a boiling cauldron operation.
- [Completeness] The LLM critique calibration strategies omit anchoring against a ground-truth labeled sample, which is the most direct calibration method.
- [Completeness] Context cost (total tokens loaded per traversal) is distinct from hop cost (link count) as a navigability signal but is not separately enumerated.
- [Completeness] False articulations (links where the stated relationship is wrong, not just missing) are not clearly covered by either the structural or neighborhood evaluation complementarity lists.
- [Grounding] A-MEM is cited as showing that "link structure is unusable for reasoning," but A-MEM's evaluation never tests navigability — the unusability is the note's inference from A-MEM's untyped link design, not a measured finding.
- [Grounding] Neighborhood evaluation is mapped to "Level B (LLM rubric grading)" from the text testing framework, but the practice described is more open-ended than Level B's structured rubric format.
- [Internal consistency] The description omits the agent-centric signals and credibility erosion sections, underrepresenting the note's scope.

PASS:
- [Grounding] The Agentic Note-Taking source attribution for credibility erosion is accurate — the source describes exactly the dynamic the note claims.
- [Grounding] The oracle-strength-spectrum framing is accurately applied — combining weak signals as oracle hardening is consistent with the source's "harden the oracle" engineering move.
- [Grounding] The spec-mining analogy for metamorphic relations holds — both extract deterministic checks from observed patterns.
- [Grounding] The note's domain stays within its grounding sources' territory; extensions (ensemble-method analogy, agent-centric signals) are clearly the note's own contributions.
- [Internal consistency] The Goodhart risk discussion in Open Questions is consistent with and generalizes the Credibility Erosion section — the note is self-aware about its own proposed signals being vulnerable to the same corruption it diagnoses.
- [Internal consistency] The term "signal" is used consistently throughout without definition drift.

Overall: 1 warning, 9 info
===
