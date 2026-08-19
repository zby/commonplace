# AI Research OS reading: retention without an acceptance gate

Working note, 2026-08-19. Fifth case, read against the baseline's standing question — does the response taxonomy fit or break. Pinned authority is the [code-grounded review](../../agent-memory-systems/reviews/ai-research-os-workshop.md) (commit `dc66605`).

## The reading

The operative oracle is deterministic scripts plus four structural lint checks: they discriminate structure (orphans, missing hubs, broken links) and origin (seed vs discovered, with fixed scores 1.0/0.8/0.5). Weakly or not discriminated: source-page faithfulness to raw evidence, synthesis quality, explanatory quality — the review is explicit that there is "no repository-wide validator for those promises" and that lint "does not compare a hub or thesis back to raw evidence."

Explanation's position is the opposite corner from ScienceFlow: it is the *medium*. Wiki syntheses, comparisons, contradictions, and open questions are the system's main content — fully represented, marked (`> Synthesis:` prefix, per-claim wikilinks), and never scored.

The conjecture's second condition barely applies, though, because there is no reject-capable acceptance step anywhere: every written page is retained, and later ingests rewrite pages in place. Two consequences worth keeping:

1. **Selection moves to read-time.** With universal retention, whatever discrimination the loop has lives in attention routing — index ordering from fixed origin scores, the query read ladder, word budgets, read caps. These discriminate origin, recency, and length, not quality. The [weakly-discriminated conjecture](../../notes/weakly-discriminated-qualities-tend-to-be-underselected.md) is stated over acceptance and retention; this case suggests the same mechanism operates over read probability when retention is universal — a candidate scope extension rather than a counterexample.
2. **The dominant failure channel is compounding, not drift.** Downstream writers consume source pages and are forbidden from reading raw material, so an unfaithful source page propagates into hubs and syntheses unchecked — the review's "cumulative abstraction error." Where the other four systems risk a population slowly enriched for form-fit, this one risks unfiltered error amplification through a mandatory derivative path: a no-oracle corner rather than an unequal-oracle case.

## Taxonomy test

A fourth response to the form-vs-explanation asymmetry, not in the baseline's three: **mark-and-expose** — label LLM judgment, cite per claim, keep `raw/` immutable, and defer discrimination to the eventual consumer. The catch: the label is instruction-level and the loop itself consumes marked content as its authoritative input, so marking bounds nothing operatively. That is the read-time analogue of the baseline's schema corollary: a marker, like a first-class slot, is representation, not selection.

Five systems now suggest the taxonomy is two-dimensional rather than a single list:

| | explanation participates in the loop | explanation excluded/absent |
|---|---|---|
| **authority contained** | Eigenius (grade cap), Commonplace (declare-and-audit, advisory force) | ontology draft (exile) |
| **authority uncontained** | AI Research OS (mark-and-expose: labeled but fully operative) | ScienceFlow (unrepresented, unmanaged) |

Participation (is explanatory content inside the production loop?) and containment (is its authority bounded relative to its oracle strength?) vary independently. If this 2×2 survives the next case, it — not the flat response list — is the candidate note.

## Neighbor note

AI Research OS is Commonplace's nearest neighbor in medium (markdown, source/synthesis separation, inspectable files), and the review already locates the divergence at where governance lives. In this workshop's terms: near-identical declared contracts, very different operative oracles — Commonplace backs part of its contract with validators and verdict gates; AI Research OS backs its contract with instruction compliance plus structural lint. A useful pair for eventually testing whether operative-oracle strength, not contract quality, predicts corpus quality over time.

---

Relevant notes:

- [four-system-baseline.md](./four-system-baseline.md) — extends: the opening position this reading tests
- [AI Research OS Workshop review](../../agent-memory-systems/reviews/ai-research-os-workshop.md) — evidenced-by: pinned code-grounded authority for this reading
- [weakly discriminated qualities tend to be underselected](../../notes/weakly-discriminated-qualities-tend-to-be-underselected.md) — tests: the read-time variant is a candidate scope extension of the conjecture
