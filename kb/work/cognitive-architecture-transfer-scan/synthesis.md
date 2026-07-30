# Working synthesis: transferable patterns across cognitive architectures

**Status:** memory-first, cross-scan conjecture; no external attribution is ready for promotion

## The useful comparison is mechanisms, not architecture scorekeeping

The scans do not support choosing a "best" cognitive architecture. They expose recurring design decisions that any agent memory or knowledge system must settle somehow:

1. What state types exist?
2. What becomes active under bounded resources?
3. How is a next operation proposed, selected, and committed?
4. What event triggers learning?
5. In what form is a successful resolution retained?
6. How does retained structure affect a later episode?
7. Which intermediate states can be observed well enough to evaluate the theory?

Architectures disagree in their answers, but the repeated questions are already useful as an evaluation frame. A system that claims "memory," "learning," or "reasoning" while leaving these transitions implicit has not yet supplied a process architecture.

## Pattern 1: access is a multi-stage causal path

[ACT-R](./act-r.md), [LIDA](./lida.md), [ASMO](./asmo.md), [DUAL](./dual.md), and [OpenCog](./opencog.md) converge in memory on a family of distinctions:

```text
retained → cue-matched → selected → actively available →
globally/task-relevant → action-selected → behavior-changing → learned-from
```

No architecture necessarily uses all these stages or these names. The provisional insight is that Commonplace's current retained → read-back → activated distinction may still compress several failure loci:

- retrieval candidate generation failed;
- the right candidate lost attention competition;
- the artifact entered context but did not become part of the task model;
- it informed a proposal but lost action selection;
- the selected action was not executable;
- the action occurred but its outcome did not update future behavior.

This is potentially significant because the stages imply different interventions and evaluations. More storage helps none of them by itself. Better retrieval addresses only the early transitions. Stronger authority can help or harm later transitions depending on whether the selected artifact is warranted.

**Local standing:** [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) already owns the important high-level distinction, while [memory design adds operational axes to artifact analysis](../../notes/memory-design-adds-operational-axes-to-artifact-analysis.md) owns activation policy. Do not create a new note unless a worked failure set proves that subdividing activation changes diagnosis or design.

**Best grounding comparison:** ACT-R retrieval/buffers versus LIDA workspace/broadcast. The question is not whether either describes LLMs. It is whether their process decompositions reveal empirically distinguishable failure stages in an agent trace.

## Pattern 2: selection values are not one number

[ACT-R](./act-r.md), [ASMO](./asmo.md), [OpenCog](./opencog.md), [PRS](./procedural-reasoning-system.md), and [Sigma](./sigma.md) suggest several quantities that ranking systems often collapse:

- epistemic support: how credible is the content?
- cue match or activation: how accessible is it now?
- attention priority: how urgently should processing be allocated?
- expected utility: how useful might an action be?
- commitment: which plan is currently being pursued?
- behavioral authority: who consumes the artifact, through what channel, with what force?

The most important local protection is already explicit: [behavioral authority](../../notes/definitions/behavioral-authority.md) is not confidence, relevance, or representational form. The new candidate is narrower: context selectors and review queues may need **typed priority contributions** rather than one opaque rank. A safety rule can be low-frequency and low-similarity yet mandatory; a novel observation can deserve attention without high confidence; a highly credible background fact can be irrelevant to the current decision.

**Significance test:** find one shipped or planned selector where collapsing these quantities causes a wrong inclusion, exclusion, or order. Without a worked case, this remains attractive ontology rather than a design need.

**Best grounding comparison:** OpenCog's remembered truth-value/attention-value separation, followed by ACT-R's activation/utility separation. Verify exact semantics before using either as precedent.

## Pattern 3: learning needs a trigger, a product, and a future activation path

[Soar](./soar.md) privileges impasse, [EPAM](./epam.md) and [CHREST](./chrest.md) use failed or inadequate discrimination, [HTM](./hierarchical-temporal-memory.md) uses violated temporal prediction, [SOSIEL](./sosiel.md) appears to use dissatisfaction, and ACT-R/Soar compile repeated problem solving. Together they yield a useful trigger taxonomy:

| Trigger | What it says is missing | Plausible retained product |
|---|---|---|
| Impasse | next-operation knowledge | scoped procedure or decision rule |
| Confusion | decision-relevant distinction | discriminator, negative example, or type refinement |
| Prediction violation | transition model | revised episode/workflow expectation |
| Repeated deliberation | efficient fast path | compiled skill, route, or validator |
| Outcome dissatisfaction | better behavior | candidate alternative, pending evaluation |

This sharpens "learn from traces." Different trace events call for different products. A generic summarizer tends to turn all of them into prose memories, even when the missing capacity is a selector, an exception, a process model, or executable procedure.

The existing KB already rejects retention alone as learning: [constraining during deployment is continuous learning](../../notes/constraining-during-deployment-is-continuous-learning.md) and [trace-extracted memory earns authority per operation, not at capture](../../notes/trace-extracted-memory-earns-authority-per-operation-not-at-capture.md) require operative, governed change. The plausible addition is a **trigger → missing-capacity → artifact-form** diagnostic, if real trace cases populate more than one row.

**Best grounding comparison:** Soar for impasse and chunking; EPAM or CHREST for discrimination; HTM only if sequence-conditioned memory becomes an active design question.

## Pattern 4: compilation is a scoped dependency claim

ACT-R production compilation and Soar chunking are already used in [the two-layer execution-system note](../../notes/theory-and-methodology-form-a-two-layer-execution-system.md). The scans add one warning worth retaining: a learned fast path is not merely a shorter trace. It asserts that a result depends on some conditions and not on discarded intermediate context.

That makes compilation a lineage and generalization problem:

1. identify the recurring expensive resolution;
2. infer the minimal conditions on which it depended;
3. choose a retained form with the required authority;
4. verify the new artifact on repeats and near-neighbors;
5. retain a fallback outside its coverage boundary;
6. invalidate or review it when dependencies change.

This appears already covered locally by the fast-path/fallback and codification notes. Further architecture reading would mainly improve provenance and supply failure cases; it should not create a duplicate general claim.

## Pattern 5: representation can be assembled during inquiry

[Copycat](./copycat.md) and [DUAL](./dual.md) resist a pipeline in which a fixed representation is retrieved first and reasoning begins second. Candidate correspondences, conceptual relevance, and active coalitions change together. [Parallel terraced scan](./parallel-terraced-scan.md) adds a resource policy: cheap processes explore many partial representations and allocate depth as coherence or information value grows.

For Commonplace, this suggests that connection discovery should not be evaluated only as top-k retrieval. A strong process may:

- retrieve an initial anchor;
- form several possible relations;
- use each relation to seek different evidence;
- revise which artifact features matter;
- preserve competing mappings until one explains more of the structure;
- state the conceptual "slippage" required for any analogy.

This could explain why short, composable notes matter beyond retrieval: they can participate in several transient coalitions without requiring one fixed place in a taxonomy. It also gives a process interpretation to [fluid resolution switching](../../notes/a-knowledge-base-should-support-fluid-resolution-switching.md).

**Significance test:** compare single-pass connection retrieval with an iterative mapping-and-retrieval process on cases where the decisive relation has low lexical similarity. Require external or internal evidence to judge the final relation; coherence alone is insufficient.

**Best grounding comparison:** Copycat plus parallel terraced scan. DUAL is secondary unless its coalition mechanics add a clearly different prediction.

## Pattern 6: capacity is a vector and scheduling is architectural

[4CAPS](./4caps.md) makes capacity local to cooperating centers, while [EPIC](./epic.md) models parallel components and executive scheduling. Together they caution against treating total context or elapsed time as explanations.

Commonplace already distinguishes soft context degradation across volume, complexity, and interference. The possible addition is methodological: predict a **load signature** across retrieval, interpretation, judgment, tool I/O, coordination, and verification, then perturb one channel. Extra calls or agents count as recruitment only when they relieve the limiting resource after handoff and reintegration costs.

This seems more likely to improve evaluation methods than ontology. It should be tested in the existing orchestration or context-efficiency work before becoming a durable note.

## Pattern 7: plans are not intentions, and shared state is not shared understanding

[PRS](./procedural-reasoning-system.md) distinguishes goal, applicable plan, committed intention, execution, and reconsideration. [R-CAST](./r-cast.md) adds a team-level conjecture: good coordination models what information another actor needs for its pending decision rather than broadcasting everything.

Together they yield a compact control sequence:

```text
goal → candidate plans → applicability → commitment → execution →
monitoring/reconsideration
                     ↑
        decision-relevant handoff/context
```

This is directly relevant to the [chatbot goal-state workshop](../chatbot-goal-state/README.md). A later user message can change belief state, satisfy a pending dependency, alter plan choice, revoke commitment, or replace the goal. Treating all five as "new context" guarantees control errors.

**Best grounding comparison:** PRS first, because its distinctions appear capable of changing the computational model. R-CAST only if multi-actor information-push or handoff policy becomes a live implementation question.

## Pattern 8: an architecture should predict traces or perturbation effects

The most reusable research method across the stronger memories is not a particular component diagram. It is commitment to intermediate consequences:

- ACT-R predicts retrieval and production events;
- Soar predicts impasses, substates, and chunks;
- LIDA predicts competition and broadcast stages;
- EPIC predicts resource overlap and bottlenecks;
- CHREST/EPAM predict learned recognition paths;
- HTM predicts expected transitions and anomaly;
- Copycat predicts changing candidate structures.

For Commonplace, any architecture claim should identify an observable trace or counterfactual intervention that differs from a simpler account. "The KB is semantic memory" is decorative. "Adding this discriminator changes which near-neighbor is opened before body text is loaded" is testable.

This may be the workshop's highest-reach methodological conclusion: borrow architectures as **hypothesis generators for process-level tests**, not as vocabularies for redescribing components.

## Initial grounding queue

Grounding should begin only when a candidate meets the stated trigger. The current order is:

1. **PRS goal/plan/intention/reconsideration** — ground when the chatbot goal-state work chooses a computational model that needs these distinctions.
2. **ACT-R versus LIDA access stages** — ground when a worked activation failure cannot be diagnosed by the current read-back/activation vocabulary.
3. **Copycat plus parallel terraced scan** — ground before designing or claiming an iterative connection-discovery scheduler.
4. **CHREST/EPAM confusion-driven indexing** — ground when a real routing error motivates a new discriminator or template rule.
5. **OpenCog truth versus attention values** — ground when a selector or queue needs to combine confidence, priority, utility, and authority.
6. **Soar impasse/chunking safeguards** — the broad analogy is already locally cited; read more only if Commonplace designs an impasse-extraction mechanism.
7. **EPIC/4CAPS resource models** — ground when a concrete orchestration experiment needs predicted component loads.
8. **HTM sequence anomaly** — ground when retrospective episode or workflow-transition memory becomes active implementation work.

ASMO, MAMID, Mibe, SOSIEL, and TinyCog should not receive completeness-driven research effort yet. Their scans preserve possible hooks and uncertainty without claiming that every historical entry deserves equal attention.

## Candidate extraction ledger

| Candidate | Present disposition | Evidence needed before promotion |
|---|---|---|
| Multi-stage access/activation trace | possible refinement of an existing note | at least two real failures requiring different interventions |
| Typed selection values | possible operational ontology | one live selector harmed by scalar collapse |
| Trigger → missing capacity → artifact form | promising synthesis | several trace cases producing different retained forms |
| Compilation as scoped dependency | already substantially covered | no new artifact unless a missing safeguard appears |
| Iterative representation/retrieval | promising experiment | benchmark with low-lexical, structurally decisive relations |
| Vector capacity/load signatures | evaluation method candidate | perturbation experiment on a real agent workflow |
| Goal/plan/intention state | live adjacent-workshop candidate | control cases distinguishing user-update types |
| Trace-predictive architecture criterion | high-reach methodology candidate | test against several architecture claims in existing reviews |
