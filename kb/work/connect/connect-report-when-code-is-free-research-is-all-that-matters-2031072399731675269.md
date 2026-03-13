# Connection Report: When code is free, research is all that matters

**Source:** [When code is free, research is all that matters](../../sources/when-code-is-free-research-is-all-that-matters-2031072399731675269.md)
**Date:** 2026-03-10
**Depth:** standard

## Summary of Source

Amy Tam argues that as AI makes code generation free, the differentiator shifts from engineering (execution against a known spec) to research (deciding what's worth building when the answer might be "nothing"). The core mechanism: engineering has built-in feedback signals (tests, benchmarks, specs) that enable automation via RL, while research lacks ground truth — you often can't know whether a solution exists, let alone verify one. "Research taste" — the ability to select which problems are worth pursuing from a vast space — is the scarce, hard-to-automate, portable skill. Current AI tools (e.g., Karpathy's autoresearch) automate execution (hyperparameter sweeps) but not problem selection.

Key concepts: research taste as problem selection, ground truth / feedback signals as the automation prerequisite, the halting problem analogy for research, taste as portable across domains, the coin-flipping metaphor for choosing which problems to work on.

## Discovery Trace

**Index scan:**
- Read kb/notes/index.md — scanned all 144 entries. Flagged candidates:
  - [oracle-strength-spectrum](../../notes/oracle-strength-spectrum.md) — oracle strength IS the feedback signal question Tam describes
  - [the-augmentation-automation-boundary-is-discrimination-not-accuracy](../../notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) — automation boundary depends on verification capability
  - [bitter-lesson-boundary](../../notes/bitter-lesson-boundary.md) — when scale helps vs when it doesn't; research taste may be on the "doesn't scale" side
  - [automating-kb-learning-is-an-open-problem](../../notes/automating-kb-learning-is-an-open-problem.md) — same problem: automating judgment-heavy operations requires oracles we can't manufacture
  - [first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit](../../notes/first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md) — taste = selecting for explanatory reach
  - [information-value-is-observer-relative-because-extraction-requires-computation](../../notes/information-value-is-observer-relative-because-extraction-requires-computation.md) — bounded observer framework connects to taste as extraction ability
  - [discovery-is-seeing-the-particular-as-an-instance-of-the-general](../../notes/discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) — discovery mechanism; research taste identifies general patterns
  - [learning-is-not-only-about-generality](../../notes/learning-is-not-only-about-generality.md) — accumulation and reach; taste is high-reach knowledge
  - [memory-management-policy-is-learnable-but-oracle-dependent](../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) — oracle dependency for learning
  - [bounded-context-orchestration-model](../../notes/bounded-context-orchestration-model.md) — selection problem analogous to research problem selection
  - [codification-and-relaxing-navigate-the-bitter-lesson-boundary](../../notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) — navigating when scale helps vs not
  - [claw-learning-is-broader-than-retrieval](../../notes/claw-learning-is-broader-than-retrieval.md) — learning beyond retrieval

**Topic indexes:**
- Read [learning-theory](../../notes/learning-theory-index.md) — confirmed oracle-strength-spectrum, bitter-lesson-boundary, memory-management-policy, first-principles-reach, discovery, information-value as relevant cluster. No additional candidates beyond index scan.

**Semantic search (via qmd):**
- query "research taste problem selection automation oracle feedback signal what is worth building" on notes:
  - constraining-and-distillation-both-trade-generality... (88%) — high score but surface match; the generality/reliability trade-off is tangential
  - the-augmentation-automation-boundary... (53%) — confirmed candidate
  - oracle-strength-spectrum (39%) — confirmed candidate
  - quality-signals-for-kb-evaluation (36%) — weak, different domain
  - methodology-enforcement-is-constraining (35%) — weak, different domain
  - claw-learning-is-broader-than-retrieval (34%) — confirmed candidate
- query "research taste problem selection automation oracle feedback signal what is worth building" on sources:
  - when-code-is-free... (93%) — the source itself
  - professional-software-developers-dont-vibe-they-control (50%) — moderate: maps task suitability to oracle strength, relevant as contrast
  - towards-a-science-of-ai-agent-reliability (38%) — relevant via discrimination/calibration findings
  - creative-thinking-by-claude-shannon (33%) — Shannon's problem-solving operators as concrete instance of "research taste"
- query "halting problem ground truth verification engineering vs research automation boundary" on notes:
  - methodology-enforcement-is-constraining (88%) — surface match on verification terms, not semantically relevant
  - bitter-lesson-boundary (37%) — confirmed candidate
  - the-augmentation-automation-boundary... (35%) — confirmed candidate

**Keyword search:**
- grep "oracle.*(strength|hard|soft)|bitter.lesson|ground.truth|feedback.*(signal|loop)" — 36 files, mostly already in candidates
- grep "taste|research.*automat|problem selection|what.*worth" — 24 files; confirmed creative-thinking-by-claude-shannon source as relevant; no new notes found

## Connections Found

- [oracle-strength-spectrum](../../notes/oracle-strength-spectrum.md) — **exemplifies**: Tam's central claim that research lacks ground truth while engineering has test suites/benchmarks IS the oracle-strength spectrum applied to the research-vs-engineering distinction. Engineering tasks sit at the hard-oracle end (tests, specs, exact verification), research sits at the no-oracle or delayed-oracle end (you don't know if a solution exists, let alone whether yours is correct). Tam's argument that AI automates engineering first is precisely the oracle-strength prediction: automation works where verification is cheap. The "harden the oracle" engineering move maps to Tam's implied question of whether research taste can ever be made verifiable. Status: seedling.

- [the-augmentation-automation-boundary-is-discrimination-not-accuracy](../../notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) — **grounds**: Tam argues AI tools automate SWE because it has "a test to pass, a spec to meet, a benchmark to clear" but can't automate research because "it's not clear what definition of ground truth one should optimize." This is the augmentation-automation boundary stated from a different angle: engineering has external hard oracles (route b), research has only self-assessment with low discrimination. Tam's claim that "this gap will close" corresponds to the open question of whether discrimination improves with scale. Status: seedling.

- [bitter-lesson-boundary](../../notes/bitter-lesson-boundary.md) — **exemplifies**: Tam's engineering-vs-research distinction maps onto the arithmetic-vs-vision-feature boundary. Engineering tasks have specs that ARE the problem (test suites, benchmarks); research taste is a theory about what problems are worth solving — a vision feature. Tam's observation that autoresearch does hyperparameter sweeps (arithmetic-regime work) but not problem selection (vision-feature work) is a concrete instance of the bitter lesson boundary running through a single system. Status: current.

- [automating-kb-learning-is-an-open-problem](../../notes/automating-kb-learning-is-an-open-problem.md) — **extends**: Both describe the same structural bottleneck at different scales. The KB's open problem is automating judgment-heavy mutations (connections, synthesis) that require oracles we can't manufacture. Tam describes the same bottleneck for research: automating problem selection requires evaluating bets whose outcomes are unknown. Both are instances of: automation stalls where the evaluation problem is unsolved. Tam's framing adds the "what to not try" dimension — the KB note focuses on what to try (propose mutations), while Tam emphasizes that knowing what to skip is equally valuable. Status: speculative.

- [first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit](../../notes/first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md) — **grounds**: Tam's "research taste" is, in Deutsch's vocabulary, the ability to select for explanatory reach over adaptive fit. The hyperparameter-sweeping autoresearch agent is doing adaptive work (what combination of settings improves this metric?). The researcher's taste is explanatory: understanding why a particular architecture might work, which transfers across domains. Tam's observation that "taste transfers even as domain knowledge shifts" (physicists become quants become AI researchers) is a direct statement of Deutsch's reach property — explanatory knowledge applies beyond its original context. Status: seedling.

- [discovery-is-seeing-the-particular-as-an-instance-of-the-general](../../notes/discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) — **grounds**: Tam's coin-flipping metaphor — the expert "weaves through the quadrillion-coin room with a preternatural air" — describes the discovery mechanism. Recognizing which problems are worth pursuing is recognizing the particular (this specific research question) as an instance of the general (a class of problems that tends to yield results). The "naming amortizes discovery cost" insight from this note explains why taste is portable: once you've identified the structural pattern that makes problems tractable, you recognize it in new domains cheaply. Shannon's observation that "the best training data for research taste doesn't exist in any corpus" maps to the note's claim that recognition cost scales with abstraction depth — the deepest discoveries can't be extracted from surface data. Status: seedling.

- [memory-management-policy-is-learnable-but-oracle-dependent](../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) — **extends**: AgeMem demonstrates that composition policy (when to store/retrieve/filter) is learnable via RL when there's a clear oracle (task completion). Tam's argument is that research taste — the composition policy for which problems to work on — lacks such an oracle. AgeMem succeeds because "did the agent complete the task?" is binary and immediate. Research taste fails the same test: "was this problem worth pursuing?" has no equivalent resolution point. This makes the source an external validation of the KB's oracle-dependency analysis from a completely different domain. Status: current.

**Bidirectional candidates** (reverse link also worth adding):
- [oracle-strength-spectrum](../../notes/oracle-strength-spectrum.md) <-> source — the source provides a vivid external argument for why the hard-oracle vs no-oracle distinction determines automation viability, from the perspective of research economics rather than KB theory.
- [bitter-lesson-boundary](../../notes/bitter-lesson-boundary.md) <-> source — the source provides a concrete real-world example of the boundary running through a domain (AI research: hyperparameter sweeps are arithmetic, problem selection is vision features).

## Rejected Candidates

- [learning-is-not-only-about-generality](../../notes/learning-is-not-only-about-generality.md) — The reach/accumulation framework is indirectly relevant (taste is high-reach knowledge), but the connection runs entirely through first-principles-reach, which already links to this note. A direct link from the source to learning-is-not-only-about-generality would add a hop without adding insight.

- [information-value-is-observer-relative-because-extraction-requires-computation](../../notes/information-value-is-observer-relative-because-extraction-requires-computation.md) — The bounded-observer framework could frame taste as "knowing which information to extract," but this requires too much interpretive stretch. The source doesn't discuss computation-bounded extraction or data ordering. Surface vocabulary overlap only.

- [bounded-context-orchestration-model](../../notes/bounded-context-orchestration-model.md) — The selection problem in orchestration (what to load into bounded context) is structurally analogous to research problem selection, but the domains are too far apart and the connection too abstract to pass the agent-traversal test. An agent following this link would gain nothing actionable.

- [codification-and-relaxing-navigate-the-bitter-lesson-boundary](../../notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) — Related through the bitter lesson, but the source says nothing about codification or relaxing. The connection runs through bitter-lesson-boundary, which is already a candidate.

- [claw-learning-is-broader-than-retrieval](../../notes/claw-learning-is-broader-than-retrieval.md) — Surface overlap on "learning beyond retrieval" but the source is about human research taste, not agent learning capacity. No genuine connection.

- [Creative Thinking by Claude Shannon](../../sources/creative-thinking-by-claude-shannon.md) — Shannon's problem-solving operators (simplification, analogy, restatement, generalization, structural analysis, inversion) are concrete instances of "research taste" in action. However, Shannon describes tactical operators for solving problems once selected, while Tam's argument is about problem selection itself — choosing which coins to flip, not how to flip them. The two are complementary but address different stages of the research process, and linking them would overstate the overlap.

- [professional-software-developers-dont-vibe-they-control](../../sources/professional-software-developers-dont-vibe-they-control.ingest.md) — The task suitability mapping to oracle strength is relevant as contrast (professional developers control agents where oracles exist), but the connection is indirect through oracle-strength-spectrum, not directly to this source.

## Index Membership

- [learning-theory](../../notes/learning-theory-index.md) — The source's claim about oracle availability as the automation bottleneck connects to the Oracle & Verification section. Not a KB note itself, so not a direct member, but connection reports from this source should be filed in the learning-theory neighborhood.
- Already exists in: kb/sources/ (captured source, no index membership yet)

## Synthesis Opportunities

**Oracle strength as the automation boundary for cognitive work (not just agent systems).** The source (research taste can't be automated because no oracle), the oracle-strength-spectrum (automation depends on verification cost), the augmentation-automation-boundary (discrimination is the bottleneck), and the automating-KB-learning note (judgment operations require oracles we can't manufacture) all converge on the same claim from different angles: **the boundary of automation is the boundary of verification.** This is stronger than what any individual note states. The oracle-strength note frames it within agent systems; Tam frames it as a general principle about cognitive work; the KB learning note shows the same pattern in knowledge curation. A synthesis note titled something like "The boundary of automation is the boundary of verification" could unify these under the claim that across all domains — engineering, research, knowledge curation — tasks become automatable precisely when verification becomes cheap, and the hard problem is always oracle construction, never generation capability.

## Flags

- None. The source connects cleanly to an existing cluster (oracle theory / bitter lesson boundary / learning theory) without crossing too many areas or making too many independent assertions.
