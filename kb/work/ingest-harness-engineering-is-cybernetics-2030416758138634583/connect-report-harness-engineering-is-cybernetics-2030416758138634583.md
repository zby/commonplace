# Connection Report: Harness Engineering Is Cybernetics

**Source:** [harness-engineering-is-cybernetics-2030416758138634583](kb/sources/harness-engineering-is-cybernetics-2030416758138634583.md)
**Date:** 2026-03-09
**Depth:** standard

## Discovery Trace

**Index scan:**
- Read `kb/notes/index.md` and flagged:
  - [agent-statelessness-means-harness-should-inject-context-automatically](kb/notes/agent-statelessness-means-harness-should-inject-context-automatically.md) — source argues agents fail when system-specific judgment is not externalized
  - [methodology-enforcement-is-stabilisation](kb/notes/methodology-enforcement-is-stabilisation.md) — docs/tests/linters/CI are explicit harness constraints
  - [deploy-time-learning-the-missing-middle](kb/notes/deploy-time-learning-the-missing-middle.md) — thread argues repo artifacts improve future runs across sessions
  - [agentic-systems-interpret-underspecified-instructions](kb/notes/agentic-systems-interpret-underspecified-instructions.md) — possible background link via spec ambiguity and interpretation selection
  - [context-efficiency-is-the-central-design-concern-in-agent-systems](kb/notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — possible overlap via parseable feedback and environment design
  - [error-messages-that-teach-are-a-stabilisation-technique](kb/notes/error-messages-that-teach-are-a-stabilisation-technique.md) — direct overlap on parseable output and errors that point to the fix
  - [agents-md-should-be-organized-as-a-control-plane](kb/notes/agents-md-should-be-organized-as-a-control-plane.md) — possible overlap on machine-readable docs
  - [mechanistic-constraints-make-popperian-kb-recommendations-actionable](kb/notes/mechanistic-constraints-make-popperian-kb-recommendations-actionable.md) — possible overlap on externalized criticism and evaluation

**Topic indexes:**
- Read [kb-design](kb/notes/kb-design.md) — additional candidates:
  - [context-loading-strategy](kb/notes/context-loading-strategy.md) — slim-router pattern adjacent to externalized guidance
  - [oracle-strength-spectrum](kb/notes/oracle-strength-spectrum.md) — selected via learning-theory cross-link from methodology enforcement
- Read [learning-theory](kb/notes/learning-theory.md) — reinforced:
  - [stabilisation](kb/notes/stabilisation.md)
  - [oracle-strength-spectrum](kb/notes/oracle-strength-spectrum.md)
  - [error-messages-that-teach-are-a-stabilisation-technique](kb/notes/error-messages-that-teach-are-a-stabilisation-technique.md)

**Semantic search:** (via qmd)
- query `"harness engineering cybernetics feedback loops externalized architectural judgment agents"` — top note hits:
  - [agent-statelessness-means-harness-should-inject-context-automatically](kb/notes/agent-statelessness-means-harness-should-inject-context-automatically.md) (0.90) — strong match on externalized knowledge and harness-side provision
  - [the-frontloading-loop-is-an-iterative-optimisation-over-bounded-context](kb/notes/the-frontloading-loop-is-an-iterative-optimisation-over-bounded-context.md) (0.55) — medium lexical overlap on loops, weak conceptual fit
  - [error-messages-that-teach-are-a-stabilisation-technique](kb/notes/error-messages-that-teach-are-a-stabilisation-technique.md) (0.35) — direct overlap on feedback artifacts that teach
  - [agents-md-should-be-organized-as-a-control-plane](kb/notes/agents-md-should-be-organized-as-a-control-plane.md) (0.34) — weak overlap on documentation-as-infrastructure
- query `"harness engineering cybernetics feedback loops externalized architectural judgment agents"` — top source hits:
  - [harness-engineering-leveraging-codex-agent-first-world-ingest](kb/sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md) (0.56) — strong prior coverage of the same practical phenomenon
  - [harness-engineering-leveraging-codex-agent-first-world](kb/sources/harness-engineering-leveraging-codex-agent-first-world.md) (0.43) — direct predecessor source
  - [towards-a-science-of-scaling-agent-systems](kb/sources/towards-a-science-of-scaling-agent-systems.md) (0.35) — weaker overlap via verification loops

**Keyword search:**
- `rg 'AI slop|error messages|remediation instructions|parseable output' kb/notes kb/sources --glob '*.md'`
  - matched [error-messages-that-teach-are-a-stabilisation-technique](kb/notes/error-messages-that-teach-are-a-stabilisation-technique.md)
  - matched [harness-engineering-leveraging-codex-agent-first-world](kb/sources/harness-engineering-leveraging-codex-agent-first-world.md)
- `rg 'externalized|machine-readable|inject context|stateless' kb/notes kb/sources --glob '*.md'`
  - matched [agent-statelessness-means-harness-should-inject-context-automatically](kb/notes/agent-statelessness-means-harness-should-inject-context-automatically.md)
  - matched [context-engineering-ai-agents-oss](kb/sources/context-engineering-ai-agents-oss.md)
- `rg 'feedback loop|out-evaluate|oracle|rewardable' kb/notes kb/sources --glob '*.md'`
  - matched [oracle-strength-spectrum](kb/notes/oracle-strength-spectrum.md)
  - matched [methodology-enforcement-is-stabilisation](kb/notes/methodology-enforcement-is-stabilisation.md)
  - matched [harness-engineering-is-cybernetics-2030416758138634583](kb/sources/harness-engineering-is-cybernetics-2030416758138634583.md)

**Link following:**
- Followed [error-messages-that-teach-are-a-stabilisation-technique](kb/notes/error-messages-that-teach-are-a-stabilisation-technique.md) to [stabilisation](kb/notes/stabilisation.md), [frontloading-spares-execution-context](kb/notes/frontloading-spares-execution-context.md), and [context-efficiency-is-the-central-design-concern-in-agent-systems](kb/notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md); only the first remained central after evaluation
- Followed [agent-statelessness-means-harness-should-inject-context-automatically](kb/notes/agent-statelessness-means-harness-should-inject-context-automatically.md) to [context-loading-strategy](kb/notes/context-loading-strategy.md); useful neighborhood context but weaker than the main connection

## Connections Found

- [agent-statelessness-means-harness-should-inject-context-automatically](kb/notes/agent-statelessness-means-harness-should-inject-context-automatically.md) — **extends**: the note argues the harness should inject definitions, ADRs, and specs because agents cannot retain them; this source broadens the same mechanism to system-specific judgment itself. "What good looks like" must be made machine-readable or the agent repeats the same architectural mistakes forever.
- [methodology-enforcement-is-stabilisation](kb/notes/methodology-enforcement-is-stabilisation.md) — **exemplifies**: the thread's prescriptions (tests agents can run, parseable CI, architectural docs, custom linters, encoded standards) are exactly the movement from tacit human practice toward durable enforcement artifacts.
- [error-messages-that-teach-are-a-stabilisation-technique](kb/notes/error-messages-that-teach-are-a-stabilisation-technique.md) — **grounds**: the source independently identifies "error messages that point to the fix" as part of the minimum viable feedback loop, reinforcing the claim that verification output is also an instruction channel.
- [deploy-time-learning-the-missing-middle](kb/notes/deploy-time-learning-the-missing-middle.md) — **exemplifies**: the thread's core practical claim is cross-session improvement through repo artifacts. Better docs, tests, and constraints change future agent behavior without changing weights.
- [oracle-strength-spectrum](kb/notes/oracle-strength-spectrum.md) — **grounds**: the generator-verifier framing ("you need to out-evaluate it") is an oracle-design argument. The bottleneck is not raw generation but manufacturing stronger correctness signals the harness can apply cheaply.
- [agentic-systems-interpret-underspecified-instructions](kb/notes/agentic-systems-interpret-underspecified-instructions.md) — **grounds**: as background theory, the thread assumes the older programming problem that specs admit multiple valid readings. What is new here is not underspecification itself, but the harness as a new environment for steering which interpretation wins and how misinterpretations get corrected.

**Bidirectional candidates** (reverse link also worth adding):
- [agent-statelessness-means-harness-should-inject-context-automatically](kb/notes/agent-statelessness-means-harness-should-inject-context-automatically.md) ↔ source — **extends**: the note would gain a stronger statement that missing context is not just vocabulary loss but missing architectural judgment
- [oracle-strength-spectrum](kb/notes/oracle-strength-spectrum.md) ↔ source — **grounds**: the note would gain a crisp practitioner formulation of why evaluation infrastructure matters more than more generation

## Rejected Candidates

- [the-frontloading-loop-is-an-iterative-optimisation-over-bounded-context](kb/notes/the-frontloading-loop-is-an-iterative-optimisation-over-bounded-context.md) — control-loop vocabulary overlap only; this source is about harness design and evaluation, not orchestration selection dynamics
- [context-efficiency-is-the-central-design-concern-in-agent-systems](kb/notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — relevant background, but the thread is not primarily a context-scarcity argument
- [agents-md-should-be-organized-as-a-control-plane](kb/notes/agents-md-should-be-organized-as-a-control-plane.md) — documentation overlap is too narrow; the thread does not discuss loading-frequency economics or AGENTS scoping
- [mechanistic-constraints-make-popperian-kb-recommendations-actionable](kb/notes/mechanistic-constraints-make-popperian-kb-recommendations-actionable.md) — shares evaluation language, but the source does not make the contradiction/falsifier argument
- [related-systems/crewai-memory](kb/notes/related-systems/crewai-memory.md) — semantic retrieval noise; memory infrastructure is not the thread's subject
- Treating [agentic-systems-interpret-underspecified-instructions](kb/notes/agentic-systems-interpret-underspecified-instructions.md) as the primary connection — too strong; the source uses that theory as support, but its main contribution is the cybernetics framing and the new harness environment

## Index Membership

- [kb-design](kb/notes/kb-design.md) — the strongest neighborhood for harness architecture, context injection, and methodology enforcement
- [learning-theory](kb/notes/learning-theory.md) — the strongest neighborhood for stabilisation, deploy-time learning, and oracle design

## Synthesis Opportunities

- The safer next move is not a strong synthesis claim yet, but a first-principles starter note that asks what harness engineering changes about software development as an environment. [agentic-systems-interpret-underspecified-instructions](kb/notes/agentic-systems-interpret-underspecified-instructions.md) can ground what is old, while this source helps articulate what is new.
