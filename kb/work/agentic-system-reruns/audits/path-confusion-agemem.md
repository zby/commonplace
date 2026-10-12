# AgeMem validation-path retrospective

## Disposition

**Substantively reasonable with recorded limits; no unresolved consequential content defect concealed by the inspected path confusion was established.** In the audit vocabulary, this supports **integrate with recorded limits**, not a new integration action. The final publication already carries the necessary qualifications.

This does not mean all affected candidates were defect-free. Runtime had quotation failures that were repaired. The first memory profile overstated completeness of summary-input provenance; later semantic verification rejected that assertion and the final profile corrected it. These were distinct from the mistyped validator paths. All three affected workers subsequently ran the supplied-path check and received a member-content pass. None of those passes certifies claim support or universal procedural compliance.

## Identity and method

- Independent retrospective auditor: `openai/gpt-6.1-sol`, medium reasoning, confirmed by `PI_PROVIDER`, `PI_MODEL` and `PI_REASONING_LEVEL`. No delegation.
- Run: `AAS-2026-10-12-2601-01885v1-32274e5bddc1-01`.
- Frozen method identity supplied by the prior audit: `cd6e8250c5277c5c6295b6940a9b01e034c9daa7`. This check did not recertify the method checkout.
- **W**: `/home/zby/llm/commonplace/.commonplace/worktrees/agemem-32274e5bddc1`.
- **R**: `W/kb/agentic-system-analyses/state/AAS-2026-10-12-2601-01885v1-32274e5bddc1-01`.
- **S**: `R/sources/2601.01885v1.html`, source identity `https://arxiv.org/html/2601.01885v1`. Independently computed SHA-256: `15a7a5f4620aa1b130b4f420a08d8c671aa601f4aad45c101eedfd05d528c7b0`.
- **P**: `W/kb/agentic-system-analyses/retained/2601-01885v1`. All 12 Markdown members are byte-identical to origin `kb/agentic-system-analyses/retained/2601-01885v1`; this is not a manifest-validation claim.

Read the [audit procedure](../audit-a-rerun.md), [prior AgeMem audit](batch-03-agemem.md), [maintenance diagnosis](../validation-path-maintenance.md) and workshop contract. Used prior findings as inspection leads, not as source authority. Read the affected final members and synthesis, compared stored candidate versions with publication, and independently inspected decisive frozen-source passages. HTML rendering retained math `alttext`; embedded schema/evaluator listings were also decoded from their captured base64 payloads. No live source or implementation was admitted. No exhaustive reanalysis or historical-account comparison was undertaken.

## Candidate-to-publication comparison

Exact candidate locators are `R/state/attempts/<attempt>.json`, field `outputs`, and `R/state/versions/<hash>`. Each stored candidate's SHA-256 was checked against its filename.

| Attempt | Returned candidate hash | Difference from final publication |
|---|---|---|
| `000005-runtime` | `502d670b70b5e9a718679d39d2705ed24571eb8f6889a346467d2f1ee74c2575` | Byte-identical to P/runtime.md. |
| `000008-epistemic` | `ad6bbf7b3b4bb796ac31e4c7b4d693085a642ad3522a612a75c32bfd463b6d84` | Byte-identical to P/epistemic.md. |
| `000024-memory-profile` | `12a49fee1ec62ef3ff7d1b56713b6312358c9b45b742a142f72e99fdcc6dd03c` | Summary production's `trace_source` assessment changes from `known` to `partial`; local note, references, axis note and rationale retain unresolved original input origins. Other classifications are unchanged. |

The corrected profile is version `f90519d70f698a10b12a14fb537b71b4585764e7348953678d4dcd401035fad7`. `R/state/judgments/000027-apply-profile-verification-1.json` refuses the original profile for its completeness overclaim. `000031-apply-profile-verification-1.json` accepts the corrected version. The correction is substantive: conversational wrapping cannot establish the provenance of supporting information, generated distractors, retrieved content or earlier summaries. It is not merely a validation-path repair.

## Independent substantive findings

1. **Runtime control and retrieval are reasonably characterized.** S `#alg3.l5`–`#alg3.l13` (HTML lines 2317–2379) samples a message, retrieves against it, inserts the results, then samples the policy action and records experience. This supports P/runtime.md `#rt-rte-stage-retrieval` and the profile's separate push/pull routes; it contradicts an exclusively policy-requested retrieval interpretation. `#alg4.l3` resets C while M persists; `#alg5.l4` carries Stage 2 context and appends q. The prose at `#A1.SS3.SSS0.Px2` says the query is withheld, while `#alg3.l8` and `#alg4.l6` include q in the state tuple. P/runtime.md `#rt-clm-context-reset` and P/synthesis.md explicitly leave actual query visibility unresolved, rather than asserting leakage or proven isolation.

2. **Preservation and meaningful maintenance are correctly qualified.** S `#A1.SS1.SSS0.Px5` (line 1447 onward) specifies summary replacement and a preservation prompt, not an independent fidelity gate. `#A1.SS1.SSS0.Px6` (line 1513 onward), equation `#A1.E15`, retains messages below the similarity threshold despite prose suggesting a criterion describing “what to keep.” The captured STM schema, `#A1.F6` (listing payload at line 1633), instead describes removal criteria. P/runtime.md `#rt-rte-context-summary` and `#rt-rte-context-filter` preserve these limits. S `#A1.SS2`, equations `#A1.E20`, `#A1.E21` and `#A1.E24`, separately reward early reduction-tool invocation, presence of query-derived tokens/phrases, and occurrence of Update/Delete. P/epistemic.md `#epi-rte-context-reward`, `#epi-rte-telemetry-reward` and `#epi-clm-maintenance-quality` reasonably distinguish these proxies from semantic fidelity or justified repair. Other reward components may indirectly penalize a harmful edit; the report does not claim every harmful edit is globally rewarded.

3. **Evaluation is not confused with knowledge admission.** S `#A1.E23` labels storage quality using q and the expected answer; `#A1.E25` judges retrieved relevance. Captured benchmark prompts at `#A3.SS2.p2` and `#A3.SS2.p4` (payload lines 3027 and 3097) instead compare supporting facts and answer equivalence to references. Qwen-Max is explicitly named at `#A3.SS2.p2.2` and `#A3.SS2.p3.1`. These support the epistemic report's distinct scoring domains and its refusal to infer a per-entry truth-acceptance gate. S `#S4.T4` (line 871 onward) independently confirms J 0.509→0.544, MQ 0.479→0.533, tokens 2078→2117 and calls 3.93→4.92. P/epistemic.md `#epi-clm-reward-benefit` and the synthesis correctly treat this as an attributed bundled comparison, not uniformly lower resource use or isolated action-level causal credit.

4. **The memory profile's central classifications have documentary support.** S `#A1.SS1.SSS0.Px1`–`Px4` separates text, dense encodings and metadata and specifies insertion/replacement/removal. The LTM schema, `#A1.F7` (payload line 1738), requests retrieved IDs and a boolean deletion confirmation; it does not establish human approval or executable enforcement. `#A2.SS1` illustrates conversation-derived preference writes and subsequent revision/read-back. `#alg2.l22`–`#alg2.l37` specifies grouped reward normalization, uniform advantage broadcast, gradient updates and returned policy. The profile reasonably retains these as claimed automatic write/read-back and learning paths without asserting a concrete database, restart durability, measured summary fidelity or inspected deployment loading. The STM span schema includes tool messages within conversation rounds, supporting tool-related summary inputs but not complete input provenance. The corrected local `partial` assessment therefore fits the source better than the original `known` assertion.

These qualifications are public in P/synthesis.md, especially “Construct memory, interrupt context, then answer,” “Evaluate experience and change later decisions,” and its Limitations table. The remaining combined text/bookkeeping experience unit prevents part-level comparisons; the synthesis records that limit. This audit is not supplying a missing qualification to rescue publication.

## Actual validation versus procedural compliance

**T** is `/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--/2026-10-12T13-59-16-666Z_01a13069-19ba-745a-b8d3-80c377c91314.jsonl`, line 31, message `5f3ae59f`, `message.details.results[1]`. Below, Wk is the nested worker within T; indexes are zero-based. Complete supplied invocations are Wk `messages[3].content[0].text`.

| Attempt; Wk locator | Wrong-path call/result | Restored supplied-path call/result | Further check after edits |
|---|---|---|---|
| Runtime; `messages[23].details.results[0]` | Wk 47/48, `call_4j0zCSZtekoEmMYIpUuFGM7j` | 49/50, `call_wfdyUGtRW9apPkOcwvDCTVw6` | No subsequent runtime edit in this worker trace. |
| Epistemic; `messages[27].details.results[1]` | 47/48, `call_EF6Mu2gZdKnwheGy6241PCvS` | 49/50, `call_ctOklI0yVVCzBkSGtuK70jQZ` | Edits at 51 and 53; final pass at 55/56, `call_jurQjMS22vOvFGpuFut6gzJY`. |
| Profile; `messages[39].details.results[0]` | 51/52, `call_edMlJoJfljxfnIWTQPORt0g7` | 53/54, `call_6OFanEsx9fv8GoHd6ecZeMbQ` | Builder edit at 55 and regeneration; final pass at 59/60, `call_8Ye9l4l1GnHPRSDULLvjip8z`. |

Call IDs omit provider suffixes; the exact full IDs and paired results are at these locators. Wrong-path calls return missing `ARTIFACT.yaml` and exit code 2. All listed passing results say:

```text
Member content check passes; invocation residue not checked. This is not job acceptance or claim support.
```

The delivered artifact path is `R/artifact`. Runtime and profile temporarily substitute `W-01/artifact`; epistemic substitutes the worktree name with an added `-01` while keeping the remaining run path. The later commands restore the supplied executable, candidate, artifact and role arguments. This is actual historical execution evidence, not inference from publication.

Runtime also has an earlier **correct-path** call at Wk 37/38, `call_f4py0mdXA6xf17o9EPMRH1Iz`, exiting 1 with five quotation findings. Wk edits 43 and 45 repair quote strings before the mistyped call and final pass. Independent source inspection confirms the underlying schema, summary and terminal-reward claims; the failed literal quotations did not require reversing those claims. This content failure was not caused by the path typo.

Procedural conclusion: the workers violated literal-path copying on the failed calls, then completed the supplied-path validation obligation. The epistemic and profile workers also rechecked their subsequently edited outputs. A passing deterministic check did not detect the original profile's completeness overclaim; later semantic verification did. Neither restored-path success nor that correction proves all source-reading, identity or other worker obligations were satisfied. No retrospective execution of the historical candidates was performed here.

## Limits and blocker

This was a bounded check of the three affected attempts, their returned versions, selected decisive source claims and final qualification propagation. It did not execute AgeMem, reproduce results, exhaustively inspect every formula or classification, audit every worker obligation, or rerun historical validators. It establishes substantive reasonableness at the paper-only boundary, not verified runtime behavior. No unresolved consequential content blocker was established within this scope.

Only this workshop report was authored. No analysis output, source, state, method, checklist or integration record was changed; no recovery, integration or commit was attempted.

## Report validation

Validate only this frontmatter-free workshop report with `commonplace-validate kb/work/agentic-system-reruns/audits/path-confusion-agemem.md`. The command result is recorded in the completion response.
