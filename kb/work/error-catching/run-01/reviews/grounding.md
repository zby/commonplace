# Grounding-alignment review — run-01

Gate: `kb/instructions/review-gates/semantic/grounding-alignment.md`

## grounding-A
### Findings
- WARN — False attribution to the Ashby source. The item states the Homeostat is a case "which Ashby himself analyses as a proposal-selection loop with a one-bit oracle." The cited source (`kb/sources/ashby-design-for-a-brain-ultrastability.md`) says the opposite on every element: "No evaluator or oracle. Nothing scores, ranks, or compares candidates... it does not evaluate a candidate"; the Homeostat "is not an instance of the proposal-selection improvement loop"; the variation–selection–retention mapping "is an analyst's **reconstruction**"; and, decisively, "Ashby did not decompose adaptation into generator and oracle, and translating him as though he had would credit him with distinctions he explicitly did without." The item cites the source as grounding an analysis the source explicitly disclaims — vocabulary and attribution mismatch, not mere compression.
- The rest of the Ashby paragraph (retention persists and steers, blind draws from a random-number table, nothing reads the setting, nothing compounds) is accurately grounded in the source; the flaw is confined to the attribution clause.
## Result: WARN

## grounding-B
### Findings
- none. The item's routes match the linked material: the oracle-strength spectrum is cited as "proposes a gradient," matching that note's own speculative framing; the in-toto paragraph stays within the source's scope (hard cryptographic oracles) and explicitly disclaims transfer to judgment-heavy verification; the Rabanser characterization matches how the oracle-strength note reports the same study; non-independence of the four sources is acknowledged and the conclusion is hedged as "a candidate for a general principle." The convergence inference is presented with its own caveats, so the stated route supports the stated (hedged) conclusion.
## Result: PASS

## grounding-C
### Findings
- WARN — Scope overreach on the in-toto source. The item claims "The paper demonstrates that any operational trust decision — including judgment-heavy ones like KB curation — can move from manual review to automation once the process is represented as signed metadata with cheap final verification." The source (`kb/sources/in-toto-farm-to-table-guarantees.md`) is a supply-chain integrity paper whose verification rests on byte identity, signatures, and artifact-flow rules; it says nothing about judgment-heavy decisions or KB curation, and its guarantees depend precisely on the availability of those hard cryptographic oracles. The extension to "any operational trust decision" is the item's own inference presented as the paper's demonstration.
- The overreach also contradicts the item's own argument elsewhere: "Why convergence matters" concedes in-toto "could be dismissed as a special property of cryptographic byte workflows," and "The practical implication" says KB curation stalls exactly because no one can cheaply verify judgment-heavy mutations.
## Result: WARN

## grounding-D
### Findings
- WARN — Cited note's scope broadened beyond what it claims. The item states that "[retrieval failure is reflection failure] establishes that this failure mode governs every self-improving architecture, parametric ones included." The linked note (`kb/notes/retrieval-failure-is-reflection-failure.md`) explicitly restricts itself in its Scope section: "The claim concerns systems whose causal connection is retrieval-mediated. Where a self-representation is consumed by an interpreter or compiler that reads all of it, retrieval is not the wire and this failure mode does not arise." The item's own preceding sentence also contradicts the citation — it says of parametric compounding that "nothing can fail to 'find' the retained change," i.e. parametric pathways are exactly where the failure mode does not apply.
- The Ashby paragraph in this variant is accurately grounded (no attribution of the proposal-selection reading to Ashby himself).
## Result: WARN

## grounding-E
### Findings
- INFO — The central premise is grounded with "since the boundary of automation is the boundary of verification," citing a note that presents that claim as a hedged synthesis ("If this holds...", "a candidate for a general principle," with a caveat that verification is the primary structural boundary, not the only one). The item uses it as a settled ground. The inference is plausible and the item's own scope section adds compatible hedges (warrant is objective-, risk-, and threshold-relative), but the route leans on a stronger reading than the cited note asserts.
- The Gödel-machine characterization matches the linked note (proof-gated acceptance, "must ignore those self-improvements whose effectiveness it cannot prove," warrant relative to the formalization); the Commonplace evidence matches the reference note (tests/validators plus human judgment, autonomy stopping at the human gates); the oracle-strength spectrum is cited modestly ("describes different verification surfaces, not a total order"); the false-positive link matches that note's claim.
## Result: PASS

## grounding-F
### Findings
- WARN — Overclaimed grounding from the oracle-strength spectrum. The item states the spectrum "establishes a gradient... and demonstrates that a task's automation feasibility is fixed by its position on that gradient." The linked note (`kb/notes/oracle-strength-spectrum.md`) says of itself: "This note proposes that the distinction is better understood as a gradient... The framework is speculative; the individual hypotheses need testing," and its maturation section lists the core reframing as "currently asserted by analogy" and needing independent support. "Establishes"/"demonstrates" misstates the epistemic status, and "automation feasibility is fixed by its position" is a determinism claim the linked note nowhere makes.
- The overclaim contradicts the item's own hedge in "Why convergence matters": "The oracle-strength spectrum could be an internally consistent theory that happens not to be true."
## Result: WARN
