# Change catalogue: session-history note

Each change is a named, scorable unit. An experimental review+revise run scores a **hit** if it makes a change in the same direction (not necessarily identical text), a **miss** if it doesn't catch the problem, and a **mistake** if it introduces a new problem or moves in the wrong direction.

## Accessibility (A) — grounding insular language for outside readers

**A1: Define "execution boundary" inline.**
Baseline: "An execution boundary usually creates two different questions"
Problem: assumes reader knows what an execution boundary is.
Direction: add a gloss — "any point where one LLM call ends and another begins."

**A2: Replace K/select(K)/P notation with plain language in prose.**
Baseline: "storage in `K` is cheap", "letting `select(K)` choose", "assembles a prompt `P`, stores the result in `K`"
Problem: notation requires reading the orchestration model note to understand.
Direction: "the scheduler's state can store everything", "a deliberate selection step", "assembles a prompt, stores the result."

**A3: Identify Slate by maker.**
Baseline: "Slate is the main tension case"
Problem: reader doesn't know what Slate is.
Direction: "Random Labs' Slate" (factual correction — was also wrongly attributed to Anthropic in one intermediate version).

**A4: Remove "bounded call/context" jargon from body.**
Baseline: "The next bounded call should see", "the next bounded context", "a specific bounded call truly needs it"
Problem: "bounded call" is KB-internal vocabulary; opaque to outside readers.
Direction: plain "call" or "context" in the body; keep "bounded-context" only in the linked opening where it's defined.

## Clarity (C) — fixing ambiguous or misleading prose

**C1: Fix ambiguous "The mistake is not storing a trace."**
Baseline: "The mistake is not storing a trace. The mistake is letting..."
Problem: reads as "the mistake is [failing to store]" on first pass.
Direction: "Storing a trace is fine — the mistake is letting..."

**C2: Reframe "For orchestration" as cognitive-capacity argument.**
Baseline: "For orchestration, that is usually the wrong trade"
Problem: the issue isn't orchestration-specific — it's about any call needing full LLM capacity.
Direction: ground in soft degradation — "LLMs degrade with context complexity — every token spent parsing irrelevant history is cognitive budget not spent on the actual task."

**C3: Fix "return-value problem" link mismatch.**
Baseline: "This is the return-value problem from the scoping note in architectural form"
Problem: the scoping note's "return value problem" section is about *what* sub-agents return (typed vs. untyped), not about *leaking internal state*.
Direction: "the scoping problem in architectural form" → "In a properly scoped system, each sub-agent gets a clean frame and the caller sees only the return value."

**C4: Cut LLM-cliche "This is not just X — it is Y."**
Baseline: "This is not just summarization — it is interface design."
Problem: the "not just X — it is Y" pattern is a stock LLM rhetorical move that adds nothing.
Direction: delete the sentence; the following sentence already says what matters.

## Structure (S) — section-level flow and cohesion

**S1: Cut duplicate bridge paragraph.**
Baseline: L18 ("The conflation arises one layer above the model itself...") previews exactly what "Where the problem actually appears" then enumerates.
Direction: delete the bridge, go straight from opening to "How the conflation arises."

**S2: Merge "Where the problem appears" + "Why they default" into one section.**
Baseline: two sections covering the same subject (how we got here).
Direction: one section "How the conflation arises" ending with the rhetorical "Why does it default this way?"

**S3: Compress trace-types taxonomy.**
Baseline: three detailed bullets + two follow-up paragraphs + failure-handling paragraph (~15 lines).
Problem: the taxonomy wasn't load-bearing enough for its weight.
Direction: one sentence listing the types + one sentence stating the conclusion.

**S4: Fold "Conversation vs refinement" section into pattern section.**
Baseline: its own section with three bullets.
Problem: too thin for a standalone section — just another example of execution-boundary compression.
Direction: one bullet in the "Execution-boundary compression" list.

**S5: Reorder pattern before tension.**
Baseline: "Tension: Slate" comes before "Execution-boundary compression."
Direction: general pattern first, then the specific tension case.

**S6: Split "artifact-first" caveat into its own bullet.**
Baseline: long compound bullet in practical principles.
Direction: two separate bullets — the principle, then the clarification.

## Cosmetic (X) — minor formatting

**X1: Capitalize bullet items for visual consistency.**
**X2: Update distillation link path (./distillation.md → ./definitions/distillation.md).**

## Scoring template

| Change | Hit | Miss | Notes |
|--------|-----|------|-------|
| A1     |     |      |       |
| A2     |     |      |       |
| A3     |     |      |       |
| A4     |     |      |       |
| C1     |     |      |       |
| C2     |     |      |       |
| C3     |     |      |       |
| C4     |     |      |       |
| S1     |     |      |       |
| S2     |     |      |       |
| S3     |     |      |       |
| S4     |     |      |       |
| S5     |     |      |       |
| S6     |     |      |       |
| X1     |     |      |       |
| X2     |     |      |       |
| **Mistakes** | | | (list any new problems introduced) |
