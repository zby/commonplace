---
description: Four use cases for inbound link visibility (hub identification, source-to-theory bridging, impact assessment, tension surfacing) with four design options and their maintenance trade-offs
type: note
traits: [has-comparison]
tags: [links]
status: speculative
---

# Backlinks — use cases and design space

## The gap

The knowledge system tracks outbound links well: notes have inline links and "Relevant Notes" footers declaring what they depend on. But no note knows who links TO it. An agent reading `deploy-time-learning-is-the-missing-middle.md` — referenced by 48 other notes at time of writing — sees only the notes it cites, not the notes that cite it.

Grep-based discovery exists (`rg 'note-title\.md' --glob '*.md'`), but agents have to think to run it. The question is whether inbound connections should be visible at reading time, and if so, how.

## Concrete use cases

### 1. Hub identification — "is this note foundational or peripheral?"

An agent lands on a note via an index. Outbound links show what informed it, but nothing shows whether 10 other notes build on it or nobody references it at all. Seeing "3 notes extend this, 2 exemplify it, 1 contradicts it" would change how carefully the agent reads and whether it risks editing.

This matters most during cold-start orientation in an unfamiliar area.

### 2. Source-to-theory bridge — "what practitioner evidence exists for this claim?"

Ingest reports in `kb/sources/` link TO KB notes (e.g., [koylanai-personal-brain-os.ingest.md](../sources/koylanai-personal-brain-os.ingest.md) links to [storing-llm-outputs-is-constraining](./storing-llm-outputs-is-constraining.md)). But the theory note doesn't know it has practitioner evidence pointing at it. As sources accumulate, backlinks would let an agent see how well-grounded a theoretical claim is — and spot synthesis opportunities when enough sources converge.

### 3. Impact assessment — "what breaks if I change this?"

Before editing a claim in a highly-referenced note, an agent needs to know what depends on it. Backlinks with relationship types would show this at a glance: "3 notes use this as foundation — changing the core claim affects them. 2 notes merely exemplify it — those are safe." Currently this requires a manual grep plus reading each result.

### 4. Tension surfacing — "who disagrees with this?"

When a note acquires a "contradicts" link from another note, the tension is only visible if you happen to read the contradicting note. Backlinks could surface tensions from both sides, making unresolved debates visible regardless of which note you enter through.

## Non-use-cases

- **Creating new notes** — finding relevant existing notes to link to is a search/discovery problem, not a backlink problem.
- **Orphan detection** — a batch maintenance task already handled by [grep-based checks](./maintenance-operations-catalogue-should-stage-distillation-into-instructions.md). Both orphan detection and hub identification use inbound link counts, but they differ in threshold (zero vs. high) and purpose (batch cleanup vs. read-time orientation). Orphan detection doesn't need read-time visibility — it's a periodic sweep, not a navigation aid.
- **Index maintenance** — indexes are curated navigation, not mechanical link lists. Backlinks don't replace the judgment needed to decide what belongs in an index.

## Design options

The use cases above all need the same underlying data — an inverted link index. They differ in whether that data should be visible in the note, computed on demand, or both.

### A. Generated report (computed, not stored in notes)

A script scans all `.md` files, extracts links, inverts them, and produces a report. Notes themselves don't change.

- Pros: zero maintenance burden, always fresh, no note pollution
- Cons: not visible when reading a note; agents must know to run the script
- Precedent: the grep-based maintenance checks already work this way

### B. Generated footer sections (sync script)

A script generates a "Referenced by:" footer in each note, similar to how `sync_topic_links.py` generates Topics footers from frontmatter. Run periodically or on commit.

- Pros: visible at read time, deterministic, no agent judgment needed
- Cons: generated sections add noise; relationship semantics can't be inferred mechanically (is this link "extends" or "exemplifies"?); merge conflicts if agents edit notes while footers are regenerating

### C. Manual bidirectional links (agent discipline)

Agents add backlinks manually whenever they create an outbound link. The /connect skill already has a "Bidirectional Check" gate, but it's applied sporadically.

- Pros: semantic relationship types preserved; curated, not mechanical
- Cons: maintenance burden; inconsistent unless enforced; 30 of 224 notes (13%) lack even outbound Relevant Notes sections as of 2026-03-27

### D. Hybrid — generated index + manual enrichment

A script generates a bare list of inbound links (no semantics). Agents optionally annotate the relationship type when they encounter the generated list. The script handles "these exist"; agents add "why it matters."

- Pros: zero-cost discovery + optional depth
- Cons: two-layer system adds complexity; unannotated backlinks are noisy

## Trade-offs

**Prose readability vs completeness.** The system prioritises inline links as prose. A backlinks footer with 12 entries is metadata, not prose — notes with many inbound links would get long sections that don't read naturally.

**Maintenance consistency.** Manual backlinks (option C) fail unless enforced. Even outbound Relevant Notes sections are incomplete. Adding a second direction doubles the surface area for inconsistency.

**Source boundary.** The /ingest pipeline deliberately keeps connections in the ingest report rather than modifying KB notes. Backlinks would create implicit two-way relationships between sources and notes — useful (use case 2) but it changes the boundary between the two layers.

## Open questions

- Which use cases justify the cost? Hub identification and source bridging seem highest value; tension surfacing is lower frequency.
- Should the script run at commit time, on demand, or as part of session start?
- Is there a threshold below which backlinks add noise rather than signal (e.g., a note with one inbound link)?

---

Relevant Notes:

- [linking-theory](./linking-theory.md) — extends: linking-theory develops link quality for outbound links; this note extrapolates the same decision-cost framing to inbound visibility
- [generate-instructions-at-build-time](./generate-instructions-at-build-time.md) — related pattern: deterministic generation from structured data, the approach that option B would follow
