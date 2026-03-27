The note contains three enumeration frameworks: the three properties (discoverable, composable, trustworthy), the five operations (accumulation, constraining, distillation, discovery, pruning), and the reach spectrum (facts → theories). Each is tested below.

---

**Framework 1: Three properties**

Grounding definition: properties needed for knowledge to improve an agent's actions under bounded context.

- Simplest instance: a single fact note. All three properties apply cleanly — a fact is discoverable if named well, trustworthy if current, composable if linked. ✓
- Most extreme: the entire internet. The bounded-context constraint makes it undiscoverable and unworkable — but this is within the framework's stated constraint. ✓
- Adjacent concept — **efficiency**: a note can be discoverable, composable, and trustworthy yet wasteful in context usage (long, dense, poorly scoped to likely queries). Context efficiency is addressed at the KB level through discoverability, but not as a property of individual notes. INFO — the gap is small because discoverability partially subsumes efficiency (a well-described note won't be loaded unnecessarily), but the connection is implicit.
- Adjacent concept — **currency**: the note explicitly acknowledges this as not fully resolved: "trustworthiness has a temporal dimension these mechanisms don't fully address." The acknowledgment is appropriate and internally flagged. No action needed.

**Framework 2: Five operations**

Grounding definition: operations that act on knowledge — accumulation (basic), constraining/distillation/discovery (transform), pruning (subtract).

- Simplest: adding one note (accumulation). ✓
- Most extreme: rewriting the entire KB. Covered by multiple overlapping operations. ✓
- Between items — **link maintenance**: adding or updating cross-note links is a common KB operation. It improves composability but doesn't fit cleanly into any of the five operations. Linking is treated as a mechanism under composability (a property), not as an operation. INFO — the gap is real but not consequential; link maintenance could be subsumed under "accumulation" or "constraining" without distorting those categories significantly.
- Between items — **curation/organization**: creating or updating indexes (area indexes, tags-index) is an operation that doesn't map cleanly to the five. It's not accumulation (no new knowledge), not constraining (no narrowing of interpretation), not distillation (no compression), not discovery (no new general concept), not pruning (nothing removed). INFO — the same as above; this is a structural maintenance operation the five-operation model doesn't name.

**WARN — pruning scope inconsistency**: The body defines pruning as "removes knowledge that is outdated, contradictory, or low-value." The table example lists "Deleting an outdated note, *marking a superseded claim `outdated`*" — marking is not removing. Soft pruning (marking, deprecating) and hard pruning (deleting) have different effects on discoverability and trustworthiness: a marked note is still loadable and can still mislead; a deleted note isn't. The framework doesn't distinguish these, but the example implies both are pruning. Either the definition should widen to include soft pruning, or the example should be corrected to reflect only deletion.

**Framework 3: Reach spectrum**

Grounding: Deutsch's distinction between adaptive (low-reach) and explanatory (high-reach) knowledge.

- Simplest: "the meeting is at 3pm" — minimal reach, clearly adaptive. ✓
- Most extreme: Newton's optics — high reach, transfers across contexts. ✓
- Between: heuristics and rules of thumb have some reach but aren't full theories. The note handles this through the "programming fast-pass" as a category with partial reach. ✓
- Adjacent: tacit knowledge (knowledge that can't be written down) — out of scope; the KB operates on written artifacts. Not claimed.

Overall: one WARN (pruning definition vs example), two INFOs (link maintenance and curation as unnamed operations). The three-property and reach frameworks are clean.
