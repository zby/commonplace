=== SEMANTIC REVIEW: agent-statelessness-means-the-context-engine-should-inject-context-automatically.md ===

Claims identified: 14

---

**Claims extracted:**

1. "agents can't carry definitions, decisions, or vocabulary between reads" (opening paragraph)
2. "An agent that reads a note linking to codification doesn't know the definition unless it follows the link — at the cost of a tool call, context space, and a decision" (opening paragraph)
3. "when the context engine loads a document, it identifies references that the agent will need and injects appropriate content" — the core claim (paragraph 2)
4. "This extends document affordances from 'what operations can I perform on this document' to 'what context gets loaded alongside this document'" (paragraph 2)
5. Definitions are the cleanest case for auto-injection — four enumerated properties: small, stable, referential not argumentative, should be loaded once per session (Evidence section)
6. "The current three definitional notes (codification, constraining, distillation) are type: note" — scope claim (The definition type section)
7. A `type: definition` would signal auto-injection, assert structural properties, formalize topical title exception, prevent unbounded growth — four-item enumeration (The definition type section)
8. Four-row table of injection candidates: definitions, area indexes, ADRs, specs — each with trigger and rationale (Beyond definitions section)
9. The loading hierarchy has four levels: always, on reference, on invoke, on demand (Reasoning section)
10. "on reference" sits between "always loaded" and "on demand" (Reasoning section)
11. "Requires our own agent runtime" — there is no interception point on someone else's runtime (Caveats)
12. Four caveats enumerated: context budget, staleness, granularity, discovery (Caveats)
13. "The context engine could track which definitions have been injected and skip duplicates" (Evidence section)
14. Link to Harness Engineering source claims it "extends auto-injection from documents to runtime state" (Relevant Notes)

---

WARN:

- [Completeness] The four-row injection candidate table ("Beyond definitions") claims to identify candidate types for auto-injection but the selection criteria are unstated. The note names definitions, area indexes, ADRs, and specs. Boundary case: **instructions and skills themselves**. A note referencing a skill or instruction faces the same problem — the agent does not know the instruction's content unless it follows the link. Instructions are referenced from methodology notes and could benefit from injection when relevant. The omission is notable because the note's own Reasoning section describes the loading hierarchy (which includes skills at the "on invoke" layer) but never asks whether the "on reference" injection pattern could apply to skills. This may be intentional (skills have their own loading mechanism) but the table presents as covering the injection space without articulating why skills are excluded.

- [Grounding alignment — scope mismatch with "document types should be verifiable"] The note claims to extend the document affordances concept: "This extends document affordances from 'what operations can I perform on this document' to 'what context gets loaded alongside this document.'" The linked source (document-types-should-be-verifiable.md) defines affordances as what the *processor* (agent) can do with a document — "types guide what the processor can do with the document." The extension to "what context gets loaded alongside" is not an affordance of the document type in the source's sense; it is a behavior of the context engine triggered by the type. The source discusses types as navigation hints the agent reads before opening a document; the note repurposes "affordance" to mean automatic side-effects of loading. The inference is plausible but the vocabulary shift could mislead readers into thinking the source already contemplates injection-style affordances when it does not.

- [Grounding alignment — Harness Engineering link] The Relevant Notes section claims the Harness Engineering source "extends auto-injection from documents to runtime state." The source (harness-engineering-leveraging-codex-agent-first-world.ingest.md) describes dynamic observability via DevTools Protocol — wiring metrics, logs, and spans into the agent's context. This is indeed providing context the agent did not request, but the mechanism is fundamentally different: it is runtime telemetry pushed into context, not document references resolved at load time. Calling this an extension of "auto-injection" conflates two distinct operations (document reference resolution vs. runtime state observation) under a single label. The ingest itself uses more cautious language: "extends automatic context injection beyond documents to runtime state — a dimension the note does not yet cover." The note's link description drops the "dimension the note does not yet cover" qualifier.

INFO:

- [Completeness — boundary case: conflicting definitions] The note argues definitions are "stable" and "referential, not argumentative." Boundary case: when two notes define the same term differently, or when a definition evolves during a period of active development. The note's once-per-session injection model assumes definitions are uncontested. The staleness caveat partially addresses temporal drift, but not simultaneous definitional conflict. In a growing KB, definitional divergence is plausible (e.g., "distillation" might acquire a second note with a competing definition). The framework does not account for this case.

- [Completeness — boundary case: injection depth] The note discusses injecting definitions referenced by a loaded document, but what about definitions referenced by the *injected* definitions? If definition A references definition B, does auto-injection recurse? The note is silent on injection depth. This is a real design question: recursive injection could blow the context budget; single-level injection could leave the agent with incomplete vocabulary. The "imported constants" analogy from programming actually highlights this gap — imports in programming languages do resolve transitively.

- [Internal consistency — "on reference" placement] The Reasoning section places "on reference" between "always" and "on invoke" in the hierarchy, but the trigger mechanisms are fundamentally different. "Always" and "on invoke" are controlled by the system architecture (CLAUDE.md is always loaded; skills load on slash command). "On reference" is triggered by document content — it requires parsing loaded documents and resolving links. The note treats these as points on a single continuum, but they differ in implementation complexity and failure modes. The hierarchy presentation may suggest a smoother gradient than actually exists.

- [Completeness — the "imported constants" analogy] The note says definitions should "behave like imported constants in a programming language: declared once, available everywhere in scope." But imported constants in programming are explicitly declared by the programmer at each usage site — the programmer decides what to import. Auto-injection removes that decision from the agent. A closer analogy might be implicit imports or auto-imports (as in some IDEs), which have known failure modes: namespace pollution, unexpected shadowing, difficulty reasoning about what is in scope. The analogy as stated understates the design risk.

- [Grounding alignment — human-LLM differences link] The link to human-llm-differences-are-load-bearing-for-knowledge-system-design.md claims "the 'cannot fill gaps' row in the dual-audience table is exactly the problem context injection addresses." The source does contain a table row about LLMs being unable to fill gaps, and it does mention context injection as a complementary response to tier separation. However, the source frames context injection as addressing "what must be present for the agent to reason correctly" — a broader framing than this note's focus on definitions and ADRs. The attribution is accurate but the source treats injection as one half of a dual response (tier separation + injection), while this note focuses exclusively on injection without addressing how it interacts with tier separation for the same document.

PASS:

- [Internal consistency — core argument] The central argument chain holds: (1) agents are stateless, (2) therefore they lack definitions unless explicitly loaded, (3) therefore the context engine should inject referenced definitions automatically. Each step follows from the previous without contradiction. The Caveats section acknowledges genuine limitations (runtime requirement, budget, staleness, granularity, discovery) without undermining the core claim. The note's self-declared "speculative" status appropriately signals the maturity level.

- [Grounding alignment — agent statelessness source] The foundational link to agent-statelessness-makes-routing-architectural-not-learned.md is accurately used. That note does establish that agents "cannot develop navigation intuition" and that "every session is day one." The note's inference — that if agents cannot carry knowledge between sessions, then the context engine should inject referenced context — is a valid extension of the source's argument. The source itself notes that "if the specific routing isn't loaded, it doesn't exist," which directly supports the need for injection.

- [Grounding alignment — instruction specificity source] The link to instruction-specificity-should-match-loading-frequency.md accurately describes its four-level hierarchy (CLAUDE.md, skill descriptions, skill bodies, task-specific docs). The note's claim to add an "on reference" layer between "always loaded" and "on demand" is a genuine extension, not a misattribution. The source does not contemplate reactive loading; the note correctly identifies this as its own contribution.

- [Internal consistency — definition type proposal] The four properties of the proposed `definition` type (signal auto-injection, assert structural properties, formalize topical title exception, prevent unbounded growth) are internally consistent and non-overlapping. The note correctly identifies that a definition needing Evidence/Reasoning/Caveats sections is really a structured-claim — this boundary criterion is coherent with the KB's existing type system.

- [Completeness — caveats coverage] The four caveats (context budget, staleness, granularity, discovery) cover the most obvious failure modes of the proposal. The context budget caveat gives a concrete estimate (4-5K tokens for 20 terms). The discovery caveat correctly identifies term detection as a harder problem than link detection. The note does not oversell the proposal.

Overall: 3 warnings, 4 info
===
