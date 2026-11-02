# Interpretation statuses, ambiguity contract and assessment design

Received 2026-11-02 to support a functional definition and a discriminating assessment of the interpreter. These are candidate distinctions and tests, not an adopted interpreter or a completed probe suite. The [workshop's evaluation boundary](./README.md#evaluation-boundary) remains binding: nothing in the library may depend on this device before adoption.

Provenance: adapted from Astra's answer of 2026-11-01, Codex session `01a19887-df49-7d73-8d3f-618e06886ec4`, retained in Git commit `c2da14dc120aef3d79309fa91e1a8513540adcc7`. This file carries the material needed for continuation without a live dependency on the originating workshop. It records a proposal and its reasoning, not independent empirical evidence of interpreter competence.

## What the definition must fix

Declare the linguistic community or variety, historical stage or update rule, admitted discourse, accessible context, semantic distinctions to preserve, and input/resource assumptions. A candidate interpreter preserves the commitments, alternatives and unresolved parameters warranted by that scoped practice. It must neither introduce unsupported commitments nor omit supported ones. This identifies an adequacy target; it does not supply the correctness relation that the [current sketch](./resource-bounded-ideal-interpreter.md) still lacks.

A useful interface exposes content or constraints, alternative readings and their conditions, unresolved references, discourse force, presuppositions and defeasible inferences, proposed discourse update, and interpretation status. The distinctions must be recoverable and testable even if not separate fields. Understanding an assertion need not decide its truth; understanding an instruction need not execute it.

For instructions, expose an acceptance condition, possibly over execution traces. “Return any integer greater than 10” permits both 11 and 12. An interpreter always returning 11 has not thereby shown that it distinguishes that condition from “greater than 0.” Appropriate replies alone can underdetermine interpretation.

## Six statuses

These statuses can coexist. Do not collapse them into one unresolved result.

| Status | What remains unsettled |
|---|---|
| Linguistic ambiguity | Which supported interpretation is intended |
| Missing context | A needed referent, parameter, or contextual fact |
| Semantic indeterminacy | The practice itself leaves a boundary or application unsettled |
| Interpreter limitation | The system cannot reliably interpret the input |
| Reasoning limitation | The content is represented, but a requested consequence is unresolved |
| Execution failure | The understood operation cannot be completed |

Investigator uncertainty about a practice is not automatically indeterminacy within the language. A missing pronoun referent is not necessarily ambiguous grammar. An impossible operation can be understood correctly.

## Candidate ambiguity contract

The purpose is to preserve unresolved commitments without treating ambiguity as permission or ordinary discretion as missing meaning. The contract belongs to the interpreter together with its controller.

For live readings with acceptance conditions `A1 ... Ak`:

- Several actions satisfying one condition are permitted freedom.
- Uncertainty about which condition governs is unresolved interpretation.
- An authorized policy may select among readings.
- If the execution contract permits it, an action satisfying every live reading may proceed without resolving the distinction. A meaning-reporting task must still retain it.
- Without authorization, satisfying some live reading does not generally license action.

An ambiguity result should carry the unresolved interpretive dimension, live alternatives or constraints, why the distinction matters to the requested operation, established commitments, and the clarification needed or authorized policies available. The handler narrows alternatives while preserving unaffected commitments. Clarifying “next Friday” must not silently change duration or participants. If the reply changes them, record an amendment. A clarification can remain incomplete or introduce another open issue.

### Limit on exact relevance detection

Do not promise to ask exactly when necessary for arbitrary expressive acceptance conditions. The probe distinguishes interpreting two conditions from deciding whether they ever differ. For example, compare an always-false condition on integers with a condition that accepts `n` exactly when a fixed computation terminates within `n` steps. Both conditions can be evaluated for any finite `n`; deciding whether they differ for any `n` would decide whether that computation ever terminates. The proposed relevance check therefore needs a restricted condition language, conservative reasoning, or an explicit inability-to-establish-relevance result. This reduction is a design limit, not evidence that natural language lacks formal semantics.

Missed consequential ambiguity and unnecessary clarification are separate failures. Always asking fails progress and precision; never asking can discard warranted alternatives.

## Assessment design

The intended result is a diagnostic assessment that separates interpretation defects from reasoning, knowledge and execution defects. It can inform the definition without claiming unrestricted perfection. Use small simulated worlds with explicit entities, relations, action rules and dialogue histories so factual access and much of the reasoning are independently controllable.

Four linked conditions:

1. **Interpretation:** provide relevant facts; request structured content, alternatives and open parameters in simple domains.
2. **Reasoning:** supply the correct formal interpretation directly; ask for consequences without the English translation step.
3. **Knowledge:** hold the sentence fixed while supplying or withholding a relevant fact; interpretation should remain stable while the factual answer changes appropriately.
4. **Compliance and execution:** supply the interpreted instruction; test action selection and execution separately.

The separation is diagnostic, not a claim of complete modularity: pragmatic interpretation can use knowledge and reasoning.

Candidate contrasts include:

| Case | Distinction to test |
|---|---|
| “Greater than 10” versus “greater than 0,” both answered with 11 | A permitted response versus recovery of the acceptance boundary |
| “The dog chased the cat” versus the reversed roles | Familiar vocabulary versus relational structure |
| “Not every lamp is on” versus “Every lamp is off” | Partial negation versus universal negation |
| “Every student read a book,” with context licensing two readings | Retaining all supported readings versus one plausible reading |
| “Mira told Lena that she had won,” without disambiguating context | Available grammar versus unavailable reference |
| “The sealed box contains a red ball” | Interpreting a claim versus knowing whether it is true |
| Correctly representing “Output exactly BLUE” but producing RED | Interpretation versus compliance |
| Asking which integer after “Return any integer greater than 10” | Missing choice versus granted discretion |

For clarification, pair genuine missing choices with granted discretion, irrelevant ambiguities, missing factual information and impossible execution. Check unrelated commitments after clarification. Include novel combinations, renamed entities, meaning-preserving paraphrases, misleading framing and genuinely relevant context changes. Do not assume a theoretically conceivable reading is live without contextual support.

Report omitted readings, invented readings, incorrect commitments, missed consequential ambiguities, unnecessary requests and lost commitments separately. Keep disputed judgments separate from clear failures. Record completion, partial results, abstention, missing outputs and cost alongside fidelity; a selective success rate does not assess the full workload. For stochastic implementations, distinguish correctness for every permitted outcome from probability-one correctness and from a small tolerated error rate.

Finite tests can challenge a universal claim; passing this proposed suite would not establish unrestricted perfection. No tests have been run here.

## Continuation and open dependencies

The receiving workshop may revise or reject these candidates under its existing commission. First preserve the statuses and diagnostic separation when building its functional definition. If only a partial specification is possible, record which correctness or relevance judgments remain unavailable and what that prevents the assessment from attributing. No downstream library adoption follows from receiving this material.

Still needed: independently warranted expected interpretations, a declared first assessment class and resource model, a treatment of disputed readings, and a worked suite with expected results. This handoff supplies neither a complete theory of English nor an independent semantic oracle.
