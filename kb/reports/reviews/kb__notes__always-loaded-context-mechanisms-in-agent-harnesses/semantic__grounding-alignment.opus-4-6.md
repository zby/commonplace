The note cites four KB notes and two external sources. Central claims traced below.

---

**Claim: cross-platform convergence on similar surfaces**

The note observes that Claude Code, Codex, Gemini, and Cursor have similar always-loaded mechanisms. It hedges: "Whether this reflects genuine convergence or shared ancestry from early prompt-engineering practices is unclear." The [OSS study] is cited as documenting "current similarity but not the history." Appropriate hedging. ✓

**Claim: Lopopolo maintains a 100-line AGENTS.md as "a map with pointers"**

Cited to the Harness Engineering ingest. Specific factual claim. INFO — I cannot verify the exact line count or the characterization without reading the source, but the specificity suggests it's drawn from the source directly.

**Claim: AGENTS.md files average 142 lines (SD=231), CLAUDE.md average 287 lines (SD=112)**

Cited to the OSS study. Specific statistics. The high SD for AGENTS.md (231 on mean 142) suggests a skewed distribution. ✓

**Claim: the control-plane model proposes three layers for system prompt organization**

Cited to [agents-md-should-be-organized-as-a-control-plane.md]. I have read this note; the three layers (invariants, routing, escalation) are accurately represented. ✓

**Claim: the loading hierarchy establishes why always-loaded context must be slim**

Cited to [instruction-specificity-should-match-loading-frequency.md]. Consistent with the KB's treatment. ✓

**Claim: configuration injection is "partial evaluation applied to instructions"**

Cited to [frontloading-spares-execution-context.md]. The characterization (pre-computing static parts so the agent doesn't waste context on resolution at runtime) is a valid application of partial evaluation. ✓

---

No WARN. One INFO on unverified Lopopolo statistics.
