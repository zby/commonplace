# Label audit: reader-need justifications

Each label in the proposed vocabularies is retrofitted against [`links-as-possibility.md`](./links-as-possibility.md). Each row names the reader-need the label serves. Labels that can't name a specific need are flagged.

"Register" below follows the KB definition: one of three content modes — theoretical, descriptive, prescriptive — determining quality goal, title conventions, and linking rules. See [`register`](../../notes/definitions/register.md).

Reader class assumed: **agent reader** (primary), with human fallback. The reader-need statements describe what an agent-with-a-task would want the linked content for.

## Intra-theoretical (seven labels, `notes-COLLECTION.md`)

| label | reader-need | verdict |
|---|---|---|
| `extends` | wants to see the argument developed further, or see where this claim leads | keep |
| `grounds` | wants to verify the premise / check the evidential base | keep |
| `enables` | wants to check the operational prerequisite — would the claim collapse without it? | keep |
| `exemplifies` | (source is instance) wants the general claim this instance falls under | keep — asymmetry runs instance→general |
| `mechanism` | wants to understand how the claim operates | keep |
| `contradicts` | wants to resolve a disagreement / see which claim survives | keep |
| `contrasts` | wants to see the neighbouring-shape distinction — what differs and why | keep |

All seven pass. They all name agent-readable epistemic states.

## Intra-descriptive (`reference-COLLECTION.md`, `agent-memory-systems-COLLECTION.md`)

| label | reader-need | verdict |
|---|---|---|
| `part-of` / `contains` | wants the containing/contained system context | keep — names a relation but the reader-need ("situate this in the larger system") follows tightly |
| `implements` / `implemented-by` | wants the concrete realization (or the abstract contract) | keep |
| `describes` | wants the object this doc describes, from an adjacent vantage | **flag**: weak — collapses to `part-of` or `see-also` in most cases |
| `cross-reference` | wants adjacent information | **drop**: too vague; no specific reader-need |
| `supersedes` / `superseded-by` | wants the current / prior version | keep (primarily ADR chains) |
| `see-also` | wants *something* but author can't name what | keep as escape hatch; use sparingly |
| `compares-with` (agent-memory-systems) | reading one review, wants a design-axis comparison with another system | keep — comparative work is the collection's core |

**Recommendation:** drop `cross-reference`; fold `describes` into `part-of` or `see-also`; in `agent-memory-systems-COLLECTION.md`, keep `compares-with` as the collection extension because the reader-need (parallel design-axis analysis) is load-bearing and distinct from theoretical `contrasts`.

## Intra-prescriptive (`instructions-COLLECTION.md`)

| label | reader-need | verdict |
|---|---|---|
| `composition` | wants the next step in a chain | keep |
| `precondition` | needs to confirm something is true/done before proceeding | keep |
| `invokes` | needs to execute a subroutine | keep |
| `applies-when` | branch condition tells them to go elsewhere | keep |
| `see-also` | weak | keep sparingly |

All survive. Prescriptive vocabulary is the most naturally action-oriented — every label already names what the agent wants to do.

## Cross-register (`link-vocabulary.md`)

| label | reader-need | verdict |
|---|---|---|
| `rationale` | reading descriptive, wants the theoretical claim the design rests on | keep |
| `justification` | reading prescriptive, wants the theoretical claim the rule rests on | **merge candidate** — same reader-need class as `rationale` ("why does this exist?"); source register is recoverable from the graph |
| `evidence` | reading theoretical, wants corroborating observation | keep |
| `derived-from` | reading theoretical, wants the specific case the claim was abstracted from | keep — distinct from `evidence` (provenance vs. corroboration) |
| `procedure` | reading descriptive, wants the how-to that operates on this | keep |
| `operates-on` | reading prescriptive, wants to know what system the procedure acts on | keep |
| `defined-in` | doesn't know the term | keep — cleanest reader-need-based label |
| `see-also` | unnameable need | keep sparingly |
| `supersedes` / `superseded-by` | wants current/prior version | keep |

**Recommendation:** merge `rationale` + `justification` → single `rationale` label. The reader-need is identical ("why does this design/rule exist?"); the source register (descriptive vs. prescriptive) is already visible from which collection authored the link.

## Summary

**Drop:** `cross-reference` (no specific reader-need).

**Merge:** `rationale` + `justification` → `rationale` (same reader-need).

**Fold:** `describes` into `part-of` or `see-also` depending on the specific case.

**Keep with guidance:** `see-also` — must pass an articulation test showing the reader-need before use. Default to a more specific label if one fits.

**Final vocabulary count:**
- Intra-theoretical: 7
- Intra-descriptive: 5 (part-of/contains, implements/implemented-by, supersedes/superseded-by, see-also, [+ compares-with in agent-memory-systems])
- Intra-prescriptive: 5 (composition, precondition, invokes, applies-when, see-also)
- Cross-register: 8 (rationale, evidence, derived-from, procedure, operates-on, defined-in, see-also, supersedes/superseded-by)

Each label carries a one-sentence reader-need that the writing skill can teach verbatim. Labels without such a justification shouldn't be adopted.
