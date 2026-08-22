# Claim skeleton: ARC skill as a reasoning and epistemic tool

## Governing contribution

**ARC is a route-asymmetric epistemic architecture: its checks address different targets at different times and exert different force, so the sixth-case comparison must classify authority routes and must report epistemic authority separately from operational authority rather than assigning ARC one system-level oracle or participation/containment cell.**

This is an ARC-specific worked-case conclusion, not a newly discovered universal taxonomy. The artifact should use existing path-level theory to explain why the ARC comparison needs this shape. It may contain several route findings because the target is exploratory workshop text, but every finding must establish, apply, compare, or bound the governing contribution.

Confidence: high for behavior directly implemented in the selected ARC files; moderate for comparison against the historical workshop syntheses; attributed-only for campaign claims reported by the ARC README.

## Exact citation key for the eventual target

Paths here are relative to `kb/work/epistemic-architectures/arc-skill-reading.md`. Use these links verbatim; the short keys below are skeleton shorthand only.

### ARC doctrine and implementation

- **AR** — [ARC repository README](../../../../related-systems/arc-skill/README.md)
- **AS** — [ARC skill doctrine](../../../../related-systems/arc-skill/skills/arc-skill/SKILL.md)
- **AP** — [prediction parser and grader](../../../related-systems/arc-skill/skills/arc-skill/scripts/arc_skill/predictions.py)
- **AL** — [live execution](../../../related-systems/arc-skill/skills/arc-skill/scripts/arc_skill/live.py)
- **AU** — [executable-rule replay and search](../../../related-systems/arc-skill/skills/arc-skill/scripts/arc_skill/rules.py)
- **AI** — [inspection and status](../../../related-systems/arc-skill/skills/arc-skill/scripts/arc_skill/inspect.py)
- **AC** — [event core](../../../related-systems/arc-skill/skills/arc-skill/scripts/arc_skill/core.py)
- **ACL** — [CLI routes](../../../related-systems/arc-skill/skills/arc-skill/scripts/arc_skill/cli.py)

### Existing five-case comparison

- **EW** — [epistemic-architectures workshop framing](./README.md)
- **EB** — [four-system baseline](four-system-baseline.md)
- **EA** — [AI Research OS reading](ai-research-os-reading.md)
- **EO** — [operator correction](operator-response.md)

### Commonplace analytical premises

- **CD** — [discovery lifecycle](../../../notes/definitions/discovery-lifecycle.md)
- **CE** — [explanatory-reach](../../../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md)
- **CW** — [fine-grained theory warrant](../../../notes/theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md)
- **CO** — [weak-oracle underselection conjecture](../../../notes/weakly-discriminated-qualities-tend-to-be-underselected.md)
- **CR** — [episode/rule re-derivability](../../../notes/retaining-the-episode-keeps-a-distilled-rule-re-derivable.md)
- **CX** — [experimental contrast limit](../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md)
- **CA** — [warranted autonomy](../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md)
- **CL** — [proposal-selection loop](../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md)
- **CV** — [Commonplace review-system semantics](../../../reference/README-REVIEW-SYSTEM.md)
- **AX** — [artifact-analysis axes](../../../notes/axes-of-artifact-analysis.md)
- **BA** — [behavioral authority](../../../notes/definitions/behavioral-authority.md)
- **AM** — [action-model consumption paths](../../../notes/an-action-model-matters-only-through-its-consumption-path.md)
- **VT** — [typed verification targets](../../../notes/verification-needs-a-typed-target-before-it-needs-an-oracle.md)
- **OS** — [oracle-strength spectrum](../../../notes/oracle-strength-spectrum.md)
- **OC** — [operative change](../../../notes/definitions/operative-change.md)
- **ME** — [methodology enforcement](../../../notes/methodology-enforcement-is-constraining.md)
- **WR** — [action-conditioned world-model tests](../../../notes/world-models-assess-explanatory-reach-through-action-conditioned.md)
- **FR** — [formal-system explanatory-reach](../../../notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md)
- **BP** — [behavioral-authority decomposition proposal](../../../reference/proposals/revise-behavioral-authority-decomposition.md)

## Ordered target structure

### 1. Opening: one system name hides several checked objects

Work:

- Open directly with the governing contribution. Define an **authority route** in one sentence as a checked target plus oracle, timing, force, epistemic implication, and operational implication.
- Name the objects that must not be collapsed: pre-action prediction text; parsed prediction claims; optional ungraded reason; prose `NOTES.md`; executable `rules.py`; generated plan; environment progress; campaign scorecard.
- State the evidence order: selected code for implemented behavior; skill/README for doctrine; README for repository-reported campaign observations; existing workshop files for the five-case baseline.
- State that an operative oracle changes admission, survival, rollback, use, or continued execution. A stored grade alone is not enough.

Inferential link: because the objects have different parsers, checks, consumers, timing, and force, a claim that “the model passed” or that ARC has one oracle is ill-typed; the route ledger must precede the comparison.

Must establish:

- The object/route distinction is necessary to state what any ARC result warrants.
- Epistemic authority and operational authority are separate columns, not synonyms.
- Code can establish enforcement but cannot establish campaign compliance.

Must not imply:

- That the listed objects exhaust the entire repository or every informal belief an agent held.
- That route-level analysis is a novel universal theory; it is an application of existing path-level premises.
- The forbidden compression “ARC verifies theories before acting.”

Citations: AP, AL, AU, AI, AC, ACL for separate implementation surfaces; AR and AS for doctrine; AX, BA, AM, VT, CW, CO, and CL for the analytical boundary.

### 2. Main evidence table: ARC authority-route ledger

Use one table with exactly these columns:

| Target / route | Oracle and timing | Implemented force | Epistemic authority | Operational authority |
|---|---|---|---|---|

Required rows and payload:

1. **Manual-action admission.** Nonempty parseable `--predict` is checked before action; failure prevents the command reaching the environment. It establishes only prediction pre-registration in the accepted grammar. It does not establish prediction quality, causal discrimination, or explanation quality. Cite AP, AL, ACL, AR, OS.
2. **Structured prediction claim.** The settled after-frame, level count, or game state grades each parsed clause after the paid action. The grade bears only on that stated observable consequence on that transition. A standalone miss is recorded but does not persistently block a later standalone action. Cite AP, AL, ACL, CW, CE.
3. **Manual batch.** Every step has a parsed prediction; after each executed action, the first miss, level advance, game over, or win discards the queue suffix. The surprising action has already happened. Call this a **one-surprise forward exposure boundary** over one queue. Cite AL, ACL, OC, BA.
4. **Retained event evidence and inspection.** JSONL events, settled frames, actions, environment state, prediction fields, receipts, diffs, and labeled click hypotheses provide inspectable episodes. Retention makes later checking and re-derivation possible; it does not itself accept a theory. Cite AC, AL, AI, CR.
5. **Prose notes and level transfer.** Headings, event citations, post-miss revision, and demotion across levels are doctrine supported by initialization, display, archive, warnings, and nudges. The selected action routes do not semantically validate headings, citations, repairs, or re-tests; any later edit can clear the modification-time warning. Cite AS, AI, AL, ACL, ME.
6. **Executable-model replay.** Re-grounded replay returns `MISMATCH`, `INCOMPLETE`, or `HISTORY_FIT`; exact `render` is checked when present, otherwise equality is under the author-chosen `observe` projection. This establishes bounded recorded-history consistency, not unseen mechanics, explanation quality, or global truth. Cite AU, ACL, CW, CE, FR.
7. **Rule-model search.** `MISMATCH` blocks search, while `INCOMPLETE` does not if the current state can be grounded; `Unknown` edges are skipped. Search establishes reachability inside the supplied modeled region, not environment reachability outside it. Cite AU, ACL.
8. **Generated-plan applicability and live execution.** Event identity, observation hash, and rule-file hash are checked before execution; every action result is checked after execution. Stale provenance refuses the plan, and first divergence discards the remaining suffix. This bounds plan use and continuation without endorsing the producing theory or rolling back the divergent action. Cite AL, AU, AI, CA, BA.
9. **Environment progress.** Returned state and completed-level count determine level/game completion after action, including cases where a prediction misses. Task success is a distinct result target. Cite AL, AC.
10. **Campaign scorecard.** README-reported benchmark outcome is an after-run whole-system observation, not an in-harness theory acceptance event or component ablation. Cite AR, CX, CW.

Table-level inference: operativity moves among admission, recorded grading, search eligibility, plan applicability, queue survival, and environment completion. Therefore “the operative oracle” has no unqualified system-wide referent in ARC.

The table must establish:

- Every retained route finding from disposition items 2–8.
- The target/oracle/timing/force chain needed for the central claim.
- Why a result may have strong behavioral force but narrow or absent epistemic force.

The table must not imply:

- Equal strength or semantics across its checks.
- That post-action containment prevents or rolls back the first surprising action.
- That a prediction grade transfers to notes, `rules.py`, strategy, or benchmark success.
- That doctrine-only requirements were followed in campaign runs.

### 3. Interpretation: where epistemic and operational authority diverge

#### 3.1 Prediction admission, consequence fit, and queue survival are three different transitions

Work:

- Explain the minimum grammar boundary: unrecognized prose is ungraded and induces generic `change`; `cell` can pass on an already-present value; `--because` is optional and ungraded.
- Contrast the pre-action admission gate with post-action clause grading and, only for queued routes, post-surprise suffix truncation.
- State that a hit or miss bears on the parsed observable claim at one transition. It neither identifies a unique causal model nor directly accepts/rejects prose explanation.
- Make the queue horizon exact: the first mismatching action is spent; only later actions in that active queue are prevented; later standalone commands remain possible.

Inferential link: ARC enforces pre-registration and forward containment, but those operational properties do not enlarge the epistemic content of the consequence check.

Must not imply: every clause is equally coarse; coarse claims were deliberately used during the campaign; misses are harmless; the system rolls back; or one miss rejects every theory that could have generated the prediction.

Citations: AP, AL, ACL, AR, CW, CE, OS, OC, CA.

#### 3.2 Notes and executable rules form unequal episode/representation pairs

Work:

- Compare event-cited prose notes with executable rules against the same retained episode history.
- Notes have self-declared `Verified`/`Assumed` status and agent-managed repair; executable rules have an automatic replay relation.
- Bound replay precisely: `HISTORY_FIT` is history- and projection-bounded; `INCOMPLETE` records gaps yet may permit locally grounded search; only `MISMATCH` blocks solve.
- Mention only the smallest doctrine/code examples needed: modification-time demotion and nudge-only note repair. Do not catalogue UI/display discrepancies.

Inferential link: inspectable evidence plus automatic replay gives the executable route stronger checking than prose lineage, but neither result licenses general explanatory warrant.

Must not imply: notes were poor or noncompliant in actual runs; automatic replay is full verification; `INCOMPLETE` means the model is false; `HISTORY_FIT` tests transfer or rival explanations.

Citations: AS, AC, AL, AU, AI, ACL, CR, CW, CE, FR, ME.

#### 3.3 Plan freshness bounds use, not endorsement

Work:

- State the ARC applicability tuple: current event identity, observation, and `rules.py` hash must match plan provenance.
- State the second-stage live check: unchanged inputs authorize attempting the plan, then each resulting observation determines whether its suffix survives.
- Compare to Commonplace only on the shared function: freshness binds evidence or a plan to unchanged inputs. ARC has no acknowledgement transition; Commonplace freshness does not execute actions.

Inferential link: provenance can strongly constrain operational use while saying nothing about whether the source theory deserves epistemic acceptance.

Must not imply: shared storage design; identical transitions; that fresh means true, endorsed, or fully handled; that a stale plan's underlying theory is false.

Citations: AL, AU, AI, CV, CA, BA.

#### 3.4 ARC uses consequence-mediated explanation participation

Work:

- Name the mechanism locally: notes or executable models generate predictions and plans, while hard live checks mostly evaluate observable consequences.
- State the main consequence: strong operational containment can coexist with weak or absent epistemic acceptance. A provenance-bound plan may be halted even when note status is self-declared or replay is incomplete.
- Identify the decisive selection locus in the selected implementation: absent prediction admission, contradictory model access to search, stale plan use, or a diverging queue suffix—not an accept/reject transition over a population of prose theories.

Inferential link: explanation participates through action generation, yet the selection and containment targets are often actions or plans. This is neither explanation exclusion nor direct epistemic grading of explanation.

Must not imply: consequence fit establishes explanatory-reach; no human or agent-level theory selection occurred; the campaign tests unequal selection over explanation quality; or “consequence-mediated” is already a warranted universal taxonomy axis.

Citations: AS, AP, AL, AU, ACL, CE, CL, CO, AM, BA.

### 4. Comparison with Commonplace and the five existing cases

Preface the table with the evidence boundary: this run compares ARC to conclusions in the historical workshop files; it does not independently re-audit the underlying Eigenius, ScienceFlow, AI Research OS, or ontology sources. Note that the ontology draft has no observed running loop and that EO records the operator's lab-tooling intent.

Use one table with these columns:

| Existing case | Operative selection/checking locus in the supplied comparison | Explanation route and authority | What ARC adds or changes |
|---|---|---|---|

Required rows:

1. **ScienceFlow.** Task-metric evaluator gates stage acceptance; retained state lacks a claim/hypothesis object, so explanation is absent. ARC also has task outcome, but adds action-guiding notes/models and per-action consequence checks. ARC is not the absent-explanation case. Cite EB plus AP, AL, AU.
2. **Ontology draft.** Measurement policy works over signed attestations; hypothesis/Knowledge is represented but unscored and non-authoritative; no running loop was observed, and EO frames this as intended lab-tooling scope. ARC does not exile explanation: notes and models guide behavior, though hard checks mostly land on consequences. Cite EB, EO, AS, AU.
3. **Eigenius.** Formal/type/certificate checks create route-specific gaps, while mechanized faithfulness is capped below `Verified`. ARC likewise requires route analysis, but its distinctive containment is plan provenance and after-action queue halting rather than primarily an epistemic grade cap. Cite EB, AL, AU.
4. **Commonplace.** Structural validation and verdict-kind gates can have acceptance force; explanatory-reach critique is report-kind and the manual reach audit is outside default acceptance. ARC's per-action consequence checks are more immediately operative, while its freshness resembles Commonplace only as an applicability boundary. Neither freshness marker is endorsement. Cite EB, CE, CV, AL, AU.
5. **AI Research OS.** Structural lint and attention routing coexist with universal page retention and no reject-capable content acceptance; explanation is the retained medium but remains operationally uncontained. ARC also retains editable synthesis, yet keeps inspectable events, automatically replays executable rules, and halts queued actions after divergence. Cite EA, AI, AU, AL.
6. **ARC conclusion row.** Prediction presence gates admission; observation grades consequences and bounds queue continuation; replay controls model-search eligibility; hashes control plan applicability; environment controls task completion. Notes, reasons, predictions, and executable models participate through different routes. Cite AP, AL, AU, AI, ACL.

Table-level inference: the five cases already hid several meanings under “containment”—grade cap, advisory force, explanation exclusion, or absent acceptance. ARC adds multiple such profiles inside one system and makes the collapse untenable.

The table must establish:

- An explicit comparison with all five prior cases, including Commonplace.
- ARC remains useful as a sixth worked case even though it does not warrant a new general taxonomy.
- ARC's distinctive contribution is temporal and route-level asymmetry, not simply “more rigorous prediction.”

The table must not imply:

- A system ranking, product review, or independent validation of the earlier cases.
- That all five cases have equal evidence grades.
- That ARC is unique in every route mechanism; the conclusion concerns what this case forces the comparison to preserve.

Citations for the comparison frame: EW, EB, EA, EO.

### 5. Commonplace-specific epistemic comparison

Use four compact paragraphs or a small three-column table (`Commonplace distinction | ARC route | comparison limit`). Each unit must do different work:

1. **Discovery lifecycle.** Commonplace separates conjecture, consequence derivation, test, acceptance, and integration. ARC implements consequence pre-registration and testing at action grain, but not a code-enforced acceptance transition for prose mechanics. `HISTORY_FIT` is a bounded test status, not general explanatory acceptance. Cite CD, AS, AU, ACL.
2. **Warrant granularity.** One prediction grade bears on one parsed consequence and transition; replay bears on an integrated executable model under its chosen comparison surface; the benchmark bears on the configured bundle. None automatically distributes warrant to prose theory, prediction gating, notes, planning, or base model. Cite CW, AP, AU, AR.
3. **Explanatory-reach.** Next-frame predictions are criticizable consequences and executable rules expose a mechanism, but recorded-history replay does not by itself vary load-bearing premises, eliminate relevant rivals, or test transfer beyond observed/measured routes. Live plan checking adds prospective fit only along encountered paths. Cite CE, AU, AL, WR, FR.
4. **Freshness and operational authority.** Commonplace pins review evidence to exact note/criterion snapshots; ARC pins a plan to current event, observation, and rules. Both are applicability claims, but only ARC directly meters action continuation. Cite CV, AL, AU, AI, CA.

Section-level inference: Commonplace supplies the distinctions needed to avoid transferring ARC's operational containment into epistemic warrant, while ARC supplies a concrete external case where that separation is load-bearing.

Must not imply: Commonplace has stronger empirical truth guarantees; ARC adopts the Commonplace discovery lifecycle; history fit is an assay outcome; or the analogy extends beyond each named function.

### 6. Taxonomy gate: participation × containment 2×2 — **FAIL unchanged**

State the result exactly: **the system-level participation × containment 2×2 fails unchanged on the ARC case.** ARC does not falsify participation or containment as questions. It falsifies the adequacy of assigning the whole system one unqualified cell.

Use a compact pressure-test table:

| ARC route | Explanation participation | Epistemic containment | Operational containment | Why one system cell loses information |
|---|---|---|---|---|
| Prose notes | direct action-guiding synthesis | self-declared status; no semantic gate in selected routes | can influence later actions without a note-level accept/reject transition | participation without matching epistemic containment |
| Standalone prediction | forecast participates; optional reason ungraded | grade limited to one consequence | admission is gated, but a miss creates no persistent stop | pre- and post-action forces differ |
| Manual batch | forecast guides each action | same transition-bounded grade | first surprise truncates only the future suffix | containment is temporal and queue-scoped |
| Executable replay/search | causal executable model participates | history/projection-bounded `HISTORY_FIT`; gaps explicit | `MISMATCH` blocks search; `INCOMPLETE` may proceed locally | epistemic status and search eligibility do not coincide |
| Generated plan | model-mediated action sequence participates | freshness does not endorse the model | stale plan refused; live divergence halts suffix | strong operational containment without model acceptance |
| Benchmark outcome | configured bundle participates only as a whole | no theory/component attribution | environment outcome ends the task | outcome is not an explanatory selection oracle |

Inferential link: “contained” currently collapses at least epistemic status, applicability, search eligibility, and continuation horizon. A successor comparison must name route, target, timing, and force, then say whether containment limits epistemic status, operational continuation, or both.

Must establish:

- Disposition item 12's exact failure result.
- Participation remains useful when qualified as direct or consequence-mediated and attached to a route.
- Operational containment can be strong while epistemic acceptance remains weak or absent.

Must not imply:

- That every route needs its own permanent taxonomy cell.
- That the two questions are useless or that every possible route-level 2×2 fails.
- That ARC alone warrants a universal replacement taxonomy.
- Promotion of the unchanged 2×2 or creation of a near-duplicate route-level note.

Citations: EA and EB for the tested 2×2; AP, AL, AU, AI, ACL for the failing ARC profiles; AX, BA, AM, CW, and CA for the route/authority interpretation.

### 7. Campaign observations and evidential limits

Use one short attributed paragraph or boxed list. The point is to bound the architecture reading, not sell performance.

Repository-reported observations available to mention:

- 25/25 games and 183/183 levels, RHAE 100.00, and 7,645 actions versus a reported median-human 17,135.
- 7,627 graded predictions with 443 misses and at least one miss in every game: local error and whole-system completion coexisted, but this does not identify why completion occurred.
- 91.6% of presses reportedly occurred in plans; single test presses missed 37.1% and planned steps missed 2.9%. Doctrine routes exploration and “proven” mechanics differently, so these are selected action classes, not an intervention on planning or halting.
- 115 reported context compactions and median notes length of 60 lines are compatible with notes serving recovery, but do not establish note quality, citation fidelity, compliance, or causal necessity.
- Offline Python was reportedly used in 24/25 games; the shipped full `rules` route was attempted once and never fit. The campaign supplies little positive worked evidence for that specific route despite its implemented contract.

Mandatory source-status sentence: the checkout supplied no run directories, so all quantities and campaign behavior above remain claims reported by AR rather than independently reconstructed event evidence.

Mandatory causal boundary: the score is a whole configured-system outcome. No matched comparison isolates prediction pre-registration, post-action halting, notes, executable modeling, planning, or base-model contribution; the test-versus-plan miss-rate contrast is confounded by doctrine-driven routing.

Must not imply:

- A component effect, ablation result, random assignment, campaign compliance, or independently verified scorecard.
- That frequent misses prove explanatory correction, or that lower plan-step misses prove prediction gating works.
- That the implemented full `rules` route explains campaign success.

Citations: AR and AS for reported quantities and routing doctrine; CX and CW for causal and bundle-attribution limits.

### 8. Negative result: ARC does not test explanatory-quality underselection

Work:

- State only the evidential limitation: the supplied evidence has no independently characterized candidate-theory population, no harness accept/reject boundary over prose explanations, and no calibrated explanation-quality outcome.
- Connect the absence to the actual selection loci found in section 3.4: actions, model-search eligibility, plan applicability, and queue suffixes.
- Conclude that ARC should not become positive `evidenced-by` support for the explanatory-quality underselection conjecture on this record.

Must not imply: the conjecture is refuted; ARC explanations are good or bad; no theory comparison happened informally; or new evidence could not change the disposition.

Citations: CO, CL, AR, AS, AP, AL, AU.

### 9. Bottom line and handoff

Work:

- Restate the governing contribution once, now as the answer to the comparison: ARC is retained as a useful sixth case because it shows why system-level labels transfer results among unlike routes.
- State the actionable taxonomy outcome: keep participation and containment only as route-qualified questions, and report epistemic authority separately from operational authority.
- Record the durable-work boundary: no new participation × containment note is warranted. A later, separately authorized edit may add ARC as a bounded worked case to BP; it must use a durable ARC source or a fresh direct code audit, not cite this temporary workshop as durable evidence.
- State that the later fold may show that one real route family exercises the proposal's existing distinctions, but may not settle the proposal's open design choices or validate a universal decomposition.

Must not imply: authorization to perform the fold in this run; a new library artifact; promotion of the unchanged 2×2; or campaign compliance.

Citations: BP, BA, AX, AM for the handoff boundary; AP, AL, AU, AI, ACL for the ARC worked case.

## Claim-disposition coverage

| Disposition item | Skeleton destination |
|---|---|
| 1. Authority-route ledger | Sections 1–2; governing contribution |
| 2. Disaggregate “the model” | Sections 1–2 |
| 3. Admission is pre-registration | Sections 2 and 3.1 |
| 4. Grade is transition-bounded | Sections 2 and 3.1 |
| 5. One-surprise forward exposure | Sections 2, 3.1, and 6 |
| 6. Notes versus executable replay | Sections 2 and 3.2 |
| 7. Bounded history fit | Sections 2, 3.2, and 5 |
| 8. Freshness is applicability | Sections 2, 3.3, and 5 |
| 9. Operational force versus warrant | Sections 3.4, 5, 6, and 9; later fold stays a handoff |
| 10. Consequence-mediated participation | Sections 3.4, 4, and 6 |
| 11. Selection locus is action/plan | Sections 3.4 and 8 |
| 12. System-level 2×2 fails unchanged | Section 6 |
| 13. Underselection not tested | Section 8 |
| 14. Campaign rates do not identify effects | Section 7 |
| 15. New evidence needed | Published limitations in sections 7–8 |
| 16. Minor mismatches are examples | Only the two bounded examples in section 3.2; no defect catalogue |
| 17. “Verifies theories before acting” | Explicitly excluded in section 1 |

## Marker disposition

- **Blocking:** none. The selected central contribution is supported without campaign run directories or an ablation.
- **Define in published text:** “authority route”; operative oracle; epistemic versus operational authority; “model” only with its named ARC object; consequence-mediated participation; containment only with its target and authority type.
- **Publish as limitations:** campaign facts are repository-reported; campaign compliance is unknown; component benefits are not identified; explanatory-quality underselection is not tested.
- **Omittable:** exact parser catalogue beyond the two admission examples; display truncation; installation, API, locking, rendering, colour, coordinate, and solver-bound details; game anecdotes; exact plan anecdotes; implementation-redesign suggestions.
- **Evidence that would reopen the boundary:** run artifacts for independent campaign events; compliance traces for note repair/re-test claims; a matched intervention or ablation for component-benefit claims. Any such addition requires reconstruction and disposition to be regenerated before altering the target claim.

## Prose discipline for the drafting stage

- Keep the route ledger as the factual spine. Later prose should interpret it, not repeat every cell.
- Use code verbs precisely: “requires,” “grades,” “records,” “refuses,” “blocks search,” “discards the suffix,” “nudges,” or “reports.” Do not upgrade a nudge into a gate or a report into acceptance.
- Attach every scope qualifier to the result it limits: one transition, one active queue, recorded history, chosen observation projection, current provenance tuple, selected files, or repository-reported campaign.
- Prefer “supports,” “establishes,” or “licenses” only with the exact target and domain named.
- Do not add product judgment, redesign advice, celebratory framing, or a generic methodology-enforcement claim. Those branches do not change the commissioned comparison.
