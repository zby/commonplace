---
gate: prose/proportion-mismatch
verdict: warn
---

The core claim is: stateless agents need automatic context injection. The load-bearing argument is that statelessness creates the need (intro) and that injection fits into the loading hierarchy (Reasoning).

The "definition type" subsection (~1 paragraph + 4 bullets) is the most developed evidence subsection, but it argues for a specific implementation artifact (a `type: definition` enum value) rather than supporting the core claim. The core claim — that injection is needed — is already established by the preceding "Definitions as the first case" subsection. The type proposal is secondary: it's about *how* the engine identifies targets, which the note elsewhere says is "an open design question."

This subsection could be its own note (e.g., "Definitions need a machine-readable type for auto-injection to work") or condensed to a paragraph within this note. As written, it gives a secondary implementation concern as much space as the architectural argument in Reasoning.

The mismatch is mild — Reasoning and Caveats are both well-developed and carry the core argument. But the definition-type section draws attention away from the general principle toward a specific design choice.
