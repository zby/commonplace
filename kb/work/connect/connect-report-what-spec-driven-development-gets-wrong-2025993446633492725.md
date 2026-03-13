# Connection Report: What spec-driven development gets wrong

**Source:** [What spec-driven development gets wrong](../../sources/what-spec-driven-development-gets-wrong-2025993446633492725.md)
**Date:** 2026-03-10
**Depth:** standard

## Note Summary

An @augmentcode post arguing that spec-driven development (SDD) fails for the same reason all documentation-first initiatives fail: documents decay because maintenance is invisible, unrewarded work. The proposed fix: make the spec a bidirectional artifact that both humans and agents read/write. A coordinator agent drafts the spec from human intent, agents update it as they discover reality diverges from the plan, and the human reviews and can redirect at any point. The "junior engineer" analogy is the core metaphor: a good junior surfaces directional decisions ("I found an existing auth context, so I wired into that instead") without narrating every line. The key design challenge is update granularity -- too much and the spec becomes noise, too little and you're back to guessing.

## Discovery Trace

**Index scan:**
- Read kb/notes/index.md -- scanned all 145 entries. Flagged candidates:
  - [agentic-systems-interpret-underspecified-instructions](../../notes/agentic-systems-interpret-underspecified-instructions.md) -- directly about spec underspecification
  - [changing-requirements-conflate-genuine-change-with-disambiguation-failure](../../notes/changing-requirements-conflate-genuine-change-with-disambiguation-failure.md) -- about specs that change vs were always ambiguous
  - [deploy-time-learning-is-agile-for-human-ai-systems](../../notes/deploy-time-learning-is-agile-for-human-ai-systems.md) -- agile co-evolution of prose and code
  - [constraining](../../notes/constraining.md) -- specs as constraining artifacts
  - [codification](../../notes/codification.md) -- spec-to-code boundary
  - [storing-llm-outputs-is-constraining](../../notes/storing-llm-outputs-is-constraining.md) -- agent updates as constraining
  - [entropy-management-must-scale-with-generation-throughput](../../notes/entropy-management-must-scale-with-generation-throughput.md) -- maintenance matching generation
  - [inspectable-substrate-not-supervision-defeats-the-blackbox-problem](../../notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) -- shared spec as inspectable substrate
  - [deploy-time-learning-the-missing-middle](../../notes/deploy-time-learning-the-missing-middle.md) -- specs as durable adaptation artifacts
  - [legal-drafting-solves-the-same-problem-as-context-engineering](../../notes/legal-drafting-solves-the-same-problem-as-context-engineering.md) -- another domain solving spec maintenance
  - [spec-mining-as-codification](../../notes/spec-mining-as-codification.md) -- extracting deterministic specs from behavior
  - [methodology-enforcement-is-constraining](../../notes/methodology-enforcement-is-constraining.md) -- enforcement gradient for specs
  - [stale-indexes-are-worse-than-no-indexes](../../notes/stale-indexes-are-worse-than-no-indexes.md) -- staleness suppressing discovery
  - [active-campaign-understanding-needs-a-single-coherent-narrative-not-composed-notes](../../notes/active-campaign-understanding-needs-a-single-coherent-narrative-not-composed-notes.md) -- bidirectional rewriting of working documents
  - [related-systems/decapod](../../notes/related-systems/decapod.md) -- intent-before-mutation via spec artifacts

**Topic indexes:**
- Read [kb-design](../../notes/kb-design-index.md) -- not directly relevant (KB architecture, not SDD)
- Read [learning-theory](../../notes/learning-theory-index.md) -- confirmed several candidates already flagged
- Read [related-systems-index](../../notes/related-systems/related-systems-index.md) -- Decapod confirmed as strongest related-system connection

**Semantic search:** (via qmd)
- query "spec-driven development documentation decay bidirectional spec maintenance agent-updated plans" on notes -- top hits:
  - [quality-signals-for-kb-evaluation](../../notes/quality-signals-for-kb-evaluation.md) (88%) -- false positive; high score from query structure, not semantic match
  - [spec-mining-as-codification](../../notes/spec-mining-as-codification.md) (50%) -- genuine match, spec extraction from behavior
  - [related-systems/decapod](../../notes/related-systems/decapod.md) (43%) -- genuine match, intent codification
  - [entropy-management-must-scale-with-generation-throughput](../../notes/entropy-management-must-scale-with-generation-throughput.md) (36%) -- genuine match, maintenance throughput
  - [changing-requirements-conflate-genuine-change-with-disambiguation-failure](../../notes/changing-requirements-conflate-genuine-change-with-disambiguation-failure.md) (35%) -- genuine match, spec ambiguity
  - [deploy-time-learning-the-missing-middle](../../notes/deploy-time-learning-the-missing-middle.md) (32%) -- genuine match, durable adaptation artifacts

- query "documentation staleness living documents co-maintained artifacts human agent collaboration on specifications" on notes -- top hits:
  - [stale-indexes-are-worse-than-no-indexes](../../notes/stale-indexes-are-worse-than-no-indexes.md) (45%) -- genuine match, staleness dynamics
  - [entropy-management-must-scale-with-generation-throughput](../../notes/entropy-management-must-scale-with-generation-throughput.md) (46%) -- already flagged
  - [methodology-enforcement-is-constraining](../../notes/methodology-enforcement-is-constraining.md) (46%) -- genuine match, enforcement gradient
  - [storing-llm-outputs-is-constraining](../../notes/storing-llm-outputs-is-constraining.md) (39%) -- genuine match, artifact constraining

- query on sources -- top hits:
  - Self (93%) -- expected
  - [agent-behavioral-contracts-formal-specification-runtime-enforcement.ingest](../../sources/agent-behavioral-contracts-formal-specification-runtime-enforcement.ingest.md) (50%) -- contracts as specification enforcement
  - [harness-engineering-leveraging-codex-agent-first-world.ingest](../../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md) (32%) -- harness engineering as spec/constraint maintenance
  - [professional-software-developers-dont-vibe-they-control.ingest](../../sources/professional-software-developers-dont-vibe-they-control.ingest.md) (36%) -- developer control strategies as constraining

**Keyword search:**
- grep "spec-driven|SDD" -- found only the target source itself. No other notes reference SDD.
- grep "bidirectional.*(spec|document|artifact)" -- found only an unrelated mention in skills-derive-from-methodology-through-distillation.md.
- grep "documentation.*(decay|stale|maintenance)" -- found only the target source itself.

## Connections Found

### Strong connections

- [agentic-systems-interpret-underspecified-instructions](../../notes/agentic-systems-interpret-underspecified-instructions.md) — **grounds**: The Augment post is implicitly about underspecification -- the spec "Add a dark mode toggle..." admits multiple implementations, and the agent's update ("Found an existing theme context provider") is an interpretation choice being surfaced rather than silently committed. The entire SDD argument rests on the phenomenon this note formalizes: specs are projections, not compilations, and agents pick interpretations the spec doesn't uniquely determine.

- [changing-requirements-conflate-genuine-change-with-disambiguation-failure](../../notes/changing-requirements-conflate-genuine-change-with-disambiguation-failure.md) — **exemplifies**: The Augment post's dark mode example is a disambiguation failure surfacing mid-execution -- the human's spec assumed a new store, but the agent found an existing theme context provider. This is exactly "the requirements didn't change, the interpretation space was wider than the spec revealed." The bidirectional spec is a mechanism for catching disambiguation failures in real time rather than at iteration boundaries.

- [deploy-time-learning-is-agile-for-human-ai-systems](../../notes/deploy-time-learning-is-agile-for-human-ai-systems.md) — **exemplifies**: The Augment post describes the same co-evolution loop this note theorizes: prose spec and code co-evolve, with the spec updating as agents discover reality. The note argues deploy-time learning extends agile by recognizing some prose stays permanently load-bearing; the Augment post independently arrives at the same position -- the spec isn't temporary backlog waiting to become code, it's a persistent co-maintained artifact.

- [entropy-management-must-scale-with-generation-throughput](../../notes/entropy-management-must-scale-with-generation-throughput.md) — **extends**: The Augment post's core observation ("Every documentation-first initiative has failed because it asked developers to do continuous maintenance work nobody sees") is the entropy management problem stated for specs: spec entropy grows with code generation, and without proportional maintenance, the spec becomes noise. The bidirectional spec is Augment's answer to the throughput matching problem -- agents maintain the spec as a side effect of doing the work, so maintenance throughput automatically scales with generation throughput.

- [inspectable-substrate-not-supervision-defeats-the-blackbox-problem](../../notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) — **exemplifies**: The bidirectional spec IS an inspectable substrate. Agents write code AND update the plan, creating a plain-text artifact that any party (human or agent) can inspect, diff, and review. The Augment post's "the spec now reflects what was actually built, not what was originally planned" is the inspectable substrate thesis in a product context.

### Moderate connections

- [deploy-time-learning-the-missing-middle](../../notes/deploy-time-learning-the-missing-middle.md) — **exemplifies**: The bidirectional spec is a deploy-time learning artifact -- it persists across sessions, adapts through use, and sits at a specific point on the verifiability gradient (restructured prompt level -- human-reviewed, not automatically testable). The spec's update mechanism (agents write back findings) is accumulation; the human's review and revision is constraining.

- [constraining](../../notes/constraining.md) — **exemplifies**: The spec starts underspecified ("Add a dark mode toggle that respects system preferences") and gets progressively constrained through agent discovery and human approval. Each agent update narrows the interpretation space ("Found existing theme context provider, wired into that") by committing to a specific implementation choice. The spec is a constraining artifact that records which interpretations were chosen and why.

- [active-campaign-understanding-needs-a-single-coherent-narrative-not-composed-notes](../../notes/active-campaign-understanding-needs-a-single-coherent-narrative-not-composed-notes.md) — **extends**: The Augment spec shares key properties with the THEORY.MD pattern this note describes -- a single document that tracks current understanding, rewritten as understanding evolves, readable as present state rather than history. The difference: THEORY.MD is the human's working model; the Augment spec is a co-maintained artifact where agents also write. The Augment post extends the pattern by making the narrative bidirectional rather than human-authored.

- [related-systems/decapod](../../notes/related-systems/decapod.md) — **contrasts**: Both require intent codification before code (Decapod's scaffold generates spec artifacts, Augment's coordinator drafts a spec). But they diverge on spec lifecycle: Decapod treats the spec as a static input validated by proof-gating ("did you do what you said?"), while Augment treats it as a living document updated during execution ("the plan changed because reality diverged"). Decapod's spec is verified; Augment's spec is evolved. These are complementary strategies for different phases of confidence.

### Weaker but genuine connections

- [spec-mining-as-codification](../../notes/spec-mining-as-codification.md) — **contrasts**: Spec mining extracts deterministic rules from observed agent behavior (bottom-up, retrospective). The Augment spec captures agent-reported deviations from the plan as they happen (real-time, prospective). Both address the gap between planned and actual behavior, but from opposite temporal directions. If Augment specs accumulated across many tasks, the recurring deviation patterns would be candidates for spec mining.

- [stale-indexes-are-worse-than-no-indexes](../../notes/stale-indexes-are-worse-than-no-indexes.md) — **exemplifies**: The Augment post's central argument is a generalization of this note's claim. A stale spec is worse than no spec because agents execute it confidently. "A stale spec misleads agents that don't know any better. They'll execute a plan that no longer matches reality, confidently, and they won't flag that anything is wrong." This is the same mechanism as stale indexes suppressing search -- the authoritative artifact satisfies the need, preventing fallback to more current information.

- [harness-engineering-leveraging-codex-agent-first-world.ingest](../../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md) — **complements**: Lopopolo's harness engineering addresses the same problem space (agents generating code at scale) with a different strategy: constrain and verify rather than co-maintain specs. The harness approach (linters, structural tests, background cleanup) is constraining applied to the codebase directly; the Augment approach (bidirectional specs) is constraining applied to the plan. They could be complementary layers.

**Bidirectional candidates** (reverse link also worth adding):
- [changing-requirements-conflate-genuine-change-with-disambiguation-failure](../../notes/changing-requirements-conflate-genuine-change-with-disambiguation-failure.md) ↔ source — the Augment post provides a concrete mechanism (bidirectional spec) that addresses the disambiguation-failure problem the note identifies; worth linking from the note as a candidate solution approach.
- [entropy-management-must-scale-with-generation-throughput](../../notes/entropy-management-must-scale-with-generation-throughput.md) ↔ source — the bidirectional spec is a concrete architecture where maintenance throughput automatically matches generation throughput; worth linking as a design pattern that achieves the scaling the note argues for.

## Rejected Candidates

- [quality-signals-for-kb-evaluation](../../notes/quality-signals-for-kb-evaluation.md) — appeared as top qmd result (88%) but this was a false positive. The note is about KB quality metrics, not about spec maintenance or documentation decay. No genuine semantic connection.
- [legal-drafting-solves-the-same-problem-as-context-engineering](../../notes/legal-drafting-solves-the-same-problem-as-context-engineering.md) — both address specs in underspecified media, but the connection is too generic. The Augment post isn't about how to write better specs; it's about who maintains them and when. Legal drafting methodology doesn't address the maintenance problem.
- [codification](../../notes/codification.md) — the Augment post is about maintaining prose specs, not about crossing the medium boundary into code. The spec explicitly stays in natural language. No genuine codification connection.
- [methodology-enforcement-is-constraining](../../notes/methodology-enforcement-is-constraining.md) — the enforcement gradient is about methodology constraints, not about spec co-maintenance. The connection would be "specs are methodology" which is too vague.
- [storing-llm-outputs-is-constraining](../../notes/storing-llm-outputs-is-constraining.md) — the agent's spec update is technically a stored output, but this connection is trivially true of any agent-written artifact. No specific insight gained.
- [professional-software-developers-dont-vibe-they-control.ingest](../../sources/professional-software-developers-dont-vibe-they-control.ingest.md) — surface vocabulary overlap (developers, agents, control) but the paper studies developer behavior, not spec architecture. Different question.

## Index Membership

- [related-systems-index](../../notes/related-systems/related-systems-index.md) — The source describes Augment's "Intent" product, which is a related system. However, this is a single tweet-length post, not a system review. If a deeper review of Intent is done, it should be added to the related systems index. The source itself does not warrant index membership.
- [learning-theory](../../notes/learning-theory-index.md) — The source exemplifies deploy-time learning, constraining, and entropy management concepts but is a captured source, not a note. Sources are not typically added to topic indexes.

## Synthesis Opportunities

**Bidirectional artifact maintenance as a design pattern.** The Augment post describes bidirectional spec maintenance. The theorist pattern (active-campaign-understanding note) describes holistic narrative rewrite. Both are responses to the same problem: working documents that must stay current during active work. A synthesis note could argue that **any long-lived working document in an agent system must be co-maintained or it decays** -- and characterize the design space of co-maintenance strategies (bidirectional updates, holistic rewrite, background cleanup agents). Contributing notes: this source, [active-campaign-understanding](../../notes/active-campaign-understanding-needs-a-single-coherent-narrative-not-composed-notes.md), [entropy-management](../../notes/entropy-management-must-scale-with-generation-throughput.md), [stale-indexes](../../notes/stale-indexes-are-worse-than-no-indexes.md).

**Disambiguation-failure detection mechanisms.** The [changing-requirements](../../notes/changing-requirements-conflate-genuine-change-with-disambiguation-failure.md) note identifies the phenomenon (disambiguation failures masquerading as changing requirements). This source proposes a mechanism (agents report when reality diverges from the plan). A synthesis could map the detection mechanisms for disambiguation failures: short iterations (agile), bidirectional specs (Augment), proof-gating (Decapod), and ask which mechanisms detect which kinds of failures.

## Flags

- No split candidate (the source makes one coherent argument about bidirectional specs).
- Tension: [Decapod](../../notes/related-systems/decapod.md) treats specs as verified inputs; Augment treats specs as evolved outputs. Both are responses to spec maintenance, with different assumptions about when the plan can be trusted.
