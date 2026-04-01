# Gate Review: semantic/grounding-alignment

- Note: `kb/notes/llm-context-is-a-homoiconic-medium.md`
- Outcome: WARN

## Finding 1

**Severity:** WARN

The opening claim is broader than the linked grounding supports.

The note says there is "no type-level distinction" and later "no structural way to distinguish" instructions from data. But the linked grounding note, `kb/notes/llm-context-is-composed-without-scoping.md`, explicitly lists role markers, delimiters, and ordering conventions as weak forms of structure. That source supports the weaker conclusion that the available structure is insufficient to provide robust scope isolation; it does not fully support the stronger claim that structure is absent.

The conclusion about scoping hazards still follows, but the attribution should be tightened to "no enforced or reliable boundary" rather than "no distinction" full stop.

## Finding 2

**Severity:** INFO

The note attributes the "unified calling conventions" result to homoiconicity more directly than the linked note justifies.

`kb/notes/unified-calling-conventions-enable-bidirectional-refactoring.md` grounds the mechanism in shared calling conventions, name-based dispatch, and stable interfaces across neural and symbolic components. That is compatible with the homoiconicity framing, but it is not the same claim. The linked note does not establish that unified calling works *because* instructions and data share one natural-language representation.

This is a plausible synthesis, but not airtight grounding. The note should present it as an inference or application, not as direct support.
