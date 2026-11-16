---
description: "Use to fix one review finding on one note by the named strategy whose pattern it matches; also the codebook of named fix strategies"
type: types/edit-operation.md
effort: judgment
decision: none
responds-to: [prose/source-residue, semantic/grounding-alignment, semantic/completeness-boundary-cases]
---

# Fix a finding by a named strategy

Resolve one review finding on the text with the strategy whose pattern it
matches, changing only the passage the finding names.

Each strategy below names a recurring pattern of review warning and its
appropriate fix. The strategies are organized by the review check they most
commonly address, but a strategy can apply across checks. The report names a
strategy by its anchor, such as `fix-strategy-taxonomy.md#stale-paths`. When
a fix fits no listed strategy, the report names it `new-pattern`; recurring
new patterns are added here.

## Steps

The caller supplies the finding as the `finding` input: a review result file,
or a file holding one finding with its criterion, its quoted passage and its
reason. Fix only that finding.

A review result can hold several findings. When the caller also supplies
`finding-answers`, the operator has decided each finding of that result:
the file's items are the findings, by their position in `findings`. Fix only
the findings whose item is `approved`. Leave every `rejected`, `deferred` or
`pending` finding untouched, even when you would fix it.

When the caller supplies `earlier-decisions`, do not fix a finding that the
operator rejected there, unless the text changed in a way that answers the
operator's reason.

1. Find the finding's passage in the text. If the text no longer shows the
   pattern the finding names, change nothing and say so in the report.
2. Choose the strategy whose pattern matches the finding. Verify the pattern
   against the text before acting, as the strategy's typical fix says.
3. Apply the strategy's typical fix to that passage, with the lightest change
   that resolves the finding.
4. If no strategy fits, fix the passage as the finding asks and name the
   strategy `new-pattern`, with one sentence describing the pattern.

## Report

One line per change: the strategy by anchor, or `new-pattern` with its
description; the passage; and what changed. A finding the text no longer
shows is reported as not applicable, with the passage that now stands there.
List once each finding of the result that you did not touch, by its position
in `findings`, with the reason: the operator did not approve it, the operator
rejected it earlier, or the text no longer shows it.

## Preserve

Every passage the finding does not name. The note's claims beyond the
narrowing or attribution the strategy prescribes: a fix that would change
what the note argues is reported, not applied.

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

*New strategies are added when `new-pattern` reports show recurring patterns.*
