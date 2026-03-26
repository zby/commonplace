---
description: Prose review adapted for review-revise experiment. Reads baseline.md, writes output to run directory.
---

# Prose Review (experiment)

**Target: kb/work/review-revise/baseline.md**

## What this is

A read-only review that catches cases where the prose misrepresents what the note actually establishes — problems that pass structural validation and may survive editorial revision because the sentences individually read fine. These are judgment checks, not deterministic rules. Report findings as WARN (likely real) or INFO (worth checking), never FAIL.

## Prerequisites

Read the target note in full. Skip git metadata — this is an experiment, not a production review.

## Checks

### 1. Source residue

**Failure mode:** The note was generalized from a domain-specific source, but concrete framing from that source leaked through — examples, vocabulary, metaphors that assume a domain the note no longer addresses.

**Test:** Read the note's title and opening paragraph to establish its claimed generality level. Then scan the body for terms, examples, or analogies that belong to a narrower domain.

**Recommendation:** Either generalize the residue or frame it explicitly as an example.

### 2. Pseudo-formalism

**Failure mode:** Notation or formal-looking apparatus that doesn't add precision beyond what the surrounding prose already provides. Variables that aren't measurable, equations that assume unstated independence, decompositions that look mathematical but are actually verbal arguments in symbols.

**Test:** Delete the formalism and re-read the passage. If the argument is equally clear and precise, the formalism was decorative. Could someone use the notation to make a quantitative prediction or derive a non-obvious consequence? If not, it's not doing formal work.

**Recommendation:** Remove the notation and strengthen the prose. If the formalism genuinely adds precision, keep it but state its assumptions explicitly.

### 3. Confidence miscalibration

**Failure mode:** A speculative framework presented as established, or established findings presented as tentative.

**Test:** For each framework, taxonomy, or causal model the note introduces, check: is it cited from a source, or is it the note's own construction? If the note's own, is it flagged as proposed?

**Recommendation:** Match the language to the epistemic status.

### 4. Proportion mismatch

**Failure mode:** The most important idea gets thin treatment while a less critical idea gets extensive development.

**Test:** Identify the note's core claim (usually the title). Ask: which section carries the most weight for that claim? Then compare word counts across sections. If the load-bearing section is shorter than supporting sections, the proportions are off.

**Recommendation:** Develop the underdeveloped section. Consider whether the overdeveloped section belongs in a separate note.

### 5. Orphan references

**Failure mode:** A specific figure, data point, or empirical claim appears with no source, context, or prior mention in the note.

**Test:** Search the note for specific numbers, percentages, named studies, or empirical claims. For each, check: is the source cited?

**Recommendation:** Either add the source and context, or remove the claim.

### 6. Unbridged cross-domain evidence

**Failure mode:** Evidence from one domain is cited as if it directly applies to another domain without explaining why the transfer is valid.

**Test:** For each cited study or empirical finding, check: does the source's domain match the note's domain? If not, does the note explain why the finding transfers?

**Recommendation:** Add a bridge that states the shared mechanism. If no bridge is defensible, weaken the claim to analogy.

### 7. Redundant restatement

**Failure mode:** A section opens by re-explaining what a prior section already established, before getting to its own contribution.

**Test:** Read the first paragraph of each section. Does it add new information, or does it restate the previous section's conclusion as setup? If the paragraph could be deleted and the section still makes sense from its second paragraph onward, it's restatement.

**Recommendation:** Cut the restating paragraph. If a brief transition is needed, one sentence suffices.

### 8. Anthropomorphic framing

**Failure mode:** Language that attributes human-like properties to models when more precise technical language is available.

**Test:** Flag verbs and nouns that imply agency, ownership, or mental states. Ask: does this word carry claims about the model's internals that the note doesn't intend to make?

**Recommendation:** Substitute precise language.

## Output

Write the review to `kb/work/review-revise/run-01/prose-review.md` using this format:

```
=== PROSE REVIEW: baseline.md ===

Checks applied: 8

WARN:
- [{check-name}] {finding with specific quote from the note}
  Recommendation: {what to change}

INFO:
- [{check-name}] {finding}

CLEAN:
- [{check-name}] {what was checked and why it held}

Overall: {CLEAN / {N} warnings, {M} info}
===
```

Report every check — WARN, INFO, or CLEAN.

## Do NOT

- Do not modify the target note. This is read-only analysis.
- Do not report structural issues (frontmatter, link health, sections). That's `/validate`'s job.
- Do not report content correctness issues (grounding alignment, completeness). That's semantic review's job.
- Do not report editorial flow issues (transitions, cohesion). That's a separate concern.
- Do not review more than one note per invocation.
