# Audit: post-trial epistemic-architecture instruction

## Verdict

The draft must not advance yet. All four cold-trial blockers received textual repairs, but only the no-candidate and material-route repairs are complete. The lifecycle-axis and non-content-route repairs still admit the conflations they were meant to prevent. Four additional blocking inconsistencies affect scope, integration, direct policy adaptation, and authority.

Both cold trials otherwise support the practical purpose. ARC exposed narrow checked-result, replay, and continuation routes without observed run instances. GBrain exposed unaccepted synthesis, absent or suspended disposition routes, and benchmark-gated policy adaptation. Neither agent needed clarification, both preserved evidence layers, and their materially different conclusions support a route-level procedure rather than a system-wide grade.

## Reconciliation

All findings were resolved in `candidate.md`:

| Finding | Resolution |
|---|---|
| F1 | Restored a declared-scope field with included and excluded components; assessed and unassessed route families now refine that boundary. |
| F2 | Replaced composite route kinds with one functional kind per row and a separate architectural-status field; checking/disposition and retention/integration must use separate linked rows. |
| F3 | Defined architectural status as a route fact, observed candidate state as an episode fact, and evidence layer as how either is known. Defined `no instance observed`, `not reached`, scoped absence, observed-but-uninspected routes, and the claimed-route early branch. |
| F4 | Restricted lifecycle integration to the post-acceptance branch. Pre-acceptance retention and use remain separate ledger functions and cannot be marked integrated. |
| F5 | Replaced the ambiguous transformation field with `content/update relation`, which distinguishes truth-apt transformations, non-truth-apt policy/content updates, and no content change. |
| F6 | Split operational authority from behavioral-authority path and broadened behavioral force to advisory, ranking, permissive, or enforcing effects. Extended the row-splitting rule to all authority-path fields. |
| F7 | Required output 1 to map every source ID to identity/revision and evidence layer, and defined a local anchor. |
| F8 | Split claim IDs from the mismatch marker; neither can substitute for the other. |
| F9 | Defined causal-experiment evidence as an interventional comparison plus design evidence, stated that contrast alone is insufficient, and required design/confounding limits on causal conclusions. |
| K1-K5 | Retained the trigger, operativity, type/collection conformance, material-route boundary, object-first order, evidence discipline, uncertainty branches, core warrant decisions, claim comparison, bounded conclusion, misuse guards, and trial-derived compression. No case narrative or broader knowledge ontology was added. |

## Coverage map

| Draft surface | Commitments checked | Basis | Audit result |
|---|---|---|---|
| Frontmatter, title, opening (`post-trial-draft.md:1-10`) | trigger, audience, route-level purpose, review-only force, epistemic-architecture and truth-apt definitions | brief; instruction collection/type contracts; reconstruction §§ Reconstructed governing result, Analysis units | Grounded and operative; K1 |
| Scope and prerequisites (`:12-47`) | system boundary, material-route cutoff, evidence layers, representational forms, early exits, exclusions | brief A4-A12; reconstruction §§ Evidence layers, Minimum executable procedure; trial blocker B4 | Material cutoff is repaired; the required output drops the declared scope, and the causal-evidence definition needs tightening; F1, F9, K2 |
| Source-and-claim boundary (`:49-57`) | revision, question, assessed/unassessed families, source IDs, missing evidence, system claims | disposition D1; trial optional compression | Scope regression and underspecified ID register; F1, F7 |
| Object inventory (`:59-63`) | stable object IDs, operative-part split, form, lineage, candidate content, claimed role, evidence | disposition B2-B5 and D2 | Grounded and executable; K2 |
| Authority-route ledger (`:65-71`) | route granularity, content/non-content distinction, target, evaluator, result, force, authorities, claim mapping, gaps | disposition C7-C20 and D3; trial blocker B2 | Repair is only partial: composite route kinds mix orthogonal facts; direct policy edits are misdescribed; operational and behavioral authority are collapsed; F2, F5, F6, F8 |
| Per-object lifecycle disposition (`:73-98`) | ampliative lifecycle, capability/state axes, non-ampliative, indeterminate, per-object/global no-candidate branches | discovery-lifecycle definition; disposition C2-C6 and D4; trial blockers B1 and B3 | Indeterminate and no-candidate branches are present. Capability/state semantics and integration remain unsafe; F3, F4, K3 |
| Claim comparison and bounded conclusion (`:100-118`) | doctrine/implementation/run/causal comparison, route-level verbs, warrant scope, no system scalar | disposition D5-D6; warrant and experimental-contrast notes | Grounded apart from claim-link and causal-evidence precision; F8, F9, K4 |
| Execution steps (`:120-160`) | dependency order, short exits, transformation decisions, route ledger, lifecycle, license bounds, claim comparison, final rule | claim skeleton and reconstruction § Minimum executable procedure | Mirrors the schemas, including their blockers; F2-F6, K4 |
| Misuse guards and verification (`:162-183`) | storage/use, novelty, labels, outcome/process, formal domain, route heterogeneity, doctrine/implementation, ontology neutrality, completion | disposition E1-E9 and D7; all named theory premises | Strong coverage, but no guard prevents retention from being marked as lifecycle integration; F4, K4 |
| Draft delta and proportionality | new trial-derived vocabulary, source IDs, material cutoff, compression, omitted rationale/cases | both cold trials; `trial-assessment.md`; collection reasoning constraint | Trial-derived additions are relevant and proportionate. No `kb/work/` dependency, outbound link, unresolved marker, extra frontmatter, or case-specific ontology remains; K1, K5 |

## Trial-blocker closure

| Trial blocker | Repair present | Closure |
|---|---|---|
| B1 — indeterminate disposition plus separate route capability and candidate-instance state | `post-trial-draft.md:73-90,144,178-179` | **Partial.** The third disposition exists, and the axes are separate fields. Their state semantics and the early claimed-route branch remain inconsistent (F3). |
| B2 — distinguish content transformations from non-content transitions | `:65-71,132-142,176-177` | **Partial.** The ledger has separate kind and content fields, but composite kinds encode availability, acceptance/disposition, and integration inside the kind; direct policy edits are forced to “content transformation: not applicable” (F2, F5). |
| B3 — distinguish per-object from global no-candidate handling | `:92-98,128,144,178` | **Resolved.** Both branches are explicit, and direct-adaptation routes remain reachable through route IDs. |
| B4 — define a material-route cutoff and completeness boundary | `:22-31,57,61,108,122-124,174-175,182` | **Resolved.** The draft defines materiality, conditions support-plumbing inclusion, names assessed and unassessed families, and prohibits a system-complete conclusion for partial coverage. F1 concerns the separate loss of the system/route scope field from output 1. |

## Blocking findings

Status: resolved

Finding F1 — The required output no longer records the declared analysis scope.

Blocking: yes

Recommendation: clarify

Anchor: `post-trial-draft.md:14-20,22-31,55-57,122-124,174`.

Disposition D1 requires system/revision, question, **and scope**. The trial repair added assessed and unassessed route families, but the post-trial schema replaced the original `scope` field instead of adding those fields beside it. Route-family coverage does not state whether the object under review is a subsystem, whole system, named route, or socio-technical boundary, nor which external components are excluded. Both cold trials needed that distinction: ARC bounded the harness against the external agent/environment, while GBrain bounded named subsystems against the rest of the product. Retain a separate declared-scope field; assessed/unassessed route families refine it rather than replace it.

Status: resolved

Finding F2 — The new `route kind` values conflate function with availability and lifecycle status.

Blocking: yes

Recommendation: clarify

Anchor: `post-trial-draft.md:65-71,142,168`.

The trials warrant a discriminator between content-changing and non-content routes, but not the composite ontology now imposed. `claimed but absent or suspended transition` is an availability/status statement, not a functional route kind. `check or disposition` merges evidence production with the decision that consumes evidence. `retention or integration` merges ordinary persistence with the successful-branch integration phase. These are precisely the boundaries the discovery-lifecycle and trial evidence require the instruction to preserve. Make functional kind independent of route availability, and require separate records when checking, disposition/acceptance, retention, integration, or operational consumption are distinct acts or carry distinct force. A claimed absent check can retain its claimed functional kind while recording absence separately.

Status: resolved

Finding F3 — The capability/state repair lacks a complete decision rule and conflicts with the early claimed-route branch.

Blocking: yes

Recommendation: clarify

Anchor: `post-trial-draft.md:75-82,126-130,144,179`; `arc-trial.md:424-427`; `gbrain-trial.md:174-177`.

The two axes solve the trials' structural problem, but their values remain ambiguous. The text does not distinguish `no instance observed` from `not reached`, say when `no route found within boundary` is licensed, or explain how an observed run can evidence a route when implementation source is unavailable without mislabelling observed evidence as `implemented`. More seriously, the second early branch orders lifecycle availability for every claimed object even though Step 6 says not to apply the lifecycle until ampliation is established. Define route availability as an architectural fact, candidate state as an episode fact, and evidence layer as how either is known. Reserve an absence value for an evidenced search boundary; use `no instance observed` when no candidate instance is available and `not reached` only for an observed candidate that did not reach the phase. In the early branch, use the indeterminate disposition unless the claim evidence itself establishes ampliation.

Status: resolved

Finding F4 — Lifecycle integration is still conflated with retention and later use.

Blocking: yes

Recommendation: clarify

Anchor: `post-trial-draft.md:71,82,86,94,144,160,165,178-179`; `gbrain-trial.md:78-84,90-92,118-128,160`.

The technical discovery lifecycle places integration on the successful branch after acceptance: it reconnects evidence or changes organization/use of an accepted claim. The schema instead defines the integration cell through a “retention/later-use consumer,” and the misuse guards forbid retention-to-acceptance leakage but not retention-to-integration leakage. The GBrain trial demonstrates the resulting drift by marking direct page writes and search availability as integration while recording acceptance absent. Require pre-acceptance retention and operational use to stay in their ledger routes. Mark lifecycle integration only when an accepted claim is subsequently integrated; otherwise use the applicable not-reached/absence/unknown state. Define that boundary inline and add it to verification.

Status: resolved

Finding F5 — `content transformation: not applicable` is false for direct adaptation that edits non-truth-apt policy content.

Blocking: yes

Recommendation: clarify

Anchor: `post-trial-draft.md:69-71,132-140,176`; `gbrain-trial.md:37-38,65-70,130-136,170`.

The GBrain held-out case contains the counterexample: SkillOpt changes prescriptive `SKILL.md` content and thereby adapts later behavior, while the output need not be truth-apt. The post-trial rule treats every such route as having no content transformation. That confuses “no truth-apt transformation to classify as acquisition/reshaping/derivation/conjecture” with “no content changed.” Narrow the field to truth-apt content transformation, or explicitly record the non-truth-apt policy/content update while keeping direct adaptation as the route kind. Do not force policy generation into the epistemic transformation classes.

Status: resolved

Finding F6 — The ledger collapses operational consequence into behavioral authority and uses a too-narrow permission definition.

Blocking: yes

Recommendation: clarify

Anchor: `post-trial-draft.md:69,142,177`; `arc-trial.md:115-128,265-308`; `gbrain-trial.md:60-70,168-170`.

Behavioral authority is the consumer/channel/force path by which retained material affects behavior; its force can be advice or ranking influence as well as permission or enforcement. Operational authority in the reconstruction is the behavior a check permits. The draft labels consumer/channel/force/horizon as `operational authority` and defines it only as later behavior “permitted,” which fits ARC continuation gates but not GBrain calibration influence or advisory consumption. State separately what operational transition a result permits, blocks, or changes and the behavioral-authority path through which an artifact/result becomes consequential, or explicitly define one field that preserves both subparts. Extend the row-splitting rule beyond target/timing/result/force when consumer, channel, horizon, evaluator domain, or epistemic license differs.

## Non-blocking findings

Status: resolved

Finding F7 — The compressed source-ID contract does not explicitly require an ID-to-source register, and `local anchor` is undefined.

Blocking: no

Recommendation: clarify

Anchor: `post-trial-draft.md:33,55-57,63,69,122`.

The trial assessment licenses source IDs to reduce repetition, but later records remain auditable only if output 1 maps every ID to a source identity and evidence layer. Say that explicitly and define a local anchor as the source-local section, symbol, line, event, or artifact locator available for that source form. This is a compression repair, not a new evidence layer.

Status: resolved

Finding F8 — `claim IDs or mismatch` permits an unkeyed mismatch.

Blocking: no

Recommendation: clarify

Anchor: `post-trial-draft.md:69,100-104,158`.

The trial assessment proposed claim IDs plus a short mismatch marker, leaving the full comparison in output 5. `Or` lets a ledger row report a mismatch without identifying the claim it mismatches. Require claim IDs (or `none`) and a separate short mismatch marker; keep the full evidence comparison in output 5.

Status: resolved

Finding F9 — The causal-experiment evidence layer states a necessary contrast condition as though it defined causal evidence.

Blocking: no

Recommendation: clarify

Anchor: `post-trial-draft.md:35-41,104,116,156,180-181`.

The experimental-contrast source establishes that a treatment/comparison pair and treatment grain bound a causal claim, but also says the contrast is not sufficient for causal identification. Define this layer as observed interventional comparison evidence, retain attribution at no finer than the actual contrast, and require design limitations to bound whether any causal conclusion is licensed. The existing component-attribution guard should remain.

Status: resolved

Finding K1 — Keep the trigger, frontmatter, opening force statement, and collection/type conformance.

Blocking: no

Recommendation: keep

Anchor: `post-trial-draft.md:1-10,12,49,120,162,172`.

The title is imperative, the description is trigger-focused, frontmatter is minimal, prerequisites/steps/verification are present, and the opening identifies the manual retrieval channel and review-informing force. The draft is self-contained and has no outbound or `kb/work/` link, unresolved authoring marker, or case narrative. This satisfies the instruction type and prescriptive collection contracts without pretending the instruction is automatically routed from the memory-review skill.

Status: resolved

Finding K2 — Keep the material-route cutoff, object-first order, evidence-layer discipline, and scoped-negative branches.

Blocking: no

Recommendation: keep

Anchor: `post-trial-draft.md:14-47,53-63,122-130,174-175`.

These commitments are grounded in brief A4-A12, typed-target ordering, the memory-review evidence stance, and trial blocker B4. They make whole-system cost and completeness explicit while preserving partial analysis. The early insufficient-evidence and out-of-scope exits are executable, and negative findings remain bounded to inspected evidence.

Status: resolved

Finding K3 — Keep the distinct indeterminate, non-ampliative, per-object no-candidate, and global no-candidate dispositions.

Blocking: no

Recommendation: keep

Anchor: `post-trial-draft.md:84-98,138,144,178`.

The GBrain trial demonstrated that indeterminate extraction cannot be forced into either preservation or conjecture. The ARC and GBrain reports demonstrated the need to distinguish one object without a candidate from an inventory with no candidate at all. These branches resolve trial blocker B3 and the indeterminate half of B1 without inventing a truth status.

Status: resolved

Finding K4 — Keep the core transformation/warrant decision, check-license separations, claim comparison, bounded conclusion, and misuse guards.

Blocking: no

Recommendation: keep

Anchor: `post-trial-draft.md:106-118,132-160,162-183`.

Acquisition, semantic-preserving reshaping, entailed derivation, ampliative conjecture, and uncertainty are grounded in the reconstruction and discovery-lifecycle boundary. Warrant remains claim-, domain-, contrast-, and route-scoped. Outcome, process, explanation, formalization, applicability, continuation, and component attribution stay distinct. The conclusion uses the disposition's authorized verbs and does not grant a system-wide score, universal oracle, or automatic acceptance.

Status: resolved

Finding K5 — Keep the trial-derived compression and avoid adding case rationale or a broader ontology.

Blocking: no

Recommendation: keep

Anchor: `post-trial-draft.md:33,51,108,174-183`.

Stable source IDs, grouped homogeneous conclusions, and decision-relevant synthesis respond directly to the two roughly 9,000-word cold reports. The additions remain output mechanics rather than claims about how every system represents knowledge. The instruction correctly omits ARC/GBrain mechanics, Commonplace review internals, product ranking, companion artifacts, and automatic memory-review integration.

## Advancement decision

The draft may advance only after F1-F9 are resolved and every keep finding is explicitly retained during reconciliation. F2-F6 are the true semantic blockers; F1 is a required-output blocker. Because F2 and F3 leave trial blockers B2 and B1 only partially closed, the current post-trial draft does not yet satisfy the promotion condition that all four trial blockers be resolved.
