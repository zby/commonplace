Key claims by section:

- **Intro**: Four always-loaded mechanisms; scoped to user-facing surfaces.
- **System prompt files**: Five content types. Tension between practitioner practice and theory.
- **Capability descriptions**: Always listed, bodies load on demand.
- **Memory**: Accumulates across sessions. Write-policy is the central axis (three models).
- **Configuration injection**: Static per installation, resolved before agent sees them.
- **Design principles**: Shared budget, cadence matching, ambient/on-demand distinction, volatile state gap.

---

**Pairwise contradiction: none found**

- "The same structural roles appear across platforms" (intro) vs. platform-specific names in each section — consistent; the claim is about structural roles, not names.
- "Memory... grows and changes through use" vs. "configuration... is static per installation" — different mechanisms, correctly distinguished.
- "Capability descriptions are always *listed* but their bodies load on demand" — this is the key structural difference from system prompt files, and it's maintained consistently.
- "Volatile project state is a gap" vs. "In practice, project state ends up in system prompt files anyway" — the note honestly acknowledges the gap exists alongside the pragmatic workaround.

**Definition drift: none observed**

"Always-loaded," "ambient," "on-demand," "surface" — all used consistently. "Surface" consistently means a configurable injection mechanism, not the content itself.

**INFO — write-policy models could generate contradictions**

The three memory write-policy models (human-governed agent writes, fully agent-managed, external pipeline) are presented as alternatives. But the note says "users can also write memory entries directly, making memory indistinguishable from system prompt content." This complicates the clean separation between system prompts (authored) and memory (accumulated). The note acknowledges this but the implication — that the four mechanisms aren't fully separable in practice — is left as an observation rather than resolved.

One INFO on mechanism separability. No WARN, no contradiction, no drift.
