=== PROSE REVIEW: 001-generate-topic-links-from-frontmatter.md ===

Checks applied: 8

WARN:
- [Source residue] The Consequences section states "Works across directories — `docs/notes/` and `docs/claw-design/` both supported." Neither `docs/notes/` nor `docs/claw-design/` exists in this repo; the actual directory structure uses `kb/notes/`. The script itself (`scripts/sync_topic_links.py`) references `kb/notes/` and `kb/claw-design/` in its usage examples. These `docs/` paths are residue from a prior directory layout that was not updated when the note was brought into this KB.
  Recommendation: Replace `docs/notes/` and `docs/claw-design/` with the current directory names (`kb/notes/` and whatever the second supported directory actually is, or remove the bullet if the cross-directory claim no longer applies).

INFO:
- [Orphan references] The note cites specific counts — "6 notes had `areas:` but no Topics section" and "5 notes had Topics linking to the wrong index" — without naming when or how the audit was performed. These are plausible first-party observations in an ADR context section, but a reader has no way to reproduce or verify them. Worth noting; not necessarily a problem for a decision record.

CLEAN:
- [Pseudo-formalism] No formal notation present. Nothing to check.
- [Confidence miscalibration] The note is an accepted ADR. It uses direct assertion to describe the decision and its consequences, which is the correct register for a decision record. No speculative frameworks are presented as established, and no established findings are hedged.
- [Proportion mismatch] The core claim is the decision to replace LLM-generated Topics footers with a deterministic script. Context (the "why") gets 2 paragraphs with concrete examples of drift. Decision (the "what") gets a clear numbered list. Consequences (the "so what") gets 5 bullets. Proportions match the load each section carries.
- [Unbridged cross-domain evidence] No cross-domain evidence is cited. The one external reference — "storing LLM outputs is constraining" — is an internal KB note used to name a general pattern, not empirical evidence from a different domain.
- [Redundant restatement] The note is concise (46 lines). No section opens by re-explaining what a prior section established. Each section begins with its own contribution.
- [Anthropomorphic framing] No language attributing human-like properties to models. The note refers to LLM behavior as "semantic judgment" and "stochastic LLM step," both precise and appropriate.

Overall: 1 warning, 1 info
===
