warning

One term is used without sufficient inline definition.

---

**"lexically scoped frame"** (line 41): "The prompt defines what's visible in the sub-agent's [lexically scoped frame], and the sub-agent inherits nothing beyond what the caller explicitly passed."

"Lexically scoped" is a programming language concept meaning "visibility determined by the syntactic structure, not runtime state." Its application to LLM context — that the sub-agent's prompt is a static, caller-defined boundary with no implicit inheritance — is non-obvious without that background. The following clause ("the sub-agent inherits nothing beyond what the caller explicitly passed") explains the *effect* but not the term. A reader unfamiliar with lexical scoping in PLs will find "lexically scoped frame" opaque while understanding the clause that follows.

The linked note is not in `kb/notes/definitions/`, so the link-as-definition exception does not apply.

Recommended fix: gloss the term inline, e.g., "the sub-agent's lexically scoped frame (a static context boundary: only what the caller explicitly wrote is visible — no implicit inheritance from conversation history or the caller's environment)." Or replace with the plain-language version already present in the sentence: "The prompt defines what's visible to the sub-agent; it inherits nothing beyond what the caller explicitly passed."

---

All other terms are either standard technical vocabulary (LLM, context window, prompt, API, schema, CI pipeline) or are defined inline:

- "Deterministic base" / "prompt layer" — introduced as a named pair with sufficient context ("files, schemas, scripts, APIs" and "natural language prompt that tells the agent what to do").
- "Enforcement gradient" — defined inline by its expansion ("instructions → skills → hooks → scripts").
- "Typed callables" — defined inline ("declared signatures, validated inputs, composable skills").
- "Distillation" — defined inline and links to the definitions/ entry, triggering the gate exception.
- "Homoiconic medium" — defined inline ("instructions and content share the same representation (natural language tokens)").
