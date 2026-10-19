# Coverage policy comparison

## Decision and implementation

**Clarify the existing materiality rule with question-driven omission checks in
report verification. Retain the roles, dependencies and publication machinery.**
Do not adopt a hard runtime/lens file-anchor bound or an exhaustive structural
inventory. Confidence is moderate in this being the smallest sufficient design
change, low in any prediction of better detection or lower effort. Neither
outcome has been measured. Retaining the live policy is defensible if the
operator does not want another prose change without a trial.

This recommendation combines policy 1's existing acceptance threshold with
policy 3's concrete selection and stopping procedure. It is a clarification,
not a fourth architecture. Countercase searches, independent correctness checks
and materiality judgments already exist; the addition is explaining which
omission questions warrant further inspection and when they are closed. The
coordinator's provisional preference for policy 3 was not evidence or a decision.
This document implements only the [comparison plan](./comparison-plan.md).
The operator subsequently authorized revision and implementation, including an
explicit effort-versus-claim-breadth stopping choice and a brief reporting burden.
The prose-only change is implemented in report verification, shared worker rules
and the verification type. Roles, dependencies, schemas and engine code are
unchanged. Existing runs remain unchanged. The alternatives below retain their
comparison status; no detection or efficiency benefit has been measured.

## Checked baseline and premise corrections

Read the [runtime instruction](../../agentic-system-analyses/instructions/analyse-agentic-system/jobs/trace-runtime.md),
[lens instructions](../../agentic-system-analyses/instructions/analyse-agentic-system/jobs/analyse-memory.md),
[epistemic instruction](../../agentic-system-analyses/instructions/analyse-agentic-system/jobs/trace-epistemic.md),
[verifier instruction](../../agentic-system-analyses/instructions/analyse-agentic-system/jobs/verify-reports.md)
and [verification type](../../agentic-system-analyses/types/agentic-system-verification.md)
together on 2026-10-11. Consequential corrections are:

- **No exhaustive duty exists.** The type explicitly rejects exhaustive repository
  inspection. The frozen tree is the verifier's comparison basis; materiality
  governs which omissions matter. Selection and stopping are underspecified.
- **Independent discovery already exists.** Both lenses call runtime provisional
  and not an inspection limit. Memory covers included parts across dimensions;
  epistemic includes operations runtime omitted. Runtime already selects a small
  warranted set of forcing cases for guarantees. None of the policies should
  replace these duties with centrally assigned directories.
- **Source-read authority needs clarification.** [Shared worker rules](../../agentic-system-analyses/instructions/analyse-agentic-system/jobs/follow-worker-rules.md)
  restrict post-analyst reads to named ambiguities at cited paths, whereas report
  verification asks for tree-based coverage. The recommendation must explicitly
  permit bounded report-verifier omission searches, not silently assume authority.
  Profile and synthesis verification remain record-based.
- **Structural accounting scales.** Policy 2 adds accounting for all modules and
  entry points; mechanical enumeration cannot decide each item's materiality.
  It can move rather than resolve unbounded work. The runtime instruction forbids
  a product inventory.
- **Recorded overlap is not completeness.** Few outside-runtime lens anchors or
  verifier coverage findings can reflect shared omissions or limited searching.
  Existing audits have selected source-backed omissions but no denominator.
- **Policy 2 includes lens-owned anchors.** Correctness checking is not excluded
  there. Its risk concerns omitted mechanisms outside both anchor sets and weak
  correspondence between files and mechanisms, not all lens discoveries.
- **Splitting is not a measured multiplier.** It can duplicate discovery and add
  reconciliation; narrower responsibilities can also reduce local work. No net
  cost estimate justifies splitting here.

The [current arrangement](./current-arrangement.md),
[proposal](./proposals/verification-coverage-bounds.md) and
[evidence base](./evidence-base.md) now reflect these qualifications. The
operator's original exhaustive-duty intent remains attributed in the proposal.
The live layout verifies runtime, memory, epistemic and reconciliation; boundary
is an input, not a correction addressee. The plan hands runtime to lenses
order-only. `artifactrun/plan.py:Input` and `artifactrun/run.py:holds` confirm
that runtime changes do not themselves lapse lens judgments.

## Three policies

Discovery selection chooses mechanisms to characterize. Omission checking asks
whether an unreported mechanism or condition could change that characterization.
Correctness checking tests reported claims against their supporting behavior.
A stopping decision for omission search does not waive correctness or a known
contradiction. The live instruction's checks of every record, anchor, status,
relation and conflict remain; question selection bounds additional omission
exploration, not those checks. All options retain analyst correction ownership and independent
lens discovery within the frozen boundary.

### 1. Clarify the existing rule

**Responsibilities and addition.** Analysts continue their current route,
dimension and countercase checks. The verifier independently supports
consequential conclusions and qualifies known material uncertainty. Clarify
that more artifacts alone do not oblige further inspection. No search territory
is removed. This largely repeats the type; its useful addition is requiring an
explicit stopping rationale rather than implying a tree-wide scan.

**Stop.** Stop optional omission exploration when required findings and emitted
claims have adequate evidence, known material challenges have been resolved or
made compatible with narrower claims, and no identified unresolved question
would change those claims. Record why further searching is not warranted.
Unknown unselected mechanisms remain unknown. The weakness is circularity:
without a selection procedure, a worker may not know which questions to identify.

**Promise, benefit and loss.** A bounded account of supported mechanisms, not
complete design-space enumeration. It preserves conditions for later transfer
assessment at minimal disruption, but may miss alternative producers, consumers
or instruction channels the worker never considers. Expected work is close to
today's, with a small explanation burden; no savings are established.

**Footprint.** `jobs/verify-reports.md` and its shared worker-rule
source-read clause; optional explanatory type prose. No plan, layout, schema,
analysis-code or engine change.

### 2. Recorded-path bound

**Responsibilities and change.** Analysts retain independent discovery. Runtime
additionally accounts for every top-level package, manifest and shipped entry
path, recording inclusion or an immateriality reason. The same verifier checks
that structural map against the tree. Lens omission searches use relevant
runtime paths plus lens-owned anchors. Reported claims still require independent
correctness checking; a needed helper cannot be ignored merely because its file
was not anchored. This introduces a search restriction, not just clarification.
An outside-both-sets mechanism is routed as runtime coverage, but any affected
misleading lens claim still needs correction by its owner.

**Stop.** Runtime structural checking stops when enumerated modules and entry
points are accounted for; lens omission searches stop when the relevant anchored
mechanisms have been checked for conditions that could alter the lens conclusions.
This is concrete but not a resource guarantee: enumeration/materiality and an
anchored large file can still require substantial work. If structural accounting
cannot finish, declare it incomplete and constrain claims; do not label the
remaining tree immaterial. Unanchored helper mechanisms remain unknown.

**Promise, benefit and loss.** Structural accounting plus path-bounded lens
review, not complete mechanism coverage. It can reuse runtime navigation and
preserve lens-found alternatives. It can also miss shared blind spots and make
the public comparison appear more complete than it is. Lost mechanisms reduce
the design alternatives available for later transfer assessment. Work may shift
from lens review to runtime inventory rather than shrink.

**Footprint.** `trace-runtime.md`, `verify-reports.md`, shared worker rules and
possibly runtime/verification type prose for incomplete accounting and limits.
The existing record shapes suffice. Same-verifier placement needs no plan,
layout, code or engine changes. A separate verifier and required runtime
inputs would be a different, larger proposal; this comparison does not justify it.

### 3. Question-driven omission checks

**Responsibilities and addition.** Analysts retain all current discovery and
countercase duties. The verifier selects a small justified set of consequential
claims spanning the central runtime and lens conclusions. Each question names
an omitted mechanism or condition that could change the claim, its likely
producer/consumer or alternate entry path, and why it matters. Anchors are
starting points, not a file fence. Search only as far as those questions warrant.
This operationalizes existing countercase/materiality behavior; it does not add
a second characterization or require one new check per record.

**Stop.** Continue a selected search while further inspection is reasonably
likely to change a consequential conclusion and retaining its breadth justifies
the effort. Otherwise retain uncertainty only where the existing wording remains
supported, or request analyst narrowing, withholding or qualification. The
verifier does not edit claims. Close each question with supported wording, a
correction request, or a local uncertainty that leaves the remaining claim true.
Stop omission expansion when selected questions have dispositions and no
identified material challenge lacks one. If reduced scope cannot support a
faithful bounded account, request correction or return inability. Do not keep
exploring merely to increase findings or weaken supported findings merely to
save work. No numerical budget is inferred from the cases. Unknown unselected
routes remain unknown; poor question selection remains the principal risk.

**Promise, benefit and loss.** Consequential-question coverage and explicit
remaining uncertainty, not exhaustive repository or part coverage. Producer,
consumer and alternative-path questions preserve mechanisms and operating
conditions useful for design-space comparison and separately commissioned
transfer assessment. Optional inventory detail may be lost. Expected work is
more selective cross-file inspection and a short decision rationale, possibly
avoiding broad low-value scans; neither net effort nor detection gain is measured.

**Footprint.** Same as policy 1. A short Verification account can retain selected
questions and dispositions; existing Limits can retain consequential unresolved
issues. No additional report member or schema is needed.

## Retained-case tests of the reasoning

These are retrospective policy judgments using the audits, not new source
inspections or proof that a worker would detect the errors. Finding IDs below
refer to the linked report, not a shared cross-report numbering scheme.

**Identity boundary.** Both Graphiti runs (`5833fd846841` and `85a21a06d35c`),
Napkin (`b831630d0978`) and blocked Letta (`d460b458ddad`) use method
`6ff7c828e94dd66abdf5af00c89db6420bc6a1ad`. Letta Code (`88afa3263646`) uses
`0265fff4dd8a9d00fa2aba78495b2c95b2abbad6`; its audit reports only four
workshop/navigation files differed, not the analysis implementation. All use
pi-sol, `openai/gpt-6.1-sol`, medium. Full run IDs, source revisions and source
paths are retained in each report. Different sources, scopes and service
conditions preclude a controlled cost comparison. The two Graphiti runs are
repeat-run evidence within one system, not two independent systems.

| Case and reported evidence | Policy 1: clarify | Policy 2: recorded paths | Policy 3: consequential questions |
|---|---|---|---|
| [Graphiti 5833 audit](../analysis-audit-evidence/reports/graphiti-analysis-and-trace-audit.md) G2–G3 and [85a audit](../analysis-audit-evidence/reports/graphiti-85a21a06d35c-analysis-and-trace-audit.md) G1–G2: successful bulk retention bypass and missing provenance index | Require scope support for raw suppression and episode retrieval/removal claims; selection remains unspecified. | Inspect anchored `graphiti_core/graphiti.py` and follow needed persistence/index consumers for correctness. These are not excluded lens anchors. File inclusion alone does not select the bulk chain. | Ask whether each advertised producer preserves suppression and populates the index consumed by retrieval/removal. Follow ordinary versus bulk write → persistence → consumer. This could change privacy and cleanup conclusions; costs targeted cross-function/file reads. |
| Graphiti complementary coverage: 5833 G1, G6 and comparison; 85a G3–G4 and gains/lost findings | Materiality can justify saga, instruction and attribute questions, but does not choose between them. | Saga code in an anchored large file remains admitted but costly to navigate. An optional cache or instruction channel outside both sets could escape lens omission review; exact outside-set membership was not measured here. | Select recurrence, instruction delivery or retained-state consumption claims; inspect hydration/save, watermark selection, server-wired versus installed text, or cache/attribute consumers as warranted. Could change recurrence and delivery accounts. Optional unselected alternatives remain unknown. |
| [Letta Code audit](../analysis-audit-evidence/reports/letta-code-analysis-and-trace-audit.md) LC2–LC3: committed/current checkout distinction, hook semantics and successful removal of unsupported `promote` | Retain independent correctness and comparison-value checks; do not accept a wrong positive with a caveat. | Correctness of anchored compilation and rendering remains required. Structural accounting of the broader harness may add work across entry points without resolving a profile inference. | Ask what later invocations actually receive and what evidence establishes promotion direction. Follow Git HEAD compilation versus checkout reads and the recorded tier guidance. Could change visibility/curation values. Existing profile review already repaired the latter; this is not a new feature or proven saving. |
| [Napkin audit](../analysis-audit-evidence/reports/napkin-analysis-and-trace-audit.md) N2–N3: retained-file consumer confused with current-run aggregation; documented automatic delivery omitted | Support emitted authority/delivery claims at the correct strength. The rule already requires this; a stop rationale alone may not reveal the confusion. | Benchmark anchors support checking the array versus file consumer; a documented channel outside both sets might be missed, but no anchor census establishes that it was outside. | Ask which retained object is reloaded, and whether automatic delivery is documented, implemented or observed. Inspect result array/save/aggregation and `docs/distill.md`. Could remove wired retained-file authority while preserving a documentation-backed positive. External consumers and deployment remain unknown. |
| [Blocked Letta audit](../analysis-audit-evidence/reports/letta-analysis-and-trace-audit.md) L1–L2: landing-page tree, recovered guessed-path failure, supported stop | Retain boundary stop; no downstream omission check is required. A failed guessed path is not absence evidence. | No runtime map exists; do not commission structural runtime accounting or follow the redirected repository under this policy. | The prerequisite question—does this pin contain the implementation?—was resolved at boundary. Stop without runtime/lens work; do not invent downstream questions. |

The Graphiti pair's complementary cache, attribute, checkpoint and evaluator
coverage shows selection variance. Searching all these alternatives costs work;
it does not establish that all belong in every central account. Bulk suppression
and provenance conditions are consequential because they alter reported retention
and consumer behavior. Backend-wide persistence, actual loss/races, compliance
and benefit remain unobserved. Letta Code's partial audit found no new substantive
correction in its samples; that is not complete coverage. Napkin's missing
implementation does not erase a documented mechanism or justify an implemented
positive. Letta's short stop is not a full-analysis speedup.

### Effort context, not a savings estimate

The [navigation audit](../../reports/retained/analysis-worker-code-navigation-trace-audit-2026-10-11.md)
counts direct source/code read calls: Letta Code 128/116 across 12 invocations,
Graphiti 85a 117/108 across 10, Napkin 172/136 across 13, blocked Letta 5/0 across
one. Letta Code runtime made 35 code reads and memory 32. Of code reads,
111/116 in Letta Code and 100/108 in Graphiti were requested with limits.
Workers already search and use bounded reads; this comparison concerns target
selection, not replacing whole-tree reading. These are calls, not unique
coverage, tokens, cost savings or latency predictions. Repair invocations are
included; independent rereads are not automatically waste. No extra measurement
was made: overlap counts would not discriminate sufficiency or shared omissions.

## Draft stopping language and reader coverage statement

The following expresses the adopted direction. The live instructions and type,
not this workshop text, govern execution. Required checks, structural blockers,
frozen-boundary rules and correction ownership remain binding:

> Independently verify consequential reported claims. Select omission questions
> by the conclusions they could change, using the required analysis questions,
> alternate shipped paths and producer/consumer dependencies, not only listed
> files. Briefly retain consequential questions, search basis, dispositions and
> stopping rationale in Verification, not every exploratory query. Continue a
> search while further inspection is reasonably likely to change a consequential
> conclusion and retaining its breadth justifies the effort. Otherwise retain a
> limit only if the wording remains supported, or request analyst narrowing,
> withholding or qualification. Close each question with supported wording, a
> correction request, or uncertainty compatible with the affected conclusion.
> Stop optional omission expansion when these questions have dispositions and no
> identified material challenge lacks one.
> Further artifacts alone do not require more inspection. A known contradiction
> cannot be deferred because the search has stopped. If narrowing cannot preserve
> a faithful bounded account, request correction or return `problem` as required.

**Draft reader statement**, specialized to the actual search, not boilerplate:

> This account characterizes the inspected mechanisms at the pinned boundary.
> Omission checks addressed [named consequential questions] through [paths and
> search method]. [Named alternatives] remain uninspected or inconclusive; the
> affected conclusions are limited to [supported routes/conditions]. No complete
> mechanism inventory, absent alternative or observed benefit follows from those
> gaps. Absence claims require their own searched boundary and warrant.

For example, scope raw-content suppression to ordinary ingestion after the bulk
countercase, rather than append “bulk not audited” to a universal suppression
claim. Remove Napkin's wired retained-file consumer value unless a reload is
supported; separately retain documented delivery at documented strength.
Remove Letta Code's unsupported promotion positive, not merely qualify the whole
profile as partial. These changes constrain claims, not just reader expectations.

## Benefit, risk, footprint and next decision

Expected benefit: make stopping explainable while directing existing independent
review toward conditions that change design understanding. Expected effort:
short selection/disposition prose plus targeted cross-file reads, with unknown
net cost. Risk: workers choose easy questions, miss an important mechanism, or
write rationales without changing broad claims. Evidence against adoption would
be recurrent missed central conditions despite justified question selection,
weaker comparison values, or added search/reporting work with no useful change
in operator or comparison-consumer decisions. Successful existing repairs argue
for preserving review, not adding reviewers or weakening it.

**Implemented change footprint:**

- Instructions/type prose: clarify `jobs/verify-reports.md`; reconcile
  the source-read clause in `jobs/follow-worker-rules.md` specifically
  for report verification. A brief search-account requirement is added to
  `types/agentic-system-verification.md`; analyst discovery remains intact.
- Plan/layout and schemas: unchanged. No split memory, new verifier or dependency
  toggle. Runtime corrections remain order-only to lenses; the existing verifier
  still judges affected claims across records.
- Analysis code and engine: unchanged. `verification.py:report_check_gate` routes
  structural blockers; no new gate is required. `rules.py:_verification_findings`
  checks affected-record citation carry-through for limits, not prose faithfulness.
- Consumers: report analysts receive correction requests; profile extraction must
  not emit unsupported positives/negatives; synthesis authors and verifiers must
  carry consequential limits faithfully. Overview/publication surfaces and
  separately commissioned transfer/comparison consumers retain their formats.

**Decision made:** the operator authorized the bounded prose-only revision,
without requiring a trial first. A new audit is not an automatic prerequisite.
This comparison cannot establish the smallest effective question set or actual
effort change. Commit the revised method before opening a new analysis; no
existing run's method boundary changes.

If a trial is wanted, separately commission one static comparison on the frozen
Graphiti 85a bulk suppression/provenance claims and one Letta Code
committed-versus-current visibility claim. Compare live-rule versus draft-rule
review of those claims without supplying audit answers to reviewers. Limit scope
to those questions and their producer/consumer dependencies, with one initial
review pass per condition and no full analysis or target execution; the operator
must set an effort ceiling before launch. Return early if frozen inputs are
missing or the ceiling prevents support, reporting unknown rather than extending
the trial. Success means faithful claim conditions, useful omission dispositions
and explicit stopping, with actual effort recorded; finding counts alone do not
qualify. Failure means misleading values survive, a relevant controlling path is
excluded, or explanation effort outweighs decision value. This would test execution and stopping after questions are supplied, not whether
reviewers independently select the important questions. It would not estimate a
system-wide detection rate or completeness. A trial still requires separate
authorization.
