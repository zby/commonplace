---
source: https://x.com/JayaGup10/status/2006384049485484145
captured: 2026-07-06T18:28:32.161674+00:00
capture: xdk
type: kb/sources/types/snapshot.md
tags: [x-post]
status_id: 2006384049485484145
conversation_id: 2006384049485484145
post_count: 1
---

# Post by @JayaGup10

Source post: https://x.com/JayaGup10/status/2006384049485484145

## 1. 2025-12-31T15:16:48.000Z https://x.com/JayaGup10/status/2006384049485484145

Before LLMs, Palantir was competing with Snowflake and Databricks.

Post-LLMs, they do not believe they have any competitors. Why? Snowflake/Databricks optimized for SQL and query throughput: get raw data into tables, run fast analytical reads, ship dashboards and models on top. Palantir made a different bet: an ontology, a world model where data is represented the way humans actually reason about it (objects, relationships, properties; nouns/verbs/adjectives). Back then, that was built for government analysts trying to make sense of messy, interdependent systems.

Then LLMs arrived and the ontology suddenly looked like the perfect interface because models don’t want a trillion rows. They want a structured, language-shaped substrate: named entities, typed relationships, constraints, and “what interacts with what”, something you can linearize into a coherent prompt, traverse, and act on. 

The bigger implication for decision traces is that the “context graph” problem we wrote about has multiple architectural solutions:

Platform-first (example: Palantir): prescribe the unified world model upfront. Pay the integration + ontology + embedded-team tax (months of use case discovery / workflow decomposition / “process mining”), and in return you get a substrate that can connect data to decisions because everything now lives inside the same model for an extremely absurd price.

Workflow-first (decision traces): don’t start by rebuilding the world. Instrument the moments where the world changes. Capture decision receipts at commit surfaces: inputs referenced, policy/constraints, exception path, approvals, action taken, outcome. Over time (not day 1), that write-time provenance becomes its own world model, learned from trajectories rather than imposed upfront (there will be many different methods here)

And importantly: this is still an ontology approach,  just a different kind. Palantir prescribes the ontology first. Our take is that startups can learn it bottom-up from traces. You start by capturing what people actually do at the decision surface: what evidence is referenced, which approvals happen, what exceptions recur, what actions are taken, what outcomes follow and over time, infer the minimal set of entities + relations that explain those trajectories. 

The missing piece is decision traces: without them, you have state, but not the legible “why”!! Cc @akoratana

Links:
- https://twitter.com/JayaGup10/status/2003525933534179480
