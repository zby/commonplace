---
type: types/note.md
description: "WikiSkill's persistent wiki and reversible skill updates, with paper-only evidence and performance-gate limits."
generated-by: analyse-agentic-system
analysis-run: AAS-2026-09-25-wikiskill-01
source-identity: https://arxiv.org/abs/2608.27454
reviewed-revision: "sha256:c093e240375e9780468edca9aa91aefecb8714ebdbef40810316644d9b2822d0"
analysis-result: kb/reports/retained/agentic-system-analysis/AAS-2026-09-25-wikiskill-01/result.md
analysis-result-sha256: 1b27b3f32961a43c1df6a9bd0fc742d07785d9ab2ba0b1951b4d37195175f82b
---

# WikiSkill

Evidence basis: [WikiSkill paper](https://arxiv.org/abs/2608.27454), captured 2026-09-17; doc-grounded analysis of the described improvement workflow, without implementation or original run artifacts.

WikiSkill separates immutable execution traces, a persistent wiki and the active skill set. Each iteration executes training tasks, compiles successes and failures into wiki patterns and summaries, proposes one skill change, and tests it on validation tasks. The gate accepts only strict score improvements. Rejected skills are rolled back while wiki knowledge and the proposal's diff, score and rejection history survive for later proposals. These are described routes, not independently inspected wiring.

The wiki maintainer receives existing wiki context and sampled traces. The proposer starts with catalog, impact history and task outcomes, then requests particular pages and traces. Inference receives all active skills directly in its system prompt. This separates diagnostic knowledge from operative procedures, but full injection leaves skill retrieval untested. PURPOSE.md preserves a rationale map; its later reading and inference delivery are not established.

The paper reports improved skill evolution and conditional cross-model transfer. Its wiki ablation removes the maintainer together with proposer wiki access, so the contrast concerns that combined mechanism. Validation accepts procedural performance, not the truth of every retained explanation. A simplified case describes revisions informed by prior failures; it does not independently establish that criticism of an explanation caused the measured improvement.

## Scope

The [exact retained analysis](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-wikiskill-01/result.md) contains the source anchors, route records, mandatory memory and epistemic lenses and all fourteen memory-comparison axes. Reflection and self-improvement are claimed at the described skill-evolution boundary. Criticism-specific learning, faithful dependence on particular recalled content, exact model fixation and runtime enforcement remain unestablished. The paper acknowledges unpruned wiki growth and does not evaluate within-rollout adaptation or very long-horizon tasks. The inference-wiki-access ablation also leaves delivery and authority unspecified.
