---
description: Analysis of where backlinks (inbound link visibility) would concretely help agents working in the KB — use cases, trade-offs, and design options
type: note
traits: [has-comparison]
areas: [links]
status: speculative
---

# Backlinks — use cases and design space

## The gap

The knowledge system tracks outbound links well: notes have inline links and "Relevant Notes" footers declaring what they depend on. But no note knows who links TO it. An agent reading `deploy-time-learning-the-missing-middle.md` — which is referenced by 10+ files — sees only the notes it cites, not the notes that cite it.

The system provides grep-based discovery (`rg 'note-title\.md' --glob '*.md'`), but that's a manual step agents have to think to perform. Backlinks would make inbound connections visible at reading time, not just searchable.

## Concrete use cases

### 1. Hub identification — "is this note foundational or peripheral?"

An agent lands on a note via an index. The outbound links show what informed this note. But the agent can't tell: is this note a hub that 10 other notes build on, or a leaf that nobody references?

With backlinks, the agent sees immediately: "3 notes extend this, 2 exemplify it, 1 contradicts it." That changes how carefully they read it and whether they consider editing it.

**Who benefits:** Any agent starting a session in an unfamiliar area. Reduces cold-start orientation cost.

### 2. Source-to-theory bridge — "what practitioner evidence exists for this claim?"

The new `docs/sources/` directory stores ingested external references. Ingest reports link TO KB notes (e.g., [koylanai-personal-brain-os.ingest.md](../sources/koylanai-personal-brain-os.ingest.md) links to [storing-llm-outputs-is-stabilization](../notes/storing-llm-outputs-is-stabilization.md)). But the theory note doesn't know it has practitioner evidence pointing at it.

As sources accumulate, backlinks would let an agent reading a theoretical note see: "3 practitioner reports exemplify this claim." That's a signal about the claim's empirical grounding — and a synthesis opportunity when enough sources converge.

**Who benefits:** The /ingest skill and any agent evaluating whether a theoretical claim has real-world evidence.

### 3. Impact assessment before editing — "what breaks if I change this?"

Before editing a claim in a highly-referenced note, an agent needs to know what depends on it. Currently this requires a manual grep + reading each result. Backlinks with relationship types would let the agent see at a glance: "3 notes use this as foundation — changing the core claim affects them. 2 notes merely exemplify it — those are safe."

**Who benefits:** Any agent editing an established note. Prevents unintentional downstream breakage.

### 4. Tension surfacing — "who disagrees with this?"

When a note acquires a "contradicts" link from another note, that tension is only visible if you happen to read the contradicting note. Backlinks would surface tensions from both sides, making unresolved debates visible regardless of which note you're reading.

**Who benefits:** Agents doing synthesis or reviewing note consistency.

## Non-use-cases (what backlinks don't help with)

- **Creating new notes** — when writing a new note, you need to find relevant existing notes to link to. That's a search/discovery problem, not a backlink problem. Grep and index scanning handle this.
- **Orphan detection** — already handled by the existing grep-based helper in CLAUDE.md. Backlinks would make it marginally easier but don't unlock new capability.
- **Index maintenance** — indexes are curated navigation, not mechanical link lists. Backlinks don't replace the judgment needed to decide what belongs in an index.

## Design options

### A. Generated report (computed view, not stored in notes)

A script scans all `.md` files, extracts links, inverts them, and produces a report or queryable artifact. Notes themselves don't change.

- Pros: zero maintenance burden, always fresh, no note pollution
- Cons: not visible when reading a note; agents must know to run the script
- Precedent: the orphan/dangling detection scripts in CLAUDE.md work this way

### B. Generated footer sections (sync script, like Topics)

A script generates a "Referenced by:" footer in each note, similar to how `sync_topic_links.py` generates Topics footers from frontmatter areas. Run periodically or on commit.

- Pros: visible at read time, deterministic, no agent judgment needed
- Cons: generated sections add noise; relationship semantics can't be inferred mechanically (is this link "extends" or "exemplifies"?); merge conflicts if agents edit notes while footers are regenerating
- Precedent: ADR-001 (generate topic links from frontmatter) — same pattern, different link type

### C. Manual bidirectional links (agent discipline)

Agents add backlinks manually whenever they create an outbound link. The /connect skill already has a "Bidirectional Check" gate, but it's applied sporadically.

- Pros: semantic relationship types preserved; curated, not mechanical
- Cons: maintenance burden; inconsistent unless enforced; 44% of notes currently lack Relevant Notes sections at all
- Precedent: the current system's aspiration, partially realized

### D. Hybrid — generated index + manual enrichment

A script generates a bare list of inbound links (no semantics). Agents can optionally annotate the relationship type when they encounter the generated list. The generated list serves as a "these exist" signal; the annotation adds the "why it matters" layer.

- Pros: zero-cost discovery + optional depth; script handles mechanical work, agents add judgment only when useful
- Cons: two-layer system adds complexity; unannotated backlinks are noisy

## Trade-offs to consider

**Prose readability vs completeness.** The system prioritises inline links as prose. A backlinks footer with 12 entries is metadata, not prose. Notes with many inbound links would get long footer sections that don't read naturally.

**Maintenance consistency.** Manual backlinks (option C) fail unless enforced. 44% of notes lack even outbound Relevant Notes sections. Adding a second direction doubles the surface area for inconsistency.

**Source integration.** The /ingest pipeline deliberately keeps connections in the ingest report rather than modifying KB notes. Backlinks would create implicit two-way relationships between sources and notes. That's useful (use case 2) but changes the boundary between sources and notes.

## Open questions

- Which use cases justify the cost? Hub identification and source bridging seem highest value; tension surfacing is lower frequency.
- Should backlinks be visible in the note itself, or only via a tool/script? The answer depends on how often agents would benefit from seeing them during normal reading vs on-demand.
- If generated, should the script run at commit time, on demand, or as part of session start?

---

Relevant Notes:
- [link-contracts-framework](./link-contracts-framework.md) — foundation: backlinks are a special case of link visibility; the "click decision" framework applies to deciding whether to follow an inbound link too
- [001-generate-topic-links-from-frontmatter](./adr/001-generate-topic-links-from-frontmatter.md) — precedent: deterministic link generation from structured data, the pattern that option B would follow

Topics:
- [links](./links.md)
