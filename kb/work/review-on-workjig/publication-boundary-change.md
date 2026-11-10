# Move routine approval to final publication

## Commission

On 2026-11-10 the operator clarified that private intermediate work is
preauthorized. The general approval boundary belongs immediately before
writing the reviewed artifact, not before executing a generated plan.
Unsettled wording and abstraction selections retain their operator stops.
Those stops are temporary procedure-development points: use retained
accepted/rejected choices and reasons to improve rules and checks, then test
on retained and fresh cases before separately authorizing automation.

Implement that boundary, then run the two already selected Sol revision
trials through preparation of the final candidate and diff. Do not approve
publication or modify either reviewed artifact. Do not force an unnecessary
wording pass to manufacture selection-stop coverage.

## Consumer change packet

| Field | Coverage and decision |
|---|---|
| Authoritative declaration | ADR 127, the revision/full-pass instructions, and the shared `edits.publication()` boundary. |
| Scope and enforcement | Both editing workflows require exact final-publication approval when changing a target. Intermediate results stay under the run. No-change completion and no-edit full-pass packets do not require artifact-write approval. |
| Resolvers and validators | Existing plan/catalog, candidate bounds, brief and original-text checks remain. The publication helper binds the candidate, original, target and decision context; operator approval does not validate an alternative candidate. |
| Schemas and derived values | No artifact schema changes. `publication.json` is code-owned approval state, not a new KB type. |
| Emitters | Revision executes generated and explicitly supplied plans without approval. Both editing workflows produce `final.md`, `final.diff` and `publication.json` before a changed target can be written. |
| Procedures and references | CLI help, workflow instructions, review guide, architecture, commands and ADR 127 describe publication approval rather than routine plan approval. |
| Collection/type contracts and control-plane templates | No change: this alters workflow authority, not artifact eligibility, type identity or installed routing. |
| Tests and fixtures | Revision and full-pass consumer tests cover automatic preparation, selection stops, final approval, replay and rejected stale or modified publication authority. General, headless, relocation and docs suites are selected alongside review tests. |
| Published views | No index or redirect mutation; changed reference/instruction pages publish normally. |
| Byte-pinned consumers | Changed instructions and prompts deliberately invalidate affected worker calls. No re-pinning or rewriting old run captures; these may cause new Sol assessments on continuation. |
| Old spellings | Searches across `src`, `tests`, `kb/instructions`, `kb/reference`: `operator\.answer|operator\.waiting` (7 lines); `plan.*approv|approv.*plan` (22); `assess.*stop|stop.*assess` (3); `publication\.json|final\.diff` (16). Counts were taken during implementation; final rescan follows integration. |
| Generated/projected forms | Editable installed command consumes the changed code and library instructions. No entry points, scaffold stubs or build metadata change. |
| Fresh and existing installs | Probe the bare installed command in a scratch initialized Git project. Existing local plan-approval records remain historical and are no longer consumed by revision. Explicit `--plan` is the override route; no silent migration or deletion. |
| Diagnostic promises | Waiting reports name final approval and show candidate/diff paths. Repeats cannot approve; changed context invalidates approval. Source/brief conflict blocks the write. Invalid supplied plans still fail validation. |
| Acceptance probe | Scratch named empty plan must complete without workers or approval; retained plan edits must not become implicit inputs. Live trials must stop with candidates and unchanged originals. Results recorded below after execution. |
| Drift guard | Shared publication helper and both workflow consumer tests enforce the same final gate. Strike-list tests retain their separate keyed approvals. |
| Historical witnesses | `approval-contract-change.md`, earlier workshop phase descriptions and old run captures describe the superseded plan gate. They remain historical evidence, not current operation. |
| Identity by convention | `artifact/plan.yaml` is retained output, not an implicitly editable input. `--plan FILE` explicitly supplies a plan. `publication.json` names exact final authority; `final.md` and `final.diff` are generated inspection artifacts. |
| Shared exclusions | No new artifact-selection predicate. Only actual target text changes trigger this publication gate. |
| Relocation side effects | No relocation, baseline migration or reviewed-note edits in this implementation. |

## Verification and live trials

Implementation verification passed before the live continuations:

- General, headless, review-workflows, agentic-analysis, relocation and docs
  default selections: **846 passed, 123 deselected**. Slow analysis workflow
  consumer selection: **17 passed**. These are selected suites, not a full-suite claim.
- Ruff and diff checks passed. All six edited library documents and the three
  workshop documents validated without failures or warnings.
- Scratch installed-project probe `/tmp/review-publication-probe-esw4_0uw`:
  an explicit empty plan completed without approval or workers. A second init
  preserved the run and a deliberately altered retained plan; a repeat used
  the explicitly supplied input rather than that altered output. The original
  stayed unchanged.
- Independent review exposed inspection-file tampering and deletion cases.
  The shared boundary now restores generated files and withdraws any approval;
  repeated execution cannot resurrect it. Tests cover changed/deleted manifest,
  candidate and diff, changed context with identical final text, changed
  selections and intermediate texts, and source/brief conflicts. A no-change
  full-pass result does not rewrite the original file.
- Final old-form rescan counts were 7, 22, 3 and 28 for the patterns above.
  Remaining plan-approval mentions describe its removal, generic operator-API
  fixtures with an arbitrary `plan.yaml` filename, or unrelated proposals.
  Historical workshop records and captured requests remain untouched.

The two trial targets and original assessment evidence are in the
[implementation plan](./plan.md#live-sol-assessments-2026-11-10). Live continuation
results will be recorded here. Publication remains outside this commission.
