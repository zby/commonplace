# Agent Memory Design Workshop

## Goal

Design an ideal memory system for agentic systems, grounded in the KB's existing theory and informed by the comparative review of 11 systems.

## Core premise

Symbolic storage is cheap and text storage is a solved problem. **Store everything** — all interaction session logs, all intermediate artifacts, all observations. The hard problem is not storage but **finding the right information at the right time** under bounded context.

"Store everything" is a working hypothesis, not a proven conclusion — it trades storage costs for indexing overhead, search pollution risk, and potential privacy exposure. The [open questions](#open-questions-to-explore) explore these costs directly. The bet is that selective retrieval can manage what aggressive storage introduces.

This inverts the emphasis of most memory system designs, which spend effort on what to store and how to compress. Instead:
- Storage: aggressive, complete, low-ceremony
- Retrieval/activation: where all the design intelligence lives

## Starting position from the KB

### What we know

1. **Context efficiency is the binding constraint** ([context-efficiency](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md)) — the basis for the core premise above.

2. **Storage does not imply activation** ([activation gap](../../notes/knowledge-storage-does-not-imply-contextual-activation.md)). Relevant knowledge can be present and still not surface. The bottleneck is whether the workflow asks the right questions.

3. **Store more than you load** ([session-history](../../notes/session-history-should-not-be-the-default-next-context.md)). Raw traces are valuable for learning and audit but should not automatically become the next call's context.

4. **Memory must serve action, not just retrieval** ([action-capacity](../../notes/claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md)). The system needs preferences, procedures, and judgment precedents — not just facts.

5. **The agency trilemma** ([comparative review](../../notes/related-systems/agentic-memory-systems-comparative-review.md)). The comparative review identifies a fundamental design tension: no system combines high agency, high throughput, and high curation quality.

6. **Lifecycle separation matters** ([three-space](../../notes/three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy-may-be-decorative.md)). Knowledge, self-knowledge, and operational artifacts have different metabolic rates. Flat memory predicts search pollution and insight trapping.

7. **Navigability vs retrieval** ([comparative review](../../notes/related-systems/agentic-memory-systems-comparative-review.md)). Vector search optimizes for QA; articulated link networks optimize for reasoning.

8. **Automated synthesis is the open frontier** ([comparative review](../../notes/related-systems/agentic-memory-systems-comparative-review.md)). Everyone automates extraction; nobody automates synthesis at production quality.

9. **Agent statelessness makes routing architectural** ([statelessness](../../notes/agent-statelessness-makes-routing-architectural-not-learned.md)). Every session is day one; routing infrastructure is permanent prosthetics.

### What the KB identifies as missing

- **Session logs** — currently not captured at all (noted in [workshop-layer](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md))
- **Automated memory evolution** — existing notes don't update when new notes arrive (A-MEM's key contribution)
- **Promotion heuristics** — no pathway from observation to durable knowledge beyond human review
- **Temporal reasoning** — no queryable model of how knowledge changes over time

## The user's key addition: session logs as primary input

Session interaction logs are a rich, underexploited substrate. They contain:
- **Decisions made** — what the user chose when alternatives were presented
- **Corrections** — where the agent went wrong and how it was redirected
- **Discoveries** — insights that emerged during work
- **Preferences** — implicit patterns in what the user accepts/rejects
- **Procedures** — workflows that recur across sessions
- **Questions asked** — what the user needs to know (activation cues for future sessions)

Since storage is cheap, the system should capture all of this. The design challenge is entirely in the retrieval/activation layer:
- How do you find the relevant precedent from 1000 sessions ago?
- How do you surface a correction made in session 47 when the same mistake is about to recur in session 312?
- How do you graduate a pattern observed across 5 sessions into an explicit preference?

## Use cases: how memory gets consumed

The design must be driven by how memory is used, not just how it's stored. Two use cases sharpen the requirements:

### Answering "why" — session logs as decision provenance

A recurring high-value question is: **why did we do it this way and not that way?** This is the question ADRs are designed to answer — but ADRs are manually authored summaries of decisions, written after the fact by someone who remembers the context.

Session logs contain the raw material that ADRs distill: the alternatives considered, the reasoning that led to a choice, the constraints that were active, the objections raised and addressed. The two approaches are complementary:

- **Session logs** provide *complete provenance* — every alternative weighed, every dead end explored, every correction made. They answer "why" questions the ADR author didn't anticipate, because they preserve what was discarded, not just what was chosen.
- **ADRs** provide *distilled decisions* — the conclusion, the key reasoning, the consequences. They answer "why" efficiently — one document instead of searching 20 session logs.
- **The bridge**: session logs make ADR writing cheaper (the material is already captured) and ADRs make session logs navigable (an ADR can point back to the sessions where the decision was actually made). An ADR is a distilled index into the relevant session logs.

This generalizes beyond ADRs. Any "why" question — why this architecture, why this naming convention, why this dependency — has an answer distributed across session logs. The memory system's job is to make that answer findable without requiring someone to manually write it down first.

### The boundary question: memory system vs project artifacts

In a software project, not everything belongs in the memory system. Code, tests, documentation, CI configuration — these are project artifacts with their own homes. The memory system is not a replacement for standard project structure.

The boundary principle: **the memory system stores what project artifacts don't preserve** — the reasoning, context, and process knowledge that produced the artifacts.

| What | Where it lives | Why |
|------|---------------|-----|
| The code | Repository | It is the artifact |
| API documentation | Project docs | Describes the artifact for consumers |
| Architecture decisions | ADRs (project) + session logs (memory) | ADR is the distilled decision; logs preserve the full reasoning |
| Why this approach over alternatives | Session logs (memory) | Not captured anywhere else — alternatives considered are invisible in the shipped code |
| User preferences and style | Memory system | No standard project location; implicit in choices across sessions |
| Recurring mistakes and corrections | Memory system | Corrections happen in sessions and are lost unless captured |
| Operational procedures that evolved through use | Memory system → eventually project docs | Start as observed patterns in logs, graduate to documented procedures |
| What was tried and abandoned | Session logs (memory) | Negative results have no home in standard project structure |

The memory system is strongest where project artifacts are weakest: **process knowledge, negative results, implicit preferences, and decision context**. Standard docs tell you *what* the system does. The memory system tells you *why it does it that way*, *what else was tried*, and *what the person who built it cares about*.

This also suggests a graduation pathway: some memory-system knowledge should eventually become project artifacts (a recurring procedure becomes a documented workflow, a preference becomes a linting rule), while session logs remain the substrate that keeps the full provenance.

## Open questions to explore

### Architecture
1. What is the right layered structure for stored-everything + selective-loading?
2. How do raw session logs relate to the library layer? What are the extraction bridges?
3. Should there be intermediate representations between raw logs and library notes? (Compressed episodes? Indexed observations? Fact extractions?)

### Retrieval/activation
4. What retrieval methods serve action-capacity (not just QA)? The activation gap note suggests cue-based, not query-based, retrieval.
5. Can the system pre-generate activation cues from session logs — essentially building a "question set" that future sessions can match against?
6. How do you avoid the expertise gap (the person who needs activation scaffolds least able to construct them)?

### Learning from logs
7. What extraction operations can run over session logs? (Preference mining, procedure extraction, correction consolidation, discovery flagging)
8. What oracles are available? Corrections are relatively clear signals; discoveries and preferences are harder to evaluate.
9. Can promotion heuristics (like ClawVault's "seen twice on different dates") work over session logs?

### Boundaries and graduation
10. Where exactly is the boundary between memory system and project artifacts? Is "stores what project artifacts don't preserve" sufficient, or are there edge cases?
11. What graduation pathways exist? When does a pattern in session logs become an ADR, a documented procedure, a linting rule, a test?
12. How does the memory system relate to existing manual distillation processes (ADRs, WRITING.md conventions)? Complement, replace, or feed into?

### The inspectability-learnability trade-off
13. How much of the retrieval policy should be inspectable (explicit rules) vs learned (trained from usage patterns)?
14. Can you get the best of both by using inspectable rules as the default with learned overrides for specific domains?

## Relevant KB notes

Core theory:
- [context-efficiency](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md)
- [activation gap](../../notes/knowledge-storage-does-not-imply-contextual-activation.md)
- [session-history](../../notes/session-history-should-not-be-the-default-next-context.md)
- [action-capacity](../../notes/claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md)
- [contextual competence theory](../../notes/an-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trusted-knowledge.md)

Memory architecture:
- [comparative review](../../notes/related-systems/agentic-memory-systems-comparative-review.md)
- [three-space model](../../notes/three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy-may-be-decorative.md)
- [flat memory failures](../../notes/flat-memory-predicts-specific-cross-contamination-failures-that-are-empirically-testable.md)
- [memory management policy](../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md)

Learning theory:
- [continuous learning = durability](../../notes/continuous-learning-requires-durability-not-weight-updates.md)
- [ephemerality prevents accumulation](../../notes/ephemeral-computation-prevents-accumulation.md)
- [agent statelessness](../../notes/agent-statelessness-makes-routing-architectural-not-learned.md)

Workshop layer:
- [workshop-layer](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md)
- [elicitation needs question-generation systems](../../notes/elicitation-requires-maintained-question-generation-systems.md)
