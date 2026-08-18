---
description: "Seeing that two items share a structure is the expensive step in connecting knowledge; articulating a seen connection is cheap, and naming a recognized structure amortizes later recognition."
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, discovery]
---

# Recognition, not linking, is the hard problem in knowledge systems

Connecting two knowledge items takes two steps with very different costs. **Recognition** is seeing that the items share a structure at some level of abstraction. **Articulation** is stating the connection once it is seen — writing the link with its reason. Articulation is comparatively cheap: once someone sees that two proofs make the same move, saying so is straightforward. Recognition is where the cost concentrates, so it is where a knowledge system's effort and tooling should go.

## Recognition cost grades with what must be recognized

| What is shared | Typical recognition cost |
|---|---|
| **Shared feature** — an observable similarity | Cheap. Embedding search, keywords, and filenames surface candidates. |
| **Shared structure** — a reusable relation, pattern, or proof shape | Expensive. Requires understanding what each item is about, then comparing them semantically. |
| **Generative model** — one process capable of producing the cases | Most expensive. Requires proposing the dimension along which the commonality becomes visible, then testing whether it explains more than the cases that suggested it. |

The grading is a heuristic, not a law. The forms are not strictly nested: a generative model can unite cases that look different on the surface. And the costs are observer-relative — they depend on the reader's prior vocabulary, tools, and access to the cases, since [information value is observer-relative](./information-value-is-observer-relative.md). Recognition also requires co-presence: a structure shared by items that never appear in the same context cannot be seen, which is why [short composable notes maximize combinatorial discovery](./short-composable-notes-maximize-combinatorial-discovery.md).

## Naming amortizes recognition

The mathematical tradition supplies the main cost reducer: name the recognized structure. A mathematician who notices that two proofs make the same move can state that move as a lemma — a reusable intermediate result. The earlier proofs become applications of the lemma, and later proofs can recognize the move by matching against the name instead of re-deriving the similarity. One expensive act of recognition becomes many cheap lookups.

The amortization has conditions. The name must carry usable membership criteria: a name without a test for what counts as an instance does not make boundary judgments cheaper. And the structure must recur: naming a structure that never reappears adds vocabulary without saving recognition.

## The mechanism-note heuristic

For a knowledge base this yields a heuristic. When several artifacts look similar, consider writing a note that names their shared mechanism rather than only linking them pairwise. Pairwise links record each recognition separately; a mechanism note converts future recognition into matching against a stated structure. The new note earns its place when its expected reuse, and its power to discriminate instances from lookalikes, exceed the context cost of one more abstraction.

Naming a shared mechanism is itself a conjecture. It enters the [discovery lifecycle](./definitions/discovery-lifecycle.md) at the conjecture phase and earns acceptance as later instances confirm, refine, or refute the proposed structure.

## Scope

The claim compares recognition with articulation, not with every linking activity: a link still needs a reader-relevant reason, and judging that reason is real work. It covers similarity-based connections; contrastive, causal, and temporal links are judgments of a different kind. And "hard" locates where cost concentrates, not a fixed ordering — with strong prior vocabulary, deep recognition can be cheap, and without co-presence, even surface recognition fails.

---

Relevant Notes:

- [information value is observer-relative](./information-value-is-observer-relative.md) — grounds: recognition cost depends on the representations, prior knowledge, and tools available to the reader
- [minimum viable vocabulary is the naming set that most reduces extraction cost](./minimum-viable-vocabulary-is-the-naming-set-that-most-reduces.md) — extends: treats which structures to name as an optimization over a bounded observer's extraction cost
- [generality bought to avoid counterexamples is paid for in precision](./generality-bought-to-avoid-counterexamples-is-paid-for-in.md) — contrasts: naming a recognized structure raises universality and precision together; defensive abstraction has the same surface and buys neither

Operationalized into:

- [/connect skill](../instructions/cp-skill-connect/SKILL.md) — the articulation test operationalizes the cheap half: a proposed link must state the specific relation that was recognized
