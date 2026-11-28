---
description: "Proposal: surface inbound links through build-time web rendering for humans and on-demand inversion for agents while allowing useful reciprocal links, not mandatory mirroring"
type: reference/types/design-proposal.md
tags: [links]
---

# Backlink surfacing

A reader viewing a policy may want to know which checklists cite it. The proposed change is to show those checklists on the published policy page, without adding links to the policy’s source file.

## Current state (as of 2026-11-28)

- **Repository search:** `rg -n -F 'policy.md' kb/ -g '*.md'` finds candidate citations to a file named `policy.md`. Inspect the matches: a filename mention is not necessarily a link, and files in different directories can share a name.
- **Review:** The [role report](../review-architecture.md) already receives citing passages. Its collector resolves local links to the target file, excludes workshop and report directories, and bounds the passages supplied. This is input to a review, not a navigation panel for someone reading the page.
- **Publication:** [ADR 025](../adr/025-complete-generated-indexes-are-build-time-only.md) keeps complete generated indexes out of committed Markdown and builds them for the site. That supplies a precedent for a generated list of citations; it does not itself adopt one.

## Design space, split by consumer

- **Human web readers** — at build time, index authored links by destination. On each rendered destination page, show a **Referenced by** list linking back to the source pages. These are outgoing navigation links on the displayed page, not citations in its Markdown. Exclude the generated lists from the index input. As with the complete indexes in ADR 025, the build does not write these links into the committed notes.
- **Repository readers** — keep lookup on demand. A dedicated command would be worth considering if filename searches repeatedly miss citations or produce costly false matches; the proposed web display does not require a command.
- **Meaning of a citation** — show which page links here without implying that it endorses the target. Where the distinction matters, let the reader inspect the authored passage.

## Foreclosed options

- **Committed generated footers** ("Referenced by:" sections written into notes by a sync script) — would put a complete generated list into the source notes, contrary to the build-time approach in ADR 025.
- **Mandatory manual bidirectionality** (agents author a backlink for every outbound link) — fan-out makes upstream maintenance scale with a note's popularity. This does not foreclose a reciprocal link that independently serves readers at the other endpoint.

## Open questions

- Noise floor: is a one-entry inbound list worth rendering, or should the web section appear only above a threshold?
- Does the agent-side recipe deserve a command (`commonplace-backlinks <note>`), or is that the codification ADR 025 says to defer until recurring failure?
- Should source→note inbound edges (the grounding need) render distinctly from note→note edges in the web view?

---

Relevant Notes:

- [inbound and outbound links serve asymmetric reader needs](../../theory/inbound-and-outbound-links-serve-asymmetric-reader-needs.md) — rests-on: the reader needs and boundaries this design must satisfy
- [ADR 025 — complete generated indexes are build-time only](../adr/025-complete-generated-indexes-are-build-time-only.md) — rests on: the one-source-two-materializations pattern and the no-new-command default this proposal extends to backlinks
