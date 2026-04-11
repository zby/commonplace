# Carnap: Explication

## Candidate borrowing

Carnap's explication replaces a vague or everyday concept with a sharper technical concept suited to a purpose. The KB already mentions this in [Constraining](../../notes/definitions/constraining.md): explication is constraining applied to concepts rather than systems.

The expansion would make explication an explicit methodology for KB vocabulary work.

## Why it fits

Commonplace depends on terms whose everyday meanings are too broad for reliable agent use: distillation, constraining, codification, context engineering, workshop, reach. The value of defining these terms is not terminological neatness. It narrows future interpretation space.

This makes definition notes a specific kind of constraining artifact:

- They replace vague terms with operational terms.
- They state what the term does and does not cover.
- They let future notes link to a stable meaning instead of redefining the term each time.
- They reduce ambiguity for agents consuming the KB.

## Possible operational form

Definition-writing could use an explication checklist:

1. What vague or overloaded term is being sharpened?
2. What operational purpose does the sharpened term serve in this KB?
3. What nearby meanings are explicitly excluded?
4. What workflows or review gates depend on this term?
5. What would count as misuse of the term?

This would improve the current "inline gloss and definition pointer" practice by giving definition notes their own quality criterion.

## Existing connections

- [Constraining](../../notes/definitions/constraining.md) — current mention of Carnap's explication as prior work
- [Context engineering](../../notes/definitions/context-engineering.md) — example of a term sharpened for the KB's architectural use
- [Distillation](../../notes/definitions/distillation.md) — example of a term disambiguated from ML knowledge distillation
- [Codification](../../notes/definitions/codification.md) — example of a term pinned to a specific medium-transition meaning
- [ADR 011: notes must be accessible to external readers](../../reference/adr/011-notes-must-be-accessible-to-external-readers.md) — definition links and glosses keep KB vocabulary usable outside always-loaded context

## Failure mode

The risk is turning every definition into a philosophical essay. Explication is useful only when it constrains future use. If a term is ordinary and unambiguous, no definition note is needed.

## What would make this worth promoting?

Promote this if definition notes start drifting or if agents misuse KB vocabulary despite existing definitions. The likely artifact would be a short section in definition-writing guidance, not a broad philosophy note.
