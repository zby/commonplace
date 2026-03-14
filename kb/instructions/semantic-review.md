---
description: Adversarial semantic review of a single KB note — checks completeness of enumerations and frameworks via boundary cases, grounding alignment with cited sources, and internal consistency. Complement to /validate (which checks structure, not content).
---

# Semantic Review

**Target: $ARGUMENTS**

If target is empty, ask which note to review. If target is a name without path, search `kb/notes/` for a matching `.md` file.

## What this is

Three content-level checks that structural validation (`/validate`) cannot perform. These are LLM judgment checks — findings are probabilistic, not deterministic. Report findings as WARN (likely real) or INFO (worth checking), never FAIL.

## Prerequisites

Read the target note in full. If it has no frontmatter (text type), report "text files are not reviewable — no claims to check" and stop.

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

1. Read the linked source (follow the markdown link). Prioritise sources that ground the note's central claims. Follow at most 5 linked sources.
2. **Check attribution accuracy** — does the source actually say what the note claims it says? Watch for:
   - **Vocabulary mismatch** — the note uses terms the source doesn't. If the note says "improves trustworthiness" but the source says "constrains the interpretation space," the note is making an inference, not an attribution. Report INFO if the inference is reasonable, WARN if it's a stretch.
   - **Scope mismatch** — the note claims a larger framework than the sources support. If the source says "two mechanisms" but the note promotes to "three operations," the upgrade is the note's own move and readers could mistake the links as grounding for the larger claim. Report WARN.
3. **Check domain coverage** — after checking individual attributions, do a whole-note pass. Ask: what is the source *about* (its domain), and does the note's argument stay within that domain? A note may accurately describe a source's claims yet silently extend them to adjacent territory. If the source formalizes X (e.g. extractable structure) but the note uses it to ground a claim about Y (e.g. information value, which includes facts), the grounding covers a subset of the claim, not the whole thing — even if every individual quote checks out. Report WARN when the note's claim domain exceeds the source's domain.
4. **Check inference validity** — does the conclusion follow from the cited evidence, or is there a logical gap? Report WARN for invalid inferences, INFO for inferences that are plausible but not airtight.

## Step 4: Internal consistency

1. Extract the key claims from each section of the note.
2. Check for **pairwise contradiction** — does any section assert something that conflicts with another section?
3. Check for **definition drift** — is a term defined one way and used differently later?
4. Check whether the **compressed summary** (if present) faithfully represents the body. Summaries often elide tensions that the body acknowledges.
5. Report WARN for contradictions, INFO for potential ambiguities.

## Output format

```
=== SEMANTIC REVIEW: {note-filename} ===

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

Always include the PASS section — it's important to show what was checked and found sound, not just what failed. This calibrates trust in the review.

## Do NOT

- Do not modify the note. This is read-only analysis.
- Do not report structural issues (frontmatter, link health, sections). That's `/validate`'s job.
- Do not treat findings as certain. These are LLM judgment calls — flag them for human review, don't assert them as facts.
- Do not review more than one note per invocation. Run separately for each note.
- Do not load more than 5 linked sources. Keep context bounded.
