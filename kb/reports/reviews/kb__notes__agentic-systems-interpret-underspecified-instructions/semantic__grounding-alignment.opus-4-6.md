The note cites definitions, linked KB notes, and one empirical source. Central claims traced below.

---

**Claim: constraining narrows interpretation space; codification is the gradient**

Cited to [definitions/constraining.md] and [definitions/codification.md]. The note's treatment of constraining (resolving underspecification + removing indeterminism) is consistent with the KB's definitions. ✓

**Claim: programming practices transfer to prompting under this framework**

Cited to [underspecification-and-indeterminism-make-programming-practices-harder-in-distinct-ways-when-applied-to-prompting.md]. The link describes the relationship as "applies." ✓

**Claim: storing LLM outputs resolves underspecification to a fixed interpretation**

Cited to [storing-llm-outputs-is-constraining.md]. A direct application of the projection model — once you store the output, you've committed to one interpretation. ✓

**Claim: Ma et al. (2026) provides "strongest empirical evidence for the two-phenomena separation"**

Cited to the prompt stability source. INFO — "strongest" is an ordering claim over all available evidence, but the note doesn't survey other empirical evidence systematically. The description (emotion/personality variations change output while holding task spec constant) does sound like a clean test of the separation. The "strongest" qualifier should be verified against the actual body of evidence.

**Claim: "interpretation errors are failures of the interpreter" bounded by the two-phenomena model**

Cited to [interpretation-errors-are-failures-of-the-interpreter.md]. The link semantics say "bounded by: the two-phenomena model assumes a perfect interpreter; real LLMs add a third failure mode." This is an honest self-limitation. ✓

**Claim: context efficiency is "intensified by" underspecification — extra context "distorts interpretation, not just wastes space"**

Cited to [context-efficiency-is-the-central-design-concern-in-agent-systems.md]. INFO — the inference that underspecification makes context qualitatively worse (not just wasteful) is the current note's contribution. The cited note argues context efficiency is central; the current note adds that underspecification amplifies the problem. This is a plausible extension but the mechanism (extra context distorting interpretation) isn't developed here.

---

No WARN. Two INFOs: "strongest empirical evidence" ordering claim, and context-efficiency intensification as own inference.
