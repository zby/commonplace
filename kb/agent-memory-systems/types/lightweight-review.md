---
type: kb/types/type-spec.md
name: lightweight-review
description: Doc-grounded review of an external agent memory or context-engineering system when no source code is reachable — the same comparison elements as agent-memory-system-review, at a lower evidence tier
schema: ./lightweight-review.schema.yaml
---

# Lightweight agent memory system review

A **doc-grounded** review of an external agent memory, knowledge, or context-engineering system whose source code is **not reachable** — coverage comes from a paper, README, article, practitioner report, or ingest, not from inspecting code.

It carries the **same comparison elements** as [agent-memory-system-review](./agent-memory-system-review.md) so it populates the cross-system comparison uniformly. The "lightweight" label is about **authority, not scope**: capture whatever the sources document — mechanisms, the four-field record, the read-back direction, borrowable ideas — but never present a reported claim as a code-grounded finding.

**Use this type when** there is no reachable, inspectable source (paper-only system, closed product, practitioner write-up) *and* the sources document enough mechanism to fill the elements below. If inspectable source later appears and is read, **promote to `agent-memory-system-review`**.

## Relationship to agent-memory-system-review

Same sections, same four-field and read-back vocabulary. **Read [agent-memory-system-review](./agent-memory-system-review.md) for the element definitions** (Artifact analysis, the four fields, Read-back placement, Trace-derived learning placement, the placement triggers). This spec records only the deltas:

- **Evidence stance is claim-level by default.** The code review marks individual items "not verified from code"; here the *entire* review is doc-derived, so state mechanisms as *reported*, and do not assert deployed behavior the sources don't support. Where sources conflict or go quiet, say so rather than filling the gap.
- **Source metadata names documents, not a repo.** Record the paper / README / article / ingest and its version or date, in the body's source lines — not a repository and commit.
- **Citations point at the sources** (URLs, and `kb/sources/` ingest or snapshot links), never at source files. Keep the review readable without the original documents.
- **Depth follows the sources.** An honestly-thin section beats invented detail. A field that the sources simply don't address is left absent with a one-line note, not guessed.

`last-checked` records when the coverage was last reconciled against its sources (the same freshness discipline as the code review's source re-read).

## Sections

The same set as `agent-memory-system-review` — see that spec for what each contains:

- **Opening** + **Source metadata** (documents + version/date, not repo + commit)
- **Core Ideas** — including the required **context-efficiency** statement
- **Artifact analysis** — the four-field record (storage substrate, representational form, lineage, behavioral authority), claim-level
- **Comparison with Our System** + nested **### Borrowable Ideas**
- **Trace-derived learning placement** — optional; include and tag `trace-derived` only when the sources document a trace-learning mechanism
- **Read-back placement** — state the one-line **direction verdict** (pull / push / both) regardless; full section + `push-activation` tag only when the sources document an engineered activation path
- **Curiosity Pass**
- **What to Watch**
- **Relevant Notes**

## Frontmatter

- `description` — discriminating retrieval filter (50–200 chars, double-quoted)
- `type: ../types/lightweight-review.md`
- `status: current` unless clearly stale
- `last-checked: "{today}"`
- `tags` — add `trace-derived` and/or `push-activation` only per the placement triggers above; otherwise omit
- `traits` — `has-external-sources` (and `has-comparison` when a Comparison section is present), as for any note carrying those

## Constraints

- Don't present reported behavior as observed. No code was read.
- Don't invent four-field or read-back detail the sources don't support — leave the field absent with a note.
- Don't update `last-checked` without actually re-reading the sources.
- If reachable source exists and is inspected, this becomes an `agent-memory-system-review`, not a lightweight review.

## Template

```markdown
---
description: Lightweight doc-grounded coverage of {system} — {one-line on what it is and where the evidence comes from}
type: ../types/lightweight-review.md
traits: [has-external-sources]
status: current
last-checked: "YYYY-MM-DD"
---

# {System name}

{One-paragraph summary — what it is, what for, who built it, and that coverage is doc-grounded (no inspectable source).}

**Source:** {paper / README / article / ingest, with link}

**Reviewed version:** {version or date, if available}

## Core Ideas

{3–6 reported mechanisms, including the context-efficiency statement.}

## Artifact analysis

{Four-field record, claim-level. See agent-memory-system-review. Lead the first two with the same extractable controlled-value tokens:}

- **Storage substrate:** `{files|repo|sqlite|rdbms|vector|graph|kv|in-memory|prompt-registry|model-weights|service-object}` — {reported justification}
- **Representational form:** `{prose|symbolic|parametric|mixed}` — {reported justification}
- **Lineage** — {authored/imported/trace-extracted + derivation status}
- **Behavioral authority** — {knowledge-artifact vs system-definition}

## Comparison with Our System

{Alignments, divergences, tradeoffs vs Commonplace, as the sources support.}

### Borrowable Ideas

{For each idea: what it would look like in Commonplace; ready now or needs a use case first.}

## Read-back placement

**Read-back:** `{pull|push|both}` — {one-line reported justification; required regardless}

{Full section + `push-activation` tag only when sources document an engineered activation path.}

## Curiosity Pass

- {Surprises or curiosities from the sources}
- {Simpler alternatives worth checking}

## What to Watch

- {A specific pending change the sources point to + its consequence for our design.}

## Relevant Notes

- {links}
```
