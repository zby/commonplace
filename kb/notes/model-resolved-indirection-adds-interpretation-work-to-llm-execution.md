---
description: A reference adds model-side interpretation only when the model must resolve it; upstream literalization is worthwhile when binding, token, authority, and regeneration costs favor it
type: kb/types/note.md
traits: [title-as-claim]
tags: [computational-model]
---

# Model-resolved indirection adds interpretation work to LLM execution

The cost of an instruction reference depends on who resolves it. A shell, harness, or tool can expand `$PROJECT_ROOT` after the model emits it; the model need not reconstruct the path. But if the model receives `{{project_root}}` and must turn it into a literal path, resolving the binding becomes part of model execution. This is **model-resolved indirection**: the model must use information elsewhere in its context to produce or apply the referenced value.

This differs from indirection in conventional code. A configuration read may perform I/O, and a lookup may miss a cache, but the programming runtime still provides a formal resolution procedure. Natural-language instructions have no equivalent procedure unless the surrounding harness supplies one.

When the model resolves a reference, the consuming context bears three structural costs:

- The model-facing context must contain the binding—or enough information to infer it—as well as each use of the reference.
- The model must identify the reference and produce an output consistent with the binding.
- The reference creates a failure surface: output may preserve the unresolved placeholder or contain a malformed or incorrect value.

These are structural costs, not claims about their magnitude. A short alias may still use fewer tokens than repeating a long literal. Deterministic executor-side expansion may preserve one authoritative configuration without imposing model-side substitution. The relevant comparison is between the complete delivered forms, not between a “literal” and a “variable” in isolation.

The same boundary appears beyond path variables. “Use the appropriate search command” leaves tool selection to the model; a literal command moves that choice upstream. A conditional branch leaves classification to the model; an assembler that knows the condition can omit branches that no longer apply. In both cases, semantic work moves upstream. It does not disappear.

## Choose the resolver and binding time

Resolve a reference before the model consumes the instruction when:

- the assembler knows the authoritative value;
- the value is stable for the generated artifact’s declared validity window;
- the model must use the value itself, rather than merely pass an alias to a deterministic resolver; and
- the literal form’s token and maintenance costs, including regeneration, do not exceed the binding and failure costs that upstream resolution removes.

Keep deterministic expansion outside the model when the execution environment is authoritative, the literal would be bulky, or a single live configuration is the best way to prevent drift. Keep a parameter in model-facing text when the model must choose or reason over its runtime value. Variation between invocations does not, by itself, require a model-facing placeholder: an assembler can inject the current file, URL, or query into each prompt before consumption.

Generated instructions create a derived-copy obligation. Their producer needs a validity rule and a regeneration or drift check. Upstream resolution trades repeated model-side interpretation for generation and maintenance work; it does not pay every flexibility cost once and forever.

## Example: knowledge-base skill portability

This boundary became concrete while making knowledge-base (KB) skills—reusable instruction units—portable across installations. A generated skill can replace installation-specific path placeholders before the model sees its instructions. Commonplace’s [instruction-generation flow](../reference/instruction-generation.md) demonstrates this: it resolves project values into generated artifacts while retaining runtime inputs as parameters. The result is [constraining](./definitions/constraining.md): the generated artifact admits fewer valid interpretations, but its copies must remain synchronized with their source.

---

Relevant Notes:

- [Frontloading spares execution context](./frontloading-spares-execution-context.md) — mechanism: pre-computation moves work out of the consuming call
- [Frontloading is partial evaluation, not divide-and-conquer](./frontloading-is-partial-evaluation-not-divide-and-conquer.md) — mechanism: binding known inputs specializes an instruction while leaving runtime inputs dynamic
- [Semantic work can be relocated but not eliminated](./semantic-work-can-be-relocated-but-not-eliminated.md) — mechanism: upstream resolution moves binding work rather than erasing it
- [An author should fix what the executor can't determine, not what it will](./fix-what-the-executor-cant-determine-not-what-it-will.md) — contrasts: live execution authority can make runtime resolution safer than an authored literal
- [Instruction specificity should match loading frequency](./instruction-specificity-should-match-loading-frequency.md) — grounds: repeated loading determines how often model-side work recurs
