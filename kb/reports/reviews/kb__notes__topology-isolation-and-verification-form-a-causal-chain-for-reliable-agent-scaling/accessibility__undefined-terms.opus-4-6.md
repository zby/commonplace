**managerial capacity** — used in the Open Questions section: "Does 'managerial capacity' — a parent agent's ability to manage children, which limits branching factor — belong in the KB's decomposition heuristics." The term is quoted and immediately explained in a parenthetical ("a parent agent's ability to manage children"), so it is adequately glossed on first and only use.

**decorrelated checks** — "The error correction framework requires decorrelated checks — the verifier's error modes must differ from the generator's." The dash-clause provides a working definition. Pass.

**sequential depth from linear to logarithmic** — used without explanation of what "sequential depth" means in this context or why hierarchical structure reduces it. The sentence "Tu argues that hierarchical structure bypasses this by reducing sequential depth from linear to logarithmic while distributing total work across parallel branches" is not unpacked for a reader unfamiliar with the computational complexity argument.

**F1** — "F1 collapses from 1.0 to ≈0.2 at depth 100" uses F1 without defining it. F1 score is a standard ML evaluation metric, so this is borderline standard vocabulary, but in a KB focused on agent systems rather than ML benchmarks, "F1 collapses" could confuse readers who don't know F1 score is bounded 0–1.

**content effects** — "The content effects evidence already suggests this: content bias is shared across model families" — this refers to a specific research phenomenon (how content of a reasoning problem biases LLM judgment, separate from logical validity). It is used as if the reader knows what "content effects" means in this technical sense. The linked source is mentioned but the term itself has no inline gloss.

The most actionable finding: "sequential depth from linear to logarithmic" is used as a technical claim without the underlying model being explained — readers without a background in the complexity argument cannot follow why hierarchy produces a logarithmic reduction.
