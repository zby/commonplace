# Mechanism reversal adjudication packet

**Status:** maintainer decision requested; no vocabulary, contract, ADR, or corpus change is authorized by this packet.

## Decision requested

The maintainer must decide how to respond to the [blind reclassification result](./blind-mechanism-reclassification-results.md), which produced the pre-registered reversal-evidence outcome against the mechanism review's 41-row EX / 72-row OP split.

Recommended response: **reject the current disposition ledger as an adoption basis and authorize a full k-sampled reclassification under a stricter boundary-application record.** Do not decide the successor spellings, the reference→notes authorization gap, or a migration plan until that replacement ledger exists.

Two alternatives remain available but require an explicit maintainer choice: abandon the split in favor of one broad successor, or override the pre-registered gate and adopt the reviewed split despite the failed thresholds.

## Evidence now on the table

The [mechanism direction review](./mechanism-label-direction-review.md) classified the 128-row positive surface as 41 explanatory (EX), 72 operational (OP), 10 prerequisite-shaped (EN), and 5 other exact successors. It recommended `explained-by` and `operates-through`, with the 10 EN rows held out.

The blind test sampled 21 EX rows, 18 OP rows, and all 10 EN rows. Three fresh isolated classifiers read the full source and target material for each row and applied only the pre-registered definitions.

| test signal | result | reading |
|---|---:|---|
| Stable EX/OP majority | 39/39 (100.0%) | passes the ≥90% threshold |
| Unanimous EX/OP classification | 34/39 (87.2%) | the supplied classes were usually applied consistently |
| Majority agrees with review | 30/39 (76.9%) | fails the ≥80% threshold |
| Direct EX↔OP reversal | 7/39 (17.9%) | fails the <15% threshold |
| Other EX/OP boundary disagreements | 2/39 (5.1%) | smaller than direct reversal |
| EN majority agrees with review | 5/10 (50.0%) | prerequisite preclassification also needs later review |

Direct EX↔OP reversal is the dominant failure, so the result is reversal evidence under the protocol rather than an ambiguous middle outcome.

## What failed

The sampled row dispositions failed to reproduce. The disagreement is asymmetric:

- Six reviewed OP rows received an EX majority. Their targets were read as accounts or general principles explaining the source, not literal execution paths: reflection/addressability, deploy-time learning, homoiconicity, the verification boundary, and the process/output-structure distinction.
- One reviewed EX row received a unanimous OP majority. Its target is a concrete codify-versus-LLM decision rule used to choose an operational representation.
- Two reviewed OP rows received an OTHER majority. Their targets supplied a descriptive scale or broader risk frame rather than an explanation, operating path, or prerequisite.

This pattern says more than “the boundary is fuzzy.” It shows the prior review sometimes treated a target that describes or explains an operation as the operation itself, and once treated an actually used decision rule as merely explanatory.

## What did not fail

The test does not show that EX and OP are indistinguishable in the supplied definitions. Every EX/OP row had a stable majority, 34 were unanimous, and 10 of 18 reviewed OP rows retained an OP majority. A recurring operational core therefore remains.

That is evidence that a split may still earn registration after a reproducible classification, not evidence that the reviewed split may be adopted now. The failed object is the current row-level disposition ledger and the adjudication readiness built on it.

The test also does not decide:

- whether `explained-by` and `operates-through` are the right spellings;
- whether one broader identifier would produce better reader decisions;
- how the full unsampled surface would move under majority classification;
- whether the single reference→notes edge should be authorized under any successor;
- whether an inverse relation earns registration;
- how the 10 EN rows divide among explanation, prerequisite, or later control-flow relations.

## Maintainer choices

### A — replace the ledger with full k-sampled classification (recommended)

Authorize a new read-only classification over the complete rebaselined positive surface. Use k≥3 fresh isolated samples per row, preserve origin labels, and produce a majority ledger with every non-unanimous row exposed for adjudication.

This honors both the pre-registered reversal rule and the workshop-wide k-sampling rule. It retains the possibility of an EX/OP split without pretending the current 41/72 counts are reliable.

Approval of A authorizes evidence production only. It does not adopt an identifier, change a contract, or approve migration.

### B — abandon the split and evaluate one broad successor

Treat the reversal as evidence that the maintenance distinction costs more than it returns, then run a new identifier evaluation for one broad relation.

Neither current candidate can simply absorb the other cohort: `explained-by` is false for the stable operational core, while `operates-through` is false for the explanatory majority. A broad-successor choice therefore needs its own assertion, reader need, revision consequence, and boundary test; retirement into existing relations or connective prose remains a valid candidate outcome.

Approval of B does not select that successor. It authorizes a new evaluation packet.

### C — override the gate and adjudicate the reviewed split

The maintainer may decide that the complete first review outweighs the sampled reversal test and proceed to spelling and authorization decisions.

This is an explicit override of two failed pre-registered thresholds. If chosen, the ADR must record the override and its reason rather than describing the test as support. The migration plan must also flag all nine sampled EX/OP disagreements for exact maintainer disposition instead of inheriting the review blindly.

## Proposed classification record for option A

The existing definitions already contain the useful distinction; the replacement run should force each classifier to expose how it applied them. Before returning EX, OP, EN, or OTHER, each vote records short answers to these tests:

1. **Literal-use test:** Is the target process, component, control path, artifact, or operational rule actually used or performed in producing the source effect, or does the target instead describe why the effect occurs?
2. **Explanation counterfactual:** If the target claim were rejected while implementations stayed unchanged, would the source's causal or explanatory argument need re-reading? A yes favors EX.
3. **Operation counterfactual:** If the target interface, behavior, control path, artifact, or rule changed while the explanation stayed accepted, would the source's operational fit or behavior need review? A yes favors OP.
4. **Prerequisite test:** Must the target be available, true, or completed before the source works even though it is neither the explanatory account nor the operating path? A yes favors EN.
5. **Neither test:** If none applies, return OTHER and name the relation rather than forcing the row into the split.

These are per-edge boundary tests, not endpoint-role signatures. They preserve the foundations workshop's decision against a role ontology.

The run should:

- rebaseline every active `mechanism` edge and the exact deferred `grounds` cohort before dispatch;
- classify every row, not only the 49-row test sample;
- use neutral row identifiers and hide origin, prior disposition, and cohort ordering from classifiers;
- retain each vote, confidence, counterfactual answers, and majority;
- report stable, unanimous, and non-majority rows separately;
- keep EN and OTHER outside either proposed successor;
- return to the maintainer with new counts and exact authorization consequences before any ADR or migration plan is drafted.

The acceptance rule for the replacement ledger should be fixed before dispatch. At minimum, no row without a stable majority should enter an automatic migration cohort, and every non-unanimous row should remain visible for maintainer adjudication.

## Downstream consequences

Until the maintainer chooses A, B, or C:

- no `explained-by` or `operates-through` catalogue entry is adopted;
- the 79 active `mechanism` rows and 49 deferred `grounds` rows do not move;
- the broader grounds migration remains blocked on these exact dispositions;
- the 10 EN rows remain held for the `enables` / `precondition` family review;
- the reference→notes authorization gap remains open;
- reader need, revision consequence, and boundary-test catalogue entries remain drafts, not registered vocabulary;
- there is no mechanism ADR into which the ADR 009 scoping amendment can honestly be folded.

The ADR 009 contradiction is logically independent and can be amended separately if the maintainer does not want it to wait for a replacement mechanism decision.

## Maintainer response

Record one choice before downstream work resumes:

- [ ] **A — full k-sampled reclassification**; approve the proposed record as written or state changes.
- [ ] **B — evaluate one broad successor**; state whether retirement must remain in the candidate set.
- [ ] **C — override the failed gate and adjudicate the reviewed split**; state the reason the complete first review should control.

No box is checked by this packet. The decision belongs to the maintainer.
