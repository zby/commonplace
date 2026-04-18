---
description: Named fix strategies for review warnings. A living codebook — agents classify each fix by strategy name, enabling audit and taxonomy evolution. Strategies that recur from "new-pattern" reports get promoted here.
type: instruction
---

# Fix Strategy Taxonomy

Each entry names a recurring pattern of review warning + appropriate fix. Agents cite strategy names in fix reports. When a fix doesn't fit any listed strategy, the agent reports it as `new-pattern` — recurring new patterns get added here.

The strategies are organized by the review check they most commonly address, but a strategy can apply across checks.

---

## Source residue

### stale-paths

**Pattern:** A reference to a path, field, command, or mechanism that no longer exists in the repo (e.g., `docs/sources/` → `kb/sources/`, `areas:` → `tags:`).

**Typical fix:** Update to the current equivalent, or remove if no equivalent exists and the reference is only illustrative. Verify staleness before acting.

### unframed-domain-examples

**Pattern:** Examples from a narrow domain (KB operations, software engineering, one specific system) used without framing in a note claiming broader scope.

**Typical fix:** Add framing ("In [domain], for instance...") rather than removing or abstracting the examples. Optionally add one cross-domain example alongside.

### single-source-vocabulary

**Pattern:** Vocabulary or structural framing from one specific source dominates a section that claims generality.

**Typical fix:** Attribute explicitly ("In [Source]'s framing...") or replace source-specific terms with domain-neutral equivalents where meaning is preserved.

### temporal-residue

**Pattern:** Present-tense references to a system state that no longer holds ("we already run," "the current architecture uses").

**Typical fix:** Shift to past tense if the historical state matters for the argument, or restate as a general principle if it doesn't.

---

## Confidence miscalibration

### hedge-own-framework

**Pattern:** The note's own taxonomy, decomposition, or causal model is presented as established fact rather than proposed analysis.

**Typical fix:** Add hedging language: "we organize," "a plausible decomposition," "in our framing." Light touch — one or two words per instance, not wholesale caveat insertion.

### hedge-strength-mismatch

**Pattern:** A source says something weaker than the note's claim, but the note presents its claim as if supported by the source.

**Typical fix:** Either weaken the claim to match the source, or make explicit that the note is extending beyond what the source establishes: "The source describes X; we extend this to Y."

---

## Grounding

### qualifier-dropped

**Pattern:** A claim from a source is cited without a qualifier that the source includes (e.g., "40% reduction" without "for voice-only tasks").

**Typical fix:** Restore the qualifier.

### scope-narrowed

**Pattern:** A source's claim is broader or different than how the note uses it — the note narrows "environment" to "context," or "several factors" to "one factor."

**Typical fix:** Widen the attribution to match the source, then make the narrowing explicit as the note's own move: "The source identifies X broadly; this note focuses on the Y component."

### unsourced-addition

**Pattern:** The note adds a characterization not present in the source (e.g., "with outsized impact on reliability" when the source only reports token savings).

**Typical fix:** Remove the unsourced characterization, or flag it as the note's own inference.

---

## Completeness

### boundary-case-acknowledged

**Pattern:** The review identifies a boundary case or omitted category that weakens a claim of exhaustiveness.

**Typical fix:** Add a brief acknowledgment — "This taxonomy does not cover X, which sits between Y and Z" or "X is a boundary case that straddles these categories." Do NOT expand the framework to include the boundary case unless the note's argument requires it.

---

*New strategies are added when `new-pattern` reports from fix sweeps show recurring patterns.*
