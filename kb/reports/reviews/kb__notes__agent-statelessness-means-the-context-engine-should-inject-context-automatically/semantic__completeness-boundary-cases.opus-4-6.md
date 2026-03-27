# Completeness & Boundary Cases

**Note:** `kb/notes/agent-statelessness-means-the-context-engine-should-inject-context-automatically.md`

## Enumerations tested

### 1. Four-tier loading hierarchy (Reasoning section, lines 58-63)

| Tier | Description |
|------|-------------|
| Always | CLAUDE.md, skill descriptions |
| On reference | definitions, ADRs, relevant indexes |
| On invoke | skill bodies |
| On demand | methodology notes, source reviews |

**Boundary cases:**

- **Simplest instance (single definition reference):** A note links to one definition. The context engine injects it on first reference. Maps cleanly to tier 2. PASS.
- **Most extreme instance (30 definitions + 5 ADRs):** Tier 2 attempts to inject all of them. The note acknowledges this in the context budget caveat (line 68: "Even small definitions add up. With 20 technical terms, auto-injecting all on first reference might cost 4-5K tokens"). The hierarchy itself has no budget-aware fallback tier — what happens when "on reference" exceeds the budget? The caveat recognizes the problem but the hierarchy doesn't encode a response (e.g., priority ordering within tier 2, or demotion to tier 4). Covered by caveat, not by the framework. **INFO — the hierarchy has no budget-overflow behavior.**
- **Recursive injection (content between tiers):** A skill body (tier 3) loads on invoke and itself references a definition. Does the context engine recursively process injected content, triggering tier 2 injection within tier 3? The note doesn't address recursive injection at all. This is a genuine boundary the framework doesn't cover. **INFO — recursive injection across tiers is unaddressed.**
- **Adjacent concept (frequently-referenced methodology note):** A methodology note that's small, stable, and referenced by many notes shares the properties that make definitions good injection candidates, but falls into tier 4 (on demand). The framework handles this by framing the candidates table as "hypotheses" (line 50), but the hierarchy presents tiers as a clean taxonomy without acknowledging that the type-based assignment may misclassify borderline items.

### 2. Injection candidates table (Evidence section, lines 43-50)

Four rows: definitions, area indexes, ADRs, specs.

**Boundary cases:**

- **Type templates:** Small, stable, needed when writing in a typed directory. Share properties with definitions but aren't listed. The table explicitly calls each row "a hypothesis" and says the trigger mechanism "may differ per case" — so the omission is by design (open-ended list), not an oversight.
- **Memory entries:** Claude Code's MEMORY.md entries are always-loaded but might also benefit from selective injection in other contexts. The always-loaded mechanism survey note describes memory as a separate surface. No gap here — the table addresses on-reference injection, not always-loaded content.

### 3. Four properties making definitions the "cleanest case" (lines 21-28)

Small, stable, referential not argumentative, loaded once per session.

**Boundary cases:**

- **Large definition:** The note handles this boundary explicitly — "a definition that needs Evidence/Reasoning/Caveats is really a `structured-claim` about the term, not a definition" (line 37). Clean boundary.
- **Unstable definition:** The staleness caveat (line 69) addresses this. Covered.
- **A "referential" link that turns out to require evaluation:** What if the agent encounters `codification` in a context where the term's applicability is disputed? The distinction between "referential" and "argumentative" links assumes the usage context doesn't matter. In practice an injected definition could become the subject of debate. The note doesn't address context-dependent link semantics. **INFO — referential vs argumentative is treated as a property of the link, but may depend on usage context.**

## Summary

No WARNs. Three INFOs:

1. **INFO:** The four-tier hierarchy has no budget-overflow behavior — what happens when tier 2 injection exceeds context limits is acknowledged as a problem in Caveats but not addressed in the hierarchy itself.
2. **INFO:** Recursive injection (content loaded via injection referencing other injectable content) is unaddressed.
3. **INFO:** The referential/argumentative distinction is treated as a link property but may be context-dependent.
