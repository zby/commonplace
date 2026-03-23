=== PROSE REVIEW: instructions-are-skills-without-automatic-routing.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The note presents its framework for the instruction/skill distinction as established fact throughout, using assertive language ("Instructions are not notes," "The directory is the type signal," "These constraints are why instructions don't belong in kb/notes/"). This is the note's own construction — a design rationale for this specific knowledge base — not a finding from an external source. The categorical tone ("Instructions are not notes. Notes are for reasoning... Instructions are for execution") reads as settled doctrine rather than a design choice this project made.
  Recommendation: Either flag the framing as a design decision ("In this system, instructions are...") or accept that the assertive voice is deliberate for a note that documents project architecture. If the latter, the seedling status should eventually graduate, since the prose already speaks with mature confidence.

- [Proportion mismatch] The core claim is in the title: instructions are skills without automatic routing. The section that most directly carries this claim — "How instructions differ from adjacent concepts" — is three short paragraphs (~90 words). Meanwhile, "Optimized for execution, not understanding" (~150 words) and "How instructions get created" (~100 words) develop secondary points at comparable or greater length. The routing distinction (the title's actual claim) gets less development than the execution-optimization distinction (a supporting property).
  Recommendation: Expand "How instructions differ from adjacent concepts" to develop the routing/discoverability distinction more fully — what exactly does "automatic routing" entail, what does its absence cost, and when is that cost acceptable? Alternatively, consider whether the title understates the note's actual scope, which is broader than just the routing distinction.

INFO:
- [Source residue] The note references specific platform paths (`.claude/skills/`, `.agents/skills/`, `$CODEX_HOME/skills`, `~/.codex/skills`) in the "Platform independence" section. These are concrete implementation details from specific agent runtimes. For a note that frames itself as a general conceptual distinction between instructions and skills, the platform-specific paths are notably concrete. They don't break the argument, but they anchor a conceptual note to particular tools that may change.
  Recommendation: Consider whether the platform paths belong in a separate implementation note or whether they should be framed more explicitly as current examples ("In Claude Code, for instance, skills are discovered from...") — which the note partially does already for Claude Code but not for Codex.

CLEAN:
- [Pseudo-formalism] No formal notation, variables, or equations present. The note uses prose throughout. Clean.
- [Orphan references] No specific figures, data points, or empirical claims appear without sourcing. The note makes design-reasoning claims, not empirical ones. Clean.
- [Unbridged cross-domain evidence] The note stays within the domain of agent-operated knowledge bases throughout. No cross-domain evidence is cited. Clean.
- [Redundant restatement] Each section opens with new material. The "How instructions differ from adjacent concepts" section revisits the skill/instruction distinction but adds new dimensions (ad hoc vs. reusable, routing vs. procedure). No section merely restates a prior section's conclusion. Clean.
- [Anthropomorphic framing] The note uses "the agent reading an instruction" and "the agent won't sense this on its own," which attribute reading and sensing to agents. However, these are appropriate descriptions of agent behavior in this knowledge base's vocabulary — agents do read documents and lack certain detection capabilities. The language is precise for the domain rather than misleadingly anthropomorphic. Clean.

Overall: 2 warnings, 1 info
===
