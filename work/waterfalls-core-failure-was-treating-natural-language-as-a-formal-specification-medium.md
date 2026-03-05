---
description: "Argues waterfall failed not because requirements change, but because natural language lacks the precise semantics needed for unambiguous phase-to-phase handoffs"
type: note
traits: []
areas: []
status: seedling
---

# Waterfall's core failure was treating natural language as a formal specification medium

The waterfall model assumes linear phase handoffs: requirements → design → implementation → testing. Each phase produces documents that serve as complete inputs to the next. This only works if those documents are unambiguous — if specification A produces exactly one valid interpretation for every reader.

Natural language doesn't have this property. It lacks precise semantics. The same requirements document yields different mental models in different readers, and those divergences compound across phases. By the time ambiguous requirements pass through ambiguous design documents into code, the gap between intent and implementation can be enormous.

## The wrong diagnosis led to the wrong cure

The waterfall community diagnosed specification failures as *insufficient detail* and responded by demanding longer, more elaborate documents. But more natural language means more ambiguity surface area, not less. The approach was self-defeating: the cure amplified the disease.

This is distinct from the conventional critique that "requirements change." Even with perfectly stable requirements, the ambiguity problem remains. A frozen spec that two engineers interpret differently still produces the wrong system.

## Responses that took the semantics problem seriously

Several movements can be read as responses to the imprecise-semantics problem, each with different trade-offs:

- **Formal methods** — the honest response. If natural language lacks precise semantics, use mathematical notation. But the cognitive overhead was too high for most projects, so adoption stayed niche.
- **Structured analysis (1980s)** — a partial formalization. Data flow diagrams, entity-relationship models, and state transition diagrams added rigor without full mathematical formalism. But natural language still glued everything together.
- **Agile/iterative development** — a pragmatic dodge. Instead of fixing the specification medium, shorten the feedback loop until ambiguity can't compound far. Working software becomes the specification because it's the one artifact with exact semantics.
- **TDD** — specification-as-code. Tests are requirements written in a language with deterministic evaluation. The specification *is* executable.

## The LLM inversion

LLMs introduce a curious inversion. Classical software engineering struggled because humans couldn't write precise specs in natural language. Now we have systems that *consume* imprecise natural language fluently — but whose outputs are themselves non-deterministic. The ambiguity has moved from the input channel to the processing engine.

This suggests that the specification problem isn't solved, just relocated. Instead of "how do we write unambiguous requirements?" the question becomes "how do we get deterministic behavior from a system that interprets ambiguous inputs?"

## Open Questions

- Did any waterfall-era thinkers explicitly identify the natural language semantics problem, or was it always framed as "requirements change"?
- Is there a useful formal framework for quantifying specification ambiguity?
- How does the LLM inversion interact with the agile "working software as spec" pattern — does it break it, since LLM-generated code is itself a product of ambiguous interpretation?
