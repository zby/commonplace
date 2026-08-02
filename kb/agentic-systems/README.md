# Agentic Systems

Coverage of external **agentic systems and harnesses as whole systems** — execution loops, orchestration APIs, sub-agent surfaces, scheduling, and control. The companion collection [agent-memory-systems](../agent-memory-systems/README.md) covers one subsystem — memory — with a full review methodology; this collection covers the rest of how agentic systems are built, starting wherever a shipped system makes contact with our theory.

## Analyses

- [Autogenesis](./autogenesis.md) — self-evolving agent framework whose paper-aligned release exposes versioned protocol resources and an explicit planning bus, while current `main` replaces them with an expanded extension taxonomy and uniform capability loop; substantial code, but incomplete experiment reproduction and a broken advertised test baseline
- [Claude Code dynamic workflows](./claude-code-dynamic-workflows.md) — model-authored orchestrator scripts over sub-agents: the first shipped harness exposure of the bounded call beneath the frozen tool loop, mapped onto the [tool-loop cluster](../notes/tool-loop-README.md)
- [Compound Engineering plugin](./compound-engineering-plugin.md) — artifact-mediated software factory whose project-knowledge and optimization loops provide search, evaluation, and retention, but whose installed prompt corpus remains outside the ordinary update loop
- [Fractal](./fractal.md) — terminal/headless RLM harness over PredictRLM: SBX-mounted workspace turns, model-authored code and sub-model calls, agent-delegation skill, and session continuity stored outside the repo
- [GBrain as an agentic system](./gbrain.md) — the agent-OS half of a popular "memory" project: host-agent adoption protocol, dream-cycle scheduler, durable crash-resumable subagent queue, fail-closed trust boundary, and a gated self-modification loop; memory subsystem reviewed in [agent-memory-systems](../agent-memory-systems/reviews/gbrain.md)
- [Exo](./exo.md) — a harness built for recursive self-improvement: a protected Rust substrate under a fully rewritable executor, allowlisted host control for build and restart, and a sandbox rewind that preserves the record of what was already tried; memory subsystem reviewed in [agent-memory-systems](../agent-memory-systems/reviews/exo.md)
- [Semantic Engine as ingest infrastructure](./semantic-engine.md) — not an agent-memory system, but a code-grounded ingest workbench: local SQLite staging, source chunking, embeddings, query, and exploratory visualization before KB promotion
