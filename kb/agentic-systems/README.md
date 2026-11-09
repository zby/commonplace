# Agentic Systems

This research explores the design space of agentic systems: which choices
matter, which combinations are possible, what constrains them, and what
evidence would justify committing to a design. Concrete systems provide
source-grounded examples, not a product ranking or an exhaustive map of
possible architectures.

The choices include how systems retain information, control execution, check
knowledge and recover from failure. The aim is to explain alternatives and
their conditions, not merely catalogue features.

## Start with a design question

- **Identify choices and alternatives:** use [Research Topics](./topics/README.md)
  to find relevant dimensions and questions about their interactions across
  Agent Memory, Runtime & Control, Knowledge & Verification, and Workflow & Recovery.
- **Investigate combinations and constraints:** follow
  [Comparisons](./comparisons/README.md) to cross-system research organized by
  architectural question, with mechanisms and their supporting records.
  A combination missing from this corpus is not thereby impossible.
- **Decide what evidence is still needed:** use [Methods & Data](./methods.md#what-the-evidence-can-settle)
  and the [future-work agenda](./topics/README.md#future-work) to distinguish
  source inspection from experiments needed before commitment.
- **Find an individual system:** use the
  [Systems Directory](../agentic-system-analyses/current-analyses.md) for current
  accepted analyses, generated at each site build.

**[Agent Memory](./topics/memory.md)** is the most developed topic: what is
retained, how does it reach the next decision, and what happens when it is
wrong? Start with the
[agent-memory landscape](./comparisons/memory/agent-memory-landscape.md), a
frozen synthesis of 243 analyses from November 2026, then follow its evidence
to individual systems.

## Follow the evidence

An accepted analysis is more than a project description. It traces operational
routes at a frozen source boundary, separates documentation claims from
inspected code, and retains supporting records and verification judgments.
Its overview links the source register, detailed accounts and limitations.

A wired retrieval path does not establish observed use, measured benefit or
causal improvement. Coverage gaps stay distinct from evidence of absence.
Compare the scope and evidence of each route rather than assigning a
system-wide property from a single feature. [Methods & Data](./methods.md)
explains these distinctions and why current listings, dataset snapshots and
historical research can have different populations. It also provides the memory
table, CSV and reproducible population boundaries.

The primary research program charts the design space and seeks solutions
useful to Commonplace. These public accounts keep source-system findings
separate from judgments about adoption in Commonplace. The
[historical Agent Memory Systems collection](../agent-memory-systems/README.md)
remains accessible; its reviews and comparison snapshots are not the current
accepted-analysis population.

## Authored accounts

- [Academic Research Skills](./reviews/academic-research-skills.md) — Claude Code research pipeline whose prompt-defined stages are supported by narrow executable checks, while orchestration, Passport resume, and terminal gate behavior remain host-dependent or internally conflicted
- [AI Agents in Depth](./reviews/ai-agent-book.md) — whole-book comparison whose Model–Harness, context, evaluation, continual-evolution, and coordination doctrine largely converges with Commonplace, while memory admission, evaluator policy, authority granularity, and several evidence claims diverge
- [Autogenesis](./reviews/autogenesis.md) — self-evolving agent framework whose paper-aligned release exposes versioned protocol resources and an explicit planning bus, while current `main` replaces them with an expanded extension taxonomy and uniform capability loop; substantial code, but incomplete experiment reproduction and a broken advertised test baseline
- [Eigenius](./reviews/eigenius.md) — typed execution and verification substrate with a manually loaded host-agent reasoning protocol: curated MCP, checked justification certificates on named load paths, incomplete recovery/provenance, and conditional Lean correspondence
- [Claude Code dynamic workflows](./reviews/claude-code-dynamic-workflows.md) — model-authored orchestrator scripts over sub-agents: the first shipped harness exposure of the bounded call beneath the frozen tool loop, mapped onto the [computational-model](../tags/computational-model-README.md)
- [Compound Engineering plugin](./reviews/compound-engineering-plugin.md) — artifact-mediated software factory whose project-knowledge and optimization loops provide search, evaluation, and retention, but whose installed prompt corpus remains outside the ordinary update loop
- [Fractal](./reviews/fractal.md) — terminal/headless RLM harness over PredictRLM: SBX-mounted workspace turns, model-authored code and sub-model calls, agent-delegation skill, and session continuity stored outside the repo
- [GBrain](./reviews-archive/gbrain-garrytan.md) — historical analysis of a memory and context service with its own operating layer: provenance-carrying facts, hook-pushed context, a nightly cycle and durable job queue, benchmark-gated skill optimization, and skill distribution to harnesses as a product surface
- [Exo](./reviews/exo.md) — a harness built for recursive self-improvement: a protected Rust substrate under a fully rewritable executor, allowlisted host control for build and restart, and a sandbox rewind that preserves the record of what was already tried; historical memory-subsystem review in [agent-memory-systems](../agent-memory-systems/reviews/exo.md)
- [Semantic Engine as ingest infrastructure](./reviews/semantic-engine.md) — not an agent-memory system, but a code-grounded ingest workbench: local SQLite staging, source chunking, embeddings, query, and exploratory visualization before KB promotion
