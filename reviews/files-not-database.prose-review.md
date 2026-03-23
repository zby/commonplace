=== PROSE REVIEW: files-not-database.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The title "Files beat a database for agent-operated knowledge bases" and opening "The temptation as a KB grows is to move to a database" assert a general claim about all agent-operated knowledge bases, but the evidence is drawn from one specific system (this KB) plus one independent practitioner report (Koylanai, 80+ files) and one commercial system (Fintool). The note does hedge later ("This isn't a files-forever position"), but the title and opening present the conclusion as established rather than as a position supported by limited evidence. The note's own Graphiti section demonstrates a genuine counterexample, which further suggests the title overstates.
  Recommendation: Consider softening the title to scope it to early-stage or single-author KBs, or add a qualifying sentence in the opening that acknowledges the evidence base is narrow. The body already does the nuanced work — the title and lead just need to match it.

- [Proportion mismatch] The core claim is "premature schema commitment" — the note's own framing elevates this as "the deeper reason" beyond the practical arguments. Yet the "Premature schema commitment" section (~150 words of original argument) is shorter than the "Where the trade-off tips: Graphiti" section (~200 words) and roughly equal to the opening bullet list (~130 words of practical arguments that the note itself calls secondary). The load-bearing argument gets the least development.
  Recommendation: Expand the "Premature schema commitment" section. The constrain/relax cycle connection is gestured at in one sentence but could carry more weight — e.g., concrete examples of schema commitments that turned out wrong, or a comparison of the cost of a file reorganization vs. a database migration.

INFO:
- [Orphan references] "11-nines durability" appears in the Relevant Notes section describing Fintool/S3. This is a specific technical claim (99.999999999% durability) attributed to a source. Since it appears only in the link annotation and the source is cited, it is not strictly orphaned, but a reader encountering it has no way to evaluate it without following the link. Worth checking whether this level of specificity in a link annotation is doing useful work or is just noise.

CLEAN:
- [Source residue] The note claims to be about agent-operated knowledge bases generally. The vocabulary ("DDL," "migration," "semantic search," "qmd," "frontmatter," "git") is domain-appropriate — these are all storage/infrastructure terms that match the note's subject. No leaked framing from an unrelated source domain was detected. The Koylanai and Graphiti references are explicitly framed as external examples.

- [Pseudo-formalism] No formal notation, equations, or symbolic apparatus is present. The note argues entirely in prose and structured lists. Clean.

- [Unbridged cross-domain evidence] The evidence sources are all within the same domain (knowledge-base architecture, agent tooling). Koylanai is a practitioner in the same space, Graphiti is a knowledge-graph system, Fintool is a production system with derived indexes. No cross-domain transfer requiring a bridge was detected.

- [Redundant restatement] Each section opens with its own contribution. The "Premature schema commitment" section does reference the prior section ("The practical arguments above are real, but there's a deeper reason"), but this is a one-sentence pivot, not a restatement. The Graphiti section similarly opens with its own framing rather than re-explaining prior material. Clean.

- [Anthropomorphic framing] The note discusses agents in terms of tool access ("Agents use Read/Write/Grep") rather than mental states. No problematic anthropomorphic language detected. Clean.

Overall: 2 warnings, 1 info
===
