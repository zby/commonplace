=== PROSE REVIEW: semantic-review-catches-content-errors-that-structural-validation-cannot.md ===

Checks applied: 8

WARN:
- [Source residue] The motivating case in paragraph 2 refers to a specific internal note ("The synthesis note on learning operations") and its specific content ("three learning operations (constraining, distillation, discovery)" and the omission of "accumulation"). This is a concrete KB-internal example that works well as illustration, but the phrase "simply adding knowledge to the store" to describe accumulation is KB-domain-specific vocabulary that a reader unfamiliar with this KB's vocabulary layer would not parse. Mild residue — the note is clearly about KB maintenance so the domain fits, but the specificity of the example does double duty as both illustration and implicit argument, which makes it harder to evaluate the general claim independently.
  Recommendation: Frame the motivating case with a single sentence establishing it as a specific instance: "For example, in this KB..." or similar. The example is effective; it just needs a one-phrase frame to separate the general claim from its illustration.

- [Confidence miscalibration] The four semantic checks are presented with assertive framing: "Four semantic checks structural validation cannot perform" (section heading) and each check is stated as a named, defined procedure. This is the note's own construction — no source is cited for this particular decomposition. The note does not flag the taxonomy as proposed. Given the note's `status: seedling`, the assertive framing ("the four checks," "each semantic check is a weak oracle") overstates the epistemic status. The four checks may be the right four, but the note presents them as THE four rather than as a proposed set.
  Recommendation: Hedge the section heading and framing: "Four candidate semantic checks" or "Four semantic checks that structural validation misses." In the pyramid section, soften "each semantic check is a weak oracle" to "each check functions as a weak oracle" — this avoids implying the set is closed. The note already uses "would" for the review skill section, which is appropriately tentative; match that register in the taxonomy section.

INFO:
- [Proportion mismatch] The core claim is that semantic review catches content errors structural validation cannot. The four checks (the payload) get roughly equal treatment (~4 sentences each), which is well-proportioned internally. However, the "review skill as implementation target" section (the how) gets comparable space to the "motivating case" section (the why). For a seedling note, the implementation-target section may be premature — it makes claims about cost models and failure semantics that aren't grounded yet. This isn't a clear mismatch, but the note's weight tilts slightly toward implementation planning rather than toward deepening the four checks themselves.

- [Redundant restatement] The opening of "Where these sit in the text testing pyramid" restates the Level A/Level B distinction already established in the first paragraph ("These are Level A checks... deterministic, cheap, reliable"). The pyramid section's first sentence ("These are Level B checks — they require LLM judgment but can be structured with rubrics") adds the Level B placement, but the contrast with Level A was already drawn in the opening. Minor overlap — not a full paragraph of restatement, but the Level A framing appears twice.

CLEAN:
- [Pseudo-formalism] No formal notation, equations, or symbolic apparatus present. The note uses prose throughout. Clean.

- [Orphan references] The note references "Simon's definition" twice. This is not fully cited (no publication, no year), but it's attributed to a named figure and used as a reference point rather than as a quantitative claim. The "three learning operations" are specific to this KB, not orphan empirical claims. No unattributed numbers or percentages. Clean — the Simon reference is borderline but functions as a known shorthand within this KB rather than an unsupported empirical claim.

- [Unbridged cross-domain evidence] No cross-domain transfers attempted. The note discusses KB maintenance practices and illustrates with KB maintenance examples. The Simon reference is from learning theory applied to a learning-theory note — the domains match. Clean.

- [Anthropomorphic framing] The note discusses LLM judgment ("require LLM adversarial reading," "an LLM might flag a valid enumeration as incomplete") but uses appropriate language. "LLM judgment" and "adversarial reading" describe the LLM's operational role, not mental states. No instances of "understands," "believes," "knows," or "possesses." Clean.

Overall: 2 warnings, 2 info
===
