# Connection Report: Codification

**Source:** [codification](kb/notes/codification.md) (test copy: kb/work/connect-refactoring/test-codification-intact.md)
**Date:** 2026-03-03
**Depth:** standard

**Note:** This is a test run against a note that already has a Relevant Notes footer with five connections. The report evaluates whether additional connections exist beyond those already present, and documents the existing links.

## Discovery Trace

**Index exploration:**
- Read [learning-theory](kb/notes/learning-theory-index.md) — the note's area index. Found the note listed under Constraining section with context: "codification is the far end where the medium itself changes from natural language to executable code." Candidates from same section: [storing-llm-outputs-is-constraining](kb/notes/storing-llm-outputs-is-constraining.md), [constraining-during-deployment-is-continuous-learning](kb/notes/constraining-during-deployment-is-continuous-learning.md), [spec-mining-as-codification](kb/notes/spec-mining-as-codification.md) (already linked). Candidates from other sections: [constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost](kb/notes/constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md), [bitter-lesson-boundary](kb/notes/bitter-lesson-boundary.md), [unified-calling-conventions-enable-bidirectional-refactoring](kb/notes/unified-calling-conventions-enable-bidirectional-refactoring.md), [inspectable-substrate-not-supervision-defeats-the-blackbox-problem](kb/notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md), [learning-is-not-only-about-generality](kb/notes/learning-is-not-only-about-generality.md)
- Read [kb-design](kb/notes/kb-design-index.md) — secondary index. Found codification mentioned in: [methodology-enforcement-is-constraining](kb/notes/methodology-enforcement-is-constraining.md) (methodology maturation as the same gradient), [skills-derive-from-methodology-through-distillation](kb/notes/skills-derive-from-methodology-through-distillation.md) (distinguishes distillation from codification)
- Followed links from [unified-calling-conventions-enable-bidirectional-refactoring](kb/notes/unified-calling-conventions-enable-bidirectional-refactoring.md) — this note already links to codification.md and develops the architectural consequence

**Semantic search:** qmd unavailable, grep-only discovery

**Keyword search:**
- grep "crystallis" in kb/notes/ — 44 files mention the term. High-signal candidates (not already linked): constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md, bitter-lesson-boundary.md, methodology-enforcement-is-constraining.md, unified-calling-conventions-enable-bidirectional-refactoring.md, inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md, agentic-systems-interpret-underspecified-instructions.md, learning-is-not-only-about-generality.md, skills-derive-from-methodology-through-distillation.md, deterministic-validation-should-be-a-script.md, operational-signals-that-a-component-is-a-relaxing-candidate.md
- grep "medium boundary|phase transition|deterministic" — 52 files. Confirmed overlap with above candidates.
- grep "verifiability gradient|verification regime" — found the same cluster of constraining/codification notes plus document-types-should-be-verifiable.md

**Inbound link scan:**
- grep "codification.md" — 25 files link to the canonical codification note. Most are already connected or are indexes/listings. Substantive inbound linkers not already in the note's footer: constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md, bitter-lesson-boundary.md, unified-calling-conventions-enable-bidirectional-refactoring.md, inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md, agentic-systems-interpret-underspecified-instructions.md, learning-is-not-only-about-generality.md

## Existing Connections (Already in Note)

The note already has five well-articulated connections in its Relevant Notes footer:

- [constraining](kb/notes/constraining.md) — **parent mechanism**: codification is the far end of the constraining spectrum
- [distillation](kb/notes/distillation.md) — **orthogonal mechanism**: targeted extraction; codification sometimes follows distillation
- [deploy-time-learning-the-missing-middle](kb/notes/deploy-time-learning-the-missing-middle.md) — **grounds**: the verifiability gradient across which codification sits at the far end
- [spec-mining-as-codification](kb/notes/spec-mining-as-codification.md) — **operational mechanism**: observe behavior, extract patterns, write deterministic code
- [oracle-strength-spectrum](kb/notes/oracle-strength-spectrum.md) — **determines**: what can codify (hard oracles enable it, weak oracles resist it)

All five pass the articulation test. All paths verified as existing files. These are the core structural connections and they are well-chosen.

## New Connections Found

- [constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost](kb/notes/constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md) — **extends**: that note explicitly uses codification as its central example of the largest compound gain ("Replacing an LLM validation check with a Python script..."). Codification is where the generality-vs-compound trade-off is most dramatic because the substrate itself changes. The codification note discusses the same trade-off ("the trade-off is generality: the code handles exactly what it handles, nothing more") but doesn't link to the note that formalises that trade-off. Strong bidirectional connection — the trade-off note already links to codification.

- [inspectable-substrate-not-supervision-defeats-the-blackbox-problem](kb/notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) — **enables**: codification produces the inspectable artifacts (deterministic code, tests, specs) that defeat the blackbox problem. Chollet's ML failure modes map to codification failure modes precisely because the output substrate is inspectable. The inspectable-substrate note already links to codification as its foundation. The reverse link is worth adding: codification matters not just for reliability/speed/cost but because it produces artifacts that are reviewable by any agent.

- [bitter-lesson-boundary](kb/notes/bitter-lesson-boundary.md) — **constrains**: the bitter lesson boundary determines when codification is permanent (calculator regime — spec IS the problem) vs when relaxing may eventually be needed (vision-feature regime — spec approximates the problem). The codification note discusses "when to codify" but frames it only in terms of oracle strength and pattern emergence. The bitter lesson boundary adds a deeper frame: even a well-codified component may need relaxing if it turns out to be a "vision feature" rather than a "calculator."

- [agentic-systems-interpret-underspecified-instructions](kb/notes/agentic-systems-interpret-underspecified-instructions.md) — **grounds**: this note provides the theoretical framework (semantic underspecification, execution indeterminism, spec-to-program projection) that codification resolves. Codification simultaneously resolves semantic underspecification (committing to one interpretation in precise code) and eliminates execution indeterminism (deterministic execution). The underspecified-instructions note already links to codification ("For the gradient of constraining techniques... see codification"). The reverse link would articulate the theoretical grounding.

**Bidirectional candidates** (reverse link also worth adding):
- [constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost](kb/notes/constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md) ↔ codification — already linked in that direction; adding the return link from codification completes the pair
- [inspectable-substrate-not-supervision-defeats-the-blackbox-problem](kb/notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) ↔ codification — already linked in that direction; return link adds the "why it matters beyond performance" dimension

## Rejected Candidates

- [methodology-enforcement-is-constraining](kb/notes/methodology-enforcement-is-constraining.md) — this note uses codification as an analogy for its own gradient (instruction → skill → hook → script parallels the constraining spectrum), but the connection is already mediated through the constraining note. Adding a direct link from codification to methodology-enforcement would be redundant — the codification note is about the mechanism in general, not about its application to methodology specifically.

- [skills-derive-from-methodology-through-distillation](kb/notes/skills-derive-from-methodology-through-distillation.md) — this note explicitly distinguishes distillation from codification. The codification note already links to distillation.md, which is the right place for that relationship. Linking to the skills-derive note would add a "not this" connection, which has low traversal value.

- [unified-calling-conventions-enable-bidirectional-refactoring](kb/notes/unified-calling-conventions-enable-bidirectional-refactoring.md) — while this note discusses how unified calling makes codification frictionless (a local operation), the relationship is about architectural enablement of codification, not about codification itself. An agent reading the codification note would not gain decision-relevant insight by following this link. The connection is better maintained from the unified-calling side (which already links to codification).

- [storing-llm-outputs-is-constraining](kb/notes/storing-llm-outputs-is-constraining.md) — describes the opposite end of the constraining spectrum (the simplest case). The connection is already captured by the shared parent (constraining.md). No direct link needed.

- [constraining-during-deployment-is-continuous-learning](kb/notes/constraining-during-deployment-is-continuous-learning.md) — mentions codification as one example of constraining during deployment, but the relationship is already captured through the constraining note.

- [learning-is-not-only-about-generality](kb/notes/learning-is-not-only-about-generality.md) — codification is cited as the clearest example of the generality-vs-compound trade-off, but the connection is better expressed through the trade-off note (constraining-and-distillation-both-trade). Adding a direct link would create a redundant path.

- [deterministic-validation-should-be-a-script](kb/notes/deterministic-validation-should-be-a-script.md) — an instance of codification in practice, but the codification note already provides its own examples (slug generator, CSV statistics, validate script). This is exemplification without new insight.

- [operational-signals-that-a-component-is-a-relaxing-candidate](kb/notes/operational-signals-that-a-component-is-a-relaxing-candidate.md) — about when to reverse codification. Relevant but the connection is better routed through bitter-lesson-boundary.md, which provides the theoretical frame for when relaxing is needed.

- [programming-practices-apply-to-prompting](kb/notes/programming-practices-apply-to-prompting.md) — discusses progressive compilation which relates to codification, but the connection is about practices that apply across the spectrum, not specifically about codification.

## Index Membership

- Already member of: [learning-theory](kb/notes/learning-theory-index.md) — listed under Constraining section with accurate context
- No additional index membership needed. The note is well-placed in the learning-theory index.

## Synthesis Opportunities

None detected. The codification note is well-integrated into the existing conceptual framework. The four new connections found fill specific gaps (the trade-off formalisation, the blackbox consequence, the bitter-lesson constraint, the theoretical grounding) without suggesting an uncaptured higher-order claim.

## Flags

- No split candidate — the note is focused on a single concept (codification as medium-boundary crossing) and its connections cluster coherently around that concept.
- No tensions detected.
- The note's existing five connections are well-chosen and well-articulated. The four new connections add dimensions the existing footer doesn't cover: the formalised trade-off, the inspectability consequence, the permanence boundary, and the theoretical grounding.

## Handling of Pre-existing Links

This note already had five connections in its Relevant Notes footer. The skill correctly:
1. Identified and documented all existing connections
2. Verified all existing link targets resolve to real files
3. Searched for connections beyond those already present
4. Found four genuine new connections that pass the articulation test
5. Did not duplicate or conflict with existing connections
6. Rejected candidates that would be redundant given existing connections (e.g., storing-llm-outputs via constraining.md)
