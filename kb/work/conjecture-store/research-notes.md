# Research notes: explanatory reach, compression and conjectural learning

Synthesis of a research handoff explored on 2026-10-23 with four scout agents (compression and reach, Pearl's hierarchy, isotropy and connection discovery, experiments). Retained here because it motivates the conjecture store; mine for theory notes or delete when the workshop closes. Literature was read as abstracts and secondary summaries, not full texts.

Tags: [KB] existing Commonplace content, [lit] literature, [new] conjecture from the session. The four scout reports were session scratch and are not retained; their citations are carried inline below.

## 1. Five principles

1. **Measure compression for a bounded reader, over the KB's working body, not over raw observations.** A derived lemma adds no bits to the unbounded description of observations but shortens every later derivation. Time-bounded notions (logical depth, computational depth, epiplexity) capture this. [lit] Bennett 1988; Antunes et al. 2006; Finzi et al. 2026. [KB] `kb/theory/information-value-is-observer-relative.md`, the epiplexity notes. The handoff's §1 puzzle dissolves under this measure.

2. **A theory's value has three separable components: unification, discrimination, amortization.** Unification: fewer independent premises across what is already held. Discrimination: new tests that separate it from rivals. Amortization: cheaper later work. None reduces to another. A theory can discriminate while compressing nothing yet, and two theories can compress equally and disagree under intervention. [KB] `kb/theory/competing-causal-theories-can-guide-distinguishing-experiments.md` already states the discrimination-without-compression case with a worked bit cost.

3. **What separates an explanation from an arbitrary compressor is addressability plus forbidding.** An explanation is a compressor whose parts can be varied and criticized separately, and each part rules something out. gzip or an LLM compresses as a whole; nothing local in it can be criticized. [lit] Kitcher's stringent argument patterns (1981, 1989); Myrvold's mutual-information unification (2003); Deutsch's hard-to-vary. [KB] `kb/theory/definitions/addressable-theory.md`. [new] framing. The Algorithmic Markov Condition fits here: it is still description length, but counted per mechanism rather than over the joint, so it is a constraint on how to count, not a fourth virtue.

4. **Compression and any other cheap score route conjectures to criticism; they never accept them.** [KB] `kb/theory/candidacy-evidence-licenses-escalation-not-acceptance.md` already argues this with two witnesses, via Peirce's economy of research.

5. **Explanatory reach can be graded by invariance range, as a partial order.** A note declares its claimed range, its exercised range, and known breakdowns. Reach compares by set inclusion of survived ranges. [lit] Woodward 2003; Hitchcock & Woodward 2003. [KB] the four-part test in `kb/theory/first-principles-reasoning-selects-for-explanatory-reach-over.md` already contains both of Woodward's components; the `unwarranted-scope` gate is the surplus between claimed and exercised range.

## 2. Where the KB already stands

- Most of handoff §6 exists: `kb/articles/what-an-automated-reviewer-should-measure.md` (draft) proposes reach and economy as reader-relative compression progress plus a separate task-gain test, and says they can disagree.
- Rung-1 vs rung-2 rival pair exists; **no rung-3 worked example exists**. The Bareinboim ingest's open action points at this gap. The causal report supplies one: Y:=U versus Y:=X xor U, which agree on both lower rungs and give probability of necessity 1 versus 0. The discriminating "test" at rung 3 is a test of an assumption (monotonicity, Tian & Pearl 2000), not an outcome experiment.
- `kb/theory/definitions/reach-assessment.md` says the natural-language route to assessing reach "remains unexplained". The four evaluators below are candidate partial answers.
- Two mild conflicts with the handoff: (a) `kb/theory/brainstorming-how-explanatory-reach-informs-kb-design.md` treats high reach as a maintenance risk (blast radius), while the handoff treats unification only as value; (b) the Bennett 2023 ingest says the weakest valid hypothesis can generalize better than the shortest, so compression is a poor generalization proxy outside its fitting distribution.
- Not yet ingested, highest transfer value: LILO / Stitch (Grand et al. 2024: LLM-written docstrings improve how abstractions get used, so the prose gloss is part of a theory), Myrvold 2003, Hitchcock & Woodward 2003, Janzing & Schölkopf 2010, Gwern "LLM Daydreaming" 2025.

## 3. The structural gap: conjecture retention

This is the one finding every report converges on and the operator independently named.

**Current state [KB, verified by rg]:**
- `kb/log.md` holds de-facto "awaiting a second witness" entries ("needs more instances, watch"). Neither `cp-skill-write` nor `cp-skill-connect` reads the log. A second witness can arrive and nothing notices.
- Connect's Synthesis Opportunities live in gitignored cache; conjectures produced there are lost unless hand-triaged. Connect-report mining found 3 synthesis candidates in 45 reports and named "hub convergence without an authored claim" as the main pattern single-artifact connect structurally cannot see.
- `kb/theory/proposals/` is for finished theory awaiting vocabulary adoption; wrong shape for a half-formed conjecture.
- The theory COLLECTION permits a note that "states its conjectural force", but the AGENTS.md quality bar ("write a note when its mechanism is understood") and the grounding-oriented skills push everything toward corroborated content.

**Reframe.** Popper does not require support to retain a conjecture; he requires boldness and refutability. Store the problem the conjecture solves, what it would unify, and what would refute or corroborate it. That is cheap and it is what makes the conjecture findable later.

**Proposal [new], merging the compression report's archive and the isotropy report's conjecture record:**
- A `conjecture` shape with full note addressability (title-as-claim, description marker, tags, links), participating in connect and in any pair sampler.
- Required sections replace required support: problem; claimed unification or new distinction; stated refuters and corroborators; rung and scope claimed; **missing piece** (the evidence, instance or bridge term that would make it consequential); **trigger query** (an `rg` pattern or claim schema).
- The proposals rule applies: other notes may point to it, never cite it as a premise.
- Review checks only that refuters and trigger are stated and that no note cites it as premise; warrant gates are skipped.
- A post-write hook or connect runs open trigger queries against each new artifact. Promotion is by second witness. Expiry is by met refuter or N unmatched sweeps, kept in git.
- Re-score dormant conjectures when the corpus grows (Schmidhuber compares compressors on the growing history). Keep a diversity archive keyed by (tag pair, claim schema), best survivor per cell, rather than one ranked list.

Falsifier for the whole mechanism: after N sweeps, no retained conjecture has been promoted by a trigger hit that ordinary writing would not have found anyway.

## 4. Candidate evaluators for prioritizing conjectures [new]

All route to criticism; none accepts. Feed them into the selection comparison in `kb/theory/retained-theories-may-improve-sample-efficiency.md`.

| Evaluator | Measures | Gamed by | Misses |
|---|---|---|---|
| Premise reduction | Independent premises removed from existing notes when the conjecture is assumed; notes that become instances; blind check that rewrites preserve claims and falsifiers | Widened vague vocabulary (`generality-bought-to-avoid-counterexamples`); fix: each instance names what is forbidden there | Notes not yet written; fragility |
| Discriminating-test yield | Feasible, decision-relevant tests on which conjecture and incumbent disagree, priced | Distinctions no decision depends on | Little; this offsets premise-reduction's bias against new discriminators |
| Bounded-reader task-cost delta | Success times cost on held-out task sequence with and without the conjecture, model and budget fixed | Overfitting, leakage, weight-resident cueing; fix: matched-length name-only baseline | Expensive; observer-relative, redo after model change |
| Cross-coupling | Given the conjecture, does revising one distant note force a predicted revision in another | Verbal couplings; fix: propagate and blind-check | Unwritten territory |
| Reach guard | Charge a unifier its maintenance and fragility cost | | |

Flagged conjecture: premise reduction and discriminating-test yield are anti-correlated early in a conjecture's life. If true, any single scalar ranking systematically discards discriminators.

## 5. Connection discovery against isotropy

- **Invisible class [new]:** relations between two non-target notes; shared structure in disjoint vocabulary across tags; one note's conclusion constraining an unlinked note's premise. Review cannot see these by construction and should not; a discovery layer runs beside review, never inside a gate.
- **Sampling evidence [lit]:** Swanson's ABC bridging (1986) needs a shared intermediate; Uzzi et al. 2013: conventional core plus one atypical tail; Alien Space of Science: strictly novel combinations recovered at only 2.35x chance; Si et al. 2024: free LLM ideation collapses to ~5% non-duplicates, so diversity must come from the sampler. Recommended policy: most budget on bridged cross-tag pairs and claim-schema matches (Gentner structure mapping), about 20% uniform random as control, quality-diversity archive to prevent attractor collapse.
- **Evaluation [new]:** stage 1 cheap gate requires a typed relation (derives, constrains, contradicts, same-mechanism, bridge) and novelty against the KB; stage 2 decorrelated critic with both full notes must produce a derivation sketch, a scope change or a discriminating test. Consequential means it changes an inference the KB supports or unifies more than two notes. An analogy that changes no inference is decoration.
- **Self-improvement:** samplers as bandit arms scored by later uptake only, policy in a skill file so it is an addressable commitment. Expect lumpy, slow returns (Letta sleep-time compute gains scale with query predictability; isotropic hits are by definition unpredicted).
- The Substack daydreaming post is, by the KB's standard, a backcast showing reachability.

## 6. Experiments

No controlled theory-builder learning run has ever been performed in Commonplace. The KB has a 12-item checklist any run must satisfy (frozen seed baseline; cite/withhold/perturb the same revision; reconstruction and deliberation-matched arms; structured shifts; pre-registration per the write-brief pilot). All three proposals use synthetic worlds with nonce names and a simulator oracle, and pretest the base model zero-shot.

- **E1 Hidden unifier.** 4-6 domains, local rules, latent unifier in some worlds and none in null worlds. Arms: directed retrieval; reconstruction; daydream with criticism and retention; budget-matched directed connect; withheld and perturbed. Measures later held-out accuracy, probes to recover after a premise break, derivation tokens, false retention in null worlds. Highest reachability risk; mitigate by scoring capacity not text recovery. No published work tests random recombination by downstream effect; this fills the gap.
- **E2 Rung gap.** Random SCMs, rivals equivalent at lower rungs, agent gets the SCM interpreter as a tool so theory management is tested rather than arithmetic. Retained rung ledger versus no ledger versus scrambled ledger. Scored against computed identifiability: correct "underdetermined", information gain of proposed tests, experiments to identification, savings from reused mechanisms across sparse shifts. Lowest reachability risk.
- **E3 Fixed-pool prioritization.** Freeze E1's conjectures plus decoys; selectors: net code-length savings, LLM reach judgment, source fit, random. Pool must contain testable-but-not-compressive and compressive-but-causally-wrong strata. Answers §1 directly: can a conjecture save inference cost without shortening description length.
- **Cheapest backcast for isotropy:** hide the log's cross-tag SYNTHESIS entries at commit T, run connect vs random vs bridged pairs, then the prospective arm with open conjecture records over the next N real writes.

## 7. Recommended next steps, in order

1. Decide the conjecture shape (trait on theory notes vs new collection) and write its type contract; this unblocks everything else and is the operator's named problem.
2. Add the rung-3 worked pair to the competing-theories note or a sibling; closes an open ingest action.
3. Ingest LILO, Myrvold 2003, Hitchcock & Woodward 2003, Janzing & Schölkopf 2010, Gwern 2025.
4. Prototype the causal theory block plus a ~100-line interpreter; run E2 arms A-C on 3-variable worlds.
5. Build the pair sampler and two-stage filter as a skill; run the backcast, then open prospective conjecture records.
6. Reconcile the two conflicts: reach as risk versus reach as value; compression versus weakest-hypothesis generalization.
