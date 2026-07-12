---
description: "BrainsAndTennis on vertical-agent quality as task-distribution-aware context compression, with L1/L2/L3 cache tiers for prompts, curated specs, and raw references"
source_snapshot: "building-a-good-vertical-agent-2065190286519906657.md"
ingested: "2026-06-12"
type: kb/sources/types/ingest-report.md
domains: [agent-architecture, context-engineering, vertical-agents, tool-design]
---

# Ingest: Building a Good Vertical Agent

Source: [building-a-good-vertical-agent-2065190286519906657.md](./building-a-good-vertical-agent-2065190286519906657.md)
Captured: 2026-06-12T10:11:23.632350+00:00
From: https://x.com/BrainsAndTennis/status/2065190286519906657

## Classification

Type: practitioner-report -- the author reports from roughly a year building Shortcut's spreadsheet agent and argues from product architecture, customer selection pressure, and concrete tool/context design choices rather than from a controlled study.
Domains: agent-architecture, context-engineering, vertical-agents, tool-design
Author: @BrainsAndTennis, reporting as a builder of Shortcut's spreadsheet agent; the credibility signal is high-stakes vertical-agent product experience, but the measurements and customer claims are self-reported.

## Summary

The source argues that a strong vertical agent is "a compression of its task distribution": with the base model fixed, performance comes from deciding what context the model sees, when it sees it, and how compressed that context is for the tasks users actually bring. It frames the system prompt, tools, skills, curated docs, and raw references as one context hierarchy. Common spreadsheet operations belong in L1 as always-resident, heavily engineered wrappers that compress reads and writes while reporting consequences. Less common capabilities belong in L2 as curated, gotcha-aware English specs fetched on demand. Rare long-tail capabilities belong in L3 as complete raw references plus a skill that teaches the agent how to search them. The worked example is spreadsheet automation, but the claimed design rule is domain-general: allocate context tiers by frequency and discovery cost.

## Connections Found

The companion connect report found the strongest fit with [context efficiency is the central design concern](../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) and [instruction specificity should match loading frequency](../notes/instruction-specificity-should-match-loading-frequency.md). This source adds a sharper optimization frame to those notes: place each capability in a context tier that minimizes expected cost over the task distribution. It also supports [agent context is constrained by soft degradation](../notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md) through the author's warnings about bloated prompts, overlapping tool schemas, and degraded accuracy from tool count. More specific connections include [always-loaded context mechanisms](../notes/always-loaded-context-mechanisms-in-agent-harnesses.md), [frontloading](../notes/frontloading-spares-execution-context.md), [bounded-context orchestration](../notes/bounded-context-orchestration-model.md), and [distillation](../notes/definitions/distillation.md). Sibling sources include the Raschka coding-agent ingest, the Fintool practitioner report, Agent Skills for Context Engineering, and the multi-agent-memory computer-architecture paper, but the new contribution here is the cache-hierarchy placement rule for a single vertical agent's domain context.

## Extractable Value

1. **Cache hierarchy as a design rule for context placement** -- The source turns the KB's existing loading-frequency principle into an optimization model: L1 costs every task but is instant, L2 costs a one-step miss, and L3 costs search over a raw substrate. This gives [context efficiency](../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) a concrete allocation heuristic based on expected task-distribution cost. [quick-win]

2. **"Context compression" as product differentiation** -- The source claims customers choose the vertical agent because it is right more often, and explains that advantage through domain-specific compression rather than a novel agent loop. This is useful convergent evidence that agent product quality can live in the context engine and execution substrate, not just the model. [quick-win]

3. **One execute-code tool plus internal API as a tool-surface compression pattern** -- The author argues that many overlapping tools degrade accuracy and that one code-execution tool lets the model compose a domain API inside code. This is a concrete design pattern for reducing tool-schema interference, but it should be treated as domain- and model-dependent until we have broader evidence. [experiment]

4. **L1 wrappers should report consequences, not just results** -- The spreadsheet write feedback groups and samples diffs, then pulls suspicious edits into review categories with severity. That extends the KB's frontloading and bounded-orchestration notes with a useful implementation detail: hot-path wrappers should compress observations and surface likely mistakes as part of the same response. [experiment]

5. **Curated specs outperform raw API references on occasional capabilities** -- L2 specs encode canonical recipes, order constraints, and runtime footguns that raw signatures omit. This supports the KB's distillation vocabulary: the artifact is not merely a shorter reference, but a use-shaped capability description for an agent performing a task. [just-a-reference]

6. **Raw complete references still need a search skill** -- L3 is not "dump everything on disk" by itself. The source's escape hatch works because a short skill maps the raw reference's structure and grep recipes, bounding the discovery cost for rare tasks. This is directly relevant to Commonplace's own skill-and-rg navigation posture. [quick-win]

## Limitations (our opinion)

The source is a persuasive practitioner report, not an empirical evaluation. It does not expose Shortcut's benchmark set, ablation results, exact tool-count experiments, or failure distribution, so the accuracy and tool-count claims should be cited as product experience rather than measured law. The source is also heavily domain-shaped: spreadsheets have a rich symbolic API, inspectable state, deterministic execution, and common read/write operations that reward wrapper engineering. Domains without a code-executable substrate may not benefit from a single execute-code tool in the same way.

The captured snapshot is text-first and appears to omit or flatten screenshots/examples from the X article. The prose explains the examples enough to ingest the architectural argument, but the exact UI/API examples should not be treated as faithfully preserved implementation evidence. Finally, the cache analogy is useful but can overfit: unlike CPU caches, agent context entries have semantic interference and activation risk, so putting an item in a "fast tier" may hurt reasoning even when it improves access speed.

## Recommended Next Action

Write a note titled `Agent context should be organized as a cache hierarchy`, connecting this source to [context efficiency is the central design concern](../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md), [instruction specificity should match loading frequency](../notes/instruction-specificity-should-match-loading-frequency.md), and [always-loaded context mechanisms in agent harnesses](../notes/always-loaded-context-mechanisms-in-agent-harnesses.md). The note should argue that context placement should minimize expected cost over a task distribution, with resident wrappers, one-step curated specs, and bounded raw-reference search as tiers.
