=== PROSE REVIEW: link-strength-is-encoded-in-position-and-prose.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The note presents its own taxonomy of link strength levels (two tables classifying position and prose patterns into five-tier strength hierarchies) using direct assertion ("Position in the document is the strongest signal," "A link woven into the argument is load-bearing") without flagging these as proposed frameworks. The five-level position hierarchy and the five-level prose-pattern hierarchy are the note's own constructions, not cited from prior work. They read as established fact rather than proposed classification. The hedging that does exist ("probably right for now" in the metadata section) does not extend to the core taxonomy.
  Recommendation: Add a framing sentence before the tables acknowledging these are proposed classifications -- e.g., "A plausible ranking of strength signals, from strongest to weakest:" -- and reserve direct assertion for the less controversial claim that position and prose carry strength information at all.

- [Proportion mismatch] The note's core claim is in its title: link strength is encoded in position and prose. The section that carries this claim ("Strength signals") is well-developed at roughly 200 words plus two tables. However, "What link strength affects" receives comparable or greater treatment (~200 words across four subsections), and "Should strength be explicit metadata?" gets another ~100 words. The consequences and implementation sections together outweigh the core mechanism section. More importantly, the "What link strength affects" section introduces four distinct applications (traversal priority, note scoring, quality signals, /connect guidance) each at thin single-paragraph treatment, spreading attention rather than deepening the core claim.
  Recommendation: Consider whether the four application subsections belong in the notes they reference (e.g., the scoring paragraph could live in the quality-signals note) rather than here. Alternatively, develop one or two applications deeply rather than four thinly.

INFO:
- [Pseudo-formalism] "This is PageRank with link-weight" (line 43) invokes a specific algorithm by name but does not explain how the proposed scheme maps to PageRank mechanics. PageRank involves iterative propagation of scores through a graph with damping; the note describes a simpler scheme where inbound links are weighted by strength. Calling it "PageRank with link-weight" may overstate the formality of the proposal, though this is a single phrase rather than sustained pseudo-formalism.

- [Redundant restatement] The opening paragraph restates what the link contracts framework covers ("defines what links should contain -- relationship type, context phrase, click-decision support") before pivoting to its own contribution. The restatement is brief (one sentence) and does serve as a contrast ("But it treats all links as equal edges"), so it is functional. Worth noting but not clearly a problem.

CLEAN:
- [Source residue] The note's claimed generality level (about link strength in knowledge bases) matches its body consistently. All examples are drawn from the KB domain (inline premise links, footer "related" entries, /connect skill). No residue from a narrower or different domain was detected.

- [Orphan references] No unsourced specific numbers, percentages, or named studies appear. The arscontexta "specificity test" reference (line 64) is linked to its source. "PageRank" is used as a concept name, not as an empirical claim.

- [Unbridged cross-domain evidence] No cross-domain transfer issues. The note stays within the knowledge-base domain throughout. The PageRank mention (line 43) is used as analogy/shorthand for weighted link scoring, not as evidence transferred from web search to knowledge bases.

- [Anthropomorphic framing] No anthropomorphic language applied to models or systems. References to "an agent deciding what to read next" correctly describe agent behavior without attributing mental states.

Overall: 2 warnings, 2 info
===
