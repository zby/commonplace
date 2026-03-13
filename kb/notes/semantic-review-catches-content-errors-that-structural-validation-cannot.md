---
description: Four specific semantic checks (enumeration completeness, grounding alignment, boundary-case coverage, internal consistency) that require LLM adversarial reading — structural validation catches form errors but misses content errors like incomplete enumerations that contradict their own grounding definitions
type: note
tags: [kb-maintenance]
status: seedling
---

# Semantic review catches content errors that structural validation cannot

The validate skill checks structural properties: valid frontmatter, link health, required sections, description quality. These are Level A checks in the [text testing pyramid](./text-testing-framework.md) — deterministic, cheap, reliable. But they miss an entire class of errors: content that is structurally perfect but semantically wrong.

## The motivating case

The synthesis note on learning operations claimed "three learning operations (constraining, distillation, discovery)" as the complete set. It had valid frontmatter, healthy links, proper sections, a discriminating description. It passed every structural check. But the enumeration was incomplete — it omitted accumulation (simply adding knowledge to the store), the most basic learning operation, which doesn't fit any of the three named operations. The note's own grounding definition (Simon's "any capacity change is learning") implied a fourth operation that the enumeration silently excluded.

This isn't a structural error. It's a content error — a claimed enumeration that doesn't cover the space defined by its own premises.

## Four semantic checks structural validation cannot perform

**Enumeration completeness** — when a note claims an exhaustive set ("three operations," "two mechanisms," "the complete set"), test whether the enumeration covers the space implied by the grounding definition. Method: identify the definition the enumeration claims to derive from, generate boundary cases from that definition, check whether each maps to one of the enumerated items. If a boundary case falls outside all items, the enumeration has a gap.

**Grounding alignment** — does the note's conclusion actually follow from the evidence and definitions it cites? A note might cite Simon's definition of learning but draw conclusions that don't follow from it, or cite a source and mischaracterise its claims. Method: load the cited sources, extract the claims attributed to them, check whether the attribution is accurate and the inference valid.

**Boundary-case coverage** — does the framework handle the simplest and most extreme cases? The "three operations" framework failed the simplest case: an agent recording a user preference. That's learning (by Simon's definition), but it's not constraining, distillation, or discovery. Method: generate the simplest possible instance of the concept the note discusses, and the most extreme one, then check whether the framework accounts for both.

**Internal consistency** — does the note contradict itself? A note might claim X in one section and not-X in another, or define a term one way and use it differently. Method: extract the key claims from each section, check for pairwise contradiction. This is distinct from cross-note consistency (which checks against the broader KB) — it's within a single note.

## Where these sit in the text testing pyramid

These are Level B checks — they require LLM judgment but can be structured with rubrics. They're more expensive than structural validation (Level A) but cheaper than full cross-corpus consistency checking (Level C). They operate on a single note plus its cited sources, not the entire KB.

The [error correction framework](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) applies: each semantic check is a weak oracle with TPR > FPR — it catches real problems more often than it false-alarms. The four checks are decorrelated (they probe different failure modes), so combining them amplifies signal. A note that passes all four has been tested on four independent axes.

## The review skill as the implementation target

Structural validation belongs in `/validate` — it's schema checking. Semantic review belongs in a separate `/review` skill — it's adversarial reading. The separation matters because:

- **Different cost model** — structural checks are cheap and should run on every save; semantic review is expensive and should run before commit or on demand
- **Different failure semantics** — structural failures are always real (a broken link is broken); semantic findings are probabilistic (an LLM might flag a valid enumeration as incomplete)
- **Different scope** — validation checks form; review checks content

The review skill would load the note, identify its key claims, run the four semantic checks, and report findings with the same PASS/WARN/FAIL format as validate. But findings are WARN by default (probabilistic), not FAIL (deterministic).

---

Relevant Notes:

- [text-testing-framework](./text-testing-framework.md) — grounds: the three-level testing pyramid (deterministic / LLM rubric / corpus) that these semantic checks map to as Level B
- [error-correction-works-above-chance-oracles-with-decorrelated-checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — grounds: the four semantic checks are decorrelated weak oracles; combining them amplifies discriminative power
- [quality-signals-for-kb-evaluation](./quality-signals-for-kb-evaluation.md) — extends: semantic review is the single-note complement to the corpus-level signals catalogued there
- [document-types-should-be-verifiable](./document-types-should-be-verifiable.md) — parallel: structural validation assumes the type system is trustworthy; semantic review checks whether the content lives up to its structural claims
- [a good agentic KB maximizes contextual competence through discoverable, composable, trustworthy knowledge](./a-good-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trustworthy-knowledge.md) — motivates: the note whose "three operations" incompleteness exposed this gap
