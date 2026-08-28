# Match register

One row per source tradition the series borrows from, following
[problem matches guide method search and mechanism matches bound transfer](../../notes/problem-matches-guide-method-search-mechanism-matches-bound-transfer.md).
A **problem match** pairs a bounded source problem with one of the
[target problems](./target-problems.md) and returns candidate responses; it
warrants nothing. A **mechanism match** holds when the response's operative
mechanism and its premises are independently present in the target part the
response would govern; only that shared relation carries warrant, and every
feature beyond it is a target-side conjecture. Composition of matched
mechanisms is a new construction with its own interaction checks, recorded in
[article roles](./article-roles.md#composition).

Status vocabulary: **established** — the mechanism match has been argued in an
accepted article or a library note; **conjectured** — the match is plausible
and its conditions are stated but not yet argued; **contrast** — the source
enters as a comparison class, not a transferred mechanism; **evidence** — the
source is a case for the closure–capability map, not a method; **failed** — a
draft assumed transfer past the shared mechanism and review defeated it; **to
assess** — no disposition yet.

## Register

| Source | Bounded source problem | Target | Candidate response | Mechanism-match status | Non-transfer boundary |
|---|---|---|---|---|---|
| Naur 1985, *Programming as Theory Building* ([ingest](../../sources/programming-as-theory-building.ingest.md)) | Why documented programs die when their programmers leave: what a program's theory is and why documentation did not transfer it | P1 | Theory as capacity, not text; three bearer tests; transfer needs contact with the holder | **Established** (accepted Naur article). See worked row 1. | The human-binding conclusion, which runs through a premise absent in the target; any claim that a composite holds a theory |
| Ryle, via Naur | Rule-following regress | P1 | Intelligent behaviour is not rule-following all the way down | Established as far as articulable rules; does not decide trained recognizers | Any claim about what a recognizer does or does not judge |
| Popper 1966 ([ingest](../../sources/popper-a-realist-view-of-logic-physics-and-history-1966.ingest.md)) | Growth of objective knowledge through criticism of stated theories | P3, and P1's "what a theory is" | Theory as an objective product with consequences beyond its producer; the problem–theory–criticism cycle | **Established** for criticism: retained theory is an addressable object whose consequences can be derived and tested | Acceptance and operational checks, which the source leaves unspecified; admission is target-side |
| Argyris 1977 ([ingest](../../sources/argyris-organizational-learning-and-mis-1977.ingest.md)) | Organizational error correction when the theory governing behaviour differs from the one stated; self-sealing control systems | P3 | Espoused theory vs theory-in-use; single- and double-loop learning; self-sealing | **Established** for the consumption-path distinction (an artifact governs only through what consumes it with binding force); double-loop *changing* governing variables is our reading | Organizational politics and interpersonal dynamics; the claim that double loop *changes* rather than questions governing variables |
| Craik 1943 ([ingest](../../sources/craik-hypothesis-on-the-nature-of-thought-1943.ingest.md)) | Why an organism benefits from an internal model | P3 | Try alternatives on the model before the world | **To assess**; snapshot required for any quote | Learning and validation of the model, which the source leaves open |
| Ashby 1960; Conant & Ashby 1970 ([ingest](../../sources/ashby-design-for-a-brain-1960.ingest.md), [ingest](../../sources/conant-ashby-every-good-regulator-1970.ingest.md)) | Adaptation without a theory: ultrastability; what a regulator must contain | P3 (contrast), P2 | Theory-free adaptation as the contrast class; a good regulator contains a model of what it regulates | **Contrast** | Ultrastability is not a mechanism for theory-mediated loops; the regulator theorem's model is not retained natural-language theory |
| Sutton 2019, *The Bitter Lesson* ([ingest](../../sources/sutton-the-bitter-lesson-original-essay.ingest.md)) | Why hand-built domain knowledge loses to methods that exploit computation | P5 | The production-method axis (specified vs selected by search or learning) | **Established** (accepted Bitter Lesson article). See worked row 2. | The weights-only extrapolation: the source's mechanism concerns production, and representational form is a separate axis |
| Sutton & Javed ([ingest](../../sources/sutton-javed-why-ai-models-stop-learning.ingest.md)) | Why deployed models stop learning; context-state adaptation vs continual weight learning | P5 | Concept formation requires continued weight learning | **Failed** as the continual-learning draft used it (C3: concept formation claimed for the composite without an autonomous witness); the big-world premise and the "what keeps knowledge correct" question transfer | The inference "concepts formed by weights must continue by weights"; the concept-formation label for artifact-level changes |
| Schmidhuber, Gödel machine ([ingest](../../sources/goedel-machines-schmidhuber.ingest.md)) | Self-modification gated on a proof of higher axiomatized utility | P2 | Gate before self-modification; searcher itself revisable | **Contrast** (the proof-governed limit; library note exists) | The proof gate requires an axiomatized utility the target lacks; nothing beyond the gate structure transfers |
| DGM, HGM, HyperAgents ([ingest](../../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md), [ingest](../../sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md), [ingest](../../sources/hyperagents.ingest.md)) | Empirical self-improving coding loops with archive and benchmark selection | P2, P4 | Cases of viability-only gates, fixed outer loops, unestablished compounding | **Evidence** for the closure–capability map | No method transfers; the cases populate regions |
| Memento-Skills, Co-Harness, Agent Symbolic Learning ([ingest](../../sources/memento-skills-let-agents-design-agents.ingest.md), [ingest](../../sources/co-harness-co-evolving-harness-and-model-weights.ingest.md), [ingest](../../sources/symbolic-learning-enables-self-evolving-agents.ingest.md)) | Learning localized artifacts around a frozen model inside a bounded update space | P5 | Rewrite–test–rollback over prompts, skills, tools; alternation with fine-tuning | **Established** as existence evidence that the selected-localized cell is populated | Scaling, evaluator–deployment match, generalization of retained artifacts |
| Prime Agent, Recuris, Apodex ([ingest](../../sources/prime-agent-a-self-improving-rlm-harness.ingest.md), [ingest](../../sources/apodex-1-1-scaling-agentic-intelligence-for-complex-work.ingest.md)) | Persistent harnesses that retain rules or weights | P3 (contrast) | Retention without a revisable theory | **Evidence** (library evidence note exists) | Nothing transfers as method |
| Bainbridge 1983, *Ironies of Automation* | An operator asked to monitor a system installed because it outperforms the operator | P2 | Automation leaves the residue that could not be automated; the monitoring irony; skill loss without routine contact | **Conjectured** for the degradation mechanism (extraction candidate E9); established for the residue reading in library notes | Industrial process-control specifics; any claim about how often the irony bites |
| Parasuraman, Sheridan & Wickens 2000 | Which stages of a task to automate, judged by consequences | P4 | Per-function allocation profile; allocation judged by performance, reliability, and cost of consequences | **Established** with declared departures (closure-tracking note): the functions are the pathway's own, the ten-level scale is not inherited | The within-function level scale; task-performance stages |
| Mission command (ADRP 6-0, MCDP 1, Stahel) ([ingest](../../sources/us-army-adrp-6-0-mission-command-2012.ingest.md), [ingest](../../sources/david-stahel-auftragstaktik-mission-command.ingest.md)) | Allocating purpose, information, and decision rights when upstream holds intent and execution holds the state | P6 | Commander's intent: purpose, key tasks, end state; bounded executor authority; governed return of control | **Conjectured**. See worked row 4. | Hierarchy, rank, doctrine, adversarial purpose; the label as stable guidance (Stahel) |
| Internal: [codifying predictable choices leaves agents with less predictable work](../../notes/codifying-predictable-choices-leaves-agents-with-less-predictable-work.md) | Composition of residual agent work after preferential codification | P2 | Selection effect on the residue | **Established** (note written 2026-08-28). See worked row 3. | The planning consequence (executor information advantage) does not move unchanged |

## Worked rows

### 1. Naur → P1

**Problem match.** Naur's bounded problem is why a successor group with full
documentation still proposed patches that destroyed a compiler's structure.
P1 asks what can hold a program's theory well enough to modify it coherently.
The match is direct and returns three candidates: theory as capacity rather
than text; bearer tests (program-specific acquisition, unregenerable premises,
reliability across occasions); transfer by contact with the holder.

**Mechanism match.** Naur's mechanism for the human binding is an inference:
similarity criteria cannot be formulated; a machine judges only by formulated
criteria; therefore no machine makes the judgment. The second premise is
absent in the target: a trained interpreter produces similarity judgments
without a stated rubric. So the human-binding conclusion does not transfer.
The bearer tests do transfer, because they are stated over capacities, and the
target's composite either has those capacities or does not. Naur's evidence
transfers as evidence about one kind of package (text plus advice) failing to
carry possession.

**Non-transfer boundary.** Blocking the bridge shows nothing about whether
any composite holds a theory. The accepted article's own repair episode is a
target-side test that a composite failed the third bearer test.

### 2. Sutton 2019 → P5

**Problem match.** Sutton's bounded problem is why hand-built knowledge
repeatedly loses to compute-leveraging methods. P5 asks whether learned
localized artifacts can compete with weights. The match returns the
production-method axis.

**Mechanism match.** Sutton's mechanism is that search and learning scale
with computation while hand-specification does not. That mechanism concerns
how content is produced. The target's representational-form choice is
independent of production method — an optimizer can select a prompt, an
expert can set a weight — so the mechanism transfers only over the production
axis. The weights-only extrapolation adds a premise (form is determined by
production method) the source does not argue.

**Non-transfer boundary.** Whether learned localized artifacts are competitive
at scale is a target-side empirical question; the accepted article states the
test and leaves it open.

### 3. Codification note → P2 (internal transfer)

**Problem match.** The source note's bounded problem is the composition of
residual agent work after a system codifies its predictable choices. P2 asks
what is left after decisions leave the human cut. Same shape: a residue after
selective transfer.

**Mechanism match.** The source mechanism is selection on the property the
receiving actor requires. That mechanism is present at the human cut. The
*property* differs because the receiver differs: code requires predictability
(a mapping fixable and verifiable cheaply); a model-plus-verifier requires
warrant (represented inputs, settled criterion, independent check). The
transfer therefore keeps the mechanism and swaps the selector, which is what
[the resulting note](../../notes/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md)
does.

**Non-transfer boundary.** The source note's planning consequence (defer
choices whose information arrives during execution) rests on an executor
information advantage that does not carry unchanged to the human cut; at that
boundary the agent already executes, so late-arriving information mostly
favours the computational side, and the horizon row captures what remains.

### 4. Mission command → P6 (workshop intent)

**Problem match.** The source's bounded problem is allocating purpose,
information, and decision rights when upstream retains intent and execution
holds the state relevant to the choice of means. P6 is that problem for this
workshop. The match returns commander's intent (purpose, key tasks, end state)
and bounded executor authority as candidates, which the README's Intent
section uses.

**Mechanism match, conditions.** The match holds only if three things are
independently true of the workshop: the operator holds a purpose the
executing agents cannot safely reconstruct (attracting researchers is not
derivable from the artifacts); the agents hold decision-relevant execution
evidence the operator does not have at handoff (what review passes found);
and the handoff governs integration, verification, and return of control (the
ledger, the closure conditions, and the ADR 080 hand-back when a change would
alter a claim). Each is plausible; none has been tested by a case where an
agent changed a task to serve the intent and the change was judged right.

**Non-transfer boundary.** Nothing about hierarchy, rank, doctrine, or
adversarial purpose transfers. Stahel's warning applies: the label
*Auftragstaktik* is not stable operating guidance, so the workshop cites the
relation, not the doctrine.

## What this register changes

- A draft may not cite a source's conclusion as support for a target claim
  unless the row's mechanism-match status licenses it; a **failed** or **to
  assess** row supports nothing beyond its non-transfer boundary.
- Ledger defeats that were transfer failures are cross-referenced here (S2,
  C3, R2). Reconstruction must re-derive the claim from the shared mechanism
  or drop it.
- Rows marked **to assess** are work items; a source with no row may not
  enter an article.
