# Check reconciliation

This ledger keeps each fresh check attached to the candidate snapshot it actually inspected. A friction report routes attention; it is not an acceptance verdict. Semantic WARNs marked material are blockers until a later candidate resolves them and a fresh audit confirms the result.

## Snapshot map

| Snapshot | SHA-256 | Fresh reports |
|---|---|---|
| `candidate-v1.md` | `018e9523ae3579cada7172bf89c19a7765258c805dca414ca2f436cba3247ef2` | `friction.md`, `semantic-audit.md` |
| `candidate-v2.md` | `8e0f53f1d16229386f690666d5cb9baa10a7d7657d251f8284b9a1e8c8c4aad2` | `friction-v2.md`, `semantic-audit-v2.md` |
| `candidate-v3.md` | `75c777a9f018ed59941dc3844d046736ab95c6374eab4cf766b9a56d326b8c46` | `friction-v3.md`, `semantic-audit-v3.md` |
| `candidate-pre-full-pass.md` | `a04bb30d6c7fb2eb81a6ee2f9a58cfe974744c572ea17bc535eb210c4d9eef28` | `semantic-audit-final.md`, `acceptance.md`, `blind-comparison.md` |
| `candidate-full-pass-v1.md` | `932a44dce42b479559ce0697051edaec7229f1249cd1b8c2c0e53dfde0d6a0c6` | `full-pass-acceptance-v1.md`, `full-pass-judge-1.md`, `full-pass-judge-2.md`, `full-pass-judge-3.md` |
| `candidate.md` | `f77ff52bcdbfec18bd81e8c8db567aa2d9c034c5535e828f61c088316a6029b7` | `final-review-summary.md`, `final-friction.md`, `final-acceptance.md` |

## First-check reconciliation: v1 to v2

- **Idea generation fell outside an outcome set that appeared closed.** Removed it from the adjacent-outcome sentence and scoped the three outcome tests as an open minimum for KB-writing evaluation.
- **`KB`, `human-agent`, and `epistemic work` did no work in the central auditability mechanism.** Broadened the workflow scope, separated optional human participation from role allocation, and narrowed the title to attempted operations.
- **`Material reported finding` left the disposition population unresolved.** Required a record for every reported challenge to a load-bearing commitment, including challenges later found unsupported.
- **Human fallibility did not erase human-machine differences.** Limited the inference to authorship being insufficient evidence of checking and left mechanism and error-rate differences empirical.
- **Missing comparative evidence did not erase every noncomparative claim.** Scoped the evidential ceiling to the supplied evidence and to effects or comparison claims.
- **Correlation mattered only when checks were combined as independent evidence.** Added that condition.
- **A trace did not by itself make a stage allocation testable.** Required success criteria in addition to trace data.
- **Authorship was not irrelevant merely because it was an inadequate proxy.** Stated that actor choice may affect performance and itself needs evaluation.

## Second-check reconciliation: v2 to pre-full-pass candidate

- **Operation traces did not expose actor allocation.** Limited the base claim to staged artifacts and handoffs; when actor allocation is tested, the trace must also record the role occupant and conditions.
- **`Investigate` was an interim route presented as a final disposition.** Made it an open status and separately enumerated final dispositions.
- **The concrete loop's bare `reject` had opposite possible objects.** Distinguished rejecting a challenge with cited support from rejecting the claim.
- **Stage-by-stage validation was stronger than a loop-level outcome claim required.** Allowed blinded loop-level comparison while requiring stage evidence only for stage attribution; retained the missing commit-and-expose criterion as an explicit evidence gap.
- **Artifact improvement was tied unnecessarily to an upheld critic finding.** Allowed independent outcome evidence such as blinded comparison; a critic finding is one route, not a prerequisite.
- **`Naive prose delegation` lacked a comparator protocol.** Defined it as seed-to-generated-prose acceptance after only global reading or approval, with no commitment-, route-, or challenge-level record.

The candidate was then compressed without changing these resolutions. The v3 semantic audit found no WARN or material blocker. The v3 friction report found that the trace, synthesis, and inspectability joints held and routed two remaining evaluation-design joints:

- **Blinding and a named outcome were insufficient to define a loop-level causal test.** The final candidate now calls for a specified comparator, role allocation, and measurement rule, describes the result as a performance comparison, and says blinding alone does not identify the cause.
- **Restatement was neither necessary nor sufficient evidence of human understanding.** The final candidate now accepts independent restatement, update, or application and excludes copied restatement along with assent.

Because the friction instruction always ranks a note's weakest joints and emits no acceptance verdict, these two changes are not followed by another friction run. The routed v3 report remains inspectable here, while the acceptance reviewer receives the final candidate independently. A final fresh semantic audit checked the changed claims and found all eight applicable gates passing, with no WARN or material blocker.

## Full pass and final targeted revision

The full improvement pass selected a stronger reader update than “attempted operations are auditable”: one independently adjudicated local correction can be established without validating the method across cases. It compressed the multistage candidate from 1,054 to 716 words. Three fresh blind judges preferred that version unanimously, with balanced ordering.

The full pass's closing cycle then found that its opening adjudicated the reported fault but did not explicitly require adjudication that a revision or narrowing resolved it. It also found that the transfer from human writing practices to distributed recorded handoffs lacked an explicit analogy boundary. The final targeted revision:

- requires adjudication of both the reported fault and the final response;
- defines independent adjudication as a separate role applying a stated criterion, rather than a different actor alone;
- requires the adjudicator to confirm that the resulting claim resolves the fault, not merely that it changed;
- says the writing-practice sequence motivates candidate handoffs but does not establish preservation of epistemic effects; and
- narrows discrimination from a requirement for every whole-loop reliability claim to a requirement for critic reliability.

Fresh review over the final hash finds the source bridge, clause packing, parsing, and semantic specification acceptable. The only catalogue WARN is grounding alignment caused by promotion-relative links being unresolved from the nested workshop path. Source-grounded acceptance resolves those links from `kb/notes/` and passes. Final friction reports `SURVIVES`; it keeps the exact three-stage decomposition as the thinnest remaining joint, consistent with the note calling that taxonomy candidate and unvalidated.
