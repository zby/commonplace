# Instruction: verify and snapshot the mixed-form source list

Five external sources were named by an external LLM review (2026-07-28) as support for the mixed-form learning program. **Their identifiers are unverified claims from that review, not facts** — an arXiv id may resolve to a different paper, a named system may not exist. Nothing in the KB may cite any of them until it is verified and snapshotted. This instruction is executable by an agent with no other session context.

Prerequisite: the `cp-skill-snapshot-web` skill and network access. If the skill is unavailable, stop and report — do not capture by hand.

## Sources

| Name | Starting identifier | What it must be to count as verified |
|---|---|---|
| Agent Symbolic Learning | arXiv 2406.18532 | "Symbolic Learning Enables Self-Evolving Agents" (or near-identical title) — agents optimizing prompts, tools, and their composition as symbolic learnables |
| ToolGate | arXiv 2601.04688 | A paper on contract-grounded / verified tool execution for LLMs, separating probabilistic cognition from deterministic execution control |
| Co-Harness | none — search; reportedly a preprint of ~2026-07-17 | Alternates harness optimization with model fine-tuning: distills successful scaffolding into weights while continuing to improve the harness |
| Memento-Skills | none — search | A system that continually rewrites structured Markdown skills as its learning mechanism. Caution: do not confuse with other "Memento"-named memory papers |
| Anthropic long-running-agents post | none — search anthropic.com engineering blog | An Anthropic engineering post on long-running agents: compaction/stronger models insufficient without persistent progress artifacts and structured environments spanning context windows |

## Procedure

Per source:

1. Resolve the identifier or search for the item. Check the found title and abstract against the "must be" column — the match is on the specific claim, not topic vibes.
2. **On mismatch or no result: record NOT FOUND with what you did find, and move on. Never substitute a similar paper for the named one** — a plausible near-match snapshotted under this list's name would be cited as if it supported claims it may not make.
3. On match: snapshot with `cp-skill-snapshot-web`.
4. Record the outcome in the Results section below (verified + snapshot path, or NOT FOUND + evidence).
5. After all five: update the "Source verification list" in this workshop's `README.md` — move verified items to the Held line with their snapshot links; annotate failures.

Commit the snapshots and the two workshop-file updates together, with explicit paths (never `git add -A`). Out of scope: no ingests, no new notes, no citations added anywhere else in the KB.

## Results

- Agent Symbolic Learning: **verified** — arXiv 2406.18532 resolves to “Symbolic Learning Enables Self-Evolving Agents”; its abstract defines prompts, tools, and their composition as symbolic learnables. Snapshot: [symbolic-learning-enables-self-evolving-agents.md](../../sources/symbolic-learning-enables-self-evolving-agents.md).
- ToolGate: **verified** — arXiv 2601.04688 resolves to “ToolGate: Contract-Grounded and Verified Tool Execution for LLMs”; its abstract specifies typed symbolic state and Hoare-style pre/postcondition checks around tool execution. Snapshot: [toolgate-contract-grounded-and-verified-tool-execution-for-llms.md](../../sources/toolgate-contract-grounded-and-verified-tool-execution-for-llms.md).
- Co-Harness: **verified** — search found arXiv 2607.22688, “Co-Harness: Co-Evolving Harnesses and Model Weights for LLM Agents,” submitted 2026-07-17; its abstract says harness optimization alternates with fine-tuning on trajectories from the improved harness. Snapshot: [co-harness-co-evolving-harnesses-and-model-weights-for-llm-agents.md](../../sources/co-harness-co-evolving-harnesses-and-model-weights-for-llm-agents.md).
- Memento-Skills: **verified** — search found arXiv 2603.18743, “Memento-Skills: Let Agents Design Agents”; its abstract identifies structured Markdown skills as persistent evolving memory updated by read-write reflective learning. Snapshot: [memento-skills-let-agents-design-agents.md](../../sources/memento-skills-let-agents-design-agents.md).
- Anthropic long-running-agents post: **verified** — Anthropic's 2025-11-26 engineering post “Effective harnesses for long-running agents” states that compaction is insufficient and reports the use of progress files, git history, structured feature requirements, and incremental verified work across context windows. Snapshot: [effective-harnesses-for-long-running-agents.md](../../sources/effective-harnesses-for-long-running-agents.md).
