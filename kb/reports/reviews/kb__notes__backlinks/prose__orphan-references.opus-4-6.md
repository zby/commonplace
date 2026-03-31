## prose/orphan-references

**Result: WARN**

Two specific figures appear without methodology or source:

1. **"referenced by 48 other notes at time of writing"** (§ The gap) — The number is plausible as a grep count and temporally qualified, but the reader cannot reproduce it without knowing what was counted (filename matches? inline links? both?). A parenthetical like "(per `rg 'deploy-time-learning' --glob '*.md'`)" would ground it.

2. **"30 of 224 notes (13%) lack even outbound Relevant Notes sections as of 2026-03-27"** (§ Design options, option C) — More complex claim: a count, a denominator, a percentage, and a date. No script or methodology cited. The precision (exact count + percentage + date) implies an authoritative audit, but the reader can't verify it.

Both are internal KB statistics that are in principle verifiable, so the risk is low. But unsupported specificity is worse than omitting the number — if the numbers drift as the KB grows, there's no pointer back to how they were computed. Softening to approximate language or citing the method would resolve both.
