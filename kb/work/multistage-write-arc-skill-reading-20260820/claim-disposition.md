# Claim disposition: ARC skill as a reasoning and epistemic tool

## Source-first disposition

This disposition treats a **target** as the object or transition a check addresses, an **oracle** as the mechanism that applies the check, **timing** as when that check runs relative to action or retention, and **force** as what the result can prevent, permit, retain, discard, or merely report. It also keeps **epistemic authority** (what a result licenses a consumer to rely on) separate from **operational authority** (how much subsequent behavior the result permits). A grade is not an operative oracle merely because it is stored; its result must change admission, survival, rollback, or continued execution over the declared route and horizon.

The evidence keys below are those defined in `reconstruction.md`. In particular, AP/AL/AU/AI/AC/ACL are selected ARC implementation files, AR/AS are ARC doctrine and author reports, EB/EA/EW/EO are the existing comparison, and CD/CE/CW/CO/CR/CX/CA/CL/CV are Commonplace's analytical premises. No incumbent target or draft was used.

### 1. ARC needs an authority-route ledger, not one system-wide oracle label

- **Proposed claim/contribution:** ARC is best described as several authority routes whose checked target, oracle, timing, force, epistemic implication, and operational implication differ; no single system-level “ARC oracle” or participation/containment cell preserves those differences.
- **Relation to the commissioned target:** This directly answers what ARC adds to or breaks in the five-case comparison. It supplies the organizing principle for the whole sixth-case reading.
- **Supporting source evidence:** The implemented routes separately cover prediction admission before a manual action, consequence grading after an action, suffix truncation after a queued miss, event-history replay before model search, plan-provenance refusal before execution, live consequence checks after each planned action, and environment outcome after action. Their targets and forces differ. **[AP, AL, AU, AI, AC, ACL]** The existing comparison currently assigns one participation/containment cell per system. **[EB, EA, EW]**
- **Closest existing artifacts:** `kb/notes/axes-of-artifact-analysis.md`, `kb/notes/definitions/behavioral-authority.md`, and `kb/notes/an-action-model-matters-only-through-its-consumption-path.md` already establish that authority and model mediation belong to operative parts and consumption paths rather than stored objects or whole systems. `kb/reference/proposals/revise-behavioral-authority-decomposition.md` already identifies applicability, staged path topology, force, and epistemic warrant as distinct concerns.
- **Disposition:** **Keep only in workshop target — central contribution.** The current artifact should apply the existing path-level theory to ARC and use it to resolve the workshop taxonomy question. It should not present the path principle itself as newly discovered.
- **Intended target path:** `kb/work/epistemic-architectures/arc-skill-reading.md`
- **Citation/revision boundary:** The importable claim here is ARC-specific: this ARC comparison must be route-level. The selected code warrants the route map, while the five-case workshop warrants the consequence for this comparison. A universal taxonomy claim would need its own evidence and should cite the existing authority-path artifacts rather than treating ARC alone as sufficient.

### 2. The object called “the model” must be disaggregated before any fit claim

- **Proposed claim/contribution:** ARC contains distinct prediction text, parsed prediction claims, an optional ungraded reason, prose notes, an executable `rules.py` model, a generated plan, environment progress, and a campaign scorecard; a statement that “the model passed” is ill-typed unless it names one of these targets.
- **Relation to the commissioned target:** This is the object inventory needed to populate the central authority-route ledger without transferring a result from one target to another.
- **Supporting source evidence:** The objects have separate parsers, storage, checks, and consumers in the selected doctrine and implementation. **[AS, AP, AL, AU, AC, AR]** The reconstruction's route table shows that their checks establish different propositions.
- **Closest existing artifacts:** `kb/notes/verification-needs-a-typed-target-before-it-needs-an-oracle.md` states the general target-class requirement; `kb/notes/theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md` blocks warrant transfer among claims, models, bundles, and scopes.
- **Disposition:** **Keep only in workshop target — structural support.** Use a compact object/route table rather than promoting a new definition.
- **Intended target path:** `kb/work/epistemic-architectures/arc-skill-reading.md`
- **Citation/revision boundary:** The inventory is specific to the supplied ARC surfaces. It does not assert that these are the only objects in the repository or that every campaign agent kept them distinct in practice.

### 3. Prediction admission enforces pre-registration, not strong falsifiability or explanation quality

- **Proposed claim/contribution:** The manual-action gate enforces a nonempty, parseable prediction with at least coarse automatically gradable observable content; it does not require a discriminating causal prediction, and the optional explanatory reason is ungraded.
- **Relation to the commissioned target:** This corrects the strongest doctrine/implementation overstatement and identifies the exact target and force of ARC's pre-action check.
- **Supporting source evidence:** Unrecognized prose becomes an ungraded note plus implied generic `change`; `cell` can pass on an already-present value; `--because` is optional and ungraded; absent or malformed prediction prevents the action path from reaching the environment. **[AP, AL, ACL]** The README's stronger “falsifiable claim” wording is doctrine. **[AR]**
- **Closest existing artifacts:** `kb/notes/oracle-strength-spectrum.md` distinguishes check strength; `kb/notes/theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md` limits what a passing check establishes.
- **Disposition:** **Keep only in workshop target — evidence for the central route analysis.**
- **Intended target path:** `kb/work/epistemic-architectures/arc-skill-reading.md`
- **Citation/revision boundary:** Attribute the grammar and blocking behavior to the selected parser/CLI path. Do not generalize “coarse” to every structured clause, and do not infer campaign use of deliberately weak predictions without run artifacts.

### 4. A post-action prediction grade warrants only the stated consequence on that transition

- **Proposed claim/contribution:** A structured prediction hit or miss bears on its parsed observable claim after one action; it does not by itself accept or reject the prose explanation, a unique causal model, the executable rules model, or the task strategy.
- **Relation to the commissioned target:** This supplies the epistemic-authority column of the prediction route and prevents “prediction fit” from becoming “theory standing.”
- **Supporting source evidence:** Each parsed clause is graded against the settled after-frame, level count, or environment state, while reasons and prose fragments are not graded and no implementation link identifies a unique motivating theory. **[AP, AL, ACL]** Warrant stays at the finest claim/model/scope the evidence identifies. **[CW, CE]**
- **Closest existing artifacts:** `kb/notes/theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md` already states the general non-distribution rule; `kb/notes/world-models-assess-explanatory-reach-through-action-conditioned.md` requires testing across the interventions or shifts a commitment claims, not one familiar transition.
- **Disposition:** **Keep only in workshop target — cited application of existing warrant theory.**
- **Intended target path:** `kb/work/epistemic-architectures/arc-skill-reading.md`
- **Citation/revision boundary:** State this as a limit on what the implemented grade entails, not as a defect or proof that a prediction cannot ever bear on a larger model when an independently specified dependency relation exists.

### 5. Queued execution has a one-surprise forward exposure boundary

- **Proposed claim/contribution:** In a manual batch or generated plan, the first mismatching action has already executed, but no later action in that queue executes; this is forward containment of operational authority, not prevention, rollback, persistent suspension, or theory rejection.
- **Relation to the commissioned target:** This is ARC's clearest distinctive force/timing result and the main reason “contained” cannot remain an unqualified epistemic label.
- **Supporting source evidence:** Grading occurs after each paid action; the first miss discards the remaining batch or plan suffix; a later standalone action remains available; there is no rollback of the surprising action. **[AL, ACL]**
- **Closest existing artifacts:** `kb/notes/definitions/operative-change.md` makes the operative horizon explicit; `kb/notes/definitions/behavioral-authority.md` supplies path and force; `kb/notes/warranted-autonomy-is-bounded-by-oracle-domain.md` keeps warranted evaluation authority within oracle scope.
- **Disposition:** **Keep only in workshop target — mechanism supporting the central contribution.** “One-surprise forward exposure boundary” should remain a local descriptive phrase unless more systems make the abstraction useful.
- **Intended target path:** `kb/work/epistemic-architectures/arc-skill-reading.md`
- **Citation/revision boundary:** Scope the boundary to one active queue. It says nothing about the cost or safety of the first divergent action, later standalone commands, other queues, or epistemic acceptance of the producing model.

### 6. Prose-note status and executable-model replay carry different epistemic force

- **Proposed claim/contribution:** ARC's note headings, event citations, post-miss revision, and cross-level demotion are mostly agent-governed doctrine plus nudges, whereas executable rules have an automatic replay relation to retained events; “Verified” prose and replay status must not be treated as the same kind of warrant.
- **Relation to the commissioned target:** This answers the brief's note, event-evidence, executable-model, and level-transfer questions while exposing route-level asymmetry inside the apparent theory layer.
- **Supporting source evidence:** Notes are initialized, archived, displayed, and nudged, but selected action paths do not validate headings, citations, semantic revision, or re-testing; the new-level banner clears on any later file edit. Rules replay can emit `MISMATCH`, `INCOMPLETE`, or `HISTORY_FIT`. **[AS, AI, AL, ACL, AU]**
- **Closest existing artifacts:** `kb/notes/retaining-the-episode-keeps-a-distilled-rule-re-derivable.md` supplies the episode/rule and lineage boundary; `kb/notes/methodology-enforcement-is-constraining.md` (title/description overlap) owns the general doctrine-to-enforcement gradient.
- **Disposition:** **Keep only in workshop target — descriptive comparison.** Exact display limits and modification-time mechanics may be examples, not independent contributions.
- **Intended target path:** `kb/work/epistemic-architectures/arc-skill-reading.md`
- **Citation/revision boundary:** Code establishes what the selected harness checks, not whether agents complied with doctrine or whether the notes were epistemically poor. Do not call executable replay full verification; its own boundary is disposed next.

### 7. Executable replay establishes bounded history fit, not general model warrant

- **Proposed claim/contribution:** `HISTORY_FIT` establishes consistency with the replayed event history under the model's render or author-chosen observation projection; it does not establish unseen mechanics, explanation quality, or global truth, and `INCOMPLETE` history can still leave a locally grounded solve route operationally available.
- **Relation to the commissioned target:** This states the exact epistemic authority and operational authority of the executable-model route.
- **Supporting source evidence:** Replay re-grounds around boundaries, records explicit `Unknown` gaps, compares exact render only when supplied, otherwise compares `observe`, and blocks solve on `MISMATCH` but not on `INCOMPLETE`. **[AU, ACL]**
- **Closest existing artifacts:** `kb/notes/theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md`, `kb/notes/first-principles-reasoning-selects-for-explanatory-reach-over.md`, and `kb/notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md` already bound formal/model evidence to its represented domain and obligations.
- **Disposition:** **Keep only in workshop target — route-specific finding.**
- **Intended target path:** `kb/work/epistemic-architectures/arc-skill-reading.md`
- **Citation/revision boundary:** The claim is about the selected replay and solve implementation. It must name whether equality was exact render equality or equality under `observe`; it must not equate search reachability inside the model with environment reachability.

### 8. ARC plan freshness is applicability, not endorsement

- **Proposed claim/contribution:** Matching event identity, current observation, and rule-file hash licenses use of a generated plan against unchanged inputs; it does not warrant the plan's producing theory, and subsequent live checks remain necessary.
- **Relation to the commissioned target:** This supplies the precise comparison with Commonplace's freshness baseline and prevents a shared word from hiding different targets and transitions.
- **Supporting source evidence:** ARC refuses stale provenance and then checks every executed plan step. **[AL, AU, AI]** Commonplace pins review evidence to note/criterion snapshots and explicitly separates freshness from endorsement or handled findings. **[CV]**
- **Closest existing artifacts:** `kb/reference/README-REVIEW-SYSTEM.md`, `kb/reference/freshness-architecture.md` (title/description overlap), and the brief's freshness definition already state Commonplace's side.
- **Disposition:** **Keep only in workshop target — bounded comparison, not a new general freshness claim.**
- **Intended target path:** `kb/work/epistemic-architectures/arc-skill-reading.md`
- **Citation/revision boundary:** Compare the shared applicability function, not storage design or transition semantics. ARC's plan provenance has no Commonplace-style acknowledgement transition; Commonplace review freshness does not execute actions.

### 9. ARC is a worked case for separating behavioral force from epistemic warrant

- **Proposed claim/contribution:** ARC demonstrates that strong operational containment can coexist with weak or absent epistemic acceptance: a plan can be provenance-bound and halted after divergence even when prose status is self-declared or executable history is incomplete.
- **Relation to the commissioned target:** In the current target this is the main consequence of the route ledger. As durable work, it supplies concrete external evidence for an already-live authority-decomposition problem.
- **Supporting source evidence:** Notes are not semantically gated, incomplete replay does not block all search, stale plans are refused, and live divergence truncates the remaining queue. **[AS, AL, AU, AI, ACL]** Existing warrant and authority theory explicitly separates what a check establishes from how an artifact can shape later behavior. **[CW, CA]**
- **Closest existing artifacts:** `kb/reference/proposals/revise-behavioral-authority-decomposition.md` already separates behavioral authority, epistemic warrant, applicability, staged path topology, force, and operativity. `kb/notes/definitions/behavioral-authority.md` is the current definition.
- **Disposition:** **Fold into existing artifact — later, separately authorized run.** Add ARC only as a bounded code-grounded worked case for the proposal's already-stated problem; do not revise the definition or settle the proposal's free choices in this run.
- **Intended target path:** `kb/reference/proposals/revise-behavioral-authority-decomposition.md`
- **Citation/revision boundary:** The fold should cite the eventual durable ARC source or a fresh direct code audit, not the temporary workshop as a durable source. It may establish that one real route family exercises the proposed distinctions. It must not claim that ARC validates a universal decomposition or that campaign agents complied with doctrine.

### 10. ARC uses consequence-mediated explanation participation

- **Proposed claim/contribution:** Explanatory content participates in ARC by generating predictions or plans, while the hard live checks mostly evaluate observable consequences rather than directly grading the explanatory content.
- **Relation to the commissioned target:** This local mechanism is more accurate than placing ARC simply on the “explanation participates” side of the workshop's 2×2.
- **Supporting source evidence:** Prose notes and executable models guide actions; parsed consequences and live after-states are checked; reasons are ungraded; replay checks executable behavior under a projection. **[AS, AP, AL, AU]**
- **Closest existing artifacts:** `kb/notes/an-action-model-matters-only-through-its-consumption-path.md` already distinguishes model-mediated pathways, and `kb/notes/world-models-assess-explanatory-reach-through-action-conditioned.md` describes consequence-testing for action-conditioned models.
- **Disposition:** **Keep only in workshop target — local analytical term.** One case does not yet warrant a new definition or taxonomy axis, and the closest library artifacts already carry the general mechanism.
- **Intended target path:** `kb/work/epistemic-architectures/arc-skill-reading.md`
- **Citation/revision boundary:** Use “consequence-mediated” to describe the route, not to claim that consequence fit establishes explanatory-reach. Direct note status, executable replay, and plan continuation remain separate routes.

### 11. ARC's decisive selection locus is often an action or plan, not a theory population

- **Proposed claim/contribution:** The selected implementation decisively rejects absent prediction admission, a contradictory executable model's access to search, a stale plan, or a diverging queue suffix; it does not expose a code-enforced accept/reject transition over a population of prose theories.
- **Relation to the commissioned target:** This prevents the sixth case from being forced into the weak-oracle selection conjecture merely because it records predictions and surprises.
- **Supporting source evidence:** Prediction misses remain recorded; prose theory revision is agent-managed; rules are evaluated for replay/search access; plans are checked for applicability and live continuation. **[AP, AL, AU, ACL]** Proposal-selection requires reject-capable evaluation and operative retention of the selected target. **[CL, CO]**
- **Closest existing artifacts:** `kb/notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md` already defines the required selection functions and force; `kb/notes/weakly-discriminated-qualities-tend-to-be-underselected.md` scopes underselection to offered candidates and reject-capable acceptance.
- **Disposition:** **Keep only in workshop target — scope conclusion.** Do not add ARC as positive evidence for theory underselection.
- **Intended target path:** `kb/work/epistemic-architectures/arc-skill-reading.md`
- **Citation/revision boundary:** This is an absence claim only over the selected files and supplied doctrine. It does not prove that no human or agent-level theory selection occurred during campaigns, only that the inspected harness route does not make it an operative acceptance population.

### 12. The participation × containment 2×2 does not survive unchanged at system level

- **Proposed claim/contribution:** ARC does not falsify participation or containment as questions, but it shows that one system-level cell collapses route, target, timing, and authority type: its prose notes, standalone predictions, queued actions, executable replay, plan freshness, and benchmark outcome occupy different profiles.
- **Relation to the commissioned target:** This is the commissioned comparison result and the direct answer to whether ARC is merely a sixth instance of an existing cell.
- **Supporting source evidence:** The ARC route table and the distinctions in items 3–11 show different participation and containment mechanisms. **[AP, AL, AU, AI, ACL]** The existing 2×2 assigns a system one cell and currently combines grade caps, advisory force, exclusion, and uncontained consumption under one “containment” axis. **[EA, EB]**
- **Closest existing artifacts:** The path-specific conclusion is already licensed by `kb/notes/axes-of-artifact-analysis.md`, `kb/notes/definitions/behavioral-authority.md`, and `kb/notes/an-action-model-matters-only-through-its-consumption-path.md`; `kb/work/epistemic-architectures/ai-research-os-reading.md` is the temporary 2×2 being tested.
- **Disposition:** **Keep only in workshop target — consequence of the central contribution.** Record that the candidate system-level 2×2 failed this worked-case gate. Do not promote the unchanged taxonomy and do not create a near-duplicate route-level note.
- **Intended target path:** `kb/work/epistemic-architectures/arc-skill-reading.md`
- **Citation/revision boundary:** The result rejects the 2×2's unqualified system-level use, not every possible route-level use of participation and containment. Any successor matrix must say whether containment limits epistemic status, operational continuation, or both.

### 13. ARC does not presently test the explanatory-quality underselection conjecture

- **Proposed claim/contribution:** The supplied ARC evidence cannot establish unequal selection over explanatory quality because it provides no independently characterized candidate-theory population, no harness accept/reject boundary over prose explanations, and no calibrated explanation-quality outcome.
- **Relation to the commissioned target:** This is a required negative result because the workshop was seeded by the underselection conjecture.
- **Supporting source evidence:** Explanation reasons and note status are not directly graded; selection force lands on admission, search eligibility, plan applicability, or queue continuation. The reported campaign supplies outcomes but not theory candidates or explanation-quality calibration. **[AR, AS, AP, AL, AU, CL, CO]**
- **Closest existing artifacts:** `kb/notes/weakly-discriminated-qualities-tend-to-be-underselected.md` already names the qualifying conditions and explicit scope; `kb/notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md` defines the required loop.
- **Disposition:** **Omit as a positive durable claim; keep only the explicit limitation in the workshop target.** ARC should not become an `evidenced-by` case for explanatory underselection on the supplied record.
- **Intended target path:** `kb/work/epistemic-architectures/arc-skill-reading.md` for the limitation; no library target.
- **Citation/revision boundary:** This does not refute the conjecture or show ARC explanations are good. It says only that the supplied architecture and campaign report do not instantiate the conjecture's evidential test over theories.

### 14. Campaign success and action-class miss rates do not identify component effects

- **Proposed claim/contribution:** The README's whole-system score and its lower reported miss rate for planned steps cannot identify the causal contribution of prediction pre-registration, notes, executable modeling, planning, or halt-on-surprise because action classes were selected by doctrine and no matched component contrast was run.
- **Relation to the commissioned target:** This bounds the empirical campaign paragraph and prevents a descriptive architecture reading from becoming a product-effect claim.
- **Supporting source evidence:** The reported score, prediction totals, plan share, and test-versus-plan miss rates come from AR; the checkout lacks run directories. Doctrine routes exploration to single steps and “proven” mechanics to plans. **[AR, AS, B]** A result identifies only the contrast actually run, and joint bundle support does not attribute component contribution. **[CX, CW]**
- **Closest existing artifacts:** `kb/notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md` and `kb/notes/theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md` already state the general causal and attribution boundaries.
- **Disposition:** **Keep only in workshop target — source-status and causal-scope boundary.** The exact reported quantities may be included as attributed observations, not as warrant for a mechanism.
- **Intended target path:** `kb/work/epistemic-architectures/arc-skill-reading.md`
- **Citation/revision boundary:** Preserve “repository-reported,” distinguish whole-system outcome from component effect, and avoid comparing action-class rates as if actions were randomly assigned to execution modes.

### 15. Independent campaign, compliance, and component-benefit claims need new evidence

- **Proposed claim/contribution:** Independent claims about campaign events, agent compliance with note/re-test doctrine, or causal benefits of ARC components require respectively run artifacts, compliance traces, or a matched intervention/ablation.
- **Relation to the commissioned target:** These are candidate claims the current evidence cannot support. Naming their exact evidence needs prevents plausible completion while keeping the code-grounded reading unblocked.
- **Supporting source evidence:** The brief says campaign directories are absent; code and doctrine cannot establish actual note repair or re-testing; the campaign score is a bundle outcome. **[B, AR, AS, AL, AI, CX, CW]**
- **Closest existing artifacts:** `kb/notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md`, `kb/notes/theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md`, and the evidence hierarchy in `reconstruction.md`.
- **Disposition:** **Evidence needed.** Omit the unsupported positive claims; retain one concise published limitation. The missing evidence does not block the selected central contribution.
- **Intended target path:** No additional target until exact evidence is acquired. If supplied later, regenerate reconstruction and disposition before changing the current claim boundary.
- **Citation/revision boundary:** Run artifacts could verify recorded events and compliance but still would not isolate a component effect. A component claim additionally needs a comparison that varies that component while controlling the relevant bundle.

### 16. Minor doctrine/implementation mismatches are examples, not independent contributions

- **Proposed claim/contribution:** The bounded note display, modification-time demotion signal, nudge-only escalation, and permissive `INCOMPLETE` solve route illustrate that ARC's selected code enforces less than the broad doctrine claims; none independently changes the comparison after the route/force distinction is stated.
- **Relation to the commissioned target:** These details can substantiate the code-over-doctrine evidence hierarchy but should not turn the commissioned reading into a defect catalogue.
- **Supporting source evidence:** The mismatches are enumerated in reconstruction from **[AR, AS, AI, AL, AU, ACL]**.
- **Closest existing artifacts:** The current target's route table is the correct home for the aggregate observation. `kb/notes/methodology-enforcement-is-constraining.md` already owns the general enforcement-gradient claim.
- **Disposition:** **Omit as independent claims.** Use at most the smallest examples needed to show which note and model statuses are doctrinal, nudged, or enforced.
- **Intended target path:** `kb/work/epistemic-architectures/arc-skill-reading.md` only as support; no separate artifact.
- **Citation/revision boundary:** Do not infer bad design, campaign noncompliance, or ineffectiveness from lack of a hard gate. The code finding is only that a stated rule is not enforced or graded by the inspected route.

### 17. “ARC verifies theories before acting” is not an admissible summary

- **Proposed claim/contribution:** The tempting one-line summary that ARC verifies a theory before action is false to the inspected architecture: before action it verifies prediction admission, while consequence fit, model replay, plan freshness, and task outcome occur at other times over other targets.
- **Relation to the commissioned target:** This is the main compression error the final prose must avoid.
- **Supporting source evidence:** Prediction grammar is checked before a manual action, structured consequences are graded afterward, replay is offline, freshness is checked before plan execution, live plan consequences afterward, and environment success after action. **[AP, AL, AU, ACL]**
- **Closest existing artifacts:** Items 1–8 of this disposition; the target/oracle distinction in `kb/notes/verification-needs-a-typed-target-before-it-needs-an-oracle.md`.
- **Disposition:** **Omit.** Replace it with the selected central contribution and route-specific statements.
- **Intended target path:** No target; this is an excluded formulation.
- **Citation/revision boundary:** No amount of campaign success repairs the category error because the error concerns which target each implemented check addresses and when.

## Selected central contribution for the commissioned target

**ARC is a route-asymmetric epistemic architecture: its checks address different targets at different times and exert different force, so the sixth-case comparison must classify authority routes and must report epistemic authority separately from operational authority rather than assigning ARC one system-level oracle or participation/containment cell.**

This is the single central contribution because it answers the governing comparison question and lets every other supported item serve as route evidence, mechanism, comparison, or scope. It also resolves the reconstruction's four-way candidate choice: route-level analysis is central; the epistemic/operational split and consequence-mediated participation are consequences inside that analysis; ARC is still retained as the sixth worked case. There is no unresolved decision and no blocking evidence gap for this target.

## Later durable library work

**Yes, one later and separately authorized library edit is warranted, but no new artifact is warranted.** ARC should be folded as a bounded code-grounded worked case into `kb/reference/proposals/revise-behavioral-authority-decomposition.md`. It directly exercises the proposal's existing distinctions among applicability/target, staged path topology and timing, force, epistemic warrant, and realized operational consequence. That run should use a durable ARC source or fresh direct code audit and should not treat this temporary workshop as a library source.

No separate participation × containment note is warranted: ARC defeats the unqualified system-level 2×2, while the useful route-level replacement is already substantially covered by the behavioral-authority and action-path artifacts. No fold into `kb/notes/weakly-discriminated-qualities-tend-to-be-underselected.md` is warranted on the supplied evidence because ARC does not expose a reject-capable theory population or calibrated explanatory-quality outcome.
