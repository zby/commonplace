# Update analysis classifications without hiding uncertainty

## Intent and end state

Deliver an executable revision of the full `analyse-agentic-system` procedure in which supported classifications and unresolved included parts coexist faithfully. The motivating write-agency probe is a starting point, not the final scope. Update affected definitions, author and verifier packets, schemas, code, tests, synthesis and downstream interfaces together. Leave the method ready for an operator-authorized full isolated test run at a committed revision.

Opening this workshop does not execute this plan. When commissioned to execute it, the executor may make the bounded design and implementation choices described below; uncertain consequential choices return to the operator. Do not launch a full analysis run or commit merely because the plan requires those steps before end-to-end acceptance.

## Acceptance invariants

1. A supported positive classification survives uncertainty about another included part.
2. An unresolved part remains named, inside its declared scope, with the missing fact and conclusion prevented. It is not omitted merely to obtain a clean result.
3. Explicit uncertainty alone does not block acceptance or publication. Unsupported values, unsupported completeness/absence claims, concealed coverage gaps and structurally invalid outputs still do.
4. A positive witness establishes existence, not complete enumeration of the system's values. A route that was not classified is not an absent route.
5. Evidence strength remains attached to the actual supporting part or mechanism. One wired route does not upgrade a claimed or opaque alternative.
6. Every classification references canonical accepted records. Profiles still add no source evidence or declarations. Source-native analysis, reconciliation and profile classification keep their roles.
7. Completeness and evidenced absence remain distinguishable from a partial positive set and from unresolved classification. Do not fix the presentation by silently losing that distinction in the matrix or synthesis.
8. Do not maintain independently authored copies of the same fact merely to fit a schema. Avoid the current duplicated value list/evidence-key bookkeeping when a simpler representation carries the same evidence.
9. Heterogeneous units retain their own conclusions. There is no system-wide epistemic score, universal evaluator, or bundled negative for learning, reflection, autonomy and self-improvement.
10. Shipped worker packets remain complete for their declared loading paths. Workshop evidence and this plan do not become execution inputs.

## Classification risks

All ten memory axes share the aggregate assessment structure. Address each explicitly, but choose its natural unit rather than applying a route list mechanically.

| Area | Failure to prevent | Candidate unit and required distinction |
|---|---|---|
| Write agency | Caller-triggered automation conflated with manual admission; unknown initial-sheet provenance or control forced into a binary answer | Write/admission mechanism; distinguish authorship, control and physical I/O. Resolve human operator versus generic caller explicitly. |
| Lineage | Unknown initial-sheet or embedding provenance erases a supported derivation path or is hidden by complete coverage | Object/part and derivation path; retain unknown provenance locally. |
| Storage substrate | Primary-store classification conceals other operative parts or opaque provider state | Operative object/part; include supported stores without inventing the opaque branch's store. |
| Representational form | Mixed checkpoint fields/payload or numerical/text material forced into one form | Operative part and consumption path; encoding is not substrate. |
| Behavioral authority | A system union loses distinct consumers/effects, or knowledge delivery is mistaken for every other force | Retained part, actual consumer and effect; reconcile the relationship to trace-fed updates without imposing a blanket implication. |
| Curation operations | A route name or prompt request becomes proof of synthesis, decay or another semantic operation; uncertainty suppresses supported operations | Implemented transformation with evidence layer; separate requested behavior from observed content transformation. |
| Read-back direction | Request, selection and delivery in one chain collapsed into one pull/push answer | Operation within the chain; classify both directions when independently established. |
| Read-back signal | Identifier on a file mistaken for targeted selection; one known pull route makes an opaque branch inapplicable | Actual selector and selected part; inapplicability requires the relevant boundary, not a convenient branch. |
| Trace learning | One positive or unresolved route incorrectly becomes a complete system-wide yes/no, or improved capacity is inferred from a retained update | Qualifying trace-fed write and later consumer; preserve bounded absence requirements. |
| Trace source | Adapter labels replace original input provenance; mixed or opaque inputs forced into a source category | Original input to each qualifying write; aggregate only supported categories. |
| Epistemic ledger and public synthesis | Separate route functions or independent properties collapsed into one unsupported negative | Preserve the existing route/function and property splits; uncertainty remains tied to its prevented conclusion. |
| Downstream matrix and comparisons | Missing or incomplete classification becomes an empty/negative category, or supported partial findings disappear | Derive supported unions while preserving unresolved coverage and evidenced absence separately. |

Observed starting evidence includes the write-agency failure and probe, an earlier unsupported `synthesize` profile value, provenance uncertainty and an audit-flagged learning-authority/trace-learning inconsistency. Other rows are prospective cases. Do not label all risks as observed failures.

## Scope and consumer inventory

Before changing a rule, follow [method maintenance](../../agentic-system-analyses/instructions/maintain-analysis-method.md), read the owning collection and selected type/instruction contracts, and identify each actual consumer and its loading channel. Search exact field names, file names and result literals. This is an initial inventory, not a complete allowlist:

- `kb/agentic-system-analyses/types/agent-memory-profile.md` and its schema: classifications, scope, evidence and coverage representation.
- `kb/agentic-system-analyses/types/agent-memory-analysis-report.md`, `types/agentic-system-epistemic-report.md`, and their schemas where changes are needed for source-side recording.
- `kb/agentic-system-analyses/instructions/agentic-analysis-records.md`: write-side roles, per-part status and required evidence. Preserve independent theory conditions and evidence layers.
- `kb/agentic-system-analyses/instructions/analyse-agentic-system/jobs/{memory,epistemic,profile,verify-profile,reconcile,verify,synthesize,verify-synthesis,worker-rules}.md`: ownership, supplied inputs, unknown-versus-blocker rules, correction and synthesis.
- `kb/agentic-system-analyses/types/agentic-system-analysis-overview.md`, set/manifest contracts and `instructions/analyse-agentic-system/SKILL.md`: amend only direct interface or operator-handoff consequences; do not redesign scheduling.
- `src/commonplace/lib/systems_matrix.py`, affected validation and workflow/set/finalization code: inspect dependencies rather than guessing that a profile-document edit is sufficient.
- `kb/agentic-systems/instructions/synthesize-agent-memory-landscape/SKILL.md` and other live taxonomy/comparison readers: inspect expectations about values, support and completeness. Update method interfaces, not their published results.
- Tests for member types, instruction composition, profiles/matrix, record/set acceptance, workflow and finalization; fixtures that encode the changed shape.
- Decision records, shipped command documentation and package/scaffold projections if the actual dependency search finds an affected interface. Existing ADR 093 and ADR 103 govern evidence and classifier roles; assess whether a new or revised ADR is required under the ADR procedure rather than amending historical rationale casually.

Authorization covers the coherent classification revision and necessary direct consumers when this plan is executed. It does not cover unrelated code cleanup, new orchestration features, auxiliary survey refreshes, retained report mutations or a blanket vocabulary redesign. Read-only dependency discovery may expand the inventory; substantial unrelated work becomes a separately reported item.

## Supported execution route

### 1. Resolve semantics and representation

Retain a concise decision record in this workshop before implementation. It must name:

- the scope and classification unit for each axis;
- definitions and consequential boundaries, especially write agency versus content authorship and authority;
- how supported classifications, weaker evidence, unresolved parts, bounded absence and inapplicability are represented;
- how source coverage is retained without an independently authored, unsupported complete-value assertion;
- derived system-level unions and downstream coverage semantics;
- all affected consumers and loading channels;
- the treatment of existing immutable analyses under changed contracts.

Use the probe and prior run audits as maintenance evidence. Do not copy their results into future source-first workers. The executor may select per-axis shapes and economical grouping under the invariants; literal reuse of the experimental YAML is not required. Do not add a new state or ontology unless a named acceptance case needs it.

The write-agency probe defines manual control as a per-write operator decision, with generic callers unresolved. Treat that as a tested candidate, not an already adopted universal definition. Choose and document the final semantic rule from product use and evidence; if competing meanings change comparison results and the intended metric cannot be established, return that choice to the operator before coding.

Existing retained analyses are real consumers, not an excuse for speculative compatibility. Never mechanically reclassify them or rewrite their frozen bytes. Determine whether a bounded contract/version distinction is necessary to keep them interpretable. Any required shim must satisfy the repository's consumer-need and BACKCOMPAT rules. If preserving them would demand uncommissioned migration or semantic fabrication, stop and propose a bounded operator decision.

### 2. Build discriminating acceptance cases

Create fixtures/examples that test the chosen definitions and representation before or alongside implementation. They may be explicitly synthetic; never present invented routes as source evidence. Cover at least:

1. Automatic curator admission plus an initial-sheet route with unknown control: retain the positive and the unresolved part; acceptance succeeds.
2. Explicit operator-controlled installation plus automatic subsequent updates: both agencies coexist, whether grouped or separate.
3. Automated API installation: do not infer human/manual control from the word caller.
4. Operator selection/read-back of an existing checkpoint: do not invent a write merely from a read; classify any separately established replacement correctly.
5. Known derivation path plus opaque initial/embedding provenance: retain both supported provenance and uncertainty.
6. Mixed symbolic/natural-language parts plus an opaque part: preserve supported forms and stores without falsely completing coverage.
7. Several consumers of one retained object with different effects: preserve each supported authority; check trace-learning/learning-authority distinctions on actual routes.
8. Requested synthesis without evidence of a new claim: do not classify it from its name; retain independently supported consolidation.
9. A chain with requested retrieval and automatic selection/delivery, plus an unresolved alternative: preserve direction and selector distinctions without unsupported inapplicability.
10. One qualifying trace-fed update plus an unclassified alternative, and mixed/opaque input sources: retain positives without a system-wide negative or fabricated source category.
11. Bounded evidenced absence versus not inspected, not determinable and unsupported positive: keep their meanings distinct. Uncertainty passes; unsupported assertion fails.
12. Public synthesis with a supported contribution and several independently unestablished properties: preserve separate scopes/limits instead of a bundled negative.
13. Matrix projection of supported partial values, unresolved entries and evidenced absence: positive counts survive; incomplete is not empty/absent; strong evidence on one witness does not upgrade another.

Preserve source-first record reference and reconciliation checks. The tests must not obtain acceptance by bypassing unresolved IDs or malformed data.

### 3. Implement the full interface change

Update canonical contracts, schemas, instructions, runtime consumers and fixtures together. Inspect skill projections and installed-package/scaffold delivery where affected. Recheck packet composition after changing an inherited rule. Every required definition must reach the worker through a declared dependency; do not rely on incidental background links.

Keep public synthesis bounded and readable. Faithful limitations remain publishable; a defect that makes any bounded account misleading still stops. Preserve meaningful negative evidence and the independent verifier, rather than achieving fewer blocks by relaxing support checks.

No task requires migrating unrelated current retained analyses or rebuilding comparison publications. Report those outputs as requiring separately authorized refresh if the interface change makes them stale.

### 4. Verify and hand off for the full run

Run relevant targeted tests during development, then `uv run pytest` and `uv run ruff check .`. All required tests must pass. Run `commonplace-validate` on changed KB artifacts and relevant collection/schema/loading checks. Review Git status and the complete diff; preserve unrelated modifications.

Retain a verification record with changed surfaces, commands/results, acceptance-case outcomes, remaining limitations and compatibility disposition. Do not call a Markdown schema pass proof of classification correctness. If an independent semantic review is delegated, preflight workers, give disjoint ownership and the experiment's acceptance/stop constraints, and retain its findings; no harness-specific model override is assumed.

Prepare an operator handoff that names:

- the full procedure/consumer changes and their intended effects;
- evidence that faithful unresolved cases pass while unsupported cases still fail;
- any remaining consequential decision or block;
- the commit containing the method, or that commit authorization is still required;
- readiness for the standard isolated full test run against Dynamic Cheatsheet at source revision `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`, unless the operator chooses another target;
- required separate authority for the test launch, publication/integration and comparison refreshes.

The committed method is a prerequisite for preparation. Never change the old run's method commit, reuse its run ID or repair its profile in place. A new full run uses the normal analysis skill and code-scheduled workflow; do not replace it with workshop replay outputs.

## Replanning and stop conditions

Return to the operator before implementation when a semantic choice changes what the axis measures and cannot be resolved from this commission, or when consumer/immutable-data handling requires a broader migration. Return after a failing acceptance case if the candidate design cannot express it faithfully without abandoning an invariant. Record the failure rather than widening scope silently.

Implementation has a fixed horizon: after the acceptance suite and consumer inventory discriminate the candidate design, implement and verify it. Do not keep adding unrelated examples or probes instead of finishing the procedure. A partial result must state what prevents the full-run readiness gate.

Stop on unavailable evidence, blocked installation/validation that cannot be repaired within scope, unsupported worker model/isolation requirements or uncertain public effects. Do not resume earlier workers or analysis loops. The executor retains scheduling and integration responsibility; delegated workers do not expand authority.

## Completion gates

- **G1 — Design:** axis units, semantics, uncertainty and consumer handling decided; consequential gaps returned.
- **G2 — Implementation:** canonical procedure, contracts, validation and affected consumers updated coherently; no workshop runtime dependency.
- **G3 — Verification:** acceptance cases, required tests, lint and KB validation pass; diff reviewed and limitations retained.
- **G4 — Ready for full run:** operator handoff and committed method revision available, or the single outstanding commit-authorization requirement stated. The method must be committed before launching preparation.
- **G5 — End-to-end evidence:** separately authorized fresh full run completed or its exact stopped/failed outcome retained; remaining findings dispositioned. Only then assess whether the revision improved full-run behavior.

G1 alone is not the outcome. G2–G4 deliver the requested full procedure update; G5 supplies the subsequent full test evidence needed before workshop closure.
