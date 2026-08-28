## Source-first disposition

Inputs: `brief.md`, `reconstruction.md` (item numbers below are its numbered material items and its lettered support paragraphs), `kb/notes/COLLECTION.md`, `kb/types/note.md`, and the existing notes named per candidate. Not read: `original.md`, the live target, `kb/reports/`, any draft. Search for prior statements: `rg` over titles and descriptions in `kb/notes/`, `kb/reference/`, `kb/agentic-systems/`, `kb/sources/` for revision cost, reconstruction cost, sunk, prototype, binding, entrenchment, correspondence, epistemic status, grain, interpretation; openings of `semantic-work-can-be-relocated-but-not-eliminated.md`, `moving-the-interpretation-enforcement-boundary-requires-coverage.md`, `mixed-epistemic-status-must-be-preserved-below-the-document-level.md` checked for overlap. No existing note states the two-component standing claim, the separate-axis point, or the paired-comparison consequence.

Record format per candidate: **Claim** (one sentence) · **Relation** to the user-supplied target claim · **Basis** (reconstruction items; user direction and inference labelled) · **Existing** statement, if any · **Disposition** (exactly one) · **Target** path · **Boundary** (why the disposition preserves a citation and revision boundary).

### C1. Prototype standing is expected revision cost with two components

- **Claim:** A theory's prototype standing is its expected revision cost, made of external binding (consumers coupled to the current version, so a change propagates) and intrinsic reconstruction cost (investment discarded on revision), so internal proof or model dependencies and lost evidential investment count before any external adoption.
- **Relation:** central.
- **Basis:** binding — items 10(c)–(d), 6, 14 (Gödel) (support (i), strongest); reconstruction — item 10(d) "sunk work", 14 (selective revision, coevolution) (support (ii), medium); the "residual becomes mechanism" clause is user direction, entailed by admitting the second component. Consumer list (procedures, training, certification, validators, executables) and example list (proof development, safety case, trained model) are user direction; see the resolution on unsourced examples below.
- **Existing:** none. The pre-formal note defines the prototype by binding alone (10(c)) and lists sunk work and rollback cost as cost sources in a separate sentence (10(d)); no note names two components or makes standing a cost quantity.
- **Disposition:** `central contribution`.
- **Target:** `kb/notes/a-natural-language-theory-is-a-prototype-codified-or-rejected.md` (edit; relocate after promotion to `kb/notes/prototype-standing-is-revision-cost-binding-plus-lost-investment.md`).
- **Boundary:** one proposition citable as a premise ("since prototype standing is revision cost…"); C2–C8 and C13–C15 are its components, consequences, and bounds and are revised with it; every independent claim (C9–C12) lives elsewhere.

### C2. Form correlates weakly with reconstruction cost and determines neither component

- **Claim:** For natural-language versus symbolic theories, representational form determines neither binding nor reconstruction cost, and at most correlates weakly with the second because symbolic artifacts tend to carry construction investment (a proof development) that natural-language statements do not.
- **Relation:** component (a bound on what enters the two components).
- **Basis:** "determines neither" — items 10(d), 14 (Gödel: a natural-language prompt with a guaranteed wire), 6 (support (iii)); "weak correlation" — inference, no input measures it. Scope fixed to natural-language vs symbolic by the brief; items 4 and 14 (coevolution) tie distributed-parametric form to per-item non-addressability and retraining cost, so the bound does not extend to that form without a caveat (see C15).
- **Existing:** the "determines neither" half is stated in the pre-formal note's cost sentence ("Nor does the medium make rejection cheap; authority, downstream coupling, sunk work, and rollback cost do"), from the stage perspective, not as a claim about standing. Not adequate as a substitute, but it is the premise to cite inline (`since …`).
- **Disposition:** `support/example/scope only`.
- **Target:** the central note, thesis paragraph and `## Scope`; inline link to `kb/notes/unformalized-improvements-need-a-pre-formal-stage-in-the-loop.md`.
- **Boundary:** removing it leaves the central claim intact but unbounded; nobody would cite it without C1. Modality: "determines neither" is universal (refuted by a natural-language/symbolic pair with equal binding and equal discarded investment that differ in standing); the correlation is statistical and must state its refuter — prevalence evidence that, at equal binding, form is a reliable predictor of reconstruction cost. If the writer cannot state the refuter in one clause, drop the correlation and keep only "determines neither" (brief, terminology section).

### C3. Epistemic status is a separate axis

- **Claim:** Whether a theory is accepted or conjectural is a lifecycle status recorded by a decision, and it neither raises nor lowers revision cost by itself.
- **Relation:** scope (the definition's "not an epistemic status" clause).
- **Basis:** inference from items 5 (acceptance is a recorded decision with no cost content), 6 (adoption is not entrenchment), 7 ("adoption … does not establish that the choice is … cheap to reverse") (support (iv)). User direction for stating it as an axis.
- **Existing:** none states independence; `kb/notes/definitions/discovery-lifecycle.md` supplies the acceptance stage; `mixed-epistemic-status-must-be-preserved-below-the-document-level.md` is about warrant granularity in documents, not cost.
- **Disposition:** `support/example/scope only`.
- **Target:** the central note, definition paragraph; inline link to `kb/notes/definitions/discovery-lifecycle.md` at "accepted".
- **Boundary:** it is a negative bound on C1 (what standing is not) and the premise of C5; stated alone it is a definitional remark with nothing to cite.

### C4. Prototype standing defined as a lifecycle standing, with the engineering-gloss disclaimer

- **Claim:** "Prototype standing" names the lifecycle standing in which a theory is still cheap to revise or reject; "prototype" is an engineering gloss, not the collection-prototype sense (clone-once creation-time contract text) nor the exemplar sense.
- **Relation:** component (definiens of C1's subject term).
- **Basis:** item 10(c) (the narrower one-line definition), 12 (collection-prototype sense), 13 (exemplar/shorthand sense and the write-time rule that a gloss must carry visible scope). User direction (a).
- **Existing:** `unformalized-improvements-…` defines the prototype by binding alone; after the rebuild its definition is narrower than C1. `kb/reference/collection-prototypes.md` defines the other sense.
- **Disposition:** `support/example/scope only` (not a `definition`-type artifact: the brief fixes "prototype" as a gloss, not canonical vocabulary, and item 13 says a gloss stays a visibly approximate handle).
- **Target:** the central note, opening; links to `kb/reference/collection-prototypes.md` and `kb/notes/vocabulary-collisions-prevented-at-write-time-not-read-time.md` at first use.
- **Boundary:** the definition cannot be revised separately from C1 because C1 is the definition's content. Pending handoff (not a fold authorized here): the pre-formal note's one-line prototype definition needs a wording check against C1 (reconstruction Conflicts 1); it is a wording alignment, not a claim change.

### C5. Warrant rule — binding is the act not to perform before acceptance for the bound scope

- **Claim:** Since binding is a cost component, binding a consumer to a theory before the theory is accepted for that consumer's scope spends prototype standing that evidence has not yet licensed, so acceptance for the bound scope — not current fit or current form — is what licenses binding.
- **Relation:** consequence.
- **Basis:** item 6 (adopt on fit, entrench only on warrant), 7 ("harden a conjectured link only to the degree its evidence warrants"; "adoption supplies authority, not prudence"), 10(e), and "for the bound scope" from item 2 plus item 6's "for a stated scope" (support (v), medium; inference for the scope clause). User direction (b).
- **Existing:** `current-task-fit-alone-does-not-warrant-costly-entrenchment.md` states the rule for a KB's structural layer, with three warrants; `exact-implementation-does-not-validate-a-requirement.md` states the provisional-codification posture. Neither states it for theories or ties it to acceptance for a scope.
- **Disposition:** `support/example/scope only`.
- **Target:** the central note, one paragraph; inline links to `kb/notes/exact-implementation-does-not-validate-a-requirement.md` (executable success is not acceptance) and `kb/notes/current-task-fit-alone-does-not-warrant-costly-entrenchment.md`.
- **Boundary:** the rule is C1 applied to the act that raises the first component; it is derived, not independent. **Coordination-value exception (reconstruction Conflicts 3), resolved by scoping rather than restating:** the rule says what acceptance status and fit license; it does not say no other warrant exists. State in one clause that binding before acceptance can still be chosen for coordination value or forced by an enduring constraint, and that then it is knowingly spent standing, priced by `current-task-fit-…`. This keeps the user's rule intact, avoids importing the three-warrant taxonomy, and leaves the exception's threshold where that note leaves it (open).

### C6. Grain — standing is assessed at the grain consumers bind to

- **Claim:** Standing is assessed per part at the grain consumers bind to, so partial codification leaves a theory with mixed standing wherever its parts differ in binding or in discarded investment.
- **Relation:** consequence/scope.
- **Basis:** item 2 (warrant per part), 4 (localized forms revise one item at a time), 10(c) ("the part a formal consumer needs is codified … while the rest stays reopenable") (support (vi); "only where binding differs" is user direction).
- **Existing:** per-part warrant is in `theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md`; per-part binding is not stated anywhere.
- **Disposition:** `support/example/scope only`.
- **Target:** the central note, one short paragraph or Scope bullet; inline link to the theory-warrant note.
- **Boundary:** extends per-part warrant to per-part cost and has no content without C1. Consistency requirement for the skeleton: the brief's phrasing "only where binding differs" must be stated so it follows from the two-component axis — parts differ in standing where either component differs; in partial codification binding is the component that usually differs, because codified and uncodified parts share the same discarded investment unless the codified part carried its own construction (a proof development). Stating binding as the only source would contradict C1.

### C7. Cheap formalization lets symbolic artifacts be experiments inside the prototype loop

- **Claim:** A symbolic artifact can exist unbound, so where the cost of construction, proof generation, or checking was the bottleneck, cheaper formalization lets a formal model enter the prototype loop as an experiment with prototype standing — with the caveat that translation, construction, proof generation, checking, and world-fit evidence are separate costs that fall independently.
- **Relation:** consequence (application of C1 and C2 to codified artifacts).
- **Basis:** item 10(f) (separable costs; "formal prototypes enter earlier"; conditional on language coverage), 10(d) ("a low-authority formal sketch can stay disposable"), 10 second paragraph (competing formal models preserve alternatives) (support (vii), strong). User direction (d): the paragraph must survive.
- **Existing:** `unformalized-improvements-…` § "Cheaper formalization moves revision into the language it already has" states the cost bundle and the conditional from the stage perspective. It is adequate for the cost-bundle list; it does not state the standing consequence (an unbound symbolic artifact has prototype standing).
- **Disposition:** `support/example/scope only`.
- **Target:** the central note, one paragraph; cite the pre-formal note inline for the separable-cost list instead of restating it, keep the conditional ("only where formalization cost was the bottleneck").
- **Boundary:** the standing consequence is C1's; the stage claim and the cost list stay owned by the pre-formal note, so revising either note does not force the other. Citer finding (reconstruction DECISION on the defense portfolio, resolved as handoff): `the-bitter-lesson-defense-portfolio-…` cites the pre-formal note, not the target, and its table row describes the stage claim; no target edit follows, and adding a portfolio link to the rebuilt note would be a portfolio edit under that note's role-classification rule — record as a pending handoff, not a fold in this run.

### C8. Testable consequence

- **Claim:** Two theories of the same form and the same epistemic status differ in prototype standing when their binding or reconstruction cost differs, and two theories of different form do not differ when those are equal.
- **Relation:** consequence (C1's refuter, stated as a prediction).
- **Basis:** user direction (e); deduction from C1 (support (viii)). No instantiating case in any input (EVIDENCE NEEDED stands: the note may state the prediction and its refuter, not cite an observation; the pre-formal note's prose-versus-sketch contrast is illustrative only).
- **Existing:** none.
- **Disposition:** `support/example/scope only`.
- **Target:** the central note, a short closing paragraph or a named "What would refute this" sentence.
- **Boundary:** it is the operational form of C1's universal modality and has no standing apart from C1.

### C9. Correspondence-boundary branch — "Formal checking moves, but does not erase, interpretation"

- **Claim:** Codification relocates interpretation to the model-to-world correspondence boundary rather than removing it: a proof warrants entailment inside the formal model, not correspondence to the claim, so world failures reopen the translation layer (scheduler example; Eigenius's separate correspondence check; DiscoverPhysics's accuracy/explanation split), except for claims whose objective is constitutively formal and so have no correspondence gap.
- **Relation:** separable (brief, must-move-out 1).
- **Basis:** item 8 (formal-systems note: proof warrants entailment from axioms, translation unchecked); 10(g) (the pre-formal note already carries the scheduler example, Eigenius, and DiscoverPhysics under "World failures identify which layer must reopen"); 15 (Eigenius: code-inspection at a pinned commit, correspondence conditional on optional anchors; DiscoverPhysics: abstract-only ingest, supports only "accuracy and explanation can come apart"). The purely-formal exception's content is not visible to this pass (it lives in `original.md`); its shape is inferred from the working title.
- **Existing:** adequate for the general claim. `kb/notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md` § "The formalization boundary" states "The formal routes move judgment upstream rather than abolishing it. A proof shows a theorem follows from axioms, not that the variables, domain, or utility function represent the original claim" and closes with "the edge of that domain is fixed by a translation they do not check"; `semantic-work-can-be-relocated-but-not-eliminated.md` states the relocation framing ("Codification is the limiting case: resolve a meaning-dependent decision once and freeze the result"); `unformalized-improvements-…` § "World failures identify which layer must reopen" holds all three examples and links the formal-systems note as `grounds` for exactly this point; `kb/agentic-systems/eigenius.md` already links the formal-systems note for separating proof validity from translation fidelity. A new note under the working title would be a third home restating two library notes and would owe its own grounding pass for both external cases.
- **Disposition:** `fold into existing`.
- **Target:** `kb/notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md`, § "The formalization boundary". Proposed delta (small): (i) one sentence naming the relocation explicitly — codification moves interpretation to the correspondence boundary; it does not remove it — with an inline link to `semantic-work-can-be-relocated-but-not-eliminated.md`; (ii) one sentence stating the purely-formal exception as the bound: a claim whose objective is itself the formal domain has no translation edge, so proof warrants it outright; (iii) footer `evidenced-by` edges to `kb/agentic-systems/eigenius.md` (proof checking with a separate, conditional correspondence check; code inspection at a pinned commit) and `kb/sources/discoverphysics-benchmarking-llms-out-of-the-box-scientific.ingest.md` (accuracy and explanation come apart; abstract-only, scoring method unknown — bounds, does not explain). Do not copy the scheduler example; it stays in the pre-formal note, which the fold may cite. Grounding: Eigenius is a code-grounded review artifact and DiscoverPhysics's use stays within its retained verbatim quotes, so no new `(snapshot required)` marker is needed for the delta as stated.
- **Boundary:** the general claim keeps one home, the examples keep one home, and the central note cites the formal-systems note by title where it needs the entailment/correspondence distinction (C7's "unbound" and C5's "executable success is not acceptance") instead of carrying the branch. Execution is a pending handoff: the brief authorizes either home but reserves execution to the user, and the skill's fold gate requires the user to see the delta before an artifact other than the target is changed. Reopen condition: if phase 2 shows the purely-formal exception asserts more than "a constitutively formal objective has no correspondence gap", that surplus is a new claim and the disposition returns to `separate new artifact`.

### C10. Codification and acceptance are independent

- **Claim:** Codification is a change of form and consumer kind — natural language into a symbolic artifact with assigned consequences — and says nothing about whether the codified content is deployed, bound, or accepted.
- **Relation:** separable (brief, must-move-out 2); used by C1 as a premise.
- **Basis:** item 3 (definition is purely about form and consumer kind; separation from adoption holds by silence, reconstruction Conflicts 2). User direction.
- **Existing:** `kb/notes/definitions/codification.md` — adequate, provided the citing sentence says the definition is about form and consumer kind, not deployment ("committed to a symbolic consumer" means consequences assigned by a formal consumer, not consumers coupled to the artifact).
- **Disposition:** `cite existing`.
- **Target:** `kb/notes/definitions/codification.md`; one sentence in the central note with an inline or `defined-in` link.
- **Boundary:** the definition owns the form crossing; the central note owns only the consequence that crossing form does not by itself change either cost component (C2), so a change to the definition's scope is reviewed there.

### C11. Prevalence hypothesis — codification pressure vs invocation frequency, misreading cost, volatility

- **Claim:** Pressure to codify a theory rises with how often it is invoked and with the cost of misreading it, and falls with its volatility.
- **Relation:** separable (brief, must-move-out 3); it concerns what drives binding, not what standing is.
- **Basis:** none in the inputs; user direction to demote or drop.
- **Existing:** none; `codify-versus-llm-decision-heuristics.md` collects four codify-vs-LLM lenses (spec completeness, oracle strength, interpretation space, pattern stability) and is the nearest home if it is ever revived.
- **Disposition:** `omit/retain in workshop`.
- **Target:** none; retained here as the record. If the user prefers the brief's other option, it becomes one `## Open Questions` bullet in the central note phrased as a question ("what sets the pressure to bind — invocation frequency, misreading cost, volatility?"), not as a tendency, since a statistical claim without a refuter is vacuous under ADR 066.
- **Boundary:** keeping it out of the central note stops a second topic (drivers of codification) from being imported by every citer of C1.

### C12. Entrenchment mechanism

- **Claim:** Binding raises replacement cost because dependants and migration cost accumulate with each consumer coupled to the current version; adoption by more consumers raises that cost without demonstrating the theory transfers.
- **Relation:** component (mechanism of the first component).
- **Basis:** item 6 (support (i)).
- **Existing:** `kb/notes/current-task-fit-alone-does-not-warrant-costly-entrenchment.md` — adequate (stated for the structural layer; applying it to theories is a transfer the central note makes explicitly).
- **Disposition:** `cite existing`.
- **Target:** that note; footer edge labelled `mechanism` ("how external binding turns into revision cost"), plus the inline use in C5.
- **Boundary:** the mechanism and its three warrants are revised there; the central note imports only "coupled consumers make replacement expensive".

### C13. A faithful rationale lowers the reconstruction component

- **Claim:** A theory retained with its rationale can be repaired part by part, while one without it must be deleted and re-derived, so a faithful rationale lowers the reconstruction component of revision cost.
- **Relation:** component (what modulates the second component).
- **Basis:** item 14 (selective revision: "With no rationale, a counterexample forces wholesale replacement — expensive"); inference that this is a reconstruction-cost effect (the note frames repair vs replacement, not cost).
- **Existing:** `kb/notes/selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md` — adequate for the repair-vs-replacement claim.
- **Disposition:** `cite existing`.
- **Target:** that note; footer edge kept (brief), label `grounds` ("why a retained rationale lowers what revision discards").
- **Boundary:** the repair claim stays there; the central note adds only the one-clause reading as a cost effect.

### C14. Proof-gated acceptance with a guaranteed wire is the maximal-binding corner

- **Claim:** A harness-loaded natural-language instruction has guaranteed consumption, so an accepted change becomes operative immediately — a natural-language artifact with maximal binding, which shows form does not set the first component.
- **Relation:** example (for C2's "determines neither").
- **Basis:** item 14 (Gödel note, "the wire is guaranteed"); transfer from prompt self-editing to theories is inference.
- **Existing:** `kb/notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md` — adequate.
- **Disposition:** `cite existing`.
- **Target:** that note; footer edge kept (brief), label `contrasts` (proof-gated acceptance couples authority and retention; here acceptance and binding are separate acts).
- **Boundary:** one clause in the central note; the case detail stays in the Gödel note.

### C15. Distributed-parametric form ties reconstruction cost to retraining

- **Claim:** In distributed-parametric form a revision is a retraining, not a per-item edit, so for that form the reconstruction component is set largely by the form itself — which is why C2 is bounded to natural-language versus symbolic.
- **Relation:** scope (bound on C2).
- **Basis:** item 4 ("weights are not [revisable one item at a time]"), item 14 (coevolution: heavy training infrastructure, days-to-weeks cycles) (reconstruction Conflicts 4; scope fixed by the brief).
- **Existing:** `kb/notes/definitions/representational-form.md` (per-item addressability) and `kb/notes/treat-continual-learning-as-representational-form-coevolution.md` (update cost) — adequate.
- **Disposition:** `support/example/scope only`.
- **Target:** the central note, one `## Scope` bullet; `defined-in` link to `representational-form.md` at the first use of "distributed-parametric" (brief, local copy findings), footer edge to the coevolution note kept (brief), label `grounds`.
- **Boundary:** a bound on C2 stated where it can be narrowed by a rescoping edit; the parametric cost facts stay owned by the two cited notes.

### Cited-as-premise items with no independent claim in this note

- "Theory" in the inspectable-parts sense — `cite existing` inline at first use, `kb/notes/theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md` (item 1). Not a separate candidate: it is the quantifier domain of C1.
- Superseded choices vs refuted beliefs — footer edge kept (brief), `kb/notes/superseded-choices-are-retained-superseded-beliefs-are-not.md`, label `contrasts` (what revision retains after standing is spent, versus what it costs). Support only.
- `kb/notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md` — inline at C7 if the writer needs "every codification is a bet"; otherwise omit. Support only.
- `kb/notes/the-bitter-lesson-defense-portfolio-has-one-load-bearing-member.md` — footer edge kept (brief), label `see-also` is not authorized for notes; use `extends` only if the portfolio's role classification is what the reader wants next, otherwise `contrasts` (it defends a stage, this note prices a standing). Writer's call; no claim content.

### Resolutions

- **DEFINE expected revision cost.** State it as the total of the two components in kind — what a revision propagates to (binding) plus what it discards (reconstruction) — assessed in advance for the scope the revision would touch, with no formula and no weights. "Expected" keeps its ordinary sense (anticipated at assessment time), and the note should say so; a probability-weighted reading would owe a probability model no input supplies. Rationale: the two bills are paid to different parties, so a maximum would hide one; a sum in kind is the weakest combination that still lets the C8 comparison run.
- **Claim modality of C1 (ADR 066).** Universal over theories in the inspectable-parts sense; declare it in the thesis. The stipulative half ("standing is expected revision cost") is a definition and is not what is refuted; the substantive universal is that the two components are exhaustive and separable and that form and status enter only through them. Refuted by one theory whose revision cost is materially set by something reducible to neither component (authority and rollback cost, named in item 10(d), must be shown to reduce to binding — rollback propagates to consumers, authority is consumers obliged to follow — or they are the counterexample), or by a pair equal in both components that differs in standing (C8). Not ideal-type: no exception is conceded, and the claim has no adequacy record to carry. The C2 correlation alone is statistical, with its refuter stated in C2.
- **Unsourced illustrative examples (safety case, certification, training).** Keep as illustrative examples that assert nothing about a named system: phrase them generically ("an approved safety case", "a certified procedure", "a trained model"), introduce them with "for instance", and do not list them as evidence. The trained model is supported by item 14 (coevolution); the other two are category illustrations the argument does not rest on (theory-independence constraint holds without them). Omit any that the writer cannot phrase without asserting a fact about a real regime.
- **Form scope.** Fixed by the brief to natural-language versus symbolic; distributed-parametric handled as C15.
- **Coordination-value exception.** Resolved under C5 by scoping.
- **Grain wording.** Resolved under C6 as a consistency requirement.
- **DECISION NEEDED:** none blocking this run. Two items need the user at handoff time, not now: authorizing the C9 fold at `formal-systems-assess-…` (delta recorded above), and whether the defense-portfolio note should gain a link to the rebuilt note (C7; a portfolio edit).

### Summary

The one central contribution is C1: a theory's prototype standing is its expected revision cost, the total in kind of external binding and intrinsic reconstruction cost, universal over theories in the inspectable-parts sense, with form (natural-language vs symbolic) determining neither component and epistemic status a separate axis; C2–C8 and C13–C15 are its bounds, consequences, mechanism citations, and examples and stay in the note as support. Dispositions other than `support/example/scope only`: `central contribution` — C1 at the target path (relocated after promotion); `fold into existing` — C9, the correspondence-boundary branch, into `kb/notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md` § "The formalization boundary" (one relocation sentence, the purely-formal exception as bound, `evidenced-by` edges to Eigenius and DiscoverPhysics; execution is a handoff pending user authorization; reopens to `separate new artifact` only if phase 2 shows the exception asserts more than a constitutively formal objective having no correspondence gap); `cite existing` — C10 at `kb/notes/definitions/codification.md` (one sentence), C12 at `current-task-fit-alone-does-not-warrant-costly-entrenchment.md` (`mechanism`), C13 at `selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md` (`grounds`), C14 at `goedel-machines-are-a-proof-governed-case-of-self-modification.md` (`contrasts`); `omit/retain in workshop` — C11, the prevalence hypothesis. Pending handoffs recorded: the C9 fold, a wording check of the pre-formal note's one-line prototype definition, and the defense-portfolio citer question. No `synthesis` trait: every component is either C1's own content or an already-citable premise.

## Incumbent reconciliation

Read: `original.md` (post-review text, SHA recorded in `README.md`). The incumbent is inventoried as a list of commitments, not as evidence: where a retained commitment needs support the source-first pass did not cite, the basis field says so. Items are numbered I1… and walked in document order; "merged into Cn" means the commitment is already disposed by that phase-1 record and the incumbent adds no separate claim. Phase-1 records are not rewritten; where phase 2 revises a phase-1 suggestion (two footer labels), the revision is stated here.

### Headline delta

The incumbent's thesis is single-component: standing is cheap revision "because little operational machinery depends on their current version", and its title makes form the subject ("Representational form does not determine whether a theory is a prototype"). The rebuild makes revision cost the subject and adds the reconstruction component (C1). Every incumbent sentence that says "binding", "operational coupling", or "rollback cost" decides standing is therefore merged into C1 as its first component, and every "only while coupling remains low" qualifier becomes "only while both components stay low". No incumbent sentence mentions discarded investment, sunk work, proof developments, or trained models; the second component enters on user direction alone (brief, target claim), as phase 1 recorded.

### Frontmatter and title

- **I0a. Title** "Representational form does not determine whether a theory is a prototype" — merged into C1/C2; replaced by the user's working title (brief). The incumbent title states C2's "determines neither" half as the whole claim.
- **I0b. Description** "Why prototype standing tracks operational binding rather than representational form: prose leaves consequences interpretive, symbols give encoded choices formal semantics, and either form can remain exploratory or become costly to revise" — must change: it is binding-only and form-centred, and it summarizes rather than discriminates. Proposed: "A theory's prototype standing is its expected revision cost — external binding plus the investment a revision discards — so natural-language versus symbolic form determines neither component and acceptance status is a separate axis". Writer may tighten.
- **I0c. Traits** `[title-as-claim]` — keep; the brief names only this trait. `has-external-sources` stays absent (the only external cases leave with C9). No `synthesis`.
- **I0d. Tags** `[learning-theory, constraining, self-improving-systems]` — keep; no reason to change surfaced.

### Opening thesis (l. 10)

- **I1.** Theory in the inspectable-parts sense, linked — merged into the cited-as-premise list (item 1).
- **I2.** Standing = cheap revision because little operational machinery depends on the current version — merged into C1 (first component only; see headline delta).
- **I3.** "This is a lifecycle standing, not an epistemic status" — merged into C3/C4.
- **I4.** "An accepted theory can remain a prototype, while a conjecture can become entrenched before it earns acceptance" — merged into C3 as its two-corner illustration (basis items 5, 6, 7; support only). Under C1 the second corner should read "entrenched or heavily invested before it earns acceptance".

### Gloss paragraph (l. 12)

- **I5.** Engineering gloss; "a build kept cheap to revise while its commitments are still being tested"; not the collection-prototype sense; not an exemplar — merged into C4 (basis items 12, 13).
- **I6.** "A rejected theory is no longer a prototype because its claim has been retracted."
  - Claim: rejection ends standing because there is no surviving claim to revise; standing is a property of surviving theories only.
  - Relation: scope. Basis: item 5 (rejection is the lifecycle's failing branch; revision returns to conjecture) and item 14 (superseded-choices: a refuted belief "loses standing"). Existing: `superseded-choices-are-retained-superseded-beliefs-are-not.md` states the refuted-belief half.
  - Disposition: `support/example/scope only`. Target: one `## Scope` bullet in the central note, merged with I29 below; footer edge to the superseded-choices note (label below, I36).
  - Boundary: a bound on C1's domain; nothing to cite alone.
- **I7.** "A surviving theory can retain prototype standing in either natural-language or symbolic form" — merged into C2.

### Form paragraph (l. 14)

- **I8.** Representational-form definition and link; "natural language leaves consequences to interpretation; codification crosses into a symbolic artifact whose formal consumer assigns consequences" — merged into C10 (cite `definitions/codification.md`) and C15 (`defined-in` link to `definitions/representational-form.md`).
- **I9.** Codification "increases semantic determinacy [but] does not by itself establish adoption, downstream dependency, or rollback cost" — merged into C10 (the one-sentence cite) and C2.
- **I10.** "An authoritative prose theory can bind training, audits, policies, and decisions. A scratch formal model can remain disposable." — merged into C2 as its paired illustration (basis item 10(b), (d): prose that binds through a procedure, audit, or contract; a low-authority formal sketch stays disposable). "Training" is unsourced; treated under the illustrative-examples resolution.

### "Form changes interpretation; binding changes revision cost" (ll. 18–22)

- **I11.** Natural language allows direct criticism before operational details are fixed; an agent can inspect, derive a test, and revise a premise without translating; the cost is interpretation at each use, since readings can assign different consequences.
  - Claim: form changes which checks are available and what each use costs in interpretation; it does not change what a revision costs.
  - Relation: scope (what form *does* determine, so the reader does not read C2 as "form is irrelevant"). Basis: item 2 ("Representational form … changes which checks are available"), item 4 (natural-language consequences come from interpretation), item 10(c) (a critic can challenge a premise or derive a test "without a build step"). Existing: stated across `theory-warrant-…`, `definitions/representational-form.md`, and `unformalized-improvements-…`; adequate.
  - Disposition: `support/example/scope only`. Target: one clause in C2's paragraph, citing the theory-warrant note inline.
  - Boundary: a contrast clause that keeps C2 from overreaching; owned by the cited notes.
- **I12.** Symbolic form fixes how a consumer treats the encoded choices but can leave a range open through parameters, nondeterminism, or quantification; codification gives the range formal semantics without selecting one value.
  - Claim: a symbolic artifact can encode alternatives, so codification need not resolve every choice.
  - Relation: component of C7 (why a formal model can still be a prototype). Basis: item 10 second paragraph ("Partial specifications and competing formal models also preserve alternatives"), item 4. The parameter/nondeterminism/quantification enumeration has no reconstruction support beyond item 4's generic "consequences assigned by a defined consumer"; it is mechanism detail the governing question does not need.
  - Disposition: `support/example/scope only` — merged into C7, citing the pre-formal note for "partial specifications and competing formal models preserve alternatives"; the enumeration is dropped (no `EVIDENCE NEEDED`: omission is allowed because neither the governing question nor the brief requires it).
- **I13.** "Neither interpretive openness nor formal semantic determinacy determines how far a revision propagates. Revision remains local only while consumers are loosely coupled" — merged into C1 (first component) and C2. The safety-case example (procedures, training, certification) — illustrative-examples resolution. "A formal model used only to explore a candidate can be discarded without migration" — merged into C7 (with the C1 qualifier: and without much discarded investment). "Entrenchment begins when replacement stops being cheap, regardless of medium" — merged into C12 (`mechanism`).

### "When codification becomes attractive" (ll. 26–30)

- **I14.** Prevalence claim with its stated refuter ("a finding that working systems, under otherwise similar conditions, preferentially formalize rare, volatile, cheap-to-misread theories over frequent, stable, expensive-to-misread ones would count against it") — merged into C11, `omit/retain in workshop`. Record for revival: the incumbent did state a refuter, so the ADR 066 statistical guard was met; what is missing is any evidence (reconstruction: none in the inputs), and the user directed demotion or removal. The refuter text above is the retained record.
- **I15.** Formalization cost is a bundle — translating, constructing, generating a proof, checking — that varies independently; cheaper proof checking does not make translation of unsettled concepts cheap; a comparison must identify which cost changed and which consumer benefits — merged into C7's cost-bundle caveat (basis item 10(f), which also lists world-fit evidence; cite rather than restate). The clause "which consumer benefits" has no reconstruction support and is dropped (omission allowed; not required).
- **I16.** Codification often accompanies stronger commitment because formally assigned consequences make an artifact easier for validators, executables, and other components to consume; adding consumers raises rollback cost; the causal step is the added binding, not symbolic form.
  - Claim: codification makes consumption by formal consumers *available*; binding happens only when such a consumer is actually coupled, so the standing change is caused by the added consumer, not by the form.
  - Relation: component (mechanism of C2's "determines neither" — why form gets mistaken for standing). Basis: item 3 (codification = consequences assigned by a formal consumer), item 10(e) (codifying before concepts settle raises replacement cost toward entrenchment), item 6 (more consumers raise migration cost). Existing: none states the availability/coupling distinction for theories.
  - Disposition: `support/example/scope only`. Target: C2's paragraph, stated as availability (universal-safe) rather than as the incumbent's "often accompanies" tendency, which would need a refuter and has no evidence; this does not expand the target claim, which already says form determines neither component and correlates only with the second.
  - Boundary: explains the confusion C1 removes; no content without C1.
- **I17.** "Prematurely adopting either prose or a symbolic artifact as operative makes being wrong expensive" — merged into C5.

### "Codification and acceptance are independent" (ll. 34–38)

- **I18.** Lifecycle link; "codification changes representation; it is not itself an epistemic decision"; a theory can be formalized before acceptance so rival models expose different consequences; it can be accepted for a use needing no formal consumer and stay in prose — merged into C10 (one sentence plus link) and C3; the rival-models clause into C7 (basis item 10 second paragraph).
- **I19.** Normative condition: a codified artifact should become operative authority only after the theory has been accepted for the scope the artifact commits; a warrant rule, not part of codification's definition; executable success cannot substitute for acceptance (exact-implementation link) — merged into C5, reframed per brief (b): the act is binding in any form, not codification. The exact-implementation inline link survives.
- **I20.** Grain: assessed at the grain consumers bind to; a premise that becomes an operative checked invariant can lose standing while the remainder retains it; mixed standing "only when operational binding differs across components" — merged into C6, with the phase-1 consistency requirement (either component; binding is the usual one). The checked-invariant example is kept as C6's illustration (basis item 10(c)).

### "Formal checking moves, but does not erase, interpretation" (ll. 42–50)

- **I21.** Verification-oriented codification can produce a formal model and obligations (theorem, invariant, type property, model-checking condition, test suite); other codifications produce only an executable rule; obligations are not constitutive of the form change.
  - Claim: codification does not require verification obligations; obligations are one product of some codifications.
  - Relation: separable (belongs with the correspondence branch or with the codification definition, not with standing). Basis: item 3 — the definition's consumer list (validators, tests, parsers, route tables, grammars) already contains codifications without obligations, so the point is implied. Existing: `definitions/codification.md` (Scope list) and `formal-systems-…` § "The proof route" (the obligation kinds).
  - Disposition: `omit/retain in workshop`. Reason: adequately implied by the codification definition; the governing question does not need it; the C9 fold may use "where obligations exist" as a framing clause without asserting it as a claim.
- **I22.** Proof warrants entailment from the formal assumptions, not correspondence; for externally interpreted theories codification relocates interpretation to the translation and correspondence boundary rather than eliminating it — merged into C9 (this is the sentence the fold's delta (i) carries).
- **I23.** Scheduler example — merged into C9; not copied (already at the pre-formal note, item 10(g)).
- **I24.** Two repair paths (reopen the concepts in prose and recodify; revise the symbolic model directly where concepts are already precise) and the return-path sentence: "Returning a theory to prose is one theory-level extension of the codify-and-relax trajectory, but it is neither the only meaning of relaxing nor a required response to failure."
  - Claim: return to prose is one relaxing move among others and is not required by a world failure.
  - Relation: separable (repair-path selection, not standing). Basis: item 10(g) — the pre-formal note's "Which layer reopens depends on the representation already in hand… If the missing dependency is precise, the symbolic model can be extended directly", which states the direct-symbolic path and therefore implies "not required"; item 9 (the trajectory runs both directions). Existing: adequate at `unformalized-improvements-…` § "World failures identify which layer must reopen".
  - Disposition: `omit/retain in workshop` — not folded with C9, because the fold target (`formal-systems-…`) does not discuss relaxing and the pre-formal note already holds the layer-reopening account. The inline codify-and-relax link that carried this sentence drops with it unless C7 uses that note (phase-1 cited-as-premise list).
- **I25.** Eigenius and DiscoverPhysics paragraph; "In both cases, the representations remain separate objects to assess" — merged into C9 (fold delta (iii)). One detail check: the incumbent's "against an allowlisted axiom set" is not in reconstruction item 15 (which records checking of supplied proof terms and conditional correspondence anchors). The fold delta should not carry that detail; if the executor wants it, `EVIDENCE NEEDED` from `kb/agentic-systems/eigenius.md` before use. Everything else in the paragraph is within item 15.
- **I26. Purely-formal exception (l. 50) — C9 reopen check.** Text: "When natural language is only an informal presentation of an authoritative formal definition, no model-to-world observational claim need remain. The correspondence argument applies to empirical and otherwise externally interpreted theories, not to every formalization." This asserts exactly the conceded bound — a theory whose authoritative object is the formal definition has no correspondence gap — plus a criterion for recognizing the case (which representation is authoritative: the natural language is the gloss, the formal definition the object) and the scope statement that matches the pre-formal note's "externally interpreted theories". It asserts nothing beyond "a constitutively formal objective has no correspondence gap". **C9 stays `fold into existing`**; the fold's delta (ii) should carry the authority criterion in one sentence, since it is what makes the bound applicable. Basis: inference (analytic: no translation edge exists where the formal object is the target); no input states it and none is needed for a conceded bound.

### "Cheap formalization changes the prototype loop" (ll. 54–58)

- **I27.** Cheaper construction, proof generation, or checking lets more candidates be expressed symbolically before adoption; formal models become experiments within the prototype phase; a theory may move repeatedly between prose and symbols or be revised entirely within symbolic form while coupling stays low — merged into C7 (basis items 10(f), 9).
- **I28.** For externally interpreted theories, cheaper in-model checking can make translation and world correspondence a larger share of the remaining uncertainty; it does not show translation became cheaper, that uncertainty must concentrate there, or that prose is the only revisable medium; cheap formalization removes one reason to defer symbolic experiments, not the lifecycle need for cheap rejection.
  - Claim: cheaper checking leaves the translation and world-fit costs where they were.
  - Relation: caveat of C7. Basis: item 10(f) ("For a concept outside every admitted language the bottleneck is elsewhere: deciding what the premise commits to, and obtaining evidence that the model fits the world"; "defeats the cost argument for natural language without removing the stage"). The "larger share" framing is a tendency with no evidence; the entailment "does not lower those costs" is what item 10(f) supports. "Prose is not the only medium" is already at the pre-formal note ("Natural language is not the only prototype surface").
  - Disposition: `support/example/scope only` — merged into C7's cost-bundle caveat as the entailment, not the share claim; the "not the only medium" clause is omitted as redundant with the cited note.
- **I29.** Conditional mechanism, not a prevalence trend; predicts change only where formalization cost was the bottleneck; no prediction for theories infeasible to formalize, not formalizable, or whose consumers gain nothing from assigned consequences — merged into C7's conditional (brief (d)); the three exclusions are already stated by the pre-formal note ("Many theories never leave: no formal consumer needs them, formalizing them is infeasible in practice, or their content may not be formalizable at all") and are cited, not restated.

### Scope bullets (ll. 62–67)

- **I30.** Theory sense; procedures, records, and state descriptions have different retirement conditions; a procedure is superseded rather than refuted — merged into the cited-as-premise list (theory sense, item 1) and the superseded-choices footer edge (item 14: choices are superseded and retained, beliefs refuted and rewritten). Keep as one Scope bullet; support only.
- **I31.** "Cheap and local are relative to named consumers and dependencies. Where neither prose nor a symbolic artifact has consumers, both can be cheap to discard."
  - Claim: binding is relative to named consumers; with no consumers standing is set by the reconstruction component alone.
  - Relation: scope of C1/C2. Basis: item 6 (entrenchment is about dependants), item 10(d). The incumbent's "both can be cheap to discard" is true under C1 only with the added qualifier "and little investment to discard" — the incumbent's binding-only version is superseded by user direction.
  - Disposition: `support/example/scope only`. Target: C2's paragraph or a Scope bullet, corrected for two components.
- **I32.** Grain scope bullet — merged into C6 (duplicate of I20).
- **I33.** "Rejection retracts the claim. Revision and suspension preserve a surviving claim's prototype standing only while its operational coupling remains low." — merged with I6 into one Scope bullet; "only while its operational coupling remains low" becomes "only while both components stay low" (basis item 5: revision returns to conjecture).
- **I34.** Model-to-world boundary applies to externally interpreted theories; purely formal theories terminate the chain in an authoritative formal definition — merged into C9 (moves with the fold; duplicate of I26).
- **I35.** Covers natural-language and symbolic forms; does not decide whether absorption into distributed-parametric form is another form change or a different lifecycle event — merged into C15, which now states positively that parametric form ties the reconstruction component to retraining and is outside C2. The undecided sub-question (form change vs lifecycle event) is dropped: the brief fixes the scope and the question is not needed to bound C2 (omission allowed).

### Open Questions (ll. 71–74)

- **I36.** "Which observable dependency and rollback costs distinguish a prototype from an adopted or entrenched theory?" — keep, reworded to both components: which observable costs measure external binding and reconstruction cost, so that C8's comparison can be run (reconstruction: no input measures either; EVIDENCE NEEDED on C8 is thereby recorded as the open question, not hidden). `support/example/scope only`; target: central note `## Open Questions`.
- **I37.** "How should a system inventory prose authorities whose operational coupling is real but not machine-readable?" — keep. Basis: item 10(b) (prose binds through procedure, audit, contract), item 14 Gödel (a harness-loaded prompt's wire is guaranteed and visible; other prose binding is not) — the question is the inference that natural-language binding is often not machine-enumerable. `support/example/scope only`; target: `## Open Questions`.
- **I38.** "When consumers bind to partially codified theories at different grains, which grain should a review or acceptance decision target?" — keep as C6's open question. `support/example/scope only`.
- **I39.** "Can theories that are not yet understood be distinguished operationally from theories that cannot be formalized?" — `omit/retain in workshop`: it duplicates the pre-formal note's second open question ("Can a loop tell, from inside, a concept outside its admitted language from one the language contains but the loop has not yet selected, or from one too costly to formalize?") and is a stage question, not a standing question.

### Footer edges (ll. 80–84) and inline links

Survival per the brief's keep list; labels from the `kb/notes/COLLECTION.md` table.

- **superseded-choices-…** — incumbent `extends`: "explains what the rejection exit implies for retaining or removing the artifact". Survives. `extends` still fits the one-axis claim: the reader at I6/I33 (rejection ends standing) wants the argument carried on to what happens to the artifact. **Revises phase 1**, which suggested `contrasts`; use `extends` with the incumbent's context phrase.
- **selective-revision-…** — incumbent `contrasts`: "cheap editing does not guarantee that a revision targets the premise that failed". Survives. Under the rebuilt claim C13 cites this note as a premise (a faithful rationale lowers what revision discards), so the label becomes `grounds` when C13 is used inline, as phase 1 recorded; the incumbent's contrast (cheap revision is not correct revision) remains true and can ride in the context phrase. If the writer does not use C13, `contrasts` still fits.
- **treat-continual-learning-…** — incumbent `extends`: "places this two-form theory path inside a three-form learning frame". Survives. Phase 1 proposed `grounds` because C15 uses its update-cost claim as a premise; both fit — use `grounds` if C15's Scope bullet leans on the retraining-cost fact, otherwise keep `extends`. Not a claim change either way.
- **the-bitter-lesson-defense-portfolio-…** — incumbent `extends`: "locates cheap formalization as an objection to permanent form, not to a prototype function". Survives (brief; C7's paragraph is what it develops). `extends` still fits the one-axis claim: the reader of C7 who wants the objection's role in the form debate goes there. **Settles phase 1's "writer's call"**: use `extends`, context "classifies the cheap-formalization objection as an objection to permanent form, not to a prototype stage". Reminder: the portfolio does not link back; handoff, not target edit (C7).
- **goedel-machines-…** — incumbent `contrasts`: "a fixed proof gate excludes unformalized candidates without making every formal candidate operative". Survives; keep `contrasts` with the context updated to C14's use (proof-gated acceptance couples authority and retention; here acceptance and binding are separate acts, and the guaranteed wire is the maximal-binding natural-language corner). `evidenced-by` would also be authorized; `exemplifies` would not (direction is instance→general, and this note is the general).
- **current-task-fit-…** — add, `mechanism` (C12); the incumbent linked it inline at I13 only.
- Inline links that survive: `theory-warrant-…` (I1), `definitions/representational-form.md` (`defined-in` at first "distributed-parametric", C15), `definitions/codification.md` (C10), `definitions/discovery-lifecycle.md` (C3), `exact-implementation-…` (C5), `formal-systems-…` (where C5/C7 need the entailment/correspondence distinction — no longer as the host of a branch). Inline links that leave with their sentences: `codification-and-relaxing-…` (I24; optional at C7), `../agentic-systems/eigenius.md` and `../sources/discoverphysics-…` (C9 fold). `kb/reference/collection-prototypes.md` and `vocabulary-collisions-…` are added at C4 (brief, local copy findings).

### Confirmation

- Exactly one current central contribution: **C1** (prototype standing is expected revision cost, the total in kind of external binding and intrinsic reconstruction cost; universal over theories in the inspectable-parts sense). The incumbent's binding-only thesis and form-centred title are merged into it and superseded on user direction.
- Non-support dispositions, complete list: `central contribution` — C1. `fold into existing` — C9 (confirmed after the I26 check; delta unchanged, plus the I25 caution on the "allowlisted axiom set" detail). `cite existing` — C10 (`definitions/codification.md`), C12 (`current-task-fit-…`, `mechanism`), C13 (`selective-revision-…`, `grounds`), C14 (`goedel-machines-…`, `contrasts`). `omit/retain in workshop` — C11/I14 (prevalence hypothesis, refuter text retained above), I21 (obligations not constitutive of codification), I24 (return path / relaxing not required), I39 (understood-vs-unformalizable open question). Everything else in the incumbent is merged into C1–C15 or the cited-as-premise list as support, example, or scope.
- `EVIDENCE NEEDED` markers: none blocking. Two are recorded as bounded conditions — C8 has no instantiating case (carried as open question I36), and I25's "allowlisted axiom set" detail must not enter the C9 fold without a check of `kb/agentic-systems/eigenius.md`.
- `DECISION NEEDED`: none blocking. Unchanged from phase 1: user authorization is needed at handoff time to execute the C9 fold and to decide whether the defense-portfolio note gains a link to the rebuilt note.
- Pending handoffs (for `README.md`): C9 fold at `formal-systems-…`; wording check of the pre-formal note's binding-only prototype definition (C4); defense-portfolio citer question (C7).
