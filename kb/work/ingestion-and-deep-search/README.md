# Workshop: Ingestion and Deep Search

## Question

How should source analysis work when the analysis purpose comes from the caller, not from the source type?

## Context

The current `/ingest` skill applies a fixed analysis template to every source. But different tasks need different things from the same source — and you should be able to re-source an article with new questions later. This means:

- Analysis instructions should flow from the process that prompted the sourcing
- Reports are purpose-driven working artifacts, not canonical metadata about the source
- The same snapshot can produce multiple reports for different purposes
- Reports belong near the work they serve, not colocated with snapshots

## What we want to discover

- What does a real workflow look like end-to-end? (question → source → extract → note)
- What artifacts get produced along the way?
- Do extraction reports naturally cluster, or are they all different?
- What's the right interface for passing analysis instructions to the ingest skill?
- How does "deep search" (sourcing multiple articles for one question) actually play out?

## Open Questions

- **Report location**: Currently saving reports in `kb/sources/` next to snapshots (easy path). Should try saving in `kb/work/` near the purpose instead and compare. Which feels more natural when you're actually working?

## Experiments

(Run actual workflows here and capture what happens.)
