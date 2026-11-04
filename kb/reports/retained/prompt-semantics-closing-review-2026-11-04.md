# Prompt semantics rewrite: closing review, 2026-11-04

## Purpose and result

This record supplies the final acceptance disposition for the operator-commissioned prompt-semantics rewrite and its [original coherence audit](./prompt-semantics-coherence-audit-2026-11-03.md). The operator requested a closing round after R5 and a whole-note cohesion pass. R1–R5 are resolved within that internal-coherence scope. The temporary workshop can close.

Reviewed the revised argument, dependent notes, relevant tag heads and backlinks against the eight conceptual cases below. This is an assistant-authored consistency review, not human verification or an empirical test. R3/R4 were committed in `f25ad7fa8`, R5 and cohesion repairs in `2080534ab`, and three note relocations plus one attached brief in `615fe4821`. The closing change repairs remaining navigation prose and retains this disposition before removing the workshop.

## Acceptance cases

| Case | Result and current home |
|---|---|
| Same prompt, English or deterministic package as reference | Pass: [the central argument](../../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md) changes diagnosis without erasing task adequacy or prediction cost. |
| Precise stochastic reference | Pass: the central argument includes decoding variation in the specified package; precision does not require identical outputs. |
| Permitted alternatives, disputed interpretation, missing evidence | Pass: the central argument distinguishes these cases and supplies different responses. [Instruction composition](../../theory/clear-instructions-can-compose-into-an-unsettled-contract.md) locates scope and precedence questions in the applicable contract. |
| One generated function, many possible behaviors | Pass: [programming practices](../../theory/programming-practices-for-prompts-need-question-specific-evidence.md) calls it a candidate implementation; [program refinement](../../theory/definitions/program-refinement.md) preserves applicable guarantees, including termination. |
| Readable code, opaque conventional code, locally understandable prompt | Pass: [representational form](../../theory/definitions/representational-form.md) separates reference adoption from question-relative inspection; [English approximation](../../theory/english-can-approximate-a-model-defined-prompt-language.md) permits local understanding without a parameter-level decomposition. |
| Successful artifact, unreliable generator | Pass: programming practices and [text testing](../../theory/automated-tests-for-text.md) retain separate obligations even for deterministic generation. The tool-mocking backlink now does too. |
| Information arriving through summaries, tools or shared state | Pass: [scoping](../../theory/llm-context-is-composed-without-scoping.md) defines a frame as one invocation's complete context. Supplied summaries and tool results are inside it; direct input exclusion does not establish causal noninterference. |
| Small interaction breaks a required invariant | Pass: [near-decomposability](../../theory/near-decomposability-may-make-local-inspection-affordable.md) distinguishes locating an intervention from preserving invariants; weak interaction is not permission to ignore correctness-relevant effects. |

## Closing repairs

- The [specialization note](../../theory/frontloading-can-specialize-instructions-around-known-inputs.md) distinguishes text insertion, candidate specialization and equivalence evidence. Its filename now matches its revised claim.
- The [verifiability note](../../theory/verifiability-gradient.md) compares concrete requirements and checks. Dependent prose no longer treats prompts, schemas, tests and code as an automatic ladder.
- The methodology and typed-callable notes distinguish packaging, activation, interface compatibility, semantic reference and requirement adequacy.
- [Retained constraints](../../theory/constraining-during-deployment-can-produce-learning-outside-weights.md) require evaluated operative use; persistence does not establish improvement or successful composition. Its filename now reflects the qualified claim.
- Tag summaries and live link labels were aligned. The tool-testing summary no longer derives generator/artifact testing from nondeterminism, and the legal-drafting comparison is scoped to English requirements.
- Three notes and the practices brief were relocated with the repository command. Published redirects preserve old library URLs. The temporary workshop receives no redirect under the workshop lifecycle contract.

## Validation and limits

Changed library artifacts and tag heads passed deterministic validation; the published redirect map passed. A tag-head size warning introduced by longer labels was resolved by shortening the navigation wording. Whitespace checks passed. The eight acceptance cases are conceptual checks, not measured model outcomes. No new source-grounding audit or whole-KB semantic certification is claimed.

The addressability/near-decomposability unification remains an explicit open candidate in the [unification ledger](../../reference/vocabulary-unification-ledger.md#addressability-and-near-decomposability). The separate invariants-under-composition workshop remains parked. Neither is needed to accept this rewrite. Near-decomposability and description-length transfers retain their conjectural status in their library homes.

The historical migration inventory and intermediate reviews remain recoverable in Git. Their settled decisions live in the program-refinement definition and [collision ledger](../../reference/vocabulary-collision-ledger.md); no unfinished migration is transferred from this workshop. External empirical passages in the scoping note and broader claims in neighboring notes were not re-audited.
