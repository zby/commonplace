# Eight-note trial — can the over-bound notes quote or split without loss?

Run 2026-08-27 by two Opus workers, read-only, four notes each. Rule under test: at most N=5 distinct `kb/sources/*.ingest.md` targets without a paired verbatim quote in the note; `(snapshot required)` sources always count; note links never count.

## Result

| Note | Ingests | Unquoted now | Route | Added quotes | Risk |
|---|---|---|---|---|---|
| theory-mediated-learning-may-improve-sample-efficiency-under-shifts | 9 | 9 | quote from existing retained quotes | 4 (~+90 w / 2766, 3%) | low |
| knowledge-storage-does-not-imply-contextual-activation | 8 | 8 | quote 3; two sources are trailer-only and need a hosting sentence, or drop them (8→6) | 3 (~+55 w / 1837, 3%) | low |
| an-omitted-loop-function-and-a-frozen-one-need-different-repairs | 7 | 7 (5 snapshot-required → floor 5) | quote ABR + DGM → exactly 5 | 3 (~+65 w / 2336, 3%) | medium: zero margin |
| evidence/real-self-improving-systems-occupy-combinations-no-rung-captures | 7 | 7 | quote Autogenesis + DGM; claim is joint over 13 table rows | 2 (~+50 w / 1644, 3%) | medium-high on form |
| a-proposal-selection-loop-requires-search-evaluation-and-retention | 6 | 6 | quote the joint autonomic trio together | 1 min / 3 (+6%) | low |
| evidence/six-reported-self-improvement-paths-expose-bounded-redesign-surfaces | 6 | 6 | quote from existing; two row details unretained | 1 min / 6 (+16%) | moderate: table bloat |
| instantiation-alone-cannot-model-agent-learning-across-sessions | 6 | 6 | drop a redundant trailer-only Erlang ingest (6→5), or quote Machine Studying | 0–1 | low |
| formal-systems-assess-explanatory-reach-through-causal-and-proof | 6 | 6 | quote CRL + Schmidhuber + invariant prediction | 3 (+8%) | low |

No note currently holds any verbatim quotation. **None needs a split, a `(snapshot required)` escape, or a new grounding run to conform.** Word growth is 2–3% on the cheapest route everywhere; the expensive routes (quote every row of a casebook table) reach +16%.

## What the trial settles

- **Fail or warn.** The force against the option — that the eight notes could not conform without losing their claim — did not materialise. Conformance is cheap in words. But it is not free in form (below), and the eight notes are not yet conformed. Recommendation: ship as **WARN**, flip to FAIL once the eight are conformed and the two authoring conventions below exist.
- **N.** Five holds: all eight reach it from retained quotes. Three would put 18 notes over and was not tried.
- **`(snapshot required)` semantics.** Attach **per source**, not per link: one snapshot-required use forces the reviewer to open the snapshot, and the cost the bound counts is artifacts opened. The validator implements this (a source counts if any occurrence carries the marker). This decides the omitted-loop note's floor of 5.

## What the trial exposes that quoting does not fix

1. **Trailer-only citations** — an ingest linked only from Relevant Notes has no sentence to host a quote. Two notes have them. Either they are adjacent (not evidential) and should not be counted — but the validator cannot tell — or they need a hosting sentence. Authoring convention needed: a source cited as evidence is cited in the body.
2. **Table-cell citations** — a casebook row is not a paragraph. Quoting two of thirteen rows is unprincipled; quoting all bloats the table. Convention needed: a casebook note hosts retained evidence in a short prose block under the table, one quote per row, or narrows each cell to what the retained quotes state.
3. **Joint casebook claims** — `six-reported-self-improvement-paths` and `real-self-improving-systems-occupy-combinations` are constitutively N-way comparisons. They conform numerically, but they are the best candidates if a `synthesis`-trait exemption is ever wanted. Not recommended now: they conform.

## Defects found on the way (follow-ups, independent of the bound)

- `kb/sources/the-risks-of-invariant-risk-minimization.ingest.md` — all four `## Quotes` entries are marked verbatim but are third-person paraphrase. They would mechanically discharge the bound while presenting summary as quotation. Needs a fresh `cp-skill-ground` run against the recorded snapshot.
- `kb/sources/huxley-godel-machine-*.ingest.md` — empty Quotes section; only usable via `(snapshot required)`.
- `real-self-improving-systems-occupy-combinations` — the DreamCoder cell asserts "statistical program fit" as the evidential limit; the retained capture does not state one, and `theory-mediated-learning-…` says so explicitly about the same ingest. The two notes are in tension on that cell.
- `towards-causal-representation-learning` and `dowhy` ingests hold two-column PDF fragments; clean sub-spans exist but the retained quotes are ugly.
