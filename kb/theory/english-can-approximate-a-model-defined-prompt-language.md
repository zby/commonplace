---
description: "English clauses supply a candidate behavioral abstraction of precise model-defined prompt semantics; local reasoning depends on its fidelity, including interactions and unexplained residual behavior."
type: types/note.md
traits: [title-as-claim, has-external-sources]
tags: [computational-model, artifact-analysis]
---

# English can approximate a model-defined prompt language

A prompt can expose meaningful parts while its precise execution semantics remains expensive to inspect. Consider a system that adopts a fixed LLM package as the reference for an operation, including inference, decoding and the relevant execution conditions. As the [semantic-reference account](./symbolic-form-holds-consumers-to-a-semantic-reference.md) explains, the package defines what the prompt permits under that path. The resulting semantics can be formal and precise, including specified variation, while its computational description is very complex.

Here ordinary English supplies a candidate coarse description of what the adopted package does. Its role is predictive: how faithfully does the description capture execution for the question at hand? This reverses the comparison used when English governs execution: there we assess the machine against the instruction; here we assess the English description against the machine-defined behavior.

English can separately govern what an interpreter ought to do. [Unsettled instruction composition](./clear-instructions-can-compose-into-an-unsettled-contract.md) concerns that requirement role. A failure of the coarse prediction does not by itself settle whether the English requirement was clear or whether execution violated it. Conversely, a faithful prediction can describe behavior the caller should reject.

In the prompt below, each clause expresses an identifiable part of the task:

> Translate the supplied text into French. Preserve personal names. Return only the translation.

The first clause selects a target language, the second governs names, and the third restricts accompanying material. This reading lets an author identify where to change the language or allow commentary. It supplies a candidate abstraction of the model-defined semantics: a compact account of selected effects, leaving most execution detail out.

Adopting the package does not establish that this abstraction faithfully describes its behavior, and does not make the package authoritative over English generally.

If the clauses' effects interact weakly enough for the question, the inspector can reason about an edit through the changed clause's coarse meaning and summaries of the other clauses. Changing French to German would then change the translation language while preserving the constraints on names and commentary.

If name handling interacts with grammatical agreement, those dependencies must enter the account. The decomposition is useful only to the extent that the omitted interactions stay within the question's tolerance.

The relevant blocks here are semantic responsibilities in the prompt, not necessarily disjoint regions of model weights. A useful coarse description need not expose the computation that realizes it. Conversely, identifying a clause's English meaning does not establish that its behavioral effects are independent. Whether this description tracks a useful decomposition of behavioral effects must be assessed empirically for the inputs and edits where it will be used. The [near-decomposability conjecture](./near-decomposability-may-make-local-inspection-affordable.md) offers a possible mechanism for affordable local inspection, not confirmation that this example has that structure.

Opacity arises for a question when the available coarse description is insufficient and establishing the required detail exceeds the inspection budget. The inspector might refine that description, obtain behavioral evidence, or inspect more of the implementation. No route requires recovering every computational detail. Thus a prompt can be understandable for changing the target language yet opaque for predicting exactly which facts a shortened translation will omit. Whether either judgment holds for a particular model requires evidence.

An empirical test would fix the package and input set, vary the three clauses separately and together, and compare predicted changes with changes in target language, name handling and commentary. The coarse account must specify those predictions and tolerated interactions before observing the results. It also needs sufficiently definite assessment criteria: if reviewers disagree about whether transliteration preserves a personal name, an observed transliteration alone does not establish a prediction failure. Settle that criterion or report the assessment under the competing readings. Failures would delimit its useful scope. This note reports no such trial; the example explains how localized prompt semantics can coexist with a complex reference, rather than confirming that a model follows this decomposition.

## Fidelity and the residual

In the proposed transfer of [Grünwald's two-part description length](../sources/grunwald-mdl-tutorial.ingest.md), the coarse English account is the hypothesis H, and recorded behavior on a specified input set supplies the data D. The residual L(D|H) is the information needed to describe that behavior given the account, including outcomes and interactions it leaves unexplained. Grünwald defines it as, verbatim, "the length, in bits, of the description of the data when encoded with the help of the hypothesis." This mapping is the note's proposal; the source does not analyze prompt semantics.

The clause-variation test probes that residual by comparing predicted and observed output properties. A prediction mismatch is evidence about the abstraction's fidelity; it is not yet a description length. Computing a two-part score also requires a fixed encoding of the account and observations, including the treatment of permitted variation. A more elaborate account may reduce the residual while increasing its own description cost. Neither score alone measures the effort of discovering or checking the account.

## Scope

English is a candidate approximation for the named package and questions, not a universally faithful or uniquely usable description.

---

Relevant Notes:

- [Symbolic form holds consumers to a semantic reference](./symbolic-form-holds-consumers-to-a-semantic-reference.md) — grounds: adoption fixes model-defined semantics without establishing their adequacy to English requirements
- [Clear instructions can compose into an unsettled contract](./clear-instructions-can-compose-into-an-unsettled-contract.md) — contrasts: English as a governing requirement can itself leave instruction interactions unsettled
- [Near-decomposability may make local inspection affordable](./near-decomposability-may-make-local-inspection-affordable.md) — mechanism: proposes when manageable interactions could support local reasoning through an abstraction
