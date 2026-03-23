=== SEMANTIC REVIEW: deep-search-is-connection-methodology-applied-to-temporarily-expanded-corpus.md ===

Claims identified: 14

---

**Step 1: Claims extracted**

1. "The KB's connection methodology (`/connect`) is corpus-agnostic — it runs the same dual discovery, articulation testing, and synthesis detection regardless of what documents it connects." (Opening paragraph)
2. "Deep search doesn't require new connection logic. It requires temporarily expanding the corpus with web search results, running existing connection machinery across the expanded set, then extracting durable insights." (Opening paragraph)
3. Two value propositions enumerated: (a) connect retrieved pieces to each other, (b) connect retrieved pieces to existing KB. (Section: Two value propositions)
4. Three abstraction depths attributed to the discovery epistemology note: shared feature, shared structure, generative model. (Section: Why this differs from naive search)
5. "Naive deep search stays at level 1." (Section: Why this differs from naive search)
6. "The `/connect` skill already operates at level 2 (the articulation test forces structural reasoning)." (Section: Why this differs from naive search)
7. Five-phase architecture: Seed search, Snapshot & inter-connect, Synthesize & redirect, Bridge to KB, Report. (Section: Proposed architecture)
8. "This is the boiling cauldron loop applied to search" — Phase 3 mapped to the boiling cauldron concept. (Section: Proposed architecture, Phase 3)
9. Four stopping criteria mapped to oracle types: diminishing returns, query exhaustion, budget, user checkpoint. (Section: Architectural tensions — Stopping criterion)
10. MVP is five steps that reuse existing skills without the iteration loop. (Section: Minimum viable version)
11. The MVP's five-step chain "is itself a scenario decomposition." (Section: Minimum viable version)
12. The note claims the process combines "both kinds of navigation" — long-range search retrieves, local link-following connects. (Value proposition 1)
13. Deep search "extends the KB's action capacity beyond retrieval into active research." (Value proposition 2)
14. "The same candidate-explosion problem that notes need quality scores to scale curation identifies for /connect, but amplified by web-scale result sets." (Section: Architectural tensions — Depth vs. cost)

---

**Step 2: Completeness and boundary cases**

The note's core framework is: deep search = temporarily expand the corpus, then run existing connection machinery. The two value propositions and the five-phase architecture are the main enumerations.

Boundary cases tested against the two value propositions:

- **Simplest instance: a single search result.** If only one result is retrieved, value proposition 1 (connect results to each other) collapses entirely — there is nothing to inter-connect. The note's architecture still prescribes Phase 2 (inter-connect) even when the result set is trivially small. The note does not discuss degenerate cases.
- **Most extreme instance: hundreds of results across a broad query.** The note acknowledges this under "Depth vs. cost" but the two value propositions don't address a third value that emerges at scale: *filtering* — deciding which results are worth connecting at all. The note mentions "aggressive pruning heuristics" but treats pruning as a cost concern, not as a value proposition in its own right.
- **Between the two value propositions: a result that contradicts existing KB content.** The two value propositions are both additive (connect to each other, connect to KB). But a deep search result that contradicts or supersedes existing KB content doesn't fit either — it challenges the KB rather than extending it. The discovery epistemology source explicitly notes that "contrastive links (contradicts, supersedes)" are a different axis from similarity, yet the note's architecture has no phase for contradiction detection.
- **Adjacent concept: search that refines a query rather than connecting results.** A human researcher often uses early search results to reformulate the question itself, not just to build connections. Phase 3 gestures at "new queries" but frames them as gap-filling, not as question refinement. The distinction matters because question refinement changes the search space, while gap-filling stays within it.

Boundary cases tested against the five-phase architecture:

- **Phase 2 assumes inter-connection is valuable before bridging to KB.** But if the user's goal is to find one specific piece of information, building an inter-result graph is wasted work. The architecture has no fast path for targeted lookup vs. exploratory research. This is a scope question the note doesn't address.

Boundary cases tested against the three abstraction depths (attributed to the discovery note):

- The note claims `/connect` operates at level 2. But the discovery note's level 2 is "shared structure — requires understanding, not just matching." The `/connect` skill's articulation test (forcing a reason for a link) could operate at level 1 with surface-level reasons ("both mention X because..."). The claim that articulation testing *forces* structural reasoning is an assertion about the skill's actual behavior, not a logical entailment.

Boundary cases tested against the four stopping criteria:

- **Missing: quality threshold.** The four criteria are all about *when to stop iterating* but none is about *whether results meet a quality bar*. A search could produce many low-quality results that overlap with each other (triggering diminishing returns) without ever producing anything useful. The stopping criteria are necessary but not sufficient — they don't distinguish convergence on good results from convergence on noise.

---

**Step 3: Grounding alignment**

Sources checked (5):

**3a. Discovery epistemology note (discovery-is-seeing-the-particular-as-an-instance-of-the-general.md)**

The note attributes "three abstraction depths for connections" to this source. The source does present three depths (shared feature, shared structure, generative model) in a table. Attribution is accurate. However, the deep search note says "Naive deep search stays at level 1" and "The `/connect` skill already operates at level 2." The source note does not make any claims about what tools or skills operate at which level. The mapping of `/connect` to level 2 is the deep search note's own inference, not something grounded in the discovery note.

**3b. Link contracts framework (link-contracts-framework.md)**

The deep search note says "The articulation test applies: 'Result A connects to Result B because [specific reason].'" and links to the link contracts framework. The link contracts note is about how links should carry intent, cost, and decision hints for readers. It does not discuss an "articulation test" — that term and concept appears to come from the `/connect` skill itself, not from this note. The link contracts note discusses link quality criteria (descriptive anchors, why/when hints) but these are reader-facing concerns, not a test for whether a connection is genuine.

**3c. Automating KB learning (automating-kb-learning-is-an-open-problem.md)**

The deep search note maps Phase 3 to "the boiling cauldron loop applied to search." The source note defines the boiling cauldron as a background process that "continuously proposes mutations" including Extract, Split, Synthesise, Relink, Reformulate, Regroup, and Retire. The deep search note's Phase 3 maps to a subset of these (roughly Synthesise and Relink), not the full boiling cauldron. The attribution is reasonable but slightly inflated — Phase 3 is an instance of two boiling cauldron operations, not the full loop.

**3d. Oracle-strength spectrum (oracle-strength-spectrum.md)**

The deep search note maps its four stopping criteria to "oracle types of varying strength" on the oracle-strength spectrum. The source note defines the spectrum as: hard oracle, soft oracle, interactive oracle, delayed oracle, no oracle. The deep search note maps: diminishing returns to "soft oracle: structural convergence," query exhaustion to "soft oracle: generative capacity depleted," budget to "no oracle: pure cost control," user checkpoint to "interactive oracle: human judgment." These mappings are reasonable and the vocabulary matches. However, budget is mapped to "no oracle" — but in the source note, "no oracle" means "vibes and anecdotes." A hard budget cap is deterministic and exact, which is closer to the hard oracle end. The mismatch is that a budget cap verifies cost compliance (hard oracle), not output quality (no oracle). The note may be conflating "no signal about quality" with "no oracle at all."

**3e. Two kinds of navigation (two-kinds-of-navigation.md)**

The deep search note claims the process "combines both kinds of navigation in a new context: long-range search retrieves external results, then local link-following connects them into a traversable temporary graph." The source note defines two kinds: following links (local) and search (long-range). The deep search note's usage is accurate — web search is long-range, then inter-connecting results creates a local link structure. The attribution is faithful.

**Domain coverage check (whole-note pass):**

The deep search note is a design exploration that synthesizes concepts from multiple KB notes. Its domain is "how to design a deep search skill." The sources it draws from cover: discovery epistemology, link quality, automated learning, oracle strength, and navigation modes. The note stays within the intersection of these domains — it uses them as design inputs rather than extending their claims. No domain overstep detected at the whole-note level.

---

**Step 4: Internal consistency**

- The opening paragraph claims deep search "doesn't require new connection logic" — only corpus expansion. But the architecture section introduces Phase 3 (Synthesize & redirect) with operations that go beyond connection: gap detection, synthesis, and query generation. These are new operations not present in `/connect`. The note partially acknowledges this ("The iteration loop (Phase 3) is the ambitious part") but the opening claim of "no new logic needed" is in tension with Phase 3 requiring synthesis and redirect logic that `/connect` does not perform.

- The MVP section says "Even single-pass 'search, snapshot, connect, bridge, report' would validate whether connection quality on web search results justifies the iteration investment." This frames the MVP as a validation step. But the same section also says the MVP "is itself a scenario decomposition whose context needs could be measured." These are compatible but subtly different framings — validation (does the base case work?) vs. measurement (what are the context needs?). No contradiction, but the MVP carries two different purposes without acknowledging the tension.

- The term "connection methodology" in the title implicitly includes whatever `/connect` does. If `/connect` operates at abstraction depth 2 (as claimed), then the title claim is that deep search applies depth-2 connection to an expanded corpus. But the note also asks whether iterative search can reach depth 3 (generative model). If it can, then deep search would exceed the connection methodology, not merely apply it. The title-as-claim would need revision.

- Definition drift check: "articulation test" is used consistently throughout. "Boiling cauldron" is used consistently. "Oracle" is used in the stopping criteria section with meanings consistent with the source note. No drift detected.

- Summary check: the note has no compressed summary section, so no summary faithfulness issue.

---

WARN:
- [Completeness] The two value propositions are both additive (connect results to each other, connect to KB). A third case — search results that *contradict* existing KB content — falls outside both. The discovery source explicitly scopes its depth hierarchy to similarity and notes that "contrastive links (contradicts, supersedes)" are a separate axis. The architecture has no phase for contradiction detection.
- [Grounding] "The articulation test applies" links to link-contracts-framework.md, but that note does not describe an "articulation test." The link contracts note discusses reader-facing link quality criteria (descriptive anchors, intent taxonomy), not a test for whether a connection is genuine. The articulation test concept likely originates in the /connect skill, not this source.
- [Grounding] Budget is mapped to "no oracle: pure cost control" but in the oracle-strength spectrum source, "no oracle" means "vibes and anecdotes." A hard budget cap is deterministic — it verifies cost compliance exactly. The note conflates "provides no signal about output quality" with "is not an oracle," when the source's spectrum is about verification strength, not quality-relevance.
- [Internal consistency] The opening paragraph claims deep search "doesn't require new connection logic," but Phase 3 (Synthesize & redirect) introduces gap detection, synthesis opportunity identification, and new query generation — operations not present in `/connect`. The note partially acknowledges Phase 3 is "the ambitious part," but the title claim that deep search IS connection methodology applied to a new corpus is strained by the note's own architecture.

INFO:
- [Completeness] The four stopping criteria address when to stop iterating but not whether results meet a quality threshold. A search could converge (diminishing returns) on low-quality results. Quality gating is a distinct concern from stopping, and the note's architecture does not separate them.
- [Completeness] The architecture has no fast path for targeted lookup vs. exploratory research. If the user needs one specific fact, building an inter-result graph (Phase 2) is overhead. The note assumes an exploratory use case without stating this scope limitation.
- [Grounding] The claim that "/connect already operates at level 2" (shared structure) is the deep search note's own inference. The discovery source defines the levels but does not map any tool or skill to them. An articulation test could operate at level 1 with surface-level reasons ("both mention X"), so the mapping depends on the skill's actual behavior, not on the test's formal structure.
- [Grounding] Phase 3 is mapped to "the boiling cauldron loop applied to search," but the boiling cauldron in the source note lists seven mutation types (Extract, Split, Synthesise, Relink, Reformulate, Regroup, Retire). Phase 3 covers roughly two of these (Synthesise, Relink). The attribution is slightly inflated — Phase 3 is an instance of a subset, not the full loop.
- [Internal consistency] The title claims deep search IS connection methodology applied to a new corpus. But the note itself asks whether iterative search can reach abstraction depth 3 (generative model), which would exceed `/connect`'s claimed depth 2. If deep search can do what `/connect` cannot, the title understates the ambition.

PASS:
- [Completeness] The five-phase architecture (Seed, Snapshot & inter-connect, Synthesize & redirect, Bridge to KB, Report) covers a coherent end-to-end flow. No phase is redundant and no obvious phase is missing within the note's stated scope.
- [Grounding] The three abstraction depths (shared feature, shared structure, generative model) are accurately attributed to the discovery epistemology note, which presents them in the same order with the same definitions.
- [Grounding] The two-kinds-of-navigation attribution is faithful. The source defines local link-following and long-range search; the deep search note's claim that web search is long-range and inter-connection creates local structure is a clean application.
- [Grounding] The workshop lifecycle concern correctly maps to the workshop layer note's concept of high-churn, value-consuming material needing extraction bridges to become library material.
- [Internal consistency] Key terms (articulation test, boiling cauldron, oracle) are used consistently throughout the note without definition drift.
- [Internal consistency] The MVP section is logically consistent with the architecture section — it is explicitly framed as the architecture minus the iteration loop (Phase 3), and the note correctly identifies Phase 3 as the part that needs separate validation.

Overall: 4 warnings, 5 info
===
