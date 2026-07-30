# Parallel terraced scan: transferable scan

**Status:** memory-first and source-ungrounded
**Recall confidence:** high

## Remembered model

Parallel terraced scan is remembered as a processing strategy associated with Hofstadter's fluid-analogy work rather than a standalone general cognitive architecture. Many possible structures or interpretations receive small amounts of work in parallel or interleaved fashion. Promising candidates attract progressively deeper processing, while stochastic exploration prevents the system from committing immediately to the first plausible path. The "terraces" are levels of depth reached as evidence accumulates.

This resembles a resource-allocation policy for uncertain search: broad and cheap first, deeper and more selective later, with the option to reopen alternatives.

## Provisional ontology

- **Candidate:** a possible interpretation, relation, source, or solution path.
- **Scout:** a cheap process that gathers a small piece of evidence.
- **Promise/urgency:** an estimate that a candidate merits more work.
- **Terrace:** a level of processing depth or resource commitment.
- **Promotion:** allocation of deeper evaluation to a promising candidate.
- **Exploration budget:** resources reserved for alternatives that have not yet accumulated support.
- **Convergence:** sufficient mutual constraint to stop widening and finish a candidate.
- **Reopening:** renewed work on a previously weak path after new evidence.

## Transfer candidates

- **`PTS-1` — formalize Commonplace navigation as progressive deepening.** Title/description scans, scoped lexical hits, selective file reads, authored-link traversal, and source checking form natural terraces. Each step should state its promotion signal.
- **`PTS-2` — allocate by expected information gain, not only current relevance.** A candidate that could decisively distinguish two hypotheses may deserve depth despite a lower similarity score.
- **`PTS-3` — preserve an exploration quota.** Always spending on the current leader creates self-confirming context. Reserve some attention for dissenting sources, weakly linked alternatives, and negative evidence.
- **`PTS-4` — stop candidates explicitly.** Record whether a path was rejected, deferred for cost, or merely not reached. Otherwise shallow non-selection looks like negative evidence.
- **`PTS-5` — vary depth within one task.** Not every retrieved artifact deserves a full read or semantic review. Expensive evaluation should be earned by cheaper evidence unless risk mandates immediate depth.

The existing [Commonplace navigation model](../../reference/navigation.md) already embodies a cheap-to-expensive reading progression. This architecture may supply a more general scheduling account and expose the missing exploration and reopening policies.

## Method worth borrowing

Compare allocation policies under a fixed context or call budget: top-k then deep read, breadth-only, depth-first, and terraced adaptive allocation. Use tasks with an initially plausible decoy and a low-ranked decisive artifact. Measure solution quality, evidence diversity, cost, premature convergence, and recovery when late evidence reverses the leader.

## Non-transfer and failure modes

- "Parallel" may mean interleaved microprocessing rather than actual concurrent execution; implementation should follow dependencies and tool constraints.
- Rich-get-richer allocation can starve novel candidates.
- Continual reopening can prevent completion unless termination criteria are explicit.
- Promise estimates derived from the same model doing the reasoning can reinforce its initial bias.
- The strategy does not supply epistemic validation; it only allocates search effort.

## Grounding questions

1. Where was parallel terraced scan defined most clearly, and what mechanisms are essential?
2. How are urgency and depth allocation computed in Copycat or related systems?
3. What guarantees diversity or prevents premature convergence?
4. Is "terrace" a discrete computational level or primarily an explanatory metaphor?
