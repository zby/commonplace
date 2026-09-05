# Examples: the bootstrap article, 2026-09-05

Every edit made to `kb/articles/bootstrapping-the-first-automated-software-house.md`
by the operator-led method, with the agent's diagnosis and the text before and
after, taken from the commits verbatim. This run differs from the first two:
the operator asked the agent to "do as much as you can on your own", so there
was no phase 1. The agent read the two earlier examples files, did the
whole-article read (README step 2), reported its conceptual findings, and ran
the phase-2 sweep from the accepted kinds alone, applying each edit as its own
commit. **No edit below has an operator verdict yet.** Each is a prediction
that the operator would accept it; a reverted commit is a refutation and
should be recorded here as such.

Operator's instruction for the run: "use
kb/work/operator-led-article-clarification/ on
kb/articles/bootstrapping-the-first-automated-software-house.md - but do as
much as you can on your own - you can find dense paragraphs or trasitions
between paragraphs and check them"

## Whole-article read: findings not acted on

Reported for the operator's decision, per README step 2. None was edited in the sweep; all five were applied afterward on the operator's verdict (examples 20 to 24 below).

1. **Possible vestigial framing: the trial-boundary sentence.** "A trial's
   boundaries identify the decisions being assessed; they need not fix the
   house's future products or responsibilities" (section "Two kinds of
   transfer") was added by `08215a3d` when declared product scope left the
   software-house definition. With scope gone from the series, the reader has
   no reason to think a boundary would fix future products, so the sentence
   reads as a defence against a reading the article no longer invites. It may
   still be wanted as a positive statement; that is the operator's call.
2. **Not a lost claim, but worth a look: the TL;DR and the residue
   prediction.** The TL;DR states the program (start human-agent, transfer
   bounded classes, two tests per trial, evidence picks the next). It does
   not mention the readiness/residue prediction (transfer the best-supported
   decisions first and people are left with the hardest-to-warrant ones),
   which the readiness section and the closing section treat as the route's
   distinctive content. The frontmatter description does not mention it
   either, so this is consistent rather than mangled; the question is whether
   the operator wants it in the TL;DR.
3. **Two terms across the series: *explanation* and *account*.** The trial
   section calls the same retained artifact "a retained explanation", "the
   incomplete dependency account", "retained account", and "the account's
   contribution". The training article uses both terms too, so a fix would be
   series-wide and was not attempted.
4. **A verdict whose why is inferred, left alone.** "The same production
   history that supports a transfer must also be able to reveal these
   failures" closes the stop-conditions section. The agent's best reading
   (a history that can only confirm success is the self-confirming
   evaluation named two bullets earlier) is inferred, not stated nearby; per
   the training-article run's lesson it is flagged, not written in. Proposed
   text if the reading is right: "The records that count as evidence for a
   transfer must be able to show these failures too; a history that can only
   confirm success is the self-confirming evaluation above."
5. **Minor unintroduced terms not touched.** *Reopened roles* in the TL;DR
   (defined only in "How each trial is specified"); *viability* among the
   update drivers in "What the house's training must produce".

## Edits applied


## 1. The validator example

- **Commit:** `7d5d9988`
- **Kind:** Unlabelled example; compressed description
- **Operator's verdict:** none yet; applied autonomously, pending review
- **Diagnosis:** A hand-written validator was mapped onto the operational/learning distinction without being announced as an example, and "its criterion" had no clear owner. Fixed by announcing the example, saying what computation now does on the operational side, and naming the validator's criterion and machinery on the learning side.

**Before:**

> A hand-written validator can complete operational transfer. Learning transfer
> requires the house to produce or revise its criterion and machinery from
> experience.

**After:**

> The difference shows in a simple case. A validator that a person wrote can
> complete operational transfer: computation now makes the decision. Learning
> transfer requires the house to have produced or revised the validator's
> criterion and machinery from its own experience.

## 2. The seed paragraph

- **Commit:** `b83c2aa6`
- **Kind:** Unsignposted roles; unsignposted transition
- **Operator's verdict:** none yet; applied autonomously, pending review
- **Diagnosis:** Four jobs in one paragraph (seed permission, two definitions, the training proposal's question, the bootstrap's aim) with no transitions, and no link back to the validator example just above. Fixed with an opening that ties the permission to the example, definitions marked as local unpacking, and the proposal introduced as a further question. A stronger rewrite that mapped the two transfers onto the two articles was rejected by the agent because the conjecture's conditions 1 and 2 already require revision of retained machinery, so the mapping would have been a wrong why.

**Before:**

> The conjecture permits a human-built seed, provided the house applies its
> program theory, revises coherently, and continues reliably without human
> production decisions. Program theory means understanding the software's purpose,
> organization, and how to handle new requests.
> An explicit project theory is one possible written carrier of that understanding,
> stating design commitments, causal assumptions, and invariants. The conjecture
> also permits reconstructing understanding from records.
> The separate proposal to [train the house from
> production](./the-software-house-as-the-unit-of-training.md) asks whether its
> own process can also produce the project-specific machinery. The bootstrap
> aims at both transfers.

**After:**

> The conjecture allows that: it permits a human-built seed, provided the house
> applies its program theory, revises coherently, and continues reliably without
> human production decisions. Program theory here means understanding the
> software's purpose, organization, and how to handle new requests. An explicit
> project theory is one possible written carrier of that understanding, stating
> design commitments, causal assumptions, and invariants; the conjecture also
> permits reconstructing understanding from records. The separate proposal to
> [train the house from production](./the-software-house-as-the-unit-of-training.md)
> asks a further question: whether the house's own process can also produce the
> project-specific machinery. The bootstrap aims at both transfers.

## 3. Admission: what a verdict does not decide; "global fit"

- **Commit:** `3d6d9a18`
- **Kind:** Verdict without its why; compressed description
- **Operator's verdict:** none yet; applied autonomously, pending review
- **Diagnosis:** "A verdict does not select the retained revision" stated a limit without saying what the review system leaves undone. "Selected global fit" compressed the evidence note's finding (the operator's decisive feedback concerned fit with the research program as a whole). Both said plainly, from the sources.

**Before:**

>   note and criterion snapshots; a verdict does not select the retained revision.
>   One episode records [the model retrieving theory and producing edits while
>   the operator selected global fit](../notes/evidence/commonplace-revision-used-theory-guided-computational-search.md).

**After:**

>   note and criterion snapshots; choosing which revision is kept is a separate
>   decision that a verdict does not make. One episode records [the model
>   retrieving theory and producing edits while the operator judged which
>   fitted the research program as a
>   whole](../notes/evidence/commonplace-revision-used-theory-guided-computational-search.md).

## 4. Credit assignment: what freshness tracks

- **Commit:** `df6fca16`
- **Kind:** Compressed description; verdict without its why
- **Operator's verdict:** none yet; applied autonomously, pending review
- **Diagnosis:** "Tracks changed review inputs, treating linked files as reading context" compressed two facts from `kb/reference/review-architecture.md` and left the reader to infer why input tracking is not credit assignment. Both facts stated, inference drawn.

**Before:**

>   The [freshness model](../reference/review-architecture.md) tracks changed
>   review inputs, treating linked files as reading context. It does not establish
>   that an earlier change caused a later outcome; people still help attribute failures.

**After:**

>   The [freshness model](../reference/review-architecture.md) tracks which of
>   a review's inputs have changed since its verdict; files the note links to
>   count as reading context, not as tracked inputs. Knowing that an input
>   changed does not establish that an earlier change caused a later outcome, so
>   people still help attribute failures.

## 5. "Missing functions" and the decision count

- **Commit:** `fb6ba09c`
- **Kind:** Unintroduced term (forward reference); verdict without its why
- **Operator's verdict:** none yet; applied autonomously, pending review
- **Diagnosis:** "Missing functions" appeared before the section that defines the functions; now points forward. "Count internal decisions" gave its reason without saying what the count replaces (people or roles); the contrast is now stated.

**Before:**

> current division of work is itself the problem. Exploratory trials can expose
> missing functions while people remain involved. Their results should guide
> which responsibilities to transfer and how to group them.
>
> Count internal decisions still supplied by people: one operator may stop
> performing one role while retaining several others. The program needs evidence
> of transfer without assuming a fixed order or steady progress at every step.

**After:**

> current division of work is itself the problem. Exploratory trials, run while
> people remain involved, can expose which functions the house still lacks, and
> their results should guide which responsibilities to transfer and how to group
> them. The next section names those functions.
>
> Measure progress by counting the internal decisions people still make, not the
> people: one operator may stop performing one role while retaining several
> others. The program needs evidence of transfer without assuming a fixed order
> or steady progress at every step.

## 6. Readiness, warrant, and the residue

- **Commit:** `78269b16`
- **Kind:** Unintroduced term (two terms for one concept); unlabelled parallel
- **Operator's verdict:** none yet; applied autonomously, pending review
- **Diagnosis:** The heading said *readiness conditions*, the body said *warranted transfer*, and nothing said they were one concept. The residue sentence listed four things people would handle without saying they are the four ways a decision fails the conditions just stated.

**Before (hunk 1):**

> A warranted transfer requires the necessary premises, a settled acceptance
> rule or grant of authority, and a check independent enough to reject a
> plausible harmful candidate. It also requires continuity when the decision or
> its evidence arrives after the current run.

**After (hunk 1):**

> A transfer is ready, or *warranted*, when the deciding process has the
> premises it needs, a settled acceptance rule or grant of authority, and a check
> independent enough to reject a plausible harmful candidate. It also needs
> continuity when the decision or its evidence arrives after the current run.

**Before (hunk 2):**

> increasingly handle missing premises, unsettled criteria, weak checks, and
> delayed consequences. The [residue

**After (hunk 2):**

> increasingly be left with the decisions that fail one of these conditions: a
> missing premise, an unsettled criterion, a weak check, or a delayed
> consequence. The [residue

## 7. The four functions and the division that may go

- **Commit:** `9f377312`
- **Kind:** Unlabelled parallel; unclear referent
- **Operator's verdict:** none yet; applied autonomously, pending review
- **Diagnosis:** Four functions listed without mapping to the table rows they answer; "need not preserve that division" had no referent. Mapping taken from the residue-classes note's table; the closing clause now says what the note says (functions stay separate, carriers need not). A first draft added "respectively" to the Commonplace carriers and was dropped: the note's continuity realization is persistent state and scheduling, not retained evidence, so the one-to-one claim would have been invented precision.

**Before:**

> try next. The remaining decisions require different
> [functions](../notes/residue-classes-need-different-mechanisms-so-architecture-is-mixed.md):
> representation, interpretation, verification, and continuity. Commonplace uses
> notes, models, code, and retained evidence to supply them; a final house need
> not preserve that division.

**After:**

> try next. The decisions that are not ready each need a different
> [function](../notes/residue-classes-need-different-mechanisms-so-architecture-is-mixed.md)
> to grow before they can move: representation for a missing premise,
> interpretation for an unsettled criterion, verification for a missing check,
> and continuity for a decision that arrives late. Commonplace currently supplies
> these functions with notes, models, code, and retained evidence; a final house
> need not keep them in separate kinds of carrier.

## 8. Which change in checking

- **Commit:** `b35a96e7`
- **Kind:** Compressed description
- **Operator's verdict:** none yet; applied autonomously, pending review
- **Diagnosis:** "A change in checking" stood in for the consequence the example sets up: Markdown files the exporter now reads need the manifest check the exemption withheld.

**Before:**

> the explanation should guide a change in checking. A further change introduces

**After:**

> the explanation should lead the house to extend manifest checks to those
> files. A further change introduces

## 9. Evidence and authority

- **Commit:** `506377a3`
- **Kind:** Unsignposted roles; unintroduced term
- **Operator's verdict:** none yet; applied autonomously, pending review
- **Diagnosis:** The paragraph's heading promised authority but nothing marked where that part began, and *reference judgment* arrived as a new term in the last sentence. A first draft said authority stays "outside the house" and was dropped: in a component trial the house under test is the selector, so "split" is what the text supports.

**Before:**

> complete automated house exists. An independent manifest
> check could reject a claimed improvement even after the revised selector
> accepts the edit. The selector being evaluated must not control that reference
> judgment.

**After:**

> complete automated house exists. Authority over the result is split: an
> independent manifest check, the *reference judgment*, can reject a claimed
> improvement even after the revised selector accepts the edit, and the selector
> being evaluated must not control that check.

## 10. The full-suite baseline

- **Commit:** `fff192e8`
- **Kind:** Verdict without its why
- **Operator's verdict:** none yet; applied autonomously, pending review
- **Diagnosis:** "Provides a useful baseline" without the reason the previous sentence set up: the transfer is judged on outcomes and cost, and the full suite fixes the outcome end. The why is adjacent, so it was written in.

**Before:**

> transferred decisions. Always running the full suite provides a useful baseline.

**After:**

> transferred decisions. Always running the full suite is the baseline: it misses
> nothing, so a selector must match its outcomes at lower cost.

## 11. The paired comparison

- **Commit:** `88824314`
- **Kind:** Compressed description
- **Operator's verdict:** none yet; applied autonomously, pending review
- **Diagnosis:** "Compare the revised state with its earlier version ... controlling other carriers of the learned information" compressed the training article's paired-continuation design. Said as the design would be described: two copies, one snapshot, one revised and one restored, untouched cases, other carriers held fixed.

**Before:**

> later decisions. One way to isolate that contribution is to compare the revised
> state with its earlier version on identical product snapshots and untouched
> cases, controlling other carriers of the learned information.

**After:**

> later decisions. One way to isolate that contribution is to run two copies of
> the house from identical product snapshots, one keeping the revised state and
> one with its earlier version restored, on cases the failure did not touch,
> while holding fixed every other place the learned information could be carried.

## 12. The two predictions and the separate error record

- **Commit:** `563f6b1d`
- **Kind:** Verdict without its why (two sites)
- **Operator's verdict:** none yet; applied autonomously, pending review
- **Diagnosis:** "Test different predictions" and "record initial errors separately" both had their reasons in the training article's advantage hypothesis (preserving changes favour the theory treatment; breaking changes may reverse it; rapid recovery erases the initial loss). Checked against that section before writing them in.

**Before:**

> plausible wrong theory. Changes that
> preserve the initial dependency account and changes that break it test different
> predictions. Record initial errors separately from recovery after feedback.

**After:**

> plausible wrong theory. Changes that preserve the initial dependency account
> and changes that break it test different predictions: the first should favour
> the theory treatment, while the second may cancel or reverse that advantage
> until the account is revised. Record initial errors separately from recovery
> after feedback, because rapid recovery can hide the initial loss in a whole-run
> score.

## 13. Trial vocabulary: continuation, local trial

- **Commit:** `cb91bd42`
- **Kind:** Unintroduced term (borrowed from a sibling article); one term per concept
- **Operator's verdict:** none yet; applied autonomously, pending review
- **Diagnosis:** *That continuation* borrowed the training article's term for paired copies of a house with no antecedent here; the sentence means the run under test. *Local trial* was a one-off qualifier.

**Before (hunk 1):**

> operation for that continuation, while still informing the next trial.

**After (hunk 1):**

> operation for that run, while still informing the next trial.

**Before (hunk 2):**

> The example makes explicit what every local trial needs before it runs:

**After (hunk 2):**

> The example makes explicit what every trial needs before it runs:

## 14. The training lineage

- **Commit:** `e73c3ae1`
- **Kind:** Unintroduced term (borrowed); verdict without its why
- **Operator's verdict:** none yet; applied autonomously, pending review
- **Diagnosis:** "Breaks its autonomous training lineage" used the training article's term without its definition and gave a consequence without the condition it follows from. The conjecture's continuation condition is named as the reason and the lineage defined at first use.

**Before:**

> interventions are allowed and recorded during bootstrapping; after a witness
> run begins, an internal human decision ends that run and breaks its autonomous
> training lineage.

**After:**

> interventions are allowed and recorded during bootstrapping. After a witness
> run begins, an internal human decision ends that run: the conjecture's
> continuation condition allows none, and the changes retained from then on no
> longer form an autonomous *training lineage*, a history of changes made while
> the models stay pinned and no person decides.

## 15. The self-approving evaluator

- **Commit:** `6c187f78`
- **Kind:** Unlabelled example
- **Operator's verdict:** none yet; applied autonomously, pending review
- **Diagnosis:** The dimensions claim and the evaluator sentence sat side by side with nothing saying the second illustrates the first or which dimension rises and which falls. Mapping taken from the note's autonomy-without-warrant case.

**Before:**

> dimensions](../notes/usefulness-autonomy-warrant-and-power-are-separate-dimensions.md).
> A self-approving evaluator can hide declining quality, so state which dimension
> changed and retain independent measures of later success, missed failures, and
> total cost.

**After:**

> dimensions](../notes/usefulness-autonomy-warrant-and-power-are-separate-dimensions.md),
> and a transfer can raise one while another falls. A self-approving evaluator,
> for example, raises autonomy while hiding declining quality. So state which
> dimension changed, and retain independent measures of later success, missed
> failures, and total cost.

## 16. Worker and client

- **Commit:** `e60a1f6e`
- **Kind:** Unintroduced term (borrowed from a note); unsignposted roles
- **Operator's verdict:** none yet; applied autonomously, pending review
- **Diagnosis:** *Worker benchmark* and *client* carried the linked note's meaning without its setup. The client is introduced as the note defines it, and the sort of client decisions into external and internal is announced as a sort.

**Before:**

> The declared boundary also determines what the comparison can establish. A
> worker benchmark [does not test the client decisions it holds
> fixed](../notes/holding-the-client-fixed-exports-the-least-warrantable-decisions.md).
> Requirements and judgments about visible behaviour remain external inputs;
> client-supplied design, diagnosis, or successor selection remains internal
> production work that the bootstrap must record and transfer.

**After:**

> The declared boundary also determines what a comparison can establish. A
> benchmark that treats the house as a worker and holds the client fixed, the
> party that chooses the task, writes the brief, and accepts the result, [does
> not test the decisions it leaves with the
> client](../notes/holding-the-client-fixed-exports-the-least-warrantable-decisions.md).
> Which of those decisions matter depends on their kind. Requirements and
> judgments about visible behaviour remain external inputs, so a client may keep
> supplying them. Design, diagnosis, or successor selection supplied by the
> client is internal production work that the bootstrap must record and
> transfer.

## 17. The admission loop and its alternatives

- **Commit:** `cb4753c6`
- **Kind:** Unsignposted roles
- **Operator's verdict:** none yet; applied autonomously, pending review
- **Diagnosis:** One paragraph described the proposal-selection loop and its partial transfer, then switched to other update architectures and a general requirement, with nothing marking the switch. "In the current approach" was kept: whether it means Commonplace's approach or this program's is not settled by the text, so the agent did not resolve it.

**Before:**

> In the current approach, a [proposal-selection
> loop](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md)
> produces candidates, evaluates them with a real chance of rejection, and makes
> an accepted change take effect. Admission itself can transfer in parts, from
> formatting and routine updates to revisions of the admission machinery. The
> endpoint requires these decisions to be computational without fixing their
> transfer order. Other update architectures are possible: reward, error,
> viability, or gradients can drive changes without a separate admission event.
> The requirement is an evidence-caused change that takes effect.

**After:**

> The current approach uses a [proposal-selection
> loop](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md):
> it produces candidates, evaluates them with a real chance of rejection, and
> makes an accepted change take effect. In that loop, admission itself can
> transfer in parts, from formatting and routine updates to revisions of the
> admission machinery. The endpoint requires all of these decisions to be
> computational without fixing the order in which they transfer. The loop is not
> the only option. Other update architectures let reward, error, viability, or
> gradients drive changes without a separate admission event. What the endpoint
> requires of any architecture is the same: an evidence-caused change that takes
> effect.

## 18. Equivalent reconstruction in the stop conditions

- **Commit:** `f3d68bbb`
- **Kind:** Unintroduced term (borrowed)
- **Operator's verdict:** none yet; applied autonomously, pending review
- **Diagnosis:** "Interventions that control equivalent reconstruction" used a term the conjecture article defines. Glossed in plain words and named as borrowed.

**Before:**

>   that control equivalent reconstruction still fail to change later decisions
>   in the predicted way.

**After:**

>   on the account still fail to change later decisions in the predicted way,
>   even after ruling out the house rebuilding the same understanding from other
>   records (the conjecture article's *equivalent reconstruction*).

## 19. "Tested regime" after the scope sweep

- **Commit:** `0609c34a`
- **Kind:** Vestigial framing (vocabulary)
- **Operator's verdict:** none yet; applied autonomously, pending review
- **Diagnosis:** Commit `08215a3d` replaced "in a declared regime" at the top of the section but left "in the tested regime" at its close. Same pattern as the first run's *trial-specific* (`bad358db`): a sweep that misses one site leaves two terms for one thing.

**Before:**

> show that this approach, in the tested regime, is not working or is not the best

**After:**

> show that this approach, under the tested conditions, is not working or is not the best

## Findings applied on the operator's verdict

After the report above, the operator replied "OK - apply these". All five whole-article findings were applied, one commit each, `764bd476` through `f0d7e2c9`. These carry an operator verdict; the nineteen sweep edits above still do not.

## 20. The trial-boundary sentence

- **Commit:** `764bd476`
- **Kind:** Defensive definition (post-restructure)
- **Operator's verdict:** "OK - apply these"
- **Diagnosis:** Whole-article finding 1. Added by `08215a3d` when product scope left the definition; its second half defended against a reading the article no longer invites. The positive half is kept because it introduces *boundary*, used twice later.

**Before:**

> The program measures two kinds of transfer separately. A trial's boundaries
> identify the decisions being assessed; they need not fix the house's future
> products or responsibilities.

**After:**

> The program measures two kinds of transfer separately. Each trial declares a
> boundary: the decisions being assessed.

## 21. TL;DR: the residue prediction

- **Commit:** `467fb481`
- **Kind:** Lost claim after restructure (partial: a section-level claim absent from the TL;DR)
- **Operator's verdict:** "OK - apply these"
- **Diagnosis:** Whole-article finding 2. Not mangled, since the frontmatter description omitted it too, but the readiness section and the closing treat the residue prediction as the route's distinctive content. One sentence added in the readiness section's own terms.

**Before:**



**After:**

> Transferring the best-supported decisions first should leave people the
> hardest-to-warrant ones, and what those still need identifies the functions
> the house must grow.

## 22. One term for the dependency account

- **Commit:** `866d3354`
- **Kind:** One term per concept (series-wide)
- **Operator's verdict:** "OK - apply these"
- **Diagnosis:** Whole-article finding 3. Six sites said *account*, two said *explanation*, for one retained artifact. Unified on *dependency account*, the training article's term for the same artifact, and introduced in italics at first use. The training article's own alternation is left for its run.

**Before (hunk 1):**

> from manifest checks. A retained explanation relates this exemption to the
> build's dependencies and assumes its configured input list is exhaustive.

**After (hunk 1):**

> from manifest checks. A retained *dependency account* relates this exemption
> to the build's dependencies and assumes its configured input list is
> exhaustive.

**Before (hunk 2):**

> the explanation should lead the house to extend manifest checks to those
> files. A further change introduces

**After (hunk 2):**

> the account should lead the house to extend manifest checks to those files. A further change introduces

## 23. The production history must show failure

- **Commit:** `8e5a05ec`
- **Kind:** Verdict without its why (inferred why, operator-accepted)
- **Operator's verdict:** "OK - apply these"
- **Diagnosis:** Whole-article finding 4. The why was two bullets away (the self-confirming-evaluation stop condition). Flagged rather than applied in the first pass per the training run's lesson; the operator accepted the proposed text unchanged.

**Before:**

> use of resources. The same production history that supports a transfer must
> also be able to reveal these failures.

**After:**

> use of resources. The records that count as evidence for a transfer must be
> able to show these failures too; a history that can only confirm success is
> the self-confirming evaluation above.

## 24. Reopened roles and viability

- **Commit:** `f0d7e2c9`
- **Kind:** Unintroduced term (two sites)
- **Operator's verdict:** "OK - apply these"
- **Diagnosis:** Whole-article finding 5. *Reopened roles* in the TL;DR said in plain words; *viability* glossed as the KB uses it for Darwin Gödel Machine admission (a change stays if the system still works).

**Before (hunk 1):**

> The program records failures, interventions, and reopened roles against
> independent outcome and cost measures.

**After (hunk 1):**

> The program records failures, interventions, and roles that return to people
> against independent outcome and cost measures.

**Before (hunk 2):**

> the only option. Other update architectures let reward, error, viability, or
> gradients drive changes without a separate admission event. What the endpoint

**After (hunk 2):**

> the only option. Other update architectures let reward, error, gradients, or a viability
> filter (a change stays if the system still works) drive changes without a
> separate admission event. What the endpoint
