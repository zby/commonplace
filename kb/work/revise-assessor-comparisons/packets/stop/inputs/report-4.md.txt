---
type: types/review-result.md
format: 2
description: Retained report review of kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
  against kb/instructions/compression-bundle/high-impact-simplification-synthesis.md
note: kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
note-sha256: 2214be116a950b1be4016de0633a69bd6e3df247b8c6750c25d37d0ef7013038
criterion: kb/instructions/compression-bundle/high-impact-simplification-synthesis.md
criterion-sha256: 0639a8d235bbdf791feaa2f1eae21d28a4131c0fe56e0a15fefe51fa524835cf
outcome: report
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/synthesis
launch: 26beef09873b4dbcac0f162f7ada70ff
completed-at: '2026-11-22T21:59:04Z'
findings:
- scope: passage
  quotes:
  - 'Continual learning, as the field uses the term and as this note uses it, asks
    for more: the system does the selecting itself.'
  reason: The opening sentence, title and description say continual learning requires
    governing behaviour-changing writes, but the note itself says mature release engineering
    already governs such writes. The condition that separates continual learning from
    governed software change, that the system's own loop does the selecting, first
    appears near the end of the last paragraph, so on first read the claim looks weaker
    and less distinctive than the note's actual commitment; a revision could state
    the self-selection condition in the opening sentence (and the description) and
    let the last paragraph elaborate it rather than introduce it.
- scope: document
  quotes: []
  reason: The final paragraph carries the governance definition, a form-placement
    aside, the human-selection contrast stated twice (release engineering, then the
    incident edit), the proposal-selection criterion, a cadence sentence and the subproblem
    scoping, so the reader loses the discriminator among asides; a revision could
    move the codification-and-relaxing aside into the representational-form paragraph
    and merge the two human-selection statements into one sentence beside the proposal-selection
    criterion, leaving the paragraph as definition, discriminator, scope.
- scope: passage
  quotes:
  - Persistence alone therefore does not create a governed behaviour-changing write.
  reason: The opening paragraph states the claim, then runs through the learning criterion,
    behavioral authority, knowledge artifact and system-definition artifact before
    restating its first sentence as a conclusion, so it reads as terminology and the
    load-bearing premise (authority belongs to a consumption path, not stored bytes)
    is not foregrounded; a revision could fold the artifact-role pair into one clause
    with its links kept, end on the consumption-path premise, and drop the closing
    restatement.
contract: report
target-sha256: 2214be116a950b1be4016de0633a69bd6e3df247b8c6750c25d37d0ef7013038
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/synthesis/calls/launches/26beef09873b4dbcac0f162f7ada70ff/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/synthesis/artifact/reviews/5db2fde015f82410fe814352/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/synthesis/calls/launches/26beef09873b4dbcac0f162f7ada70ff/outputs/review.md
raw-output-sha256: a7ce3ef93810477ae8f0e289d7a12e18155042de155983c4877f7a4a217ddeb1
---

# Simplification synthesis: continual learning requires governing writes

The note is short and its four paragraphs each serve the claim. The gate findings are mostly local, but three of them meet at one structural issue: the distinctive commitment (self-selection) sits at the end, inside the paragraph that collects the most asides. The opportunities below address that issue first, then the final paragraph's order, then the opening's density. The local defensive clauses in the form paragraph ("broadening the system boundary does not remove them", "It need not touch all three every time") are minor compression and are left to the individual findings.

## Opportunities

### 1. Put the self-selection condition in the opening claim

- Location: first paragraph, "Continual learning in a deployed system requires more than retaining new content. It requires governing durable changes to future behaviour"; final paragraph, "Continual learning, as the field uses the term and as this note uses it, asks for more: the system does the selecting itself."
- Combines: core-claim-obscured (self-selection clause, form-placement aside); detail-overhang (doubled boundary caveat) as context.
- Preserve or decide: The note uses "govern" for both human release engineering ("Mature release engineering already governs hand-authored readable changes") and the autonomous case ("autonomously *choosing* a behaviour-changing write"). The author must decide whether "governing" in the title and description already includes autonomous selection, or whether the claim needs an explicit qualifier such as "the system's own loop". That is a term choice with consequences for the title, so it is not a compression edit. One possible resolution, for illustration only: "It requires the system's own loop to govern durable changes to future behaviour: selecting a candidate update, validating it, and deciding how it enters the behaviour-determining system." Preserve the note's position that hand-authored changes are still learning; only continual learning needs self-selection.

### 2. Reorder the final paragraph around one discriminator

- Location: final paragraph, from "Form placement is itself revisable." through "Continual-learning systems must close that evidence-responsive loop at the cadence their environment requires."
- Combines: branch-bloat (form-placement branch); core-claim-obscured (form-placement aside); detail-overhang (doubled boundary caveat, codification aside); marginal-value-redundancy (incident-edit repetition, cadence sentence).
- Preserve or decide: Merging the two human-selection statements must keep both halves: hand-authored changes are learning by people's selection ("the system learned"), and they are maintenance, not continual learning. The two current sentences carry different supports (release engineering as the general practice; the incident edit as a concrete case), so the author chooses which carries the merged sentence. The codification-and-relaxing aside adds a dynamic the rest of the note does not state (per marginal-value-redundancy), so moving it into the form paragraph is preferable to deleting it. The author must also decide whether the cadence sentence restates the second paragraph's install-before-retraining constraint or turns the discriminator into an operational requirement; the gate findings leave that open. Keep the closing scope sentence ("governance relates them rather than replacing them"), which the gates judged to be scoping, not recap.

### 3. Make the opening paragraph lead with its premise, not its terminology

- Location: first paragraph, from "This note uses the broad criterion" through "Persistence alone therefore does not create a governed behaviour-changing write."
- Combines: core-claim-obscured (definition run); marginal-value-redundancy (closing restatement).
- Preserve or decide: The branch-bloat review identifies the knowledge-artifact / system-definition-artifact / behavioral-authority sequence as the premise that storing something does not decide whether it changes behaviour, so the compression must keep the consumption-path claim and its links, not just shorten the list. The learning-criterion sentence grounds why non-weight changes count as learning and should survive in some form. Whether the paragraph ends on the consumption-path premise or on the artifact-role distinction is an author's choice; either removes the restatement of the opening sentence.
