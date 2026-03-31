## prose/redundant-restatement

**Result: WARN**

Checked the opening of each section:

- **Spec-to-Program Projection**: "A natural-language spec admits multiple valid programs. The LLM picks one:" — advances with a new model, not a restatement. PASS.

- **Narrowing the Interpretation Space**: "The usual tools: system prompts, few-shot examples..." — jumps straight to enumeration. PASS.

- **Boundaries**: "Agentic systems interleave LLM components and code." — one-sentence setup. PASS.

- **Constraining and Relaxing**: "Components exist on a spectrum from underspecified semantics (natural language, LLM-interpreted) to precise semantics (formal language, deterministic code). Logic can move in both directions." — The Boundaries section ended two sentences earlier with: "But boundaries aren't fixed. As systems evolve, logic moves across them." These say the same thing: logic moves across the underspecified/precise divide. The opening of Constraining and Relaxing restates this with slightly more precision (adding "spectrum" and naming the endpoints), but if deleted, the section works fine starting from "**Constraining**: Replace an LLM component with a deterministic one." **Severity: INFO** — the restatement adds the spectrum framing (setup) where the original was a closing pivot (transition), so the two serve different structural roles. Mild duplication, not same-role redundancy.

- **Testing and Debugging**: "The two phenomena create different challenges for testing and debugging." — one-sentence topic sentence connecting back to the framework. PASS.

- **Design Implications**: "Treating agentic systems as interpreters of underspecified instructions suggests:" — one-sentence lead-in to a list. PASS.

One minor instance at the Constraining and Relaxing opening. Low severity.
