# Integration review, 2026-11-04

## Scope and result

Requested by the operator after parallel revisions. Compared the commit chain after `693ab4306` through `6ecdced41` with this session's central argument, practices rewrite, invariant-preservation correction and uncommitted generator/artifact repair. Inspected the 22-commit log, aggregate changed-path list, substantive diffs for the central/refinement changes and F4–F8 repairs, current affected passages, the revised practices brief and the projection inventory. Backlink relabeling was inspected as migration scope, not independently certified line by line. External papers were not re-audited.

No architectural reversal is needed. Candidate program refinement preserves our refusal to assume generated code is valid. Interpretation-relative judgments and the distinction between permitted alternatives and disputed permission sharpen the two-account argument. Guarantee preservation and constructor-specific composition limits agree with the invariant discussion. The practices brief now reflects the completed terminology decision, so its former instruction to defer that decision is no longer active.

The uncommitted change in [Automated tests for text](../../theory/automated-tests-for-text.md) remains compatible: generator and artifact checks are distinct even with deterministic generation. Preserve it. Its unchanged ending, “We haven't built any of this yet,” is an additional current-state check before that note is treated as fully refreshed; the present session only repaired its testing rationale.

The following are residual conflicts or overclaims, not instructions to revert the parallel commits. Proposed wording remains subject to the next note-level repair.

## R1 — One generated function is not one behavior

Disposition: corrected after operator approval on 2026-11-04. The note now distinguishes the candidate implementation from its permitted behaviors and retains the guarantee-preservation obligation. The finding below records the reviewed wording.

[Programming practices](../../theory/underspecification-and-indeterminism-complicate-programming-for.md), Code extraction, now says “generation fixes one behavior.” The section is about generating a function, not observing a single execution. Even a deterministic function has behavior across inputs, and generated code may contain randomness or depend on state. The new [program-refinement definition](../../theory/definitions/program-refinement.md) compares what artifacts permit and preserves guarantees beyond successful outputs.

Repair: say generation fixes one candidate implementation, whose permitted behavior must be checked against the applicable specification. Keep candidate status, the separate adequacy question and the new terminology. This is the smallest direct collision with our edited note.

## R2 — Scoping needs a stated architecture and influence path

Disposition: corrected on 2026-11-04. The operator chose a local definition of frame as the complete context supplied to one model invocation. Summaries and tool results supplied to that invocation are inside the frame. The note now states direct access exclusion rather than absence of all causal influence. Scope is treated as a usual feature of practical traditional programming languages, not a consequence of symbolic form; no general account of its origin is adopted. The zero-error claim and dependent glosses now describe code applying defined input-selection rules without repeated model interpretation; the rule and implementation still need checking. The finding below records the earlier wording.

[LLM context is composed without scoping](../../theory/llm-context-is-composed-without-scoping.md), The architectural response, correctly stops deriving scope from symbolic membership. But it now says no adopted package marks tokens out of range, scope can only be imposed outside a call, and excluded tokens “cannot influence” a frame.

Those conclusions exceed the reference-choice argument. The claim needs the flat-context architecture it describes; a governing reference alone says nothing about masking or enforced internal boundaries. Excluding a token sequence from direct input also does not exclude information conveyed by a summary, a tool result or shared state. The same section still assigns “zero error cost” to surrounding code.

Repair: describe the actual harness exclusion and what is held fixed. Distinguish direct input isolation from broader noninterference, and code-enforced boundaries from infallible code. The central note cannot ground a universal architecture claim.

## R3 — Precise semantics does not imply either cheap or impossible inspection

Disposition: corrected on 2026-11-04. Corrected the inspection and equivalence claims. The note now allows proofs where available, bounds behavioral evidence to tested cases, and distinguishes preservation of English requirements from equivalence under an adopted package. A file-listing example separates answer requirements from execution traces. The shared-medium identity claim is removed: textual insertion does not establish specialization or equivalence. The note now presents candidate specialization, distinguishes template expansion from model behavior, and no longer treats staged task organization as incompatible with specialization. Dependent link summaries were corrected. The finding below records the earlier wording.

[Frontloading as partial evaluation](../../theory/frontloading-is-partial-evaluation-not-divide-and-conquer.md), Where the analogy stretches, now permits exact semantics under an adopted package. However, it says the meaning “is too costly to inspect” and equivalence must be evidenced “rather than derived from the semantics.” These are categorical where our account is question- and budget-relative.

Repair: distinguish availability of precise semantics from the cost and method of establishing this particular substitution's equivalence. Some substitutions may admit proofs; others need scoped behavioral evidence. The shared-medium claim that distinguishes partial evaluation from divide-and-conquer also remains an independent warrant question already named in F6; this repair did not resolve it.

## R4 — A caveat does not yet repair the verifiability ladder

Disposition: corrected on 2026-11-04 after the operator requested examples. The note now compares JSON syntax, summary faithfulness, evidence-array shape, date formatting and deterministic sentence selection. Reset conditions, execution cost, checking cost and check strength are separate; stable prose is no longer automatically misplaced. Examples are explicitly illustrative, with no measured timing claims. The finding below records the earlier wording.

[The verifiability gradient](../../theory/verifiability-gradient.md) now names reference adoption, inspection cost, execution cost and oracle quality separately. Its table and following paragraph still say restructured prompts require human review, deterministic module tests run in milliseconds, and verification becomes cheaper and sharper down the table. The placement section still treats stable behavior remaining in natural language as misplaced.

These unqualified claims conflict with the practices note's question-specific checks and with the note's own new caveat. Stability alone does not supply an adequate oracle, justify extraction or establish its cost advantage.

Repair: make the rows explicitly configured examples with named checks and costs, or replace the ordering with independent assessment dimensions. Keep evidence-guided movement in either direction; remove the automatic ranking by artifact kind.

## R5 — Some F8 prose still lets packaging or implementation settle too much

- [Metacircular methodologies](../../theory/llm-executed-methodologies-are-metacircular-interpreters.md) still says a practice moves down an enforcement gradient and “Each step is constraining,” immediately before saying the gradient is not inherent. A change in packaging need not narrow any reading or behavior. Describe what a particular transition commits, as [methodology enforcement](../../theory/methodology-enforcement-is-constraining.md) requires.
- [Instructions as typed callables](../../theory/instructions-are-typed-callables.md) still categorizes checking evidential support as underspecified semantics without naming the governing reference. Its new sentence says only a predicate justified against the requirement settles what an operation requires. Adoption can settle model-defined semantics; neither adoption nor implementing a predicate independently decides the caller's requirement. Separate formal reference, adequacy and the cost of assessing support.
- [Constraining during deployment](../../theory/constraining-during-deployment-is-continuous-learning.md) now qualifies which gains a step can buy, but still says retained gains “persist, accumulate, and compose,” and that constraining improves adaptive capacity. Retention alone establishes neither successful composition nor improvement. Keep the claim about changes whose improvements are established, with relevant interaction checks; do not import the parked invariant workshop as if it supplied a theorem.

These are follow-ups to repaired arguments, not a finding that all of F8 remains untouched. The explicit extraction scope in [codification and relaxing](../../theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) and the stability/conformance separation in [progressive constraining](../../theory/progressive-constraining-commits-only-after-patterns-stabilize.md) support the current direction.

## Workflow disposition

The previous workshop header claimed every audit finding had a repair commit while its table still named the uncommitted F3 correction. More importantly, it used “closed” where repair review remained outstanding. The README now distinguishes applied repairs from unresolved claims and replaces the obsolete proposal-stage instructions with current acceptance checks. The projection inventory remains a historical search record; its current-status header must be read before its original counts and recommendations.

No library artifact was changed by this integration review. Subsequent R1 and R2 corrections are recorded above. R1 and the compatible local F3 correction were committed in `b69e7b478`. R3 is also corrected above. R4 is corrected above. Next work through R5 one note at a time. Review completion, not the existence of repair commits, determines closure.


## Navigation follow-up after R4

The backlink scan found remaining ladder language in [orchestration strategies and run state](../../theory/orchestration-strategies-and-run-state-have-opposite-persistence.md), [automating KB learning](../../theory/automating-kb-learning-is-an-open-problem.md), and [governing behavior-changing writes](../../theory/continual-learning-requires-governing-behaviour-changing-writes.md). The [oracle-strength spectrum](../../theory/oracle-strength-spectrum.md) also identifies retry properties with oracle strength. Review these against the revised requirement-relative examples during final navigation acceptance; repairing the target note does not settle those claims.
