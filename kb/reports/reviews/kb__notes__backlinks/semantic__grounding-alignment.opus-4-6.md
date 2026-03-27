---
note: kb/notes/backlinks.md
gate: semantic/grounding-alignment
---

The note makes four grounding claims checked below. Linked notes were read where available.

## `linking-theory.md` — "backlinks are a special case of link visibility; what makes a link worth following applies to inbound links too"

Read `linking-theory.md`. The note develops a theory of *outbound* link quality: links are decision points, and link quality is "the reduction of navigation uncertainty per unit of context consumed." Every example, practice, and prediction in that note concerns how an agent decides whether to *follow* an outbound link — typed relationships, claim titles, position encoding. Inbound links are not mentioned.

The backlinks note claims this theory extends to inbound visibility ("what makes a link worth following applies to inbound links too"). This is an inference, not something linking-theory.md states. The extension is plausible — if link quality is about decision-cost reduction, knowing who links to you could similarly reduce navigation uncertainty. But the target note does not make this move.

WARN: the Relevant Notes footer presents linking-theory.md as a foundation for the backlinks note ("backlinks are a special case of link visibility"), but linking-theory.md doesn't address inbound links or backlink visibility. The connection is the backlinks note's own extrapolation, not a claim grounded in the cited source. The relationship phrase overstates the scope of the cited note.

## `generate-instructions-at-build-time.md` — "related pattern: deterministic generation from structured data, the approach that option B would follow"

Read `generate-instructions-at-build-time.md`. That note is about generating instruction/skill files from templates at setup time, so LLMs read literal paths rather than substituting runtime variables. The principle invoked (deterministic generation, pay flexibility cost once) is shared with option B's approach to generating backlink footer sections from a link scan.

The analogy holds at the abstract level but the domains differ: template-to-instruction generation vs. link-scan-to-footer generation. The former resolves configuration (paths, repo locations); the latter produces content derived from graph data. Neither note depends on the other.

INFO: the connection is a pattern analogy, not a direct grounding. The cited note doesn't discuss note-footer generation or link data. The relationship label "related pattern" is accurate but the Relevant Notes phrase implies the approach is closer to B than the actual domain gap warrants.

## Ingest report factual claim — "koylanai-personal-brain-os.ingest.md links to storing-llm-outputs-is-constraining.md"

This is a concrete factual claim used to illustrate use case 2 (source-to-theory bridge). It's cited inline as a real example rather than a hypothetical. The claim is verifiable by reading the ingest report. Not read in this pass; flagging for verification.

INFO: the example functions as an existence proof for use case 2. If the link exists in the ingest report, the grounding is sound. If not, use case 2 loses its only concrete illustration and becomes purely hypothetical.

## `/connect skill` — "already has a 'Bidirectional Check' gate, but it's applied sporadically"

"Applied sporadically" is a behavioral claim about agent practice, not grounded in any cited note or data. The existence of the gate is checkable; whether it's applied sporadically is not grounded by reference.

INFO: "applied sporadically" is asserted without evidence. It may be accurate but reads as a rhetorical qualifier supporting option C's weakness argument rather than a documented observation.

## Domain coverage

The note's central causal claim — that inbound link invisibility causes agents to misread notes as peripheral when they're actually foundational — is plausible but not grounded in any cited evidence. No agent trace data, no examples of actual misreads, no citation to observations about how agents navigate. The use cases are motivated by reasoning from first principles, not from observed failures.

INFO: the problem framing ("agents have to think to run grep") is stated as fact but not grounded. The note is speculative (status: speculative) so this is appropriate to its epistemic level, but the reasoning would benefit from at least one documented instance where inbound invisibility caused a concrete problem.
