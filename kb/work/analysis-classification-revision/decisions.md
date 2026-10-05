# Classification revision decisions

## G1 decision

Adopt revision 2 of `memory-comparison` for newly produced profiles. Keep the unversioned revision 1 readable for immutable retained sets. New workflow outputs must use revision 2. Never rewrite or mechanically reclassify retained profiles. Revision identity must survive matrix projection and CSV export; changed write-agency semantics must not be silently pooled across revisions.

Write agency measures control of admission for each write. `manual` requires an explicit human operator decision supplying, editing, approving or replacing that retained content. Software/model admission without that decision is `automatic`. Starting a workflow does not make later admission manual. Generic caller identity alone is unresolved, not manual. Authorship, physical I/O and behavioral authority are independent. This chooses the operator-control candidate under the plan's delegated semantic choice: it answers who controls admission rather than who invokes an API.

## Representation

Revision 2 has `version: 2`, `scope` and `axes`. Each axis has `assessment`, `units`, `records` and `note`. Keep the existing assessment vocabulary. Each unit has `scope`, `assessment`, `findings`, `records` and `note`. Each finding has one `value`, `basis`, `records` and `note`. A finding is authored once; values and evidence maps in downstream rows are derived, not independently authored.

Unit scopes name the actual object, path, transformation, input or consumer. Several findings can share a unit only when they share its classification scope and coverage. Distinct evidence bases stay on distinct findings even for the same value. `known` asserts complete classification within that named unit; `partial` retains positive findings plus named unresolved included parts; `not-determinable` means inspection did not establish any controlled value; `uninspected` names an uninspected included part. `absent` needs bounded absence records. `inapplicable` needs the relevant boundary and reason. All references resolve through the accepted record set. Units with unresolved scope cannot be dropped to obtain `known`.

Axis assessment describes coverage of the explicitly named inventory, not an independently authored value list. `known` requires all included units resolved and evidence that the inventory covers the scoped boundary. `partial` requires positive findings and unresolved coverage. No positives plus unresolved inspection stays `uninspected` or `not-determinable`. `absent` and `inapplicable` remain separately warranted. A wholly inapplicable unit inventory requires axis `inapplicable`, not `known`. Whole-axis push-signal inapplicability requires complete pull-only direction or bounded absence of read-back; trace-source inapplicability requires complete bounded absence of qualifying trace learning. A positive or unresolved prerequisite prevents whole-axis inapplicability. A positive witness never establishes complete inventory. Semantic verification checks inventory support; deterministic validation checks structure, references and incompatible combinations, not source truth.

Derived unions retain all supported positive findings. Strong evidence on one finding does not upgrade another. Matrix output retains unit data, axis coverage rationale and revision identity as well as a compatibility projection of value unions, strongest existence evidence and coverage. Complete-value statistics require complete coverage and strong evidence for every positive unit finding, not merely one strong witness per value. Local trace-learning `no` is bounded absence, never a system-wide negative in a partial axis; a positive `yes` suppresses `no` from the derived system union without erasing its local unit evidence.

## Axis units and boundaries

| Axis | Unit and boundary |
|---|---|
| storage_substrate | Each operative retained object/part, including opaque provider state; encoding is not substrate. |
| representational_form | Operative part and consumption path; split mixed text, symbolic and numerical parts. |
| lineage | Object/part and derivation path; known derivation does not resolve initial or embedding provenance. |
| behavioral_authority | Retained part, actual consumer and effect; several effects coexist and delivery is not compliance. Trace-fed artifact updates may establish learning authority at their update consumer; downstream knowledge consumption is separate. |
| write_agency | Write/admission mechanism, distinguishing human admission control, authorship and physical I/O. Reads do not establish writes. |
| curation_operations | Implemented transformation with evidence layer; a requested synthesis or route label is not an implemented new claim. |
| read_back_direction | Request, selection and delivery operations within a chain; delivery fulfilling a request is pull, independent unsolicited supply can be push. |
| read_back_signal | Actual selector and selected retained part on push operations; pull-only inapplicability needs complete direction coverage. |
| trace_learning | Each qualifying automatic trace-fed write and later consumer; improved capacity is a separate epistemic claim. Local bounded negatives do not negate positive alternatives. |
| trace_source | Original input to each qualifying trace-fed write; adapter labels do not determine provenance. |

Epistemic conditions, learning, reflection, autonomy and self-improvement retain independent route/property conclusions. Publishable bounded positives coexist with separately stated unestablished properties; unsupported assertions and concealed gaps remain blocking defects.

## Consumer inventory and delivery

- Profile type/schema: schema validation and declared profile/verify-profile packet dependencies.
- Record contract, memory/epistemic/reconcile/verify packets: declared workflow dependencies; source-native coverage and local uncertainty precede classification.
- Profile, verifier, synthesis and synthesis-verifier packets plus worker rules: job composition, correction/blocking and bounded public claims.
- `systems_matrix.py`, validation, set/workflow/finalization: validation must read both revisions, newly scheduled profile acceptance must require revision 2; immutable enumeration may read revision 1.
- Matrix/table/statistics scripts and landscape/taxonomy instructions: derived unions, coverage and revision-aware comparison. Inspect callers and update direct interfaces.
- Tests: schema/member, packet composition, workflow acceptance, matrix and synthetic semantic cases. Synthetic examples are not evidence for external systems.
- Skill projections remain canonical symlinks; no new skill name or acquisition/orchestration change.
- ADR 093 is superseded only for representation/changed semantics by a new implemented ADR; ADR 103's source-first classifier role remains intact.

The prior probes and audit are maintenance evidence only. Luna's retained evaluation is now available, but its Sol-comparison sentence conflicts with the current Sol result; do not use it to support a reliability or exact cross-model comparison claim. The original probe bytes remain untouched.

## Compatibility and stop boundaries

The real retained Dynamic Cheatsheet set warrants a narrowly marked revision-1 reader. Do not infer operator agency from its old caller-based classifications. Existing publications require separately authorized refresh. No full run, commit, publication or retained-data mutation is authorized by this implementation. Stop if the bounded dual reader cannot preserve frozen sets without fabricating classifications or if a semantic acceptance case cannot be expressed under these invariants.
