# Reflective improvement divergence: problem map

This is a provisional synthesis, not a settled vocabulary or theory. Its purpose is to preserve the current leads while making their differences visible enough to test.

## Candidate central claim

> An open-ended self-improvement pathway needs episode closure, not convergence.

Further improvement may always be possible. A system therefore cannot generally wait until no candidates remain, all concerns have disappeared, or its behavior-determining organization has reached a fixed point. It needs a decision that another improvement step is not currently worth more than returning resources and control to the objective the pathway serves.

The stronger reflective hypothesis is that the stop decision is unusually unstable when the pathway can revise the representations and machinery through which it searches, evaluates, retains, scopes, and terminates improvements.

## Distinctions to preserve

| Working phenomenon | What changes or fails to settle | Why it may matter |
|---|---|---|
| Lifetime open-endedness | The system remains improvable after an episode | Usually desirable; not itself a failure |
| Search non-convergence | Candidate generation continues finding alternatives | Requires allocation or marginal-value stopping, not necessarily artifact repair |
| Revision drift | Successive candidates move away from the seed or change its identity | May be legitimate split/kill/reframing, or loss of the original task |
| Oscillation | Later revisions undo or reopen earlier revisions | Consumes evaluation without durable progress |
| Scope expansion | Improving one surface exposes or admits further surfaces | Can turn a bounded repair into an unbounded system rewrite |
| Criterion drift | The objective, proxy, evaluator, or acceptance rule changes during search | Earlier progress and comparisons may cease to be commensurable |
| Operational non-termination | Improvement processing does not yield to object-level operation | Converts possible local improvement into system-level opportunity cost |
| Stock divergence | Retained changes accumulate without retirement or reconciliation | A lifecycle failure distinct from one episode failing to halt |

The likely unifying object is not artifact similarity or mathematical convergence. It is **control allocation under a moving improvement frontier**. The workshop should test that rather than assume it.

## Provisional mechanism

1. An objective exposes a defect or opportunity in behavior-determining organization.
2. The improvement pathway generates a candidate change.
3. Evaluation of the candidate or inspection of the changed system reveals another possible change.
4. In a reflective system, that new target may be part of the pathway itself: its representation, search policy, evaluator, retention path, scope rule, or scheduler.
5. Revising the pathway can enlarge or move the frontier against which completion was being judged.
6. If the scheduler treats “another useful change exists” as “continue this episode,” the loop has no reason to yield while any addressable defect remains.
7. Object-level work is displaced even when each accepted local change is defensible.

This suggests a possible pathology of [compounding](../../notes/improvements-can-accumulate-without-compounding.md): when retained improvements to defect-finding help produce later improvements, they can raise the arrival rate of candidates faster than evaluation and repair discharge them. The pathway becomes locally more capable and operationally less terminating.

## Initial cases

### Gas Town and the “just two more things” behavior

In [The Shape of Things to Come](https://yegge.ai/essays/the-shape-of-things-to-come/), Steve Yegge reports that Gas Town worked through one model version but failed with a later model that continually wanted to make “just two more things” better in Gas Town before beginning real work. On his account, the model never converged on readiness and the harness became unusable.

What the report may evidence:

- an open, salient self-modification surface can capture foreground work;
- changing the model can change termination behavior without changing the retained harness artifacts;
- locally plausible harness work can be globally harmful through displaced task work.

What it does not distinguish:

- revision non-convergence versus simple task-routing preference;
- whether the harness lacked a stop rule, failed to enforce one, or supplied an objective that rewarded continued self-work;
- whether the revisions improved Gas Town locally;
- frequency, generality, or reflection-specific causation.

### Automated note refinement

[Automated note refinement as a search over a fixed source bundle](../../reference/proposals/automated-note-refinement-as-search-over-source-bundle.md) identifies a structural non-convergence case: a good refinement may split a note, drift from its seed, or conclude the note should not exist. It responds by changing the search object and using budget exhaustion or incumbent survival rather than artifact stability as the stopping rule.

This is a design proposal, not evidence that reflective systems generally diverge. It does establish a concrete architecture in which convergence of one identity-stable artifact is the wrong success condition.

### Commonplace full-improvement closure

[Full improvement pass closure](../../reference/full-improvement-pass-closure.md) reports that all five calibration passes ended with residual Open items. The workflow deliberately runs one closing assay cycle, records remaining findings, and stops rather than initiating another edit/review round.

This is a bounded operational response to the possibility that every repair reopens another concern. It shows that inspected closure without convergence can be implemented. It does not show that an unbounded version would actually diverge, nor that one closing cycle is optimal outside that workflow.

### Gödel machine

The [Gödel-machine account](../../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md) makes “switch now versus continue searching” part of the proof obligation. This treats continued improvement search as an alternative action with opportunity cost, not as free background computation. It is a formal limiting case rather than an implemented empirical instance, but it suggests that the halt/continue allocation is intrinsic to self-modification architecture.

### Deferred traversal improvements

[Traversal improvements should be deferred via logging](../../notes/traversal-improvements-should-be-deferred-via-logging-to-avoid-mid.md) handles a small recurring form of control capture: ordinary work continually exposes nearby KB improvements. Recording the signal and processing it in a separate pass preserves the opportunity without letting it recursively interrupt the current task.

The mechanism is weaker than reflective self-improvement—the traversing agent need not modify its own improvement machinery—but the pattern supplies a non-reflective or weakly reflective comparison for whether episode separation alone repairs the problem.

## Rival explanations

Do not let “reflection causes divergence” absorb failures better explained by:

- an underspecified task or missing completion criterion;
- a scheduler that never imposed a step or resource bound;
- reward hacking against a proxy for visible activity;
- novelty preference or a model-specific reluctance to declare completion;
- poor task routing that makes harness work more salient than object work;
- a weak evaluator that cannot compare the marginal value of another revision with deployment;
- missing retirement, which grows state across episodes rather than preventing one episode from ending;
- ordinary optimization on a non-convex or changing environment with no self-representation involved.

The reflection-specific claim survives only if revisability of the pathway's own representations or machinery explains behavior beyond these generic causes.

## Candidate controls

These are hypotheses to compare, not a recommended bundle:

- **Hard episode budget** — stop after a fixed time, cost, token, step, or candidate bound.
- **Incumbent survival** — stop after no challenger beats the best-so-far candidate for a declared number of rounds.
- **Marginal-value decision** — compare the expected benefit of another improvement step with returning to operation.
- **Phase boundary** — improvement signals discovered during object work enter a queue rather than opening nested revision immediately.
- **Stable in-episode contract** — freeze objective, evaluator, scope, and stop rule for one episode; permit their governed revision only between episodes.
- **External adoption decision** — allocate the final “no more now” outside the candidate or machinery currently being judged.
- **Residual-finding retention** — preserve unresolved concerns so stopping does not require pretending they were solved.
- **Rollback and localized acceptance** — contain the cost of drift and oscillation when an accepted change later proves harmful.
- **Opportunity-cost accounting** — measure displaced object-level throughput, human judgment, and maintenance rather than only quality of accepted revisions.

The most consequential candidate is the stable in-episode contract. A stop rule that the active revision can relax whenever it encounters the boundary is not a stop rule. But freezing it forever would contradict the reflective aim. The possible resolution is time-indexed governance: fixed during an episode, addressably revisable between episodes under a separate decision.

## Predictions and discriminating observations

1. Strengthening a critic without adding an episode budget will increase findings and episode length more reliably than it increases completed object-level work.
2. Systems that may revise their scope or stop rule during the active episode will show longer and less predictable tails than systems that freeze them until the next episode.
3. Deferring newly noticed improvements should reduce task interruption while retaining most later improvement value, provided the deferred queue has a reliable retrieval and processing path.
4. A system can show improving local revision scores while declining against its declared objective once opportunity cost is counted.
5. Model upgrades will sometimes change convergence behavior even with identical retained artifacts, because the model is part of the interpreter implementing the stopping policy.
6. Hard-oracle domains will support marginal-value stopping more readily than semantic or aesthetic domains, where “another concern exists” is cheap to generate and expensive to discharge.

## Candidate durable outputs

- **Theory note:** *An open-ended self-improvement pathway needs episode closure, not convergence.*
- **Theory note or scope section:** reflection's distinctive contribution is a moving improvement frontier, not generic non-termination.
- **Methodology:** freeze the active episode's objective, evaluation contract, scope, and stop rule; route proposed changes to those surfaces into a later episode.
- **Extension to the reflective-self-improvement article:** add divergence and episode closure as a failure surface only after the general claim survives comparison with non-reflective optimization.

No output is committed in advance. The workshop may instead conclude that search, revision, state accumulation, and operational non-termination need separate notes with no useful “divergence” umbrella.
