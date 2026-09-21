# Failure modes of a chat-tuned model in unattended processing

Posed by the operator on 2026-09-21, from conclusions of an outside chat session pasted into the commissioning conversation. The catalogue entries and the repair-ordering refinement below come from that paste; the placement against existing KB material is this workshop's first pass.

## Goal

Commonplace wants unattended processing: review, fixing, revision, and maintenance that run without a human reading each step. The models that do this work are post-trained for human-mediated interaction. That post-training cannot be removed, because instruction following and tool calling come from the same training.

The workshop therefore treats the mismatch as an engineering problem with three outputs:

1. **A catalogue of observable failure modes** — behaviors a model shows in Commonplace processing that harm the result when no human is reading along.
2. **A system-level countermeasure for each entry** — a change to unit size, workflow shape, output format, or checking, in preference to a prompt that asks the model to behave differently.
3. **A regression check for each entry** — a fixture and a measurable signal, so a countermeasure can be shown to work and a model or harness change can be shown not to have undone it.

## The causal hypothesis is a working frame, held tentative

The framing hypothesis is that human-oriented optimization causes or amplifies these behaviors. The catalogue does not depend on it. An entry is a behavior, a harm, and a countermeasure; each stays useful if the cause turns out to be pretraining, annotation protocol, decoding, or harness design.

The KB has a recorded stance on this attribution and the workshop inherits it. The retained report on [provider treatment of operator-communication failures](../../reports/retained/provider-treatment-of-operator-communication-failures-2026-08-29.md) cites evidence that preference models are miscalibrated across length, structure, jargon, sycophancy, and vagueness, reads it as "evidence for a general selection pressure", and declines to attribute any specific behavior to reward-model bias. A sycophancy mechanism was also removed from the note now titled [generation confidence does not by itself certify soundness](../../notes/generation-confidence-does-not-by-itself-certify-soundness.md) as unsupported. So each entry records candidate explanations as candidates, and no promoted note may assert a training cause on the strength of this catalogue alone.

One candidate explanation is general enough to state here. **Evaluation-horizon bias:** human preference judgments are made over short episodes, so optimization against them can favor output that reads well within one episode over properties that only show across a whole artifact or across time. This is an explanation, not an observable behavior, so it is not a catalogue entry. It matters for two reasons. It predicts which behaviors to look for: the ones whose cost falls outside the episode that produced them. And it suggests a reading of the short-note discipline: a small unit makes a local evaluation a better approximation of the properties we care about. That reading would extend [a note is an atomic step relative to the check that reads it](../../notes/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md), which already sizes a note to one checker pass, and it may be an instance of [weakly discriminated qualities tend to be underselected](../../notes/weakly-discriminated-qualities-tend-to-be-underselected.md) with the episode length as the discrimination limit. Neither connection has been argued yet.

## Admission rule

The catalogue is a working list grown by observation, on the model of the [change-operations catalogue](../change-operations-catalogue/README.md). This follows the KB's norm to [build contracts from real failures, not from a taxonomy of possible checks](../../notes/automated-tests-for-text.md).

- An entry is **admitted** when a recorded instance shows the behavior in Commonplace processing: a commit, a fix report, a review result, a log entry, or a dated operator observation.
- A behavior known from outside reports or from general experience, with no recorded local instance, is a **candidate**. Candidates are listed so a session that meets one can record the instance; they carry no countermeasure work until admitted.
- A behavior is stated in observable terms. "The model loses focus" is not admissible; "the edit leaves N of M flagged inconsistencies in place" is. This follows the method in [human writing structures transfer to LLMs because failure modes overlap](../../notes/human-writing-structures-transfer-to-llms-because-failure-modes.md): name the failure and show the agent exhibits it; do not argue from analogy.
- The list carries no completeness claim. A missing behavior is not evidence of its absence.

## Boundary with neighbouring workshops

- [error-catching](../error-catching/README.md) owns the detection techniques: their grid, economics, and gaps. This workshop consumes that grid when choosing a countermeasure and does not rebuild it. Its gate statistics are evidence for a candidate here (mechanical defects are caught more often than judgment defects), which that workshop reads as detector economics.
- [agent-curiosity-and-structural-coherence](../agent-curiosity-and-structural-coherence/README.md) owns the mechanism question for one behavior: locally acceptable, globally misplaced material, and whether the agent originates the structural concern. This catalogue may list that behavior with a pointer; it does not run rival-mechanism experiments on it. That workshop names training origin and longitudinal erosion as its own follow-ons.
- [writing-as-thinking-process-transfer](../writing-as-thinking-process-transfer/README.md) holds the open item "fix-routing-by-scope in FIX-SYSTEM". The first catalogue entry bears on it directly; a change to the fix system is coordinated there or taken over explicitly, not made twice.
- [reflective-improvement-divergence](../reflective-improvement-divergence/README.md) owns revision drift and oscillation across repeated passes.

## Evaluation boundary

- A countermeasure is accepted on a measured difference on a fixture, at a fixed model partition, with repeated trials. One good run is a lead.
- A regression check for a judging step reuses the design in [calibrating semantic gates against labelled fixtures](../../reference/proposals/calibrating-semantic-gates-against-labelled-fixtures.md) unless the entry states why that design does not fit.
- Gains from imposed structure are tested, not assumed; see [process structure and output structure are independent levers](../../notes/process-structure-and-output-structure-are-independent-levers.md).
- Countermeasures already theorized in the library are cited, not re-derived: proposer and critic separation in [the adversarial loop note](../../notes/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md), decorrelation limits in [error correction works above chance oracles with decorrelated checks](../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md), and unresolved-state preservation in [mixed epistemic status must be preserved below the document level](../../notes/mixed-epistemic-status-must-be-preserved-below-the-document-level.md).

## Files

- [catalogue.md](./catalogue.md) — admitted entries, then candidates awaiting a recorded instance.

## What closes this workshop

The workshop closes when at least three admitted entries each have a shipped countermeasure and a regression check that has been run at least once, and the catalogue has either been promoted to a library artifact with a stated maintenance rule (how an entry is admitted, how it is retired when a model change removes the behavior) or judged not worth keeping as a standing artifact, with the reason written down. The evaluation-horizon hypothesis is promoted to a note, folded into an existing note, or dropped, independently of the catalogue's fate.
