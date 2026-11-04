---
description: "Progressive extraction uses repeated behavior to identify stable candidates, then checks the extracted rule against the applicable requirement before committing it."
type: types/note.md
traits: [title-as-claim]
tags: [learning-theory, computational-model, constraining]
---

# Progressive constraining commits only after patterns stabilize

LLMs can generate code from a spec — spec in, code out. Generation alone does not establish the guarantees expected of a conformant compilation. The LLM produces one candidate implementation and may make choices the spec leaves unsettled. The output is a candidate [program refinement](./definitions/program-refinement.md), not evidence of conformance. Judging it requires an applicable interpretation of the spec; disputed permission boundaries must be settled or reported. The [two accounts of prompting](./prompting-changes-failure-diagnosis-with-the-semantic-reference.md) distinguish these questions.

Adopting the generated code immediately is **one-shot constraining**: the operation is committed to the candidate's choices before they have been checked. Producing code alone does not make it authoritative. Once adopted, the implementation can exclude alternatives the English requirement allowed, or implement a reading whose permissibility remains disputed.

The alternative is **progressive constraining**: don't freeze on one run. Observe the LLM's behavior across many runs, identify which interpretations it consistently favours, and check those stable patterns against the requirement before extracting them into deterministic code. Leave unresolved cases with an explicit route for judgment or clarification.

Constructed example: a file-renaming agent consistently lowercases names and replaces spaces with underscores. That stability identifies a candidate `sanitize_filename()` rule; it does not establish permission to lowercase. If the contract requires preserving case, the stable behavior is a violation. If it only asks for “clean names,” whether case changes are allowed may need clarification. Once the policy is settled, check the extracted function against it, including collision cases such as `Report` and `report`. A case such as “is '2024-03' a date or a version?” can still require judgment.

The two modes trade off differently:

- **One-shot** commits immediately. The artifact fixes the generated choices without establishing that they match the requirement. A wide or disputed permission boundary increases what must be checked; it does not by itself give a probability of failure.
- **Progressive** defers commitment. You only codify what's empirically stable across runs, so the resulting code reflects behavior the system actually exhibited — not a single generated candidate. Stability is not conformance: a model can consistently violate an instruction, so the extracted rule is still checked against the applicable requirement before it is committed. You pay for this with observation time, the check, and the cost of running the underspecified version longer.

Progressive extraction uses [codification](./definitions/codification.md) to retain patterns supported by both behavioral evidence and checks against the requirement; stability alone supplies only the first. One-shot is faster when the spec is narrow enough that one reading is as good as another — or when you genuinely don't care which interpretation wins. Progressive pays off when the interpretation space is wide and only part of it matters in practice.

Either way, **version both spec and artifact**. Regeneration is another candidate — potentially a different resolution of the same ambiguity. Even repeatable generation does not establish conformance to the English requirement.

---

Relevant Notes:

- [prompting changes failure diagnosis with the semantic reference](./prompting-changes-failure-diagnosis-with-the-semantic-reference.md) — grounds: the English account, under which an instruction permits several behaviors and the executor produces one
- [program refinement](./definitions/program-refinement.md) — grounds: a generated implementation is a candidate refinement; observed runs show a pattern is stable, and the check against the applicable requirement is what makes the commitment a refinement step
- [codification](./definitions/codification.md) — related: progressive constraining is codification applied only to patterns that stabilize across runs
- [constraining](./definitions/constraining.md) — related: both modes are constraining moves; they differ in when commitment happens
- [Selecting an LLM output fixes a result, not its interpretation](./selecting-an-llm-output-fixes-a-result-not-its-interpretation.md) — contrasts: selecting one generated artifact immediately fixes result identity, while progressive constraining waits for repeated evidence before narrowing semantics
