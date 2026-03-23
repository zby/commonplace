=== SEMANTIC REVIEW: scenario-decomposition-drives-architecture.md ===

Claims identified: 18

--- Step 1: Claims extracted ---

1. [Opening paragraph] "What's missing is the bridge: start from concrete user stories, decompose them into steps, identify what the agent needs at each step, and derive architectural requirements from that analysis."
2. [Two operating contexts] "The scenarios must work in two distinct contexts: this repo, where the methodology is the content; and installed projects, where user content and methodology are separate trees."
3. [Installed project context] "In normal operation, the agent should not need to consult commonplace/ at all — everything is distilled into skills and the CLAUDE.md fragment."
4. [Installed project context] "But distillation is not lossless. When the agent hits a case the distilled procedures don't cover, it must escalate to commonplace/kb/notes/ for the full reasoning."
5. [User stories section] "The right unit isn't 'read' or 'write' — it's a complete user story with its full chain of agent actions."
6. [Four user stories enumeration] Four user stories are identified: Write a note, Ingest a source, Respond to a change, Answer a question.
7. [Write a note decomposition] The common path is the same in both contexts — "In commonplace, types and WRITING.md are the originals. In an installed project, they're copies. The agent doesn't know or care — the paths are the same."
8. [Escalation path] "The escalation adds 2-3 hops to a different tree. It's expensive but rare."
9. [Commonplace escalation] "In commonplace, this escalation doesn't exist." because methodology notes ARE the content.
10. [Ingest skill limitation] "Current skills don't do this" (signal that escalation is available).
11. [Answer a question] "Answer a question rarely escalates because it's a read-only scenario — the agent searches, reads, follows links, synthesizes. No structural decisions."
12. [Architectural principles — enumeration of 6] Six architectural principles "fall out" of the decomposition.
13. [Where system is strong] "The combination of always-loaded search patterns, description-as-retrieval-filter, and claim titles means the 'find related notes' step works well."
14. [Where system is strong] "The decomposition confirms that the installation architecture's design — copy operational artifacts, keep methodology separate — produces a clean common path. Most writes stay in kb/ with 3 hops."
15. [Gaps enumeration] Four gaps identified: end-to-end orchestration, post-write connection gap, escalation discoverability, scenario awareness in skills.
16. [Escalation discoverability] "The agent has no signal that it's in a case the distilled procedures don't cover."
17. [Measurable artifacts] "The decomposition tables above are now implemented as structured scenario files in test/scenarios/."
18. [Measurable artifacts] "Hops are stored in the scenario files (they're architectural, determined by the step structure), but instruction bytes are NOT stored — they're calculated dynamically by reading the actual source files."

--- Step 2: Completeness and boundary cases ---

**Claim 6: Four user stories enumeration.** The note identifies four user stories: Write a note, Ingest a source, Respond to a change, Answer a question. The implicit scope is "what the KB is used for," grounded in the linked scenarios.md note.

Boundary cases tested:

(a) **Maintenance/refactoring existing notes** — The user asks the agent to restructure, merge, or split existing notes. This is neither "write a note" (it modifies existing ones) nor "answer a question." It involves reading many notes, understanding their relationships, and making structural changes. It shares properties with "write a note" but its context needs differ: it requires understanding the existing graph structure, not just finding related notes. The note's decomposition table doesn't cover the "understand current structure" step that maintenance requires.

(b) **Review/validate a note (this very task)** — The agent reads a note, follows its sources, applies judgment criteria, and writes a report. It's a hybrid of "answer a question" (read-only analysis) and "write a note" (produces output). The review procedure requires loading an instruction file, which is a "know the structure" step — but the four stories don't have a clean slot for "load a procedure and apply it to existing content."

(c) **Delete or deprecate a note** — The agent needs to remove a note and update all references. This requires graph-aware operations (find all inbound links, update indexes) that none of the four stories exercise.

(d) **Bulk operations (tag sweep, index rebuild, audit)** — These are mentioned in CLAUDE.md's escalation boundaries as "externally triggered operation class" but don't map to any of the four user stories. They have distinct context needs: they require loading many notes at once rather than the sequential hop pattern the decomposition assumes.

**Claim 11: "Answer a question rarely escalates because it's a read-only scenario."** The note's own counterexample (methodology questions in installed projects) partially undermines the "rarely" claim. More importantly, the reasoning "read-only therefore no escalation" doesn't follow — an agent answering a question about writing conventions or link semantics would need the same methodology depth as one doing a write, even though no file is created.

**Claim 12: Six architectural principles.** The note lists six principles that "fall out" of the decomposition. The implicit claim is that these are the complete set of architectural insights derivable from the analysis.

Boundary case: **Cross-scenario context reuse.** The note observes that "find related notes" is shared across scenarios, but doesn't derive an architectural principle about caching or context sharing between scenario steps. If the agent writes a note and then needs to connect it, the "find related notes" results from step 1 are relevant to the connection step — but nothing in the architecture addresses whether this context is preserved or must be regenerated. Given the agent-statelessness constraint, this seems like a real architectural concern the decomposition could surface.

---

**Step 3: Grounding alignment**

**Claim against scenarios.md:** The note says scenarios.md "describes what the KB is used for" and uses it as the foundation for the four user stories. Scenarios.md actually describes only two scenarios: "upstream change analysis" and "proposing our own changes." The note's four user stories (write a note, ingest a source, respond to a change, answer a question) are a significant expansion. "Respond to a change" maps roughly to "upstream change analysis," but "write a note," "ingest a source," and "answer a question" are not in scenarios.md at all. The note frames this as decomposing the scenarios, but it is actually expanding the scenario set. The link label says "foundation: defines the concrete use cases this note decomposes" — this overstates the relationship; the note builds on and substantially extends what scenarios.md provides.

**Claim against commonplace-installation-architecture.md:** The note says the installation architecture "reasons about read and write as abstract operations and optimizes for hop count." The installation architecture note does discuss reads and writes as operations and includes hop-count tables. This characterization is accurate. The note also claims its decomposition "confirms the two-tree design" — the installation architecture note does argue for two trees (user kb/ vs framework commonplace/), and the scenario decomposition does support that argument via the escalation path analysis. This grounding checks out.

**Claim against instruction-specificity-should-match-loading-frequency.md:** The note says the decomposition "matches the instruction specificity should match loading frequency principle." The loading frequency note describes a hierarchy: CLAUDE.md (always) -> skill descriptions (always) -> skill bodies (on demand) -> task docs (on demand). The scenario decomposition's layered structure (always-loaded routing -> on-demand types/WRITING.md -> methodology fallback) does map to this hierarchy. Attribution is accurate.

**Claim against skills-derive-from-methodology-through-distillation.md:** The note says "everything is distilled into skills and the CLAUDE.md fragment" and that "distillation is not lossless." The distillation note does argue that skills are distilled from methodology notes, that the distillation is lossy, and that the source material remains valuable for edge cases. The note's use of these concepts is consistent with the source.

**Claim against agent-statelessness-makes-routing-architectural-not-learned.md:** The note says "there's no 'something feels off' intuition" for the agent when hitting edge cases. The statelessness note does describe this exact phenomenon — the "degradation cliff" where the agent falls from KB-augmented to generic LLM without any awareness signal. Attribution is accurate.

---

**Step 4: Internal consistency**

**Definition drift check on "escalation."** The note uses "escalation" to mean two slightly different things: (1) the agent recognizes a gap in distilled procedures and consults methodology (the explicit escalation path in the decomposition), and (2) the agent merely encounters methodology questions that require looking in commonplace/kb/ (the "answer a question" case). The first is a deliberate decision to seek deeper reasoning; the second is just routing to a different search scope. The note treats both under "escalation" without distinguishing them, which could blur the concept.

**Tension between "escalation is expensive but rare" (claim 8) and the gaps section.** The gaps section identifies escalation discoverability as a significant concern and notes that "the agent has no signal that it's in a case the distilled procedures don't cover." If the agent can't reliably recognize when escalation is needed, calling it "rare" is potentially misleading — it may be rarely triggered rather than rarely needed. The note partially acknowledges this ("no amount of routing can guarantee" the agent recognizes edge cases), but the framing in the common path section suggests escalation is a minor cost, while the gaps section suggests it's a significant design problem. This is a tension rather than a contradiction — both can be true — but the note doesn't explicitly reconcile them.

**Consistency between title claim and body.** The title says "scenario decomposition drives architecture." The body delivers on this — it decomposes scenarios and derives architectural principles. The title-body alignment is good.

**Summary faithfulness.** The note has no compressed summary section, so this check is not applicable.

---

WARN:
- [Grounding alignment] The note claims scenarios.md is the "foundation: defines the concrete use cases this note decomposes," but scenarios.md only contains two scenarios (upstream change analysis, proposing own changes). Three of the four user stories in this note (write a note, ingest a source, answer a question) do not appear in scenarios.md. The note expands the scenario set rather than decomposing it — the link label overstates the grounding relationship.
- [Completeness] The four user stories omit maintenance-class operations (refactoring, merging, deleting, bulk operations). These have structurally different context needs — graph-aware rather than sequential-hop — and the note's decomposition framework doesn't account for them. CLAUDE.md itself acknowledges these as a distinct "externally triggered operation class," suggesting the note's scenario set is incomplete for its stated purpose of deriving architectural requirements.

INFO:
- [Completeness] "Answer a question rarely escalates because it's a read-only scenario" is weakened by the note's own counterexample (methodology questions in installed projects) and by the observation that read-only analysis of methodology-laden content requires the same depth as write operations. The "read-only therefore no escalation" inference is not airtight.
- [Internal consistency] Minor definition drift on "escalation" — used for both the deliberate gap-recognition-and-methodology-consultation pattern and the simpler case of routing methodology questions to commonplace/kb/. These are structurally different (one involves recognizing a gap; the other is just search-scope selection) but are treated as the same concept.
- [Internal consistency] Tension between "escalation is expensive but rare" (common path section) and the gaps section's emphasis on escalation discoverability as a significant design problem. If the agent cannot reliably detect when escalation is needed, the actual frequency of needed-but-missed escalations is unknown, making the "rare" characterization unverifiable.
- [Completeness] The six architectural principles don't address cross-scenario context reuse — whether context gathered in one step (e.g., "find related notes") can be preserved for later steps (e.g., "connect to existing knowledge") within the same session. Given that agent statelessness is a central concern of the linked notes, this seems like a derivable architectural insight the decomposition could surface.

PASS:
- [Grounding alignment] Attribution to commonplace-installation-architecture.md is accurate — that note does reason about read/write as abstract operations with hop counts, and this note's decomposition does confirm the two-tree design.
- [Grounding alignment] Attribution to instruction-specificity-should-match-loading-frequency.md is accurate — the loading hierarchy maps correctly onto the step-frequency patterns in the decomposition.
- [Grounding alignment] Attribution to skills-derive-from-methodology-through-distillation.md is accurate — the distillation-is-lossy claim and the escalation-as-distillation-gap framing are both supported by the source note.
- [Grounding alignment] Attribution to agent-statelessness-makes-routing-architectural-not-learned.md is accurate — the "no 'something feels off' intuition" claim and the degradation cliff concept are faithfully represented.
- [Internal consistency] The title claim ("scenario decomposition drives architecture") is well-supported by the body — the note performs the decomposition and derives architectural principles from it.
- [Internal consistency] The two operating contexts (commonplace repo vs installed project) are consistently maintained throughout the note — the common path, escalation path, and gap analysis all correctly distinguish between the two contexts.

Overall: 2 warnings, 4 info
===
