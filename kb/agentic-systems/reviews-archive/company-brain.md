---
type: types/note.md
description: Company Brain combines a Slack agent runtime with scoped memory, human-correctable guidance and distinct tool approval paths; source inspection separates this wiring from demonstrated learning.
generated-by: analyse-agentic-system
analysis-run: AAS-2026-09-26-company-brain-01
source-identity: https://github.com/supermemoryai/company-brain
reviewed-revision: 0071d6164991ce5dccddbd645bcac631ee477572
analysis-result: kb/reports/retained/agentic-system-analysis-archive/AAS-2026-09-26-company-brain-01/result.md
analysis-result-sha256: ea4ff6d13ceaf4d60d13e9b00f9caab088f307721d1ada8668792d223aedf13a
---

# Company Brain

**Evidence basis:** source code and shipped documentation at [0071d6164991ce5dccddbd645bcac631ee477572](https://github.com/supermemoryai/company-brain/tree/0071d6164991ce5dccddbd645bcac631ee477572), inspected on 2026-09-26. No deployed run or causal experiment was assessed.

Company Brain is a Slack-centered agent runtime with external Supermemory integration. It owns event handling, model/tool loops, approvals, schedules, retained context and reply delivery. Its strongest supported adaptation mechanism is retained, human-correctable guidance that later model calls receive. Whether that guidance improves future performance remains untested in this evidence boundary.

## Runtime and control

Signed Slack events reach an organization Durable Object. Explicit turns run with recoverable state; passive conversations can be triaged into silence, acknowledgement, investigation or an answer. The main model receives current conversation, selected memory, skills and workspace guidance, then chooses tools or a terminal reply. Runtime code owns budgets, request updates, suspension and publication. Current packaging uses D1, KV and Durable Object SQLite; some architecture prose still describes the earlier Postgres deployment. These findings are wired implementation, not observed production reliability. See the exact result's CMP-1, RTE-1 and RTE-2.

Connected apps have two material paths. Code Mode runs generated JavaScript in QuickJS and applies native-call policy: classified reads can run, other effects pause for approval or are denied to read-only actors. A direct MCP fallback uses a different approval predicate for personal connections: destructive flags and a finite write-verb list. Unknown names therefore do not receive identical handling across the two paths. The fallback predicate is:

> if (annotations?.destructiveHint === true) return true
> return tokenizeToolName(toolName).some((tok) => WRITE_VERBS.has(tok))
> --- https://github.com/supermemoryai/company-brain/blob/0071d6164991ce5dccddbd645bcac631ee477572/src/brain/tools/mcp/tool-policy.ts

Human decisions check the original asker, workspace, expiry and current turn. Optional Cloudflare/Daytona shell work has its own command guards and effect boundary. Consequently, a universal claim that every external write receives approval exceeds the inspected enforcement. Actual remote permissions and isolation depend on deployment and provider contracts. See RTE-3, RTE-4, RTE-5 and RTE-6.

## What persists and returns

The memory boundary is wider than the company-knowledge store:

- Scoped documents, returned memories and topic/profile metadata feed requested search and automatic context selection. DMs can include accessible private-channel containers; explicit operator-selected surfaces form a separate path.
- Learned interaction style, approved generated skills and editable workspace guidance can shape later turns. Human correction can trigger targeted forgetting and replacement. Delivery is wired; behavioral activation was not measured.
- Approval continuations retain deterministically compacted messages. Thread/principal investigation checkpoints separately retain methods, answer excerpts and bounded tool trajectories, with six-hour idle expiry.
- Research drafts and sent history inform future planning; reviewed sends promote watch targets. Entity caches support later lookups.

These are application-visible SQLite and service objects carrying natural language and symbolic metadata. Both requested reads and automatic delivery exist. Trace-fed durable derivatives qualify for the comparison profile's `trace_learning: yes`, including approval compaction; this does not mean learning through criticism has improved capacity. Overall task horizon remains uncertain because a thread key does not establish whether a later request is the same task. See the individual memory object and route records in the [exact result](../reports/retained-archive/AAS-2026-09-26-company-brain-01/result.md).

Several implementation details limit stronger memory claims. `save_memory` first fills a capture buffer; durable submission happens later and can fail or queue. The compatibility adapter accepts options such as `dreaming` and `isFullReplace` but does not forward them to the service. The investigation field named `verifiedEvidence` admits an answer excerpt when any native call succeeded; it does not verify every proposition. External extraction, semantic indexing and model parameters remain uninspected. See CMP-3, RTE-15 and RTE-21.

## Evidence, correction and learning

The producing model is instructed to trace assertions to evidence and label inference. Final reply selection instead checks publishable form:

> /** Selects reply content without invoking another model or judging semantics. */
> --- https://github.com/supermemoryai/company-brain/blob/0071d6164991ce5dccddbd645bcac631ee477572/src/brain/turn/finalization/output.ts

Proactive research generates reviewable drafts with sources and flags. A draft lacking tool evidence can still be retained for human review; sending is an explicit operational decision, without a required recorded truth verdict. Generalizing a human's style preference into a durable team preference is a conjecture, even when the prompt asks for direct human evidence. Retention and delivery do not establish epistemic acceptance. See RTE-9, RTE-10, RTE-11, RTE-12, RTE-14 and RTE-17.

Under the [theory-builder definition](../../notes/definitions/theory-builder.md), localized guidance, criticism and iteration are afforded; content-dependent consumption of a particular theory remains unestablished. Membership and learning therefore remain uninspected. Runtime-state [reflection](../../notes/definitions/reflective-system.md) is wired: execution updates the step-budget representation, which changes tool availability. A style-adaptation [self-improvement pathway](../../notes/definitions/self-improving-system.md) is also wired in the dispositional sense, but no later operation was shown causally to depend on its update. Human correction and adoption roles preclude inferring autonomous theory building from unattended execution alone.

## Scope

This review covers the pinned application, not Supermemory internals, model providers, Slack, MCP servers or deployed Cloudflare/Daytona isolation. Dedicated long-running research is explicitly described as unshipped in the pinned guide. Candidate-linked correction/revision/later-use records would strengthen the theory-builder assessment; controlled later-capacity comparisons would be needed for a learning claim.

The [retained exact result](../reports/retained-archive/AAS-2026-09-26-company-brain-01/result.md) contains the source register, canonical mechanisms, specialist reconciliation, comparison profile, retained quotations and validation boundaries.
