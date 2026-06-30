# Split and Rehome Critique: Prose has no reliable dereference, so a declared fact must be reinforced where it applies

**Target:** `kb/work/agent-note-improvement/case-02-prose-dereference/baseline-working-tree.md`

## Main note to preserve

**Claim:** Because LLM-read prose does not mechanically dereference declarations into later uses, facts that must govern downstream interpretation often need local reinforcement, with an external check keeping the repeated copies aligned.

**Minimum argument:**

- In code and other codified forms, a named declaration can be resolved mechanically wherever it is referenced.
- LLM-read prose does not have that operation; applying a declaration later is an interpretive act.
- Interpretive reach decays with distance, non-obviousness, and conditional applicability.
- Therefore prose sometimes needs denormalized reinforcement at the point of use.
- Redundant prose copies can drift, so the safe pattern is denormalized reader-facing copy plus normalized verification.
- The rule is graded by representational form: codified artifacts need less reinforcement, prose-like artifacts need more.

Material that must stay: the code/frontmatter contrast, the `status: seedling` example, the denormalize-copy/normalize-check rule, the costs of bulk/branching/guard work, the representational-form boundary, and the falsifiable ablation.

## Branch inventory

| Branch | Current location | Destination | Why |
|---|---|---|---|
| Code dereference analogy | Opening | Keep | It is the main contrast that makes the prose failure concrete. |
| `status: seedling` point-of-use example | Opening | Keep | It grounds the claim in an actual KB behavior: a status label should change how downstream claims are treated. |
| "Single-source-of-truth, correct for code, is unsafe for prose" | Main argument | Keep, but narrow | Strong and useful, but should be phrased as safe where dereference is mechanical rather than universally correct for all code. |
| Denormalized copies with normalized check | Main argument | Keep | This is the note's operational payoff and distinguishes useful redundancy from uncontrolled duplication. |
| Conditional applicability pushes branching somewhere | Costs | Keep, but compress | This is a real cost of reinforcement, but the paragraph currently carries more detail than needed for the central claim. |
| Guard work | Costs | Keep | It prevents the note from recommending unchecked duplication. |
| Representational-form scope | Scope | Keep | It prevents overgeneralization and links the claim to the KB's vocabulary. |
| Testing it | Final section | Keep, but tighten | The note is seedling; the falsifiable form is useful. The section should be shorter and point directly to the ablation. |

## Rehoming candidates

None. The baseline does not contain a branch like the hallucination section in case 01. Its secondary material mostly supports the same operational rule.

Possible future note, not a split from this one:

- **Conditional facts make prose denormalization pay a branching cost** — Claim: denormalizing unconditional facts is cheap, but denormalizing value-dependent facts pushes branching into templates, process constraints, or validators. Required support: examples across note status banners, type-specific instructions, and generated indexes. It should not be split now because the current note needs this cost as a caveat.

## Deletion candidates

- Delete or compress wording that invites a literal claim that all code uses single-source-of-truth safely. The relevant property is mechanical dereference, not code as a domain.
- Compress the conditional-applicability explanation so it states the branching tradeoff without walking through too many alternatives.
- Compress the "Testing it" section so the weak point and ablation do not feel like a second mini-proposal.

## Revision target

The revised local copy should stay as one note. It should make the central chain more explicit: formal dereference makes single declarations travel; prose has interpretation instead; interpretation decays with distance and conditionality; reliable use therefore requires local reinforcement; safe reinforcement requires a normalized external check. The revision should tighten costs and testing, not split the note.
