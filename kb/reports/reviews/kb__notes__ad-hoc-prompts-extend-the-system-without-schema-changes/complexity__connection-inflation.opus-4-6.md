warn

The note has 8 footer links. Several restate connections made explicit in the body:

**Inflated entries:**
- `instructions-are-typed-callables` — body says "Typed callables sit at the other end" with inline link and explains the contrast fully. Footer's "Both are correct for different moments" is already stated in the body.
- `methodology-enforcement-is-constraining` — body says "the enforcement gradient (methodology-enforcement-is-constraining.md)" with inline link and explains the gradient. Footer is redundant.
- `wikiwiki-principle-lowest-friction-capture-then-progressive-refinement` — body says "This is lowest-friction capture, then progressive refinement applied to the skill layer" with inline link. Footer is redundant.
- `skills-derive-from-methodology-through-distillation` — body says "The extraction step itself is distillation" with inline link. Footer is redundant.

**Justified entries:**
- `unified-calling-conventions-enable-bidirectional-refactoring` — not mentioned in the body at all. Footer reveals a non-obvious connection (unified conventions make prompt → skill extraction possible without changing call sites).
- `a-functioning-kb-needs-a-workshop-layer-not-just-a-library` — not linked in the body. Footer identifies that workshop is where ad hoc instructions live and library is where they constrain into skills — a non-obvious architectural mapping.
- `llm-context-is-composed-without-scoping` — linked inline, but the footer's "grounds: ad hoc instructions notes are effective sub-agent interfaces because they provide lexically scoped frames" adds a navigational label useful for agents loading the footer.
- `programming-practices-apply-to-prompting` — footer's framing ("sometimes staying at the prompt level is the right choice, not a failure to compile") adds an angle not stated explicitly in the body.

Four entries (instructions-are-typed-callables, methodology-enforcement-is-constraining, wikiwiki-principle, skills-derive-from-distillation) are inflation. Removing them would reduce noise; the relationships are fully covered inline.
