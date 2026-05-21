# Workshop: Ingestion And Deep Search

## Question

How should agents run deep search over a KB without mixing discovery, source processing, synthesis, and promotion into one overloaded task?

The original question was narrower: how to decouple source analysis from downloading. That produced two implemented cleanup threads:

- `cp-skill-ingest` now owns source assimilation and writes only an `.ingest.md` report.
- `cp-skill-connect` now owns graph-discovery context and writes only a connect report.

Those stable contracts moved into the shipped skills and type specs. This workshop now keeps the remaining unsolved problem: how to organize broader, iterative research where each pass may discover sources, process them, synthesize findings, and write instructions for the next bounded agent call.

## Current Claim

Deep search should be treated as staged context engineering, not as one long browsing session.

The useful pattern from the experiments is:

1. **Discovery** - find candidate sources, reject weak ones, and decide what is worth processing.
2. **Processing** - snapshot and ingest selected sources through stable contracts.
3. **Instruction writing** - frontload the selected inputs, goal, relevance judgments, and output contract into a self-contained work packet.
4. **Synthesis** - hand the packet to a clean-context sub-agent that reads bounded material and writes the lens-shaped result.
5. **Promotion** - separately decide whether any result should become a note, reference doc, instruction, ADR, index change, or follow-up task.

This separates judgment-heavy selection from focused reading and keeps promotion authority out of search and synthesis reports.

## What Remains Open

- When should a deep-search loop continue versus stop?
- What state should each iteration preserve for the next one: sources, rejected candidates, search queries, claims found, uncertainties, or instructions?
- Should deep search have a reusable skill, or should it remain a pattern composed from `snapshot`, `ingest`, `connect`, instruction notes, and sub-agent delegation?
- Where should deep-search work packets live, and when should they expire?
- How much of the caller's judgment should be written into the instruction note versus left for the synthesis agent?
- What should count as a successful deep-search result: source coverage, answer quality, new claims, reduced uncertainty, or promotable artifacts?

## Retained Artifacts

- [Directed-reading contract inventory](./directed-reading-inventory.md) - map of stable and ad hoc reading contracts that already exist in the KB.
- [Instructions: A-MEM automation-quality trade-off](./instructions-amem-automation-quality.md) - concrete example of a frontloaded instruction packet used in an experiment.

## Evidence So Far

The A-MEM learning-operations experiment showed that a custom lens can extract different value from the same source than standard ingestion. The automation-quality experiment showed that a frontloaded instruction packet lets a sub-agent synthesize multiple documents without rediscovering why they matter. The memory-systems review experiment showed the larger pattern: discovery, processing with `/ingest`, instruction writing, then clean-context synthesis.

The implemented connect/ingest cleanup moved the stable parts of that pattern into reusable contracts. The remaining design work is the orchestration layer for open-ended deep search.
