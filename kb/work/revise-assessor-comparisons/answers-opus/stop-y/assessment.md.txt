# Assessment: Continual learning requires governing behaviour-changing writes

**Proposed purpose (the operator named none):** Agents and maintainers who design deployed learning loops should see why persisting content is not continual learning. They should also see what such a loop must govern: selecting, validating and authorizing behaviour-changing writes, and coordinating them across the representational forms the system can change.

**Outcome: stop.** The highest-value change is a correction to the claim itself, and it would restructure the argument. The note does not decide whether "requires" is constitutive (an ungoverned durable change is not continual learning) or about reliability (governance is what makes continual learning safe). Its field-usage sentence asserts the constitutive reading as convention. That assertion is unsupported, and the reports say it is false of the ML literature. The note's own grounds and its paragraph on parametric continual learning support only the reliability reading. Which reading holds decides the thesis, the title's "requires" and the opening sentence. The passes do not change claims. Because a rewrite would replace the text they work on, no passes are planned.

## Ranked changes against the purpose

1. **Decide what "requires" claims, and drop or source "as the field uses the term".** Cost: a rewrite of the opening claim and the discriminator paragraph, possibly the title. Route: rewrite, not a pass (see Stop). Sources: critique (`kb/reports/state/review/results/kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md/kb/instructions/critique-note.md`), premise decomposition (`.../kb/instructions/premise-decomposition-gate.md`), composition friction (`.../kb/instructions/composition-friction-gate.md`), and findings `semantic/conceptual-role-conflation`, `semantic/epistemic-status-blur` and `semantic/underspecified-assertions`.
2. **Give the regression-validation premise real support or mark it as conjecture.** Cost: one sentence plus a link, but it changes a claim's support. Route: claim question / rewrite commission. Finding `semantic/grounding-alignment` (fail) and `sentence/misleading-link-text` item 1: the scheduler-LLM note says nothing about compounding silent degradation.
3. **State the self-selection condition in the opening, not only at the end.** Cost: restructure the opening and the final paragraph. Route: rewrite. Source: compression synthesis opportunity 1 (`kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/synthesis`). This depends on item 1.
4. **Reorder the final paragraph as definition, discriminator, scope, with one human-selection statement.** Cost: one paragraph reorder plus a merge. Pass: `readability-and-flow` (findings `compression-bundle/detail-overhang` and `marginal-value-redundancy` item 4). Deferred because the rewrite will replace this paragraph.
5. **Split the verbless dash-list in the counting criterion into its own sentence.** Cost: one sentence. Pass: `fix-strategy-taxonomy` on `sentence/clause-packing` and `sentence/parsing-ambiguity`. Deferred: the sentence sits in the passage under claim question 1.
6. **Repair footer labels and stale link texts.** Cost: a few footer lines. Pass: `fix-strategy-taxonomy` on `kb/theory/COLLECTION` and `sentence/misleading-link-text` items 2–3. This would survive a rewrite, but it is low value against the purpose. Leave it for the rewrite commission or a focused `--finding` run after it.
7. **Add a `## Scope` section.** Cost: a new section that pulls limits out of the prose. Finding `kb/types/note`. Which limits belong in it depends on item 1, so it belongs to the rewrite.
8. **Gloss "operative retention", "reject-capable evaluation" and "contextual activation" inline.** Cost: two short glosses. Pass: `fix-strategy-taxonomy` on `accessibility/undefined-terms`. Deferred: the first gloss sits in the disputed discriminator sentence.

## Sentence a hostile reviewer would attack first

"Continual learning, as the field uses the term and as this note uses it, asks for more: the system does the selecting itself." It attributes a stipulation to "the field" without a source. ML continual learning is defined by learning from a non-stationary stream without catastrophic forgetting, not by self-selection behind a reject gate. The sentence also makes the title's "requires" partly true by definition.

## What reads well

The opening paragraph's consumption-path argument holds: behavioural authority belongs to a consumption path, not to stored bytes, so persistence alone cannot decide which write shapes behaviour. The weights-only-updater conditional also holds. Every report that tested these two premises found that they survive.

## Candidate overclaims: support or divergence

- "Continual learning, as the field uses the term and as this note uses it, asks for more: the system does the selecting itself." — **Support**, and wrong as stated. It may be narrowed to the note's stipulation. This is the stop item.
- "candidate writes must be validated against regression, because continual adaptation compounds silent degradation" — **Support**. It may be narrowed (per-write, built into the update rule, or post-install with rollback) or re-grounded. Dependents (dfa-moe, dual-nature OPD, merchantbench, harness-continual-learning, long-horizon-agents) rely on the regression-validation requirement, so the requirement must survive in some form.
- "deployment evidence arrives online and is often sparse, so candidate writes must be cheap to propose and install" — **Support**. It may be narrowed to agent deployments with low-volume feedback.
- "a learning loop must decide which form a lesson belongs in" — **Support**. It may be narrowed to systems with several writable forms or to design-time placement.
- "Persistence alone therefore does not create a governed behaviour-changing write." / "belongs to a consumption path, not to stored bytes" — **Divergence**. This is the note's distinctive position against store-everything memory. Many dependents rely on it, so keep it.
- "then an updater restricted to weights freezes consequential choices outside its reach" — **Divergence**. Keep it; dependents rely on it.
- "Those changes are learning too: the software learns by selection that people perform on it." — **Divergence**. The note keeps human-selected change inside learning while excluding it from continual learning. Keep it.

## Stale qualifications (claim questions, own commits after approval)

- The description says updates are coordinated "across the representational forms a system can change". The body says a loop "need not touch all three every time". The description should match the body.
- The footer annotation on "Only explicit retention is durable, writable, and addressable" says it is "the form-level trade space this note defers to". The body defers that trade space to the representational-form coevolution note, and the link text is a stale title (the target is now "Explicit retention provides direct targets for selective revision").
- The footer link text "Constraining during deployment is continual learning" claims more than its target's current title, "Constraining during deployment can produce learning outside weights".
- The footer gloss on the scheduler-LLM link ("why symbolic writes are cheaply validated and parametric ones are not") extends the target to parametric writes, which it does not discuss.
- Several footer `grounds` edges name "axes" (reach, addressability, sample efficiency) that the body never names or uses.

## Claim questions for the operator

1. **Constitutive or reliability "requires" (defect; two readings).** Passage: the opening "It requires governing durable changes…" together with "A behaviour-changing write counts as continual learning when the system's own loop selects and retains it… — for retained candidates, search, reject-capable evaluation, and operative retention". Reading A: online gradient continual learning, which the note's third paragraph calls "parametric continual learning", is not continual learning because nothing can reject a candidate. Reading B: it is continual learning, and governance is a reliability requirement. Under each reading a reader would classify the field's paradigm case differently. Reports: critique-note, premise-decomposition-gate, finding `semantic/underspecified-assertions`. This one goes to the stop.
2. **Field attribution (defect: unsupported, likely false).** Passage: "as the field uses the term". Reports: critique-note, composition-friction-gate, premise-decomposition-gate, findings `semantic/epistemic-status-blur` and `semantic/conceptual-role-conflation`. This one goes to the stop.
3. **Regression premise without support (defect: unsupported).** Passage: "because continual adaptation compounds silent degradation (see Scheduler-LLM…)". Report: composition-friction-gate; findings `semantic/grounding-alignment` (fail) and `sentence/misleading-link-text`. One or two sentences would correct it, but it is in the rewrite scope.
4. **Hybrid propose-and-approve loops (defect: unsorted boundary case).** Passage: "The same edit hand-authored in reaction to an incident is maintenance". The note lists "authorize" as a governance step, yet places human selection outside the loop. A system that proposes from deployment evidence and has an operator approve is left unsorted. Dependent `kb/sources/hyra-2-next-step-for-auto-research.ingest.md` cites human approval as evidence for the note. Reports: premise-decomposition-gate, finding `semantic/completeness-boundary-cases`. One sentence would correct it.
5. **Read-time governance (choice/extension, unclear).** If authority belongs to a consumption path, does "governing writes" include read-time selection in store-everything memory? Reports: premise-decomposition-gate, critique-note. I cannot tell whether this is a defect or an extension, so I treat it as a choice: no defect is shown and I do not rank it first. It affects the title's locus ("writes"), so the rewrite commission should decide it.
6. **Move the self-selection condition into the opening and description (choice, no defect shown).** Source: synthesis opportunity 1. It is subordinate to question 1.

## Findings not acted on (run stopped), each once

- `accessibility/undefined-terms` (depth 3): the glosses sit in the disputed discriminator sentence; deferred to the rewrite.
- `compression-bundle/detail-overhang` (depth 4) and `compression-bundle/marginal-value-redundancy` (depth 4): they target paragraphs the rewrite will restructure. The defensive clauses ("It need not touch all three every time", "broadening the system boundary does not remove them") are minor. "Need not touch all three" also bears on the stale description, which is claim-adjacent.
- `kb/theory/COLLECTION` (depth 2): the footer label repairs would survive, but they are low value against the purpose; the rewrite or a later focused run can take them.
- `kb/types/note` (depth 2): which limits go in a Scope section depends on question 1.
- `semantic/completeness-boundary-cases`, `semantic/conceptual-role-conflation`, `semantic/epistemic-status-blur`, `semantic/grounding-alignment`, `semantic/underspecified-assertions` (depth 2): claim questions, not passes.
- `sentence/clause-packing` and `sentence/parsing-ambiguity` (depth 5): they target the disputed discriminator sentence.
- `sentence/misleading-link-text` (depth 5): item 1 is claim question 3; items 2–3 are stale link texts listed above.
- Extension, not recommended: the role report's untaken recommendation from `kb/sources/dual-nature-generalization-on-policy-distillation.ingest.md` (that validation scope must reach beyond an update's nominal domain). The claim stands without it.
- Extension, not recommended: the role report's untaken evidenced-by candidate `kb/sources/llm-agents-are-not-always-faithful-self-evolvers.ingest.md` (its reason is unseen).
- Extension, not recommended: the PARTLY SUPPLIED retirement or revert step (agentic-reasoning survey, intern-s2-mobius). The claim as scoped stands without it.

## Stop

See `plan.md`. The route is `commonplace-revise rewrite kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md --commission FILE`, with the commission prepared using `cp-skill-write-multistage`.
