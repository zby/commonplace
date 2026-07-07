# Compression Bundle Review: Bottom-up structure inference needs capture at the decision surface, not the state

**Target:** `kb/notes/structure-inference-needs-capture-at-the-decision-surface.md`
**Bundle:** `kb/work/agent-note-improvement/compression/`

## Overall Result

WARN

## Gate Results

| Gate | Result | Summary |
|---|---|---|
| compression/core-claim-obscured | PASS | Claim is stated in full by the second sentence of paragraph 1 and the title is claim-shaped; later sections are subordinate elaborations, not detours the reader must dig through. |
| compression/branch-bloat | WARN | Two paragraphs step outside this note's own claim to narrate how it relates to *other* notes' claims (wikiwiki principle; create-memory-directly / trace-derived-extraction), duplicating work the Relevant Notes list already does. |
| compression/detail-overhang | INFO | The "why is cheap" section restates the intro's decision-shaped/state-shaped item list in near-synonymous terms before adding its own payload. |
| compression/marginal-value-redundancy | WARN | The same two paragraphs flagged under branch-bloat also fail the redundancy test: their content is already captured, at proportional length, in the Relevant Notes annotations for those same links. |

## Findings

### compression/branch-bloat

- WARN: Section "Capture position is therefore a precondition on the inference mechanism," paragraph 2 (the wikiwiki-principle contrast, "This sharpens the 'structure earned, not imposed' idea...why does not wait."). This paragraph doesn't add a boundary condition, counterexample, or premise for *this* note's claim — it explains how this note's claim relates to a different note's claim. That relation is already recorded, at the same level of insight, in the Relevant Notes entry for `wikiwiki-principle-lowest-friction-capture-then-progressive-refinement.md` ("adds the capture-point condition ... defer structure, but not capture of the why"). Demote to that one link annotation; if the closing line ("the why does not wait") is worth keeping for its memorability, fold it as a single clause into Section 1 instead of keeping a full paragraph here.
- WARN: Section "Boundary: right capture point is necessary, not sufficient," paragraph 2 (the create-memory-directly / trace-derived-extraction paragraph, "The same split explains why creating memory directly...decision-shaped in the first place."). Unlike paragraph 1 of that section (which genuinely narrows the scope of *this* note's claim — necessary vs. sufficient), this paragraph doesn't bound or qualify the current claim; it explains a separate design tradeoff (direct creation vs. deferred extraction) that belongs to those two other notes. It duplicates the Relevant Notes entries for `create-memory-directly.md` and `use-trace-derived-extraction.md` almost verbatim. Cut the paragraph; the two existing link annotations already carry the same content more economically.
- PASS: The two Open Questions are already correctly rehomed as speculative extensions (threshold of "decision-shaped," continuum vs. dichotomy) rather than argued in the body — no action needed.

### compression/detail-overhang

- INFO: Section "The 'why' is cheap at the decision surface and expensive-to-impossible from state," first two sentences ("which evidence it looked at, which policy bound it, which exception it hit, who signed off, what it chose, what followed" / "the row that changed... the final value... the resulting record" vs. "A changed field tells you *that* something is now true...") largely re-lists the same decision-shaped/state-shaped items the intro paragraph already gave ("the inputs referenced, the constraints in play, the exception path, the approval, the action taken, the outcome" vs. "the row that changed, the final value, the resulting record"). The section's real payload — the cheap-vs.-expensive-to-impossible reasoning and the link to the ingress problem — is proportional and worth keeping; only the repeated inventory of examples could be trimmed to a shorter callback ("the same inputs, constraints, and exceptions named above").

### compression/marginal-value-redundancy

- WARN: Same two paragraphs as under branch-bloat (wikiwiki contrast; create-memory-directly / trace-derived-extraction). Deletion test: removing either paragraph breaks nothing in the note's stated support route for its own claim, since the corresponding Relevant Notes bullets already state the relation at equal or better precision. Recommend cutting both paragraphs from the body, keeping the Relevant Notes annotations as the sole record of those two relations (optionally preserving one memorable clause from the wikiwiki paragraph, per the branch-bloat finding).

## Suggested Revision

Keep the intro paragraph, the "why is cheap" section (trim the repeated item list to a short callback), the spec-mining paragraph (it supplies the mechanism-level reason bottom-up inference depends on capture position), and the first paragraph of the "Boundary" section (the necessary-vs.-sufficient scope limit against the authority-at-verification note). Cut the wikiwiki-contrast paragraph and the create-memory-directly/trace-derived-extraction paragraph from the body — both merely re-narrate relations already stated in the Relevant Notes list — optionally keeping one clause from the wikiwiki paragraph ("deferring structure is safe; deferring capture of the why is not") folded into Section 1's close. This shortens the note by roughly two paragraphs while leaving the core claim, its mechanism, and its one genuine scope boundary intact.
