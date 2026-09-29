---
description: "Proposal: cut the scoping job, the memory handoff protocol and the review job from agentic-system analysis, derive the public review from the verified overview, and fix source identity and the blockers form in code"
type: reference/types/design-proposal.md
---

# Fewer authored decisions in agentic-system analysis

> **Archived** (see [archive README](./README.md)). Adopted by [ADR 097](../../adr/097-agentic-analysis-drops-decisions-that-change-no-result.md): the overview, memory report and generated review type specs and the analysis job instructions carry the live design. The pre-adoption state of the workflow's authored decisions remains here — design texture only.

The operator selected five cuts on 2026-09-29 from the workshop's simplification candidates (`kb/work/analysis-offload-to-code/simplification-candidates.md`, Decisions 1, 2, 3, 5 and 6). This proposal stated the contract changes they needed.

## Current state (as of 2026-09-29)

After [ADR 096](../../adr/096-analysis-passes-declare-their-own-records-under-lens-prefixes.md):

- A `scoping` job ran between the runtime pass and the lenses. It chose `brief` or `full` depth for each lens and named trigger records; no code read the depth. The overview rendered its output as `## Lens scoping`. Both lens members stated their scope again: the memory profile's `scope`, and block 1 of the epistemic report.
- Code wrote `memory-input.md` (boundary, source, the scoping record's memory part, and the runtime member). The memory method (`analyse-agent-memory.md`) described a private handoff: the specialist hashed its input and method by hand, and the member carried `canonical-register-sha256`, `method-sha256` and `worker-model`. `_verify_memory_member` checked only the first, against `memory-input.md`, which was gitignored run state, so no clean checkout could verify it. Nothing checked the other two beyond presence.
- A `review` job wrote `review-body.md` after verification: a description, an `Evidence basis:` line and prose. `review_body_refusals` checked only the H1, that line and the description.
- The caller gave `source-identity` at opening, and the boundary worker wrote `source.identity` independently; nothing compared the two. `_check_incumbent` compared identities by exact string.
- The workflow continued only when the verification's Blockers text, lowercased and without a final period, equalled `none`.
