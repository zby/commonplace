# Run 01: Three standard reviews on baseline

Reviews run: semantic-review, prose-review, complexity-review (all in parallel)

## Scoring

| Change | Hit/Miss | Source | Notes |
|--------|----------|--------|-------|
| A1 (define "execution boundary") | Miss | — | No review checks accessibility for outsiders |
| A2 (replace K/select notation) | **Explicit miss** | Prose pseudo-formalism: CLEAN | Review saw the notation, considered it, decided it was "cross-reference shorthand" and "borderline acceptable; no action needed" |
| A3 (identify Slate by maker) | Miss | — | No review flagged unidentified system |
| A4 (remove "bounded call" jargon) | Miss | — | No review checks for KB-internal vocabulary |
| C1 (ambiguous negation) | Miss | — | No review checks sentence-level parsing ambiguity |
| C2 (wrong framing "for orchestration") | Miss | — | No review noticed the framing should be grounded in cognitive capacity |
| C3 (misleading link) | **Hit** | Semantic grounding INFO | "The identity claim ('this IS the return-value problem') slightly overstates the correspondence" — caught the mismatch between the note's use and the scoping note's actual "return value problem" |
| C4 (LLM cliche) | Miss | — | No review checks for stock LLM rhetorical patterns |
| S1 (cut duplicate bridge) | Miss | Prose redundant-restatement: INFO | Found a *different* redundancy (closing restates opening) but not the bridge paragraph duplicating the next section |
| S2 (merge sections) | Near-miss | Complexity claim-to-section | Noticed overlap between "Where the problem appears" and "Why they default" but decided "each has enough distinct content to justify separate treatment" |
| S3 (compress taxonomy) | **Explicit miss** | Complexity framework-decoration: CLEAN | Review explicitly passed it: "earns its structure... enables comparison across a dimension — loading profile — that a single prose paragraph would obscure" |
| S4 (fold conv-vs-refinement) | **Hit** | Complexity claim-to-section + connection inflation | "functions as a cross-reference, not an argument step" — recommended folding into Relevant Notes entry |
| S5 (reorder pattern/tension) | Miss | — | No review checks section ordering |
| S6 (split caveat bullet) | Miss | — | Too granular for any review |
| X1 (capitalize bullets) | Miss | — | Cosmetic, below review threshold |
| X2 (fix link path) | Miss | — | /validate's job, not review |

## Summary

**Hits: 2/16** (C3, S4)
**Near-misses: 1** (S2 — noticed but decided against)
**Explicit misses: 2** (A2, S3 — reviewed and judged not-a-problem)
**Silent misses: 11**
**Mistakes: 0**

## Findings not in catalogue

The reviews also surfaced findings that don't correspond to any of our 16 changes:

- Semantic WARN: trace taxonomy missing structured intermediate artifacts (opposite direction from S3)
- Semantic WARN: five reasons omit hard context-window exhaustion
- Semantic INFO: overlapping problem locations (chat sessions vs continuing sessions)
- Semantic INFO: Slate uncertainty weakens pattern claim
- Semantic INFO: "cheap/expensive" gloss not in orchestration model source
- Semantic INFO: temporal boundary between exploratory and mature phases unspecified
- Prose WARN: trace taxonomy confidence miscalibration (own construction presented as established)
- Prose INFO: anthropomorphic framing ("thought," "want")
- Complexity INFO: 11 Relevant Notes is high, 2 footer-only

## Analysis

**The big gap is accessibility.** All 4 A-items missed. No existing review asks "would someone outside this KB understand this note?" The pseudo-formalism check came closest (A2) but evaluated notation as internal cross-reference rather than reader accessibility.

**Sentence-level prose issues are invisible.** C1 (ambiguous negation), C2 (wrong framing), C4 (LLM cliche) are below the granularity of all three reviews. The prose review checks for representational patterns, not individual sentence quality.

**Structural judgments diverge from ours.** S2 and S3 were noticed but the reviews reached opposite conclusions. The complexity review thought the trace taxonomy earned its weight; we compressed it. The complexity review saw the section overlap; we merged them.
