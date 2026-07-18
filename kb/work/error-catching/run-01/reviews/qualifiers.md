# Review: load-bearing-qualifiers

Gate: `kb/instructions/review-gates/semantic/load-bearing-qualifiers.md`

## qualifiers-A
### Findings
- The title "The boundary of automation is the boundary of **symbolic** verification" and the opening claim ("Tasks become automatable when symbolic verification is cheap...") carry the qualifier "symbolic", but the reasoning never uses the symbolic property. The word appears nowhere else in the body. The evidence spans the whole oracle-strength gradient (hard to soft), Amodei's confidence tracking "verification availability" generally, and Tam's "tests, specs, benchmarks" — none of these arguments depends on verification being symbolic rather than, say, human-executed-but-cheap or statistical. "Symbolic" is exactly the kind of signal adjective the gate names. Deletion test: restate as "the boundary of automation is the boundary of verification" — every proof step (generation without verification produces output not automation; discrimination not accuracy; oracle construction as bottleneck) goes through unchanged, and the description frontmatter itself already states the claim without the qualifier ("verification cost as the primary structural determinant of automation"). No hidden boundary case in the body depends on symbolic-ness; the in-toto section's byte-level oracles are an example, not a precondition. Non-load-bearing qualifier narrowing the central claim and filename-level title.
## Result: WARN

## qualifiers-B
### Findings
- none. The title "The boundary of automation is the boundary of verification" states the claim at the breadth the argument actually supports. The remaining scope restriction — "the" boundary meaning "the primary structural boundary, not the only one" — is explicitly flagged and defended in the final caveat, i.e., it is an acknowledged true boundary, not an unexamined narrowing. Qualifiers inside the body ("cheap", "per-instance", "external") are each used by the reasoning (cost asymmetry, discrimination mechanism, unreliable self-assessment) and are load-bearing.
## Result: PASS

## qualifiers-C
### Findings
- The title "The boundary of automation is the boundary of **deterministic** verification" and the opening claim carry the qualifier "deterministic", which the reasoning never uses. "Deterministic" appears in the body only as one property of the hard-oracle end of the spectrum ("exact, cheap, deterministic"), yet the argument explicitly covers a gradient down to soft and no oracles, and cites error correction amplifying *weak* (non-deterministic, above-chance) oracles as part of the practical implication — directly contradicting a determinism precondition. Amodei's confidence gradient and Tam's labor-economics argument turn on verification availability and cost, not determinism. Deletion test: drop "deterministic" and the entire argument goes through unchanged; the description frontmatter already states the unqualified form. "Deterministic" is one of the gate's named signal adjectives. Non-load-bearing qualifier narrowing the central claim and filename-level title.
## Result: WARN

## qualifiers-D
### Findings
- The title "Agent statelessness makes **typed** routing architectural, not learned" narrows the claim to typed routing, but the argument never uses the typed property. The mechanism (each session starts cold; the agent cannot accumulate navigation intuition; therefore routing artifacts are permanent architecture) applies to every routing mechanism the note itself lists — "routing tables, skill descriptions, type templates, naming conventions, directory structure, activation triggers, area indexes" — most of which are not typed at all (naming conventions, directory structure). The description frontmatter states the claim without the qualifier ("all knowledge routing infrastructure ... is permanent architecture"). "Typed" appears only in the title and in one echo phrase ("every typed routing mechanism"); no proof step, boundary, or counterexample depends on it. Deletion test: "Agent statelessness makes routing architectural, not learned" — the argument goes through unchanged. Non-load-bearing qualifier narrowing the central claim and filename-level title.
## Result: WARN

## qualifiers-E
### Findings
- The title "Agent statelessness makes **deterministic** routing architectural, not learned" carries the qualifier "deterministic", which does no work in the reasoning. The argument rests on statelessness and the source-vs-compiled discipline, and the note's own routing inventory includes non-deterministic mechanisms — skill descriptions the agent judges relevance against, "methodology notes load on demand" — so determinism is not even descriptively accurate for the mechanisms covered, let alone a proof precondition. The description frontmatter states the unqualified claim ("all knowledge routing infrastructure ... is permanent architecture"). "Deterministic" is one of the gate's named signal adjectives. Deletion test: drop it and every section (degradation cliff, source vs. compiled, design consequences) goes through unchanged. Non-load-bearing qualifier narrowing the central claim and filename-level title.
## Result: WARN

## qualifiers-F
### Findings
- INFO: The title's "LLM outputs" is LLM-specific wording; the constraining mechanism (a stored sample resolves semantic underspecification and freezes execution indeterminism) would generalize to any stochastic generator. However, the note is plainly scoped to LLM orchestration throughout — prompts, temperature, agent workflows, KB ingestion — and the underspecification/indeterminism properties are argued from LLM behavior specifically, so per the gate's special case this is intentional domain scoping, not a WARN.
- All other qualifiers are load-bearing: "specific" in the description ("keeping a specific LLM output") is the crux of the sample-vs-distribution distinction the testing section builds on; the oracle-strength precondition on the generator/verifier strategy is used to mark exactly where the strategy breaks down (delayed/no-oracle zones, verbatim risk). Removing either would falsify or weaken the argument.
## Result: PASS
