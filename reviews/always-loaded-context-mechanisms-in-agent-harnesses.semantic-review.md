<!-- REVIEW-METADATA
note-path: kb/notes/always-loaded-context-mechanisms-in-agent-harnesses.md
last-full-review-note-sha: e6c74431300a233929262852f34bc4b407c3d5d6
last-full-review-note-commit: 6e2e74d37a330987366c2d846513e4b52f97a11f
last-full-review-at: 2026-03-23T21:56:08+01:00
last-accepted-note-sha: e6c74431300a233929262852f34bc4b407c3d5d6
last-accepted-note-commit: 6e2e74d37a330987366c2d846513e4b52f97a11f
last-accepted-at: 2026-03-23T21:56:08+01:00
last-acceptance-kind: full-review
review-type: semantic-review
-->
=== SEMANTIC REVIEW: always-loaded-context-mechanisms-in-agent-harnesses.md ===

Claims identified: 14

1. [Scope] The note catalogues "user-facing mechanisms — the surfaces that project authors and tool developers control" for always-loaded context, explicitly excluding platform-injected context (safety preambles, behavioral guidelines, tool schemas).
2. [Enumeration] There are four always-loaded context surfaces: system prompt files, capability descriptions, memory, configuration injection.
3. [Enumeration] System prompt files carry five distinct kinds of content: constraints, routing rules, definitions, domain scope, operational recipes.
4. [Causal] "What unifies these is not that they're all directives... but that the agent needs them available before it knows what task it's working on."
5. [Attribution] The OSS study found build commands in 40 repos and testing instructions in 25.
6. [Attribution] Lopopolo maintains a 100-line AGENTS.md as "a map with pointers to deeper sources of truth" for a 1M LOC agent-generated codebase.
7. [Attribution] AGENTS.md files average 142 lines (SD=231), with 50% never updated after creation; CLAUDE.md files average 287 lines (SD=112).
8. [Definition] Capability descriptions are always *listed* but their bodies load on demand — "the key structural difference from system prompt files."
9. [Enumeration] Three memory write policies: human-governed agent writes, fully agent-managed, external pipeline.
10. [Claim] Configuration injection is "partial evaluation applied to instructions."
11. [Claim] "All four surfaces compete for the same finite context window."
12. [Claim] "The ambient/on-demand distinction is the load-bearing one" — system prompt files, memory, and resolved configuration are ambient; capability descriptions are "the one surface where detailed content loads on demand."
13. [Claim] Write cadences differ across surfaces (weeks/months for system prompts, days/weeks for capabilities, continuously for memory, rarely for configuration).
14. [Claim] "Volatile project state is a gap" — it doesn't fit cleanly on any surface.

WARN:
- [Completeness] The four-surface enumeration excludes conversation/session history as an always-loaded mechanism. In harnesses like Claude Code and Cursor, the active conversation is always present in context and competes for the same token budget. The note scopes itself to "user-facing mechanisms... that project authors and tool developers control," which could exclude conversation history since it is generated rather than authored. But some harnesses allow users to configure how much history is retained (e.g., conversation pruning settings, max turns), making it partially user-controlled. If the exclusion is intentional, the note would benefit from stating it explicitly, as readers surveying "what occupies the context window" will notice the absence.
- [Completeness] The four-surface taxonomy omits project file context that some harnesses auto-include. Cursor, for example, automatically indexes and injects relevant code snippets from the project into the context based on the current file or query — this is always-loaded in the sense that the user configures the indexing scope but doesn't manually trigger injection per session. This mechanism sits awkwardly between "configuration injection" (it is configured once) and "capability descriptions" (it loads content on demand based on relevance). It may fall outside the note's stated scope of "user-facing mechanisms" if interpreted as platform behavior, but it is user-configurable (which repos to index, which files to exclude), making the boundary fuzzy.
- [Grounding] The note says "CLAUDE.md files average 287 lines (SD=112)" citing the OSS study. The OSS study ingest notes that "Copilot instructions 310 lines" but does not explicitly state CLAUDE.md averages at 287 lines (SD=112) in the ingest summary. The ingest does say "AGENTS.md files average 142 lines (SD=231)" which the note also cites. The CLAUDE.md statistic may come from the original paper rather than the ingest, but verifying this against the source PDF would be needed. If the note is attributing a figure the ingest does not contain, the attribution may be accurate (from the full paper) but cannot be confirmed from the linked source alone.

INFO:
- [Completeness] The three memory write policies (human-governed agent writes, fully agent-managed, external pipeline) do not explicitly cover a fourth pattern: human-only memory (no agent writes at all). Some teams use MEMORY.md or equivalent files purely as human-authored context that happens to live in the memory surface — essentially a second system prompt file. The note acknowledges that "users can also write memory entries directly," blurring the boundary, but the three named policies all assume the agent participates in writing. A purely human-written memory file would collapse the distinction between memory and system prompt files, which may be the note's point ("indistinguishable from system prompt content except by the expectation that it will also accumulate agent-written entries"), but the policy taxonomy does not name this edge case.
- [Completeness] The five content categories for system prompt files (constraints, routing rules, definitions, domain scope, operational recipes) could face a boundary case with "persona/tone instructions" — directives like "respond concisely" or "use formal tone" that appear in many real-world system prompt files. These are not constraints in the "do/don't" sense, not routing rules, not definitions, not domain scope, and not operational recipes. They could be forced into "constraints" but the fit is strained since they shape style rather than guard against failure. The OSS study's 14 content categories include items like "contribution guidelines" that do not map cleanly to the five either, suggesting the five categories are a simplification of a richer space.
- [Boundary] The "ambient/on-demand distinction is the load-bearing one" claim (claim 12) says capability descriptions are "the one surface where detailed content loads on demand." But configuration injection is described as resolved "at build time or at session start" — which means the detailed configuration values are not ambient in the same sense as system prompt files and memory (present every session as authored text). They are pre-resolved and then ambient. This is a minor distinction but it means the ambient/on-demand axis actually has three positions: always-present-as-authored (system prompts, memory), resolved-then-present (configuration), and listed-but-body-on-demand (capabilities). The note's binary framing elides this middle position.
- [Internal consistency] The Design Principles section states "capability descriptions are scanned as a list every session but their bodies load on demand." Earlier, the Capability Descriptions section says "capability descriptions are always *listed* but their bodies load on demand." These are consistent with each other. However, the Design Principles section also says "The ambient/on-demand distinction is the load-bearing one" and places capability descriptions on the on-demand side, while the descriptions themselves are ambient (always listed). The note is aware of this dual nature ("always listed but bodies load on demand") but the Design Principles characterization of capabilities as the on-demand surface slightly oversimplifies what the note itself established earlier.

PASS:
- [Grounding] The attribution of the control-plane model's three layers (invariants, routing, escalation boundaries) accurately reflects the linked note `agents-md-should-be-organized-as-a-control-plane.md`, which defines exactly these three layers with matching descriptions.
- [Grounding] The claim that the control-plane model "explicitly excludes volatile state from system prompt files" is confirmed by the exclusion rules section of the linked note, which lists "volatile project state (active campaign details, temporary decisions)" as content that should stay out of AGENTS.md.
- [Grounding] The characterization of configuration injection as "partial evaluation applied to instructions" correctly reflects the linked `frontloading-spares-execution-context.md` note, which develops the partial evaluation framing in detail and explicitly describes template variable expansion and pre-computation of known values as PE applied to LLM instructions.
- [Grounding] The reference to the loading hierarchy from `instruction-specificity-should-match-loading-frequency.md` accurately reflects that note's four-tier model (CLAUDE.md -> skill descriptions -> skill bodies -> task-specific docs) and its core principle that always-loaded context must be slim.
- [Grounding] The AGENTS.md 142-line average (SD=231) and 50% stagnation rate are accurately attributed to the OSS study, which reports these figures in its summary.
- [Grounding] The Lopopolo 100-line AGENTS.md characterization aligns with the OSS study ingest's reference to the Harness Engineering source.
- [Internal consistency] The note's scoping exclusion (platform-injected context is out of scope) is maintained throughout — no section drifts into discussing safety preambles, behavioral guidelines, or tool schemas as part of the taxonomy.
- [Internal consistency] The "volatile project state is a gap" analysis is internally consistent — it systematically walks through each surface, explains why volatile state does not fit, and arrives at a coherent conclusion that system prompt files are "the least bad option." No section contradicts this.
- [Internal consistency] The tension between practitioner behavior (embedding operational recipes) and the control-plane model's recommendation (route them to on-demand documents) is flagged honestly as "real and unresolved" rather than resolved in favor of either side. This prevents a consistency problem that would arise from asserting both positions.

Overall: 3 warnings, 4 info
===
