# Use declared types for review outputs

## Intent and scope

Use Commonplace artifact types instead of contracts duplicated in workflow
Python. Following Fable's assessment, the operator approved this order:
commit the approval fix, capture binding write briefs, trial revision live,
then implement the individual review-result slice before the first collection
sweep. The operator selected older artifacts and Sol; both ordinary revision
trials have now completed through explicit final-publication approval. Settled
intermediate work is preauthorized; exact final publication and unsettled
selection decisions require approval. See the
[boundary change](./publication-boundary-change.md) and the
[live assessment record](./plan.md#live-sol-assessments-2026-11-10).
Later type slices remain proposals; directory typing is a separate decision.

The intended result is one declared contract per output: the worker reads
it, runtime acceptance checks it, and an operator can validate the saved
artifact with the same contract. Keep pair and bundle call granularity,
per-pair result storage, explicit approval and one guarded publication.
Do not turn this into the shared-orchestrator project.

A bundle call already declares a separate output for every requested gate.
An individual **review result** is therefore the right typed artifact; the
**review gate** is its criterion, not its output type. No bundle-review type
or new bundle file is needed.

Done means the selected output types govern both worker acceptance and saved
files, the corresponding handwritten structural checks are removed, and
fake-harness tests preserve retries, approval, replay and publication safety.
Schema success is not evidence that a review's judgment is correct.

## Recommendation

Introduce four types in the first implementation sequence, with a stop for
review after the first one. Reuse two existing types. Assess remaining prose
outputs separately; do not invent a universal report type merely to label
files. Do not adopt a directory type in the first sequence.

| Artifact | Proposed contract | What it covers |
|---|---|---|
| One gate, type-conformance, collection-conformance or critique result | **New `types/review-result.md`** and schema | Outcome, anchored findings and review body, plus code-owned target/criterion identity, hashes and executor provenance in the stored result. Verdict and report-kind results share the type. |
| Worker's full-pass disposition proposal | **New `types/full-pass-decision.md`** and schema | `disposition`, `update`, `merge-target`, and the warranted-contribution, disposition and routed-attention sections. |
| Worker's closing judgment | **New `types/full-pass-closing.md`** and schema | `closing-status`, update assessment, defects and explanatory body. Its status allows `repair-needed`, unlike the final packet's reduced `closing-status` field. |
| Revision plan, editable through explicit `--plan` input | **New `types/revision-plan.md`** and schema | Purpose, defended claims, ordered pass entries, optional scopes and stop reason. |
| Published full-pass packet | **Reuse `types/full-pass-report.md`** | Already typed. Make runtime reads and publication use its schema; extend it only for missing structural rules. |
| Connect output inside the full pass | **Reuse `types/connect-report.md`** | Already has a schema and required sections; the workflow currently checks only that the output is nonempty. |

All new type specifications belong in `kb/types/`, beside their schemas.
Before writing them, read that collection's contract and the type-spec
contract. The type specification supplies the semantic content contract and
a copyable template; its schema owns structural requiredness and enums.
Keep instructions about launch, approval and publication in the workflow
instructions, not in the type's content contract.

### Worker output and stored review result

Do not ask a worker to invent hashes, launch ids, recorded model or timestamps.
Keep a single result type with an explicit division of field ownership:

- The worker supplies `type`, `findings`, `outcome` and the review body. The
  contract explains which fields code adds before the artifact is complete.
- Code supplies the note and criterion identities, captured-input hashes,
  profile, actual model, run, launch and completion time. Code may generate
  the retrieval description rather than ask the worker to repeat metadata.
- The acceptance adapter checks the claimed type against the expected type,
  rejects worker-supplied reserved metadata, constructs the completed
  candidate in memory and validates it. The same completed bytes are stored
  after acceptance. Preserve the original worker output in the launch record.
- The raw worker fragment is not advertised as a standalone valid stored
  artifact. It is validated through the documented completion boundary, not
  by making all provenance fields optional in the result schema.

Use `outcome: pass | warn | fail | report` as the sole machine-readable
verdict. Remove the terminal `## Result:` protocol rather than keeping two
verdict channels. A report-kind criterion still must produce `report`, and
a verdict-kind criterion must not: that comparison uses the requested pair's
contract and remains a runtime check.

This is a format change, not just adding `type:`. The strict footer parser
can disappear only after its prompts, instructions, readers and tests have
changed. The initial search found 71 matching lines for
`Result:|outcomes|parse_verdict|parse_report` across `src`, `tests`,
`kb/instructions` and `kb/types`; inventory consumers, not just those lines.
Do not silently support two authoritative verdicts.

### Questions settled before the result slice

**Require checkable anchors for passage-local findings.** The type will
require a `findings` array, with each finding carrying `scope`, `quotes` and
`reason`. A passage finding has `scope: passage` and one or more verbatim
quotes from the captured note. Each quote must locate a unique contiguous
span; use a longer quote when a shorter one is ambiguous. A document-wide or
absence finding has `scope: document`, an empty quote list and a reason that
names the whole-document condition or missing element. Do not fabricate a
quote for an absence. `warn` and `fail` require a nonempty findings list;
`pass` and report-kind outputs may have none.

The schema owns these shapes and conditional requirements. Acceptance checks
quoted text against the captured note, never the live file. This is a new
check, not a deletion of existing Python. It catches invented or misplaced
anchors, not an unsound judgment or a worker disguising a local finding as
document-wide. Keep the body's synthesis free prose without reproducing the
findings verbatim. Before implementation, record this intentional contract
tightening in the multi-consumer change packet.

**Do not assume moving the verdict is judgment-neutral.** The worker template
will put findings before `outcome` within frontmatter and ask for assessment
before verdict selection. This keeps the finding rationale before the
serialized verdict, but does not prove equivalent reasoning or accuracy.
The operator-authorized calibration should compare old and new formats on
identical captured notes and criteria with the same profile and call grouping.
Retain verdict differences and inspect their reasons and anchors. Do not
confound format with pair-versus-bundle grouping or call a small unchanged
sample proof of equivalence. Fake-harness tests establish the protocol only.
Paid comparison calls need their own agreed scope; they are not implicit in
implementing a schema.

**Explicit file validation reaches state artifacts.** A fresh installed
project was probed with a deliberately malformed `types/full-pass-report.md`
under `kb/reports/state/`, whose `.commonplace-validation-ignore` existed.
`commonplace-validate <absolute-file-path> --json` analysed one file, reported
16 missing required fields and exited 1. `ValidationRun.validate()` also
validates its explicitly supplied path rather than discovering files through
the ignore filter. The runtime adapter must use that explicit candidate path;
a skipped directory scan is not evidence of conformance. Regression cases
for saved files and in-memory candidates are retained in
`tests/commonplace/review_workflows/test_type_boundary.py`; both reject the
malformed packet through the required-field schema, not an unrelated error.

**Cut over without migrating absent baselines.** This checkout currently has
zero Markdown result files under `kb/reports/state/review/results/`. Inventory
again immediately before cutover. Reject old-format results clearly rather
than silently reinterpret them, and leave old run artifacts untouched. If
another consumer has old results or an active run, stop for an explicit
cutover decision; this observation authorizes neither deletion nor migration.

### Disposition proposal versus published packet

Keep these separate types. The worker's proposal has only three decision
fields and its rationale. The published packet also has final-text hashes,
closing outcome, repair use and operator-resolution fields that do not exist
when the proposal is written. Making every packet field optional to admit a
proposal would weaken validation of the stored packet.

Put shared decision enums and conditional constraints in a schema fragment
referenced by both types. Do not copy the same choices into Python and two
schemas. Python still branches on the accepted decision; those branches are
execution, not duplicate structural validation.

### Revision plan representation

Recommend converting the proposed `plan.yaml` into `plan.md`, with the plan
mapping in YAML frontmatter and `type: types/revision-plan.md`. Keep the
assessment report separate initially; combining assessment and plan is a
separate operator-interface choice, not needed to adopt the type.

This lets ordinary Markdown type validation work without adding a general
raw-YAML artifact system. Update `--plan`, approval messages, recorded option
handling, fixtures and operating instructions together. Preserve explicit
`--plan` overrides of stopped plans, selection approvals and unapproved-list
warnings, and exact final-publication approval. Do not reintroduce routine
approval of generated or explicitly supplied plans.
Do not keep the old extension while quietly changing its content grammar.

If keeping raw YAML is a consumer requirement, return that choice before
implementation: it needs an explicitly schema-backed YAML input adapter,
and would not yet be an ordinary typed Markdown artifact. Do not claim
`commonplace-validate plan.yaml` supports that today.

## Checks removed, moved and retained

“Removed” here means deleted from workflow-specific code after a declared
schema covers the same failure. Parsing and generic schema execution still
exist. A check moved into an imperative type rule is **centralized**, not
eliminated. New validation is not counted as a code reduction.

| Current code | Change | What remains |
|---|---|---|
| `results.read_result()` required-field, string, mapping and outcome checks; `write_result()` outcome membership | Replace with expected-type validation against `review-result`. Remove a separately maintained Python outcome list as validation authority. | Parsing, dataclass construction/serialization, field ownership, path confinement, atomic write, identity resolution, watched-parts hashing and freshness. |
| `outcomes.py`: `parse_verdict()`, `parse_report()`, terminal-line and competing-signal regexes | Delete once `outcome` frontmatter replaces the footer everywhere. `gates.check()` and `gates.outcome()` become typed parsing/validation adapters. | The requested verdict/report-kind restriction; one named output per requested pair; rejection and correction behavior. Prose is no longer a second decision channel. |
| `full_pass.PACKET_SCHEMA`, `PACKET_SECTIONS`, `_headings()` | Move field constraints and required headings to `full-pass-decision` schema. Delete constants/helper when no other callers remain. | Worker ask, parsing accepted data and disposition branching. |
| `_packet_check()` field combinations | Schema conditionals: non-merge has null target; merge requires a nonempty target; undetermined update requires keep; update none excludes keep. | Resolve merge target safely, check existence and that it is not the reviewed note. A schema cannot inspect the checkout. |
| `full_pass.CLOSING_SCHEMA` and `_closing()` local shape checks | Move enums and conditionals to `full-pass-closing`: non-hand-back requires preserved/strengthened; repair-needed requires a nonempty list of nonempty defect strings; other statuses require an empty list. | One-repair budget, applying the decision to the particular candidate text and choosing hand-back after exhausted repair. |
| `revise.PLAN_SCHEMA` and structural parts of `plan_checks()` | Move required fields, purpose/defend string shape, pass-entry shape, allowed keys and scope type into `revision-plan` schema. | Resolve pass names against the live catalog, forbid duplicate pass names, enforce catalog depth order, normalize missing scope and select profiles. JSON Schema `uniqueItems` does not forbid the same pass with different scopes. |
| `read_packet()` currently checks parsing and type, not the full declared schema | Replace with complete packet contract validation, and validate generated packets before publication. This mostly adds protection rather than deleting code. | Compare hashes against actual files, resolution authority and state, pending-packet behavior, atomic publication. |
| `_methods()` nonempty check for connect | Replace with existing connect type validation, including required sections. This adds validation beyond the old check. | Add source identity agreement and normal link-health checks. Candidate paths that appear only in prose or tables are not automatically checked by the schema or link validator; either add a type-owned extractor/check or retain that explicit gap. Authorised relation labels and useful connections still require judgment. |
| Edit bounds and approval checks | **Retain.** | Title/H1/type/brief preservation, captured-brief publication guard, removal of human verification after a body edit, no new validation failures, copyeditor frontmatter equality, captured approvals, stale-key rejection, run lock, checkout guard and compare-before-write. These compare versions or enforce authority. |

The production-call search currently finds `headless.decisions` used only
by full pass and revision. Once all three decision asks use declared types,
its mini-schema machinery (`Schema`, `describe()`, `violations()`) can go.
If typed acceptance and normal frontmatter parsing replace its remaining
callers, delete `decisions.py` and replace its mini-schema-specific tests
with equivalent typed-output tests. Recheck consumers at implementation time;
do not keep an unused compatibility API. Preserve `Run.checked()` as the
retry mechanism rather than introducing a second one for types.

### Remaining prose outputs

The following are not covered by the four new types:

- Compression, friction and premise reports currently receive only a nonempty
  check. Their instructions define different report content. Audit those
  contracts before proposing separate report types. A common type with only
  a nonempty body would centralize one check, not enforce those methods.
- The revision assessment and each pass's explanatory report are companion
  prose outputs, not decision mappings. `decide(..., also=[...])` does not
  validate companion content. Add types only after choosing which content
  requirements should be machine-checked; do not imply they become validated
  by typing the plan.
- Strike lists use a `No candidates.` sentinel or top-level Markdown entries.
  A possible later **`revision-candidates`** type could replace that grammar
  with a structured candidate list and make empty-list meaning explicit.
  That changes what the operator edits. Trial it separately; moving the same
  list parser into a type rule is not a simplification by itself.
- Revised note texts retain the original artifact's type, or remain plain
  text if the original has no frontmatter. Do not wrap or retype them as
  review reports just to make a directory layout accept them.
- CLI run summaries, Workjig records and approval records are execution
  state, not worker-authored review artifacts. This plan adds no KB types
  for them.

## Runtime integration

Use the existing parsed-document and type-resolution machinery:
`note_parser.ParsedDocument.to_validation_object()`,
`type_resolver.resolve_type_definition()`/`resolve_type()` and
`validate_instance()`. These already expose frontmatter, body, headings,
links and dates to JSON Schema. Required headings need no review-specific
regex interpreter.

Do not blindly inherit `note.schema.yaml`: it forbids a frontmatter field
named `status`. Rename the closing output's current `status` to
`closing-status` in code, prompts and fixtures at cutover, matching the
packet's vocabulary while retaining the closing judgment's larger enum.

Build only the small adapter needed to check captured candidate text under
an **expected** type and intended artifact path. It must:

1. Reject malformed/duplicate-key frontmatter and a missing or wrong `type`
   before schema validation. `validate_instance()` normalizes the type value
   to its profile, so that function alone does not prove the worker supplied
   the expected identity. The current frontmatter parser uses a safe YAML
   loader without duplicate-key rejection. Add that check at the parsing
   boundary; the directory manifest's `UniqueKeyLoader` is an existing
   precedent. This is added protection, not a removed check.
2. Apply schema, base and applicable imperative type checks through the
   normal validation machinery. A schema-only fast path must be explicitly
   described as partial validation, not full type conformance.
3. Preserve validation severity: existing schemas have warnings as well as
   failures. Do not turn every schema diagnostic into a rejected attempt.
4. Validate at the intended saved path, not the temporary worker-output
   path. Specify path context to workers. In particular, connect requires
   file-relative links, while review prose may refer to the reviewed note's
   paths. Test source checkout and installed-library resolution.
5. Supply the type specification and its schema dependencies as captured
   worker/check inputs, so a changed output contract cannot reuse an
   unchecked old answer. Audit schema-loader caching between invocations;
   do not add a registry or replay subsystem.
6. Feed actionable validation findings into the existing `checked()` retry.
   Validate explicitly supplied plans without making validation an approval
   action. An invalid supplied plan remains an operator error. Publication
   approval binds the checked candidate and context, not an editable plan.

Record intentional contract tightening, including duplicate-key rejection
and any newly closed field sets. A failed old fixture may expose a previously
accepted malformed output; do not silently weaken the new schema to preserve
it, or silently change a valid consumer contract to make a test pass.

Output validity and judgment freshness are different. A changed result type
requires current contract validation; it does not automatically imply that
the note/criterion judgment changed. Decide explicitly at cutover whether
old-format results are rejected or removed by an operator. Do not silently
mark malformed records fresh, bulk rewrite hashes or delete local history.
No compatibility layer is proposed without a named consumer need.

## Directory-type fit assessment

A [directory artifact](../../reference/definitions/directory-artifact.md)
uses `ARTIFACT.yaml` and a type's declared roles. The live implementation in
`directory_layout.py`, `directory_artifact.py` and `validation.py` is the
basis for this assessment, not a claim that directory types are universal.

### What fits now

Current layouts support fixed, direct-child Markdown roles with a fixed
expected type; required roles and one scalar-field discriminator; shared
identity fields; citation/verification relations; and optional exact-byte
member pins. Working instances can be incomplete, with missing-role
findings. Candidate bytes can be checked in a role before being written.

| Candidate | Fit | Recommendation |
|---|---|---|
| Entire Workjig run | Poor: nested calls, JSON state, YAML plans, dynamic pass/gate counts and multiple text versions. | Do not type the runtime directory. It is execution history, not one finished review product. |
| Gate sweep or bundle | Poor: requested gates vary by applicability and freshness; fixed roles cannot express an arbitrary requested set. | Keep individual typed results. A bundle type is not necessary to validate named per-gate outputs. |
| Revision run | Poor: variable passes, hash-keyed strike lists, arbitrary original artifact types and partial stops. | File types first. Do not encode a workflow state machine into layout requiredness. |
| One full-pass review cycle | Partial: several methods have fixed roles, but per-gate results vary and some method report types do not yet exist. | Revisit only after member contracts are settled. Do not create summary files solely to hide variable members from the layout. |
| A small completed full-pass evidence directory | Best bounded candidate: packet, disposition proposal and an optional closing judgment are fixed Markdown roles once the new types exist. | Optional later prototype, not a required deliverable. It could check completeness and identity agreement, but currently removes no substantial workflow check. |

The last candidate would be a product alongside the run, not a manifest
around every run file. It would require materializing typed decision and
closing outputs at stable paths. Required closing presence could potentially
follow the packet's `closing-status` values. Check no-edit, undetermined,
ready, hand-back and exhausted-repair cases before declaring that layout.

Do not equate the closing judgment's candidate-text hash with the packet's
final-text hash: on hand-back the note retains its starting text, while the
closing judgment concerns a rejected candidate. Identity declarations must
state an actual shared identity, not conceal this distinction. Pins prove
which member bytes are present; they do not prove those bytes were reviewed
or that publication was authorised.

### Limits that might justify evolution

- **Repeated or keyed roles:** no way today to declare “one result for each
  requested gate” or “one report per planned pass.” A future repeated-role
  facility would need a bounded declaration source, unique member keys,
  missing/extra-member diagnostics and reference semantics. Do not design it
  until a concrete product needs it.
- **Nested or non-Markdown members:** current role paths must be direct `.md`
  files. Nested artifacts and raw captures/YAML/JSON are not declared members.
  Open membership does not validate them. Adding globs alone would not solve
  role identity, containment or cross-member references.
- **Polymorphic subject roles:** a reviewed note may have any registered type
  or no frontmatter. A role currently expects one exact type. Do not change
  the note's type or add a dummy wrapper merely to fit the layout.
- **Verification protocol coupling:** live layout validation calls
  `protocol_findings()` for `verifies` roles and requires `## Blockers` and
  `## Limits`, with addressed blockers for several subjects. The review
  closing output uses `status`, `update` and `defects`; it is not that
  protocol. A possible evolution is selecting the verification protocol
  through the member contract instead of assuming one grammar. Runtime code
  must still apply its verdict to the exact subject version. Merely adding
  `verifies` cannot enforce approval, replay or publication.
- **Relations beyond equal fields:** identity compares fields of the same
  name; it does not compute content digests or map a candidate hash to a
  differently named packet field. Keep explicit version-binding checks, or
  justify a narrow type rule. Do not invent a general constraint language.

**Decision:** no directory-type change in this implementation sequence.
Reopen with one concrete evidence directory and examples of failures its
layout would catch. Adopt it only if those checks replace real conventions
or duplicated checks without distorting the artifacts. If an extension is
needed, commission that extension separately and test existing analysis-set
consumers; review adoption must not silently redefine `verifies` for them.

## Implementation sequence and acceptance

The approval-interface follow-up is committed as `e93284673`. Binding briefs
are implemented in `4a29b1bf5` for planning and editing workers without changing judge
inputs or result freshness. The two ordinary live revision trials completed
through publication. The operator subsequently prioritized the
[planning-free baseline](./planning-free-baseline.md) and independent operation
evaluation before this type cutover. Step 2 remains the first type implementation,
not permission to combine workflows or launch paid calibration. Ordinary plan execution needs no
approval; do not infer final publication authority from permission to prepare
a candidate. Live strike selection and full-pass validation remain separate
unfinished checks.

1. **Inventory and contract cutover.** Freeze the worker/stored-field split,
   audit footer consumers, and write the multi-consumer change packet. Choose
   behavior for existing local results and in-flight runs. Planning does not
   authorize deleting them. Keep the current operator-interface changes.
2. **One vertical slice: `review-result`.** Add the type/schema and candidate
   adapter; convert pair and bundle output acceptance and stored readers and
   writers together. Update criterion/prompts that teach the footer. Remove
   `outcomes.py` only after no production consumer uses it. Stop and compare
   the new adapter with the deleted checks before generalizing it.
3. **Full-pass decisions.** Add decision and closing types; share decision
   constraints with the existing packet schema. Validate stored packets.
   Remove local field schemas, heading checks and schema-expressible
   combinations, retaining filesystem and execution checks.
4. **Revision plan and connect.** Add the typed Markdown plan and update
   every named-plan/approval path. Enforce the existing connect type. Keep
   pass-catalog rules; distinguish checked links from unparsed candidate paths.
   Record remaining untyped
   companion reports rather than implying universal coverage.
5. **Review the deletion ledger and remaining gaps.** Demonstrate schema
   authority through malformed fixtures and changed-schema tests. Revisit
   other prose types only where a real contract or consumer warrants them.
   Directory typing remains a separate optional decision.

Required probes:

- Pair and bundle calls accept the same typed individual result format;
  omitted or wrong output types, bad outcomes and wrong criterion kinds are
  rejected. One malformed bundle output follows the existing retry policy.
- Passage quotes must exist uniquely in captured text. Invented or ambiguous
  quotes fail; legitimate document-wide and absence findings need no fabricated
  anchor. A live-note edit cannot make an invalid captured-text quote valid.
- Explicit saved-file and in-memory candidate validation still rejects malformed
  state artifacts beneath `.commonplace-validation-ignore`.
- Worker metadata cannot spoof captured inputs or executor provenance.
  Saved results and completed in-memory candidates validate identically.
- Invalid packet/closing field combinations and missing headings fail through
  schemas. Missing or unsafe merge paths still fail runtime checks.
- Revision plans reject unknown/repeated passes and wrong catalog order as
  before. Unapproved edits, changed approvals, stop overrides, named plans,
  changed instructions/profiles and publication conflicts retain their tests.
- Changing a type or a referenced schema changes acceptance and invalidates
  affected call reuse without relying on a process restart or stale cache.
- Connect links resolve from the intended report path in both checkout and
  installed-project probes. Nonempty but malformed connect reports fail.
- General, review, headless, validation, docs and affected installation and
  relocation suites pass; shared-runtime changes also select analysis consumer
  suites and relevant slow tests under `tests/README.md`. Changes to shared
  frontmatter parsing or type resolution also require the full fast suite.
- Validate type specs and representative output fixtures with
  `commonplace-validate`. Demonstrate the same rejection in worker acceptance,
  saved-file validation and operator-edited plan handling where applicable.

Paid live trials require the operator's direction. This plan adds no automatic
review-of-reviews loop and no new shared-orchestrator implementation. Report
partial completion by naming which output contracts are now typed and which
remain instruction-only; do not claim completion merely because files carry
`type:`.
