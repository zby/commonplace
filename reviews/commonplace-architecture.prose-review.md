=== PROSE REVIEW: commonplace-architecture.md ===

Checks applied: 8

WARN:
- [Proportion mismatch] The core claim of this note is "the commonplace repo's own internal layout" (per the title and description), yet the longest and most developed section is "Global types belong in CLAUDE.md, not kb/types/" — an argument about one specific design choice. The "Current layout" section (the actual architecture) is a bare directory tree with no explanatory prose, and "What's missing" is a three-row table with no discussion. The note's center of gravity is the global-types argument, but the note frames itself as an architecture overview.
  Recommendation: Either develop the layout and missing-artifacts sections with explanatory prose proportional to their architectural importance, or retitle the note to reflect that its real contribution is the global-types decision (and extract the layout into its own note or keep it as a brief preamble).

- [Confidence miscalibration] The "What's missing" table lists `CLAUDE.md` as "Missing" with status note "The repo's own instructions, routing table, and knowledge system section." The repo now has a `CLAUDE.md` — this table row is stale and asserts a gap that no longer exists. Similarly, the "Decision: drop `kb/types/` as a required directory" is stated as a concluded decision without indicating whether it has been enacted or remains proposed.
  Recommendation: Update the missing-artifacts table to reflect current state. For the decision, indicate whether it is enacted (and link to the commit or change) or still proposed.

INFO:
- [Redundant restatement] The opening sentence — "The commonplace repo is itself a knowledge base — it uses its own knowledge system to document the methodology for building knowledge bases" — is repeated verbatim from `CLAUDE.md`. Within this note it serves as an introduction, so it's not strictly redundant *internally*, but a reader arriving from CLAUDE.md will read the same sentence twice. Worth noting as a minor friction point.

- [Proportion mismatch] The "Open Questions" section contains two bullets that feel underdeveloped relative to the specificity of the global-types argument. They read as afterthoughts rather than live questions the note is tracking. If these questions have been resolved, they should be removed; if they're active, they could benefit from brief context on what makes each question hard.

CLEAN:
- [Source residue] The note is about the repo's own architecture. All terms — "types/", "CLAUDE.md", "frontmatter", "maturity ladder" — belong to the commonplace domain. No leaked vocabulary from an external source domain.

- [Pseudo-formalism] No formal notation or mathematical apparatus is used. The directory tree and table are appropriate representational choices for this content.

- [Orphan references] No specific figures, percentages, or empirical claims appear without context. All references are to internal repo artifacts.

- [Unbridged cross-domain evidence] The note does not cite evidence from external domains. All claims are about the repo's own design.

- [Anthropomorphic framing] The note uses "the agent internalizes" and "agents read them repeatedly" — these are standard usage in this KB's vocabulary for describing LLM agent behavior during document creation. The verbs "internalizes" and "read" are used in their operational sense (loaded into context, parsed during execution) rather than implying cognitive states. Clean within this KB's conventions.

Overall: 2 warnings, 2 info
===
