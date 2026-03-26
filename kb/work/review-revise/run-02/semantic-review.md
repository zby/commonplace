=== SEMANTIC REVIEW: baseline.md ===

Claims identified: 16

---

### Claims extracted

1. **[Opening]** "Storing execution history and loading it into the next agent call are separate decisions" — the title claim.
2. **[Opening]** "In the bounded-context orchestration model, storage in `K` is cheap; bounded context is expensive."
3. **[Opening]** "The mistake is not storing a trace. The mistake is letting a session runtime decide that stored history should automatically become the next call's context instead of letting `select(K)` choose."
4. **[Paragraph 2]** "The conflation arises one layer above the model itself" — the orchestration model does not require chat history or a tool loop; higher-level interfaces introduce the conflation.
5. **[Where the problem actually appears]** Three higher-level interfaces cause the problem: chat sessions, framework-owned tool loops, continuing agent sessions.
6. **[Where the problem actually appears]** "The packaging layer starts deciding what later calls inherit — and it defaults to 'everything.'"
7. **[Why chat sessions and tool loops default...]** "Raw history is the easiest way to preserve maximum information when the caller does not yet know what matters."
8. **[Why chat sessions and tool loops default...]** "This makes transcript inheritance a sensible exploratory default."
9. **[Why transcript inheritance breaks down]** Five-item enumeration of costs: receives more than needed; local tactical debris survives; downstream stages must re-interpret; interfaces remain implicit; context pollution compounds.
10. **[Why transcript inheritance breaks down]** "This is the return-value problem from the scoping note in architectural form."
11. **[The right split]** Three-type trace taxonomy: conversation transcripts, tool/action traces, reasoning traces — with different loading profiles.
12. **[The right split]** Ordering claim: "The argument against loading traces as next-context is sharpest for reasoning traces, strong for conversation transcripts, and most nuanced for tool traces."
13. **[The right split]** "The key separation is not 'store vs discard' but 'persist in symbolic state vs load into bounded context.'"
14. **[Tension: Slate]** Slate workers return episodes — "compressed representations of what happened during a bounded action" — fitting the anti-transcript argument.
15. **[Execution-boundary compression]** "Across these systems, the shared move is compression at the execution boundary" — four exemplars cited.
16. **[The practical principle]** Four-part guidance: store more than you load; use trace-preserving storage early; move toward artifact-first loading; keep raw trace as auxiliary substrate.

---

### Step 2: Completeness and boundary cases

#### Framework A: Three higher-level interfaces (claim 5)

The note names chat sessions, framework-owned tool loops, and continuing agent sessions as the sources of the conflation.

Boundary cases:

1. **Simplest instance: a single SDK call with no state.** No history exists, so no conflation is possible. The note implicitly acknowledges this ("With raw SDK calls, there is no built-in transcript problem"). PASS — the framework correctly excludes the simplest case.

2. **RAG pipeline with retrieval context passed forward.** A system assembles retrieved documents into the next prompt. This is not a chat session, not a tool loop, and not a "continuing agent session" — it is application code passing retrieval results forward. Yet if the retrieval results accumulate without pruning, the same "everything gets inherited" problem can arise. INFO — the three categories focus on conversation/session-shaped interfaces and may undercover non-conversational context accumulation patterns (e.g., retrieval pipelines, shared scratchpads) that produce the same pathology through a different mechanism.

3. **Human-in-the-loop multi-turn editing.** A human reviews agent output, gives corrections, and the cycle repeats with full history. This straddles "chat session" and "continuing agent session" but the human's corrections are signal-dense, not debris. The blanket claim that transcript inheritance "defaults to everything" is less clearly a mistake here because the human is actively curating. INFO — the note's framing assumes the inherited content is mostly noise; the argument is weaker when the accumulated transcript is signal-rich (e.g., expert-driven correction loops).

4. **Persistent memory systems (e.g., MemGPT-style).** These maintain an external memory bank and selectively page content in/out across calls. They are neither chat sessions nor tool loops, but they share the "what to load next" question. The note's framework doesn't clearly address memory-augmented architectures that are already performing selective loading but still face the conflation problem at the memory-retrieval level. INFO — the three-category framing covers the most common cases but doesn't address memory-augmented architectures where selective loading is attempted but the selection policy may still default to recency (producing a subtler version of the same problem).

#### Framework B: Three trace types (claim 11)

The note distinguishes conversation transcripts, tool/action traces, and reasoning traces.

Boundary cases:

1. **Structured data artifacts (JSON, tables, code).** A tool call returns a JSON object that is both a tool trace and a structured deliverable. The note acknowledges this ("sometimes the trace *is* the deliverable" for tool traces). PASS — the taxonomy handles this via the tool-trace category.

2. **Error/failure traces.** The note explicitly addresses failure handling in the paragraph following the taxonomy: "A bounded execution may return a structured failure artifact while the raw trace is stored separately." PASS — failure traces are covered.

3. **Planning/goal traces.** An agent produces a plan (sub-goals, task decomposition). This is neither conversation, nor tool/action, nor reasoning in the narrow sense. It is closer to reasoning but is often a deliverable that the next call *should* load. The note's ordering claim — "argument against loading is sharpest for reasoning traces" — would apply to plans, yet plans are one of the strongest cases for loading. WARN — planning artifacts (sub-goal decompositions, task plans) sit between "reasoning traces" and "tool traces" in the taxonomy. The ordering claim that reasoning traces are "almost never worth loading into the next call" becomes problematic when the reasoning trace *is* a plan that the scheduler needs to execute. The bounded-context orchestration model note itself describes planning calls whose output is loaded into subsequent iterations. The taxonomy does not clearly place plans, and the ordering claim may be too strong for this case.

4. **Compressed episode (Slate-style).** The note discusses this in the Tension section. It acknowledges episodes are "more trace-shaped than a narrow result" and flags this as a tension case. PASS — explicitly handled.

5. **Agent self-assessment / confidence scores.** An agent returns both a result and a confidence assessment. The confidence assessment is metadata about reasoning, not a conversation, tool action, or reasoning chain itself. INFO — meta-cognitive outputs (confidence scores, uncertainty flags, self-assessments) don't map cleanly to any of the three trace types. They are closer to structured return values than traces, suggesting the taxonomy may be missing a "structured result metadata" category that is distinct from all three trace types.

#### Framework C: Four-part practical principle (claim 16)

Boundary cases:

1. **The "right" interface is already known at design time.** The principle says to use trace-preserving storage early "when you do not yet know the right interface." But some tasks have well-understood interfaces from the start (e.g., classification, extraction with known schema). For these, starting with full trace preservation is unnecessary overhead. INFO — the temporal progression (trace-preserving early, artifact-first later) assumes interface uncertainty. When the interface is known upfront, the "early" phase can be skipped, but the principle doesn't say this explicitly.

---

### Step 3: Grounding alignment

**Source 1: bounded-context-orchestration-model.md**

The baseline claims (2, 3) that "storage in `K` is cheap; bounded context is expensive" and that `select(K)` is the right control point for what enters the next call. The orchestration model note confirms this directly: "`K` accumulates over the loop" and "the `select` function builds a prompt `P` from the current state `K`, subject to the feasibility constraint." The baseline's characterization is accurate. PASS — the baseline's use of the orchestration model's `K` / `select(K)` terminology and semantics aligns with the source.

**Source 2: llm-context-is-composed-without-scoping.md**

The baseline (claim 10) says the costs of transcript inheritance are "the return-value problem from the scoping note in architectural form." The scoping note's "return value problem" section discusses what sub-agents return and frames it as an interface question: "A function returns a typed value. A sub-agent returns natural language." The scoping note's point is about the *absence of explicit interfaces between stages* — the baseline's restatement as the same problem "in architectural form" is accurate, since the baseline is discussing how the lack of explicit return artifacts between orchestration stages produces the same consequences at system scale. PASS — the attribution to the scoping note is faithful. The scoping note does discuss how flat context prevents explicit contracts between stages, which is exactly what the baseline claims transcript inheritance perpetuates.

**Source 3: the-chat-history-model-trades-context-efficiency-for-implementation-simplicity.md**

The baseline (claims 7-8) cites this note for the claim that chat history is a "sensible exploratory default." The source note confirms this precisely: "Chat is a strong exploratory default" and "When the right handoff artifact is not yet known, preserving the transcript avoids premature compression." The source also states the note is about an "architectural tradeoff" while the baseline is the "mechanism-level claim" — this relationship is correctly reflected in the baseline's Relevant Notes section. PASS — the baseline faithfully represents the chat-history note's argument and correctly positions itself as downstream.

**Source 4: tool-loop-index.md**

The baseline (claim 4) says the conflation "arises one layer above the model itself" when higher-level interfaces package bounded calls as sessions. The tool loop index describes this: frameworks "own this loop because the mechanics are repetitive protocol work" and the question is "who gets to decide what the next step *can do*." The index's downstream consequences list explicitly includes "session history should not be the default next context — sub-tasks should start with constructed prompts, not inherit the parent's full conversation." PASS — the baseline's characterization of the tool loop as a packaging layer that introduces transcript inheritance is consistent with the tool loop index.

**Source 5: definitions/distillation.md**

The baseline (claim 15) says "the shared move is compression at the execution boundary" and links to distillation.md for the mechanism. The distillation note defines distillation as "compressing knowledge so that a consumer can act on it within bounded context." The baseline's "execution-boundary compression" is a specific application of this general definition — compression at a particular architectural point (the execution boundary) targeting a specific consumer (the next bounded call). The baseline does not claim distillation says anything about execution boundaries specifically; it uses distillation as the mechanism label. PASS — the attribution is appropriate. Execution-boundary compression is an instance of distillation as defined by the source.

---

### Step 4: Internal consistency

1. **Pairwise contradiction check.**

   The note says transcript inheritance is "a sensible exploratory default" (claim 8) and later says "The default mistake is to let a chat interface or framework-owned tool loop decide what the next bounded call should inherit" (final paragraph). These are not contradictory because the first is qualified ("early in a design, when the real interface between stages is still unknown") and the second refers to production orchestration. The temporal qualifier resolves the apparent tension. PASS — the note consistently distinguishes the exploratory phase (where trace preservation is appropriate) from the mature orchestration phase (where it becomes costly).

2. **Definition drift check.**

   "Trace" is used in multiple senses: (a) raw execution history, (b) the three-type taxonomy (conversation/tool/reasoning), (c) compressed episodes as "trace-shaped." The note is generally careful to qualify which sense it means, though the phrase "trace-preserving storage" in the practical principle (claim 16) leaves it slightly ambiguous whether it means "store the raw trace" or "store something trace-shaped." INFO — "trace" carries multiple meanings across the note. The practical principle's "trace-preserving storage" is slightly ambiguous — it could mean "store everything raw" or "store in a format that preserves trace structure." Context suggests the former, but the phrasing could be tighter.

3. **Compressed summary check.**

   The description field says: "Storing execution history and loading it into the next agent call are separate decisions; chat and framework-owned tool loops conflate them by making session history the default next context." This faithfully captures the title claim and the mechanism. It does not mention the three-type trace taxonomy or the practical principle, but a description is a retrieval filter, not a summary. PASS — the description accurately represents the note's central argument.

4. **Section consistency on the ordering claim.**

   The "right split" section claims the argument against loading is "most nuanced for tool traces." The execution-boundary compression section then gives Slate episodes as an exemplar, noting they are "more trace-shaped than a narrow result." These are consistent — the Slate case is presented as a tension, not a counter-example. PASS — the ordering claim and the Slate tension section are consistent; the note correctly flags Slate as a boundary case rather than a refutation.

---

WARN:
- [Completeness — three trace types] Planning artifacts (sub-goal decompositions, task plans) sit between "reasoning traces" and "tool traces" in the taxonomy. The ordering claim that reasoning traces are "almost never worth loading into the next call" becomes problematic when the reasoning trace *is* a plan the scheduler needs to execute. The bounded-context orchestration model note itself describes planning calls whose output enters `K` and is loaded into subsequent iterations (lines 56, 78-80 of that note). The baseline's taxonomy does not clearly place plans, and the ordering claim may be too strong for this case.

INFO:
- [Completeness — three interfaces] The three categories (chat sessions, tool loops, continuing sessions) focus on conversation-shaped interfaces. Non-conversational context accumulation patterns (RAG pipelines, shared scratchpads, memory-augmented systems) can produce the same "everything gets inherited" pathology through different mechanisms not addressed by the taxonomy.
- [Completeness — three interfaces] The note assumes inherited content is mostly noise. The argument is weaker for signal-rich accumulation contexts (e.g., expert-driven correction loops) where the transcript carries high information density.
- [Completeness — three trace types] Meta-cognitive outputs (confidence scores, uncertainty flags, self-assessments) do not map cleanly to any of the three trace types, suggesting the taxonomy may be incomplete for structured result metadata.
- [Completeness — practical principle] The temporal progression (trace-preserving early, artifact-first later) assumes interface uncertainty. When the interface is known upfront, the guidance does not explicitly say the early phase can be skipped.
- [Internal consistency] "Trace" carries multiple meanings across the note. The practical principle's "trace-preserving storage" is slightly ambiguous — it could mean "store everything raw" or "store in a format that preserves trace structure."

PASS:
- [Completeness — three interfaces] The simplest case (single SDK call, no state) is correctly excluded by the note's own framing.
- [Completeness — three trace types] Structured data deliverables, failure traces, and compressed episodes are all accounted for in the taxonomy or in explicit tension sections.
- [Grounding — bounded-context orchestration model] The baseline's use of `K`, `select(K)`, and the storage-is-cheap / context-is-expensive framing aligns with the source note.
- [Grounding — scoping note] The "return-value problem in architectural form" attribution faithfully represents the scoping note's argument about absent interfaces between stages.
- [Grounding — chat-history note] The "sensible exploratory default" characterization matches the source note verbatim and the directional relationship (this note downstream of that one) is correctly stated.
- [Grounding — tool loop index] The packaging-layer characterization is consistent with the tool loop index's argument about framework ownership.
- [Grounding — distillation] Execution-boundary compression is a faithful application of the distillation definition; no scope mismatch.
- [Internal consistency] The "sensible exploratory default" and "default mistake" claims are not contradictory — temporal qualification resolves the apparent tension.
- [Internal consistency] The description faithfully represents the note's central argument.
- [Internal consistency] The ordering claim and Slate tension section are consistent; the note correctly flags Slate as a boundary case.

Overall: 1 warning, 5 info
===
