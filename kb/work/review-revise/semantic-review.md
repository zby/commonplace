---
description: Semantic review adapted for review-revise experiment. Reads baseline.md, writes output to run directory.
---

# Semantic Review (experiment)

**Target: kb/work/review-revise/baseline.md**

Note: this note originally lived at `kb/notes/session-history-should-not-be-the-default-next-context.md`. Resolve linked sources relative to `kb/notes/`.

## What this is

Three content-level checks that structural validation (`/validate`) cannot perform. These are LLM judgment checks — findings are probabilistic, not deterministic. Report findings as WARN (likely real) or INFO (worth checking), never FAIL.

## Prerequisites

Read the target note in full. Skip git metadata — this is an experiment, not a production review.

## Step 1: Extract claims

Read the note and list its key claims. A claim is any assertion the note makes — explicit statements, enumerations, causal arguments, definitions. Include:

- Numbered enumerations ("three operations," "two mechanisms")
- Causal claims ("X because Y," "X improves Y")
- Definitions ("X is Y")
- Scope claims ("all," "only," "the complete set")
- Dependency claims ("X depends on Y," "X is the foundation")

Write down each claim verbatim with its location (section heading or line context). These are the inputs to the three checks below.

## Step 2: Completeness and boundary cases

This is the most important check. It applies to enumerations, frameworks, taxonomies, and any argument that claims to cover a space.

For each enumeration or framework claim:

1. **Find the grounding definition.** Two paths:
   - If the note cites an explicit definition (e.g. "per Simon, learning is any capacity change"), use that as the ground.
   - If no explicit definition is cited, use the note's own framing — its title claim, its stated scope, the concept it defines. Every framework implicitly defines a space; generate boundary cases from that implicit space.
2. **Generate boundary cases.** Produce 3-5 cases that probe the edges:
   - The **simplest possible instance** of the concept the note discusses.
   - The **most extreme instance** — what happens at scale, under pressure, or in degenerate cases.
   - Cases that sit **between enumerated items** — things that seem like they should be covered but don't clearly map to any single item.
   - Cases from **adjacent concepts** — things that are close but might fall outside the claimed scope.
3. **Test each boundary case** against the enumeration or framework. Does it map cleanly to one of the enumerated items? Does the framework account for it?
4. **Report findings:**
   - WARN if a boundary case clearly falls outside all enumerated items or breaks the framework.
   - INFO if a boundary case is ambiguously covered — it could be forced into an item but the fit is strained.

## Step 3: Grounding alignment

For each causal claim or conclusion that cites evidence or references another note:

1. Read the linked source (follow the markdown link, resolving relative to `kb/notes/`). Prioritise sources that ground the note's central claims. Follow at most 5 linked sources.
2. **Check attribution accuracy** — does the source actually say what the note claims it says? Watch for:
   - **Vocabulary mismatch** — the note uses terms the source doesn't.
   - **Scope mismatch** — the note claims a larger framework than the sources support.
3. **Check domain coverage** — does the note's argument stay within the domain the sources support?
4. **Check inference validity** — does the conclusion follow from the cited evidence, or is there a logical gap?

## Step 4: Internal consistency

1. Extract the key claims from each section of the note.
2. Check for **pairwise contradiction** — does any section assert something that conflicts with another section?
3. Check for **definition drift** — is a term defined one way and used differently later?
4. Check whether the **compressed summary** (if present) faithfully represents the body.
5. Report WARN for contradictions, INFO for potential ambiguities.

## Output

Write the review to `kb/work/review-revise/run-01/semantic-review.md` using this format:

```
=== SEMANTIC REVIEW: baseline.md ===

Claims identified: {count}

WARN:
- [{check-name}] {finding with specific quote from the note}

INFO:
- [{check-name}] {finding}

PASS:
- [{check-name}] {what was checked and why it held}

Overall: {CLEAN / {N} warnings, {M} info}
===
```

Always include the PASS section.

## Do NOT

- Do not modify the target note. This is read-only analysis.
- Do not report structural issues (frontmatter, link health, sections). That's `/validate`'s job.
- Do not treat findings as certain. These are LLM judgment calls.
- Do not load more than 5 linked sources. Keep context bounded.
