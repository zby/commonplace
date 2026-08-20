# Local case corpus

## Selection rule

This is not an inventory of LLM failures. A case belongs only if it helps distinguish at least two of these possibilities:

- the agent lacks the relevant responsibility or argument model;
- it has the model but does not construct or activate it for the current unit;
- immediate context conditions a local proposal before any global comparison;
- the controller stops after local adequacy without running structural review;
- it notices an oddity but does not value it enough to interrupt;
- it does not turn the oddity into a structural subgoal;
- it diagnoses the issue but generates only local or additive remedies;
- it generates both kinds but an explicit oracle does not select the stronger design; or
- it selects the design but cannot carry it through safely.

For prose, a case is relevant only when the target material is locally defensible: true or plausible, topically connected, and reasonably fluent. An irrelevant sentence is an easy coherence defect, not the proposed failure. The evidence must say why the unit does not earn its present argumentative role, size, or position. A human accepted edit is a candidate reference, not unique ground truth.

## Software cases and fixtures

### Freshness review: tests passed while a user-facing path could never succeed

The [freshness-module review](../freshness-module-review/README.md) began only after a full code review for bugs, inconsistencies, and overengineering was requested. All 18 tests passed. The review nevertheless found that `commonplace-freshness-accept` rejected every possible target kind, leaving a shipped CLI and roughly 95 lines of its body unreachable; the two tests for the path asserted that it raised. The [findings](../freshness-module-review/findings.md) also separated caller-enforced invariants, a default that disables compare-and-swap, dead exports, redundant work, and unresolved retention policy.

This is a useful fixture because the local check is explicit: the tests accurately preserved the disabled behavior while failing to ask whether a command that can only fail should exist. Once the broader question was commissioned, the agent could identify the design problem and recommend deletion rather than another guard.

**What it isolates:** behavioral test success can coexist with a design anomaly, and an agent can diagnose the anomaly when the task is widened from test correctness to architectural review.

**What it does not show:** that an implementation agent saw the anomaly and ignored it, because the original construction trace is unavailable.

### Commissioned architecture search: explicit framing produces global alternatives

The [source-architecture alternatives survey](../src-architecture-alternatives/alternatives-survey.md) distinguishes helper extraction from missing models: duplicated parsing becomes a proposed load-once KB graph, and duplicated execution paths become one staged pipeline. This is a positive comparison because explicit instruction to search the architecture produces non-local, potentially subtractive models. It supports an activation or task-framing lead, but cannot establish that the same alternatives would be originated, selected, or implemented during a bounded feature task.

## Natural-language cases and fixtures

These cases concern artifact role rather than generic prose quality. None preserves an original online trace in which an agent spontaneously encountered and ignored the anomaly; they are frozen revision cases and capability controls for constructing that experiment. Exact passages and admission gaps are separated in the [prose fixture candidates](./prose-fixture-candidates.md).

### 1. Semantic value did not imply positional value

In [agent-note-improvement case 02](../agent-note-improvement/case-02-prose-dereference/README.md), a standalone `Scope` section contained a useful representational-form boundary. The ordinary semantic gates passed it and the load-bearing-qualifier gate positively defended it because the qualifier protected the claim's truth. A purpose-built marginal-value gate instead found that the unit did not earn a standalone section: the mechanism already implied most of the boundary, so one useful phrase should be folded earlier and the section deleted.

This is close to the user's target observation. Nothing inside the section is obviously bad, and it is connected to the note's topic. The high-altitude question is different: what unique job does this section perform relative to the rest of the artifact?

**What it isolates:** semantic correctness and local relevance are weaker than justified placement and size; local semantic checks can defend material that a whole-document marginal-value review recommends folding or removing.

**What it does not show:** spontaneous failure to notice, unique correctness of the human preference, or sentence-level misplacement without a controlled perturbation.

### 2. Useful support became a second thesis

In [agent-note-improvement case 03](../agent-note-improvement/case-03-adversarial-loop-writing-filter/README.md), a paragraph about corpus connection work was coherent and interesting but changed the note's remembered center of gravity from reconstructing the writing-is-thinking filter to defending corpus-scale agent work. The [compression review](../agent-note-improvement/case-03-adversarial-loop-writing-filter/compression-bundle-review.md) called it a separate defense that competed with the note's main claim. The successful revision folded it into one secondary-payoff sentence.

This is the strongest current candidate for “topically related but globally misplaced.” The paragraph supports the broad subject associatively while occupying too much of the document's argumentative budget and role.

**What it isolates:** a locally valuable paragraph can compete with the artifact's intended thesis; whole-document role and remembered center are not reducible to sentence quality.

**What it does not show:** that folding is uniquely correct or that an unprompted agent would fail to propose it. The case must be independently role-annotated and perturbed before use as an experimental fixture.

### 3. Correct diagnosis elicited additive defense rather than deletion

In [agent-note-improvement case 01](../agent-note-improvement/case-01-llm-generation-relaxes-goals/README.md), the accepted revision removed speculative branches while preserving the witness-relaxation mechanism. Generic critique correctly found overclaiming but mostly proposed qualifications, comparison units, workflow distinctions, and new sections. A purpose-built pruning instruction came closer yet still wanted to compress or preserve material the accepted edit deleted. A split/rehome frame did best, while still proposing more future notes than the accepted revision kept.

**What it isolates:** in these runs, issue detection, structural candidate generation, and edit choice separated; a correct concern was followed by preservation and addition rather than the reference deletion.

**What it does not show:** whether preservation was caused by curiosity, training, politeness, loss aversion, or a defensible preference for retaining ideas. It is branch-level revision, not yet a sentence-placement experiment.

### 4. Local gates missed or mishandled whole-document operations

The [gated revision change catalogue](../review-revise-gated/change-catalogue.md) records a human target containing sentence fixes and whole-document operations. By [run 08](../review-revise-gated/run-08/scores.md), focused gates detected 14 of 16 target changes, but the two true misses were merging overlapping sections and compressing an overweight taxonomy. A dedicated bridge-duplication gate finally detected a repeated preview, yet the reviser deleted the wrong sentence and left the bridge. The [noise audit](../review-revise-gated/run-08/gate-noise-audit.md) also shows a completeness gate correctly sensing soft taxonomy boundaries but recommending expansion when the target compressed the taxonomy.

**What it isolates:** local detection, global diagnosis, operation selection, and operation execution are distinct. Making a lens more specific can surface an anomaly without supplying the correct structural edit.

**What it does not show:** a common cause across all misses or that every target human edit was uniquely superior.

### 5. Explicit section ownership and deletion permission provide a capability ceiling

The [auditable editing experiment](../auditable-llm-editing/README.md) supplies a positive prose control. Direction `D009` explicitly said to “delete duplicated statements rather than adding another paragraph.” `D010` assigned each section one theoretical job, and `D014` supplied a full desired section-role map plus aggressive deletion permission. The accepted `CAND014` materially compressed the theoretical prelude while its verification recorded all ten tracked claims as preserved.

**What it isolates:** an agent can execute a global, subtractive prose revision when section ownership, the anomaly class, and much of the operator are supplied.

**What it does not show:** spontaneous anomaly registration, subgoal origination, or independent discovery of the desired section model. It anchors the specified-transformation end of the intervention ladder.

## A required prose counterexample: local redundancy can be correct

[Local materialization should outperform distant natural-language declarations](../../notes/local-materialization-should-outperform-distant-declarations.md) advances an untested statistical conjecture: for distant or non-obvious uses, a generated local view from one canonical value should outperform declaration-only presentation. It distinguishes generated exact or derived views from human-authored restatement and makes a held-out correct, non-contradictory application rate the primary comparison.

This blocks a naive transfer from software: duplication, locality, or addition is not itself a prose smell. A valid experiment must show role conflict or a downstream cost, not merely that two sentences overlap. A counterexperiment should compare canonical-only, point-of-use reinforcement, and checked canonical-plus-local reinforcement on both immediate uptake and later revision drift. If deliberate reinforcement wins, the shared theory must concern global-role conflict rather than subtraction or single-source organization in general.

## Conditional analogues, quarantined from the base case

These artifacts may supply later experimental methods, but they are not evidence for locally connected global misplacement and should not be counted toward closure:

- The [linking-foundations retrospective](../linking-foundations/automation-boundary-retrospective.md) records a human-originated question followed by strong agent reasoning once framed.
- The [Decapod curiosity experiment](../curiosity-prompts/experiment-report.md) suggests that question framing changes what gets investigated, but has only two trials per condition.
- [Agents Explore but Agents Ignore](../../sources/agents-explore-but-agents-ignore-llms-lack-environmental.ingest.md) separates information surfacing from later interaction in artificial agent tasks.
- The local [SlopCodeBench practitioner run](../../sources/why-software-factories-fail-slopcodebench-2081797628552270027.ingest.md) is a small lead on iterative code erosion, not its mechanism.
- The [failure-mode transfer note](../../notes/human-writing-structures-transfer-to-llms-because-failure-modes.md) supplies a cross-domain evaluation rule, not evidence that this particular behavior transfers.

## What the local corpus does not yet contain

- A preserved implementation trace where an agent encounters responsibility in the wrong module, applies a local workaround, and never raises the structural concern.
- An admitted prose perturbation independently shown to be locally coherent but globally role-incongruent, with unrelated, correct-placement, and genuine-bridge controls.
- An online prose task where the agent works next to the misplaced unit and has an opportunity to originate a rehoming subgoal before retrospective review is requested.
- A stage-separated comparison of open noticing, role-model diagnosis, structural-candidate generation, identical-set selection, and exact execution in both domains.
- Evidence that software and prose share a stage-specific intervention signature rather than only an additive-looking output.

Those absences define the experiment and web-search priorities. They also prevent the current corpus from supporting a broad claim that curiosity is the fundamental cause of poor structure or that one trained faculty produces both domains' failures.
