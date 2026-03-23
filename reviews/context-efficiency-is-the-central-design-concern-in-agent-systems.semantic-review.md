<!-- REVIEW-METADATA
note-path: kb/notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md
last-full-review-note-sha: 80f97c9d23096e48eeae1c65fbd2638ee3280057
last-full-review-note-commit: 5d0771d0710a683a620be574bcc3f3b86bbdb60b
last-full-review-at: 2026-03-23T09:32:55+01:00
last-accepted-note-sha: 80f97c9d23096e48eeae1c65fbd2638ee3280057
last-accepted-note-commit: 5d0771d0710a683a620be574bcc3f3b86bbdb60b
last-accepted-at: 2026-03-23T09:32:55+01:00
last-acceptance-kind: full-review
review-type: semantic-review
-->
=== SEMANTIC REVIEW: context-efficiency-is-the-central-design-concern-in-agent-systems.md ===

Claims identified: 14

## Step 1: Claims extracted

1. "In agent systems, the scarce resource is context — the finite window of tokens the agent can attend to." (opening paragraph)
2. "Context is not just another resource. It is the *only channel* through which an agent receives instructions, understands its task, accesses knowledge, and reasons toward action." (opening paragraph)
3. "A CPU has registers, cache, RAM, disk, and network as separate tiers. An LLM has one context window. Everything competes for the same space." (opening paragraph)
4. "Context is the lowest-degree-of-freedom resource in agent systems: unitary within each inference call, impossible to tier at the attention level (though system architecture can build tiers around it), and hard to expand without architectural change." (second paragraph)
5. "The binding constraint is soft degradation, not hard token limits." (third paragraph)
6. "Extra context doesn't just waste space — it can dilute instructions, contaminate scopes, and distort interpretation." (end of intro)
7. "The soft bound operates across two dimensions — volume (how many tokens) and complexity (how hard they are to use)." (Volume and complexity section)
8. "The dimensions are distinguishable but not fully separable; reducing volume often reduces complexity as a side effect." (Volume and complexity section)
9. Koylan's Personal Brain OS reduced token usage for voice-only tasks by 40% by splitting merged modules into isolated scopes — "a pure volume intervention." (Volume and complexity section)
10. "Nominal context windows have grown at roughly 30x per year since mid-2023." (Growing windows section)
11. "Growing windows address volume but not complexity. A five-level indirection chain is equally costly whether the window is 8K or 2M tokens." (Growing windows section)
12. "Context demand grows with task ambition — richer tool outputs, longer histories, more complex instructions. This is a Jevons paradox." (Growing windows section)
13. Six architectural responses enumerated as the set of patterns context scarcity produces. (Architectural responses section)
14. "The natural computational model is symbolic scheduling over bounded LLM calls." (Architectural responses section)

## Step 2: Completeness and boundary cases

**Framework under test: The six architectural responses to context scarcity.**

The note claims "context scarcity produces most architectural patterns in agent system design" and lists six responses: frontloading/partial evaluation, progressive disclosure, context management, sub-agent isolation, navigation design, and instruction notes over data dumps.

Boundary cases:

1. **Caching / memoization of LLM outputs.** An agent system that caches results of prior LLM calls and replays them instead of re-deriving answers. This saves context by avoiding re-derivation but does not cleanly fit frontloading (which is pre-computing at build time, not runtime caching) or context management (which the note scopes to compaction, observation masking, and sub-agent delegation). It sits between the two.

2. **Tool-call offloading (moving computation out of context entirely).** When an agent calls a calculator, a code interpreter, or a database query, computation happens outside the context window. The note mentions "symbolic scheduling over bounded LLM calls" but the enumerated architectural responses list does not name tool offloading as a pattern, despite it being one of the most basic ways to avoid spending context on non-semantic work. The bounded-context orchestration model reference gestures at this, but the list is presented as the set of patterns and tool offloading is absent.

3. **Retrieval-augmented generation (RAG).** RAG systems dynamically load relevant chunks rather than pre-loading everything. This partially maps to "navigation design" but has a distinct mechanism: an external retrieval system, not the agent's own navigation judgment, selects what enters context. The note's framing emphasizes agent-driven navigation decisions; retrieval-system-driven selection is a different mechanism serving the same goal.

4. **Prompt compression / distillation of instructions themselves.** Rewriting verbose instructions into terse equivalents that convey the same information in fewer tokens. This targets volume directly and complexity as a side effect. It could be forced into "context management" but the note describes that category as "compaction, observation masking, and sub-agent delegation" — runtime techniques for managing accumulation, not pre-flight compression of the instruction surface itself.

5. **Conversation reset / fresh context starts.** Deliberately terminating a conversation and starting fresh rather than continuing with accumulated history. This is a common practitioner response to soft degradation that does not clearly map to any of the six responses. It is a brute-force volume intervention.

**Framework under test: "Context is unitary within each inference call, impossible to tier at the attention level (though system architecture can build tiers around it)."**

Boundary cases:

1. **Multi-modal context (images, audio).** Images and audio enter the context window but are processed through different encoders before reaching attention. Whether a diagram "competes for the same space" in the same way as text tokens is unclear — the note's model assumes a homogeneous token stream. The parenthetical qualifier ("within each inference call") helps, but multi-modal inputs may not compete symmetrically with text tokens even within a single call.

2. **Structured decoding / constrained generation.** Techniques like JSON-mode or grammar-constrained decoding alter how the model processes context by restricting the output distribution. This is not exactly tiering, but it changes the effective cost of context by narrowing interpretation space — a mechanism the note does not account for in its cost model.

## Step 3: Grounding alignment

**Claim: Koylan reduced token usage for voice-only tasks by 40% by splitting merged modules into isolated scopes — "a pure volume intervention."**
Source checked: `kb/sources/koylanai-personal-brain-os.md`

The current note text now includes the qualifier "for voice-only tasks," which was missing in a prior version. Attribution of the 40% figure is accurate. The note characterizes this as "a pure volume intervention," which aligns with the source's description of splitting modules to avoid loading irrelevant content. The note no longer makes the unsupported "outsized impact on agent reliability" claim present in an earlier version. The note adds "The key point for this note: large windows do not remove complexity costs, and raw token count alone does not predict usable context" — this inference goes beyond what the Koylan source demonstrates (the source shows a volume saving, not evidence about complexity costs), but is flagged as the note's own interpretive addition rather than attributed to the source.

**Claim: Lopopolo's Codex team shipped 1M lines of agent-generated code, required a 100-line AGENTS.md as "a map, not a manual," because "the bottleneck was not model capability but the structure of the environment — tools, feedback, and constraints, of which context structure is a central component."**
Source checked: `kb/sources/harness-engineering-leveraging-codex-agent-first-world.md`

The current note text has improved from an earlier version. It now attributes the bottleneck to "the structure of the environment — tools, feedback, and constraints" and positions context as "a central component" of that broader picture, rather than claiming the bottleneck was purely context. The source's key lesson #7 says: "The bottleneck was the environment, not the model." The source explicitly distinguishes harness engineering from context engineering. The note's current framing — context as a central component of a broader environmental bottleneck — is a reasonable characterization, though the note's overall thesis (context efficiency is THE central design concern) still claims more centrality for context than the Lopopolo source supports. The source treats context as one of several co-equal environmental factors.

**Claim: Anthropic defines context engineering as "strategies for curating and maintaining the optimal set of tokens during LLM inference" and describes context as "a critical but finite resource" with an "attention budget" that "every token depletes."**
Source: Anthropic (2025) blog post (external URL, not followed — taken at face value as a direct quote).

**Claim: The soft-bound premise and two-dimensions decomposition come from the soft-degradation note.**
Source checked: `kb/notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md`

The soft-degradation note establishes volume and complexity as two dimensions and identifies soft degradation as the binding constraint. Attribution is accurate. The soft-degradation note links back to this note as "extends," confirming the intended dependency direction.

**Claim: Sub-agents provide "lexically scoped frames" with only what the caller explicitly passes.**
Source checked: `kb/notes/llm-context-is-composed-without-scoping.md`

The scoping note describes sub-agents as providing lexical scoping and uses the "lexically scoped frames" language. Attribution is accurate.

**Claim: Context is the lowest-degree-of-freedom resource, per the solve-low-DoF-first principle.**
Source checked: `kb/notes/solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking-better-designs.md`

The low-DoF note describes a general sequencing heuristic: commit the least flexible decision first. The note under review applies this by asserting that context is the lowest-degree-of-freedom resource. The low-DoF note itself does not identify context as a low-DoF resource — that identification is this note's own application. The application is reasonable but the "lowest" claim is an empirical assertion the source does not make.

## Step 4: Internal consistency

**Definition drift check: "tier" / "unitary."**
The opening paragraph now includes the parenthetical "(though system architecture can build tiers around it)" after claiming context is "impossible to tier at the attention level." This is an improvement over a prior version's unqualified "impossible to tier" — the qualifier explicitly acknowledges the tension between within-call unitariness and system-level tiering. The architectural responses section (sub-agent isolation, symbolic scheduling, context management) describes system-level tiering mechanisms. The parenthetical resolves what was previously an internal contradiction.

**Definition drift check: "context efficiency."**
The title claims context efficiency is "the central design concern." The body develops this through both volume and complexity dimensions. The final paragraph says "context efficiency should be evaluated at design time." The term is used consistently throughout.

**Summary faithfulness check.**
No compressed summary section is present, so this sub-check does not apply.

**Tension between "central" and the multi-factor evidence.**
The title claims context efficiency is "the central design concern." The Lopopolo source (cited approvingly) frames the bottleneck as the broader environment — tools, feedback, constraints — not just context. The note now acknowledges this by writing "of which context structure is a central component," which partially addresses the tension. However, the title's "THE central design concern" framing remains stronger than the cited evidence supports. Simon's attention economics and the working memory literature support attention as A scarce resource but do not establish it as THE central one over, say, feedback quality or tool design. The note's argument for centrality rests on the "only channel" claim — everything must pass through context — which is a structural argument the note makes on its own authority rather than one grounded in the cited sources.

WARN:
- [Completeness] The six architectural responses omit tool-call offloading (moving computation out of context entirely), which is arguably the most fundamental response to context scarcity. The bounded-context orchestration model reference gestures at this, but the enumerated list is presented as the set of patterns context scarcity produces, and offloading to deterministic tools is absent as a named pattern. This is notable because the note's own linked bounded-context orchestration model note treats the symbolic-scheduler/bounded-call separation — which IS tool offloading — as the foundational architecture, yet the enumerated responses list does not include it.
- [Grounding] The note's title claim — context efficiency is THE central design concern — is stronger than any individual cited source supports. The Lopopolo source explicitly frames the bottleneck as broader than context. Simon's attention economics establishes scarcity but not primacy over other design concerns. The Anthropic source calls context "a critical but finite resource" — critical, not central. The centrality claim is the note's own structural argument ("only channel"), which is reasonable but should be recognized as the note's own move rather than as something grounded in the cited evidence.

INFO:
- [Completeness] The six architectural responses do not clearly cover retrieval-augmented generation as a distinct mechanism. RAG is partially captured by "navigation design" but uses an external retrieval system rather than agent-driven navigation judgment — a different mechanism serving the same context-saving goal.
- [Completeness] Conversation reset (deliberately starting fresh to shed accumulated context) is a common practitioner response to soft degradation not mapped to any of the six listed responses.
- [Grounding] The "lowest-degree-of-freedom resource" characterization of context is presented as an application of the low-DoF principle, but the low-DoF source note does not identify context as a low-DoF resource — that identification is this note's own empirical claim. The inference is plausible but not sourced.
- [Grounding] The Koylan section draws the inference that "large windows do not remove complexity costs, and raw token count alone does not predict usable context" from a source that demonstrates only a volume-dimension saving. The note flags this as its own interpretive point ("The key point for this note"), which is transparent, but a reader might still read the Koylan citation as supporting the complexity claim when it only supports the volume claim.

PASS:
- [Completeness] The volume/complexity decomposition is well-grounded in the soft-degradation note and holds up under boundary testing. The distinction is clear, the interaction between dimensions is acknowledged ("distinguishable but not fully separable"), and the note correctly tags each architectural response with its primary dimension target.
- [Grounding] The soft-degradation premise attribution is accurate — the soft-degradation note establishes both dimensions and identifies soft degradation as the binding constraint. The dependency direction between the notes is clean and reciprocally acknowledged.
- [Grounding] The sub-agent/lexical-scoping attribution to the scoping note is accurate — the scoping note uses the same "lexically scoped frames" language and develops the same mechanism.
- [Grounding] The homoiconicity and underspecification references accurately describe the properties as stated in their respective source notes.
- [Grounding] The Lopopolo attribution has improved: the note now characterizes context as "a central component" of the broader environmental bottleneck rather than claiming the bottleneck is purely context. This is a more defensible framing than narrowing the source to context alone.
- [Consistency] The "unitary/impossible to tier" framing now includes the parenthetical "(though system architecture can build tiers around it)," which resolves the previous internal tension between the opening's unitariness claim and the body's description of system-level tiering via sub-agents and external state.
- [Consistency] The volume/complexity framework is applied consistently throughout the note — each architectural response is tagged with its primary dimension, and the Jevons paradox argument correctly targets volume only.
- [Consistency] The term "context efficiency" is used with stable meaning throughout the note.

Overall: 2 warnings, 4 info
===
