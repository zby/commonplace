# Assessment: Continual learning requires governing behaviour-changing writes, not just storing content

Artifact: `kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md`

**Proposed purpose (no operator purpose was given):** A reader who designs or evaluates deployed agent systems should be able to tell when a system's durable changes count as continual learning and not just stored content. They should also see what the system's own loop must do with a behaviour-changing write: select it, validate it, give it an authority path and coordinate it across forms.

**Verdict: stop.** The highest-value change is to fix what the central claim says, and passes cannot do that. The note supports two readings of "requires", and readers would reach different conclusions under each one. Settling it changes the thesis statement. It probably also moves the self-selection condition from the last paragraph to the opening, and possibly into the title. That is a restructuring. The one support the note offers for its regression-validation premise does not support that premise. Dependents rely on the discriminator and on the regression requirement, so the operator must also decide their changes. No passes are planned.

## What reads well

The note shows compactly why persistence cannot fix a write's force: behavioural authority belongs to a consumption path, not to stored bytes. Its concessions on parametric forgetting and on the remaining storage and activation subproblems keep the cross-form argument from becoming a dismissal of weights.

## Sentence a hostile reviewer attacks first

"Continual learning, as the field uses the term and as this note uses it, asks for more: the system does the selecting itself." It attributes to the field, without a source, the criterion that separates continual learning from maintenance. The field's paradigm cases do not meet that criterion: sequential gradient training with EWC or replay has no reject-capable candidate. This attack comes from report-2 (critique), report-3 (premise decomposition) and findings 7 and 8.

## Ranked changes (highest value against the purpose first)

1. **Decide what "requires" means and state the self-selection condition in the claim.** This is a restructuring (cost: new thesis sentence, opening, description and maybe title). No pass can do it; it needs the rewrite route. The defect has two readings:
   - **Constitutive reading.** Ungoverned durable change is not continual learning. The note's discriminator ("A behaviour-changing write counts as continual learning when the system's own loop selects and retains it … reject-capable evaluation …") supports this reading.
   - **Reliability reading.** Governance is what continual learning needs to stay reliable. The broad learning criterion the note adopts as grounds ("any durable change in a system's capacity") supports this reading, and so does the regression argument.

   Under the constitutive reading, online gradient continual learning during deployment is not continual learning. Under the reliability reading, it is. Paragraph 3 calls it "Parametric continual learning". Finding 10 (underspecified-assertions) shows that this choice changes the title claim's truth conditions.

   Report-4's synthesis (opportunity 1) adds a related point. The title and opening say continual learning "requires governing" writes. The body says "Mature release engineering already governs hand-authored readable changes" and calls that maintenance, not continual learning. So the opening claim, as worded, does not state the note's distinctive commitment. Moving self-selection into the opening sentence and description reorders the argument.

2. **Re-ground or recast the regression premise.** This changes a claim (cost: one or two sentences plus a support decision). Finding 9 is a grounding-alignment **fail**: "because continual adaptation compounds silent degradation" cites the scheduler-LLM separation note, which does not discuss degradation, compounding or continual adaptation. Report-1 rates this the thinnest joint. Report-3 gives counterexamples: bounded-step online learners, and post-install rollback. The premise is unsupported on the page. The fix is a claim decision: find support, mark the premise as conjecture, or widen validation to "per-write, update-rule or post-install with rollback". Passes cannot make that decision.

3. **Recast "as the field uses the term"** as the note's stipulated narrowing, or cite field usage. This changes a claim (cost: one sentence). Reports 2 and 3 and findings 7 and 8 raise it. It is bound up with item 1: report-3 warns that a stipulated definition makes the title "partly true by definition". So it cannot be repaired on its own until item 1 is decided.

4. **Place human-approval hybrids relative to "the system's own loop".** This changes a claim (cost: one sentence). It is a defect of the two-readings kind (finding 6; report-3). A loop that proposes from deployment evidence while an operator approves before installation is the common shape. The text sorts it either way: "authorize" is a governance step, yet "people outside its loop did the selecting" makes it maintenance. A dependent (`hyra-2`) already cites human approval as evidence for the note.

5. **Final-paragraph compression and reorder** (readability-and-flow, depth 4). Cost: a paragraph rework. Merge the doubled human-selection statement (findings 2 and 3), move the codification aside into the forms paragraph, and drop the closing restatement in paragraph 1. This would pay off on its own. But the rewrite in item 1 replaces this paragraph and the opening, so a pass now would be wasted.

6. **Split the discriminator sentence and give its dash-list a verb** (fix-strategy-taxonomy on findings 11 and 13; cost: one sentence). This is the same sentence that has open claim questions (items 1 and 4), so a pass must not touch it now.

7. **Footer link repairs.** Cost: local label and link-text edits.
   - Replace `defines` and `sharpens` with registered labels.
   - Fix the reversed `exemplifies` label and the bare `evidenced-by` gloss (finding 4).
   - Update two stale link texts (finding 12).
   - Fix the "axes" glosses that misdescribe the body (finding 5, info).

   These are independent of the rewrite and would still pay off afterwards. Leave them to the rewrite commission, or plan them on the rewritten text, so that the footer is not edited twice.

8. **Gloss "operative retention", "reject-capable evaluation" and "contextual activation"** (finding 1). Cost: a short inline gloss each. The first two sit in the discriminator sentence under item 1, so defer them with it.

9. **`## Scope` section** (finding 5). Cost: move the limits into their own section. Which limits exist depends on how item 1 is decided, so this belongs in the rewrite commission.

## Depth 1 and synthesis proposals, sorted

- **Constitutive/reliability ambiguity of "requires"** (report-2): **defect** (two readings; see item 1). Correcting it restructures the thesis, so it stops the run.
- **Field-usage attribution** (reports 1, 2 and 3): **defect**. The case is sequential gradient continual learning with EWC or replay, which has no self-selection and no reject gate. The sentence alone could be fixed, but the fix depends on item 1.
- **Regression premise unsupported** (report-1; finding 9 fail): **defect**, because the claim is unsupported. Passes cannot fix it.
- **Human-approval hybrid** (report-3; finding 6): **defect** of the two-readings kind. A one-sentence fix once item 1 is settled.
- **Write locus versus read-time selection** (reports 2 and 3): can't tell between defect and extension. Report-3 calls it LOCAL. The note's own premise ("belongs to a consumption path") makes read-time selection a candidate counterexample to the "writes" in the title. Treat it as a **choice** with no defect shown, for the operator to settle in the rewrite commission.
- **Form choice by the loop is not universal** (report-3, "a learning loop must decide which form a lesson belongs in"): **defect** of a narrow kind. The case is a system with one writable form fixed at design time. One clause fixes it. It is a claim question.
- **Sparsity does not support cheap writes** (reports 1 and 3): **defect** of a narrow kind. The "so" combines online arrival, which supports cheap writes, with sparsity, which does not. One clause fixes it. It is a claim question.
- **"Resulting problem" introduces authorization without an argument** (report-1): **extension**. The claim stands without the extra argument.
- **Synthesis 1, put self-selection in the opening:** **choice**, but it is folded into the defect in item 1.
- **Synthesis 2 and 3** (reorder the final paragraph; lead the opening with its premise): **choice**. Ranked below item 1 and superseded by the rewrite.

## Dependents affected (role report)

Role report run directory: `kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/role`.

- **System-selected discriminator.**
  - `kb/sources/hot-take-llm-can-jump.ingest.md` and `kb/sources/on-learning-how-to-learn-learning-strategies.ingest.md` rely on it.
  - `kb/sources/hyra-2-next-step-for-auto-research.ingest.md` relies on human approval counting as governance.

  Settling item 1 or item 4 changes the sense these dependents use.
- **Regression requirement.** `kb/sources/dfa-moe-dual-forgetting-vision-language-continual-learning.ingest.md`, `kb/sources/dual-nature-generalization-on-policy-distillation.ingest.md`, `kb/sources/merchantbench-long-term-coherence.ingest.md`, `kb/sources/long-horizon-agents-levels-ticks-cascaded-intelligence.ingest.md` and `kb/sources/harness-continual-learning-adaptation-beyond-model-parameters.ingest.md` rely on it. Recasting the premise (item 2) may change what they cite.
- **Unseen files.** 18 linking files are cut from the role report, so other dependents may exist.

## Divergence versus support (candidate overclaims)

- "Persistence alone therefore does not create a governed behaviour-changing write": **divergence** (keep). Many dependents rely on it.
- "an updater restricted to weights freezes consequential choices outside its reach": **divergence** (keep).
- "Those changes are learning too: the software learns by selection that people perform on it": **divergence** (keep). It is the note's stance that maintenance is still learning.
- "Continual learning, as the field uses the term …": **support**. It may be narrowed or recast; it is an open claim question.
- "because continual adaptation compounds silent degradation": **support**. It may be narrowed; it is an open claim question.
- "deployment evidence arrives online and is often sparse, so candidate writes must be cheap": **support**. It may be narrowed.

## Stale qualifications

- The description says updates are coordinated "across the representational forms a system can change". The body says a loop "need not touch all three every time" (report-2).
- The footer gloss on "Only explicit retention…" says the note "defers" the form-level trade space to it. The body defers that to the coevolution note (findings 5 and 12).
- The footer's `grounds` glosses name "axes" (reach, addressability, sample efficiency) that the body never uses (finding 5).
- The footer gloss on the scheduler-LLM note covers "parametric" writes, which the target does not discuss (finding 9).

## Claim questions for the operator

These are open behind the stop. The rewrite commission should settle them.

1. Is "requires" constitutive or about reliability? Does online gradient continual learning during deployment count (item 1; report-2; finding 10)?
2. Is self-selection the field's usage or this note's stipulation (findings 7 and 8; reports 2 and 3)?
3. What supports "continual adaptation compounds silent degradation"? Must validation be per-write, or may an update rule or rollback provide it (finding 9; reports 1 and 3)?
4. Is a human approver of a system-proposed candidate inside the loop (finding 6; report-3)?
5. Do read-time selection designs fall under "governing writes" (reports 2 and 3)?
6. Can the form choice be made at design time (report-3)? Does sparsity, or only online arrival, motivate cheap writes (reports 1 and 3)?

## Findings not acted on (each once, with reason)

- **Finding 1** (undefined-terms): deferred, because its passages are rewritten under item 1. "Contextual activation" could be glossed after the rewrite.
- **Finding 2** (detail-overhang): deferred, because its paragraph is restructured by the rewrite.
- **Finding 3** (marginal-value-redundancy): deferred for the same reason. The cuts of "It need not touch all three every time" and "broadening the system boundary does not remove them" are also defensible as scope statements, and finding 5 counts them as limits.
- **Finding 4** (theory COLLECTION footer labels): not planned now, to avoid editing the footer twice. Apply it to the rewritten text.
- **Finding 5** (note type, Scope section): its limits depend on item 1. Include it in the commission.
- **Finding 6** (completeness-boundary-cases): a claim question (4).
- **Finding 7** (conceptual-role-conflation): a claim question (2).
- **Finding 8** (epistemic-status-blur): claim questions (2 and 3).
- **Finding 9** (grounding-alignment, fail): an unsupported claim. It is part of the stop.
- **Finding 10** (underspecified-assertions): part of the stop (item 1).
- **Finding 11** (clause-packing): its sentence carries open claim questions, so passes are scoped away from it.
- **Finding 12** (misleading-link-text): the inline scheduler-LLM citation belongs to the stop. Apply the two stale footer link texts to the rewritten text.
- **Finding 13** (parsing-ambiguity): same sentence as finding 11, so it is scoped away.
- **Role-report untaken recommendations** (a regression-validation example beyond the nominal domain; citing the faithful-self-evolvers ingest): **extensions**. The purpose does not ask for them.
- **Report-1's "open-ended behaviour" validation gap:** an **extension**.

## Route

`commonplace-revise rewrite kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md --commission FILE`, with the commission prepared using `cp-skill-write-multistage`. The operator may decline the restructuring. They can then answer the claim questions as separate commits and re-run quick revision for the local passes (items 5–8).
