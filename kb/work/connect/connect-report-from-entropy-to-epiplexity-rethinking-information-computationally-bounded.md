# Connection Report: From Entropy to Epiplexity: Rethinking Information for Computationally Bounded Intelligence

**Source:** [from-entropy-to-epiplexity-rethinking-information-computationally-bounded](kb/sources/from-entropy-to-epiplexity-rethinking-information-computationally-bounded.md)
**Date:** 2026-03-09
**Depth:** standard

## Context

This is a source snapshot (raw academic paper capture). It already has:
- An ingest file ([from-entropy-to-epiplexity-rethinking-information-computationally-bounded.ingest.md](kb/sources/from-entropy-to-epiplexity-rethinking-information-computationally-bounded.ingest.md)) with 7 identified connections
- A synthesis note written from the ingest: [information-value-is-observer-relative-because-extraction-requires-computation](kb/notes/information-value-is-observer-relative-because-extraction-requires-computation.md)

The source snapshot itself has no outbound links. The connections below assess what should link TO or FROM this source, distinguishing from what the ingest already captures.

## Discovery Trace

**Index scan:**
- Read kb/notes/index.md (148 entries) -- flagged 10 candidates based on descriptions:
  - [information-value-is-observer-relative-because-extraction-requires-computation](kb/notes/information-value-is-observer-relative-because-extraction-requires-computation.md) -- direct synthesis from this paper
  - [bitter-lesson-boundary](kb/notes/bitter-lesson-boundary.md) -- computational bounds determining what structures survive
  - [codification-and-relaxing-navigate-the-bitter-lesson-boundary](kb/notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) -- navigating extractable structure
  - [distillation](kb/notes/distillation.md) -- targeted extraction = bounded information extraction
  - [context-efficiency-is-the-central-design-concern-in-agent-systems](kb/notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) -- bounded context as resource
  - [structure-activates-higher-quality-training-distributions](kb/notes/structure-activates-higher-quality-training-distributions.md) -- structure affecting learning outcomes
  - [discovery-is-seeing-the-particular-as-an-instance-of-the-general](kb/notes/discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) -- recognition cost hierarchy
  - [learning-is-not-only-about-generality](kb/notes/learning-is-not-only-about-generality.md) -- capacity decomposition
  - [first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit](kb/notes/first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md) -- explanatory reach
  - [agent-capability-reduces-to-selection-quality-over-bounded-context](kb/notes/agent-capability-reduces-to-selection-quality-over-bounded-context.md) -- bounded observer in selection

**Topic indexes:**
- Read [learning-theory](kb/notes/learning-theory.md) -- confirmed the "Information & Bounded Observers" section already lists the synthesis note; no additional candidates beyond index scan

**Semantic search:** (via qmd)
- query "computationally bounded observer information structure extraction epiplexity" in notes --
  - [information-value-is-observer-relative](kb/notes/information-value-is-observer-relative-because-extraction-requires-computation.md) (93%) -- already known, direct synthesis
  - [agent-capability-reduces-to-selection-quality](kb/notes/agent-capability-reduces-to-selection-quality-over-bounded-context.md) (56%) -- framing matters for bounded observers, uses observer-relative concept
  - [discovery-is-seeing-the-particular](kb/notes/discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) (43%) -- recognition cost = computational bound
  - [symbolic-scheduling-over-bounded-llm-calls](kb/notes/symbolic-scheduling-over-bounded-llm-calls-is-the-right-model-for-agent-orchestration.md) (38%) -- bounded context model, materialised intermediates
  - [learning-theory](kb/notes/learning-theory.md) (37%) -- the index itself
  - [constraining-and-distillation-both-trade-generality](kb/notes/constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md) (35%) -- trade-off mechanics
  - Remaining hits below 35% -- surface overlap only, skipped

- query "computationally bounded observer information structure extraction epiplexity" in sources --
  - [from-entropy-to-epiplexity ingest](kb/sources/from-entropy-to-epiplexity-rethinking-information-computationally-bounded.ingest.md) (93%) -- self-reference
  - [from-entropy-to-epiplexity snapshot](kb/sources/from-entropy-to-epiplexity-rethinking-information-computationally-bounded.md) (56%) -- target itself
  - [induction-bias-sequence-models ingest](kb/sources/induction-bias-sequence-models-ebrahimi-2026.ingest.md) (43%) -- architectures as computational bounds
  - Remaining hits below 35% -- skipped

**Keyword search:**
- grep "epiplexity" in kb/ -- found 6 files (all already known: the source pair, the ingest, the synthesis note, discovery note, induction bias ingest, sources index)
- grep "bounded observer|computationally bounded" -- found 8 files, all already in candidate list
- grep "minimum description length|MDL|Kolmogorov complexity" -- only found in the source pair itself; no other KB content uses these terms
- grep "synthetic data|data ordering|curriculum" -- found induction bias ingest, AgeMem ingest, memory management note, agent-statelessness note, and the source pair; no new candidates

## Connections Found

### Already established connections (via ingest and synthesis note)

The ingest file already identifies connections to 7 notes, and the synthesis note (`information-value-is-observer-relative`) links to 4 of those plus the ingest itself. The following connections are already captured through the ingest:

1. [information-value-is-observer-relative-because-extraction-requires-computation](kb/notes/information-value-is-observer-relative-because-extraction-requires-computation.md) -- the synthesis note written from this source; links back to the ingest
2. [context-efficiency-is-the-central-design-concern-in-agent-systems](kb/notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) -- via ingest connection #1
3. [learning-is-not-only-about-generality](kb/notes/learning-is-not-only-about-generality.md) -- via ingest connection #2
4. [distillation](kb/notes/distillation.md) -- via ingest connection #3; also links to synthesis note
5. [bitter-lesson-boundary](kb/notes/bitter-lesson-boundary.md) -- via ingest connection #4
6. [discovery-is-seeing-the-particular-as-an-instance-of-the-general](kb/notes/discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) -- via ingest connection #5; also links to synthesis note
7. [structure-activates-higher-quality-training-distributions](kb/notes/structure-activates-higher-quality-training-distributions.md) -- via ingest connection #6
8. [induction-bias-sequence-models-ebrahimi-2026](kb/sources/induction-bias-sequence-models-ebrahimi-2026.md) -- via ingest source-to-source connection

### New connections (not yet captured)

- [agent-capability-reduces-to-selection-quality-over-bounded-context](kb/notes/agent-capability-reduces-to-selection-quality-over-bounded-context.md) -- **grounds**: The paper's core insight (same data, different extractable structure depending on computational budget) directly grounds the agent-capability note's claim that "framing matters, not just selection" -- the same knowledge presented differently has different value to a bounded observer. The note already references the synthesis note, but the paper itself provides the formal framework (time-bounded MDL) that makes this claim precise: a bounded agent's extraction capacity determines what's worth including *and how*. The paper's data ordering paradox (left-to-right text outperforms reverse) is a concrete instance of the select function's framing problem.

- [codification-and-relaxing-navigate-the-bitter-lesson-boundary](kb/notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) -- **extends**: The ingest connection to bitter-lesson-boundary is captured, but the codification/relaxing note adds a distinct angle. Epiplexity predicts when codification bets are safe: a component with low epiplexity (structure already fully captured) is safe to codify; one with high epiplexity (hidden structure a more powerful observer could extract) is a relaxing candidate. The paper's CSPRNG result (max entropy, zero epiplexity) is the extreme case: a component with no extractable structure at all, permanently in the arithmetic regime.

- [constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost](kb/notes/constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md) -- **grounds**: The paper provides a formal measure for the generality being traded. When constraining constrains the interpretation space, it reduces the computational budget needed to extract structure (lowering epiplexity for the constrained observer). The trade-off is quantifiable: more constraint = lower epiplexity needed = faster extraction, at the cost of excluding structure that a less-constrained observer could reach.

- [oracle-strength-spectrum](kb/notes/oracle-strength-spectrum.md) -- **complements**: Oracle strength determines how cheaply you can *verify* correctness; epiplexity determines how much *structure* a bounded observer can *extract*. These are distinct but interacting dimensions. A problem with high epiplexity and a hard oracle (much hidden structure, but verifiable when found) is the best candidate for scaling. A problem with high epiplexity and no oracle is the worst -- hidden structure exists but you can't tell when you've found it.

**Bidirectional candidates** (reverse link also worth adding):
- [agent-capability-reduces-to-selection-quality-over-bounded-context](kb/notes/agent-capability-reduces-to-selection-quality-over-bounded-context.md) <-> source -- the note already cites the synthesis note but would benefit from citing the primary source for the formal framework
- [codification-and-relaxing-navigate-the-bitter-lesson-boundary](kb/notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) <-> source -- the prediction about codification safety is a new argument not in the ingest

## Rejected Candidates

- [symbolic-scheduling-over-bounded-llm-calls-is-the-right-model-for-agent-orchestration](kb/notes/symbolic-scheduling-over-bounded-llm-calls-is-the-right-model-for-agent-orchestration.md) -- The bounded-context model is relevant but the connection is indirect: the scheduling note is about orchestration mechanics, not information theory. The connection to bounded observers is already captured through agent-capability-reduces-to-selection-quality, which is the note that bridges the formal model to practical agent architecture. Adding a direct link from the scheduling note to the epiplexity paper would add no navigational value beyond what the existing chain provides.
- [first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit](kb/notes/first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md) -- The note already links to the synthesis note with relationship "complements: reach means the explanation makes structure accessible to observers in multiple contexts." The source paper adds nothing beyond what the synthesis note captures for this connection. The relationship is genuinely mediated through the synthesis.
- [learning-is-not-only-about-generality](kb/notes/learning-is-not-only-about-generality.md) -- Already connected via ingest. The source snapshot would not add value beyond the ingest link.

## Index Membership

- [learning-theory](kb/notes/learning-theory.md) -- The source is already referenced in the "Reference material" section of learning-theory through its ingest. No change needed.
- Already represented through: ingest file listed in sources/index.md; synthesis note listed in learning-theory index

## Synthesis Opportunities

The ingest already flagged and executed the primary synthesis opportunity: the note "Information value is observer-relative because extraction requires computation" was written to unify four threads (context efficiency, distillation, discovery, bitter lesson boundary) under the epiplexity framework.

A **second-order synthesis** remains unflagged: the epiplexity paper plus the induction bias paper together suggest a note titled something like "Architectural constraints are a form of observer-dependent structure extraction." The induction bias ingest flagged this as "Architectural constraints as a form of constraining" but the epiplexity framing adds precision: different architectures (transformer vs RNN) are different computational bounds extracting different epiplexity from the same data. The kappa metric (sharing factor) measures whether the architecture amortizes learning across problem variations -- which is whether the architecture can extract shared structure. This would connect learning-theory's bounded-observer subsection to the bitter-lesson-boundary more tightly.

## Flags

- The source snapshot has no outbound links. This is expected for source snapshots (they are raw captures), but the ingest file serves as the connection hub. No structural issue.
- The ingest's "Recommended Next Action" (write the observer-relative synthesis note) has been completed.
- The ingest identified 7 connections, but only some have been made bidirectional. Several notes that the ingest recommends connecting to (bitter-lesson-boundary, context-efficiency, structure-activates-higher-quality-training-distributions, learning-is-not-only-about-generality) do not yet link back to either the source or the ingest. This is tracked in the ingest itself.
