# RF-05 — Quote append does not preserve grounding warrant

**State:** open  
**Repair shape:** policy/ADR correction, then freshness implementation  
**Severity:** high  
**Depends on:** [RF-04](./rf-04-linked-evidence-is-outside-freshness.md)

## Finding

ADR 073 permits overlapping and disputed retained passages, yet says appending
quotes is safe without staling an accepted grounding review. Append-only byte
growth is monotone storage; epistemic support is not monotone. A later passage
can contradict, narrow, or contextualize the passage on which the old verdict
rested.

## Evidence

- [ADR 073's quote rules](../../reference/adr/073-untracked-source-snapshots-require-ingest-grounding.md)
  permit disputed passages without reconciliation.
- The same ADR declares quote append safe without staleness.
- [The grounding gate](../../instructions/review-gates/semantic/grounding-alignment.md)
  evaluates source scope and inference, not merely whether one supporting
  substring remains present.

## Why it matters

The mutation rule can preserve an old PASS after the retained source context has
become materially less supportive. This is a direct mismatch between the
claimed warrant and the admitted data state.

## Provisional repair direction

Remove the blanket safety claim. Make quote-section changes freshness inputs, or
give retained passages stable identities and bind each review to the exact
passage set it considered. Decide separately how disputed passages trigger
reconciliation.

## Done when

- ADR 073 and the grounding gate state one consistent mutation/freshness rule.
- Appending counterevidence cannot leave an old grounding verdict silently
  current.
- Tests cover supportive, qualifying, and contradictory append cases.
