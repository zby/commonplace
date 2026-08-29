# Match register

One row per source tradition the series borrows from, following
[problem matches guide method search and mechanism matches bound transfer](../../notes/problem-matches-guide-method-search-mechanism-matches-bound-transfer.md).
A **problem match** pairs a bounded source problem with one of the
[target problems](./target-problems.md) and returns candidate responses; it
warrants nothing. A **mechanism match** holds when the response's operative
mechanism and its premises are independently present in the target part the
response would govern; only that shared relation carries warrant, and every
feature beyond it is a target-side conjecture. **Match depth** records whether
source and target share the condition that generated the problem
(causal-origin) or only the later control problem (downstream); the deeper
match strengthens the reason to inspect a source without substituting for the
mechanism test. Composition of matched
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

| Source | Bounded source problem | Target | Match depth | Candidate response | Mechanism-match status | Non-transfer boundary |
|---|---|---|---|---|---|---|
| Naur 1985, *Programming as Theory Building* ([ingest](../../sources/programming-as-theory-building.ingest.md)) | Why documented programs die when their programmers leave: what a program's theory is and why documentation did not transfer it | P1 | Causal-origin: the theory is a capacity a package may fail to carry, in source and target alike | Theory as capacity, not text; three bearer tests; transfer needs contact with the holder | **Established** (accepted Naur article). See worked row 1. | The human-binding conclusion, which runs through a premise absent in the target; any claim that a composite holds a theory |
| Ryle, via Naur | Rule-following regress | P1 | Causal-origin: the regress applies to any rule-follower | Intelligent behaviour is not rule-following all the way down | Established as far as articulable rules; does not decide trained recognizers | Any claim about what a recognizer does or does not judge |
| Popper 1966 ([ingest](../../sources/popper-a-realist-view-of-logic-physics-and-history-1966.ingest.md)) | Growth of objective knowledge through criticism of stated theories | P3, and P1's "what a theory is" | Causal-origin for criticism: a stated theory has consequences beyond its producer in both | Theory as an objective product with consequences beyond its producer; the problem–theory–criticism cycle | **Established** for criticism of an objective theory; admission and acceptance are target-side. See worked row 5. | Acceptance and operational checks, which the source leaves unspecified; the immediate successor-problem step as an operational stage; logical relations equated with what an interpreter finds |
| Argyris 1977 ([ingest](../../sources/argyris-organizational-learning-and-mis-1977.ingest.md)) | Organizational error correction when the theory governing behaviour differs from the one stated; self-sealing control systems | P3 | Per candidate. Operativity test: causal-origin — the actor acquired its operating theory tacitly before any declared theory existed, by socialization there and pretraining here. Update-target distinction: downstream — double loop is hard there because of threat, here because of a fixed decomposition and evaluator. Self-sealing: downstream — Model I is absent; training-induced disposition is only an analogue | Espoused theory vs theory-in-use; single- and double-loop learning; self-sealing | **Established** for the operativity test and the update-target distinction; **conjectured** for structural self-sealing; the motivational mechanism does not transfer. See worked row 6. | Model I values, defensive routines, organizational politics; the claim that double loop *changes* rather than questions governing variables; any evidence about agent-architecture performance |
| Craik 1943 ([ingest](../../sources/craik-hypothesis-on-the-nature-of-thought-1943.ingest.md)) | Why an organism benefits from an internal model | P3 | Unassessed | Try alternatives on the model before the world | **To assess**; snapshot required for any quote | Learning and validation of the model, which the source leaves open |
| Ashby 1960; Conant & Ashby 1970 ([ingest](../../sources/ashby-design-for-a-brain-1960.ingest.md), [ingest](../../sources/conant-ashby-every-good-regulator-1970.ingest.md)) | Adaptation without a theory: ultrastability; what a regulator must contain | P3 (contrast), P2 | Contrast; no match claimed | Theory-free adaptation as the contrast class; a good regulator contains a model of what it regulates | **Contrast** | Ultrastability is not a mechanism for theory-mediated loops; the regulator theorem's model is not retained natural-language theory |
| Sutton 2019, *The Bitter Lesson* ([ingest](../../sources/sutton-the-bitter-lesson-original-essay.ingest.md)) | Why hand-built domain knowledge loses to methods that exploit computation | P5 | Causal-origin: growing computation rewards search and learning over hand-built knowledge in both | The production-method axis (specified vs selected by search or learning) | **Established** (accepted Bitter Lesson article). See worked row 2. | The weights-only extrapolation: the source's mechanism concerns production, and representational form is a separate axis |
| Sutton & Javed ([ingest](../../sources/sutton-javed-why-ai-models-stop-learning.ingest.md)) | Why deployed models stop learning; context-state adaptation vs continual weight learning | P5 | Causal-origin for the big-world premise; the response mechanism failed | Concept formation requires continued weight learning | **Failed** as the continual-learning draft used it (C3: concept formation claimed for the composite without an autonomous witness); the big-world premise and the "what keeps knowledge correct" question transfer | The inference "concepts formed by weights must continue by weights"; the concept-formation label for artifact-level changes |
| Schmidhuber, Gödel machine ([ingest](../../sources/goedel-machines-schmidhuber.ingest.md)) | Self-modification gated on a proof of higher axiomatized utility | P2 | Contrast; no match claimed | Gate before self-modification; searcher itself revisable | **Contrast** (the proof-governed limit; library note exists) | The proof gate requires an axiomatized utility the target lacks; nothing beyond the gate structure transfers |
| DGM, HGM, HyperAgents ([ingest](../../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md), [ingest](../../sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md), [ingest](../../sources/hyperagents.ingest.md)) | Empirical self-improving coding loops with archive and benchmark selection | P2, P4 | Evidence; not a borrowed mechanism | Cases of viability-only gates, fixed outer loops, unestablished compounding | **Evidence** for the closure–capability map | No method transfers; the cases populate regions |
| Memento-Skills, Co-Harness, Agent Symbolic Learning ([ingest](../../sources/memento-skills-let-agents-design-agents.ingest.md), [ingest](../../sources/co-harness-co-evolving-harness-and-model-weights.ingest.md), [ingest](../../sources/symbolic-learning-enables-self-evolving-agents.ingest.md)) | Learning localized artifacts around a frozen model inside a bounded update space | P5 | Instance of the target class, not a source tradition | Rewrite–test–rollback over prompts, skills, tools; alternation with fine-tuning | **Established** as existence evidence that the selected-localized cell is populated | Scaling, evaluator–deployment match, generalization of retained artifacts |
| Prime Agent, Recuris, Apodex ([ingest](../../sources/prime-agent-a-self-improving-rlm-harness.ingest.md), [ingest](../../sources/apodex-1-1-scaling-agentic-intelligence-for-complex-work.ingest.md)) | Persistent harnesses that retain rules or weights | P3 (contrast) | Evidence; not a borrowed mechanism | Retention without a revisable theory | **Evidence** (library evidence note exists) | Nothing transfers as method |
| Bainbridge 1983, *Ironies of Automation* | An operator asked to monitor a system installed because it outperforms the operator | P2 | Causal-origin: selective automation leaves the residue it could not take, in both | Automation leaves the residue that could not be automated; the monitoring irony; skill loss without routine contact | **Conjectured** for the degradation mechanism (extraction candidate E9); established for the residue reading in library notes | Industrial process-control specifics; any claim about how often the irony bites |
| Parasuraman, Sheridan & Wickens 2000 | Which stages of a task to automate, judged by consequences | P4 | Downstream: supervisory-control allocation and pathway-function allocation share the reporting problem, not its cause | Per-function allocation profile; allocation judged by performance, reliability, and cost of consequences | **Established** with declared departures (closure-tracking note): the functions are the pathway's own, the ten-level scale is not inherited | The within-function level scale; task-performance stages |
| Mission command (ADRP 6-0, MCDP 1, Stahel) ([ingest](../../sources/us-army-adrp-6-0-mission-command-2012.ingest.md), [ingest](../../sources/david-stahel-auftragstaktik-mission-command.ingest.md)) | Allocating purpose, information, and decision rights when upstream holds intent and execution holds the state | P6 | Downstream: no adaptive opponent in the workshop; only the later control problem is shared | Commander's intent: purpose, key tasks, end state; bounded executor authority; governed return of control | **Conjectured**. See worked row 4. | Hierarchy, rank, doctrine, adversarial purpose; the label as stable guidance (Stahel) |
| Internal: [codifying predictable choices leaves agents with less predictable work](../../notes/codifying-predictable-choices-leaves-agents-with-less-predictable-work.md) | Composition of residual agent work after preferential codification | P2 | Causal-origin: the same selection mechanism, with the selector changed | Selection effect on the residue | **Established** (note written 2026-08-28). See worked row 3. | The planning consequence (executor information advantage) does not move unchanged |

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

### 5. Popper 1966 → P3, and P1's sense of "theory"

**Problem match.** Popper's bounded problem is how objective knowledge grows:
how theories, as products standing outside their producers, are consumed so
that criticism yields new problems. P3 asks how retained natural-language
theory guides operation and stays revisable; P1 needs a sense of *theory*
that is not a mental state. The match covers the revisability half of P3 and
the vocabulary half of P1, and returns four candidates from the retained
quotes: theories are "exosomatic artefacts" that can be "contained in a book"
or "stored in a library"; their logical relations hold "quite independently of
whether or not anybody has noticed or understood" them, so that "the person
who produces a theory may very often not understand it"; growth follows
`P1 → TT → EE → P2`; and consuming a theory "means criticising them,
changing them, and often even demolishing them, in order to replace them by
better ones"
([ingest](../../sources/popper-a-realist-view-of-logic-physics-and-history-1966.ingest.md)).

**Mechanism match.** The operative mechanism is that a stated theory has
consequences that can be derived and compared — with other theories and with
observations — by a consumer who need not be its producer, and that
eliminating an error this way changes the problem. Its premises are: the
theory is stated, so it has content beyond anyone's grasp of it; some consumer
can derive consequences; criticism is applied with the strongest available
means. All three are independently present in the target part this governs,
the retained-theory layer. A note is a stored object; a language-model
interpreter derives consequences and finds incompatibilities across notes;
review gates apply criticism. So three things transfer: retained theory is an
addressable object, not a mental state (this is what the accepted Naur article
means by *retained theory* as against *holding* it); criticism operates on the
object and can be done by a consumer who does not hold the capacity the object
describes; and productive criticism is measured by the problem it exposes, not
only by the correction it makes.

Two target-side conditions attach. In Popper the consequences stand in
*logical* relations; in the target they are derived by interpretation, so the
derivation is itself a criticizable claim about the object, and the interpreter
enters as an error source the schema does not model. And criticism converges
in the target only when checks are decorrelated from the error — a
re-reading under the same prompt is not Popper's "critical discussion" — as
[mechanistic constraints make Popperian KB recommendations actionable](../../notes/mechanistic-constraints-make-popperian-kb-recommendations-actionable.md)
already argues.

The accepted Naur article's repair episode is target-side evidence for the
transferred split: the improvement pass criticized the note correctly with only
the object in hand, and failed at repair, which needed the capacity. Popper
predicts the first; nothing in Popper predicts the second, which is Ryle's and
Argyris's territory.

**Non-transfer boundary.** Popper supplies no acceptance rule and no
operational checks (the ingest's own limit), so admission is a target-side
construction — the discovery lifecycle's staged acceptance and integration,
not the immediate `P2`. "Problem depth" as a progress signal has no measure
in the source. The essay's arguments on reduction, physics, and logic do not
enter. And the World 3 vocabulary is Naur's citation, not this text's.

### 6. Argyris 1977 → P3

**Problem match.** Argyris's bounded problem is why organizations correct
routine errors but fail at errors that require questioning governing
objectives and policies, given that "theories-in-use are the theories of
action that actually govern their actions" while espoused theories are the
ones "people report are governing their actions", and given that control
systems can make learning self-sealing
([ingest](../../sources/argyris-organizational-learning-and-mis-1977.ingest.md)).
P3 asks how retained theory comes to guide operation with binding force and
stays revisable when its governing commitments are wrong. The match covers
both halves and returns four candidates: an operativity test (espoused vs
in-use); an update-target distinction (single loop corrects "so the job gets
done and the action remains within stated policy guidelines"; double loop is
"the thermostat questioning its order"); a learning unit ("organizations
learn through individuals acting as agents for them", and learning "requires
the capacity to know when it is unable to identify and correct errors"); and
a self-sealing mechanism (errors "camouflaged", their inhibiting loops
camouflaged, "the camouflage is camouflaged").

**Mechanism match, per candidate.**

- *Operativity test.* Mechanism: behaviour is governed by whatever theory is
  actually consumed in selecting it, not by what is declared. Premises: an
  actor selects behaviour; some representation participates; the declared and
  the participating representation can differ. All present in the target, and
  already carried by
  [an action model matters only through its consumption path](../../notes/an-action-model-matters-only-through-its-consumption-path.md)
  and the behavioral-authority definition. Transfers as P3's criterion: the
  theory-in-use is the theory on the consumption path with binding force. The
  target adds a location the source does not have: the gap between espoused
  and in-use falls between retained text and the model's prior and routing,
  so a note can be espoused while the weights supply the theory-in-use. The
  mechanism is the same, and so is the generating condition: an operating
  theory acquired tacitly — by socialization there, by pretraining here —
  before any declared theory was written. **Established; causal-origin.**
- *Update-target distinction.* Mechanism: correction within governing
  variables differs from inquiry into them. Premise: a distinction between
  action rules and the objectives or policies that set them. Present in the
  target as the difference between editing an artifact inside a decomposition
  and revising the decomposition, objective, or evaluator. Transfers as the
  update-target distinction. Does not transfer: that double loop *changes*
  governing variables (the source says *questions*), and the mapping to a
  generality axis, which
  [learning is not only about generality](../../notes/learning-is-not-only-about-generality.md)
  already labels as Commonplace's interpretation. **Established.**
- *Learning unit.* Mechanism: the system learns through its agents' actions
  when the results are retained in the system's maps and norms rather than
  only in the agents. Premise: retention outside the acting individual. Present
  in the target as retained artifacts consumed by later loops. Transfers as
  the unit statement behind ledger row C2 — the deployed system, not the
  interpreter, is the unit — and as a requirement on the evaluator: a
  learning system needs the capacity to know when it cannot correct an error.
  **Established** for the unit; the evaluator requirement is a candidate
  gate-adequacy condition.
- *Self-sealing.* Mechanism in the source: Model I theories-in-use (win,
  control unilaterally, suppress) make threatening errors uncorrectable and
  camouflage the inability. The motivational premise — an actor with status to
  protect — is absent in the target, so that mechanism does not transfer.
  What is present is the structural form: an evaluator that cannot detect its
  own inability to correct. The accepted Naur article's episode is an
  instance — the pass assessed each repair against a brief reconstructed
  after it had defeated the earlier claim and reported the contribution
  strengthened. The structural form transfers as a reading of captured or
  self-confirming evaluators. **Conjectured**; the defensive-routine account
  does not enter. Argyris's further claim that tightening control corrupts
  the evidence it was meant to improve has a target-side analogue in
  [narrowing bought to survive review](../../notes/narrowing-bought-to-survive-review-is-paid-for-in-content.md),
  but it is an analogue, not a match, until the mechanism is shown to be the
  same.

**Non-transfer boundary.** Model I and Model II values, interpersonal
defensive routines, organizational politics, and the stylized local-versus-
distant information-system contrast do not enter. The source offers no
addressable retained theory, theory-search procedure, benchmark, or
sample-efficiency result, so it grounds vocabulary and the failure mechanism,
never claims about an agent architecture's learning performance (the
ingest's own boundary). The source's loop vocabulary does not establish a
shared mechanism with Ashby's ultrastability; the two remain separate rows.

**What the two rows settle together.** Popper's mechanism operates on the
stated object; Argyris's binding operates on the consumed theory. The Naur
repair episode splits exactly at that seam — critique needed the object,
repair needed the theory-in-use — which is a candidate answer to the
criticism × theory-in-use interaction check in
[article roles](./article-roles.md#composition): criticism of the stated
theory can reach a divergent theory-in-use only where the mediation trace
reads what was consumed, not what was retained.

## What this register changes

- A draft may not cite a source's conclusion as support for a target claim
  unless the row's mechanism-match status licenses it; a **failed** or **to
  assess** row supports nothing beyond its non-transfer boundary.
- Ledger defeats that were transfer failures are cross-referenced here (S2,
  C3, R2). Reconstruction must re-derive the claim from the shared mechanism
  or drop it.
- Rows marked **to assess** are work items; a source with no row may not
  enter an article.
