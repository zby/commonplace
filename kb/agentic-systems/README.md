# Agentic Systems

Coverage of external **agentic systems and harnesses as whole systems** — execution loops, orchestration APIs, sub-agent surfaces, scheduling, and control. The companion collection [agent-memory-systems](../agent-memory-systems/README.md) covers one subsystem — memory — with a full review methodology; this collection covers the rest of how agentic systems are built, starting wherever a shipped system makes contact with our theory.

## Analyses

- [Claude Code dynamic workflows](./claude-code-dynamic-workflows.md) — model-authored orchestrator scripts over sub-agents: the first shipped harness exposure of the bounded call beneath the frozen tool loop, mapped onto the [tool-loop cluster](../notes/tool-loop-README.md)
- [Fractal](./fractal.md) — terminal/headless RLM harness over PredictRLM: SBX-mounted workspace turns, model-authored code and sub-model calls, agent-delegation skill, and session continuity stored outside the repo
- [GBrain as an agentic system](./gbrain.md) — the agent-OS half of a popular "memory" project: host-agent adoption protocol, dream-cycle scheduler, durable crash-resumable subagent queue, fail-closed trust boundary, and a gated self-modification loop; memory subsystem reviewed in [agent-memory-systems](../agent-memory-systems/reviews/gbrain.md)
- [Semantic Engine as ingest infrastructure](./semantic-engine.md) — not an agent-memory system, but a code-grounded ingest workbench: local SQLite staging, source chunking, embeddings, query, and exploratory visualization before KB promotion
