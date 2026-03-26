---
description: "Prose review v2 — catches representational failures. Key change from v1: pseudo-formalism check considers standalone readability, not just internal precision. Redundant-restatement check looks at transitions between sections, not just section openings."
---

# Prose Review v2 (experiment)

**Target: kb/work/review-revise/baseline.md**

## What this is

A read-only review that catches cases where the prose misrepresents what the note actually establishes. These are judgment checks, not deterministic rules. Report findings as WARN (likely real) or INFO (worth checking), never FAIL.

## Prerequisites

Read the target note in full. Skip git metadata — this is an experiment.

## Checks

### 1. Source residue

**Failure mode:** The note was generalized from a domain-specific source, but concrete framing leaked through.

**Test:** Read the title and opening to establish the claimed generality level. Scan the body for terms or analogies that belong to a narrower domain.

### 2. Pseudo-formalism

**Failure mode:** Notation or formal-looking apparatus that doesn't add precision beyond what prose provides.

**Test:** Two tests, both must pass for notation to be acceptable:
1. **Precision test:** Delete the notation and re-read. If the argument is equally clear, the formalism was decorative.
2. **Standalone readability test:** Would a reader who has NOT read the source model understand the sentence with the notation? Notation that serves as cross-reference shorthand for insiders but is opaque to outsiders fails this test even if it passes the precision test.

Notation fails if it fails either test. "Storage in `K` is cheap" may pass the precision test (K names a specific concept more concisely than prose) but fail the standalone test (a reader who hasn't read the orchestration model note cannot parse the sentence).

**Recommendation:** Replace notation with plain language unless the note uses it in formal arguments (equations, pseudocode, algorithmic steps).

### 3. Confidence miscalibration

**Failure mode:** A speculative framework presented as established, or established findings presented as tentative.

**Test:** For each taxonomy or causal model, check: cited from a source, or the note's own? If the note's own, is it flagged as proposed?

### 4. Proportion mismatch

**Failure mode:** The most important idea gets thin treatment while a less critical idea gets extensive development.

**Test:** Identify the core claim. Compare word counts across sections. If the load-bearing section is shorter than supporting sections, the proportions are off.

### 5. Orphan references

**Failure mode:** A specific claim appears with no source or context.

**Test:** Search for specific numbers, named studies, or empirical claims. Check for sources.

### 6. Unbridged cross-domain evidence

**Failure mode:** Evidence from one domain is cited as if it applies to another without explaining the transfer.

**Test:** For each cited finding, check domain match. If no match, check for a bridge explanation.

### 7. Redundant restatement

**Failure mode:** A section or paragraph re-explains what a prior section already established.

**Test (expanded from v1):** Two specific patterns to check:
1. **Section-opening restatement:** A section's first paragraph restates the previous section's conclusion. If deletable without loss, it's restatement.
2. **Bridge paragraph duplication:** A transition paragraph between sections previews exactly what the next section then enumerates. If the transition paragraph and the section's own content cover the same ground, the transition is redundant.

### 8. Anthropomorphic framing

**Failure mode:** Language that attributes human-like properties to models when more precise language is available.

**Test:** Flag verbs implying agency or mental states. Check if more precise alternatives exist.

## Output

Write the review to the run directory using this format:

```
=== PROSE REVIEW v2: baseline.md ===

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
- Do not report structural issues (frontmatter, link health). That's `/validate`'s job.
- Do not report content correctness (grounding, completeness). That's semantic review's job.
