=== SEMANTIC REVIEW: distilled-artifacts-need-source-tracking-at-the-source.md ===

Claims identified: 11

1. Distillation produces artifacts optimized for a single goal (para 1)
2. Inline links to sources would dilute focus of distilled artifacts (para 1)
3. "The reader of the instruction doesn't need to follow a link to understand why a convention exists; they need to follow the convention." (para 1)
4. When a source note changes, every artifact distilled from that source is potentially stale (para 2)
5. Without a record of what went into the distillation, there's no way to know which artifacts to review (para 2)
6. "The dependency link belongs at the source, not the target." (Source-side tracking)
7. A distillation typically draws from multiple source notes (Source-side tracking)
8. Source-side tracking optimizes for the primary maintenance scenario (Source-side tracking)
9. The reverse query is cheap: grep finds all notes linking to a target (Source-side tracking)
10. The distilled artifact has no staleness signal (table)
11. Staleness detection flows in the direction of change (closing paragraph)

WARN:
- [Completeness] The note claims "Without a record of what went into the distillation, there's no way to know which artifacts to review" (para 2). But the note itself later acknowledges a reverse lookup mechanism: "rg 'WRITING.md' kb/notes/ finds all notes linking to the target." If a maintainer knows which distilled artifact they care about, they can already find its sources via grep — even without "Distilled into:" links. The "no way to know" claim is about the forward direction (source changed, which targets are affected?), but the absolute phrasing oversells the gap. The reverse direction is cheap and always available; what's missing without source-side tracking is specifically the forward direction. The note knows this (the table and the grep sentence show it) but the paragraph 2 framing elides the distinction.

- [Completeness] The note's framework presents exactly two options: links at the source ("Distilled into:") or links at the target (inline back-links in the distilled artifact). It argues for source-side and against target-side. But there is a third option the framework does not consider: a separate dependency manifest — a standalone file or section that maps sources to distilled targets, owned by neither. This is how many build systems work (Makefiles, package.json dependency lists). The linked note on make-like staleness detection describes precisely this kind of external dependency graph. A manifest would avoid both problems the note identifies (diluting distilled artifacts AND burdening source notes with forward pointers that may themselves go stale). The binary framing may still reach the right conclusion, but the space of alternatives is larger than presented.

INFO:
- [Grounding] The link to "indirection is costly in LLM instructions" is annotated as "motivates: why distilled artifacts shouldn't carry links back to sources." The indirection note argues that variables, config references, and abstraction layers cost interpretation overhead in LLM instructions. But a markdown link in a note is not the same kind of indirection — it does not require the LLM to resolve a variable or perform substitution. A link is inert unless followed. The indirection note's argument is about cognitive/computational overhead during execution, not about the mere presence of navigational metadata. The motivational relationship is plausible (both concern keeping distilled artifacts lean) but the mechanism is different from what the source note actually describes.

- [Grounding] The link to "frontloading spares execution context" is annotated: "motivates: distillation is a form of frontloading; source-side tracking preserves the pre-frontloaded dependency structure." The frontloading note is about pre-computing static parts of instructions to spare execution context. The connection to source tracking is indirect: the note under review argues that distillation is a kind of frontloading (reasonable), and that source-side tracking preserves the dependency structure that frontloading eliminates from the target (also reasonable). But the frontloading note itself says nothing about tracking dependencies or provenance. The inference chain (frontloading removes derivation traces -> therefore we need source-side tracking to preserve them) is the reviewed note's own move, not something grounded in the source.

- [Internal consistency] The note says distilled artifacts should have "no staleness signal" (table row), but the note also states that grep can find all sources linking to a distilled target. If sources carry "Distilled into:" links, and a maintainer runs grep on the distilled artifact's filename, the distilled artifact effectively does have an indirect staleness signal — it just requires the maintainer to initiate the query rather than seeing it inline. The table's clean "None" slightly overstates the asymmetry.

- [Completeness] Claim 9 ("The KB is small enough that grep is the query engine") is presented as a supporting argument for the reverse-lookup being cheap. This implicitly scopes the entire design to small KBs. The note does not discuss what happens when the KB grows large enough that grep becomes expensive or produces too many false-positive matches. This is not necessarily a problem (the note may be intentionally scoped), but the scope limitation is implicit rather than stated.

PASS:
- [Internal consistency] The two-audience table is internally consistent with the rest of the note. The reader/links/staleness-signal decomposition faithfully maps to the prose arguments in each section. No definition drift detected — "distilled artifact," "source note," "staleness," and "focus" are used consistently throughout.
- [Grounding] The link to "skills derive from methodology through distillation" is accurately attributed. That note establishes distillation as the methodology-to-skill derivation relationship, and the reviewed note builds on that foundation by addressing how to track the derivation. The "foundation" relationship annotation is correct.
- [Grounding] The link to "link graph plus timestamps enables make-like staleness detection" is accurately attributed. That note describes using the link graph for staleness detection; the reviewed note's "Distilled into:" links provide additional dependency edges for that mechanism. The "extends" annotation is appropriate.
- [Internal consistency] The note's title claim ("distilled artifacts need source tracking at the source") is faithfully developed by the body. The argument flows coherently: distilled artifacts should stay focused (para 1) -> but staleness detection needs dependency information (para 2) -> therefore track at the source (Source-side tracking section). No compressed summary elides tensions.
- [Completeness] The note's central design recommendation (put "Distilled into:" links in source notes) was tested against boundary cases: (a) a distillation with a single source (the "typically draws from multiple" claim still works — a single source just has one entry); (b) a distilled artifact that is itself a source for further distillation (the pattern composes — the intermediate note carries both incoming links and its own "Distilled into:" footer); (c) a source that is distilled into many targets (the pattern scales linearly in footer entries). All boundary cases map cleanly.

Overall: 2 warnings, 4 info
===
