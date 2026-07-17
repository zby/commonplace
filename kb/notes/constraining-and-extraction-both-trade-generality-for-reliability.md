---
description: Constraining narrows interpretation and extraction produces focused use-shaped artifacts; both can trade generality for reliability, speed, or cost when task fit is good
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, constraining, distillation]
---

# Constraining and extraction can trade generality for reliability, speed, or cost

[Capacity can change along generality, reliability, speed, and cost dimensions](./learning-is-not-only-about-generality.md). [Constraining](./definitions/constraining.md) narrows the space of valid interpretations. **Extraction** produces a focused, use-shaped artifact from larger material. With good task fit, either operation can trade some generality for gains in one or more of the other dimensions, but through different mechanisms.

## How constraining can make the trade

[Codification](./definitions/codification.md) — the far end of the constraining spectrum — makes this trade especially visible when a deterministic implementation fully captures the operation. Replacing an LLM validation check with a Python script doesn't change *what* gets checked — within the script's specified contract, it can change how reliably the check runs, how fast it runs, and its marginal cost once written. What you give up is generality: the script handles exactly what it handles, nothing more.

Improvements in reliability, speed, or cost are not exclusive to codification. Constraining short of codification (storing outputs, writing conventions) can also improve one or more of them. Across the constraining spectrum, successful constraints spend semantic latitude for narrower behavior; the size and direction of each effect depend on task fit and implementation, not on a universal ranking by medium.

## The trade-off in action

As an illustration rather than a benchmark, compare assigning multiplication to a general-purpose LLM with using a dedicated calculator. Within a specified numeric representation and supported input range, the calculator can execute the operation deterministically and locally; relative to a particular LLM setup, those properties can improve reliability, latency, or marginal execution cost. The trade is a narrower task repertoire: the calculator does not also translate, summarise, or write prose. Whether the calculator is less general within multiplication itself depends on the two tools' supported input contracts.

## How extraction can make the trade

Extraction reshapes a larger body of reasoning into a focused artifact for a specific use case, context budget, or agent. When the selected material and arrangement fit the later task, the extracted artifact is narrower than the source but leaves less material to load, less selection work, and fewer opportunities to choose the wrong source fragment.

For example, a skill worked out from many methodology notes can fit in a single context window. Loading less material can reduce processing time and context cost. Preselecting the relevant premises and ordering the steps can make execution more reliable because the agent no longer has to reconstruct the procedure from a larger note cluster each time. The methodology notes remain for edge cases the skill cannot cover — the fast-path-with-fallback arrangement of [theory and methodology form a two-layer execution system](./theory-and-methodology-form-a-two-layer-execution-system.md).

These gains depend on task fit. An extraction that omits a needed premise, fixes an unsuitable order, or is reused outside its intended task can reduce reliability even while reducing context. Production, maintenance, and fallback work can also outweigh the savings, so extraction does not guarantee faster or cheaper execution.

## The mechanisms differ in operation

Constraining narrows how an artifact may be interpreted, sometimes by crossing into a symbolic medium. Extraction instead produces a new, focused artifact from a larger source and usually remains in natural language. Neither operation has a fixed yield ranking: the effects on reliability, speed, and cost depend on task fit and implementation.

Both directions are [capacity change](./learning-is-not-only-about-generality.md). The reverse — relaxing a constrained component, or loading the full source instead of the extracted artifact — can trade gains in reliability, speed, or cost back for generality.

---

Relevant Notes:

- [Fixed artifacts split into exact specs and proxy theories](./fixed-artifacts-split-into-exact-specs-and-proxy-theories.md) — grounds: distinguishes cases where narrowing can harden confidently from cases where relaxing may be needed
