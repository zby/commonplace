"spec" — used without inline definition: "A `spec` needs Design/Implementation sections." In this KB, `spec` is a document type with specific meaning (a KB type name, not just a generic specification). A reader unfamiliar with the KB's type system cannot tell from context what a `spec` is beyond the circular implication that it requires Design/Implementation sections.

"structured-claim" — used similarly: "`structured-claim` needs Evidence and Reasoning sections." This is a KB-internal type name used as if known.

Both are used as type names within a sentence that discusses the type system, so the context does hint they are document types — but does not define them or link to their definitions. Given the note's purpose (explaining how text artifacts can be tested), a reader encountering these names for the first time needs at least a brief gloss or link to the type definitions.

"wiki-links" — used in the Deterministic level bullet: "no dangling wiki-links." The note links to `./storing-llm-outputs-is-constraining.md` via `[artifact testing problem]` but does not define wiki-links inline. "Wiki-link" is a specific format (double-bracket `[[...]]` links as opposed to standard markdown links) that is KB-convention vocabulary. A brief gloss or the note's own convention statement that this KB does not use wiki-links would clarify.
