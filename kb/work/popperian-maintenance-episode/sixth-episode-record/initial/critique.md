<!-- copied from the gitignored kb/reports tree; original frontmatter retained below as data -->

```yaml
review_job_id: 8384
review_pair_id: 20918
note_path: kb/notes/unformalized-improvements-need-a-pre-formal-stage-in-the-loop.md
criterion_path: kb/instructions/critique-note.md
model_partition: codex
runner: /root/initial_critique
runner_model: gpt-5.4
runner_effort: xhigh
result_kind: report
outcome: null
completed_at: '2026-08-26T15:53:12+00:00'
```
# Critique: Reaching unformalized improvements needs a pre-formal stage somewhere in the loop

**Note:** kb/notes/unformalized-improvements-need-a-pre-formal-stage-in-the-loop.md
**Central commitment:** A self-improvement loop cannot reach candidates whose concepts are still unsettled unless some stage, somewhere before binding formalization, can criticize and revise them outside the formal gate.
**Critique mode:** claim
**Attack outcome:** partially lands

## Strongest case against it
A strong formal-methods objection is that the note turns a limitation of one class of systems into a universal architectural necessity. Its key move is from "this Gödel-style proof gate only admits fully formalized candidates" to "there must therefore be a pre-formal stage somewhere in any loop that reaches unsettled improvements." But that only follows if "formal representation" means a fully specified, commitment-bearing surrogate. An informed opponent can deny that premise. A loop can search over partial specifications, sketches, latent-variable models, surrogate objectives, empirical patches, or mixed symbolic/learned representations that deliberately leave concepts unsettled while still making them machine-operable enough for comparison and revision. On that view, the necessary ingredient is not a distinct pre-formal criticism stage but a rich enough candidate language plus evaluation machinery that can work on incomplete representations.

The note's scope restriction makes the problem sharper, but also exposes the weakness. It says the claim concerns "externally interpreted theories about a system or its domain, read by a person or a language model." Under that description, an interpretive stage is already built in by definition: if the candidate is a human- or LLM-read theory, of course some interpretive criticism must happen somewhere. That makes the necessity claim close to analytic for that artifact class, while the larger architectural thesis remains unearned. The note therefore risks equivocating between a narrow claim that is true by stipulation for externally interpreted theories and a broader claim that real improvement loops cannot absorb concept revision into richer formal or mixed representations.

## How the note engages it
Partially engaged. The note does real work against a weaker version of the objection: it distinguishes warrant limits from admission limits, argues that upstream translation relocates rather than removes criticism, and concedes that settled concepts can move directly into a formal gate when translation becomes cheap. Those sections answer "a formal gate can still benefit from upstream prose work."

What it does not squarely answer is the stronger version above: why partial or mixed formalizations do not already count as admission of the candidate, and why concept revision inside such representations is not enough to dissolve the claimed necessity of a separate pre-formal stage. The note repeatedly asserts that an unsettled concept "must be stated, criticized, and bounded before a new model is built," but it does not defend that "before" against systems that refine the concept through iterative modeling, testing, and relaxation inside the candidate space itself. Its evidence also shows that formal validity and world-fit can come apart; it does not show that the only repair path is an upstream natural-language stage.

## Constructive findings
- Define `formal representation` tightly enough to exclude sketches, mixed representations, and empirical surrogate models, or else relax the necessity claim.
- Separate the narrow stipulative claim about externally interpreted natural-language theories from the broader architectural claim about self-improvement loops in general.
- Either defend why concept revision cannot be carried by richer formal candidate spaces, or weaken "that it exists is not" to a comparison claim about specific architectures such as Gödel-style proof gates and Commonplace-like human/LLM theory work.

## Secondary objections (optional)
- The Commonplace pathway and the Eigenius/DiscoverPhysics contrasts show a translation boundary, but they do not by themselves establish a distinct stage as opposed to an iterative modeling-and-validation process.
- The "relaxed Gödel machine" label may suggest a principled family relation stronger than the evidence supplied; the note mainly shows an analogy plus one added stage.

## Result: REPORT
