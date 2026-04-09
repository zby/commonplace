# Workshop: Trace-Derived Systems Review Queue

## Question

Which external systems most improve the current review of [trace-derived learning techniques in related systems](../../notes/trace-derived-learning-techniques-in-related-systems.md), and how should each be reviewed?

## Why this workshop exists

The current survey now covers Napkin, Pi Self-Learning, OpenViking, ClawVault, Autocontext, OpenClaw-RL, AgeMem, and Trajectory-Informed Memory Generation. A web search surfaced a second wave of plausible additions.

This workshop holds the **execution packets** for those candidates so the work can be delegated cleanly:

- each file is self-contained
- each file names the target repo and paper
- each file asks the same comparison questions against the current trace-derived note

## Review priority

1. **ACE** — execution feedback into evolving playbooks; likely the closest artifact-learning analogue to Autocontext
2. **Dynamic Cheatsheet** — persistent adaptive cheatsheet updated at test time; strong artifact-promotion candidate
3. **Reflexion** — classic verbal reflection loop with episodic memory; important historical anchor
4. **ExpeL** — cross-task experience extraction and reuse; likely relevant to artifact-learning and retrieval-time reinjection
5. **Voyager** — reusable skill library learned from iterative trajectories; different domain, same trace-to-artifact shape
6. **Agent-R** — failure/correction traces turned into iterative self-training; strongest weight-learning addition in this queue

## In evaluation (review exists, needs trace-derived placement)

7. **REM** — four-database episodic memory with LLM consolidation from episodes to scored semantic facts; review exists, needs trace-derived placement assessment
8. **auto-harness** — minimal benchmark-gated outer loop with suite promotion and freeform learnings; review exists, needs trace-derived placement assessment
9. **Pal** — Agno-based personal agent with framework-owned agentic memory, past-session search, and operational learnings; review exists, needs trace-derived placement assessment
10. **browzy.ai** — local compiled wiki with session digests and multi-source crystallized drafts; review exists, needs trace-derived placement assessment as a weak live-session artifact-learning case
11. **DocMason** — sync promotes Codex/Claude host interactions into published interaction-memory directories with manifests and conservative semantic outputs; review exists, needs trace-derived placement assessment
12. **Playground** — imports chat logs and exec traces into archive/memory branches and synthetic memory turns; review exists, needs trace-derived placement assessment
13. **CORAL** — eval-gated multi-agent coding harness that turns attempt histories and inter-agent reflection into durable shared notes and reusable skills; likely belongs as a prompt-mediated trace-to-artifact system
13. **MemPalace** — mines conversation traces into durable verbatim drawers, heuristic memory-type rooms, and agent diaries; review exists, needs placement as a storage-first live-session artifact case
14. **Synapptic** — mines Claude Code JSONL sessions into weighted profiles and benchmark-filtered guards, then compiles them into assistant memory files; review exists, likely belongs as a prompt-policy trace-mining system
15. **virtual-context** — compacts live conversation and tool traces into durable summaries, facts, tag memories, and shared session state; likely belongs as a service-owned trace-to-symbolic-memory system

## Parked but likely worth a later pass

- Re-ReST
- REMEMBERER
- MIRA
- CoMEM-Agent
- InfMem
- MAEL

## Expected output from each review

- use `kb/instructions/review-related-system/SKILL.md` so the target repo is cloned or updated under `related-systems/`
- write or update one related-system note under `kb/notes/related-systems/`
- run semantic review on that note
- run `/validate` on that note
- answer whether the system should be added to the trace-derived survey, and if so, under which axis positions

## Files in this workshop

- [instructions-ace-review.md](./instructions-ace-review.md)
- [instructions-dynamic-cheatsheet-review.md](./instructions-dynamic-cheatsheet-review.md)
- [instructions-reflexion-review.md](./instructions-reflexion-review.md)
- [instructions-expel-review.md](./instructions-expel-review.md)
- [instructions-voyager-review.md](./instructions-voyager-review.md)
- [instructions-agent-r-review.md](./instructions-agent-r-review.md)
- [instructions-rem-review.md](./instructions-rem-review.md)
- [instructions-auto-harness-review.md](./instructions-auto-harness-review.md)
