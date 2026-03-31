The note contains three enumeration frameworks: the three properties (discoverable, composable, trustworthy), the five operations (accumulation, constraining, distillation, discovery, pruning), and the reach spectrum (facts → theories). Each is tested below.

---

**Framework 1: Three properties**

Grounding definition: properties needed for knowledge to improve an agent's actions under bounded context.

- Simplest instance: a single fact note with a good title. Discoverable (if well-named), trustworthy (if current), composable (if linked). All three properties apply cleanly. ✓
- Most extreme: the entire internet as a knowledge base. Bounded context renders it undiscoverable, which cascades — per the dependency structure, composability and trustworthiness become inert. The framework handles this correctly through its own stated constraint. ✓
- Adjacent concept — **efficiency/conciseness**: a note can be discoverable, composable, and trustworthy yet wasteful in context budget (verbose, poorly scoped). Context efficiency is treated as a system-level concern addressed through discoverability mechanisms (progressive disclosure, resolution-switching), not as a per-note property. INFO — the gap is minor because discoverability partially subsumes efficiency, but a reader could ask why "efficient" isn't a fourth property given the note's emphasis on bounded context as the central constraint.
- Adjacent concept — **currency**: the note explicitly flags this: "trustworthiness has a temporal dimension these mechanisms don't fully address." Acknowledged and appropriate. No action needed.
- Adjacent concept — **actionability**: the Tension section acknowledges that procedures have low reach but high action value. Whether actionability reduces to the three properties (trustworthy + discoverable procedure = actionable) or is genuinely independent is not fully argued. INFO — the tension section handles this but the resolution relies on the operations (constraining makes procedures reliable) rather than showing actionability is formally covered by the three properties.

**Framework 2: Five operations**

Grounding definition: operations that act on knowledge — accumulation (basic), constraining/distillation/discovery (transform), pruning (subtract).

- Simplest: adding one note (accumulation). ✓
- Most extreme: rewriting the entire KB from scratch. Covered by multiple overlapping operations. ✓
- Between items — **link maintenance**: adding or improving cross-note links is a common KB operation. It improves composability but doesn't map cleanly to any single operation. It could be subsumed under accumulation (adding connection knowledge) or constraining (narrowing link semantics from vague to precise). INFO — the gap is real but not consequential; the five operations don't need to be exhaustive of every KB activity to serve their argumentative role.
- Between items — **reorganization/curation**: creating or restructuring indexes doesn't produce new knowledge (not accumulation), doesn't narrow interpretation (not constraining), doesn't compress (not distillation), doesn't posit a new general concept (not discovery), doesn't remove anything (not pruning). INFO — same as link maintenance; these are structural maintenance activities the model doesn't name.

**WARN — pruning scope inconsistency**: The body defines pruning as "removes or deprecates knowledge that is outdated, contradictory, or low-value." The table example includes "marking a superseded claim `outdated`" alongside "Deleting an outdated note." Marking is not removing — a marked note remains loadable and can still mislead. Soft pruning (deprecation) and hard pruning (deletion) have different effects on discoverability and trustworthiness. The definition mentions "deprecates" which partially covers soft pruning, but the analysis of pruning's effects ("removing a stale note eliminates a source of wrong premises") only describes hard pruning. Either the effects analysis should address both modes, or the distinction should be noted.

**Framework 3: Reach spectrum**

Grounding: Deutsch's adaptive-vs-explanatory distinction.

- Simplest: "the meeting is at 3pm" — minimal reach, clearly adaptive. ✓
- Most extreme: Newton's optics — high reach, transfers across domains. ✓
- Between: heuristics and rules of thumb. These have partial reach — they transfer somewhat but don't fully explain why they work. The note handles intermediate cases through the programming fast-pass (a bet on partial reach) and the three depths of discovery (shared feature → shared structure → generative model). ✓
- Adjacent: tacit knowledge (can't be written down). Out of scope since the KB operates on written artifacts. Not claimed. ✓

Overall: one WARN (pruning definition vs. effects analysis), two INFOs (efficiency as near-miss fourth property, link maintenance/curation as unnamed operations). The three-property and reach frameworks are clean.
