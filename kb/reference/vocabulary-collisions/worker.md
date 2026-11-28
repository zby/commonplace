---
description: "Writing decision for worker where these uses meet: delegated agent and ordinary actor."
type: types/note.md
---

# Worker

Use "worker" only in the delegation sense. For the ordinary sense write "actor" or the specific noun.

A sub-worker is a headless worker an agent calls through `commonplace-sub-worker`. A sub-agent is provided by the calling harness itself.

## Senses

Delegation: an agent that receives a packet and works inside a parent's authority (`AGENTS.md` Delegation, `kb/types/instruction.md`, skills). Ordinary: any resource-bounded person or agent doing work.

## Why these uses are retained

The senses sit on surfaces that rarely co-load (operating instructions versus theory), and the sentence usually disambiguates.

## When to reconsider

An instruction or theory note needs the ordinary sense as a load-bearing noun, or a misresolution is observed in a run. Renaming the delegation sense to "sub-agent" is not the fallback: an inventory (2026-10-30) found the delegation sense spans harness sub-agents and headless processes that ADR 086 and ADR 118 define as not sub-agents, with about 450 live lines, code identifiers and frozen `worker:` keys. A fallback needs a role word distinct from both.

Recorded 2026-10-30, `kb/work/open-ended-work-economics`.
