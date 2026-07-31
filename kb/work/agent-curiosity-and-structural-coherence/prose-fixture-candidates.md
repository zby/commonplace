# Prose fixture candidates

## Status and admission rule

These are frozen seeds for constructing the first experiment, not scored benchmark items and not proof of a general failure. Each comes from a preserved baseline and a later reference revision or review trace. Before admission, independent raters must see two views:

1. a local window without headings, where the target must remain fluent and topically connected; and
2. the whole note plus a thesis and section-purpose map, where raters must agree that the target duplicates, competes with, or belongs outside its present role.

Reject a candidate if the local panel finds it plainly incoherent, the global panel cannot agree on a structural problem and defensible operation, or the reference edit merely expresses one editor's taste without a stated document consequence.

## Candidate 1: a conclusion embedded in a duplicate preview bridge

**Frozen source:** [session-history baseline](../review-revise-gated/baseline.md), paragraph at lines 17–18.

**Target unit:**

> That is useful for interactive UX, but it is the wrong default for most agent orchestration.

**Immediate context:** the preceding sentences explain that higher-level chat and tool-loop interfaces make session history the easiest state carrier. The next heading, “Where the problem actually appears,” then enumerates those same interfaces.

**Why it is superficially connected:** the sentence is a direct evaluation of the chat-interface mechanism just described. It is grammatical, true to the note's position, and provides a normal concluding cadence for the paragraph.

**Candidate global-role conflict:** the whole paragraph previews the next section rather than advancing the introduction. This final sentence also states the note's practical conclusion before the mechanism and trade-off have been developed. The [reference target](../review-revise-gated/target.md) deletes the introductory bridge and restates the interactive-session/orchestration contrast at the end of the note, where it functions as a conclusion.

**Preserved agent trace:** the [run-08 prose gate](../review-revise-gated/run-08/prose-review.md) detected the duplicate bridge, but the [reviser](../review-revise-gated/run-08/scores.md#new-gate-results) removed this concluding sentence and left the actual preview in place. This makes the fixture useful for separating anomaly detection from selecting the right unit and operation.

**Unresolved before admission:** validate whether the sentence itself is misplaced or whether only the surrounding preview is redundant. A sentence-rehome condition should preserve the proposition near the conclusion rather than reward exact text deletion.

## Candidate 2: locally relevant support that becomes a second thesis

**Frozen source:** [writing-filter baseline](../agent-note-improvement/case-03-adversarial-loop-writing-filter/baseline-working-tree.md), paragraph beginning “And the connection work is the part Borretti never reaches.”

**Target passage:**

> He writes about composing single pieces; he says nothing about curation across a corpus — finding where an idea connects, contradicts, or extends across hundreds of notes. That labor has no solo equivalent to be contemptible about: it is not thinking outsourced but one mind's reach over its own accumulated knowledge, extended past what a single pass can hold.

**Immediate context:** the preceding paragraph concedes that the human judge remains bounded by their own knowledge but says the agent can take rendering and connection work off their hands. The following conclusion argues that an adversarial loop can reconstruct the writing-as-thinking filter.

**Why it is superficially connected:** corpus connection is one activity delegated inside the human-agent loop, so the passage follows semantically from the division of labor and offers an appealing additional benefit.

**Candidate global-role conflict:** the note's thesis concerns whether adversarial review can reconstruct the filter lost by delegating composition. The passage starts a different defense of corpus-scale agent work and risks becoming the reader's remembered thesis. The [reference revision](../agent-note-improvement/case-03-adversarial-loop-writing-filter/revised-from-compression-bundle.md) removes the standalone paragraph and preserves its proposition as one subordinate sentence: corpus connection is a secondary payoff, not a separate proof.

**Preserved agent trace:** the [compression review](../agent-note-improvement/case-03-adversarial-loop-writing-filter/compression-bundle-review.md) explicitly diagnosed a second thesis and proposed remove or rehome. Earlier generic and pruning critiques are catalogued in the [case README](../agent-note-improvement/case-03-adversarial-loop-writing-filter/README.md).

**Unresolved before admission:** obtain independent agreement on the note's thesis and whether the passage should be deleted, folded, or split into another note. The experiment should reward correct role demotion, not exact recovery of one human edit.

## Candidate 3: a true boundary that may not earn a standalone section

**Frozen source:** [prose-dereference baseline](../agent-note-improvement/case-02-prose-dereference/baseline-working-tree.md), `Scope` section.

**Target unit:**

> The reliability of single-source scales with **representational form**. At the codified end — a schema field, a type, a function signature — a declaration dereferences and one statement suffices. At the prose end it does not, and reinforcement is needed. Between them the requirement is graded: the more formal the artifact, and the more local and obvious the application, the fewer restatements; the more prose-like, distant, and non-obvious, the more.

**Why it is superficially connected:** the section states a real boundary of the note's claim and uses the same code/prose contrast as the mechanism.

**Candidate global-role conflict:** ordinary semantic gates defended the qualifier because it protects the claim's truth. A later marginal-value review argued that the section mostly restates a gradient already established and should not remain a standalone unit; one useful phrase could be folded into the mechanism. The [case record](../agent-note-improvement/case-02-prose-dereference/README.md#2026-06-16-strengthened-marginal-value-redundancy-gate) preserves that disagreement.

**Why this is initially a boundary case, not a positive:** there is no settled accepted deletion, and a section can legitimately make an implicit boundary explicit for readers. If global raters disagree, exclude it from the main benchmark and retain it as a judgment-calibration case. It tests whether a purported high-altitude judge merely equates repetition with misplacement.

## Easy operation control: an empty elevation sentence

The session-history baseline also contains:

> This is not just summarization — it is interface design.

The next sentence already states the substantive interface claim, and the [reference target](../review-revise-gated/target.md) deletes the elevation sentence. The stock-phrase gate found it reliably across runs. This is not the hard target: it is a locally connected but low-value sentence whose deletion should be easy once review is requested. Use it to distinguish inability to delete at all from failure on topically useful, globally misplaced material.

## First experiment packet to build

For each admitted hard fixture, create a minimally perturbed note and freeze:

- thesis, section-purpose map, and argument dependencies before any agent sees the case;
- local-window and global-view human ratings;
- open online-edit condition, open retrospective-review condition, role-conflict cue, supplied role map, named rehome operation, frozen-candidate ranking, and exact-edit ceiling;
- a genuine bridge-repair control where adding a transition supplies a missing inference and is the correct operation; and
- outcome scoring for target detection, operation, destination, claim preservation, local fluency, and whole-document role fit.

The current candidate set is too small and too entangled with retrospective review to establish prevalence. Its immediate purpose is to make the user's observation inspectable enough to test.
