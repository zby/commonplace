# Preserving requirements through composition

Working candidate after five rounds of fresh-context brainstorming, independent critique and cleanup. The examples are constructed except for the explicitly identified reading of the freshness architecture. This is not a library definition or a claim of observed runtime failure. [Source assessments](./source-assessments.md) separate the literature from our transfers.

## What this account adds

[Program refinement](../../theory/definitions/program-refinement.md) states replacement obligations; [bounded impact](../../theory/localized-retention-pays-where-change-is-sparse-in-a-matching.md) distinguishes edit locality from checking scope. This account supplies concrete probes for missing assumptions. Its practical benefit has been tested only on the examples below.

First name the requirement, initial conditions and observable behavior. Determine whether it concerns states, individual executions, eventual progress or comparisons across runs. Then identify which environmental assumptions each local guarantee needs, who supplies them, and for how long.

If “Return JSON only” and “raise an exception on failure” leave the failure channel unsettled, settle that contract first. A precise implementation cannot decide which requirement the caller ought to adopt.

## Choosing a probe

These are starting points for a named requirement, not an exhaustive checklist.

| Change or claim | Discriminating check | What passing does not establish |
|---|---|---|
| A checked condition is used later | Pause after checking, change relevant state, resume use | Other schedules or real atomicity unless separately checked |
| Baseline replacement after work runs asynchronously | Exercise an intervening transition, including create/retire when initially absent | Review coverage of current live files |
| Object ownership or copying changes | Compare caller-owned nested state before and after the operation | Independence of prose meanings or every mutation route |
| Access to a confidential input changes | Compare declared public observations across runs varying only that input | Other inputs, histories or stochastic distributional equality |
| Eventual completion is promised | Find an enabled initiating action and justify scheduling and termination assumptions | Progress merely because local promises match |
| A local implementation is replaced | Re-establish the affected premises of the old argument | Applicability of old passing test results to the replacement |

## Checking and using an approval

Constructed finite model: versions A and B are immutable; `current=A`; the permanent set `approved={A}` records acceptance of exactly A; publication is empty. Approval here does not mean semantic correctness. Required state invariant: `publication = empty or publication ∈ approved`. Revocation, expiry, dependency changes and multiple publications are excluded.

Three individually atomic steps can interleave:

1. **C — Check:** record whether `current` belongs to `approved`.
2. **E — Edit:** change `current` to unapproved B.
3. **P — Copy:** if the recorded check passed, publish the version currently selected by `current`.

In order CEP, the check is accurate, the editor changes only its pointer, and the publisher copies the current version. All those limited local guarantees hold, but publication contains unapproved B. A stronger guarantee that the publisher emits only approved versions needs a condition this composition fails to supply: the checked version must be the copied version.

An atomic **check-and-publish** reads, checks and records the same immutable version relative to editing. Alternatively, capture an immutable version and check and publish that version if publishing an older approval is allowed. Another unprotected check only moves the gap.

Enumeration with C before P gives exactly CEP (violation), CPE (approved A published), and ECP (refusal). Both placements of E relative to atomic check-and-publish preserve the invariant. These results concern this finite model, not the atomicity of a deployed pipeline. Refusing publication can preserve safety without establishing eventual publication.

## A different requirement: baseline transition eligibility

The [freshness architecture](../../reference/freshness-architecture.md#queue-to-finalize-concurrency-invariant) describes revision/generation guards at review finalization. Reviewing captured bytes does not establish that a queued job may still replace the current baseline. An intervening baseline transition can invalidate that authority.

The documented guard concerns baseline concurrency, not live-file currency. A capture can finalize after a later file edit if no competing baseline transition occurred; its evidence remains attached to the captured inputs. Conversely, a recent capture can lose the concurrency check. These are different properties from the publication invariant above.

Replacing the persistent generation check with “baseline absent” is a discriminating proposed edit: an absent/create/retire sequence can restore absence while changing eligibility. A review of that edit should reopen queue-time identity and transition-time evidence. It need not re-evaluate reviewer semantic quality unless its inputs or guarantee also change. This is an architecture-document interpretation, not a code audit or observed defect.

## Reusing an argument after a local edit

List the old argument's affected premises. For each, retain justified support, obtain replacement support, or mark it unresolved. Finish this bounded review when every listed premise has a disposition and no discovered relevant interaction remains unexamined. An unresolved premise prevents the preservation claim through that argument. A newly discovered dependency reopens the boundary.

Constructed example: a diagnostic renderer receives a mutable review descriptor and returns presentation text. Publication does not use the text, but its argument assumes the renderer leaves the descriptor and approval records unchanged.

Replacing concatenation with a string builder can leave that reasoning applicable if the replacement satisfies the premises it uses. Recheck no mutation for the publication claim; display equivalence is separate. Old test results describe the old implementation; rerunning them gives bounded evidence about the new one.

A one-line change from `display = deepcopy(review)` to `display = review` can break the premise. Stripping whitespace in `display["candidate"]["text"]` now mutates the caller's nested object. The executed one-input probe produced the same display text in both variants, but only the alias variant changed the input. A correct publisher may reject that changed descriptor: the probe establishes a broken preservation premise, not inevitable publication of unreviewed bytes.

Check discovered writes through aliases, files, globals or callbacks. For prose, check whether an edit changes the meanings or assumptions the old reasoning uses; storage separation cannot establish semantic independence.

## Held-out requirement: compare runs

A deterministic report pipeline extracts two public facts A and B. Its formatter returns [A,B] for confidential bit 0 and [B,A] for bit 1. Both outputs contain the correct facts, satisfy the schema and omit the literal bit. Per-output checks pass while order reveals the bit.

The chosen requirement is that the public observations, including order, remain independent of this bit, with public inputs and relevant public initial state fixed. If the declared observation were only the unordered set of returned facts, this difference would be permitted. Correct fact content and equivalent observations are distinct criteria.

For one fixed document, run both bit values. The secret-dependent formatter fails the comparison; fixed public ordering passes. The pair exhausts secret values for this finite deterministic case, not other documents or retained-state histories. Conformance concerns the stated relation; predicting how often dependence appears answers a different question.

For stochastic execution, first specify what should remain equal, such as output distributions conditional on public input. Unequal samples can occur without dependence, and equal samples can occur despite it. A fixed-seed comparison tests a particular coupling, not distributional equality.

## Limits that remain useful

Matching “review finishes after publication” with “publication follows review” supplies no initiating action. Even an acyclic plan needs termination and scheduling assumptions to establish completion.

Convergence can coexist with crossing a required bound, so stability evidence cannot discharge an invariant obligation. The affine counterexample and calculations remain in [the round 3 record](./rounds.md); no dynamic model of prompt behavior has been established.

These probes expose missing obligations; they do not prove that the dependency account is complete, that weak interactions are harmless, or that every requirement admits an affordable check.
