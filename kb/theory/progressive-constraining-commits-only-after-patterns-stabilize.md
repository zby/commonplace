---
description: Constraining via LLM code generation freezes one unchecked reading of the spec in one shot, but progressive constraining observes behavior across many runs and commits only the interpretations that consistently emerge
type: types/note.md
traits: [title-as-claim]
tags: [learning-theory, computational-model, constraining]
---

# Progressive constraining commits only after patterns stabilize

LLMs can generate code from a spec — spec in, code out. But this is not compilation: the LLM resolves the semantic ambiguity of the spec and produces one implementation from the space the spec admits. The output is a candidate [program refinement](./definitions/program-refinement.md) of the spec, inside the permitted set or outside it, and nothing in the output says which. See [prompting changes failure diagnosis with the semantic reference](./prompting-changes-failure-diagnosis-with-the-semantic-reference.md) for why spec-to-program is many-to-one rather than semantics-preserving.

This property gives LLM code generation a specific character: it is **one-shot constraining** — freeze a single unchecked candidate into code. Whatever interpretation the LLM landed on this run becomes law, and the other valid interpretations are discarded silently. Regenerating the same spec later may produce a different law.

The alternative is **progressive constraining**: don't freeze on one run. Observe the LLM's behavior across many runs, identify which interpretations it consistently favours, and extract *those* stable patterns into deterministic code — keeping the LLM for genuinely ambiguous cases.

Example: a file-renaming agent initially uses LLM judgment for everything. You notice it always lowercases and replaces spaces with underscores — so you extract `sanitize_filename()` to code. The agent still handles ambiguous cases ("is '2024-03' a date or a version?"), but the common path is now deterministic.

The two modes trade off differently:

- **One-shot** commits immediately. You get a deterministic artifact now, but the commitment is arbitrary — whatever the LLM sampled on that run. If the spec was wide, the chance that the frozen candidate matches what you actually wanted is low.
- **Progressive** defers commitment. You only codify what's empirically stable across runs, so the resulting code reflects behavior the system actually exhibited — not a single sample of what the spec allows. You pay for this with observation time and the cost of running the underspecified version longer.

Progressive is [codification](./definitions/codification.md) taken seriously: commit to symbolic media where a pattern has proven itself, not where the spec happens to admit it. One-shot is faster when the spec is narrow enough that one reading is as good as another — or when you genuinely don't care which interpretation wins. Progressive pays off when the interpretation space is wide and only part of it matters in practice.

Either way, **version both spec and artifact**. Regeneration is another candidate — potentially a different resolution of the same ambiguity — not a deterministic rebuild from source.

---

Relevant Notes:

- [prompting changes failure diagnosis with the semantic reference](./prompting-changes-failure-diagnosis-with-the-semantic-reference.md) — grounds: the English account, under which an instruction permits several behaviors and the executor produces one
- [program refinement](./definitions/program-refinement.md) — grounds: a generated implementation is a candidate refinement; observed runs are the check that makes a commitment a refinement step
- [codification](./definitions/codification.md) — related: progressive constraining is codification applied only to patterns that stabilize across runs
- [constraining](./definitions/constraining.md) — related: both modes are constraining moves; they differ in when commitment happens
- [Selecting an LLM output fixes a result, not its interpretation](./selecting-an-llm-output-fixes-a-result-not-its-interpretation.md) — contrasts: selecting one generated artifact immediately fixes result identity, while progressive constraining waits for repeated evidence before narrowing semantics
