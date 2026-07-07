# Compression Bundle Review: A derived copy of recomputable truth must be checked or absent

**Target:** `kb/notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md`
**Bundle:** `kb/work/agent-note-improvement/compression/`

## Overall Result

WARN

## Gate Results

| Gate | Result | Summary |
|---|---|---|
| compression/core-claim-obscured | PASS | The claim ("checked or absent; hand-maintained-and-trusted is forbidden") is stated in the frontmatter description, the title, and the opening paragraph, in bolded terms, before any apparatus. |
| compression/branch-bloat | INFO | "What enforcement buys" resolves a real tension between two other notes but is not needed to support the core deontic claim; its destination (stay condensed here vs. live mainly as a link relationship) is unclear. |
| compression/detail-overhang | WARN | Two passages elaborate past the point their job requires: the second paragraph of "Where the rule applies" and the "What enforcement buys" section, both of which end by compressing themselves into a single sentence, showing the surrounding prose was excess. |
| compression/marginal-value-redundancy | WARN | "What enforcement buys" (3 paragraphs) restates, at length, exactly what the two corresponding "Relevant Notes" bullets already say in one line each — fold the section down or let the link descriptions carry it. |

## Findings

### compression/branch-bloat

- INFO: The "What enforcement buys" section (four paragraphs, from "Two established principles pull in opposite directions..." through "...secures frontloading's validity window") is not required to support the note's core claim ("must be checked or absent"). It supplies a genuine, non-obvious synthesis — a third class ("recomputable-and-checked") between arbitrary and situational — but that synthesis is really an extension of two *other* notes' framework (`frontloading-spares-execution-context.md`, `fix-what-the-executor-cant-determine-not-what-it-will.md`), not a load-bearing premise for this note's own argument. Consider whether this belongs as a full section here versus a compressed aside, since the "Relevant Notes" list already carries the same relationship as one-line "extends" descriptions.

### compression/detail-overhang

- WARN: "Where the rule applies" section, second paragraph ("What flips the regime is the check price. ... Same structure throughout — derived copy, moving source, staleness risk — at a different check price; the price is what changes the balance."). The final sentence compresses the whole paragraph's point into one clause. The preceding four sentences (Level A/B framing, "two things change," interrupt-placement dissolving) restate the same idea three times with heavy parallel rhetoric before the paragraph closes by summarizing itself. Compress to roughly: state the check-price flip, name the two consequences (enforce-or-omit becomes mandatory; the validator becomes the interrupt surface) in one sentence each, and drop the closing recap sentence or use it *as* the topic sentence instead.
- WARN: "What enforcement buys" section restates both cited notes' claims in more detail than a reader needs to follow the argument here (a full sentence each rehearsing "frontloading wants X" and "the executor principle wants Y" before resolving the tension). Since both notes are already linked, the setup can be one clause per side ("frontloading wants it inlined; the executor principle wants it left out") rather than a full paragraph restating each note's reasoning.

### compression/marginal-value-redundancy

- WARN: The "What enforcement buys" section's payload — enforcement creates a third class, "recomputable-and-checked," between arbitrary and situational, reconciling frontloading with the fix-what-the-executor-can't-determine principle — is already stated concisely in the two corresponding "Relevant Notes" bullets: "extends: enforcement is the move that secures frontloading's validity window for recomputable inserted values" and "extends: adds recomputable-and-checked as a third class between arbitrary and situational on its fix-or-leave axis." The body section spends roughly four paragraphs re-deriving what those two lines already assert. Deletion test: removing the section would not break the note's stated support route for "must be checked or absent" — the "What checked requires" and "Consequences" sections carry that weight independently. Fold the section down to a short paragraph (the third-class framing plus one sentence on why it matters) and let the two link descriptions carry the rest, or keep the fuller version only if the note's purpose is meant to include this synthesis as a second, coequal contribution.

## Suggested Revision

Keep the note's opening paragraph, "The asymmetry that forces the rule," "Where the rule applies" (trim its second paragraph to its closing-sentence-level compression), "What checked requires — and its limits," "Consequences," and "Instances across four surfaces" essentially as-is — they carry the deontic claim and its scope without excess. Shrink "What enforcement buys" from four paragraphs to one short paragraph: name the tension between frontloading and the executor-fix principle in a clause each, state that enforcement is the resolving third class, and stop — trusting the "Relevant Notes" extends-bullets to carry the fuller cross-reference rather than re-deriving it in the body. This preserves the note's actual claim ("checked or absent") at full prominence while cutting the section that does the least first-party work per sentence.
